---
status: Proposed
title: 'Blameless post-incident review can stop its trace at "the system", which names no decision-maker, so that those who set budgets, staffing and deadlines drop out of the account along with the operator it shields: where the body that commissions a review also governs it, its contributing causes and action items stop at or below that body''s own decisions, and the review keeps upstream provenance only when its tracing crosses that body''s authority'
version: 1
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
- CLAIM-tmpx4kjt
summary: >-
  The lead filer's (Claude, in this session), proposed on 2026-11-18 in
  answer to the owner's request to consider blameless culture in
  engineering as a case ([QUESTION-476](../questions.d/QUESTION-476.md)), and accepted for filing by the
  owner ("all of the above please"). A hypothesis with a discriminating
  prediction: blameless review shields the sharp end, but if its trace
  stops at "the system", the upstream controllers of [CLAIM-707](CLAIM-707.md) drop out as
  well; its contributing causes and action items should stop at or below
  the authority of the body that commissions it. The proposed study is
  [CASE-tmpw9202](../cases.d/CASE-tmpw9202.md). No reading tests it: the SRE chapter's design fits its
  premise (internal review, senior management taking part, no team
  indicted), and Dekker and Nyce argue its mechanism for hospitals. The
  wording is the assistant's (Claude, in this session); adopting it is the
  owner's call.
---
<!-- inactive-ok-file: CLAIM-707 CASE-292 — Proposed; filed from the exchange "Assess Depp Heard Abuse" and its readings, cited with their standing -->
<!-- inactive-ok-file: CLAIM-tmpx4kjt CASE-tmpw9202 THEORY-tmpuc245 THEORY-tmpfomub THEORY-tmpl5x2t — new; filed with this claim -->
<!-- inactive-ok-file: ADR-075 — Proposed; the admission routes -->

# CLAIM-tmp5g7xc: Blameless post-incident review can stop its trace at "the system", which names no decision-maker, so that those who set budgets, staffing and deadlines drop out of the account along with the operator it shields: where the body that commissions a review also governs it, its contributing causes and action items stop at or below that body's own decisions, and the review keeps upstream provenance only when its tracing crosses that body's authority

## The claim

Blameless review was built against one failure: blame settling on the
person nearest the event, the moral crumple zone of [CLAIM-707](CLAIM-707.md). It answers
by moving the account from people to "systems and processes": "You can't
"fix" people, but you can fix systems and processes" (the SRE chapter,
[THEORY-tmpuc245](../theory.d/THEORY-tmpuc245.md)). But "the system" is not an agent. A trace that ends there
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
and who gets to say" ([THEORY-tmpfomub](../theory.d/THEORY-tmpfomub.md)).

**The prediction.** In postmortems commissioned and governed inside the
organization, the highest organizational level named among contributing
causes will rarely exceed the commissioning body's own authority, and
action items will cluster at or below the reviewing team's authority.
Independent investigators will name and target higher levels more often.
The Tempe report fits that half: the NTSB, outside the companies and
agencies it investigates, named Uber's culture and Arizona's oversight and
addressed its recommendations to them ([CASE-292](../cases.d/CASE-292.md), [CLAIM-tmpx4kjt](CLAIM-tmpx4kjt.md)).

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
concerns where the trace stops when blame is not. [CASE-tmpw9202](../cases.d/CASE-tmpw9202.md) is the
proposed study.

## Where it sits

- **[CLAIM-tmpx4kjt](CLAIM-tmpx4kjt.md)** complements it: an investigator outside the
  organization can carry provenance upstream without blame. This claim
  says when one inside cannot.
- **[CLAIM-707](CLAIM-707.md)** complements it: blame where blame is practised, the trace
  where it is withheld.
- **Cook** ([THEORY-tmpl5x2t](../theory.d/THEORY-tmpl5x2t.md), point 11): organizations leave the trade
  between production and risk ambiguous, "often intentionally". Those are
  the decisions the trace would have to reach.
- **Dekker and Nyce** ([THEORY-tmpfomub](../theory.d/THEORY-tmpfomub.md)) corroborate the mechanism, not the
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
