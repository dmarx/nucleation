---
number: 892
status: Proposed
formerly:
- CLAIM-tmpn0u3a
title: 'Erosion of the skill a store replaces costs, per demand, the skill''s price times the chance that the demand falls back on it plus the share of the skill that checking the stored result repeats: it weighs little where demand is predictable, the store rarely wrong and checking cheap, as with a cockpit''s speed bugs, and most where reuse cannot be forecast or checking re-derives, as with a filed argument'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-108; derived in
    the model of CASE-326 and checked by a test in
    scratch/studies/lead-108/test_costmodel.py.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation: a store route, as the model of CASE-326
  defines it, whose expected cost per demand rises with erosion at a rate
  other than c[(1 − π) + π(σδ + φ)]. Or a case in which erosion of the
  replaced skill raises the store route's cost by a path the formula leaves
  out, for instance by lowering the chance δ that checking catches a wrong
  result, by enough to reverse which of two stores weighs erosion more. Not
  defeated by a case in which erosion is large, which the formula prices.
tags:
- cognition
- information-retrieval
date: '2026-11-22'
line:
- distributed-agency
- formal-apparatus
grounds:
- CASE-326
complements:
- CLAIM-891
bears_on:
- QUESTION-095
summary: >-
  [QUESTION-095](../questions.d/QUESTION-095.md)'s readings named erosion of the alternative as a cost the
  record's filing account leaves out: Risko and Gilbert, [THEORY-343](../theory.d/THEORY-343.md), find
  that offloading wears down the internal route. In the model of
  [CASE-326](../cases.d/CASE-326.md), a store route falls back on computing when a demand is not
  one the store serves (chance 1 − π) or when a wrong stored result is
  caught (πσδ). If checking repeats a share φ of the computing route, it
  draws on the eroded skill on every served use as well. So erosion ε costs,
  per demand, εc[(1 − π) + π(σδ + φ)]. It locates where [QUESTION-095](../questions.d/QUESTION-095.md)'s
  erosion term matters. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-326 CLAIM-891 — new; filed in this run of 2026-11-22 -->
<!-- inactive-ok-file: THEORY-343 — Proposed; the reading that names the term, cited as such -->

# CLAIM-892: Erosion of the skill a store replaces costs, per demand, the skill's price times the chance that the demand falls back on it plus the share of the skill that checking the stored result repeats: it weighs little where demand is predictable, the store rarely wrong and checking cheap, as with a cockpit's speed bugs, and most where reuse cannot be forecast or checking re-derives, as with a filed argument

## The claim

In the model of [CASE-326](../cases.d/CASE-326.md) a served demand costs ρ + v + σ[δ(c(1+ε) + R
+ …) + (1 − δ)L] and an unserved one costs miss + c(1+ε) + …, where c(1+ε)
is computing on demand after erosion ε. Let checking repeat a share φ of
the computing route, so that v = v₀ + φc(1+ε). Differentiating the expected
cost per demand in ε:

  ∂/∂ε = c[(1 − π) + π(σδ + φ)].

Everything else in the cost is independent of ε. The test
`test_erosion_weight_is_chance_of_fallback_plus_checking_share` checks it
numerically; `test_erosion_raises_fallback_only` checks the case φ = 0.

## What it shows about the cases

- **The bugs.** π = 1, σ small, and checking compares the card's weight
  with the displayed weight, not recalling a speed (φ near 0). Erosion of
  the crew's memory for speeds weighs about cσδ per read, and in the run an
  erosion of 300% moved the saving from 6.2 to 5.8. Hutchins's point that
  the bugs do not improve any pilot's memory ([NOTE-867](../notes.d/NOTE-867.md)) costs little,
  because the route that memory serves is almost never taken.
- **A filed argument.** π is often low and unforecastable ([CLAIM-308](CLAIM-308.md)), and
  checking that a filed answer is still current partly re-derives it (φ
  well above 0). Erosion then weighs on nearly every use. Whether it bites
  depends on who would reconstruct, which is an owner's choice set out in
  [CLAIM-891](CLAIM-891.md).
- **A LEGO bin.** The route replaced is search, which does not erode with
  disuse in any way the record has, so ε is about 0 whatever its weight.

## What it does not say

- That erosion is small anywhere. ε is a rate the formula weights, not
  estimates; no reading on the record measures it for any of the three.
- That the weighting covers every path. Erosion could also lower δ, the
  chance that checking notices a wrong result, a second-order path the
  formula leaves out; the defeat condition names it.
- That ε is fixed. The model holds it constant; in Risko and Gilbert it
  grows with reliance, which would make it a function of n.
