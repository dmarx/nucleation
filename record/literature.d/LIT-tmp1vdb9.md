---
status: Active
status_note: >-
  read in full 2026-10-15 from the authors' arXiv preprint, latest version v2 of
  16 March 2018 (arxiv.org/pdf/1711.08513, 40 pp.); the ICML version (PMLR 80:1939–1948,
  proceedings.mlr.press/v80/hebert-johnson18a/hebert-johnson18a.pdf, with a supplement)
  was fetched and its definitions and theorem statements compared, not read in full.
  Worth reading as the source definition of multicalibration: calibration required
  on every set in a collection C of large, efficiently identifiable subpopulations;
  a patching algorithm that reaches it from O(log|C|/α^{11/2}γ^{3/2}) samples in
  time linear in |C|, with a circuit of size O(s/α⁴γ); learning it equivalent to
  weak agnostic learning of C, and so hard for rich C under cryptographic assumptions;
  and calibration on any predictor's level sets at almost no cost in squared error.
  Its multi-AE (accuracy in expectation on every S in C) is what later work calls
  multiaccuracy; the paper does not use that word. For [QUESTION-tmpadry4](../questions.d/QUESTION-tmpadry4.md) it supplies
  adequacy relative to a class of observers in correlation form (a violation is
  a set in C correlating with the residual), but it states no indistinguishability
  theorem, no distinguishing advantage and nothing from signal detection; that framing
  is Dwork et al.'s ([LIT-tmpoyjmt](LIT-tmpoyjmt.md)). For [CLAIM-152](../claims.d/CLAIM-152.md) it is consistent and adds a second
  relativity: adequacy is relative to the outcome, to the features through p*, and
  to the class C, and even with all three fixed the adequate predictor is not unique.
  For [QUESTION-tmpdzpy2](../questions.d/QUESTION-tmpdzpy2.md) it gives a formal instance of budget-relative sufficiency
  in which representing an adequate predictor is cheap (only modestly larger than
  the observer class) while finding one can be hard, but it has no notion of an
  optimal partition and does not show one changing with the budget.
title: Calibration for the (Computationally-Identifiable) Masses
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: 'Filed, not read. Identifier checked on arXiv on 2026-10-15: v1 submitted
    22 November 2017; the arXiv title omits the "Multicalibration:" prefix of the
    ICML version. Not held in the Anthology of the SOTA: a grep of its record/ (clone
    of 2026-10-15, commit d1573d2) for the authors, title and identifier found nothing.
    Read the same day (NOTE-tmprrwdk).'
tags:
- learning-theory
- probabilistic-modeling
- anthology-candidate
date: '2026-10-15'
published: '2017-11-22'
arxiv: '1711.08513'
first_author: Hébert-Johnson
keywords:
- multicalibration
- calibration
- fairness
- computationally identifiable subpopulations
implementations: []
summary: >-
  Hébert-Johnson, Kim, Reingold and Rothblum (2018), ICML; arXiv 1711.08513. A predictor
  is α-multicalibrated on a collection C of subpopulations if, within every set
  S in C, the individuals given (roughly) the same prediction v have true probabilities
  averaging within α of v, except on an α-fraction of S. For any C whose sets have
  size at least γN, a simple iterative patching algorithm reaches multicalibration
  from O(log|C|/α^{11/2}γ^{3/2}) samples in time linear in |C|, and the result is
  a circuit only O(s/α⁴γ) in size when the sets of C are computed by size-s circuits.
  Learning it is equivalent, up to polynomial factors, to weak agnostic learning
  of C, so it is hard for rich C under cryptographic assumptions. Calibrating any
  predictor h on its own level sets as well as on C costs at most 6α in squared
  error. All guarantees are relative to the benchmark p*, which is itself defined
  relative to the features available, and they hold only for large sets; the paper
  offers no uniqueness for the predictor and does not state a theorem in indistinguishability
  form.
---

# LIT-tmp1vdb9: Calibration for the (Computationally-Identifiable) Masses

Hébert-Johnson, Ú., Kim, M. P., Reingold, O. and Rothblum, G. N. (2018). Multicalibration: Calibration for the (computationally-identifiable) masses. In *Proceedings of the 35th International Conference on Machine Learning (ICML 2018)*. [ARXIV-1711.08513](https://arxiv.org/abs/1711.08513)

## Key takeaways

Read in full ([NOTE-tmprrwdk](../notes.d/NOTE-tmprrwdk.md)). A predictor is α-multicalibrated on a collection C of subpopulations if, within every set S in C, the individuals given (roughly) the same prediction v have true probabilities averaging within α of v, except on an α-fraction of S. For any C whose sets have size at least γN, a simple iterative patching algorithm reaches multicalibration from O(log|C|/α^{11/2}γ^{3/2}) samples in time linear in |C|, and the result is a circuit only O(s/α⁴γ) in size when the sets of C are computed by size-s circuits. Learning it is equivalent, up to polynomial factors, to weak agnostic learning of C, so it is hard for rich C under cryptographic assumptions. Calibrating any predictor h on its own level sets as well as on C costs at most 6α in squared error. All guarantees are relative to the benchmark p*, which is itself defined relative to the features available, and they hold only for large sets; the paper offers no uniqueness for the predictor and does not state a theorem in indistinguishability form.

## Why this is here

The owner asked whether material downstream of computational indistinguishability, or the signal detection literature, could help with [CLAIM-tmpvdl53](../claims.d/CLAIM-tmpvdl53.md) and the bounded-observer questions. Read for [QUESTION-tmpadry4](../questions.d/QUESTION-tmpadry4.md). Calibration relative to the subsets a class of computations can pick out is the individuation-by-sufficiency of [CLAIM-152](../claims.d/CLAIM-152.md) with the observer's resources made explicit. Machine-learning theory, with the anthology flag; filed here for that question.

The reading ([NOTE-tmprrwdk](../notes.d/NOTE-tmprrwdk.md)) narrows this. The paper defines no distinguisher; its tests are first-moment checks on sets in the class intersected with level sets. The framing of adequacy as indistinguishability to a class is Dwork et al. 2021 ([LIT-tmpoyjmt](LIT-tmpoyjmt.md)). Even with outcome, features and class fixed, the adequate predictor is not unique, and finding one can be hard where representing one is cheap.
