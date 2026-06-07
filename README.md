# Study Assistant

Study Assistant is a local-first learning assistant project.

The code lives in this Git repository. Personal study files live separately in
iCloud Drive so PDFs, notes, and generated exports can be used across Mac mini,
MacBook, iPad, and other Apple devices.

## Project Roles

- Summarizer agent: organizes and summarizes study notes, PDFs, and raw inputs.
- Wrong-answer agent: turns mistakes into structured review notes.
- Quiz agent: generates practice questions from selected materials.

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
│   └── storage.md
├── app/
├── scripts/
└── data/
    └── .gitkeep
```

## GitHub Sync Workflow

Use this repository for code only.

Typical flow:

```sh
git pull
# work locally
git status
git add .
git commit -m "Describe the change"
git push
```

Do not commit personal study files, local databases, cache files, API keys, or
generated uploads.
