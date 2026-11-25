---
number: 923
status: Proposed
formerly:
- CLAIM-tmpmcrb7
title: 'Frustration and thwarting are independent'
statement: >-
  With operative thwarting identified by silencing a process, structural
  frustration and thwarting are independent in both directions: under a
  resolution that seeks joint satisfaction a member is thwarted only where
  the demands in force are jointly unsatisfiable, and in a minimal conflict
  exactly one member goes unmet while every other member is separately a
  but-for cause of it; a pair that conflicts minimally need not thwart each
  other inside a larger organization; thwarting where joint satisfaction is
  attainable needs a resolution that weighs authority or preference beyond
  the demands; and a frustrated set can leave an unmet member acting with no
  process responsible
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-076. The
    constructions and their checks are scratch/studies/lead-076/frustration.py
    and test_frustration.py.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the constructions or the derivation: a finite organization
  with a joint-satisfaction-maximizing resolution in which a member is
  unmet and acting at the outcome while the demands the resolution reads
  are jointly satisfiable; a minimal conflict, whose members act whenever
  unmet, in which that resolution leaves two members unmet, or in which
  silencing some other member does not get the unmet one met. Or a
  premise failing: a reading of operative thwarting the record adopts on
  which counterfactual silencing of a process is not the test, for
  example one that counts a resolution rule or a constraint as the
  thwarter, on which construction C2 would be thwarting. Also defeated
  as a claim of its own if it only restates CLAIM-631's items 3 and 6
  and QUESTION-131's two-demand example.
tags:
- mathematics
- self-governance
- causality
date: '2026-11-22'
line:
- distributed-agency
- formal-apparatus
- will-organization
rests_on:
- CLAIM-347
- CLAIM-549
complements:
- CLAIM-631
bears_on:
- QUESTION-131
summary: >-
  [QUESTION-131](../questions.d/QUESTION-131.md) asks when structural frustration shows up as operative
  thwarting, whether thwarting can occur where joint satisfaction is
  possible, and what evidence attributes it. It asks for thwarting shown
  "ideally ... by counterfactual intervention", and [LEAD-076](../leads.d/LEAD-076.md) for
  constructions that separate the two in each direction. In a finite model
  of arrangements, acceptance sets, quiet sets and a resolution rule, with
  thwarting tested by silencing a process, six constructions and two
  exhaustive random checks give the claim. Thwarting inside the
  requirement complex needs a resolution that weighs something besides the
  demands. In a minimal conflict the thwarting is real and belongs to the
  rest of the collection. Pairwise attribution fails once others share one
  side's demand. And frustration can be unvoiced ([CLAIM-631](CLAIM-631.md)'s item 3) or
  causally idle. The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-631 THEORY-052 — Proposed or new; the integration this complements, the reading cited for operative thwarting, and the study filed with this claim -->

# CLAIM-923: Frustration and thwarting are independent

## The model

