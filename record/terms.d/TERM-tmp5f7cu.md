---
status: Active
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
  it is present ([CLAIM-tmp9gt89](../claims.d/CLAIM-tmp9gt89.md)).
used_by:
- CLAIM-tmp9gt89
---
<!-- inactive-ok-file: LIT-tmpl2mgd — Deferred; works registered unread, cited for what they would be read for, not leaned on -->
<!-- inactive-ok-file: CLAIM-199 CLAIM-tmp9gt89 — Proposed; open claims and accounts cited as open, nothing here rests on their being settled -->

# TERM-tmp5f7cu: operational availability, of a resource for an action: the chance that an agent–environment system, given the cue it actually has, deploys the resource for the task before the deadline

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
- **Affordance** (Gibson, [LIT-tmpl2mgd](../literature.d/LIT-tmpl2mgd.md), unread). A17: an affordance exists whether
  or not it is perceived; this is the chance it is realized in time.
- **Existence.** The medic's "If I can't find it, it isn't there" is
  α ≈ 0 read as absence. A16: "literally false as a claim about inventory,
  but potentially correct as an operational equivalence."
