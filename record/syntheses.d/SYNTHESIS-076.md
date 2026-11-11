---
number: 76
status: Proposed
formerly:
- SYNTHESIS-tmpc35sn
title: 'Reaching under a budget is not holding, and telling apart is not turning into one another: feasible, reachable and reliably reached come apart, a transition''s threshold is the least peak over admissible paths, stable under error and a frontier rather than a total when there are several resources, a budget grows a compatibility complex and a reachability filtration that do not fix each other, observing budgets split what can be told apart while acting budgets under peak costs merge what can be reached, the category chosen decides what counts as the same, navigating and diagnosing have complexities of their own, and the same split recurs for control inputs and for synchronization demands indexed by control parameters'
version: 1
defeated_if: >-
  A component misstated or misattributed here; an in-force member of this
  part of the formal-apparatus line left out without a reason given; a
  link this account states that no component states; or a link to another
  part of the line stated here wrongly or left out. Its standing is its
  components': a component retired or demoted takes its clause with it,
  and nothing here holds the clause up.
tags:
- mathematics
- operations-research
- individuation
- control-theory
date: '2026-11-11'
line:
- formal-apparatus
integrates:
- CLAIM-639
- CLAIM-571
- CLAIM-567
- CLAIM-563
- CLAIM-580
- CLAIM-585
- CLAIM-577
- CLAIM-586
- CLAIM-564
- CLAIM-560
- CLAIM-583
- CLAIM-607
- CLAIM-591
- CLAIM-594
- CLAIM-598
- CLAIM-578
- CLAIM-575
- CLAIM-565
- CLAIM-574
- CLAIM-581
- CLAIM-557
- CLAIM-570
- CLAIM-592
- CLAIM-590
- CLAIM-572
- CLAIM-455
- CLAIM-561
- CLAIM-632
- CLAIM-345
- CLAIM-542
- CLAIM-589
- CLAIM-582
- CLAIM-618
- ARG-061
- QUESTION-375
- QUESTION-376
- QUESTION-384
- QUESTION-391
- QUESTION-438
summary: >-
  A part account of the formal-apparatus line: the part on feasibility,
  reachability and thresholds under resources, with the restricted Yoneda
  profiles and budgeted individuation built on them, 38 entries. All but
  one are first in another line (realizability, readiness,
  will-organization or distributed-agency), and every one is already
  integrated by an account of that line; this account integrates them
  again because their `line` includes formal-apparatus. The line's
  account is built over it. It adds nothing of its own; its standing is
  its components'.
---
<!-- inactive-ok-file: CLAIM-618 CLAIM-632 ARG-061 — Proposed; components, with their standing -->
<!-- inactive-ok-file: SYNTHESIS-024 SYNTHESIS-027 SYNTHESIS-040 SYNTHESIS-041 SYNTHESIS-042 SYNTHESIS-043 SYNTHESIS-045 SYNTHESIS-051 SYNTHESIS-056 SYNTHESIS-068 CLAIM-631 CLAIM-634 CASE-203 ADR-075 ADR-084 — Proposed; the accounts that already integrate the members, and entries cited for what they hold, nothing here resting on their being settled -->
<!-- inactive-ok-file: SYNTHESIS-009 — Superseded; cited as the entry CLAIM-632 returned from -->
<!-- inactive-ok-file: ARG-053 — Rejected; cited as the argument CLAIM-561 undercuts -->
<!-- inactive-ok-file: CLAIM-639 SYNTHESIS-074 SYNTHESIS-075 SYNTHESIS-079 SYNTHESIS-080 SYNTHESIS-088 — Proposed; cited with its standing -->

# SYNTHESIS-076: Reaching under a budget is not holding, and telling apart is not turning into one another: feasible, reachable and reliably reached come apart, a transition's threshold is the least peak over admissible paths, stable under error and a frontier rather than a total when there are several resources, a budget grows a compatibility complex and a reachability filtration that do not fix each other, observing budgets split what can be told apart while acting budgets under peak costs merge what can be reached, the category chosen decides what counts as the same, navigating and diagnosing have complexities of their own, and the same split recurs for control inputs and for synchronization demands indexed by control parameters

*A part account of the formal-apparatus line ("Formal apparatus", [ADR-040](../decisions.d/ADR-040.md)):
the part a community map of stored relations and mentions groups around
[CLAIM-571](../claims.d/CLAIM-571.md)'s threshold and [CLAIM-567](../claims.d/CLAIM-567.md)'s three properties, with the
restricted Yoneda profiles and budgeted individuation built on them, the
control-cost results they borrow, and the parameter-indexed complex of
synchronization demands. The line's account is built over it and its
sibling parts. Only [QUESTION-438](../questions.d/QUESTION-438.md) has formal-apparatus as its first line.
Every member is already integrated by an account of its first line or of
another line it carries: [SYNTHESIS-042](SYNTHESIS-042.md) (reaching under resources, 17
members), [SYNTHESIS-040](SYNTHESIS-040.md) (budgeted individuation, 8), [SYNTHESIS-024](SYNTHESIS-024.md)
(readiness, 7), [SYNTHESIS-051](SYNTHESIS-051.md) (distributed-agency, 4), [SYNTHESIS-027](SYNTHESIS-027.md)
(readiness, 2), [SYNTHESIS-041](SYNTHESIS-041.md) (will-organization, 2), [SYNTHESIS-045](SYNTHESIS-045.md)
(assembly and nucleation, 2), [SYNTHESIS-068](SYNTHESIS-068.md) (pragmatic-transport, 2) and
[SYNTHESIS-056](SYNTHESIS-056.md) (distributed-agency, 1). This account integrates every
member again, because their `line` includes formal-apparatus.*

## The account

