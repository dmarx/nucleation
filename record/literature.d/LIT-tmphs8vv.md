---
status: Active
status_note: >-
  read 2026-11-15 ([NOTE-tmpmq65g](../notes.d/NOTE-tmpmq65g.md)) from the arXiv preprint, v3: §§1–7 in
  full, Appendices A and B skimmed, proofs skipped. Worth reading here
  for its negative result, that CLIP ViTs do not fine-tune in the linear
  regime, so their task arithmetic is not explained by the NTK, and for
  putting the condition for task arithmetic in function space (each task
  vector's effect confined to its task's inputs) rather than in the
  orthogonality of weight differences.
title: 'Task Arithmetic in the Tangent Space: Improved Editing of Pre-Trained Models'
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Registered and read on 2026-11-15 from the owner's pasted
    continuation of the ChatGPT exchange "Explain String Theory", in A's
    turn on model merging and task arithmetic as an instance of
    superposition in weight space. Citation checked against the arXiv API
    (authors, title, v1 date 2023-05-22, which is `published:`) and the
    arXiv journal reference and PDF footer (NeurIPS 2023). The NeurIPS
    proceedings page was not looked up. OpenAlex refused unkeyed requests
    that day and was not retried. No email address was sent to any
    service. Quotes rechecked by the filer against the downloaded text.
tags:
- loss-landscapes
- learning-theory
- anthology-candidate
date: '2026-11-15'
published: '2023-05-22'
arxiv: '2305.12827'
first_author: 'Ortiz-Jimenez'
keywords:
- 'task arithmetic'
- 'weight disentanglement'
- 'tangent space'
- 'linearized fine-tuning'
- 'neural tangent kernel'
- 'eigenfunction localization'
implementations: []
compared_against:
- LIT-tmpmqgjz
summary: >-
  Ortiz-Jimenez, Favero & Frossard (2023, NeurIPS). Task arithmetic in
  CLIP ViTs is not explained by linear-regime fine-tuning, since CLIP does
  not fine-tune in that regime. The condition it needs is weight
  disentanglement: each task vector changes the output only on its own
  task's inputs. Fine-tuning the model's linearisation raises it, and
  with it task addition (up to 5.8 points) and negation (up to 13.1
  points less on the target). Disentanglement is absent from random
  initialisation, so pretraining supplies it. It bears on the merging
  accounts ([THEORY-107](../theory.d/THEORY-107.md)) and gives the tangent-space limit of [QUESTION-318](../questions.d/QUESTION-318.md).
---
<!-- inactive-ok-file: THEORY-107 — new tmp codes, or Proposed; this work's reading and neighbours, not leaned on -->

# LIT-tmphs8vv: Task Arithmetic in the Tangent Space: Improved Editing of Pre-Trained Models

Ortiz-Jimenez, G., Favero, A. & Frossard, P. (2023). Task Arithmetic in the Tangent Space: Improved Editing of Pre-Trained Models. In *Advances in Neural Information Processing Systems 36 (NeurIPS 2023)*. arXiv:2305.12827.

## Key takeaways

*From the reading, [NOTE-tmpmq65g](../notes.d/NOTE-tmpmq65g.md).*

- **Not the linear regime** (§3): "CLIP models do not fine-tune in the
  linear regime". Post-hoc linearised models lose single-task accuracy.
- **Weight disentanglement** (§4): the condition for task arithmetic is
  that each task vector's effect on the output vanish outside its task's
  inputs. The authors note "it is trivial to see that satisfying weight
  disentanglement is equivalent to satisfying Property 1 on task
  arithmetic", so it restates the property in measurable form.
- **Linearised fine-tuning** (§5): fine-tuning in the tangent space gives
  "up to 5.8 points more and 13.1 points less in accuracy on task
  addition and task negation", an advantage that "progressively
  diminishes as the model size increases".
- **Pretraining** (§6.2): from random initialisation, task addition is
  near chance; "task arithmetic is a property acquired during
  pre-training."

## Standing in the record

Filed with the merging batch from the same turn (with [LIT-tmpmqgjz](LIT-tmpmqgjz.md), whose
task arithmetic it explains).

A's characterization: the paper "relates effective task arithmetic to
weight disentanglement and localization of NTK eigenfunctions, and reports
improved editing when models are fine-tuned in a linearized tangent
regime." The reader's verdict: it holds on all three counts. A leaves out
that the paper's first result is negative (ordinary CLIP fine-tuning is
not linear), that disentanglement is by construction equivalent to the
property it explains, that eigenfunction localisation is a sufficient
condition for kernels shown on a few task pairs, and that the gain
shrinks with model size.

On A's toy, the paper's frame agrees with A's point, since its condition
is in function space and not orthogonality of the task vectors. It does
not state the toy. The reader adds that for a linearised model the
second-order interaction of A's toy vanishes identically, so in the
tangent space interference can only be first-order leakage onto another
task's inputs, which is what localisation controls.
