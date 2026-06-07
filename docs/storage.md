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
