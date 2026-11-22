---
status: Proposed
title: 'Exact computation on small finite experiments checks the receiver-restricted order''s results: the exclusive-or rendering and a strict reversal of Blackwell''s order for a one-coordinate receiver, and random instances of the achievable-set criterion, the respected-garbling theorem, the ceiling and the code-reading converse, with no disagreement'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-100. Code, tests
    and results are under scratch/studies/lead-100/.
standing: documented
kind: executed-study
tags:
- information-theory
- mathematical-statistics
date: '2026-11-22'
line:
- pragmatic-transport
- formal-apparatus
illustrates:
- CLAIM-tmp03h8w
- CLAIM-199
summary: >-
  The six results of CLAIM-tmp03h8w were checked by exact computation with
  linear programs (scipy's HiGHS) on finite experiments, in
  scratch/studies/lead-100/ (rorder.py, run_checks.py, results.json, about
  25 seconds on one thread). Two constructions reproduce CLAIM-199's
  exclusive-or example on a common medium and result 5's strict reversal.
  Four batches of random instances (300, 300, 500 and 200) found no
  disagreement with results 2, 3, 4 and 6. The checks illustrate the proofs
  and bear none of their weight.
---
<!-- inactive-ok-file: CLAIM-tmp03h8w — new, filed with this case -->

# CASE-tmphabte: Exact computation on small finite experiments checks the receiver-restricted order's results: the exclusive-or rendering and a strict reversal of Blackwell's order for a one-coordinate receiver, and random instances of the achievable-set criterion, the respected-garbling theorem, the ceiling and the code-reading converse, with no disagreement

## What was done

A receiver class is given by the vertices of its rule hull (for a class
that reads through a deterministic code T, the rules T·D with D
deterministic). Usable risk is a minimum over those vertices. Inclusion of
achievable sets is a linear feasibility problem, and when it fails a
second linear program returns a separating loss. Seeds are fixed
(numpy default_rng(100)).

## Constructions

- **E1, CLAIM-199's exclusive-or on one medium.** Θ = {0,1}, medium
  {0,1}², source x₁ a fair coin and x₂ = θ ⊕ x₁, rendering the garbling
  (x₁, x₂) ↦ (x₁ ⊕ x₂, 0). The one-coordinate receiver's risk for guessing
  θ under 0–1 loss is 0.5 with the source and 0 with the rendering; the
  unrestricted receiver's is 0 with both. The garbling is not in Mon(R).
- **E2, the strict reversal (result 5).** P reports x₁ = θ with
  probability 0.9 and an independent fair coin in x₂. The one-coordinate
  receiver: P ⪰_R source true, source ⪰_R P false, risks 0.1 and 0.5. The
  unrestricted receiver: source ⪰ P true, P ⪰ source false, risks 0 and
  0.1.

## Random checks

Three situations, a medium of four outcomes, two actions; receivers read
through a random surjective code onto two letters, unless stated.

| Batch | Result checked | Instances | Outcome |
|---|---|---|---|
| T1 | 2: inclusion decides the order, for every prior | 300 (150 inclusions) | 300 agree. With inclusion, 0 of 45,000 random (loss, prior) pairs favoured P'. Without it, the separating loss rescaled by each of 5 random priors favoured P' every time. |
| T2 | 3 and 6: respecting G is factoring GT = TH | 300 (154 respected) | Hull test and factoring test agree on all 300. No monotonicity violation in 7,700 random (P, loss, prior) triples for respected G. For each of the 146 others, the identity experiment with the separating loss shows G helping. |
| T3 | 4: the ceiling | 500 | 0 violations. |
| T4 | 6: code-reading receivers have Blackwell's order on PT | 200 (codes onto three letters, three actions) | Inclusion and "P'T is a garbling of PT" agree on all 200 (117 dominated). |

## What it shows and does not

The computations agree with the proofs everywhere they were tried, and the
two constructions are exact (no sampling). The random batches are small
and confined to deterministic codes; they would catch a gross error in a
statement, not a subtle one in a proof, and the claim does not rest on
them.
