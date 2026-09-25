---
number: 46
status: Skimmed
formerly:
- NOTE-tmpcdown
paper: LIT-064
title: 'Chu & Raginsky, expected soft maxima of Gaussian processes'
version: 1
date: '2026-09-25'
summary: >-
  For a centered Gaussian process on a finite index set, the expected softmax-weighted average g(β) = E[Σ X_t e^{βX_t}/Z] scales like σ·√(E D(ν_β‖ν_0)) (upper bound always, Sudakov-type lower bound at low temperature, matching for i.i.d.). The quenched free energy scales likewise with the Rényi-½ divergence. Both reduce to the classical √log|T| maximal inequalities as β→∞.
---

<!-- inactive-ok-file: LIT-064 — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-25 -->

# NOTE-046: Chu & Raginsky, expected soft maxima of Gaussian processes

## Contribution

Extremal behaviour of stochastic processes matters across probability, statistical physics, theoretical computer science and learning theory. The paper studies centered Gaussian processes on finite index sets and the expected values of their smoothed ("soft") maxima. Upper and lower bounds are obtained by combining statistical-physics tools (the Gibbs variational principle and replica-symmetric representations of Gibbs averages) with Sudakov minoration from probability. The bounds are indexed by an inverse temperature β and recover the usual Gaussian maximal inequalities as β→∞. The Random Energy Model serves as an illustration.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- §1, Eqs. 2–4: two soft proxies for max_t X_t are the log-sum-exp "β-softmax" (within log|T|/β above the max) and the Gibbs average g(X;β), which moves from the sample mean at β=0 to the max as β→∞. The paper defines the quenched g(β) (Eq. 5) and the quenched free energy φ(β) (Eq. 6).
- §1 results: (1) g(β) ≲ σ√(E D(ν_β‖ν_0)) for all β, with g(β) ≳ a√(E D(ν_β‖ν_0)) for β ≥ β* (a is the minimum separation), and ≍ for i.i.d. N(0,σ²). (2) φ(β) ≲ σ√(E D_{1/2}(ν_β‖ν_0)), with a matching lower bound for i.i.d. The KL (resp. Rényi) divergence of the Gibbs measure from uniform takes the role of log|T| at finite temperature.
- §1.1: the authors believe these finite-β bounds are new, and contrast them with Liu (2022, 2023) on Sudakov-type bounds for log-integral relaxations of convex-body widths.
- The proofs sit in §3 (Gibbs variational upper bound; Sudakov low-temperature lower bound; the i.i.d. case) and §4 (free energy, including a Sudakov-type bound without independence, §4.3).
- §5 (REM, Theorem 7): elementary finite-N bounds on the quenched pressure show the quadratic-vs-linear scaling in β on either side of β_c = 2√log 2, though the constants are not sharp.

## Open questions

- g(β) is exactly the softmax-weighted expectation used in attention and in Boltzmann/Gibbs policies with Gaussian logits. The √(KL from uniform) scaling is a candidate tool for bounding expected attention output or entropy-regularised selection. This is the "softmax analysis" relevance flagged in the triage. It is not ML work itself, so filing would need a concrete ML-facing claim to hang it on.
- Check the constants and the threshold β* in Theorem 1's lower bound (how it depends on covariance), and whether the i.i.d. matching extends to weakly correlated logits.
