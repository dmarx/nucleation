---
status: Active
status_note: >-
  read in full 2026-10-31 ([NOTE-tmp5vh75](../notes.d/NOTE-tmp5vh75.md)); its "tempered posterior" is a
  temperature, the posterior at effective sample size 1/D_ξ within a
  region of constant diffusion, and the "accessibility" that would make
  SGD differ from Bayes across regions is not derived but fitted
  ([THEORY-tmpe0idn](../theory.d/THEORY-tmpe0idn.md)); its sub-diffusion fits are filed as Proposed
  ([THEORY-tmptkuok](../theory.d/THEORY-tmptkuok.md)).
title: 'Almost Bayesian: The Fractal Dynamics of Stochastic Gradient Descent'
version: 2
history:
- version: 1
  date: '2026-10-31'
  note: >-
    Filed, not read, from A4 and A14 of the exchange "Analyze
    nucleation concepts" (2026-10-30 to 31). Citation checked
    against arXiv (v1 2025-03-28). A4 cited the ICLR 2026
    proceedings version, "Almost Bayesian: Dynamics of SGD Through
    Singular Learning Theory"; the U1–U6 reader found it in the ICLR
    2026 proceedings, and the arXiv record carries the older title.
    `published:` takes the arXiv date (ADR-002). The summary follows
    the abstract and the exchange's description; a reading should
    check it first.
- version: 2
  date: '2026-10-31'
  note: >-
    Read in full from the arXiv preprint 2503.22478v2 (16 March 2026),
    38 pp., in NOTE-tmp5vh75; status Deferred → Active. A correction to
    v1's note: the v2 PDF is the ICLR 2026 camera-ready ("Published as a
    conference paper at ICLR 2026") and carries the ICLR title; only the
    arXiv metadata keep the older one. The LIT title follows the
    metadata, as v1 decided. A second correction: "(if it exists)" is
    not in the v2 abstract or the arXiv abstract; it qualifies the local
    steady state in §3.4 (p. 6). The ICLR proceedings abstract was not
    checked. The summary is rewritten from the text.
tags:
- learning-theory
- loss-landscapes
- anthology-candidate
date: '2026-10-31'
published: '2025-03-28'
arxiv: '2503.22478'
first_author: 'Hennick'
keywords:
- 'stochastic gradient descent'
- 'singular learning theory'
- 'Bayesian posterior'
- 'accessibility'
- 'anomalous diffusion'
- 'fractional Fokker-Planck equation'
- 'local learning coefficient'
implementations: []
summary: >-
  Hennick & De Baerdemacker (2025; ICLR 2026). Models late-training SGD as
  sub-diffusion on a porous landscape: a time-fractional Fokker–Planck
  equation, the local learning coefficient as the medium's mass
  dimension, and a spectral dimension d_s fitted from weight
  displacement, R(t) ∝ t^(d_s/2λ) with d_s ≤ λ. Where an effective scalar
  diffusion D_ξ is constant on a region, the steady state is
  exp(−L/D_ξ), the posterior tempered to effective sample size 1/D_ξ.
  How mass is shared between regions is not derived; in one toy test the
  cluster masses of SGD solutions match an SGLD posterior after a fitted
  tempering scale. Displacement fits cover MNIST MLPs, TinyStories models
  and fine-tuned ImageNet convnets.
---
<!-- inactive-ok-file: QUESTION-tmpiir0l THEORY-tmptkuok — Open or Proposed; the question this bears on, and a THEORY filed from the reading -->

# LIT-tmp107c0: Almost Bayesian: The Fractal Dynamics of Stochastic Gradient Descent

Hennick, M., & De Baerdemacker, S. (2025). Almost Bayesian: The fractal dynamics of stochastic gradient descent. arXiv:2503.22478. Published at ICLR 2026 as "Almost Bayesian: Dynamics of SGD Through Singular Learning Theory".

Read in full in [NOTE-tmp5vh75](../notes.d/NOTE-tmp5vh75.md).

## Why this is here

A4 gave it as the strongest recent form of the SGD–Bayes connection, with "accessibility constraints" as what separates the two. That is the term [QUESTION-tmpiir0l](../questions.d/QUESTION-tmpiir0l.md) asks about. The reading finds less there than the question's title expects. Within a region the paper's steady state is a tempered posterior, so the correspondence it gives is between a noise scale and a sample size, as in Mandt et al. ([LIT-tmpwzrx7](LIT-tmpwzrx7.md)), and not between training time and sample size. Accessibility, the part that would make SGD's weighting of regions differ from the posterior's, is not derived ([THEORY-tmpe0idn](../theory.d/THEORY-tmpe0idn.md)). Phase transitions are explicitly outside its steady-state theory. Its displacement results bear on how SGD moves late in training ([THEORY-tmptkuok](../theory.d/THEORY-tmptkuok.md)).
