---
status: Active
status_note: 'read 2026-10-09 (NOTE-tmp2aqt4); worth reading for the result that posterior sampling from simulation alone, when (X, Y) can be drawn but the likelihood cannot be evaluated, is a Schrödinger bridge between the joint p(x, y) and a reference p_ref(x|y)p(y) with y held fixed along the path (Proposition 1), solvable by iterative proportional fitting with learned drifts (CDSB). Its first iteration is the ordinary conditional score-based model, so later ones refine it, and the reference end can be a cheap posterior approximation rather than noise. Gains over the conditional score model are at equal small step counts and are not uniform across metrics; it filters the Lorenz-63 model with 20 steps where the score model diverges.'
title: 'Conditional Simulation Using Diffusion Schrödinger Bridges'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read from arXiv v2 (26 June 2022, the UAI camera-ready): main text
    read closely; proofs and supplementary skimmed, not checked line by
    line (NOTE-tmp2aqt4). Details checked against arXiv (v1 submitted 27
    February 2022; v2 the UAI 2022 camera-ready, 29 pages). The PMLR
    volume was not checked separately. `published:` is the arXiv v1
    date. Not held in the Anthology of the SOTA as a LIT: a grep of its
    record/ (clone of 2026-10-09, commit 1cffe8f) for the identifier,
    the title and the authors found the work named only in prose inside
    other entries, or not at all.
tags:
- probabilistic-modeling
- mathematics
- anthology-candidate
date: '2026-10-09'
published: '2022-02-27'
arxiv: '2202.13460'
first_author: 'Shi'
keywords:
- 'Schrödinger bridge'
- 'conditional simulation'
- 'diffusion models'
- 'inverse problems'
- 'optimal filtering'
implementations: []
summary: >-
  Shi, De Bortoli, Deligiannidis & Doucet (2022), UAI, PMLR 180. Extends
  the Schrödinger-bridge formulation of diffusion generative modelling
  from unconditional to conditional simulation, applied to super-
  resolution, filtering in state-space models and refining pre-trained
  networks. Read: the extended-space bridge is proved; the empirical gains
  are at small step counts and mixed across metrics.
---

# LIT-tmplnel0: Conditional Simulation Using Diffusion Schrödinger Bridges

Yuyang Shi, Valentin De Bortoli, George Deligiannidis and Arnaud Doucet
(2022), *UAI 2022*, PMLR 180 —
[ARXIV-2202.13460](https://arxiv.org/abs/2202.13460)

## Key takeaways

- **The construction.** Conditional simulation, sampling p(x|y_obs) when
  only (X, Y) can be simulated, cannot use a bridge to the posterior
  directly, since the posterior cannot be sampled. The paper poses instead
  the bridge between the joint p(x, y) and p_ref(x|y)p(y), with y frozen
  along the path, and proves it is the average over y of the per-
  observation bridges (Proposition 1). Iterative proportional fitting then
  splits into conditional forward and backward chains in x, trainable with
  De Bortoli et al.'s Diffusion SB losses with y as an extra input
  (Proposition 2, Algorithm 1).
- **Refining the score model.** The first IPF iteration is the
  conditional score-based model (CSGM); later ones correct its bias. The
  data-end error of the n-th iterate is at most 2/n times the KL from the
  initial noising process to the bridge (Proposition 3), which argues for
  a y-dependent forward process.
- **Informed references.** The reverse process can start from an
  approximation to the posterior: an upsampled low-resolution image, an
  EnKF Gaussian, or a pre-trained SRFlow model, which a short bridge
  (N = 10) then refines (FID 30.92 to 15.00 on CelebA 8× super-resolution,
  at a small cost in PSNR).
- **Evidence.** Sharper 2D posteriors than a monotone GAN; BOD posterior
  moments closer to MCMC than MGAN or inverse transport on most
  statistics; better image metrics than CSGM at equal small N in most but
  not all cells (Table 2); Lorenz-63 filtering at N = 20 where CSGM
  diverges, with the advantage gone at N = 100.
- **Limits** the authors state: the minimal step count is unknown in
  practice, atypical observations are poorly served by amortization, and
  each filtering step solves a new bridge.

## Standing in the record

Filed on 2026-10-09 at the owner's request, as one of the works in the
reference list of the owner's working manuscript (October 2026) that the
record did not yet hold. See the curation entry of that day. It is a
machine-learning paper an anthology topic could hold (generative-modeling,
analysis-and-evaluation), so it carries the `anthology-candidate` flag
([ADR-005](../decisions.d/ADR-005.md)); it is here because the owner asked for
the manuscript's references to be filed in this record.
