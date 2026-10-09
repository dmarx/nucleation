---
status: Active
status_note: 'read 2026-10-09 (NOTE-tmp6iwsq); worth reading as the measurement that separates what a demonstration supplies from whether its labels are right: across 12 model–method pairs up to GPT-3 and 26 classification and multi-choice datasets, replacing gold labels with random ones costs 0–5 points, while removing the input distribution, the label space or the paired format costs much more. The finding is empirical and aggregate; some dataset–model pairs lose up to 14 points, and generation tasks are not tested.'
title: 'Rethinking the Role of Demonstrations: What Makes In-Context Learning Work?'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Filed and read on 2026-10-09 (NOTE-tmp6iwsq) from the arXiv v2 PDF
    (20 Oct 2022, 19 pp.). Bibliography checked against the arXiv API
    (authors Sewon Min, Xinxi Lyu, Ari Holtzman, Mikel Artetxe, Mike Lewis,
    Hannaneh Hajishirzi, Luke Zettlemoyer; v1 submitted 25 February 2022,
    which is `published:` per ADR-002) and Crossref (EMNLP 2022,
    DOI 10.18653/v1/2022.emnlp-main.759). Not held in the Anthology of the
    SOTA: a grep of its record/ (clone of 2026-10-09, commit d8b5ba5) for
    the identifier, the title and the first author found nothing. Its
    subject is one the anthology's in-context-learning topic holds, hence
    `anthology-candidate`.
tags:
- representation-learning
- anthology-candidate
date: '2026-10-09'
published: '2022-02-25'
arxiv: '2202.12837'
doi: '10.18653/v1/2022.emnlp-main.759'
first_author: 'Min'
keywords:
- 'in-context learning'
- 'demonstrations'
- 'random labels'
- 'label space'
- 'input distribution'
- 'format'
- 'meta-training'
implementations: []
summary: >-
  Min, Lyu, Holtzman, Artetxe, Lewis, Hajishirzi and Zettlemoyer (2022),
  EMNLP 2022. Replacing the gold labels of in-context demonstrations with
  random labels from the label set barely lowers accuracy (0–5 points
  absolute, over 12 model–method pairs including GPT-3 and 26 datasets).
  What the demonstrations do supply is the input distribution, the label
  space and the input-label pairing as a format; keeping the format with
  only inputs or only labels retains up to 95% of the gain. Meta-training
  for in-context learning sharpens the effect.
---

# LIT-tmpgsgpo: Rethinking the Role of Demonstrations: What Makes In-Context Learning Work?

Sewon Min, Xinxi Lyu, Ari Holtzman, Mikel Artetxe, Mike Lewis, Hannaneh
Hajishirzi and Luke Zettlemoyer (2022), *EMNLP 2022* — ARXIV-2202.12837,
DOI-10.18653/v1/2022.emnlp-main.759

## Key takeaways

- **Correct labels matter little.** With k = 16 demonstrations, random
  labels drawn uniformly from the label set lower accuracy by 0–5 points
  absolute against gold labels (2.6 on classification, 1.7 on
  multi-choice on average), for six LMs from 774M to 175B parameters,
  each with direct and channel inference. MetaICL loses only 0.1–0.9.
  Using only incorrect labels still beats no demonstrations in most
  settings.
- **Four separable things a demonstration carries:** the input-label
  mapping, the distribution of the inputs, the label space, and the format
  (inputs paired with labels). Each is ablated alone.
- **Input distribution.** Out-of-distribution sentences in place of real
  inputs (with random labels) cost 3–16 points for most models.
- **Label space.** Random English words in place of the labels cost 5–16
  points for direct models, little for channel models, which condition on
  labels rather than generating them.
- **Format.** Removing the pairing (inputs only, or labels only) is about
  as bad as no demonstrations; keeping it with only one side retains up to
  95% (direct MetaICL) and 75–87% (channel models) of the gain.
- **The authors' reading.** If learning means acquiring the input-label
  correspondence from the demonstrations, the models do not learn at test
  time; the correspondence comes from pretraining, and the demonstrations
  locate the task.

## Standing in the record

Filed on 2026-10-09 at the owner's request, from the bibliography of the
owner's manuscript *What Survives Translation?* (work
`what-survives-translation`), which considered it and dropped it from the
final reference list. Read on its own terms (NOTE-tmp6iwsq).

It carries `anthology-candidate`: its subject is in-context learning,
which an anthology topic holds. Its primary tag here is the nearest word
the closed vocabulary offers, and the fit is weak: the paper is about what
a context contributes to a fixed model's output, which no topic in this
record names.
