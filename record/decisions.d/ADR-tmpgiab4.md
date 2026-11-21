---
status: Active
title: 'A line, learning-and-inquiry, is added for how a system that draws distinctions comes to learn and to inquire, the candidate the first cross-line audit found; the eight principle accounts take it first and the claims it gathers take it beside their lines'
version: 1
history:
- version: 1
  date: '2026-11-21'
  note: >-
    Filed Active: the owner ruled before it was written, on the promotion
    pull request, 599: "adopt the ADRs and the candidate line, then
    merge".
tags:
- record
- taxonomy
date: '2026-11-21'
summary: >-
  The first audit of cross-line accounts under ADR-tmpg1n72 (curation entry
  of 2026-11-21) found that the eight accounts of the manuscript's
  principles P2 and P4 to P10 are each a bridge between lines. Together they
  answer a question no line holds: how any system draws distinctions, learns
  and inquires. It put that to the owner as a candidate line, and the owner
  adopted it. The line is added to the `lines` vocabulary with the audit's
  blurb. "Inquiry as specification" moves from record-as-apparatus's blurb
  into the new one, since it was the general question and not the record's
  case of it. The eight accounts take the line first. CLAIM-535 (P1),
  CLAIM-402 (P3) and CLAIM-794 (the narrowed part of the predicted cycle)
  take it beside their present lines. Rejected: folding the theme into
  record-as-apparatus, and leaving it as eight bridges.
---

# ADR-tmpgiab4: A line, learning-and-inquiry, is added for how a system that draws distinctions comes to learn and to inquire, the candidate the first cross-line audit found; the eight principle accounts take it first and the claims it gathers take it beside their lines

## Context

ADR-tmpg1n72 permitted accounts whose scope is a theme that crosses lines. It also audited each such account as a possible sign of a missing line: does it answer a question no line holds, does it recur, and would it be found more easily as a line? Its first audit, a curation entry of 2026-11-21, took the eight accounts filed for principles P2 and P4 to P10 of the owner's manuscript, "From Obstruction to Reorganization". It found that seven are bridges on their own, each carrying a question already held by a line its components sit in. Taken together, with P1 and P3, they answer a question none of the record's lines names. That question recurs: it is the manuscript's Part I, and the eight accounts were filed together for it. The audit drafted a name, a blurb and a scope, and put the candidate to the owner. The owner ruled on pull request 599: "adopt the ADRs and the candidate line, then merge".

## Decision

1. **The line.** `learning-and-inquiry`, labelled "Learning and inquiry". Its blurb is the audit's draft: how a system that draws distinctions comes to learn and to inquire. That covers distinctions relative to a target and a budget, learning as the formation of a maintained capacity, distinction or channel, occasioned and not guaranteed by a discrepancy, and inquiry as specification that can revise its own language, answers and criteria. It is kept apart from records-of-inquiry and record-as-apparatus.
2. **What it takes from an existing line.** Record-as-apparatus's blurb named "inquiry as specification". The general question moves to the new line, and record-as-apparatus keeps the record as its own case.
3. **What it gathers now:**
   - the eight accounts: SYNTHESIS-109, SYNTHESIS-110, SYNTHESIS-111, SYNTHESIS-112, SYNTHESIS-113, SYNTHESIS-114, SYNTHESIS-115 and SYNTHESIS-116. Each takes the line first, since the theme is its scope;
   - CLAIM-535 (P1), CLAIM-402 (P3) and CLAIM-794 (the narrowed part of the cycle). Each takes it after its present lines, which keep their order.
4. **What it does not gather yet.** The claims behind P5 and P8 that no other line holds as its own question are left to the next synthesis review. That review also files the line's account over the eight (ADR-083's coverage), since a line account is the review's work, not this decision's.

## Alternatives

- **Fold the theme into record-as-apparatus.** That line holds the record as the case. The theme is general: a trained network and an institution are its examples as much as the record is.
- **Leave it as eight bridges.** The audit found all three of its questions answered yes for the set. Leaving it would keep the theme findable only through the manuscript.

## Consequences

- `luria.yaml` gains one line term, and record-as-apparatus's blurb is narrowed.
- The claims index and the current-account view gain a line, and its account is due at the next synthesis review.
- The eight accounts are no longer cross-line in the sense of ADR-tmpg1n72: each now has a line. They stay accounts of a theme, now a line's theme, and their prefaces are left as written, dated 2026-11-20.
