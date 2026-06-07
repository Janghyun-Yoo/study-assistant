# PDF Rendering Guide

Use this guide when converting Markdown study notes into PDF.

## Layout Principles

- The first page should work as a standalone rapid-review card.
- Keep paragraphs short. Prefer bullets and tables.
- Use tables for diagnosis, differential diagnosis, drugs, contraindications,
  and exam traps.
- Separate contraindications, cautions, and adverse effects.
- Use explicit page breaks when the PDF becomes crowded.

## Preferred Page Plan

1. Page 1: exam snapshot and core disease script
2. Page 2: diagnosis, tests, and differential diagnosis
3. Page 3: treatment algorithm and drug table
4. Page 4: contraindications, exam traps, active recall

## Markdown Page Break

Use a horizontal rule as a page-break marker in PDF-oriented notes:

```text
---
```

## Visual QA Checklist

- Korean text renders correctly.
- No table extends beyond page margins.
- No table row is clipped.
- Headings are visually distinct from body text.
- Drug tables remain readable.
- The final PDF is 2-4 pages for one disease/topic whenever possible.

## Source-Inspired Patterns

This project uses structural ideas from public Markdown note systems, including
metadata/front matter, active-recall Q&A sections, and PDF-aware page breaks.
Do not copy external templates verbatim into generated notes.
