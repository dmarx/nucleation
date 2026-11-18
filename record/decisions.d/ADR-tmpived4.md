---
status: Proposed
title: "A work capability-restraint-relational-freedom is added for the owner's manuscript from the exchange Assess Depp Heard Abuse: a claim is a member when the manuscript or an addition offered for it states the claim's proposition or uses it as a step"
version: 1
tags:
- record
date: '2026-11-18'
summary: >-
  At the owner's request of 2026-11-18, the closed works vocabulary gains
  capability-restraint-relational-freedom, "Capability, Restraint, and
  Relational Freedom". It is the manuscript the owner asked for at U22 of
  the exchange "Assess Depp Heard Abuse". ChatGPT drafted it at A49 and
  offered additions in later turns. A claim or ARG is a member when the
  manuscript, or a passage that A explicitly offers for it, states the
  entry's proposition or uses it as a step. Membership says nothing of
  status (ADR-032). The owner expected the work to be mostly a subset of
  the line rightful-power. On reading, it is not: 28 claims are members,
  and only 7 carry the line. The manuscript's question, its last
  sections and the later additions sit in the line. Its body relays the
  record's earlier claims on dependence, correction, self-binding and
  capability trajectories, and those keep their own lines. Rejected:
  counting only entries filed from the exchange; restricting the work to
  members of the line; counting what the provenance table cites but the
  text does not use; and having no work.
---
<!-- inactive-ok-file: ADR-tmpkc7xl — Proposed; the line's decision, this pull request's base -->
<!-- inactive-ok-file: SYNTHESIS-100 — Proposed; the account whose audit of the manuscript this decision reads -->
<!-- inactive-ok-file: QUESTION-478 QUESTION-475 QUESTION-485 — Open; held parts of the manuscript that cannot carry the field -->
<!-- inactive-ok-file: CLAIM-716 CLAIM-720 CLAIM-721 CLAIM-727 CLAIM-734 CLAIM-737 CLAIM-746 CLAIM-624 CLAIM-670 CLAIM-675 CLAIM-688 — Proposed; members of the work, cited as members whatever their standing -->
<!-- inactive-ok-file: CLAIM-684 — Proposed; cited in the manuscript's provenance table and not used in its text, so not a member -->

# ADR-tmpived4: A work capability-restraint-relational-freedom is added for the owner's manuscript from the exchange Assess Depp Heard Abuse: a claim is a member when the manuscript or an addition offered for it states the claim's proposition or uses it as a step

## Context

At U22 of the exchange "Assess Depp Heard Abuse" (2026-11-16), the owner
asked: "flesh this out in the form of a manuscript. anywhere you feel
inclined to cite something in Nucleation, track backwards to identify
relevant LIT items to reference as citations." A49 wrote "Capability,
Restraint, and Relational Freedom: Toward a Theory of the Legitimate
Governance of Capabilities" ("Working manuscript — November 2026"). It
has sixteen sections, a reference list and a provenance table tracing its
themes through this record. Later turns offer additions for "the
manuscript" or "our manuscript". Seven do so explicitly:

- A51: two propositions on delayed gratification;
- A53 §8: a section on "The Political Economy of Capability Governance";
- A55: a principle on fait accompli breach;
- A57 §8: remedial externalization and remedial capture;
- A59: preemptive agency foreclosure, and the wrong of building a
  relationship in which such acts prevail;
- A68 §4: resistance to enforcement as influence over the norm;
- A71 §12 and A76: legitimacy against adequacy, and a concise thesis.

The record already holds the manuscript's argument, spread over many
entries. The filings of 2026-11-17 and 2026-11-18 filed the exchange's
new ideas. SYNTHESIS-100 audits A49 among A's syntheses. ADR-tmpkc7xl,
the decision this pull request is based on, added the line rightful-power
for the exchange's inquiry. That decision left the manuscript's work to
be "decided separately", expected to "sit inside the line". On
2026-11-18 the owner asked for the work and expected it to be mostly a
subset of the line.

The `works` field exists on CLAIM and ARG only (luria.yaml; docs/record.md).
A question, case or term cannot be a member, whatever part it plays in
the manuscript.

