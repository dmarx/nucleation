---
status: Active
title: "Transfer entropy from J to I is the Kullback entropy of assuming that I's next state, given its last k states, does not depend on J's last l states, so it is zero exactly when J's past leaves I's transition law unchanged; unlike time-delayed mutual information it is directional and zero for static correlation, and it removes a common input only when that input is conditioned on"
version: 1
tags:
- information-theory
- complex-systems
- causality
date: '2026-10-17'
source:
- LIT-tmpz9o5z
summary: >-
  Schreiber (2000), [LIT-tmpz9o5z](../literature.d/LIT-tmpz9o5z.md), read in full in [NOTE-tmplm3la](../notes.d/NOTE-tmplm3la.md). The
  definition and its zero condition are exact. The comparison with
  delayed mutual information rests on two coupled-map lattices built with
  a known direction. The continuum-limit claim is asserted. The Letter's
  tent-map coefficient appears to be twice what Eq. 4 gives.
---

# THEORY-tmp1jjkw: Transfer entropy from J to I is the Kullback entropy of assuming that I's next state, given its last k states, does not depend on J's last l states, so it is zero exactly when J's past leaves I's transition law unchanged; unlike time-delayed mutual information it is directional and zero for static correlation, and it removes a common input only when that input is conditioned on

## Source

Schreiber (2000), "Measuring Information Transfer", arXiv nlin/0001042v1
(Phys. Rev. Lett. 85, 461), [LIT-tmpz9o5z](../literature.d/LIT-tmpz9o5z.md), read in full in [NOTE-tmplm3la](../notes.d/NOTE-tmplm3la.md).
The PRL version was not compared.

## What was actually shown

**The definition (Eq. 4).**
T_{J→I} = Σ p(i_{n+1}, i_n^{(k)}, j_n^{(l)}) log[p(i_{n+1} | i_n^{(k)},
j_n^{(l)}) / p(i_{n+1} | i_n^{(k)})], with i_n^{(k)} = (i_n, …,
i_{n−k+1}) and j_n^{(l)} likewise. It is the Kullback entropy (Eq. 1) of
the generalized Markov property p(i_{n+1} | i_n^{(k)}) = p(i_{n+1} |
i_n^{(k)}, j_n^{(l)}), so it is nonnegative and zero exactly when that
property holds. k and l are free; l = k and l = 1 are "most natural".

**Why it is directional.** Mutual information is symmetric, and the
asymmetry of conditional entropy is H_I − H_J, not flow. Eq. 4 conditions
on the target's own past, so correlation inherited from common history
does not count.

**Examples.** In a tent-map lattice with binary partition, T in the
coupling direction is of order ε² while delayed MI is zero to the same
order; against the coupling T is zero. In an Ulam-map lattice T stays
consistent with zero against the coupling through every bifurcation,
and is zero in a period-two window where delayed MI is 1 bit.

What could have come out otherwise: in the Ulam lattice T against the
coupling could have been nonzero in the windows where delayed MI was
nearly symmetric. It was not.

## What this does not say

- **That positive T is information moving from J to I.** The Letter
  calls it "transfer" and "exchange" but defines nothing beyond Eq. 4,
  a conditional dependence. Whether that is a flow is [CLAIM-tmpu9ivq](../claims.d/CLAIM-tmpu9ivq.md)'s
  question.
- **That unobserved common drivers are excluded.** Only a known driver Z,
  conditioned on, is (p. 2). The heart–breath asymmetry is left open to a
  common trigger by the author.
- **That T is interventional.** Eq. 4 is observational; when it bears on
  interventions is [THEORY-tmp4g68i](THEORY-tmp4g68i.md)'s and [CLAIM-tmp6nu4a](../claims.d/CLAIM-tmp6nu4a.md)'s question.
- **Which k and l to use.** Results at k = l = 1 are not shown to survive
  longer histories.
- **Anything about estimation error.** No bias, variance or null
  distribution is given; [THEORY-641](THEORY-641.md) supplies a χ² null under a
  parametric model.
- **The tent-map constant.** The reading's evaluation of Eq. 4 gives
  α²ε²/(2 ln 2), half the Letter's α²ε²/ln 2. With α fitted, nothing
  qualitative changes.

## Connections

- [THEORY-641](THEORY-641.md) and [THEORY-tmp0xaeq](THEORY-tmp0xaeq.md) are later results about this quantity:
  a likelihood-ratio limit in general, half the Granger statistic for
  Gaussians.
- [THEORY-275](THEORY-275.md) uses a delayed variant, I(y_{t+τ}; x_t | y_t), which is Eq.
  4 at k = l = 1 only for τ = 1.
- [THEORY-568](THEORY-568.md) counts T as one summand of a Shannon invariant's numerator.
- [TERM-tmpj9z04](../terms.d/TERM-tmpj9z04.md) is the record's own statement of the term.
