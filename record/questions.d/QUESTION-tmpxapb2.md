---
status: Open
title: 'When a coarse variable''s reduced dynamics carry memory of the eliminated variables, does it admit a finite-dimensional Markovian augmentation with controlled prediction error, and is a level whose history, not its present state, does the predicting still a level?'
version: 1
tags:
- complex-systems
- mathematics
- natural-sciences
date: '2026-10-19'
line: distributed-agency
summary: >-
  A3 and A5 of the exchange of 2026-10-19 on coarse-to-fine processes,
  A5's candidate Q3. The Mori–Zwanzig decomposition writes any projected
  dynamics as a Markovian term, a memory term and noise. The record holds
  no reading of it. Its criteria of closure ([THEORY-257](../theory.d/THEORY-257.md)) condition on the
  coarse variable's own history, so memory is not by itself a failure of
  them, and [CLAIM-327](../claims.d/CLAIM-327.md) already locates a collective in a variable members
  read from the past.
---
<!-- inactive-ok-file: LIT-tmpai9kc LIT-tmpki8cm LIT-tmple6xy LIT-tmpvihtb — Deferred; works registered unread, cited as open, nothing here rests on them -->
<!-- inactive-ok-file: CLAIM-157 CLAIM-327 THEORY-257 — Proposed; open claims and readings named for context, nothing here rests on their being settled -->
# QUESTION-tmpxapb2: When a coarse variable's reduced dynamics carry memory of the eliminated variables, does it admit a finite-dimensional Markovian augmentation with controlled prediction error, and is a level whose history, not its present state, does the predicting still a level?

## Why it is a question

Eliminating variables does not remove their influence. It returns as
memory and noise. A5's example: with ẋ = −ax + by and ẏ = cx − dy,
keeping only x gives

ẋ(t) = −a x(t) + bc ∫₀ᵗ e^{−d(t−s)} x(s) ds + b e^{−dt} y(0),

with memory kernel K(t) = bc e^{−dt}. When d is large the memory fades and
a Markovian model of x may serve. When d is small it persists. A5: "it
would be premature to interpret persistent memory as evidence that the
system has no meaningful macroscopic organization. It might instead mean
that **the correct macrostate includes history or an additional internal
memory coordinate**."

A3 gave the general form, Ż = F(Z) + ∫ K(t − s, Z_s) ds + η, and a caution
the record keeps: the split into drift, memory and noise depends on the
projection, so "an arbitrary norm of the memory kernel is not, by itself, a
representation-invariant measure of emergence."

## What the record holds

- [THEORY-257](../theory.d/THEORY-257.md): dynamical independence conditions on Y's own history. A5:
  "non-Markovianity of Z_t is not automatically a violation of its
  dynamical-independence criterion." What it forbids is information from
  the micro history beyond that.
- [CLAIM-327](../claims.d/CLAIM-327.md): a reputation or standing is an endogenous variable because
  members read the accumulated past and act on it.
- [CLAIM-157](../claims.d/CLAIM-157.md) and [CASE-043](../cases.d/CASE-043.md): a block test on synchronous dynamics misses a
  coupling that runs through storage, such as Otto's notebook, and needs a
  time-lagged version that is not built.
- No reading of Mori–Zwanzig. Chorin, Hald and Kupferman ([LIT-tmpai9kc](../literature.d/LIT-tmpai9kc.md),
  [LIT-tmple6xy](../literature.d/LIT-tmple6xy.md)) and Parish and Duraisamy ([LIT-tmpvihtb](../literature.d/LIT-tmpvihtb.md)) are registered
  unread. Germano ([LIT-tmpki8cm](../literature.d/LIT-tmpki8cm.md)) supplies a related distinction: a
  hierarchy of filtered descriptions can exist with no closed equation at
  any level.

## What would count as an answer

For a stated class, conditions under which the reduced process has a
finite-dimensional Markovian augmentation (the coarse variable plus k
memory coordinates) whose prediction error is bounded, with k and the error
in terms of the spectrum of the eliminated dynamics; and a ruling on
whether the record's level criteria should be applied to the augmented
state or to the instantaneous one. A5's own limit: this is "a candidate
theoretical extension, not a result already established for social or
cognitive systems."
