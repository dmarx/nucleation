---
status: Proposed
title: 'Multiplicative growth with independent, identically distributed returns gives a lognormal cross-section, not a power law, but the same growth with an additive floor gives a stationary power-law tail whose exponent κ solves E[A^κ] = 1, even when the process contracts on average'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  A Kesten process W' = AW + B meeting the standard conditions (E[log A]
  < 0, P(A > 1) > 0, log A non-lattice, E[A^κ log⁺A] and E[B^κ] finite)
  whose stationary tail is not Pareto with exponent κ; or pure i.i.d.
  multiplicative growth with finite-variance log returns whose
  cross-section after many steps is not close to lognormal.
tags:
- probabilistic-modeling
- complex-systems
- mathematics
date: '2026-11-21'
line:
- formal-apparatus
grounds:
- LIT-tmpx9axf
- THEORY-696
summary: >-
  A's, from A3 §2 and §4 of the exchange "Rich Get Richer Power Laws"
  (2026-11-20). W_{t+1} = A_t W_t gives log W as a sum, hence a lognormal
  by the central limit theorem, with every unit facing the same returns.
  Adding B_t (W_{t+1} = A_t W_t + B_t, Kesten, [LIT-tmpx9axf](../literature.d/LIT-tmpx9axf.md)) gives
  P(W > x) ∝ x^(−κ) with E[A^κ] = 1, so "a process with an overall
  stabilizing tendency can still generate extreme outcomes". Checked by
  simulation in this session: with log A ~ N(−0.05, 0.3²), κ = 1.111 and
  the Hill estimate is 1.10 to 1.12. A3 §4's "these mechanisms are not
  mutually exclusive" is made concrete in the body. The work is
  registered and unread. The wording is A's (the other assistant in the
  exchange "Rich Get Richer Power Laws", A3); adopting it is the owner's
  call.
bears_on:
- QUESTION-tmp21jtb
---
<!-- inactive-ok-file: LIT-tmpx9axf — Deferred; registered from this exchange and not read -->
<!-- inactive-ok-file: CLAIM-tmply70l CLAIM-tmp1dlyp CLAIM-tmp8h6nt THEORY-tmp23821 ARG-tmpk3nh6 — Proposed or new; claims filed with this one from the same exchange, and the reading and argument of 2026-11-21 -->

# CLAIM-tmpiervv: Multiplicative growth with independent, identically distributed returns gives a lognormal cross-section, not a power law, but the same growth with an additive floor gives a stationary power-law tail whose exponent κ solves E[A^κ] = 1, even when the process contracts on average

## The claim (A3 §2)

"**Multiplication becomes addition on a logarithmic scale.**" With
W_{t+1} = W_t A_t and i.i.d. finite-variance log A, log W_t is a sum, so W_t
is approximately lognormal. "Everyone might face exactly the same
distribution of returns. Yet large inequalities still emerge because
compounding amplifies differences across trajectories." But "A pure
multiplicative process generally produces a lognormal distribution at a
fixed time, rather than a true power-law tail."

With an additive term, W_{t+1} = A_t W_t + B_t, "Under suitable conditions,
including an overall tendency toward contraction but occasional growth
multipliers greater than one", the stationary law has P(W > x) ∝ x^(−κ)
with "**E[A^κ] = 1**" (Kesten, [LIT-tmpx9axf](../literature.d/LIT-tmpx9axf.md)). "Rare sequences of favorable
multipliers compound into exceptionally large values."

The record holds geometric Brownian motion and its time-average growth
μ − σ²/2 ([THEORY-696](../theory.d/THEORY-696.md)), but not the lognormal cross-section or the
Kesten tail.

## Checked (the assistant, with python3 -I)

- **Kesten.** log A ~ N(μ, σ²) with μ = −0.05 and σ = 0.3, and B = 1.
  Then E[A^κ] = exp(κμ + κ²σ²/2) = 1 gives κ = −2μ/σ² = 1.111.
  400,000 paths run 3,000 steps give Hill estimates of 1.102, 1.116 and
  1.100 from the top 400, 1,000 and 4,000. The process contracts on
  average (E[log A] < 0), as A says it may.
