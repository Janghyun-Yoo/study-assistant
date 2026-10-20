# PDF Rendering Guide

Use this guide when converting Markdown study notes into PDF.

## Layout Principles

- The first page should work as a standalone rapid-review card.
- Use the top title format `{system} > {unit}`, such as `순환기 > 심부전`.
- Do not place a version/subtitle line directly under the top PDF title.
- Keep paragraphs short. Prefer bullets and tables.
- Use tables for diagnosis, differential diagnosis, drugs, contraindications,
  and exam traps.
- Avoid over-wide first columns when they contain short labels. For every table,
  choose widths by column role and average text length. In tables such as
  `Exam Snapshot`, `Disease Flow`, `Diagnosis and Tests`, and drug tables, keep
  label columns compact and give more width to explanation-heavy columns.
- In 2-column `Field`/answer tables, the first column should usually be about
  one quarter of the table width. If a column repeatedly wraps awkwardly,
  compress wording, add semantic `<br/>` breaks, or split/reshape the table.
- In `Field / High-Yield Answer` tables, when an answer has `label = long
  component list` plus a trailing safety, trigger, or trap note, prefer explicit
  breaks as `label<br/>= components<br/>→ note` so the label, component list,
  and follow-up note remain visually distinct instead of wrapping after a
  semicolon.
- In compact drug anchor tables with `Class / Representative drugs / Exam Use /
  Watch`, reserve extra width for `Exam Use`, because add-on trigger lines are
  the answer key. Useful suffix patterns belong in the `Class` cell, not in a
  new column.
- In `Step / Flow / Cue` tables such as `Disease Flow`, the `Step` column should
  be the narrowest column, with enough width reserved for `Exam Cue` to avoid
  one- or two-word trailing wraps.
- In `Pattern / Mechanism Flow / Dominant Clues / Exam Move` tables, keep
  `Pattern` compact and avoid over-widening `Mechanism Flow`; reserve enough
  width for `Dominant Clues` so clinical chunks such as `CXR 폐부종` do not
  leave `폐부종` alone on the final line. A useful preset is near `18 / 29 / 30
  / 23`.
- Table-width presets are starting points, not final answers. Prefer the nearby
  optimized width that minimizes orphan final lines such as `있음`, `가능`,
  `단서`, `후보`, or clinical findings such as `폐부종` before adding manual
  `<br/>` breaks.
- The renderer may reduce table text by up to 0.4 pt when width optimization
  alone cannot prevent one-word or short two-token final lines such as `상승`,
  `확인`, `AF 단서`, or `폐정맥압 상승`. If those still remain, report a layout
  warning instead of hiding the issue.
- Short Korean suffix fragments such as `축`, `군`, `형`, `류`, `계`, `증`, `병`,
  `염`, `법`, `술`, `제`, `약`, `원인`, and `질환` should not land alone in
  table cells, including lines created by explicit `<br/>`.
- Semantic chunks inside table cells should stay together. Prefer moving
  phrases such as `→ RV failure`, `→ ↑systemic venous pressure`,
  `diltiazem exception`, `폐정맥압 상승`, `RV-PVR 축`, or `원인 질환` to the next
  line as a unit rather than splitting the phrase across lines.
- Compact tables may use study symbols to shorten lines: `↑` for increase/rise,
  `↓` for decrease/low/reduced function, `O` for present/with, `X` for
  standalone absent/not-applied status, `+` for positive, and `−` for negative.
  Verify that these glyphs render correctly in the embedded PDF font. Do not
  use `X` to replace natural-language action guidance such as `~없이`,
  `~하지 않기`, `피하기`, `금지`, `주의`, or `아님`; avoid symbol-only wording for
  contraindications or red-bold safety warnings.
- Visual-anchor interpretation tables using
  `What to Look For / Exam Cue / Common Trap` should reserve enough space for
  the first column's pattern findings; the renderer preset should stay near
  `38 / 30 / 32`.
- For concept-bridge or comparison tables where the first column carries
  bilingual concept labels, split the label with `<br/>`, such as
  `폐동맥고혈압<br/>(PAH)`, and keep the first column only wide enough for that
  two-line label. Give the saved width to mechanism/core-concept columns so
  causal chains do not wrap awkwardly.
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
- For `Algorithm Review Map`, `Visual Anchor`, and other figure-based sections,
  treat the heading, subheading, and first image or interpretation table as one
  review block. Do not leave an algorithm/visual heading orphaned above a page
  break while the image starts on the next page.
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
- Allen contraindications, "do not use" medications, disease-worsening drug
  classes, or safety-stopping conditions that are likely exam choices should be
  red bold in the final PDF. Mark only the avoid phrase or drug class, not the
  whole row.
- In subtype-split table cells, bold only the branch label at the start of each
  line, such as `좌심부전:` or `ADHF/폐부종:`, so the split is scannable without
  making the whole cell visually heavy.
