# Reader notes: music (Papadimitriou & Jurafsky 2020, arXiv 2004.14601)

## 2026-11-19 copy located and read
- arXiv PDF https://arxiv.org/pdf/2004.14601 (v3, 30 Oct 2020), HTTP 200, 11 pages. Read in full incl. appendix table.
- TILT: train AWD-LSTM on L1, freeze LSTM, finetune only the linear embedding layers on Spanish (L2), test Spanish ppl. n = 5 seeds.
- Means (appendix): uniform 513.66, Zipf 493.15, music 256.15, code 139.11, nesting parens 170.98, flat parens 170.30; Spanish L1 52.33.
- Doubts: body text gives flat parens 170.03 and code 139.10, appendix 170.30 and 139.11 (small internal inconsistency).
- Measure is zero-shot-structure ppl with frozen LSTM, not cost/speed of later learning; no full-finetune or data-efficiency condition.
- Corpus sizes not matched: music 23M tokens, code 9.5M, others 100M.

## 2026-11-19 bearings searched
- No LIT/NOTE for this work in the record (grep for author, arXiv id, title: none).
- Named: CLAIM-756 (qualifies weakly: measure is not cost of later learning), QUESTION-039 (background), TERM-131 (background), THEORY-tmpk9cmk (Hu et al.: partial tension, flat crossing pairs = nesting here vs. hierarchy "crucial" there; different architecture and measure).
- Others: TERM-117, CLAIM-596 (end-state measure cannot tell head start from speed-up), THEORY-tmpd6l4a, THEORY-tmp0lbb1, THEORY-tmprqq7k, QUESTION-495, CLAIM-754, THEORY-967 (bracket-matching head, background).
- 36 quotes checked by script against downloaded text: all found.
