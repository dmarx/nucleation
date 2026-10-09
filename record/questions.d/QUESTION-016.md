---
number: 16
status: Open
formerly:
- QUESTION-tmpk199j
title: 'Under what conditions does iterated reconstruction preserve, or progressively destroy, task-relative sufficiency?'
version: 1
tags:
- information-theory
- philosophy-of-language
date: '2026-10-08'
line: pragmatic-transport
refines:
- QUESTION-002
summary: >-
  A86 §10, the second of three "target results". Neither it nor the
  other two was proved or stated in C6 or the manuscript, which has the
  data-processing inequality for a fixed Markov chain and a drift bound,
  not a sufficiency result.
refined_by:
- QUESTION-010
---
<!-- inactive-ok-file: CLAIM-050 CLAIM-056 — Proposed; open, and cited as open: the claim, argument or reading is under test, not settled -->

# QUESTION-016: Under what conditions does iterated reconstruction preserve, or progressively destroy, task-relative sufficiency?

## Why it is a question

A86 §10 named three results the theory should aim at: (a) compression that
preserves a chosen family of decision problems; (b) when iterated
reconstruction preserves or destroys sufficiency; (c) how much decoder
adaptation compensates for lower rate ([QUESTION-020](QUESTION-020.md)). This is (b).

## Where it stands

The manuscript §8 has I(Z;U_(n+1)) ≤ I(Z;U_n) for a fixed Markov chain, with the
caveat that added evidence changes the graph, and a bound on distributional
error ([CLAIM-056](../claims.d/CLAIM-056.md)). Neither says when a chain keeps the Blackwell sufficiency for a
family Q of communicative decisions ([CLAIM-050](../claims.d/CLAIM-050.md)). A garbling of a garbling is a
garbling, so sufficiency for Q can only decline along a pure chain. The open
part is the case the manuscript flags, interpreters with side information, where
a retelling "can then improve an audience's task performance" (A86 §3).
