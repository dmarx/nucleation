---
status: Proposed
title: 'Two forms of support that give a party the same capabilities now can leave it different capabilities later: where capacity is learned by doing and decays with disuse, support that does the work shrinks what the party can reach unaided while support that covers only its shortfall does not, so support, or a technology, cannot be ranked by present capability sets and has to be assessed by the capability trajectory it produces'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation: in CLAIM-605's model (dC/dt = λPC(1 − C) −
  μC, λ = 1, μ = 0.3, τ = 1.5), a party at C = 0.7 under full substitutive
  support and under capacity-first support does not have the same
  delivered functioning and the same unaided capability at t = 0, or does
  not have different unaided capability at t = 5 (C = 0.156 against 0.7)
  and after withdrawal (0 against 0.7). Or an argument that the capability
  approach's capability set already includes the person's later sets, so
  that evaluating it at a time is not evaluating it as a snapshot. Not
  defeated by evidence that a given technology does not deskill its
  users, which bears on whether the model applies (CASE-tmpf71w4), not on
  the derivation.
tags:
- society-and-governance
- well-being
- complex-systems
date: '2026-11-13'
line:
- transient-support
- will-organization
rests_on:
- CLAIM-605
- CLAIM-352
bears_on:
- QUESTION-398
summary: >-
  A's, from the exchange "Analyze technological civilization trap"
  (2026-11-13): A17 §V ("A technology can increase what someone
  accomplishes today while reducing what they will be capable of
  accomplishing tomorrow"; "We should investigate how particular forms of
  assistance change the person's future capability trajectory") and A23
  §6 ("We therefore need to evaluate capability trajectories, not merely
  present capability sets"), joining [CLAIM-605](CLAIM-605.md)'s capability trap to Sen's
  capability approach as [CLAIM-352](CLAIM-352.md) reads it. The record holds the
  dynamics ([CLAIM-605](CLAIM-605.md)) and the reading of Sen ([CLAIM-352](CLAIM-352.md)), not the
  consequence for evaluating support. The derivation is checked here in
  [CLAIM-605](CLAIM-605.md)'s own model. The model is illustrative; A17 itself says it is
  "not empirical evidence that a particular technology produces such
  decline", and the proposed study is [CASE-tmpf71w4](../cases.d/CASE-tmpf71w4.md). The wording is A's;
  adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-603 — Proposed; the record's claim on division of labour, cited with its standing -->
<!-- inactive-ok-file: CASE-tmpf71w4 — filed from the same exchange, Proposed -->

# Two forms of support that give a party the same capabilities now can leave it different capabilities later: where capacity is learned by doing and decays with disuse, support that does the work shrinks what the party can reach unaided while support that covers only its shortfall does not, so support, or a technology, cannot be ranked by present capability sets and has to be assessed by the capability trajectory it produces

## The claim

A17 §V, reading [CLAIM-605](CLAIM-605.md) against A's earlier use of Sen:

> **A technology can increase what someone accomplishes today while
> reducing what they will be capable of accomplishing tomorrow.**
>
> The capability set is dynamic.
>
> This deepens Sen's approach.

A23 §6 put it as a rule of evaluation: "We therefore need to evaluate
**capability trajectories**, not merely present capability sets."

## The derivation

Take [CLAIM-605](CLAIM-605.md)'s model as it stands: demand 1, the party's output τC,
dC/dt = λPC(1 − C) − μC, with λ = 1, μ = 0.3, τ = 1.5. Start a party at
its kept state, C = 0.7, where its unaided output is min(1.05, 1) = 1.

- **Under full substitutive support** (the support does all the work, P =
  0), the demand is met in full, by the support.
- **Under capacity-first support** (P = min(τC, 1)), the demand is met in
  full, by the party, and the support supplies nothing.

At t = 0 the two are the same in every respect a capability set records:
the same functioning delivered (the demand met), and the same set of
functionings the party could reach unaided (C = 0.7). By t = 5 they are
not. Under substitution C = 0.7e^(−1.5) = 0.156, below [CLAIM-605](CLAIM-605.md)'s
threshold of 0.276, with unaided output 0.23; under capacity-first support
C stays 0.7. Withdraw both supports at t = 5 and let sixty units pass:
the first party's capacity goes to 0, the second's stays at 0.7
(recomputed for this filing by Euler integration in `python3 -I`).

So an evaluation that compares the two supports by the capability sets
they leave at the moment of comparison cannot tell them apart at t = 0,
though one of them removes a capability the party has and the other
keeps it. [CLAIM-352](CLAIM-352.md) reads Sen's opportunity aspect as viable reachability
mapped to valued functionings; the reachable set itself moves under the
support, so the opportunity aspect has to be read along the trajectory.

## What it does not say

- Not that any actual technology deskills its users. The model is
  [CLAIM-605](CLAIM-605.md)'s toy, and A17 §IX says so: "the fact that assistance can
  diminish capacity in a particular dynamical model does not establish
  that AI assistance generally diminishes human competence." Whether
  capacity in a real skill is learned by doing, decays with disuse and
  needs capacity present to grow is the question [CASE-tmpf71w4](../cases.d/CASE-tmpf71w4.md) would test.
- Not that substitution is wrong. A17: "Automating dangerous or exhausting
  work may be overwhelmingly beneficial", and [CLAIM-603](CLAIM-603.md) holds that a
  capability given up for reliable supply can be a division of labour.
  The claim is about what an evaluation must look at, not its verdict.
- Not that Sen ignores time. Whether his framework already evaluates
  capability over a life is a question for a reading of Sen's own works
  (registered unread from this exchange), not settled here.
