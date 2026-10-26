---
status: Active
title: 'On four subject–verb agreement tasks in Pythia-70M and Gemma-2-2B, circuits of sparse-autoencoder features and autoencoder error nodes, selected by linear estimates of indirect effect, carried half or more of the behaviour on held-out pairs with about 100 and 500 nodes, where circuits of neurons needed about 1,500 and more than 30,000; with the error nodes removed, the same feature circuits carried little of it, under about a quarter in Pythia and almost none in Gemma'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed Active from NOTE-tmpr0gdc, the reading of Marks et al. (2025) in
    full. One study; the title claims what its Figure 3 measured, read from
    a page rendering, with the authors' hedge that error nodes cannot
    fairly be compared with neurons kept, and nothing in the record
    contradicts it (ADR-047 v3). The paper's 50,000 neurons for Gemma lies
    beyond the plotted range, so the title says "more than 30,000". The
    reading that agreement is carried by an arrangement of features across
    pathways is in THEORY-tmpyawf9 and the NOTE.
tags:
- representation-learning
- causality
date: '2026-10-26'
source:
- LIT-tmp5b0z9
extended_by:
- THEORY-tmpyawf9
summary: >-
  Marks et al. (2025), LIT-tmp5b0z9, read in NOTE-tmpr0gdc: §§2–3.2,
  Figure 3 and Appendices A, B and H. Faithfulness is (m(C) − m(∅))/(m(M) −
  m(∅)) with nodes outside the circuit mean-ablated, scored on the latter
  two thirds of each circuit only. The features plus the dense error terms
  are a small circuit; the features by themselves are not. It says nothing
  about what the error terms hold, and it does not compare features with
  neurons on equal terms, which the authors say cannot be done.
---
<!-- inactive-ok-file: CLAIM-tmpwr001 THEORY-tmpyawf9 — Proposed; the claim this bears on and the account filed from the same reading, cited as open -->
# THEORY-tmpuogp2: On four subject–verb agreement tasks in Pythia-70M and Gemma-2-2B, circuits of sparse-autoencoder features and autoencoder error nodes, selected by linear estimates of indirect effect, carried half or more of the behaviour on held-out pairs with about 100 and 500 nodes, where circuits of neurons needed about 1,500 and more than 30,000; with the error nodes removed, the same feature circuits carried little of it, under about a quarter in Pythia and almost none in Gemma

## Source

Marks, Rager, Michaud, Belinkov, Bau and Mueller (2025), *Sparse feature
circuits*, ICLR 2025, arXiv:2403.19647, LIT-tmp5b0z9, read in full in
NOTE-tmpr0gdc: §2 (formulation), §3.1–3.2 with Figure 3 (read from a
rendering of p. 5), and Appendices A, B and H.

## What was actually shown

**The decomposition.** At each site with an autoencoder, x = Σ f_i(x)v_i +
b + ε(x). Feature activations f_i and the error ε are nodes; a node's
indirect effect on m = log P(correct verb) − log P(wrong verb) for a
contrastive pair (subject number flipped) is estimated by attribution
patching or integrated gradients, averaged over the training pairs, and
thresholded. Neuron circuits are found the same way with basis directions
and no error terms.

**Faithfulness.** On held-out pairs, nodes outside the circuit are
mean-ablated; the first third of each circuit is left unablated and
unscored. Averaged over the four tasks, feature circuits pass one half by
about 100 nodes (Pythia) and 500 (Gemma). Neuron circuits reach about 0.5
at 1,500 nodes in Pythia; in Gemma they are near 0.3 at 30,000, the edge
of the plot, and the paper puts the half point at 50,000.

**Without the errors.** The curves for the feature circuits with every
error node removed stay under about 0.25 in Pythia and near zero in Gemma.
With only the attention and MLP error nodes removed they stay much closer
to the full feature circuits. "Removing residual stream SAE error nodes
severely disrupts the model."

**Completeness.** Ablating a few feature nodes removes the behaviour even
with all error nodes left in; hundreds or thousands of neurons are needed
for the same.

**What could have come out otherwise.** The features could have carried
the behaviour by themselves, with the error terms negligible. In these
models and tasks they did not.

## What this does not say

- **Not that features beat neurons as units.** A feature circuit's error
  nodes are dense and high-dimensional, and the authors say they "cannot
  be fairly compared to neurons".
- **Not what the errors contain.** Features the dictionary missed, or
  structure no sparse dictionary of this width captures.
- **Not about the first layers.** The first third of each circuit is not
  scored, because held-out pairs use different tokens.
- **Not general.** Two small models, one family of tasks with templated
  contrasts.

## Connections

- **CLAIM-tmpwr001.** Features recovered without the task do not carry
  it on their own; what does is features plus a remainder, arranged across
  positions and layers.
- **THEORY-tmp4lqc8.** Two results that point the same way from
  different tests: SAE features localize supplied variables worse than
  neurons, and SAE features without their error terms carry little of a
  behaviour.
- **THEORY-504.** The residual-stream errors matter most here, as
  residual-stream autoencoders cost Gemma 2 the most loss there.
- **THEORY-tmph7ceb.** The same family of linear estimates selects the
  nodes.
