---
number: 1163
status: Active
formerly:
- THEORY-tmpx3lyj
title: 'Krakauer et al.''s organismal and colonial individuality, A* = I(S_{n+1}; S_n) and A = I(S_{n+1}; S_n | E_n), cannot decrease when variables are moved from the environment into the candidate system, so maximizing either over candidate boundaries selects the largest candidate, and a boundary found this way needs a size cost the measures do not contain'
version: 1
history:
- version: 1
  date: '2026-10-29'
  note: >-
    Filed Active from NOTE-1400, re-derived. It is the article's own
    statement (Theory in Biosciences 2020, "Both individuality measures
    can only grow or stay constant with increasing system size"), and
    the expansions it gives were checked line by line with the chain
    rule for mutual information. A* + nC = A + I(S_{n+1}; E_n) was
    checked on the article's two-unit example at four parameter settings
    (record script, 2026-10-29), where both sides agree to machine
    precision.
tags:
- individuation
- information-theory
date: '2026-10-29'
source:
- LIT-1137
summary: >-
  Krakauer, Bertschinger, Olbrich, Flack and Ay (2020), [LIT-1137](../literature.d/LIT-1137.md), read in
  [NOTE-1400](../notes.d/NOTE-1400.md). Mutual information cannot fall when either argument is
  enlarged, and A′ ≥ A follows by the chain rule with the remaining
  environment as condition. It is a fact about the measures, not about
  any system. It does not say how to price size, and nC, the third
  measure, can move either way. It is the formal content of A11's
  remark recorded in [QUESTION-115](../questions.d/QUESTION-115.md).
---
<!-- inactive-ok-file: CLAIM-157 — Proposed; named as an untested candidate for the size cost, nothing here rests on it -->

# THEORY-1163: Krakauer et al.'s organismal and colonial individuality, A* = I(S_{n+1}; S_n) and A = I(S_{n+1}; S_n | E_n), cannot decrease when variables are moved from the environment into the candidate system, so maximizing either over candidate boundaries selects the largest candidate, and a boundary found this way needs a size cost the measures do not contain

## Source

Krakauer, D., Bertschinger, N., Olbrich, E., Flack, J. C. & Ay, N. (2020),
[LIT-1137](../literature.d/LIT-1137.md), §"Individuality measures in an illustrative example", read in
[NOTE-1400](../notes.d/NOTE-1400.md). The 2014 preprint states the monotonicity too but offers a
stopping rule instead of a size cost.

## What was actually shown

Let the world be split into system S and environment E, and move a part
ΔS of E into the system, leaving E′. Writing S′ = (S, ΔS):

- **A* (organismal).** A′* = I(S′_{n+1}; S′_n)
  = I(S′_{n+1}; S_n) + I(S′_{n+1}; ΔS_n | S_n)
  = A* + I(ΔS_{n+1}; S_n | S_{n+1}) + I(S′_{n+1}; ΔS_n | S_n).
  Both added terms are conditional mutual informations, hence ≥ 0.
- **A (colonial).** A = I(S_{n+1}; S_n | E′_n, ΔS_n), and
  A′ = I(S′_{n+1}; S_n, ΔS_n | E′_n)
  = I(S′_{n+1}; ΔS_n | E′_n) + I(S′_{n+1}; S_n | E′_n, ΔS_n)
  ≥ I(S_{n+1}; S_n | E′_n, ΔS_n) = A,
  the inequality because adding ΔS_{n+1} to the first argument cannot
  lower a conditional mutual information.

So along any chain of nested candidates both measures are
non-decreasing, and the whole world, with an empty environment, attains
the maximum of each. The article draws the consequence itself: the
measures "are not sufficient to detect the precise boundaries between
individuals. In order to obtain precise boundaries we would need to
impose a cost function—or regularizer—on system size". The third
measure, nC = I(S_{n+1}; E_n | S_n), changes by
−I(S_{n+1}; ΔS_n | S_n) + I(ΔS_{n+1}; E′_n | ΔS_n, S_{n+1}, S_n) and can
rise or fall.

What could have come out otherwise: a conditional measure can fall when
its condition grows, so A was not monotone by inspection. It is because
the variables moved out of the condition enter the arguments.

## What this does not say

- It does not say the measures are useless. Compared across candidates of
  equal size, or normalized (Bourrat's C1 divides by an entropy,
  [NOTE-027](../notes.d/NOTE-027.md)), they can still rank.
- It does not supply the size cost, or say what form it should take. The
  record's priced individuation ([CLAIM-154](../claims.d/CLAIM-154.md), [CLAIM-157](../claims.d/CLAIM-157.md)) is one candidate,
  untested against these measures.
- It does not say nC finds boundaries. nC can fall as the candidate grows,
  but it also reaches zero for the whole world, so minimizing it has the
  same end point.
- It says nothing about whether the measures track propagation rather
  than association; that is [THEORY-424](THEORY-424.md).
