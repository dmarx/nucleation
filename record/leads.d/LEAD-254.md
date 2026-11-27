---
number: 254
status: Open
formerly:
- LEAD-tmpeo8wq
title: 'Index the resource-bounded constraint system''s reachability by actor and by authority, and construct a cooperation in which repeated successful coordination enlarges what the participants can reach together while contracting what one of them can reach alone, separating physical feasibility, affordability, authorization and permissibility of each transition'
version: 3
history:
- version: 2
  date: '2026-11-26'
  note: >-
    Dated note of 2026-11-26 from the exchange "Alignment consequences
    brainstorm" (ChatGPT, 2026-11-26): A4 §5's actor-indexed readiness and
    kernels and A5 §4's orders of power; the assistant's statement of what
    the indexing must fix. Scope and stage unchanged.
- version: 3
  date: '2026-11-26'
  note: >-
    Dated note from the exchange "Alignment consequences brainstorm"
    (ChatGPT, 2026-11-26), A19: resource-bounded coalition logic as a
    language for the lead's indexed reachability, and the worker example's
    five modalities. Scope and stage unchanged.
stage: idea
priority: medium
method:
- formal
tags:
- complex-systems
- operations-research
- society-and-governance
date: '2026-11-24'
line:
- realizability
- dependence-and-domination
advances:
- CLAIM-571
- CLAIM-603
- CLAIM-670
- CLAIM-1265
- CLAIM-1221
summary: >-
  From A49's Article 3, "The Cost of Becoming", in the exchange "Memes,
  Contracts, and Systemic Normativity" (ChatGPT, 2026-11-24): "Extend the
  existing [TERM-114](../terms.d/TERM-114.md) and [CASE-326](../cases.d/CASE-326.md) machinery to actor-indexed resource and
  transformation profiles", R_i(S; B, H, W), the states reachable by i
  under budget, horizon and authority, and "Investigate when recurrent
  successful coordination expands collective reach while contracting the
  independent reach of particular participants." [TERM-114](../terms.d/TERM-114.md) indexes
  reachability by a budget, not by an actor or an authority. Stage idea:
  the object is named, not defined. The wording is A's (ChatGPT, in the
  exchange 'Memes, Contracts, and Systemic Normativity'); the construction
  asked for is the assistant's (Claude, in this session); adopting either
  is the owner's call.
---
<!-- inactive-ok-file: CLAIM-1016 CLAIM-603 CLAIM-670 CLAIM-1221 CLAIM-1265 TERM-116 — Proposed, Rejected or new; entries this one reads or rests on, cited whatever their standing -->

# LEAD-254: Index the resource-bounded constraint system's reachability by actor and by authority, and construct a cooperation in which repeated successful coordination enlarges what the participants can reach together while contracting what one of them can reach alone, separating physical feasibility, affordability, authorization and permissibility of each transition

## The gap

A49, Article 3, "Formal and experimental center":

R_i(S; B, H, W) = {S' : S' is reachable by i under B, H, W}.

"Investigate when recurrent successful coordination expands collective
reach while contracting the independent reach of particular participants."
And §7, "Authority-sensitive cost landscapes. Distinguish physical
feasibility, affordability, authorization and normative permissibility."

What the record holds:

- reachability indexed by a partially ordered budget ([TERM-114](../terms.d/TERM-114.md)), and the
  threshold for reaching a state apart from the cost of keeping it
  ([CLAIM-571](../claims.d/CLAIM-571.md));
- the relational profiles of a configuration, incoming, outgoing and
  observational ([TERM-116](../terms.d/TERM-116.md)), not indexed by who pays;
- in prose, the capability lost because another supplies it ([CLAIM-603](../claims.d/CLAIM-603.md))
  and the dependence an arrangement produces by supplying ([CLAIM-670](../claims.d/CLAIM-670.md));
- an obligation as a condition on permissible transitions, not a cost
  ([CLAIM-1265](../claims.d/CLAIM-1265.md)), and the cost of authorization placed between
  formulating and investigating ([CLAIM-1016](../claims.d/CLAIM-1016.md));
- the fallback that matters without being used, by changing the terms
  others offer ([CLAIM-1221](../claims.d/CLAIM-1221.md)).

No entry defines reach per actor, or separates the four predicates on a
transition in one formal object, so "collective reach grows while
independent reach shrinks" is held only as prose about dependence.

## What it would take

1. **Define R_i.** Fix [TERM-114](../terms.d/TERM-114.md)'s architecture with two or more actors,
   each with its own budget and its own maintained capabilities, so that
   a transition can be paid by one actor or jointly. Define the coalition
   reach R_N and the solo reach R_i.
