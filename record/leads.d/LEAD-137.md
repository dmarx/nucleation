---
number: 137
status: Open
formerly:
- LEAD-tmpojgj4
title: 'Check on a non-lattice system of coupled agents whether variables chosen for informativeness across a buffer match the gap-isolated block'
version: 1
stage: idea
priority: medium
method:
- formal
- empirical
tags:
- natural-sciences
- individuation
- information-theory
date: '2026-11-19'
line:
- distributed-agency
advances:
- QUESTION-065
- CLAIM-157
summary: >-
  Named in [QUESTION-065](../questions.d/QUESTION-065.md). Filed by the backlog audit of 2026-11-19.
---
<!-- inactive-ok-file: CLAIM-157 — Proposed; cited in the backlog audit of 2026-11-19 -->

# LEAD-137: Check on a non-lattice system of coupled agents whether variables chosen for informativeness across a buffer match the gap-isolated block

## What it would do

In a model of coupled agents, compute the variables most informative
across a buffer and the gap-isolated blocks, and compare them.

Where the record names it:

- [QUESTION-065](../questions.d/QUESTION-065.md): "A result for a system that is not a lattice, such as
  coupled agents. It would show that variables chosen for informativeness
  across a buffer match [CLAIM-157](../claims.d/CLAIM-157.md)'s gap-isolated block. Or a local system
  where they diverge."

## What would count

A match extends the lattice result [QUESTION-065](../questions.d/QUESTION-065.md) starts from; a divergence
in a local system answers it the other way and bounds [CLAIM-157](../claims.d/CLAIM-157.md).

## Note of 2026-11-22: carried out

Run as a delegated lead. A non-lattice coupled-agent system was built (a
linear Gaussian VAR(1) on communities laid on a path, random within) and the
two variables were computed and compared across 960 systems
([CASE-tmpoeu1o](../cases.d/CASE-tmpoeu1o.md)): the variable most informative about the far environment
across a buffer (top canonical correlation) and [CLAIM-157](../claims.d/CLAIM-157.md)'s gap-isolated
block (the leading mode of the region's dynamics). They coincide on a
lattice-like homogeneous boundary (overlap 0.99) and generically diverge off
it (overlap mean 0.74, down to 0.19): the informative variable is a boundary
mode, the block the spread collective mode. The finding is [CLAIM-tmpzdcl1](../claims.d/CLAIM-tmpzdcl1.md),
which answers [QUESTION-065](../questions.d/QUESTION-065.md) the divergence way and bounds [CLAIM-157](../claims.d/CLAIM-157.md). What
remains: the uniqueness part of [QUESTION-065](../questions.d/QUESTION-065.md) is untouched, and the finding
is shown for one model family with one reading of informativeness
(equal-time); a conditional-information or time-lagged reading, or a nonlinear
system, is left open. Status and stage unchanged; the owner marks the lead.
