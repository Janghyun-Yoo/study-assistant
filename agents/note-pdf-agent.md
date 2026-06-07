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

Optional:

- User's current level of confidence
- Desired PDF length
- Specific focus, such as drugs, diagnosis, differential diagnosis, or treatment

## Output Sections

Use this order unless the topic clearly requires a different structure.

1. Source and Scope
2. One-Line Summary
3. Definition
4. Core Pathophysiology
5. Causes and Risk Factors
6. Symptoms and Signs
7. Diagnostic Approach
8. Key Tests
9. Differential Diagnosis
10. Treatment Principles
11. Drug Table
12. Contraindications and Cautions
13. Complications and Prevention
14. National Exam Points
15. Common Traps
16. Five-Minute Review Questions

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

1. Page 1: overview, definition, pathophysiology, symptoms
2. Page 2: diagnosis, tests, differential diagnosis
3. Page 3: treatment and drug table
4. Page 4: exam points, traps, review questions

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
