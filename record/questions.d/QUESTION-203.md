---
number: 203
status: Open
formerly:
- QUESTION-tmpenqmz
title: 'How does the average degree of the S¹ hidden-metric model flow under geometric coarse-graining when the closure fails between nearby supernodes, and does an exact ν(γ, β, r) confirm or move the phase boundaries γ = 3 and β = 2?'
version: 1
tags:
- network-science
- complex-systems
date: '2026-10-20'
line: 'formal-apparatus'
summary: >-
  The degree-flow part of the promotion condition formerly on [THEORY-190](../theory.d/THEORY-190.md).
  [THEORY-190](../theory.d/THEORY-190.md) was promoted on 2026-10-20 ([ADR-047](../decisions.d/ADR-047.md) v2) narrowed to what was
  proved: the coarse-grained link probability tends to the S¹ form as the
  supernodes' separation grows, and exceeds it between nearby supernodes.
  The source's flow of ⟨k⟩ as r^ν, and its phase boundaries, rest on the
  closure holding at every separation and on a power-law approximation.
---

# QUESTION-203: How does the average degree of the S¹ hidden-metric model flow under geometric coarse-graining when the closure fails between nearby supernodes, and does an exact ν(γ, β, r) confirm or move the phase boundaries γ = 3 and β = 2?

## Why it is a question

García-Pérez, Boguñá and Serrano derive ⟨k⟩′ = r^ν⟨k⟩ with ν = 2/(γ−1) − 1
or 2/β − 1, so that the flow runs to a complete graph if γ < 3 or β < 2 and
to a ring otherwise. That derivation treats the coarse-grained graph as an
S¹ model with renormalized parameters at every separation. [THEORY-190](../theory.d/THEORY-190.md)
shows the closure holds only asymptotically: between neighbouring
supernodes, where most links lie, the union of member links exceeds the
S¹ form, by up to 86% in a worked example. Whether the flow and its phase
boundaries survive that excess, the record cannot say. Until 2026-10-20
this was part of [THEORY-190](../theory.d/THEORY-190.md)'s promote_when.

## What would answer it

- An exact ν(γ, β, r), or a bound on it, for the coarse-grained graph
  itself rather than for its first-order S¹ approximation, confirming or
  correcting the boundaries γ = 3 and β = 2.
- An exact computation of ⟨k⟩′ for small r on the actual union of member
  links, compared with the source's series for r = 2.

What would not answer it: more real networks whose layers collapse, or
the source's first-order flow again. The question is about what the model
does under the transformation.
