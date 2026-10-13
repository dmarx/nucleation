---
status: Proposed
title: A regularized linear readout can tell apart only representations that
  differ in normalized kernel, and kernels fix a representation only up to
  the symmetry of what is observed, so any distinction beyond that is supplied
  by the analyst, not by the readouts
version: 1
history:
- version: 1
  date: '2026-10-13'
  note: Split from CLAIM-193 under ADR-040, at the owner's request ("go ahead
    with the group B splits"). The assistant restated the general content
    without the premises about translation that CLAIM-193 rests on; CLAIM-193
    now rests on this claim.
role: thesis
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
- THEORY-002
- THEORY-018
- THEORY-019
summary: The general content of [CLAIM-193](CLAIM-193.md), filed alone under [ADR-040](../decisions.d/ADR-040.md) so that
  the linear result does not rest on [CLAIM-142](CLAIM-142.md), whose realist reading is about
  communicative identity. What a regularized linear readout decodes is a function
  of the normalized kernel ([THEORY-008](../theory.d/THEORY-008.md)). Kernels fix a representation only
  up to the symmetry of what is observed ([THEORY-002](../theory.d/THEORY-002.md)). An inner product beyond
  that is a stipulation ([THEORY-018](../theory.d/THEORY-018.md)). And spectral degeneracy does not identify
  the symmetry ([THEORY-019](../theory.d/THEORY-019.md)). These are proved results for learned representations.
supports:
- CLAIM-193
---
<!-- inactive-ok-file: CLAIM-142 CLAIM-193 THEORY-002 THEORY-008 THEORY-019 — Proposed; cited for what each holds or applies, open, not settled -->

# CLAIM-tmpqe024: A regularized linear readout can tell apart only representations that differ in normalized kernel, and kernels fix a representation only up to the symmetry of what is observed, so any distinction beyond that is supplied by the analyst, not by the readouts

## The claim

For one important probe family, linear readouts, the separating power is
known exactly:

- **The kernel decides.** What a regularized linear readout can decode
  from a representation is a function of its normalized kernel
  ([THEORY-008](../theory.d/THEORY-008.md)). Two representations with the same normalized kernel are
  indistinguishable to every such readout, whatever basis they are written
  in. CKA, CCA and GULP are averages of readout agreement.
- **Kernels fix representations only up to symmetry.** Convergence of
  kernels fixes representations only up to the symmetry group of what is
  observed ([THEORY-002](../theory.d/THEORY-002.md)).
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
