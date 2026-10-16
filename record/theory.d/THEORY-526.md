---
number: 526
status: Active
formerly:
- THEORY-tmpgg88t
title: "The Čech cohomology obstruction of a support section is a sound but incomplete witness of contextuality: it vanishes exactly when the section lies in a compatible family of integer combinations of support sections, so it is non-zero on every section of every All-vs-Nothing model, over any coefficient ring, on a connected cover, yet it misses the Hardy model entirely, part of a strongly contextual Kochen–Specker cover, and every section of a strongly contextual model on the fully symmetric (2,2,4) Bell cover"
version: 1
tags:
- contextuality
- quantum-foundations
- mathematics
date: '2026-10-16'
source:
- LIT-277
- LIT-278
- LIT-279
extends:
- THEORY-012
summary: >-
  Abramsky, Mansfield & Barbosa (2011), [LIT-277](../literature.d/LIT-277.md) ([NOTE-250](../notes.d/NOTE-250.md)); Abramsky,
  Barbosa, Kishida, Lal & Mansfield (2015), [LIT-278](../literature.d/LIT-278.md) ([NOTE-251](../notes.d/NOTE-251.md)); Carù
  (2017), [LIT-279](../literature.d/LIT-279.md) ([NOTE-252](../notes.d/NOTE-252.md)). The criterion (Prop 4.2 / Prop 16) and the
  All-vs-Nothing theorem (Thm 21) are proved; the three failures are
  explicit models, which the readers re-computed exactly over ℤ and ℤ/2.
  Two steps are the readers': that the §8 cover and the (2,2,4) model
  admit no All-vs-Nothing argument over any ring, by Thm 21 read
  contrapositively. The witness is possibilistic, so it cannot grade
  anything below strong contextuality.
extended_by:
- THEORY-524
---

<!-- inactive-ok-file: THEORY-014 — Proposed; named for an analogy NOTE-251 draws, nothing here rests on it -->

# THEORY-526: The Čech cohomology obstruction of a support section is a sound but incomplete witness of contextuality: it vanishes exactly when the section lies in a compatible family of integer combinations of support sections, so it is non-zero on every section of every All-vs-Nothing model, over any coefficient ring, on a connected cover, yet it misses the Hardy model entirely, part of a strongly contextual Kochen–Specker cover, and every section of a strongly contextual model on the fully symmetric (2,2,4) Bell cover

## Source

Abramsky, Mansfield & Barbosa (2011), [LIT-277](../literature.d/LIT-277.md), read in full in [NOTE-250](../notes.d/NOTE-250.md),
which re-ran every example as exact linear algebra. Abramsky, Barbosa,
Kishida, Lal & Mansfield (2015), [LIT-278](../literature.d/LIT-278.md), read in full in [NOTE-251](../notes.d/NOTE-251.md), both
arXiv versions (v2 is the published text; Prop 16's proof survives only
in v1). Carù (2017), [LIT-279](../literature.d/LIT-279.md), read in [NOTE-252](../notes.d/NOTE-252.md), with the counterexample
verified exhaustively.

## What was actually shown

**The obstruction ([LIT-277](../literature.d/LIT-277.md), §4).** Free the support presheaf of an
empirical model over ℤ. For a section s₁ of context C₁, choose
no-signalling lifts sᵢ that agree with it on each overlap; δ⁰(s₁, …, sₙ)
vanishes on C₁, and its class γ(s₁) in the cohomology of the kernel
presheaf relative to C₁ need not vanish, because (s₁, …, sₙ) is not a
relative cochain. [LIT-278](../literature.d/LIT-278.md) recovers the same class as the snake lemma's
connecting map, which [NOTE-251](../notes.d/NOTE-251.md) checked agrees with the concrete one.

**The criterion ([LIT-277](../literature.d/LIT-277.md) Prop 4.2; [LIT-278](../literature.d/LIT-278.md) Prop 16).** γ(s₁) = 0 iff s₁
lies in a compatible family of formal ℤ-linear combinations of support
sections. So γ(s) ≠ 0 for some s witnesses logical contextuality, and
γ ≠ 0 on every section witnesses strong contextuality (Prop 4.3, Prop
19). Neither is necessary.

