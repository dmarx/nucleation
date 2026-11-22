---
status: Proposed
title: 'emergence by predictive efficiency, of one causal description from another: the first is a coarse-graining of the second and is predicted more efficiently, its excess entropy a larger share of its statistical complexity (E/Cµ); the opposite, a coarse-graining predicted less efficiently, is submergence'
version: 1
tags:
- complex-systems
- information-theory
date: '2026-11-22'
line:
- formal-apparatus
complements:
- TERM-062
- TERM-141
draws_on:
- THEORY-tmpttfgp
- THEORY-756
summary: >-
  Shalizi and Moore's definition (LIT-2996, §IV.A, read in NOTE-tmpunt6q;
  THEORY-tmpttfgp): a relation of "emergence" between two sets of causal
  variables "if (1) one is a coarse-graining of the other and (2) the
  coarse-grained variables can be predicted more efficiently", efficiency
  being E/Cµ after Palmer. Their case: argon's internal energy at a 1 ms
  step, 0.87, against its microstate at 1 ns, 0.5. Fills a gap: NOTE-935
  compares Seth's Granger emergence with "Shalizi and Moore's predictive
  efficiency", and the record held no entry for it. The wording is the
  assistant's (Claude, in this session), the definition Shalizi and
  Moore's; adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-tmpttfgp TERM-141 THEORY-257 CLAIM-tmp3ima1 — Proposed or new; the reading this term draws on, the term it complements, the account it is set against and the claim that uses it -->

# TERM-tmpaztqn: emergence by predictive efficiency, of one causal description from another: the first is a coarse-graining of the second and is predicted more efficiently, its excess entropy a larger share of its statistical complexity (E/Cµ); the opposite, a coarse-graining predicted less efficiently, is submergence

## Definition

Take a process and two sets of causal variables for it, each the causal
states (TERM-062) of some observation of it, with statistical complexity
Cµ (the entropy of the causal states) and excess entropy E (the
information past and future share, TERM-141). The **predictive
efficiency** of a description is E/Cµ, "the fraction of the information
it contains which actually effects the future" (after Palmer). A
description A is **emergent** from B when

1. A is a coarse-graining of B (a function of it), and
2. A's predictive efficiency exceeds B's.

When A is a coarse-graining of B and is predicted *less* efficiently,
the relation is what Crutchfield called **submergence** (Shalizi and
Moore, §IV.A, after a personal communication).

Since E ≤ Cµ for causal states (THEORY-756), the efficiency lies in
[0, 1].

## The case

Argon, a cubic centimetre at fixed temperature, pressure and number
(Shalizi and Moore §IV.A, numbers from Shalizi's thesis): the internal
energy has entropy 33.3 bits and entropy rate 4.4 bits per millisecond,
so E = 28.9 bits and E/Cµ = 0.87; the microstate is its own causal
state, Cµ = 6.6·10²⁰ bits, with E = 3.3·10²⁰ bits at a 1 ns step, so
E/Cµ = 0.5 (recomputed: 28.9/33.3 = 0.868). Thermodynamics emerges from
statistical mechanics in this sense: "thermodynamic variables are more
informative about their own dynamics."

## Conditions

- **Relative to the observables.** Each description is the causal
  states of a chosen observation; "A different set of initial variables
  will, generally, lead to a different set of causal states" (§VI). The
  relation compares two such choices; it does not pick one out.
- **Relative to the time step.** The authors note that the argon
  comparison "is rather unfair to the macrostates": at matched resolution
  the macro efficiency would be "essentially one", and the micro at the
  macro time-scale "essentially zero". The verdict depends on the time
  steps at which each is predicted, which the definition does not fix.
- **Exact laws.** The quantities assume the conditional laws known
  exactly; nothing is said about estimating them.

## What it is not

- **Not Granger emergence** (Seth, NOTE-935), which asks whether a macro
  variable is autonomous from, and G-caused by, its micro variables.
- **Not dynamical independence** (THEORY-257) or informational closure
  (THEORY-820), which condition on the microscopic past; this relation
  compares each description's prediction of itself.
- **Not the "predictive efficiency" of THEORY-026** (Still and
  colleagues, named so in NOTE-416), which is the thermodynamic efficiency
  of a driven system's memory, a different quantity.
- **Not symmetric.** By the definition a description cannot be emergent
  from one and also have that one emergent from it, since each requires
  the other to be its coarse-graining with lower efficiency. Shalizi and
  Moore's §IV.B says both of the hydrodynamic and thermodynamic levels,
  which is a slip by this definition (NOTE-tmpunt6q, Limitations).

## Sources

Shalizi and Moore 2003 (LIT-2996, read 2026-11-22 in NOTE-tmpunt6q; the
reading is THEORY-tmpttfgp). Used by CLAIM-tmp3ima1.
