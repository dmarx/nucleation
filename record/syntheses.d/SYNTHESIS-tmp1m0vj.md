---
status: Proposed
title: 'Reaching a configuration has a resource threshold of its own, the least peak over admissible paths, which can exceed what holding either end takes and is relative to a fixed architecture; feasible, reachable and reliably reached come apart, failures of a transition have distinct remedies, a form needs separate resources to build, keep and move, several resources give a non-convex frontier rather than a total, and a budget set to last period''s spending loses every transition that needs slack with no sign in output'
version: 2
history:
- version: 2
  date: '2026-11-10'
  note: >-
    At the split of readiness (ADR-tmptlkel), the third part became the
    line transient-support. The introduction and the heading of the links
    across say so; the components and links are unchanged.
defeated_if: >-
  A component misstated or misattributed here; an in-force component of
  the reaching-and-paying part of the readiness line left out without a
  reason given; or a link this account states that no component states.
  Its standing is its components': a component retired or demoted takes
  its clause with it, and nothing here holds the clause up.
tags:
- operations-research
- mathematics
- complex-systems
date: '2026-11-10'
line:
- readiness
integrates:
- CLAIM-571
- CLAIM-567
- CLAIM-568
- CLAIM-556
- CLAIM-569
- CLAIM-585
- CLAIM-580
- CLAIM-577
- CLAIM-579
- CLAIM-572
- CLAIM-598
- TERM-105
- TERM-106
- CASE-198
- CASE-200
- CASE-201
- CASE-205
- CASE-206
- CASE-209
- CASE-211
- CASE-215
- QUESTION-392
- QUESTION-400
- QUESTION-404
---
<!-- inactive-ok-file: CASE-198 CASE-200 CASE-201 CASE-205 CASE-209 CASE-210 CASE-211 CASE-215 TERM-107 TERM-110 TERM-112 — Proposed; components and citations, with their standing -->

# SYNTHESIS-tmp1m0vj: Reaching a configuration has a resource threshold of its own, the least peak over admissible paths, which can exceed what holding either end takes and is relative to a fixed architecture; feasible, reachable and reliably reached come apart, failures of a transition have distinct remedies, a form needs separate resources to build, keep and move, several resources give a non-convex frontier rather than a total, and a budget set to last period's spending loses every transition that needs slack with no sign in output

*A part account of the readiness line: the part filed from the pasted
synthesis on constraint architectures (2026-11-04) and the assistant's
propositions offered after it. Most of its entries also carry
realizability, where four of its claims are first. The line's account is
built over it and its sibling part. A third part, withdrawing transient
support, became the line transient-support at the split of readiness
([ADR-tmptlkel](../decisions.d/ADR-tmptlkel.md)).*

## The account

