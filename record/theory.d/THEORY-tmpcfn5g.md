---
status: Proposed
promote_when: >-
  An independent derivation, or the record's own by proof or by the
  stationary vector, of the 1/i visiting law for the process that from
  state i jumps uniformly to a state below i, and of the asymptotic i^(−λ)
  occupation of its mixture with uniform jumps over all states. Not met
  by the word-frequency example, which the title does not assert.
title: 'Corominas-Murtra, Hanel and Thurner prove that a process jumping uniformly to a lower state visits state i with probability exactly 1 over i, and that mixing its nested steps with uniform jumps gives occupation falling as i to the minus lambda'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 from the delegated reading in NOTE-tmpyqqhq; quotations
    rechecked by the filer against the text.
tags:
- probabilistic-modeling
- complex-systems
date: '2026-11-22'
source:
- LIT-2997
bears_on:
- QUESTION-505
summary: >-
  Corominas-Murtra, Hanel and Thurner (2015), LIT-2997, read in
  NOTE-tmpyqqhq. Sample-space reduction as a route to Zipf's law, with the
  exponent as the share of nested steps. Proved for uniform jumps only;
  a Markov chain with no reinforcement. Proposed until the derivation is
  checked independently.
---
<!-- inactive-ok-file: NOTE-tmpyqqhq CLAIM-795 THEORY-2150 QUESTION-505 LIT-tmppzucs — Proposed, Deferred or new; this account's reading and the entries it bears on -->

# THEORY-tmpcfn5g: Corominas-Murtra, Hanel and Thurner prove that a process jumping uniformly to a lower state visits state i with probability exactly 1 over i, and that mixing its nested steps with uniform jumps gives occupation falling as i to the minus lambda

## Source

Corominas-Murtra, Hanel and Thurner (2015), LIT-2997, read in NOTE-tmpyqqhq
from arXiv v3.

## What was actually shown

The strict process (throw die N, then die K − 1 after getting K, down to 1)
visits site i with probability that "can easily be shown to follow an exact
Zipf's law, PN(i) = 1/i" (p. 2, eq. 1), by induction on N; visits and
occupation are proportional because each run is strictly decreasing.
Mixing each step with probability 1 − λ with a uniform jump over all N
states and restarting at the top gives p(i)/p(1) = Π_{j<i}(1 + λ/j)^(−1),
"an asymptotically exact power-law with exponent λ" (p. 4), and a frequency
exponent (1 + λ)/λ. The reader's stationary-vector check gives slopes
−1.000, −0.702, −0.503 for λ = 1, 0.7, 0.5.

## What this does not say

- Not that every sample-space-reducing process gives Zipf's law, despite
  the abstract's "necessarily": only uniform jumps are treated.
- Not that word frequencies come from this mechanism: λ = 0.9 is read off
  a fitted slope.
- Not a history- or reinforcement-dependent process: the strict process is
  a Markov chain, P(j | i) = 1/(i − 1).

## Connections

Item 5 of CLAIM-795. A mix of a structured and a uniform choice sets the
exponent here as in Mitzenmacher's attachment with a uniform share
(THEORY-2150). A rival feedback-free route to Zipf in words is Miller's
random typing (LIT-tmppzucs). The account `bears_on` QUESTION-505. It is
not in `corroborates` on CLAIM-795: the claim's item 5 grounds on it.
