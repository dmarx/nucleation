---
status: Open
title: 'Under what conditions can organizational constraint architectures be synthesized from a specified family of desired, jointly realizable capabilities?'
version: 1
tags:
- society-and-governance
- operations-research
- mathematics
date: '2026-11-05'
line:
- distributed-agency
summary: >-
  A's proposal, from the pasted synthesis on constraint architectures
  (pasted by the owner on 2026-11-04, continuing the exchange on emergency
  readiness whose share link could not be fetched), Part 1. FACT is a
  synthesis procedure for flexures: specify the motions, read off the
  constraint spaces that give them. The question is whether anything like
  it exists for organizations, and under what conditions. A's form of the
  design problem: min Cost(O,π) s.t. R(O,π,c) ≥ 1−ε_c for every required
  context c. Even in mechanics the procedure has limits, which bound what
  an answer could look like. No held question asks it. The wording is
  A's; adopting it is the owner's call.
---
<!-- inactive-ok-file: NOTE-tmpla9de — Skimmed; Hopkins's 2007 thesis, the reading the quotations come from -->
<!-- inactive-ok-file: THEORY-tmpmbmox THEORY-tmpybouv TERM-tmpuc919 — Proposed; the readings' accounts and A's proposals of 2026-11-04, cited as filed -->

# QUESTION-tmpa16u7: Under what conditions can organizational constraint architectures be synthesized from a specified family of desired, jointly realizable capabilities?

## Why it is a question

FACT turns design around. Hopkins's 2007 thesis ([NOTE-tmpla9de](../notes.d/NOTE-tmpla9de.md);
[THEORY-tmpmbmox](../theory.d/THEORY-tmpmbmox.md)) gives a designer who has specified the motions a stage must
permit the constraint spaces that permit them, and which constraints
within those spaces add stiffness without changing the motions. A asks
whether an organization's constraint architecture could be synthesized
the same way, from the capabilities it must have. A's design problem:

  min Cost(O,π) s.t. R(O,π,c) ≥ 1−ε_c for every required context c,

with R the readiness for context c ([TERM-tmpuc919](../terms.d/TERM-tmpuc919.md)). Topology optimization
of compliant mechanisms is a second mechanical precedent, in A's form
inverse design, min_G C(G) subject to the demands lying in K(G), (Krishnakumar and
Suresh, [THEORY-tmpybouv](../theory.d/THEORY-tmpybouv.md)).

That the capabilities be jointly realizable is a precondition, and the
record has a word for it:
the family must be a face of the compatibility complex of some
architecture ([CLAIM-347](../claims.d/CLAIM-347.md)). A family that no admissible architecture realizes
jointly is frustrated in [TERM-060](../terms.d/TERM-060.md)'s structural sense, and no synthesis
procedure can return it.

Even in mechanics, specifying what is wanted does not always fix a
design that gives only that. Hopkins 2007: "Instances exist in which some
desired degrees of freedom may not be achieved without including other
unwanted degrees of freedom." And FACT's 26 matching pairs hold only for
ideal pure-force constraints.

## What would answer it

Conditions on the family of capabilities and on a declared class of
organizational architectures under which a procedure returns an
architecture realizing every capability in the family, and does not
return one that realizes unwanted ones; or a proof that, for a given
class, no such procedure exists. A duality like FACT's between what an
organization may do and what constrains it would be one route
([QUESTION-tmphk9w2](QUESTION-tmphk9w2.md) asks what of that duality survives outside mechanics).

## What would not answer it

A single architecture that happens to realize one family; or a procedure
that realizes the capabilities by also realizing others it does not
report.
