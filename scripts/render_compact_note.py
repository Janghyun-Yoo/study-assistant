from __future__ import annotations

import argparse
import html
import re
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    CondPageBreak,
    Frame,
    Image as RLImage,
    KeepTogether,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


FONT_DIRS = [
    Path(__file__).resolve().parents[1] / "assets" / "fonts",
    Path.home() / "Library" / "Fonts",
    Path("/Library/Fonts"),
    Path("/System/Library/Fonts"),
    Path("/System/Library/Fonts/Supplemental"),
]

FONT_STACK = [
    {
        "family": "Pretendard",
        "regular": ["Pretendard-Regular.ttf", "Pretendard-Regular.otf"],
        "medium": ["Pretendard-Medium.ttf", "Pretendard-Medium.otf"],
        "semibold": ["Pretendard-SemiBold.ttf", "Pretendard-SemiBold.otf"],
    },
    {
        "family": "Noto Sans KR",
        "regular": ["NotoSansKR-Regular.otf", "NotoSansKR-Regular.ttf"],
        "medium": ["NotoSansKR-Medium.otf", "NotoSansKR-Medium.ttf"],
        "semibold": ["NotoSansKR-SemiBold.otf", "NotoSansKR-SemiBold.ttf"],
    },
    {
        "family": "Apple SD Gothic Neo",
        "regular": ["AppleSDGothicNeo.ttc"],
        "medium": ["AppleSDGothicNeo.ttc"],
        "semibold": ["AppleSDGothicNeo.ttc"],
    },
    {
        "family": "AppleGothic",
        "regular": ["AppleGothic.ttf"],
        "medium": ["AppleGothic.ttf"],
        "semibold": ["AppleGothic.ttf"],
    },
]


def find_font_file(names: list[str]) -> Path | None:
    for font_dir in FONT_DIRS:
        for name in names:
            path = font_dir / name
            if path.exists():
                return path
        for name in names:
            matches = sorted(font_dir.glob(name))
            if matches:
                return matches[0]
    return None


def register_ttf(name: str, path: Path) -> bool:
    try:
        pdfmetrics.registerFont(TTFont(name, str(path)))
        return True
    except Exception:
        return False


def register_font_set() -> dict[str, str]:
    for entry in FONT_STACK:
        family = re.sub(r"[^A-Za-z0-9]+", "", entry["family"])
        regular_name = f"{family}-Regular"
        regular = register_first_available(regular_name, entry["regular"])
        if not regular:
            continue

        medium_name = f"{family}-Medium"
        medium = register_first_available(medium_name, entry["medium"]) or regular
        semibold_name = f"{family}-SemiBold"
        semibold = register_first_available(semibold_name, entry["semibold"]) or medium

        pdfmetrics.registerFontFamily(
            regular,
            normal=regular,
            bold=semibold,
            italic=regular,
            boldItalic=semibold,
        )
        return {
            "family": entry["family"],
            "regular": regular,
            "medium": medium,
            "semibold": semibold,
        }

    return {
        "family": "Helvetica",
        "regular": "Helvetica",
        "medium": "Helvetica-Bold",
        "semibold": "Helvetica-Bold",
    }


def register_first_available(name: str, candidates: list[str]) -> str | None:
    for candidate in candidates:
        path = find_font_file([candidate])
        if path and register_ttf(name, path):
            return name
    return None


def strip_front_matter(text: str) -> str:
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            return text[end + 5 :].lstrip()
    return text


def split_table_row(line: str) -> list[str]:
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return [cell.strip() for cell in line.split("|")]


def is_separator_row(line: str) -> bool:
    cells = split_table_row(line)
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell.strip()) for cell in cells)


