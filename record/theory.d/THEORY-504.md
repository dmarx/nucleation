---
number: 504
status: Active
formerly:
- THEORY-tmpdlewi
title: "In the Gemma Scope sparse autoencoders on Gemma 2, the two fidelity measures disagree by site: residual-stream autoencoders cost more next-token loss than MLP or attention ones at comparable fraction of variance unexplained, and base-model autoencoders transfer to the instruction-tuned model by loss more than by variance explained"
version: 2
history:
- version: 2
  date: '2026-10-27'
  note: >-
    A dated note added: two circuits works read on 2026-10-26
    concern residual-stream autoencoders and find what the
    dictionary leaves out to matter there. Status and title are
    unchanged.
tags:
- representation-learning
- anthology-candidate
date: '2026-10-16'
source:
- LIT-611
summary: >-
  Lieberum et al. (2024), [LIT-611](../literature.d/LIT-611.md), read in [NOTE-482](../notes.d/NOTE-482.md). Across every layer
  and sublayer of Gemma 2 2B and 9B, JumpReLU autoencoders on the residual
  stream raise the language model's loss more, when spliced in, than MLP
  and attention autoencoders whose FVU is about the same; and autoencoders
  trained on the base model lose little loss on instruction-tuned rollouts
  while showing a larger FVU gap. The authors' explanations (the residual
  stream is the bottleneck; fine-tuning re-weights old features) are
  conjectures, and the authors say no agreed metric of autoencoder quality
  exists.
---

# THEORY-504: In the Gemma Scope sparse autoencoders on Gemma 2, the two fidelity measures disagree by site: residual-stream autoencoders cost more next-token loss than MLP or attention ones at comparable fraction of variance unexplained, and base-model autoencoders transfer to the instruction-tuned model by loss more than by variance explained

## Source

Lieberum, Rajamanoharan, Conmy, Smith, Sonnerat, Varma, Kramár, Dragan,
Shah & Nanda (2024), [LIT-611](../literature.d/LIT-611.md), read in full in [NOTE-482](../notes.d/NOTE-482.md).

## What was actually shown

**The autoencoders.** A JumpReLU SAE encodes x as f(x) = z ⊙ H(z − θ) with
z = W_enc x + b_enc and a learned per-latent threshold θ, decodes as
W_dec f + b_dec, and trains on ‖x − x̂‖² + λ‖f(x)‖₀ (Eqs. 1–4). The release
covers every layer and sublayer of Gemma 2 2B and 9B, and three layers of
27B, at widths 2¹⁴ to 2²⁰, each at several sparsities, trained on 4–16B
tokens.

**Two fidelity measures.** Delta LM loss is the rise in the model's
cross-entropy when the reconstruction is spliced into the forward pass.
FVU is reconstruction error over the error of predicting the mean.

**The disagreement by site (§4.1, Fig. 2, App. C.1).** At a given mean L0,
delta LM loss is consistently higher for residual-stream autoencoders than
for MLP-output and attention-output ones, while FVU is roughly comparable
across sites. The paper's account is that each sublayer is a small part of
the residual stream, so its errors matter less downstream.

**The disagreement in transfer (§4.5, Fig. 8, App. C.4).** Autoencoders
trained on the base model raise loss on instruction-tuned rollouts almost
as little as autoencoders trained on the instruction-tuned model. By FVU
the gap is larger. Splicing base autoencoders into the instruction-tuned
model can even lower its loss on user prompts.

**Other measured regularities.** Wider autoencoders reconstruct better at
fixed L0, their firing-frequency mode shifts lower, and a cluster of
ultra-high-frequency latents persists (Figs. 4–5). Reconstruction loss
rises over the first tokens of a sequence (Fig. 3). Fidelity is best on
mathematics and worst on Europarl (Fig. 9).

## What this does not say

- **That residual-stream autoencoders are worse autoencoders.** The same
  reconstruction error costs more there because more of the computation
  reads it. Which measure is the right one is the open problem the authors
  state: "there is no consensus on what constitutes a reliable metric for
  the quality of a sparse autoencoder" (§4).
- **That fine-tuning leaves the features unchanged.** The authors'
  hypothesis, that fine-tuning re-weights old features and adds chat
  features that matter little for next-token loss, is offered to explain
  the transfer and is not tested.
- **That the latents are the model's features.** The paper calls them
  latents on purpose (footnote 4). The linear-features premise is built
  in, not tested, and nothing is evaluated against known features.
- **That JumpReLU is more interpretable.** The interpretability comparison
  is reproduced from another paper, at one width on one model, and finds
  little difference among JumpReLU, TopK and Gated autoencoders.

## Connections

- **The superposition premise** is Elhage et al. ([LIT-323](../literature.d/LIT-323.md)): more features
  than dimensions, recoverable when sparse. Engels et al. ([LIT-322](../literature.d/LIT-322.md)) found
  circular, multi-dimensional features by clustering such latents, which
  the report lists as an open problem for autoencoders.
- **The anthology** holds Kantamneni et al. ([ANTH-LIT-568](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-568.md)), who probe with
  Gemma Scope latents and find they add almost nothing over baselines.
- **[NOTE-482](../notes.d/NOTE-482.md)** reads the flat price λ per active latent as an information
  criterion charging a fixed cost per component, so that choosing λ and
  the width is a model-comparison problem. That is the reader's framing,
  not the paper's, and this account does not rest on it.

## Note of 2026-10-27: two residual-stream readings set beside it

Two of the circuits works read on 2026-10-26 at the owner's request
concern residual-stream autoencoders, the site where this account finds
the loss cost highest.

- Marks et al.'s sparse feature circuits ([LIT-tmp5b0z9](../literature.d/LIT-tmp5b0z9.md)) use Gemma
  Scope's residual-stream autoencoders on Gemma-2-2B, beside their own on
  Pythia-70M. They find that "removing residual stream SAE error nodes
  severely disrupts the model", and without the error nodes their feature circuits recover
  little of subject–verb agreement ([THEORY-tmpuogp2](THEORY-tmpuogp2.md)).
- Templeton et al. ([LIT-tmp8w8uj](../literature.d/LIT-tmp8w8uj.md)) train residual-stream autoencoders on
  Claude 3 Sonnet that explain at least 65% of the variance, and keep the
  error term when steering ([NOTE-tmpfpjyr](../notes.d/NOTE-tmpfpjyr.md)).

Neither compares sites at equal variance unexplained, which is this
account's measurement. Both agree that at the residual stream what the
dictionary leaves out carries much of the behaviour. The account is
unchanged.
