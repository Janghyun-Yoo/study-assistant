# Compact Exam Note Template

---
type: compact-exam-note
system:
topic:
source: Allen's Library
kmle_source:
url:
generated:
storage_pdf: Study Assistant/PDFs/{system}/{topic}.pdf
storage_md: Study Assistant/Notes/{system}/{topic}/md/{topic}.md
tags:
---

# {System} > {Unit}

Do not add a version/subtitle line under the top title in the PDF. Track
versions in file names, front matter, or source notes instead.

Gold standard reference: `heart-failure-compact-note` based on v2.9.

Future notes should match that style unless the user asks otherwise: Allen-first
integrated content, exam snapshot, disease flow, concept bridge for important
classifications placed where the concept is needed, readable tables, restrained
blue/red emphasis, representative drug names with naming patterns, concise
source notes, optional visual anchors for visually diagnosed topics, and
slightly generous spacing above major section headings.

Use Allen as the structural skeleton for compact notes. For concept and disease
explanation, target roughly Allen 80% and KMLE 20%: begin from Allen's overview,
summary table, section order, and exam-facing comments, then add only KMLE items
that fill a real gap or sharpen a national-exam decision. For exam tendency,
common traps, and active recall, KMLE can carry about half the weight because
problem explanations reveal how the concept is tested. Do not let KMLE treatment
algorithms, drug lists, or guideline-style details take over the early disease
script. Preserve source algorithms as late `Algorithm Review Map` material
rather than as the main note outline.

When a KMLE reinforcement point uses a compressed term, guideline abbreviation,
or algorithm label such as `4 pillars`, `GDMT`, or `device trigger`, expand it
at first use in one short phrase. Do not leave the first-page term empty by
writing only "see treatment/trap later"; show the core components or definition
first, then send details to treatment, traps, or active recall.
In early `Exam Snapshot`/summary tables, if that expansion takes the form
`label = long component list` followed by a safety, trigger, or trap note, use
semantic line breaks: `label<br/>= components<br/>→ note`. For example:
`HFrEF 예후 개선 4축(4 pillars)<br/>= ARNI/ACEi/ARB + evidence BB + MRA + SGLT2i<br/>→ MRA 안전성, CRT/ICD trigger는 treatment/trap에서 확인`.

