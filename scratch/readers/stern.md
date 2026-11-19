# Reader notes: stern (Stern, Rocktäschel, Locatelli, Ruis, "Rethinking Pre-pretraining", arXiv 2610.40051)

## 2026-11-19 Copy located and read
- arxiv.org/abs/2610.40051 (v1, 29 Oct 2026), arxiv.org/pdf/2610.40051 and arxiv.org/html/2610.40051 all fetched (HTTP 200). Read the PDF text in full; appendices A (data), D (hyperparameters) skimmed, B, C, E read.
- Main finding: compute-matched PPT (NCA, k-Dyck, DeclRef, code; C4 control) never beats pure FineWeb training in three regimes (data-constrained 100M tokens/1e18 FLOPs; data-unconstrained 1e18-9e18; over-Chinchilla 881M/50B).
- Additive compute (PPT on top of NL budget): k-Dyck and NCA help at 50M and 100M NL tokens; gain gone at 1B under spectral init.
- NCA reproduction of Lee et al.: 5.4% perplexity gain under original init; N(0,0.02) embeddings improve baseline 9.0% and close gap.
- Retention: PPT-distribution BPB rises after the phase boundary for NCA, k-Dyck and code; 5% interleaving keeps it. Code too, "progressively overwritten".
- Aryabumi et al. cited only as motivation for including code (intro), not tested or disputed. Hu et al. 2025 (2502.19249) is a main target: k-Dyck generated with their code; BLiMP sub-task gains "in line with" theirs; they dispute that priors persist.
- Three seeds per point.
