# Reader notes: music (Papadimitriou & Jurafsky 2020, arXiv 2004.14601)

## 2026-11-19 copy located and read
- arXiv PDF https://arxiv.org/pdf/2004.14601 (v3, 30 Oct 2020), HTTP 200, 11 pages. Read in full incl. appendix table.
- TILT: train AWD-LSTM on L1, freeze LSTM, finetune only the linear embedding layers on Spanish (L2), test Spanish ppl. n = 5 seeds.
- Means (appendix): uniform 513.66, Zipf 493.15, music 256.15, code 139.11, nesting parens 170.98, flat parens 170.30; Spanish L1 52.33.
- Doubts: body text gives flat parens 170.03 and code 139.10, appendix 170.30 and 139.11 (small internal inconsistency).
- Measure is zero-shot-structure ppl with frozen LSTM, not cost/speed of later learning; no full-finetune or data-efficiency condition.
- Corpus sizes not matched: music 23M tokens, code 9.5M, others 100M.
