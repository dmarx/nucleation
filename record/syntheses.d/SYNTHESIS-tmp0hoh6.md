---
status: Proposed
title: 'A correspondence or a comparison of experiments says only what it is anchored to: an intertwining through an uninformative map is vacuous or lossy, so the map must be anchored to independently measured distinctions and evaluated on tasks other than those it was estimated on, and probes that train a system cannot also certify what it preserves; a map that nearly intertwines two operators carries their commutator within a bound linear in the defects; and over finite sets the directed gap in Bayes risk vanishes for every problem and prior exactly at Blackwell''s order, an exact fit of an outcome kernel is a garbling, and Le Cam''s deficiency is a linear programme whose value is the least uniform excess loss over every decision problem with losses in [0, 1]'
version: 1
defeated_if: >-
  A component misstated or misattributed here; an in-force component of
  the correspondence-and-deficiency part of the formal-apparatus line left
  out without a reason given; or a link this account states that no
  component states. Its standing is its components': a component retired
  or demoted takes its clause with it, and nothing here holds the clause
  up.
tags:
- mathematical-statistics
- model-comparison
- probabilistic-modeling
date: '2026-11-11'
line:
- formal-apparatus
integrates:
- CLAIM-011
- CLAIM-266
- CLAIM-373
- CLAIM-381
- CLAIM-380
- CLAIM-503
summary: >-
  A part account of the formal-apparatus line: what a correspondence
  between source and target, or a comparison between two experiments,
  can certify, and how the comparison is computed for finite experiments.
  Six entries that the mechanical map placed with the intervention and
  sufficiency entries, from which they are set apart because they barely
  link to them. Four also carry pragmatic-transport, and all four
  are set out already by that line's accounts. The line's account is
  built over this one. It adds nothing of its own; its standing is its
  components'.
---
<!-- inactive-ok-file: CLAIM-063 CLAIM-117 CLAIM-228 — Proposed; entries the components cite, with their standing -->
<!-- inactive-ok-file: SYNTHESIS-063 SYNTHESIS-064 — Proposed; pragmatic-transport accounts that already integrate components, named and not integrated -->
<!-- inactive-ok-file: ADR-075 ADR-083 ADR-084 — Proposed; the decisions this account is drafted under -->
<!-- inactive-ok-file: SYNTHESIS-tmp68daz SYNTHESIS-tmpa7ef9 SYNTHESIS-tmpdbary — Proposed; cited with its standing -->

# SYNTHESIS-tmp0hoh6: A correspondence or a comparison of experiments says only what it is anchored to: an intertwining through an uninformative map is vacuous or lossy, so the map must be anchored to independently measured distinctions and evaluated on tasks other than those it was estimated on, and probes that train a system cannot also certify what it preserves; a map that nearly intertwines two operators carries their commutator within a bound linear in the defects; and over finite sets the directed gap in Bayes risk vanishes for every problem and prior exactly at Blackwell's order, an exact fit of an outcome kernel is a garbling, and Le Cam's deficiency is a linear programme whose value is the least uniform excess loss over every decision problem with losses in [0, 1]

*A part account of the formal-apparatus line (ADR-083, ADR-084). The
line's account is built over it and over the accounts of the line's other
parts. The mechanical community map put these six entries in one part
with twenty entries on intervention, sufficiency and maintenance, which
the sibling account sets out. They are a second inquiry: five stored
pairs among the six, and one to the twenty, CLAIM-503's and CLAIM-517's
`complements` of each other, against 31 pairs among the twenty.*

*CLAIM-011, CLAIM-380, CLAIM-381 and CLAIM-503 also carry
pragmatic-transport, and that line's accounts integrate three of them:
SYNTHESIS-063 holds CLAIM-011, CLAIM-381 and CLAIM-503, and SYNTHESIS-064
holds CLAIM-380. This account integrates them again because their `line`
includes formal-apparatus. CLAIM-266 and CLAIM-373 carry formal-apparatus
only and have no other account.*

## The account

