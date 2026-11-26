---
number: 76
status: Proposed
formerly:
- SYNTHESIS-tmpc35sn
title: 'Reaching under a budget is not holding'
statement: >-
  Reaching under a budget is not holding, and telling apart is not turning
  into one another: feasible, reachable and reliably reached come apart, a
  transition's threshold is the least peak over admissible paths, stable
  under error and a frontier rather than a total when there are several
  resources, how the resource composes fixes both whether the affordable
  processes compose and which modal logic reachability within a budget
  validates, a budget grows a compatibility complex and a reachability
  filtration that do not fix each other, observing budgets split what can be
  told apart while acting budgets under peak costs merge what can be
  reached, the budget at which a difference first shows or first matters is
  a threshold and not a distance, the category chosen decides what counts
  as the same, navigating and diagnosing have complexities of their own,
  and the same split recurs for control inputs and for synchronization
  demands indexed by control parameters
version: 2
history:
- version: 2
  date: '2026-11-26'
  note: >-
    At the synthesis review of 2026-11-26, under ADR-151, rewritten from
    an inventory into one argument, and placing the two demonstrated
    claims of 2026-11-26 the filing's synthesis worker left for this
    review: CLAIM-tmpti7cf (the modal logics of budgeted reach) and
    CLAIM-tmpik3z0 (κ as the separating budget). With them come the
    entries their steps need: CLAIM-tmpi0rdz, which rests on
    CLAIM-tmpti7cf; QUESTION-tmpahfz9, which it answers in part;
    CLAIM-646, the limit it names; and CLAIM-968 with CASE-373, the
    measured separating budget CLAIM-tmpik3z0 complements. Other entries
    filed since version 1 that touch this part's members are named in the
    body and left to a coverage pass. The per-component list, the list of
    links stated and the table of pairs are dropped; they are in version
    1. The statement is extended; the title is unchanged.
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
- CLAIM-tmpti7cf
- CLAIM-tmpi0rdz
- CLAIM-646
- QUESTION-tmpahfz9
- CLAIM-968
- CASE-373
- CLAIM-tmpik3z0
summary: >-
  A part synthesis of the formal-apparatus line: the part on
  feasibility, reachability and thresholds under resources, with the
  restricted Yoneda profiles and budgeted individuation built on them,
  the modal reading of budgeted reach and the separating budget added on
  2026-11-26. Nearly all its members are first in another line
  (realizability, readiness, will-organization or distributed-agency), and
  most are integrated by an account of that line as well; this one
  integrates them because their `line` includes formal-apparatus. The
  line's account is built over it. It adds nothing of its own; its
  standing is its components'.
---
<!-- inactive-ok-file: CLAIM-618 ARG-061 — Proposed; components, with their standing -->
<!-- inactive-ok-file: SYNTHESIS-024 SYNTHESIS-027 SYNTHESIS-040 SYNTHESIS-041 SYNTHESIS-042 SYNTHESIS-043 SYNTHESIS-045 SYNTHESIS-051 SYNTHESIS-056 SYNTHESIS-068 CLAIM-631 CLAIM-634 CASE-203 — Proposed; the accounts that already integrate the members, and entries cited for what they hold, nothing here resting on their being settled -->
<!-- inactive-ok-file: SYNTHESIS-009 — Superseded; cited as the entry CLAIM-632 returned from -->
<!-- inactive-ok-file: ARG-053 — Rejected; cited as the argument CLAIM-561 undercuts -->
<!-- inactive-ok-file: SYNTHESIS-074 SYNTHESIS-075 SYNTHESIS-079 SYNTHESIS-080 SYNTHESIS-088 — Proposed; cited with its standing -->
<!-- inactive-ok-file: CLAIM-tmpti7cf CLAIM-tmpi0rdz CLAIM-tmpik3z0 QUESTION-tmpahfz9 TERM-tmp8nuak SYNTHESIS-tmp4kh41 CLAIM-646 CLAIM-968 CASE-373 CLAIM-654 CLAIM-663 CLAIM-770 CLAIM-780 CLAIM-781 CLAIM-878 CLAIM-921 CLAIM-944 CLAIM-969 CLAIM-999 CLAIM-1046 CLAIM-1079 CLAIM-1095 CLAIM-1097 CLAIM-1151 CLAIM-1171 CLAIM-1186 CLAIM-1192 CLAIM-679 CASE-267 CASE-269 — Proposed or Open; components and entries cited at the synthesis review of 2026-11-26 -->

# SYNTHESIS-076: Reaching under a budget is not holding

