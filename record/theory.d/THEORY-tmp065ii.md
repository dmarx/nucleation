---
status: Active
title: "The single-photon Mach–Zehnder phenomenology with balanced beamsplitters and phases 0 or π, including which-way detection, the bomb tester, delayed choice and the quantum eraser, is reproduced exactly by a local, deterministic classical field model with an epistemic restriction, so that slice of interference forces neither complementarity, nor observer-dependent reality, nor nonlocality"
version: 1
tags:
- quantum-foundations
- contextuality
date: '2026-10-16'
source:
- LIT-019
summary: >-
  Catani, Leifer, Schmid & Spekkens (2021), [LIT-019](../literature.d/LIT-019.md), read in full in
  [NOTE-018](../notes.d/NOTE-018.md). Each mode carries a binary occupation and a binary phase; an
  agent may know at most one of N, Φ, N⊕Φ; the beamsplitter swaps N_L with
  Φ_L⊕Φ_R. The model gives the quantum statistics for the phase shifter,
  which-way detection, the bomb tester (¼), delayed choice and the eraser.
  The existence proof holds for that fragment. The paper's further claim,
  that the model is generalized-noncontextual and so classical by its
  preferred criterion, is asserted, not proved, and unbalanced
  beamsplitters already admit a no-go.
---

<!-- inactive-ok-file: THEORY-010 THEORY-tmpmr94x — Proposed; named in Connections as related accounts, not leaned on -->

# THEORY-tmp065ii: The single-photon Mach–Zehnder phenomenology with balanced beamsplitters and phases 0 or π, including which-way detection, the bomb tester, delayed choice and the quantum eraser, is reproduced exactly by a local, deterministic classical field model with an epistemic restriction, so that slice of interference forces neither complementarity, nor observer-dependent reality, nor nonlocality

## Source

Catani, Leifer, Schmid & Spekkens (2021), [LIT-019](../literature.d/LIT-019.md), read in full in
[NOTE-018](../notes.d/NOTE-018.md), which re-derived the statistics.

## What was actually shown

**Scope ("TRAP" phenomenology, §2.1).** Only the predictions that the
standard arguments for three interpretational claims use: balanced (50-50)
beamsplitters, phases ϕ ∈ {0, π}, a single excitation, the photon entering
at port L. Unbalanced and continuous-phase predictions are excluded
(§5.2.4).

**The model ("toy field theory").** Each mode j has a physical state
(N_j, Φ_j) ∈ Z₂ × Z₂. An agent may know at most one of N, Φ, N⊕Φ and is
maximally ignorant otherwise (p. 12). Dynamics are local and deterministic.
The beamsplitter is the Swap Rule: swap N_L and Φ_L⊕Φ_R, keep Φ_R and
N_L⊕N_R (Eqs. 13, 31). A π phase shift is Φ ↦ Φ⊕1 (Eq. 34). A
nondestructive measurement of N conditions on the outcome and randomizes
that mode's Φ (p. 14). [NOTE-018](../notes.d/NOTE-018.md) confirms that this is [LIT-007](../literature.d/LIT-007.md)'s quadrature
epistricted theory of bits, with modes as systems and every map symplectic
affine over Z₂.

**Results.**
- Phase shifter: ϕ = 0 gives output L with probability 1, ϕ = π gives R
  (Eqs. 26, 39).
- Which-way detector on R: it fires with probability ½, and either way it
  randomizes Φ_R, so the outputs become ½/½ (Eqs. 46–53).
- Bomb tester: a working bomb is certified without exploding with
  probability ¼, carried by a local phase flip of the unoccupied mode
  (§4.1).
- Delayed choice: N and the relative phase both have values throughout; the
  late choice fixes which one can be inferred (§4.2).
- Eraser: measuring one ancilla variable sorts runs by N_R (no interference
  in either subset), the other by the back-action on Φ_R (full interference
  in each); the choice changes nothing about modes L and R (App. A.3,
  Eq. 57).
- The account survives destructive detectors and a removed mirror
  (App. C.3–C.4), and recasts as a cellular automaton with kinematical
  locality (App. C.6).

**The mechanism.** The vacuum in the unused arm is a state of incomplete
knowledge, not of reality. An empty mode still carries a phase bit, which a
detector can flip without the arm being occupied. The flip propagates
locally to the second beamsplitter, where the relative phase decides the
output port. Dependence on later choices is inference, not influence.

**What could have come out otherwise.** Some prediction in the fragment
could have resisted every local classical model. None did. The locality
depends on reading the vacuum epistemically: the paper notes that every
ψ-ontic model needs nonlocality for the eraser, because the eraser is an
EPR-type scenario (App. B, citing Harrigan–Spekkens).

## What this does not say

- **That interference as such is classical.** The paper's title and §5.1.1
  speak of "interference phenomena" and the "only mystery". The body covers
  the balanced, ϕ ∈ {0, π} fragment. The paper itself concedes that
  unbalanced beamsplitters and the functional form of the wave–particle
  duality relation admit no generalized-noncontextual model (its ref. [24]),
  as do Hardy's interferometers.
- **That the model is generalized-noncontextual.** That it is, and so
  classical by the authors' preferred criterion, is asserted "for the same
  reason that other epistemically restricted ... theories do" (p. 28). No
  argument shows that operationally equivalent quantum procedures in the
  fragment receive the same toy distribution ([NOTE-018](../notes.d/NOTE-018.md), C5). The conclusion
  that the three interpretational claims are not forced does not need it.
- **That the fragment's host theory is classical.** The two-mode "qubit
  field theory" is the two-qubit stabilizer subtheory, which already
  contains the Peres–Mermin contextuality proof. The model is classical for
  the fragment, not for the theory the fragment is described in.
- **That it works for fermions.** Aharonov's objection (fn. 42) stands
  unanswered.

## Connections

- The toy bit theory whose kinematics this is, and how it differs from the
  stabilizer theory, is [THEORY-tmp9pyej](THEORY-tmp9pyej.md).
- No-broadcasting is another phenomenon [LIT-007](../literature.d/LIT-007.md) lists as reproduced by
  epistricted theories; within quantum theory it is [THEORY-tmpz1eac](THEORY-tmpz1eac.md).
- Hance et al. ([LIT-090](../literature.d/LIT-090.md)) doubt in an appendix that nonnegative ontological
  models can reproduce the bomb tester. This model does, for the fragment
  ([NOTE-072](../notes.d/NOTE-072.md), C8); the account of what ψ-ontology theorems exclude is
  [THEORY-tmpmr94x](THEORY-tmpmr94x.md).
- [THEORY-010](THEORY-010.md) also finds an epistemically restricted class reproducing what
  was offered as a mark of quantum contextuality. The generalized and
  Kochen–Specker notions of noncontextuality are [THEORY-011](THEORY-011.md) and [THEORY-015](THEORY-015.md).
