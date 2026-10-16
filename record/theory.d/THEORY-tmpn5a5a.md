---
status: Active
title: "A U-turn stopping rule for Hamiltonian Monte Carlo leaves the target invariant once the trajectory is built as a random balanced doubling tree and the next state is drawn only from states that could have regenerated it; with a dual-averaged step size it matched the best hand-tuned identity-mass HMC on two of four test posteriors and beat it about threefold on the other two, and its ergodicity is not shown"
version: 1
tags:
- probabilistic-modeling
date: '2026-10-16'
source:
- LIT-085
summary: >-
  Hoffman & Gelman (2011), [LIT-085](../literature.d/LIT-085.md), read in full in [NOTE-081](../notes.d/NOTE-081.md). The
  invariance argument (conditions C.1–C.4 and the 2⁻ʲ tree probability)
  is complete, and so is the O(j)-memory kernel. Ergodicity is not
  addressed. The efficiency comparison is against HMC with an identity
  mass matrix on four smooth, near-unimodal targets, and the
  dual-averaging constants were tuned on one of the four. The account is
  of the 2011 algorithm; production NUTS has since changed its selection
  rule, U-turn criterion and adaptation.
---

# THEORY-tmpn5a5a: A U-turn stopping rule for Hamiltonian Monte Carlo leaves the target invariant once the trajectory is built as a random balanced doubling tree and the next state is drawn only from states that could have regenerated it; with a dual-averaged step size it matched the best hand-tuned identity-mass HMC on two of four test posteriors and beat it about threefold on the other two, and its ergodicity is not shown

## Source

Hoffman & Gelman (2011), "The No-U-Turn Sampler", arXiv 1111.4246v1,
[LIT-085](../literature.d/LIT-085.md), read in full in [NOTE-081](../notes.d/NOTE-081.md). Figures 3–7 were read from captions
and prose, not plotted points. The JMLR 2014 version was not compared.

## What was actually shown

**Why the naive rule fails.** Stopping when (θ̃ − θ)·r̃ < 0 breaks time
reversibility, so the chain no longer leaves the target invariant.

**The repair (§3.1.1, pp. 7–10).** Add a slice variable u. Build the
trajectory by doubling forwards or backwards at random, so that a tree
of height j is equally likely, at 2⁻ʲ, from each of its leaves. Choose
the next state uniformly from a set C of visited states that lie in the
slice and that would not have triggered a stop before the full tree was
built. Given conditions C.1–C.4 on (B, C), the procedure leaves p(θ)
invariant. The argument is a Gibbs step plus eq. 7. It is complete,
though not stated as a numbered theorem (C1). The efficient kernel of
eq. 10 satisfies detailed balance and needs O(j) memory rather than
O(2ʲ) (C2).

**Step size.** Nesterov's dual averaging, adapted with t₀ and κ, tunes ε
during warm-up toward a target acceptance statistic δ, after which ε is
frozen. Its convergence rests on an assumed, unverified monotonicity of
h(ε) (C4).

**The comparison (§4.4).** Four targets: a 250-dimensional Gaussian,
German-credit logistic regression (25 parameters), a 302-dimensional
hierarchical logistic regression, and a 3001-dimensional stochastic
volatility model. HMC ran over 10 trajectory lengths × 8 values of δ,
NUTS over 15 values of δ, 10 seeds per cell. The measure was the minimum
ESS per gradient evaluation. NUTS at δ = 0.6 roughly equalled HMC's best
on the two regressions and beat it about threefold on the Gaussian and
the stochastic volatility model. HMC's best trajectory length varied
about 100-fold across targets (0.17 to 17.62). The comparison ignores the
cost of HMC's tuning runs, which favours HMC.

What could have come out otherwise: tuned HMC could have beaten NUTS on
some target, and the dual averaging could have missed δ. HMC never won;
the averaging hit δ except on stochastic volatility, where burn-in was
longer.

## What this does not say

- **That NUTS converges, or how fast.** Only invariance is proved. There
  is no irreducibility or geometric-ergodicity argument (C3).
- **That NUTS beats HMC in general.** One HMC variant (identity mass
  matrix), four smooth, near-unimodal targets. No funnels, no
  multimodality, no heavy tails, no comparison with a mass matrix or with
  Riemannian or windowed HMC.
- **That it needs no tuning.** The user tunes nothing, but γ, t₀ and κ
  were hand-set on one of the four test targets, and the authors say they
  may not work as well elsewhere (p. 16).
- **That δ ≈ 0.65 is the NUTS default.** The paper concludes δ = 0.6 for
  NUTS; 0.65 is its HMC value ([NOTE-081](../notes.d/NOTE-081.md), Corrections).
- **That this is the sampler in use today.** Later implementations use
  multinomial selection, a generalized U-turn criterion and adapted mass
  matrices. The reading did not verify those changes.

## Connections

- [NOTE-081](../notes.d/NOTE-081.md) finds the paper plausibly anthology material, carrying an
  instruction for Bayesian computation that no anthology topic now
  holds. This THEORY states only the invariance result and the measured
  comparison, not the practice.
- The hierarchical Bayesian fits of [THEORY-tmp9tc4c](THEORY-tmp9tc4c.md) (HDDM) use earlier
  PyMC MCMC samplers, not NUTS.