- **Gibrat.** The same multipliers without B, over 300 steps: log W has
  skewness −0.001 and excess kurtosis 0.003. Normal, so W is lognormal.
- **A3's fixed-rate table.** $100 at 2%, 6% and 12% for 30 years gives
  $181, $574 and $2,996. Checked, and A labels it an illustration.

## Not mutually exclusive, made concrete (the assistant's)

A3 §4 asserts that the mechanisms "are not mutually exclusive" and gives
no combined model. Two exist in what is checked here:

- **Gibrat plus entry is Reed's mechanism.** A common growth rate with
  exponential ages gives a Pareto tail ([CLAIM-tmp1dlyp](CLAIM-tmp1dlyp.md), item 6). Linear
  preferential attachment is the same thing in logarithmic time
  ([CLAIM-tmply70l](CLAIM-tmply70l.md)).
- **Gibrat plus a floor is Kesten.** The additive B is a floor that stops
  log W from drifting off to −∞, so the lognormal spreading reaches a
  stationary state with a Pareto tail.

So the three ways a power law comes out of proportional growth are entry
(a spread of ages), a floor or reinjection, and both. A pure Gibrat
process with neither gives a lognormal that only widens.

## What it does not say

- Not that any real wealth or firm-size tail comes from either. A3 §2's
  policy reading, "reducing privileged access to opportunities addresses
  one mechanism, while changing the structure of compounding, shocks, or
  wealth floors addresses another", has no support in the exchange
  ([CLAIM-tmp8h6nt](CLAIM-tmp8h6nt.md)).
- Not the conditions in full. Kesten's theorem needs more than A states
  (see `defeated_if`), and they were not checked against the paper, which
  is unread.

## Note of 2026-11-21: Mitzenmacher, read

Mitzenmacher's review (LIT-tmpwdtfj) was read in full (NOTE-tmp0rhkc;
the reading is THEORY-tmp23821). It **corroborates** the claim and
**qualifies** its floor; it is not a ground for the Kesten half.

- **Supports the lognormal half.** "if the ln Fk are independent and
  identically distributed variables with finite mean and variance, then
  asymptotically Xj will approach a lognormal distribution" (§5, p. 236).
- **Supports a floor turning it into a power law, in another form.** "As
  long as there is a bounded minimum that acts as a lower reflective
  barrier to the multiplicative model, it will yield a power law instead
  of a lognormal distribution" (§5.1, p. 238). The paper's floor is a
  **reflecting barrier**, a minimum income below which one cannot fall,
  not Kesten's additive B. The title's "additive floor" is one kind of
  floor; a reflecting minimum is another, and either stops log W from
  drifting to −∞. The section "Not mutually exclusive, made concrete"
  above should be read with both.
- **Does not state the exponent or the conditions.** Neither
  E[A^κ] = 1 nor Kesten's conditions appear; the paper defers to Kesten
  (1973) and Gabaix (1999). Its Champernowne example (F = 1/2 with
  probability 2/3, 2 with probability 1/3, a lowest class) instantiates
  the equation, though the paper does not say so: (2/3)·2^(−κ) +
  (1/3)·2^κ = 1 at κ = 1, its Pr[X ≥ x] = m/x, with E[ln F] = −0.231 < 0
  and E[F] = 1. Checked by the filer (python3 -I): two million steps of
  the chain with its floor give Pr[class ≥ k] = 0.500, 0.251, 0.063 and
  0.0079 at k = 2, 3, 5 and 8, against 2^(−(k−1)).
- **The three-way account.** §8 names two of this claim's routes, "once
  the observation time is random or a lower boundary is put into effect";
  the random observation time is the entry route (§7, Reed's double
  Pareto).

So LIT-tmpwdtfj leaves this claim's `grounds` and THEORY-tmp23821
`corroborates` it (ARG-tmpk3nh6). The Kesten half still rests on Kesten
(LIT-tmpx9axf), unread, and the "What it does not say" caveat on the
conditions stands. Status unchanged.