- **The threshold.** [CLAIM-571](../claims.d/CLAIM-571.md) (A's, demonstrated, Active): for a fixed
  architecture and one capacity, the threshold for reaching a target "is
  the least, over admissible transition paths, of the peak requirement
  along the path, and it is infinite when no admissible path joins the
  two". [TERM-106](../terms.d/TERM-106.md) (A's, made exact by the filer, Active) names the gap
  above the costlier endpoint reconfiguration slack, with a one-sided form
  from where the system is and a set-valued form for several resources;
  A: "Slack isn't merely unused capacity held in reserve against
  disturbances." [TERM-105](../terms.d/TERM-105.md) (A's, Active) sorts resource constraints by the
  function of a path they bound, so the peak is one type of six. The
  instances: [CASE-206](../cases.d/CASE-206.md) (the filer's, Active), a degree-4 origami vertex
  whose switch costs 1.866 against ends of 0.75 and 0.875; [CASE-198](../cases.d/CASE-198.md) (the
  filer's numbers on A's sequence, Proposed), where admitting a change of
  architecture lowers the threshold from 1.3 to 1.0; [CASE-211](../cases.d/CASE-211.md) (A's
  example, Proposed), time for peak; [CASE-201](../cases.d/CASE-201.md) (the filer's numbers,
  Proposed), fixed material and variable usable capacity.
- **What the threshold separates.** [CLAIM-567](../claims.d/CLAIM-567.md) (the filer's construction
  from A's separations, demonstrated, Active): feasible, reachable and
  reliably reached are three properties, "each implied by the next and
  none implying it". [CASE-209](../cases.d/CASE-209.md) (the filer's times, Proposed) puts
  sequential capability between them for one squad: "Its repertoire is
  broader than its simultaneous service capacity." [CLAIM-568](../claims.d/CLAIM-568.md) (A's,
  interpretive, Active) sorts failed transitions into four obstructions
  with different remedies, and "added actuation can overcome an energy
  barrier and cannot join disconnected configurations"; [CASE-205](../cases.d/CASE-205.md) (the
  filer's instance, Proposed) is its control limitation. [CLAIM-556](../claims.d/CLAIM-556.md) (A's,
  interpretive, Active) adds compatibility before the four and
  regeneration after them, so "a diagnosis runs through six levels, each
  with its own repair"; whether missing information is a further level is
  [QUESTION-404](../questions.d/QUESTION-404.md) (Open). Whether an intervention creates a capability or
  only cheapens one is [QUESTION-392](../questions.d/QUESTION-392.md) (A's, Open).
- **What a form costs.** [CLAIM-569](../claims.d/CLAIM-569.md) (the filer's construction from A's,
  demonstrated, Active): constructing, maintaining and moving a form are
  three requirements, none fixing another, so "having enough to sustain
  it is not having enough to acquire it". [CLAIM-585](../claims.d/CLAIM-585.md) (the filer's
  construction from A's toy, demonstrated, Active): with several
  resources the sufficient budgets are upward-closed and can be
  non-convex, so "no threshold on a weighted total of the resources
  describes it". [CLAIM-580](../claims.d/CLAIM-580.md) (the assistant's, demonstrated, Active): the
  threshold does not amplify error, since "a planner who knows each
  configuration's cost to within ε knows a transition's threshold to
  within ε". [CLAIM-579](../claims.d/CLAIM-579.md) (the assistant's hypothesis, interpretive, Active):
  a reserve has a location, so "an organization can hold ample slack and
  still be pinned".
- **How a budget rule removes options.** [CLAIM-577](../claims.d/CLAIM-577.md) (the assistant's,
  demonstrated, Active): a budget set each period to the last period's
  peak spending never rises, and holding a configuration loses every
  transition that needs slack from it; "The loss leaves no trace in
  output." [CASE-200](../cases.d/CASE-200.md) (the filer's reading of A's recursion, Proposed) is
  the same numbers under carry-over, where the transition survives, and
  under expiry or a cut on unspent funds, where it does not.
- **Observing against acting, and abundance.** [CLAIM-572](../claims.d/CLAIM-572.md) (the
  assistant's, demonstrated, Active): when observing and acting share one
  budget, the cheapest readiness buys a prefix of the probes, the
  affordable splits can be disconnected, and greedy stopping can miss the
  least total. [CLAIM-598](../claims.d/CLAIM-598.md) (the assistant's, demonstrated, Active): whether
  more of every resource helps an assembly turns on whether the competing
  steps consume it, so "Slack held as uniform surplus is not neutral."
  [CASE-215](../cases.d/CASE-215.md) (the assistant's, Proposed) gives its timing at equal
  integrated exposure, and [QUESTION-400](../questions.d/QUESTION-400.md) (A's, Open) asks whether
  reallocating a fixed stock selects the form that results.

## The components

- [CLAIM-571](../claims.d/CLAIM-571.md), A's wording, thesis, demonstrated, Active; lines readiness,
  realizability, formal-apparatus.
- [CLAIM-567](../claims.d/CLAIM-567.md), the filer's construction, thesis, demonstrated, Active;
  first line realizability; rests on [CLAIM-571](../claims.d/CLAIM-571.md).
- [CLAIM-568](../claims.d/CLAIM-568.md), A's, thesis, interpretive, Active; first line
  realizability; rests on [CLAIM-571](../claims.d/CLAIM-571.md).
- [CLAIM-556](../claims.d/CLAIM-556.md), A's, thesis, interpretive, Active; first line
  realizability; rests on [CLAIM-568](../claims.d/CLAIM-568.md), [CLAIM-566](../claims.d/CLAIM-566.md), [CLAIM-347](../claims.d/CLAIM-347.md) and [CLAIM-586](../claims.d/CLAIM-586.md).
- [CLAIM-569](../claims.d/CLAIM-569.md), the filer's construction, thesis, demonstrated, Active;
  rests on [CLAIM-571](../claims.d/CLAIM-571.md); uses [TERM-105](../terms.d/TERM-105.md).
- [CLAIM-585](../claims.d/CLAIM-585.md), the filer's construction, thesis, demonstrated, Active;
  rests on [CLAIM-571](../claims.d/CLAIM-571.md).
- [CLAIM-580](../claims.d/CLAIM-580.md), the assistant's, thesis, demonstrated, Active; rests on
  [CLAIM-571](../claims.d/CLAIM-571.md).
- [CLAIM-577](../claims.d/CLAIM-577.md), the assistant's, thesis, demonstrated, Active; rests on
  [CLAIM-571](../claims.d/CLAIM-571.md); uses [TERM-106](../terms.d/TERM-106.md).
- [CLAIM-579](../claims.d/CLAIM-579.md), the assistant's, thesis, interpretive, Active; uses
  [TERM-106](../terms.d/TERM-106.md); grounds [THEORY-1418](../theory.d/THEORY-1418.md).
- [CLAIM-572](../claims.d/CLAIM-572.md), the assistant's, thesis, demonstrated, Active; rests on
  [CLAIM-535](../claims.d/CLAIM-535.md), [CLAIM-570](../claims.d/CLAIM-570.md) and [CLAIM-574](../claims.d/CLAIM-574.md).
- [CLAIM-598](../claims.d/CLAIM-598.md), the assistant's, thesis, demonstrated, Active; first line
  realizability; grounds [CASE-217](../cases.d/CASE-217.md).
- [TERM-105](../terms.d/TERM-105.md) and [TERM-106](../terms.d/TERM-106.md), A's, Active; [TERM-106](../terms.d/TERM-106.md) refines [TERM-107](../terms.d/TERM-107.md).
- [CASE-206](../cases.d/CASE-206.md), the filer's, construction, Active; first line realizability;
  illustrates [CLAIM-571](../claims.d/CLAIM-571.md), [CLAIM-567](../claims.d/CLAIM-567.md), [CLAIM-572](../claims.d/CLAIM-572.md) and [CLAIM-592](../claims.d/CLAIM-592.md).
- [CASE-198](../cases.d/CASE-198.md), [CASE-200](../cases.d/CASE-200.md), [CASE-201](../cases.d/CASE-201.md), [CASE-205](../cases.d/CASE-205.md), [CASE-209](../cases.d/CASE-209.md) and [CASE-211](../cases.d/CASE-211.md),
  constructions on A's models with the filer's numbers, Proposed.
- [CASE-215](../cases.d/CASE-215.md), the assistant's, construction, Proposed; first line
  realizability; illustrates [CLAIM-562](../claims.d/CLAIM-562.md) and [CLAIM-598](../claims.d/CLAIM-598.md).
- [QUESTION-392](../questions.d/QUESTION-392.md) and [QUESTION-400](../questions.d/QUESTION-400.md), A's, Open; [QUESTION-404](../questions.d/QUESTION-404.md), moved from
  [CLAIM-568](../claims.d/CLAIM-568.md)'s defeat condition by the twenty-sixth status review, Open.
  All three are first in realizability.

## Links the components state, and where

- **Everything rests on the threshold.** [CLAIM-567](../claims.d/CLAIM-567.md), [CLAIM-568](../claims.d/CLAIM-568.md), [CLAIM-569](../claims.d/CLAIM-569.md),
  [CLAIM-577](../claims.d/CLAIM-577.md), [CLAIM-580](../claims.d/CLAIM-580.md) and [CLAIM-585](../claims.d/CLAIM-585.md) rest on [CLAIM-571](../claims.d/CLAIM-571.md); [CASE-198](../cases.d/CASE-198.md),
  [CASE-200](../cases.d/CASE-200.md) and [CASE-206](../cases.d/CASE-206.md) illustrate it.
- **Reachability between feasibility and reliability.** [CLAIM-568](../claims.d/CLAIM-568.md)'s
  summary: the four obstructions "refine the gaps between [CLAIM-567](../claims.d/CLAIM-567.md)'s
  feasible, reachable and reliable". [CASE-209](../cases.d/CASE-209.md): its sequential property
  sits between the two others "as [CLAIM-567](../claims.d/CLAIM-567.md)'s reachability sits between
  feasibility and reliability".
- **The levels.** [CLAIM-556](../claims.d/CLAIM-556.md)'s summary: four levels are [CLAIM-568](../claims.d/CLAIM-568.md)'s
  obstructions and the sixth is [CLAIM-566](../claims.d/CLAIM-566.md)'s regeneration.
- **The rule and the reserve.** [CLAIM-577](../claims.d/CLAIM-577.md) sets its rule against
  [CASE-200](../cases.d/CASE-200.md)'s carry-over; [CASE-200](../cases.d/CASE-200.md) calls the unspent 0.3 a
  reconfiguration reserve built in installments and organizational slack
  measured against output ([TERM-106](../terms.d/TERM-106.md), [TERM-107](../terms.d/TERM-107.md)); [CLAIM-579](../claims.d/CLAIM-579.md) calls a funding
  rule that moves where a reserve may be applied "a variant of [CLAIM-577](../claims.d/CLAIM-577.md)'s
  mechanism".
- **Abundance against slack.** [CLAIM-598](../claims.d/CLAIM-598.md)'s body: "This qualifies
  [CLAIM-577](../claims.d/CLAIM-577.md)'s reading of excess as standing slack."
- **Budget space.** [CLAIM-572](../claims.d/CLAIM-572.md)'s body: a reallocation between observing
  and acting "is a transition with its own threshold, as in [CLAIM-571](../claims.d/CLAIM-571.md),
  but in budget space rather than configuration space".

## Links across to the sibling part and to transient-support, stated

- **To the keeping part.** [CLAIM-572](../claims.d/CLAIM-572.md) complements [CLAIM-561](../claims.d/CLAIM-561.md); [CLAIM-569](../claims.d/CLAIM-569.md)
  bears on [QUESTION-395](../questions.d/QUESTION-395.md) and [QUESTION-386](../questions.d/QUESTION-386.md); [CASE-200](../cases.d/CASE-200.md) is "one mechanism for
  [QUESTION-386](../questions.d/QUESTION-386.md)", with [CLAIM-558](../claims.d/CLAIM-558.md)'s decay the competence version; [CASE-209](../cases.d/CASE-209.md)
  and [CASE-210](../cases.d/CASE-210.md) name each other, and [CASE-211](../cases.d/CASE-211.md) names [CASE-210](../cases.d/CASE-210.md) as "the
  record's case of a deadline-constrained extrication"; [TERM-106](../terms.d/TERM-106.md) sets
  itself apart from [TERM-110](../terms.d/TERM-110.md)'s revision rule and from [TERM-112](../terms.d/TERM-112.md), and calls
  its operational reserve one input to readiness ([TERM-115](../terms.d/TERM-115.md)).
- **To transient-support ([SYNTHESIS-tmprhzl8](SYNTHESIS-tmprhzl8.md)).** [CLAIM-601](../claims.d/CLAIM-601.md) uses [TERM-105](../terms.d/TERM-105.md), reading a savings
  buffer as a replenishable reserve whose depth sets a deadline.

## Not stated on the record

- **[CLAIM-601](../claims.d/CLAIM-601.md)'s buffer as a transition threshold.** Reading a delayed
  investment as a transition in [CLAIM-571](../claims.d/CLAIM-571.md)'s sense would equate a
  replenishable reserve with a capacity, which [TERM-105](../terms.d/TERM-105.md) keeps apart and
  [CLAIM-571](../claims.d/CLAIM-571.md) disclaims ("That the peak is the only cost"). Not filed.
- **[CLAIM-597](../claims.d/CLAIM-597.md)'s supply rate as [CLAIM-569](../claims.d/CLAIM-569.md)'s maintenance requirement.**
  Writing ρs = dθ/(1 − θ) as the upkeep of a form adds only a name to
  [CLAIM-597](../claims.d/CLAIM-597.md)'s formula. Not filed.
- **Whether [CLAIM-556](../claims.d/CLAIM-556.md)'s two added levels are complete.** [QUESTION-404](../questions.d/QUESTION-404.md)
  holds the open case.

## What it does not say

- That organizations have configuration spaces with such costs. Every
  claim here says the organizational reading is A's analogy or a model,
  and [CLAIM-579](../claims.d/CLAIM-579.md) that "No organizational case in the record shows slack
  present in total and absent at the bottleneck."
- That real budget rules are pure spend-matching ([CLAIM-577](../claims.d/CLAIM-577.md)).
- Anything with standing of its own.