def inline_markup(text: str) -> str:
    text = re.sub(
        r'<span style="color:(#[0-9A-Fa-f]{6})">\*\*(.*?)\*\*</span>',
        lambda m: f'<font color="{m.group(1)}"><b>{html.escape(m.group(2))}</b></font>',
        text,
    )
    text = re.sub(
        r'<span style="color:(#[0-9A-Fa-f]{6})">(.*?)</span>',
        lambda m: f'<font color="{m.group(1)}">{html.escape(m.group(2))}</font>',
        text,
    )
    text = html.escape(text, quote=False)
    text = re.sub(r"&lt;(font|b|/font|/b)(.*?)&gt;", r"<\1\2>", text)
    text = re.sub(r"&lt;br\s*/?&gt;", "<br/>", text, flags=re.IGNORECASE)
    text = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"`([^`]+)`", r"<font color='#374151'>\1</font>", text)
    text = text.replace("&lt;=", "&le;").replace("&gt;=", "&ge;")
    return text


def paragraph(text: str, style: ParagraphStyle) -> Paragraph:
    return Paragraph(inline_markup(text), style)


def small_html(line: str) -> str | None:
    stripped = line.strip()
    if stripped.startswith("<small>") and stripped.endswith("</small>"):
        return stripped[7:-8]
    return None


def keep_together(text: str) -> str:
    return re.sub(r"(?<=\S) (?=\S)", "\u00A0", text)


KOREAN_SUFFIX_FRAGMENTS = {
    "계",
    "군",
    "류",
    "명",
    "법",
    "병",
    "술",
    "약",
    "염",
    "원인",
    "제",
    "증",
    "질환",
    "축",
    "형",
}

ORPHAN_WORDS = {
    "가능",
    "관리",
    "금지",
    "낮음",
    "단서",
    "상승",
    "우선",
    "있음",
    "폐부종",
    "주의",
    "치료",
    "평가",
    "확인",
    "후보",
} | KOREAN_SUFFIX_FRAGMENTS

ORPHAN_ACRONYMS = {
    "ECMO",
    "IABP",
    "LVAD",
    "MCS",
}

ENGLISH_CLINICAL_TAIL_WORDS = {
    "congestion",
    "disease",
    "edema",
}

ENGLISH_CLINICAL_PHRASES = {
    "alveolar edema",
    "coronary artery disease",
    "interstitial edema",
    "mechanical complication",
    "organ hypoperfusion",
    "pulmonary congestion",
    "pulmonary edema",
    "severe valve disease",
    "structural heart disease",
    "vascular congestion",
}

STRANDED_ACTION_CHUNKS = {
    "CABG 고려",
    "ECMO 고려",
    "IABP 고려",
    "LVAD 고려",
    "MCS 고려",
    "PCI 고려",
}


def protect_semantic_chunks(text: str) -> str:
    protected = text
    fixed_phrases = [
        *sorted(ENGLISH_CLINICAL_PHRASES),
        "diltiazem exception",
        "volume depletion",
        "renal artery stenosis",
        "PAH 약물 금지",
        "nitrate 병용 금기",
        "원인 단서",
        "ECG 단서",
        "우심축 우선",
        "CXR 폐부종",
        "폐정맥압 상승",
        "동반질환 관리",
        "근거 낮음",
        "원인 질환",
        "shock을 강화",
        "치료 방향 확인",
        "CABG 고려",
        "ECMO 고려",
        "IABP 고려",
        "LVAD 고려",
        "MCS 고려",
        "PCI 고려",
        "RV-PVR 축",
        "폐혈관 축",
        "우심부전/RV-PVR 축",
        "우심부전/폐혈관 축",
    ]
    for phrase in fixed_phrases:
        protected = protected.replace(phrase, keep_together(phrase))

    token = r"(?:[A-Za-z0-9/%+\-.]+|[가-힣]+)"
    mixed_token = r"(?:[A-Za-z0-9가-힣/%+\-.]+)"
    suffix_pattern = "|".join(
        re.escape(word) for word in sorted(KOREAN_SUFFIX_FRAGMENTS, key=len, reverse=True)
    )
    protected = re.sub(
        rf"→\s*[↑↓]?\s*{token}(?:\s+{token}){{0,3}}",
        lambda match: keep_together(match.group(0)),
        protected,
    )
    protected = re.sub(
        rf"±\s*{token}(?:\s+{token}){{0,3}}",
        lambda match: keep_together(match.group(0)),
        protected,
    )
    protected = re.sub(
        rf"{token}\s+(?:상승|감소|확장|저하|낮음|금지|우선|단서|확인|치료|평가|관리|가능|있음)",
        lambda match: keep_together(match.group(0)),
        protected,
    )
    protected = re.sub(
        rf"\bgroup\s+\d+\s+PH\b",
        lambda match: keep_together(match.group(0)),
        protected,
        flags=re.IGNORECASE,
    )
    protected = re.sub(
        rf"(?<![A-Za-z0-9가-힣]){mixed_token}\s+(?:{suffix_pattern})(?![A-Za-z0-9가-힣])",
        lambda match: keep_together(match.group(0)),
        protected,
    )
    return protected


