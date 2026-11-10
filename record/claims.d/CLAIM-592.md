---
number: 592
status: Active
formerly:
- CLAIM-tmpy6y22
title: 'Whether a system''s own reachable classes ever coincide with what an observer can tell apart depends on the order of the observer''s probe costs as well as on the mechanism: the two partitions agree exactly at partitions common to the observer''s refinement chain and the system''s merge tree, a level of the merge tree can be made to agree under some cost order exactly when it is the common refinement of some set of the available probes, and the cost order decides which of those levels actually appear'
version: 3
history:
- version: 2
  date: '2026-11-06'
  note: >-
    Promoted at the twenty-seventh status review (ADR-057), at the status
    review's ruling (the owner delegated these rulings). CASE-206 leaves
    grounds and illustrates the claim instead: its four points are argued
    for any finite system, and the vertex is the instance the body works.
    Its premises, CLAIM-570, CLAIM-581 and CLAIM-574, are Active, no
    objection is filed, and the argument and the vertex's two cost orders
    were re-checked, the latter in scratch/formal/case206_check.py.
    Nothing in the record meets its defeated_if.
- version: 3
  date: '2026-11-07'
  note: >-
    At the third synthesis review of 2026-11-07: the summary's cost order at CASE-206's
    vertex held only with flatness and mode at the case's costs. Over all 24
    orders of the four probes the middle level appears in 8, exactly when
    depth is dearer than both mode and side; the summary now says so. Title
    and defeater unchanged.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the argument: a system, under nested probe families and
  peak-cost mutual reachability, in which O_o = A_a for a partition absent
  from one of the two chains; a level of the merge tree that is the common
  refinement of a set of probes and yet agrees under no cost order; or one
  that agrees under some cost order without being such a refinement. Not
  defeated by probe families that are not nested or by costs that are not
  peak costs, which the claim excludes.
tags:
- individuation
- mathematics
- epistemology
date: '2026-11-05'
line:
- realizability
- formal-apparatus
rests_on:
- CLAIM-570
- CLAIM-581
- CLAIM-574
bears_on:
- QUESTION-374
summary: >-
  The assistant's own proposition, filed on 2026-11-05 at the owner's
  request after the frontiers of [CLAIM-570](CLAIM-570.md) were computed on the
  degree-4 vertex. As the observing budget rises, the observer's partitions
  form a chain, each the common refinement of the probes affordable so far;
  as the acting budget rises, the system's reachable classes form another,
  the levels of its merge tree. The two partitions agree exactly at
  partitions both chains contain. Reordering probe costs changes only the
  first chain, so a level of the merge tree can be brought into agreement
  under some cost order exactly when it is the common refinement of some
  set of the available probes (put that set first), and the actual order
  decides which such levels appear. On the vertex, flat and the four
  half-branches agree exactly when depth is dearer to observe than both
  mode and side, in 8 of the 24 orders of the four probes; with flatness
  and mode at CASE-206's costs, that is when side is cheaper than depth. Checked on 1,500 random systems over every cost
  order. So whether a mechanism's own kinds are visible as individuals is a
  joint fact about what it can become, what can be measured, and what is
  cheap to measure first. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
complements:
- CLAIM-572
---

# CLAIM-592: Whether a system's own reachable classes ever coincide with what an observer can tell apart depends on the order of the observer's probe costs as well as on the mechanism: the two partitions agree exactly at partitions common to the observer's refinement chain and the system's merge tree, a level of the merge tree can be made to agree under some cost order exactly when it is the common refinement of some set of the available probes, and the cost order decides which of those levels actually appear

## The claim

Fix a finite system, a finite set of probes, each a partition of the
states with a cost, and peak costs on reversible moves.

1. **Two chains.** Order the probes by cost, p₁, …, p_k. As o rises, O_o
   runs through the chain π₀ ⊇ π₁ ⊇ … ⊇ π_k, where π_j is the common
   refinement of p₁, …, p_j and π₀ puts everything in one class. As a
   rises, A_a runs through the levels of the merge tree of [CLAIM-581](CLAIM-581.md),
   from all-apart to the components of the move graph.
