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

Gold standard reference:

```text
outputs/notes/heart-failure-compact-note.md
outputs/pdf/heart-failure-compact-note.pdf
```

Use the latest canonical heart-failure compact note as the current quality baseline for future
disease notes. Match its overall pattern: integrated Allen/KMLE content,
first-page exam snapshot, disease-flow reasoning, compact concept bridges
placed immediately before the section that uses the concept, readable tables,
restrained color emphasis, drug names with naming patterns, source notes for
KMLE/external additions, and the `{system} > {unit}` title format. Section
headings such as `Disease Flow` and `Concept Bridge` should have visible
breathing room above them, especially after tables or source-note boxes.
`Exam Traps and Active Recall` should also keep normal major-section spacing
when it follows an algorithm, table, or source-note box; use reduced top spacing
only if the section starts at the top of a new page.

When expanding an Allen-based unit, always read and reflect the short overview
or editorial comment near the top of the Allen page. Use it to decide what the
page is really trying to teach and what is likely to matter for exam questions.
Do not turn every background concept into a long textbook section. If a basic
concept is not usually examined directly, mention only the minimum needed to
support diagnosis, treatment, or problem solving, then move on.

Top-level note/PDF titles should use the unit path format:

```text
{system} > {unit}
```

For example:

```text
순환기 > 심부전
```

Do not place a small version/subtitle line directly under the PDF title.
Version history belongs in the filename, front matter, source notes, or update
log.

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

Use integrated prose/tables when sources broadly agree. Do not split the main
note into rigid `[Allen]` and `[KMLE]` blocks if they are explaining the same
concept. The study flow should read like one coherent national-exam note.

Use visible labels only when a point is meaningfully source-specific:

```text
[KMLE 보강]        for KMLE-only concept additions or page-specific framing
[KMLE 문제 포인트] for KMLE question/explanation patterns
[외부 보강]        for guideline/reference additions not present in Allen/KMLE
[시험 재구성]      for Codex-generated exam rules, traps, or memory aids
```

Allen's Library is usually the base source for the current page, so do not label
every Allen-derived sentence. Instead, list the Allen page in `Source Notes`.
If Allen and KMLE say the same thing, merge the content and cite both in the
small source note below the section.

Use Allen's top overview/comment as the source-scope filter:

- Preserve exam-facing framing, common presentations, diagnostic habits, and
  "watch for this" comments.
- Keep non-exam background physiology/anatomy only when it explains a decision
  rule, classification, treatment choice, or common trap.
- Omit low-yield textbook detail that does not change the exam flow.
- If the user asks for deeper conceptual review, expand only that concept.

## Output Sections

For disease topics, preserve a clinical reasoning flow. The reader should be
able to follow:

```text
definition -> causes/risk factors -> pathophysiology -> symptoms/signs
-> diagnosis/tests -> treatment -> prevention/follow-up -> exam traps
```

When useful, include a compact `Disease Flow` table near the beginning:

```text
Cause/Risk -> Mechanism -> Clinical Clue -> Diagnostic Test -> Treatment
```

Use this order unless the topic clearly requires a different structure.

1. Metadata
2. Exam Snapshot
3. Disease Flow
4. Definition and core pathophysiology
5. Causes and risk factors
6. Symptoms and signs
7. Diagnosis and tests
8. Concept Bridge, placed just before the first section that depends on it
9. Differential diagnosis
10. Treatment algorithm
11. Drug table
12. Contraindications, cautions, complications, and prevention
13. National exam traps
14. Active Recall Q&A
15. Source Notes

## Concept Bridge Rule

When a classification, abbreviation, subtype, score, staging system, or named
syndrome changes diagnosis, testing, prognosis, treatment, or problem solving,
add a short `Concept Bridge` before the note relies on that concept.

Placement matters. Do not put every concept bridge immediately after `Disease
Flow` by default. Place it where the reader needs it: immediately before a
classification table, diagnostic algorithm, treatment algorithm, drug table, or
exam-trap section that would otherwise feel ungrounded. A brief mention in
`Exam Snapshot` or `Disease Flow` does not force an early bridge; those sections
may preview the concept, while the bridge should appear before sustained use.

The bridge should answer four questions:

```text
1. What is the classification based on?
2. What does each item mean?
3. Why does the distinction matter clinically or on exams?
4. What test, threshold, or clue confirms the distinction?
```

