---
number: 201
# Don't copy this file by hand — run `luria new question`. A QUESTION is an
# open question the record's own argument is organised around. Claims and
# THEORY readings name it in `answers`, and its page shows both (ADR-032).

# Open | Answered | Dissolved | Deferred | Superseded
status: Open
formerly:
- QUESTION-tmpymmv6

# The question, as a question. Repeat it as the `# QUESTION-…:` heading.
title: 'Do random patterns stored by the Hebbian outer-product rule stay attractors with basins of nonzero width up to a load near 0.14N at large N, does recall then collapse for every pattern at once, and at what overlap do two stored patterns fuse?'

version: 1
tags:
- complex-systems
- neuroscience
date: '2026-10-20'

# REQUIRED: the line of inquiry, from `lines` in luria.yaml.
line: 'nucleating-argument'
summary: >-
  The promotion condition formerly on [THEORY-272](../theory.d/THEORY-272.md). [THEORY-272](../theory.d/THEORY-272.md) was narrowed
  to Hopfield's 1982 simulations at N = 30 and 100 and promoted on
  2026-10-20 ([ADR-047](../decisions.d/ADR-047.md) v3). Whether the capacity, collapse and fusion it
  measured hold at large N is open.

# refines: [QUESTION-000]   # the broader question this sharpens

answered_by:
- THEORY-800
---

<!-- unresolved-ok-file: QUESTION-000 — the placeholder a new document replaces -->

# QUESTION-201: Do random patterns stored by the Hebbian outer-product rule stay attractors with basins of nonzero width up to a load near 0.14N at large N, does recall then collapse for every pattern at once, and at what overlap do two stored patterns fuse?

## Why it is a question

[THEORY-272](../theory.d/THEORY-272.md) holds what Hopfield measured at N = 30 and 100. Recall
degrades severely near 0.15N random patterns. An extra pattern 10 bits
from another at N = 100 often fuses with it. At 25-fold overload, no
stored pattern stays stable. Hopfield expects the 0.15N figure "for all
large N" from a Gaussian estimate of the crosstalk, but he shows it only
at N ≤ 100, and the record holds no large-N treatment. Until 2026-10-20
this was [THEORY-272](../theory.d/THEORY-272.md)'s promote_when.

## What would answer it

- A reading of the analytic treatment of the same model (Amit,
  Gutfreund and Sompolinsky 1985 and 1987, or an equivalent).
- A simulation at N in the thousands, showing that stored random
  patterns are attractors with basins of nonzero width up to a load near
  0.14–0.15N, that recall then collapses for all patterns rather than
  degrading pattern by pattern, and at what overlap two patterns fuse.

Against it: the capacity scaling failing at large N, or the large-N
basins shrinking to zero width at any load.

What would not answer it: another simulation at N = 30 or 100, the sizes
[THEORY-272](../theory.d/THEORY-272.md) already rests on.
