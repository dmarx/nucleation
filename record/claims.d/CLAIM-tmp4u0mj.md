---
status: Proposed
title: "The questions an organization can both pose and answer by a deadline lie between an inner bound, those whose posing and answering fit the horizon and budget run one after the other, and an outer bound, those each of whose processes fits alone, and where between them depends on precedence and sharing that neither frontier records, so two organizations with the same query and answer frontiers can differ in what they can jointly do"
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  A joint schedule for a question that does not, restricted to one
  process, give a schedule for that process alone within the same horizon
  and budget (breaking the outer bound); or a recomputation of the
  two-organization example in which their separate frontiers differ or
  their joint sets agree.
tags:
- operations-research
- epistemology
date: '2026-11-23'
line:
- learning-and-inquiry
- readiness
- formal-apparatus
bears_on:
- QUESTION-tmp3cft4
rests_on:
- CLAIM-tmpiwxla
- CLAIM-tmpdvgrf
- CLAIM-tmpq4crr
complements:
- CLAIM-tmpj15c6
uses:
- TERM-092
summary: >-
  A gap in A52 §7 and A54 §7 of the exchange "Explain First Contact RL"
  (ChatGPT, 2026-11-23), filled. A52 closes on "whether we can derive a
  joint inquiry–response feasibility or viability boundary that cannot be
  recovered by independently calculating the query frontier and the answer
  frontier"; A54 §7 asserts it "is not determined by the query frontier and
  answer frontier taken separately", with two examples and no
  construction. Here: the bounds the separate frontiers do give, and a
  checked pair of organizations that they cannot tell apart. The wording is
  the assistant's (Claude, in this session); adopting it is the owner's
  call.
---
<!-- inactive-ok-file: CLAIM-tmpiwxla CLAIM-tmpq4crr CLAIM-tmp1m3ba TERM-tmpz28l1 CLAIM-tmpj15c6 CLAIM-tmpx0wv9 TERM-tmpace0k TERM-tmpdk711 — Proposed; the construction this rests on, A's claim, the owner's conjecture, the viability kernel, and the joint relation and terms filed beside it -->

# CLAIM-tmp4u0mj: The questions an organization can both pose and answer by a deadline lie between an inner bound, those whose posing and answering fit the horizon and budget run one after the other, and an outer bound, those each of whose processes fits alone, and where between them depends on precedence and sharing that neither frontier records, so two organizations with the same query and answer frontiers can differ in what they can jointly do

## The gap

A54 §7 defines the joint frontier 𝒥(S; H, B) as the questions q for which
there is an admissible joint schedule σ that formulates and investigates q,
produces an adequate response by H and respects shared capacities B, and
says "This is not determined by the query frontier and answer frontier
taken separately." Its reasons are two examples: two activities "affordable
in isolation but infeasible together because they require the same scarce
expert", and two inquiries that "share expensive preliminary work". A52
had asked whether such a boundary "cannot be recovered" from the two
frontiers. Neither turn shows what the frontiers do determine.

## The construction

Let F_Q(H, B) be the questions whose posing fits horizon H and budget B
with the answer left aside, the query frontier (for posing alone, TERM-092's
inquiry frontier), and F_A(H, B) the questions whose adequate answer can be
produced within H and B once the question is posed, the answer frontier.
Costs are nonnegative and a schedule's use of time and resources is
monotone in what it schedules.

- **Outer bound.** 𝒥(H, B) ⊆ F_Q(H, B) ∩ F_A(H, B). A joint schedule
  restricted to the posing is a schedule for posing alone, finishing by H
  and using no more than B, and likewise for the answer.
