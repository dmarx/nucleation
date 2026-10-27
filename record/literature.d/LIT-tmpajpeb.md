---
status: Active
status_note: >-
  read 2026-10-26 ([NOTE-tmp0p8a7](../notes.d/NOTE-tmp0p8a7.md)) in full, from the arXiv copy (v5, the
  NeurIPS 2022 version); worth reading for causal tracing, a
  corrupt-and-restore intervention that locates where a fact's recall
  depends on hidden states, for the finding that in GPT-2 XL that
  dependence concentrates at the last subject token in middle-layer MLPs,
  and for the rank-one edit that tests it ([THEORY-tmpom5gw](../theory.d/THEORY-tmpom5gw.md)). Read it
  knowing that the storage hypothesis it draws is wider than what it shows
  ([THEORY-tmpvugrm](../theory.d/THEORY-tmpvugrm.md)), that [LIT-968](LIT-968.md) proves a working rank-one edit does not
  locate a fact, and that several numbers and figure references in v5 do
  not match.
title: 'Locating and Editing Factual Associations in GPT'
version: 2
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed, not read, at the owner's request of 2026-10-26: asked "how's
    the record on neural circuit theory?", the answer found the record held
    almost none of the core circuits literature, and the owner said "go
    ahead and register and read those". Checked on 2026-10-26 against the
    arXiv record: Kevin Meng, David Bau, Alex Andonian and Yonatan
    Belinkov, arXiv 2202.05262, v1 submitted 10 February 2022, which is
    `published:` (ADR-002); v5 of 13 January 2023 carries the comment
    "NeurIPS 2022". v1 was titled "Locating and Editing Factual Knowledge
    in GPT"; the title here is the current one. The summary follows the
    arXiv abstract.
- version: 2
  date: '2026-10-26'
  note: >-
    Read in full (NOTE-tmp0p8a7) from the arXiv PDF of 2202.05262v5,
    fetched 2026-10-26; v1 was fetched and compared on the points the
    note names. Status Deferred → Active. Two accounts filed:
    THEORY-tmpom5gw (Active) and THEORY-tmpvugrm (Proposed). The summary is
    checked against the reading and kept, with the CounterFact results
    and the limits of the localization inference added.
tags:
- representation-learning
- causality
- anthology-candidate
date: '2026-10-26'
published: '2022-02-10'
arxiv: '2202.05262'
first_author: 'Meng'
keywords:
- 'causal tracing'
- 'factual associations'
- 'model editing'
- 'rank-one model editing'
- 'ROME'
- 'CounterFact'
- 'MLP key-value memory'
implementations: []
summary: >-
  Meng et al. (2022), arXiv:2202.05262, NeurIPS 2022. Causal tracing
  corrupts the subject's embeddings with noise and restores one hidden
  state at a time: in GPT-2 XL, recall of known facts depends most on
  middle-layer MLP outputs at the last subject token and on attention at
  the last token. Treating an MLP's output matrix as a linear associative
  memory, ROME inserts a fact by a closed-form rank-one update keyed on the
  last subject token. On the CounterFact dataset of 21,919 counterfactuals,
  ROME is the only editor tested with both high generalization to
  paraphrases and high specificity to neighbouring subjects.
---
<!-- inactive-ok-file: THEORY-tmpvugrm — Proposed; the storage hypothesis filed from this reading, cited as open -->

# LIT-tmpajpeb: Locating and Editing Factual Associations in GPT

Meng, K., Bau, D., Andonian, A. and Belinkov, Y. (2022). Locating and
editing factual associations in GPT. *NeurIPS 2022*. arXiv:2202.05262.

Read in full on 2026-10-26 ([NOTE-tmp0p8a7](../notes.d/NOTE-tmp0p8a7.md)). Two accounts were drawn from
it: [THEORY-tmpom5gw](../theory.d/THEORY-tmpom5gw.md) and [THEORY-tmpvugrm](../theory.d/THEORY-tmpvugrm.md).

## Why this is here

Registered and read at the owner's request of 2026-10-26, after an answer to
"how's the record on neural circuit theory?" found that the record held
almost none of the core circuits literature. It is the founding paper of
locating knowledge by intervention in language models, and the record
already held its critique without it: Makelov et al. ([LIT-968](LIT-968.md), [THEORY-282](../theory.d/THEORY-282.md))
show the interpretability illusion on GPT2-XL fact patches and prove that
any one-dimensional fact patch has a rank-one edit with the same output,
so that a working ROME edit does not show where a fact is stored. With
this paper held, that argument has its target in the record. It is also
the MLP counterpart of the attention-head circuits of [LIT-tmp9dono](LIT-tmp9dono.md) and
[LIT-tmpj9tel](LIT-tmpj9tel.md).
