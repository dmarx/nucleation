---
status: Proposed
title: 'The mathematics of waves and distributed modes, which covers harmonic and spectral decomposition, multiscale analysis, scattering and response operators, interference, mode coupling, localization and reconstruction, applies to how learning systems acquire, execute and compose computations, and earns its place where a description in independently justified modes and their couplings predicts a learned network''s responses to unseen queries, interventions, training and merging better than feature-, circuit- or parameter-level accounts fitted with the same information'
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  On matched, prospective tests, such as circuit emergence across
  checkpoints, recoverability of controlled associations after
  intervention, and merge compatibility, mode-and-coupling descriptions
  predict no better than static feature, circuit-attribution, gating or
  parameter-overlap accounts given the same data; or the modes that
  appear to carry the prediction are artefacts of the chosen basis,
  disappearing under a change of coordinates, dictionary or permutation of
  hidden units.
tags:
- learning-theory
- representation-learning
- mathematics
- anthology-candidate
date: '2026-11-15'
line:
- learned-structure
- formal-apparatus
uses:
- TERM-118
complements:
- CLAIM-407
bears_on:
- QUESTION-275
- QUESTION-217
summary: >-
  The owner's hypothesis, from the continuation of the exchange "Explain
  String Theory" (2026-11-15): "what I think ties all of this together
  isn't optical phenomena specifically, so much as wave phenomena. there's
  already a rich connection between deep learning dynamics and harmonic
  analysis. my hypothesis here is that tools for describing wave phenomena
  are likely applicable to understanding learning and
  cognition/computation". The criterion for when it holds, and the
  defeaters, are A's operationalization (A14, A23, A24), adopted here as
  the claim's test. The record's strongest held case is [THEORY-022](../theory.d/THEORY-022.md), where
  a network computes with Fourier characters. A merging method's
  "frequency" that is not one (FREE-Merging, read for this filing) shows
  what the claim must exclude. The hypothesis is the owner's; the wording
  and its test are A's, and adopting them is the owner's call.
---
<!-- inactive-ok-file: THEORY-022 THEORY-tmp3lla6 THEORY-tmpomhf0 CLAIM-tmp7jyur CASE-tmp71zhd CASE-tmp9201a — Proposed or new; the held case and the entries filed with this one -->

# CLAIM-tmpumro8: The mathematics of waves and distributed modes, which covers harmonic and spectral decomposition, multiscale analysis, scattering and response operators, interference, mode coupling, localization and reconstruction, applies to how learning systems acquire, execute and compose computations, and earns its place where a description in independently justified modes and their couplings predicts a learned network's responses to unseen queries, interventions, training and merging better than feature-, circuit- or parameter-level accounts fitted with the same information

## The claim

The owner's: tools for describing wave phenomena are likely applicable to
learning and computation. The claim is not that networks are waves, nor
that facts are stored as holograms. A put it this way: "Instead of asking
whether learning and cognition are literally wave phenomena, ask whether
the emergence of computational organization can be understood through the
same mathematical structures that govern the organization and interaction
of modes in wave-bearing systems."

A splits it into three conjectures, about learning, inference and
individuation:

1. **Modal formation through learning.** Training reorganizes the
   operators and subspaces that fix which distinctions are available. Under
   squared-error gradient flow the residual obeys ė = −K_τ e, and in a
   moving eigenbasis e = U_τ a it becomes ȧ = −Λ_τ a − Ω_τ a with
   Ω_τ = U_τᵀU̇_τ skew. The second term is a reorganization of the modes,
   not a relaxation along them (noted on [QUESTION-217](../questions.d/QUESTION-217.md)).
2. **Modal interaction during computation.** A circuit can be a
   reproducible, causally consequential pattern of coupling among modes of
   the layer transfer operators, M_ℓ(x) = U_{ℓ+1}ᵀ J_ℓ(x) U_ℓ, which inputs
   select (noted on [QUESTION-275](../questions.d/QUESTION-275.md)).
3. **Individuation through interaction structure.** A computational
   organization may be better identified by its stable couplings and
   intervention responses than by a fixed set of components, relative to a
   declared task, representation and intervention family.

## What it needs, and what defeats it

A spectral decomposition alone is not evidence: almost any operator has
one. The modes must be justified independently, by a task symmetry (the
Fourier characters of ℤ/p in [THEORY-022](../theory.d/THEORY-022.md)), an invariant subspace, or a
validated functional role. FREE-Merging ([THEORY-tmp3lla6](../theory.d/THEORY-tmp3lla6.md)) shows the
failure the claim must exclude. Its "frequencies" run over the arbitrary
order of a weight matrix's rows and columns. A permutation of hidden units
changes the function not at all and changes the spectrum.

The test is prospective. A's experiments are filed as [CASE-tmp71zhd](../cases.d/CASE-tmp71zhd.md) (a
Fourier circuit's birth across training) and [CASE-tmp9201a](../cases.d/CASE-tmp9201a.md) (recoverability
of controlled associations under intervention, compute and merging).

## Which sense of "wave"

The readings filed with this claim use "wave" in three senses:
- **Travelling:** cortical waves that propagate (Muller et al.).
- **Standing:** spatially damped standing responses (Gepshtein et al.).
- **Spectral:** modes of an operator (the merging and Fourier readings).

Only the spectral sense is at issue here. The physical senses also warn
against importing linear superposition: colliding cortical waves sum about
30% below the sum of each alone ([THEORY-tmpomhf0](../theory.d/THEORY-tmpomhf0.md)). What counts as a
justified mode is sharpened by [CLAIM-tmp7jyur](CLAIM-tmp7jyur.md), which requires invariance
under the network's function-preserving symmetries. This section is the
assistant's (Claude, in this session).

## What it does not say

- **That learning or cognition obeys a wave equation.** Gradient flow is
  dissipative relaxation, not oscillation.
- **That a mode is a unit of cognition.** Whether a mode-based description
  individuates anything is conjecture 3, still open.
- **That it extends to cognition generally.** A: "A model that describes
  cognition only in terms of oscillations or resonances would risk
  discarding the semantic and causal distinctions that make it cognition in
  the first place."
