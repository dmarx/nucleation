# Reader notes: blakeney (arXiv 2406.03476)

## Copy
- arxiv.org/pdf/2406.03476 (v1, 5 Jun 2024; only version, v2 404). Fetched 2026-11-19, read in full (13 pp incl. appendix).
- Title/authors from text: "Does your data spark joy? Performance gains from domain upsampling at the end of training", Cody Blakeney, Mansheej Paul, Brett W. Larsen (equal), Sean Owen, Jonathan Frankle (Databricks Mosaic Research).

## Reading
- One 7B MPT model, 1T tokens, base mix (Table 2); domain upsampling (DU) = branch from base checkpoint, drop large-scale CC, continue to 1T (Table 4).
- 20% DU: MMLU 35.69->42.59, GSM8K 14.71->22.97, HE 17.23->23.40 (Table 5).
- Duration ablation 5/10/20/30% (Table 6): MMLU peaks 10%, Core Avg 20%, GSM8K/HE rise monotonically.
- NO run of the DU mix for the full 1T: the "late vs throughout" conclusion is inferred from the duration trend ("the mix used for DU should not be used for the entire duration").
- Dataset utility: 10% DU sans math subsets (Table 7) falls BELOW no-DU baseline on MMLU (29.71) and GSM8K (11.37).
- No seeds/repeats stated. "Order of magnitude cheaper" counts only the final phase; the shared base run is sunk cost.
