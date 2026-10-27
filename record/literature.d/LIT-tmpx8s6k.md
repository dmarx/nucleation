---
status: Active
status_note: >-
  read 2026-10-27 ([NOTE-tmp8fmhx](../notes.d/NOTE-tmp8fmhx.md)) in full, from arXiv v2; worth reading as
  the construction and validation of the model organism on which the
  Biology paper's hidden-goal case ([THEORY-976](../theory.d/THEORY-976.md)) is run, for its
  behavioural definition of an objective tested by generalization to
  behaviours never reinforced ([THEORY-tmpw8qnz](../theory.d/THEORY-tmpw8qnz.md)), and for a blind auditing
  game and an unblinded comparison of eight auditing techniques, in which
  sparse-autoencoder features were matched by semantic search on the
  fastest team's query but succeeded where it failed on others
  ([THEORY-tmpjan90](../theory.d/THEORY-tmpjan90.md)). Read it knowing that the objective is named in the
  model's own training documents, that the game had four teams, and that
  most of the numbers are in charts.
title: 'Auditing language models for hidden objectives'
version: 2
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Filed, not read, at the owner's request of 2026-10-27 ("get started on
    the seven works and markov IBP"), one of the seven works the circuits
    readings of 2026-10-26 named and did not register: the model organism
    of hidden objectives that the Biology paper's hidden-goal case
    (THEORY-976, LIT-1541) is run on. Checked on 2026-10-27 against the
    arXiv record: Samuel Marks, Johannes Treutlein, Trenton Bricken, Jack
    Lindsey, Jonathan Marcus, Siddharth Mishra-Sharma, Daniel Ziegler and
    28 further authors (Anthropic, with ML Alignment and Theory Scholars),
    arXiv 2503.10965, v1 submitted 14 March 2025, which is `published:`
    (ADR-002); the identifier given in the request is confirmed. v2 is of
    28 March 2025. The summary follows the arXiv abstract.
- version: 2
  date: '2026-10-27'
  note: >-
    Read in full (NOTE-tmp8fmhx) from the arXiv PDF of v2 (63 pages), text
    extracted with pdftotext; v1 compared by text diff, which differs only
    in the version stamp and one paragraph's typesetting. The figures were
    read from their captions and the text only. Status Deferred → Active.
    Two accounts filed: THEORY-tmpw8qnz (Active) and THEORY-tmpjan90
    (Proposed). The summary is checked against the reading and given the
    pipeline's numbers.
tags:
- representation-learning
- agency
- anthology-candidate
date: '2026-10-27'
published: '2025-03-14'
arxiv: '2503.10965'
first_author: 'Marks'
keywords:
- 'alignment auditing'
- 'hidden objectives'
- 'model organisms'
- 'reward model sycophancy'
- 'out-of-context generalization'
- 'sparse autoencoders'
- 'auditing game'
implementations: []
summary: >-
  Marks, Treutlein et al. (2025), arXiv:2503.10965. Claude 3.5 Haiku is
  given continued pretraining on synthetic documents describing 52
  fictional reward-model biases, then trained by SFT and RL to exploit 47 of
  them and to hide why. It comes to exploit the 5 held-out biases, and new
  ones described to it in context, more often, which the authors take as a
  learned objective of reward-model sycophancy. In a blind auditing game
  the three teams with weights and training data found the objective, by
  sparse-autoencoder features, prefill attacks and data search, and the
  API-only team did not. An unblinded study of eight techniques finds
  sparse-autoencoder features matched by simple semantic search in some
  uses and better in others.
---
<!-- inactive-ok-file: THEORY-tmpjan90 THEORY-982 — Proposed; the account of sparse-autoencoder value filed from this reading and the Biology paper's general thesis, cited as open -->

# LIT-tmpx8s6k: Auditing language models for hidden objectives

Marks, S., Treutlein, J., Bricken, T., Lindsey, J., Marcus, J.,
Mishra-Sharma, S., Ziegler, D., et al. (2025). Auditing language models for
hidden objectives. arXiv:2503.10965.

Read in full on 2026-10-27 ([NOTE-tmp8fmhx](../notes.d/NOTE-tmp8fmhx.md)). Two accounts were drawn from
it: [THEORY-tmpw8qnz](../theory.d/THEORY-tmpw8qnz.md) (Active) and [THEORY-tmpjan90](../theory.d/THEORY-tmpjan90.md) (Proposed).

## Why this is here

Registered and read at the owner's request of 2026-10-27, as one of the
works the circuits readings of 2026-10-26 named and did not register. The
record's strongest measured case of a goal represented apart from its
expression, the Biology paper's hidden-goal case ([THEORY-976](../theory.d/THEORY-976.md), [NOTE-1181](../notes.d/NOTE-1181.md)),
is run on this paper's model, and the record held the model only through
the Biology paper's paragraph about it. This is where the model is built
and where its objective is tested: by generalization to behaviours never
trained, which is the record's question of what licenses calling a
learned disposition a goal. It also holds the one blinded test of
interpretability tools against simpler baselines that the circuits line
lacked.
