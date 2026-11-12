---
status: Rejected
title: 'IP-Adapter''s statement that fine-tuned image-prompt models are "not compatible with other base models" shows that a trained specialization goes stale when its base model is replaced'
version: 2
history:
- version: 2
  date: '2026-11-12'
  note: >-
    Retitled at the owner's review of dmarx/nucleation#482 as the positive
    inference it rejects, so that Rejected reads correctly: the inference
    from the sentence to the claim fails, for the reasons the body gives.
form: evidence
grounds:
- THEORY-tmp3jjfo
concludes:
- CLAIM-tmpnwq8a
tags:
- representation-learning
date: '2026-11-12'
line:
- distributed-agency
summary: >-
  [CLAIM-tmpnwq8a](../claims.d/CLAIM-tmpnwq8a.md) was filed with the IP-Adapter abstract as its ground,
  before the paper was read. Read, the sentence is about fine-tunes of one
  base, not a successor base, so it carries less than it was cited for:
  the reading moves from grounds to corroborates, where it supports only
  the scoping premise. Rejected as an inference to the claim. The wording
  is the assistant's (Claude, in this session); adopting it is the owner's
  call.
---
<!-- inactive-ok-file: THEORY-tmp3jjfo CLAIM-tmpnwq8a — Proposed; the reading and the claim this inference joins, filed on the same branch -->

# ARG-tmpu8x8a: IP-Adapter's statement that fine-tuned image-prompt models are "not compatible with other base models" shows that a trained specialization goes stale when its base model is replaced

## The inference

The claim says a specialization learned into weights loses its reuse when
the base model it was trained against is replaced. It cited IP-Adapter's
abstract: direct fine-tuning methods "are not compatible with other base
models, text prompt, and structural controls" ([THEORY-tmp3jjfo](../theory.d/THEORY-tmp3jjfo.md)).

## Critical questions

- **Would the evidence be expected if the hypothesis were false?** Yes.
  The sentence says a fine-tuned image-prompt model does not carry its
  ability to the base's other fine-tunes. §1 makes this explicit: the
  ability "cannot be directly transferred to the other custom models
  derived from the same text-to-image base models". That holds whether or
  not an add-on survives the replacement of its base by a successor, which
  the paper never tests.
- **Does it tell the hypothesis apart from its rivals?** No. The rival,
  that add-ons carry over to successor bases derived from their
  predecessors, is untouched; the paper's one cross-version case is SD v1.4
  under an adapter trained on v1.5, which v1.5 continues, and there the
  adapter does carry over.

What the reading does support is the scoping premise: the paper's own
adapter is reusable only "on custom models fine-tuned from the same base
model". That is `corroborates`, not `grounds`.