- When source-summary items use different clinical axes, render them as
  separate branch lines rather than slash-merged labels; for example, separate
  `저박출` symptoms from `청진` findings.
- Keep source notes with the table, figure, or paragraph they document. Avoid
  a short `출처:` line orphaned at the top of the next page; it is acceptable to
  use smaller source-note text or move the preceding block with the note.
- For short section-opening prose, prefer one review sentence per line using
  `<br/>` when each sentence can fit on one line. Leave naturally wrapping long
  sentences alone.
- Add images only when they improve recognition or problem solving. For ECG,
  CXR, CT/MRI, ultrasound, dermatology, ophthalmology, pathology, and endoscopy
  topics, use a compact `Visual Anchors` section with 1-3 representative images
  and short interpretation notes.
- Clinical images and ECG strips should be exact crops from the user's source
  page, PDF, screenshot, or image file. Do not redraw, regenerate, or
  stylistically reinterpret them.
- Allowed image edits are limited to cropping, resizing, rotation correction,
  and gentle brightness/contrast cleanup. Avoid labels, circles, arrows, or
  overlays unless the user explicitly asks for an annotated copy.
- If the image source is unavailable, leave a `원본 crop 필요` placeholder and
  keep the visual interpretation in the table below it.
- When the image is rendered above the table, omit any redundant `Image` column
  from the interpretation table. The table should start with `What to Look For`
  or a similar interpretation column.
- If multiple screenshots, source crops, or photos duplicate the same finding or
  algorithm, render only the clearest one. Prefer the version that stays legible
  at PDF scale and reduces visual clutter.
- Use an `Image` table column only if images are actually embedded inside table
  cells. The current compact-note renderer normally renders images as separate
  blocks, so most visual-anchor tables should be 3-column interpretation tables.
- Keep each visual anchor close to the diagnosis, test, or differential section
  that uses it. Avoid collecting many images at the end of the note.
- Use Markdown image syntax on its own line:

```text
![Short descriptive alt text](path/to/image.png)
```

- Prefer local image paths that the renderer can access. If a path contains
  spaces, wrap it in angle brackets:

```text
![ECG showing atrial flutter](</absolute/path/Study Assets/ecg/flutter.png>)
```

- For compact-note PDFs, image width should fit the text frame and height should
  usually stay under about one third of a page. Add interpretation bullets or a
  small table below the image instead of relying on the image alone.
- Algorithm review maps are an exception: fit them as large as needed for
  readability, usually up to about one half of a page. If the text inside the
  algorithm becomes too small, split the crop into two logical parts.
- Place algorithm review maps near the end of the relevant unit or immediately
  after the reconstructed treatment/diagnostic section. The crop is for final
  structural review; the note should still contain a compact exam-oriented table
  or flow before the original source map.

## Font

Preferred Korean PDF font:

```text
Pretendard
```

The compact-note renderer should first look for bundled project fonts in:

```text
assets/fonts/
```

This project expects these TrueType files there when producing canonical PDFs:

```text
Pretendard-Regular.ttf
Pretendard-Medium.ttf
Pretendard-SemiBold.ttf
```

Keeping the fonts in the repo makes PDF output reproducible even when the local
macOS user font folder does not have Pretendard installed.

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
Study Assistant/Notes/{system}/{topic}/md/{topic}.md
Study Assistant/PDFs/{system}/{topic}.pdf
```

If an experimental version is needed, create it in temporary local output or in
the topic `_archive` folder. Do not leave date-stamped or cache-busting PDFs in
the active `Study Assistant/PDFs/{system}/` folder.

## Unit Finalization

For a folder such as `순환기/심부전`, final PDF cleanup happens after the unit has
absorbed the relevant Allen pages, KMLE concept material, and problem-solving
notes. Until then, keep drafts readable but do not compress them aggressively.

At finalization, review the rendered PDF as a whole and adjust:

- Section order and page-break placement.
- Heading spacing after tables and source-note boxes.
- Heading orphans, where a major heading appears alone at the bottom of a page
  and its table or first paragraph begins on the next page.
- Image/algorithm orphans, where a review-map or visual-anchor heading appears
  on one page but the first image or interpretation table begins on the next.
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
- Algorithm/visual headings stay with the first image or interpretation table
  they introduce.
- `Exam Traps and Active Recall` has clear separation from the preceding
  algorithm/table/source-note block.
- Page breaks do not leave a page containing only a small trailing note.
- Page count feels proportional to the amount of useful content; drafts may be
  shorter or longer than the final topic note.

## Source-Inspired Patterns

This project uses structural ideas from public Markdown note systems, including
metadata/front matter, active-recall Q&A sections, and PDF-aware page breaks.
Do not copy external templates verbatim into generated notes.
