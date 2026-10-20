from __future__ import annotations

import argparse
import os
import re
import shutil
import tempfile
import unicodedata
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from render_compact_note import build_pdf


DEFAULT_STORAGE_ROOT = (
    Path.home()
    / "Library"
    / "Mobile Documents"
    / "com~apple~CloudDocs"
    / "Study Assistant"
)


@dataclass(frozen=True)
class SyncPaths:
    storage_root: Path
    topic_root: Path
    active_pdf: Path
    active_md: Path
    legacy_pdf_dir: Path
    archive_pdf_dir: Path
    archive_md_dir: Path


@dataclass(frozen=True)
class ArchivePair:
    active_pdf: Path | None
    active_md: Path | None
    version: int


@dataclass(frozen=True)
class LegacyGroup:
    stem: str
    pdf: Path | None
    md: Path | None


def safe_part(value: str, label: str) -> str:
    if not value.strip():
        raise ValueError(f"{label} must not be empty")
    if "/" in value or "\0" in value:
        raise ValueError(f"{label} must not contain path separators")
    return unicodedata.normalize("NFC", value.strip())


def normalized_name(value: str) -> str:
    """Compare Unicode spellings without renaming any existing file."""
    return unicodedata.normalize("NFC", value)


def same_file(left: Path, right: Path) -> bool:
    """Path spelling can differ on macOS even when both paths name one file."""
    try:
        return left.samefile(right)
    except FileNotFoundError:
        return False


def parse_date(value: str | None) -> str:
    if value is None:
        return datetime.now().strftime("%y%m%d")
    if not re.fullmatch(r"\d{6}", value):
        raise ValueError("--date must use YYMMDD format, for example 260706")
    return value


def default_storage_root() -> Path:
    env_path = os.environ.get("STUDY_ASSISTANT_STORAGE_PATH")
    if env_path:
        return Path(env_path).expanduser()
    return DEFAULT_STORAGE_ROOT


def build_paths(storage_root: Path, system: str, topic: str) -> SyncPaths:
    topic_root = storage_root / "Notes" / system / topic
    return SyncPaths(
        storage_root=storage_root,
        topic_root=topic_root,
        active_pdf=storage_root / "PDFs" / system / f"{topic}.pdf",
        active_md=topic_root / "md" / f"{topic}.md",
        legacy_pdf_dir=topic_root / "pdf",
        archive_pdf_dir=topic_root / "_archive" / "pdf",
        archive_md_dir=topic_root / "_archive" / "md",
    )


def existing_versions(paths: SyncPaths, topic: str, date_text: str) -> list[int]:
    versions: list[int] = []
    pattern = re.compile(rf"^{re.escape(normalized_name(topic))}_{date_text}_ver\.(\d+)\.(?:pdf|md)$")
    for archive_dir in (paths.archive_pdf_dir, paths.archive_md_dir):
        if not archive_dir.exists():
            continue
        for path in archive_dir.iterdir():
            match = pattern.match(normalized_name(path.name))
            if match:
                versions.append(int(match.group(1)))
    return versions


def next_version(paths: SyncPaths, topic: str, date_text: str) -> int:
    versions = existing_versions(paths, topic, date_text)
    return max(versions, default=0) + 1


def archive_name(topic: str, date_text: str, version: int, suffix: str) -> str:
    return f"{topic}_{date_text}_ver.{version}{suffix}"


def archive_paths_available(paths: SyncPaths, topic: str, date_text: str, version: int) -> bool:
    return not (
        (paths.archive_pdf_dir / archive_name(topic, date_text, version, ".pdf")).exists()
        or (paths.archive_md_dir / archive_name(topic, date_text, version, ".md")).exists()
    )


def reserve_archive_version(paths: SyncPaths, topic: str, date_text: str, version: int) -> int:
    while not archive_paths_available(paths, topic, date_text, version):
        version += 1
    return version


def active_pdf_variants(paths: SyncPaths, topic: str) -> list[Path]:
    # glob with a Korean prefix may miss decomposed filenames on macOS.
    return sorted(
        path
        for path in paths.active_pdf.parent.glob("*.pdf")
        if normalized_name(path.name).startswith(normalized_name(topic))
        and not same_file(path, paths.active_pdf)
    )