Tables should not waste horizontal space on short label columns. For every
table, choose column widths based on each column's role and average text length.
Keep label columns such as `Field`, `Step`, `Test`, `Category`, `Class`, `Item`,
`Pattern`, `Situation`, and `Cause Group` compact, and give more width to
explanation-heavy columns such as `High-Yield Answer`, `Core Concept`,
`Mechanism`, `Mechanism Flow`, `Role`, `Better Rule`, and `Treatment Anchor`.
For `Test / Use / Expected Finding / Exam Trap` tables, keep `Use` compact when
it only names the test purpose. Give recovered width to `Expected Finding`
first when it contains imaging/lab finding lists; use semantic breaks in
`Exam Trap` before letting traps squeeze finding phrases.
If a column repeatedly wraps awkwardly, first compress the wording or add
semantic `<br/>` breaks; if that is not enough, rename/split columns or split
the table into two smaller tables.
In clinical clue columns such as `Dominant Clues`, `Clinical Clues`, `Finding`,
and `Exam Cue`, keep clinical finding chunks together. Phrases such as
`CXR 폐부종`, `JVP↑`, `하지부종`, and `전신정맥 울혈` should not split so that a
short finding such as `폐부종` lands alone on a line. Prefer column width
redistribution before adding manual `<br/>` breaks.
In `Expected Finding` and other finding-list columns, keep English clinical
phrases together as well. Do not split `alveolar edema`, `vascular congestion`,
`pulmonary edema`, `severe valve disease`, `coronary artery disease`, or
`structural heart disease` so that `edema`, `congestion`, or `disease` lands
alone. First try column-width redistribution to keep the full finding list on
one line; if that is not possible, move the whole clinical phrase to the next
line.
Do not leave standalone clinical acronyms such as `MCS`, `IABP`, `LVAD`, or
`ECMO` alone on a final table line when they are part of an action phrase. Attach
the action word, such as `MCS 고려`, or redistribute width before accepting the
layout.
Keep add-on/modifier operators with the treatment or item they modify. Never let
`±` sit at the end of one line while the add-on moves to the next line. If the
phrase wraps, make the branch explicit as `anchor treatment<br/>± add-on
treatment`, e.g. `norepinephrine으로 perfusion pressure 확보<br/>±
dobutamine/milrinone`.
Also avoid leaving short device/procedure action chunks such as `MCS 고려`,
`ECMO 고려`, `IABP 고려`, `LVAD 고려`, `PCI 고려`, or `CABG 고려` as an accidental
final line. Keep the trigger plus action together, e.g. `refractory면 MCS 고려`,
or make the split intentional with a complete branch line such as
`Escalation: refractory shock → MCS 고려`.
For dense cause-to-result phrases in table cells, prefer a semantic break before
the arrow when the cause/entity is long and the result is a list:
`cause/entity<br/>→ consequence list`. Example:
`papillary muscle rupture<br/>→ acute MR, VSD, free wall rupture/tamponade`.
Do not leave short Korean suffix fragments such as `축`, `군`, `형`, `류`, `계`,
`증`, `병`, `염`, `법`, `술`, `제`, `약`, `원인`, or `질환` alone on a table line.
Keep short labels such as `RV-PVR 축`, `폐혈관 축`, and `원인 질환` together or
rewrite the label.
For `Step / Flow / Cue` tables such as `Disease Flow`, make the `Step` column
very compact. Give recovered width to the column carrying the long decision
logic; if semantic breaks make `Exam Cue` comfortable, prioritize
`High-Yield Flow` so treatment/mechanism lines do not strand short action
chunks.
In `Disease Flow`, prefer compact line-based summaries over complete sentences.
Each line should read like a decision card: `test/action → purpose` or `branch
label: key items`. Use `<br/>` between lines. Keep Allen summary coverage, but
compress it into scannable steps instead of prose.
If a row represents several pathophysiologic directions, bold each starting
mechanism and place downstream effects on separate lines when needed. If an
exam-cue cell has a profile/classification statement that wraps awkwardly,
rewrite it as a header plus branch lines, e.g.
`KMLE profile:<br/>warm-wet은 diuretic/vasodilator,<br/>cold-wet은 shock 처치`.
After adding semantic chunk protection or manual `<br/>` in one table cell,
re-check the whole table's column widths. Do not accept a width candidate that
fixes one cell but creates a new orphan elsewhere, such as `방향 확인`, `강화`,
`edema`, `congestion`, or `disease`.
For conditional exam cues that would likely take two lines, split at the
condition boundary rather than letting the renderer wrap mid-thought:
`condition<br/>clinical decision/action`, e.g.
`MI 뒤 호흡곤란/저혈압이면<br/>ACS + mechanical complication을 같이 본다`.
Apply this to all cue/trap/decision table cells, including `Exam Cue`,
`Exam Trap`, `Common Trap`, `Better Rule`, `Watch`, `Exam Move`, and
active-recall `Answer`. Prefer `새 murmur + shock이면<br/>mechanical complication`
over an accidental `mechanical` / `complication` split.
For non-condition evidence cues, use `context/evidence<br/>interpretation`, e.g.
`"저혈압"보다 organ hypoperfusion 단서가<br/>shock을 강화`.
If a table cell has a long caveat, risk, or result clause after `;` or a
clause-separating comma, keep that second clause together. If it cannot stay on
the same line, insert the break after the punctuation:
`primary point;<br/>secondary caveat` or `selected indication,<br/>major risk`.
Do not force this rule on short simple lists such as `A, B, C`.

When using an Allen page, begin from the short top overview/comment. Let that
overview decide the exam-facing scope. Briefly mention basic concepts only when
they are necessary for diagnosis, treatment, classification, or a common exam
trap; otherwise omit them.

