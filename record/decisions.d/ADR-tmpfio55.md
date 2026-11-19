---
status: Proposed
title: "A work cost-structure-of-possibility is added for the owner's manuscript from the exchange Topological protection explained: a claim is a member when the manuscript or an addition offered for it states the claim's proposition or uses it as a step"
version: 1
tags:
- record
date: '2026-11-19'
summary: >-
  At the owner's decision of 2026-11-19, the closed works vocabulary
  gains cost-structure-of-possibility, "The Cost Structure of
  Possibility". It is the manuscript the owner asked for at U19 of the
  exchange "Topological protection explained", which ChatGPT drafted at
  A43. Membership follows ADR-104's rule: a claim or ARG is a member when
  A43, or a passage A explicitly offers for it, states the entry's
  proposition or uses it as a step; a reference-list citation alone does
  not count. Membership says nothing of status (ADR-032). On reading, 16
  claims are members, 4 of them Proposed. They sit mostly in the lines
  realizability and formal-apparatus. Rejected: counting the reference
  list; counting every claim that is an instance of A43's general
  amortization result; and having no work.
---
<!-- inactive-ok-file: ADR-104 — Proposed; the decision whose pattern and rule this one follows -->
<!-- inactive-ok-file: CLAIM-478 CLAIM-576 CLAIM-295 CLAIM-184 — Proposed; members of the work, cited as members whatever their standing -->
<!-- inactive-ok-file: CLAIM-358 — Proposed; near the manuscript's text and judged not a member, cited with its standing -->

# ADR-tmpfio55: A work cost-structure-of-possibility is added for the owner's manuscript from the exchange Topological protection explained: a claim is a member when the manuscript or an addition offered for it states the claim's proposition or uses it as a step

## Context

At U19 of the exchange "Topological protection explained" (2026-11-19),
the owner asked: "flesh this out in the form of a (sketched)
manuscript". The request followed A41's research question: how
historically accumulated constraints change the cost of realizing
future possibilities. A43 wrote "The Cost Structure of Possibility:
Historical Investment, Effective Constraints, and the Emergence of
Capabilities" ("Working manuscript — theoretical sketch, November
2026"). It has an abstract, thirteen sections and a reference list:

- §1, the thesis: "An emergent organization can be understood as a
  historically accumulated investment that changes the cost structure of
  future possibility";
- §2, selective contraction and time-scale separation as the source of
  effective constraints;
- §3, amortization, and the separate costs of acquiring, keeping,
  operating and revising an organization;
- §4, a budget-feasible repertoire, and three routes of capability
  change;
- §5, productive nuclei, and organization that changes the cost of
  further organization;
- §6, compressed history and what it must keep;
- §7, three worked examples;
- §8 and §9, capability against substantive freedom, capability
  trajectories, and the cost of revision;
- §10, two propositions and four hypotheses with a design; §11, limits;
  §12 and §13, discussion and conclusion.

The reference list names twelve of this record's entries as "research
context". Two later turns offer theses for a manuscript, and both are
read as offered for another one. A46 §10 gives "the thesis I'd put at the center of the next
manuscript", on learning. A60 §9 would "strengthen our manuscript's
central thesis" in the same form, "Learning as the historical
redistribution of computational work". So the work is A43 alone. On
2026-11-19 the owner answered "yes" to the offer of a work for it.

The `works` field exists on CLAIM and ARG only. A question, case or term
cannot be a member.

## Decision

- **The `works` vocabulary gains `cost-structure-of-possibility`**,
  labelled "The Cost Structure of Possibility". Its blurb names the
  request, the draft, its thesis and the lines that hold its argument.
- **Membership is ADR-104's rule.** A CLAIM or ARG is in the work when
  A43, or a passage A explicitly offers for it, states the entry's
  proposition in any wording, or uses it as a step in its argument. A
  citation in the reference list, with no use in the text, does not
  count. Nor does a use of only an entry's proviso, or of a reason it
  gives, as ADR-104's revision found for one of its members.
  Whether the record believes a member is its status (ADR-032).
- **Members are found by reading.** Each candidate was read against the
  section it would come from. The curation entry gives each member's
  section.

## Alternatives

- **Count the reference list.** CLAIM-354 is listed there as
  "Multidimensional freedom and organizational capability". The claim is
  about degrees of an agent's freedom of will, compared by a partial
  order, and the text uses neither. §9 separates first-order capability
  from the capacity for revision, one of its dimensions, and goes no
  further.
- **Count every instance of A43's general results.** §3 states
  amortization in general, so any claim about an amortized cost would
  join. CLAIM-303 is counted because §3.1 states its break-even proposition
  and §3.3 its costs of keeping. CLAIM-358 is not counted: §7.3's
  conventions replace negotiation and supervision alike, and A43 does
  not state its contrast between local settlement and escalation.
- **No work.** The members are in eleven lines, and no line groups
  them. Without the work, the manuscript's claims cannot be read
  together, nor can one see which of them the record believes.

## Consequences

- The work can be read as one set. Twelve members are Active.
  CLAIM-478, CLAIM-576, CLAIM-295 and CLAIM-184 are Proposed.
- Two members are in other works as well: CLAIM-675 in
  capability-restraint-relational-freedom, and CLAIM-184 in
  luria-nucleating-an-argument.
- The parts of A43 that cannot carry the field are named in the curation
  entry: QUESTION-095 (§3.2), TERM-114 (§4), TERM-117 (§5.1) and
  TERM-062 (§6).
- A claim filed in an open pull request (#528) takes §5.2's recursive
  step. It joins the work once both pull requests merge.
- The first application is in this decision's pull request: the
  vocabulary entry, the 16 members, each with a history note and a
  version bump, the curation entry and the changelog fragment.
