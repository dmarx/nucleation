---
number: 43
status: Active
formerly:
- TERM-tmpz8i47
title: 'fidelity, as a profile of directed distortions compared component by component'
version: 1
tags:
- philosophy-of-language
- information-theory
date: '2026-10-10'
line: pragmatic-transport
supersedes:
- TERM-010
summary: >-
  The owner agreed at U41 to unify the record's fidelity lineages, and
  A129 §3 made one transport with several tests. The profile had four
  components at A129, five at A151, A178 and A218, and an optional sixth
  at A203. Transports are compared componentwise; a scalar exists only
  once a task fixes weights. Supersedes [TERM-010](TERM-010.md)'s weighted scalar as the
  foundation; [TERM-015](TERM-015.md) and [TERM-021](TERM-021.md) stay in force as what the components
  measure.
used_by:
- CLAIM-128
- CLAIM-133
- CLAIM-139
- CLAIM-147
- CLAIM-tmpbi9eb
- CLAIM-tmpwvljf
---
<!-- inactive-ok-file: CLAIM-127 CLAIM-128 — Proposed; open, and cited as open: the claim is under test, not settled -->

# TERM-043: fidelity, as a profile of directed distortions compared component by component

## Definition

A125 §3 proposed that the two Active fidelity lineages be unified: "The
first is a *measurement criterion*; the second is the *general relation*."
The owner answered at U41: "agreed." A129 §3: "the solution is not to add
more meanings to the word *fidelity*. We should distinguish the
transformation being evaluated from the tests applied to it."

A transport T from a source system to a target system "specifies how
realizations, contexts, observations, and relevant inference tasks
correspond" (A129 §3). Its fidelity is the profile of its distortions. A151
§5 gives five components, D(T) = (D_obs(T), D_struct(T), D_dec(T),
D_causal(T), D_dyn(T)), and glosses each:

| Component | What it measures (A151 §5) |
|---|---|
| Observational | Differences between corresponding context-indexed empirical distributions |
| Structural | Failures to preserve restriction maps and specified relational constraints |
| Decision-theoretic | Loss of ability to perform relevant communicative inference tasks |
| Causal | Differences in responses to corresponding interventions |
| Dynamical | Differences in subsequent interpretation and reconstruction trajectories |

A129 §3 had four components, without D_causal, which it added after them
as "Pearl adds another dimension". A178 and A218 keep five. A203 §22 adds a
sixth, D_χ: "The character component D_χ is optional and meaningful only
when the relevant transformation representations have been defined".

Transports are compared component by component: T_1 ⪯ T_2 when
D_j(T_1) ≤ D_j(T_2) for every j. "When the profiles trade off, the
transports are incomparable without selecting additional priorities"
(A129 §3). A weighted sum D_w = Σ_j w_j D_j is "introduced for
optimization" once a task fixes w. A151 §5: "two translations can preserve
different structures without being forced into a universal ranking. We can
introduce task-specific weights when a scalar objective is useful." The
consequence for ranking translations is [CLAIM-128](../claims.d/CLAIM-128.md).

## How the older terms sit in the profile

- **[TERM-021](TERM-021.md)** is D_obs, with the source distributions pushed forward by
  the transport: D_obs(T) = Σ_C w_C d_C(T_C# e_C^o, e_τ(C)^t) (A125 §3).
- **[TERM-015](TERM-015.md)** is the directed, graded relation that the components measure.
  A129 §3: "[TERM-015](TERM-015.md) supplies the general directed, graded transport
  relation."
- **[TERM-033](TERM-033.md)** is the zero-distortion limit over response trajectories. A129
  §3: "[TERM-033](TERM-033.md) supplies the limiting case of trajectory-based behavioral
  equivalence."
- **[TERM-028](TERM-028.md) and [TERM-034](TERM-034.md)** are D_dec. The profile drops [TERM-034](TERM-034.md)'s rate
  constraint and its interpreter, which A108 had put in the definition.
- **[TERM-036](TERM-036.md),** fidelity as preservation of selected symmetries, is not
  placed. A203's optional D_χ comes nearest to it, and no turn connects
  them.

## What it is not

- **Not [TERM-010](TERM-010.md)'s scalar.** [TERM-010](TERM-010.md) minimized a weighted sum of three
  distortions under a rate budget. This term supersedes it as the
  foundation. The scalar survives as one weighting, chosen per task.
- **Not a metric.** Each component is directed, and only D_obs has a
  formula.
- **D_causal is not cleanly a further component.** A129 §3 defines it as
  Σ_a π(a) d(T_# P_o(Y | do(a)), P_t(Y′ | do(τ(a)))). That is [TERM-033](TERM-033.md)'s
  comparison under corresponding interventions at one step, and it overlaps
  D_dyn ("Does the reconstruction respond similarly to subsequent framing
  interventions?"). A129 says that D_causal "makes the relationship between
  dynamic fidelity and causal fidelity precise", but does not separate them
  (R1). D_causal also needs a correspondence τ on interventions as well as on
  contexts ([CLAIM-127](../claims.d/CLAIM-127.md)), and how it would be estimated when corresponding
  interventions cannot be identified is [QUESTION-005](../questions.d/QUESTION-005.md).
- **Character distance is a diagnostic, not a definition of fidelity.**
  A198 §VIII: "I would resist turning character distance into the
  universal definition of communicative fidelity." A218 §8: "Character
  similarity is neither a general sufficient condition nor a universal
  definition of fidelity."
- **Not a partial order on transports.** Componentwise comparison is a
  partial order on profile vectors, but only a preorder on transports:
  distinct transports can share a profile (R1).
