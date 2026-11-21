---
number: 2140
status: Proposed
formerly:
- THEORY-tmpky55f
promote_when: >-
  An independent study, on at least one model family outside Pythia and
  GPT-NeoX, finding that affine per-layer probes trained by distillation
  give latent-prediction perplexity falling monotonically with depth, that
  residual updates have negative cosine with the loss gradient at most
  layers, and that hidden-state covariance similarity decreases with layer
  separation.
title: 'Belrose and colleagues show that in pre-LayerNorm transformer language models each layer''s hidden state can be decoded by an affine translator into a next-token distribution whose perplexity falls smoothly with depth, that residual updates align with the negative loss gradient at every layer, as iterative inference predicts, and that decoding needs a separate translator per layer because hidden-state covariance drifts apart with layer separation'
version: 1
tags:
- representation-learning
- learning-theory
- anthology-candidate
date: '2026-11-21'
source:
- LIT-2942
corroborates:
- CLAIM-767
summary: >-
  Depth as iterative refinement of a prediction, with the representation
  itself drifting ([CLAIM-771](../claims.d/CLAIM-771.md)); gradient-aligned updates as the
  systematic row of [CLAIM-767](../claims.d/CLAIM-767.md). Proposed until its promote_when is
  met.
---
<!-- inactive-ok-file: THEORY-104 — Proposed; cited in the readings of 2026-11-21 -->
<!-- inactive-ok-file: CLAIM-767 CLAIM-771 — Proposed, Deferred or new; filed in this contribution of 2026-11-21 or the ones it builds on -->

# THEORY-2140: Belrose and colleagues show that in pre-LayerNorm transformer language models each layer's hidden state can be decoded by an affine translator into a next-token distribution whose perplexity falls smoothly with depth, that residual updates align with the negative loss gradient at every layer, as iterative inference predicts, and that decoding needs a separate translator per layer because hidden-state covariance drifts apart with layer separation

## Source

Belrose, Ostrovsky, McKinney, Furman, Smith, Halawi, Biderman and Steinhardt, [LIT-2942](../literature.d/LIT-2942.md), read in [NOTE-2219](../notes.d/NOTE-2219.md) from arXiv 2303.08112v6 (11 Nov 2025).

## What was actually shown

§1, §3, Figure 6 and Appendices C and C.1 as quoted in the NOTE.

## What this does not say

Not that the representation is shared across layers; not stages; not beyond the models measured.

## Connections

[LIT-1534](../literature.d/LIT-1534.md) (Elhage and colleagues: the residual stream); [THEORY-104](THEORY-104.md); [THEORY-176](THEORY-176.md) (stitching); [ANTH-LIT-569](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-569.md) (the anthology's entry for this paper).