**Where it is complete ([LIT-278](../literature.d/LIT-278.md), Thm 21).** Call a model All-vs-Nothing
over a commutative ring R when the R-linear equations every context's
support satisfies have no global solution. Then AvN_R(S) ⇒ SC(Aff S) ⇒
CSC_R(S) ⇒ CSC_ℤ(S) ⇒ SC(S). The step that matters: a compatible family
through 1·s₀ has coefficient sum 1 in every context, so the counit
evaluates it to a global section of the affine closure, which an AvN
argument forbids. The proof assumes a connected cover, which the
theorem does not state. Every state stabilised by an AvN triple of
n-qubit Paulis gives such a model (Thm 4). GHZ, Peres–Mermin, the PR box
and the triangle are AvN over ℤ₂, which is why [LIT-277](../literature.d/LIT-277.md) found γ ≠ 0 on
all their sections.

**Where it fails.**

- *Hardy ([LIT-277](../literature.d/LIT-277.md) §5).* γ = 0 on all 13 support sections, over ℤ and ℤ/2
  ([NOTE-250](../notes.d/NOTE-250.md)'s count; the paper shows one). Every Hardy context's affine
  hull is the whole event set, so no AvN argument exists over any ring.
- *A Kochen–Specker cover ([LIT-277](../literature.d/LIT-277.md) §8).* {A,B,C},{B,D,E},{C,D,E},{A,D,F},
  {A,E,G} is strongly contextual, yet γ = 0 on 9 of its 15 sections.
- *The (2,2,4) Bell cover ([LIT-279](../literature.d/LIT-279.md) §4).* A strongly contextual model,
  supported on b₁ = a₁, b₂ = a₂ + 1 mod 4 and two "staircase" contexts, has
  γ = 0 on all 22 sections over ℤ and ℤ/2, and over ℚ. The cover is
  connected, its symmetries act transitively, and no measurement is
  private. That refutes [LIT-277](../literature.d/LIT-277.md)'s Conjecture 8.1 for symmetry of the
  cover, and its diagnosis that private measurements are the cause.

The failures share one mechanism: signed combinations such as [10] −
[11] + [01] close a loop inside a context that no actual section closes.
Cohomology over R sees a model only up to its affine closure.

What could have come out otherwise: symmetry of the cover could have
forced completeness, as [LIT-277](../literature.d/LIT-277.md) conjectured. It does not.

## What this does not say

- **That cohomology detects only All-vs-Nothing models.** Theorem 21 runs
  one way. Whether every cohomologically strongly contextual model is
  AvN over some ring is open ([NOTE-251](../notes.d/NOTE-251.md)).
- **That all quantum strong contextuality is All-vs-Nothing.** [LIT-278](../literature.d/LIT-278.md)
  asserts it (p. 17) with no citation or survey.
- **Anything probabilistic.** Only supports are used, so the witness is
  blind to Bell–CHSH-type contextuality with full support and cannot
  grade models below contextual fraction 1.
- **That higher-degree obstructions help.** For no-signalling models
  every level above the first is empty ([LIT-279](../literature.d/LIT-279.md), Prop 5.6).
- **That strong contextuality is equivalent to every γ_C being
  injective.** [LIT-279](../literature.d/LIT-279.md)'s Prop 6.1 is false in that direction; the PR box
  refutes it ([NOTE-252](../notes.d/NOTE-252.md)).
- **That Liar cycles are contextual models in general.** The length-4
  cycle is the PR box at the level of supports, and [NOTE-251](../notes.d/NOTE-251.md) derives
  cohomological strong contextuality for every length N ≥ 3; the encoding
  fails at N = 1 and 2, the classic Liar included.

## Connections

- [THEORY-012](THEORY-012.md) holds the exact criterion, a global section of the support
  or of the distributions. This account is about a computable relaxation
  of it, and refines the cohomology line [THEORY-012](THEORY-012.md) carries in its "does
  not say".
- [THEORY-524](THEORY-524.md) carries it further: on cyclic covers an iterated joint
  model makes the same obstruction exact.
- [THEORY-014](THEORY-014.md)'s point that signed global sections always exist over ℝ has
  a discrete analogue here, noted in [NOTE-251](../notes.d/NOTE-251.md) as an inference: the
  obstruction fails exactly where affine combinations can glue.
