---
number: 199
status: Active
formerly:
- CASE-tmp0d5si
title: 'Three configurations, all mutually reachable and so isomorphic in the path groupoid, with one-way costs U to L 1, L to U 3, U to R 3 and R to U 1: the additive cheapest-cost distance is directed and graded, d(L, R) = 6 against d(R, L) = 2, each configuration''s cost-to-target profile recovers it exactly, and under peak costs the same moves give other distances'
version: 2
history:
- version: 2
  date: '2026-11-06'
  note: >-
    Promoted at the status review's ruling (the owner delegated these
    rulings; ADR-057): a construction whose facts are its definition
    (ADR-042), its stated computations (both closures, the triangle
    inequality, recovery from profiles, budget-2 reach, budgeted
    transitivity, the observing and acting frontiers) re-run
    independently by a second checker with python3 -I. Standing
    fictional is kept.
standing: fictional
kind: construction
tags:
- mathematics
- individuation
- complex-systems
date: '2026-11-05'
line:
- realizability
illustrates:
- CLAIM-590
- CLAIM-581
summary: >-
  A's toy, from the owner's paste of 2026-11-05 (fourth), A's "Toward a
  resource-sensitive Yoneda theory of individuation" §§2 and 3: an origami
  mechanism's unfolded state U and two folded states L and R, with
  d(U, L) = 1, d(L, U) = 3, d(U, R) = 3 and d(R, U) = 1, the cheapest moves
  between L and R passing through U. A's table, its budget-2 example and its
  recovery formula d(x, y) = sup_p [d(p, y) − d(p, x)] are checked by the
  filer with python3 -I on all nine pairs. The filer adds the same moves
  under peak costs, where the distances change and mutual reachability
  within a budget is transitive, against the additive case, where at
  budget 3 it is not, so the toy is an instance of [CLAIM-581](../claims.d/CLAIM-581.md)'s
  contrast with directed moves. The construction is the filer's, from A's
  toy; adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-202 — Proposed; A's proposals of 2026-11-05, the assistant's own, the entries filed beside them and the record's open term for the senses of individuation, cited as filed, nothing here resting on their being settled -->

# CASE-199: Three configurations, all mutually reachable and so isomorphic in the path groupoid, with one-way costs U to L 1, L to U 3, U to R 3 and R to U 1: the additive cheapest-cost distance is directed and graded, d(L, R) = 6 against d(R, L) = 2, each configuration's cost-to-target profile recovers it exactly, and under peak costs the same moves give other distances

## The case

A (§3): "Suppose an origami mechanism has an unfolded reference state U
and two distinct folded configurations, L and R. Both folded states are
geometrically valid and physically reachable. But the actuation system
makes some transformations more expensive than others." The moves and
their costs are

d(U,L)=1, d(L,U)=3,
d(U,R)=3, d(R,U)=1,

