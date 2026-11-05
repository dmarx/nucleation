---
status: Proposed
title: 'A one-degree-of-freedom precision stage: five independent constraints leave one usable motion, and two designs with the same freedom space, one with every constraint doubled, differ in disturbance error and in drive force'
version: 1
standing: fictional
kind: construction
tags:
- mathematics
- natural-sciences
date: '2026-11-05'
line:
- distributed-agency
illustrates:
- CLAIM-345
summary: >-
  A's proposal, from the pasted synthesis on constraint architectures
  (pasted by the owner on 2026-11-04, continuing the exchange on emergency
  readiness whose share link could not be fetched), Part 1: a
  one-degree-of-freedom stage, freedom dimension 1 and constraint
  dimension 5, and "compare designs with identical freedom spaces and
  different stiffnesses". Built here as a linear stiffness model with two
  designs, the second adding a redundant twin to every constraint: the
  freedom space is the same, the disturbance error halves and the drive
  force doubles, so neither design dominates. Hopkins's theses supply the
  fact the construction turns on, that redundant constraints change
  stiffness, load capacity and stability and leave the kinematics alone.
  An analogue, static, of [CLAIM-345](../claims.d/CLAIM-345.md)'s point, which A proposed to extend
  by a dated note rather than a new claim. The construction is the
  filer's, from A's one-degree-of-freedom stage; adopting it is the
  owner's call.
---
<!-- inactive-ok-file: NOTE-tmpla9de NOTE-tmpnscd2 — Skimmed; Hopkins's 2007 and 2010 theses, the readings the quotations come from -->
<!-- inactive-ok-file: THEORY-tmpmbmox THEORY-tmpeo94c — Proposed; the readings' accounts, cited as filed, nothing here rests on their being settled -->

# CASE-tmpzms3l: A one-degree-of-freedom precision stage: five independent constraints leave one usable motion, and two designs with the same freedom space, one with every constraint doubled, differ in disturbance error and in drive force

## The case

**Setting (A's).** A rigid stage held by flexures, small motions. A
twist t = (v, ω) and a wrench w = (f, τ) pair by power, ⟨w, t⟩ = fᵀv +
τᵀω. An ideal constraint transmits a wrench and permits exactly the
twists reciprocal to it, so the freedom space is F = C^⊥ and, for
independent ideal constraints, dim F + dim C = 6. A one-degree-of-freedom
stage has dim C = 5 and dim F = 1: five constraints, one usable motion
t_f.

**Two designs (the filer's).** Model each flexure i as a stiffness k_a
along its constraint wrench w_i, and a small parasitic stiffness k_p
against the stage's motion along t_f, since a real flexure is not
perfectly free.

- **Design 1**: five flexures with independent wrenches w_1, …, w_5.
- **Design 2**: the same five, each with a twin along the same constraint
  line, ten flexures in all.

**What is held fixed.** The freedom space. Adding the twins adds no new
constraint direction, so C, and with it F = C^⊥, is unchanged. That is
Hopkins's definition of a redundant constraint (2007, [NOTE-tmpla9de](../notes.d/NOTE-tmpla9de.md)): "A
constraint is non-redundant if when it is added to or removed from a
system, the kinematics or the freedom space of that system changes."

**What differs.**

- **Disturbance error.** A disturbing wrench in the constrained directions
  is resisted by the stiffness along C, which design 2 doubles, so the
  parasitic error it causes halves.
- **Drive force.** Moving the stage by Δ along t_f works against the
  parasitic stiffness, k_p per flexure, so design 1 needs a force of 5k_pΔ
  and design 2 one of 10k_pΔ.

Design 2 is twice as precise against disturbance and needs twice the
drive. Neither dominates: which is better depends on the task's
tolerance and its actuator.

**What the theses say.** Hopkins 2007: "In practice, the flexure system's
stiffness, load capacity, and stability change but the system's
kinematics do not" ([THEORY-tmpmbmox](../theory.d/THEORY-tmpmbmox.md)). Hopkins 2010 ([NOTE-tmpnscd2](../notes.d/NOTE-tmpnscd2.md); [THEORY-tmpeo94c](../theory.d/THEORY-tmpeo94c.md)):
adding redundant constraints "would affect the system's elastomechanics,
dynamics, and load capacity without changing the system DOFs". A: the
same kinematics can be realized by designs "differing in stiffness, load capacity, thermal stability, symmetry, and susceptibility to error."

## What it can show

That equal nominal freedom spaces do not fix precision or effort. A
proposed this as an extension of [CLAIM-345](../claims.d/CLAIM-345.md): "Equal nominal freedom spaces
do not entail equal control effort, precision, disturbance rejection, or
task performance. This should primarily extend existing [CLAIM-345](../claims.d/CLAIM-345.md) rather
than duplicate it." The case illustrates that extension by a static
analogue. [CLAIM-345](../claims.d/CLAIM-345.md)'s own result is dynamic, the least quadratic effort
set by the Gramian; here the freedom space plays the role of the rank
and the stiffness matrix the role of the Gramian. A: "the topology of
permitted transformations and the robustness or cost of actually
performing those transformations are different properties."

## What it cannot show

- **Control effort in [CLAIM-345](../claims.d/CLAIM-345.md)'s sense.** The model is quasi-static and
  computes no effort over a horizon.
- **The costs of redundancy.** A real twin cannot lie exactly on its
  partner's line; misfit under fabrication error loads the stage, a cost
  the 2007 thesis does not treat.
- **Anything organizational.** A's table pairing freedom space,
  constraint space, actuation space and stiffness with organizational
  analogues is, in A's words, "a conceptual comparison, not a claim of
  mathematical equivalence".
