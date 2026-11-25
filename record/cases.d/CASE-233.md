---
number: 233
status: Active
formerly:
- CASE-tmpwln61
title: 'A transition with a barrier: on configurations [0, 1] with a holding requirement r(q) = 0.7 + 2.4q(1 − q), both ends cost 0.7, every path between them passes 1.3 at q = 1/2, and at a budget of 1.0 the feasible set falls into two components, each end feasible and neither reachable from the other'
version: 3
history:
- version: 2
  date: '2026-11-18'
  note: >-
    Promoted at the status review's ruling (the owner delegated these
    rulings; ADR-057): a construction whose facts are its definition
    (ADR-042), re-derived step by step at the review. r(0) = r(1) = 0.7;
    q(1 − q) is at most 1/4, reached only at q = 1/2, so r peaks at 1.3
    there; every continuous path in [0, 1] from 0 to 1 passes 1/2 by the
    intermediate value theorem, and the straight path reaches no more, so
    the threshold is 1.3; r ≤ 1.0 is q(1 − q) ≤ 1/8, with roots
    (1 ± √½)/2, about 0.146447 and 0.853553, and between them r > 1.0,
    so the feasible set at 1.0 is two intervals, one holding each end;
    for any budget from 0.7 up to but not including 1.3 the same holds
    with the roots moving toward 1/2, and at 1.3 the set is all of [0, 1]; the slack is 0.6. Re-run
    independently with python3 -I (grid maximum 1.3 at q = 0.5; one gap
    in the feasible set at 1.0 on 100,001 points). This resolves the
    credence inversion of CLAIM-571, Active and grounded in this case.
    ADR-096, under which the case was filed, stays Proposed; the case's
    status is credence in the construction, not in that decision.
    Standing fictional is kept. The text is unchanged.
- version: 3
  date: '2026-11-25'
  note: >-
    Gains the line governing-possibility (atlas scope 14) under ADR-
    tmpd3ckn: the entry is in that scope's core fiber in the hyperarticle
    atlas v0.3 (scratch/atlas/atlas-v0.3.md), and each atlas scope is
    documented as a line. No other change.
standing: fictional
kind: construction
tags:
- mathematics
- operations-research
date: '2026-11-12'
line:
- realizability
- readiness
- governing-possibility
summary: >-
  [CLAIM-571](../claims.d/CLAIM-571.md)'s own construction, A's example from the pasted synthesis on
  resource-bounded realizability, checked there by the claim's filer and
  again here, filed as a case under [ADR-096](../decisions.d/ADR-096.md) as its first application.
  It grounds [CLAIM-571](../claims.d/CLAIM-571.md)'s clause that the threshold for reaching a
  configuration need not equal the configuration's requirement. [CASE-198](CASE-198.md)
  and [CASE-200](CASE-200.md) alter it. The wording of the case is the assistant's
  (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-198 CASE-200 — Proposed; the variants of this construction -->

# CASE-233: A transition with a barrier: on configurations [0, 1] with a holding requirement r(q) = 0.7 + 2.4q(1 − q), both ends cost 0.7, every path between them passes 1.3 at q = 1/2, and at a budget of 1.0 the feasible set falls into two components, each end feasible and neither reachable from the other

## The construction

Configurations Q = [0, 1]. Holding q needs r(q) = 0.7 + 2.4q(1 − q) of
one capacity that must be held at each moment. The admissible paths are
the continuous paths in [0, 1]. A = 0 and B = 1.

- **The ends are cheap**: r(0) = r(1) = 0.7.
- **The barrier**: every path from 0 to 1 passes q = 1/2, where
  r = 1.3, and the straight path reaches no more, so [CLAIM-571](../claims.d/CLAIM-571.md)'s
  threshold B*(0, 1) = 1.3.
- **At a budget of 1.0** the feasible set {q : r(q) ≤ 1.0} is
  q(1 − q) ≤ 1/8, that is [0, (1 − √½)/2] ∪ [(1 + √½)/2, 1], about
  [0, 0.1464] ∪ [0.8536, 1]. Both ends are feasible; they lie in
  different components; neither reaches the other.
- **The components merge at 1.3.** The reconfiguration slack,
  B* − max(r(0), r(1)), is 0.6 ([TERM-106](../terms.d/TERM-106.md)).

Checked on 2026-11-12 with `python3 -I`: r(0) = r(1) = 0.7; the maximum
on a grid of 10,001 points is 1.3, at q = 0.5; the roots of r = 1.0 are
0.146447 and 0.853553; and on a grid of 100,001 points the feasible set
at 1.0 has exactly one gap, between 0.14644 and 0.85356.

## What it shows

That the threshold for reaching a configuration can exceed what holding
either end requires, which is [CLAIM-571](../claims.d/CLAIM-571.md)'s "need not equal". It is the
example the readiness and realizability lines reuse: [CASE-198](CASE-198.md) lowers the
threshold to 1.0 by a staging architecture, and [CASE-200](CASE-200.md) reaches 1.3 on a
per-period budget of 1.0 by carry-over.

## What it cannot show

Anything about real configuration spaces; the requirement function is
stipulated. Nor the threshold's being infinite, the claim's other clause,
which needs no admissible path at all ([CLAIM-571](../claims.d/CLAIM-571.md) cites the split nappes
of an origami vertex for that).

## Provenance

A's example, from the pasted synthesis on resource-bounded realizability
(2026-11-05), as [CLAIM-571](../claims.d/CLAIM-571.md)'s body gives it.
