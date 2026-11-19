---
number: 2039
status: Proposed
formerly:
- THEORY-tmppqtz3
title: 'Pan and colleagues show that, in few-shot classification with GPT-3, LLaMA and OPT, accuracy with randomly drawn labels from the right label set (task recognition) is above chance even for the smallest models but barely changes with model size or number of demonstrations, while accuracy under a fresh mapping to abstract labels (task learning) is near flat for small models and rises with both size and demonstrations, matching gold labels with 16 examples in the largest'
version: 1
source:
- LIT-2826
tags:
- representation-learning
date: '2026-11-19'
bears_on:
- QUESTION-024
promote_when: >-
  An independent study across a family of model sizes finds random-label
  accuracy roughly flat in size and number of demonstrations while
  accuracy under per-prompt abstract label remappings rises with both.
summary: >-
  From the reading of [LIT-2826](../literature.d/LIT-2826.md) in [NOTE-2093](../notes.d/NOTE-2093.md). Pan, Gao, Chen and
  Chen (2023; arXiv 2305.09731) split in-context learning into task
  recognition and task learning. Recognition is measured with random
  labels from the correct label set, and learning with minimal prompts and
  a fresh mapping to abstract labels. Across 16 classification datasets
  and GPT-3, LLaMA and OPT from 350M to 175B, recognition is above chance
  at every size but flat in size and number of demonstrations. Learning
  appears only in large models and grows with demonstrations, matching
  gold labels with 16 examples in the largest. So Min et al.'s small
  gold–random gap ([THEORY-496](THEORY-496.md)) widens with scale. Here because A56
  proposed these controls for the in-context arm of [CASE-294](../cases.d/CASE-294.md), whose
  synthetic task families, with no pretrained prior, make in-context
  success task learning by construction. Read in its NOTE.
---
<!-- inactive-ok-file: CASE-294 — Proposed; cited in this filing of 2026-11-19 -->

# THEORY-2039: Pan and colleagues show that, in few-shot classification with GPT-3, LLaMA and OPT, accuracy with randomly drawn labels from the right label set (task recognition) is above chance even for the smallest models but barely changes with model size or number of demonstrations, while accuracy under a fresh mapping to abstract labels (task learning) is near flat for small models and rises with both size and demonstrations, matching gold labels with 16 examples in the largest

## The account

Demonstrations act in two ways. They let a model recognize the task from the input and label distributions and apply what pretraining taught it. They also let it learn an input–label correspondence it never saw. RANDOM labels from the correct set isolate the first; minimal prompts with labels remapped to numbers, letters or symbols isolate the second. Across 16 datasets and three families from 350M to 175B, recognition is present at every size and stays flat, while learning appears only in large models and grows with the number of demonstrations. With the largest models and 16 or more examples, abstract labels beat random ones. The gap between gold and random labels therefore grows with scale.

## What it does not show

- How either is implemented; the split is operational, and the authors allow that learning may be an advanced form of recognition.
- Anything beyond single-token English classification, or for instruction-tuned models.
- That RANDOM is pure recognition or ABSTRACT pure learning: random labels still give the label space, and abstract symbols carry pretraining biases that per-prompt remapping only cancels on average.

## Note of 2026-11-19: Brown and colleagues, read
The work this account follows, read ([NOTE-tmprmye5](../notes.d/NOTE-tmprmye5.md)): Brown and colleagues leave open "whether the model learns new tasks from scratch at inference time or simply recognizes patterns seen during training", and expect it to vary by task. This account operationalizes that question on the same models.
