---
status: Active
status_note: >-
  read 2026-10-31 (NOTE-tmpyxfno; appendices B, C1, C3, C4 skimmed); worth
  reading as the fullest working of the evidence-as-partition-function
  dictionary with sample size as inverse temperature: generalization
  error as equipartition, a "learning capacity" equal to K/2 in regular
  and to the RLCT in singular models (THEORY-tmp5nt8h), and a
  sample-size-dependent prior that reproduces AIC. The dictionary is
  formal; it has no physical currents or dissipation.
title: 'Correspondence between thermodynamics and inference'
version: 2
history:
- version: 1
  date: '2026-10-31'
  note: >-
    Filed, not read, from A14 of the exchange "Analyze nucleation
    concepts" (2026-10-30 to 31). Citation checked against Crossref
    (PRE 99, 052140, 2019-05-30) and arXiv (v1 2017-06-05, titled
    "On the correspondence between thermodynamics and inference");
    `published:` takes the arXiv date (ADR-002). The summary follows
    the abstract and the exchange's description; a reading should
    check it first.
- version: 2
  date: '2026-10-31'
  note: >-
    Read in NOTE-tmpyxfno from arXiv 1706.01428v5 (body and appendix A in
    full; appendix B and the worked derivations of appendix C skimmed,
    C2 read). Status Deferred → Active. The citation stands. The summary
    is rewritten from the text. The registration's "model complexity as
    an entropic term in a free energy" is right for the free energy; the
    paper's new quantities are the learning capacity and the Gibbs
    entropy. Tags: mathematical-statistics and model-comparison put
    first, as what the paper is about; anthology-candidate added
    (ADR-005), since it recommends a prior for model selection.
    Produces THEORY-tmp5nt8h.
tags:
- mathematical-statistics
- model-comparison
- thermodynamics
- anthology-candidate
date: '2026-10-31'
published: '2017-06-05'
arxiv: '1706.01428'
doi: '10.1103/PhysRevE.99.052140'
first_author: 'LaMont'
keywords:
- 'Bayesian inference'
- 'statistical mechanics'
- 'free energy'
- 'model selection'
- 'learning capacity'
- 'equipartition'
- 'objective prior'
implementations: []
summary: >-
  LaMont & Wiggins (2019). Treats the Bayesian evidence as a partition
  function with sample size N as inverse temperature and derives the
  thermodynamic quantities. The internal energy is the leave-one-out
  predictive loss, whose excess K/2N is equipartition. The heat capacity
  becomes a learning capacity, K/2 in a regular model and the learning
  coefficient in a singular one, lower where the prior or discreteness
  fixes parameters ("freeze-out"), proposed as the definition of
  sloppiness. A prior chosen to make the Gibbs entropy zero is
  Jeffreys-like, depends on N, reproduces AIC and avoids the
  Lindley–Bartlett paradox in one simulation.
---

# LIT-tmpayntj: Correspondence between thermodynamics and inference

LaMont, C. H., & Wiggins, P. A. (2019). Correspondence between thermodynamics and inference. *Physical Review E*, 99, 052140.

Read in NOTE-tmpyxfno.

## Why this is here

A14's starting point for setting SLT's e^{-nK} beside a physical e^{-ΩV}. A14 itself kept them apart: the same statistical geometry does not fix the same physical currents or dissipation. Bears on THEORY-087. The reading bears A14's caution out. The paper's temperature is a sample size, and its dictionary has no dynamics, so nothing in it corresponds to a current, a housekeeping dissipation or an escape path, which are what LIT-tmpm46ks and LIT-tmp24302 attach to maintained physical states. What it does give THEORY-087 is a second derivative of the Occam penalty with an equipartition reading (THEORY-tmp5nt8h). That derivative approaches the RLCT only logarithmically when the multiplicity exceeds one, as in CASE-152's model.
