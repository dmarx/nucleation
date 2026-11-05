---
status: Open
title: 'Can a resource-indexed topological summary of a solution space, such as its persistence or the diameter of its components, detect whether navigating it is computationally easy or hard?'
version: 1
tags:
- mathematics
- complex-systems
date: '2026-11-05'
line:
- formal-apparatus
summary: >-
  A's question, from the pasted synthesis on resource-bounded realizability
  (three responses, pasted by the owner on 2026-11-05, continuing the
  exchange on constraint architectures), Response 3, closing: "Could its
  resource-dependent topology detect transitions between computationally
  easy and hard regimes?" A also says the reverse, in §5, that a
  persistence summary "cannot generally tell you whether finding the path is
  computationally difficult". The readings give one alignment: for Boolean
  languages, "small diameter and tractability of the st-connectivity
  problem are remarkably aligned" (Gopalan et al.). Persistence, one- or
  multiparameter, sees connectivity across budgets and not direction or
  path length. The wording is A's; adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmpbi4ca CLAIM-tmpy685m NOTE-tmp6e0rl NOTE-tmpec4ov NOTE-tmpusebl THEORY-tmpqzxwh — Proposed or Skimmed; A's proposals of 2026-11-04 and 2026-11-05, the readings' accounts and partial readings, and the entries filed beside them, cited as filed, nothing here resting on their being settled -->

# QUESTION-tmp3rkac: Can a resource-indexed topological summary of a solution space, such as its persistence or the diameter of its components, detect whether navigating it is computationally easy or hard?

## Why it is a question

A, in Response 3's closing: "Could its resource-dependent topology detect
transitions between computationally easy and hard regimes?" And in §5: "A
persistent-homology summary might tell you when two folded states become
connected as the allowed bending energy increases. It cannot generally
tell you whether finding the path is computationally difficult, whether an
actuator can execute it, or whether a control policy can follow it
reliably."

**What the readings give.**

- **An alignment of a metric with complexity.** Gopalan, Kolaitis, Maneva
  and Papadimitriou (NOTE-tmpec4ov): for Boolean languages, components have
  linear diameter when st-connectivity is polynomial and can have
  exponential diameter otherwise; "small diameter and tractability of the
  st-connectivity problem are remarkably aligned." Diameter is a property
  of the solution graph, not of a budget filtration, and the alignment is
  across languages, not a test on one instance.
- **What persistence sees.** Sublevel-set persistence records when
  components merge and holes appear as the budget rises (THEORY-tmpqzxwh;
  CLAIM-tmpbi4ca), and its multiparameter form has stable invariants but no
  complete discrete one (Vipond, NOTE-tmpusebl; Botnan and Lesnick,
  NOTE-tmp6e0rl). It forgets direction (CLAIM-tmpy685m) and path length.
- **Summaries can be hard to compute.** Botnan and Lesnick report that the
  interleaving distance between multiparameter modules is NP-hard to
  compute for two or more parameters, so comparing two systems'
  resource-indexed topology is itself a problem with a complexity.

## What would answer it

A summary computable from a family's resource-indexed topology, its
persistence, the diameters of its components or another such invariant,
that separates families easy to navigate from hard ones, with a proof; or
two families with the same summary and opposite navigation complexity,
which would show the summary cannot.

## What would not answer it

An alignment on one family or one instance, or a summary that detects
hardness only because it encodes the solution graph itself.
