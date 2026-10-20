# Common Rules

These rules apply to all study-assistant agents.

## Core Principles

- Do not reproduce Allen's Library content verbatim.
- Transform source material into the user's own study structure.
- Focus on national medical exam preparation.
- Prefer clinically useful structure over long prose.
- Separate facts, reasoning, uncertainty, and exam strategy.
- For Allen-based compact notes, use Allen as the note skeleton and KMLE as
  selective reinforcement. Concept and disease explanation should feel roughly
  Allen 80% / KMLE 20%; exam tendency, traps, and active recall can be closer to
  50 / 50. KMLE-only algorithms, drug lists, and guideline-style details should
  not dominate the early disease script.
- When adding KMLE reinforcement terms, guideline abbreviations, or algorithm
  labels such as `4 pillars`, `GDMT`, or `device trigger`, expand the term at
  first use in one short phrase. Do not write only "see treatment/trap later";
  show the core components or definition first, then defer details.
- In early `Exam Snapshot`/summary tables, if a KMLE reinforcement point uses
  `label = long component list` and then adds a safety, trigger, or trap note,
  split it with `<br/>` as `label`, `= components`, then `→ note`. Example:
  `HFrEF 예후 개선 4축(4 pillars)<br/>= ARNI/ACEi/ARB + evidence BB + MRA + SGLT2i<br/>→ MRA 안전성, CRT/ICD trigger는 treatment/trap에서 확인`.
- Include concrete cutoff values for classifications, scores, stages, lab
  thresholds, and imaging criteria whenever the source provides them.
- When a table defines or compares major concept terms, put the bilingual label
  in the leftmost label column and place the English/abbreviation on the next
  line with `<br/>`, such as `박출률 감소 심부전<br/>(HFrEF)`,
  `폐고혈압<br/>(PH)`, or `폐성심<br/>(cor pulmonale)`. Keep explanation columns
  focused on criteria, mechanism, and exam cues instead of repeating the full
  term.
- In prose definitions, write the Korean term with the standard English term or
  abbreviation in parentheses on first use. Do not force this on every repeated
  term, drug name, or minor detail.
- When clinically meaningful subtypes or parallel mechanisms are mixed, split
  them into separate reasoning flows instead of averaging them into one line.
- Once a split is introduced, carry it consistently through explanation,
  diagnosis, treatment, traps, and recall when it changes problem solving.
- Treat Allen summary tables and top overview boxes as mandatory coverage
  anchors. Every item in those compact source summaries must appear in the
  `Exam Snapshot`, `Disease Flow`, or an adjacent early summary table, even when
  the same detail is expanded later in the note.
- Before drafting `Disease Flow`, break Allen's compact summary table into a
  coverage checklist: causes/risk factors, clinical clues, diagnosis/tests, and
  treatment branches. Whenever possible, map every checklist item into the
  `Disease Flow` row where it drives problem solving instead of copying the
  source table as a second table.
- It is acceptable to compress or reorganize Allen summary wording, but do not
  silently drop a summary category such as causes, symptoms/signs, diagnosis,
  treatment, lifestyle correction, add-on therapy, or acute-vs-chronic treatment
  framing.
- If a source summary would make `Disease Flow` too crowded, keep only the
  existence and decision axis there, then place a small adjacent early summary
  table immediately below it. Later detailed sections may expand the item, but
  they should not be the only place the Allen summary item appears.
- When Allen highlights contraindications, "do not use" medications, disease-
  worsening drug classes, or safety-stopping conditions that are likely to
  appear as exam choices, mark only the tested phrase in red bold using
  `<span style="color:#B91C1C">**...**</span>`.
- In tables, place parallel subtype/mechanism branches on separate lines with
  `<br/>` instead of relying on semicolons or long sentences.
- Bold only the subtype/branch label or mechanism starter at the start of a
  branch line; keep the rest of the causal chain in regular weight unless
  separately high-yield. In pathophysiology rows with multiple directions, bold
  each starting driver, such as `**↓contractility or mechanical pump failure**`
  and `**↑LV filling pressure**`.
- Do not merge clinically different axes into one slash label when importing an
  Allen summary into `Disease Flow`. For example, split `저박출` symptoms and
  `청진` findings into separate `<br/>` branch lines instead of writing
  `저박출/청진`.
- Use actual arrow symbols (`→`) for causal and mechanism flows instead of
  ASCII `->`.