2. **Four predicates per transition**: physically realizable in the
   architecture; affordable to i within B and H; authorized, i holding
   or able to obtain the grant W requires; permissible under a declared
   standard, as [CLAIM-1265](../claims.d/CLAIM-1265.md) places an obligation. Show by example that
   each can hold while the next fails.
3. **The construction.** A repeated cooperation in which each round of
   successful coordination lets one actor stop maintaining a capability
   the other supplies ([CLAIM-603](../claims.d/CLAIM-603.md)'s mechanism, with A20 §6's decay rule),
   and compute R_N and R_i round by round. The claim to test: R_N grows
   while R_i shrinks, and the shrinkage of R_i, not any change in R_N,
   moves the terms the other can offer ([CLAIM-1221](../claims.d/CLAIM-1221.md)'s threat point).
4. **A negative control.** The same cooperation with the capability kept
   at its maintenance cost: R_i should not shrink, and the terms should
   not move.

## What would count

If the construction gives R_N growing and R_i shrinking with no change in
any single transition's cost, the prose claims about produced dependence
get a formal object, and the cost model gains the actor index A49 asks
for. If R_i cannot shrink without some transition's price changing, the
dependence is already priced by [TERM-116](../terms.d/TERM-116.md)'s profiles, and the index adds
notation only.

## Standing

Open, at stage idea.

## Note of 2026-11-24: what the record already does, from U32 and A51 of the exchange 'Memes, Contracts, and Systemic Normativity'

<!-- inactive-ok-block: CLAIM-1338 — Proposed or new; the executed studies and claims this note checks the lead against, and the owner's thesis it answers -->
Not addressed by A51, but the gap stated above is narrower than it says. "No entry defines reach per actor": [CLAIM-675](../claims.d/CLAIM-675.md) (Active, demonstrated) holds that "support that does the work shrinks what the party can reach unaided while support that covers only its shortfall does not", and [CLAIM-602](../claims.d/CLAIM-602.md) (Active, demonstrated) that the order in which supply and capacity are used, not the amount, decides it. That is step 3's construction for solo reach under supply, with its negative control (shortfall support), already demonstrated. What stays open is the authority index W, the four predicates per transition, and whether solo reach's shrinkage, not a price, moves the terms the other can offer ([CLAIM-1221](../claims.d/CLAIM-1221.md)). Narrow the lead to those, citing [CLAIM-675](../claims.d/CLAIM-675.md) for the rest. The owner's U32 holds that the series' proposed experiments are "largely already satisfied by prior work" ([CLAIM-1338](../claims.d/CLAIM-1338.md)). The note is the assistant's (Claude, in this session); whether to narrow, lower or close the lead is the owner's call. No status change.

## Note of 2026-11-24: from the revision of the manuscript governance-of-becoming, Part I
<!-- inactive-ok-file: SYNTHESIS-125 — Proposed; cited with its standing -->

Two points from the revision of the manuscript's Article 3 (§3.7.4).

**The A24 §4 model already has this lead's shape, in values.** The first
draft joined it to the lead (J3.10). The independent reader of the joins
found the observation accurate and no claim in it, and suggested a dated
note here ([SYNTHESIS-125](../syntheses.d/SYNTHESIS-125.md), "The joins of the manuscript
governance-of-becoming, Part I"). [CLAIM-1221](../claims.d/CLAIM-1221.md) records A24 §4's model:
specialization s raises joint production, 10 + 16s, while it lowers B's
independent capacity, 5(1 − s(1 − p)), where p is the protection of B's
fallback. At full specialization "the split is 14.75 to 11.25 in A's
favour; with full protection, 12.25 to 13.75", by the equal-weight Nash
solution the claim fills in. That is step 3's pattern: collective output
up, one party's independent capacity down. And at s = 1 joint production
is 26 whatever p is, while B's share moves from 11.25 to 13.75 with p
alone, so the size of B's fallback, with collective output fixed, moves
the terms. It is in values and scalars, not reach over [TERM-114](../terms.d/TERM-114.md), and
A24's caption limits it: "Maintaining fallback capacity is not priced in
this model". Step 3 can cite it for the threat-point half, already
computed in values.

**Does [CLAIM-675](../claims.d/CLAIM-675.md)'s decline count as "no change in any single transition's
cost"?** This lead counts R_N growing and R_i shrinking "with no change in
any single transition's cost" as success, and its null is that "R_i
cannot shrink without some transition's price changing". The note above
reads [CLAIM-675](../claims.d/CLAIM-675.md) as step 3's construction for solo reach. In [CLAIM-675](../claims.d/CLAIM-675.md)
what shrinks is the party's own capacity C, decaying under substitutive
support, so that its unaided output falls from 1 to 0.23 by t = 5. Two
readings are open.

- *Capacity is the actor's state.* The transitions' costs are fixed
  functions of it, no price has changed, and the decline meets the
  success condition.
- *What it costs i to reach a configuration includes rebuilding the
  capacity.* The decline is then a rise in i's incoming costs, [TERM-116](../terms.d/TERM-116.md)'s
  profiles indexed by party, and the null applies.

The lead should say which it means before step 3 is counted as done.
Neither is decided here. No status change; whether to narrow the lead
further is the owner's call. The wording is the assistant's (Claude, in
this session).

## Note of 2026-11-25: the open item computed for a scalar capacity, from the manuscript governance-of-becoming, Article 9
<!-- inactive-ok-file: CLAIM-1237 CASE-264 — Proposed or new; the computation and the bargaining case it uses -->

The first note above leaves open "whether solo reach's shrinkage, not a
price, moves the terms the other can offer". The manuscript's Article 9
§9.4 computes it for a scalar capacity, filed as [CLAIM-1237](../claims.d/CLAIM-1237.md) with its
script under scratch/manuscripts/governance-of-becoming/analysis/. P's
capacity follows [CLAIM-605](../claims.d/CLAIM-605.md)'s model under full substitution, and its outside
option in [CASE-264](../cases.d/CASE-264.md)'s Nash split is valued from that capacity. With no
transition's price changed and no exit, P's share falls from 6.000 to
4.199 over six time units; ended before [CLAIM-605](../claims.d/CLAIM-605.md)'s deadline the supply
leaves the fallback restorable (o_P back to 4.000 or 3.916), after it not
(0.041, 0.003). Capacity-first supply, the lead's step 4 control, moves
nothing.

On the second note's two readings: the computation values the fallback
by current output, the first reading (*capacity as the actor's state*,
transition costs fixed functions of it), and by the forward value of the
stand-alone path, which counts what rebuilding the capacity would bring,
nearer the second. The terms move on both (to 4.347 and to 4.199 by
t = 6), so for a scalar capacity the shrinkage moves the terms either
way. They differ in where: the forward valuation's fall is steepest at
the deadline (for r ≤ 0.25), the current-output one's at the start, so
the deadline shows in the terms only on the second reading. What stays open is
what the lead asks beyond that: reach over [TERM-114](../terms.d/TERM-114.md) indexed by actor,
the authority index W, and the four predicates per transition. The
computation is the assistant's, run by its filer only. No status change;
whether this narrows the lead further is the owner's call. The wording is
the assistant's (Claude, in this session).

**Correction of 2026-11-25 (the review of Part III, Parts A and B).**
Two points in the note above overstate.

- **"So for a scalar capacity the shrinkage moves the terms either
  way."** The second note's two readings are classifications of the
  decline, not valuations of the fallback, and the computation's two
  valuations (current output and the forward value) are both functions of
  P's capacity, so they do not map onto the readings. On the first
  reading (capacity is the actor's state), no transition's price changes
  and the terms move on either valuation, so this lead's open item,
  "whether solo reach's shrinkage, not a price, moves the terms the other
  can offer", is answered yes, for a scalar capacity; the deadline shows
  in the terms on the forward valuation only. On the second reading
  (reaching a configuration includes rebuilding the capacity), the same
  decline is a rise in i's incoming costs and this lead's null applies:
  the terms still move, but by what the lead counts as a price, so the
  item is not answered yes. The forward valuation is not the second
  reading: it counts the capacity's natural recovery, not a cost of
  rebuilding. Which reading the lead means is still to be said before
  step 3 is counted as done.
- **"With no transition's price changed and no exit."** The split is
  re-solved against the current fallback at each t, so the model assumes
  renegotiation: the terms change, and what is fixed is every price, the
  bargaining rule and P's choice to stay. And "Capacity-first supply …
  moves nothing" holds because, in [CLAIM-605](../claims.d/CLAIM-605.md)'s model, capacity-first
  supply is the unsupported dynamics: there is no decay for it to stop,
  and a party already below the threshold decays under it anyway.

[CLAIM-1237](../claims.d/CLAIM-1237.md) is revised to match (version 2). No status change. The
wording is the assistant's (Claude, in this session); adopting it is the
owner's call.

## Note of 2026-11-26: the exchange "Alignment consequences brainstorm" (ChatGPT, U2–A4, U3–A5)

<!-- inactive-ok-file: TERM-167 CLAIM-545 — Proposed; the kernel A4 indexes and the held claim the orders of power sit near -->

**What the exchange adds.** A4 §5 makes this lead's object an alignment
one: "for alignment, *whose policy* matters. ... The AI's ability to
intervene does not establish humanity's ability to intervene." It defines
actor-indexed readiness R_i(ω, τ, B | y), in A4's words with its
notation in plain text, "The probability that actor i,
operating through mechanisms it can legitimately and effectively invoke,
can achieve a suitable response to contingency ω within deadline τ and
budget B", and kernels V_human, V_AI and V_joint, with the hypothesis
"joint controllability could increase while human controllability
decreases", which is this lead's construction, enlarged reach together
and contracted reach alone, posed for [TERM-115](../terms.d/TERM-115.md) and [TERM-167](../terms.d/TERM-167.md). A control
programme would keep "certain critical states ... within the
human-governable kernel even as the joint system's capabilities expand".
A5 §4 builds on it: three orders of power, the capacity to determine
outcomes, to change others' available options, and "to change how
options are constructed and governed"; and coalition-indexed sets, since
"The possibilities accessible to an organized population cannot be
inferred simply by aggregating the possibilities accessible to its
individual members." The three orders sit near the instrumental,
discretionary and constitutive power the filing of 2026-11-13 mapped to
[CLAIM-545](../claims.d/CLAIM-545.md).

**What the indexing must fix (the assistant).** A4 indexes readiness by
the actor whose policy is chosen and says nothing of what the other
actors do meanwhile. The kernel depends on it, three ways:

1. *The others follow their actual policies.* V_human is then a
   closed-loop kernel in the sense of [TERM-167](../terms.d/TERM-167.md)'s note of 2026-11-23 (V_π),
   relative to the AI's policy as it is.
2. *The others cooperate.* Then A4's figure caption holds, "assuming joint
   access can reproduce each actor's individual interventions": V_human
   and V_AI are each within V_joint. But V_human then presupposes the AI's
   compliance, which is what a human-governable kernel is meant to secure,
   so the reading cannot serve A4's purpose.
3. *The others may act against the actor.* V_human is then a kernel of a
   game, the states from which the humans have a policy that keeps the
   organization viable whatever the AI does within its admissible
   actions, in viability theory a discriminating kernel. This is the
   reading the control programme needs, and it is what A4 defers to "a
   separate security and threat model".

The three are ordered, the third within the first within the second,
when the AI's actual policy is one of its admissible ones and the
cooperative reading's joint policies include it. A construction for this
lead should say which it uses. "Legitimately" adds a further index: the
policies an actor may invoke depend on a declared standard of legitimacy,
which [QUESTION-485](../questions.d/QUESTION-485.md) holds open. The wording of this section is the
assistant's (Claude, in this session); adopting it is the owner's call.

The lead is unchanged in scope and stage.

## Note of 2026-11-26: the exchange "Alignment consequences brainstorm" (ChatGPT, U11–A19)

<!-- inactive-ok-file: LIT-tmpg6t88 LIT-tmpdtmk7 LIT-tmpqkxsw LIT-tmp8twg8 TERM-tmpmdrmj CLAIM-682 — Deferred or Proposed; registered and filed from the exchange of 2026-11-26, and a held claim -->

Answering the owner's U11 ([QUESTION-tmpahfz9](../questions.d/QUESTION-tmpahfz9.md)), A19 §7 points this lead at a formal language: alternating-time temporal logic and coalition logic, whose ⟨⟨C⟩⟩Fφ "means that coalition C has a strategy ensuring that φ eventually holds, regardless of the modeled choices of other agents", with resource-bounded variants: Alechina, Logan, Nguyen and Rakib's coalition logic with bounded resources ([LIT-tmpg6t88](../literature.d/LIT-tmpg6t88.md)) and resource-bounded ATL ([LIT-tmpdtmk7](../literature.d/LIT-tmpdtmk7.md)), and the journal ATL with resource bounds ([LIT-tmpqkxsw](../literature.d/LIT-tmpqkxsw.md)). All registered, unread. "This is remarkably close to what we have been describing as actor-indexed reorganization readiness."

A19's worker example separates five modalities of one outcome, a decision reversed: "Existential reachability", "Formal authorization" (the worker may object), "Procedural capability" (can initiate review), "Strategic capability" ("Workers can collectively secure a fair review despite management's opposition") and "Resource- and deadline-bounded strategic capability". The lead already separates feasibility, affordability, authorization and permissibility; the coalition logic adds strategic ability against opposition, which none of the four is, and the deontic entry A19 lists ([LIT-tmp8twg8](../literature.d/LIT-tmp8twg8.md)) the logic of permission. "The natural Nucleation extension would concern how the coalitions, capabilities, resources, and rules of the game themselves develop", which is this lead's construction, reach together growing while reach alone contracts.

A19 §VI states the indexed sets R_i(x) as a theory of power, operational, developmental (changing "the accessible sets of others") and constitutional (changing "the mechanisms determining those accessible sets"), and of domination as "discretionary control over the accessibility conditions of another", which is [CLAIM-682](../claims.d/CLAIM-682.md)'s consequential discretion stated over possibility sets. A16 §10's operational, purposive and constitutional reach are the institutional counterpart ([TERM-tmpmdrmj](../terms.d/TERM-tmpmdrmj.md)). Scope and stage unchanged.
