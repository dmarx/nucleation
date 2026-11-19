---
status: Proposed
title: 'Yin and Steinhardt show that, in twelve language models from 70M to 7B parameters, few-shot in-context accuracy depends mainly on function-vector heads and not on induction heads once heads with both properties are spared, increasingly so with scale, while induction heads matter more for the token-loss difference; and that across Pythia training induction heads form near step 1,000 while function-vector heads strengthen from about step 16,000 to the end, many of them having first been induction heads'
version: 1
source:
- LIT-tmpbi4vz
tags:
- representation-learning
date: '2026-11-19'
promote_when: >-
  An independent ablation study on models above 1B parameters finds that
  ablating induction heads with low function-vector scores costs few-shot
  ICL accuracy no more than random ablation while ablating function-vector
  heads with low induction scores costs substantially more; or an
  independent analysis of training checkpoints finds function-vector heads
  that earlier had high induction scores.
summary: >-
  From the reading of LIT-tmpbi4vz in NOTE-tmpa9eoe. Yin and Steinhardt
  (2025; arXiv 2502.14010) compare induction heads and function-vector
  (FV) heads in twelve models (Pythia 70M–6.9B, GPT-2, Llama 2 7B).
  Ablating each type while sparing heads of the other shows that few-shot
  in-context accuracy depends mainly on FV heads, increasingly with scale.
  Induction heads matter for Olsson et al.'s token-loss difference, which
  the authors show measures something else. Across Pythia training,
  induction heads form near step 1,000 of 143,000. FV heads strengthen
  from about step 16,000 to the end, with few-shot accuracy, and many
  began as induction heads; that they are precursors is the authors'
  conjecture. Here because A56 used it for the in-context arm of CASE-
  tmphsr99. On Pythia it says in-context ability is still rising at late
  checkpoints, and it qualifies THEORY-990. Read in its NOTE.
---
<!-- inactive-ok-file: THEORY-990 — Proposed; cited in this filing of 2026-11-19 -->

# THEORY-tmpqvj8f: Yin and Steinhardt show that, in twelve language models from 70M to 7B parameters, few-shot in-context accuracy depends mainly on function-vector heads and not on induction heads once heads with both properties are spared, increasingly so with scale, while induction heads matter more for the token-loss difference; and that across Pythia training induction heads form near step 1,000 while function-vector heads strengthen from about step 16,000 to the end, many of them having first been induction heads

## The account

Induction heads and function-vector heads are mostly different heads, though their scores correlate. Controlling for that correlation reverses the usual attribution. For few-shot accuracy on held-out tasks, non-FV induction heads can be ablated about as harmlessly as random heads in models above 1B. Non-induction FV heads cannot, and the gap grows with scale. The older attribution rested on token-loss difference, which induction heads do carry, and on the overlap between the two sets. In Pythia, induction heads appear near step 1,000 of 143,000 and plateau. FV heads appear around step 16,000 and strengthen to the end, and few-shot accuracy rises with them. Many FV heads were induction heads first, and never the reverse.

## What it does not show

- That induction heads cause FV heads to form: the precursor reading is the authors' conjecture from correlation over 8 checkpoints of one run per size.
- That FV heads are the whole mechanism, or that the result holds for tasks beyond Todd et al.'s mostly lexical set.
- Anything about fine-tuning plasticity or acquisition cost across checkpoints.
