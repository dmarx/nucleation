---
status: Proposed
title: 'A chain of n moves and a complete graph on the same n + 1 configurations, every configuration and every move needing one unit of peak capacity and every move spending one unit: every pair is joined at budget 1 in both, while the least cumulative cost from one end to the other is n in the chain and 1 in the complete graph'
version: 1
standing: fictional
kind: construction
tags:
- mathematics
- operations-research
date: '2026-11-12'
line:
- realizability
- formal-apparatus
illustrates:
- CLAIM-581
summary: >-
  A's construction, from the exchange "Identify Synthesis Opportunities"
  (2026-11-08, A11, A12 and A14), filed as a case at the owner's
  instruction (U5) that claims resting on explicit constructions be
  connected to cases describing them. It grounds CLAIM-tmp2u6bs: the
  peak-capacity threshold between every pair of configurations can agree
  in two systems whose least cumulative costs differ by any factor. It also
  illustrates CLAIM-581's remark that under additive costs "within budget
  of each other" is not an equivalence. The wording is A's; adopting it is
  the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmp2u6bs — Proposed; the claim this construction grounds, filed with it -->

# CASE-tmpbbfq8: A chain of n moves and a complete graph on the same n + 1 configurations, every configuration and every move needing one unit of peak capacity and every move spending one unit: every pair is joined at budget 1 in both, while the least cumulative cost from one end to the other is n in the chain and 1 in the complete graph

## The case

Two systems on configurations 0, 1, …, n. Holding any configuration
needs one unit of a capacity that must be held at each moment
(CLAIM-571's resource), and so does every move. Each move also spends
one unit of a cumulative budget (TERM-105's expenditure).

- **The chain** allows moves only between i and i + 1.
- **The complete graph** allows a move between every pair.

A's version, at A12: "Both systems permit travel between every pair of
states at peak capacity 1. But the minimum cumulative expenditure from
state 0 to state 2 differs. Generalizing to an n-edge chain versus a
complete graph makes the cost ratio n:1, with identical
peak-reachability hierarchies." (A's LaTeX delimiters around n are dropped.) A's figure has n = 2 (chain: "2 moves:
expenditure 2"; triangle: "1 move: expenditure 1").

## What it shows

- **Peak thresholds agree.** CLAIM-571's threshold, the least over paths
  of the peak along the path, is 1 for every pair in both systems, and no
  pair is joined below 1. So CLAIM-581's threshold pseudo-ultrametric is
  the same in both, and so is the hierarchy of classes it induces: one
  class at every budget from 1 up, none below.
- **Cumulative costs do not.** The least spend from 0 to n is n in the
  chain and 1 in the complete graph. The ratio grows without bound in n.
- **Additive budgets give no equivalence** (CLAIM-581). In the chain, at
  a cumulative budget of 1, 0 is within budget of 1 and 1 of 2, but 0 is
  not within budget of 2.

A said its own script passed for n = 2 to 40. The filer reran an
independent check on 2026-11-12 (Dijkstra for both costs, n = 2, 3, 10,
40, 100): every pair has threshold 1 in both systems, and the cost from 0
to n is n against 1.

## What it cannot show

- Anything about which semantics a real organization's resource has;
  TERM-105 keeps the types apart, and the case is fictional.
- That the two systems are otherwise alike. Their move sets differ; what
  they share is every peak threshold, which is the point.

## Provenance

A drafted it as evidence for a claim it numbered 634 and a case it
numbered 233, in a bundle never committed. The claim's number now names
a different claim on the record.
