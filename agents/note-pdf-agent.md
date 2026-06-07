# Agent: National Exam Compact Note PDF

## Mission

Create a compact national-exam-oriented study note from an Allen's Library
theory page and prepare it for PDF output.

This agent does not copy the source page. It restructures the topic into a
high-yield disease or concept note.

## Best Used For

- Disease overview pages
- Diagnosis and treatment pages
- Drug-heavy topics
- Exam-prep review before solving questions
- Creating a short PDF to review later

## Required Inputs

- Page title
- Page URL
- Main topic or disease name
- Source text or visible page contents

Optional KMLE source:

- Matching KMLE system PDF from `docs/kmle-source-map.md`
- Topic-specific KMLE section text, if available

Optional:

- User's current level of confidence
- Desired PDF length
- Specific focus, such as drugs, diagnosis, differential diagnosis, or treatment

## Template Basis

Use `templates/compact-exam-note.md` as the preferred Markdown structure for
new PDF notes.

The template is adapted from common Markdown study-note patterns:

- Metadata/front matter for source, system, topic, and storage location
- Compact first-page summary for fast review
- Table-heavy sections for diagnosis, treatment, and drugs
- Active-recall Q&A at the end
- Explicit page-break markers for PDF layout control

Do not copy external templates verbatim. Use them only as structural inspiration.

## Source Priority

Use sources in this order:

1. Allen's Library current theory page
2. Matching KMLE textbook section for the same system/topic
3. External guideline or standard medical reference, only when needed
4. Codex exam-oriented restructuring

KMLE must be scoped to the same topic. Do not summarize an entire KMLE system
PDF or import unrelated KMLE sections.

Use visible labels when mixing source types:

```text
[Allen 이론]
[KMLE 개념]
[KMLE 문제 포인트]
[외부 보강]
[시험 재구성]
```

## Output Sections

Use this order unless the topic clearly requires a different structure.

1. Metadata
2. Exam Snapshot
3. Core Disease Script
4. Diagnosis and Tests
5. Treatment Algorithm
6. Drug Table
7. Contraindications and Cautions
8. Differential Diagnosis
9. National Exam Traps
10. Active Recall Q&A
11. Source Notes

## Drug Table Requirements

When drugs are relevant, include a table with:

```text
Drug/Class | Effect | Mechanism | When to Use | Contraindications | Cautions | Major Adverse Effects
```

Do not merge contraindications and adverse effects. They answer different
exam-style questions.

## Exam Focus Rules

- Highlight findings that move the diagnosis from vague symptom to specific
  disease.
- Identify the test that confirms or classifies the diagnosis.
- Distinguish first-line treatment, add-on treatment, and emergency treatment.
- List "do not use" situations for important medications.
- Convert confusing points into decision rules.

## PDF Requirements

The preferred PDF is 2-4 pages per disease or topic.

Suggested layout:

1. Page 1: exam snapshot and core disease script
2. Page 2: diagnosis, tests, and differential diagnosis
3. Page 3: treatment algorithm and drug table
4. Page 4: contraindications, exam traps, active recall

Use page-break markers in Markdown when the note is long:

```text
---
```

When rendering the PDF, avoid dense prose blocks. Prefer short bullets, compact
tables, and section boxes. The final PDF should be easy to scan in 5-10 minutes.

Before delivering a PDF, verify:

- Korean text renders correctly.
- Tables fit within page width.
- No row text is clipped.
- Drug contraindications and adverse effects are separated.
- The first page can stand alone as a rapid review card.

## Final Output

Create a Markdown note first. If requested, render it as PDF.

Temporary or repo-local outputs may be saved under:

```text
outputs/pdf/
```

Also save the Markdown version under:

```text
outputs/notes/
```

## iCloud Storage Rule

Final personal study notes should also be copied to iCloud Drive using this
system/topic hierarchy:

```text
~/Library/Mobile Documents/com~apple~CloudDocs/Study Assistant/Notes/{system}/{topic}/
```

Examples:

```text
Study Assistant/Notes/순환기/심부전/
Study Assistant/Notes/호흡기/COPD/
Study Assistant/Notes/소화기/간경변/
```

Inside each topic folder, keep PDF and Markdown files in separate subfolders:

```text
Study Assistant/Notes/{system}/{topic}/pdf/{topic-slug}-compact-note.pdf
Study Assistant/Notes/{system}/{topic}/md/{topic-slug}-compact-note.md
```

If the system or topic is unclear, infer it from the Allen's Library breadcrumb,
page title, or table of contents. If still uncertain, ask the user before saving.

Suggested system folder names include:

```text
순환기, 호흡기, 소화기, 신장, 내분비, 감염, 혈액종양, 류마티스,
신경, 정신, 소아, 산부인과, 외과, 응급, 예방의학, 의료법규
```

## Continuation Rule

If a note for the same `{system}/{topic}` already exists, continue from the
existing Markdown source instead of creating a completely separate note.

Use the Markdown file as the source of truth:

```text
Study Assistant/Notes/{system}/{topic}/md/{topic-slug}-compact-note.md
```

Then regenerate the PDF from that updated Markdown:

```text
Study Assistant/Notes/{system}/{topic}/pdf/{topic-slug}-compact-note.pdf
```

Recommended workflow:

1. Check whether a matching topic folder already exists in iCloud.
2. If an existing Markdown source exists, read it first.
3. Merge new Allen/KMLE/source material into the relevant sections.
4. Preserve the existing structure unless it is clearly broken.
5. Update `Source Notes` and, when useful, add a short `Update Log` entry.
6. Re-render the PDF with the same canonical filename.

Versioned files such as `-v2` or date-stamped copies may be created for
experiments, but the topic folder should keep one canonical latest file:

```text
{topic-slug}-compact-note.md
{topic-slug}-compact-note.pdf
```

Do not append directly to a PDF as the primary workflow. PDFs are treated as
rendered outputs; Markdown is the editable working file.
