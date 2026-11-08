---
number: 338
status: Proposed
formerly:
- CLAIM-tmpj10k0
title: 'The selectivity active inference gives action, sampling what one expects to experience, is played in the coupled meaning–authority model by the authority space: influence decides which operators retrieve and so what the next judgement observes, which makes Friston''s self-confirming sampling the model''s authority-to-interpretation arrow and his agent a coupled loop run without independent scoring'
version: 5
history:
- version: 2
  date: '2026-10-21'
  note: >-
    Note of 2026-10-21 added, from the exchange of 2026-10-20 on effective
    description, agency and legibility: A22's "which facts become legible
    enough to count as evidence" is this claim's authority arrow stated for
    institutions; whether it is a new channel is QUESTION-253. The
    claim is unchanged.
- version: 3
  date: '2026-11-04'
  note: >-
    Vocabulary only, under ADR-070: "endorse" in TERM-053's sense now
    reads conferral (TERM-103) or grant (TERM-101). The
    content is unchanged.
- version: 4
  date: '2026-11-07'
  note: >-
    CLAIM-336, which this claim rests on, moved into the SYNTHESIS scheme as
    SYNTHESIS-011 at the synthesis review of 2026-11-07; `rests_on` now
    names the synthesis (ADR-080). No other change.
- version: 5
  date: '2026-11-08'
  note: >-
    The syntheses this pointed at returned to CLAIM at the decision that
    a SYNTHESIS is an account (ADR-084), so `rests_on` names
    CLAIM-336 for SYNTHESIS-011. No other change.
role: thesis
warrant: interpretive
defeated_if: >-
  A showing that the selectivity of active-inference sampling cannot be
  represented as an allocation of influence among operators without the
  world-state variable that action changes: that what selective sampling
  does depends on the world being changed, and retrieval from an
  agent's own store cannot reproduce it, for example because only
  changed hidden states can deliver the perturbations that action then
  explains away. Not defeated by the difference in where the sampling
  acts, which is what the mapping relocates.
tags:
- cognition
- probabilistic-modeling
- agency
date: '2026-10-17'
line:
- distributed-agency
- pragmatic-transport
rests_on:
- CLAIM-297
- CLAIM-336
grounds:
- LIT-1181
- CASE-099
complements:
- CLAIM-341
- CLAIM-342
summary: >-
  The owner's, U10 of the exchange of 2026-10-16, on Friston et al.'s
  "sampling selectively what one expects to experience": "I think this
  selectivity maps to the authority space in my coupled model." Worked
  out by A10. Selective sampling is the β arrow of [CASE-099](../cases.d/CASE-099.md), authority
  shaping interpretation through what it retrieves. Policies scored on
  current beliefs are the γ arrow. So Friston's agent runs both arrows,
  and his "this weakness becomes the strength" accepts capture, with the
  anchor moved outside the loop to selection on whole agents. The sharp
  edge: the mapping relocates sampling from the world to retrieval, which
  is [CLAIM-337](CLAIM-337.md)'s move reversed, and it holds only if the agent's own
  store can surprise it as the world can.
---
<!-- inactive-ok-file: SYNTHESIS-011 ADR-080 CLAIM-336 — Proposed or Superseded; the synthesis this claim rests on, the decision that let it, and the claim it was -->
<!-- inactive-ok-file: TERM-053 — Superseded by ADR-070 (conferral, TERM-103; grant, TERM-101); cited as the term of its time -->

# CLAIM-338: The selectivity active inference gives action, sampling what one expects to experience, is played in the coupled meaning–authority model by the authority space: influence decides which operators retrieve and so what the next judgement observes, which makes Friston's self-confirming sampling the model's authority-to-interpretation arrow and his agent a coupled loop run without independent scoring

## The claim