- In dense table cells, if a long cause/entity is followed by `→` and a list of
  consequences, prefer a semantic break before the arrow:
  `cause/entity<br/>→ consequence list`. This keeps the arrow with the result
  line and reads better than wrapping the result list mid-phrase.
- In compact tables and exam-cue lines, use concise symbols when meaning stays
  clear: `↑` for increase/rise/high/expansion, `↓` for decrease/low/reduced
  function, `O` for present/with, `X` only for a standalone absent/not-applied
  state marker, `+` for positive, and `−` for negative. Keep `→` for
  cause/effect, test/purpose, and treatment/effect flows.
- Apply shorthand first inside tables, `Disease Flow`, `Treatment Flow`,
  `Exam Snapshot`, and trap/recall lines where row width matters. Do not
  over-shorten definitions, source notes, dosing, contraindications, or red-bold
  safety warnings; avoid using `X` alone for a contraindication when "avoid" or
  the red-bold phrase is the tested point.
- Use `X` only in compact status phrases such as `edema X`, `DM X`, or
  `적응증 X` when the whole cell is marking presence/absence. Do not use `X` to
  replace natural-language instructions such as `~없이`, `~하지 않기`, `피하기`,
  `금지`, `주의`, or `아님`; in `Watch`, `Trap`, and `Exam Point` cells, keep
  action guidance readable in natural language.
- Use images selectively when visual pattern recognition is part of the exam
  skill. ECG, CXR, CT/MRI, ultrasound, dermatology, ophthalmology, pathology,
  and endoscopy can justify a compact `Visual Anchors` section; routine disease
  notes should not get images by default.
- Do not redraw, regenerate, or stylistically reinterpret clinical images or ECG
  strips. Use exact crops from user-provided source pages, PDFs, screenshots, or
  image files whenever possible.
- Limit image edits to crop, resize, rotation correction, and gentle
  brightness/contrast cleanup. Put labels and interpretation in the note text,
  not on top of the image, unless the user explicitly requests annotation.
- If the source image is unavailable, leave a `원본 crop 필요` placeholder instead
  of fabricating a substitute image.
- When adding a visual anchor, keep it study-facing: one representative image
  plus what to look for, the exam cue, the key differential, and the trap is
  usually better than many unlabeled images.
- If multiple screenshots, source crops, or photos duplicate the same finding or
  algorithm, choose the single clearest visual. Prefer the one that is more
  concise, readable in the final PDF, and useful for exam review. Keep both only
  when they teach different decisions.
- If a visual anchor image is shown outside the table, the interpretation table
  must not include an `Image` column. Reserve `Image` columns for cases where
  the image is embedded inside the table cell.
- Avoid committing copyrighted Allen/KMLE images to the repository. Prefer
  user-owned local crops or public-domain/open-license images, and include a
  short source note when an external image is used.
- For KMLE or guideline algorithms, use an `Algorithm Review Map`: preserve the
  original algorithm as a full crop for final review, then summarize only the
  high-yield branch points below it. Treat it as review/appendix material, not
  as the main outline for the disease note. Do not regenerate the diagram.
  If a user-provided screenshot captures the same algorithm more clearly than
  the original crop, use the screenshot and omit the duplicate crop.
- If an algorithm crop becomes unreadable when fit to one page, split it into
  two logical crops instead of over-compressing it.
- Mark uncertain or guideline-sensitive content clearly.
- Do not present study notes as medical advice for real patient care.

## Output Style

- Be concise but not shallow.
- Use tables for drugs, differential diagnosis, tests, and treatment choices.
- For every table, size columns by role and expected text length. Keep label
  columns such as `Field`, `Step`, `Test`, `Category`, `Class`, `Item`,
  `Pattern`, `Situation`, and `Cause Group` compact, and give extra width to
  explanation-heavy columns such as `High-Yield Answer`, `Core Concept`,
  `Mechanism`, `Mechanism Flow`, `Role`, `Better Rule`, and `Treatment Anchor`.
- In `Test / Use / Expected Finding / Exam Trap` tables, treat `Use` as a
  compact role column when it contains short action labels such as `확인`,
  `분류`, or `severity`. Give the recovered width to `Expected Finding` first
  when it contains imaging/lab finding lists; `Exam Trap` can use semantic
  breaks before it steals width that would keep findings on one line.
