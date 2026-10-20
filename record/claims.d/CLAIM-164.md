---
number: 164
status: Active
formerly:
- CLAIM-164
title: 'What a spectral gap makes definite is the subspace of the cluster it isolates, not a single direction: the gap picks the object, and the object is a vector only when its own gap is wide'
version: 3
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
- version: 2
  date: '2026-10-19'
  note: >-
    Note added, carrying out the promotion audit's decision
    (record/promotion-audit/decisions/CLAIM-164.yaml, batch 015, ADR-047).
    THEORY-084, one of this claim's grounds, was split after the note of
    2026-10-12 described it whole. Its spectral identity is now CLAIM-377,
    Active; the block inheritance and the threshold stay in THEORY-084,
    Proposed. The new note says which part is established and what it
    gives this claim. Grounds and status are unchanged.
- version: 3
  date: '2026-10-20'
  note: >-
    Note of 2026-10-20 added, from the reading of Nadler et al. (NOTE-986). The claim is unchanged.
role: thesis
warrant: demonstrated
defeated_if: >-
  A perturbation regime in which a subspace bounded by a wide gap rotates
  by more than Davis–Kahan's ‖δT‖/δ, or a degenerate cluster whose
  individual vectors are stable under small noise.
tags:
- mathematics
- individuation
- complex-systems
date: '2026-10-11'
line:
- distributed-agency
- formal-apparatus
uses:
- TERM-046
summary: >-
  Dual-filed from [MOM-CLM-144](https://github.com/dmarx/mathematics-of-meaning/blob/main/record/claims.d/CLM-144.md) ([ADR-037](../decisions.d/ADR-037.md)). Under a perturbation δT, the
  subspace spanned by a cluster of singular values separated by a gap δ
  rotates by at most ‖δT‖/δ (Davis–Kahan), whatever happens to the
  vectors inside it. So the well-defined unit is the gap-isolated
  projector. Re-measured here. With [CLAIM-154](CLAIM-154.md) it is a criterion: the
  gap picks the object, and the Occam factor says whether the gap is big
  enough.
complements:
- CLAIM-154
- CLAIM-377
supports:
- CLAIM-157
grounds:
- THEORY-078
- THEORY-084
---

# CLAIM-164: What a spectral gap makes definite is the subspace of the cluster it isolates, not a single direction: the gap picks the object, and the object is a vector only when its own gap is wide

## The claim

From [MOM-CLM-144](https://github.com/dmarx/mathematics-of-meaning/blob/main/record/claims.d/CLM-144.md). Let a cluster of singular values be separated from the
rest of the spectrum by a gap δ ([TERM-046](../terms.d/TERM-046.md)<!-- ref::uses: TERM-046 -->). The invariant is the subspace V they span,
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

- **How large the gap must be.** That is [CLAIM-154](CLAIM-154.md).
- **That spectral subspaces are the only candidates for units.** It is a
  claim about what a gap makes definite in a linear description.

## Note of 2026-10-12: evidence now linked

Two THEORYs now ground this claim. [THEORY-084](../theory.d/THEORY-084.md): a spectral threshold on the lazy-regime Fisher is well posed only at gaps between blocks, with guarantees stated only for whole eigenspaces. [THEORY-078](../theory.d/THEORY-078.md), weaker because its attribution is made by eye: a cut at the bulk edge keeps the span of the class means, not C discriminative directions.

## Note of 2026-10-19: which part of [THEORY-084](../theory.d/THEORY-084.md) is established

Since the split of [THEORY-084](../theory.d/THEORY-084.md), only its first step is held Active, as
[CLAIM-377](CLAIM-377.md): the Gauss–Newton Fisher βJᵀJ and the NTK Gram matrix JJᵀ have the
same non-zero eigenvalues with the same multiplicities, and the eigenvectors
correspond as u ↦ Jᵀu, normalized. That gives this claim one exact instance.
A gap in the Fisher's spectrum is the same gap in the NTK Gram's, and the
subspaces the two gaps isolate correspond, so a gap test run on either is the
same test. That the lazy-regime Fisher inherits the NTK's harmonic-degree
blocks, and that a threshold is well posed only between them, are still
[THEORY-084](../theory.d/THEORY-084.md)'s, Proposed. This claim does not need them: its core is
Davis–Kahan.

## Note of 2026-10-20: a gap-isolated subspace need not count slow variables

Nadler, Lafon, Coifman and Kevrekidis ([NOTE-986](../notes.d/NOTE-986.md), §5.2) show that a
slow subspace isolated by a gap can be spanned by several functions of one
slow variable, ψ and its powers, when the gap between that variable's
harmonics and the fast modes is wide. So the dimension of the subspace
this claim makes definite is not the number of slow variables. The object
is still the subspace. Reading off how many independent slow variables it
holds needs a further step, which the gap does not supply.