The owner, at U10, on Friston et al.'s description of action as "sampling
selectively what one expects to experience" ([LIT-1181](../literature.d/LIT-1181.md), [NOTE-960](../notes.d/NOTE-960.md)):
"I think this selectivity maps to the authority space in my coupled model."

In [CLAIM-297](CLAIM-297.md)'s circuit, frame → retrieval → interpretation → grant →
future retrieval policy, influence w decides which operators act, the
operators that act decide what is retrieved, and what is retrieved is what
the next judgement observes. The current allocation of influence selects
the evidence. In [CASE-099](../cases.d/CASE-099.md)'s two-hypothesis linearization:

- **Selective sampling is the β arrow.** The specialist with authority
  retrieves evidence for its own hypothesis, and so moves the meaning
  toward it. In Friston et al., action samples the data the agent
  expects, and unexpected perturbations are "explained away by action and
  not perceived".
- **Policy selection on current beliefs is the γ arrow.** Active inference
  scores policies by expected free energy, computed under the agent's
  current beliefs, so the prevailing interpretation decides which policy,
  and so which sampling, gets authority.

The model's γ is the coupling from interpretation to grants. It is
not active inference's γ, the precision over policies, which in this
mapping sits on the authority side.

With both arrows present, [CASE-099](../cases.d/CASE-099.md) says the symmetric state is captured
once βγ > (1 − α)(1 − δ). Friston et al. see the self-confirmation and
accept it: "this weakness becomes the strength". Their anchor is outside
the loop, in selection on whole agents: "agents who do not have the right
priors cannot exist". In the model's terms, the free-energy agent is a
coupled loop run without independent scoring (no Regime B, [CLAIM-330](CLAIM-330.md)),
whose errors are corrected only by the removal of organizations that get
them wrong.

## What it adds to the thesis

- **The selecting work Friston gives action is done inside the model.** It
  is done by allocating authority among operators, with no action on the
  world. This is [CLAIM-341](CLAIM-341.md)'s thesis at the place where active
  inference is most explicit about why action matters.
- **The anchor question moves.** If selective sampling is authority, then
  what anchors a mind is whatever scores its operators independently of
  the interpretation they serve ([CLAIM-342](CLAIM-342.md), [QUESTION-121](../questions.d/QUESTION-121.md)).
  Friston's answer is selection across agents, which is not available
  within one.
- **Active inference is the commitment regime of [CLAIM-340](CLAIM-340.md).**
  Predictions are made before the sensations they are scored against.
  [CLAIM-340](CLAIM-340.md) says this protects against capture only when the
  interpretation bends the reading of the evidence no more than it bends
  the predictions. Friston's selective sampling bends what arrives.

## What it does not say

- It does not show that action and retrieval are the same. Action changes
  hidden states of the world, which can then deliver what the agent did
  not expect. Retrieval draws from the agent's own store. The mapping
  needs the store to play the world's part: to hold distinctions that a
  query can reach and that the current interpretation did not put there
  ([CLAIM-298](CLAIM-298.md)). Whether it can is the claim's open point, and its
  defeater.
- It is [CLAIM-337](CLAIM-337.md)'s move run in the other direction. That counter
  says the judgement loop is action and perception one blanket inward.
  This claim says active inference's sampling is authority one blanket
  outward. Both say the two are formally alike. They disagree about which
  description is primary.
- Friston et al. do not use the word authority, and the mapping is not
  theirs.

## Note of 2026-10-21: which facts become legible as evidence

A22 of the exchange of 2026-10-20: "Authority can affect not merely how
evidence is interpreted, but which facts become legible enough to count as
evidence at all". That is this claim's authority arrow (influence decides
what the next judgement observes), stated for institutions, with the
categories and reporting requirements an institution keeps in place of
retrieval. Whether that is a new channel or [CLAIM-340](CLAIM-340.md)'s κ′ is
[QUESTION-253](../questions.d/QUESTION-253.md). The term is filed as [TERM-064](../terms.d/TERM-064.md).
