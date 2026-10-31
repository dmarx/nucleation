---
status: Read
paper: LIT-tmpxo5z5
title: 'Mandt, Hoffman & Blei — variational analysis of constant SGD'
version: 1
history:
- version: 1
  date: '2026-10-31'
  note: >-
    Read in full from the arXiv preprint 1602.02666v1 (8 February 2016),
    11 pp. in the ICML two-column layout, fetched 2026-10-31. The ICML 2016
    proceedings version (pp. 354–363) was not compared. Text extracted with
    `pdftotext -layout`. I read the abstract, §§1–6, the supplement
    (Appendices A–C) and the reference list; the figures did not survive
    extraction, their captions and Table 1 did. It was read against the
    2017 JMLR paper (NOTE-tmpiaa2o), which contains all of it. The checks
    of Theorems 1–2 recorded there cover this paper's Theorems 1–2.
date: '2026-10-31'
summary: >-
  The first version of Mandt, Hoffman and Blei's argument: constant-rate SGD
  as an Ornstein–Uhlenbeck process near a non-degenerate optimum, whose
  Gaussian stationary distribution can be fitted to a Gaussian posterior by
  choosing the rate, batch size and preconditioner, with SGFS analysed the
  same way and a variational EM scheme for hyperparameters. Every result
  reappears, with the same numbers, in the 2017 JMLR paper, which adds
  momentum, constant-rate SGLD and iterate averaging; this one has nothing
  the later one lacks.
---
<!-- inactive-ok-file: QUESTION-tmpiir0l — Open; the question this reading bears on -->

# NOTE-tmph1our: Mandt, Hoffman & Blei — variational analysis of constant SGD

## Contribution

It introduces the device of the 2017 paper: treat constant-rate SGD as a
multivariate OU process under four assumptions (§2.2), take its Gaussian
stationary law (Eqs. 12–13), and minimise KL to the Gaussian posterior
(Eq. 14) over the optimiser's settings. Theorem 1 gives the optimal scalar
rate ε* = 2DS/(N tr BBᵀ) (Eq. 17), Theorem 2 the optimal preconditioner
(2S/εN)(BBᵀ)⁻¹ (Eq. 19), Corollary 1 the optimal diagonal one, and
Theorem 3 rederives SGFS's preconditioner (Eq. 25). The experiments are
the 2017 paper's §7.1 and §7.3: Table 1's KL values are identical.

## Key insight

As in the 2017 paper (NOTE-tmpiaa2o): the learning rate, batch size and
preconditioner choose a stationary distribution, and its scale ε/S is
what is matched to the posterior's 1/N.

## Assumptions

A1–A4 as in the 2017 paper: Gaussian gradient noise, constant noise
covariance, the continuous-time limit, and a quadratic loss near the
optimum (§2.2, pp. 2–3). This version does not state that A must be
positive definite in so many words, but the posterior it targets is
f ∝ exp(−(N/2)θᵀAθ) (Eq. 14) and the stationary covariance needs A's
eigenvalues positive (App. A, "by the positivity of the eigenvalues of
A"). The abstract states the scope: SGD "after an initial phase of
convergence, generates samples from a stationary distribution".

## Key results

- **Eq. 13.** ΣAᵀ + AΣ = (ε/S)BBᵀ.
- **Theorem 1.** ε* = 2DS/(N tr BBᵀ) (Eq. 17).
- **Theorem 2.** H* = (2S/εN)(BBᵀ)⁻¹ (Eq. 19).
- **Corollary 1.** H*_kk = 2S/(εN(BBᵀ)_kk) (Eq. 23).
- **Theorem 3, Corollary 2.** SGFS's preconditioner (2/εN)(BBᵀ + EEᵀ)⁻¹
  is KL-optimal and exact; diagonal and scalar truncations (Eq. 26).
- **Table 1.** KL to the posterior on wine, skin and protein, identical to
  the 2017 paper's.
- **Hyperparameters (§4.2, Fig. 3).** Constant SGD on θ with a decreasing
  rate on λ selects an L2 strength close to BBVI's on MNIST and covertype.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Constant SGD's stationary law is N(0, Σ) with ΣA + AΣ = (ε/S)BBᵀ under A1–A4 | strong (derivation) | App. A |
| C2 | The KL-optimal rate and preconditioner are Eqs. 17 and 19, and the full preconditioner is exact | strong (derivation) | Theorems 1–2; checked in NOTE-tmpiaa2o |
| C3 | Constant SGD approximates the posterior about as well as SG-MCMC methods, when preconditioned | moderate (experiment) | Table 1, three regression datasets |
| C4 | It supports hyperparameter selection comparable to BBVI | weak | Fig. 3, one model, two datasets |

## Connections

Superseded in content by the 2017 JMLR paper, LIT-tmpwzrx7, which this
paper's arXiv record does not point to. Hennick and De Baerdemacker cite
this version ("Mandt et al., 2016b") as the non-degenerate case
(NOTE-tmp5vh75).

## Bearing on the record

- **QUESTION-tmpiir0l.** The second row of the question's table cites this
  paper with the 2017 one. That is accurate, with the scope of the 2017
  reading: stationary regime, quadratic loss, one basin. This paper says
  nothing about training's transient. It adds nothing to the question that
  the 2017 paper does not.
- **No THEORY of its own.** Its results are filed once, with this paper as
  a second source, in THEORY-tmp7gcht.
- **ML practice.** The same instructions as the 2017 paper; the LIT keeps
  `anthology-candidate`.

## Limitations

- As the 2017 paper, without its momentum, SGLD and averaging results.
- Slips: Eq. 3 writes the prior term as "+ (1/N) log p(θ)" where the
  negative log joint needs "−" (the 2017 paper corrects it); Eq. 16 writes
  KL(q‖f) as E_q[log f] − E_q[log q], the sign reversed, though its
  right-hand side is the KL. Appendix B's Eq. 30 drops the −½log|Σ| term
  that Eq. 32 then restores. None affects a result.

## Open questions

None beyond those in NOTE-tmpiaa2o.
