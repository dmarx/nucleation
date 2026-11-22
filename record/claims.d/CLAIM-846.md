---
number: 846
status: Proposed
formerly:
- CLAIM-tmpwl8y8
title: 'Scale-free correlations do not need heavy-tailed marginals: a Gaussian field with a power-law spectrum has Gaussian values at every point, so what is scale-free can be a scaling relation rather than a distribution of magnitudes'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the construction: a stationary Gaussian field with a
  power-law two-point function whose one-point law is not Gaussian, or a
  showing that the simulated field's correlations are not a power law over
  the stated range. Also defeated as a separate entry if the record
  already held that power-law correlation and heavy-tailed marginals are
  independent; at filing, no claim, term or reading did (ledger search
  for "scale invariance", "heavy tail", "scale-free" in claims, terms and
  questions).
tags:
- complex-systems
- probabilistic-modeling
- mathematics
date: '2026-11-21'
line:
- formal-apparatus
uses:
- TERM-142
summary: >-
  A's, at A27 §9 of the exchange "Rich Get Richer Power Laws": an ordered
  magnet "can have scale-free spatial correlations without having a
  heavy-tailed probability distribution of individual spin angles", since
  spin-wave theory is Gaussian, so "the fundamental organizing object may
  be a scaling relation rather than a distribution of magnitudes"; and
  A10 §2's Brownian motion, self-similar in time and Gaussian at each
  time. The assistant adds the check (a simulated 3D Gaussian field with
  1/k² spectrum: kurtosis 3.00, correlation ∝ r^(−1.09) against the exact
  r^(−1)), the converse (independent Pareto draws: power-law tail, no
  correlation), and a bounded case (the 2D Ising model at T_c). The
  wording is A's (the other assistant in the exchange "Rich Get Richer
  Power Laws", A27 §9, A10 §2); adopting it is the owner's call.
---
<!-- inactive-ok-file: NOTE-tmpurjns NOTE-tmpcjw5n — new or Skimmed; readings of 2026-11-22 -->
<!-- inactive-ok-file: THEORY-tmpwtoad — Proposed, Deferred or new; the readings of 2026-11-22 and the entries they bear on -->
<!-- inactive-ok-file: TERM-142 CLAIM-810 CLAIM-841 CLAIM-840 — filed from the same exchange on 2026-11-21 -->

# CLAIM-846: Scale-free correlations do not need heavy-tailed marginals: a Gaussian field with a power-law spectrum has Gaussian values at every point, so what is scale-free can be a scaling relation rather than a distribution of magnitudes

## A's statement (A27 §9)

> An ordered magnet can have scale-free spatial correlations without
> having a heavy-tailed probability distribution of individual spin
> angles. Indeed, the long-wavelength Gaussian spin-wave theory has
> Gaussian Fourier-mode fluctuations. The scale-free property lies in how
> their variance depends on spatial frequency: ⟨|θ_k|²⟩ ∝ k^(−2), not in
> the distribution of values of θ at a fixed point.

A then separates "Are unusually large outcomes disproportionately
common?" from "Are fluctuations at widely different spatial or temporal
scales related by the same mathematical law?": "A single system can
satisfy either, both, or neither." A10 §2 had given the first instance:
Brownian motion is self-similar, B(at) =d √a B(t), "yet its position at
any fixed time has a Gaussian distribution". A23 §5 adds the multifractal
case: "a heavy-tailed marginal distribution alone is not evidence of
multifractality".

## The argument

A stationary Gaussian field is fixed by its two-point function, and every
linear functional of it, its value at a point included, is Gaussian. So
any power-law two-point function, C(r) ∝ r^(−a) with 0 < a < d, or
equivalently a spectrum S(k) ∝ k^(a−d) ([TERM-142](../terms.d/TERM-142.md)), gives scale-free
correlations with Gaussian one-point values. The equipartition spectrum
of A27 §3, ⟨|θ_k|²⟩ ∝ T/(ρ_s k²), is the case a = d − 2.

**Checked** (`python3 -I`, seed fixed). Six samples of a Gaussian field on
a periodic 128³ lattice with spectrum 1/K²(k), K² the lattice Laplacian:

