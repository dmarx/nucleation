---
status: Active
status_note: >-
  read 2026-10-26 (NOTE-tmpueby3) in full, from the arXiv PDF of v1;
  worth reading as the record's first developmental use of the learning
  coefficient, for per-head trajectories that separate attention heads by
  function (THEORY-tmp9uzkw), and for its observations of heads changing
  role as circuits form (THEORY-tmp1dufu, Proposed). Read it knowing that
  it is one two-layer attention-only model with three appendix seeds, that
  the estimates are trusted only for their ordering, that cluster counts
  were chosen by eye, and that nothing is predicted before it happens.
title: 'Differentiation and Specialization of Attention Heads via the Refined Local Learning Coefficient'
version: 2
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed, not read. At T24 the reply says "developmental interpretability
    research has tracked attention-head specialization" and "existing
    research using refined local learning coefficients has already examined
    progressive attention-head differentiation", with no author or title.
    The record's reading of T24 named this paper from memory; the lookup
    confirmed it. Checked on 2026-10-26 against the arXiv record: George
    Wang, Jesse Hoogland, Stan van Wingerden, Zach Furman and Daniel Murfet,
    arXiv 2410.02984, v1 submitted 3 October 2024, which is `published:`;
    the ICLR 2025 proceedings list it. The summary follows the arXiv
    abstract.
- version: 2
  date: '2026-10-26'
  note: >-
    Read in full (NOTE-tmpueby3) from the arXiv PDF of 2410.02984v1.
    Status Deferred → Active. Two accounts filed: THEORY-tmp9uzkw (Active)
    and THEORY-tmp1dufu (Proposed). The summary is checked against the
    reading and kept.
tags:
- learning-theory
- loss-landscapes
- representation-learning
- anthology-candidate
date: '2026-10-26'
published: '2024-10-03'
arxiv: '2410.02984'
first_author: 'Wang'
keywords:
- 'local learning coefficient'
- 'refined LLC'
- 'singular learning theory'
- 'developmental interpretability'
- 'attention heads'
- 'multigram circuit'
implementations: []
summary: >-
  Wang, Hoogland, van Wingerden, Furman & Murfet (2024), arXiv:2410.02984,
  ICLR 2025. Refined variants of the local learning coefficient, a
  complexity measure from singular learning theory, are applied to
  individual components of a two-layer attention-only transformer, tracing
  how attention heads progressively differentiate into distinct functional
  roles during training, what data they specialize to, and a previously
  unidentified multigram circuit (abstract).
---
<!-- inactive-ok-file: THEORY-tmp1dufu — Proposed; an account filed from this reading, cited as open -->
<!-- inactive-ok-file: LIT-354 — Unavailable; named as the record's only holding on singular learning theory, nothing here rests on it -->

# LIT-tmpa32mr: Differentiation and Specialization of Attention Heads via the Refined Local Learning Coefficient

Wang, G., Hoogland, J., van Wingerden, S., Furman, Z. & Murfet, D. (2024).
Differentiation and specialization of attention heads via the refined local
learning coefficient. *ICLR 2025*. arXiv:2410.02984.

Read in full on 2026-10-26 (NOTE-tmpueby3). The summary is checked
against the reading.

## Why this is here

Cited at T24 as prior art for components of a network becoming
differentiated over training. The record held singular learning theory only
through Watanabe ([LIT-354](LIT-354.md), Unavailable) and the WBIC ([LIT-616](LIT-616.md)), and nothing
from developmental interpretability. It bears on [QUESTION-tmpivbso](../questions.d/QUESTION-tmpivbso.md) and on
[QUESTION-039](../questions.d/QUESTION-039.md).
