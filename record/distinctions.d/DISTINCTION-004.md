---
number: 4
status: Proposed
formerly:
- DISTINCTION-tmpvz9hk
title: "Goal-conduciveness valence is not an outcome's pull"
between:
- TERM-076
- TERM-188
rests_on:
- CLAIM-1366
bears_on:
- QUESTION-544
statement: >-
  Goal-conduciveness valence (TERM-076) and outcome valence (TERM-188)
  are distinct: the first is a signed position of the system along the
  ordering its negotiation's wins climb, and the second is a probability
  over the outcomes the system's movement ends in
criterion: >-
  Goal-conduciveness valence is a property of the system's position, signed
  against a reference course, and exists only where the wins admit an
  ordinal potential; outcome valence is a property of an outcome, a pull
  directed at the system, and exists for any terminal component of the
  winning dynamics, cyclic or not
tells_apart: >-
  A terminal cycle in the winning dynamics. On it the wins admit no
  potential, so goal-conduciveness valence has no sign, while the cycle's
  outcome valence is its basin probability, 0.5 or 0.8 in
  scratch/studies/lead-314/indecision.py depending on the starts.
  Where the wins are acyclic the two can still diverge: a high-pull outcome
  can sit low on the potential if the potential's sink has a small basin
defeated_if: >-
  A showing that in the record's model the two are one quantity, for
  example that basin probability is a monotone function of position along
  the potential wherever a potential exists and that the cyclic case is
  excluded by the model's assumptions; or a showing that no observation of
  an organization separates a system's sign of position from the pull of
  the outcomes it ends in.
version: 1
tags:
- emotion-and-affect
- motivation
date: '2026-11-26'
line:
- organizational-affect
summary: >-
  The first DISTINCTION, filed as the demonstration of the decision adding
  the scheme ([ADR-153](../decisions.d/ADR-153.md)). It binds the two senses of "valence" that
  [CLAIM-1413](../claims.d/CLAIM-1413.md) separates in prose, and says what tells them apart: a
  terminal cycle, computed. The owner asked for the scheme on 2026-11-26 so
  that operationalization can be mapped to theory. The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: TERM-076 TERM-188 CLAIM-1366 CLAIM-1413 ADR-153 — Proposed or new; the terms bound, the result the observation rests on, the claim that uses the distinction, the open question, and the decision -->

# DISTINCTION-004: Goal-conduciveness valence is not an outcome's pull

## The sides

- **Goal-conduciveness valence** ([TERM-076](../terms.d/TERM-076.md)). The negotiation among a
  system's perspectives has, approximately, a potential, and the system's
  valence is signed by whether it runs ahead of or behind a reference
  course along it. A property of the system's position.
- **Outcome valence** ([TERM-188](../terms.d/TERM-188.md)). The pull an outcome exerts on the
  system's movement, in Lewin's sense as the record expects it. A property
  of the outcome.

## Telling them apart

| | Goal-conduciveness valence | Outcome valence |
|---|---|---|
| Operationalized as | sign of position along the ordinal potential of the recorded wins ([CLAIM-434](../claims.d/CLAIM-434.md)) | basin probability of a terminal component of the condensation ([CLAIM-1366](../claims.d/CLAIM-1366.md)) |
| Exists when | the wins are acyclic | always, for every terminal component |
| On a terminal cycle | no sign | 0.5 or 0.8 (indecision.py) |

The terminal cycle is the observation that separates them, and it is
computed, not found. A documented organization with one would make it a
CASE, to be named in `witnessed_by`.

## What it does not say

Which sense "valence" should name in the record. That is
[CLAIM-1413](../claims.d/CLAIM-1413.md)'s question, and the owner's. Nor that either is affect
([QUESTION-544](../questions.d/QUESTION-544.md)). Nor whether the owner's direction-of-predisposition
sense ([CLAIM-1386](../claims.d/CLAIM-1386.md)) is outcome valence or a third sense; if a third,
it needs its own TERM and a distinction from each.
