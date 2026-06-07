# Storage

This project separates application code from personal learning materials.

## Local Code Repository

Path:

```text
/Users/jhsmacmini/codex-projects/study-assistant
```

Purpose:

- Application code
- Agent prompts
- Scripts
- Documentation
- Tests
- Database migrations
- Example configuration

These files can be committed to GitHub.

## iCloud Learning Storage

Path:

```text
/Users/jhsmacmini/Library/Mobile Documents/com~apple~CloudDocs/Study Assistant
```

Suggested structure:

```text
Study Assistant/
├── Inbox/
├── Library/
├── Notes/
│   ├── 순환기/
│   │   └── 심부전/
│   │       ├── pdf/
│   │       └── md/
│   ├── 호흡기/
│   └── 소화기/
└── Exports/
```

Purpose:

- PDFs
- Images
- Raw class notes
- Markdown notes
- Summaries
- Wrong-answer notes
- Quiz exports

These files should not be committed to GitHub.

## Notes Organization

Generated study notes should use this hierarchy:

```text
Study Assistant/Notes/{system}/{topic}/
```

Examples:

```text
Study Assistant/Notes/순환기/심부전/
Study Assistant/Notes/호흡기/COPD/
Study Assistant/Notes/소화기/간경변/
```

For compact note outputs, keep the PDF and editable Markdown source together:

```text
Study Assistant/Notes/순환기/심부전/pdf/heart-failure-compact-note.pdf
Study Assistant/Notes/순환기/심부전/md/heart-failure-compact-note.md
```

## Rules

Commit to GitHub:

- App code
- README
- Docs
- Scripts
- Tests
- `.env.example`
- Database migrations

Do not commit to GitHub:

- `.env`
- API keys
- Real study files
- iCloud files
- Local databases
- Embedding caches
- Uploaded files
- `node_modules`