## Decision

- **The `works` vocabulary gains `capability-restraint-relational-freedom`**,
  labelled "Capability, Restraint, and Relational Freedom". Its blurb
  names the request, the draft and its thesis.
- **Membership.** A CLAIM or ARG is in the work when the manuscript (A49),
  or a passage A explicitly offers for it, does either of two things:
  - states the entry's proposition, in any wording; or
  - uses the entry's proposition as a step in its argument.

  A passage A offers for the manuscript counts; one that only extends the
  discussion does not. A citation in the provenance table, with no use in
  the text, does not count. Whether the record believes a member is its
  status, and the two may disagree (ADR-032).
- **Members are found by reading, not by line.** Each candidate was read
  against the passage it would come from. The curation entry gives each
  member's section.
- **The line is not a condition.** A member keeps the lines it carries,
  and joining the work adds no line to it.

## The expectation, checked

The owner expected the work to be mostly a subset of rightful-power. It
is not. Of 28 member claims, 7 carry the line: CLAIM-716, CLAIM-720,
CLAIM-721, CLAIM-727, CLAIM-734, CLAIM-737 and CLAIM-746. These are the
manuscript's guiding thesis and §12 (grounds against authority), its
§8.1, its §11, and the later additions on remedies and on legitimacy
against adequacy. The manuscript's research question is the line's root
question QUESTION-478, which holds §13's five conditions as a list to
test.

The other 21 hold the body of the paper. Twelve were on the record
before the exchange, and nine were filed from its earlier turns. They
carry six other lines:
dependence-and-domination, organizational-normativity,
distributed-agency, transient-support, will-organization and
flourishing-and-meaning. They hold:

- the method;
- the control of terms of dependence;
- moral commitments as resources;
- predatory and produced dependence;
- capability trajectories;
- collective restraint;
- correction capacity;
- responsibility for conditions.

A49 says so itself: it uses "Nucleation's existing distinctions to
support the argument". So the work and the line overlap, and neither
contains the other. The line also holds eight member claims the
manuscript does not use: the rights, answerability and blame material
the exchange reached after A76.

The blurb therefore says that the argument is held "in the line
rightful-power and its neighbours", not in the line alone.

## Alternatives

- **Count only the entries filed from the exchange.** Under this rule
  the work would have 16 members, not 28. It would also drop the
  claims the manuscript is built from: CLAIM-462, CLAIM-523, CLAIM-624,
  CLAIM-688 and CLAIM-675 are all named in its provenance table and
  stated in its text. A manuscript's claims are those it marshals, which
  is the vocabulary's own definition.
- **Restrict the work to members of the line.** This would make the
  owner's expectation true by definition. It would leave out most of
  §3 to §11.
- **Count what the provenance table cites.** CLAIM-354 and CLAIM-684
  appear there, but the text does not state their propositions. CLAIM-354
  supplies only a hedge about partial comparability, and CLAIM-684's
  rising burden of justification is not argued. Counting citation would
  admit A's mispairings too: the curation entry of 2026-11-17 found the
  table pairs CLAIM-363 and CLAIM-670 with works neither cites. Each of
  those two is a member only because the text uses it.
- **No work.** The line already groups the exchange's inquiry. But a
  manuscript is a view over the argument (the vocabulary's blurb), and
  without the work there is no way to read the paper's claims together,
  or to see which of them the record believes.

## Consequences

- The work can be read as one set across eight lines. The `works` view
  shows which members are Active (CLAIM-363, CLAIM-462, CLAIM-464,
  CLAIM-523) and which are Proposed (the rest).
- Parts the manuscript draws on that cannot carry the field are named in
  the curation entry, not tagged. These are QUESTION-478 (§13),
  QUESTION-475 (A68 §4), QUESTION-485 (A71 §12's deeper proposition), the
  cases of §4, §6 and A51, and the terms of §3 and §5.
- Passages held by no entry are listed in the curation entry with the
  reason each was left.
- The first application is in this decision's pull request. It holds the
  vocabulary entry and the 28 members, each with a history note, the
  curation entry and the changelog fragment.
