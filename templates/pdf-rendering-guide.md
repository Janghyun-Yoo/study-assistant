# PDF Rendering Guide

Use this guide when converting Markdown study notes into PDF.

## Layout Principles

- The first page should work as a standalone rapid-review card.
- Use the top title format `{system} > {unit}`, such as `순환기 > 심부전`.
- Do not place a version/subtitle line directly under the top PDF title.
- Keep paragraphs short. Prefer bullets and tables.
- Use tables for diagnosis, differential diagnosis, drugs, contraindications,
  and exam traps.
- Separate contraindications, cautions, and adverse effects.
- Use explicit page breaks when the PDF becomes crowded or when a major section
  should start as a new review unit.
- Do not force a draft note into a fixed page count. While a topic/unit is still
  growing, leave room for future Allen/KMLE/problem-solving additions.
- Do layout cleanup at the unit-level finalization step. For final versions,
  remove awkward orphan pages and excessive blank space, but keep useful study
  content rather than compressing mechanically.
- Bold section headings need visible breathing room above them, especially after
  tables and source-note boxes. For the current gold-standard compact-note
  renderer, major H1 sections should generally use about 14-16 pt of space above
  and 7-8 pt below; H2 sections should use about 11-13 pt above and 5-6 pt below.
- Do not leave a section heading stranded at the bottom of a page when the
  table, algorithm, or first explanatory paragraph starts on the next page. If
  there is not enough room below a major heading for the first meaningful block,
  move the heading itself to the next page. This is especially important for
  `Concept Bridge`, treatment algorithms, dense drug tables, and `Exam Traps and
  Active Recall`.
- Avoid table widows: do not leave only one or two trailing rows of a table on
  the next page when the table could instead start cleanly on the following
  page. For compact notes, subheadings that introduce tables should reserve
  enough space for the heading plus a meaningful first chunk of the table.
- `Exam Traps and Active Recall` should keep the same major-H1 spacing when it
  follows a table or source-note box. Use a first-heading/no-top-space style
  only when the section begins at the very top of a new page.
- Use readable table text sizes. Disease-flow and core clinical tables should
  use normal table text, not tiny footnote-sized text. Dense drug tables may be
  slightly smaller, but should generally stay at or above about 6.5 pt with
  enough line spacing to read on screen.
- Use emphasis sparingly. Bold important concepts and key decision rules. Blue
  bold can mark high-yield/frequently tested items, and red bold can mark
  contraindications or major safety warnings. Avoid coloring large blocks of
  text.

## Font

Preferred Korean PDF font:

```text
Pretendard
```

Recommended weights:

```text
Title/section headings: Pretendard SemiBold
Subtitles/table labels: Pretendard Medium
Body/table text: Pretendard Regular
```

Renderer requirement:

```text
Register and use three separate faces when available:
- Pretendard Regular for body paragraphs and table cells
- Pretendard Medium for table header labels and compact sublabels
- Pretendard SemiBold for the title, section headings, and bold emphasis
```

Before generating or updating a canonical PDF, verify that Pretendard is
installed in one of the local macOS font locations:

```text
~/Library/Fonts/
/Library/Fonts/
```

Expected installable files include:

```text
Pretendard-Regular.otf
Pretendard-Medium.otf
Pretendard-SemiBold.otf
```

Equivalent `.ttf` files are also acceptable if the renderer can embed them.
For the current ReportLab-based compact-note renderer, the official Pretendard
OTF files may fail to embed because they use PostScript/CFF outlines. If that
happens, install the official `public/static/alternative/*.ttf` files from the
same Pretendard release as well; these TrueType files are the preferred
Pretendard source for this renderer.

Why:

- Good Hangul readability for screen and print.
- Korean, English abbreviations, and numbers sit together more naturally than
  the default macOS fallback fonts.
- Distributed under the SIL Open Font License, so PDF embedding is acceptable.

Fallbacks:

```text
Noto Sans KR
Apple SD Gothic Neo
AppleGothic
```

Use AppleGothic only as a last fallback for local rendering, because it is less
comfortable for dense study PDFs.

If Pretendard is missing, install it from the official Pretendard release and
place the Regular, Medium, and SemiBold font files in `~/Library/Fonts/` or
`/Library/Fonts/`, then regenerate the PDF. Until it is installed, prefer
`Noto Sans KR` if locally available. `Apple SD Gothic Neo` may appear in Font
Book as a macOS system font, but some PDF renderers cannot embed its `.ttc`
file; in that case, fall back only temporarily. `AppleGothic` remains the last
local fallback.

## Natural Page Plan

1. Page 1: exam snapshot and core disease script
2. Page 2: diagnosis, tests, and differential diagnosis
3. Page 3: treatment algorithm and drug table
4. Page 4: contraindications, exam traps, active recall

## Markdown Page Break

Use a horizontal rule as a page-break marker in PDF-oriented notes:

```text
---
```

## Continued Notes

When updating an existing topic, edit the Markdown source first and regenerate
the PDF. Do not treat the PDF as the editable source.

Preferred canonical pair:

```text
md/{topic-slug}-compact-note.md
pdf/{topic-slug}-compact-note.pdf
```

If an experimental version is needed, create a temporary `-v2` or date-stamped
copy, then promote the best result back to the canonical filename.

## Unit Finalization

For a folder such as `순환기/심부전`, final PDF cleanup happens after the unit has
absorbed the relevant Allen pages, KMLE concept material, and problem-solving
notes. Until then, keep drafts readable but do not compress them aggressively.

At finalization, review the rendered PDF as a whole and adjust:

- Section order and page-break placement.
- Heading spacing after tables and source-note boxes.
- Heading orphans, where a major heading appears alone at the bottom of a page
  and its table or first paragraph begins on the next page.
- Table widows, where only one or two final rows spill to the next page.
- Orphan pages with only a small leftover note.
- Excessive blank lower-page space when it harms review flow.

## Visual QA Checklist

- Korean text renders correctly.
- No table extends beyond page margins.
- No table row is clipped.
- Headings are visually distinct from body text.
- Drug tables remain readable.
- Font weight is not too heavy for paragraph reading.
- Section headings are not pressed tightly against preceding content.
- `Exam Traps and Active Recall` has clear separation from the preceding
  algorithm/table/source-note block.
- Page breaks do not leave a page containing only a small trailing note.
- Page count feels proportional to the amount of useful content; drafts may be
  shorter or longer than the final topic note.

## Source-Inspired Patterns

This project uses structural ideas from public Markdown note systems, including
metadata/front matter, active-recall Q&A sections, and PDF-aware page breaks.
Do not copy external templates verbatim into generated notes.
