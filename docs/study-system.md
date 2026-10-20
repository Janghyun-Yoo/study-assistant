# Codex Study System

This repository is not primarily an app. It is a reusable study system made of
agent instructions, templates, session notes, and generated study outputs.

## Goal

Use Codex as a structured study partner while studying with Allen's Library.

The system has two main agents:

1. National exam compact note PDF agent
2. National exam problem-solving helper agent

## Agent Roles

### 1. Compact Note PDF Agent

Turns an Allen's Library theory page into a compact national-exam-style note.
It emphasizes disease structure, diagnosis, tests, treatment, drug mechanisms,
contraindications, and exam traps. The final output can be rendered as PDF.

See: `agents/note-pdf-agent.md`

### 2. Problem-Solving Helper Agent

Analyzes the user's reasoning after solving a question. It identifies where the
thinking went off track, classifies the mistake, and creates reusable decision
rules for similar questions.

See: `agents/problem-solving-agent.md`

## Directory Structure

```text
study-assistant/
  agents/
    note-pdf-agent.md
    problem-solving-agent.md
  instructions/
    common-rules.md
    allen-source-policy.md
  templates/
    compact-exam-note.md
    disease-note.md
    drug-table.md
    pdf-rendering-guide.md
    problem-review.md
    wrong-answer-log.md
  sessions/
  outputs/
    pdf/
    notes/
```

## Basic Usage

For theory-page study:

```text
Use agents/note-pdf-agent.md.
Based on the current Allen's Library theory page, create a compact exam note
using templates/compact-exam-note.md and prepare it for PDF output.
```

For question review:

```text
Use agents/problem-solving-agent.md.
I chose [my answer], the correct answer was [correct answer], and my reasoning
was [my thought process]. Analyze the reasoning and make a review note.
```

## iCloud Note Storage

Generated personal study notes should be organized in iCloud Drive with
user-facing PDFs separated from editable topic materials.

```text
~/Library/Mobile Documents/com~apple~CloudDocs/Study Assistant/PDFs/{system}/{topic}.pdf
~/Library/Mobile Documents/com~apple~CloudDocs/Study Assistant/Notes/{system}/{topic}/
```

Examples:

```text
Study Assistant/PDFs/순환기/심부전.pdf
Study Assistant/Notes/순환기/심부전/
```

The compact note PDF agent should save the latest PDF in the top-level PDF
collection and the editable Markdown file in the topic folder:

```text
Study Assistant/PDFs/{system}/{topic}.pdf
Study Assistant/Notes/{system}/{topic}/md/{topic}.md
```

## Template References

Study Assistant adapts structural ideas from public Markdown study-note systems,
such as metadata/front matter, active-recall Q&A blocks, and PDF-aware page
breaks. See `docs/template-references.md`.

## First Principle

Allen's Library is the content and question platform. This repository is the
study operating system around it: summarization, restructuring, reasoning
analysis, review, and accumulated weak-point tracking.
