---
status: Answered
title: 'If a map of a representation X of finite support keeps no information about a categorical concept A, how much information about X can it keep, and when does it keep that much?'
version: 1
tags:
- information-theory
- philosophy-of-language
date: '2026-10-21'
line: pragmatic-transport
refines:
- QUESTION-010
summary: >-
  The one-step, information-theoretic part of [QUESTION-010](QUESTION-010.md), split off
  under [ADR-049](../decisions.d/ADR-049.md) and answered by [THEORY-281](../theory.d/THEORY-281.md). The map can keep at most
  H(X|A), and it keeps that much exactly when X is a function of the
  output and A. A deterministic map gets there only when the concept
  groups' distributions are permutations of one another. Chains, and
  relations as against a categorical label, stay with [QUESTION-010](QUESTION-010.md).
answered_by:
- THEORY-281
---
<!-- inactive-ok-file: THEORY-199 — Proposed; named as the partial answer that stays with the parent, not leaned on -->

# QUESTION-tmpn9k0p: If a map of a representation X of finite support keeps no information about a categorical concept A, how much information about X can it keep, and when does it keep that much?

## Answer

At most H(X|A), and no more. This is the part of [QUESTION-010](QUESTION-010.md) that its
note of 2026-10-14 called "the one-step, information-theoretic form for
one categorical concept", split off on 2026-10-21 ([ADR-049](../decisions.d/ADR-049.md)).

[THEORY-281](../theory.d/THEORY-281.md) (Active) answers it, from Chowdhury et al. ([LIT-963](../literature.d/LIT-963.md)), with the
record's re-derivation of 2026-10-20. The map Z is made from X alone,
possibly with independent randomness, so A → X → Z.

- **The cap.** If I(Z;A) = 0, the chain rule gives I(Z;X) = I(Z;X|A) ≤
  H(X|A). Nothing else is assumed.
- **When the cap is reached.** Exactly when H(X|Z,A) = 0, that is, when X
  is a function of Z and A.
- **Deterministic maps.** A deterministic Z = f(X) reaches the cap only
  if the groups' distributions are permutations of one another. Under
  disjoint group supports that condition is also enough.
- **Stochastic maps.** They reach the cap whenever each group's
  distribution is a coarsening of one common law. Under disjoint finite
  supports such a law always exists, at the cost of a larger output
  support.
- **The price.** With disjoint groups, A is a function of X and the cap
  is H(X) − H(A). Erasing the concept costs at least its entropy.

## What it leaves to [QUESTION-010](QUESTION-010.md)

The answer is about one step, an ideal map that knows the distributions,
and a concept given by a categorical label. [QUESTION-010](QUESTION-010.md) asks about a
chain, and about the relations a task family needs. The task form,
I(Z;B) ≤ H(B|A) for any B, is the record's step, not the source's
([THEORY-281](../theory.d/THEORY-281.md), "What this does not say"). With overlapping groups, no map
that reaches the cap is constructed. [THEORY-199](../theory.d/THEORY-199.md), the noise-driven answer of the
same shape, is Proposed and stays with the parent.
