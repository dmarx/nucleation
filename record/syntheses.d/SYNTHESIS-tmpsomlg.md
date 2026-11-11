---
status: Proposed
title: 'Forbidding self-grants does not stop an operator from amplifying its own authority under damped recursive delegation, one-hop allocation within an epoch makes authority exactly independent of an operator''s own grants and lets delegating to a nearer ally pay, and leave-one-out delegation keeps that independence beyond one hop without that guarantee'
version: 1
defeated_if: >-
  A component misstated or misattributed here; an in-force component of
  the delegation-accounting part of the formal-apparatus line left out
  without a reason given; or a link this account states that no component
  states. Its standing is its components': a component retired or demoted
  takes its clause with it, and nothing here holds the clause up.
tags:
- self-governance
- game-theory
- mathematics
date: '2026-11-11'
line:
- formal-apparatus
integrates:
- CLAIM-282
- CLAIM-375
- CLAIM-502
---
<!-- inactive-ok-file: ADR-075 CLAIM-285 SYNTHESIS-050 — Proposed; components, decisions and accounts cited with their standing -->
<!-- inactive-ok-file: TERM-053 — Superseded; cited as the entry of its time -->
<!-- inactive-ok-file: SYNTHESIS-tmpvz4mj — Proposed; cited with its standing -->

# SYNTHESIS-tmpsomlg: Forbidding self-grants does not stop an operator from amplifying its own authority under damped recursive delegation, one-hop allocation within an epoch makes authority exactly independent of an operator's own grants and lets delegating to a nearer ally pay, and leave-one-out delegation keeps that independence beyond one hop without that guarantee

*A part account of the formal-apparatus line: one of the line's eleven
small clusters, three entries first in distributed-agency, where
[SYNTHESIS-050](SYNTHESIS-050.md) integrates all three under counting grants. This account
integrates them again because their `line` includes formal-apparatus. The
line's account is built over it and its sibling parts.*

## The account

- **Cycle bans do not stop amplification.** [CLAIM-282](../claims.d/CLAIM-282.md) (A2's analysis of
  the owner's U2 design, conceded and checked; granted, demonstrated,
  Active, version 3): under damped recursive delegation, reciprocal and
  cyclic grants recycle authority, so an operator's authority depends on
  its own grants though none grants itself; one-hop allocation within an
  epoch, from budgets and baselines fixed independently of outgoing
  grants, makes it exactly independent of them. Its summary: "No
  accounting rule removes the slower route: an operator can change its
  authority by changing what others grant."
- **Delegating pays under one hop.** [CLAIM-375](../claims.d/CLAIM-375.md) (split from [CLAIM-285](../claims.d/CLAIM-285.md) at
  the owner's direction, carrying out the promotion audit; thesis,
  demonstrated, Active): under one-hop allocation, granting influence to
  an ally nearer one's policy than the authority-weighted decision moves
  the decision strictly toward one's policy while one's own authority
  stays fixed, so the two conditions of the grant scheme hold together.
  "They constrain different quantities."
- **Independence beyond one hop.** [CLAIM-502](../claims.d/CLAIM-502.md) (found by the eighteenth
  status review, re-derived and filed by the nineteenth; thesis,
  demonstrated, Active): leave-one-out damped delegation counts the
  authority reaching each operator only along paths that have not passed
  through it, so "an operator's authority can be independent of its own
  grants while a grant carries authority further than one hop". It
  conserves no total, leaves the social route open, and "[CLAIM-375](../claims.d/CLAIM-375.md)'s
  guarantee does not carry over": the decision moved toward the granter in
  1,772 of 2,141 trials.

## The components

- [CLAIM-282](../claims.d/CLAIM-282.md), A2's, granted, demonstrated, Active; first line
  distributed-agency; complements [CLAIM-277](../claims.d/CLAIM-277.md).
