---
number: 598
status: Active
formerly:
- CLAIM-tmpt0fnx
title: 'Whether more of every resource raises, leaves or lowers the chance that an assembly reaches its target depends, at each branch point, on whether the competing steps consume further resource: a branch whose steps all consume alike is unchanged by uniform abundance, and one where the wrong step consumes and the right one does not is made worse by it, as Majikes et al. report for a single DNA origami fold that excess staples block'
version: 2
history:
- version: 2
  date: '2026-11-06'
  note: >-
    Narrowed and promoted at the status review's ruling (the owner
    delegated these rulings; ADR-057, ADR-058): the title's last
    clause read "as DNA origami's blocked single fold is by staple
    excess", an empirical assertion in a demonstrated claim, carried
    by THEORY-1457 (Proposed); it is now an attribution, and
    THEORY-1457 corroborates the claim. CASE-217, its one premise, was
    promoted in the same change.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the argument: a first-order branching process in which
  scaling the supply of every component by λ changes the choice at a branch
  point whose competing steps have the same order in that supply, or leaves
  unchanged a choice whose steps differ in order. Not defeated by assembly
  that is not first-order in the supply, by cooperative steps whose order
  changes with the state, or by finite-horizon effects of slow steps, which
  the claim excludes or treats separately.
tags:
- complex-systems
- mathematics
- natural-sciences
date: '2026-11-05'
line:
- realizability
- readiness
- formal-apparatus
grounds:
- CASE-217
bears_on:
- QUESTION-400
- QUESTION-380
complements:
- CLAIM-594
corroborated_by:
- THEORY-1457
summary: >-
  The assistant's, from A's second synthesis on DNA origami, pasted by the
  owner on 2026-11-05. In A's branching model of assembly, the chance of
  reaching the target is a product of branch choices, each a ratio of the
  rates of the competing steps. If supply rises uniformly by λ, a step that
  consumes a further unit, binding another molecule, speeds up by λ, while
  a step within what is already assembled does not. So a choice is
  unchanged by abundance when its competing steps consume alike, and
  shifted when they differ. More of everything hurts where the wrong step
  consumes and the right one does not. Majikes et al. 2021 find exactly
  this for one fold of a DNA origami: two staple molecules can each take
  one end and block it, and the folded share j/(j + S₀) falls as staple
  excess rises. A's remark that "The relevant resource isn't always total
  abundance" is thus made exact. The wording is the assistant's (Claude, in
  this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-215 — Proposed or new; the model, the companion claim, the question it bears on, and the slack claim it qualifies -->

# CLAIM-598: Whether more of every resource raises, leaves or lowers the chance that an assembly reaches its target depends, at each branch point, on whether the competing steps consume further resource: a branch whose steps all consume alike is unchanged by uniform abundance, and one where the wrong step consumes and the right one does not is made worse by it, as Majikes et al. report for a single DNA origami fold that excess staples block

## The claim

Let an assembly pass through states s, and from each state let competing
first-order steps leave at rates k_i(s) λ^{m_i}. Here λ scales the supply of
every component, and m_i is how many further units of supply step i
consumes: 1 for binding another molecule, 0 for a step within what is
already assembled. With absorbing outcomes, the chance of reaching the
target is a sum over paths of products of branch shares

  k_i λ^{m_i} / Σ_j k_j λ^{m_j}.

1. **Equal order, no effect.** If all steps competing at a state have the
   same m, the λ factors cancel and the share is independent of λ. More of
   everything changes only how fast the system moves, not where it goes.
2. **Unequal order, an effect.** If they differ, the share of the
   higher-order steps rises with λ. The chance of the target rises with
   abundance where the right step consumes more than the wrong one, and
   falls where the wrong step consumes more.
3. **Relative availability.** Shifting supply between components, as
   opposed to scaling it, changes the k_i and moves the shares even where
   every m is equal. This is A's "Guided nucleation" row ([CASE-217](../cases.d/CASE-217.md)).

4. **Timing at equal integrated exposure.** The same reasoning applies over time.
   Supply that arrives while the system is in a state whose wrong step
   consumes it does harm there, and does good where the right step does.
   So whether front-loading or delay is better depends on which steps the
   supply enters. In [CASE-215](../cases.d/CASE-215.md), with integrated exposure ∫c dt fixed (not a\n   conserved stock), the yield
   front-loaded, even or delayed is 70.6, 58.8 and 24.8 % when nucleation
   uses the supply. It is 45.4, 58.8 and 65.3 % when the supply traps the
   unnucleated scaffold and completes the nucleated one.

Shown in [CASE-217](../cases.d/CASE-217.md), and for timing in [CASE-215](../cases.d/CASE-215.md). At A's baseline, with the trap entered from the
nucleus by binding a further molecule and completion intramolecular, the
yield falls from 59.3 % at λ = 1 to 19.0 % at λ = 20. If every step
consumes alike, it stays at 59.3 %.

## The molecular instance

Majikes et al. 2021 ([NOTE-1633](../notes.d/NOTE-1633.md), [THEORY-1457](../theory.d/THEORY-1457.md)), read in this pull request: for one staple-mediated
fold, closing the fold is intramolecular (its effective concentration j),
while blocking it takes a second staple molecule (concentration S₀). Their
equilibrium model gives folded/blocked = j/S₀ at high excess, so yield
1/(1 + S₀/j), falling as excess rises. This is point 2 with m = 0 against
m = 1, at equilibrium rather than kinetically. Rothemund found whole
rectangles indistinguishable at 9:1 and 100:1 excess. That is consistent
with Majikes et al.'s hypothesis that folding displaces blocking strands,
which changes the order of the wrong step as assembly proceeds.

## What it adds

- **To [QUESTION-400](../questions.d/QUESTION-400.md).** Allocation and abundance act through
  different terms: reallocation through the k_i, uniform abundance only
  through differences in m.
- **To readiness.** Slack held as uniform surplus is not neutral. It helps
  where the productive steps draw on it, and harms where the
  counterproductive steps do, as staple excess shows. This qualifies
  [CLAIM-577](CLAIM-577.md)'s reading of excess as standing slack.
- **To [CLAIM-594](CLAIM-594.md).** Both name a resource whose amount changes which
  outcome is reached, not only how fast. Heat does it by changing costs;
  abundance does it by the order of the steps that draw on it.

## What it does not say

- **That DNA origami assembly is first-order in staple supply throughout.**
  Cooperativity changes effective orders state by state.
- **Anything about organizations** beyond the logic. Which organizational
  steps "consume" a resource, and which do not, needs a model of its own.
