---
status: Proposed
title: "A work governance-of-possibility is added for the owner's manuscript from the exchange Explain First Contact RL: a claim is a member when the manuscript states the claim's proposition or uses it as a step"
version: 1
tags:
- record
date: '2026-11-23'
summary: >-
  At the owner's word of 2026-11-23 ("treat this as a manuscript generated
  by the repo and add a new works entry connecting it to its argument"),
  the closed works vocabulary gains governance-of-possibility, "Regulation
  as the Governance of Possibility". It is the manuscript the owner asked
  for at U24 and U25 of the exchange "Explain First Contact RL", which
  ChatGPT drafted at A46 and fleshed out at A48. Membership follows
  [ADR-104](ADR-104.md)'s rule. On reading, 37 claims are members: 23 on the default
  branch and 12 filed from the exchange's earlier turns, plus two filed
  from the manuscript in this change. Rejected: filing the manuscript as a
  work read from outside (a LIT); counting its lineage list; and having
  no work.
---
<!-- inactive-ok-file: CLAIM-711 CLAIM-tmpf71gk CLAIM-tmpyakra TERM-tmpu5k0o TERM-tmpz28l1 CASE-315 — Proposed; members of the work, cited as members whatever their standing, and entries filed or relied on with it -->

# ADR-tmpsfjxu: A work governance-of-possibility is added for the owner's manuscript from the exchange Explain First Contact RL: a claim is a member when the manuscript states the claim's proposition or uses it as a step

## Context

At U24 of the exchange "Explain First Contact RL" (2026-11-23), the owner
asked ChatGPT to "draft an article synthesizing our discussion"; A46 did,
and at U25 ("flesh this out") A48 wrote "Regulation as the Governance of
Possibility: Identity, Slow Modes, and the Temporal Organization of
Adaptive Industrial Ecosystems". It has an abstract, fifteen sections and
a closing "Theoretical lineage and status" that names eight of this
record's entries:

- §1–§2, regulation as the governance of which organizations an
  ecosystem can attain, sustain and revise, and the compatibility complex;
- §3–§5, identity as historical continuity, selective temporal filtering,
  slow modes and what must be stabilized;
- §6–§7, demands with deadlines, and the temporal architecture of
  governance;
- §8, the viability of adaptive readiness;
- §9, a model in which regimes matched on present output diverge after a
  contingency: utilization-matched, reserve-preserving and redesigned;
- §10–§13, diagnosis, overconsolidation, harmony as conserved capability,
  and the governance of governance; §14 limits, §15 conclusion.

The record holds the exchange's turns U1 to U23 (dmarx/nucleation#749).
On 2026-11-23 the owner first asked for the manuscript to be filed "as a
work"; it was filed as a LIT, and the owner corrected that within the
hour. The `works` field exists on CLAIM and ARG only.

## Decision

- **The `works` vocabulary gains `governance-of-possibility`**, labelled
  "Regulation as the Governance of Possibility". Its blurb names the
  request, the draft, its thesis and the lines that hold its argument.
- **The work is A48**, which supersedes A46: A46 is the draft A48 fleshes
  out at the owner's request, and claims A46 alone cites ([CLAIM-354](../claims.d/CLAIM-354.md)) are
  not members.
- **Membership is [ADR-104](ADR-104.md)'s rule.** A CLAIM or ARG is in the work when
  A48 states its proposition, in any wording, or uses it as a step. A
  citation in "Theoretical lineage and status" with no use in the text
  does not count, nor does a use of only a proviso or a reason an entry
  gives. Whether the record believes a member is its status ([ADR-032](ADR-032.md)).
- **Members are found by reading.** Each candidate was read against the
  section it would come from; the curation entry gives each member's
  section and the exclusions.
- **Gap fills are not members.** A fill the assistant files against the
  manuscript's argument is not offered for it, so it is not in the work
  unless the owner adds it.

## Alternatives

- **A LIT, NOTE and THEORY, as a work read from outside.** Tried first
  and reverted. The manuscript is the record's own argument recast for a
  reader, written at the owner's request from the record's entries; a
  reading would set its claims apart from the entries that hold them.
- **Count the lineage list.** [CLAIM-560](../claims.d/CLAIM-560.md) is cited there for the
  separation of existence, reachability and reliability, which it holds
  only in part; it is a member because §2.1 and §9 use what it holds, not
  because it is listed. [TERM-115](../terms.d/TERM-115.md) is listed and used, but a term cannot
  carry the field.
- **No work.** The members are in five lines, and no line groups them.

## Consequences

- 35 held claims join the work, each with a history note and a version
  bump: 23 Active and 12 Proposed. Two claims filed from the manuscript
  in this change join it too: [CLAIM-tmpf71gk](../claims.d/CLAIM-tmpf71gk.md) (§9.2–9.4) and [CLAIM-tmpyakra](../claims.d/CLAIM-tmpyakra.md)
  (§12).
- Nine members are in other works as well: [CLAIM-079](../claims.d/CLAIM-079.md), 099 and 075 in
  organization-of-will; [CLAIM-582](../claims.d/CLAIM-582.md), 478 and 569 in
  cost-structure-of-possibility; [CLAIM-711](../claims.d/CLAIM-711.md), 523 and 462 in
  capability-restraint-relational-freedom.
- The parts of A48 that cannot carry the field are named in the curation
  entry: [TERM-115](../terms.d/TERM-115.md) (§6), [TERM-tmpz28l1](../terms.d/TERM-tmpz28l1.md) (§8), [TERM-tmpu5k0o](../terms.d/TERM-tmpu5k0o.md) (§11, filed from
  it), [QUESTION-371](../questions.d/QUESTION-371.md) and [QUESTION-tmpn9t5a](../questions.d/QUESTION-tmpn9t5a.md) (§12), [QUESTION-395](../questions.d/QUESTION-395.md) (§9), and
  [LEAD-080](../leads.d/LEAD-080.md) with [CASE-315](../cases.d/CASE-315.md) (§9.6).
- The first application is in this decision's pull request: the
  vocabulary entry, the members, the entries filed from the manuscript,
  the curation entry and the changelog fragment.
