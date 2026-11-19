# Reader notes: ito (Ito et al. 2022, arXiv 2209.07431, NeurIPS 2022)

## Copies (2026-11-19)
- arXiv PDF https://arxiv.org/pdf/2209.07431 (v3, 21 Sep 2022, comment "NeurIPS 2022"): 200, read in full.
- NeurIPS proceedings paper + supplemental PDF (proceedings.neurips.cc, hash d0241a0f...): 200. Word diff against arXiv: main text identical apart from header line; appendices moved to the supplement. DOI 10.52202/068431-2335.

## Reading
- Main text read in full, appendices A.1-A.10 read, supplementary figure captions read.
- ANN: 2 hidden layers x128 ReLU, Adam lr 0.001, dropout. Pretraining: Primitives (1-rule), Simple task (2-rule), Combined; each to 99%.
- Zero-shot on full C-PRO: Vanilla 23.25%, Primitives 31.51%, Simple 70.57%, Combined 92.15%.
- Sample saving: Vanilla trained on 60/64 contexts to >=90% "required up to 4.23x training samples to match the performance of the Combined model", counting pretraining samples. The one acquisition-cost number; "up to" with no spread given.
- Number of seeds not stated in text; t(38) one-sample df suggests 39 networks per condition (inference, not stated).
- Intervention on representations: none. Link PS -> generalization is correlational (r=0.88 across Combined pretraining). Only manipulation: order of pretraining reversed (SFig. 4) -> zero-shot "reduced to chance"; True/False output units "lesioned" after pretraining (a readout removal, not a test).

## Design verdict against LEAD-tmphfbq0
- (a) Later cost measured, with/without earlier learning: partly. One number (4.23x, "up to"), pretraining samples counted; but the comparison is Combined at zero C-PRO training vs Vanilla trained on 60/64 contexts to >=90% (held-out 96.02% vs Combined 92.15% on all 64), so the match is loose. SFig. 2/3 give incremental-acquisition sample curves (figures only; no numbers in text beyond "after learning only 7 C-PRO contexts").
- (b) Matched first stage / organizations: each pretraining regime run to 99% on its own tasks; regimes differ in PS (abstraction), not memorize/shortcut arms. Closest analogue: Reverse-combined (same pretraining tasks and 99% criterion, reversed order) -> zero-shot "reduced to chance" and more pretraining samples (SFig. 4); no PS or later-acquisition cost reported for it in text.
- (c) Intervention on learned representation: none. PS-generalization link is r=0.88 across the Combined pretraining trajectory; the authors read it causally ("directly facilitated").
- The search note's "no lesion" holds; the only "lesion" is removal of the pretraining True/False output units.

## Bearings (record searched)
- Not on the record (no LIT; no note cites 2209.07431). Search list in search.md names it.
- CLAIM-756: corroborates weakly (earlier acquisition lowers later cost, earlier cost counted; but the earlier step here is not loss-making on its own measure). THEORY-tmpk9cmk/tmpmy98s/tmpd6l4a/tmp0lbb1: parallel. THEORY-tmpmy98s has the weight-shuffle intervention Ito lacks.
- CLAIM-675/754: equal stopping criterion (90% on C-PRO training set) with different generalization -> an instance of equal present competence, different later capability (analogy, in a toy ANN).
- QUESTION-397/CLAIM-596/TERM-117: Ito measures zero-shot (state) and later sample counts (rate) but cannot separate head start from changed dynamics: background/analogy.
- THEORY-794/117, QUESTION-207 (Uselis): parallel on compositional generalization with linearly factored representations; Ito's PS is a related geometry measure.
- QUESTION-039: SFig. 4 order effect bears (order of acquisition matters).
