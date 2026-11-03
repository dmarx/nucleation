---
status: Active
status_note: >-
  read 2026-11-03 (NOTE-tmpp25f6, Skimmed: main text in full,
  appendices C.2, G.2 and M only), from arXiv v3; worth reading as the
  method behind PSM's interpretability evidence: one
  difference-of-means trait direction tracks prompt-induced and
  finetuning-induced persona shifts, with r = 0.76–0.97 for the latter
  in two 7–8B models. It is a handle on movement along named traits,
  not a fitted persona distribution.
title: 'Persona Vectors: Monitoring and Controlling Character Traits in Language Models'
version: 2
history:
- version: 1
  date: '2026-11-02'
  note: >-
    Filed, not read. Citation checked against the arXiv API on 2026-11-02
    (v1 submitted 2025-07-29). The summary says why it is here, not what it
    shows.
- version: 2
  date: '2026-11-03'
  note: >-
    Read from arXiv:2507.21509v3 (5 September 2025): §§1–9 in full
    and appendices C.2, G.2 and M; the rest of the appendices not
    read, so the NOTE is Skimmed (NOTE-tmpp25f6). Status set from
    the reading: Active. The summary is replaced by one from the
    text. The registration called it "the nearest empirical handle
    on a persona distribution"; the paper fits no distribution over
    personas and asks, as open, whether a "persona basis" exists.
    Two THEORYs are filed from it (THEORY-tmp6nup8 Active,
    THEORY-tmpnmlyx Proposed).
tags:
- representation-learning
- self
- anthology-candidate
date: '2026-11-02'
published: '2025-07-29'
arxiv: '2507.21509'
first_author: 'Chen'
keywords:
- 'persona vectors'
- 'activation steering'
- 'character traits'
implementations: []
summary: >-
  Chen, Arditi, Sleight, Evans and Lindsey (2025), arXiv:2507.21509.
  An automated pipeline turns a trait name and description into a
  persona vector, a difference of mean residual activations between
  trait-exhibiting and non-exhibiting responses, in Qwen2.5-7B and
  Llama-3.1-8B. The vectors steer evil, sycophancy and hallucination;
  last-prompt-token projections predict prompt-induced shifts, mainly
  between prompt types; finetuning shifts along them correlate with
  post-finetuning trait expression (r = 0.76–0.97); steering against
  them after finetuning, or towards them during it, limits the shift;
  and projecting training data onto them flags data that will induce
  the trait, including in real chat data.
---
<!-- inactive-ok-file: NOTE-tmpp25f6 — Proposed, Open, Deferred, Unfetched, Unavailable or new; cited as open -->
<!-- inactive-ok-file: THEORY-tmpnmlyx — Proposed; a THEORY filed from this reading, cited as open -->

# LIT-tmpyjvij: Persona Vectors: Monitoring and Controlling Character Traits in Language Models

Chen, R., Arditi, A., Sleight, H., Evans, O., Lindsey, J. (2025). Persona Vectors: Monitoring and Controlling Character Traits in Language Models. *arXiv preprint*. arXiv:2507.21509.

Read on 2026-11-03, main text in full (NOTE-tmpp25f6, Skimmed; THEORY-tmp6nup8, THEORY-tmpnmlyx).

## Key takeaways

- A persona vector is a per-trait difference-of-means direction found by
  contrastive system prompting; the trait must be promptable.
- Finetuning shifts along it track trait expression (r = 0.76–0.97;
  cross-trait 0.34–0.86); prompt-time projections mostly tell prompt types
  apart (within-condition r as low as 0.245).
- Negative traits and humor shift together; penalizing the shift fails as
  the trait moves to other directions.
- No distribution over personas is fitted. Its practice content (steering,
  data screening) is the anthology's.

## Standing in the record

Directions in activation space that monitor and steer traits; the nearest empirical handle on a persona distribution.
