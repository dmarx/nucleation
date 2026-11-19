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