- one-point kurtosis 2.999 to 3.007 (Gaussian: 3), skewness within
  ±0.005;
- the correlation along the axes, fitted as A r^(−p) + B over r = 3 to 20
  (B absorbs the periodic box's zero-mode subtraction), gives p = 1.09;
  the exact lattice Green's function of the same field fits A/r + B
  within 2.4% over that range with A = 0.082, against the continuum
  1/4π = 0.080. So the correlations are the d = 3 law r^(−(d−2)) = r^(−1),
  and the sampled exponent is within sampling error of it.

The converse, a heavy-tailed marginal with no scale-free relation: 2 × 10⁶
independent Pareto draws with α = 1.5 have a survival function of log-log
slope −1.505, and their lag-1 to lag-3 autocorrelations (of log x) are
below 4 × 10⁻⁴ in size. The spectrum is flat.

A third case needs no check: the 2D Ising model at T_c has spins ±1, a
bounded marginal, and C(r) ∝ r^(−1/4).

## What follows

Heavy-tailed marginals ([TERM-142](../terms.d/TERM-142.md)'s sense 1) and scale-covariant laws
(its senses 2 and 3) are independent. Fitting a power law to a histogram
tests the first and says nothing about the second; a system can be
scale-free in the sense that matters for its organization while every
measured magnitude is thin-tailed. This is the step the ledgers asked for
before the exchange's other claims about "scale-free" could be filed
cleanly; [CLAIM-810](CLAIM-810.md) uses the same Gaussian field to separate scale
invariance from transfer across scales, and [CLAIM-841](CLAIM-841.md) uses the
Goldstone case as a route to scaling without criticality.

## What it does not say

- That heavy tails and scale-free correlations never come together. At a
  percolation threshold cluster sizes are heavy-tailed and correlations
  are power laws; the claim is that neither requires the other.
- That the owner's bulk-and-tail intuition (U5, [CLAIM-840](CLAIM-840.md)) is wrong. It is a claim
  about event-size distributions, sense 1; A27 §9 calls this example a
  refinement of it, not a refutation.

## Note of 2026-11-22: Stringer and colleagues, read

Stringer and colleagues ([LIT-2972](../literature.d/LIT-2972.md), [NOTE-tmp923nm](../notes.d/NOTE-tmp923nm.md), [THEORY-tmpwtoad](../theory.d/THEORY-tmpwtoad.md)): **a
parallel.** In V1 the power-law spectrum "arises from correlations between
cells rather than from the distribution of firing rates or signal
variance" (Extended Data Fig. 7): a power-law spectrum without heavy-tailed
marginals is what the measured code shows, in the spirit of this claim's
separation of spectrum from marginals. A parallel, so no relation.

## Note of 2026-11-22: Toner and Tu (1998), Halperin and Drouin-Touchette, read

**Parallels, no edge.** Three readings of 2026-11-22 carry this claim's
point in their own cases. Halperin ([LIT-tmp3zns2](../literature.d/LIT-tmp3zns2.md), [NOTE-tmpuwmny](../notes.d/NOTE-tmpuwmny.md), eqs. 2–3)
and Drouin-Touchette ([LIT-tmp6hh1r](../literature.d/LIT-tmp6hh1r.md), [NOTE-tmpurjns](../notes.d/NOTE-tmpurjns.md), §2.2, eq. 18) give the
Gaussian spin-wave computation this claim checks numerically: phase
variance ∝ ln r and correlations ∝ r^(−T/2πρ_s), with Gaussian angles at
every point. Toner and Tu ([LIT-2970](../literature.d/LIT-2970.md), [NOTE-tmpcjw5n](../notes.d/NOTE-tmpcjw5n.md)) put a flock's
scale-free content in correlation functions and a density structure
factor that diverges as q → 0, not in a distribution of magnitudes.
And Drouin-Touchette add a limit of the Gaussian route this claim does
not need but should not be read past: the spin-wave energy alone "is
perfectly analytic" and has no transition (§3.1), which comes from
vortices, outside any Gaussian field. No status change.
