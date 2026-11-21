---
status: Proposed
title: "The Lyapunov identity for embeddings coupled through a shared-parameter kernel closes the feedback loop between kernel and representation as a route to active dynamics, so the strong active-matter reading needs a source outside gradient flow"
version: 1
form: formal-application
rests_on:
- CLAIM-tmpet76z
concludes:
- CLAIM-tmp526xr
tags:
- representation-learning
- learning-theory
- thermodynamics
date: '2026-11-21'
line:
- learned-structure
summary: >-
  A29 §2 of the exchange "Rich Get Richer Power Laws" calls the
  co-evolution of the embedding kernel and the representation "the first
  potentially rich feedback loop", and [CLAIM-tmp526xr](../claims.d/CLAIM-tmp526xr.md)'s gaps rely on
  [CLAIM-tmpet76z](../claims.d/CLAIM-tmpet76z.md) to say that loop cannot make the system active. The
  identity dL/dt = −‖Σ_j J_jᵀ g_j‖² uses only the kernel's value at each
  instant, so it holds however the kernel changes; applied to A29's
  equation it rules the loop out as a source of sustained currents under
  gradient flow, and leaves the strong reading to the optimizer, mismatched
  noise or a changing objective. Proposed. The wording is the assistant's
  (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmpet76z CLAIM-tmp526xr THEORY-209 — new and Proposed, filed from the exchange "Rich Get Richer Power Laws" on 2026-11-21, or Proposed entries the record already held -->

# ARG-tmp0rq99: The Lyapunov identity for embeddings coupled through a shared-parameter kernel closes the feedback loop between kernel and representation as a route to active dynamics, so the strong active-matter reading needs a source outside gradient flow

## The inference

A29 §2, after deriving ż_i = −Σ_j K_ij ∇_(z_j) L with K_ij = J_i J_jᵀ:
"K_ij evolves during feature learning, rather than remaining fixed in
general. That means the interaction mechanism and the representational
geometry can reorganize each other. **The particles move because the
network learns, but the manner in which they can move also changes as the
network learns.** This is the first potentially rich feedback loop."

A29 does not say the loop makes the system active; its §4 states that
"Ordinary gradient flow is a relaxation process". But the loop is the
only candidate source of activity that A29's equation itself contains, and
the weak/strong split of [CLAIM-tmp526xr](../claims.d/CLAIM-tmp526xr.md) is sharp only if it is closed.

1. [CLAIM-tmpet76z](../claims.d/CLAIM-tmpet76z.md): under gradient flow with a loss that depends on the
   parameters only through the embeddings, dL/dt = −‖Σ_j J_jᵀ g_j‖² ≤ 0,
   and K = JJᵀ is positive semidefinite at every θ.
2. The identity uses K only at the current instant. It contains no
   assumption that K is fixed.
3. So along any gradient-flow trajectory, with K co-evolving as it will,
   L is a Lyapunov function: the embeddings relax and carry no sustained
   current.
4. So the feedback loop between kernel and representation does not take
   the system from [CLAIM-tmp526xr](../claims.d/CLAIM-tmp526xr.md)'s weak reading to its strong one. A
   strong reading needs a source the identity excludes: momentum or an
   adaptive optimizer's memory, noise whose covariance is not matched to
   the mobility ([THEORY-209](../theory.d/THEORY-209.md)), or a time-dependent objective.

## Critical questions

- **Does the mapping premise hold?** The identity is stated for exactly
  A29 §2's equation, under A29's own condition ("when the relevant
  parameter dependence is through the specified embeddings"). The mapping
  is the identity map. It was checked numerically in this session for a
  random two-layer network ([CLAIM-tmpet76z](../claims.d/CLAIM-tmpet76z.md): agreement to 5 parts in 10¹¹).
- **Are the model's assumptions met in the new domain?** Not in practical
  training, and the conclusion is stated so as not to need them. Weight
  decay outside the embedding loss, momentum, Adam, minibatch noise and
  fresh negatives each break an assumption. The argument shows only that
  the loop is not, by itself, a source of activity; whether training as
  practised is active depends on those other terms, which is what
  [CLAIM-tmp526xr](../claims.d/CLAIM-tmp526xr.md)'s strong reading asks to have shown. A changing kernel
  could still matter to activity in combination with them, for instance by
  rotating the noise relative to the mobility; that is a property of the
  noise term, not of the loop.

## Verdict

[CLAIM-tmpet76z](../claims.d/CLAIM-tmpet76z.md) supports [CLAIM-tmp526xr](../claims.d/CLAIM-tmp526xr.md)'s split: the weak reading follows
from gradient flow with a co-evolving kernel, and the strong reading
cannot come from that co-evolution. Proposed.
