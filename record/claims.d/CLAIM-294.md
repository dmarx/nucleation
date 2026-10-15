---
number: 294
status: Active
formerly:
- CLAIM-tmp2rwpl
title: Two inquiry histories can agree on every current conclusion and still call
  for different revisions of it, so a current marginal belief is not a sufficient
  state for updating on evidence about what it depended on
version: 1
role: thesis
warrant: demonstrated
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
- QUESTION-105
grounds:
- CASE-093
- THEORY-347
- THEORY-353
summary: >-
  A5's central claim, made exact by A8's construction ([CASE-093](../cases.d/CASE-093.md)) and checked
  here. Two joint distributions over a hypothesis H and a condition C share P(H)
  = 0.9; learning C = 1 sends one to 1.0 and the other to 0.8. Keeping only the
  marginal merges histories that need different updates. It does not say a full
  posterior falls short ([CLAIM-300](CLAIM-300.md)), or that a dependency graph is the fix
  ([CLAIM-293](CLAIM-293.md)).
supports:
- CLAIM-295
---
<!-- inactive-ok-file: CLAIM-295 — Proposed; open claims and accounts cited as open, nothing here rests on their being settled -->

# CLAIM-294: Two inquiry histories can agree on every current conclusion and still call for different revisions of it, so a current marginal belief is not a sufficient state for updating on evidence about what it depended on

## The claim

A5: "the information required for future epistemic revision may differ
from the information required to reconstruct present conclusions". A8
turned the intuition into a construction ([CASE-093](../cases.d/CASE-093.md)). With H, C binary and
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
revision competence this way, is [CLAIM-295](CLAIM-295.md) and stays Proposed.

## What it does not say

- Not that a current state can never suffice. A5's qualification: "A
  complete Bayesian posterior over all relevant latent variables can be
  sufficient for subsequent updating." [CLAIM-300](CLAIM-300.md) and [CASE-082](../cases.d/CASE-082.md) hold that half.
- Not that keeping justifications is the remedy. Keeping the joint over
  (H, C) is enough here, with no history at all.
- Not that a counterexample to one representation is evidence for
  another. A18: "Showing that a conclusion-only summary fails on a
  revision task does not establish that a justification graph
  succeeds."

## The same point in belief-revision logic (note of 2026-10-15)

Two readings filed the same day give the full-belief form of this claim.
Hansson's survey ([LIT-1072](../literature.d/LIT-1072.md), read in [NOTE-866](../notes.d/NOTE-866.md)): bases {p, q} and
{p, p ↔ q} have the same closure, yet after revision by ¬p one agent
believes q and the other ¬q. The bases are "statically equivalent" and not
"dynamically equivalent". In AGM ([LIT-1050](../literature.d/LIT-1050.md), read in [NOTE-874](../notes.d/NOTE-874.md)) the
closed theory alone does not determine a revision; a selection function
over its remainders must be added. Both match this claim's caveat: a
richer current state, a base or an ordering, suffices for one revision.
Neither is a record of what a belief depended on, so neither supports
reading this claim as an argument for keeping justifications ([CLAIM-295](CLAIM-295.md)'s
question, not this one's).