When Allen provides a compact summary table or top summary box, run a coverage
pass before finalizing. Each source-summary item must be visible in the `Exam
Snapshot`, `Disease Flow`, or an adjacent early summary table. Compress and
rephrase freely, but do not leave summary items only in later detailed sections.
Before drafting `Disease Flow`, turn the Allen summary table into a coverage
checklist: causes/risk factors, clinical clues, diagnosis/tests, and treatment
branches. Map each item into the `Disease Flow` row where it changes problem
solving, using one `<br/>` line per decision. Avoid duplicating the source table
verbatim.
For treatment pages, this includes lifestyle correction, first-line chronic
therapy, phenotype-specific treatment, add-on/device options, and acute
treatment framing when those appear in the Allen summary.
If the checklist makes `Disease Flow` too crowded, keep the decision axis in
`Disease Flow` and put the extra source-summary detail in a small adjacent early
summary table directly below it.

Keep source notes attached to the table, figure, or paragraph they document.
Avoid leaving a short `출처:` note alone on the next page; source-note text can
be smaller than body text if that keeps it on the same page.

Keep figure-based review blocks together. For `Algorithm Review Map`, `Visual
Anchor`, or similar sections, the heading, subheading, and first image/table
should move as one unit; do not leave the heading on a page by itself while the
visual starts on the next page.

For short section-opening prose, prefer one review sentence per line using
`<br/>` when each sentence is short enough to fit on one line. Example:
`Allen 상단 총평의 핵심은 ... 점이다.<br/>국시에서는 ... 먼저 잡는다.`
Do not insert manual breaks into long sentences that already wrap naturally.

If Allen highlights contraindications, "do not use" medications, disease-
worsening drug classes, or safety-stopping conditions that are important for
exam choices, mark only the tested phrase in red bold:
`<span style="color:#B91C1C">**contraindication / avoid item**</span>`.
Do not color entire rows or long explanatory sentences.

## Exam Snapshot

| Field | High-Yield Answer |
|---|---|
| One-line definition |  |
| Classic presentation |  |
| Key pathophysiology |  |
| Confirm/classify with |  |
| First-line treatment |  |
| Must-not-miss cause |  |
| Common trap |  |

## Disease Flow

| Step | High-Yield Flow |
|---|---|
| 원인/위험인자 |  |
| 병태생리 |  |
| 임상증상/징후 |  |
| 진단/검사 |  |
| 치료 |  |
| 예방/추적 |  |

If the topic contains multiple clinically important subtypes, directions, or
parallel mechanisms, do not collapse them into one generic flow. Split the
relevant row into subtype-specific mini-flows so each mechanism leads to its
own clinical clue, test, or treatment implication. Example for heart failure:
`**좌심부전:** LV dysfunction → ↓CO + ↑LV filling pressure → pulmonary congestion<br/>**우심부전/폐혈관 축:** RV dysfunction or ↑PVR → ↑systemic venous pressure → JVP/edema/hepatomegaly`.
Use the same approach for mixed entities such as left/right disease,
forward/backward failure, obstructive/restrictive patterns, acute/chronic forms,
or classification groups that change exam reasoning.

