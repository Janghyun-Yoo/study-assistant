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
disease notes. Match its overall pattern: Allen-first integrated content,
first-page exam snapshot, disease-flow reasoning, compact concept bridges
placed immediately before the section that uses the concept, readable tables,
restrained color emphasis, drug names with naming patterns, source notes for
KMLE/external additions, optional visual anchors for visually diagnosed topics,
optional algorithm review maps for source algorithms, and the `{system} >
{unit}` title format. Section
headings such as `Disease Flow` and `Concept Bridge` should have visible
breathing room above them, especially after tables or source-note boxes.
Tables should allocate width according to content: short label columns such as
`Field`, `Step`, `Test`, `Category`, `Class`, `Item`, `Pattern`, `Situation`,
and `Cause Group` should be compact, while explanation-heavy columns such as
`High-Yield Answer`, `Core Concept`, `Mechanism`, `Mechanism Flow`, `Role`,
`Better Rule`, and `Treatment Anchor` should get the extra width. If a column
repeatedly wraps awkwardly, compress the wording, add semantic `<br/>` breaks,
or split/reshape the table instead of accepting a cramped PDF table.
For `Test / Use / Expected Finding / Exam Trap` tables, treat `Use` as compact
when it only gives short purpose labels. Prioritize width for `Expected Finding`
when it carries imaging/lab finding lists; use semantic breaks in `Exam Trap`
before letting trap text squeeze finding phrases.
When a recurring table shape becomes part of the gold standard, mirror its
column-role intent in the PDF renderer's table-width presets or fallback rules.
Treat those presets as starting points: during PDF rendering, prefer a nearby
optimized width that avoids one- or two-word orphan final lines such as `있음`,
`가능`, `단서`, or `후보` before adding manual `<br/>` breaks.
In clinical clue columns such as `Dominant Clues`, `Clinical Clues`, `Finding`,
and `Exam Cue`, keep clinical finding chunks together. Phrases such as
`CXR 폐부종`, `JVP↑`, `하지부종`, and `전신정맥 울혈` should not split so that a
short finding such as `폐부종` lands alone on a line. Prefer column width
redistribution before adding manual `<br/>` breaks.
In `Expected Finding` and other finding-list columns, preserve English clinical
phrases such as `alveolar edema`, `vascular congestion`, `pulmonary edema`,
`severe valve disease`, `coronary artery disease`, and
`structural heart disease`. First try column-width redistribution so the full
list stays on one line; if that cannot work, move the whole phrase to the next
line rather than leaving only `edema`, `congestion`, or `disease`.
The renderer may reduce table text by up to 0.4 pt to avoid one-word or short
two-token final lines such as `상승`, `확인`, `AF 단서`, `폐정맥압 상승`, `edema`,
`congestion`, or `disease`.
If those remain after optimization, treat the console layout warning as a sign
that the table may need wording, semantic breaks, or reshaping.
Also preserve semantic chunks inside table cells: phrases such as
`→ RV failure`, `→ ↑systemic venous pressure`, `diltiazem exception`, and
`폐정맥압 상승` should move to the next line as a unit rather than splitting in
the middle. Short Korean suffix fragments such as `축`, `군`, `형`, `류`, `계`,
`증`, `병`, `염`, `법`, `술`, `제`, `약`, `원인`, and `질환` should not land alone
in table cells; keep labels such as `RV-PVR 축`, `폐혈관 축`, and `원인 질환`
together. Standalone clinical acronyms such as `MCS`, `IABP`, `LVAD`, and
`ECMO` should not be left alone on the final line of an action cell; attach them
to an action word such as `MCS 고려` or adjust table width.
Keep add-on/modifier operators with the following item. In treatment cells, `±`
belongs with the optional add-on, not with the preceding line. If the phrase
wraps, write it intentionally as `anchor treatment<br/>± add-on treatment`, such
as `norepinephrine으로 perfusion pressure 확보<br/>± dobutamine/milrinone`.
Short device/procedure action chunks such as `MCS 고려`, `ECMO 고려`,
`IABP 고려`, `LVAD 고려`, `PCI 고려`, and `CABG 고려` should also not sit alone as
accidental final lines. Keep the trigger plus action together when possible,
such as `refractory면 MCS 고려`; if the action is intentionally separated, make it
a complete branch line such as `Escalation: refractory shock → MCS 고려`.
For dense cause-to-result phrases in table cells, prefer breaking before the
arrow when the cause/entity is long and the result is a list:
`cause/entity<br/>→ consequence list`. Example:
`papillary muscle rupture<br/>→ acute MR, VSD, free wall rupture/tamponade`.
For `Step / Flow / Cue` tables such as `Disease Flow`, make the `Step` column
the narrowest column. Give the saved width to the column carrying the longest
decision logic; when semantic breaks make `Exam Cue` comfortable, prioritize
`High-Yield Flow` so treatment/mechanism lines do not strand short action
chunks.
`Exam Traps and Active Recall` should also keep normal major-section spacing
when it follows an algorithm, table, or source-note box; use reduced top spacing
only if the section starts at the top of a new page.

