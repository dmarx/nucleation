---
status: Active
status_note: >-
  read 2026-11-05 (NOTE-tmpxbvec) from the arXiv v1 preprint, main text in
  full and supplementary information skimmed; the RSC version of record
  not read; worth reading for sequential deployment programmed by an
  ordering of energy barriers, and, for the anthology, as a training
  formulation for a data-free physics-informed network. Its main limits: a
  truss model that omits crease rotation stiffness, bending, buckling,
  friction and contact; the "FEA validation" uses the same truss
  abstraction, so only the one three-layer prototype tests the mechanics,
  and there the absolute barriers differ from prediction and are compared
  after normalizing to the bottom layer; inverse design returns one of
  many geometries.
title: 'Physics-informed neural networks for programmable origami metamaterials with controlled deployment'
version: 1
history:
- version: 1
  date: '2026-11-05'
  note: >-
    Registered and read on 2026-11-05 from the owner's pasted synthesis on
    FACT, rigidity, compliant mechanisms and origami (pasted 2026-11-04,
    written by another assistant), where it is cited as R5. The citation was
    checked by the reader against Crossref, OpenAlex and arXiv: Sukheon
    Kang, Youngkwon Kim, Jinkyu Yang and Seunghwa Ryu, Materials Horizons
    12(24), 10641–10655 (2025); arXiv 2508.13559, v1 19 August 2025, which
    is `published:` (Crossref gives only the year; OpenAlex's 1 January is a
    placeholder); PubMed 41257337. The synthesis's attribution is correct.
    Read from the arXiv v1 PDF (https://arxiv.org/pdf/2508.13559), 62 pages
    with the supplementary information; the RSC typeset version was not
    fetched, so differences from it are unchecked. Status Active.
tags:
- natural-sciences
- anthology-candidate
date: '2026-11-05'
published: '2025-08-19'
arxiv: '2508.13559'
doi: '10.1039/D5MH01607J'
first_author: 'Kang'
keywords:
- 'physics-informed neural networks'
- 'origami metamaterials'
- 'Kresling pattern'
- 'inverse design'
- 'bistability'
- 'energy barriers'
- 'sequential deployment'
implementations: []
summary: >-
  Kang, Kim, Yang & Ryu (2025). Conical Kresling origami is modelled as a
  truss of linear springs; a small network mapping height to twist is
  trained without data, by minimizing energy along the torque-free path,
  and jointly with the geometric parameters for inverse design from two
  stable heights and a barrier. Forward predictions match a beam-truss FEA
  (R² > 0.93) and inverse designs their targets (R² > 0.99). Three-layer
  stacks with ascending barriers fold bottom to top in FEA and in a scaled
  PET prototype, with barrier errors of −7.93% and −16.16% after
  normalization and residual energy the model lacks.
---
<!-- inactive-ok-file: THEORY-tmpb6xqr — Proposed; cited from the reading of Kang et al. (2025) as open -->

# LIT-tmpovo05: Physics-informed neural networks for programmable origami metamaterials with controlled deployment

Kang, S., Kim, Y., Yang, J. & Ryu, S. (2025). Physics-informed neural networks for programmable origami metamaterials with controlled deployment. *Materials Horizons* 12(24): 10641–10655. doi:10.1039/D5MH01607J. arXiv:2508.13559.

## Key takeaways

*From the reading, NOTE-tmpxbvec.*

- **Data-free.** Forward prediction and inverse design "without requiring
  pre-collected training data" (abstract).
- **Programming the curve.** "The inverse design routine specifies both
  target stable-state heights and separating energy barriers, enabling
  freeform programming of the entire energy curve."
- **Sequential deployment.** Each layer "folds in a predetermined order
  dictated by its barrier height", kept by "a sequence margin between
  adjacent barrier heights that exceeds expected experimental deviations".
- **Limited validation.** The FEA shares the truss abstraction; the one
  prototype shows the order, with barrier errors up to 16% after
  normalization.

## Standing in the record

Cited in the pasted synthesis on constraint architectures as R5, by its
bibliography only, under origami as resource-constrained reconfiguration.
It orders transitions by barrier height under a monotone load; it does not
treat whether a transition is reachable under a resource cap. Its central
contribution is a training formulation for a physics-informed network,
which is machine-learning practice, so it carries the
`anthology-candidate` flag. Filed from it: THEORY-tmpb6xqr.
