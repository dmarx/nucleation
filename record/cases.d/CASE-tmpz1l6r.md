---
status: Proposed
title: 'A tolerance-indexed pass rate for a set of demands, the probability that one of k sampled courses of action of at most T steps meets every demand in the set within its tolerance, with a simulated institution whose internal evaluator sees only the demands it has discovered and an independent evaluator sees them all'
version: 1
standing: stipulated
kind: construction
tags:
- mathematics
- society-and-governance
- operations-research
date: '2026-11-12'
line:
- realizability
- organizational-normativity
illustrates:
- CLAIM-tmpvceet
- CLAIM-tmpyc5md
bears_on:
- QUESTION-279
- QUESTION-tmpuftum
draws_on:
- THEORY-tmps74c5
reported_in:
- LIT-tmpt7avk
summary: >-
  A's (ChatGPT's), A44 §2 and §7 of the exchange "Medical Ethics and Media
  Enshitification" (2026-11-11), on the owner's U21. A generalization of
  PASS@(k,T) that A marks as "a proposed generalization, not a metric
  defined in the PASS@(k,T) paper", joining it to CLAIM-555's tolerance
  regions, and a proposed simulation that uses it. Not run. The wording is
  A's; adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmpvceet CLAIM-tmpyc5md THEORY-tmps74c5 — filed from the same exchange, Proposed -->
<!-- inactive-ok-file: CLAIM-555 — Proposed; the tolerance-indexed acceptance sets the construction uses -->

# CASE-tmpz1l6r: A tolerance-indexed pass rate for a set of demands, the probability that one of k sampled courses of action of at most T steps meets every demand in the set within its tolerance, with a simulated institution whose internal evaluator sees only the demands it has discovered and an independent evaluator sees them all

## The case

**The quantity (A44 §2).** For a policy π, a set of demands S with losses
L_i and tolerances ε_i (CLAIM-555's A_i(ε_i) = {x : L_i(x) ≤ ε_i}), and
budgets k and T:

PASS^π_{S,ε}@(k,T) = Pr[∃ j ≤ k : ∀ i ∈ S, L_i(τ^(j)) ≤ ε_i],

with τ^(1), …, τ^(k) independent trajectories of at most T steps. Its axes
are breadth k, depth T and the tolerance vector ε. It is antitone in S, by
CLAIM-tmpvceet's step 1, and monotone in each ε_i.

**Two probabilities (A44 §5).** "Oracle-assessed availability", the chance
that some sampled policy is acceptable, against "Operational success", the
chance that an acceptable policy is selected and implemented. The paper's
pass@k credits the first; an institution needs the second, and the two
differ when its own evaluator cannot recognize the acceptable candidate.

**The simulation (A44 §7).** An institution faces a known, independently
specified set of stakeholder requirements, some visible at once and some
discoverable only after a sequence of inquiries. Policies with the same
total budget split it differently among repeated shallow attempts, deeper
investigation, verification and implementation. An internal evaluator
scores against the requirements found so far; an independent one scores
against all. Then reward the institution for a low internal failure count,
and see whether it learns "to avoid inquiries likely to uncover additional
requirements".

## What it can show

Whether CLAIM-tmpvceet's incentive produces avoidance of inquiry in an
adaptive system, and which designs prevent it. With the tolerance axis, it
can tell an improved pass rate by accommodation from one by relaxed
tolerances (CLAIM-549's distinction).

## What it cannot show

That the stipulated requirements are justified: A44 says the experiment
"would not derive the legitimacy of the underlying requirements". And a
finite run of failures does not show a demand set unsatisfiable, the
limitation A44 states and QUESTION-279 asks about.
