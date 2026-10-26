---
status: Active
title: 'On one MLP layer each of GPT2-small, Pythia-410M and Pythia-1.4B, transcoders trained to imitate the MLP lay on or above the sparsity–loss frontier of sparse autoencoders trained on its output, at one learning rate tuned on transcoders and one seed, and in a single rater''s blind reading of 50 random features each from Pythia-410M layer 15, 41 transcoder and 38 SAE features were judged interpretable'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed Active from NOTE-tmpbsp9v. One study read in full; the title
    claims no more than its §4 measured, with the authors' own hedges on the
    learning rate and the seed kept, so a replication request does not hold
    it back (ADR-047 v3). Gemma Scope's contrary result (NOTE-482) is on
    another model and does not contradict the title as scoped. The paper's
    general claim that transcoders improve on MLP SAEs (NOTE-tmpbsp9v, C6)
    is a ranking of interpretability methods, and is left in the NOTE.
tags:
- representation-learning
date: '2026-10-26'
source:
- LIT-tmptgo43
summary: >-
  Dunefsky, Chlenski and Nanda (2024), [LIT-tmptgo43](../literature.d/LIT-tmptgo43.md), read in [NOTE-tmpbsp9v](../notes.d/NOTE-tmpbsp9v.md):
  §4, Table 1, Fig. 3 and Apps. E–F. It does not say transcoders are better
  than SAEs in general. The SAE learning rate was not tuned, all runs
  shared one seed and data order, one layer per model was measured, and on
  Gemma 2 2B Gemma Scope found transcoders worse than MLP-output SAEs at
  fixed L0 ([LIT-611](../literature.d/LIT-611.md), [NOTE-482](../notes.d/NOTE-482.md)).
---
# THEORY-tmptjiep: On one MLP layer each of GPT2-small, Pythia-410M and Pythia-1.4B, transcoders trained to imitate the MLP lay on or above the sparsity–loss frontier of sparse autoencoders trained on its output, at one learning rate tuned on transcoders and one seed, and in a single rater's blind reading of 50 random features each from Pythia-410M layer 15, 41 transcoder and 38 SAE features were judged interpretable

## Source

Dunefsky, Chlenski and Nanda (2024), arXiv:2406.11944, [LIT-tmptgo43](../literature.d/LIT-tmptgo43.md), read
in full in [NOTE-tmpbsp9v](../notes.d/NOTE-tmpbsp9v.md): §4.1–4.2, Table 1, Fig. 3, Apps. E and F.

## What was actually shown

**The design.** For GPT2-small layer 8, Pythia-410M layer 15 and
Pythia-1.4B layer 15, several transcoders (MLP input → MLP output) and
several SAEs (on MLP output) were trained at different λ₁, all 32 ×
d_model wide, on 60M OpenWebText tokens, with Adam at 2 × 10⁻⁵ and seed 42.
Each was spliced into the model in place of the MLP output and scored by
next-token cross-entropy on the same 3.2M tokens, against mean L0. The
unmodified model and the mean-ablated MLP bound the range.

**The result.** "In all cases, transcoders are equal to or better than
SAEs. In fact, the gap between transcoders and SAEs seems to widen on
larger models." (The record read this from the text and the caption;
Figure 3's points were not legible in the extracted text.)

**Interpretability.** A transcoder (L0 44.04, 3.35 nats) and an SAE on MLP
inputs (L0 47.85, 3.36 nats) at nearly the same point of the frontier: 50
random features each, shuffled, judged from top-activating examples
before their source was revealed. Transcoder 41 interpretable, 8 maybe, 1
not; SAE 38, 8, 4. The counts sum to 50 each.

**What could have come out otherwise.** SAEs could have dominated the
frontier, as Gemma Scope later found on Gemma 2 2B; the blind counts could
have favoured the SAE.

## What this does not say

- **Not a general ranking.** The authors: the shared learning rate "might
  not be optimal for SAEs", and "a different set of hyperparameters could
  have allowed SAEs to surpass transcoders". One seed, one layer per model.
- **Not for other models.** On Gemma 2 2B the order reverses ([LIT-611](../literature.d/LIT-611.md),
  [NOTE-482](../notes.d/NOTE-482.md)), for reasons not established.
- **Not an interpretability measurement in any strong sense.** One rater,
  one layer, one model, top-activating examples only; the three-point gap
  in "interpretable" is within what a second rater could move.
- **Not about circuits.** Fidelity here is the loss with one MLP replaced;
  it says nothing about how faithful the circuits read off the transcoder
  are.
