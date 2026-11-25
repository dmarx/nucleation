---
number: 273
status: Proposed
formerly:
- CASE-tmp86zrj
title: 'Orthogonal task updates that interact'
statement: >-
  Orthogonal task updates can interact: for f_w(x) = (w·x)², the updates (1,
  0) and (0, 1) from w = 0 are orthogonal, yet at x = (1, 1) their joint
  effect exceeds the sum of their separate effects by 2, the mixed
  second-order term that a model linearized at its base cannot have
version: 2
history:
- version: 2
  date: '2026-11-18'
  note: >-
    Note of 2026-11-18 added: Zhu, Li and Cai (2026), read, as an
    empirical instance of composition that depends on the inputs. No other
    change.
standing: stipulated
kind: construction
tags:
- learning-theory
- mathematics
date: '2026-11-15'
line:
- learned-structure
bears_on:
- QUESTION-318
draws_on:
- THEORY-1892
- THEORY-1890
summary: >-
  A's construction from A15 of the continuation of the exchange "Explain
  String Theory" (2026-11-15), after the owner's "I suspect there are
  results in the model merging literature that would be relevant here".
  The arithmetic is rechecked (scratch/formal/reconstruction_channel_checks.py).
  No paper read for this filing states it. That the interaction is the
  mixed second derivative integrated over the square, and vanishes
  identically for a model linearized at the base, is the reader's
  derivation; it matches the tangent-space regime of Ortiz-Jimenez et al.
  ([THEORY-1892](../theory.d/THEORY-1892.md)) and the second-order term Zhou et al. bound
  ([THEORY-1890](../theory.d/THEORY-1890.md)). Proposed because the
  construction is A's; adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-1892 THEORY-1890 — Proposed; the readings the construction is set against -->

# CASE-273: Orthogonal task updates that interact

## The construction

The interaction of two updates on an output is

    𝓘(x) = f_{θ0+ΔA+ΔB}(x) − f_{θ0+ΔA}(x) − f_{θ0+ΔB}(x) + f_{θ0}(x)
         = ∫₀¹∫₀¹ D²_θ f_{θ0+sΔA+tΔB}(x)[ΔA, ΔB] ds dt.

For f_w(x) = (w·x)², w0 = 0, ΔA = (1, 0), ΔB = (0, 1) and x = (1, 1), the
four values are 0, 1, 1 and 4, so 𝓘 = 4 − 1 − 1 + 0 = 2, although
ΔA·ΔB = 0.

## What it shows

Orthogonality in parameter space does not make task updates add in
function. Whether they compose depends on curvature along the path that
joins them, and so on the inputs and the downstream computation. That is
why the merging papers read with this filing measure compatibility through
features, singular subspaces or a propagated interference term, not
through parameter angles.

## What it cannot show

That a given merge fails. In models fine-tuned from one start, layerwise
feature linearity often holds approximately ([THEORY-1890](../theory.d/THEORY-1890.md)), so the cross
term can be small in practice.

## Note of 2026-11-18: Zhu, Li and Cai (2026), read

<!-- inactive-ok-file: THEORY-1996 — new; the reading's account -->

Zhu, Li and Cai ([LIT-2779](../literature.d/LIT-2779.md), [NOTE-2078](../notes.d/NOTE-2078.md); [THEORY-1996](../theory.d/THEORY-1996.md)) find in
merged LoRA task vectors what this construction shows in miniature: the
same pair of updates is non-additive in output on code prompts and
additive on math prompts, "Neither pair identity" "nor input distribution
alone determines compositionality". At 0.5B a parameter-space clustering
audit detects nothing where the functional contrast is intact, "which is
the concrete sense in which parameter summaries" "under-determine
functional composition". The pairs' absolute cosines are not reported, so
the construction's premise, orthogonal updates, is not measured as such.
