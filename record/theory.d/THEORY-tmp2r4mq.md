---
status: 'Proposed'
promote_when: "An exact computation or bound of how the average degree of the S¹ model flows under geometric coarse-graining that accounts for the short-range excess of the coarse-grained link probability over the S¹ form, giving ν(γ, β, r) for general r and confirming the phase boundaries γ = 3 and β = 2 with ν = 2/(γ − 1) − 1 or 2/β − 1 in the limit. It is refuted if the excess between neighbouring supernodes moves either boundary or changes the exponent's form. Further synthetic networks whose degree roughly follows r^ν cannot settle it, since the excess is largest where most links lie."
title: 'Under geometric coarse-graining of the S¹ hidden-metric network model the average degree flows as r^ν, with ν = 2/(γ − 1) − 1 when the degree exponent γ sets it and 2/β − 1 when β does, so the coarse-grained networks run toward a complete graph for γ < 3 or β < 2 and toward a ring otherwise'
version: 1
tags:
- network-science
- complex-systems
date: '2026-10-20'
source:
- LIT-869
summary: >-
  The degree flow that [THEORY-190](THEORY-190.md)'s title carried before the promotion audit (batch 048) narrowed it to the asymptotic closure of the S¹ connection law. García-Pérez, Boguñá and Serrano (2017), [LIT-869](../literature.d/LIT-869.md), derive it to first order by treating the coarse-grained graph as an S¹ model at every separation. The record's exact computation shows that treatment fails between nearby supernodes, so the flow is unproved. Filed under [ADR-047](../decisions.d/ADR-047.md) v4.
extends:
- THEORY-190
answers:
- QUESTION-203
---


# THEORY-tmp2r4mq: Under geometric coarse-graining of the S¹ hidden-metric network model the average degree flows as r^ν, with ν = 2/(γ − 1) − 1 when the degree exponent γ sets it and 2/β − 1 when β does, so the coarse-grained networks run toward a complete graph for γ < 3 or β < 2 and toward a ring otherwise

## Source

García-Pérez, Boguñá and Serrano (2017), [LIT-869](../literature.d/LIT-869.md): the flow
⟨k⟩′ = r^ν⟨k⟩ with ν = 2/(γ − 1) − 1 or 2/β − 1, and the phases it
implies, derived from the renormalized S¹ parameters under a power-law
approximation.

## What is asserted, and by whom

That the average degree of the model obeys this flow, with phase
boundaries at γ = 3 and β = 2: small-world networks that densify toward a
complete graph below them, and sparsening toward a ring above. The
authors derive it; it is a statement about the model.

## What the record holds toward it

- [THEORY-190](THEORY-190.md) (Active): the coarse-grained link probability tends to the
  S¹ form with the stated maps as the supernodes' separation grows large,
  with relative error of order β times block width over separation.
- Against the derivation as given: between neighbouring supernodes the
  union of member links exceeds the S¹ form, by 32–86% in the worked
  example with two-node blocks ([THEORY-190](THEORY-190.md)'s note of 2026-10-20). Most of
  a node's links lie there, so the flow inherits the excess.

## What would confirm or reject it

An exact ν(γ, β, r) that accounts for the excess and keeps the
boundaries confirms it; one that moves them refutes the stated form.
[QUESTION-203](../questions.d/QUESTION-203.md) asks the same thing as a question.
