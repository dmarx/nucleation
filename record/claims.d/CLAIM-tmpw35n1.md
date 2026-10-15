---
status: Active
title: 'Where source and rendering are experiments about one common situation, a rendering that depends on the situation other than through the source is not a garbling of it and can be incomparable with it in Blackwell''s order: with Z uniform on {1, 2, 3}, a source that tells whether Z = 1 and a rendering that tells whether Z = 3 each have the lower 0–1 risk on one of the problems of saying whether Z = 1 and whether Z = 3, so neither dominates'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the worked case: a Markov kernel G with P(V | Z) = G P(U | Z)
  for these U and V, or a computation showing that one of U and V has Bayes
  risk no greater than the other's on every bounded decision problem about Z
  under every prior.
tags:
- mathematical-statistics
- information-theory
- translation
date: '2026-10-15'
line: pragmatic-transport
grounds:
- THEORY-156
summary: >-
  Split from [CLAIM-258](CLAIM-258.md) under [ADR-043](../decisions.d/ADR-043.md): the worked case that objection uses,
  stated on its own so that its warrant can be. Over a common situation Z
  uniform on three values, U reports whether Z = 1 and V whether Z = 3. V
  is not a garbling of U, since given U = 0 it still varies with Z, and the
  risks on "say whether Z = 3" (0 from V, 1/3 from U) and "say whether
  Z = 1" (the reverse) show neither experiment dominates. It is an
  existence result by construction. It does not say this is the normal
  translation case, which is [CLAIM-258](CLAIM-258.md)'s reading and is interpretive.
supports:
- CLAIM-258
---
<!-- inactive-ok-file: THEORY-156 — Proposed; cited for the definition of Blackwell's order, which the construction only applies -->
<!-- inactive-ok-file: CLAIM-258 CLAIM-212 CLAIM-091 — Proposed; the objection this case was split from, the reply that reads it as a report case, and the compensation claim the objection applies it through, cited as open -->
<!-- inactive-ok-file: LIT-778 — Deferred; Torgersen, unread here, named as where the quantitative question lies and not leaned on -->

# CLAIM-tmpw35n1: Where source and rendering are experiments about one common situation, a rendering that depends on the situation other than through the source is not a garbling of it and can be incomparable with it in Blackwell's order: with Z uniform on {1, 2, 3}, a source that tells whether Z = 1 and a rendering that tells whether Z = 3 each have the lower 0–1 risk on one of the problems of saying whether Z = 1 and whether Z = 3, so neither dominates

## The claim

This is the worked case of [CLAIM-258](CLAIM-258.md), stated on its own. Blackwell's
experiments share their parameter. [THEORY-156](../theory.d/THEORY-156.md): "An experiment is an n-tuple
of probability measures on a common space, one per state", and α is
sufficient for β "if there is a stochastic transformation T with T m_i =
M_i for every state i". A garbling needs the rendering to depend on Z only
through the source text, V ⫫ Z | U.

Let Z be uniform on three situations, 1, 2 and 3.

- The source text tells its reader only whether Z = 1: U = 1 if Z = 1, and
  U = 0 otherwise.
- A translator who knows the setting tells the target reader only whether
  Z = 3: V = 1 if Z = 3, and V = 0 otherwise.

V is not a garbling of U, because given U = 0 it still varies with Z. And
neither experiment is at least as informative as the other. Take the
problem "say whether Z = 3", with loss 1 for a wrong answer. From V the risk
is 0. From U it is 1/3: on U = 1 the answer is certainly no, and on U = 0,
which has probability 2/3, the two remaining situations are equally likely,
so any answer is wrong half the time. For "say whether Z = 1" the risks are
reversed. If either experiment dominated the other, it would do at least as
well in every problem under every prior. So U and V are incomparable in
Blackwell's order.

The case needs nothing but the definitions and two risk computations, so
it is demonstrated. [CLAIM-212](CLAIM-212.md) reads the same case as a report case and
reaches the same verdict.

## What it does not say

- It does not say that the line's central translations are like this, or
  that Blackwell's order fails to reach them. That is [CLAIM-258](CLAIM-258.md)'s reading,
  which rests on this case and on [CLAIM-091](CLAIM-091.md)'s compensation, and it is
  interpretive.
- It does not say that non-garblings are typically incomparable with their
  source. The case shows that one can be.
- It does not say how far apart U and V are. That is a question for Le
  Cam's deficiency, which [THEORY-156](../theory.d/THEORY-156.md) names and the record has not read
  (Torgersen, [LIT-778](../literature.d/LIT-778.md)).
- It does not say the rendering is worse. It is better for one decision and
  worse for another.
