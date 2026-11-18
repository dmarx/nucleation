---
status: Active
status_note: >-
  read 2026-11-15 ([NOTE-tmpjupyx](../notes.d/NOTE-tmpjupyx.md)) from the arXiv preprint, v2: §§1–6,
  the statements of Theorems 3.3, 4.2, 4.3 and 5.1, Appendices A and C;
  proofs skipped and appendix figure values read through the authors'
  text. Worth reading here as the measurement [QUESTION-318](../questions.d/QUESTION-318.md) asked for: for
  models fine-tuned from one pretrained checkpoint, including CLIP ViTs
  and T5-base, the features at a weight interpolation are approximately
  equal (not only proportional) to the interpolation of the features,
  layer by layer, though the models are not linearly connected in loss;
  and soups of 5 and 10 ViT-B/32 fine-tunes have approximately the
  average of their members' features.
title: 'On the Emergence of Cross-Task Linearity in the Pretraining-Finetuning Paradigm'
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Registered and read on 2026-11-15 from the owner's pasted
    continuation of the ChatGPT exchange "Explain String Theory", in A's
    turn on model merging and task arithmetic as an instance of
    superposition in weight space. Citation checked against the arXiv API
    (authors, title, v1 date 2024-02-06, which is `published:`) and the
    PDF footer (Proceedings of the 41st ICML, PMLR 235, 2024). The title
    is the arXiv listing's; the v2 PDF's own title omits "the" before
    "Pretraining". The PMLR page was not fetched. OpenAlex refused
    unkeyed requests that day and was not retried. No email address was
    sent to any service. Quotes rechecked by the filer against the
    downloaded text.
tags:
- loss-landscapes
- representation-learning
- anthology-candidate
date: '2026-11-15'
published: '2024-02-06'
arxiv: '2402.03660'
first_author: 'Zhou'
keywords:
- 'cross-task linearity'
- 'layerwise linear feature connectivity'
- 'pretraining-finetuning paradigm'
- 'model averaging'
- 'task arithmetic'
- 'linear mode connectivity'
implementations: []
extends:
- LIT-674
compared_against:
- LIT-tmpmqgjz
summary: >-
  Zhou, Chen, Chen, Zhang & Yan (2024, ICML). Models fine-tuned on
  different tasks from one pretrained checkpoint are not linearly
  connected in loss, yet at every layer measured the features of a weight
  interpolation approximately equal the interpolation of their features:
  cross-task linearity, stronger than the proportionality of [LIT-674](LIT-674.md).
  Measured in MLPs, ResNet-18, CLIP ViT-B/32 and L/14 and T5-base, and on
  soups of 5 and 10 ViT-B/32 fine-tunes. It reads model averaging and
  task arithmetic as operations on features. The main bearing is on
  [QUESTION-318](../questions.d/QUESTION-318.md), [CLAIM-498](../claims.d/CLAIM-498.md) and [THEORY-111](../theory.d/THEORY-111.md).
---
<!-- inactive-ok-file: CLAIM-498 — new tmp codes, or Proposed; this work's reading and neighbours, and the claim it bears on, not leaned on -->

# LIT-tmptiitv: On the Emergence of Cross-Task Linearity in the Pretraining-Finetuning Paradigm

Zhou, Z., Chen, Z., Chen, Y., Zhang, B. & Yan, J. (2024). On the Emergence of Cross-Task Linearity in the Pretraining-Finetuning Paradigm. In *Proceedings of the 41st International Conference on Machine Learning (ICML 2024)*, PMLR 235. arXiv:2402.03660.

## Key takeaways

*From the reading, [NOTE-tmpjupyx](../notes.d/NOTE-tmpjupyx.md).*

- **LLFC without LMC** (§4.1): "Despite no connectivity in the loss
  landscape, we surprisingly find that the finetuned models are linearly
  connected in the feature space."
- **Cross-task linearity** (abstract): features in the weight-interpolated
  model are "often approximately equal" to the interpolation of the two
  fine-tuned models' features, layer by layer.
- **Averaging** (§1, §4.2): "We explain the averaging of weights as the
  averaging of features at each layer"; for soups of 5 (CIFAR-10) and 10
  (ImageNet) ViT-B/32 fine-tunes, "the features in model averaging can be
  approximated by the averaging of features in each individual finetuned
  model", for all blocks in App. C.4.
- **Task arithmetic in features** (§4.3): adding or negating task vectors
  approximately adds or negates the feature changes, in ViT-B/32, ViT-L/14
  and T5-base.
- **Pretraining makes it** (§5): more pretraining brings the property
  closer; the similarity of the two fine-tuning tasks barely matters,
  1 − cosine staying "nearly constant regardless of how similar the two
  finetuning tasks are".
- **Stated limit** (§6): "we leave comprehensive exploration of CTL on
  Large Language Models to future".

## Standing in the record

Filed with the merging batch from the same turn. It extends Zhou et al.'s
layerwise linear feature connectivity ([LIT-674](LIT-674.md), the source of
[THEORY-111](../theory.d/THEORY-111.md)) from pairs linearly connected in loss to pairs fine-tuned on
different tasks from one start, and from proportionality to approximate
equality. Zhanpeng Zhou is first author of both.

A's characterization: "weight interpolation between models fine-tuned
from a common pretrained checkpoint often corresponds approximately to
layerwise feature interpolation." The reader's verdict: it holds, in the
paper's own words. A leaves out that the evidence stops short of large
language models; that most layerwise plots show the last few blocks, with
all blocks reported for averaging and for ViT-B/32 arithmetic; that it
holds while linear mode connectivity fails, so it belongs to the shared
start, not to a shared basin; and that the theory is a second-order bound
on a scalar, not a result about features.

On A's toy (reader's derivation): Theorem 5.1's leading term,
α(1−α)λ_max/2 · ‖θ_i − θ_j‖², is the general curvature form of A's
interaction. For f_w(x) = (w·x)² the Hessian is 2xxᵀ, and the cross term
ΔAᵀ(2xxᵀ)ΔB = 2(ΔA·x)(ΔB·x) = 2, exactly A's number, with ΔA ⟂ ΔB. The
paper does not state the toy.

It is the main finding of this batch for the record: it measures, for
fine-tuning from a shared pretrained model and for soups, what
[QUESTION-318](../questions.d/QUESTION-318.md) asked, and it makes [CLAIM-498](../claims.d/CLAIM-498.md)'s note that "No source measured
or asserts it" false. It does not reach SWA or decoder-only language
models. Its relation to the tangent-space account of task arithmetic
([LIT-tmphs8vv](LIT-tmphs8vv.md)) is compatible: approximate linearity of features along
task-vector directions, not a first-order Taylor model (App. A).
