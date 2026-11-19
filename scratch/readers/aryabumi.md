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
