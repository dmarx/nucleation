# Reader notes: Aryabumi et al. 2024, arXiv 2408.10914 (To Code, or Not To Code?)

## 1. Copy located and read (2026-11-19)
- arxiv.org/html/2408.10914 (v1 only, per abs page), HTTP 200, full text incl. appendices A-C. Converted to text in my scratchpad.
- Figures are images; numbers in text come from prose and Table 2.

## 2. Setup (Sec 3.1, Table 2)
- code->text: 200B code (80% code / 20% markup) then 200B continued pretraining = +180B text +20B code (footnote 5: "10% of code in text mixture").
- balanced->text: 100B text + 100B code init, then +180B text +20B code.
- text-only: 400B text; balanced-only: 200B/200B. All 400B total before cooldown. Cooldown +32B text +8B code (40B).
- So code->text sees 180B NL tokens vs 400B for text-only, and gets reasoning 53.3 vs 49.0, knowledge 9.5 vs 9.5 (Table 2). Authors do NOT state this as a token saving; framed as relative gains at fixed total tokens.
- No seeds/repeats mentioned anywhere (grep). 64 models total.
- No pure-ordering control: there is no text->code or matched mixed run with same token totals per source; balanced-only is the mixing comparator but it has 200B text vs 180B+100B=280B for balanced->text.

## 3. Results read (Secs 3.1-3.6, 5, 6; appendices skimmed)
- Sec 3.1 relative gains (8.8% / 8.2% NL reasoning over text-only) reproduce from Table 2: 53.3/49.0 and 53.0/49.0.
- Key point the authors do not discuss: after cooldown (Table 2), text-only 54.1 reasoning / 11.1 knowledge; balanced->text 54.9 / 10.9; code->text 52.1 / 10.3. The code-first NL advantage does not survive cooldown; code->text ends below text-only.
- Mixing: 25% code from scratch (200B) best NL reasoning, +3.4% over 0% (Sec 3.3); knowledge falls monotonically with code share.
- No seeds, no error bars; one run per variant ("we train a new model independently"). 470M subset rule: only benchmarks above random for all models.
- LR schedule for the continued phase not stated (cosine, warmup 1325 steps for "all models").
- Internal inconsistencies: intro vs Sec 3.4 numbers (1.9%/41% vs 2%/35%), win-rate figures (33.7 vs 34.7), "Figure 9" cited for 2.8B but appendix Fig 9 is win-rates.

## 4. Bearings searched
- Named: CLAIM-756, QUESTION-039, TERM-131, THEORY-tmpk9cmk, -tmpd6l4a, -tmp0lbb1, -tmpd6smn. Also CLAIM-754, CLAIM-758, TERM-117, CASE-294, QUESTION-495, THEORY-293, THEORY-tmplutfz.
- Record holds no LIT for this work (grep for 2408.10914 / Aryabumi: none).
- Verdict forming: weak, qualifying evidence for CLAIM-756's premise; not a cost/sample-efficiency measurement; the 180B-vs-400B text comparison is computable but not claimed.
