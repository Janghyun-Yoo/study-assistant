"""Run with a Python environment containing ReportLab:

python3 -m unittest discover -s tests -v
"""
from contextlib import redirect_stdout
import hashlib
import io
from pathlib import Path
import sys
import tempfile
import unicodedata
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import sync_compact_note_to_icloud as sync


def nfd(text):
    return unicodedata.normalize("NFD", text)


def snapshot(root):
    return {
        str(path.relative_to(root)): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in root.rglob("*") if path.is_file()
    }


class SyncTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.storage = self.root / "storage"
        self.paths = sync.build_paths(self.storage, "순환기", "심부전")
        self.source = self.root / "source.md"
        self.source.write_text(
            "---\ntopic: 심부전\n---\n# 순환기 > 심부전\n\n검증용 노트.\n",
            encoding="utf-8",
        )

    def write(self, path, content):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)
        return path

    def active_pair(self):
        # Actual decomposed directory-entry spelling, as seen in iCloud.
        self.write(self.paths.active_md.with_name(nfd("심부전.md")), b"old markdown")
        self.write(self.paths.active_pdf.with_name(nfd("심부전.pdf")), b"old pdf")
        if not self.paths.active_md.exists():
            self.skipTest("Requires a normalization-insensitive filesystem (macOS)")

    def run_sync(self, dry_run=False):
        output = io.StringIO()
        with redirect_stdout(output):
            sync.run_sync(
                self.source, "순환기", "심부전", self.storage, "261021", dry_run,
            )
        return output.getvalue()

    def test_decomposed_active_files_are_not_legacy_or_validation_failures(self):
        self.active_pair()
        self.assertEqual(sync.legacy_md_candidates(self.paths, "심부전"), [])
        self.assertEqual(sync.legacy_pdf_candidates(self.paths, "심부전"), [])
        sync.validate_sync(self.paths, "심부전")

    def test_dry_run_preserves_every_file_and_archives_each_active_file_once(self):
        self.active_pair()
        before = snapshot(self.root)
        with patch.object(sync, "build_pdf") as renderer:
            output = self.run_sync(dry_run=True)
        self.assertEqual(snapshot(self.root), before)
        self.assertEqual(output.count("archive:"), 2)
        renderer.assert_not_called()

    def test_decomposed_versions_and_legacy_pairs_are_detected(self):
        self.active_pair()
        self.write(self.paths.archive_pdf_dir / nfd("심부전_261021_ver.7.pdf"), b"archive")
        self.write(self.paths.archive_md_dir / nfd("심부전_261021_ver.4.md"), b"archive")
        self.assertEqual(sync.next_version(self.paths, "심부전", "261021"), 8)
        self.write(self.paths.active_pdf.parent / nfd("심부전-v2.pdf"), b"legacy pdf")
        self.write(self.paths.active_md.parent / "심부전-v2.md", b"legacy md")
        groups = sync.legacy_groups(self.paths, "심부전")
        self.assertEqual(len(groups), 1)
        self.assertIsNotNone(groups[0].pdf)
        self.assertIsNotNone(groups[0].md)
        with self.assertRaises(RuntimeError):
            sync.validate_sync(self.paths, "심부전")

    def test_existing_archive_is_never_replaced(self):
        source = self.write(self.root / "old.md", b"source")
        destination = self.write(self.root / nfd("심부전_261021_ver.1.md"), b"archive")
        with self.assertRaises(FileExistsError), redirect_stdout(io.StringIO()):
            sync.archive_file(source, destination, False)
        self.assertEqual(source.read_bytes(), b"source")
        self.assertEqual(destination.read_bytes(), b"archive")

    def test_render_failure_preserves_existing_materials(self):
        self.active_pair()
        before = snapshot(self.root)
        with patch.object(sync, "build_pdf", side_effect=RuntimeError("render failed")):
            with self.assertRaisesRegex(RuntimeError, "render failed"):
                self.run_sync()
        self.assertEqual(snapshot(self.root), before)

    def test_two_real_syncs_preserve_active_legacy_archives_and_other_materials(self):
        self.active_pair()
        existing = self.write(
            self.paths.archive_pdf_dir / nfd("심부전_261021_ver.7.pdf"), b"archive seven",
        )
        self.write(self.paths.active_pdf.parent / nfd("심부전-v2.pdf"), b"legacy pdf")
        self.write(self.paths.active_md.parent / "심부전-v2.md", b"legacy md")
        image = self.write(self.paths.active_md.parent / "images/keep.png", b"keep image")
        other = self.write(self.storage / "PDFs/순환기/다른주제.pdf", b"other topic")
        self.run_sync()
        self.assertEqual(
            (self.paths.archive_pdf_dir / "심부전_261021_ver.8.pdf").read_bytes(), b"old pdf",
        )
        self.assertEqual(
            (self.paths.archive_md_dir / "심부전_261021_ver.8.md").read_bytes(), b"old markdown",
        )
        self.assertEqual(
            (self.paths.archive_pdf_dir / "심부전_261021_ver.9.pdf").read_bytes(), b"legacy pdf",
        )
        self.assertEqual(
            (self.paths.archive_md_dir / "심부전_261021_ver.9.md").read_bytes(), b"legacy md",
        )
        self.assertTrue(self.paths.active_pdf.read_bytes().startswith(b"%PDF-"))
        first_pdf = self.paths.active_pdf.read_bytes()
        first_md = self.paths.active_md.read_bytes()
        self.assertIn(b"storage_pdf:", first_md)
        self.run_sync()
        self.assertEqual(
            (self.paths.archive_pdf_dir / "심부전_261021_ver.10.pdf").read_bytes(), first_pdf,
        )
        self.assertEqual(
            (self.paths.archive_md_dir / "심부전_261021_ver.10.md").read_bytes(), first_md,
        )
        self.assertEqual(existing.read_bytes(), b"archive seven")
        self.assertEqual(image.read_bytes(), b"keep image")
        self.assertEqual(other.read_bytes(), b"other topic")
        self.assertEqual(len(list(self.paths.archive_pdf_dir.glob("*.pdf"))), 4)
        sync.validate_sync(self.paths, "심부전")


if __name__ == "__main__":
    unittest.main()
