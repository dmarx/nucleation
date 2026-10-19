---
status: Open
title: 'In the Poincaré ball H^r for r > 2, does embedding a tree with worst-case distortion 1 + ε need Ω((ℓ/(εr)) log deg_max) bits per coordinate for r up to about log deg_max, and Ω(ℓ/ε) beyond, matching the code-based upper bound?'
version: 1
tags:
- representation-learning
- mathematics
date: '2026-10-19'
line: 'learned-structure'
summary: >-
  The higher-dimensional half of the promotion condition formerly on
  [THEORY-196](../theory.d/THEORY-196.md), moved here when [THEORY-196](../theory.d/THEORY-196.md)'s planar lower bound was split off
  as [THEORY-tmpfydax](../theory.d/THEORY-tmpfydax.md) on 2026-10-19. [LIT-874](../literature.d/LIT-874.md)'s Proposition 3.1 gives the
  upper bound in H^r. No lower bound in H^r is held, so whether dimension
  helps exactly as much as the construction uses is open.
---
<!-- inactive-ok-file: THEORY-196 — Proposed; the account whose condition this was, cited as open -->

# QUESTION-tmpr1c4g: In the Poincaré ball H^r for r > 2, does embedding a tree with worst-case distortion 1 + ε need Ω((ℓ/(εr)) log deg_max) bits per coordinate for r up to about log deg_max, and Ω(ℓ/ε) beyond, matching the code-based upper bound?

## Why it is a question

[LIT-874](../literature.d/LIT-874.md) (read in [NOTE-679](../notes.d/NOTE-679.md)) places a node's children at hypercube vertices
chosen by a Hadamard code, and so embeds any tree in H^r with distortion
1 + ε using O((ℓ/(εr)) log deg_max) bits per coordinate for r up to about
log deg_max + 1, and O(ℓ/ε) beyond (Proposition 3.1). The matching lower
bound is proved only in the plane, which [THEORY-tmpfydax](../theory.d/THEORY-tmpfydax.md) now holds with
explicit constants. The paper's remark that no dimension helps beyond
log deg_max is a footnote argument. Until 2026-10-19, [THEORY-196](../theory.d/THEORY-196.md)'s
promote_when asked for this extension together with the planar proof.
[THEORY-196](../theory.d/THEORY-196.md)'s title is about the plane, and its body disclaims the
extension, so the clause moved here.

## What would answer it

A proof that some family of trees embedded in H^r with worst-case
distortion 1 + ε forces a node to hyperbolic distance
Ω((ℓ/(εr)) log deg_max) from the origin for r ≲ log deg_max, and Ω(ℓ/ε)
beyond. The planar argument's angle-packing step ([THEORY-tmpfydax](../theory.d/THEORY-tmpfydax.md), step 4)
would become a spherical-code bound on S^(r−1). Or a construction that
beats Proposition 3.1 in depth or in dimension. Experiments in which
deep trees need more bits than bushy ones cannot settle it, because the
upper bound already predicts that.
