---
status: Rejected
title: "Newman's review, by its generating-function derivation of a random walk's first-return time, shows that the exponent 3/2 shared by critical branching cascades and random-walk first passage comes from the hitting-time identity"
version: 1
form: source
grounds:
- THEORY-tmp6jdas
concludes:
- CLAIM-815
tags:
- probabilistic-modeling
- mathematics
date: '2026-11-22'
line:
- formal-apparatus
summary: >-
  Whether Newman's review (LIT-2976), cited unread in CLAIM-815's grounds,
  carries the claim that the shared 3/2 comes from one identity. It does
  not: Newman derives the walk's 3/2 by generating functions (§IV.C) and
  never mentions branching processes, the cycle lemma or Dwass's formula.
  It gives one side of the coincidence and nothing on the link. Rejected
  as a route; LIT-2976 leaves the claim's grounds and its reading
  corroborates only the walk's exponent. Standing of the conclusion apart
  from this route: CLAIM-815 holds it on its own derivation, checked with
  python3 -I, and on CASE-303; no read source states the identity. The wording is the assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-815 THEORY-tmp6jdas CASE-303 — Proposed; the claim, the reading and the case it rests on -->

# ARG-tmp275n1: Newman's review, by its generating-function derivation of a random walk's first-return time, shows that the exponent 3/2 shared by critical branching cascades and random-walk first passage comes from the hitting-time identity

## The inference

CLAIM-815: the 3/2 of critical branching and of first passage both come
from the hitting-time theorem, P(T = n) = (1/n)·P(W_n = −1), with the
local central limit theorem giving n^(−1/2). Ground offered:
THEORY-tmp6jdas.

## Critical questions (source)

**Does the work say this, read in context?** No. §IV.C (pp. 15–16) writes
the generating function of the symmetric walk's returns and extracts
f_2n ∝ n^(−3/2): "So the distribution of return times follows a power law
with exponent α = 3/2." Branching appears nowhere in the review, and
neither does the cycle lemma or the exploration of a tree as a walk.

**Is it said within the scope the claim needs?** Only for the walk's
exponent, which is one input to the claim, not its thesis.

**Does the claim lean on the reading for more than it holds?** It did, by
listing LIT-2976 in its grounds. Corrected there: the reading corroborates
the walk's 3/2 and is not a ground.

## Verdict

Rejected as a route to the thesis.
