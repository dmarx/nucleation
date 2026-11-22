---
status: Proposed
title: 'A coarse-grained description, the sloppiness of a model and the emergence of one level from another are each defined only relative to a chosen set of observables and a demanded precision, and given that choice the dynamics fix the rest: which partition is causal, which parameter combinations are stiff, and whether one description emerges from another'
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  A definition of macrostate, of sloppiness or of emergence in this
  family, in use by its own authors, whose verdict for a given system is
  shown to be the same under every choice of observables and every
  precision (so that the dynamics alone fix it); or a case in which,
  observables and precision fixed, two applications of one of these
  definitions to the same dynamics give different verdicts, so that the
  dynamics do not fix the rest. A description whose authors call it
  objective does not meet the first clause unless its verdict is shown to
  be invariant under a change of observables.
tags:
- complex-systems
- information-geometry
- information-theory
date: '2026-11-22'
line:
- formal-apparatus
grounds:
- THEORY-tmpx26x7
- THEORY-tmpttfgp
complements:
- CLAIM-820
uses:
- TERM-140
- TERM-135
- TERM-062
- TERM-tmpaztqn
bears_on:
- QUESTION-517
summary: >-
  Alternative (a), the lean, of two filed for one gap; alternative (b) is
  the dated note of 2026-11-22 on [QUESTION-517](../questions.d/QUESTION-517.md), which records the previous
  filer's view that the record already holds this across [TERM-140](../terms.d/TERM-140.md),
  [TERM-135](../terms.d/TERM-135.md) and [CLAIM-820](CLAIM-820.md) and needs no entry. The claim widens what those
  entries hold for sloppiness to coarse-graining and emergence, on two
  readings: Quinn and colleagues ([THEORY-tmpx26x7](../theory.d/THEORY-tmpx26x7.md)), that "sloppiness is a
  property both of the scientific model and the predictions of interest",
  that "The Ising model is not sloppy, and has no beautiful emergent
  theory, unless one only cares about long length and time scales", and
  that ΛCDM is sloppy yet fully determined at the precision of its data;
  and Shalizi and Moore ([THEORY-tmpttfgp](../theory.d/THEORY-tmpttfgp.md)), that the observables are the
  observer's and the causal states then "fixed entirely by the objective,
  microphysical dynamics", "Nature has no preferred questions." The
  wording is the assistant's (Claude, in this session); adopting it is
  the owner's call.
---
<!-- inactive-ok-file: THEORY-tmpx26x7 THEORY-tmpttfgp CLAIM-820 TERM-140 TERM-135 TERM-tmpaztqn THEORY-257 — Proposed or new; the readings this claim rests on, the entries it widens, the term it uses and the account it is set against -->

# CLAIM-tmp3ima1: A coarse-grained description, the sloppiness of a model and the emergence of one level from another are each defined only relative to a chosen set of observables and a demanded precision, and given that choice the dynamics fix the rest: which partition is causal, which parameter combinations are stiff, and whether one description emerges from another

**Alternative (a), the lean.** Filed beside alternative (b), the dated
note of 2026-11-22 on [QUESTION-517](../questions.d/QUESTION-517.md), which holds that no entry is needed.
The owner chooses.

## The claim

Three notions the record holds, each with the same two-part shape:

1. **Coarse-graining (macrostates).** Shalizi and Moore ([THEORY-tmpttfgp](../theory.d/THEORY-tmpttfgp.md)):
   one starts from observables, "the product of our ability to observe the
   system, and our choices about what to predict"; beyond that choice "the
   causal state we use are completely out of our control, fixed entirely
   by the objective, microphysical dynamics. A different set of initial
   variables will, generally, lead to a different set of causal states"
   (§VI). The precision enters too: a litre of gas observed yearly has
   trivial causal states, its variables washing out (§III.C).
2. **Sloppiness (and the effective dimension it gives).** Quinn and
   colleagues ([THEORY-tmpx26x7](../theory.d/THEORY-tmpx26x7.md), §8.2): "sloppiness is a property both of
   the scientific model and the predictions of interest. The Ising model is
   not sloppy, and has no beautiful emergent theory, unless one only cares
   about long length and time scales. And a systems biology model is not
   sloppy if one designs experiments to measure one parameter at a time."
   And precision (§2): a sloppy model "will have an effective
   low-dimensional description if many of its widths are small compared
   to the precision of the predictions demanded. This need not be the
   case": ΛCDM is sloppy and "all parameters are well determined from the
   data". Given the observables and the noise, the Fisher spectrum is
   fixed by the model.
3. **Emergence.** Shalizi and Moore's relation ([TERM-tmpaztqn](../terms.d/TERM-tmpaztqn.md)) compares
   two descriptions, each the causal states of a chosen observation, at
   chosen time steps; its verdict for argon (0.87 against 0.5) moves with
   the time steps, "essentially one" or "essentially zero" at others
   (§IV.A). Quinn and colleagues' Ising sentence ties emergence to the
   same choice of what one cares about.

Hence: for each, the observer supplies the observables and the precision,
and the dynamics (or the model) supply the verdict. None is fixed by the
dynamics alone, and none is a matter of taste once the choice is made.
Shalizi and Moore's "for every question we ask It, Nature has a definite
answer; but Nature has no preferred questions" (§VI) states it for the
first; the claim is that it holds for all three.

## Which gap it fills

The record held the relativity for sloppiness, in [TERM-140](../terms.d/TERM-140.md) ("Relative to
a design"), [TERM-135](../terms.d/TERM-135.md) (condition 1, relative to an experiment) and
[CLAIM-820](CLAIM-820.md) (relative to the observables fitted and, since version 3, to
the precision demanded). It held causal states as target-relative
([TERM-062](../terms.d/TERM-062.md)). It did not hold that coarse-graining, sloppiness and
emergence share the shape, nor Shalizi and Moore's reading, now read,
that this is what makes macrostates both subjective and objective. Two
readings of 2026-11-22 (Quinn and colleagues; Shalizi and Moore) supply
it, and [QUESTION-517](../questions.d/QUESTION-517.md)'s "What would answer it" needs it named: an
effective dimension is to be stated with its observables and precision.

## What it does not say

- Not that any choice of observables is as good as any other. Shalizi
  and Moore rank choices by efficiency (emergence); Quinn and colleagues
  ask whether "caring about the answers to the right questions" is what
  makes science possible, a speculation the record leaves in the reading.
- Not that dynamical independence ([THEORY-257](../theory.d/THEORY-257.md)), which the record holds
  fixes macrovariables "by the dynamics rather than by a chosen query",
  is wrong: it is a further criterion within a chosen class of
  coarse-grainings, and the claim's first defeater clause asks that such
  a criterion be shown invariant under a change of observables.
- Not that the three notions agree on a given system; that is
  [QUESTION-517](../questions.d/QUESTION-517.md).

## Where it rests

Interpretive: two readings, each stating the relativity for its own
notion, joined by the assistant. Grounds [THEORY-tmpx26x7](../theory.d/THEORY-tmpx26x7.md) and
[THEORY-tmpttfgp](../theory.d/THEORY-tmpttfgp.md); complements [CLAIM-820](CLAIM-820.md).
