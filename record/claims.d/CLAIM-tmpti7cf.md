---
status: Proposed
title: 'Resource composition fixes the modal logic of reach'
statement: >-
  Reading "reachable within budget b" as a modal accessibility relation
  R_b, the logic it validates is fixed by how the resource composes and by
  whether moves reverse: under peak costs with reversible moves and free
  holding, R_b is an equivalence relation at every budget and validates S5;
  with one-way moves it is a preorder and validates S4; where holding a
  configuration itself costs, R_b is reflexive only at configurations
  affordable to hold, S5 there and only KB4 on the whole space; under
  cumulative costs R_b is not transitive at any finite positive budget, so
  the 4 axiom fails, while possibility within b of possibility within c
  gives possibility within b + c, against within max(b, c) under peak costs
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation below: a reversible move graph with peak
  costs and free holding on which reachability within some b is not an
  equivalence relation; a one-way graph with peak costs on which it is not
  reflexive and transitive; a graph with holding costs on which it fails to
  be symmetric and transitive; or a graph with additive costs on which
  possibility within b of possibility within c fails to give possibility
  within b + c. Several resources at once, replenishable reserves and
  deadlines are outside the stated conditions and do not defeat it.
tags:
- logic
- mathematics
- operations-research
date: '2026-11-26'
line:
- realizability
- formal-apparatus
rests_on:
- CLAIM-563
- CLAIM-581
- CLAIM-571
- CLAIM-591
bears_on:
- QUESTION-tmpahfz9
summary: >-
  A gap fill ([ADR-137](../decisions.d/ADR-137.md)) for A19 §5 of the exchange "Alignment consequences
  brainstorm" (ChatGPT, 2026-11-26), which proposes reading [CLAIM-563](CLAIM-563.md) and
  [CLAIM-581](CLAIM-581.md) as modal results: "In the peak-capacity case, with admissible
  holding and no additional deadline, accessibility at a fixed budget can
  form a reflexive, transitive relation. Its modal semantics then validate
  S4. If accessibility is also symmetric on the affordable state space, it
  validates S5." A19 is right, and the derivation below sorts its cases:
  under [CLAIM-581](CLAIM-581.md)'s own premise, reversible moves, the relation is already
  symmetric, so the record's ultrametric case is S5, not S4; S4 is the
  one-way case of [CLAIM-591](CLAIM-591.md); and A19's "admissible holding" is the
  condition that holding costs, [CLAIM-571](CLAIM-571.md)'s r(x), stay within the budget,
  without which reflexivity fails. Checked with python3 -I on 2,000 random
  graphs. The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-646 CLAIM-tmpi0rdz LIT-tmpdtmk7 LIT-tmpyehic — Deferred, Proposed; filed, registered or cited in the filing of 2026-11-26 from the exchange "Alignment consequences brainstorm" -->

# CLAIM-tmpti7cf: Resource composition fixes the modal logic of reach

## The gap

A19 §5, answering the owner's U11 ([QUESTION-tmpahfz9](../questions.d/QUESTION-tmpahfz9.md)), introduces "a
family" of relations R_b = {(x, y) : d(x, y) ≤ b} and reads x ⊨ ◇_b φ to mean
that φ "is realizable from configuration x within resource budget b". It
asks whether ◇_b◇_b φ → ◇_b φ holds and answers "It depends on how
resources compose": under peak capacity "Transitivity holds", under
cumulative expenditure "Transitivity fails". It then states the S4 and S5
cases quoted in the summary, and the composition laws ◇_b◇_c φ →
◇_{b+c} φ (cumulative) and ◇_b◇_c φ → ◇_{max(b,c)} φ (peak), calling them
"proposed modal restatements of existing compositional results, under the
corresponding assumptions about paths and costs". It does not say which
assumptions give which logic, and the record's ultrametric result is
stated for reversible moves, which settles the symmetric case.

## The derivation

Let d be the least, over admissible paths, of the path's cost, and
R_b = {(x, y) : d(x, y) ≤ b} (on a finite move graph the least is
attained, as [CLAIM-581](CLAIM-581.md) step 2 notes). The standard correspondences are:
axiom T (□φ → φ) with reflexivity, 4 (◇◇φ → ◇φ) with transitivity, B
(φ → □◇φ) with symmetry; S4 is T + 4, S5 is T + 4 + B.

1. **Peak costs, reversible moves, free holding.** d(x, x) = 0, d is
   symmetric, and d(x, z) ≤ max(d(x, y), d(y, z)) ([CLAIM-581](CLAIM-581.md) step 1). So
   R_b is reflexive, symmetric and transitive at every b: an equivalence
   relation, whose frames validate S5. This is [CLAIM-581](CLAIM-581.md)'s "equivalence
   relation at every budget" read modally, and [CLAIM-563](CLAIM-563.md)'s closure at
   every budget under max.
