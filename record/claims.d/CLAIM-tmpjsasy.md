---
status: Active
title: 'What a spectral gap makes definite is the subspace of the cluster it isolates, not a single direction: the gap picks the object, and the object is a vector only when its own gap is wide'
version: 1
history:
- version: 1
  date: '2026-10-11'
  note: >-
    Dual-filed from MOM-CLM-144 under ADR-037. Active here because the
    result rests on Davis–Kahan, a standard perturbation theorem, and
    because MOM's measurement was re-run independently on 2026-10-11.
    That was a 400×30 operator at noise 0.02 with 150 resamples, not
    MOM's 300. It reproduced the pattern: the degenerate case's top
    vector drifted 41° median and 86° max while the top-2 subspace
    drifted 2.3°, and with a wide gap at the top the vector was the more
    stable object (2.1° against 4.7°). The exact angles differ from
    MOM's with the random draw.
role: thesis
defeated_if: >-
  A perturbation regime in which a subspace bounded by a wide gap rotates
  by more than Davis–Kahan's ‖δT‖/δ, or a degenerate cluster whose
  individual vectors are stable under small noise.
tags:
- mathematics
- individuation
- complex-systems
date: '2026-10-11'
line: distributed-agency
summary: >-
  Dual-filed from [MOM-CLM-144](https://github.com/dmarx/mathematics-of-meaning/blob/main/record/claims.d/CLM-144.md) ([ADR-037](../decisions.d/ADR-037.md)). Under a perturbation δT, the
  subspace spanned by a cluster of singular values separated by a gap δ
  rotates by at most ‖δT‖/δ (Davis–Kahan), whatever happens to the
  vectors inside it. So the well-defined unit is the gap-isolated
  projector. Re-measured here. With [CLAIM-tmp45kkg](CLAIM-tmp45kkg.md) it is a criterion: the
  gap picks the object, and the Occam factor says whether the gap is big
  enough.
complements:
- CLAIM-tmp45kkg
---
<!-- inactive-ok-file: ADR-037 — Proposed; the decision this entry is filed under -->

# CLAIM-tmpjsasy: What a spectral gap makes definite is the subspace of the cluster it isolates, not a single direction: the gap picks the object, and the object is a vector only when its own gap is wide

## The claim

From [MOM-CLM-144](https://github.com/dmarx/mathematics-of-meaning/blob/main/record/claims.d/CLM-144.md). Let a cluster of singular values be separated from the
rest of the spectrum by a gap δ. The invariant is the subspace V they span,
or equivalently the projector P onto V. Under a perturbation δT, P moves by
at most about ‖δT‖/δ, which is Davis–Kahan. A single vector is its own
cluster only when its own gaps are wide. Where values are degenerate, "the
k-th vector" names nothing: any rotation within V is an equally good basis.

## Why this record holds it

Davis–Kahan is standard. The 2026-10-11 re-run reproduced MOM's table
qualitatively (history note). The vector failed under degeneracy, with a
maximum near a right angle, while the subspace held. Where the top value had
a wide gap of its own, the vector was the more stable object, because the
top-2 subspace's boundary then fell in a narrow gap.

For this record it says what the unit is once a boundary test has been run.
The unit is the block or cluster that a gap sets off, not any one member or
coordinate. In the dancing couple that is the pair's joint mode, not either
dancer's own. That application is this record's.

## What it does not say

- **How large the gap must be.** That is [CLAIM-tmp45kkg](CLAIM-tmp45kkg.md).
- **That spectral subspaces are the only candidates for units.** It is a
  claim about what a gap makes definite in a linear description.
