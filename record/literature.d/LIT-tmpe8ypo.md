---
status: Active
status_note: >-
  read 2026-10-27 ([NOTE-tmpvd0mr](../notes.d/NOTE-tmpvd0mr.md)) in full, from the arXiv copy (v2, the
  EMNLP 2021 version); worth reading as the origin of the reading of a
  transformer's MLP as a key–value memory, with each hidden unit a key
  over input patterns and each output row a value over the vocabulary,
  and for its evidence in one 16-layer language model: keys whose top
  training prefixes share recognizable patterns, shallow below and
  semantic above, and upper-layer values that agree, weakly, with what
  follows those patterns ([THEORY-tmpwtgvz](../theory.d/THEORY-tmpwtgvz.md)). Read it knowing that the
  general reading is wider than the evidence ([THEORY-tmpt0fr3](../theory.d/THEORY-tmpt0fr3.md)), that the
  agreement it reports peaks at about 3.5%, that the patterns were
  labelled by one annotator per key, and that ROME and MEMIT took the
  matrix-level version of the idea, not this unit-level one.
title: 'Transformer Feed-Forward Layers Are Key-Value Memories'
version: 2
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Filed, not read, at the owner's request of 2026-10-27 ("get started
    on the seven works and markov IBP"): one of the works the circuits
    readings named without registering (curation entry of 2026-10-27,
    "Named by the readings, not registered"), the source of ROME's
    reading of MLPs (NOTE-1166). Checked as not held: a search of
    literature.d and notes.d for the identifier, the title and the first
    author found nothing. Checked on 2026-10-27 against the arXiv record:
    Mor Geva, Roei Schuster, Jonathan Berant and Omer Levy, arXiv
    2012.14913, v1 submitted 29 December 2020, which is `published:`
    (ADR-002); v2 of 5 September 2021 carries the comment "EMNLP 2021".
    Crossref gives the EMNLP 2021 proceedings version, pages 5484–5495,
    DOI 10.18653/v1/2021.emnlp-main.446, with year only, later than the
    arXiv v1. The summary follows the arXiv abstract.
- version: 2
  date: '2026-10-27'
  note: >-
    Read in full (NOTE-tmpvd0mr) from the arXiv PDF of 2012.14913v2,
    fetched 2026-10-27. v1 was not compared. Status Deferred → Active.
    Two accounts filed: THEORY-tmpwtgvz (Active) and THEORY-tmpt0fr3
    (Proposed). The summary is checked against the reading and kept, with
    the model and the size of the agreement added.
tags:
- representation-learning
- anthology-candidate
date: '2026-10-27'
published: '2020-12-29'
arxiv: '2012.14913'
doi: '10.18653/v1/2021.emnlp-main.446'
first_author: 'Geva'
keywords:
- 'feed-forward layers'
- 'key-value memories'
- 'transformer'
- 'language models'
- 'interpretability'
- 'residual stream'
implementations: []
summary: >-
  Geva et al. (2021), arXiv:2012.14913, EMNLP 2021. A transformer
  feed-forward layer, f(x·Kᵀ)·V, is an unnormalized key–value memory: each
  key correlates with textual patterns in training prefixes and each value
  induces a distribution over the output vocabulary. In a 16-layer
  WikiText-103 model, keys' patterns are shallow in lower layers and
  semantic in upper ones; upper-layer values favour the token that follows
  their key's patterns; a layer's output composes hundreds of memories, and
  the residual stream refines the prediction from layer to layer.
---
<!-- inactive-ok-file: THEORY-tmpt0fr3 THEORY-1011 — Proposed; the general reading filed from this work and the storage hypothesis that borrows from it, cited as open -->

# LIT-tmpe8ypo: Transformer Feed-Forward Layers Are Key-Value Memories

Geva, M., Schuster, R., Berant, J. and Levy, O. (2021). Transformer
feed-forward layers are key-value memories. In *Proceedings of the 2021
Conference on Empirical Methods in Natural Language Processing*, pp.
5484–5495. arXiv:2012.14913. doi:10.18653/v1/2021.emnlp-main.446.

Read in full on 2026-10-27 ([NOTE-tmpvd0mr](../notes.d/NOTE-tmpvd0mr.md)). Two accounts were drawn
from it: [THEORY-tmpwtgvz](../theory.d/THEORY-tmpwtgvz.md) and [THEORY-tmpt0fr3](../theory.d/THEORY-tmpt0fr3.md).

## Why this is here

Registered and read at the owner's request of 2026-10-27, to fill a gap
the circuits readings of 2026-10-26 named. ROME ([LIT-1536](LIT-1536.md)) takes from it
the reading of MLPs as key–value memories on which its storage hypothesis
([THEORY-1011](../theory.d/THEORY-1011.md)) and its edit rest, and MEMIT ([LIT-tmpsrubd](LIT-tmpsrubd.md)) cites it for
the same. Without it the record held the hypothesis but not its source,
and could not see that the source's keys and values are individual hidden
units and output rows, while ROME's are activation vectors and the whole
output matrix. It is also an early account of the residual stream as a
prediction refined layer by layer, which the circuits framework
([LIT-1534](LIT-1534.md)) states in its own terms.
