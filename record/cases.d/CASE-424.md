---
number: 424
status: Proposed
formerly:
- CASE-tmp3xxqg
title: 'The Chubby planned outage'
statement: >-
  The global Chubby planned outage: services at Google added dependencies on
  the global instance of its lock service on the assumption that it would
  never go down, so its rare outages reached users, and SRE now holds it to
  meet but not significantly exceed its service level objective,
  synthesizing a controlled outage in any quarter in which true failures
  have not brought availability below target
version: 1
standing: documented
kind: specimen
tags:
- software-engineering
- society-and-governance
date: '2026-11-24'
line:
- dependence-and-domination
- readiness
illustrates:
- CLAIM-603
reported_in:
- LIT-3234
summary: >-
  A sidebar by Marc Alvidrez in the SRE book's chapter "Service Level
  Objectives" ([LIT-3234](../literature.d/LIT-3234.md)), which A34 §2 of the exchange "Memes,
  Contracts, and Systemic Normativity" (ChatGPT, 2026-11-24) names the
  "Priority case for filing". The facts are the book's, quoted from its
  web edition, checked on 2026-11-24; the reading in the last section is
  A's (ChatGPT, in the exchange "Memes, Contracts, and Systemic
  Normativity"); adopting it is the owner's call.
---

<!-- inactive-ok-file: ARG-257 CLAIM-603 CLAIM-1256 CLAIM-1343 LIT-3234 — Proposed, Deferred or new; filed or registered with the exchange 'Memes, Contracts, and Systemic Normativity', cited whatever their standing -->

# CASE-424: The Chubby planned outage

## The case

From the SRE book ([LIT-3234](../literature.d/LIT-3234.md)), checked against the web edition on
2026-11-24:

> Chubby [Bur06] is Google’s lock service for loosely coupled distributed
> systems. In the global case, we distribute Chubby instances such that
> each replica is in a different geographical region. Over time, we found
> that the failures of the global instance of Chubby consistently
> generated service outages, many of which were visible to end users. As
> it turns out, true global Chubby outages are so infrequent that service
> owners began to add dependencies to Chubby assuming that it would never
> go down. Its high reliability provided a false sense of security
> because the services could not function appropriately when Chubby was
> unavailable, however rarely that occurred.
>
> The solution to this Chubby scenario is interesting: SRE makes sure
> that global Chubby meets, but does not significantly exceed, its
> service level objective. In any given quarter, if a true failure has
> not dropped availability below the target, a controlled outage will be
> synthesized by intentionally taking down the system. In this way, we
> are able to flush out unreasonable dependencies on Chubby shortly after
> they are added.

The chapter's surrounding text names the general dynamic:
"over-reliance on the service, when users incorrectly believe that a
service will be more available than it actually is".

## The reading (A's)

A34 §2 tabulates it: "Declared specification | The published
reliability objective", "Realized regularity | Exceptional observed
availability", "Structural expectation | Dependent systems assume
uninterrupted availability", "Constitutive dependency | Interruption
defeats downstream capabilities", "Reflexive intervention | Controlled
disruption exposes the discrepancy". "The controlled outage is not simply
a test of Chubby. It is an intervention into the relationships that have
developed around Chubby."

## Bearing

It grounds [CLAIM-1256](../claims.d/CLAIM-1256.md), with [ARG-257](../arguments.d/ARG-257.md) saying how far. It
illustrates [CLAIM-603](../claims.d/CLAIM-603.md): the dependents lost a capability, tolerance of
Chubby's absence, because Chubby reliably supplied what made it
unneeded, and the supply was one-way and set from outside, [CLAIM-603](../claims.d/CLAIM-603.md)'s
condition for dependence rather than division of labour. A36 §5 uses the
case again for constitutional conventions ([CLAIM-1343](../claims.d/CLAIM-1343.md)).