def legacy_pdf_candidates(paths: SyncPaths, topic: str) -> list[Path]:
    candidates: list[Path] = []
    if paths.legacy_pdf_dir.exists():
        candidates.extend(sorted(paths.legacy_pdf_dir.glob("*.pdf")))
    if paths.active_pdf.parent.exists():
        candidates.extend(active_pdf_variants(paths, topic))
    return dedupe_paths(candidates)


def legacy_md_candidates(paths: SyncPaths, topic: str) -> list[Path]:
    md_dir = paths.active_md.parent
    if not md_dir.exists():
        return []
    return dedupe_paths(sorted(
        path for path in md_dir.glob("*.md") if not same_file(path, paths.active_md)
    ))


def legacy_groups(paths: SyncPaths, topic: str) -> list[LegacyGroup]:
    by_stem: dict[str, dict[str, Path]] = {}
    for kind, candidates in (
        ("pdf", legacy_pdf_candidates(paths, topic)),
        ("md", legacy_md_candidates(paths, topic)),
    ):
        for path in candidates:
            group = by_stem.setdefault(normalized_name(path.stem), {})
            previous = group.get(kind)
            if previous is not None and not same_file(previous, path):
                raise ValueError(f"Distinct files share a normalized name: {previous}, {path}")
            group[kind] = path
    return [
        LegacyGroup(stem=stem, pdf=items.get("pdf"), md=items.get("md"))
        for stem, items in sorted(by_stem.items())
    ]


def dedupe_paths(paths: list[Path]) -> list[Path]:
    seen: set[tuple[int, int]] = set()
    result: list[Path] = []
    for path in paths:
        stat = path.stat()
        identity = (stat.st_dev, stat.st_ino)
        if identity not in seen:
            result.append(path)
            seen.add(identity)
    return result


def planned_archive_pair(paths: SyncPaths, date_text: str, topic: str) -> ArchivePair | None:
    active_pdf = paths.active_pdf if paths.active_pdf.exists() else None
    active_md = paths.active_md if paths.active_md.exists() else None
    if not active_pdf and not active_md:
        return None
    return ArchivePair(active_pdf=active_pdf, active_md=active_md, version=next_version(paths, topic, date_text))


def archive_file(src: Path, dest: Path, dry_run: bool) -> None:
    print(f"archive: {src} -> {dest}")
    if dry_run:
        return
    if dest.exists():
        raise FileExistsError(f"Refusing to replace an existing archive: {dest}")
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(src), str(dest))


def copy_file(src: Path, dest: Path, dry_run: bool) -> None:
    print(f"copy: {src} -> {dest}")
    if dry_run:
        return
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dest)


def update_storage_metadata(markdown_text: str, system: str, topic: str) -> str:
    lines = markdown_text.splitlines()
    if not lines or lines[0].strip() != "---":
        return markdown_text

    end = None
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            end = index
            break
    if end is None:
        return markdown_text

    replacements = {
        "storage_pdf": f"Study Assistant/PDFs/{system}/{topic}.pdf",
        "storage_md": f"Study Assistant/Notes/{system}/{topic}/md/{topic}.md",
    }
    seen: set[str] = set()
    for index in range(1, end):
        key = lines[index].split(":", 1)[0].strip()
        if key in replacements:
            lines[index] = f"{key}: {replacements[key]}"
            seen.add(key)

    insert_at = end
    for key, value in replacements.items():
        if key not in seen:
            lines.insert(insert_at, f"{key}: {value}")
            insert_at += 1

    trailing_newline = "\n" if markdown_text.endswith("\n") else ""
    return "\n".join(lines) + trailing_newline


def stage_markdown(markdown_path: Path, staged_md: Path, system: str, topic: str) -> None:
    text = markdown_path.read_text(encoding="utf-8")
    staged_md.write_text(update_storage_metadata(text, system, topic), encoding="utf-8")