- **Inner bound.** Where running the two one after the other is admissible
  and the resources are pooled, every q with T_Q(q) + T_A(q) ≤ H and
  C_Q(q) + C_A(q) ⪯ B is in 𝒥(H, B): the sequential schedule meets both.
  Here T_Q, T_A, C_Q and C_A are the times and costs of one way of posing q
  and of answering q as so posed. Read off the frontiers, the bound takes
  the least time and cost of posing and the least of answering, and those
  may belong to different ways of posing. Then the bound holds only when
  the cost of answering does not depend on how the question was posed.
  Where it does, a question inside the bound computed from the frontiers
  can be jointly out of reach: in CLAIM-tmpj15c6's construction 4 the least
  costs sum to 5 and the true joint cost is 9. The outer bound needs no such
  condition, since a joint schedule's parts cost at least the least costs.
- **Between them,** membership depends on what neither frontier records:
  whether the answer can start on a partial specification, whether the two
  draw on the same server or pool, and, for sets of questions, whether they
  share preliminary work. That is CLAIM-tmpiwxla's route structure and
  CLAIM-tmpq4crr's three couplings, and for demands with deadlines it is
  CLAIM-tmpdvgrf's point that a change of response architecture can enlarge
  what is jointly feasible without weakening any demand.

## The check

With python3 -I, H = 4, posing and answering each 3 days. In every
organization below, posing alone fits (3 ≤ 4) and answering alone fits
(3 ≤ 4), so the separate frontiers are the same.

- X, separate experts, the answer able to start after one day of
  specification: joint finish max(3, 1 + 3) = 4, feasible.
- Y, separate experts, the answer waiting for the finished question:
  3 + 3 = 6, infeasible.
- Z, one expert doing both: 6, infeasible.

So 𝒥 is not a function of (F_Q, F_A). A54's sharing example runs the
other way for sets of questions: two inquiries each costing 3 that share 2
of preliminary work cost 4 together, not 6, so the joint set of questions
is not the product of the single ones either, and it is a downward-closed
complex as in CLAIM-tmpdvgrf.

## What it does not say

- Not more than CLAIM-tmpj15c6, filed beside it from A58 §2: that the
  frontiers at every budget do fix the joint pairs once the rule by which
  formulating and answering compose is declared, so that what is left over
  is the rule. The two agree: the organizations X, Y and Z above have the
  same frontiers at every horizon and differ only in that rule. This claim
  adds the bounds that hold whatever the rule is, the inner one only where
  posing a question does not change what answering it costs (the
  qualification above, from CLAIM-tmpj15c6's construction 4).
- Not which object the record should call the inquiry frontier. Whether
  TERM-092 should become the joint object or stay the query frontier beside
  a new term is the owner's choice, filed from U30 and A58.
- Not the viability question A52 §7 asks, whether an organization can keep
  "a sufficiently rich joint inquiry–response frontier" as its resources
  and questions evolve. That is TERM-tmpz28l1's viability kernel with the
  joint set in place of reorganization routes, and "rich" is undefined.
- Not the owner's point about parallelism (CLAIM-tmp1m3ba) beyond the
  route structure: maintained perspectives change the state S, and so the
  activation times, which this static construction takes as given.

## Note of 2026-11-23: against A58's joint relation and the two terms

Filed in the same batch from A58 (U30): CLAIM-tmpx0wv9 and the two
alternatives for TERM-092, TERM-tmpace0k and TERM-tmpdk711. This claim's
𝒥(H, B) is the question projection of CLAIM-tmpx0wv9's relation 𝓕_S(H, B),
its "resolved questions", which is TERM-tmpdk711's question side. Its F_A is
the conditional answer frontier (the question supplied, the answer charged),
not the joint answer frontier that both terms derive from 𝓕. Its F_Q is
TERM-092's askable set as the term now stands; under alternative (a),
TERM-tmpace0k, that set would be named the query frontier and "inquiry
frontier" would name 𝓕. The bounds hold under either name. They give what
CLAIM-tmpx0wv9's third site of failure, joint realizability, can and cannot
be read from: a question outside the outer bound fails at the first or
second site, and one between the bounds fails, if at all, at the third. The
note is the assistant's (Claude, in this session); adopting it is the
owner's call.