Keep it compact: usually 3-6 bullets or a small table. Do not add a bridge for
every familiar word. Use it for concepts that would otherwise make later drug
tables, algorithms, or exam traps feel ungrounded.

Examples:

- HFrEF/HFpEF: EF-based classification; systolic vs filling/diastolic problem;
  echo confirms; treatment evidence differs.
- STEMI/NSTEMI/UA: ECG and troponin-based ACS classification; reperfusion and
  antithrombotic strategy differ.
- DKA/HHS: ketosis/acidosis vs severe hyperglycemic dehydration; fluid,
  insulin, and potassium priorities differ.
- Asthma/COPD: variable/reversible obstruction vs chronic fixed obstruction;
  inhaler strategy and exacerbation clues differ.

## Drug Table Requirements

When drugs are relevant, include a table with:

```text
Drug/Class | Representative drugs | Name pattern | Effect | Mechanism | When to Use | Contraindications | Cautions | Major Adverse Effects
```

Representative drugs should include common generic names likely to appear in
questions. When a class has a recognizable naming pattern, include it in the
`Name pattern` column using parentheses, such as `(~sartan)`, `(~pril)`,
`(~dipine)`, `(~olol)`, `(~gliflozin)`, or `(~statin)`. If a class has no
useful pattern, write `none` or the key exception.

In rendered PDFs, use restrained color emphasis:

- Bold for important concepts, key decision rules, and must-remember drug
  patterns.
- Blue bold for especially high-yield or frequently tested points.
- Red for contraindications, "do not use" situations, or safety-stopping
  warnings.

Do not bold/color every cell. The table should still read as a clean study
table, not as a fully highlighted page.

Do not merge contraindications and adverse effects. They answer different
exam-style questions.

## Exam Focus Rules

- Highlight findings that move the diagnosis from vague symptom to specific
  disease.
- Preserve the disease flow: why it happens, how it presents, how it is
  confirmed, and how it is treated.
- Identify the test that confirms or classifies the diagnosis.
- Distinguish first-line treatment, add-on treatment, and emergency treatment.
- List "do not use" situations for important medications.
- Convert confusing points into decision rules.

## PDF Requirements

Do not force a fixed page count while a topic or unit is still being expanded.
Let the note length grow naturally as related Allen pages, KMLE concept
sections, problem explanations, drug tables, and external reinforcements are
added.

For draft or partial notes, prioritize clean section spacing, readable tables,
and clear source labels over page-count compression. Layout cleanup should be
done at the unit-level finalization step, after the relevant Allen/KMLE/problem
content for that unit has been gathered. At that point, tighten obvious wasted
space and remove awkward orphan pages, but do not delete useful study content
merely to hit a target page count.

Suggested layout:

1. Page 1: exam snapshot and core disease script
2. Page 2: diagnosis, tests, and differential diagnosis
3. Page 3: treatment algorithm and drug table
4. Page 4: contraindications, exam traps, active recall

Use page-break markers in Markdown when the note becomes visually crowded or
when a section should start as a new review unit:

```text
---
```

When rendering the PDF, avoid dense prose blocks. Prefer short bullets, compact
tables, and section boxes. The final PDF should be easy to scan in 5-10 minutes.
Headings should have enough vertical space to be visually distinct from the
previous table or paragraph.

Before delivering a PDF, verify:

- Korean text renders correctly.
- Tables fit within page width.
- No row text is clipped.
- Disease-flow and core tables are readable without zooming excessively.
- Dense drug tables include representative names/patterns but remain legible.
- Drug contraindications and adverse effects are separated.
- The first page can stand alone as a rapid review card.
- No heading is pressed tightly against the previous section.
- No page contains only a tiny trailing source note unless that is intentional.

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

## Unit Finalization Rule

Treat each folder such as `순환기/심부전` as a living unit note. While adding
multiple Allen pages, KMLE concept sections, or KMLE problem explanations, keep
appending and merging into the Markdown source without obsessing over final PDF
pagination.

Only when the unit is being finalized should the agent polish the PDF layout:

- Reorder sections if the study flow is clearer.
- Add or remove page breaks for natural review units.
- Ensure bold section headings have enough spacing above them.
- Keep `Exam Traps and Active Recall` visually separated from the preceding
  table/algorithm/source-note block.
- Avoid pages that contain only a short trailing note or source box.
- Keep page count proportional to useful content, not to a fixed target.

Do not append directly to a PDF as the primary workflow. PDFs are treated as
rendered outputs; Markdown is the editable working file.
