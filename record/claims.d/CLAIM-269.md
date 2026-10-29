---
number: 269
status: Proposed
formerly:
- CLAIM-tmpqe024
title: A regularized linear readout can tell apart only representations that
  differ in normalized kernel, and kernels fix a representation only up to
  the symmetry of what is observed, so any distinction beyond that is supplied
  by the analyst, not by the readouts
version: 4
history:
- version: 1
  date: '2026-10-13'
  note: Split from CLAIM-193 under ADR-040, at the owner's request ("go ahead
    with the group B splits"). The assistant restated the general content
    without the premises about translation that CLAIM-193 rests on; CLAIM-193
    now rests on this claim.
- version: 2
  date: '2026-10-19'
  note: >-
    Split at the owner's direction, carrying out the promotion audit's
    decision (record/promotion-audit/decisions/CLAIM-269.yaml, batch 015,
    ADR-047). The readout result, on a finite set of stimuli, is now
    CLAIM-379, Active: for ridge b > 0 readouts cannot tell apart
    exactly the representations related by an orthogonal map, and the CCA
    member those related by an invertible linear map. This claim rests on
    it and keeps the two clauses grounded on Proposed THEORYs: that
    converging kernels fix a representation only up to the symmetry of
    what is observed (THEORY-002), and that degeneracy does not identify
    the symmetry (THEORY-019). It stays Proposed until they are settled.
- version: 3
  date: '2026-10-29'
  note: >-
    The second bullet's ground moved from THEORY-002 to THEORY-004 and
    THEORY-723 by the eleventh status review (ADR-057, ADR-058). The
    bullet uses only what a kernel and a softmax distribution fix, which
    those Active readings hold, and not THEORY-002's reading of the
    Platonic hypothesis, which this claim never invokes. THEORY-002's
    supports entry for this claim is removed. The old bullet: Convergence
    of kernels fixes representations only up to the symmetry group of
    what is observed (THEORY-002). The claim is unchanged.
- version: 4
  date: '2026-10-29'
  note: >-
    rests_on CLAIM-385 added by the twelfth status review (ADR-057,
    ADR-058). The fourth bullet, that degeneracy does not identify the
    symmetry, is what this claim adds to CLAIM-379, and it is CLAIM-385's
    item 4, the record's own demonstrated result. THEORY-019, the reading
    the bullet also cites, was promoted the same day, so the blocker note
    of this date is revised to say what is left. The claim is unchanged
    and the status stays Proposed.
role: thesis
warrant: demonstrated
defeated_if: A regularized linear readout shown to separate two representations
  with the same normalized kernel. Or two representations with the same kernel
  shown to differ in some readout-decodable property not fixed by a symmetry
  of the observed data.
tags:
- representation-learning
- mathematics
date: '2026-10-13'
line:
- formal-apparatus
grounds:
- THEORY-008
- THEORY-004
- THEORY-723
- THEORY-018
- THEORY-019
summary: The general content of [CLAIM-193](CLAIM-193.md), filed alone under [ADR-040](../decisions.d/ADR-040.md) so that
  the linear result does not rest on [CLAIM-142](CLAIM-142.md), whose realist reading is about
  communicative identity. What a regularized linear readout decodes is a function
  of the normalized kernel ([THEORY-008](../theory.d/THEORY-008.md)). Kernels fix a representation only
  up to the symmetry of what is observed (THEORY-004, THEORY-723). An inner product beyond
  that is a stipulation ([THEORY-018](../theory.d/THEORY-018.md)). And spectral degeneracy does not identify
  the symmetry ([THEORY-019](../theory.d/THEORY-019.md)). These are proved results for learned representations.
rests_on:
- CLAIM-379
- CLAIM-385
supports:
- CLAIM-193
---
<!-- inactive-ok-file: CLAIM-142 CLAIM-193 — Proposed; cited for what each holds or applies, open, not settled -->

# CLAIM-269: A regularized linear readout can tell apart only representations that differ in normalized kernel, and kernels fix a representation only up to the symmetry of what is observed, so any distinction beyond that is supplied by the analyst, not by the readouts

## The claim

For one important probe family, linear readouts, the separating power is
known exactly:

- **The kernel decides.** What a regularized linear readout can decode
  from a representation is a function of its normalized kernel
  ([THEORY-008](../theory.d/THEORY-008.md)). Two representations with the same normalized kernel are
  indistinguishable to every such readout, whatever basis they are written
  in. CKA, CCA and GULP are averages of readout agreement.
- **Kernels fix representations only up to symmetry.** A centred kernel
  fixes a representation up to a translation and an orthogonal map
  ([THEORY-004](../theory.d/THEORY-004.md)), and a softmax model's output distribution fixes its final
  layer only up to an invertible linear map ([THEORY-723](../theory.d/THEORY-723.md)).
- **Anything further is stipulated.** Softmax training identifies a final
  layer only up to an invertible linear map, so no inner product on it is
  intrinsic ([THEORY-018](../theory.d/THEORY-018.md)).
- **The spectrum does not recover the symmetry.** Symmetry forces
  degeneracy, but degeneracy does not identify a symmetry ([THEORY-019](../theory.d/THEORY-019.md)).

So a linear probe family separates exactly what the kernel separates.
It collapses representations that differ only by a symmetry of the
observed data, and a distinction drawn beyond that comes from the analyst.

## Where the record applies it

[CLAIM-193](CLAIM-193.md) carries the result to communicative realizations read through a
probe family, resting on [CLAIM-142](CLAIM-142.md) for the relativity of observational
equivalence there. It now also rests on this claim for the linear result.

## What it does not say

- It does not cover nonlinear probes, behavioural probes or human judges.
- It does not say any domain other than learned representations has a
  kernel playing the same role. That is each application's step.

## Note of 2026-10-19: the readout half is held Active

The first bullet above, with what follows from it through [THEORY-004](../theory.d/THEORY-004.md), is
now [CLAIM-379](CLAIM-379.md), filed Active with its derivation. For ridge b > 0 the
kernel K_X and the Gram matrix determine each other, so readouts collapse
exactly the orthogonal orbit of a centred representation; the CCA member
collapses the invertible-linear orbit. What this claim adds, and why it
stays Proposed, is the fourth bullet: that spectral degeneracy does not
identify the symmetry of the observed data ([THEORY-019](../theory.d/THEORY-019.md)).

## Note of 2026-10-29: what holds it back

No premise is now Proposed: THEORY-019 is Active since the twelfth status
review, and the fourth bullet also rests on CLAIM-385. What is left is a
check of the claim's own last step, that a distinction beyond the kernel's
symmetry "is supplied by the analyst", which may be interpretive rather
than demonstrated.
