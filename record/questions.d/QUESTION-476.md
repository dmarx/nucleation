---
number: 476
status: Open
formerly:
- QUESTION-tmp2t6ve
title: 'Does blameless post-incident practice in engineering keep accountability while giving up blame, and if it does, does it keep or lose the upstream provenance of an incapacity that blame supplies?'
version: 1
tags:
- society-and-governance
- ethics
- software-engineering
date: '2026-11-17'
line:
- organizational-normativity
- distributed-agency
refines:
- QUESTION-470
summary: >-
  The owner's, from U48 of the exchange "Assess Depp Heard Abuse"
  (2026-11-17), its last turn: ""blameless culture" in modern
  engineering could be an interesting case for analysis here". The
  exchange ends there; A never answered, and no work was named. The
  question puts the owner's suggestion to the two claims of the owner's
  U47 it bears on: that accountability is not blame ([CLAIM-742](../claims.d/CLAIM-742.md)) and
  that blame supplies provenance for holding upstream actors accountable
  ([CLAIM-733](../claims.d/CLAIM-733.md)). The suggestion is the owner's; the wording of the
  question is the filer's (Claude, in this session), and adopting it is
  the owner's call.
---
<!-- inactive-ok-file: CLAIM-707 — Proposed or Open; filed from the first share of the same exchange (PR 510) and reconciled with this filing on 2026-11-18 -->
<!-- inactive-ok-file: CLAIM-717 CLAIM-733 CLAIM-742 TERM-127 — filed from the exchange "Assess Depp Heard Abuse" (2026-11-17), new and Proposed -->
<!-- inactive-ok-file: THEORY-144 — Proposed; the record's nearest entries, cited with their standing -->

# QUESTION-476: Does blameless post-incident practice in engineering keep accountability while giving up blame, and if it does, does it keep or lose the upstream provenance of an incapacity that blame supplies?

## Why it is a question

The owner's U48, the last turn of the exchange "Assess Depp Heard Abuse"
(https://chatgpt.com/share/6afcb46d-83a8-83e9-9c85-4a0c3604405b), 2026-11-17:

> "blameless culture" in modern engineering could be an interesting case for analysis here

**The exchange ends here, with no answer.** No assistant turn follows U48,
no source is named, and nothing in the exchange discusses blameless
culture, post-incident review or "just culture" before it. The question is
therefore the owner's prompt, put in the terms of the owner's U47, the turn
it answers to:

- **Accountability without blame** ([CLAIM-742](../claims.d/CLAIM-742.md)). The owner: "perhaps
  "blame" and "accountability" aren't the same thing." A blameless
  review is, on its face, a practice that keeps correction (find what
  failed, repair it, prevent recurrence) while withholding blame from the
  people involved. If it works, it is a real instance of correction whose
  grounds are not those of blame.
- **Blame as provenance** ([CLAIM-733](../claims.d/CLAIM-733.md)). The owner: ""blame" gives us
  provenance for holding upstream actors accountable as well." A practice
  that refuses to blame anyone may also stop tracing whose decisions
  produced the conditions of the failure. Or it may trace them better,
  because people report what happened when they are not punished for it.
  Which of these happens is the open part.

## What would count as an answer

- **Keeps correction and provenance:** a documented practice in which
  reviews without individual blame still trace contributing decisions
  upstream (who set the staffing, the deadline, the tooling, the review
  procedure) and lead to repair there. That would show the owner's two
  claims separable in practice: provenance without blame.
- **Keeps correction, loses provenance:** evidence that blameless reviews
  stop at the system as an impersonal cause, so that decisions by those who
  govern the system escape the account. That would be the failure A110 §8
  calls "blame displacement" turned round: no one is blamed, and the
  conditions some actors set are not repaired ([CLAIM-717](../claims.d/CLAIM-717.md)).
- **Neither:** evidence that "blameless" in practice relocates blame, for
  example to the person who did not follow the process, so that it is not
  an instance of accountability without blame at all.

## Sources, not from the exchange

The exchange names none. Candidate sources, offered by the lead filer and
not by the exchange, for whoever takes this up: John Allspaw's "Blameless
PostMortems and a Just Culture" (Etsy Code as Craft, 2012); Sidney Dekker's
*Just Culture*; and the chapter "Postmortem Culture" in Google's *Site
Reliability Engineering*. None is registered on the record, and none is
cited here as evidence.

## How it sits with the record

Nothing on the record holds blameless culture, post-incident review or just
culture. The nearest held material is in safety science: [THEORY-144](../theory.d/THEORY-144.md)
(Rasmussen's drift toward the boundary of acceptable performance, whose body
says it does not claim "that individuals are blameless"), and [CASE-151](../cases.d/CASE-151.md)
(Wells Fargo, where leadership blamed and disciplined individual employees
for what the board's investigation traced to the sales model), a case of
the opposite practice. From the same exchange, A17 §1's moral crumple
zone, the person nearest the failure absorbing the blame, is filed as
[CLAIM-707](../claims.d/CLAIM-707.md); A17 §9 had already said that "A person can be required to
explain their decisions and participate in correcting a failure without
necessarily being morally culpable for everything that happened", and
that an institution should "examine system failures without automatically
identifying the nearest human as their sufficient explanation". That is
the closest the exchange came to the owner's case before U48. The
responsibility senses at issue are [TERM-127](../terms.d/TERM-127.md)'s.

[QUESTION-470](QUESTION-470.md), from the first share of the same exchange, asks when an
organization's responsibility to repair a harm survives the absence or
dispersion of blameworthiness. This question refines it for one practice:
blameless post-incident review is an organization's attempt to keep
accountability and repair while setting blame aside, and whether it keeps
the upstream provenance blame supplies is a part of that question.