When expanding an Allen-based unit, always read and reflect the short overview
or editorial comment near the top of the Allen page. Use it to decide what the
page is really trying to teach and what is likely to matter for exam questions.
Do not turn every background concept into a long textbook section. If a basic
concept is not usually examined directly, mention only the minimum needed to
support diagnosis, treatment, or problem solving, then move on.

Allen is the skeleton; KMLE is the selective reinforcement. For concept and
disease explanation, aim for roughly Allen 80% and KMLE 20% by following Allen's
overview, summary table, and section order first, then adding only KMLE material
that fills a genuine gap or sharpens a national-exam decision. For exam
tendency, common traps, and active recall, KMLE can carry about half the weight.
Do not let KMLE treatment algorithms, long drug lists, or guideline-style
details dominate the early disease script; keep those as compact treatment
anchors, traps, or late `Algorithm Review Map` review material.

When a KMLE reinforcement point uses a compressed term, guideline abbreviation,
or algorithm label such as `4 pillars`, `GDMT`, or `device trigger`, expand it
at first use in one short phrase. Do not write only "see treatment/trap later";
show the core components or definition first, then defer detailed indications,
exceptions, or safety notes to treatment, traps, or active recall.
In early `Exam Snapshot`/summary tables, if that expansion takes the form
`label = long component list` followed by a safety, trigger, or trap note, use
semantic line breaks: `label<br/>= components<br/>→ note`. For example:
`HFrEF 예후 개선 4축(4 pillars)<br/>= ARNI/ACEi/ARB + evidence BB + MRA + SGLT2i<br/>→ MRA 안전성, CRT/ICD trigger는 treatment/trap에서 확인`.

When Allen flags contraindications, "do not use" medications, disease-worsening
drug classes, or safety-stopping conditions that are important exam choices,
make only the key avoid phrase red bold with
`<span style="color:#B91C1C">**...**</span>`. Do not color the full sentence or
entire table row.

Keep source notes visually attached to the block they document. If a short
`출처:` note would land alone on the next page, reduce source-note size or move
the preceding table/figure/paragraph with it. Source notes may be smaller than
body text.

For section-opening prose, use `<br/>` to put each short sentence on its own
review line when several short sentences would otherwise run together. Do not
force manual breaks into long sentences that already wrap naturally.

## Visual Anchor Rule

Use images selectively when visual pattern recognition is itself a tested skill.
Do not add images to every disease note by default. Add a short `Visual
Anchors` section only when the image changes exam reasoning, diagnosis, or
memory more than another paragraph would.

High-value image categories:

- ECG strips for arrhythmia, ACS, chamber enlargement, electrolyte changes, and
  other ECG-first diagnoses.
- CXR, CT, MRI, ultrasound, angiography, and nuclear imaging when the imaging
  pattern is a common exam clue.
- Dermatology, ophthalmology, pathology gross/micro, endoscopy, and procedural
  images when recognition matters.