*A part synthesis of the formal-apparatus line ("Formal apparatus", ADR-040): the part grouped around CLAIM-571's threshold and CLAIM-567's three properties, with the restricted Yoneda profiles and budgeted individuation built on them, the control-cost results they borrow, and the parameter-indexed complex of synchronization demands. The line's synthesis, SYNTHESIS-088, is built over it and its sibling parts: SYNTHESIS-075 (effective constraints and probes), SYNTHESIS-074 (frustration), SYNTHESIS-079 (intervention) and SYNTHESIS-080 (stability). Its members are also integrated by accounts of their first lines, chiefly SYNTHESIS-042 (reaching under resources), SYNTHESIS-040 (budgeted individuation) and SYNTHESIS-024 (readiness). Version 2 is written under ADR-151. It adds nothing. Its standing is its components'.*

## The question

What does a resource budget do to what a system can reach, and to what
can be told apart in it? The part answers in one direction throughout:
having enough to hold a configuration, or to tell two apart, is not
having enough to reach it or to turn one into the other.

## The argument

**Feasible, reachable and reliably reached are three, and the threshold
sits between the first two.** Each is implied by the next and none
implies it, which puts reachability between the structural infeasibility
and the realized violation CLAIM-357 separates (CLAIM-567). For one
capacity and a fixed architecture, the threshold for reaching a target
is the least, over admissible paths, of the peak requirement along the
path, infinite when no path joins the two (CLAIM-571). Whether the
affordable processes compose depends on how the resource composes:
closure holds exactly when b ⊗ b ≤ b, always for the maximum and, for
the sum, only at 0 and infinity, so the peak case is the threshold's
(CLAIM-563).

