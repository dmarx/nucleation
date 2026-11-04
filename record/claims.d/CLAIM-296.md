---
number: 296
status: Active
formerly:
- CLAIM-tmp9gt89
title: What a system has, what it knows it has, and what it can deploy within a
  task's deadline are different, and the last is a relation among the resource,
  the agent, its environment, the task, the deadline and the cue, not a property
  of any one of them
version: 2
history:
- version: 2
  date: '2026-10-29'
  note: >-
    Promoted by the sixteenth status review (ADR-057), at the status
    review's ruling (the owner delegated these rulings). Its term
    TERM-055 and its ground THEORY-346 are Active, it has no
    objection, and nothing in the record meets its defeat condition.
    THEORY-351 moves from grounds to corroborated_by (ADR-058): the
    claim is A17's, argued from CASE-085, and its note of 2026-10-15
    cites Hutchins's cockpit as the closest case the record holds, a
    stylized task analysis with no measurements. The claim is
    unchanged.
role: thesis
warrant: interpretive
defeated_if: >-
  A18's condition: for a stated model of agency, an independently justified criterion
  of capability that depends only on what is possessed, with no contribution from
  access, organization or constraint. Or a case in which a change only to the arrangement
  of the system leaves every such capability unchanged where this claim says it
  should move.
tags:
- agency
- cognition
- embodied-cognition
date: '2026-10-15'
line: distributed-agency
uses:
- TERM-055
grounds:
- THEORY-346
summary: >-
  A18's first candidate, from the owner's EMT case ([CASE-085](../cases.d/CASE-085.md)): the drug was
  stocked, the EMT knew it, and it could not be found before the medic moved on.
  "If I can't find it, it isn't there" is false of the inventory and right of the
  decision. [TERM-055](../terms.d/TERM-055.md) names the relation. A19 added the cue: the same memory
  under a different request may retrieve it.
illustrated_by:
- CASE-085
- CASE-094
complements:
- CLAIM-306
- CLAIM-312
corroborated_by:
- CLAIM-310
- THEORY-351
bears_on:
- QUESTION-101
---
<!-- inactive-ok-file: CLAIM-tmpvhj8j TERM-tmpuc919 — Proposed or new; A's proposals of 2026-11-04 on emergency readiness, cited as open -->
<!-- inactive-ok-file: NOTE-tmpxzaki NOTE-tmpy7mc8 NOTE-tmpdnqqh LIT-tmpum63p LIT-tmpt3a4i LIT-tmpjzyct — Skimmed or Unavailable; the location-model readings of 2026-11-04, cited as open -->
<!-- inactive-ok-file: LIT-1060 LIT-1065 — Unavailable; held without a reading, cited for what they would be read for, not leaned on -->

# CLAIM-296: What a system has, what it knows it has, and what it can deploy within a task's deadline are different, and the last is a relation among the resource, the agent, its environment, the task, the deadline and the cue, not a property of any one of them

## The claim

A17 §10: "Possessing a resource, possessing information about that
resource, and possessing the capability to deploy it are distinct
conditions. The last is relative to a task, a deadline, and the
organization of the agent–environment system." A16: the medic's line "is
literally false as a claim about inventory, but potentially correct as an
operational equivalence."

A17 §1 separated five levels in [CASE-085](../cases.d/CASE-085.md): physical presence (yes), knowing it
is present (yes, the unit had been checked), knowing where (not quickly
enough), retrieving it in time (no), and its still serving the purpose
(the medic changed the request). A18 noted these "are separate
predicates, not a universal logical hierarchy: an item can be deployable
by a practiced procedure even if no participant can explicitly state its
location."

A19 added the cue. "You possessed the information that the medication
was present, but the request did not successfully elicit the information
where to find it." That some cue retrieves an item does not mean the cue
now given does ([QUESTION-096](../questions.d/QUESTION-096.md)).

## Why it is a distributed-agency claim

A17: availability "is not an intrinsic property of the medication, nor
purely a subjective property of the person searching for it. The
organization of the ambulance, the distribution of knowledge among team
members, the unfolding clinical event, and the time remaining all
participate in determining it." That makes the capacity to deploy a
resource a candidate capacity of the organized whole ([QUESTION-101](../questions.d/QUESTION-101.md)). Gibson's
affordances ([LIT-1065](../literature.d/LIT-1065.md)) and Hutchins's distributed cognition ([LIT-1060](../literature.d/LIT-1060.md)) are the
traditions, both registered unread.

## What it does not say

- Not that existence depends on observers. A17: "practical availability
  depends on an organized relation between the world, the agent, and the
  demands of the situation."
- Not that the failure in [CASE-085](../cases.d/CASE-085.md) was the EMT's. A17 §8: the operational
  reading "could be used to treat a failure of the entire retrieval
  system as merely a failure of an individual."
