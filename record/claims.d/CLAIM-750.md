---
number: 750
status: Proposed
formerly:
- CLAIM-tmp5g7xc
title: 'Blameless post-incident review can stop its trace at "the system", which names no decision-maker, so that those who set budgets, staffing and deadlines drop out of the account along with the operator it shields: where the body that commissions a review also governs it, its contributing causes and action items stop at or below that body''s own decisions, and the review keeps upstream provenance only when its tracing crosses that body''s authority'
version: 2
history:
- version: 2
  date: '2026-11-22'
  note: >-
    A dated note added: the SRE workbook chapter read for LEAD-189
    (corroborates the mechanism), a specimen that illustrates the claim,
    and an objection to its unit filed as a claim. No change of status
    or title.
role: thesis
warrant: empirical
defeated_if: >-
  A coded corpus of postmortems from blameless reviews commissioned and
  governed inside the organization, in which contributing causes routinely
  name decisions above the reviewing team's authority (budgets, staffing,
  deadlines, priorities set above it) and action items routinely target
  such decisions, at rates not clearly below those of reviews by bodies
  independent of the organization. Not defeated by an independent
  investigator that reaches upstream, such as the NTSB at Tempe, which the
  claim predicts; nor by action items above the team that are written and
  never assigned an owner who could carry them out, which count for the
  claim; nor by the objection that it restates the crumple-zone claim,
  which is about where blame lands where blame is practised, while this is
  about where the trace stops where blame is withheld.
tags:
- society-and-governance
- software-engineering
- ethics
date: '2026-11-18'
line:
- rightful-power
bears_on:
- QUESTION-476
complements:
- CLAIM-707
- CLAIM-751
summary: >-
  The lead filer's (Claude, in this session), proposed on 2026-11-18 in
  answer to the owner's request to consider blameless culture in
  engineering as a case ([QUESTION-476](../questions.d/QUESTION-476.md)), and accepted for filing by the
  owner ("all of the above please"). A hypothesis with a discriminating
  prediction: blameless review shields the sharp end, but if its trace
  stops at "the system", the upstream controllers of [CLAIM-707](CLAIM-707.md) drop out as
  well; its contributing causes and action items should stop at or below
  the authority of the body that commissions it. The proposed study is
  [CASE-293](../cases.d/CASE-293.md). No reading tests it: the SRE chapter's design fits its
  premise (internal review, senior management taking part, no team
  indicted), and Dekker and Nyce argue its mechanism for hospitals. The
  wording is the assistant's (Claude, in this session); adopting it is the
  owner's call.
---
<!-- inactive-ok-file: CLAIM-707 CASE-292 — Proposed; filed from the exchange "Assess Depp Heard Abuse" and its readings, cited with their standing -->
<!-- inactive-ok-file: CLAIM-751 CASE-293 THEORY-2000 THEORY-1997 THEORY-1998 — new; filed with this claim -->

# CLAIM-750: Blameless post-incident review can stop its trace at "the system", which names no decision-maker, so that those who set budgets, staffing and deadlines drop out of the account along with the operator it shields: where the body that commissions a review also governs it, its contributing causes and action items stop at or below that body's own decisions, and the review keeps upstream provenance only when its tracing crosses that body's authority

## The claim

Blameless review was built against one failure: blame settling on the
person nearest the event, the moral crumple zone of [CLAIM-707](CLAIM-707.md). It answers
by moving the account from people to "systems and processes": "You can't
"fix" people, but you can fix systems and processes" (the SRE chapter,
[THEORY-2000](../theory.d/THEORY-2000.md)). But "the system" is not an agent. A trace that ends there
names no decision, and so no one who made one. The operator is shielded,
and so are those who set the budget, the staffing level, the deadline and
the priority that the operator worked within: [CLAIM-707](CLAIM-707.md)'s upstream
controllers. Blamelessness then reproduces the crumple zone's result one
level up. No one is blamed, and the conditions some actors set are not
repaired. That is the second answer [QUESTION-476](../questions.d/QUESTION-476.md) lists, "keeps correction,
loses provenance".

**The mechanism.** A review is commissioned and governed by someone. In
the SRE chapter, drafts go to "a group of senior engineers", with "senior
management's active participation in the review", and the norm forbids
"indicting any individual or team". A contributing cause that names a
decision of the reviewers' own management is awkward to write under that
norm and harder to turn into an action item that the reviewing team can
own. Dekker and Nyce argue the general point for hospitals: what counts as
a just response "depends on where one is located in the organization ...
and who gets to say" ([THEORY-1997](../theory.d/THEORY-1997.md)).

**The prediction.** In postmortems commissioned and governed inside the
organization, the highest organizational level named among contributing
causes will rarely exceed the commissioning body's own authority, and
action items will cluster at or below the reviewing team's authority.
Independent investigators will name and target higher levels more often.
The Tempe report fits that half: the NTSB, outside the companies and
agencies it investigates, named Uber's culture and Arizona's oversight and
addressed its recommendations to them ([CASE-292](../cases.d/CASE-292.md), [CLAIM-751](CLAIM-751.md)).

**The conditional answer to [QUESTION-476](../questions.d/QUESTION-476.md).** Blameless practice keeps
upstream provenance only when its tracing crosses the authority of the
body that commissions it.

## Admission

