# Compact Exam Note Template

---
type: compact-exam-note
system:
topic:
source: Allen's Library
kmle_source:
url:
generated:
storage_pdf: Study Assistant/Notes/{system}/{topic}/pdf/
storage_md: Study Assistant/Notes/{system}/{topic}/md/
tags:
---

# {System} > {Unit}

Do not add a version/subtitle line under the top title in the PDF. Track
versions in file names, front matter, or source notes instead.

Gold standard reference: `heart-failure-compact-note` based on v2.9.

Future notes should match that style unless the user asks otherwise:
integrated Allen/KMLE content, exam snapshot, disease flow, concept bridge for
important classifications placed where the concept is needed, readable tables,
restrained blue/red emphasis, representative drug names with naming patterns,
concise source notes, and slightly generous spacing above major section
headings.

Tables should not waste horizontal space on short label columns. For every
table, choose column widths based on each column's role and average text length.
Keep label columns such as `Field`, `Step`, `Test`, `Category`, `Class`, `Item`,
`Pattern`, `Situation`, and `Cause Group` compact, and give more width to
explanation-heavy columns such as `High-Yield Answer`, `Core Concept`,
`Mechanism`, `Mechanism Flow`, `Role`, `Better Rule`, and `Treatment Anchor`.
If a column repeatedly wraps awkwardly, first compress the wording or add
semantic `<br/>` breaks; if that is not enough, rename/split columns or split
the table into two smaller tables.
For `Step / Flow / Cue` tables such as `Disease Flow`, make the `Step` column
very compact and give the recovered width to `High-Yield Flow` and especially
`Exam Cue` so short cue phrases do not fall onto awkward trailing lines.

When using an Allen page, begin from the short top overview/comment. Let that
overview decide the exam-facing scope. Briefly mention basic concepts only when
they are necessary for diagnosis, treatment, classification, or a common exam
trap; otherwise omit them.

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
Bold only the subtype/branch label at the start of each branch line, such as
`**좌심부전:**` or `**ADHF/폐부종:**`; keep the causal chain or explanation after
the label in regular weight unless it deserves separate high-yield emphasis.
Use actual arrow symbols (`→`) for causal flows instead of ASCII `->`.

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

### Drug Table

| Drug/Class | Representative drugs | Name pattern | Effect | Mechanism | When to Use | Contraindications | Cautions | Major Adverse Effects |
|---|---|---|---|---|---|---|---|---|
|  |  | e.g. `(~sartan)`, `(~pril)`, `(~dipine)`, `(~olol)`, `(~gliflozin)` |  |  |  |  |  |  |

### Contraindications / Cautions

| Situation | Avoid/Watch | Reason |
|---|---|---|
|  |  |  |

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
