---
status: Open
title: 'In released language models, do the relational linear properties reported so far lie in the subspaces that enter the logits, with Γ ⊆ N and Γ_q ⊆ M, so that they are properties of the distribution and not of one fitted model?'
version: 1
tags:
- representation-learning
- mathematics
date: '2026-10-19'
line: 'learned-structure'
summary: >-
  The trained-model half of the promotion condition formerly on [THEORY-234](../theory.d/THEORY-234.md),
  moved here unchanged when [THEORY-234](../theory.d/THEORY-234.md) was narrowed and promoted on
  2026-10-19. Theorem 14 of Marconato et al. says a relational linear
  property is shared by every model inducing the same distribution when
  it lies in N with Γ_q ⊆ M. Whether the linearities reported in trained
  models meet that condition has not been measured.
---

# QUESTION-tmpogcb0: In released language models, do the relational linear properties reported so far lie in the subspaces that enter the logits, with Γ ⊆ N and Γ_q ⊆ M, so that they are properties of the distribution and not of one fitted model?

## Why it is a question

[THEORY-234](../theory.d/THEORY-234.md), narrowed on 2026-10-19, holds two things for softmax
next-token predictors on a shared vocabulary. Two models induce the same
distribution exactly when they are extended-linearly equivalent
(Theorem 5). And a relational linear property is shared by all such models
or none when it lies in the subspaces that enter the logits: Γ ⊆ N, with
Γ_q ⊆ M (Theorem 14). Both were re-derived for the promotion audit's
batch 012 ([ADR-047](../decisions.d/ADR-047.md)). Until that date, [THEORY-234](../theory.d/THEORY-234.md)'s promote_when also asked,
as an alternative, for "a measurement in released language models of the
subspaces M, N and Γ_q for relations where linearity has been reported,
showing whether Theorem 14's conditions hold there". That asks whether the
theorem bears on trained models, which [THEORY-234](../theory.d/THEORY-234.md) disclaims. It moved here
unchanged.

It is open because every result in [LIT-950](../literature.d/LIT-950.md) needs exact equality of
distributions, and the paper has no experiments ([NOTE-746](../notes.d/NOTE-746.md)). The record
holds reports of linear relational structure in single trained models.
Those say nothing about the equivalence class.

## What would answer it

A measurement on one or more released models. Estimate F, G, M and N from
the embeddings and pivoted unembeddings, then, for relations where
linearity has been reported, estimate Γ and Γ_q and test Γ ⊆ N and
Γ_q ⊆ M, with a tolerance stated in advance. It would show the reported
properties to be properties of the distribution if the containments
hold. It would show them to be possibly artefacts of one fitted model if
Γ_q has a substantial component in F outside M. Further reports of linear
structure in single models cannot settle it.
