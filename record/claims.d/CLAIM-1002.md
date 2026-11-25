---
number: 1002
status: Proposed
formerly:
- CLAIM-tmp104zk
title: 'Parallel perspectives raise the chance that some route answers a question only insofar as their failures are independent, so keeping several is valuable for the distinct, causally consequential routes to answers they supply and not for their number, and making every perspective conform to the dominant interpretation before it is resourced correlates their answers and spends that value'
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  A case in which perspectives whose failures are perfectly correlated
  still raise the chance that some route answers, beyond the best of them
  alone; or a showing that a conformity requirement on resourcing leaves
  the correlation of their answers unchanged.
tags:
- epistemology
- social-science
- probabilistic-modeling
date: '2026-11-23'
line:
- learning-and-inquiry
- distributed-agency
rests_on:
- CLAIM-1148
- CLAIM-416
bears_on:
- QUESTION-520
complements:
- CLAIM-1038
summary: >-
  A54 §5 of the exchange "Explain First Contact RL" (ChatGPT, 2026-11-23):
  with several maintained perspectives the organization holds "a portfolio
  of partial answers". Its formula assumes independence and A54 says so;
  the assistant's check gives the value of a second route as the
  correlation between the routes rises. A54 cites [THEORY-148](../theory.d/THEORY-148.md) (Zollman,
  Proposed) for the limit: diversity of pursuit that persists too long
  prevents convergence. The wording is A's (ChatGPT, at A54 of the exchange
  "Explain First Contact RL"); adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-148 CLAIM-1195 CLAIM-1038 CLAIM-1042 — Proposed; the claim this develops, the gap fill, the reading A cites and the thesis that uses this -->

# CLAIM-1002: Parallel perspectives raise the chance that some route answers a question only insofar as their failures are independent, so keeping several is valuable for the distinct, causally consequential routes to answers they supply and not for their number, and making every perspective conform to the dominant interpretation before it is resourced correlates their answers and spends that value

## The claim

A54 §5: each maintained perspective has its own response profile
R_i(q; H, B_i), and "For a query that can be successfully answered by any
one of several independent approaches, the chance of at least one
successful answer is"

P(success | q) = 1 − ∏_i (1 − p_i(q)).

"This expression assumes conditional independence of the approaches'
success events. Correlated failures can substantially reduce the benefit
of parallelism." Two independent approaches at 0.6 each give 0.84, "But if
both rely on the same erroneous assumption, their failures may be almost
perfectly correlated."

"So preserving multiple perspectives is not intrinsically valuable because
it increases their count. It matters because they may supply **distinct,
causally consequential routes to answers**." And: "If every perspective
must conform to the currently dominant interpretation before receiving
resources, their eventual answers may become highly correlated."

The limit, from [THEORY-148](../theory.d/THEORY-148.md): preserving alternative lines "can protect
against misleading early evidence, but excessive persistence of
disagreement can prevent useful convergence". "The ideal is not permanent
fragmentation."

## The check

The assistant's, with python3 -I. For two routes each succeeding with
probability p = 0.6 and correlation ρ between their success indicators,
P(both fail) = q² + ρpq with q = 0.4, so P(some route succeeds) =
1 − 0.16 − 0.24ρ: 0.84, 0.78, 0.72 and 0.60 at ρ = 0, 0.25, 0.5 and 1. At
ρ = 1 the second route adds nothing. A54's figure checks.

## Where the record holds parts of it

- [CLAIM-416](CLAIM-416.md): competing perspectives "compete over the tests that measure
  them as well as under them", and a fair test need not be neutral across
  competences. A conformity requirement on resourcing is such a test, and
  this claim adds what it costs: correlated routes.
- [THEORY-148](../theory.d/THEORY-148.md) holds the value of transient diversity of pursuit for a group
  learning by trying; this claim moves it from beliefs about which option
  is best to routes for answering a question under a deadline.

## What it does not say

- Not that more perspectives are always better. With coordination and
  maintenance costs ([CLAIM-1195](CLAIM-1195.md)), a route whose success is highly
  correlated with those already held can cost more than it adds.

## Note of 2026-11-23: two senses of "distinct"

[CLAIM-1038](CLAIM-1038.md), filed from A60 in the same batch, says at the scale of an
ecosystem what this claim says for one question: richness tracks diversity
of consequential capabilities, not the number of constituents. The two use
"distinct" differently. Here a route adds value insofar as its failures are
independent of the others', and that holds of two copies of one method
whose failures are independent, which is redundancy (0.84 against 0.6 in
the check above). [CLAIM-1038](CLAIM-1038.md) counts a constituent for differing in
what it can answer. A54's warning against conformity before resourcing
joins them: making perspectives conform both correlates their failures and
removes their differences. In [CLAIM-1042](CLAIM-1042.md)'s coverage model, independent
parallel attempts are what let similar generalists out-cover specialists,
so the two senses can pull apart. The note is the assistant's (Claude, in
this session); adopting it is the owner's call.
