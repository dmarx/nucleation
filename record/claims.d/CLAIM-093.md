---
number: 93
status: Active
formerly:
- CLAIM-tmprdod5
title: 'Not every invariance of a stochastic or communicative process implies a Noether conservation law: the symmetry principle can be borrowed, a conservation analogue has to be derived'
version: 1
role: disclaimed
warrant: demonstrated
tags:
- mathematics
- philosophy-of-language
date: '2026-10-08'
line:
- pragmatic-transport
- formal-apparatus
works:
- what-survives-translation
complements:
- CLAIM-107
summary: >-
  A105, limiting the owner's U37 appeal to Noether in the same reply
  that conceded the rest. The manuscript §4 and §11: Noether-type
  results give "conservation criteria for particular stochastic
  processes, not a universal conservation law of meaning".
grounds:
- THEORY-211
---
<!-- inactive-ok-file: THEORY-211 — Proposed; the learning-dynamics instance filed on 2026-10-13, open -->

# CLAIM-093: Not every invariance of a stochastic or communicative process implies a Noether conservation law: the symmetry principle can be borrowed, a conservation analogue has to be derived

## The claim

A105: "**not every invariance of an arbitrary stochastic or communicative
process implies a Noether conservation law**. Noether's theorem requires an
appropriate variational structure and continuous symmetry. Our translation
kernels do not automatically have either. What we can borrow immediately is the
symmetry principle. What we would have to *derive* is an appropriate analogue of
conservation." The derivation it found is Baez and Fong's theorem for Markov
processes, "a genuine conservation-theoretic connection for the continuous-time
Markov special case" ([CLAIM-107](CLAIM-107.md), qualified by [CLAIM-094](CLAIM-094.md)).

Manuscript §4: "Noether's first theorem relates suitable continuous variational
symmetries to conserved currents; its hypotheses do not hold automatically in
communicative systems." §11: "Noether-type results supply conservation criteria
for particular stochastic processes, not a universal conservation law of
meaning."

## Note of 2026-10-13: an instance in learning dynamics

Two readings give this claim a worked instance outside communication.

- **A derived law, with a condition.** In Neural Mechanics ([LIT-1012](../literature.d/LIT-1012.md)), a
  differentiable symmetry of a network's loss gives a conserved quantity
  under gradient flow only when a further condition holds,
  ⟨θ, [∂_α ∂_θ ψ]g⟩ = 0 (Theorem 1). The conservation law is derived for
  the dynamics; it does not come with the invariance alone.
- **A symmetry with no conservation law.** Under SGD, a stochastic process
  whose minibatch gradients share the symmetry exactly, the same quantity
  is not conserved. For a rescaling symmetry, minibatch noise drives it
  toward the point where the layers' gradient noise balances (Ziyin et
  al., [LIT-1013](../literature.d/LIT-1013.md); [THEORY-211](../theory.d/THEORY-211.md)).

[THEORY-211](../theory.d/THEORY-211.md) now grounds this claim. The instance supports the claim's
point that a symmetry principle can be borrowed but its conservation
analogue has to be derived, and shows the derivation can come out
negative.
