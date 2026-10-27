---
status: Active
title: 'On Pythia language models from 410M to 12B parameters, in three single prompt pairs and two small prompt distributions, verifying attention or neuron nodes by activation patching in the order given by attribution patching, a first-order gradient estimate of each node''s noising effect, found the nodes with the largest effects at about 2 to 50 times the cost of an oracle ordering, below unordered patching, subsampling and block search in every setting; its misses were concentrated in queries and keys behind saturated attention and in nodes whose direct and indirect effects nearly cancel'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed Active from NOTE-tmpz2cvc, the reading of Kramár et al. (2024)
    in full. One study; the title claims no more than its figures show,
    with the relative costs read off its bar charts as approximate, and
    nothing in the record contradicts it (ADR-047 v3). The wider claim
    that it transfers is THEORY-tmpq26u7, Proposed.
tags:
- representation-learning
- causality
date: '2026-10-26'
source:
- LIT-tmp4de8g
summary: >-
  Kramár, Lieberum, Shah & Nanda (2024), [LIT-tmp4de8g](../literature.d/LIT-tmp4de8g.md), read in
  [NOTE-tmpz2cvc](../notes.d/NOTE-tmpz2cvc.md). Ground truth is each node's exact single-node noising
  effect on the clean prompt's negative log probability. Recomputing the
  softmax for queries and keys removes many misses; dropping one layer's
  gradient at a time helps on single prompt pairs but not on the
  distributions, where AtP with the softmax fix or plain AtP is cheapest.
  It says nothing about coarser nodes, other model families, effect
  magnitudes or false positives.
extended_by:
- THEORY-tmpq26u7
---
<!-- inactive-ok-file: THEORY-tmpq26u7 THEORY-tmpoirdq — Proposed; the wider thesis and a neighbouring account, cited as open -->

# THEORY-tmpo1u9l: On Pythia language models from 410M to 12B parameters, in three single prompt pairs and two small prompt distributions, verifying attention or neuron nodes by activation patching in the order given by attribution patching, a first-order gradient estimate of each node's noising effect, found the nodes with the largest effects at about 2 to 50 times the cost of an oracle ordering, below unordered patching, subsampling and block search in every setting; its misses were concentrated in queries and keys behind saturated attention and in nodes whose direct and indirect effects nearly cancel

## Source

Kramár, Lieberum, Shah and Nanda (2024), *AtP\*: An efficient and
scalable method for localizing LLM behaviour to components*, arXiv
2403.00745, [LIT-tmp4de8g](../literature.d/LIT-tmp4de8g.md), read in full in [NOTE-tmpz2cvc](../notes.d/NOTE-tmpz2cvc.md): §§2–4, Figures
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
  [THEORY-tmpq26u7](THEORY-tmpq26u7.md).
- **Not that AtP* is always best.** On the two distributions AtP with the
  softmax fix (IOI) or plain AtP (A-AN) is cheaper.
- **Not about multi-node effects.** The ground truth is single-node
  noising; denoising gave worse results on IOI, unexplained.

## Connections

- **[THEORY-tmpoirdq](THEORY-tmpoirdq.md).** Circuits found by edge attribution can drop
  attention edges where the softmax saturates, a source of apparent change
  that is the method's, not the model's.
- **[THEORY-tmp77xju](THEORY-tmp77xju.md).** ACDC's HISP baseline is this estimate up to the
  absolute value; there it ranked hand-found edges below ACDC on three
  tasks, a different measure from this one.