Carry that split through the whole note, not only this table. If `Disease Flow`
separates subtypes or mechanisms, the later pathophysiology, symptoms/signs,
diagnosis/tests, treatment, exam traps, and active recall sections should reuse
the same branches whenever the distinction changes reasoning. Do not introduce
a left/right, acute/chronic, or phenotype split in `Disease Flow` and then
return to a blended generic explanation in the rest of the document.
When multiple branches appear inside one table cell, put each branch on its own
line with `<br/>` so the separation remains visible in both Markdown and PDF.
Bold only the subtype/branch label or mechanism starter at the start of each
branch line, such as `**좌심부전:**`, `**ADHF/폐부종:**`, or
`**↑LV filling pressure**`; keep the causal chain or explanation after the label
in regular weight unless it deserves separate high-yield emphasis.
Do not merge clinically different axes into one slash label when importing an
Allen summary into `Disease Flow`; split items such as `저박출` symptoms and
`청진` findings into separate branch lines.
Use actual arrow symbols (`→`) for causal flows instead of ASCII `->`.
When a long cause/entity points to a result list inside a narrow table cell, use
`<br/>` before `→` so the result line starts with the arrow.
Use compact symbols in tables and exam-cue lines when they improve scan speed:
`↑` increase/rise/high, `↓` decrease/low/reduced function, `O` present/with,
`X` standalone absent/not-applied status, `+` positive, `−` negative, and `→`
cause/effect or test/purpose. Do not over-compress definitions, source notes,
dosing, contraindications, or red-bold safety warnings. Do not use `X` to
replace natural-language action guidance such as `~없이`, `~하지 않기`, `피하기`,
`금지`, `주의`, or `아님`.

Place any needed `Concept Bridge` immediately before the section that relies on
that concept. Do not keep it directly after `Disease Flow` by default. For
example, put an EF classification bridge just before clinical classification or
treatment sections that depend on HFrEF/HFpEF, and put an acute-vs-chronic
treatment bridge just before the treatment algorithm.
When the bridge explains a classification, score, stage, severity grade, lab
threshold, or imaging criterion, include the concrete cutoff values in the
table. Do not write only "reduced", "preserved", "positive", "severe", or
"high-risk" when the source gives a number. Example: `HFrEF: LVEF ≤40%`,
`HFmrEF: 41-49%`, `HFpEF: ≥50% + filling-pressure evidence`.
When a bridge, classification table, or comparison table introduces major
concept terms, put the bilingual label in the leftmost label column (`Item`,
`Pattern`, `Cause Group`, `Situation`, etc.). Prefer Korean + abbreviation to
keep tables readable, and put the English/abbreviation on its own line with
`<br/>`, such as `박출률 감소 심부전<br/>(HFrEF)`,
`폐고혈압<br/>(PH)`, `폐동맥고혈압<br/>(PAH)`, and
`폐성심<br/>(cor pulmonale)`. Do not repeat the same bilingual label inside
explanation columns; keep those cells focused on cutoff values, causal chains,
exam cues, and treatment implications. In prose definitions, bilingual first use
is allowed, but do not repeat it every time.

## Core Disease Script

### Definition

Write one integrated definition. Do not split Allen and KMLE if the concept is
substantially the same.

<small>출처: Allen page; KMLE p.__ if this section includes KMLE-only framing.</small>


### Pathophysiology

- 

<small>출처: Allen/KMLE/외부 보강 중 실제로 사용한 추가 내용만 표시.</small>

### Causes / Risk Factors

| Category | Examples | Exam Cue |
|---|---|---|
|  |  |  |

### Symptoms / Signs

| Finding Group | Findings | Why It Matters |
|---|---|---|
|  |  |  |

---

## Diagnosis and Tests

### Diagnostic Approach

1.
2.
3.

### Key Tests

| Test | Use | Expected Finding | Exam Trap |
|---|---|---|---|
|  |  |  |  |

### Differential Diagnosis

| Alternative | Clue For | Clue Against | Deciding Test/Point |
|---|---|---|---|
|  |  |  |  |

## Visual Anchors

Use this section only when visual recognition is high-yield, such as ECG, CXR,
CT/MRI, ultrasound, dermatology, ophthalmology, pathology, or endoscopy. Skip it
for topics where images would be decorative rather than diagnostic.

Usually include 1-3 images per unit. Place each image close to the section that
uses it, and keep the interpretation text short.

Use exact crops from the user's source page, PDF, screenshot, or image file.
Do not redraw or regenerate clinical images. If the source image is not yet
available, write `원본 crop 필요` and keep the interpretation table ready.
When multiple screenshots, source crops, or photos show substantially the same
finding or algorithm, include only the clearest one. Prefer the visual that is
more concise, readable in PDF, and directly useful for exam review. Keep both
only when they answer different tasks, such as one diagnostic image and one
separate treatment algorithm.

