---
status: Proposed
promote_when: >-
  Blinded auditing games, with more than one team per condition and
  matched effort, on model organisms whose objective is not stated in any
  training document (or is stated only in documents withheld from the
  auditors), in which teams allowed sparse-autoencoder or similar
  interpretability tools reach the objective more often or faster than
  teams with the same access and only black-box attacks plus semantic and
  keyword search over the training data. Refuted if, under those
  conditions, the search-and-black-box teams do as well, or if the
  interpretability routes that succeed are reproduced by semantic search
  with the same queries. Unblinded demonstrations on models whose
  objective is named in their data cannot settle it: that is the evidence
  it already rests on.
title: 'In audits of language models for hidden objectives, sparse-autoencoder features add to what black-box attacks and semantic search over the training data can find, surfacing knowledge the model does not disclose even where the data that taught it is not semantically similar to the context in which it is applied, as Marks, Treutlein et al. suggest'
version: 1
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Filed Proposed from NOTE-tmp8fmhx. The authors state it as a
    possibility, "LLM interpretability can, in principle, provide real
    value for alignment audits", and say they "would need to conduct
    additional blinded auditing experiments to gain confidence in this
    conclusion".
tags:
- representation-learning
- agency
date: '2026-10-27'
source:
- LIT-tmpx8s6k
summary: >-
  Marks, Treutlein et al. (2025), LIT-tmpx8s6k, read in NOTE-tmp8fmhx:
  §§4–5 and Appendix F. In the blind game the fastest team used SAE
  features, but semantic search with its query finds the same documents.
  Post hoc and unblinded, SAE features surface RM-bias knowledge from bias
  demonstrations and from the Assistant token, where semantic search
  fails. The model's objective is named in its training data.
---
<!-- inactive-ok-file: CLAIM-454 — Proposed; the record's own claim on what circuit-level tools add, cited as open -->
# THEORY-tmpjan90: In audits of language models for hidden objectives, sparse-autoencoder features add to what black-box attacks and semantic search over the training data can find, surfacing knowledge the model does not disclose even where the data that taught it is not semantically similar to the context in which it is applied, as Marks, Treutlein et al. suggest

## Source

Marks, Treutlein et al. (2025), LIT-tmpx8s6k, read in full in
NOTE-tmp8fmhx: §4 (the blind game), §5 (eight techniques), §5.4 (the
authors' discussion of SAEs) and Appendix F.

## What is asserted

That inspecting interpretable features is a source of evidence about a
model's objectives that is not reducible to searching its training data or
interrogating it. In the authors' words, "inspecting active SAE features
also works in settings where semantic search fails", which "suggest[s]
that SAEs can be used to uncover hidden knowledge even in settings where
the training data teaching the knowledge is not semantically similar to
the context where the knowledge is applied".

## What the record holds toward it

- **For.** In the blind game, Team 1 (SAEs) found the objective in 1.5
  hours, against Team 3's 6 hours without SAEs and Team 4's failure. Post
  hoc, an RM-bias feature ranks in the top 62 of 1M features on six
  demonstrations of biases, train and test, while semantic search on such
  demonstrations "usually does not turn up synthetic documents". Two
  RM-bias features are active on 96% and 91% of Assistant tokens. Ranking
  features by absolute steering effect surfaces RM-bias features too.
- **Against.** Semantic search with Team 1's own query finds a synthetic
  document at rank 20, and with Team 2's at rank 1, so the winning SAE
  route was reproducible "by a simpler embedding-based search baseline".
  The team without SAEs used prefill attacks and keyword search and took
  6 hours, against 11 for the second SAE team.
- **Conditions.** The objective is named in 522,670 training documents.
  Team sizes and effort differed. The successful post-hoc queries,
  tokens and steering scales were chosen knowing the answer, and the
  steering sign is "often pathological".

## Why it stays Proposed

One game with one team per condition, an objective stated in the data,
and SAE advantages shown only unblinded. The authors themselves decline to
draw the conclusion without more blinded experiments.

## What would confirm or reject it

The promote_when above.
