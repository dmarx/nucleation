---
status: Active
title: 'Over a scenario of n contexts in an odd cycle, changing the support of one context takes the contextual fraction from 1 to 0 while the other n − 1 contexts and every marginal are kept exactly, at a weighted observational distortion of 1/n, so within a scenario the fraction''s Lipschitz constant against that distortion is at least n; and any change of global extension needs a contextual model on one side'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the construction: a global distribution consistent with every
  context of the odd-cycle model in which all contexts anticorrelate; a
  context of the modified model that the equal mixture of the two alternating
  assignments fails to reproduce; a marginal that differs between the two
  models; or a weighted distortion between them other than 1/n.
tags:
- contextuality
- mathematics
date: '2026-10-15'
line:
- pragmatic-transport
- formal-apparatus
grounds:
- CASE-037
- THEORY-165
uses:
- TERM-043
complements:
- CLAIM-tmpbogw2
summary: >-
  Split from [CLAIM-201](CLAIM-201.md) under [ADR-043](../decisions.d/ADR-043.md): the derivation that claim called
  "decisive and checkable", stated on its own. For odd n, an n-cycle of
  ±1 observables in which every context anticorrelates is strongly
  contextual; making one context correlate gives a model with a global
  distribution. The two agree on n − 1 contexts and on every marginal,
  differ by total variation 1 in the last, and so lie at weighted D_obs =
  1/n with contextual fractions 1 and 0. For n = 3 it is [CASE-037](../cases.d/CASE-037.md) with one
  observable relabelled. It answers how small the local change can be; it
  says nothing about whether any data are contextual.
supports:
- CLAIM-201
---
<!-- ref::uses-file: TERM-043 — applied unnamed: the weighted observational distortion D_obs computed in the example is the observational component of the profile this term defines -->
<!-- inactive-ok-file: THEORY-165 — Proposed; continuity of the contextual fraction, cited for its scenario-dependent constant, not as settled -->
<!-- inactive-ok-file: CLAIM-201 CLAIM-105 — Proposed; the narrowing that rests on this and the headline it bears on, cited as open -->

# CLAIM-tmp9fgji: Over a scenario of n contexts in an odd cycle, changing the support of one context takes the contextual fraction from 1 to 0 while the other n − 1 contexts and every marginal are kept exactly, at a weighted observational distortion of 1/n, so within a scenario the fraction's Lipschitz constant against that distortion is at least n; and any change of global extension needs a contextual model on one side

## The claim

Within one scenario, global compatibility can change maximally while most
local judgements are kept exactly. Take n odd, n ≥ 3, and observables
a_1, …, a_n with outcomes ±1. The contexts are C_i = {a_i, a_(i+1)} for
i = 1, …, n, indices mod n, so that C_n = {a_n, a_1}. Weight every context
1/n.

- **Model e.** In every context the two observables disagree: the outcomes
  (+, −) and (−, +) each have probability 1/2. A global assignment
  consistent with every context's support would need a_(i+1) = −a_i for
  every i, so going round the cycle a_1 = (−1)^n a_1 = −a_1, since n is odd.
  No ±1 value satisfies that, so no global assignment is consistent with the
  supports. The model is strongly contextual, and its contextual fraction
  is 1.
- **Model e′.** The same, except in C_n, where a_n = a_1: the outcomes
  (+, +) and (−, −) each have probability 1/2. Now the constraints are
  a_(i+1) = −a_i for i = 1, …, n − 1 and a_n = a_1. The first n − 1 give
  a_n = (−1)^(n−1) a_1 = a_1, since n − 1 is even, so they agree with the
  last. The two assignments a_i = s(−1)^(i−1), s = +1 or −1, satisfy every
  constraint. Their equal mixture reproduces every context: in C_i for
  i < n it gives (s(−1)^(i−1), −s(−1)^(i−1)), which is (+, −) or (−, +)
  with probability 1/2 each; in C_n it gives (s, s), which is (+, +) or
  (−, −) with probability 1/2 each. So e′ has a global distribution, and
  its contextual fraction is 0.
- **What changed.** In both models every observable is +1 or −1 with
  probability 1/2 in each context that measures it, so neither signals, and
  overlap consistency is the same. The contexts C_1, …, C_(n−1) are
  identical. C_n changed from support {(+, −), (−, +)} to the disjoint
  support {(+, +), (−, −)}, a total-variation distance of 1. With equal
  weights the weighted observational distortion is D_obs = (1/n) · 1 = 1/n.

For n = 3 this is [CASE-037](../cases.d/CASE-037.md) with the outcomes of one observable relabelled,
the pair [CLAIM-tmpbogw2](CLAIM-tmpbogw2.md) states for one scenario; this claim is its general
form.
So within a fixed scenario the contextual fraction can fall from 1 to 0 at a
weighted local distortion of 1/n, which is as small as one likes for large
n. [THEORY-165](../theory.d/THEORY-165.md) says the fraction is Lipschitz within a scenario and that its
constant "depends on the scenario and is not bounded here". Measured against
weighted D_obs, the example shows the constant is at least n.

The bound that moving every context by at most ε moves each overlap
discrepancy by at most 2ε ([CLAIM-219](CLAIM-219.md)) is respected: no marginal moves at
all. It concerns overlap consistency and every context moved a little, not
global extension with most contexts kept exactly.

Every such case needs a contextual model on one side, here e: if both
models had a global extension, global extension would not have changed.

## What it does not say

- That any data are contextual, or that a rendering does this. Whether
  behavioural data supply the contextual side is [CLAIM-tmpxrlyo](CLAIM-tmpxrlyo.md), and what
  follows for [CLAIM-105](CLAIM-105.md)'s headline is [CLAIM-201](CLAIM-201.md)'s, which rests on this claim.
- Anything across scenarios. The construction keeps the scenario fixed; a
  change of scenario, where the fraction can jump, is a different case.
- That the bound of n is tight. It is a lower bound on the constant,
  measured against weighted D_obs with equal weights.