- [CLAIM-375](../claims.d/CLAIM-375.md), the promotion audit's split, thesis, demonstrated, Active;
  first line distributed-agency; rests on [CLAIM-282](../claims.d/CLAIM-282.md); complements
  [CLAIM-502](../claims.d/CLAIM-502.md); uses [TERM-103](../terms.d/TERM-103.md), [TERM-101](../terms.d/TERM-101.md) and [TERM-053](../terms.d/TERM-053.md).
- [CLAIM-502](../claims.d/CLAIM-502.md), the status reviews', thesis, demonstrated, Active; first
  line distributed-agency; objects to [CLAIM-282](../claims.d/CLAIM-282.md); complements [CLAIM-375](../claims.d/CLAIM-375.md);
  uses [TERM-103](../terms.d/TERM-103.md) and [TERM-101](../terms.d/TERM-101.md).

## Links the components state, and where

All three pairs are linked by relations:

- **The one-hop rule.** [CLAIM-375](../claims.d/CLAIM-375.md) rests on [CLAIM-282](../claims.d/CLAIM-282.md): its point 1 "is
  [CLAIM-282](../claims.d/CLAIM-282.md)'s one-hop case", and its "What it does not say" cites
  [CLAIM-282](../claims.d/CLAIM-282.md) for the failure under recursive delegation and for the social
  route.
- **The objection and the narrowing.** [CLAIM-502](../claims.d/CLAIM-502.md) objects to [CLAIM-282](../claims.d/CLAIM-282.md).
  [CLAIM-282](../claims.d/CLAIM-282.md)'s version 2 note: "[CLAIM-502](../claims.d/CLAIM-502.md) shows both clauses false", and
  its title now says only the damped recursive rule and the one-hop rule;
  its "What it does not say" names leave-one-out delegation. [CLAIM-502](../claims.d/CLAIM-502.md)
  says its rule may be one way to fix the open conventions of A2's
  path-based rule ([CLAIM-282](../claims.d/CLAIM-282.md)).
- **The guarantee.** [CLAIM-375](../claims.d/CLAIM-375.md) and [CLAIM-502](../claims.d/CLAIM-502.md) complement each other.
  [CLAIM-375](../claims.d/CLAIM-375.md) holds open whether some multi-hop rule keeps both conditions;
  [CLAIM-502](../claims.d/CLAIM-502.md) shows leave-one-out keeps the first and not, in general, the
  second.

## Links to other parts, stated

None. No member names a member of the line's other part accounts or of the entries the line account ([SYNTHESIS-tmpvz4mj](SYNTHESIS-tmpvz4mj.md)) integrates directly, and none of them names a member here. Outside the line, [CLAIM-285](../claims.d/CLAIM-285.md)
(Proposed) is the incentive thesis [CLAIM-375](../claims.d/CLAIM-375.md) was split from, and [CLAIM-277](../claims.d/CLAIM-277.md)
holds the social route as how durable trust arises.

## Where else these entries are integrated

[SYNTHESIS-050](SYNTHESIS-050.md) (distributed-agency's conferral part) integrates all three,
and its "Accounting" link records [CLAIM-502](../claims.d/CLAIM-502.md)'s objection to [CLAIM-282](../claims.d/CLAIM-282.md).

## Not stated on the record

Tested by [ADR-075](../decisions.d/ADR-075.md)'s step 5 at this review and not filed:

- **Only one-hop allocation, among the rules on record, keeps both
  conditions.** The rules on record are the damped recursive rule
  ([CLAIM-282](../claims.d/CLAIM-282.md): the first condition fails), one hop ([CLAIM-375](../claims.d/CLAIM-375.md): both hold)
  and leave-one-out ([CLAIM-502](../claims.d/CLAIM-502.md): the first holds, the second fails in some
  trials). As a statement about these three it is the components side by
  side; as a statement about every multi-hop rule it is what [CLAIM-375](../claims.d/CLAIM-375.md)
  holds open. Fails as adding nothing on record, and is open beyond it.

## What it does not say

- That operators delegate, or delegate well; [CLAIM-375](../claims.d/CLAIM-375.md) leaves that to
  [CLAIM-285](../claims.d/CLAIM-285.md).
- That any rule closes the social route of moving others' grants; all
  three disclaim it.
