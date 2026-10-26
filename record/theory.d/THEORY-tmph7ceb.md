---
status: Active
title: 'In Claude 3 Sonnet''s middle-layer residual stream, on two prompts for which every active sparse-autoencoder feature was ablated, how strongly a feature was active predicted its ablation effect on the answer poorly (correlation about 0.12) while its gradient attribution predicted it well (about 0.81), and on the multi-step prompt only three of the ten most active features were among the ten with the largest ablation effect'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed Active from NOTE-tmpfpjyr, the reading of Templeton et al. (2024)
    in full. One study; the title claims no more than its two-prompt
    comparison measured, with every active feature ablated, and nothing in
    the record contradicts it (ADR-047 v3). That activation is a poor guide
    to role in general is not claimed; the authors call the example
    "somewhat cherry-picked".
tags:
- representation-learning
- causality
date: '2026-10-26'
source:
- LIT-tmp8w8uj
extended_by:
- THEORY-tmp14ee2
summary: >-
  Templeton et al. (2024), [LIT-tmp8w8uj](../literature.d/LIT-tmp8w8uj.md), read in [NOTE-tmpfpjyr](../notes.d/NOTE-tmpfpjyr.md): Features
  as Computational Intermediates and the appendix on ablations and
  attributions. On "The capital of the state where Kobe Bryant played
  basketball is" (Sacramento against Albany), the five features with the
  largest ablation effect, Kobe Bryant, California, capital, Los Angeles
  and the Lakers, rank as low as 70th to 162nd by activation. It does not
  say how often this holds beyond the two prompts, and for other prompts
  the authors found no intermediate features at this layer.
---
<!-- inactive-ok-file: CLAIM-tmpwr001 THEORY-tmp14ee2 — Proposed; the claim this bears on and the wider thesis filed from the same reading, cited as open -->
# THEORY-tmph7ceb: In Claude 3 Sonnet's middle-layer residual stream, on two prompts for which every active sparse-autoencoder feature was ablated, how strongly a feature was active predicted its ablation effect on the answer poorly (correlation about 0.12) while its gradient attribution predicted it well (about 0.81), and on the multi-step prompt only three of the ten most active features were among the ten with the largest ablation effect

## Source

Templeton, Conerly, Marcus, Lindsey et al. (2024), *Scaling
monosemanticity*, [LIT-tmp8w8uj](../literature.d/LIT-tmp8w8uj.md), read in full in [NOTE-tmpfpjyr](../notes.d/NOTE-tmpfpjyr.md): Features as
Computational Intermediates and the appendix "Ablations and
Attributions".

## What was actually shown

**The measures.** Attribution: the gradient of the logit difference
between the answer and a baseline token with respect to the middle-layer
residual stream, dotted with the feature's decoder vector, times its
activation. Ablation: the feature clamped to zero at one position, the
forward pass completed, and the change in the logit difference recorded.
Both prompts had every active feature ablated "for completeness".

**The prompts.** "John says, 'I want to be alone right now.' John feels"
(sad against happy), and "Fact: The capital of the state where Kobe
Bryant played basketball is" (Sacramento against Albany).

**The result.** Across the two prompts, attribution correlates with
ablation effect at about 0.81 and activation at about 0.12. On the Kobe
prompt the top five by ablation (Kobe Bryant, California, capital, Los
Angeles, the Lakers) match the top five by attribution up to order; the
Lakers feature is the 70th most active, California the 97th, the Los
Angeles area-code feature the 162nd. Three of the ten most active features
are among the ten with the largest ablation effect, against eight of the
ten most attributed. A control prompt about Kobe's team's rival implicates
the Kobe and Lakers features and not the California or Los Angeles ones.

**What could have come out otherwise.** The most active features could
have been the ones the answer depends on. They were mostly features of the
prompt's surface (the start-of-sequence token, "be" in "want to be", the
word "alone").

## What this does not say

- **Not general.** Two prompts at one layer of one model. The authors call
  the example "somewhat cherry-picked", and for some prompts the features
  found by attribution and ablation related only to input or output.
- **Not that the intermediate features form a circuit.** No edges between
  them are measured; the sequence Kobe → California → Sacramento is the
  authors' reading.
- **Not that attribution is exact.** Its correlation with ablation is
  about 0.81 on these prompts.

## Connections

- **[CLAIM-tmpwr001](../claims.d/CLAIM-tmpwr001.md).** A measured case of the claim's point in a network:
  that a feature is active says little about whether it carries the
  computation; which features do is found by intervening.
- **[THEORY-tmpuogp2](THEORY-tmpuogp2.md).** The same method (linear approximations to indirect
  effects) is how sparse feature circuits choose their nodes.
- **[THEORY-tmp4lqc8](THEORY-tmp4lqc8.md).** MIB scores features by interchange interventions
  for supplied variables; here features are found by ablation for an
  answer, with no variable supplied.
