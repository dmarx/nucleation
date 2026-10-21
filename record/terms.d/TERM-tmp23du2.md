---
status: Proposed
title: 'causal state, of a process relative to a target future: a class of pasts that induce the same conditional law over that future, the coarsest prescient partition of the pasts; the ε-machine when the future is the process''s own, the υ-machine when it is a coarse-graining''s future predicted from the micro past'
version: 1
tags:
- information-theory
- complex-systems
date: '2026-10-21'
line: formal-apparatus
summary: >-
  Crutchfield and Shalizi's causal states ([THEORY-756](../theory.d/THEORY-756.md), from [LIT-1260](../literature.d/LIT-1260.md)) and
  Rosas et al.'s υ-machine ([THEORY-820](../theory.d/THEORY-820.md)), under one definition with the
  target and the source of the pasts explicit. Used in [THEORY-820](../theory.d/THEORY-820.md),
  [THEORY-756](../theory.d/THEORY-756.md) and [CLAIM-152](../claims.d/CLAIM-152.md) with no TERM. A13 of the exchange of
  2026-10-20: "A TERM would make that concept discoverable before someone
  knows which theorem to search for", and A14 asked that it say whose
  histories are taken. It is the owner's U13 category exactly,
  "definitions we've crystallized that are not currently in conflict".
  Proposed: recorded, not adopted. A13 called it "predictive state"; the
  record's word is kept.
---
<!-- inactive-ok-file: TERM-tmpfezzd — Proposed; the disambiguation of closure filed from the same exchange -->

# TERM-tmp23du2: causal state, of a process relative to a target future: a class of pasts that induce the same conditional law over that future, the coarsest prescient partition of the pasts; the ε-machine when the future is the process's own, the υ-machine when it is a coarse-graining's future predicted from the micro past

## Definition

Fix a source of pasts (a process W, with past W⃗_t) and a target future
(a block Z⃗⁺ of some process Z). Two pasts are equivalent when they induce
the same conditional law over the target:

w⃗ ∼ w⃗′ ⟺ P(Z⃗⁺ | W⃗_t = w⃗) = P(Z⃗⁺ | W⃗_t = w⃗′), at every block length.

A **causal state** is a class of this relation. A13 gave the relation as
h ∼_Z h′ ⟺ P(Z_future | h) = P(Z_future | h′), and A14 asked that the
entry "state explicitly whether the histories are taken from the
microscopic process or from the macro process. [THEORY-820](../theory.d/THEORY-820.md) depends on
comparing those two predictive-state partitions." So:

- **ε-machine**, W = Z: a process's own pasts for its own future
  (Crutchfield and Shalizi; [THEORY-756](../theory.d/THEORY-756.md)).
- **υ-machine**, W = X and Z = g(X⃗): the micro pasts for a
  coarse-graining's future (Rosas et al.; [THEORY-820](../theory.d/THEORY-820.md) (b)).

The partition is the coarsest prescient one: any function of the pasts
that carries all they carry about the target future refines it
([THEORY-820](../theory.d/THEORY-820.md) (b), [THEORY-756](../theory.d/THEORY-756.md)). For a coarse-graining Z, the two coincide
exactly when Z is informationally closed ([THEORY-820](../theory.d/THEORY-820.md) (c); [TERM-tmpfezzd](TERM-tmpfezzd.md),
sense 1).

## What it is not

- **Not "predictive state" in a separate sense.** A13's name. The
  record's word is causal state, and the title keeps it.
- **Not any sufficient statistic.** It is the coarsest one ([THEORY-820](../theory.d/THEORY-820.md) (b),
  [THEORY-756](../theory.d/THEORY-756.md)).
- **Not target-free.** It is canonical only given the target, and the
  target only given the measuring instrument ([CLAIM-152](../claims.d/CLAIM-152.md)'s note of
  2026-10-20, from Crutchfield and Shalizi's logistic map).
- **Not interventional.** The classes are of conditional laws, so "causal"
  here is predictive, as in [THEORY-820](../theory.d/THEORY-820.md)'s Granger sense.
