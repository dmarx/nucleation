---
number: 65
status: Open
formerly:
- QUESTION-tmprg4fj
title: 'Can the target that a sufficiency-based boundary is relative to be supplied by the system''s own locality, as informativeness about its far environment across a buffer, so that the coarse variables kept no longer depend on the analyst, and is the partition that wins for a given target unique?'
version: 1
tags:
- natural-sciences
- information-theory
- mathematics
date: '2026-10-12'
line: 'distributed-agency'
refines:
- QUESTION-035
summary: >-
  Filed in the fourth synthesis pass to give readings no question asked
  for a place in the argument. It bears on [CLAIM-152](../claims.d/CLAIM-152.md), [CLAIM-154](../claims.d/CLAIM-154.md),
  [CLAIM-157](../claims.d/CLAIM-157.md), [CLAIM-164](../claims.d/CLAIM-164.md) and [QUESTION-035](QUESTION-035.md). [THEORY-198](../theory.d/THEORY-198.md), [THEORY-205](../theory.d/THEORY-205.md) and
  [THEORY-157](../theory.d/THEORY-157.md) answer it in part; the body gives each one's limit.
---
<!-- inactive-ok-file: THEORY-257 — Proposed; a reading listed with its limits, an answer in part -->

# QUESTION-065: Can the target that a sufficiency-based boundary is relative to be supplied by the system's own locality, as informativeness about its far environment across a buffer, so that the coarse variables kept no longer depend on the analyst, and is the partition that wins for a given target unique?

## The question

[CLAIM-152](../claims.d/CLAIM-152.md) makes every individuation by sufficiency relative to a target. [QUESTION-035](QUESTION-035.md) asks for a verdict "relative to a stated target". Two things are left open. First, whether some target is fixed by the system rather than chosen by the analyst. In a local system, that target is what one region tells about regions beyond a buffer. Second, whether a given target yields one winning partition or several.

## Why the record needs it

The mechanism is locality. What crosses a buffer is carried by the leading modes of the transfer between regions, which are set by a spectral gap. That is the object [CLAIM-164](../claims.d/CLAIM-164.md) names and [CLAIM-157](../claims.d/CLAIM-157.md) prices. If locality fixes the target, [CLAIM-157](../claims.d/CLAIM-157.md)'s verdicts are less arbitrary than [CLAIM-152](../claims.d/CLAIM-152.md) allows. If not, [CLAIM-152](../claims.d/CLAIM-152.md) stands unqualified. A boundary test that returns several equally good partitions cannot give [QUESTION-035](QUESTION-035.md) its verdict.

## What the record holds

- [THEORY-198](../theory.d/THEORY-198.md): a coarse-graining that keeps all information about the far environment "makes the coarse measure factorize across the block, so the renormalized Hamiltonian gains no range". The coarse description stays local. Limit: actual maximizers fall short of full capture, and the partition is fixed in advance.
- [THEORY-205](../theory.d/THEORY-205.md): the first feature of the information bottleneck is "the boundary weak value of the leading transfer-matrix eigenvector". Under degeneracy it is a subspace, as [CLAIM-164](../claims.d/CLAIM-164.md) says. Limit: shown for slabs of a cylinder only.
- [THEORY-157](../theory.d/THEORY-157.md): given a target, a complete sufficient statistic is minimal (Bahadur), and it is independent of what is ancillary to that target (Basu). That bears on uniqueness. Limit: it needs completeness and says nothing about locality.
- [THEORY-257](../theory.d/THEORY-257.md) ([LIT-979](../literature.d/LIT-979.md), [NOTE-791](../notes.d/NOTE-791.md)): dynamical independence, zero information flow from the micro history into a coarse-graining given its own history, fixes emergent variables by the dynamics. The target is the coarse variable's own future, so no outside query is chosen. It answers both parts in part. Limits: the system/environment boundary is assumed, the scale is chosen, and the optima are not unique (the cost is multimodal, and exact independence is generically absent). Its criterion is closure, not informativeness about a far environment across a buffer, so it is not this question's target.

## What would answer it

A result for a system that is not a lattice, such as coupled agents. It would show that variables chosen for informativeness across a buffer match [CLAIM-157](../claims.d/CLAIM-157.md)'s gap-isolated block. Or a local system where they diverge.

## Note of 2026-11-22: the non-lattice case, run

[LEAD-137](../leads.d/LEAD-137.md) built the coupled-agent system this question calls for — a
linear Gaussian VAR(1) on communities laid on a path, random within, so not a
lattice — and compared the two variables ([CASE-375](../cases.d/CASE-375.md), [CLAIM-970](../claims.d/CLAIM-970.md)).
The answer is the second branch, divergence, for the generic case. The
variable most informative about the far environment across a buffer and
[CLAIM-157](../claims.d/CLAIM-157.md)'s gap-isolated block coincide on a lattice-like homogeneous
boundary (overlap 0.99) but generically diverge off it (overlap mean 0.74,
down to 0.19 under symmetric coupling): the informative variable is a boundary
mode, the block the spread collective mode, and they agree only under a
homogeneous boundary or one-way drive. So locality does not on its own supply
the block criterion's target in a generic local system; the match is a
property of the lattice's homogeneous boundary. The first part of the question
is answered the negative way for that case; the uniqueness part is untouched.
