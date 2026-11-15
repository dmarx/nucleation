---
status: Active
status_note: >-
  read 2026-11-15 (NOTE-tmpmpv2r) from the arXiv preprint, v1 (§§1–4.2,
  Tables 1–3, Algorithm 1; §4.3, the ablations and Appendices A–H
  skipped). Published at ICML 2026, PMLR 306, per the PDF footer and the
  arXiv comment. Worth reading here as an activation-space, data-
  conditioned account of LoRA merge interference: concatenate the LoRAs
  along rank and insert a fixed linear router, the least-squares solution
  for reconstructing each LoRA's output on its own task's inputs, which
  beats task arithmetic, TIES and DARE on the same rank budget in
  FLUX.1-dev. Bears on THEORY-107 as a non-coordinate remedy that wins
  where both were tried; it does not separate sign from scale.
title: 'SSR-Merge: Subspace Signal Routing for Training-Free LoRA Merging in Diffusion Models'
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Registered and read on 2026-11-15 from the owner's pasted
    continuation of the ChatGPT exchange "Explain String Theory", in A's
    turn on how model merging fails (merging LoRA subspaces by routing
    signals). Citation checked against the arXiv API: Zhengxuan Wei, Yi
    Dong, Zonghui Li, Xianhui Lin, Xing Liu, Hong Gu, Shaofeng Zhang,
    Wenbin Li and Qi Fan; v1 2026-06-09, which is `published:`; comment
    "Accepted at ICML 2026", and the PDF footer gives PMLR 306. A's
    "ICML 2026, demonstrated in diffusion models" is correct. No email
    address was sent to any service.
tags:
- loss-landscapes
- representation-learning
- anthology-candidate
date: '2026-11-15'
published: '2026-06-09'
arxiv: '2606.10617'
first_author: 'Wei'
keywords:
- 'LoRA merging'
- 'diffusion models'
- 'signal routing'
- 'subspace router'
- 'decorrelation'
- 'training-free'
- 'structural re-parameterization'
implementations: []
compared_against:
- LIT-675
summary: >-
  Wei et al. (2026), ICML. Merges K LoRAs of a diffusion model by
  concatenating them along the rank dimension and inserting a Kr × Kr
  router R = QG⁻¹ built from one calibration prompt per task, the
  least-squares solution for reconstructing each LoRA's output on its own
  task's inputs; R is absorbed into B, so the merge is one static LoRA.
  Task arithmetic is R = I. On FLUX.1-dev with nine subject LoRAs it keeps
  over 90% of single-LoRA fidelity and beats task arithmetic, TIES, DARE,
  RobustMerge and IterIS. Training-free but not data-free. Bears on
  THEORY-107 as an activation-space account of interference.
---
<!-- inactive-ok-file: THEORY-107 — Proposed; the coordinate account of merge interference this reading bears on -->

# LIT-tmpanxdy: SSR-Merge: Subspace Signal Routing for Training-Free LoRA Merging in Diffusion Models

Wei, Z., Dong, Y., Li, Z., Lin, X., Liu, X., Gu, H., Zhang, S., Li, W. &
Fan, Q. (2026). SSR-Merge: Subspace Signal Routing for Training-Free LoRA
Merging in Diffusion Models. *Proceedings of the 43rd International
Conference on Machine Learning*, PMLR 306. arXiv:2606.10617v1. Code:
github.com/nagara214/SSR-Merge (not fetched).

## Key takeaways

*From the reading, NOTE-tmpmpv2r.*

- **The reframing** (§1): "reframing model merging as signal routing
  rather than parameter arithmetic".
- **The router** (abstract, §3): it "employs an inverse correlation matrix
  to decorrelate mixed signals", and "a directional guide matrix steers
  these purified signals into their respective task-specific subspaces".
  Theorem 3.1: R minimizes Σ‖B_comb R Z_k − Y_k‖²_F.
- **Same budget** (§4): "Task Arithmetic, TIES, DARE, and SSR operate on
  the same collection of K low-rank updates; SSR only replaces identity
  routing with a statistics-derived router."
- **Fidelity** (Table 1, FLUX.1-dev, K = 9): DINO 0.6713 and CLIP 0.7850,
  against 0.6240 and 0.7520 for IterIS; SSR "consistently recovers over
  90.2% of the single-task oracle performance".
- **Composition** (Table 3): success rate 0.91, against 0.76 for task
  arithmetic and 0.69 for TIES.

## Standing in the record

A, in the exchange, says the paper "combines LoRA subspaces and
routes/decorrelates internal signals rather than merely adding their
parameters", in ICML 2026, demonstrated in diffusion models. The reader
found nothing wrong in it; it is close to the authors' own words. Two
things it leaves out matter here. The router is derived from data, one
calibration prompt per task, so the method is training-free but not
data-free. And "routing" is a fixed linear map absorbed into the weights,
not gating that depends on the input.

Its objective, layer-local reconstruction of each LoRA's output on its
own inputs, is the RegMean family, which TIES (LIT-675) compares against
and which this paper leaves out for numerical instability.