2. **Agreement.** O_o = A_a exactly when the two are the same partition,
   so the partitions on which they ever agree are the partitions in both
   chains. Each agreement holds on a rectangle, [o_j, o_(j+1)) × [a_i,
   a_(i+1)), between consecutive changes of each chain ([CLAIM-570](CLAIM-570.md)).
3. **What the order can do.** Changing the probe costs changes the first
   chain and not the second. Every partition in the first chain is the
   common refinement of some set of probes. Conversely, any such
   refinement appears in the first chain for the cost order that puts its
   probes first. So a level P of the merge tree agrees under some cost
   order exactly when P is the common refinement of some set of the
   probes.
4. **What it cannot do.** No cost order makes a level agree that no set of
   probes refines to. And one order makes two levels P and Q both agree
   only if they come from nested probe sets, T_P ⊆ T_Q with P the
   refinement of T_P and Q of T_Q, since the observer's chain adds probes
   one at a time in cost order. Two levels reachable only from incomparable
   probe sets can each be brought into view, but not under one order.

Checked with python3 -I: on 1,500 random systems of six states, with four
random three-valued probes and random peak costs, the levels that agree
under some one of the 24 cost orders were exactly the levels that are
common refinements of probe subsets, every time.

## The vertex

On [CASE-206](../cases.d/CASE-206.md)'s nine states, the merge tree's middle level is the flat
state with the four half-branches, which is the common refinement of the
flatness, mode and side probes. With costs in that order and depth last,
that level is in the observer's chain and the two partitions agree on it.
With depth costing less than side, the first three probes are flatness,
mode and depth. Their refinement splits each mode into deep and shallow
and does not separate the sides, so it is no level of the merge tree. The
later refinement, all apart, agrees only in the trivial corner.

## What it adds

- **Three contributions kept apart.** What the mechanism can become fixes
  the merge tree. What can be measured at all fixes which of its levels are
  candidates (refinements of probe sets). What is cheap to measure first
  fixes which candidates actually show up as individuals both from outside
  and from inside. [CLAIM-557](CLAIM-557.md) said individuation is indexed by two
  budgets; this says what decides whether those budgets ever see the same
  thing.
- **A design lever.** An organization or an instrument-maker who can change
  what is cheap to observe can bring a chosen level of the system's own
  structure into view, if and only if some set of available probes refines
  to it.

## What it does not say

- It needs nested probe families and peak-cost reachability, as
  [CLAIM-570](CLAIM-570.md) does.
- It says nothing about which cost order is natural for a given observer;
  that is empirical.
- Agreement of the two partitions is a fact about identification under
  budgets. Whether the agreed classes are individuals in any constitutive
  sense stays with [QUESTION-284](../questions.d/QUESTION-284.md).

## Note of 2026-11-05: the DNA origami readings

Read on the owner's request to connect the record's realizability inquiry to DNA origami; the works were chosen by the assistant.

**Wagenbauer, Wachauf and Dietz, "Quantifying quality in DNA self-assembly".** Wagenbauer, Wachauf and Dietz (2014), [LIT-2128](../literature.d/LIT-2128.md), read in [NOTE-1637](../notes.d/NOTE-1637.md), support the claim in
kind: the cheap defect label splits samples by ensemble composition and the costly cryo-EM, by the
authors' account, would split them by shared site-specific defects, so which distinctions are
bought first depends on which probe is cheap. No costed probe family is set out.

No status changes.

## Note of 2026-11-05: the further DNA origami readings

The works cited in A's two syntheses on DNA origami, pasted by the owner on 2026-11-05, read in this pull request.

**Majikes, Hasni, Haridas, Robertson, Pintar, Zwolak and Liddle, "Complex cooperativity in DNA origami revealed via design-dependent defectivity".** Majikes et al. (2026), [LIT-2127](../literature.d/LIT-2127.md), support the claim at the level of example. They state that "yield measurements have an inverse relationship between their resolution and both their cost and throughput", from gels to AFM to DNA-PAINT. Their AFM classes are "a very approximate substitute" for staple counts. The cheaper probe is not a coarsening of the dearer one:
- The gel merges a damaged design with well-folded ones.
- It also splits well-folded designs by mobility.

This bears on [CLAIM-574](CLAIM-574.md)'s nesting of probe families. No probe costs are quantified.

No status changes.
