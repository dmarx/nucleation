---
status: Proposed
title: 'The withdrawal inquiry takes transient-support as its first line: QUESTION-398 and the entries that argue it lead with transient-support, and carry realizability only where they bear on a realizability-first entry, which completes the split of readiness'
version: 1
tags:
- record
date: '2026-11-11'
summary: >-
  [ADR-087](ADR-087.md) split readiness and moved its withdrawal part to the new line
  transient-support, keeping each entry's other lines where they were. Nine
  of the thirty had realizability first, [QUESTION-398](../questions.d/QUESTION-398.md), the part's root,
  among them. The synthesis review of 2026-11-11 found that part again
  inside realizability, mostly closed there too: its entries carry
  realizability chiefly because they bear on [QUESTION-398](../questions.d/QUESTION-398.md), whose first line
  it was ([ADR-085](ADR-085.md)). This decision gives [QUESTION-398](../questions.d/QUESTION-398.md) and the withdrawal
  entries transient-support as their first line, and keeps realizability on
  them only where [ADR-085](ADR-085.md) supplies it, through a relation to a
  realizability-first entry. Nineteen entries change. [CLAIM-597](../claims.d/CLAIM-597.md), [CLAIM-600](../claims.d/CLAIM-600.md),
  [CLAIM-604](../claims.d/CLAIM-604.md) and [CLAIM-606](../claims.d/CLAIM-606.md) keep realizability, because they bear on
  [QUESTION-399](../questions.d/QUESTION-399.md), the nucleus question, which stays in realizability.
  Rejected: leaving the first lines as [ADR-087](ADR-087.md) left them; moving [QUESTION-399](../questions.d/QUESTION-399.md)
  as well; keeping realizability on every moved entry.
---
<!-- inactive-ok-file: ADR-085 — Proposed; the line rule this applies -->
<!-- inactive-ok-file: CLAIM-606 — Proposed; entries moved, with their standing -->

# ADR-tmpqp8c4: The withdrawal inquiry takes transient-support as its first line: [QUESTION-398](../questions.d/QUESTION-398.md) and the entries that argue it lead with transient-support, and carry realizability only where they bear on a realizability-first entry, which completes the split of readiness

## Context

[ADR-087](ADR-087.md) split readiness in two. The withdrawal part, thirty entries filed on
A's [QUESTION-398](../questions.d/QUESTION-398.md) ("Under what conditions does a partial organization become
independent of the intervention that originally established it?"), became
the line transient-support. It moved each entry "in place", so an entry whose
first line was realizability kept it first. [ADR-087](ADR-087.md) also rejected moving the
part into realizability: whether support can be withdrawn without decline "is
a question of its own".

The synthesis review of 2026-11-11 drafted realizability's first account. It
found the same part inside realizability as one of five parts, mostly closed
by either count. Counting stored relations, it had 51 inside, 5 out and 2 in.
Most of its entries carried realizability for one reason: they bear on
[QUESTION-398](../questions.d/QUESTION-398.md), whose first line was realizability, and [ADR-085](ADR-085.md) gives an entry
the first line of a question it bears on. The root kept the withdrawal
inquiry inside realizability after the split meant to take it out.

## Decision

- **[QUESTION-398](../questions.d/QUESTION-398.md) takes transient-support as its first line.** It is the
  withdrawal inquiry's root question. It has no relation to a
  realizability-first entry, so it no longer carries realizability.
- **The entries of the withdrawal inquiry lead with transient-support.**
  These are the entries of the part that already carried transient-support,
  and [QUESTION-416](../questions.d/QUESTION-416.md) and [QUESTION-420](../questions.d/QUESTION-420.md). Those two are replication questions of
  the urban readings filed on [QUESTION-398](../questions.d/QUESTION-398.md), like their siblings already in
  transient-support.
- **They carry realizability only where [ADR-085](ADR-085.md) supplies it.** That means an
  answers, objects_to or bears_on relation to a realizability-first entry,
  or refines between questions. This is the standard the defect sweep of
  2026-11-11 applied when [CLAIM-555](../claims.d/CLAIM-555.md) dropped will-organization.
  - [CLAIM-597](../claims.d/CLAIM-597.md), [CLAIM-600](../claims.d/CLAIM-600.md), [CLAIM-604](../claims.d/CLAIM-604.md) and [CLAIM-606](../claims.d/CLAIM-606.md) keep it. Each bears on
    [QUESTION-399](../questions.d/QUESTION-399.md), "Under what conditions does a productive partial
    organization become a self-maintaining nucleus", which stays in
    realizability.
  - [CLAIM-604](../claims.d/CLAIM-604.md) and [CLAIM-606](../claims.d/CLAIM-606.md) gain transient-support, because they bear on
    [QUESTION-398](../questions.d/QUESTION-398.md).
  - The other fifteen drop realizability.
- **Each changed entry gets a history note naming the relation that gives or
  removes each line.** Nothing else changes.
- **Transient-support's account follows the move.** [SYNTHESIS-032](../syntheses.d/SYNTHESIS-032.md) integrates
  the four new members and gives every component's lines as they now stand
  (version 5).

## Alternatives considered

- **Leave the first lines as [ADR-087](ADR-087.md) left them.** This leaves transient-support's
  own root in realizability. Through [ADR-085](ADR-085.md), the withdrawal inquiry stays a
  closed part of realizability, and setting realizability aside would take it
  along.
- **Move [QUESTION-399](../questions.d/QUESTION-399.md) too.** [QUESTION-399](../questions.d/QUESTION-399.md) asks when a partial organization
  becomes a self-maintaining nucleus, which is a question about nucleation.
  It links to realizability's assembly part. It keeps realizability first, and
  the claims that bear on both questions carry both lines.
- **Keep realizability on every moved entry.** Then realizability's account
  must integrate fifteen entries that take no part in its argument, and the
  split would be undone in the line it was meant to leave.

## Consequences

- Realizability's account is drafted without the withdrawal part. The
  claims that bear on [QUESTION-399](../questions.d/QUESTION-399.md) stay in it.
- No `rests_on` step from a moved claim crosses lines: each claim it rests
  on shares a line with it.
- Rerunning [ADR-085](ADR-085.md)'s rule after the move finds no entry missing
  transient-support.
