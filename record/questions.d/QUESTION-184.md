---
number: 184
status: Open
formerly:
- QUESTION-tmpd26fs
title: "Do real groups whose members update by averaging reach a settled estimate that moves away from the truth as the largest influence weight grows, as DeGroot's model predicts?"
version: 1
tags:
- network-science
- social-science
- epistemology
date: '2026-10-19'
line: 'distributed-agency'
refines:
- QUESTION-047
summary: >-
  Filed when the promotion audit (batch 036, [ADR-047](../decisions.d/ADR-047.md) v2) narrowed and
  promoted [THEORY-321](../theory.d/THEORY-321.md) to the theorem within DeGroot's model for a strongly
  connected society. The former promote_when asked for a case outside the
  model; this question holds it, together with a check of the theorem for
  societies with several closed groups.
---
<!-- inactive-ok-file: CLAIM-914 CASE-340 — Proposed; filed 2026-11-22 by LEAD-061, cited in its dated note -->

# QUESTION-184: Do real groups whose members update by averaging reach a settled estimate that moves away from the truth as the largest influence weight grows, as DeGroot's model predicts?

## Why it is a question

[THEORY-321](../theory.d/THEORY-321.md) now states Golub and Jackson's characterization ([LIT-999](../literature.d/LIT-999.md)) as a
theorem about repeated DeGroot averaging in a strongly connected society:
the consensus converges to the truth as the society grows if and only if
the largest influence weight vanishes. The mathematics is proved and was
re-derived. What is open is whether real communities update closely
enough to DeGroot for the condition to decide their beliefs. The model's
members are naïve: they do not discount repeated information, signals are
independent, and weights are fixed ([NOTE-840](../notes.d/NOTE-840.md)).

A second, narrower matter is held here too. [NOTE-840](../notes.d/NOTE-840.md) records Proposition 2
for any convergent weight matrix, with several closed groups allowed. The
audit's sketch suggests a vanishing largest weight may not then suffice:
many small closed groups, each of growing size, can each settle on its own
average, and the chance that some of them misses the truth need not
vanish. Whether the paper's definitions exclude this was not checked
against the source.

## What would answer it

A laboratory network experiment or field data in which the updating rule
is held fixed, the influence structure is changed, and the group's
settled estimate moves away from the truth as the largest influence weight
grows would answer it yes. Such an experiment in which accuracy does not
track maximal influence would answer it no. Further simulations of the
DeGroot model do not settle it: they only restate the theorem. For the
narrower matter, reading Golub and Jackson's Proposition 2 and Theorem 3
with their definitions of influence and wisdom for several closed groups
settles it.

## Note of 2026-11-22: the narrower matter, settled

[LEAD-061](../leads.d/LEAD-061.md) reread Golub and Jackson's Proposition 2 and Theorem 3 with
their definitions. The definitions do not exclude the audit's sketch:
influence sums to 1 on each minimal closed group (Theorem 3) and wisdom
is the convergence of the maximum deviation over all agents
(Definition 3). With ⌊n/k⌋ closed groups of k = ⌈√(ln n)⌉ and
Bernoulli(1/2) signals, s_1 → 0 and the probability that some group's
consensus misses by 1/2 tends to 1 ([CASE-340](../cases.d/CASE-340.md)). So a vanishing
largest weight does not suffice with many closed groups; it is still
necessary, and it suffices when s_1·log m → 0, m the number of closed
groups, in particular when m is bounded ([CLAIM-914](../claims.d/CLAIM-914.md), offered as the
answer to this half). The main question, about real groups, is open.