Image fidelity rule:

- For clinical images, ECG strips, CXR, CT, MRI, ultrasound, endoscopy,
  pathology, dermatology, and ophthalmology, do not redraw, regenerate, or
  stylistically reinterpret the finding.
- Prefer an exact crop from the user's source page, PDF, screenshot, or
  user-provided image file. Preserve the diagnostic content as-is.
- Allowed edits are limited to cropping, resizing, rotation correction, and
  gentle brightness/contrast cleanup when readability improves without changing
  the finding.
- Do not add arrows, circles, labels, or overlays onto the image unless the user
  explicitly asks for an annotated copy. Put interpretation in the note below
  the image instead.
- If the source image is unavailable, leave a clear `원본 crop 필요` placeholder
  and write the interpretation table from the source text; do not fabricate a
  substitute image.

Keep visual anchors compact:

- Usually 1-3 images per unit note.
- Place the image near the section where the pattern is used, not automatically
  at the end.
- Under each image, add 2-4 concise bullets or a small table covering what to
  look for, the exam cue, the key differential, and the trap.
- If the image is placed outside the table, do not include a redundant `Image`
  column in the interpretation table. Use columns such as `What to Look For`,
  `Exam Cue`, and `Common Trap`.
- For `What to Look For / Exam Cue / Common Trap`, treat `What to Look For` as
  a pattern-finding column, not a short label column; keep it wide enough for
  visual signs and use the renderer preset near `38 / 30 / 32`.
- Use an `Image` column only when the image itself is embedded inside a table
  cell; otherwise it wastes space and repeats the visible image.
- If the note already risks becoming too long, prefer one representative image
  plus a high-yield interpretation table over many similar images.
- If multiple screenshots, source crops, or photos show substantially the same
  finding or algorithm, choose only the clearest one. Prefer the version that is
  concise, legible at PDF scale, and directly useful for exam review. Keep both
  only when they serve different review tasks.
- Do not use decorative or generic stock images.

Source and storage rules:

- Avoid committing copyrighted Allen/KMLE images to the repository.
- Prefer user-owned local crops from personal study sources or
  public-domain/open-license medical images.
- Store reusable local note images outside the code repo or in a clearly
  personal, non-committed study-assets folder; reference them with Markdown image
  syntax only when the PDF renderer can access the file.
- Always include a short source note or attribution when an external image is
  used.

## Algorithm Review Map Rule

Use `Algorithm Review Maps` for source algorithms that are useful as a final
one-glance review of the whole decision structure. This is separate from
`Visual Anchors`: visual anchors train pattern recognition, while algorithm
review maps preserve the original treatment or diagnostic pathway for review.

Good candidates:

- KMLE or guideline treatment algorithms.
- Diagnostic algorithms with branching decisions.
- Large flowcharts where the spatial layout helps recall the sequence.

Use source crops, not regenerated diagrams:

- Crop the whole algorithm from the local PDF, screenshot, or user-provided
  source image.
- Do not redraw or restyle the algorithm.
- If the algorithm is too large to read on one PDF page, split it into two
  logical crops rather than shrinking it until unreadable.
- If a user-provided screenshot or simplified crop covers the same algorithm
  with better readability than a busy KMLE/source crop, use the clearer visual
  and omit the duplicate source crop from the PDF.
- Place the review map near the end of the relevant unit or immediately after
  the reconstructed treatment/diagnostic section.
- Add a short interpretation table below it with the key branch points, exam
  move, and trap. Do not rewrite every box from the image.
- For KMLE crops, keep them in personal local outputs and avoid committing them
  to public Git history.

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

