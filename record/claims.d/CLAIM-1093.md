---
number: 1093
status: Active
formerly:
- CLAIM-tmpf71gk
title: 'Reserve and redesign are complementary'
statement: >-
  Maintaining a reserve and redesigning a transition change different
  components of readiness, one keeping enough capacity to cross an existing
  transition barrier and the other lowering the barrier itself, and under a
  budget that follows peak use they are complementary requirements rather
  than independently sufficient alternatives, unless the redesigned barrier
  is no higher than the cost of holding
version: 3
history:
- version: 2
  date: '2026-11-24'
  note: >-
    Revised to concede CLAIM-1099 (ADR-059), at the owner's word of
    2026-11-24 ("promote the ten", with this concession written in the
    same pass as the promotion table says; under the dialectic regime):
    CLAIM-1099 shows that under a budget set to the last period's peak
    use a redesigned transition is lost like the original unless a
    reserve is also held, so reserve and redesign are complements, not
    alternatives, except where the redesigned threshold is at most the
    holding cost. The title takes A53's wording, with "can be" made exact by CLAIM-1099's exception. Old title: "Maintaining
    a reserve and redesigning a transition are distinct routes to
    readiness: one keeps enough capacity to cross an existing transition
    barrier, the other lowers the barrier itself". The Standing section
    says the same. Nothing dropped needs routing: the old title's "distinct routes" read as alternatives, which CLAIM-1099 shows false, a note only
    (README, narrowing kind 3).
- version: 3
  date: '2026-11-24'
  note: >-
    Promoted to Active at the owner's word of 2026-11-24 ("handle the
    fixes for the twelve ... use your best judgement"; ADR-057's four
    criteria for an interpretive thesis): its premises CLAIM-577 and
    CLAIM-571 are Active; its one objection, CLAIM-1099, is written in
    by the revision above; nothing meets its defeated_if, since
    CLAIM-1099 shows redesign needing a reserve only where the
    redesigned threshold exceeds the holding cost, not always, and no
    held claim states the distinction (CLAIM-1180 derives what trading
    one for the other costs, and says CLAIM-1093 is the distinction);
    and the owner's word is the assent. An interpretive promotion,
    listed for the owner in the pull request.
role: thesis
warrant: interpretive
defeated_if: A showing that one route always requires the other, so that they are
  not distinct routes but parts of one; or that either is already a claim the record
  holds.
tags:
- operations-research
- society-and-governance
- self-governance
date: '2026-11-23'
line:
- readiness
- realizability
rests_on:
- CLAIM-577
- CLAIM-571
works:
- governance-of-possibility
summary: 'A48 §9.2–9.4 of the exchange "Explain First Contact RL" (ChatGPT, 2026-11-23),
  the manuscript governance-of-possibility: Regimes II and III "achieve adaptive
  readiness through different means", "reserve maintenance and mechanism redesign".
  A36 had named both remedies in a line; A48 sets them side by side as distinct
  forms of governance. [CLAIM-1099](CLAIM-1099.md) objects. The wording is A''s (ChatGPT, in
  the exchange of 2026-11-23); adopting it is the owner''s call.'
bears_on:
- QUESTION-395
---

# CLAIM-1093: Reserve and redesign are complementary

## The claim

In A48's model (§9), configuration A is held at a cost of 1, and the
transition to B passes through a configuration costing 3 ([CLAIM-577](CLAIM-577.md)'s
case; its threshold is [CLAIM-571](CLAIM-571.md)'s least peak over paths). Regime II
keeps a budget of 3 despite needing 1; Regime III "invests in an
alternative transition mechanism", a staging path whose peak is 2. "One
preserves enough capacity to cross the existing transition barrier. The
other changes the transition barrier itself."

## Standing

In A's voice, revised on 2026-11-24 to concede [CLAIM-1099](CLAIM-1099.md) ([ADR-059](../decisions.d/ADR-059.md)), in
A53's wording, with the exception [CLAIM-1099](CLAIM-1099.md) states added to the title: "Maintaining a reserve and redesigning a transition change
different components of reconfiguration readiness. Under
utilization-matched budgeting they can be complementary requirements
rather than independently sufficient alternatives." [CLAIM-1099](CLAIM-1099.md) shows
that under §9.1's own budget rule the redesigned route is lost like the
original unless a reserve is also held, so the two are distinct in what
they change but not alternatives; redesign replaces the reserve only
where its threshold is at most the cost of holding. The old title called
them "distinct routes to readiness", which read as alternatives.

## Note of 2026-11-23: the study filed

The manuscript's study is now on the record as [CASE-412](../cases.d/CASE-412.md). In its model the two routes are not alternatives under the peak rule, since redesign without a reserve (III-a) loses its route, while the reading this claim's Standing section concedes, that the two change different things, is untouched. The note is the assistant's (Claude, in this session); adopting it is the owner's call.

## Note of 2026-11-24: the exchange 'Memes, Contracts, and Systemic Normativity', A53

A53 proposes recording [CLAIM-1099](CLAIM-1099.md)'s objection as a concession: "Maintaining a reserve and redesigning a transition change different components of reconfiguration readiness. Under utilization-matched budgeting they can be complementary requirements rather than independently sufficient alternatives." The Standing section above already says so, but no history note names the objection, so the status-review worklist would count it unwritten once [CLAIM-1099](CLAIM-1099.md) is Active. The claim is A's, so the revision is the assistant's to make at that ruling, with A53's wording as the candidate. The note is the assistant's (Claude, in this session), reporting A's (ChatGPT's) text; adopting either is the owner's call. No status change.