2. **Peak costs, one-way moves.** The concatenation step still gives the
   strong triangle inequality for directed paths, and d(x, x) = 0, but d
   need not be symmetric ([CLAIM-591](CLAIM-591.md)). R_b is a preorder: S4. This is the
   case A19's first sentence describes.
3. **Holding costs.** If, as in A19 §2's formula d_peak(x, y) =
   inf over paths of sup_{z∈γ} r(z), the path's cost includes the
   requirement r of the configurations it passes through, endpoints
   included, then d(x, x) = r(x): staying at x costs what holding x costs
   ([CLAIM-571](CLAIM-571.md)'s holding requirement, kept apart in [CLAIM-581](CLAIM-581.md)'s "Identity
   is free; holding is not"). R_b is then reflexive exactly on the
   affordable set X_b = {x : r(x) ≤ b}. On X_b it is an equivalence (S5
   with reversible moves); on the whole space it is symmetric and
   transitive but not reflexive, the logic KB4, in which □φ → φ fails at
   the configurations the budget cannot hold. That is A19's "admissible
   holding".
4. **Cumulative costs.** d is an extended (quasi-)pseudometric, so R_b is
   reflexive, and symmetric for reversible moves, but not transitive at a
   finite positive b once there are two composable moves each costing
   more than b/2 ([CLAIM-563](CLAIM-563.md) step 4; [CLAIM-581](CLAIM-581.md) step 4's 0.6 + 0.6). Axiom 4
   fails. The triangle inequality gives the graded law: if d(x, y) ≤ b and
   d(y, z) ≤ c then d(x, z) ≤ b + c, so ◇_b◇_c φ → ◇_{b+c} φ.
5. **Peak composition across budgets.** If d(x, y) ≤ b and d(y, z) ≤ c then
   d(x, z) ≤ max(b, c), directed or not, so ◇_b◇_c φ → ◇_{max(b,c)} φ.
   With b = c this is axiom 4 at one budget.

**Check (python3 -I).** On 2,000 random six-configuration graphs with
move costs uniform on [0, 10] and budgets 3, 5 or 7, the relation R_b
was reflexive, symmetric and transitive in all 2,000 under reversible peak
costs; reflexive and transitive in all 2,000 and symmetric in 120 under
one-way peak costs; with holding costs uniform on [0, 6], symmetric and
transitive in all 2,000 and reflexive on the whole space in 917, on the
affordable set in all 2,000; under reversible additive costs, transitive
in 1,006. Across all triples and budget pairs (2, 5), (4, 4) and (6, 3)
on the one-way graphs, no failure of the max law under peak costs and
none of the sum law under additive costs.

## What follows

- **The modal language adds a vocabulary, not a result.** Each case is a
  restatement of [CLAIM-563](CLAIM-563.md), [CLAIM-581](CLAIM-581.md) and [CLAIM-591](CLAIM-591.md). What it adds is that
  the record's resource semantics and its modal semantics are the same
  choice: [TERM-105](../terms.d/TERM-105.md)'s distinction between peak capacity and cumulative
  expenditure, which [CLAIM-581](CLAIM-581.md) showed decides whether configurations fall
  into nested kinds, also decides whether "possibly possible within b" is
  "possible within b".
- **Graded families are needed under sum.** Under cumulative costs no
  single budget's operator is closed; the logic must carry the budget as
  an index that adds, [CLAIM-563](CLAIM-563.md)'s grade, which is what resource-bounded
  ATL does ([LIT-tmpdtmk7](../literature.d/LIT-tmpdtmk7.md), unread).
- **Entrenchment is constrained.** In an S5 frame what can be made to hold
  necessarily already holds necessarily, so a
  reversible peak budget cannot express lock-in at one budget;
  [CLAIM-tmpi0rdz](CLAIM-tmpi0rdz.md) works this out for A23's modal table.

## What it does not say

- That the modal reading is the right geometry of possibility. A19 says
  so itself: "ordinary modal logic cannot recover every geometric
  property of a space". Two move graphs with the same budget-indexed
  equivalence classes have the same S5 frames at every b and may differ in
  cumulative cost by any factor ([CLAIM-646](CLAIM-646.md)).
- Anything about several resources at once, deadlines, or replenishable
  reserves, which have no such composition law ([CLAIM-563](CLAIM-563.md), "What it does
  not say").
- That the topological reading of S4 ([LIT-tmpyehic](../literature.d/LIT-tmpyehic.md)) is about reachability:
  closure in a topology is nearness, not a path within a budget, as A19 §10
  cautions.