with no direct move between L and R: "The cheapest transitions between the
folded states go through U: d(L,R)=6, d(R,L)=2." Costs add along a path
and an identity costs 0 (A §2: "If costs are additive under composition
and identity processes cost zero, then d(x,z) ≤ d(x,y)+d(y,z)"). The
distance d(x, y) is the least cost of a process from x to y. The
mechanism is invented, so the case is fictional; its facts are its
definition.

**The cost table** (row: from; column: to), A's and checked:

| from | to L | to U | to R |
|---|---|---|---|
| L | 0 | 3 | 6 |
| U | 1 | 0 | 3 |
| R | 2 | 1 | 0 |

**One groupoid, three distances.** A: "All configurations are mutually
reachable. In the ordinary path-groupoid description, all three are
isomorphic. But their resource profiles differ substantially." In the
Lawvere metric space the table defines, no two of them are isomorphic,
since that needs d(x, y) = d(y, x) = 0.

**Budgets.** A: "starting from U with a budget of 2, the system can reach
L but not R. Starting from R with the same budget, it can reach L, but the
reverse journey is unaffordable." Within budget 2, L reaches only itself,
U reaches L and U, and R reaches all three.

**Recovery from profiles.** A (§2) defines the cost-to-target profile
Y_d(x): p ⟼ d(p,x) and states "For finite directed distances, the entire
directed distance from x to y can be recovered from these profiles:
d(x,y)=sup_p [d(p,y)−d(p,x)]. The triangle inequality gives the upper
bound, and choosing p=x gives equality." Here the profiles, over
p = (L, U, R), are Y_d(L) = (0, 1, 2), Y_d(U) = (3, 0, 1) and
Y_d(R) = (6, 3, 0), the columns of the table, and the formula returns the
table on all nine pairs. A: "This is a concrete form of the enriched
Yoneda embedding, which is isometric for Lawvere metric spaces." The
outgoing profiles d(x, −) are the rows; [QUESTION-031](../questions.d/QUESTION-031.md) records the
isometry for the additive base.

**The same moves under peak costs (the filer's).** If each move's figure
is a peak requirement and a path costs its largest move, as in
[CLAIM-590](../claims.d/CLAIM-590.md)'s base, the table becomes:

| from | to L | to U | to R |
|---|---|---|---|
| L | 0 | 3 | 3 |
| U | 1 | 0 | 3 |
| R | 1 | 1 | 0 |

Take x and y identified at budget b when each reaches the other within b.
Under peak costs that relation is transitive at every budget: at b < 3 no
two configurations are identified and at b ≥ 3 all three are. Under
additive costs, at budgets 3 to 5 U is identified with L and with R while
L and R are 6 apart, so the relation is intransitive, and only at 6 do all
three join. That is [CLAIM-581](../claims.d/CLAIM-581.md)'s contrast between peak and additive
semantics, here with directed moves, which that claim sets aside
([CLAIM-591](../claims.d/CLAIM-591.md)): the peak case still gives nested classes, the additive
case does not.

**Checked** by the filer with python3 -I: the closure of the four moves
under addition reproduces A's table; the triangle inequality holds on all
27 triples; the recovery formula equals d on all nine pairs; the budget-2
reach sets are as above; the peak-cost closure is as above; and mutual
reachability within b is transitive at every b tested under max and
fails at b = 3 and 4 under addition.

## Observing costs, and the two frontiers

Added on 2026-11-05 from A's later reading of this pull request. Read A's
one-way costs as peak costs: the directed thresholds are U→L 1, L→U 3,
U→R 3, R→U 1, L→R 3 and R→L 1, so all three states are mutually reachable
only at acting budget 3. Give the observer two probes, of the assistant's
choosing: "flat or folded", costing 1, which separates U from L and R; and
"which side", costing 2, which separates L from R. Computed exhaustively,
the budget pairs at which everything indistinguishable is mutually
reachable are those with o ≥ 2 or a ≥ 3, and those at which everything
mutually reachable is indistinguishable are those with o < 1 or a < 3; the
partitions coincide below o = 1 with a ≥ 3 and from o = 2 with a < 3.
[CLAIM-570](../claims.d/CLAIM-570.md) states and proves the general form.

## What it can show

That one move graph, with every configuration reachable from every other,
carries a directed and graded geometry that the groupoid forgets and the
cost-to-target profiles keep in full; that the formation cost of a state
(its column) and its transformation cost (its row) differ, as A's §4
"easy to assemble but hard to change once assembled" says, here for L:
cheap to reach from U and from R, dear to leave for R; and that which
composition law the costs obey changes the distances and whether budgeted
identification sorts the states into classes.

It is A's second target result of §11 in its smallest form for states of
one mechanism: "two mechanisms with the same unrestricted reachability but
different resource-enriched Yoneda profiles" ([CASE-202](CASE-202.md)).

## What it cannot show

- **Anything about a real mechanism.** The costs are stipulated; no
  origami vertex is claimed to have them. [CASE-206](CASE-206.md) is a computed
  vertex, under a footprint.
- **That detecting a state costs what producing it costs.** A: "A
  budgeted ability to produce a state is not necessarily the same as an
  ability to detect that state." The table prices transformations only;
  no test is modelled.
- **That the three are distinct individuals.** They are states of one
  mechanism, told apart by what it costs to move between them, in
  [TERM-088](../terms.d/TERM-088.md)'s descriptive sense at most.
