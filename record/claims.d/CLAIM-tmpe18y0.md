---
status: Proposed
title: 'Families of constrained systems on different physical substrates may admit equivalent resource-bounded process structures under two-way resource simulation with bounded overhead, even where their configuration spaces and microscopic dynamics differ, and the classes so defined for feasibility, reachability, control and regeneration need not coincide'
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  For families of the kinds A names, rigid-origami mechanisms built from
  bounded local primitives, finite constraint networks and organizational
  models declared with a size parameter: a proof or a systematic finding
  that no two-way resource simulation with polynomial overhead exists
  between two of them that preserves the costs of processes and not only
  the yes or no of reachability; or that every simulation found works only
  by declaring the transition graph directly, the triviality
  TERM-tmpckwjg names; or that the structures preserved are only those the
  compatibility complex already carries. Also defeated as new, though not as
  true, if it asserts no more than the mutual reducibility of families whose
  reconfiguration is PSPACE-complete, which the readings already give. Not
  defeated, or confirmed, by agreement or disagreement in one small
  example.
tags:
- complex-systems
- mathematics
- philosophy-of-science
date: '2026-11-05'
line:
- realizability
grounds:
- THEORY-tmp34oop
- THEORY-tmpmcxbv
uses:
- TERM-tmpckwjg
- TERM-tmpr3hl8
bears_on:
- QUESTION-tmpkcffa
summary: >-
  A's hypothesis, from the pasted synthesis on resource-bounded
  realizability (three responses, pasted by the owner on 2026-11-05,
  continuing the exchange on constraint architectures), stated three times:
  Response 1 §3 (universality by efficient mutual simulation, U_comp and
  U_phys as "two potentially independent classifications"), Response 2 §6
  ("Resource-bounded constraint systems may admit universality classes
  defined by" their feasible configurations, resource-indexed
  transformations and modifiable architectures), and Response 3 §8
  ("Families of constrained systems with different physical substrates may
  admit equivalent resource-bounded process structures"). Merged as one
  claim, stated in [TERM-tmpckwjg](../terms.d/TERM-tmpckwjg.md)'s computational sense. A does not present
  it as a theorem. Interpretive: no such equivalence is shown; the honest
  defeaters include that it may say no more than PSPACE-completeness
  already does. The wording is A's; adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmp06538 CLAIM-tmplysd0 NOTE-tmpec4ov TERM-tmpckwjg TERM-tmpr3hl8 THEORY-tmp34oop THEORY-tmpmcxbv — Proposed or Skimmed; A's proposals of 2026-11-04 and 2026-11-05, the readings' accounts and partial readings, and the entries filed beside them, cited as filed, nothing here resting on their being settled -->

# CLAIM-tmpe18y0: Families of constrained systems on different physical substrates may admit equivalent resource-bounded process structures under two-way resource simulation with bounded overhead, even where their configuration spaces and microscopic dynamics differ, and the classes so defined for feasibility, reachability, control and regeneration need not coincide

## The claim

A, three times.

- Response 1 §3: "Two resource-bounded constraint systems belong to the
  same computational universality class when they can efficiently simulate
  one another in a way that preserves constraint satisfaction, permitted
  transformations, and resource requirements up to a specified overhead."
  Physical constraints "would enter in a second layer", giving "two
  potentially independent classifications".
- Response 2 §6: "Resource-bounded constraint systems may admit
  universality classes defined by the structure of their feasible
  configurations, the resource-indexed transformations between those
  configurations, and the operations by which their constraint
  architectures can themselves be modified and maintained." "I wouldn't
  present that as a theorem yet."
- Response 3 §8: "Families of constrained systems with different physical
  substrates may admit equivalent resource-bounded process structures,
  even when their geometric configuration spaces and microscopic dynamics
  differ." "The challenge would be to find nontrivial examples and
  establish the equivalence mathematically."

And that the classes may split: "It might turn out that there are several
related universality classes, depending on whether we're classifying
feasibility, reachability, control, or regeneration" (Response 2 §5).

**Stated in the record's terms.** Equivalence is two-way resource
simulation, or a resource-aware bisimulation, with overhead bounded by an
order-preserving resource transformation ([TERM-tmpckwjg](../terms.d/TERM-tmpckwjg.md)'s computational
sense), between families of [TERM-tmpr3hl8](../terms.d/TERM-tmpr3hl8.md)'s systems; the classes are taken
separately for which configurations are feasible, which are reachable at
which budgets, which can be driven by the inputs, and which regenerate.

**What the record holds toward it.**

- **Within one substrate, a structure-preserving universality.** Gopalan et
  al. ([NOTE-tmpec4ov](../notes.d/NOTE-tmpec4ov.md); [THEORY-tmpmcxbv](../theory.d/THEORY-tmpmcxbv.md)): from a Boolean language that is not
  tight every relation is faithfully expressible, preserving connectivity
  of solutions, and the navigation problems are PSPACE-complete. That is a
  universality of navigation structure within Boolean CSPs.
- **Across folding and constraint logic, at the decision level.** Eppstein
  ([NOTE-tmpv7lp6](../notes.d/NOTE-tmpv7lp6.md); [THEORY-tmp34oop](../theory.d/THEORY-tmp34oop.md)) proves flaps-and-flips connectivity
  PSPACE-complete by reduction from nondeterministic constraint logic. The
  reduction preserves the yes or no of reachability, not the costs of
  paths, and the model is a toy that its author does not offer as origami
  in general.
- **One pair of physical substrates for logic.** The origami Boolean
  networks ([LIT-tmpmjw68](../literature.d/LIT-tmpmjw68.md)) implement logic in folding states; that is the
  expressive sense, for combinational functions.

## What it does not say

- **That any such equivalence exists.** None is shown. A's own test is a
  three-way comparison under scaling ([QUESTION-tmpkcffa](../questions.d/QUESTION-tmpkcffa.md)): "Agreement in one
  small example would be evidence of a shared model, not a universality
  theorem."
- **That it is new at the decision level.** Families whose reconfiguration
  is PSPACE-complete are already mutually reducible in polynomial time. The
  hypothesis says more only if its simulations carry the costs of
  processes and the other structures A lists.
- **That organizations are such families.** An organizational model has no
  size parameter until one is declared ([CLAIM-tmplysd0](CLAIM-tmplysd0.md)), and without one
  neither the computational nor the scaling sense applies to it.
- **That the obstruction profile is shared.** A's "substrate-independent"
  obstruction levels ([CLAIM-tmp06538](CLAIM-tmp06538.md)) would be one structure such a
  simulation preserves; the hypothesis includes it and the record has not
  tested it.

## Note of 2026-11-05: the resource-bounded realizability readings

The second paste of the pasted synthesis on resource-bounded realizability revises the hypothesis. A universality theory "should classify the structures preserved when configurations, processes, and constraint-maintenance mechanisms are translated across substrates, relative to declared computational and observational regimes", and its central problem is when composition and reconfiguration "create new effective possibilities, representations, or obstructions that persist across those translations". The revision adds maintenance mechanisms to what is translated, and makes the classification relative to a declared regime, as in [TERM-065](../terms.d/TERM-065.md)'s effective-description regimes. The third paste states the hypothesis for relational profiles, in the conjecture [QUESTION-tmptcuch](../questions.d/QUESTION-tmptcuch.md) records. A still offers it as a conjecture. No status changes.
