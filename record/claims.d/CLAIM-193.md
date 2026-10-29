---
number: 193
status: Proposed
formerly:
- CLAIM-tmppqir6
title: 'A linear probe family can tell apart only realizations whose representations differ in normalized kernel, and kernels fix a representation only up to the symmetry of what is observed: any distinction beyond that is supplied by the analyst'
version: 4
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Warrant corrected from demonstrated to interpretive at the owner's
    direction, carrying out the promotion audit's decision
    (record/promotion-audit/decisions/CLAIM-193.yaml, batch 003, ADR-047).
    Since the ADR-040 split of 2026-10-13, the demonstrated linear-readout
    result has been CLAIM-269's, and the first disjunct of this claim's
    defeat condition was CLAIM-269's, word for word. That disjunct is
    dropped. What this claim adds is the carry-over to communicative
    realizations, which the body calls "the filer's step", so it is
    interpretive (ADR-043). The status stays Proposed.
- version: 3
  date: '2026-10-29'
  note: >-
    The second bullet's ground moved from THEORY-002 to THEORY-004 and
    THEORY-723 by the eleventh status review (ADR-057, ADR-058). The
    bullet uses only what a kernel and a softmax distribution fix, which
    those Active readings hold, and not THEORY-002's reading of the
    Platonic hypothesis, which this claim never invokes. THEORY-002's
    supports entry for this claim is removed. The old bullet: Convergence
    of kernels fixes representations "only up to the symmetry group of
    what is observed" (THEORY-002). The claim is unchanged.
- version: 4
  date: '2026-10-29'
  note: >-
    rests_on CLAIM-142 replaced by CLAIM-264 by the thirteenth status
    review (ADR-057), at the status review's ruling (the owner delegated
    these rulings). The claim uses only the relativity of observational
    equivalence, which is CLAIM-264's general content, not CLAIM-142's
    realist half; CLAIM-142 is now a complement. The defeat condition is
    restated to the claim's own step, since as worded any basis-dependent
    or nonlinear probe family met it, and the claim puts those outside its
    scope. The old condition: For communicative realizations, a probe
    family is found whose separating power is not determined by a kernel
    or similarity structure over the realizations, so that the linear-readout
    result (CLAIM-269) does not carry across. The claim is
    unchanged and the status stays Proposed.
role: thesis
warrant: interpretive
defeated_if: >-
  A linear probe family used on communicative realizations is found that
  does not read them through one representation with a kernel, so that
  CLAIM-269's result does not fix its separating power.
tags:
- representation-learning
- mathematics
date: '2026-10-12'
line: pragmatic-transport
rests_on:
- CLAIM-264
- CLAIM-269
grounds:
- THEORY-008
- THEORY-004
- THEORY-723
- THEORY-018
- THEORY-019
summary: >-
  A partial answer to [QUESTION-031](../questions.d/QUESTION-031.md) for the linear case, from THEORYs
  the record held without linking them to the line. What a regularized
  linear readout decodes is a function of the normalized kernel
  ([THEORY-008](../theory.d/THEORY-008.md)); kernels fix a representation only up to the symmetry of
  what is observed (THEORY-004, THEORY-723); an inner product beyond that is a
  stipulation ([THEORY-018](../theory.d/THEORY-018.md)); and spectral degeneracy does not identify the
  symmetry ([THEORY-019](../theory.d/THEORY-019.md)). Proved results for learned representations;
  the carry-over to communicative realizations is the filer's.
complements:
- CLAIM-209
- CLAIM-142
bears_on:
- QUESTION-031
---
<!-- inactive-ok-file: CLAIM-269 — Proposed; the general form of a premise, filed under ADR-040, open -->
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
- **Kernels fix representations only up to symmetry.** A centred kernel
  fixes a representation up to a translation and an orthogonal map
  ([THEORY-004](../theory.d/THEORY-004.md)), and a softmax model's output distribution fixes its final
  layer only up to an invertible linear map ([THEORY-723](../theory.d/THEORY-723.md)).
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

## Note of 2026-10-13: the general content is filed separately

Under [ADR-040](../decisions.d/ADR-040.md), the linear-readout result is filed on its own as [CLAIM-269](CLAIM-269.md), in the
formal-apparatus line, resting on no claim. This claim now rests on it for
the general content, and keeps [CLAIM-142](CLAIM-142.md), for carrying the result to communicative realizations. Claims in other lines that need
only the general content cite [CLAIM-269](CLAIM-269.md), so setting pragmatic-transport aside
does not take it from them.

## Note of 2026-10-19: the warrant

The linear-readout result is [CLAIM-269](CLAIM-269.md)'s, in the formal-apparatus line,
and its defeat condition is that claim's. This claim keeps the step that
communicative realizations read through a probe family have a kernel that
plays the same role. That step is argued, not proved, and whether human
judges are a probe family at all is the open dispute between [CLAIM-142](CLAIM-142.md) and
[CLAIM-206](CLAIM-206.md). So the warrant is interpretive.

## Note of 2026-10-29: what holds it back

Its premises are now Active (CLAIM-264, CLAIM-269), and its defeat condition
was restated today to its own step: that a linear family used on
communicative realizations reads them through one representation with a
kernel. The restated test has not yet been weighed against the record's
probe families on communicative realizations, so nothing yet says whether
any of them meets it.
