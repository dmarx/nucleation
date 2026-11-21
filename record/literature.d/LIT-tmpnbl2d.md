---
status: Active
status_note: >-
  read 2026-11-21 ([NOTE-tmp92pjh](../notes.d/NOTE-tmp92pjh.md), Read) from arXiv 2308.12108v2; filed as
  [THEORY-tmpousrw](../theory.d/THEORY-tmpousrw.md). The source of the local learning coefficient estimator
  the record's singular-learning entries use.
title: 'The Local Learning Coefficient: A Singularity-Aware Complexity Measure'
version: 2
history:
- version: 1
  date: '2026-11-21'
  note: >-
    Filed, not read. Identifier checked on the arXiv API on 2026-11-21, no email address sent. Not held: no hit for the arXiv id or the title in record/literature.d (LIT-1535, the refined LLC, is a different work).
- version: 2
  date: '2026-11-21'
  note: >-
    Read in full from the arXiv preprint 2308.12108v2 (30 September 2024) in
    NOTE-tmp92pjh; status Deferred → Active; THEORY-tmpousrw filed. Venue:
    v1 gave 'AISTATS 2025 (PMLR 258)'. The copy read says 'Preprint. Under
    review.' and the arXiv record carries no journal reference, so the venue
    is not confirmed and is removed from the summary until checked; it was
    not checked elsewhere. The summary is rewritten from the reading.
tags:
- learning-theory
- loss-landscapes
- anthology-candidate
date: '2026-11-21'
published: '2023-08-23'
arxiv: '2308.12108'
first_author: 'Lau'
keywords: []
implementations: []
summary: >-
  Lau, Furman, Wang, Murfet & Wei, The Local Learning Coefficient: A
  Singularity-Aware Complexity Measure, arXiv 2308.12108 (v2, 2024; the 2025
  conference venue given at registration is not confirmed). Defines the
  local learning coefficient of a local minimum as the volume-scaling
  exponent of its low-loss set, and estimates it with SGLD as nβ*(E[Lₙ] −
  Lₙ(w*)) under a posterior tempered at β* = 1/log n and localized by a
  Gaussian of precision γ. Consistency is conjectured; calibrated only in
  noiseless deep linear networks up to 10⁸ parameters, mostly
  underestimating; elsewhere used for relative comparisons.
---
<!-- inactive-ok-file: ARG-tmpdvwy2 CLAIM-tmpcg4uu THEORY-tmpousrw — Proposed or Rejected entries filed on 2026-11-21 from the exchange "Rich Get Richer Power Laws" and from the readings of its works, or Deferred works not yet read -->

# LIT-tmpnbl2d: The Local Learning Coefficient: A Singularity-Aware Complexity Measure

Lau, Furman, Wang, Murfet & Wei. arXiv 2308.12108 (v2, 2024). The venue AISTATS 2025 (PMLR 258), given when it was registered, is not confirmed by the copy read.

## Standing in the record

Registered on 2026-11-21 from the exchange "Rich Get Richer Power Laws", where A cites it at A37 for the local learning coefficient as a measure of degeneracy. Read the same day ([NOTE-tmp92pjh](../notes.d/NOTE-tmp92pjh.md)) and filed as [THEORY-tmpousrw](../theory.d/THEORY-tmpousrw.md). It is the estimator behind [THEORY-1275](../theory.d/THEORY-1275.md) ([LIT-1894](LIT-1894.md)) and [THEORY-975](../theory.d/THEORY-975.md) ([LIT-1535](LIT-1535.md)), and bears on [CLAIM-tmpcg4uu](../claims.d/CLAIM-tmpcg4uu.md) ([ARG-tmpdvwy2](../arguments.d/ARG-tmpdvwy2.md)), [LEAD-tmpfrw11](../leads.d/LEAD-tmpfrw11.md) and [QUESTION-tmp7d1ws](../questions.d/QUESTION-tmp7d1ws.md).