- **What anchors a correspondence.** CLAIM-011 (the assistant's objections
  at A34 and A40, with A40's remedy, recovered from drafts that dropped
  them, granted, demonstrated, Active): "a trivial map that collapses
  every state to one point could make the equation vacuously true", and
  "unless Φ is sufficiently informative, preserving its image of a
  commutator does not establish preservation of the entire commutator
  structure"; the remedy is to "Require state correspondences to be
  estimated on one collection of tasks and evaluated on another". It
  objects to CLAIM-117 "as stated, not to its truth".
- **What a training signal cannot certify.** CLAIM-266 (the assistant's
  restatement of CLAIM-149's general content, split at the owner's
  request, interpretive, Active): "When the two are the same probe family,
  evaluation measures fit to the training signal, not preservation", so
  "preservation has to be shown under probes the system was not trained
  against". It "does not say metrics in the training probes are
  worthless, only that they are not a certificate."
- **Carrying a commutator.** CLAIM-373 (the manuscript's identity, split
  from CLAIM-063 and proved, demonstrated, Active): with defects
  E_A = ΦA − A′Φ and E_B = ΦB − B′Φ,
  Φ[A,B] − [A′,B′]Φ = A′E_B + E_A B − B′E_A − E_B A, so the commutator is
  carried within (‖A‖ + ‖A′‖)‖E_B‖ + (‖B‖ + ‖B′‖)‖E_A‖. It does not say
  "That the defects can be read off data", nor "That the commutator
  structure of the source is preserved. Only its image under Φ is
  (CLAIM-011)."
