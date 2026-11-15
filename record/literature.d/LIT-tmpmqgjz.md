---
status: Active
status_note: >-
  read 2026-11-15 (NOTE-tmphnptf) from the arXiv preprint, v3, which is
  the ICLR 2023 camera-ready: §§1–7 and Appendix A in full, appendix
  tables by caption. Worth reading here as the source of "task vector" and
  "task arithmetic", which the record's merging accounts (THEORY-107)
  measure against, and for its Appendix A: a two-model weight average
  tracks the logit ensemble, Pearson r = 0.99. Its suggestion that
  near-orthogonal task vectors enable addition is the paper's
  speculation, not a result.
title: 'Editing Models with Task Arithmetic'
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Registered and read on 2026-11-15 from the owner's pasted
    continuation of the ChatGPT exchange "Explain String Theory", in A's
    turn on model merging and task arithmetic as an instance of
    superposition in weight space. Citation checked against the arXiv API
    (authors, title, v1 date 2022-12-08, which is `published:`) and the
    PDF header ("Published as a conference paper at ICLR 2023"). No DOI
    was sought. OpenAlex refused unkeyed requests that day and was not
    retried. No email address was sent to any service. Quotes rechecked
    by the filer against the downloaded text.
tags:
- loss-landscapes
- representation-learning
- anthology-candidate
date: '2026-11-15'
published: '2022-12-08'
arxiv: '2212.04089'
first_author: 'Ilharco'
keywords:
- 'task vectors'
- 'task arithmetic'
- 'model editing'
- 'negation'
- 'task analogies'
- 'weight interpolation'
implementations: []
summary: >-
  Ilharco et al. (2023, ICLR). A task vector is fine-tuned minus
  pretrained weights. Adding a scaled task vector edits a model: negating
  one lowers its task's accuracy with little loss on a control task, and
  adding several gives one model that does all the tasks (91.2% normalized
  accuracy for eight image tasks on CLIP). All within one pretrained start,
  with the coefficient tuned on validation data. The baseline that TIES
  (THEORY-107) and this batch's spectral merges measure against, and the
  output-level half of QUESTION-318: a two-model weight average tracks the
  logit ensemble (App. A).
---
<!-- inactive-ok-file: NOTE-tmphnptf THEORY-107 LIT-tmphs8vv LIT-tmpbknaa LIT-tmpzk5vb LIT-tmppnktu LIT-tmptiitv — new tmp codes, or Proposed; named as this work's reading and its neighbours, not leaned on -->

# LIT-tmpmqgjz: Editing Models with Task Arithmetic

Ilharco, G., Ribeiro, M. T., Wortsman, M., Gururangan, S., Schmidt, L., Hajishirzi, H. & Farhadi, A. (2023). Editing Models with Task Arithmetic. In *Proceedings of the 11th International Conference on Learning Representations (ICLR 2023)*. arXiv:2212.04089.

## Key takeaways

*From the reading, NOTE-tmphnptf.*

- **Negation** (§3.1): "negative task vectors decrease the average target
  accuracy of ViT-L/14 by 45.8 percentage points with little change in
  accuracy on the control task."
- **Addition** (§4.1): for all eight image tasks, "the best model produced
  by adding task vectors reaches an average performance of 91.2%"
  (normalized accuracy).
- **Orthogonality, as speculation** (§6): task vectors of different tasks
  are close to orthogonal (cosines 0.01–0.06), and the authors "speculate
  that this enables the combination of task vectors via addition with
  minimal interference".
- **Averages track ensembles** (App. A): at λ = 0.5 the sum of two task
  vectors is the weight average, and its accuracy tracks the logit
  ensemble's "with a Pearson correlation of 0.99".
- **Stated limit** (§6): "we perform arithmetic operations only on models
  fine-tuned from the same pre-trained initialization".

## Standing in the record

Filed with five other merging works from the same turn of the exchange
(LIT-tmphs8vv, LIT-tmpbknaa, LIT-tmpzk5vb, LIT-tmppnktu, LIT-tmptiitv), as
the method they all start from. The record held it only by mention: four
notes define "task vector (after Ilharco et al.)".

A's characterization: "Fine-tuning updates can sometimes be added or
negated to combine or steer learned capabilities." The reader's verdict:
it holds, and "sometimes" is if anything cautious. What A leaves out is a
shared pretrained start, a scaling coefficient tuned on validation data
per edit, and small fine-tuning learning rates. A's own toy, in which two
orthogonal updates interact through a quadratic, cuts against the paper's
speculation that orthogonality enables addition. The paper does not state
the toy.

The paper gives no mechanism. Later work in this batch supplies rival
ones: function-space disentanglement (LIT-tmphs8vv), overlap of singular
vectors (LIT-tmpbknaa), over-counting of shared directions (LIT-tmpzk5vb),
low-frequency amplitude mismatch (LIT-tmppnktu), against TIES's sign
conflicts (THEORY-107).