- **Three properties and the threshold.** [CLAIM-567](../claims.d/CLAIM-567.md) (the filer's
  construction from A's two separations, demonstrated, Active): feasible,
  reachable and reliably reached are "three properties, each implied by the
  next and none implying it", and it "inserts reachability between the
  structural infeasibility and realized violation that [CLAIM-357](../claims.d/CLAIM-357.md)
  separates". [CLAIM-571](../claims.d/CLAIM-571.md) (A's wording, demonstrated, Active): for a fixed
  architecture and one capacity, the threshold for reaching a target "is
  the least, over admissible transition paths, of the peak requirement
  along the path, and it is infinite when no admissible path joins the
  two". Its body: "It is the resource-quantitative form of the separation
  between a feasible target and a reachable one ([CLAIM-567](../claims.d/CLAIM-567.md))." [CLAIM-563](../claims.d/CLAIM-563.md)
  (A's, sharpened by the reader, demonstrated, Active) says when the
  affordable processes compose: closure holds "exactly when b ⊗ b ≤ b, so
  always for maximum and, for sum, only at 0 and infinity", and "The peak
  case is the record's threshold."
- **The threshold as a planner meets it.** [CLAIM-580](../claims.d/CLAIM-580.md) (the assistant's,
  demonstrated, Active): the threshold moves by at most the largest error
  in the requirement, so "a planner who knows each configuration's cost to
  within ε knows a transition's threshold to within ε, and its
  reconfiguration slack to within 2ε". [CLAIM-585](../claims.d/CLAIM-585.md) (the filer's construction
  from A's, demonstrated, Active): with several capacities the sufficient
  budgets form an up-set with a Pareto frontier, and "the set need not be
  convex, so no threshold on a weighted total of the resources describes
  it". [CLAIM-577](../claims.d/CLAIM-577.md) (the assistant's, demonstrated, Active): under a budget
  set each period to last period's peak spending, "any transition whose
  threshold exceeds the cost of holding the current configuration is lost
  after one period spent holding it"; its summary calls it "[CLAIM-079](../claims.d/CLAIM-079.md)'s
  stability without viability, produced by a budget rule".
- **Two filtrations under a budget.** [CLAIM-586](../claims.d/CLAIM-586.md) (A's, demonstrated,
  Active): the compatibility complex indexed by a budget grows with it and
  never exceeds the unbudgeted complex, "So a missing face is either short
  of resources at b or structurally frustrated, and the unbudgeted complex
  tells which." [CLAIM-564](../claims.d/CLAIM-564.md) (the reader's derivation from A's construction,
  demonstrated, Active) makes the implications among demands antitone in
  the budget, "the implication counterpart of [CLAIM-586](../claims.d/CLAIM-586.md)'s split between
  being short of resources and being structurally frustrated". [CLAIM-560](../claims.d/CLAIM-560.md)
  (A's, demonstrated on A's example with the filer's demands, Active)
  pairs the compatibility filtration with a reachability filtration: "K(b)
  depends on Q(b) and the demands only; R(b) on how Q(b) is joined by
  moves. Neither fixes the other." [CLAIM-583](../claims.d/CLAIM-583.md) (the filer's construction from
  A's, demonstrated, Active): two systems with "Same complex, same move
  rule, same costs, different reachability". [CLAIM-607](../claims.d/CLAIM-607.md) (the record's own
  conditional demonstration, split from [CLAIM-583](../claims.d/CLAIM-583.md), Active): "This claim
  shows it one level up, for constraint languages." [CLAIM-591](../claims.d/CLAIM-591.md) (A's wording,
  the filer's constructions, demonstrated, Active): under directed moves
  connectivity does not settle reachability, "so a persistence summary of
  sublevel sets bounds the reachability filtration without fixing it".
- **Where a budget is not a budget.** [CLAIM-594](../claims.d/CLAIM-594.md) (the assistant's,
  demonstrated, Active): when the resource that pays for crossing barriers
  also sets the costs, as heat does in DNA origami, reaching within a time
  budget need not be monotone in the resource, and "budgeted reachability
  with fixed costs, where more budget never loses a reachable state, is
  the special case of a resource that leaves the costs unchanged".
  [CLAIM-598](../claims.d/CLAIM-598.md) (the assistant's, from A's second synthesis on DNA origami,
  demonstrated, Active): whether uniform abundance helps or hurts depends,
  at each branch point, on whether the competing steps consume further
  resource; "Both name a resource whose amount changes which outcome is
  reached, not only how fast."
- **Complexity and diagnosis.** [CLAIM-578](../claims.d/CLAIM-578.md) (A's, demonstrated, Active):
  complexity belongs to a family of problems posed over configuration
  spaces, not to one space, and "For the record it means that one
  organization's compatibility complex carries no complexity." [CLAIM-575](../claims.d/CLAIM-575.md)
  (the filer's, from the complexity readings, demonstrated, Active),
  resting on it: "So telling geometric disconnection from a capacity
  bottleneck can be PSPACE-hard, and knowing how far over budget the
  cheapest path is can be NP-hard." [CLAIM-565](../claims.d/CLAIM-565.md) (the filer's, from A's
  question and the readings, demonstrated, Active): with constants,
  positive 1-in-3 SAT and positive NAE-3SAT have "the same clone, and
  navigation on opposite sides of the dichotomy".
- **Telling apart and turning into one another.** [CLAIM-574](../claims.d/CLAIM-574.md) (A's wording,
  the proof given and the guard the filer's, demonstrated, Active):
  restricted Yoneda profiles over nested probe families only split objects
  as the budget grows, so "objects told apart at a lower budget stay apart
  at every higher one". [CLAIM-581](../claims.d/CLAIM-581.md) (the assistant's, demonstrated, Active):
  under peak costs on reversible moves "the transition threshold between
  configurations is an extended pseudo-ultrametric", so identification
  within a budget is an equivalence whose classes nest into one tree, and
  "The resource semantics is an individuation choice." [CLAIM-557](../claims.d/CLAIM-557.md) (the
  assistant's, demonstrated, Active), resting on both: "A system's budgeted
  individuation is then indexed by a pair, an observing budget and an
  acting budget, and the two can be traded or decoupled." [CLAIM-570](../claims.d/CLAIM-570.md) (A's
  construction, made exact by the assistant, demonstrated, Active) gives
  the up-set and down-set of budget pairs where one partition contains the
  other, with their boundaries. [CLAIM-592](../claims.d/CLAIM-592.md) (the assistant's, demonstrated,
  Active): the two partitions agree only on levels common to both chains,
  and "the cost order decides which of those levels actually appear".
  [CLAIM-590](../claims.d/CLAIM-590.md) (the filer's construction from A's, demonstrated, Active): the
  path groupoid of a degree-4 vertex identifies its folded states and the
  category enriched in peak footprint keeps them 1.866 apart, so
  "equivalence of possibilities is not equivalence of resource-bounded
  capabilities". [CLAIM-455](../claims.d/CLAIM-455.md) (stated in [CASE-154](../cases.d/CASE-154.md) and filed at the audit of
  2026-10-27, demonstrated, Active): for one bounded observer a
  transformation of a representation can make one task's distinction
  legible and another's illegible, so "a regime that improves one
  perspective's competence can disable another's".
- **One budget for observing and acting, and readiness.** [CLAIM-572](../claims.d/CLAIM-572.md) (the
  assistant's, demonstrated, Active): when observing and acting draw on
  one budget, the cheapest readiness buys a whole prefix of the probes,
  the affordable splits can be disconnected, and stopping when the next
  probe does not pay can miss the optimum; "A reallocation of this kind is
  a transition with its own threshold, as in [CLAIM-571](../claims.d/CLAIM-571.md), but in budget space
  rather than configuration space." [CLAIM-561](../claims.d/CLAIM-561.md) (A's, demonstrated, Active):
  provisional mobilization can minimize expected loss when the resource is
  more likely to be cancelled than used, so "a cancellation rate alone
  therefore cannot identify waste". [CLAIM-632](../claims.d/CLAIM-632.md) (the assistant's integration,
  filed as [SYNTHESIS-009](SYNTHESIS-009.md) and returned to CLAIM under [ADR-084](../decisions.d/ADR-084.md), demonstrated,
  Proposed): records kept per capacity bound readiness and identify it only
  when the capacities' dependence is known, and a refutation outlasts the
  record while a certification does not.
- **Control inputs.** [CLAIM-345](../claims.d/CLAIM-345.md) (A's statement, the record's proof,
  demonstrated, Active): "Equal controllability rank does not fix the cost
  of control". [CLAIM-542](../claims.d/CLAIM-542.md) (the owner's point, A's statements, the reader's
  scalar derivation, demonstrated, Active): sensitivity fixes neither the
  allocation nor the authorship of control, "so only feedback that
  observes the state turns cheaper control into reliable direction".
  [CLAIM-589](../claims.d/CLAIM-589.md) (A's, demonstrated, Active), resting on both: "permitted
  directions, actuated directions and transitions achievable at acceptable
  cost are three objects", the second inside the first at each instant,
  while over a horizon reach can exceed both. [CLAIM-582](../claims.d/CLAIM-582.md) (A's, the second
  half's construction the filer's, demonstrated, Active): an added hard
  constraint in a fixed model cannot enlarge reach, "So the reachability
  dimension of [CLAIM-354](../claims.d/CLAIM-354.md) cannot grow under an added constraint in a fixed
  model"; what it can improve is robustness or reliability.
- **Synchronization demands over control parameters.** [CLAIM-618](../claims.d/CLAIM-618.md) (the
  owner's conjecture, A's construction, the reader's witness, demonstrated,
  Proposed): each locking region lies inside the compatibility region of
  the same demands and need not equal it; "This is [CLAIM-567](../claims.d/CLAIM-567.md)'s
  feasible/reliably-reached split carried over a space of control
  parameters." [ARG-061](../arguments.d/ARG-061.md) (the assistant's wording of A's construction,
  formal application, Proposed) concludes it and finds that two of its
  further statements need a premise it does not state, the admissible
  configurations Q(λ) being the locked ones, which "would make it plainer
  that this is [CLAIM-567](../claims.d/CLAIM-567.md)'s split carried over control parameters".

What stays open is A's programme of questions on this part: whether a
resource-indexed topological summary detects navigation complexity
([QUESTION-375](../questions.d/QUESTION-375.md)), what property of a constraint language fixes navigation
beyond Boolean languages and under budgets ([QUESTION-376](../questions.d/QUESTION-376.md), answered for
Boolean languages with constants by [CLAIM-565](../claims.d/CLAIM-565.md)), when restricted enriched
profiles agree with bisimulation pseudometrics ([QUESTION-384](../questions.d/QUESTION-384.md)), when an
effective constraint stops being a good approximation ([QUESTION-391](../questions.d/QUESTION-391.md)), and
when changes in the complex of synchronization demands coincide with
bifurcations of the locked states ([QUESTION-438](../questions.d/QUESTION-438.md)).

## The components

- [CLAIM-571](../claims.d/CLAIM-571.md), A's wording, thesis, demonstrated, Active; first line
  readiness, then realizability and formal-apparatus.
- [CLAIM-567](../claims.d/CLAIM-567.md), the filer's construction from A's, thesis, demonstrated,
  Active; first line realizability, also readiness; rests on [CLAIM-571](../claims.d/CLAIM-571.md).
- [CLAIM-563](../claims.d/CLAIM-563.md), A's, sharpened by the reader, thesis, demonstrated, Active;
  first line realizability; uses [TERM-105](../terms.d/TERM-105.md) and [TERM-114](../terms.d/TERM-114.md).
- [CLAIM-580](../claims.d/CLAIM-580.md), the assistant's, thesis, demonstrated, Active; first line
  readiness; rests on [CLAIM-571](../claims.d/CLAIM-571.md).
- [CLAIM-585](../claims.d/CLAIM-585.md), the filer's construction from A's, thesis, demonstrated,
  Active; first line readiness; rests on [CLAIM-571](../claims.d/CLAIM-571.md).
- [CLAIM-577](../claims.d/CLAIM-577.md), the assistant's, thesis, demonstrated, Active; first line
  readiness; rests on [CLAIM-571](../claims.d/CLAIM-571.md); uses [TERM-106](../terms.d/TERM-106.md).
- [CLAIM-586](../claims.d/CLAIM-586.md), A's, thesis, demonstrated, Active; first line realizability,
  also distributed-agency; rests on [CLAIM-347](../claims.d/CLAIM-347.md); uses [TERM-060](../terms.d/TERM-060.md).
- [CLAIM-564](../claims.d/CLAIM-564.md), the reader's derivation from A's, thesis, demonstrated,
  Active; first line realizability; grounds [CASE-212](../cases.d/CASE-212.md); uses [TERM-060](../terms.d/TERM-060.md).
- [CLAIM-560](../claims.d/CLAIM-560.md), A's, thesis, demonstrated, Active; first line realizability;
  rests on [CLAIM-586](../claims.d/CLAIM-586.md) and [CLAIM-571](../claims.d/CLAIM-571.md); uses [TERM-114](../terms.d/TERM-114.md).
- [CLAIM-583](../claims.d/CLAIM-583.md), the filer's construction from A's, thesis, demonstrated,
  Active; first line realizability; rests on [CLAIM-347](../claims.d/CLAIM-347.md); uses [TERM-114](../terms.d/TERM-114.md).
- [CLAIM-607](../claims.d/CLAIM-607.md), the record's own conditional demonstration, thesis,
  demonstrated, Active; first line realizability; grounds [THEORY-1407](../theory.d/THEORY-1407.md) and
  [THEORY-1413](../theory.d/THEORY-1413.md).
- [CLAIM-591](../claims.d/CLAIM-591.md), A's wording, the filer's constructions, thesis, demonstrated,
  Active; first line realizability; uses [TERM-114](../terms.d/TERM-114.md).
- [CLAIM-594](../claims.d/CLAIM-594.md), the assistant's, thesis, demonstrated, Active; first line
  realizability; grounds [CASE-216](../cases.d/CASE-216.md).
- [CLAIM-598](../claims.d/CLAIM-598.md), the assistant's, thesis, demonstrated, Active; first line
  realizability, also readiness; grounds [CASE-217](../cases.d/CASE-217.md).
- [CLAIM-578](../claims.d/CLAIM-578.md), A's, thesis, demonstrated, Active; first line realizability;
  grounds [THEORY-1375](../theory.d/THEORY-1375.md).
- [CLAIM-575](../claims.d/CLAIM-575.md), the filer's, thesis, demonstrated, Active; first line
  realizability; rests on [CLAIM-578](../claims.d/CLAIM-578.md); grounds [THEORY-1372](../theory.d/THEORY-1372.md) and [THEORY-1375](../theory.d/THEORY-1375.md).
- [CLAIM-565](../claims.d/CLAIM-565.md), the filer's (the Post-lattice step the filer's and the
  lead's), thesis, demonstrated, Active; first line realizability; grounds
  [THEORY-1407](../theory.d/THEORY-1407.md) and [THEORY-1413](../theory.d/THEORY-1413.md).
- [CLAIM-574](../claims.d/CLAIM-574.md), A's wording, thesis, demonstrated, Active; first line
  realizability, also pragmatic-transport; rests on [CLAIM-264](../claims.d/CLAIM-264.md); grounds
  [THEORY-032](../theory.d/THEORY-032.md); uses [TERM-069](../terms.d/TERM-069.md) and [TERM-065](../terms.d/TERM-065.md).
- [CLAIM-581](../claims.d/CLAIM-581.md), the assistant's, thesis, demonstrated, Active; first line
  realizability; rests on [CLAIM-571](../claims.d/CLAIM-571.md) and [CLAIM-563](../claims.d/CLAIM-563.md).
- [CLAIM-557](../claims.d/CLAIM-557.md), the assistant's, thesis, demonstrated, Active; first line
  realizability; rests on [CLAIM-574](../claims.d/CLAIM-574.md) and [CLAIM-581](../claims.d/CLAIM-581.md).
- [CLAIM-570](../claims.d/CLAIM-570.md), A's construction made exact by the assistant, thesis,
  demonstrated, Active; first line realizability; rests on [CLAIM-574](../claims.d/CLAIM-574.md) and
  [CLAIM-581](../claims.d/CLAIM-581.md); grounds [CASE-199](../cases.d/CASE-199.md).
- [CLAIM-592](../claims.d/CLAIM-592.md), the assistant's, thesis, demonstrated, Active; first line
  realizability; rests on [CLAIM-570](../claims.d/CLAIM-570.md), [CLAIM-581](../claims.d/CLAIM-581.md) and [CLAIM-574](../claims.d/CLAIM-574.md).
- [CLAIM-590](../claims.d/CLAIM-590.md), the filer's construction from A's, thesis, demonstrated,
  Active; first line realizability, also pragmatic-transport; rests on
  [CLAIM-571](../claims.d/CLAIM-571.md) and [CLAIM-563](../claims.d/CLAIM-563.md); grounds [CASE-206](../cases.d/CASE-206.md) and [THEORY-032](../theory.d/THEORY-032.md); uses [TERM-114](../terms.d/TERM-114.md).
- [CLAIM-572](../claims.d/CLAIM-572.md), the assistant's, thesis, demonstrated, Active; first line
  readiness, also realizability; rests on [CLAIM-535](../claims.d/CLAIM-535.md), [CLAIM-570](../claims.d/CLAIM-570.md) and
  [CLAIM-574](../claims.d/CLAIM-574.md).
- [CLAIM-455](../claims.d/CLAIM-455.md), from [CASE-154](../cases.d/CASE-154.md) at the audit of 2026-10-27, thesis,
  demonstrated, Active; first line distributed-agency; grounds [CASE-154](../cases.d/CASE-154.md);
  uses [TERM-064](../terms.d/TERM-064.md).
- [CLAIM-561](../claims.d/CLAIM-561.md), A's, thesis, demonstrated, Active; first line readiness;
  grounds [CASE-213](../cases.d/CASE-213.md); uses [TERM-109](../terms.d/TERM-109.md); undercuts [ARG-053](../arguments.d/ARG-053.md) (Rejected).
- [CLAIM-632](../claims.d/CLAIM-632.md), the assistant's, thesis, demonstrated, Proposed; first line
  readiness; rests on [CLAIM-587](../claims.d/CLAIM-587.md) and [CLAIM-558](../claims.d/CLAIM-558.md); uses [TERM-115](../terms.d/TERM-115.md); answers
  [QUESTION-395](../questions.d/QUESTION-395.md).
- [CLAIM-345](../claims.d/CLAIM-345.md), A's statement with the record's proof, thesis, demonstrated,
  Active; first line will-organization.
- [CLAIM-542](../claims.d/CLAIM-542.md), the owner's point, A's statements and the reader's
  derivation, thesis, demonstrated, Active; first line will-organization;
  rests on [CLAIM-345](../claims.d/CLAIM-345.md).
- [CLAIM-589](../claims.d/CLAIM-589.md), A's, thesis, demonstrated, Active; first line realizability;
  rests on [CLAIM-345](../claims.d/CLAIM-345.md) and [CLAIM-542](../claims.d/CLAIM-542.md); grounds [THEORY-1432](../theory.d/THEORY-1432.md).
- [CLAIM-582](../claims.d/CLAIM-582.md), A's, the second half's construction the filer's, thesis,
  demonstrated, Active; first line realizability.
- [CLAIM-618](../claims.d/CLAIM-618.md), the owner's conjecture and A's construction, thesis,
  demonstrated, Proposed; first line distributed-agency; rests on
  [CLAIM-347](../claims.d/CLAIM-347.md); grounds [THEORY-1082](../theory.d/THEORY-1082.md) and [THEORY-1087](../theory.d/THEORY-1087.md).
- [ARG-061](../arguments.d/ARG-061.md), the assistant's wording, formal application, Proposed; first
  line distributed-agency; concludes [CLAIM-618](../claims.d/CLAIM-618.md); grounds [THEORY-1082](../theory.d/THEORY-1082.md) and
  [THEORY-1087](../theory.d/THEORY-1087.md).
- [QUESTION-375](../questions.d/QUESTION-375.md), [QUESTION-376](../questions.d/QUESTION-376.md), [QUESTION-384](../questions.d/QUESTION-384.md) and [QUESTION-391](../questions.d/QUESTION-391.md), A's, Open;
  first line realizability. [QUESTION-384](../questions.d/QUESTION-384.md) refines [QUESTION-393](../questions.d/QUESTION-393.md).
- [QUESTION-438](../questions.d/QUESTION-438.md), A's, Open; first line formal-apparatus, also
  distributed-agency.

## Links the components state, and where

- **Everything leans on the threshold.** [CLAIM-567](../claims.d/CLAIM-567.md), [CLAIM-560](../claims.d/CLAIM-560.md), [CLAIM-577](../claims.d/CLAIM-577.md),
  [CLAIM-580](../claims.d/CLAIM-580.md), [CLAIM-581](../claims.d/CLAIM-581.md), [CLAIM-585](../claims.d/CLAIM-585.md) and [CLAIM-590](../claims.d/CLAIM-590.md) rest on [CLAIM-571](../claims.d/CLAIM-571.md);
  [CLAIM-571](../claims.d/CLAIM-571.md) complements [CLAIM-563](../claims.d/CLAIM-563.md), [CLAIM-575](../claims.d/CLAIM-575.md) and [CLAIM-591](../claims.d/CLAIM-591.md). [CLAIM-571](../claims.d/CLAIM-571.md)'s
  note of 2026-11-05: "[CLAIM-560](../claims.d/CLAIM-560.md) pairs the threshold with [CLAIM-586](../claims.d/CLAIM-586.md)'s
  compatibility filtration; neither determines the other." Its "What it
  does not say" sends several resources to [CLAIM-585](../claims.d/CLAIM-585.md).
- **Composition.** [CLAIM-581](../claims.d/CLAIM-581.md) and [CLAIM-590](../claims.d/CLAIM-590.md) rest on [CLAIM-563](../claims.d/CLAIM-563.md); [CLAIM-563](../claims.d/CLAIM-563.md)
  complements [CLAIM-585](../claims.d/CLAIM-585.md) and its "What it does not say" gives "for
  [CLAIM-585](../claims.d/CLAIM-585.md)'s two paths needing (3, 1) and (1, 3) it gives (1, 1), which
  suffices for neither"; its note of 2026-11-05 says "The peak-capacity
  case is worked on a degree-4 vertex in [CLAIM-590](../claims.d/CLAIM-590.md)". [CLAIM-574](../claims.d/CLAIM-574.md)'s "What it
  does not say" names "[CLAIM-563](../claims.d/CLAIM-563.md)'s closure condition" and "The
  cost-retaining version is an enrichment, as in [CLAIM-590](../claims.d/CLAIM-590.md)." [CLAIM-560](../claims.d/CLAIM-560.md)'s
  "What it does not say" cites [CLAIM-563](../claims.d/CLAIM-563.md) for cumulative costs and [CLAIM-585](../claims.d/CLAIM-585.md)
  for several resources.
- **Error and several resources.** [CLAIM-580](../claims.d/CLAIM-580.md) complements [CLAIM-585](../claims.d/CLAIM-585.md) and
  "puts the set of sufficient budgets of [CLAIM-585](../claims.d/CLAIM-585.md) between the true set
  shifted up by ε and shifted down by ε in each coordinate". [CLAIM-577](../claims.d/CLAIM-577.md),
  [CLAIM-581](../claims.d/CLAIM-581.md) and [CLAIM-586](../claims.d/CLAIM-586.md) send several resources to [CLAIM-585](../claims.d/CLAIM-585.md), and
  [CLAIM-591](../claims.d/CLAIM-591.md) notes that [CLAIM-571](../claims.d/CLAIM-571.md) and [CLAIM-585](../claims.d/CLAIM-585.md) are stated over paths
  without direction.
- **The filtrations.** [CLAIM-560](../claims.d/CLAIM-560.md) rests on [CLAIM-586](../claims.d/CLAIM-586.md) and complements
  [CLAIM-567](../claims.d/CLAIM-567.md), [CLAIM-583](../claims.d/CLAIM-583.md) and [CLAIM-591](../claims.d/CLAIM-591.md); its "What it does not say": "[CLAIM-583](../claims.d/CLAIM-583.md)
  shows reachability can differ where the complex agrees at every budget".
  [CLAIM-591](../claims.d/CLAIM-591.md): persistence "bounds the reachability filtration of [CLAIM-560](../claims.d/CLAIM-560.md)
  from above". [CLAIM-564](../claims.d/CLAIM-564.md) complements [CLAIM-586](../claims.d/CLAIM-586.md) and [CLAIM-574](../claims.d/CLAIM-574.md). [CLAIM-586](../claims.d/CLAIM-586.md)'s
  note of 2026-11-05 records [CLAIM-564](../claims.d/CLAIM-564.md) as filed from the reading of
  Ignatov, and reads [CLAIM-583](../claims.d/CLAIM-583.md) and [CLAIM-578](../claims.d/CLAIM-578.md) as marking what the complex
  does not carry. [CLAIM-583](../claims.d/CLAIM-583.md) complements [CLAIM-560](../claims.d/CLAIM-560.md), [CLAIM-565](../claims.d/CLAIM-565.md), [CLAIM-567](../claims.d/CLAIM-567.md),
  [CLAIM-590](../claims.d/CLAIM-590.md) and [CLAIM-607](../claims.d/CLAIM-607.md), and its body sends the version across languages
  to [CLAIM-607](../claims.d/CLAIM-607.md), which complements it. [QUESTION-391](../questions.d/QUESTION-391.md)'s note of 2026-11-05
  reads [CLAIM-586](../claims.d/CLAIM-586.md)'s structural frustration as relative to the declared
  configurations.
- **Fixed costs and their scope.** [CLAIM-594](../claims.d/CLAIM-594.md) complements [CLAIM-581](../claims.d/CLAIM-581.md),
  [CLAIM-570](../claims.d/CLAIM-570.md) and [CLAIM-598](../claims.d/CLAIM-598.md) and says of [CLAIM-581](../claims.d/CLAIM-581.md) and [CLAIM-570](../claims.d/CLAIM-570.md), "This claim
  marks their scope." [CLAIM-570](../claims.d/CLAIM-570.md)'s note of 2026-11-05: where the acting
  resource is heat, "A_a is not monotone in a ([CLAIM-594](../claims.d/CLAIM-594.md))". [CLAIM-581](../claims.d/CLAIM-581.md)
  complements [CLAIM-594](../claims.d/CLAIM-594.md). [CLAIM-598](../claims.d/CLAIM-598.md) complements [CLAIM-594](../claims.d/CLAIM-594.md) and says "This
  qualifies [CLAIM-577](../claims.d/CLAIM-577.md)'s reading of excess as standing slack."
- **Complexity.** [CLAIM-575](../claims.d/CLAIM-575.md) rests on [CLAIM-578](../claims.d/CLAIM-578.md), and [CLAIM-578](../claims.d/CLAIM-578.md)'s "What it
  does not say" names diagnosis as a further question "with its own
  complexity ([CLAIM-575](../claims.d/CLAIM-575.md))". [CLAIM-565](../claims.d/CLAIM-565.md) and [CLAIM-578](../claims.d/CLAIM-578.md) complement each other,
  and [CLAIM-565](../claims.d/CLAIM-565.md) cites [CLAIM-578](../claims.d/CLAIM-578.md) for one instance having no complexity.
  [CLAIM-565](../claims.d/CLAIM-565.md) and [CLAIM-578](../claims.d/CLAIM-578.md) bear on [QUESTION-376](../questions.d/QUESTION-376.md), whose summary says "[CLAIM-565](../claims.d/CLAIM-565.md)
  gives a pair with one clone and opposite navigation"; its "What would
  answer it" names [CLAIM-571](../claims.d/CLAIM-571.md)'s threshold, and its "What would not answer
  it" cites [CLAIM-578](../claims.d/CLAIM-578.md). [CLAIM-567](../claims.d/CLAIM-567.md) complements [CLAIM-578](../claims.d/CLAIM-578.md). [QUESTION-375](../questions.d/QUESTION-375.md) cites
  [CLAIM-571](../claims.d/CLAIM-571.md) for what persistence sees and [CLAIM-591](../claims.d/CLAIM-591.md) for what it forgets.
- **The two budgets.** [CLAIM-557](../claims.d/CLAIM-557.md) rests on [CLAIM-574](../claims.d/CLAIM-574.md) and [CLAIM-581](../claims.d/CLAIM-581.md) and
  complements [CLAIM-570](../claims.d/CLAIM-570.md) and [CLAIM-577](../claims.d/CLAIM-577.md); its summary adds [CLAIM-590](../claims.d/CLAIM-590.md)'s
  sublevel groupoid. [CLAIM-574](../claims.d/CLAIM-574.md)'s note of 2026-11-05 returns the pairing.
  [CLAIM-570](../claims.d/CLAIM-570.md) and [CLAIM-592](../claims.d/CLAIM-592.md) rest on [CLAIM-574](../claims.d/CLAIM-574.md) and [CLAIM-581](../claims.d/CLAIM-581.md), [CLAIM-592](../claims.d/CLAIM-592.md) also
  on [CLAIM-570](../claims.d/CLAIM-570.md); [CLAIM-570](../claims.d/CLAIM-570.md)'s body: "[CLAIM-557](../claims.d/CLAIM-557.md) says the outside and inside
  partitions move in opposite directions; this gives the two boundaries at
  which one contains the other", and [CLAIM-592](../claims.d/CLAIM-592.md)'s: "[CLAIM-557](../claims.d/CLAIM-557.md) said
  individuation is indexed by two budgets; this says what decides whether
  those budgets ever see the same thing." [CLAIM-577](../claims.d/CLAIM-577.md)'s note of 2026-11-05:
  "[CLAIM-557](../claims.d/CLAIM-557.md) reads this claim as a decoupling of two budgets".
- **The enrichment.** [CLAIM-581](../claims.d/CLAIM-581.md): the threshold is "the hom of the
  max-enriched category of [CLAIM-590](../claims.d/CLAIM-590.md)"; [CLAIM-590](../claims.d/CLAIM-590.md)'s note of 2026-11-05
  returns it. [CLAIM-574](../claims.d/CLAIM-574.md) and [CLAIM-590](../claims.d/CLAIM-590.md) complement each other; [CLAIM-590](../claims.d/CLAIM-590.md)
  complements [CLAIM-581](../claims.d/CLAIM-581.md) and [CLAIM-583](../claims.d/CLAIM-583.md). [QUESTION-384](../questions.d/QUESTION-384.md) cites [CLAIM-590](../claims.d/CLAIM-590.md)'s
  enriched profiles and [CLAIM-574](../claims.d/CLAIM-574.md)'s restricted profiles as the relational
  side of its comparison.
- **Legibility.** [CLAIM-574](../claims.d/CLAIM-574.md)'s note of 2026-11-07 sets it beside [CLAIM-455](../claims.d/CLAIM-455.md):
  "Read together, distinctions grow with the probe family, and legibility
  grows with the observer's rule class".
- **Shared budget and readiness.** [CLAIM-572](../claims.d/CLAIM-572.md) rests on [CLAIM-570](../claims.d/CLAIM-570.md) and
  [CLAIM-574](../claims.d/CLAIM-574.md), takes [CLAIM-581](../claims.d/CLAIM-581.md)'s peak cost as its instance of a reach cost,
  complements [CLAIM-592](../claims.d/CLAIM-592.md) and [CLAIM-561](../claims.d/CLAIM-561.md), and reads a reallocation as
  [CLAIM-571](../claims.d/CLAIM-571.md)'s threshold "in budget space rather than configuration space";
  of [CLAIM-561](../claims.d/CLAIM-561.md): "Sending the general response early is the hedge at o =
  0." Its note of 2026-11-07, "noted, not filed", prices [CLAIM-592](../claims.d/CLAIM-592.md)'s
  agreement on [CASE-206](../cases.d/CASE-206.md)'s vertex under one budget. [CLAIM-632](../claims.d/CLAIM-632.md) counts
  [CLAIM-561](../claims.d/CLAIM-561.md) among those that show a reserve's value is conditional, and
  disclaims readiness in [CLAIM-572](../claims.d/CLAIM-572.md)'s sense, "the observing and response
  budget, which is a different notion".
- **Control and constraint.** [CLAIM-542](../claims.d/CLAIM-542.md) rests on [CLAIM-345](../claims.d/CLAIM-345.md), and its
  summary: "[CLAIM-345](../claims.d/CLAIM-345.md) holds the cost formula and not the allocation across
  channels." [CLAIM-589](../claims.d/CLAIM-589.md) rests on [CLAIM-345](../claims.d/CLAIM-345.md) and [CLAIM-542](../claims.d/CLAIM-542.md) for its cost and
  reliability separations, cites [CLAIM-567](../claims.d/CLAIM-567.md)'s fork ("A reachable target can
  also be reached with probability 1/2 when the process meets an unbiased
  fork"), and complements [CLAIM-567](../claims.d/CLAIM-567.md) and [CLAIM-582](../claims.d/CLAIM-582.md). [CLAIM-582](../claims.d/CLAIM-582.md)'s reliability
  witness is "[CLAIM-567](../claims.d/CLAIM-567.md)'s fork" with the distractor branch blocked, and it
  complements [CLAIM-567](../claims.d/CLAIM-567.md) and [CLAIM-589](../claims.d/CLAIM-589.md). [CLAIM-567](../claims.d/CLAIM-567.md) complements [CLAIM-582](../claims.d/CLAIM-582.md) and
  [CLAIM-589](../claims.d/CLAIM-589.md).
- **Synchronization.** [ARG-061](../arguments.d/ARG-061.md) concludes [CLAIM-618](../claims.d/CLAIM-618.md) and names [CLAIM-567](../claims.d/CLAIM-567.md)'s
  feasible and reliably reached as what the regions are once Q(λ) is the
  locked configurations; its "What it does not show" sends reachability
  and basin size to [CLAIM-567](../claims.d/CLAIM-567.md) and the coincidence of boundaries to
  [QUESTION-438](../questions.d/QUESTION-438.md). [CLAIM-618](../claims.d/CLAIM-618.md) complements [CLAIM-567](../claims.d/CLAIM-567.md), which complements it back,
  bears on [QUESTION-438](../questions.d/QUESTION-438.md), and cites [ARG-061](../arguments.d/ARG-061.md) for the two premises it needs.
  [QUESTION-438](../questions.d/QUESTION-438.md): "[CLAIM-618](../claims.d/CLAIM-618.md) gives the two objects".

## Links to other parts, stated

From this part's members to members of the line's other parts, each pair
once, with the entry that states it. Eighteen pairs: seven to the part on
effective constraints and probes ([SYNTHESIS-075](SYNTHESIS-075.md)), six to the part on
frustration ([SYNTHESIS-074](SYNTHESIS-074.md)), three to the part on intervention
([SYNTHESIS-079](SYNTHESIS-079.md)) and two to the part on stability
([SYNTHESIS-080](SYNTHESIS-080.md)). None reach the small clusters or the entries the line account ([SYNTHESIS-088](SYNTHESIS-088.md)) integrates directly.

- **To [SYNTHESIS-075](SYNTHESIS-075.md).**
  - [CLAIM-574](../claims.d/CLAIM-574.md) rests on [CLAIM-264](../claims.d/CLAIM-264.md): "agreement on a restricted family can
    fall short of isomorphism, and a dense family restores full
    faithfulness. This claim adds the order between".
  - [CLAIM-574](../claims.d/CLAIM-574.md) and [CLAIM-302](../claims.d/CLAIM-302.md) complement each other. [CLAIM-574](../claims.d/CLAIM-574.md)'s body:
    "[CLAIM-302](../claims.d/CLAIM-302.md)'s efficient tests are a subfamily of all tests".
  - [CLAIM-574](../claims.d/CLAIM-574.md) uses [TERM-069](../terms.d/TERM-069.md) and [TERM-065](../terms.d/TERM-065.md): "The same holds, more simply,
    for [TERM-069](../terms.d/TERM-069.md)'s observational equivalence", and "This is [TERM-065](../terms.d/TERM-065.md)'s
    regime with its probes ordered".
  - [CLAIM-574](../claims.d/CLAIM-574.md) names [CLAIM-152](../claims.d/CLAIM-152.md) in the same sentence: "and [CLAIM-152](../claims.d/CLAIM-152.md)'s
    relativity to a target with the targets nested".
  - [CLAIM-557](../claims.d/CLAIM-557.md)'s "What it adds": "[CLAIM-302](../claims.d/CLAIM-302.md)'s pseudorandom ensembles are
    the converse limit"; [CLAIM-302](../claims.d/CLAIM-302.md)'s note of 2026-11-05: "[CLAIM-557](../claims.d/CLAIM-557.md) sets
    this claim's pseudorandom ensembles at one end of a two-budget
    picture".
  - [QUESTION-384](../questions.d/QUESTION-384.md)'s "What would not answer it": "Agreement under probes
    chosen to agree. [CLAIM-322](../claims.d/CLAIM-322.md): such probes show only that they can be
    selected."
- **To [SYNTHESIS-074](SYNTHESIS-074.md).**
  - [CLAIM-572](../claims.d/CLAIM-572.md) rests on [CLAIM-535](../claims.d/CLAIM-535.md): "[CLAIM-535](../claims.d/CLAIM-535.md)'s setting, with costs on both
    halves"; [CLAIM-535](../claims.d/CLAIM-535.md)'s note of 2026-11-07 reads A58 §8's route as
    "[CLAIM-572](../claims.d/CLAIM-572.md)'s hedge, and it is open only where a hedge exists".
  - [CLAIM-559](../claims.d/CLAIM-559.md) rests on [CLAIM-561](../claims.d/CLAIM-561.md): its first stage's "ΔV(p0) > 0, as in
    [CLAIM-561](../claims.d/CLAIM-561.md)".
  - [CLAIM-586](../claims.d/CLAIM-586.md)'s body: "[CLAIM-365](../claims.d/CLAIM-365.md)'s worked case, where no budget helps, is a
    non-face of K_Q". [CLAIM-631](../claims.d/CLAIM-631.md) (Proposed) takes [CLAIM-586](../claims.d/CLAIM-586.md) as a premise in
    its body: "everything below holds at any budget b, taking ℛ as the
    arrangements affordable at b."
  - [CLAIM-618](../claims.d/CLAIM-618.md)'s body: "[CLAIM-538](../claims.d/CLAIM-538.md) gives tolerances only for real offsets";
    [CLAIM-538](../claims.d/CLAIM-538.md)'s note of 2026-11-07: "[CLAIM-618](../claims.d/CLAIM-618.md), filed from the same
    exchange, uses circle-valued acceptance sets with tolerances and
    leaves their feasibility test unstated." [CLAIM-634](../claims.d/CLAIM-634.md) (Proposed) sets
    [CLAIM-618](../claims.d/CLAIM-618.md) outside its scope: "[CLAIM-153](../claims.d/CLAIM-153.md) and [CLAIM-618](../claims.d/CLAIM-618.md) are on S¹, where
    winding enters and the convex test does not transfer."
- **To [SYNTHESIS-079](SYNTHESIS-079.md).**
  - [CLAIM-577](../claims.d/CLAIM-577.md)'s "What it adds": "[CLAIM-414](../claims.d/CLAIM-414.md)'s matched trajectories and the
    unrecorded calls of [CASE-203](../cases.d/CASE-203.md) are the observational side of this."
  - [CLAIM-632](../claims.d/CLAIM-632.md)'s body: "[CLAIM-414](../claims.d/CLAIM-414.md) (Active) holds that intervention is not
    the only way to tell systems apart".
  - [QUESTION-391](../questions.d/QUESTION-391.md)'s body cites [CLAIM-480](../claims.d/CLAIM-480.md) among the held time-scale forms:
    "eliminating a slowly relaxing interior leaves a history-dependent
    constraint".
- **To [SYNTHESIS-080](SYNTHESIS-080.md).**
  - [CLAIM-577](../claims.d/CLAIM-577.md) and [CLAIM-079](../claims.d/CLAIM-079.md) complement each other; [CLAIM-577](../claims.d/CLAIM-577.md)'s "What it
    adds": "It is stability without viability by budget ([CLAIM-079](../claims.d/CLAIM-079.md))".
  - [CLAIM-589](../claims.d/CLAIM-589.md)'s body: "This is the shape of [CLAIM-079](../claims.d/CLAIM-079.md)'s split between
    stability and viability, with the input bound as the constraint."



## Whether the part holds together

Counting each pair of the 38 members linked by a front-matter relation or
a mention in either's body, summary or history, there are 84 pairs inside
the part and 18 to other parts. Grouped by what they argue:

| | reaching (24) | individuation (9) | control (2) | synchronization (3) |
|---|---|---|---|---|
| reaching | 41 | 15 | 2 | 2 |
| individuation | | 20 | 0 | 0 |
| control | | | 1 | 0 |
| synchronization | | | | 3 |

The individuation members ([CLAIM-557](../claims.d/CLAIM-557.md), [CLAIM-570](../claims.d/CLAIM-570.md), [CLAIM-572](../claims.d/CLAIM-572.md), [CLAIM-574](../claims.d/CLAIM-574.md),
[CLAIM-581](../claims.d/CLAIM-581.md), [CLAIM-590](../claims.d/CLAIM-590.md), [CLAIM-592](../claims.d/CLAIM-592.md), [CLAIM-455](../claims.d/CLAIM-455.md) and [QUESTION-384](../questions.d/QUESTION-384.md)) are tied to
the rest by 15 pairs, among them [CLAIM-581](../claims.d/CLAIM-581.md)'s and [CLAIM-590](../claims.d/CLAIM-590.md)'s resting on
[CLAIM-571](../claims.d/CLAIM-571.md) and [CLAIM-563](../claims.d/CLAIM-563.md), so the part is one inquiry, as [SYNTHESIS-043](SYNTHESIS-043.md) found
for the same two groups in the realizability line. The control pair
reaches the part only through [CLAIM-589](../claims.d/CLAIM-589.md). The synchronization members reach
it only through [CLAIM-567](../claims.d/CLAIM-567.md) (two pairs) and reach the frustration part by as
many ([CLAIM-618](../claims.d/CLAIM-618.md) with [CLAIM-538](../claims.d/CLAIM-538.md) and [CLAIM-634](../claims.d/CLAIM-634.md)); their text names [CLAIM-567](../claims.d/CLAIM-567.md)'s
split as what they carry over, so they are kept here.

## Not stated on the record

Links across the components that no entry states, tested by [ADR-075](../decisions.d/ADR-075.md)'s
step 5 at this review:

- **Spend-matching inside a shared budget.** That under [CLAIM-577](../claims.d/CLAIM-577.md)'s rule
  applied to the acting share of [CLAIM-572](../claims.d/CLAIM-572.md)'s budget, an organization that
  holds its posture through a quiet period stays ready only where each
  circumstance has an acceptable response within the holding cost, so no
  observing restores what the rule foreclosed. Which spend the rule
  matches, and whether probes recur each period, is a free parameter;
  closed as the acting share only, the sentence is [CLAIM-577](../claims.d/CLAIM-577.md)'s step 3
  substituted into [CLAIM-572](../claims.d/CLAIM-572.md)'s criterion with [CLAIM-572](../claims.d/CLAIM-572.md)'s point 1, a
  trivial derivation. Not filed.
- **Stability carried to the boundaries.** That [CLAIM-580](../claims.d/CLAIM-580.md)'s bound carries
  to [CLAIM-570](../claims.d/CLAIM-570.md)'s boundary a_S(o) and [CLAIM-572](../claims.d/CLAIM-572.md)'s cheapest readiness, each a
  maximum or minimum of thresholds. Valid and trivial. Not filed.
- **Stability not carried to the agreement.** That an estimate of the
  requirement within ε, which fixes every threshold to within ε
  ([CLAIM-580](../claims.d/CLAIM-580.md)), does not fix which merge-tree levels [CLAIM-592](../claims.d/CLAIM-592.md)'s two chains
  agree on, since two merges within 2ε can be reordered. It passes the derivation route and is filed at this review as [CLAIM-639](../claims.d/CLAIM-639.md) (Proposed), which this account integrates.
- **A parameter-indexed complex against a budgeted one.** That [CLAIM-618](../claims.d/CLAIM-618.md)'s
  complex over control parameters, unlike [CLAIM-586](../claims.d/CLAIM-586.md)'s over a budget, need
  not be monotone. It turns on Q(λ), which [ARG-061](../arguments.d/ARG-061.md) finds unstated: a free
  parameter. Not filed.
- **Control energy as a cumulative cost.** That [CLAIM-345](../claims.d/CLAIM-345.md)'s least effort,
  a sum over steps, is a cumulative expenditure, so by [CLAIM-563](../claims.d/CLAIM-563.md) the
  displacements affordable within a finite positive energy budget are not
  closed under composition. An instance of [CLAIM-563](../claims.d/CLAIM-563.md)'s sum case. Not
  filed.

## What it does not say

- That organizations have configuration spaces, holding requirements,
  probe costs or Gramians of these kinds; each component says its
  organizational reading is A's analogy or a model.
- That physical probe families are nested, or physical moves reversible;
  the DNA origami readings on [CLAIM-574](../claims.d/CLAIM-574.md), [CLAIM-581](../claims.d/CLAIM-581.md) and [CLAIM-591](../claims.d/CLAIM-591.md) find them
  often not.
- That the locking region equals the compatibility region for the
  ordinary tongue without the premise [ARG-061](../arguments.d/ARG-061.md) names ([CLAIM-618](../claims.d/CLAIM-618.md), Proposed).
- Anything with standing of its own.
