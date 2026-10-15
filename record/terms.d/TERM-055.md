---
number: 55
status: Active
formerly:
- TERM-tmp5f7cu
title: 'operational availability, of a resource for an action: the chance that an
  agent–environment system, given the cue it actually has, deploys the resource
  for the task before the deadline'
version: 1
tags:
- agency
- cognition
date: '2026-10-15'
line: distributed-agency
summary: >-
  A17 §3's α, with A19's cue added. Named because the exchange used it in five turns
  (A16 to A19, and A23 §II) under "available", "accessible" and "deployable". The
  term separates the deployability of a resource from its presence and from knowing
  it is present ([CLAIM-296](../claims.d/CLAIM-296.md)).
used_by:
- CLAIM-296
---
<!-- inactive-ok-file: LIT-1065 — Deferred; works registered unread, cited for what they would be read for, not leaned on -->
<!-- inactive-ok-file: CLAIM-199 CLAIM-296 — Proposed; open claims and accounts cited as open, nothing here rests on their being settled -->

# TERM-055: operational availability, of a resource for an action: the chance that an agent–environment system, given the cue it actually has, deploys the resource for the task before the deadline

## Definition

A17 §3: α_{q,τ}(x; a, e) = sup over procedures π available to agent a in
environment e of P(retrieval of x under π takes at most τ, and π
succeeds), for task q and deadline τ. A19 §4 added the cue actually
supplied, q: α(x | q, M, a, e, τ), the probability of deploying x by τ given
the request as made and the memory M as held. A23 §II.C uses that form.

Five things it is not, from A17 §1: physical presence; knowing that the
resource is present; knowing where it is; deploying it in time (this
term); and its still serving the purpose, since a resource deployed in
time can be the wrong one.

## What it must not be confused with

- **Usable information** ([CLAIM-199](../claims.d/CLAIM-199.md)), which is about what a receiver's
  rules can extract from a rendering. This is about acting, and includes
  the time the extraction takes.
- **Affordance** (Gibson, [LIT-1065](../literature.d/LIT-1065.md), unread). A17: an affordance exists whether
  or not it is perceived; this is the chance it is realized in time.
- **Existence.** The medic's "If I can't find it, it isn't there" is
  α ≈ 0 read as absence. A16: "literally false as a claim about inventory,
  but potentially correct as an operational equivalence."

## Note of 2026-10-15: retrieval done before the request

Hutchins's cockpit study ([LIT-1066](../literature.d/LIT-1066.md), read in [NOTE-867](../notes.d/NOTE-867.md)) shows a
factor this definition does not carry. The crew computes approach speeds
25–30 minutes before landing, at low workload, and sets bugs on the
airspeed indicators; when the speeds are needed, reading them is "a
judgment of spatial adjacency". The environment supplies the cue (the
displayed weight selects the card; the needle nearing a bug), and the
work of retrieval is moved ahead of the deadline. α as defined starts the
clock at the request. A system can raise α by doing retrieval earlier and
leaving its result in the world, which the definition counts only through
the environment term e. That is worth making explicit if the term is
revised. The study is a task analysis, with no measurements and no
failures, for an anticipated and invariant task, not a search for one item
under a deadline as in [CASE-085](../cases.d/CASE-085.md).

## Note of 2026-10-15: the procedure chosen is not the best one

α takes the supremum over the procedures available. Gray and Fu
([LIT-1058](../literature.d/LIT-1058.md), read in [NOTE-864](../notes.d/NOTE-864.md)) show that people do not pick the best
procedure: they pick the cheapest, and a few hundred milliseconds of
extra access cost was enough to shift them from perfect information on a
display to memory. Realized deployment can therefore fall below α, as in
[CASE-085](../cases.d/CASE-085.md), where recall was tried before search.

