---
number: 138
status: Open
formerly:
- QUESTION-tmp3bfqc
title: 'When does the truncated n × n matrix of a functional map stay nearly orthogonal and nearly block-diagonal by eigenspace under a near-isometry, and how does the bound depend on the spectral gap at n?'
version: 1
tags:
- mathematics
date: '2026-10-19'
line: formal-apparatus
summary: >-
  The truncation clause of [THEORY-297](../theory.d/THEORY-297.md)'s former promote_when. [THEORY-297](../theory.d/THEORY-297.md) is
  Active for bijections, with orthogonality for volume-preserving maps and
  eigenspace preservation for exact isometries. For an exact isometry the
  truncated block is orthogonal when n ends at a spectral gap. What is open
  is the near-isometric case, which [LIT-993](../literature.d/LIT-993.md) cites to Kato and does not show.
---

# QUESTION-138: When does the truncated n × n matrix of a functional map stay nearly orthogonal and nearly block-diagonal by eigenspace under a near-isometry, and how does the bound depend on the spectral gap at n?

## Why it is a question

[THEORY-297](../theory.d/THEORY-297.md) holds Ovsjanikov et al.'s structural results ([LIT-993](../literature.d/LIT-993.md), read in
[NOTE-822](../notes.d/NOTE-822.md)) for a bijection T between shapes. At the owner's direction, from
the promotion audit of 2026-10-19 ([ADR-047](../decisions.d/ADR-047.md), batch 007), it went Active with
the results re-derived. The clause of its promote_when that asked for the
conditions under which the truncated matrix stays orthogonal was moved here
unchanged.

For an exact isometry the answer is easy. The full matrix C is
block-diagonal by eigenspace, so if n ends at a gap between eigenvalues,
the leading n × n block is a direct sum of orthogonal blocks. The open case
is the near-isometry. Then C mixes eigenspaces a little, and whether the
span of the first n eigenfunctions survives depends on the gap between the
nth and (n + 1)st eigenvalues. The paper cites Kato (1995) for this and
does not show it. It also reports that C stops being nearly diagonal
quickly under non-isometric deformation, measured on one data set.

## What would answer it

A perturbation bound, read in a source the record holds or proved here,
for the leading block of C under a map whose metric distortion is at most
ε. For instance, a Davis–Kahan-type bound on the angle between the
truncated eigenspaces, in terms of ε and the gap at n. Shape-matching
benchmarks cannot settle it, since they test the method and not the bound.
