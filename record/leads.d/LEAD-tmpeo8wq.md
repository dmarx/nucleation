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
  existing TERM-114 and CASE-326 machinery to actor-indexed resource and
  transformation profiles", R_i(S; B, H, W), the states reachable by i
  under budget, horizon and authority, and "Investigate when recurrent
  successful coordination expands collective reach while contracting the
  independent reach of particular participants." TERM-114 indexes
  reachability by a budget, not by an actor or an authority. Stage idea:
  the object is named, not defined. The wording is A's (ChatGPT, in the
  exchange 'Memes, Contracts, and Systemic Normativity'); the construction
  asked for is the assistant's (Claude, in this session); adopting either
  is the owner's call.
---
<!-- inactive-ok-file: CASE-326 CLAIM-1016 CLAIM-603 CLAIM-670 CLAIM-tmp2jhc1 CLAIM-tmpdu9v6 TERM-116 — Proposed, Rejected or new; entries this one reads or rests on, cited whatever their standing -->

# LEAD-tmpeo8wq: Index the resource-bounded constraint system's reachability by actor and by authority, and construct a cooperation in which repeated successful coordination enlarges what the participants can reach together while contracting what one of them can reach alone, separating physical feasibility, affordability, authorization and permissibility of each transition

## The gap

A49, Article 3, "Formal and experimental center":

R_i(S; B, H, W) = {S' : S' is reachable by i under B, H, W}.

"Investigate when recurrent successful coordination expands collective
reach while contracting the independent reach of particular participants."
And §7, "Authority-sensitive cost landscapes. Distinguish physical
feasibility, affordability, authorization and normative permissibility."

What the record holds:

- reachability indexed by a partially ordered budget (TERM-114), and the
  threshold for reaching a state apart from the cost of keeping it
  (CLAIM-571);
- the relational profiles of a configuration, incoming, outgoing and
  observational (TERM-116), not indexed by who pays;
- in prose, the capability lost because another supplies it (CLAIM-603)
  and the dependence an arrangement produces by supplying (CLAIM-670);
- an obligation as a condition on permissible transitions, not a cost
  (CLAIM-tmpdu9v6), and the cost of authorization placed between
  formulating and investigating (CLAIM-1016);
- the fallback that matters without being used, by changing the terms
  others offer (CLAIM-tmp2jhc1).

No entry defines reach per actor, or separates the four predicates on a
transition in one formal object, so "collective reach grows while
independent reach shrinks" is held only as prose about dependence.

## What it would take

1. **Define R_i.** Fix TERM-114's architecture with two or more actors,
   each with its own budget and its own maintained capabilities, so that
   a transition can be paid by one actor or jointly. Define the coalition
   reach R_N and the solo reach R_i.
2. **Four predicates per transition**: physically realizable in the
   architecture; affordable to i within B and H; authorized, i holding
   or able to obtain the grant W requires; permissible under a declared
   standard, as CLAIM-tmpdu9v6 places an obligation. Show by example that
   each can hold while the next fails.
3. **The construction.** A repeated cooperation in which each round of
   successful coordination lets one actor stop maintaining a capability
   the other supplies (CLAIM-603's mechanism, with A20 §6's decay rule),
   and compute R_N and R_i round by round. The claim to test: R_N grows
   while R_i shrinks, and the shrinkage of R_i, not any change in R_N,
   moves the terms the other can offer (CLAIM-tmp2jhc1's threat point).
4. **A negative control.** The same cooperation with the capability kept
   at its maintenance cost: R_i should not shrink, and the terms should
   not move.

## What would count

If the construction gives R_N growing and R_i shrinking with no change in
any single transition's cost, the prose claims about produced dependence
get a formal object, and the cost model gains the actor index A49 asks
for. If R_i cannot shrink without some transition's price changing, the
dependence is already priced by TERM-116's profiles, and the index adds
notation only.

## Standing

Open, at stage idea.
