---
status: Proposed
title: 'A shared record can represent who contributed a proposition and what standing the record gives it, but not what any collaborator believes or that all of them know the current standing: access to the record is a precondition of coordinating on it, not evidence that they have'
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  A record of this kind that does fix its collaborators' states: a
  mechanism by which writing or accepting an entry guarantees that each
  collaborator holds the corresponding belief, or that every collaborator
  has read the current standing and knows the others have, under the
  asynchronous, unacknowledged reading such a record allows. Also defeated
  if it only restates CLAIM-346's epistemic-coordination obstruction with
  nothing added about records. Not defeated by a protocol of
  acknowledgements added to the record: that is a second mechanism, and
  the claim is about what the record represents by itself.
tags:
- epistemology
- social-ontology
- agency
date: '2026-11-12'
line:
- record-as-apparatus
- distributed-agency
rests_on:
- CLAIM-346
grounds:
- THEORY-tmp4cr0g
uses:
- TERM-tmp8deza
bears_on:
- QUESTION-tmpxq2sb
summary: >-
  A's, at A32 §1 of the exchange "luria experiment design" (2026-11-10),
  developing its phrase "shared epistemic state" at the owner's request
  (U13). Of four statements about a hypothesis, "Agent A believes H",
  "Agent A has proposed H", "The record currently endorses H" and
  "Everyone knows that the record endorses H", A says "Luria can help
  represent the middle two. It cannot automatically establish the first or
  fourth", and "publishing a record does not establish common knowledge".
  A45 §9 keeps it as an exclusion from the experimental program. It rests
  on [CLAIM-346](CLAIM-346.md), whose third obstruction is epistemic coordination, and
  [ARG-tmpbuocw](../arguments.d/ARG-tmpbuocw.md) argues that Halpern and Moses's result reaches a record
  read asynchronously. The wording is A's; adopting it is the owner's
  call.
---
<!-- inactive-ok-file: TERM-tmp8deza ARG-tmpbuocw THEORY-tmp4cr0g — filed from the same exchange, Proposed -->

# CLAIM-tmpyp3u3: A shared record can represent who contributed a proposition and what standing the record gives it, but not what any collaborator believes or that all of them know the current standing: access to the record is a precondition of coordinating on it, not evidence that they have

## The claim

From A32 §1 of the exchange "luria experiment design"
(https://chatgpt.com/share/6af35bfc-35f8-83e9-a63d-d594703eabda). A sets
four statements about a hypothesis H apart:

| Statement | What it is about | Can the record represent it? |
|---|---|---|
| A believes H | a collaborator's state | no |
| A has proposed H | a contribution and its voice | yes: an entry, its author, its role |
| the record endorses H | the record's standing judgement | yes: a status under a scheme |
| everyone knows the record endorses H | synchronization of all collaborators | no |

The record holds the second and third as entries and fields. The first is
a fact about an agent, which the record can report only as the agent's own
contribution. The fourth is a fact about every collaborator's reading of
the record and about their knowledge of one another's readings. A32: "An
agent could have an outdated checkout, miss a notification, misunderstand a
status, or fail to inspect a relevant objection. Accessibility is a
precondition for coordination, not proof of successful coordination."

So a claim that a team coordinated through a shared record has two parts
to show: that the record held the right standing, and that the
collaborators acted on it. The second is not read off the first. A32's
consequence for any evaluation: "the test should ask whether agents
actually converge on a correct understanding of the shared record, not
simply whether correct information was available somewhere", measured as
the fraction of agents who misread the standing, provenance or bearing of
an entry after a shared update.

## Why the fourth cannot be had

[CLAIM-346](CLAIM-346.md) holds epistemic coordination as an obstruction of its own,
constructed with the coordinated-attack problem: a feasible, preferred
joint action can fail because the agents cannot know that they know.
Halpern and Moses ([LIT-1213](../literature.d/LIT-1213.md), read in [NOTE-1381](../notes.d/NOTE-1381.md); [THEORY-tmp4cr0g](../theory.d/THEORY-tmp4cr0g.md)) show
that common knowledge cannot be gained over a channel whose deliveries are
not guaranteed (Theorem 5), nor over one that delivers every message but
at uncertain times (Theorem 8). A record read asynchronously, from
checkouts that may be stale, with no acknowledgement of who has read what,
is such a channel for its standing ([ARG-tmpbuocw](../arguments.d/ARG-tmpbuocw.md)). Publishing the standing
therefore makes it available, not commonly known.

## What it does not say

- Not that the record is useless for coordination. Much coordination needs
  less than common knowledge, and [NOTE-1381](../notes.d/NOTE-1381.md) records that timestamped
  common knowledge, with clocks every collaborator shares, gives the
  eventual form (Theorem 12, unchecked there). The claim is about what the record
  represents, not about what suffices.
- Not that the record represents nothing about belief. An entry's author
  and role say who put a proposition forward and in what voice. That is a
  fact about a contribution ([TERM-tmp8deza](../terms.d/TERM-tmp8deza.md)), not about a mind.
- Not about this record's owner and assistants specifically. The same
  holds for any collaborators who read a shared record on their own
  schedule.