- Not why retrieval failed in [CASE-085](../cases.d/CASE-085.md), or why the medic changed the
  request.

## Note of 2026-10-15: the cockpit, where arrangement alone changes capacity

Hutchins's "How a cockpit remembers its speeds" ([LIT-1066](../literature.d/LIT-1066.md), read in
[NOTE-867](../notes.d/NOTE-867.md)) is the closest the record now holds to a case for this
claim. "Individual pilot memory has not been enhanced; rather, the memory
function has now become a property of a larger system." The pilots are
unchanged; the speed card and the bugs change which processes are
assembled, so what the crew can deploy in time changes with the
arrangement alone, as [QUESTION-101](../questions.d/QUESTION-101.md) asks. Two limits. It is a stylized
task analysis with no measurements and no failure cases, and its task is
anticipated, mandated and invariant, about information and not about
locating an object. And it adds a factor this claim does not list: work
done before the request, by leaving the result in the environment (see
the note of the same date on [TERM-055](../terms.d/TERM-055.md)).

## Note of 2026-10-28: bearing on [QUESTION-101](../questions.d/QUESTION-101.md)

At the owner's ruling on the fourth status review, this claim bears on
[QUESTION-101](../questions.d/QUESTION-101.md) and does not answer it. It separates having a resource,
knowing it is had and deploying it, and makes deploying relational. That
frames what "available" means. It does not say when availability is the
system's and not a member's, for a stated class of tasks, which is what
the question asks.

## Note of 2026-11-04: Guigues, Kleywegt and Nascimento, "Policies for the Operation of an Ambulance Fleet", read

Their preparedness metric ([LIT-tmphy35q](../literature.d/LIT-tmphy35q.md)) is defined over the ambulances a station can actually deploy, so a busy unit adds nothing. That supports separating having a resource from being able to deploy it, at the level of a fleet. It leaves open whether a steady-state fleet rate is an instance of the claim's agent-level relation or only an analogue. No status changes.

## Note of 2026-11-04: Erkut, Ingolfsson and Erdoğan, "Ambulance location for maximum survival", read

In the expected-covering models ([LIT-tmprfb8b](../literature.d/LIT-tmprfb8b.md)), a unit at a station counts only with the probability that it is free. That supports the claim's distinction in a location model. It leaves open the cue and the knowing-it-has parts, which the model lacks. No status changes.

## Note of 2026-11-04: U.S. Fire Administration, "Dispatched and Canceled en Route", read

The NFIRS guidance ([LIT-tmpnhw2v](../literature.d/LIT-tmpnhw2v.md)) records separately the resources assigned, the units that arrived and the units cancelled en route, and it excludes from the incident data the calls a department could not answer for lack of resources. That supports the claim's distinctions at the level of reporting. It leaves open how often the missing case occurs, since NFIRS by design does not see it. No status changes.

## Note of 2026-11-04: the emergency-service location models, read through neighbours (Larson and Odoni; de Oliveira, de Sá and Martins; Mukhopadhyay et al.)

Larson's hypercube model, Daskin's MEXCLP and ReVelle and Hogan's MALP ([LIT-tmpum63p](../literature.d/LIT-tmpum63p.md), [LIT-tmpt3a4i](../literature.d/LIT-tmpt3a4i.md), [LIT-tmpjzyct](../literature.d/LIT-tmpjzyct.md), all unread) were read through neighbours, and all three give a formal case of the gap between having a resource and being able to deploy it by a deadline. In the hypercube model (Larson and Odoni, [NOTE-tmpxzaki](../notes.d/NOTE-tmpxzaki.md), prose only), a unit busy on another call is present but not deployable, and the units of last resort are deployable only when the system is saturated. In MEXCLP and MALP (de Oliveira, de Sá and Martins, [NOTE-tmpy7mc8](../notes.d/NOTE-tmpy7mc8.md), §2), a covering ambulance that is busy does not count, and the chance that one of k covering servers is free is 1 − b^k under independence. The review by Mukhopadhyay et al. ([NOTE-tmpdnqqh](../notes.d/NOTE-tmpdnqqh.md), §6.1) sorts deterministic coverage models, in which "Resources at a facility are considered to be always available", from probabilistic ones. In all of them unavailability comes from congestion alone, with no cue or knowledge component, so they qualify the claim's deployable tier and leave the first two untouched. No status changes.

## Note of 2026-11-04: deployability under a policy

A's CLAIM-tmpvhj8j and TERM-tmpuc919 (both Proposed) carry the split between having and deploying to an organization. Equipment present and staff qualified do not give readiness if a complementary capacity is absent or the policy does not mobilize them, and since readiness is a joint probability, one resource's utilization need not track it. The claim is unchanged.
