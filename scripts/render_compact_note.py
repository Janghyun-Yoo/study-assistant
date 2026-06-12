from __future__ import annotations

import argparse
import html
import re
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    CondPageBreak,
    Frame,
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


def normalized_header(rows: list[list[str]]) -> list[str]:
    if not rows:
        return []
    return [re.sub(r"<.*?>", "", cell).strip().lower() for cell in rows[0]]


def table_widths(rows: list[list[str]], available_width: float) -> list[float]:
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
        if header and header[0] == "step":
            weights = [0.13, 0.44, 0.43]
        elif header and header[0] in {"test", "finding", "category", "class"}:
            weights = [0.17, 0.43, 0.40]
        else:
            weights = [0.20, 0.43, 0.37]
    elif cols == 4:
        if header and header[0] in {"pattern", "item", "situation", "cause group", "개념"}:
            weights = [0.18, 0.31, 0.27, 0.24]
        else:
            weights = [0.17, 0.29, 0.30, 0.24]
    elif cols == 5:
        weights = [0.14, 0.23, 0.22, 0.23, 0.18]
    elif cols == 6:
        weights = [0.12, 0.20, 0.14, 0.20, 0.19, 0.15]
    else:
        weights = [1 / cols] * cols
    total = sum(weights)
    return [available_width * w / total for w in weights]


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
        fontSize=7.2,
        leading=9.4,
        textColor=colors.HexColor("#4B5563"),
        leftIndent=2,
        rightIndent=2,
        spaceBefore=3,
        spaceAfter=6,
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
    while i < len(lines):
        line = lines[i].rstrip()
        if not line.strip():
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
                data = [[paragraph(cell, table_style) for cell in row] for row in norm_rows]
                data[0] = [paragraph(cell, header_style) for cell in norm_rows[0]]
                table = Table(
                    data,
                    colWidths=table_widths(norm_rows, available_width),
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
                story.append(table)
                story.append(Spacer(1, 5))
            continue
        if line.startswith("# "):
            if not first_h1:
                story.append(CondPageBreak(52 * mm))
                story.append(Spacer(1, 6))
            story.append(paragraph(line[2:].strip(), h1))
            first_h1 = False
        elif line.startswith("## "):
            heading = line[3:].strip()
            min_space = 30 * mm if heading == "Source Notes" else 58 * mm
            story.append(CondPageBreak(min_space))
            story.append(paragraph(heading, h2))
        elif line.startswith("### "):
            heading = line[4:].strip()
            if heading in {"Common Traps", "Active Recall Questions"}:
                min_space = 105 * mm
            elif heading == "PAH Drug Mini-Table":
                min_space = 88 * mm
            else:
                min_space = 42 * mm
            story.append(CondPageBreak(min_space))
            story.append(paragraph(heading, h3))
        elif line.startswith("<small>") and line.endswith("</small>"):
            story.append(paragraph(line[7:-8], small))
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