def run_sync(
    markdown_path: Path,
    system: str,
    topic: str,
    storage_root: Path,
    date_text: str,
    dry_run: bool,
) -> None:
    markdown_path = markdown_path.expanduser().resolve()
    if not markdown_path.exists():
        raise FileNotFoundError(markdown_path)

    paths = build_paths(storage_root.expanduser(), system, topic)
    print(f"storage_root: {paths.storage_root}")
    print(f"active_pdf: {paths.active_pdf}")
    print(f"active_md: {paths.active_md}")

    archive_pair = planned_archive_pair(paths, date_text, topic)
    legacy_archive_groups = legacy_groups(paths, topic)

    if dry_run:
        print(f"render: {markdown_path} -> temporary PDF")
    else:
        paths.active_pdf.parent.mkdir(parents=True, exist_ok=True)
        paths.active_md.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="compact-note-sync-") as temp_dir:
        temp_root = Path(temp_dir)
        staged_md = temp_root / f"{topic}.md"
        staged_pdf = temp_root / f"{topic}.pdf"
        if not dry_run:
            stage_markdown(markdown_path, staged_md, system, topic)
            build_pdf(markdown_path, staged_pdf)

        if archive_pair is not None:
            version = archive_pair.version
            if archive_pair.active_pdf is not None:
                archive_file(
                    archive_pair.active_pdf,
                    paths.archive_pdf_dir / archive_name(topic, date_text, version, ".pdf"),
                    dry_run,
                )
            if archive_pair.active_md is not None:
                archive_file(
                    archive_pair.active_md,
                    paths.archive_md_dir / archive_name(topic, date_text, version, ".md"),
                    dry_run,
                )
            next_archive_version = version + 1
        else:
            next_archive_version = next_version(paths, topic, date_text)

        for group in legacy_archive_groups:
            version = reserve_archive_version(paths, topic, date_text, next_archive_version)
            if group.pdf is not None and (group.pdf.exists() or dry_run):
                archive_file(
                    group.pdf,
                    paths.archive_pdf_dir / archive_name(topic, date_text, version, ".pdf"),
                    dry_run,
                )
            if group.md is not None and (group.md.exists() or dry_run):
                archive_file(
                    group.md,
                    paths.archive_md_dir / archive_name(topic, date_text, version, ".md"),
                    dry_run,
                )
            next_archive_version = version + 1

        copy_file(staged_md if not dry_run else markdown_path, paths.active_md, dry_run)
        copy_file(staged_pdf if not dry_run else Path("<temporary PDF>"), paths.active_pdf, dry_run)

    if not dry_run:
        validate_sync(paths, topic)
    print("sync complete" if not dry_run else "dry run complete")


def validate_sync(paths: SyncPaths, topic: str) -> None:
    if not paths.active_pdf.exists():
        raise RuntimeError(f"active PDF was not created: {paths.active_pdf}")
    if not paths.active_md.exists():
        raise RuntimeError(f"active Markdown was not created: {paths.active_md}")
    if paths.legacy_pdf_dir.exists():
        leftovers = sorted(paths.legacy_pdf_dir.glob("*.pdf"))
        if leftovers:
            names = ", ".join(path.name for path in leftovers[:5])
            raise RuntimeError(f"legacy topic PDF folder still has PDFs: {names}")
    variants = active_pdf_variants(paths, topic)
    if variants:
        names = ", ".join(path.name for path in variants[:5])
        raise RuntimeError(f"active PDF folder has same-topic variants: {names}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Render a compact note PDF and sync canonical artifacts to iCloud."
    )
    parser.add_argument("--markdown", required=True, type=Path)
    parser.add_argument("--system", required=True)
    parser.add_argument("--topic", required=True)
    parser.add_argument("--storage-root", type=Path, default=None)
    parser.add_argument("--date", default=None, help="Archive date in YYMMDD format.")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    system = safe_part(args.system, "--system")
    topic = safe_part(args.topic, "--topic")
    date_text = parse_date(args.date)
    storage_root = args.storage_root.expanduser() if args.storage_root else default_storage_root()

    run_sync(
        markdown_path=args.markdown,
        system=system,
        topic=topic,
        storage_root=storage_root,
        date_text=date_text,
        dry_run=args.dry_run,
    )


if __name__ == "__main__":
    main()
