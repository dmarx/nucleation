---
number: 1897
status: Proposed
formerly:
- THEORY-tmpqakuv
promote_when: >-
  An independent group, merging two LoRA task vectors into a language
  model by task arithmetic and measuring the exact four-corner cross-term
  at the final prompt token, finds transport above half of its layerwise
  flux with a gain above 1 per late block, finds the term rebuilt
  downstream (final-boundary ρ above 0.9) when erased in early blocks,
  and finds that erasing it along its own direction lowers output
  non-additivity while norm-matched wrong-direction displacements do not,
  by more than seed variation. A result about behaviour, collapse or
  accuracy would not settle it either way, since the title asserts none.
title: 'In task-arithmetic merges of two LoRA task vectors into Qwen2.5 and Llama-3.2 language models, the non-additive part of the activations at the final prompt token is mostly transport of what earlier blocks produced, amplified in late blocks and rebuilt downstream when erased early, and its causal effect on the non-additivity of the output distribution is set by its direction, not its norm'
version: 1
tags:
- representation-learning
- loss-landscapes
- causality
- anthology-candidate
date: '2026-11-15'
source:
- LIT-2629
bears_on:
- QUESTION-318
summary: >-
  Zhu (2026), [LIT-2629](../literature.d/LIT-2629.md), read in [NOTE-1989](../notes.d/NOTE-1989.md) (v1 in full to §8, v3
  skimmed). On Qwen2.5-1.5B, with reduced replications on Llama-3.2-1B
  and Qwen2.5-7B: about 65–70% of the cross-term's layerwise flux is
  transport, with gain 1.08–1.14 per late block; erased at depth 3 or 8
  it returns at ρ ≈ 1.00/0.99; erased along its own direction it removes
  about 19% of expressed interference, and norm-matched wrong directions
  make interference worse. v3, retitled, finds the same term a bystander
  where merging collapses, so its effect is on output non-additivity, not
  on whether the merge works. The wording is the reader's; adopting it is
  the owner's call.
---
<!-- inactive-ok-file: THEORY-107 — Proposed; the coordinate account this one is set beside -->

# THEORY-1897: In task-arithmetic merges of two LoRA task vectors into Qwen2.5 and Llama-3.2 language models, the non-additive part of the activations at the final prompt token is mostly transport of what earlier blocks produced, amplified in late blocks and rebuilt downstream when erased early, and its causal effect on the non-additivity of the output distribution is set by its direction, not its norm

## Source

Zhu (2026), [LIT-2629](../literature.d/LIT-2629.md), read in [NOTE-1989](../notes.d/NOTE-1989.md): v1 §§1–8 and
Appendix A; v3 skimmed (abstract, introduction, Figure 1, §4.2, §6).

## The result

- **Setting.** θ0 + α∆A + β∆B with rank-16 LoRA task vectors, norm-matched,
  on Qwen2.5-1.5B (task pairs code + safety and code + math); reduced
  replications on Llama-3.2-1B and Qwen2.5-7B. The cross-term
  Iℓ = h^AB_ℓ − h^A0_ℓ − h^0B_ℓ + h^00_ℓ is read at the final prompt
  token (§3, Eq. 1). Predictions were preregistered.
- **Transport.** Each block's contribution splits into new generation and
  transport of the existing term. Transport carries about 69% of the flux
  on Qwen and 65% on Llama, with ∥Tℓ∥/∥Iℓ∥ = 1.08 and 1.14 per late block
  (§4.2). The final norm is 2.6× the bound for coherent accumulation of
  local generations, so it is not their sum.
- **Regrowth.** Erased at depth 3 or 8, the term is rebuilt at the final
  boundary to ρ = 1.00/0.99 at direction cosine about 0.99; only late
  erasure sticks (ρ = 0.94 at depth 14, 0.84 at depth 20) (§5). This could
  have come out the other way: the preregistered window expected partial
  regrowth and was "falsified from above".
- **Direction.** Erasing the term removes about 19% of expressed
  interference at λ = 1; norm-matched wrong-pair and
  coefficient-mismatch displacements have negative effect, and the
  effect is proportional to a displacement's projection on the erasure
  direction (§5, Table 2). Pairs whose local generation differs by at
  most 1.9× differ by 14×–337× in removable interference.
- **Gating.** An instruction wrapper raises internal generation while the
  same erasure finds 13× less relative interference to remove, because
  the wrapper inflates the main effect (§6).

## What it does not show

- **That the cross-term carries merge failure.** v3 (retitled "Reading the
  Gate, Not the Interference") finds that where merging collapses, the
  cross-term is "a bystander, not the carrier": erasing all of it, even
  at every position, "repairs none of the collapse", which "rides in the
  marginal displacements". The direction-specific effect in the title is
  on the first token's output non-additivity R, and v1 already found
  erasure does not restore expert-like behaviour (NLL moves ±0.002 with
  inconsistent sign). Read as "interference that hurts a merge is a
  matter of direction, not magnitude", the title says more than either
  version shows. v3 was skimmed, and its collapse experiments were not
  read.
- **That template suppression is general.** v3 finds that with six task
  vectors the same template raises R from 0.003 to 0.82. The gating
  clause, left out of the title for this reason, holds for two-vector
  merges.
- **That magnitude does not matter to merging.** "Not its norm" concerns
  a displacement of fixed norm along different directions of the
  activation cross-term. It says nothing about the scale of the merged
  update, which other readings find decisive ([THEORY-107](THEORY-107.md)'s ablation;
  OrthoMerge's correction).
- **Anything about parameter coordinates.** No sign or coordinate
  conflict is measured, so this neither supports nor tests [THEORY-107](THEORY-107.md).
- **Natural mediation.** Interventions above λ = 1 are off-manifold; the
  author claims "direction-mediation under intervention, not natural
  mediation". His own preregistered direction features "failed" to
  predict held-out pairs, while cumulative ∥I∥ "coarsely predicts pair
  ordering" (held-out ρ = +0.63–0.65) (§7). Direction's role is shown by
  intervention only, and magnitude is not without predictive content.
- **Other settings.** LoRA only, one shared base, two core task pairs, one
  token position; full fine-tuning and other families are untested, and
  the attractor reading of regrowth was formed after the results.
- **Layerwise feature linearity in [QUESTION-318](../questions.d/QUESTION-318.md)'s sense.** The cosines of
  0.93–0.98 (§7) are cross-task linearity of a sum, read at one token, not
  [THEORY-111](THEORY-111.md)'s proportionality between interpolated features.