- If a column repeatedly creates awkward line breaks, shorten the cell text,
  add semantic `<br/>` breaks, rename/split columns, or split the table rather
  than leaving a cramped table in the final PDF.
- When a new recurring table shape is added to the gold standard, mirror it in
  the PDF renderer's table-width presets or fallback rules so the rendered PDF
  reflects the same column-role intent.
- Treat table-width presets as starting points. The PDF renderer should prefer
  a nearby optimized width when it prevents orphan lines such as `있음`, `가능`,
  `단서`, or `후보` from landing alone on the final line.
- In clinical clue columns such as `Dominant Clues`, `Clinical Clues`,
  `Finding`, and `Exam Cue`, keep clinical finding chunks together. Phrases such
  as `CXR 폐부종`, `JVP↑`, `하지부종`, and `전신정맥 울혈` should not split so
  that a short finding such as `폐부종` lands alone on a line. Prefer column
  width redistribution before adding manual `<br/>` breaks.
- In finding-list columns such as `Expected Finding`, keep English clinical
  phrases together too. Phrases such as `alveolar edema`,
  `vascular congestion`, `pulmonary edema`, `severe valve disease`,
  `coronary artery disease`, and `structural heart disease` should not split
  into `alveolar` / `edema`, `vascular` / `congestion`, or `severe valve` /
  `disease`. First adjust column width so the whole list fits on one line; if
  that is not possible, move the whole phrase to the next line rather than
  leaving only the head noun such as `edema`, `congestion`, or `disease`.
- Before adding manual `<br/>` breaks, let the renderer try column-width
  optimization and up to 0.4 pt of table-font reduction. Treat one-word or short
  two-token final lines such as `상승`, `확인`, `관리`, `낮음`, `AF 단서`, or
  `폐정맥압 상승`, clinically meaningful solo findings such as `폐부종`, English
  clinical head nouns such as `edema`, `congestion`, or `disease`, and
  standalone clinical acronyms such as `MCS`, `IABP`, `LVAD`, or `ECMO` as
  layout QA failures when they remain.
- If a sentence-like table cell still wraps awkwardly after width optimization,
  convert it into semantic lines instead of accepting an accidental orphan. For
  profile or classification cues, use a header line plus branch lines, e.g.
  `KMLE profile:<br/>warm-wet은 diuretic/vasodilator,<br/>cold-wet은 shock 처치`.
- After adding semantic chunk protection or manual `<br/>` in one table cell,
  re-check column-width optimization for the whole table. A width candidate is
  not acceptable if it fixes one cell but creates a new orphan elsewhere, such
  as `방향 확인`, `강화`, `edema`, `congestion`, or `disease`. Prefer stable
  table-wide balance over over-widening a single column.
- For conditional clinical cues that would likely render as two lines, split the
  condition from the decision/action instead of accepting an accidental wrap.
  Use `condition<br/>clinical decision/action`, especially for phrases ending in
  `이면`, `라면`, `때`, or `시`. Do not force a break when the full cue fits
  naturally on one line.
- Apply this conditional-break rule across all table cue/trap/decision cells,
  including `Exam Cue`, `Exam Trap`, `Common Trap`, `Better Rule`, `Watch`,
  `Exam Move`, and active-recall `Answer` cells. The goal is to keep the
  decision phrase intact, e.g. `새 murmur + shock이면<br/>mechanical complication`,
  instead of letting the renderer split inside the decision phrase such as
  `mechanical` / `complication`.
- In cue/trap/decision cells, also use `context/evidence<br/>interpretation`
  when the cell is not a strict condition. For example, prefer
  `"저혈압"보다 organ hypoperfusion 단서가<br/>shock을 강화` over an accidental
  `organ` / `hypoperfusion` split.
- When a table cell has a long second clause after `;` or a clause-separating
  comma, do not let only the first words of that clause remain on the previous
  line. If the second clause wraps, put the break right after the punctuation:
  `primary point;<br/>secondary caveat` or `selected indication,<br/>major
  risk`. Do not apply this to short simple lists such as `A, B, C`.
- Treat short Korean suffix fragments such as `축`, `군`, `형`, `류`, `계`, `증`,
  `병`, `염`, `법`, `술`, `제`, `약`, `원인`, and `질환` as layout QA failures
  when they land alone in table cells. Prefer semantic chunk protection, then
  width/font optimization, then wording or label revision.
