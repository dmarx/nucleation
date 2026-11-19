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

## Bearings searched
- Record holds the work only in LEAD-tmpjdtrl item 3 ("domain upsampling late"): accurate, no LIT yet.
- CLAIM-756: weak/qualifying at most. No earlier acquisition lowering a later one's cost; the late phase is the acquisition, measured by final benchmark score at fixed 1T tokens. Base 0.8T run is a shared prefix, not varied.
- QUESTION-039: parallel on "the moment" (DU duration trade-off), not acquisition timing of a structure.
- THEORY-tmpd6smn (Liu et al.): contrasts. Liu: heavy late code mix ends worse than none (after fine-tuning, small models); Blakeney: late code+domain upsample helps at 7B (no fine-tuning). Different measures.
- THEORY-tmpk9cmk, tmpd6l4a, tmp0lbb1, tmplutfz: background/parallel; Blakeney is the opposite placement (specialized data last, not first).
- THEORY-2006 / CLAIM-758: background only (no later fine-tune measured).
- TERM-131: the dataset-ablation (sans math) is a counterfactual on a late acquisition, fits the term's counterfactual comparator for the late phase only.
- Quotes rechecked by script against the downloaded text (whitespace-normalized).
