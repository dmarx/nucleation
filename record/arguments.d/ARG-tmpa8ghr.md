---
status: Proposed
title: "Beck and Cohen's gamma superstatistics, as a source, with the assistant's condition on the spread, carries item 4 of the catalogue of feedback-free power-law mechanisms for spreads of rates with power-law weight at zero rate, not for every spread"
version: 1
form: source
rests_on:
- CLAIM-tmpf9qt9
grounds:
- THEORY-tmpczldx
concludes:
- CLAIM-795
tags:
- probabilistic-modeling
- thermodynamics
date: '2026-11-22'
line:
- formal-apparatus
summary: >-
  Whether Beck and Cohen ([LIT-2962](../literature.d/LIT-2962.md)), read in [NOTE-tmpj8ro5](../notes.d/NOTE-tmpj8ro5.md), carry [CLAIM-795](../claims.d/CLAIM-795.md)'s
  item 4, a "mixture of exponential rates" giving a power law. Their eq. 13
  is the item's formula with energy for time: a gamma spread gives
  (1 + bE)^(−c). But their uniform and two-level spreads keep exponential
  tails, and they say the large-E behaviour "strongly depends on the
  function f(β)". With [CLAIM-tmpf9qt9](../claims.d/CLAIM-tmpf9qt9.md) (power-law weight at zero rate is
  necessary and sufficient), the reading carries the item for the gamma
  spread its `defeated_if` names and for any spread with that weight, not
  for mixtures as such. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-795 CLAIM-tmpf9qt9 THEORY-tmpczldx THEORY-2131 ARG-tmp3ppjy — Proposed or new; the claim, the readings and the condition this argument joins -->

# ARG-tmpa8ghr: Beck and Cohen's gamma superstatistics, as a source, with the assistant's condition on the spread, carries item 4 of the catalogue of feedback-free power-law mechanisms for spreads of rates with power-law weight at zero rate, not for every spread

## The inference

[CLAIM-795](../claims.d/CLAIM-795.md), item 4: exponential waiting times with gamma-distributed rates
give P(T > t) = (b/(b + t))^a, and mixtures are a route to power laws with
no positive feedback. [THEORY-tmpczldx](../theory.d/THEORY-tmpczldx.md): B(E) = ∫ f(β) e^(−βE) dβ, with the
closed forms. [CLAIM-tmpf9qt9](../claims.d/CLAIM-tmpf9qt9.md): which f give a power-law B.

## Critical questions (source)

**Does the work say this, read in context?** For the gamma case, yes:
eq. 13, B = (1 + bE)^(−c), is item 4's survival with a = c and the scale
inverted, and the paper's c is the gamma's shape, "the effective number of
degrees of freedom" over two (p. 5). The paper does not discuss waiting
times or use the words "power law"; the mapping of energy to time and
inverse temperature to rate is the integral's, not the paper's.

**Is it said within the scope the claim needs?** Not for "a mixture of
exponential rates" in general. Beck's uniform density on [a, a + b] keeps
an exponential tail (eq. 5), and the paper's main result is that the
densities agree only at small variance. [CLAIM-tmpf9qt9](../claims.d/CLAIM-tmpf9qt9.md) states the
condition, power-law weight at zero rate, and checks it. Item 4's
`defeated_if` already names "a gamma spread of rates", so the thesis is
not defeated; its label "a mixture of exponential rates" reads wider than
what holds.

**Does the claim lean on the reading for more than it holds?** A's
"heterogeneity across a population alone yields a power law" (as the LIT
first summarized it) did; the claim's item 4, read with its `defeated_if`,
does not.

## Verdict

Support for item 4 as stated with its gamma spread, and for any spread
with power-law weight at zero rate. [THEORY-tmpczldx](../theory.d/THEORY-tmpczldx.md) replaces [LIT-2962](../literature.d/LIT-2962.md) in
[CLAIM-795](../claims.d/CLAIM-795.md)'s `grounds`, beside [THEORY-2131](../theory.d/THEORY-2131.md). Newman's route ([ARG-tmp3ppjy](ARG-tmp3ppjy.md)) is
unaffected.