- **A directed decision term.** CLAIM-380 (steps (a) to (d) of CLAIM-326 on
  the finite case, split at the owner's direction, demonstrated, Active):
  D⁺_Q(U → V; π) is directed, zero from a garbling back to its source,
  vanishes for every finite problem and prior exactly when the rendering
  is at least as informative as the source (Blackwell's Theorem 6,
  THEORY-717), and has A86's D_Q as its symmetrization. It "does not state
  the prior-free form or the relation to Le Cam's deficiency".
- **Kernels and their computation.** CLAIM-381 (the derivational core of
  CLAIM-228, split at the owner's direction, demonstrated, Active): a
  constant kernel "fails the condition" whenever the averaged target
  responses vary with the item, an exact fit "is a garbling, with the item
  as the common parameter", and Le Cam's deficiency between the two finite
  tables "is one linear programme". It "does not say the restated measure
  tells rendering procedures apart", which is CLAIM-228's empirical
  question.
- **The randomization criterion.** CLAIM-503 (the status review's
  re-derivation of Le Cam's criterion from Han's lecture, demonstrated,
  Active): over finite sets, one experiment is ε-deficient relative to
  another in every decision problem with losses in [0, 1] "exactly when a
  single Markov kernel brings it within ε in total variation at every
  state"; "At ε = 0 this is the finite Blackwell–Sherman–Stein theorem".

## The components

- CLAIM-011, the assistant's (A34 §3 and A40 §6.4, remedy A40 §8.4),
  recovered by the record, granted, demonstrated, Active; first line
  pragmatic-transport, also formal-apparatus (ADR-040, group C); objects
  to CLAIM-117; undercuts ARG-006.
- CLAIM-266, the assistant's restatement, split from CLAIM-149 under
  ADR-040 at the owner's request, thesis, interpretive, Active;
  formal-apparatus only; grounds CASE-041.
- CLAIM-373, the manuscript's §9 identity, split from CLAIM-063 at the
  owner's direction, thesis, demonstrated, Active; formal-apparatus only;
  uses TERM-024.
- CLAIM-380, split from CLAIM-326 at the owner's direction, thesis,
  demonstrated, Active; first line pragmatic-transport; grounds
  THEORY-717.
- CLAIM-381, split from CLAIM-228 at the owner's direction, thesis,
  demonstrated, Active; first line pragmatic-transport; rests on
  CLAIM-011; grounds THEORY-717.
- CLAIM-503, filed at the twenty-first status review at its ruling, the
  re-derivation the record's, thesis, demonstrated, Active; first line
  formal-apparatus, also pragmatic-transport; rests on CLAIM-381; grounds
  LIT-1847; complements CLAIM-517.

## Links the components state, and where

- **The remedy as a premise.** CLAIM-381 rests on CLAIM-011: its fidelity
  condition "is scored on held-out items, which is CLAIM-011's remedy."
- **The image only.** CLAIM-373's limits: "That the commutator structure
  of the source is preserved. Only its image under Φ is (CLAIM-011)."
- **Training probes.** CLAIM-266's summary: filed alone "so that it does
  not rest on CLAIM-011's account of correspondences in translation".
  CLAIM-011's note of 2026-10-10 names the same step through CLAIM-149,
  which rests on CLAIM-266: "Its remedy carried from correspondences to
  training objectives: a probe family that trains a transformation cannot
  certify it".
- **Deficiency.** CLAIM-503 rests on CLAIM-381: its δ "is CLAIM-381's
  linear programme", and its limits leave "the deficiency restricted to a
  family Q of problems" to "CLAIM-381's finite computation, and it is
  bounded by this one". Its "Connections": CLAIM-326 and CLAIM-380 do not
  state the prior-free form, and "This claim states that form for finite
  sets". CLAIM-380 and CLAIM-381 share THEORY-717 as ground and do not
  cite each other.

## Links to other parts, stated

Outgoing: none. No component here relates to, or names, an entry of
another part of the line.

Incoming, stated by entries of other parts:

- **Effective description (SYNTHESIS-tmpa7ef9).** CLAIM-264's summary: filed alone "so
  that it does not rest on CLAIM-046 and CLAIM-011, which are about
  pragmatic identity", and its body names "the remedy of anchored
  correspondences (CLAIM-011)". CLAIM-322: "The rule is CLAIM-011's remedy
  applied to probes".
- **Frustration (SYNTHESIS-tmp68daz).** CLAIM-265 is filed alone so that "the order of
  tests does not rest on CLAIM-011", and CLAIM-143 rests on CLAIM-011 for
  its application. CLAIM-495: "CLAIM-373's bound on carrying commutators
  and LIT-1820's holonomy measure different things."
- **Naming (SYNTHESIS-tmpdbary).** CLAIM-132 puts "CLAIM-011's anti-collapse condition
  into a character setting".

Across to the sibling account of this part: CLAIM-503 and CLAIM-517
complement each other, in front matter only.

## Not stated on the record

Links across the components that no entry states, tested by ADR-075's
step 5 and not filed:

- **Fidelity where it was fitted certifies nothing.** That agreement
  measured where a map or a system was estimated or trained never
  certifies what it preserves (CLAIM-011's remedy, CLAIM-266), joined to the
  sibling part's CLAIM-517. As a universal it is false by CLAIM-517's
  coverage step, under which a training loss that sees the full response
  at every boundary context does certify viability. As "need not
  certify" it is the held instances. The narrower sentence leaves "the
  contexts that decide" free.
- **The deficiency as the measure of anchoring.** That Le Cam's
  deficiency (CLAIM-503) measures how far a correspondence falls short of
  CLAIM-011's anchoring. CLAIM-381 already states the parts that hold: a
  constant kernel fails the across-items condition, and scoring is on
  held-out items, "which is CLAIM-011's remedy". Beyond that the sentence
  has no derivation, and "anchored" is CLAIM-011's informal word.
- **Blackwell at both ends.** That CLAIM-380's vanishing for every problem
  and prior is CLAIM-503's δ = 0. CLAIM-503 states it ("At ε = 0 this is
  the finite Blackwell–Sherman–Stein theorem") and its "Connections" names
  CLAIM-380.

## What it does not say

- That any measure here tells rendering procedures apart (CLAIM-381,
  CLAIM-503; CLAIM-228's question).
- Anything for infinite outcome spaces (CLAIM-380, CLAIM-503).
- That defects or correspondences can be read off data (CLAIM-373).
- Anything with standing of its own.
