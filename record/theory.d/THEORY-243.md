---
number: 243
status: Active
formerly:
- THEORY-tmp6lt8x
title: 'In the three-unit identity network x ↦ x(1, 0, 1) ↦ (0, 2, 1)·h, aligning the input with the third unit and aligning it with the direction (h₁ + h₂)/√2, two alignments related by an orthogonal change of basis, pass every interchange intervention on the input equally, so interchange interventions on that variable alone do not fix which internal direction mediates it'
version: 2
history:
- version: 2
  date: '2026-10-20'
  note: >-
    Narrowed and promoted, carrying out the promotion audit's decision for
    THEORY-243 (batch 062, ADR-047 v2). The tie was re-derived and checked
    numerically for every pair of inputs. The title now states what the
    constructed network proves, and no longer generalises to "fixed only
    relative to a chosen decomposition into units". A tie in a trained
    network, or a uniqueness bound, the former promote_when, moves to
    QUESTION-234.
tags:
- causality
- philosophy-of-science
- representation-learning
date: '2026-10-14'
source:
- LIT-961
- LIT-968
summary: >-
  Wu et al. (2024), [LIT-961](../literature.d/LIT-961.md), Appendix A, and Makelov et al. (2023),
  [LIT-968](../literature.d/LIT-968.md), Appendix A.3 and §8, read in [NOTE-809](../notes.d/NOTE-809.md) and [NOTE-782](../notes.d/NOTE-782.md).
  Both rotate the same three-unit identity network. The input aligns with
  h₃ in one basis and with (h₁ + h₂)/√2 in the other, equally well under
  interchange interventions on the input (re-derived 2026-10-20). The
  reply says intervening on further variables separates them; that was not
  checked. Makelov et al. rest their verdict on component boundaries; the
  reply rests its on the interventions performed. Shown exactly for one
  constructed network only; whether trained networks have such ties is
  open (QUESTION-234).
---

# THEORY-243: In the three-unit identity network x ↦ x(1, 0, 1) ↦ (0, 2, 1)·h, aligning the input with the third unit and aligning it with the direction (h₁ + h₂)/√2, two alignments related by an orthogonal change of basis, pass every interchange intervention on the input equally, so interchange interventions on that variable alone do not fix which internal direction mediates it

## Source

Wu et al. (2024), [LIT-961](../literature.d/LIT-961.md), read in [NOTE-809](../notes.d/NOTE-809.md): Appendix A (Eq. 16–17)
and §3.3. Makelov, Lange and Nanda (2023), [LIT-968](../literature.d/LIT-968.md), read in
[NOTE-782](../notes.d/NOTE-782.md): §3.3 with footnote 4, Appendix A.3, and §8 under "The
importance of correct model units". The two papers disagree about almost
everything else; this is the point they share.

## What was actually shown

**The network.** x ↦ h = x(1, 0, 1) ↦ y = (0, 2, 1)·h = x. In the standard
basis the input is copied to h₃ and read from it. Patching h₃ from x′
into x gives x′.

**The rotation.** Makelov et al. (A.3) take the orthonormal basis
d₁ = (e₁ + e₂)/√2, d₂ = (−e₁ + e₂ − 2e₃)/√6, d₃ = (−e₁ + e₂ + e₃)/√3. In
it, d₁ "takes the role that e₃ had before": the input is copied to it
and read from it, and d₂ and d₃ become a disconnected and a dormant
direction. The reply (App. A) uses a different rotation with
(1/√2, 1/√2, 0) as its first row and writes the network as
g(x) = (1/√2)(√2x)_H1 − (1/√2)(√2x)_H2 + (1·x)_H3 = x. Either way,
patching along d₁ from x′ into x also gives x′ (§3.3, checked by script
in [NOTE-809](../notes.d/NOTE-809.md)).