```md
![Short descriptive alt text](path/to/image.png)
```

When the image is placed above the table, do not keep a redundant `Image`
column. Use the table only for interpretation:

| What to Look For | Exam Cue | Common Trap |
|---|---|---|
| 핵심 시각 패턴 | 문제에서 주는 단서 | 헷갈리는 감별/오답 |

In this visual-anchor interpretation table, `What to Look For` is not a short
label column. Keep it wide enough for pattern findings, with the current PDF
renderer preset using roughly `38 / 30 / 32` for
`What to Look For / Exam Cue / Common Trap`.

Use an `Image` column only when the image itself is embedded inside the table
cell, which the current compact-note renderer does not normally do.

---

## Treatment

## Concept Bridge: {classification or abbreviation, if needed here}

Use this section when a subtype, abbreviation, staging system, or classification
will affect the following diagnosis, test, treatment, prognosis, or exam
strategy section. Skip it when there is no meaningful classification issue.
Include exact criteria or cutoff values when they exist. For major concept terms,
put the bilingual label in the leftmost row label and split the English/abbrev
onto the next line, such as `박출률 감소 심부전<br/>(HFrEF)`,
`폐고혈압<br/>(PH)`, or `폐성심<br/>(cor pulmonale)`. Do not repeat full English
names in the explanation cells unless the English wording itself is the tested
point.

| Item | Core Concept | Why It Matters | How to Confirm |
|---|---|---|---|
| 한글 용어<br/>(abbr) | 기준/핵심 개념 | 임상/시험 의미 | 확인법/함정 |

### Treatment Algorithm

1.
2.
3.

### Algorithm Review Map

Use this only when KMLE, a guideline, or another source has an algorithm whose
whole structure is worth reviewing visually. Crop the original algorithm from
the source PDF/image. Do not redraw it. If the crop is too large to read, split
it into two logical parts.
If a user-provided screenshot summarizes the same algorithm more cleanly than a
busy source crop, use the clearer screenshot as the review map and cite the
source crop in the note instead of rendering both.

```md
![Short descriptive alt text](path/to/source-algorithm-crop.png)
```

| Review Point | Exam Move | Trap |
|---|---|---|
| 핵심 분기점 | 문제에서 먼저 판단할 것 | 알고리즘을 잘못 적용하는 경우 |

### Drug Table

| Drug/Class | Representative drugs | Name pattern | Effect | Mechanism | When to Use | Contraindications | Cautions | Major Adverse Effects |
|---|---|---|---|---|---|---|---|---|
|  |  | e.g. `(~sartan)`, `(~pril)`, `(~dipine)`, `(~olol)`, `(~gliflozin)` |  |  |  |  |  |  |

For compact `Drug Anchor Table` variants without a `Name pattern` column, write
useful suffixes in the `Class` cell instead, such as `ACEi (~pril)`,
`ARB (~sartan)`, `BB (~lol)`, or `SGLT2i (~gliflozin)`.

For `Add-on`, `2nd line`, `selected`, `consider`, or `필요시` drugs, the
`When to Use` cell must show the selection trigger. If several drugs are grouped
in one row, use separate `<br/>` lines such as `drug: trigger`. Do not place
device/procedure choices in a drug row; put those in treatment flow or a
separate trigger table.

### Contraindications / Cautions

| Situation | Avoid/Watch | Reason |
|---|---|---|
|  | <span style="color:#B91C1C">**Allen/KMLE major contraindication or avoid-list item**</span> | 시험에서 피해야 하는 선택지/악화 요인 |

---

## Exam Traps and Active Recall

### National Exam Points

- 

### Common Traps

| Trap | Better Rule |
|---|---|
|  |  |

### Active Recall Q&A

| Question | Answer |
|---|---|
|  |  |

### Source Notes

- Allen's Library page:
- KMLE source:
- External reference check:
- Guideline-sensitive points:
