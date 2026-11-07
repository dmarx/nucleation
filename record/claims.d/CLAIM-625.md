---
number: 625
status: Proposed
formerly:
- CLAIM-tmptwm5l
title: "Over time intervals, gluing and continuation are different properties of histories: under local dynamics and a pointwise viability constraint the viable histories form a sheaf, yet restriction from a longer interval to a shorter need not be onto, and a viable history on [0, t] extends viably to [0, T] exactly when its endpoint can stay viable for the remaining time, so a coherent history can be terminal"
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  A time-invariant system with a pointwise constraint set in which the
  viable histories fail to glue, or in which a viable history whose
  endpoint lies in the finite-horizon viability kernel has no viable
  extension, or one whose endpoint lies outside it has one. Also defeated
  if it only restates CLAIM-131's split between gluing and extension: the
  claim must add the temporal reading, in which extension is the
  finite-horizon viability kernel of THEORY-134. Not defeated by
  time-dependent constraints or non-local conditions, where the viable
  histories need not form a sheaf.
tags:
- mathematics
- complex-systems
date: '2026-11-07'
line:
- realizability
- formal-apparatus
grounds:
- THEORY-134
complements:
- CLAIM-131
- CLAIM-079
summary: >-
  A24 and A25 §2 of the exchange "Individuation, Possibility, and
  Disposition" (2026-11-06 to 07), answering the owner's U11, which asked
  whether the inquiry was "circling back towards some of the
  sheaf/topos-theoretic machinery". A: "gluing is about agreement on
  overlaps; continuation is about whether a history has an admissible
  future". It is the temporal case of [CLAIM-131](CLAIM-131.md)'s split between gluing and
  extension. The identification of extension with [THEORY-134](../theory.d/THEORY-134.md)'s viability
  kernel over the remaining horizon is the reader's qualification of A's
  "promising formal bridge". The wording is A's; adopting it is the
  owner's call.
---
<!-- inactive-ok-file: CASE-231 — filed from the same exchange, Proposed -->

# CLAIM-625: Over time intervals, gluing and continuation are different properties of histories: under local dynamics and a pointwise viability constraint the viable histories form a sheaf, yet restriction from a longer interval to a shorter need not be onto, and a viable history on [0, t] extends viably to [0, T] exactly when its endpoint can stay viable for the remaining time, so a coherent history can be terminal

## The claim

A24 of the exchange "Individuation, Possibility, and Disposition"
(https://chatgpt.com/share/6aee7a9b-f13c-83e9-a865-6a29c2c3ff7e): "gluing
is about agreement on overlaps; continuation is about whether a history
has an admissible future". A25 §2 assigns to each interval the admissible
trajectories over it, and for I ⊆ J notes of the restriction map that
"this map need not be surjective". Its example is ẋ = −1 with x > 0 and
x(0) = 1: the history is viable on every [0, T] with T < 1 and has no
viable continuation past t = 1. "A sheaf can describe a coherent history
that is nevertheless terminal."

A25 §2 forms the subsheaf of viable histories, those staying in the
constraint set K, and says: "For local dynamics and pointwise viability
conditions, these viable histories inherit the usual gluing properties."

**The reader's qualification.** A calls this "a very promising formal
bridge" to viability kernels. Made exact: for time-invariant dynamics, a
viable history on [0, t] extends to a viable history on [0, T] exactly
when its endpoint lies in the set of states from which some evolution
stays in K for time T − t, the finite-horizon form of [THEORY-134](../theory.d/THEORY-134.md)'s
viability kernel. Time-invariance is what lets the remaining horizon be
shifted to start at 0.

This is [CLAIM-131](CLAIM-131.md)'s distinction carried from contexts to time intervals.
In both, a compatible family glues and the obstruction is that a
restriction map is not onto. For contexts the missing extension is a
global section; for intervals it is a future.

## What it does not say

- That the sheaf of viable histories says how likely continuation is. On
  the A ↔ B → D chain of [CASE-231](../cases.d/CASE-231.md) every finite horizon has surviving
  histories, while surviving forever has probability zero (A25 §3).
- Anything about time-dependent constraints or conditions on whole
  histories, where gluing itself can fail.