When Allen and KMLE differ in emphasis, let Allen decide the main note outline.
Use KMLE to add missing high-yield classifications, cutoff values, treatment
updates, and problem-answering traps. If a KMLE point is useful but bulky, move
it to `Exam Traps and Active Recall`, a compact treatment anchor, or an
`Algorithm Review Map` instead of expanding the core disease explanation.

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
definition → causes/risk factors → pathophysiology → symptoms/signs
→ diagnosis/tests → treatment → prevention/follow-up → exam traps
```

When useful, include a compact `Disease Flow` table near the beginning:

```text
Cause/Risk → Mechanism → Clinical Clue → Diagnostic Test → Treatment
```

If a topic mixes multiple clinically important subtypes, directions, or
parallel mechanisms, split the flow instead of writing one blended mechanism.
Each subtype should have its own short causal chain when it leads to different
symptoms, tests, treatment choices, or exam traps. For heart failure, distinguish
left-sided and right-sided flows:

```text
**좌심부전:** LV dysfunction → ↓CO + ↑LV filling pressure → pulmonary congestion<br/>**우심부전/폐혈관 축:** RV dysfunction or ↑PVR → ↑systemic venous pressure → JVP/edema/hepatomegaly
```

Apply the same rule to mixed entities such as left/right disease,
forward/backward failure, obstructive/restrictive patterns, acute/chronic forms,
or classification groups that change clinical reasoning.

This is a whole-note organization rule, not just a `Disease Flow` rule. Once a
meaningful subtype or mechanism split is introduced, carry that split through
the later pathophysiology, clinical signs, diagnostic approach, treatment flow,
exam traps, and active recall questions whenever it changes reasoning. The note
should not separate mechanisms in the first table and then collapse them back
into a generic paragraph or treatment list.

Formatting matters. When multiple branches appear inside one table cell, put
each branch on its own line using `<br/>`. Avoid semicolon-only or sentence-only
separation for subtype chains, because it becomes hard to scan in the PDF.
For `Disease Flow`, prefer compact line-based summaries over complete sentences.
Each line should read like a decision card: `test/action → purpose` or `branch
label: key items`. Preserve Allen summary coverage, but compress it into
scannable steps rather than prose.
Bold only the subtype/branch label or mechanism starter at the start of each
branch line, then keep the causal chain or explanation in regular weight unless
it deserves separate high-yield emphasis. In pathophysiology rows with several
directions, bold each starting driver, such as `**↓contractility**` or
`**↑LV filling pressure**`.
Do not merge clinically different axes into one slash label when importing an
Allen summary into `Disease Flow`; split items such as `저박출` symptoms and
`청진` findings into separate branch lines.
Use actual arrow symbols (`→`) for causal flows instead of ASCII `->`.
When a long cause/entity points to a consequence list in a narrow table cell,
insert `<br/>` before `→` so the arrow begins the result line.
Use compact symbols in table cells and exam-cue lines when they shorten the row
without making it cryptic:

- `↑`: increase/rise/high/expansion
- `↓`: decrease/low/reduced function
- `O`: present/with
- `X`: standalone absent/not-applied state marker
- `+`: positive
- `−`: negative
- `→`: cause/effect, test/purpose, treatment/effect

If a profile/classification cue wraps awkwardly or leaves an orphan, make the
structure explicit with semantic breaks, e.g.
`KMLE profile:<br/>warm-wet은 diuretic/vasodilator,<br/>cold-wet은 shock 처치`.
After adding semantic chunk protection or manual `<br/>` in one table cell,
re-check the whole table's column widths. Reject width candidates that fix one
cell but create a new orphan elsewhere, such as `방향 확인`, `강화`, `edema`,
`congestion`, or `disease`.
If a conditional clinical cue would likely render as two lines, split after the
condition marker instead of accepting a random wrap:
`condition<br/>clinical decision/action`, e.g.
`MI 뒤 호흡곤란/저혈압이면<br/>ACS + mechanical complication을 같이 본다`.
Apply this rule across all cue/trap/decision table cells, including `Exam Cue`,
`Exam Trap`, `Common Trap`, `Better Rule`, `Watch`, `Exam Move`, and active
recall `Answer`. Prefer `새 murmur + shock이면<br/>mechanical complication` over
an accidental split inside the decision phrase such as `mechanical` /
`complication`.
For non-condition evidence cues, use `context/evidence<br/>interpretation`, e.g.
`"저혈압"보다 organ hypoperfusion 단서가<br/>shock을 강화`.
When a long caveat, risk, or result clause follows `;` or a clause-separating
comma in a table cell, split after the punctuation if the second clause would
wrap: `primary point;<br/>secondary caveat` or `selected indication,<br/>major
risk`. Keep short simple lists such as `A, B, C` inline.

Prioritize shorthand in `Exam Snapshot`, `Disease Flow`, `Treatment Flow`,
drug/test/trap tables, and active-recall answers. Avoid over-shortening
definitions, source notes, dosing, contraindications, or red-bold safety
warnings; do not replace an important "avoid/contraindicated" phrase with only
`X`.
Use `X` only for compact status phrases like `edema X`, `DM X`, or `적응증 X`
when the cell is marking absence/not-applied status. Do not replace
natural-language instructions such as `~없이`, `~하지 않기`, `피하기`, `금지`,
`주의`, or `아님`; `Watch`, `Trap`, and `Exam Point` cells should keep action
guidance readable.

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

Before moving past the first draft, compare Allen's top overview and compact
summary table against the early note. Every summary item should be represented
in `Exam Snapshot`, `Disease Flow`, or an adjacent early summary table. Later
drug, diagnosis, or trap tables can expand the point, but they do not replace
the early coverage signal. For treatment summaries, explicitly account for
lifestyle correction, chronic first-line therapy, phenotype-specific treatment,
add-on/device options, and acute treatment framing when present.
For `Disease Flow`, first convert Allen's compact summary table into a coverage
checklist: causes/risk factors, clinical clues, diagnosis/tests, and treatment
branches. Map each checklist item into the row where it changes problem solving,
using compact `<br/>` decision lines rather than copying the source table. If
that would make the flow too crowded, keep the decision axis in `Disease Flow`
and add a small adjacent early summary table immediately below it.

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

If the classification, score, stage, severity grade, lab result, or imaging
criterion has concrete cutoff values, include those numbers in the bridge. Do
not write only qualitative labels such as "reduced", "preserved", "positive",
"severe", or "high-risk" when the source gives a threshold. For EF-based heart
failure classification, write `HFrEF: LVEF ≤40%`, `HFmrEF: 41-49%`, and
`HFpEF: ≥50% + evidence of increased filling pressure`.

When introducing major concept terms in a concept bridge, classification table,
or comparison table, put the bilingual label in the leftmost row-label column
(`Item`, `Pattern`, `Cause Group`, `Situation`, etc.). Prefer Korean +
abbreviation to keep tables readable, and place the English/abbreviation on the
next line with `<br/>`, e.g. `박출률 감소 심부전<br/>(HFrEF)`,
`폐고혈압<br/>(PH)`, `폐동맥고혈압<br/>(PAH)`, and
`폐성심<br/>(cor pulmonale)`. Keep the explanation cells focused on criteria,
mechanisms, and exam cues instead of repeating full English names. In prose
definitions, write the Korean term with the standard English term or
abbreviation in parentheses on first use, then use the compact Korean or
abbreviated form afterward.

Keep it compact: usually 3-6 bullets or a small table. Do not add a bridge for
every familiar word. Use it for concepts that would otherwise make later drug
tables, algorithms, or exam traps feel ungrounded.

Examples:

- HFrEF/HFmrEF/HFpEF: EF-based classification with cutoffs; HFrEF LVEF ≤40%,
  HFmrEF 41-49%, HFpEF ≥50% plus filling-pressure evidence; echo confirms;
  treatment evidence differs.
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

For compact `Drug Anchor Table` formats that do not have a `Name pattern`
column, put useful patterns directly in the `Class` cell, such as
`ACEi (~pril)`, `ARB (~sartan)`, `BB (~lol)`, or `SGLT2i (~gliflozin)`. Do not
add an extra pattern column to a compact anchor table just for suffixes.

For `Add-on`, `2nd line`, `selected`, `consider`, or `필요시` drugs, the
`When to Use` or `Exam Use` cell must state the trigger that makes the drug the
answer. Do not leave only "selected patient" or "선별 환자에서 보조". If several
drugs are grouped in one row, write `drug: trigger` on separate `<br/>` lines;
split the row if the triggers are too different. Keep `Watch` for
contraindications, cautions, and traps rather than indications.

Do not mix device/procedure triggers into a drug row. Put CRT, ICD, transplant,
ablation, procedures, or devices in treatment flow or a separate trigger table
with the clinical clue that selects them.

In rendered PDFs, use restrained color emphasis:

- Bold for important concepts, key decision rules, and must-remember drug
  patterns.
- Blue bold for especially high-yield or frequently tested points.
- Red for contraindications, "do not use" situations, or safety-stopping
  warnings.
- Red bold for Allen contraindications/avoid-list items that are likely to be
  tested as exam choices.

Do not bold/color every cell. The table should still read as a clean study
table, not as a fully highlighted page.

Do not merge contraindications and adverse effects. They answer different
exam-style questions.

## Exam Focus Rules

- Highlight findings that move the diagnosis from vague symptom to specific
  disease.
- Keep short table label columns compact and reserve more width for mechanism,
  diagnostic reasoning, treatment logic, and exam-trap explanations. In
  2-column `Field`/answer tables, the first column should usually be about one
  quarter of the table width.
- Preserve the disease flow: why it happens, how it presents, how it is
  confirmed, and how it is treated.
- When multiple mechanisms or subtypes are clinically meaningful, separate
  their causal chains instead of averaging them into one pathophysiology line.
- Keep clinically meaningful splits consistent across the whole note: the same
  branches should reappear in symptoms, diagnosis, treatment, traps, and recall
  when they affect problem solving.
- Use `<br/>` inside table cells to put parallel subtype/mechanism branches on
  separate lines.
- Bold subtype/branch labels at the start of each branch line, but do not bold
  the entire causal chain.
- Use actual arrow symbols (`→`) for causal and mechanism flows; do not use
  ASCII `->` in generated study notes.
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
- No `Algorithm Review Map`, `Visual Anchor`, or figure-based section leaves
  only the heading/subheading on one page while the first image or table starts
  on the next page.
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
layout:

```text
~/Library/Mobile Documents/com~apple~CloudDocs/Study Assistant/PDFs/{system}/{topic}.pdf
~/Library/Mobile Documents/com~apple~CloudDocs/Study Assistant/Notes/{system}/{topic}/md/{topic}.md
```

Examples:

```text
Study Assistant/PDFs/순환기/심부전.pdf
Study Assistant/Notes/순환기/심부전/md/심부전.md
```

Keep active PDFs out of the topic folder. The topic folder is for editable
Markdown, screenshots/images, and archives:

```text
Study Assistant/Notes/{system}/{topic}/_archive/pdf/{topic}_YYMMDD_ver.N.pdf
Study Assistant/Notes/{system}/{topic}/_archive/md/{topic}_YYMMDD_ver.N.md
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
Study Assistant/Notes/{system}/{topic}/md/{topic}.md
```

Then regenerate the PDF from that updated Markdown:

```text
Study Assistant/PDFs/{system}/{topic}.pdf
```

Recommended workflow:

1. Check whether a matching topic folder already exists in iCloud.
2. If an existing Markdown source exists, read it first.
3. Merge new Allen/KMLE/source material into the relevant sections.
4. Preserve the existing structure unless it is clearly broken.
5. Update `Source Notes` and, when useful, add a short `Update Log` entry.
6. Re-render the PDF and sync the canonical Markdown/PDF with
   `scripts/sync_compact_note_to_icloud.py`.

Versioned files such as `-v2` or date-stamped copies may be created only as
temporary local outputs or archived outputs. The active iCloud locations should
keep one canonical latest file:

```text
Notes/{system}/{topic}/md/{topic}.md
PDFs/{system}/{topic}.pdf
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
