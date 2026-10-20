# Study Assistant

Study Assistant is a local-first learning assistant project.

Agent instructions, templates, scripts, and selected study outputs live in this
Git repository. Active personal study files live in iCloud Drive so PDFs, notes,
and generated exports can be used across Mac mini, MacBook, iPad, and other
Apple devices. The tracked heart-failure note is the current reference output.

## Project Roles

- Summarizer agent: organizes and summarizes study notes, PDFs, and raw inputs.
- Wrong-answer agent: turns mistakes into structured review notes.
- Quiz agent: generates practice questions from selected materials.

## Current Agent Setup

This repository now starts with two Allen's Library-focused Codex agents:

- Compact note PDF agent: turns theory pages into national-exam-style compact
  notes with stronger drug tables, contraindications, cautions, and exam traps.
- Problem-solving helper agent: analyzes reasoning flow, wrong answers, and
  reusable decision rules for national exam questions.

See `docs/study-system.md` for the full study-system design.

## Storage Model

Code and project configuration are stored here:

```text
/Users/jhsmacmini/codex-projects/study-assistant
```

User learning files are stored in iCloud Drive:

```text
/Users/jhsmacmini/Library/Mobile Documents/com~apple~CloudDocs/Study Assistant
```

## Repository Layout

```text
study-assistant/
├── README.md
├── .gitignore
├── .env.example
├── docs/
│   ├── storage.md
│   └── study-system.md
├── agents/
├── instructions/
├── templates/
├── assets/fonts/
├── outputs/
│   ├── notes/순환기/심부전/
│   │   ├── heart-failure-compact-note.md
│   │   └── images/
│   └── pdf/순환기/심부전/heart-failure-compact-note.pdf
├── app/
├── scripts/
├── sessions/
└── data/
    └── .gitkeep
```

## GitHub Sync Workflow

Use GitHub to synchronize instructions, templates, scripts, bundled fonts, and
the selected reference outputs already tracked under `outputs/`. Keep raw
textbooks, unrelated personal notes, and temporary render checks out of commits.
Existing tracked images do not grant permission to add further copyrighted
Allen/KMLE source images; follow the source rules in `instructions/common-rules.md`.

Typical flow:

```sh
git status
# If there are local changes, preserve and review them before pulling.
git pull --ff-only
# work locally
git status
git add <reviewed-files>
git commit -m "Describe the change"
git push
```

Do not commit secrets, local databases, caches, raw source uploads, or the whole
iCloud folder. Review selected output changes before staging them.

## Continuing a Note and iCloud Sync

Reference Markdown and PDF:

- `outputs/notes/순환기/심부전/heart-failure-compact-note.md`
- `outputs/pdf/순환기/심부전/heart-failure-compact-note.pdf`

Continue from the existing iCloud Markdown after comparing it with the repository
copy. The active iCloud layout is:

```text
Study Assistant/PDFs/{system}/{topic}.pdf
Study Assistant/Notes/{system}/{topic}/md/{topic}.md
Study Assistant/Notes/{system}/{topic}/_archive/{pdf,md}/{topic}_YYMMDD_ver.N.{pdf,md}
```

The sync script uses `--storage-root` first, then the exported
`STUDY_ASSISTANT_STORAGE_PATH` environment variable, then
`~/Library/Mobile Documents/com~apple~CloudDocs/Study Assistant`. It does not
automatically load `.env`. Use Python with ReportLab installed; the bundled
Pretendard fonts are included in `assets/fonts/`.

First inspect the plan without changing iCloud files:

```sh
python3 scripts/sync_compact_note_to_icloud.py \
  --markdown outputs/notes/순환기/심부전/heart-failure-compact-note.md \
  --system 순환기 --topic 심부전 --dry-run
```

When the source and destinations are correct, omit `--dry-run` to render the PDF,
archive existing Markdown/PDF versions, and install the new active files. Run
only one sync for a topic at a time. A dry run checks paths and the archive plan;
it does not render or verify write access. The script copies Markdown/PDF only:
relative image references must also resolve beside the destination Markdown
(for example `md/images/`). Preserve those assets when continuing a note.
