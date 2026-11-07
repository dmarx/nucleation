---
status: Proposed
title: 'Three perspectives whose majority preferences cycle, x over y, y over z and z over x: a chair who admits only the contests x against y and y against z gets an acyclic record with x on top and one dissenter in each admitted contest, though a majority prefers z to x, and admitting z against x restores the cycle'
version: 1
standing: stipulated
kind: construction
tags:
- game-theory
- self-governance
- mathematics
date: '2026-11-07'
line:
- distributed-agency
- organizational-affect
illustrates:
- CLAIM-448
summary: >-
  The reader's construction, from the second share of the exchange
  "Individuation, Possibility, and Disposition" (U26, 2026-11-07). A57
  says CLAIM-448 "shows" that a coherent decision record can be produced
  by selectively excluding dissent. CLAIM-448 is interpretive, and the
  model that would settle it is unbuilt. This is that model in its
  smallest case, and it makes the claim's existence half true. It does
  not test what real interventions do. Filed at the owner's direction.
  The wording is the assistant's (Claude, in this session); adopting it
  is the owner's call.
---

# CASE-tmp3l0hh: Three perspectives whose majority preferences cycle, x over y, y over z and z over x: a chair who admits only the contests x against y and y against z gets an acyclic record with x on top and one dissenter in each admitted contest, though a majority prefers z to x, and admitting z against x restores the cycle

## The case

An organization has three perspectives and three options. Their orders
are:

- P1: x, y, z;
- P2: y, z, x;
- P3: z, x, y.

Taken pairwise by majority, x beats y (P1, P3), y beats z (P1, P2) and z
beats x (P2, P3). The winning-move relation is a cycle, so no ordinal
potential describes it.

A chair, whose role is the organization's legibility regime (TERM-064),
admits only two contests to the record: x against y, and y against z.
The admitted relation is acyclic, with the order x, y, z. The record
names x as the outcome, and in each admitted contest one perspective
dissents: P2 against x over y, and P3 against y over z. Nothing in the
record shows that a majority prefers z to x. Admitting z against x,
through a channel the chair does not control, brings the cycle into the
record, and recorded conflict rises.

The check is `scratch/formal/agenda_cycle_check.py` (run with
`python3 -I`). It enumerates the orders of the three options and finds
none consistent with all three contests, and the order x, y, z for the
admitted two.

## What it shows

CLAIM-448's existence half: "an acyclic record, even a persistent
potential, can be the product of selective contestation, so observed
coherence is not evidence that the organization's perspectives are
integrated". Here the record is coherent, the perspectives are not
integrated, and the coherence is produced by which contests the regime
admits.

## What it does not show

- **Persistence.** A potential "even a persistent" one would need the
  regime to keep excluding the contest over time. The construction is a
  single round.
- **Real interventions.** CLAIM-448's prediction, that an intervention
  which improves legibility can raise recorded conflict, is shown only
  for this toy, in which admitting the excluded contest restores the
  cycle. Whether real organizations behave so is untested.
- **Intent.** The chair's selection could be deliberate or a fixed
  procedure. The construction does not separate the two.

## Connections

- The agenda effect is the social-choice result that an agenda-setter
  facing a majority cycle can fix the outcome by ordering or restricting
  pairwise votes. The case uses it as the mechanism of a legibility
  regime, not as a voting result.
- CLAIM-553, the owner's, is the individual-scale form: a perspective
  that does not intervene has not thereby endorsed, because observed
  intervention carries a legibility factor. Here a perspective whose
  contest is not admitted has not thereby agreed.
