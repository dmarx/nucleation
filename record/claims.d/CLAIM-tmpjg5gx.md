---
status: Proposed
title: 'A norm can be stabilized by the reliance it attracts: compliance makes a practice predictable, others specialize around it, and their stake in its continuation funds its maintenance, which raises compliance, so a practice established past a threshold can persist where a weakly established one would not, and can outlast a weakening of the reasons that first supported it'
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  A showing that, in the cases the claim covers, the persistence of norms
  around which much activity has specialized is fully explained without the
  reliance loop, by conformity, sanctions or coordination payoffs that do
  not depend on how much has been built on the norm, so that varying the
  amount of dependent investment while holding those fixed leaves the
  norm's persistence unchanged; or a showing that norms with heavy dependent
  investment do not persist after their original reasons weaken any more
  often than norms without it.
tags:
- social-ontology
- complex-systems
date: '2026-11-24'
line:
- organizational-normativity
- dependence-and-domination
complements:
- CLAIM-tmphq6hp
- CLAIM-277
- CLAIM-785
- CLAIM-475
bears_on:
- QUESTION-128
summary: >-
  A22 §§3–5 of the exchange "Memes, Contracts, and Systemic Normativity"
  (ChatGPT, 2026-11-24), at the owner's U17. "Our framework adds a
  complementary mechanism: the accumulation of organizational investments
  that presuppose the norm's continued operation." "A practice might
  originally be adopted because it is convenient. Later it becomes
  indispensable because everything else has adapted to it." A22's model,
  x' = σ(b + λg) − x, r' = α(x − r), g' = β(rx − g), has equilibria with
  x* = σ(b + λx*²). The assistant's check finds the bistability A22
  asserts, its threshold, and the hysteresis that carries the "outlast"
  clause, within limits (see the body). The wording is A's (ChatGPT, in the
  exchange 'Memes, Contracts, and Systemic Normativity'), and the checks
  are the assistant's (Claude, in this session); adopting it is the owner's
  call.
---

<!-- inactive-ok-file: CLAIM-tmphq6hp CLAIM-785 CLAIM-tmp1nubb — Proposed; the operative-norm claim filed with this and the held claim on predicates as constraints -->

# CLAIM-tmpjg5gx: A norm can be stabilized by the reliance it attracts: compliance makes a practice predictable, others specialize around it, and their stake in its continuation funds its maintenance, which raises compliance, so a practice established past a threshold can persist where a weakly established one would not, and can outlast a weakening of the reasons that first supported it

## The claim

A22 §3: "Consider a practice n that is initially contingent. Repeated
compliance makes it predictable. Other processes then specialize around
that predictability. Over time, changing the practice becomes increasingly
costly because more activities depend upon it." The loop: regular
compliance, increasing reliance, rising cost of deviation, resources spent
on enforcement, more compliance. "Compliance produces reasons for further
compliance."

This adds to the usual mechanisms of norm stability ("incentives,
conformity, social expectations, sanctions and coordination equilibria") a
mechanism that grows with what others have built on the norm: "This would
help explain why norms can persist even after their original justification
disappears."

## The model, and the assistant's check

A22 §5 writes compliance x, reliance r and maintenance resources g as

- x' = σ(b + λg) − x,
- r' = α(x − r),
- g' = β(rx − g),

with σ the logistic function, b a baseline tendency to comply, and λ the
strength of maintenance feedback. At equilibrium r* = x*, g* = (x*)², so
x* = σ(b + λ(x*)²), and "For some parameters, this admits multiple
equilibria."

The assistant checked this with `python3 -I`, finding fixed points of the
reduced equation and the eigenvalues of the full three-variable Jacobian
(α = β = 0.2, A22's settings):

- **Bistability.** With b = −3 and λ = 8 (A22's defaults) there are three
  equilibria: x* ≈ 0.048 (stable), 0.689 (a saddle, one positive
  eigenvalue ≈ 0.13) and 0.993 (stable). With b = −3, bistability needs
  λ above about 6.4; with λ = 8, it holds for b from about −4.33 to about
  −1.57, and above that only the high state exists, below it only the low.
- **The threshold.** Started at x = r = s, g = s², the system goes to the
  high state only for s above ≈ 0.689, the saddle. A22's widget default,
  s = 0.6, falls to the low state (x ≈ 0.048): the "sufficiently
  established practice" has to be established past roughly 69% compliance
  at these settings.
- **Outlasting its reasons, within limits.** A practice established where
  only the high state exists (b = −1) and then subjected to a fall in b
  stays high down to b = −4.3 (x ≈ 0.95), while the same practice started
  fresh at b = −4.3 dies out (x ≈ 0.013); at b = −4.5 the established
  practice also collapses. So in the model the loop lets a norm outlast a
  weakening of its baseline support by a margin set by λ, not its
  disappearance.

The check narrows A22's sentence "norms can persist even after their
original justification disappears": in this model they persist after the
reasons weaken, up to a point, not after they vanish; persistence after
they vanish would need maintenance feedback large enough that the high
state exists at any baseline the reasons' loss leaves.

## What it does not say

- Not that the stabilized norm is good. A22 §3: "The pathology does not
  consist simply in stabilization. It concerns what becomes stabilized,
  whose interests it serves and whether revision remains possible."
- Not that the model forms a standard. A22 §5: "The model does not
  demonstrate endogenous formation of a standard of correctness: its
  maintenance rule is supplied by the modeler. It demonstrates a candidate
  stabilization mechanism." That leaves QUESTION-128 where it was.
- Not that reliance is the only stabilizer. A22 §16 lists seven
  mechanisms that can produce the same compliance (CLAIM-tmp1nubb).

## Relation to the record

CLAIM-277's loop, trust as the regularity of grants that "entrenches
whatever gained influence early", is the same shape applied to authority
among processes. CLAIM-785's accrual of predicates, which stabilizes an
entry "from prose convention to lint rule", is A22 §4's example of a norm
"more strongly realized through its progressive incorporation into an
organization's material and procedural architecture".