- Preserve semantic chunks inside table cells. Phrases such as `→ RV failure`,
  `→ ↑systemic venous pressure`, `diltiazem exception`, `폐정맥압 상승`, and
  `원인 단서` should move to the next line as a unit rather than splitting in the
  middle. Short labels such as `RV-PVR 축`, `폐혈관 축`, and `원인 질환` should
  also stay together. If an acronym is the tested action, attach it to its action
  word, such as `MCS 고려`, instead of leaving the acronym alone.
- Keep add-on/modifier operators with the item they modify. Do not leave `±` at
  the end of a line while the drug/procedure moves below. If a treatment phrase
  wraps, prefer `anchor treatment<br/>± add-on treatment`, e.g.
  `norepinephrine으로 perfusion pressure 확보<br/>± dobutamine/milrinone`.
- Do not let short device/procedure action chunks such as `MCS 고려`,
  `ECMO 고려`, `IABP 고려`, `LVAD 고려`, `PCI 고려`, or `CABG 고려` sit alone as
  an accidental final table line. First try column-width redistribution; if the
  action is meant to be a separate branch, rewrite it as a full semantic line
  such as `Escalation: refractory shock → MCS 고려`.
- When a cause-to-result phrase is too dense for one table line, insert the
  break before the arrow rather than after the arrow, for example
  `papillary muscle rupture<br/>→ acute MR, VSD, free wall rupture/tamponade`.
- For `Step / Flow / Cue` tables such as `Disease Flow`, keep `Step` as the
  narrowest column and give more width to `Flow` and `Cue`. If manual semantic
  breaks make `Cue` less width-hungry, give the recovered width to
  `High-Yield Flow` so treatment or mechanism lines do not leave short action
  chunks stranded.
- In `Disease Flow`, prefer compact line-based summaries over complete
  sentences. Write each line as `test/action → purpose` or `branch label: key
  items`, using `<br/>` between lines. Preserve Allen summary coverage, but
  compress the wording into scannable decision steps instead of prose.
  When the row represents several pathophysiologic directions, bold each
  mechanism starter and place downstream effects on separate lines when needed.
- Keep source notes visually attached to the table, figure, or paragraph they
  document. Do not let a short `출처:` note sit alone at the top of the next
  page; reduce source-note text size or move the preceding block with it.
- Treat `Algorithm Review Map`, `Visual Anchor`, and other figure-based
  sections as a single review block: heading, subheading, and the first image or
  table should stay together. Do not leave a heading/subheading on one page
  while the algorithm or visual it introduces starts on the next page.
- In section-opening prose, when two or more short sentences would otherwise run
  together in one paragraph, separate each sentence with `<br/>` so each reads
  as one review line. Do not force line breaks into long sentences that already
  wrap naturally.
- Put exam-relevant traps and decision rules near the end.
- Avoid decorative formatting that makes PDF review harder.
- Prefer Korean medical exam language, but keep standard English abbreviations
  when commonly used, such as HF, HFrEF, ECG, CXR, BNP, ACEi, ARB, MRA.
- In compact drug anchor tables, show useful class name patterns in the `Class`
  cell, such as `ACEi (~pril)`, `ARB (~sartan)`, `BB (~lol)`, or
  `SGLT2i (~gliflozin)`. Do not add a separate `Name pattern` column unless the
  note is using a full drug table.
- In drug tables, `Add-on`, `2nd line`, `selected`, `consider`, and `필요시`
  must include the trigger that makes the drug/class the answer. Avoid empty
  phrases such as "선별 환자에서 보조" unless the specific selection condition is
  also shown. If several drugs share one row, write `drug: trigger` on separate
  `<br/>` lines; split the row when triggers are too different. Keep `Watch`
  for contraindications, cautions, and traps rather than indications.
- Do not bury device/procedure triggers inside a drug row. Put CRT, ICD,
  transplant, ablation, procedure, or device choices in treatment flow or a
  separate trigger table with the clinical clue that selects them.

## Medical Safety

- If a diagnosis or treatment rule may depend on updated guidelines, mention
  that verification may be needed.
- If drug contraindications or dosing are involved, avoid pretending to provide
  exhaustive prescribing guidance.
- For medications, distinguish mechanism, effect, indication, contraindication,
  caution, and adverse effects.

## Study Behavior

- Ask for the user's reasoning before giving a full answer when analyzing a
  solved question.
- Do not stop at "memorize this." Convert the point into a usable decision rule.
- Track repeated weak points when possible.
