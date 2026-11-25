---
status: Open
title: 'Index the resource-bounded constraint system''s reachability by actor and by authority, and construct a cooperation in which repeated successful coordination enlarges what the participants can reach together while contracting what one of them can reach alone, separating physical feasibility, affordability, authorization and permissibility of each transition'
version: 1
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
- CLAIM-tmpdu9v6
- CLAIM-tmp2jhc1
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
<!-- inactive-ok-file: CLAIM-1016 CLAIM-603 CLAIM-670 CLAIM-tmp2jhc1 CLAIM-tmpdu9v6 TERM-116 — Proposed, Rejected or new; entries this one reads or rests on, cited whatever their standing -->

# LEAD-tmpeo8wq: Index the resource-bounded constraint system's reachability by actor and by authority, and construct a cooperation in which repeated successful coordination enlarges what the participants can reach together while contracting what one of them can reach alone, separating physical feasibility, affordability, authorization and permissibility of each transition

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
  ([CLAIM-tmpdu9v6](../claims.d/CLAIM-tmpdu9v6.md)), and the cost of authorization placed between
  formulating and investigating ([CLAIM-1016](../claims.d/CLAIM-1016.md));
- the fallback that matters without being used, by changing the terms
  others offer ([CLAIM-tmp2jhc1](../claims.d/CLAIM-tmp2jhc1.md)).

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
   standard, as [CLAIM-tmpdu9v6](../claims.d/CLAIM-tmpdu9v6.md) places an obligation. Show by example that
   each can hold while the next fails.
3. **The construction.** A repeated cooperation in which each round of
   successful coordination lets one actor stop maintaining a capability
   the other supplies ([CLAIM-603](../claims.d/CLAIM-603.md)'s mechanism, with A20 §6's decay rule),
   and compute R_N and R_i round by round. The claim to test: R_N grows
   while R_i shrinks, and the shrinkage of R_i, not any change in R_N,
   moves the terms the other can offer ([CLAIM-tmp2jhc1](../claims.d/CLAIM-tmp2jhc1.md)'s threat point).
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

<!-- inactive-ok-block: CLAIM-tmpyp0ju — Proposed or new; the executed studies and claims this note checks the lead against, and the owner's thesis it answers -->
Not addressed by A51, but the gap stated above is narrower than it says. "No entry defines reach per actor": [CLAIM-675](../claims.d/CLAIM-675.md) (Active, demonstrated) holds that "support that does the work shrinks what the party can reach unaided while support that covers only its shortfall does not", and [CLAIM-602](../claims.d/CLAIM-602.md) (Active, demonstrated) that the order in which supply and capacity are used, not the amount, decides it. That is step 3's construction for solo reach under supply, with its negative control (shortfall support), already demonstrated. What stays open is the authority index W, the four predicates per transition, and whether solo reach's shrinkage, not a price, moves the terms the other can offer ([CLAIM-tmp2jhc1](../claims.d/CLAIM-tmp2jhc1.md)). Narrow the lead to those, citing [CLAIM-675](../claims.d/CLAIM-675.md) for the rest. The owner's U32 holds that the series' proposed experiments are "largely already satisfied by prior work" ([CLAIM-tmpyp0ju](../claims.d/CLAIM-tmpyp0ju.md)). The note is the assistant's (Claude, in this session); whether to narrow, lower or close the lead is the owner's call. No status change.
