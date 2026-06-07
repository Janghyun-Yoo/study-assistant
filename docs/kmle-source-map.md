# KMLE Source Map

KMLE textbooks are stored in iCloud and used as personal study references.

Do not commit KMLE PDFs to GitHub.

## iCloud Location

```text
~/Library/Mobile Documents/com~apple~CloudDocs/Study Assistant/Library/
```

## System File Map

| System | KMLE PDF |
|---|---|
| 순환기 | 2027 PACIFIC KMLE 01_순환기.pdf |
| 호흡기 | 2027 PACIFIC KMLE 02_호흡기.pdf |
| 소화기 | 2027 PACIFIC KMLE 03_소화기.pdf |
| 신장 | 2027 PACIFIC KMLE 04_신장, 감염.pdf |
| 감염 | 2027 PACIFIC KMLE 04_신장, 감염.pdf |
| 내분비 | 2027 PACIFIC KMLE 05_내분비, 알레르기.pdf |
| 알레르기 | 2027 PACIFIC KMLE 05_내분비, 알레르기.pdf |
| 혈액 | 2027 PACIFIC KMLE 06_혈액,종양,류마티스.pdf |
| 종양 | 2027 PACIFIC KMLE 06_혈액,종양,류마티스.pdf |
| 류마티스 | 2027 PACIFIC KMLE 06_혈액,종양,류마티스.pdf |

## Use Rule

For a generated note, use only the KMLE section matching the current system and
topic.

Examples:

```text
Allen: 순환기 > 심부전
KMLE: 2027 PACIFIC KMLE 01_순환기.pdf
Scope: 심부전 section only
```

```text
Allen: 소화기 > 간경변
KMLE: 2027 PACIFIC KMLE 03_소화기.pdf
Scope: 간경변 section only
```

## Source Labels

When KMLE is used, distinguish:

```text
[KMLE 개념]
[KMLE 문제 포인트]
```

Use `[KMLE 개념]` for textbook-style explanation and summarized concepts.
Use `[KMLE 문제 포인트]` for repeated question clues, answer-choice traps, and
exam-pattern observations.

## Current Technical Status

The KMLE PDFs appear to be image-based or have unusable text layers.

Observed for:

```text
2027 PACIFIC KMLE 01_순환기.pdf
```

- `pypdf` extracted almost no text.
- Page rendering with `pdftoppm` works.
- OCR is likely required for reliable topic search and section extraction.

## Next Technical Step

Build an OCR/indexing workflow:

1. Render selected page ranges to images.
2. OCR pages.
3. Build a searchable page index.
4. Locate the topic section, such as `심부전`.
5. Extract only relevant pages for note generation.