**How the resource composes also fixes the logic of what is possible
within a budget.** Read reachability within b as a modal accessibility
relation, as A19 of the exchange of 2026-11-26 proposed for
QUESTION-tmpahfz9 (the owner's question on how the record's geometries of
possibility relate). Then under peak costs with reversible moves and free
holding it is an equivalence at every budget and validates S5; with
one-way moves it is a preorder, S4; where holding a configuration costs,
it is reflexive only where the budget can hold, KB4 on the whole space;
under cumulative costs axiom 4 fails at every finite positive budget,
and possibility within b of possibility within c gives possibility within
b + c, against max(b, c) under peak costs (CLAIM-tmpti7cf, the
assistant's). Each case restates CLAIM-563, CLAIM-581 and CLAIM-591, and
the claim says so: what it adds is that the record's resource semantics
and its modal semantics are one choice. Its limit is CLAIM-646: two
systems with the same threshold between every pair, and so the same S5
frames at every budget, can differ in cumulative cost by any factor. One
consequence is drawn. In an S5 frame what can be made to hold
necessarily already holds necessarily, so a difference that is latent at
a configuration cannot be made entrenched within the same reversible
peak budget; entrenchment needs one-way moves or a lower budget to hold
with than the one used to reach, which the budget tree supplies
(CLAIM-tmpi0rdz, resting on CLAIM-tmpti7cf and CLAIM-581). It names
CLAIM-571's gap between reaching and holding and CLAIM-679's slack cut to
need as the record's instances.

**The threshold as a planner meets it.** It moves by at most the largest
error in the requirement, so a planner who knows each cost within ε
knows each threshold within ε and its slack within 2ε (CLAIM-580), and
an estimate within ε does not fix which merge-tree levels CLAIM-592's
two chains agree on, since two merges within 2ε can be reordered
(CLAIM-639, filed at the review that wrote version 1). With several
capacities the sufficient budgets form an up-set with a frontier, which
need not be convex, so no threshold on a weighted total describes it
(CLAIM-585). A budget set each period to last period's peak never rises,
and any transition whose threshold exceeds the cost of holding is lost
after one period spent holding (CLAIM-577), stability without viability
produced by a budget rule.

**A budget grows two filtrations that do not fix each other.** The
budgeted compatibility complex grows with the budget and never exceeds
the unbudgeted one, so a missing face is either short of resources or
structurally frustrated (CLAIM-586), and implications among demands are
antitone in the budget (CLAIM-564). Beside it runs a reachability
filtration: the complex depends on the admissible configurations and the
demands, reachability on how they are joined by moves, and neither fixes
the other (CLAIM-560). Two systems with the same complex, move rule and
costs can differ in reachability (CLAIM-583), and one level up, for
constraint languages, the same holds conditionally (CLAIM-607). Under
directed moves connectivity does not settle reachability, so a
persistence summary bounds the reachability filtration without fixing it
(CLAIM-591).

**Where a budget is not a budget.** When the resource that pays for
crossings also sets the costs, as heat does, reaching need not be
monotone in the resource, and fixed-cost reachability is the special
case (CLAIM-594); whether uniform abundance helps turns on whether the
competing steps consume it (CLAIM-598). Both mark the scope of the
monotone results above.

**Navigating and diagnosing have complexities of their own.**
Complexity belongs to a family of problems, not to one organization's
complex (CLAIM-578). Telling geometric disconnection from a capacity
bottleneck can be PSPACE-hard, and how far over budget the cheapest path
is NP-hard (CLAIM-575, resting on CLAIM-578). Two constraint languages
with the same clone can lie on opposite sides of the navigation
dichotomy (CLAIM-565), which answers QUESTION-376 for Boolean languages
with constants.

**Telling apart runs the other way from turning into one another.**
Restricted Yoneda profiles over nested probe families only split objects
as the budget grows (CLAIM-574). Under peak costs on reversible moves the
threshold is an extended pseudo-ultrametric, so identification within an
acting budget is an equivalence whose classes nest into one tree, and the
resource semantics is an individuation choice (CLAIM-581). So a system's
budgeted individuation is indexed by two budgets, an observing one that
splits and an acting one that merges, which can be traded or decoupled
(CLAIM-557, resting on both). CLAIM-570 gives the region of budget pairs
where one partition contains the other and its boundaries, and the two
partitions agree only on levels common to both chains, with the cost
order deciding which appear (CLAIM-592). The path groupoid of a degree-4
vertex identifies its folded states while the category enriched in peak
footprint keeps them 1.866 apart, so equivalence of possibilities is not
equivalence of resource-bounded capabilities (CLAIM-590). For one bounded
observer, a transformation can make one task's distinction legible and
another's illegible (CLAIM-455).

**The budget at which a difference first shows, or first matters, is a
threshold, not a distance.** Probing two compatibility-equivalent
systems at rising move budgets, the verdict stabilizes at a finite
budget, and a construction realizes any chosen one, so the budget at
which a reachability distinction first appears is a measurable threshold
(CLAIM-968, run in CASE-373). A23 of the exchange of 2026-11-26 defined a
consequentiality threshold κ, the least cost of a witness under which the
difference between two configurations produces an outcome difference of
at least ε. It is the least budget at which A23's own budgeted
consequential difference reaches ε, so it is the record's separating
budget for outcome distinctions (CLAIM-570, CLAIM-968); and it is not a
distance: infinite for a configuration and itself, failing the triangle
inequality, and bound only by the reverse inequality
min(κ_{ε/2}(x, y), κ_{ε/2}(y, z)) ≤ κ_ε(x, z) (CLAIM-tmpik3z0, the
assistant's, resting on CLAIM-570 and CLAIM-574). What A23 adds is the
witness family, probes that become available through attainable
development, which needs the witness to be common to the two
configurations (TERM-tmp8nuak).

**One budget for observing and acting.** When both draw on one budget,
the cheapest readiness buys a whole prefix of the probes, the affordable
splits can be disconnected, and stopping when the next probe does not pay
can miss the optimum; a reallocation is a transition with its own
threshold in budget space (CLAIM-572, resting on CLAIM-570, CLAIM-574
and CLAIM-535). Provisional mobilization can minimize expected loss when
the resource is more likely to be cancelled than used, so a cancellation
rate alone cannot identify waste (CLAIM-561). Records kept per capacity
bound readiness and identify it only when the capacities' dependence is
known (CLAIM-632).

**The same split recurs for control and for synchronization.** Equal
controllability rank does not fix the cost of control (CLAIM-345), and
sensitivity fixes neither the allocation nor the authorship of control
(CLAIM-542, the owner's point). Permitted directions, actuated directions
and transitions achievable at acceptable cost are three objects
(CLAIM-589, resting on both), and an added hard constraint in a fixed
model cannot enlarge reach, only robustness or reliability (CLAIM-582).
Over a space of control parameters, each locking region lies inside the
compatibility region of the same demands and need not equal it, which is
CLAIM-567's split carried over (CLAIM-618, the owner's conjecture, A's
construction, Proposed); its argument needs a premise it does not state,
that the admissible configurations are the locked ones (ARG-061).

## Where it stands

The members of version 1 are Active demonstrations, except CLAIM-618
and ARG-061, which are Proposed. The entries added here are Proposed:
CLAIM-646 and CLAIM-968 are demonstrated and unreviewed, and the modal
reading and the separating budget of 2026-11-26 are checked derivations
awaiting review. The organizational readings of all
of it are A's analogies or models, as each component says.

Open: whether a resource-indexed topological summary detects navigation
complexity (QUESTION-375); what property of a constraint language fixes
navigation beyond Boolean languages and under budgets (QUESTION-376);
when restricted enriched profiles agree with bisimulation pseudometrics
(QUESTION-384); when an effective constraint stops being a good
approximation (QUESTION-391); when changes in the complex of
synchronization demands coincide with bifurcations of the locked states
(QUESTION-438); and how the record's geometries of possibility relate
(QUESTION-tmpahfz9), which CLAIM-tmpti7cf answers for reachability within
one resource.

The part is one inquiry, not several: at version 1, 15 of the 84 pairs
inside it joined the individuation members to the reaching members,
among them CLAIM-581's and CLAIM-590's resting on CLAIM-571 and
CLAIM-563; the control pair reaches it only through CLAIM-589, and the
synchronization members only through CLAIM-567, whose split their text
says they carry. The entries of 2026-11-26 rest on members of both
groups. Its links to the sibling parts are stated in version 1 and are
unchanged: chiefly CLAIM-574 on CLAIM-264 and CLAIM-302 (SYNTHESIS-075),
CLAIM-572 on CLAIM-535 and CLAIM-586 on CLAIM-365 (SYNTHESIS-074),
CLAIM-577 with CLAIM-414 (SYNTHESIS-079), and CLAIM-577 and CLAIM-589
with CLAIM-079 (SYNTHESIS-080).

**Not yet taken into account.** Entries filed between version 1 and
2026-11-26 that carry formal-apparatus and rest on, complement or
corroborate a member here are not integrated by this version, which
places only the filings of 2026-11-26: CLAIM-654, CLAIM-663, CLAIM-770,
CLAIM-780, CLAIM-781, CLAIM-878, CLAIM-921, CLAIM-944, CLAIM-969,
CLAIM-999, CLAIM-1046, CLAIM-1079, CLAIM-1095, CLAIM-1097, CLAIM-1151,
CLAIM-1171, CLAIM-1186 and CLAIM-1192, with CASE-267 and CASE-269 on
QUESTION-438. Most are integrated by an account of another line or
another formal-apparatus part; CLAIM-780, CLAIM-921, CLAIM-944,
CLAIM-1079, CLAIM-1097 and CLAIM-1151 by none. Whether each belongs here
is the next coverage pass's question.

## Not stated on the record

- **Spend-matching inside a shared budget.** That under CLAIM-577's rule
  applied to the acting share of CLAIM-572's budget, an organization
  that holds its posture through a quiet period stays ready only where
  each circumstance has an acceptable response within the holding cost.
  Closed as the acting share only, it is CLAIM-577's step 3 substituted
  into CLAIM-572's criterion, a trivial derivation. Not filed.
- **Stability carried to the boundaries.** That CLAIM-580's bound
  carries to CLAIM-570's boundary and CLAIM-572's cheapest readiness,
  each a maximum or minimum of thresholds. Valid and trivial. Not filed.
- **A parameter-indexed complex against a budgeted one.** That
  CLAIM-618's complex over control parameters, unlike CLAIM-586's over a
  budget, need not be monotone. It turns on the admissible
  configurations, which ARG-061 finds unstated: a free parameter. Not
  filed.
- **Control energy as a cumulative cost.** That CLAIM-345's least
  effort, a sum over steps, is a cumulative expenditure, so by CLAIM-563
  the displacements affordable within a finite energy budget are not
  closed under composition and, by CLAIM-tmpti7cf, axiom 4 fails for
  them. An instance of the sum case. Not filed.
- **The two budgets as two S5 families.** That under reversible peak
  costs both of CLAIM-557's budgets give equivalence frames, the acting
  family coarsening as its budget grows (CLAIM-tmpti7cf, CLAIM-581) and
  the observing family refining (CLAIM-574, CLAIM-tmpik3z0's filtration),
  so CLAIM-557's opposite directions are two nested families of S5
  frames. A restatement of CLAIM-557 in the modal vocabulary. Not filed.
- **A budget rule as the lower budget of entrenchment.** CLAIM-tmpi0rdz's
  third route needs holding at a lower budget than the one used to reach.
  CLAIM-577's rule produces exactly that, a budget fallen to the holding
  cost; CLAIM-tmpi0rdz names CLAIM-679's slack cut to need and not
  CLAIM-577. The same point on a second instance. Not filed.

## What it does not say

- That organizations have configuration spaces, holding requirements,
  probe costs or Gramians of these kinds; each component says its
  organizational reading is A's analogy or a model.
- That physical probe families are nested, or physical moves
  reversible; the DNA origami readings on CLAIM-574, CLAIM-581 and
  CLAIM-591 find them often not.
- That the modal reading is the right geometry of possibility: two move
  graphs with the same budgeted classes have the same S5 frames and may
  differ in cumulative cost by any factor (CLAIM-646).
- That separating outcomes shows the difference causes them
  (CLAIM-tmpik3z0).
- That the locking region equals the compatibility region for the
  ordinary tongue without the premise ARG-061 names.
- Anything with standing of its own.