- **The organization.** A finite set of attainable arrangements ℛ, and
  members i with acceptance sets Aᵢ ([CLAIM-347](CLAIM-347.md)) and quiet sets Qᵢ ⊇ Aᵢ,
  where i does not act toward its demand ([CLAIM-549](CLAIM-549.md), [CLAIM-631](CLAIM-631.md)'s Tᵢ).
- **Resolution.** A rule picks the next arrangement from the demands it
  reads: those of members that are met, who maintain them, and of members
  that are unmet and acting. An unmet, quiet member has dropped its demand
  for now. The outcome is the fixed point of iterating the rule.
- **Structural frustration** of S is S ∉ 𝒦 ([CLAIM-347](CLAIM-347.md)).
- **Operative thwarting.** Member i is operatively thwarted at the outcome
  when i is unmet and acting there, and silencing some other process j
  (removing j's push from the resolution, its demand still counted for
  who is met) yields an outcome at which i is met. j is then a *but-for
  thwarter*; a set silenced together is a but-for set. This makes
  [QUESTION-131](../questions.d/QUESTION-131.md)'s "identified constraint or countervailing mechanism,
  ideally shown by counterfactual intervention" a definition. The choice
  is the assistant's.

Two rules are used:

- *joint-satisfaction-seeking*: the arrangement meeting the most read
  demands, ties by a fixed order;
- *authority*: each read member pushes, with its weight, for its
  preferred arrangement within its acceptance set.

## The claim

1. **Under a joint-satisfaction-seeking rule, an unmet, acting member at
   the outcome means the demands the rule reads there are jointly
   unsatisfiable.** If they were in 𝒦 the rule would meet them all, and
   every unmet, acting member is among them. So under such a rule there
   is no thwarting without structural frustration of the demands in
   force. Checked on 4000 random organizations (two to four members, two
   to five arrangements, random quiet sets), 1579 of them with an unmet,
   acting member.
2. **In a minimal conflict of members who act whenever unmet, the same rule
   leaves exactly one member unmet, and each other member is separately a
   but-for thwarter of it.** All of S is read, every S ∖ {k} is in 𝒦, and S
   is not, so the maximum is |S| − 1 met. Silencing j ≠ i makes S ∖ {j}
   the read set, which the rule then meets, i included. Which member goes
   unmet is set by the tie-break, as [QUESTION-131](../questions.d/QUESTION-131.md) says ("Which one goes
   unmet depends on what the organization does"). The thwarting is
   attributable to every other member and to none in particular: the
   obstruction belongs to the collection ([QUESTION-131](../questions.d/QUESTION-131.md)), and so does the
   counterfactual responsibility. Checked on every random organization
   whose member set was a minimal non-face (1253 of 20,000 drawn), and on
   the symmetric conflicts of two to six members.
3. **A minimal conflicting pair need not thwart each other inside a larger
   organization** (C4). Member i wants x; j, k and l want y. Then {i, j}
   is a minimal non-face, but silencing j leaves y the winner. No single
   member is a but-for thwarter of i; the minimal but-for sets are pairs.
   Attribution is relative to the whole set of demands in force, not to
   the conflicting collection, which extends [CLAIM-361](CLAIM-361.md)'s indexing to a
   reference collection from frustration to thwarting.
4. **Thwarting without frustration needs a resolution that weighs
   something besides the demands** (C5). Take ℛ = {x, y, z},
   A₁ = {x, z} and A₂ = {y, z}, so z meets both. Member 2 has weight 2 and
   prefers y, and under the authority rule y wins. Member 1 is unmet and
   acting, and silencing 2 gets it met. Under the joint-satisfaction rule
   the same organization reaches z and no one is thwarted. This is
   [CLAIM-357](CLAIM-357.md)'s governance-induced frustration, shown counterfactually.
   [CASE-153](../cases.d/CASE-153.md)'s sentry is an instance (C6). Protecting while inspecting meets
   both the sentry's demand and the investigator's, yet a sentry with
   authority and a preference for sheltering blind thwarts the
   investigator, and silencing it is the protected investigator.
   [CASE-346](../cases.d/CASE-346.md) runs it.
5. **Frustration without thwarting**, two ways.
   - *Unvoiced* (C1, [CLAIM-631](CLAIM-631.md)'s item 3): the unmet member is quiet.
   - *Causally idle* (C2): R = {x, y}, A₁ = {x}, A₂ = {y}, every member acts
     when unmet, and the resolution does not read the demands. It always
     yields y. Member 1 is unmet and acting, so [CLAIM-631](CLAIM-631.md)'s precondition
     holds. Yet silencing member 2, or deleting its demand altogether,
     leaves member 1 unmet. The pair is frustrated, and the frustration is
     not why member 1 is unmet.

## What it adds to [CLAIM-631](CLAIM-631.md)

[CLAIM-631](CLAIM-631.md) gives the precondition of thwarting (an unmet, acting member)
and says "it gives a necessary condition of thwarting, not thwarting".
This claim supplies the missing test, a counterfactual on processes, and
says when it is passed:

- always in a minimal conflict under a responsive rule, by every other
  member;
- not necessarily in a larger organization (item 3);
- inside 𝒦 only through authority or preference (item 4);
- not at all where the resolution does not respond (item 5).

[CLAIM-631](CLAIM-631.md)'s item 6, "the precondition can occur where joint satisfaction
is possible", becomes thwarting proper in item 4, and item 1 says what it
requires.

## What it does not say

- That silencing is the only test of thwarting. A reading on which a
  constraint or the resolution rule itself can thwart (self-determination
  theory's environmental thwarting, [THEORY-052](../theory.d/THEORY-052.md)) would count C2 as
  thwarting. Which reading the record adopts is [QUESTION-131](../questions.d/QUESTION-131.md)'s and the
  owner's, and it is named in the defeater.
- That every responsive rule behaves like the joint-satisfaction one.
  Items 1 and 2 are proved for that rule, weighted or not; other
  responsive rules were not checked.
- Anything about felt frustration, strain ([CLAIM-368](CLAIM-368.md)) or the scales of
  [NOTE-1527](../notes.d/NOTE-1527.md) and [NOTE-1530](../notes.d/NOTE-1530.md).
