---
status: Active
status_note: >-
  read in full 2026-11-15 ([NOTE-tmpwodpq](../notes.d/NOTE-tmpwodpq.md)) from arXiv v4 (22 pp.,
  NeurIPS 2023). Worth reading as the linear, second-moment counterpart
  of the record's information-theoretic erasure results: linear
  guardedness is exactly zero cross-covariance, and one closed-form
  oblique projection is the least edit achieving it under every
  inner-product norm.
title: 'LEACE: Perfect linear concept erasure in closed form'
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Registered and read on 2026-11-15 at the owner's request ("File LEACE
    too if we don't already have that one"). Checked first: no LIT held
    the arXiv id or title; LEACE was discussed in LIT-963 and NOTE-820
    only. Citation from the arXiv API and the PDF: Nora Belrose, David
    Schneider-Joseph, Shauli Ravfogel, Ryan Cotterell, Edward Raff and
    Stella Biderman, NeurIPS 2023; v1 submitted 2023-06-06, which is
    `published:`. Read by a delegated reader; the filer string-matched
    every quotation used and checked the central theorems numerically
    (NOTE-tmpwodpq).
tags:
- information-theory
- representation-learning
- anthology-candidate
date: '2026-11-15'
published: '2023-06-06'
arxiv: '2306.03819'
first_author: 'Belrose'
keywords:
- 'concept erasure'
- 'linear guardedness'
- 'cross-covariance'
- 'oblique projection'
- 'whitening'
- 'concept scrubbing'
- 'amnesic probing'
implementations:
- 'EleutherAI concept-erasure (github.com/EleutherAI/concept-erasure)'
summary: >-
  Belrose, Schneider-Joseph, Ravfogel, Cotterell, Raff & Biderman (2023),
  NeurIPS. No linear predictor under any convex loss beats a constant at
  predicting a concept Z from X if and only if every class has the same
  mean, that is, the cross-covariance Σ_XZ is zero; an affine edit Px + b
  achieves this if and only if P annihilates colsp(Σ_XZ). The least such
  edit, in mean squared distance under every inner-product norm at once,
  is one closed-form oblique projection: whiten, project out the whitened
  cross-covariance directions, unwhiten. Applied layer by layer
  ("concept scrubbing") to erase part of speech, it raises LLaMA and
  Pythia perplexity sharply where a random erasure of equal rank does
  not. Linear only, by the authors' own statement.
---

# LIT-tmpme1pw: LEACE: Perfect linear concept erasure in closed form

Nora Belrose, David Schneider-Joseph, Shauli Ravfogel, Ryan Cotterell,
Edward Raff and Stella Biderman, "LEACE: Perfect linear concept erasure in
closed form", NeurIPS 2023; arXiv:2306.03819.

## Key takeaways

*From the reading, [NOTE-tmpwodpq](../notes.d/NOTE-tmpwodpq.md).*

- **Linear guardedness is a second-moment condition.** The conditions
  "are all equivalent" (§3), among them that "Every component of X has
  zero covariance with every component of Z".
- **Which edits guard.** r(x) = Px + b guards "if and only if the
  columns of the cross-covariance matrix ΣXZ are contained in the null
  space of P" (Thm 4.1).
- **The least edit.** P* = I − W⁺P_{WΣXZ}W, with W the whitening, and
  "there is a single erasure function that minimizes all such norms
  simultaneously" (Thms 4.2–4.3). It "is not an orthogonal projection in
  general" but an oblique one. A filer's numerical check confirms all
  three properties.
- **Scrubbing part of speech** from every layer of LLaMA 7B raises bits
  per byte from 0.69 to 1.73, against 0.69 for a random erasure of the
  same rank (Table 1). The authors' reading: "autoregressive language
  models heavily rely on linearly encoded part-of-speech information".
- **Only linear.** "We conjecture that it is intractable to
  nondestructively edit X so as to prevent a general nonlinear adversary
  from recovering Z" (§7).

## Standing in the record

Filed on 2026-11-15 at the owner's request, alongside MuEdit ([LIT-tmpy7s15](LIT-tmpy7s15.md)) and
AlphaEdit ([LIT-tmpyijzd](LIT-tmpyijzd.md)), which also edit by projection (onto null spaces of preserved
keys). The paper itself makes no connection to model editing.

The record already discussed LEACE without holding it. Chowdhury et al.
([LIT-963](LIT-963.md), [NOTE-820](../notes.d/NOTE-820.md), [THEORY-281](../theory.d/THEORY-281.md)) compare against it, and report a
nonlinear boundary surviving it on a toy; LEACE's own §7 grants that gap.
Its guardedness is Xu et al.'s V-information at zero for linear V
([LIT-1309](LIT-1309.md), [NOTE-1048](../notes.d/NOTE-1048.md)), and [THEORY-846](../theory.d/THEORY-846.md)'s point that computation can create
usable information is why linear erasure does not settle nonlinear
access.

The method, debiasing representations, is machine-learning practice and
carries the `anthology-candidate` flag. Its theorems are mathematics and
are filed here.
