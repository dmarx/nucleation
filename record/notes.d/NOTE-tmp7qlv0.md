---
status: Read
paper: LIT-tmp8pcca
title: 'Belrose, Ostrovsky, McKinney, Furman, Smith, Halawi, Biderman and Steinhardt — The tuned lens'
version: 1
history:
- version: 1
  date: '2026-11-21'
  note: >-
    Read on 2026-11-21 by a delegated reader from arXiv 2303.08112v6 (11
    Nov 2025): the abstract, §§1–6, Appendices C, C.1 and D.1 in full; A
    and B by captions; E skimmed. v6 notes that earlier lenses were
    undertrained and the experiments were not redone. Running notes on the
    branch claude/readers/tuned-lens (ADR-108). Quotations the filing
    leans on rechecked by the filer by script against the downloaded text.
date: '2026-11-21'
summary: >-
  Per-layer affine translators decode each hidden state into a next-token
  distribution whose perplexity falls smoothly with depth; residual
  updates align with the negative loss gradient at every layer;
  hidden-state covariance drifts apart with layer separation, so the
  refinement is of one prediction, not of one fixed representation. In
  Pythia 6.9B only the first layer is crucial when deleted.
---
<!-- inactive-ok-file: ADR-108 — Proposed; cited in the readings of 2026-11-21 -->
<!-- inactive-ok-file: CLAIM-tmp2yj4t CLAIM-tmpcvuyr — Proposed, Deferred or new; filed in this contribution of 2026-11-21 or the ones it builds on -->

# NOTE-tmp7qlv0: Belrose, Ostrovsky, McKinney, Furman, Smith, Halawi, Biderman and Steinhardt — The tuned lens

## Contribution

The tuned lens; causal basis extraction and stimulus–response alignment as tests of fidelity; measurements of residual–gradient alignment and of layer deletion in transformers.

## Key results

1. **Iterative inference** (§1): each layer is read "as performing an incremental update to a latent prediction of the next token", with "each successive layer achieving lower perplexity".
2. **Gradient-aligned updates** (App. C): "each layer reliably updates the hidden state in a direction of decreasing loss"; in Pythia 6.9B the residual–gradient cosine is negative at every layer at least 95% of the time, with magnitudes at most 0.05.
3. **Representational drift** (§1, §3, Fig. 6): covariance matrices of hidden states at different layers "drift apart as the number of layers separating them increases"; removing two outlier dimensions introduced at layer 4 "reveals smooth representational drift with depth"; the final layer often changes sharply.
4. **Deletion** (App. C.1): in Pythia 6.9B "only the very first layer is crucial for performance".
5. **Authors**: eight, including Stella Biderman and Jacob Steinhardt, whom the record's entry had omitted.

## Assumptions and concepts

Pre-LayerNorm models; the final distribution as target; features as directions; mean ablation; first-order argument for iterative inference. Concepts: tuned lens, translator, representational drift, transfer penalty, model stitching, prediction depth.

## Bearing on the record

- **[CLAIM-tmpcvuyr](../claims.d/CLAIM-tmpcvuyr.md)** (supports; qualifies). Smooth perplexity, gradient-aligned updates and cheap deletion beyond layer 1 support refinement; but what is refined is one prediction, readable through a per-layer affine map, while the representation's basis drifts. Version 2 says "refining one prediction". No stages appear in prediction quality.
- **[CLAIM-tmp2yj4t](../claims.d/CLAIM-tmp2yj4t.md)** (corroborates the systematic row): residual updates aligned with −∇L at every layer are a correlated, biased contribution, small in magnitude; smooth drift with layer separation is consistent with accumulation along a restatement chain; the outlier onset and final-layer jump are discontinuities a uniform model would not predict.
- **[LIT-tmp8pcca](../literature.d/LIT-tmp8pcca.md)**: the anthology holds this paper as [ANTH-LIT-569](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-569.md); cited on the entry.

## Limitations

Undertrained lenses by the authors' own v6 note; many results on single Pythia models; tiny alignment magnitudes; the method targets pre-LN models.
