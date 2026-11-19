# Reader notes: stern (Stern, Rocktäschel, Locatelli, Ruis, "Rethinking Pre-pretraining", arXiv 2610.40051)

## 2026-11-19 Copy located and read
- arxiv.org/abs/2610.40051 (v1, 29 Oct 2026), arxiv.org/pdf/2610.40051 and arxiv.org/html/2610.40051 all fetched (HTTP 200). Read the PDF text in full; appendices A (data), D (hyperparameters) skimmed, B, C, E read.
- Main finding: compute-matched PPT (NCA, k-Dyck, DeclRef, code; C4 control) never beats pure FineWeb training in three regimes (data-constrained 100M tokens/1e18 FLOPs; data-unconstrained 1e18-9e18; over-Chinchilla 881M/50B).
- Additive compute (PPT on top of NL budget): k-Dyck and NCA help at 50M and 100M NL tokens; gain gone at 1B under spectral init.
- NCA reproduction of Lee et al.: 5.4% perplexity gain under original init; N(0,0.02) embeddings improve baseline 9.0% and close gap.
- Retention: PPT-distribution BPB rises after the phase boundary for NCA, k-Dyck and code; 5% interleaving keeps it. Code too, "progressively overwritten".
- Aryabumi et al. cited only as motivation for including code (intro), not tested or disputed. Hu et al. 2025 (2502.19249) is a main target: k-Dyck generated with their code; BLiMP sub-task gains "in line with" theirs; they dispute that priors persist.
- Three seeds per point.

## 2026-11-19 Bearings searched
- No LIT/NOTE for this work in the record yet; grep for 2610.40051 / title empty.
- THEORY-tmpk9cmk (Hu et al.): qualifies/contradicts in generality. Stern use Hu's k-Dyck generator; compute-matched k-Dyck never beats baseline under spectral init; additive k-Dyck gain persists at 1B NL tokens under the non-spectral inits (Hu's N(0,0.02) among them), vanishes under spectral. Also: their C4 control on a single LR schedule matches baseline, and they say prior NL controls with an optimizer reset and own schedule are handicapped -- bears on Hu's "matched NL first phase gets much of the saving". Head-persistence clause only indirectly touched (they measure PPT-distribution BPB, not heads).
- CLAIM-756: background/qualifies the empirical instances cited for it; does not touch the valuation claim.
- QUESTION-039: background (order matters; front-loaded acquisitions lost at boundary).
- CLAIM-758 (overconsolidation): parallel; forgetting at an abrupt distribution shift, not continued stabilization.
- THEORY-tmpd6l4a (Skill-it): parallel/supports mixing over sequencing; THEORY-tmp0lbb1 (curriculum): qualifies; THEORY-tmpd6smn (Liu midtraining, code early helps): qualifies/tension.
- Aryabumi et al. cited only as motivation for testing code; not tested or disputed.
- Open doubt: seeds for the Figure 5 retention runs are not stated specifically; runs untuned.
