# Reader notes: tenney-pipeline (LIT-tmp166hz)

- 2026-11-21: located https://arxiv.org/pdf/1905.05950 (arXiv, lawful); fetched, PDF, 6 pages (v-latest), text via pdftotext. No barrier.
- 2026-11-21: read all 9 pages (arXiv v2, 9 Aug 2019): text, Fig 1/2 (BERT-large) and Fig A.2/A.3 (BERT-base) read from embedded images; Fig 3 read rendered; A.4-A.7 by caption only.
  - BERT-large CoG (s): POS 11.68, Consts 13.06, Deps 13.75, Ent 13.16, SRL 13.63, Coref 15.80, SPR 12.72, Rel 12.83.
  - BERT-large expected layer (Delta): POS 3.39, Consts 3.79, Deps 5.69, Ent 4.64, SRL 6.54, Coref 9.47, SPR 9.93, Rel 9.40.
  - K(Delta)/K(s) large: POS 1.60/0.19, Consts 1.57/0.83, Deps 1.15/0.87, Ent 1.61/0.06, SRL 1.31/0.46, Coref 0.60/0.50, SPR 0.33/0.01, Rel 0.50/0.01.
  - BERT-base CoG: 5.59, 6.01, 6.55, 6.86(Ent), 6.60(SRL), 7.96, 6.59, 6.80; Exp layer: 1.76, 2.38, 2.52, 2.42, 2.59, 3.62, 4.29, 4.16.
  - Observation: CoG of the 5 pipeline tasks all within ~layers 11.7-15.8 of 24; Deps/SRL/Ent ordering flips between metrics and models. Overlapping regions, not a stack.