def table_paragraph(text: str, style: ParagraphStyle) -> Paragraph:
    return paragraph(protect_semantic_chunks(text), style)


def markdown_image(line: str) -> tuple[str, str] | None:
    match = re.fullmatch(r"!\[([^\]]*)\]\((.+)\)", line.strip())
    if not match:
        return None

    alt = match.group(1).strip()
    target = match.group(2).strip()
    if target.startswith("<"):
        end = target.find(">")
        if end == -1:
            return None
        path_text = target[1:end].strip()
    else:
        path_text = re.sub(r"\s+(['\"]).*\1\s*$", "", target).strip()

    return alt, path_text


def resolve_image_path(path_text: str, markdown_path: Path) -> Path | None:
    if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", path_text):
        return None
    path = Path(path_text).expanduser()
    if not path.is_absolute():
        path = markdown_path.parent / path
    return path


def image_flowable(
    alt: str,
    path_text: str,
    markdown_path: Path,
    available_width: float,
    max_height: float,
    caption_style: ParagraphStyle,
    *,
    reserve_space: bool = True,
) -> list:
    path = resolve_image_path(path_text, markdown_path)
    if path is None:
        return [paragraph(f"[Image skipped: remote URL not supported] {alt or path_text}", caption_style)]
    if not path.exists():
        return [paragraph(f"[Image missing] {alt or path_text}: {path}", caption_style)]

    try:
        width, height = ImageReader(str(path)).getSize()
    except Exception as exc:
        return [paragraph(f"[Image unreadable] {alt or path_text}: {exc}", caption_style)]

    scale = min(available_width / width, max_height / height, 1.0)
    image = RLImage(str(path), width=width * scale, height=height * scale)
    image.hAlign = "CENTER"

    flowables = []
    if reserve_space:
        flowables.append(CondPageBreak(image.drawHeight + 16))
    flowables.extend([image, Spacer(1, 3)])
    if alt:
        flowables.append(paragraph(f"Figure: {alt}", caption_style))
    else:
        flowables.append(Spacer(1, 4))
    return flowables


def image_max_height_mm(alt: str, path_text: str) -> float:
    marker = f"{alt} {path_text}".lower()
    if "algorithm" in marker or "review map" in marker:
        return 138
    return 62


def next_content_index(lines: list[str], start: int) -> int:
    i = start
    while i < len(lines) and not lines[i].strip():
        i += 1
    return i


def normalized_header(rows: list[list[str]]) -> list[str]:
    if not rows:
        return []
    return [re.sub(r"<.*?>", "", cell).strip().lower() for cell in rows[0]]


