---
number: 996
status: Active
formerly:
- THEORY-tmpo1u9l
title: 'On Pythia language models from 410M to 12B parameters, in three single prompt pairs and two small prompt distributions, verifying attention or neuron nodes by activation patching in the order given by attribution patching, a first-order gradient estimate of each node''s noising effect, found the nodes with the largest effects at about 2 to 50 times the cost of an oracle ordering, below unordered patching, subsampling and block search in every setting; its misses were concentrated in queries and keys behind saturated attention and in nodes whose direct and indirect effects nearly cancel'
version: 2
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed Active from NOTE-1190, the reading of Kramár et al. (2024)
    in full. One study; the title claims no more than its figures show,
    with the relative costs read off its bar charts as approximate, and
    nothing in the record contradicts it (ADR-047 v3). The wider claim
    that it transfers is THEORY-1000, Proposed.
- version: 2
  date: '2026-10-27'
  note: >-
    A dated note added: the estimate whose misses this entry measures,
    from Nanda's post registered and read on 2026-10-27, is placed
    under Connections. Title and status unchanged.
tags:
- representation-learning
- causality
date: '2026-10-26'
source:
- LIT-1531
summary: >-
  Kramár, Lieberum, Shah & Nanda (2024), [LIT-1531](../literature.d/LIT-1531.md), read in
  [NOTE-1190](../notes.d/NOTE-1190.md). Ground truth is each node's exact single-node noising
  effect on the clean prompt's negative log probability. Recomputing the
  softmax for queries and keys removes many misses; dropping one layer's
  gradient at a time helps on single prompt pairs but not on the
  distributions, where AtP with the softmax fix or plain AtP is cheapest.
  It says nothing about coarser nodes, other model families, effect
  magnitudes or false positives.
extended_by:
- THEORY-1000
---
<!-- inactive-ok-file: THEORY-1000 THEORY-997 — Proposed; the wider thesis and a neighbouring account, cited as open -->
<!-- inactive-ok-file: THEORY-tmp52c5a — Proposed; the method author's own map of where the estimate fails, cited as open -->

# THEORY-996: On Pythia language models from 410M to 12B parameters, in three single prompt pairs and two small prompt distributions, verifying attention or neuron nodes by activation patching in the order given by attribution patching, a first-order gradient estimate of each node's noising effect, found the nodes with the largest effects at about 2 to 50 times the cost of an oracle ordering, below unordered patching, subsampling and block search in every setting; its misses were concentrated in queries and keys behind saturated attention and in nodes whose direct and indirect effects nearly cancel

## Source

Kramár, Lieberum, Shah and Nanda (2024), *AtP\*: An efficient and
scalable method for localizing LLM behaviour to components*, arXiv
2403.00745, [LIT-1531](../literature.d/LIT-1531.md), read in full in [NOTE-1190](../notes.d/NOTE-1190.md): §§2–4, Figures
1–9 (Figures 1, 2 and 9 from page renderings), Appendices A and B.

## What was actually shown

**Ground truth.** For each node n (a head's query, key, value or output,
or an MLP neuron, at one token position), the exact effect of replacing
its activation on the clean prompt by its value on a reference prompt,
on the negative log probability of the clean next token, averaged in
absolute value over prompt pairs.

**The estimate.** (n(x_noise) − n(x_clean))ᵀ ∂L/∂n, all nodes at once.

**The measure.** The forward passes needed to verify the top K true nodes
when nodes are patched in the method's order, combined over K by an
inverse-rank-weighted geometric mean and divided by the oracle's cost.

**The result**, read off Figures 2 and 9: across Pythia 410M, 1B, 2.8B and
12B, AtP's relative cost ranges from about 2 (IOI distribution) to about
50 (CITY-PP on Pythia-1B). In every setting and model it is below the
iterative baseline and below subsampling, blocks and hierarchical search,
which run from about 5 (iterative, IOI distribution) to over 1,000
(iterative, neurons). The rank plots (Figures 4–5) place AtP's false
negatives among queries and keys whose attention probability changes
most under the patch, and among neurons with large direct-effect ratios
(5.35, 12.2 and 0 for the three largest corrected by GradDrop).

**What could have come out otherwise.** Gradients could have ordered the
nodes no better than chance, as they would if effects were dominated by
non-linear responses; the iterative and sampling methods could have won
on distributions, where averaging favours them.

## What this does not say

- **Not that AtP's estimates are accurate in size.** Only ranks are
  evaluated; false positives are removed by verification and not counted.
- **Not about coarser nodes.** Layers, residual streams and sliding
  windows are out of scope; the authors expect AtP to be worse there.
- **Not about other models.** Pythia only; the transfer is
  [THEORY-1000](THEORY-1000.md).
- **Not that AtP* is always best.** On the two distributions AtP with the
  softmax fix (IOI) or plain AtP (A-AN) is cheaper.
- **Not about multi-node effects.** The ground truth is single-node
  noising; denoising gave worse results on IOI, unexplained.

## Connections

- **[THEORY-997](THEORY-997.md).** Circuits found by edge attribution can drop
  attention edges where the softmax saturates, a source of apparent change
  that is the method's, not the model's.
- **[THEORY-970](THEORY-970.md).** ACDC's HISP baseline is this estimate up to the
  absolute value; there it ranked hand-found edges below ACDC on three
  tasks, a different measure from this one.

## Note of 2026-10-27: the estimate's derivation, now held

- **THEORY-tmpeqz27** (from Nanda's post, LIT-tmpo09rn, read in
  NOTE-tmpxnucs) is the derivation of the estimate whose misses this entry
  measures. It is exact when the metric is affine in the activation and
  gives no effect for a nonlinearity in saturation whatever the true
  change, which is this entry's first cause of misses, predicted.
- **THEORY-tmp52c5a** is the post's own map of where the estimate should
  fail (large patches, the first MLP layer, saturation, effects needing
  several features). Cancelling direct and indirect effects, this entry's
  second cause, is not on it.
