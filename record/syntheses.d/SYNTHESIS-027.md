---
number: 27
status: Proposed
formerly:
- SYNTHESIS-tmp78y0i
title: 'Readiness for a rare contingency is a probability of effective response under an imposed contingency, which a record of use does not measure, so neither low use nor frequent cancellation shows a reserve to be waste; a capacity is worth what the capacities it works with let it deliver, records kept per capacity bound readiness and do not identify it, and a capability kept for rare events decays unless it is practised outside operation'
version: 2
history:
- version: 2
  date: '2026-11-10'
  note: >-
    At the split of readiness (ADR-087), the third part became the
    line transient-support. The introduction and the heading of the links
    across say so; the components and links are unchanged.
defeated_if: >-
  A component misstated or misattributed here; an in-force component of
  the keeping-and-judging part of the readiness line left out without a
  reason given; or a link this account states that no component states.
  Its standing is its components': a component retired or demoted takes
  its clause with it, and nothing here holds the clause up.
tags:
- operations-research
- probabilistic-modeling
- society-and-governance
date: '2026-11-10'
line:
- readiness
integrates:
- TERM-115
- TERM-109
- TERM-107
- TERM-108
- TERM-110
- TERM-112
- TERM-113
- CLAIM-561
- CLAIM-559
- CLAIM-584
- ARG-053
- CLAIM-587
- CLAIM-632
- CLAIM-558
- CASE-210
- CASE-213
- CASE-203
- QUESTION-386
- QUESTION-394
- QUESTION-395
- QUESTION-403
- QUESTION-433
- QUESTION-434
- QUESTION-435
- QUESTION-444
---
<!-- inactive-ok-file: CLAIM-584 CLAIM-632 CASE-200 CASE-203 CASE-210 TERM-107 TERM-108 TERM-110 TERM-112 TERM-113 — Proposed; components and citations, with their standing -->
<!-- inactive-ok-file: ARG-053 — Rejected; a component, the inference the part rejects -->
<!-- inactive-ok-file: SYNTHESIS-009 — Superseded; cited as the entry CLAIM-632 returned from -->

# SYNTHESIS-027: Readiness for a rare contingency is a probability of effective response under an imposed contingency, which a record of use does not measure, so neither low use nor frequent cancellation shows a reserve to be waste; a capacity is worth what the capacities it works with let it deliver, records kept per capacity bound readiness and do not identify it, and a capability kept for rare events decays unless it is practised outside operation

*A part account of the readiness line: the part filed from the exchange on
emergency readiness and its bibliography (2026-11-04), with what later
filings added to it. The line's account is built over it and its sibling
part. A third part, withdrawing transient support, became the line
transient-support at the split of readiness ([ADR-087](../decisions.d/ADR-087.md)).*

## The account

