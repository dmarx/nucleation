---
status: Proposed
title: "In the demand-weighted coverage of an ecosystem, the integral over future questions of the best readiness any one perspective offers, a perspective adds the integral of its excess over that best, so a duplicate adds nothing; but the ordering of similar against differentiated ecosystems reverses when perspectives attempt in parallel, share a budget or are chosen by a selector that cannot tell the questions apart, and since coverage is linear in demand, uncertainty about demand over a fixed set of questions adds nothing beyond the mean demand"
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in one of the derivations or in the constructed examples below,
  for coverage defined as A60 §4 defines it. Not defeated by a different
  measure of coverage: the claim is about A60's.
tags:
- ecology
- operations-research
- probabilistic-modeling
date: '2026-11-23'
line:
- realizability
- readiness
- formal-apparatus
bears_on:
- QUESTION-tmpzblpf
- QUESTION-395
summary: >-
  A gap fill ([ADR-137](../decisions.d/ADR-137.md)) for A60 §4 of the exchange "Explain First Contact
  RL" (ChatGPT, 2026-11-23), whose coverage model, C(E;μ) = ∫ max_i r_i(q)
  dμ(q), is offered as why diversity tracks richness, with the conditions
  "one perspective can be selected without substantial activation or
  coordination cost" and "the added capacity does not displace or
  interfere with the others", and the remark that "the really difficult
  part is that μ is not fully known". The model's properties are derived
  and its conditions shown to carry the result, with each example checked
  by script (python3 -I). The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---

<!-- inactive-ok-file: ARG-tmpbchnj — Open or new; the question this bears on, the claims whose model it checks, and the argument that applies it -->

# CLAIM-tmp7iie0: In the demand-weighted coverage of an ecosystem, the integral over future questions of the best readiness any one perspective offers, a perspective adds the integral of its excess over that best, so a duplicate adds nothing; but the ordering of similar against differentiated ecosystems reverses when perspectives attempt in parallel, share a budget or are chosen by a selector that cannot tell the questions apart, and since coverage is linear in demand, uncertainty about demand over a fixed set of questions adds nothing beyond the mean demand

## The gap

A60 §4 defines, for perspectives *i* with readiness r_i(q) (the
probability of an acceptable answer to question *q* within the deadline and
resources), R_E(q) = max_i r_i(q) and C(E; μ) = ∫ R_E dμ over a family Q*
of future questions weighted by μ. It states two conditions and then
argues from the model to diversity's value, including against unknown μ.
It does not derive what the model implies, nor how much the conditions
carry. This entry does both.

## The derivations

1. **Marginal value.** Adding perspective *j* to E changes R_E(q) to
   max(R_E(q), r_j(q)), so C rises by ∫ (r_j − R_E)⁺ dμ: the demand-weighted
   excess of *j* over the best already present. A duplicate, or any *j*
   dominated pointwise, adds exactly zero. Checked: in a three-question
   example, specialists (0.9,0,0), (0,0.9,0), (0,0,0.9) under uniform μ,
   adding (0.95, 0.2, 0) raises C by 0.01667, the formula's value; adding a
   second (0.9,0,0) raises it by 0.
2. **Under max, differentiation wins.** Three similar generalists
   (0.6, 0.6, 0.6) give C = 0.6; the three specialists give 0.9.
3. **Under parallel attempts it reverses.** If every perspective attempts
   and they fail independently, R_E(q) = 1 − Π_i (1 − r_i(q)). The
   generalists then give 1 − 0.4³ = 0.936 and the specialists still 0.9.
   Redundancy is what A60 §2 says it is, reliability "against independent
   failures", and the aggregation rule decides whether it counts.
4. **Under a shared budget, a duplicate lowers coverage.** Let readiness
   scale with each perspective's share of a budget H, r_i = s_i · min(1,
   H/n). With H = 2 the three specialists give C = 0.6, two of them alone
   also 0.6, and the three plus a duplicate 0.45. This is A60's "displace
   or interfere" condition, and it is not a margin: it can flip the sign of
   adding a constituent.
5. **Under a selector that cannot tell questions apart, differentiation's
   advantage vanishes.** The max presumes that each question reaches the
   perspective best at it. If the ecosystem can tell question 2 from the
   others but not 0 from 1, it routes both to whichever perspective is
   best on average over the two. The specialists then give C = 0.6, the
   same as the generalists. Recognizing which perspective a demand needs
   is a query-side capacity (the inquiry frontier, [TERM-092](../terms.d/TERM-092.md)), so the model's
   result presupposes the very capacity A60 §6 credits diversity with.
6. **Uncertainty about demand reduces to its mean.** C is linear in μ, so
   for any prior over μ supported on measures over Q*, E[C(E; μ)] = C(E;
   E[μ]). Checked by Monte Carlo (200,000 draws of μ from a Dirichlet with
   parameters (4.5, 4.5, 1)): two specialists (1,0,0), (0,1,0) give 0.8999
   against C at the mean of 0.9; one generalist (0.6,0.6,0.6) gives 0.6
   against 0.6. In expectation the specialists win. Under the worst case
   over point masses, min_q R_E(q), the specialists give 0 and the
   generalist 0.6.

## What follows

- Within the model, unknown demand favours diversity only through a
  risk-averse or worst-case evaluation, which rewards covering every
  question somewhat, or through questions outside Q*, which C cannot
  score at all. A60's "capacities for recognizing future demands that
  nobody can currently specify" is the second: it is an argument outside
  the model, and interpretive.
- The model supports the claim that diversity of consequential capabilities
  tracks richness under single selection, a recognizing selector and no shared
  budget. Under the other conditions, similar constituents can be worth
  more, or an added one worth less than nothing ([ARG-tmpbchnj](../arguments.d/ARG-tmpbchnj.md)).

## The check

The examples were computed with a script run under `python3 -I` in this
session: the marginal-value identity, the three aggregation rules, the
budget-share example and the routing example exactly, and the Dirichlet
expectation by Monte Carlo with a fixed seed.

## Standing

Proposed, the assistant's. It fills the gap A60 §4 leaves between its
model and its conclusion, and bears on [QUESTION-395](../questions.d/QUESTION-395.md): the marginal-value
formula is a criterion for telling a warranted reserve from wasteful redundancy
under single selection, and derivation 3 shows that under parallel
attempts a redundant copy can be the warranted one.
