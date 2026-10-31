---
status: Active
status_note: >-
  read 2026-10-31 ([NOTE-tmpbslp3](../notes.d/NOTE-tmpbslp3.md)), body and appendices, with the proofs
  skimmed; worth reading for an exact account of iterated
  reconstruction through fresh low-rank views, in which forgetting the
  ancestor first improves and then destroys fidelity to the world, and
  every student fits its teacher exactly on its own sample
  ([THEORY-tmpp515i](../theory.d/THEORY-tmpp515i.md)).
title: 'Why Self-Training Helps and Hurts: Denoising vs. Signal Forgetting'
version: 2
history:
- version: 1
  date: '2026-10-31'
  note: >-
    Filed, not read, from A16 of the exchange "Analyze nucleation
    concepts" (2026-10-30 to 31). Citation checked against arXiv (v1
    2026-02-15); A16 named it as "Wu, Yang & Sun (2026)" without an
    identifier. The summary follows the abstract and the exchange's
    description; a reading should check it first.
- version: 2
  date: '2026-10-31'
  note: >-
    Read from the arXiv preprint 2602.14029v1, 29 pp., in NOTE-tmpbslp3;
    proofs of Appendices C–F skimmed. Status Deferred → Active. The
    citation stands. The summary is rewritten from the text. The
    registration's summary and A16's description were accurate. Theorem
    3.2 was checked by Monte Carlo. THEORY-tmpp515i filed. The
    anthology-candidate flag stays.
tags:
- learning-theory
- mathematical-statistics
- anthology-candidate
date: '2026-10-31'
published: '2026-02-15'
arxiv: '2602.14029'
first_author: 'Wu'
keywords:
- 'self-training'
- 'denoising'
- 'signal forgetting'
- 'deterministic equivalents'
implementations: []
summary: >-
  Wu, Yang & Sun (2026). In overparameterized linear regression,
  iterated self-training with fresh covariates, noiseless pseudo-labels
  and minimum-norm students projects the estimate each round onto the
  row space of a new design. Noise from the first fit decays at
  (1 + τ)⁻¹ per round, and signal along a direction of variance s at
  s/(s + τ). Risk is U-shaped under anisotropy, monotone under isotropy,
  and tends to that of predicting zero. Deterministic equivalents
  concentrate uniformly over ridge parameters, and an iterated GCV
  picks the stopping round. One CIFAR-10 experiment shows the U-shape.
---

# LIT-tmpcewsq: Why Self-Training Helps and Hurts: Denoising vs. Signal Forgetting

Wu, M., Yang, A. Y., & Sun, Q. (2026). Why self-training helps and hurts: Denoising vs. signal forgetting. arXiv:2602.14029.

Read in [NOTE-tmpbslp3](../notes.d/NOTE-tmpbslp3.md).

## Why this is here

With [LIT-tmptkqrv](LIT-tmptkqrv.md), A16's evidence that recursive reconstruction can lose as well as correct. It is the formal neighbour of [CLAIM-081](../claims.d/CLAIM-081.md) and [CLAIM-270](../claims.d/CLAIM-270.md) on forgetting the ancestor. The reading makes the neighbourhood precise. The chain forgets its ancestor entirely, and since the ancestor carries noise, forgetting it first improves fidelity to the source and then destroys it. A single projection repeated would change nothing; the loss comes from drawing a new one each round ([THEORY-tmpp515i](../theory.d/THEORY-tmpp515i.md)). Each student also fits its teacher exactly on its own sample while differing from it elsewhere, an illustration for [CLAIM-tmpekkm7](../claims.d/CLAIM-tmpekkm7.md).
