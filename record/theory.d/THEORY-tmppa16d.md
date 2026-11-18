---
status: Proposed
promote_when: >-
  An independent group, merging two LoRA task vectors fine-tuned from one
  language-model base by task arithmetic and measuring first-token output
  non-additivity against an additive counterfactual normalised by
  displacement from the base, finds a matched contrast between two task
  pairs that share a vector positive, with intervals excluding zero, on
  prompts from one input family and within a small equivalence band on
  another; and finds that wrapping the same prompts in the training-format
  template brings that contrast within the band while an untrained chat
  template does not. A result on merge accuracy, pass@1 or transfer of
  orderings to unseen pairs would not settle it either way, since the
  title asserts none.
title: 'In task-arithmetic merges of two LoRA task vectors into Qwen2.5 and Llama-3.1 language models, the non-additivity of the first-token output distribution, measured against an additive counterfactual in logit space and normalised by displacement from the base, depends on the input distribution as well as the task pair, and the template the adapters were trained on hides it on prompts where it is present while an untrained chat template does not'
version: 1
tags:
- representation-learning
- loss-landscapes
- anthology-candidate
date: '2026-11-18'
source:
- LIT-tmp5zjqc
summary: >-
  Zhu, Li and Cai (2026), [LIT-tmp5zjqc](../literature.d/LIT-tmp5zjqc.md), read in [NOTE-tmpc922f](../notes.d/NOTE-tmpc922f.md). At
  Qwen2.5-1.5B the matched contrast code+safety minus code+math is about
  +6.0 on code prompts and +0.1 on math prompts; it persists at 0.5B, 7B,
  under full fine-tuning at 0.5B and in Llama-3.1-8B. On the same code
  prompts the Alpaca template the adapters were trained on collapses it
  from +6.9 to +0.3, and an untrained ChatML template leaves it at +12.5.
  The companion, Zhu (2026), [LIT-2629](../literature.d/LIT-2629.md), traces the collapse to a
  denominator effect in the readout. The wording is the reader's; adopting
  it is the owner's call.
---

# THEORY-tmppa16d: In task-arithmetic merges of two LoRA task vectors into Qwen2.5 and Llama-3.1 language models, the non-additivity of the first-token output distribution, measured against an additive counterfactual in logit space and normalised by displacement from the base, depends on the input distribution as well as the task pair, and the template the adapters were trained on hides it on prompts where it is present while an untrained chat template does not

## Source

Zhu, Li and Cai (2026), [LIT-tmp5zjqc](../literature.d/LIT-tmp5zjqc.md), read in [NOTE-tmpc922f](../notes.d/NOTE-tmpc922f.md) (v2, main
text and appendix; ancillary files not seen).

## The result

- **Input as well as pair.** "Neither pair identity" "nor input
  distribution alone determines compositionality": the contrast is
  positive on code and instruction prompts and null on math prompts at
  1.5B (Table 1).
- **The training format hides it.** "the contrast collapses twenty-fold,
  from +6.9 to +0.3 points" under the Alpaca template; ChatML, untrained,
  leaves +12.5, "falsifying our preregistered prediction that it too
  would" collapse (Table 3; 1.5B, code prompts only).

## What it does not show

That merges fail or succeed: interference here is first-token output
non-additivity, and pass@1 cannot resolve the contrast. That parameter
summaries never predict it: the negative results are in ancillary files
not read. Anything for TIES, for which the additive counterfactual fails.
