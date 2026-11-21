---
status: Proposed
title: "Occupancy of entailment cones is not a measure of learning: it rises when cone boundaries move as well as when representations flow, it rises under collapse, and nested cones make a coarse concept's cone entered no later than a fine one's by construction, so coarse-to-fine learning needs an independent measure of when each level's distinction becomes decodable"
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  A cone family with C_fine ⊆ C_coarse in which a representation can enter
  the fine cone strictly before the coarse one; or a population density
  and moving cone for which dQ/dt differs from the flux term plus the
  boundary term below. Not met by an occupancy measure that is compared
  with held-out decodability at each level, which is the remedy the claim
  names.
tags:
- representation-learning
- learning-theory
- information-theory
date: '2026-11-21'
line:
- learned-structure
bears_on:
- QUESTION-tmpseqwl
- QUESTION-217
grounds:
- LIT-tmp03a0g
- THEORY-846
summary: >-
  A35 §4–§6 of the exchange "Rich Get Richer Power Laws" (2026-11-21),
  answering the owner's U21 ([QUESTION-tmpseqwl](../questions.d/QUESTION-tmpseqwl.md)). By the transport theorem cone
  occupancy rises through boundary motion as well as flow, and collapse
  raises it for any cone covering the collapsed region; and in nested cones
  "measuring the first time it enters each cone will automatically produce
  an apparent coarse-to-fine ordering. That ordering is imposed by the
  geometry." Genuine progressive learning needs an independent measure:
  held-out decodability at each level, or the information chain rule
  across levels. The wording is A's (the other assistant in the exchange
  "Rich Get Richer Power Laws", A35); adopting it is the owner's call.
---
<!-- inactive-ok-file: LIT-tmp03a0g — Deferred works registered from the exchange "Rich Get Richer Power Laws" and not read -->

# CLAIM-tmp6mjfc: Occupancy of entailment cones is not a measure of learning: it rises when cone boundaries move as well as when representations flow, it rises under collapse, and nested cones make a coarse concept's cone entered no later than a fine one's by construction, so coarse-to-fine learning needs an independent measure of when each level's distinction becomes decodable

## The claim

**Two ways to fill a cone.** A35 §4: with population density ρ_t, current j
(∂ρ/∂t = −∇·j) and a moving region C_t whose boundary has normal velocity
v_b, the occupancy Q(t) = ∫_(C_t) ρ_t dV changes as

dQ/dt = −∮_(∂C_t) j·n dA + ∮_(∂C_t) ρ v_b·n dA,

the first term representations flowing in, the second the cone moving over
them. "Both processes can increase cone occupancy, but only the first
necessarily involves movement of representations. And even that movement
need not be semantically beneficial": a model that collapses everything into
one region raises occupancy of any cone covering it while discriminative
information falls. "This is why cone occupancy alone is not a sufficient
learning metric."

**Order by construction.** A35 §5: if C_sparrow ⊆ C_bird, a representation
in the sparrow cone is in the bird cone, so the first entry into the bird cone
is never later than into the sparrow cone. "**That ordering is imposed by the
geometry. It is not evidence that the network learned coarse concepts before
fine concepts.** To establish genuine progressive learning, we need an
independent measure of when the underlying distinctions become available",
such as held-out classification or conditional decodability at each level.
This is [QUESTION-217](../questions.d/QUESTION-217.md)'s distinction exactly: cone first-entry times are a
refinement order by construction and cannot stand in for the acquisition
order, which [QUESTION-217](../questions.d/QUESTION-217.md) defines by a decoder's risk.

**A signature that is not built in.** A35 §6: with Y_coarse a function of
Y_fine, I(Z_t; Y_fine) = I(Z_t; Y_coarse) + I(Z_t; Y_fine | Y_coarse), and
coarse-to-fine learning predicts the first term saturating before the
second rises. But fine structure can sit latent under coarse labels:
representations trained on coarse labels keep finer structure recoverable
by clustering (Yang, Steinhardt and Hu, [LIT-tmp03a0g](../literature.d/LIT-tmp03a0g.md), Deferred: registered,
not read), so both the information present and the information accessible
to restricted decoders should be measured. And a matched null: A35 §9's
enrichment E_t(C) = log[P_t(C)/P₀(C)] against a covariance-matched or
label-shuffled reference, read beside held-out correctness.

## Checked

Both halves are elementary. The transport identity is Reynolds' theorem
with the continuity equation substituted; the first-entry order is set
inclusion: if z ∈ C_fine at time t then z ∈ C_coarse at t, so
τ_coarse ≤ τ_fine for first-entry times.

## Gap

The chain-rule diagnostic is stated for Shannon information, just after A35
argues that usable information is what matters. Usable (V-)information
fails the data-processing inequality ([THEORY-846](../theory.d/THEORY-846.md)), and its chain rule does
not hold in general, so the two-term split has to be stated for Shannon
information and the usable version measured level by level instead.
