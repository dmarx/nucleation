---
status: Proposed
title: 'Shalizi and Moore propose that, for a chosen set of observables of a system with Markov microdynamics, the macrostates are the causal states of the observed process, the coarsest partition of observation histories that predicts the observables as well as the whole history does and whose own dynamics is therefore Markov, so that which observables to start from is the observer''s choice and the partition reached from them is fixed by the dynamics; and they call one causal description emergent from another when it is a coarse-graining of it and is predicted with higher efficiency E/Cµ, arguing both from examples rather than new theorems'
promote_when: >-
  An independent source, or a worked model in the record, takes a stated
  observation function on a stated Markov microdynamics, computes the
  causal states of the observed process, shows that they are Markov and
  recover (or knowingly refine or coarsen) the system's accepted
  macrostates, and shows that the E/Cµ comparison ranks that
  coarse-graining above the micro description.
version: 1
tags:
- complex-systems
- thermodynamics
- information-theory
date: '2026-11-22'
source:
- LIT-2996
bears_on:
- QUESTION-517
corroborates:
- CLAIM-152
summary: >-
  Shalizi and Moore (2003), [LIT-2996](../literature.d/LIT-2996.md), read in [NOTE-tmpunt6q](../notes.d/NOTE-tmpunt6q.md). Their answer
  to whether macrostates are objective or subjective is "both": the
  observables are the observer's, the causal states reached from them are
  fixed by the dynamics. "A different set of initial variables will,
  generally, lead to a different set of causal states"; "Nature has no
  preferred questions." Their emergence is a coarse-graining predicted
  more efficiently (argon: 0.87 against 0.5), held in [TERM-tmpaztqn](../terms.d/TERM-tmpaztqn.md).
---
<!-- inactive-ok-file: TERM-tmpaztqn THEORY-257 CLAIM-tmp3ima1 — Proposed or new; the term filed from this reading, the account it contrasts with and the claim it grounds -->
<!-- inactive-ok-file: THEORY-tmpx26x7 — Proposed; the reading of Quinn and colleagues, joined with this one in CLAIM-tmp3ima1 -->

# THEORY-tmpttfgp: Shalizi and Moore propose that, for a chosen set of observables of a system with Markov microdynamics, the macrostates are the causal states of the observed process, the coarsest partition of observation histories that predicts the observables as well as the whole history does and whose own dynamics is therefore Markov, so that which observables to start from is the observer's choice and the partition reached from them is fixed by the dynamics; and they call one causal description emergent from another when it is a coarse-graining of it and is predicted with higher efficiency E/Cµ, arguing both from examples rather than new theorems

## Source

Shalizi and Moore, "What Is a Macrostate? Subjective Observations and
Objective Dynamics", arXiv cond-mat/0303625 (2003), published in
Foundations of Physics 55, 2 (2025), [LIT-2996](../literature.d/LIT-2996.md), read in full from the
arXiv PDF in [NOTE-tmpunt6q](../notes.d/NOTE-tmpunt6q.md).

## What was actually argued

- Abstract: macrostates are "the unique maximal partition of phase space
  which 1) is consistent with our observations (a subjective fact about
  our ability to observe the system) and 2) obeys a Markov process (an
  objective fact about the system's dynamics)"; one refines "until we
  reach a set of states which predict their own future, i.e. which are
  Markovian".
- §II, cited from Shalizi and Crutchfield (2001): "the causal states form
  the coarsest possible prescient partition".
- §III: the causal partition can equal the observed one (P, V, T of an
  ideal gas), refine it (hysteresis, spin glasses) or coarsen it (the
  nematic director, n = −n; variables that wash out).
- §III.D: "In the causal states we have arrived, so to speak, at objective
  explanations of subjective quantities."
- §IV.A, argon (numbers from Shalizi's thesis): macrostate E/Cµ = 28.9/33.3
  = 0.87 at a 1 ms step, microstate 3.3·10²⁰/6.6·10²⁰ = 0.5 at 1 ns; "This
  leads us to define a relation of “emergence” between two sets of causal
  variables if (1) one is a coarse-graining of the other and (2) the
  coarse-grained variables can be predicted more efficiently."
- §IV.B: thermodynamic and hydrodynamic descriptions "coexist, because
  they are intended to answer different questions — not because one is
  more objective than the other."
- §VI: "A different set of initial variables will, generally, lead to a
  different set of causal states"; "for every question we ask It, Nature
  has a definite answer; but Nature has no preferred questions."

What could have failed: the causal states of the observed thermodynamic
variables could have been as costly to predict as the microstates; on
the argon numbers they are more efficient.

## What this does not say

- Not that the dynamics alone fix the macrostates: they fix them given
  the observables.
- Not closure relative to the microscopic past: the macro process is
  Markov in its own past; informational closure ([THEORY-820](THEORY-820.md)) and
  dynamical independence ([THEORY-257](THEORY-257.md)) condition on the micro past, and
  the paper makes no comparison.
- No new theorems: optimality is cited; the argon numbers come from the
  thesis; noise-free observations and known conditional laws are assumed.
- Not why good macrovariables are extensive or reusable (§V, left open).

## Connections

Supports [TERM-062](../terms.d/TERM-062.md)'s target-relativity and [THEORY-756](THEORY-756.md). Contrast with
[THEORY-257](THEORY-257.md) and [THEORY-820](THEORY-820.md). Grounds [TERM-tmpaztqn](../terms.d/TERM-tmpaztqn.md) and, with Quinn and
colleagues ([THEORY-tmpx26x7](THEORY-tmpx26x7.md)), [CLAIM-tmp3ima1](../claims.d/CLAIM-tmp3ima1.md). Bears on [QUESTION-517](../questions.d/QUESTION-517.md).
