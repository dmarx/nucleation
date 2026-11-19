# Reader notes: opper (Opper, Morrison, Siddharth, arXiv 2311.00128)

## 2026-11-19: copy located and read
- arXiv PDF v2 (https://arxiv.org/pdf/2311.00128), 200, 6 pages + appendix; also arXiv HTML fetched (200). Lawful (arXiv preprint). Text extracted with pdftotext; kept in scratchpad, not here.
- Read in full: abstract, sections 1-12, appendices A-B.
- First impressions: BabyBERTa variant (8 layers, hidden 512), BabyLM strict-small (~10M), 120k steps, 3 seeds. Grammar measure: BLiMP ("original") plus held-out zero-shot tasks. Curricula: sequence-complexity (entropy, unigram, block) all fail to beat random sampling; speech-only beats text-only at 40k steps; speech->all ~ random (67.74 vs 68.21 overall); corpus simple->complex 68.77 vs random 68.21 vs reverse 66.72; control corpus (AO-Childes+CBT+Wikipedia) curriculum 67.28 vs random 66.38.
- The "proportion of training steps, not tokens" line is an interpretation (lines vs tokens: speech 80% of lines, 56% of tokens), not a separately manipulated variable.
- No measurement of later learning of other data (no loss on text/domain after speech first). Not the owner's recalled result.