**Who says what.** The reply: f and g "are behaviorally identical yet
structurally different", the input "could be H3 in the original basis
… or H1 in the rotated basis", and "the causal abstraction framework
cannot determine structural equivalence between objects". It adds that
aligning further variables (intervening on H2) would give different
counterfactual behaviour and so separate them. Makelov et al.: in the
toy "the distinction between causally disconnected, dormant and faithful
to the computation directions is artificial", and if activation spaces
may be re-parametrized "by crossing the boundaries between e.g.
attention heads and MLP layers, calling the MLP subspace 'illusory' is
much more tenuous" (§8). Their answer is that components such as heads
and MLP layers do qualitatively different work, so mixing them makes
explanations "less parsimonious and less principled".

What could have come out otherwise: one alignment could have failed some
interchange intervention on the aligned variable. In the toy, none does.

## What this does not say

- **Not that any alignment will do.** The tie holds for the interventions
  performed. Aligning more variables breaks it, as the reply notes.
- **Not shown in a trained model.** The only exact case is the
  constructed network. The reply's claim that complex models will have
  "multiple distinct fully correct abstractions" is a conjecture, and so
  is its link to the complexity of the high-level model.
- **Not that component boundaries are arbitrary.** Makelov et al. give
  reasons to privilege them. The account says only that the privilege
  comes from outside the interventions.
- **Not about constitution.** It concerns which internal variable
  mediates a behaviour, not what makes the behaviour what it is.

## Connections

- **[QUESTION-030](../questions.d/QUESTION-030.md)**, the conceptual half. A218 concedes that causal
  tests do not settle which relations are constitutive. This is the same
  shape one level down: in a network, causal tests within a fixed set of
  interventions do not settle which internal variable mediates, without a
  prior choice of units. The question's own requirement, a theory of the
  act against which empirical results are read, has its analogue here in
  the choice of decomposition. Not marked `answers:`, since it is about
  networks, not communicative acts.
- **[CLAIM-150](../claims.d/CLAIM-150.md).** Supports its premise that interventional success
  underdetermines the ontology, with a proved instance in a simple
  system.
- **[TERM-038](../terms.d/TERM-038.md).** Its "causal" grade is basis-relative in this sense: the
  modal profile under a fixed set of interventions does not single out
  one bearer.
- **[THEORY-282](THEORY-282.md)** is the illusion this tie complicates: whether a
  direction is illusory or faithful depends, in the toy, on the basis.

## Note of 2026-10-20: the tie re-derived

The promotion audit (batch 062) worked the toy through.

**Standard basis.** h = (x, 0, x), with readout weights (0, 2, 1).

- Unit 3 carries x and is read.
- Unit 1 carries x and is not read.
- Unit 2 is read and is always 0.

Patching unit 3 from x′ gives h = (x, 0, x′), so y = x′.

**Rotated basis.** Makelov et al.'s d₁ = (e₁ + e₂)/√2,
d₂ = (−e₁ + e₂ − 2e₃)/√6 and d₃ = (−e₁ + e₂ + e₃)/√3 are orthonormal. Per
unit x, h has coordinates (1/√2, −3/√6, 0) in this basis, and the readout
has (√2, 0, √3). So d₁, d₂ and d₃ play the roles of e₃, e₁ and e₂.

Patching along d₁ sets h ← h + ((h′ − h)·d₁)d₁. This gives
h = (x + (x′ − x)/2, (x′ − x)/2, x), so y = (x′ − x) + x = x′.

Both alignments therefore pass the interchange on the input for every
pair (x, x′). A numerical check on 1000 random pairs agrees to 5 × 10⁻¹⁵.
Patching the carried-but-unread direction, e₁ or d₂, leaves y = x in
either basis.

**What the title dropped.** The title used to say that "which internal
direction is the mediating variable is fixed only relative to a chosen
decomposition into units". That holds in this network. As a general
statement it needs the trained-network tie or the uniqueness bound that
the former promote_when asked for, and that is now [QUESTION-234](../questions.d/QUESTION-234.md).

The reply's remark that aligning a second variable separates the two
alignments was not checked. [CLAIM-150](../claims.d/CLAIM-150.md) cites this account as a proved
instance of interventional underdetermination, and the narrowed title
still supplies that.

