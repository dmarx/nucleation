---
number: 966
status: Active
formerly:
- THEORY-tmp1bwxc
title: 'Greedy edge pruning of the ACDC kind, which removes each edge whose removal changes the output metric by less than a threshold given the edges already removed, keeps only one input of a redundant OR gate, and which input it keeps depends on the order in which edges are visited, so when a model has redundant sufficient paths the circuit it returns is one of several sufficient subgraphs'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed Active from NOTE-1170. Conmy et al. show the one-input
    outcome in a toy (Appendix M); the record re-derived it, including the
    dependence on visiting order, which the paper does not state for the
    toy, and checked both orders numerically (ADR-047 v2).
tags:
- representation-learning
- causality
date: '2026-10-26'
source:
- LIT-1547
summary: >-
  Conmy et al. (2023), [LIT-1547](../literature.d/LIT-1547.md), Appendix M, read in [NOTE-1170](../notes.d/NOTE-1170.md).
  For out = 1 − ReLU(1 − x − y) with x = y = 1, removing either input alone
  leaves the output at 1, so the first one visited is pruned and the
  second is then kept; visiting y first keeps x instead. It does not say
  how common redundant paths are in trained models, nor that any other
  method does better: HISP keeps neither input.
---
<!-- inactive-ok-file: THEORY-802 — Proposed; the wider thesis on several correct explanations, cited as open -->

# THEORY-966: Greedy edge pruning of the ACDC kind, which removes each edge whose removal changes the output metric by less than a threshold given the edges already removed, keeps only one input of a redundant OR gate, and which input it keeps depends on the order in which edges are visited, so when a model has redundant sufficient paths the circuit it returns is one of several sufficient subgraphs

## Source

Conmy, Mavor-Parker, Lynch, Heimersheim and Garriga-Alonso (2023),
[LIT-1547](../literature.d/LIT-1547.md), read in full in [NOTE-1170](../notes.d/NOTE-1170.md): Algorithm 1 (§3), Appendix J
(parent order on induction) and Appendix M (OR gates).

## What was actually shown

**The construction** (Appendix M). A one-layer transformer with model
dimension 1, two heads that each write 1 into the residual stream, and an
MLP computing 1 − ReLU(1 − x − y), an OR of the two heads' outputs on
binary inputs. The dataset is one prompt; ablation is to zero. The
ground-truth circuit is both head-to-MLP edges. ACDC "only recovers one
OR gate input. This is because the iterative algorithm prunes the first
input to the OR gate it iterates over and then keeps the other."

**The re-derivation.** With x = y = 1 the output is 1. Removing x alone
gives 1 − ReLU(0) = 1, a change of 0 < τ, so x is removed. With x removed,
removing y gives 1 − ReLU(1) = 0, a change of 1 ≥ τ, so y is kept. Visiting
y first removes y and keeps x by the same steps. Checked for both orders
with τ = 0.1 (record script, 2026-10-26): the order x, y keeps {y}; the
order y, x keeps {x}. Either output is a subgraph that reproduces the
model's output exactly, and neither is the set of edges the model uses.

**Order matters in a trained model too.** On the two-layer induction model
the authors "found that iterating in increasing order of the head index
was important to achieve better results" (Appendix J).

## What this does not say

- **Not how often trained models contain redundant paths.** The toy is
  constructed; Appendix J shows order dependence on induction without
  locating its cause.
- **Not that other methods do better.** In the same toy HISP keeps
  neither input and subnetwork probing keeps one plus extra nodes.
- **Not that the returned subgraph is wrong as a sufficient circuit.** It
  is sufficient by construction; what fails is the reading of it as the
  set of components that carry the behaviour.

## Connections

- **[THEORY-802](THEORY-802.md) and [QUESTION-234](../questions.d/QUESTION-234.md).** [THEORY-802](THEORY-802.md) asserts several distinct,
  fully correct abstractions at the level of directions; this is the same
  shape at the level of components, proved for a constructed case. It
  does not meet [THEORY-802](THEORY-802.md)'s promote_when, which asks about basis-related
  alignments of one variable.
- **[THEORY-978](THEORY-978.md).** Causal scrubbing, of which ACDC searches a narrow
  class, is likewise silent between hypotheses that score alike.
