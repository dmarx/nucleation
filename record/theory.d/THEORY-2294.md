---
number: 2294
status: Active
formerly:
- THEORY-tmpm653d
title: 'Rogers, Suriar, Lueder, Deo and Sudhakar present Google''s blameless postmortem as aimed at what failed and not who, with action items that improve systems rather than people, kept blameless by leaders who recast blameful questions, to managers and from executives, as questions about process, while questions about priorities set above the team are left to reviews of repeated incidents'
version: 2
history:
- version: 2
  date: '2026-11-23'
  note: >-
    Promoted to Active at the status review's ruling (the owner delegated
    these rulings; ADR-057) and ADR-065: the title reports what the
    chapter presents, read in full (NOTE-2391), and nothing in the
    record contradicts it. The old condition moves with the wider thesis
    to THEORY-2302 (ADR-047 kind 1). Old condition: "A second reading
    of the chapter, or another of Google's published statements of its
    postmortem practice, confirms three things: that a blameless
    postmortem's causes focus on "what" and not "who" and its action items
    aim at improving systems rather than people; that leaders are to keep
    it blameless by recasting blameful questions, including questions to
    managers and from executives, as questions about process; and that
    questions about priorities set above a team (whether feature velocity
    trumps reliability) are raised in the review of repeated incidents
    rather than in the single postmortem. Whether the practice achieves
    its aims is not asserted."
tags:
- software-engineering
- society-and-governance
date: '2026-11-22'
source:
- LIT-3187
bears_on:
- QUESTION-476
corroborates:
- CLAIM-742
- CLAIM-750
summary: >-
  Rogers, Suriar, Lueder, Deo and Sudhakar (2018), [LIT-3187](../literature.d/LIT-3187.md), read in
  [NOTE-2391](../notes.d/NOTE-2391.md). Google's practical account of postmortem culture, with a
  real postmortem shown whole. It bears on [QUESTION-476](../questions.d/QUESTION-476.md) on both halves. It
  corroborates [CLAIM-742](../claims.d/CLAIM-742.md), since "Declaring official ownership results in
  accountability, which leads to action" separates accountability from
  blame in the practice's own words. It corroborates the mechanism of
  [CLAIM-750](../claims.d/CLAIM-750.md), not its prediction: the norm that forbids indicting a team
  also recasts a question to a manager as a question about process. It
  also supplies an objection to how [CLAIM-750](../claims.d/CLAIM-750.md) is tested ([CLAIM-1062](../claims.d/CLAIM-1062.md)).
  The wording is the filer's (Claude, in this session); adopting it is the
  owner's call.
---
<!-- inactive-ok-file: CLAIM-742 CLAIM-750 THEORY-2000 — Proposed; the claims this corroborates and the reading of the earlier chapter -->
<!-- inactive-ok-file: CLAIM-1062 CASE-418 — new; the objection and the specimen filed from the reading -->

# THEORY-2294: Rogers, Suriar, Lueder, Deo and Sudhakar present Google's blameless postmortem as aimed at what failed and not who, with action items that improve systems rather than people, kept blameless by leaders who recast blameful questions, to managers and from executives, as questions about process, while questions about priorities set above the team are left to reviews of repeated incidents

Rogers, Suriar, Lueder, Deo and Sudhakar (2018), [LIT-3187](../literature.d/LIT-3187.md), read in
[NOTE-2391](../notes.d/NOTE-2391.md).

## The account

A good postmortem's root cause "Focuses on "what" went wrong, not "who"
caused the incident"; its action items "Are aimed at improving the system
instead of improving people"; "No individual or team is blamed". Naming
individuals makes people "afraid of being publicly shamed" and "motivated
to cover up facts". "Declaring official ownership results in
accountability, which leads to action."

Leaders "should consistently exemplify blameless behavior". The chapter's
examples of keeping a review blameless recast a question to a manager
("why aren't you making sure that everyone finishes the training?") as a
rule for the rotation, and a vice-president's question ("why didn't you
listen to that person?") as a generic one about "any warning signs".

Questions about priorities set above the team appear under repeated
incidents: "Is feature velocity trumping reliability fixes?" A
"cross-functional group of developers, SREs, and organizational leaders"
reviews the postmortem process as a whole.

## Bearing

- **[CLAIM-742](../claims.d/CLAIM-742.md)**: corroborates. Ownership is named as the source of
  accountability, apart from blame.
- **[CLAIM-750](../claims.d/CLAIM-750.md)**: corroborates the mechanism only. The norm against
  indicting a team works on questions to managers as on questions to
  engineers, recasting them as process. The prediction, about where
  action items stop across many reviews, it does not test; its one real
  postmortem is filed as [CASE-418](../cases.d/CASE-418.md).
- **[QUESTION-476](../questions.d/QUESTION-476.md)**: bears on. The first half is answered by design; on the
  second, the chapter keeps upstream questions out of the single
  postmortem and puts them, if anywhere, in reviews across incidents.
- **[THEORY-2000](THEORY-2000.md)**: same practice, same organization; this reading meets
  that theory's `promote_when` (dated note there).

## What it does not show

- That the practice works: "Our experience shows" is asserted.
- Whether the reviews of repeated incidents, or the cross-functional
  group, in fact reach decisions above the teams.
