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
├── PDFs/
│   └── 순환기/
│       └── 심부전.pdf
├── Notes/
│   ├── 순환기/
│   │   └── 심부전/
│   │       ├── md/
│   │       ├── screenshot/
│   │       └── _archive/
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

For compact note outputs, keep the latest user-facing PDF in the top-level
PDF collection and keep the editable Markdown source in the topic folder:

```text
Study Assistant/PDFs/순환기/심부전.pdf
Study Assistant/Notes/순환기/심부전/md/심부전.md
```

## Continuing Existing Topic Notes

For the same system/topic, continue editing the existing Markdown source and
then regenerate the PDF.

Canonical latest files:

```text
Study Assistant/PDFs/{system}/{topic}.pdf
Study Assistant/Notes/{system}/{topic}/md/{topic}.md
```

Before replacing canonical files, archive the previous version with the topic,
date, and version number:

```text
Study Assistant/Notes/{system}/{topic}/_archive/pdf/{topic}_YYMMDD_ver.N.pdf
Study Assistant/Notes/{system}/{topic}/_archive/md/{topic}_YYMMDD_ver.N.md
```

For example, the first archived heart failure files on July 6, 2026 are:

```text
심부전_260706_ver.1.pdf
심부전_260706_ver.1.md
```

If the same topic is updated again on the same date, increment the version
number. On a new date, start again at `ver.1`.

Do not leave experimental, dated, or cache-busting PDFs in the active PDF
collection. Use temporary local output or the topic `_archive` folder instead.

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
