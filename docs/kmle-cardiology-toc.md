# KMLE Cardiology TOC Index

Source file:

```text
Study Assistant/Library/2027 PACIFIC KMLE 01_순환기.pdf
```

Technical note:

- The PDF is image-based.
- `pypdf` extraction returned almost no usable text.
- `pdftoppm` page rendering works.
- `tesseract` OCR with `kor+eng` works well enough for page discovery.

## Confirmed Heart Failure Pages

| Topic | PDF Page | Status | Notes |
|---|---:|---|---|
| 심부전 단원 시작 | 212 | confirmed visually | 정상 심장 vs. 심부전, CO/SV/HR, preload/contractility/afterload |
| 심부전의 원인, 증상, 진단 | 219 | confirmed visually | Allen 심부전 원인/증상/진단 페이지와 직접 매칭되는 KMLE 개념 파트 |
| 만성 심부전 치료 / HFrEF GDMT | 237 | confirmed visually | ARNI, ACEi/ARB, beta-blocker, MRA, SGLT2i, diuretics |
| 심부전 문제/해설 | 252-253 | confirmed visually | chronic HF treatment and medication-choice question patterns |

## OCR-Derived TOC Notes

The first TOC OCR pass showed:

```text
@ 심부전 _212
정상 심장 vs. 심부전
심부전의 원인, 증상, 진단 ... 219
만성 심부전의 치료 ... number partially unclear, visually confirmed around 237
급성 비보상성 심부전 및 급성 폐부종 ... number unclear, needs confirmation
```

Important correction:

```text
심부전의 원인, 증상, 진단 starts at PDF page 219, not page 19.
```

The OCR missed the leading `2` in one summary TOC line.

## How to Use This Index

For the Allen page:

```text
순환기 > 심부전 > 심부전 원인, 증상, 진단
```

Use KMLE pages:

```text
212-236 for KMLE concept background
219 onward for cause/symptom/diagnosis details
237 onward for chronic HF treatment/GDMT
252-253 for question-style medication/treatment points
```

When generating a note, label content:

```text
[KMLE 개념]
[KMLE 문제 포인트]
```

Do not quote the KMLE text verbatim. Summarize and restructure for personal
study.

## Needs Further Confirmation

| Topic | Expected Area | Status |
|---|---|---|
| 급성 비보상성 심부전 및 급성 폐부종 | after chronic treatment/question pages | needs page confirmation |
| Full 심부전 range end page | before 판막질환 start page 274 | needs range confirmation |