By a discriminating prediction ([ADR-075](../decisions.d/ADR-075.md)). Juxtaposed, [CLAIM-707](CLAIM-707.md) (blame
lands downstream of control) and the SRE chapter's design (blame
withheld, review internal) leave open where a blameless trace stops. This
claim settles it: at the commissioning body's authority. The outcome
against it is the defeater: internal reviews whose causes and action items
reach above the team as often as independent ones do. It does not restate
[CLAIM-707](CLAIM-707.md), which concerns where blame lands when it is assigned; this
concerns where the trace stops when blame is not. [CASE-293](../cases.d/CASE-293.md) is the
proposed study.

## Where it sits

- **[CLAIM-751](CLAIM-751.md)** complements it: an investigator outside the
  organization can carry provenance upstream without blame. This claim
  says when one inside cannot.
- **[CLAIM-707](CLAIM-707.md)** complements it: blame where blame is practised, the trace
  where it is withheld.
- **Cook** ([THEORY-1998](../theory.d/THEORY-1998.md), point 11): organizations leave the trade
  between production and risk ambiguous, "often intentionally". Those are
  the decisions the trace would have to reach.
- **Dekker and Nyce** ([THEORY-1997](../theory.d/THEORY-1997.md)) corroborate the mechanism, not the
  prediction. Their case is the opposite failure, [QUESTION-476](../questions.d/QUESTION-476.md)'s third
  answer: a just-culture scheme that relocates blame by rank. Both say the
  hierarchy that governs the review shapes what it finds.

## What it does not say

- That blameless review is worse than blame. Blame stops at the sharp end
  too, by Cook's account and [CLAIM-707](CLAIM-707.md)'s; this claim is about where a
  blameless trace stops, not about whether blame goes further.
- That the reviewers act in bad faith. The mechanism needs only that a
  review's commissioners govern what it writes.
- That "the system" is never the right answer. It is incomplete when the
  system has authors whose decisions it omits.

## Note of 2026-11-18: what holds it back

The claim is empirical and untested: no reading codes postmortems by the highest organizational level their contributing causes and action items reach, internal against independent, and [CASE-293](../cases.d/CASE-293.md) is the proposed study. The SRE chapter ([THEORY-2000](../theory.d/THEORY-2000.md)) and Dekker and Nyce ([THEORY-1997](../theory.d/THEORY-1997.md)) bear on the mechanism only.

## Note of 2026-11-22: a pilot coding runs in the predicted direction
<!-- inactive-ok-file: CASE-335 CLAIM-905 — new; the pilot and its finding, filed for LEAD-119 on 2026-11-22 -->

The first coded corpus bearing on this claim's prediction is [CASE-335](../cases.d/CASE-335.md), run for [LEAD-119](../leads.d/LEAD-119.md). Causes above the engineering team appear in 2 of 30 public postmortems against 7 of 10 CSB reports, and action items above it in 4 against 9. No postmortem names corporate leadership, while 5 of the reports do. That meets the "prediction holds" rule fixed before coding. The finding is filed separately as [CLAIM-905](CLAIM-905.md), which corroborates this claim. One coder, the assistant (Claude, Opus 5.5), of the same model family that wrote the claim tested and the codebook, coding with the prediction known: the pilot is not independent. The arms differ in domain and severity (software outages against chemical accidents) as well as in who reviews. So the defeater is not tested yet: the pilot does not hold domain fixed. An observation made after coding fits the mechanism: the four postmortems whose action items reach above the team were written by the organization's leadership (a CEO, founders, and two authors the coder recalls as CTOs).

No status changes.

## Note of 2026-11-22: the SRE workbook read: the mechanism corroborated, an exemplar that fits, and an objection to the unit
<!-- inactive-ok-file: THEORY-tmpm653d THEORY-tmp9j928 CASE-tmptkkgm ARG-tmp117cw CLAIM-tmpauu5r — new; filed for LEAD-189 on 2026-11-22 -->

Read for LEAD-189 on 2026-11-22: Google's SRE workbook chapter on postmortem culture (THEORY-tmpm653d, NOTE-tmpf58r7), which now `corroborates` this claim, and the SRE book's example postmortem (THEORY-tmp9j928, NOTE-tmpdiani).

- **The mechanism, corroborated.** The norm against indicting a team works on questions to managers too. The workbook rewrites "You're the manager; why aren't you making sure that everyone finishes the training?" as a rule for the on-call rotation, and meets a vice-president's "why didn't you listen to that person?" with "maybe we ask generically if there were any warning signs". In each, a question that would reach a decision-maker becomes one about process. Its checklist has action items "vetted and approved by the technical leads of the service".
- **An exemplar that fits the prediction.** The workbook's real postmortem, shown as good practice, names ""The installer" has limited staffing" among what went poorly and assigns fourteen action items, all technical, to engineers, none to staffing (CASE-tmptkkgm, which `illustrates` this claim; ARG-tmp117cw). The case carries an alternative reading: the installer may be a peer team, so the instance may be lateral, not upward. The filer leans to the first reading.
- **The example postmortem** fits trivially and tests nothing: a fictional bug and surge have no upstream decision to miss.
- **An objection, filed as a claim.** CLAIM-tmpauu5r objects to the unit of the prediction: the workbook routes upstream questions ("Is feature velocity trumping reliability fixes?") to reviews of repeated incidents and to a process review with "organizational leaders", so a practice could keep upstream provenance across incidents while each postmortem stops at the team. The pilot (CASE-335) and the proposed study (CASE-293) code single postmortems. The objection concedes that the workbook gives no evidence those channels reach above the teams.

No status changes.
