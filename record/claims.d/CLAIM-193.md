---
number: 193
status: Proposed
formerly:
- CLAIM-tmppqir6
title: 'A linear probe family can tell apart only realizations whose representations differ in normalized kernel, and kernels fix a representation only up to the symmetry of what is observed: any distinction beyond that is supplied by the analyst'
version: 1
role: thesis
defeated_if: >-
  A regularized linear readout is shown to separate two representations
  with the same normalized kernel. Or, for communicative realizations, a
  probe family is found whose separating power is not determined by a
  kernel or similarity structure over the realizations, so that the
  result does not carry across.
tags:
- representation-learning
- mathematics
date: '2026-10-12'
line: pragmatic-transport
answers:
- QUESTION-031
rests_on:
- CLAIM-142
grounds:
- THEORY-008
- THEORY-002
- THEORY-018
- THEORY-019
summary: >-
  A partial answer to [QUESTION-031](../questions.d/QUESTION-031.md) for the linear case, from four THEORYs
  the record held without linking them to the line. What a regularized
  linear readout decodes is a function of the normalized kernel
  ([THEORY-008](../theory.d/THEORY-008.md)); kernels fix a representation only up to the symmetry of
  what is observed ([THEORY-002](../theory.d/THEORY-002.md)); an inner product beyond that is a
  stipulation ([THEORY-018](../theory.d/THEORY-018.md)); and spectral degeneracy does not identify the
  symmetry ([THEORY-019](../theory.d/THEORY-019.md)). Proved results for learned representations;
  the carry-over to communicative realizations is the filer's.
complements:
- CLAIM-209
---
<!-- inactive-ok-file: CLAIM-142 CLAIM-204 CLAIM-206 CLAIM-209 CLAIM-217 THEORY-019 — Proposed; cited in a note of 2026-10-12 as open, for what each holds, not as settled -->

# CLAIM-193: A linear probe family can tell apart only realizations whose representations differ in normalized kernel, and kernels fix a representation only up to the symmetry of what is observed: any distinction beyond that is supplied by the analyst

## The claim

[QUESTION-031](../questions.d/QUESTION-031.md) asks when a chosen family of probes separates the
realizations a task needs told apart, and when it collapses distinct ones.
[CLAIM-142](CLAIM-142.md) says observational equivalence is relative to the probes. For
one important family, linear readouts, the record already holds an exact
answer:

- **The kernel decides.** "What a regularized linear readout can decode
  from a representation is a function of its normalized kernel"
  ([THEORY-008](../theory.d/THEORY-008.md), proved identities). Two representations with the same
  normalized kernel are indistinguishable to every such probe, whatever
  basis they are written in. CKA, CCA and GULP are averages of readout
  agreement.
- **Kernels fix representations only up to symmetry.** Convergence of
  kernels fixes representations "only up to the symmetry group of what is
  observed" ([THEORY-002](../theory.d/THEORY-002.md)).
- **Anything further is stipulated.** Softmax training identifies a final
  layer only up to an invertible linear map, so "no inner product on it is
  intrinsic", and a chosen one is fixed by stipulation ([THEORY-018](../theory.d/THEORY-018.md)).
- **The spectrum does not recover the symmetry.** Symmetry forces
  degeneracy, but "degeneracy does not identify a symmetry" ([THEORY-019](../theory.d/THEORY-019.md)).

So a linear probe family separates exactly what the kernel separates. It
collapses realizations that differ only by a symmetry of the observed data,
and a distinction drawn beyond that comes from the analyst, not from the
probes. That gives [CLAIM-142](CLAIM-142.md)'s relativity a precise form in this case.

## What it does not say

- It does not cover nonlinear probes, behavioural probes or human judges,
  which is most of what the pragmatic-transport line uses. It answers the
  linear half of [QUESTION-031](../questions.d/QUESTION-031.md).
- The four results are about learned representations. That communicative
  realizations, read through a probe family, have a kernel playing the same
  role is the filer's step.
- [THEORY-019](../theory.d/THEORY-019.md) also bears on [QUESTION-036](../questions.d/QUESTION-036.md), toward a negative answer, as that
  question's note records.

## Note of 2026-10-12: human judges, and related entries

"What it does not say" counts human judges among the probes this result
does not cover. PR [#121](https://github.com/dmarx/nucleation/issues/121)'s round of 2026-10-10 contests that placing.
[CLAIM-142](CLAIM-142.md) version 2, on which this claim rests, says "The judges are the
criterion ([CLAIM-217](CLAIM-217.md)), not a probe", while [CLAIM-206](CLAIM-206.md) treats
human same-kind judgements as "themselves one probe family"; that dispute
is open. On the first reading this result bounds what an analyst's linear
family can separate when tested against the judges' standard; on the
second it leaves out one probe family among others. [CLAIM-217](CLAIM-217.md) also
addresses [QUESTION-031](../questions.d/QUESTION-031.md): "[QUESTION-031](../questions.d/QUESTION-031.md) asks when a family is rich enough;
this says rich enough relative to what." This claim's "comes from the
analyst, not from the probes" is the linear-case form of [CLAIM-209](CLAIM-209.md)'s
first clause, now related by `complements`, and of the part [CLAIM-204](CLAIM-204.md)
says the analyst can certify.
