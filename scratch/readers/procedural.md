# Reader notes: procedural (Jiang et al., arXiv 2601.21725)

- 2026-11-19: located arXiv HTML at https://arxiv.org/html/2601.21725 (HTTP 200, no check). Downloaded to my scratchpad and converted to text (~15k words). Reading next.
- Read the full text (v2, 27 May 2026, CC BY 4.0), appendices A-N skimmed with tables read.
  - Setup: T1 procedural tokens then T2 semantic tokens; "additive" (T2 fixed) vs "substitutive" (cut T2, add small T1). Nothing frozen; embeddings reinitialised for semantic runs.
  - 124M GPT-2-small models on C4 / CodeParrot / DeepMind-Math; T2 = 655M / 1B / 1.6B (from steps x batch x length in App. E.3). 2.1M procedural tokens = 0.3/0.2/0.1%.
  - Savings: 45% C4 and 33% CodeParrot with 2.1M; 14% DM-Math needs 10.4M procedural tokens (~0.6%, not 0.1%). So the abstract's "0.1-0.3%" and "86%" do not refer to the same run for DM-Math.
  - Warm-up cost: not explicitly added into a FLOP total; text says saving of tokens "and thus FLOPs". Hyperparameter sweep over T1 configs is not costed.
  - Seeds: 10 for the small algorithmic probes; NO seed count stated for the semantic runs (Sec. 5, App. L).
  - 1.3B substitutive: 82M procedural tokens -> 66% of C4, 75% of CodeParrot.
  - Cites Papadimitriou & Jurafsky 2023 (2304.13060, "Injecting structural hints"), not 2004.14601. Hu et al. 2025 cited as prior; no head-to-head.
- Next: record bearings.
- Bearings searched. No LIT for this work on the record or on this branch yet; the only characterization is the lead brief's "reportedly 0.1-0.3% ... 55/67/86%", which is the abstract's and conflates two runs for DM-Math (86% needs 10.4M tokens, ~0.6%).
  - CLAIM-756: supports the premise (earlier acquisition lowers later cost; earlier cost tiny), not the valuation content. THEORY-tmpk9cmk: parallel, independent second instance with different procedures; lacks Hu's natural-language first-phase control. THEORY-tmpd6l4a, THEORY-tmp0lbb1: parallel. QUESTION-039: partial (amount/duration matters non-monotonically, App. I). TERM-117: application (vector productivity: Union hurts Sorting, helps Multiplication). CLAIM-754/758: some procedures raise later costs; overfitting the first phase impairs transfer. THEORY-1030 (Geva) background to the MLP finding.
  - Open doubt: whether substitutive points are read off one cosine-scheduled baseline curve or from re-scheduled shorter runs; the text does not say. No seed count for semantic runs.
- Quotes rechecked by script against the downloaded text. Report sent.