def plain_cell_length(cell: str) -> int:
    text = re.sub(r"<br\s*/?>", " ", cell, flags=re.IGNORECASE)
    text = re.sub(r"<.*?>", "", text)
    text = re.sub(r"[*_`]+", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return len(text)


def content_based_weights(rows: list[list[str]], cols: int) -> list[float]:
    lengths = [0.0] * cols
    row_count = max(len(rows), 1)
    for row in rows:
        for index in range(cols):
            cell = row[index] if index < len(row) else ""
            lengths[index] += min(plain_cell_length(cell), 120)

    averages = [max(length / row_count, 1.0) for length in lengths]
    scores = [average ** 0.5 for average in averages]
    total = sum(scores)
    raw_weights = [score / total for score in scores]
    return normalized_clamped_weights(raw_weights, minimum=0.24, maximum=0.42)


def normalized_weights(weights: list[float]) -> list[float]:
    total = sum(weights)
    if not total:
        return [1 / len(weights)] * len(weights)
    return [weight / total for weight in weights]


def normalized_clamped_weights(
    weights: list[float], minimum: float, maximum: float
) -> list[float]:
    result = [0.0] * len(weights)
    fixed = [False] * len(weights)

    while True:
        remaining_total = 1.0 - sum(result[index] for index, is_fixed in enumerate(fixed) if is_fixed)
        remaining_weight = sum(weight for weight, is_fixed in zip(weights, fixed) if not is_fixed)
        candidates: list[float | None] = [None] * len(weights)

        for index, (weight, is_fixed) in enumerate(zip(weights, fixed)):
            if is_fixed:
                continue
            candidate = remaining_total / max(fixed.count(False), 1)
            if remaining_weight:
                candidate = remaining_total * weight / remaining_weight
            candidates[index] = candidate

        changed = False
        for index, candidate in enumerate(candidates):
            if candidate is None:
                continue
            if candidate > maximum:
                result[index] = maximum
                fixed[index] = True
                changed = True
        if changed:
            continue

        for index, candidate in enumerate(candidates):
            if candidate is None:
                continue
            if candidate < minimum:
                result[index] = minimum
                fixed[index] = True
                changed = True

        if not changed:
            for index, candidate in enumerate(candidates):
                if candidate is not None:
                    result[index] = candidate
            return result


def base_table_weights(rows: list[list[str]]) -> list[float]:
    cols = max(len(row) for row in rows)
    header = normalized_header(rows)
    if cols <= 2:
        if header and header[0] == "field":
            weights = [0.24, 0.76]
        elif header and header[0] in {"question", "trap"}:
            weights = [0.40, 0.60]
        else:
            weights = [0.34, 0.66]
    elif cols == 3:
        if header[:3] == ["what to look for", "exam cue", "common trap"]:
            weights = [0.38, 0.30, 0.32]
        elif header and header[0] == "step":
            weights = [0.09, 0.51, 0.40]
        elif header and header[0] in {"test", "finding", "category", "class"}:
            weights = [0.17, 0.43, 0.40]
        else:
            weights = content_based_weights(rows, cols)
    elif cols == 4:
        if header[:4] == ["class", "representative drugs", "exam use", "watch"]:
            weights = [0.15, 0.27, 0.36, 0.22]
        elif header[:4] == ["test", "use", "expected finding", "exam trap"]:
            weights = [0.15, 0.18, 0.41, 0.26]
        elif header and header[0] == "pattern" and "dominant clues" in header:
            weights = [0.18, 0.29, 0.30, 0.23]
        elif header and header[0] in {"pattern", "item", "situation", "cause group", "개념"}:
            weights = [0.18, 0.31, 0.27, 0.24]
        else:
            weights = [0.17, 0.29, 0.30, 0.24]
    elif cols == 5:
        weights = [0.14, 0.23, 0.22, 0.23, 0.18]
    elif cols == 6:
        weights = [0.12, 0.20, 0.14, 0.20, 0.19, 0.15]
    else:
        weights = [1 / cols] * cols
    return normalized_weights(weights)


def width_candidates(base_weights: list[float]) -> list[list[float]]:
    cols = len(base_weights)
    delta_limit = 0.02 if cols >= 5 else 0.06
    deltas = [0.01, 0.02] if cols >= 5 else [0.01, 0.02, 0.03, 0.04, 0.05, 0.06]
    lower = [max(0.08, weight - delta_limit) for weight in base_weights]
    upper = [min(0.82, weight + delta_limit) for weight in base_weights]
    seen = {tuple(round(weight, 5) for weight in base_weights)}
    candidates = [base_weights]

    for source in range(cols):
        for target in range(cols):
            if source == target:
                continue
            for delta in deltas:
                candidate = list(base_weights)
                candidate[source] -= delta
                candidate[target] += delta
                if candidate[source] < lower[source] or candidate[target] > upper[target]:
                    continue
                key = tuple(round(weight, 5) for weight in candidate)
                if key not in seen:
                    seen.add(key)
                    candidates.append(candidate)

    return candidates


def line_text(line) -> str:
    if isinstance(line, tuple) and len(line) >= 2:
        words = line[1]
        text = " ".join(str(word) for word in words if word)
        return re.sub(r"\s+", " ", text).strip()
    words = getattr(line, "words", [])
    parts = [getattr(word, "text", "") for word in words]
    text = " ".join(part for part in parts if part)
    return re.sub(r"\s+", " ", text).strip()


def line_tokens(text: str) -> list[str]:
    return re.findall(r"[A-Za-z0-9/%+\-.]+|[가-힣]+", text)


def orphan_line_penalty(text: str) -> float:
    if not text:
        return 0.0
    cleaned = re.sub(r"[.,;:!?()\[\]{}]+$", "", text).strip()
    if cleaned in ORPHAN_ACRONYMS:
        return 1000.0
    if cleaned in STRANDED_ACTION_CHUNKS:
        return 650.0
    if cleaned.lower() in ENGLISH_CLINICAL_TAIL_WORDS:
        return 1000.0
    if re.fullmatch(r"\(?[A-Za-z0-9/%+\-.]{2,20}\)?", text.strip()):
        return 0.0
    if text.strip().startswith("(") and text.strip().endswith(")") and not re.search(r"[가-힣]", text):
        return 0.0
    tokens = line_tokens(cleaned)
    if not tokens:
        return 0.0
    if cleaned in ORPHAN_WORDS:
        return 1100.0
    if len(tokens) == 1 and re.search(r"[가-힣]", cleaned) and len(cleaned) <= 2:
        return 900.0
    if len(tokens) <= 3 and len(cleaned) <= 18 and any(token in ORPHAN_WORDS for token in tokens):
        return 1000.0
    return 0.0


def punctuation_clause_wrap_penalty(previous_line: str, current_line: str) -> float:
    if not previous_line or not current_line:
        return 0.0

    previous = previous_line.strip()
    current = current_line.strip()
    if ";" in previous and not previous.endswith(";"):
        tail = previous.rsplit(";", 1)[1].strip()
        if tail and len(line_tokens(tail)) <= 8:
            return 450.0

    if "," not in previous:
        return 0.0

    tail = previous.rsplit(",", 1)[1].strip()
    if not tail or len(line_tokens(tail)) > 5:
        return 0.0

    combined = f"{tail} {current}".lower()
    if re.search(
        r"\b(afterload|bleeding|caveat|edema|hemolysis|ischemia|pulmonary|risk|selected)\b",
        combined,
    ) or re.search(r"(가능|고려|위험|주의|확인)", f"{tail} {current}"):
        return 300.0
    return 0.0


def paragraph_wrap_metrics(
    cell: str, style: ParagraphStyle, width: float
) -> tuple[float, int, float, list[str]]:
    paragraph_obj = table_paragraph(cell, style)
    paragraph_obj.wrap(max(width - 6, 1), 10_000)
    lines = list(getattr(getattr(paragraph_obj, "blPara", None), "lines", []) or [])
    penalty = 0.0
    orphans = []
    for index, line in enumerate(lines):
        if index == 0:
            continue
        text = line_text(line)
        line_penalty = orphan_line_penalty(text)
        if line_penalty:
            penalty += line_penalty
            orphans.append(text)
        previous_text = line_text(lines[index - 1])
        punctuation_penalty = punctuation_clause_wrap_penalty(previous_text, text)
        if punctuation_penalty:
            penalty += punctuation_penalty
            orphans.append(f"punctuation clause: {text}")
    return paragraph_obj.height, len(lines), penalty, orphans


def table_width_score(
    rows: list[list[str]],
    weights: list[float],
    base_weights: list[float],
    available_width: float,
    table_style: ParagraphStyle,
    header_style: ParagraphStyle,
) -> tuple[float, list[str]]:
    widths = [available_width * weight for weight in weights]
    score = sum(abs(weight - base) for weight, base in zip(weights, base_weights)) * 180
    total_height = 0.0
    orphans = []

    for row_index, row in enumerate(rows):
        row_height = 0.0
        for col_index, cell in enumerate(row):
            style = header_style if row_index == 0 else table_style
            height, line_count, orphan_penalty, cell_orphans = paragraph_wrap_metrics(
                cell,
                style,
                widths[col_index],
            )
            row_height = max(row_height, height)
            score += orphan_penalty
            orphans.extend(
                f"r{row_index + 1}c{col_index + 1}:{orphan}"
                for orphan in cell_orphans
            )
            if row_index == 0 and line_count > 1:
                score += (line_count - 1) * 35
        total_height += row_height

    return score + total_height * 0.45, orphans


def table_style_variant(
    style: ParagraphStyle,
    name: str,
    font_size_delta: float,
) -> ParagraphStyle:
    return ParagraphStyle(
        name,
        parent=style,
        fontSize=style.fontSize + font_size_delta,
        leading=style.leading + font_size_delta,
    )


def style_candidates(
    cols: int,
    table_style: ParagraphStyle,
    header_style: ParagraphStyle,
) -> list[tuple[ParagraphStyle, ParagraphStyle, float]]:
    if cols >= 5:
        deltas = [0.0, -0.2]
    else:
        deltas = [0.0, -0.2, -0.4]

    candidates = []
    for delta in deltas:
        if delta == 0:
            candidates.append((table_style, header_style, 0.0))
            continue
        adjusted_table = table_style_variant(table_style, f"table_{delta}", delta)
        adjusted_header = table_style_variant(header_style, f"table_header_{delta}", delta)
        candidates.append((adjusted_table, adjusted_header, abs(delta)))
    return candidates


def optimized_table_layout(
    rows: list[list[str]],
    available_width: float,
    table_style: ParagraphStyle,
    header_style: ParagraphStyle,
) -> tuple[list[float], ParagraphStyle, ParagraphStyle, list[str]]:
    base_weights = base_table_weights(rows)
    candidates = width_candidates(base_weights)
    cols = len(base_weights)
    best_score = None
    best_weights = base_weights
    best_table_style = table_style
    best_header_style = header_style
    best_orphans = []

    for candidate_table_style, candidate_header_style, shrink in style_candidates(
        cols,
        table_style,
        header_style,
    ):
        for weights in candidates:
            score, orphans = table_width_score(
                rows,
                weights,
                base_weights,
                available_width,
                candidate_table_style,
                candidate_header_style,
            )
            score += shrink * 320
            if best_score is None or score < best_score:
                best_score = score
                best_weights = weights
                best_table_style = candidate_table_style
                best_header_style = candidate_header_style
                best_orphans = orphans

    return (
        [available_width * weight for weight in best_weights],
        best_table_style,
        best_header_style,
        sorted(set(best_orphans)),
    )


def optimized_table_widths(
    rows: list[list[str]],
    available_width: float,
    table_style: ParagraphStyle,
    header_style: ParagraphStyle,
) -> list[float]:
    widths, _, _, _ = optimized_table_layout(rows, available_width, table_style, header_style)
    return widths


def table_widths(rows: list[list[str]], available_width: float) -> list[float]:
    return [available_width * weight for weight in base_table_weights(rows)]


def build_pdf(markdown_path: Path, pdf_path: Path) -> None:
    fonts = register_font_set()
    styles = getSampleStyleSheet()
    base = ParagraphStyle(
        "base",
        parent=styles["BodyText"],
        fontName=fonts["regular"],
        fontSize=8.6,
        leading=12.0,
        alignment=TA_LEFT,
        spaceAfter=4,
    )
    small = ParagraphStyle(
        "small",
        parent=base,
        fontSize=6.8,
        leading=8.6,
        textColor=colors.HexColor("#4B5563"),
        leftIndent=2,
        rightIndent=2,
        spaceBefore=2,
        spaceAfter=5,
    )
    caption = ParagraphStyle(
        "caption",
        parent=small,
        alignment=TA_LEFT,
        fontSize=7.0,
        leading=9.0,
        spaceBefore=2,
        spaceAfter=7,
    )
    h1 = ParagraphStyle(
        "h1",
        parent=base,
        fontName=fonts["semibold"],
        fontSize=18,
        leading=23,
        spaceBefore=0,
        spaceAfter=10,
        textColor=colors.HexColor("#111827"),
    )
    h2 = ParagraphStyle(
        "h2",
        parent=base,
        fontName=fonts["semibold"],
        fontSize=12.2,
        leading=16,
        spaceBefore=13,
        spaceAfter=6,
        textColor=colors.HexColor("#111827"),
    )
    h3 = ParagraphStyle(
        "h3",
        parent=base,
        fontName=fonts["medium"],
        fontSize=10.2,
        leading=13.2,
        spaceBefore=9,
        spaceAfter=4,
        textColor=colors.HexColor("#111827"),
    )

    page_width, page_height = A4
    margin_x = 14 * mm
    margin_y = 13 * mm
    available_width = page_width - 2 * margin_x
    frame = Frame(margin_x, margin_y, available_width, page_height - 2 * margin_y, id="normal")
    doc = BaseDocTemplate(
        str(pdf_path),
        pagesize=A4,
        leftMargin=margin_x,
        rightMargin=margin_x,
        topMargin=margin_y,
        bottomMargin=margin_y,
    )
    doc.addPageTemplates([PageTemplate(id="main", frames=[frame])])

    text = strip_front_matter(markdown_path.read_text(encoding="utf-8"))
    lines = text.splitlines()
    story = []
    i = 0
    first_h1 = True
    current_heading = ""
    while i < len(lines):
        line = lines[i].rstrip()
        if not line.strip():
            i += 1
            continue
        image_parts = markdown_image(line)
        if image_parts:
            alt, path_text = image_parts
            story.extend(
                image_flowable(
                    alt,
                    path_text,
                    markdown_path,
                    available_width,
                    image_max_height_mm(alt, path_text) * mm,
                    caption,
                )
            )
            i += 1
            continue
        if line.strip() == "---":
            story.append(PageBreak())
            i += 1
            continue
        if line.startswith("|"):
            raw_rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                if not is_separator_row(lines[i]):
                    raw_rows.append(split_table_row(lines[i]))
                i += 1
            if raw_rows:
                cols = max(len(row) for row in raw_rows)
                norm_rows = [row + [""] * (cols - len(row)) for row in raw_rows]
                table_style = ParagraphStyle(
                    "table",
                    parent=base,
                    fontName=fonts["regular"],
                    fontSize=6.9 if cols >= 5 else 7.5,
                    leading=8.8 if cols >= 5 else 9.7,
                )
                header_style = ParagraphStyle(
                    "table_header",
                    parent=table_style,
                    fontName=fonts["medium"],
                )
                col_widths, table_style, header_style, warnings = optimized_table_layout(
                    norm_rows,
                    available_width,
                    table_style,
                    header_style,
                )
                if warnings:
                    header_label = " | ".join(norm_rows[0])
                    print(
                        "[table-layout-warning] "
                        f"{current_heading or 'untitled'} / {header_label}: "
                        f"remaining orphan candidates={', '.join(warnings[:6])}"
                    )
                data = [[table_paragraph(cell, table_style) for cell in row] for row in norm_rows]
                data[0] = [table_paragraph(cell, header_style) for cell in norm_rows[0]]
                table = Table(
                    data,
                    colWidths=col_widths,
                    repeatRows=1,
                    splitByRow=1,
                    hAlign="LEFT",
                )
                table.setStyle(
                    TableStyle(
                        [
                            ("FONTNAME", (0, 0), (-1, -1), fonts["regular"]),
                            ("FONTNAME", (0, 0), (-1, 0), fonts["medium"]),
                            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#EEF2FF")),
                            ("TEXTCOLOR", (0, 0), (-1, 0), colors.HexColor("#111827")),
                            ("GRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#CBD5E1")),
                            ("VALIGN", (0, 0), (-1, -1), "TOP"),
                            ("LEFTPADDING", (0, 0), (-1, -1), 3),
                            ("RIGHTPADDING", (0, 0), (-1, -1), 3),
                            ("TOPPADDING", (0, 0), (-1, -1), 3),
                            ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
                        ]
                    )
                )
                j = i
                while j < len(lines) and not lines[j].strip():
                    j += 1
                source_html = small_html(lines[j]) if j < len(lines) else None
                if source_html is not None:
                    source = paragraph(source_html, small)
                    table_width, table_height = table.wrap(available_width, page_height)
                    source_width, source_height = source.wrap(available_width, page_height)
                    group = [table, Spacer(1, 3), source, Spacer(1, 5)]
                    if table_height + source_height + 8 <= frame._height * 0.92:
                        story.append(KeepTogether(group))
                    else:
                        story.extend(group)
                    i = j + 1
                else:
                    story.append(table)
                    story.append(Spacer(1, 5))
            continue
        if line.startswith("# "):
            current_heading = line[2:].strip()
            if not first_h1:
                story.append(CondPageBreak(52 * mm))
                story.append(Spacer(1, 6))
            story.append(paragraph(line[2:].strip(), h1))
            first_h1 = False
        elif line.startswith("## "):
            heading = line[3:].strip()
            current_heading = heading
            next_i = next_content_index(lines, i + 1)
            next_line = lines[next_i].rstrip() if next_i < len(lines) else ""
            image_i = -1
            image_subheading = ""
            if next_line.startswith("### "):
                candidate_i = next_content_index(lines, next_i + 1)
                if candidate_i < len(lines) and markdown_image(lines[candidate_i].rstrip()):
                    image_i = candidate_i
                    image_subheading = next_line[4:].strip()
            if heading in {"Algorithm Review Maps", "Visual Anchors"} and image_i >= 0:
                alt, path_text = markdown_image(lines[image_i].rstrip()) or ("", "")
                group = [
                    paragraph(heading, h2),
                    paragraph(image_subheading, h3),
                    *image_flowable(
                        alt,
                        path_text,
                        markdown_path,
                        available_width,
                        image_max_height_mm(alt, path_text) * mm,
                        caption,
                        reserve_space=False,
                    ),
                    Spacer(1, 5),
                ]
                story.append(KeepTogether(group))
                current_heading = image_subheading
                i = image_i + 1
                continue
            min_space = 30 * mm if heading == "Source Notes" else 74 * mm
            story.append(CondPageBreak(min_space))
            story.append(paragraph(heading, h2))
        elif line.startswith("### "):
            heading = line[4:].strip()
            current_heading = heading
            if heading in {"Common Traps", "Active Recall Questions"}:
                min_space = 105 * mm
            elif heading == "PAH Drug Mini-Table":
                min_space = 88 * mm
            else:
                min_space = 42 * mm
            story.append(CondPageBreak(min_space))
            story.append(paragraph(heading, h3))
        elif small_html(line) is not None:
            story.append(paragraph(small_html(line) or "", small))
        elif line.startswith("- "):
            story.append(paragraph("• " + line[2:].strip(), base))
        else:
            story.append(paragraph(line.strip(), base))
        i += 1

    doc.build(story)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("markdown", type=Path)
    parser.add_argument("pdf", type=Path)
    args = parser.parse_args()
    args.pdf.parent.mkdir(parents=True, exist_ok=True)
    build_pdf(args.markdown, args.pdf)


if __name__ == "__main__":
    main()
