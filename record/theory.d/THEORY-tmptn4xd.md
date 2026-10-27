---
status: Active
title: 'On synthetic data from factorial hidden Markov models with three or five hidden chains of two or three states, an unconstrained hidden Markov model with as many states as the chains have joint settings overfits, its test-set excess over the true model rising to 175 bits per observation at five three-state chains against 4.5 for the factorial model trained exactly, while factorial models trained with completely factorized or structured variational E steps are not significantly worse than exact training'
version: 1
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Filed Active from NOTE-tmp0rtz0 under ADR-047's rule for one study read
    in full, with the title limited to what was measured: Table 1 and
    §4.1 of Ghahramani and Jordan (1997), read as text in the authors'
    copy and checked against the publisher's PDF. The structured
    approximation's one significant difference from exact training is in
    its favour, at five two-state chains.
tags:
- probabilistic-modeling
- representation-learning
date: '2026-10-27'
source:
- LIT-tmpkxifq
summary: >-
  Ghahramani and Jordan (1997), LIT-tmpkxifq, read in NOTE-tmp0rtz0. Four
  sizes, 15 random parameter sets each, 20 training and 20 test sequences
  of length 20, four-dimensional, C = 0.0025I, one run per set. In bits per
  observation over the true model, the K^M-state HMM's test excess is
  2.29, 9.81, 11.57 and 175.35; the exact factorial HMM's 1.05, 1.26, 2.51
  and 4.49; the structured approximation's 1.04, 0.90, 1.53 and 4.30. It
  is a result on small synthetic problems the model generated, not on
  real data or long sequences.
---
<!-- inactive-ok-file: CASE-165 — Proposed; the construction this bears on, cited as open -->

# THEORY-tmptn4xd: On synthetic data from factorial hidden Markov models with three or five hidden chains of two or three states, an unconstrained hidden Markov model with as many states as the chains have joint settings overfits, its test-set excess over the true model rising to 175 bits per observation at five three-state chains against 4.5 for the factorial model trained exactly, while factorial models trained with completely factorized or structured variational E steps are not significantly worse than exact training

## Source

Ghahramani and Jordan (1997), *Factorial hidden Markov models*,
LIT-tmpkxifq, read in full in NOTE-tmp0rtz0: §4.1 and Table 1.

## What was actually shown

Data from factorial HMMs with parameters drawn uniformly and normalized,
C = 0.0025I, four sizes (M, K) = (3, 2), (3, 3), (5, 2), (5, 3), 15
parameter sets each; 20 training and 20 test sequences of length 20;
each algorithm run once per set, for at most 100 EM iterations. Test-set
negative log likelihood in bits per observation relative to the true
model, mean ± one standard deviation over 15:

| (M, K) | HMM | exact | Gibbs | CFVA | SVA |
|---|---|---|---|---|---|
| (3, 2) | 2.29 ± 1.02 | 1.05 ± 0.72 | 1.78 ± 1.22 | 1.20 ± 1.11 | 1.04 ± 1.01 |
| (3, 3) | 9.81 ± 2.55 | 1.26 ± 0.99 | 2.50 ± 0.87 | 1.50 ± 1.53 | 0.90 ± 0.84 |
| (5, 2) | 11.57 ± 3.71 | 2.51 ± 1.21 | 3.35 ± 1.14 | 2.07 ± 1.74 | 1.53 ± 1.05 |
| (5, 3) | 175.35 ± 84.74 | 4.49 ± 2.24 | 3.95 ± 1.14 | 5.14 ± 0.69 | 4.30 ± 1.62 |

The HMM's training excess at (5, 3) is −4.80: it fits the training
sequences better than the generating model. By the paper's tests, Gibbs
(ten samples per variable) is significantly worse than exact on the three
smaller sizes; the completely factorized approximation is never
significantly different; the structured one is not different on three
sizes and better at (5, 2), p < 0.05.

## What this does not say

- **Not that the approximations are accurate in general.** The problems
  are tiny (sequences of 20 steps), nearly noiseless, and drawn from the
  model itself.
- **Not that the structured approximation regularizes.** The authors offer
  that as one of two explanations of the (5, 2) difference, the other
  being chance.
- **Not anything about the Bach result**, which is read from a chart.

## Connections

- **LIT-1577.** The infinite factorial HMM keeps the factorial structure
  and lets M grow; its experiments compare priors, not inference methods.
- **CASE-165.** A fitted version of the case's per-member chains would face
  this paper's trade-off between exact and approximate E steps
  (NOTE-tmp0rtz0).
