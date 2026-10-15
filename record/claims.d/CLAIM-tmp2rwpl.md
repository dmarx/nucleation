---
status: Active
title: Two inquiry histories can agree on every current conclusion and still call
  for different revisions of it, so a current marginal belief is not a sufficient
  state for updating on evidence about what it depended on
version: 1
role: thesis
defeated_if: >-
  An error in the construction: two distributions with the stated conditionals whose
  marginals for H differ, or whose updates on C = 1 coincide. Nothing empirical
  bears on it.
tags:
- epistemology
- probabilistic-modeling
date: '2026-10-15'
line:
- nucleating-argument
- formal-apparatus
answers:
- QUESTION-tmpga1fv
grounds:
- CASE-tmpziral
summary: >-
  A5's central claim, made exact by A8's construction ([CASE-tmpziral](../cases.d/CASE-tmpziral.md)) and checked
  here. Two joint distributions over a hypothesis H and a condition C share P(H)
  = 0.9; learning C = 1 sends one to 1.0 and the other to 0.8. Keeping only the
  marginal merges histories that need different updates. It does not say a full
  posterior falls short ([CLAIM-tmpp7a8x](CLAIM-tmpp7a8x.md)), or that a dependency graph is the fix
  ([CLAIM-tmp2deky](CLAIM-tmp2deky.md)).
supports:
- CLAIM-tmp7t44x
---
<!-- inactive-ok-file: CLAIM-tmp7t44x — Proposed; open claims and accounts cited as open, nothing here rests on their being settled -->

# CLAIM-tmp2rwpl: Two inquiry histories can agree on every current conclusion and still call for different revisions of it, so a current marginal belief is not a sufficient state for updating on evidence about what it depended on

## The claim

A5: "the information required for future epistemic revision may differ
from the information required to reconstruct present conclusions". A8
turned the intuition into a construction ([CASE-tmpziral](../cases.d/CASE-tmpziral.md)). With H, C binary and
P(C = 1) = 0.5 in both histories:

| | history A | history B |
|---|---|---|
| P(H = 1 \| C = 1) | 1.0 | 0.8 |
| P(H = 1 \| C = 0) | 0.8 | 1.0 |
| P(H = 1) | 0.9 | 0.9 |

Both marginals are 0.5·1.0 + 0.5·0.8 = 0.9. On learning C = 1, history A
goes to 1.0 and history B to 0.8. A memory that keeps P(H) maps both
histories to the same state and cannot make both updates. That is a
proof by counterexample of the non-implication, and the arithmetic was
checked for this entry.

## Why it is Active

It is an existence result, true by construction ([ADR-040](../decisions.d/ADR-040.md)
puts it in `formal-apparatus` as a second line). A8 drew the line where
this entry does: "The construction proves that preserving the current
marginal belief about H does not generally preserve everything required
for subsequent Bayesian updating. ... The broader hypothesis about real
research-agent memory should remain Proposed." The thesis the
nucleating-argument line cares about, that some inquiries in fact lose
revision competence this way, is [CLAIM-tmp7t44x](CLAIM-tmp7t44x.md) and stays Proposed.

## What it does not say

- Not that a current state can never suffice. A5's qualification: "A
  complete Bayesian posterior over all relevant latent variables can be
  sufficient for subsequent updating." [CLAIM-tmpp7a8x](CLAIM-tmpp7a8x.md) and [CASE-tmp390tl](../cases.d/CASE-tmp390tl.md) hold that half.
- Not that keeping justifications is the remedy. Keeping the joint over
  (H, C) is enough here, with no history at all.
- Not that a counterexample to one representation is evidence for
  another. A18: "Showing that a conclusion-only summary fails on a
  revision task does not establish that a justification graph
  succeeds."