- **What readiness is.** [TERM-115](../terms.d/TERM-115.md) (A's, Active) defines it as the
  probability that an organization, under the policy it actually follows,
  delivers an effective response to a specified contingency by its
  deadline: "It is defined under intervention, so a record of what was
  done does not measure it." It is a family indexed by contingency, not one
  number. The terms filed beside it keep apart what a record of use runs
  together: provisional commitment, between keeping a capability and
  exercising it ([TERM-109](../terms.d/TERM-109.md), A's, Active); organizational slack, useful or
  wasteful, "which the output alone does not tell apart" ([TERM-107](../terms.d/TERM-107.md), the
  filer's, Proposed); a proxy objective misaligned with no one gaming it
  ([TERM-108](../terms.d/TERM-108.md), the filer's, Proposed); the ratchet, in which the measured
  party acts on the measure ([TERM-110](../terms.d/TERM-110.md), the filer's, Proposed); a unit of
  last resort, whose "record of use measures congestion, not its worth"
  ([TERM-112](../terms.d/TERM-112.md), the filer's, Proposed); and three senses of coverage
  ([TERM-113](../terms.d/TERM-113.md), the filer's, Proposed).
- **Use does not show worth.** [CASE-210](../cases.d/CASE-210.md) (A's, Proposed) gives two
  departments with the same record of completed work, only one of which
  can meet a deadline-bound extrication. The inference from low exercise
  to waste, [ARG-053](../arguments.d/ARG-053.md) (A's), is Rejected, and its conclusion is filed as
  the disclaimed [CLAIM-584](../claims.d/CLAIM-584.md) (A's wording, Proposed). [CLAIM-561](../claims.d/CLAIM-561.md) (A's,
  demonstrated, Active) puts the threshold for provisional dispatch below
  one half in an expected-loss model of [CASE-213](../cases.d/CASE-213.md) (A's, Active), so "a
  cancellation rate alone therefore cannot identify waste", and it
  undercuts [ARG-053](../arguments.d/ARG-053.md). [CLAIM-559](../claims.d/CLAIM-559.md) (A's, demonstrated, Active), resting on
  [CLAIM-561](../claims.d/CLAIM-561.md), makes dispatch and cancellation both optimal under one
  objective; in A's words "The original dispatch is not retrospectively
  refuted by later cancellation". [CASE-203](../cases.d/CASE-203.md) (the filer's, a documented
  specimen, Proposed) shows the national fire incident data recording
  committed and cancelled units while "the data omit the failures that
  most concern readiness".
- **What a reserve is worth, and what records show.** [CLAIM-587](../claims.d/CLAIM-587.md) (A's,
  demonstrated, Active) makes a response the conjunction of complementary
  capacities, so "the marginal value of a capability depends on the
  system in which it is embedded". [CLAIM-632](../claims.d/CLAIM-632.md) (the assistant's,
  demonstrated, Proposed), resting on [CLAIM-587](../claims.d/CLAIM-587.md) and [CLAIM-558](../claims.d/CLAIM-558.md), gives the
  criterion [QUESTION-395](../questions.d/QUESTION-395.md) asks for in half: records kept per capacity bound
  readiness between the Fréchet bounds and identify it only when the
  dependence is known, so they refute a required readiness through the
  weakest capacity and certify it only when the shortfalls stay within its
  margin; under decay "a refutation outlasts the record and a
  certification does not". It answers [CASE-210](../cases.d/CASE-210.md)'s "Inventories, training
  records and drills would." with how far they would.
- **How the capability is kept.** [CLAIM-558](../claims.d/CLAIM-558.md) (the filer's, interpretive,
  Active): a procedural capability seldom called on decays with time
  since use, and practice in the interval slows the decay, so "a
  capability kept for rare events is maintained by practice outside
  operation, not by operation". The extension from an individual's skill
  to an organization's capability is the filer's.

What stays open is the evaluation and the rules: which observations,
interventions or models tell a warranted reserve from waste
([QUESTION-395](../questions.d/QUESTION-395.md), A's; "Both say passive observation of ordinary operation
is not enough; neither says what is."); how the dispatch threshold moves
when costs depend on the system's state ([QUESTION-394](../questions.d/QUESTION-394.md), A's); and under
which funding rules allocating by observed activity loses a rare
capability ([QUESTION-386](../questions.d/QUESTION-386.md), A's, which says "Its existence and harmfulness
should not be assumed.").

## The components

- [TERM-115](../terms.d/TERM-115.md), A's, Active; complements [TERM-055](../terms.d/TERM-055.md) (distributed-agency).
- [TERM-109](../terms.d/TERM-109.md), A's, Active.
- [TERM-107](../terms.d/TERM-107.md), [TERM-108](../terms.d/TERM-108.md), [TERM-110](../terms.d/TERM-110.md), [TERM-112](../terms.d/TERM-112.md) and [TERM-113](../terms.d/TERM-113.md), the filer's,
  Proposed. Each waits on its settle condition, a claim of the record's
  own stated in it, and none has one.
- [CLAIM-561](../claims.d/CLAIM-561.md), A's, thesis, demonstrated, Active; second line
  formal-apparatus; grounds [CASE-213](../cases.d/CASE-213.md); complements [CLAIM-520](../claims.d/CLAIM-520.md)
  (distributed-agency) and [CLAIM-572](../claims.d/CLAIM-572.md) (the reaching part).
- [CLAIM-559](../claims.d/CLAIM-559.md), A's, thesis, demonstrated, Active; second line
  formal-apparatus; rests on [CLAIM-561](../claims.d/CLAIM-561.md); complements [CLAIM-535](../claims.d/CLAIM-535.md)
  (will-organization).
- [CLAIM-584](../claims.d/CLAIM-584.md), A's wording, disclaimed, Proposed.
- [ARG-053](../arguments.d/ARG-053.md), A's, Rejected; grounds [CASE-210](../cases.d/CASE-210.md) and [CASE-213](../cases.d/CASE-213.md), concludes
  [CLAIM-584](../claims.d/CLAIM-584.md).
- [CLAIM-587](../claims.d/CLAIM-587.md), A's, thesis, demonstrated, Active; complements [CLAIM-422](../claims.d/CLAIM-422.md)
  and [CLAIM-347](../claims.d/CLAIM-347.md).
- [CLAIM-632](../claims.d/CLAIM-632.md), the assistant's (returned from [SYNTHESIS-009](SYNTHESIS-009.md) on
  2026-11-08), thesis, demonstrated, Proposed; second line
  formal-apparatus; its body has an "Admission" section (derived route).
- [CLAIM-558](../claims.d/CLAIM-558.md), the filer's, thesis, interpretive, Active; grounds
  [THEORY-1424](../theory.d/THEORY-1424.md) and [THEORY-1404](../theory.d/THEORY-1404.md).
- [CASE-210](../cases.d/CASE-210.md), A's, construction, Proposed; illustrates [CLAIM-414](../claims.d/CLAIM-414.md)
  (evidence-for-experience).
- [CASE-213](../cases.d/CASE-213.md), A's, construction, Active; illustrates [CLAIM-559](../claims.d/CLAIM-559.md).
- [CASE-203](../cases.d/CASE-203.md), the filer's, documented specimen, Proposed; illustrates
  [CLAIM-296](../claims.d/CLAIM-296.md) (distributed-agency).
- [QUESTION-386](../questions.d/QUESTION-386.md), [QUESTION-394](../questions.d/QUESTION-394.md) and [QUESTION-395](../questions.d/QUESTION-395.md), A's, Open.
- [QUESTION-403](../questions.d/QUESTION-403.md) and [QUESTION-433](../questions.d/QUESTION-433.md), Open: promotion conditions moved from
  [THEORY-1404](../theory.d/THEORY-1404.md) and [THEORY-1424](../theory.d/THEORY-1424.md), [CLAIM-558](../claims.d/CLAIM-558.md)'s grounds. [QUESTION-433](../questions.d/QUESTION-433.md) names
  [QUESTION-403](../questions.d/QUESTION-403.md) as related.
- [QUESTION-434](../questions.d/QUESTION-434.md), Open, opened by the twenty-ninth status review on Hua and
  colleagues' hypercube convergence proof ([THEORY-1426](../theory.d/THEORY-1426.md)); second line
  formal-apparatus.
- [QUESTION-435](../questions.d/QUESTION-435.md), Open, the second-source demand moved from [THEORY-1378](../theory.d/THEORY-1378.md),
  the reading [TERM-110](../terms.d/TERM-110.md) cites for a ratchet that stops learning.
- [QUESTION-444](../questions.d/QUESTION-444.md), Open, moved from [THEORY-1412](../theory.d/THEORY-1412.md), a reading of an ambulance
  preparedness policy.

[QUESTION-434](../questions.d/QUESTION-434.md), [QUESTION-435](../questions.d/QUESTION-435.md) and [QUESTION-444](../questions.d/QUESTION-444.md) link to no component by a
relation or a mention; they are listed because their `line` field places
them here, and each reaches the part only through a reading.

## Links the components state, and where

- **[CASE-213](../cases.d/CASE-213.md) to the two claims.** [CLAIM-561](../claims.d/CLAIM-561.md) grounds on it and [CLAIM-559](../claims.d/CLAIM-559.md)
  is illustrated by it; [CASE-213](../cases.d/CASE-213.md)'s body: "[CLAIM-561](../claims.d/CLAIM-561.md) adds the costs;
  [QUESTION-394](../questions.d/QUESTION-394.md) asks how coverage changes them."
- **The rejected inference.** [ARG-053](../arguments.d/ARG-053.md) is undercut by [CLAIM-561](../claims.d/CLAIM-561.md) and
  rejected on [CASE-210](../cases.d/CASE-210.md); [CLAIM-584](../claims.d/CLAIM-584.md)'s body: "What would show it is an
  evaluation of the kind [QUESTION-395](../questions.d/QUESTION-395.md) asks for, not a count of uses."
- **From readiness to records.** [CLAIM-632](../claims.d/CLAIM-632.md) joins [CLAIM-587](../claims.d/CLAIM-587.md), [TERM-115](../terms.d/TERM-115.md),
  [CASE-210](../cases.d/CASE-210.md) and [CLAIM-558](../claims.d/CLAIM-558.md), as its summary says; [CASE-210](../cases.d/CASE-210.md)'s note of
  2026-11-07 points to it (under the code it then had, [SYNTHESIS-009](SYNTHESIS-009.md)).
- **From decay to the funding loop.** [QUESTION-386](../questions.d/QUESTION-386.md)'s model has
  competence decaying without funded maintenance, and says the loop
  "would act on one factor of [CLAIM-587](../claims.d/CLAIM-587.md)'s joint readiness".
- **Slack, coverage and readiness.** [TERM-107](../terms.d/TERM-107.md), [TERM-112](../terms.d/TERM-112.md) and [TERM-113](../terms.d/TERM-113.md)
  each say, under "What it is not", how they differ from [TERM-115](../terms.d/TERM-115.md);
  [TERM-113](../terms.d/TERM-113.md) calls coverage a proxy objective in [TERM-108](../terms.d/TERM-108.md)'s sense; [TERM-108](../terms.d/TERM-108.md)
  sets misalignment apart from the ratchet of [TERM-110](../terms.d/TERM-110.md).

## Links across to the sibling part and to transient-support, stated

- **To the reaching part.** [CLAIM-572](../claims.d/CLAIM-572.md) (Active) complements [CLAIM-561](../claims.d/CLAIM-561.md):
  "Sending the general response early is the hedge at o = 0." [CLAIM-569](../claims.d/CLAIM-569.md)
  (Active) bears on [QUESTION-395](../questions.d/QUESTION-395.md) and [QUESTION-386](../questions.d/QUESTION-386.md), and [CLAIM-632](../claims.d/CLAIM-632.md) cites it
  for the construction cost a waste verdict must not overlook. [CASE-200](../cases.d/CASE-200.md)
  (Proposed) on [QUESTION-386](../questions.d/QUESTION-386.md): "That is one mechanism for [QUESTION-386](../questions.d/QUESTION-386.md),
  here acting on a reconfiguration reserve rather than on competence; the
  competence version is [CLAIM-558](../claims.d/CLAIM-558.md)'s decay." [CLAIM-577](../claims.d/CLAIM-577.md) (Active) is the
  pure case of the same mechanism ([QUESTION-386](../questions.d/QUESTION-386.md)'s note of 2026-11-05), and
  [QUESTION-394](../questions.d/QUESTION-394.md)'s note names A's simulator as its cheapest test. [TERM-106](../terms.d/TERM-106.md)
  refines [TERM-107](../terms.d/TERM-107.md), and [TERM-110](../terms.d/TERM-110.md)'s revision rule is what [CASE-200](../cases.d/CASE-200.md)'s cut
  on unspent funds is.
- **To transient-support ([SYNTHESIS-032](SYNTHESIS-032.md)).** [CLAIM-558](../claims.d/CLAIM-558.md) complements [CLAIM-602](../claims.d/CLAIM-602.md) and
  corroborates [CLAIM-600](../claims.d/CLAIM-600.md). [QUESTION-386](../questions.d/QUESTION-386.md)'s note: "In [CLAIM-602](../claims.d/CLAIM-602.md), funding
  that pays for the work rather than for the organization doing it
  selects substitution, which lowers the capacity kept." [CLAIM-632](../claims.d/CLAIM-632.md) says a
  waste verdict does not call for abolition, since "rebuilding costs
  construction ([CLAIM-569](../claims.d/CLAIM-569.md)) or may be impossible below a threshold
  ([CLAIM-605](../claims.d/CLAIM-605.md))".

## Not stated on the record

Links across the components that no entry states, tested by [ADR-075](../decisions.d/ADR-075.md)'s
step 5 at this review and not filed:

- **When a records-based certification expires.** [CLAIM-632](../claims.d/CLAIM-632.md)'s expiry
  clause with [CLAIM-558](../claims.d/CLAIM-558.md)'s decay rates would put a clock on a
  certification. It needs a map from a skill's effect size to a
  capacity's probability of holding, which no component gives: a free
  parameter.
- **Records that miss a foreclosed transition.** That per-capacity
  records can certify readiness for a contingency whose response needs a
  transition [CLAIM-577](../claims.d/CLAIM-577.md)'s rule has priced out. It is already inside
  [CLAIM-632](../claims.d/CLAIM-632.md)'s premise that the records estimate every capacity the
  response needs; nothing is added.
- **[CLAIM-572](../claims.d/CLAIM-572.md)'s readiness as a case of [TERM-115](../terms.d/TERM-115.md)'s.** It holds only once
  a deadline and a policy are chosen to make it hold, and [CLAIM-632](../claims.d/CLAIM-632.md) says
  the two are "a different notion".

## What it does not say

- That any reserve is warranted or wasteful; [CLAIM-632](../claims.d/CLAIM-632.md) gives a criterion
  for a declared verdict, and [CASE-210](../cases.d/CASE-210.md) says warrant "needs an objective,
  a distribution of incidents or a robust reliability requirement".
- That real dispatch policies are optimal ([CLAIM-561](../claims.d/CLAIM-561.md)), or that an
  organization's capability decays as an individual's skill does
  ([CLAIM-558](../claims.d/CLAIM-558.md), interpretive).
- That the five Proposed terms are settled.
- Anything with standing of its own.
