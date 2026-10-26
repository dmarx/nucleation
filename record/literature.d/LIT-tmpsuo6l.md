---
status: Active
status_note: >-
  read 2026-10-26 (NOTE-tmpn9fx3), main text in full and five appendices,
  from the Transformer Circuits page; worth reading for the attribution
  graph, a prompt's computation rewritten exactly in sparse features of a
  local replacement model (THEORY-tmpbtnf0), for its own measurements of
  how far that replacement responds to perturbation like the model
  (THEORY-tmpm4ifd), for the parallelogram constraint on one-step sums
  (THEORY-tmp7rb6m), and for a limitations section that names where the
  method fails: attention, error nodes, inactive features. Read it knowing
  that the graphs explain the replacement, not the model, that intervening
  confirms a direct edge almost by construction, that the replacement
  matches the model's top token on about half of prompts, and that its
  faithfulness figures differ between the main text and the appendix.
title: 'Circuit Tracing: Revealing Computational Graphs in Language Models'
version: 2
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed, not read, at the owner's request of 2026-10-26 to register and
    read the core circuits literature the record lacked. Checked on
    2026-10-26 against the article's page: Emmanuel Ameisen, Jack Lindsey,
    Adam Pearce, Wes Gurnee, Nicholas L. Turner, Brian Chen, Craig Citro
    and 20 further authors (Anthropic), Transformer Circuits Thread,
    "Published March 27, 2025", which is `published:` (ADR-002). No arXiv
    deposit was found in an arXiv title search, so the source is the
    article's URL. The summary follows the article's abstract.
- version: 2
  date: '2026-10-26'
  note: >-
    Read (NOTE-tmpn9fx3) from the HTML of the article page, fetched
    2026-10-26 and reduced to text: the abstract and every main-text
    section from the Introduction through Related Work, and five
    appendices (CLT Implementation Details, Validating the Replacement
    Model, Nuances of Steering with Cross-Layer Features, Unexplained
    Variance and Choice of Steering Factors, and the opening of Similar
    Features and Supernodes). The interactive figures were not available;
    they are taken from the text, captions and inline tables. Status
    Deferred → Active. Three accounts filed: THEORY-tmpbtnf0,
    THEORY-tmpm4ifd and THEORY-tmp7rb6m, all Active. The summary is
    checked against the reading and kept.
tags:
- representation-learning
- causality
- anthology-candidate
date: '2026-10-26'
published: '2025-03-27'
url: 'https://transformer-circuits.pub/2025/attribution-graphs/methods.html'
first_author: 'Ameisen'
keywords:
- 'circuit tracing'
- 'attribution graphs'
- 'cross-layer transcoder'
- 'replacement model'
- 'mechanistic interpretability'
- 'mechanistic faithfulness'
implementations: []
extends:
- LIT-tmptgo43
summary: >-
  Ameisen et al. (2025), Transformer Circuits Thread. A cross-layer
  transcoder, whose features each read the residual stream at one layer
  and write to every later MLP output, stands in for a model's MLPs. On one
  prompt, with attention patterns and normalization denominators frozen and
  error terms added back, this local replacement model reproduces the
  model's activations exactly, and its attribution graph decomposes each
  feature's pre-activation into linear edges. The graphs, pruned and
  grouped into supernodes, give hypotheses about an 18-layer model and
  Claude 3.5 Haiku that are then tested by perturbing features in the
  underlying model.
---
<!-- inactive-ok-file: THEORY-022 CLAIM-tmpwr001 THEORY-802 — Proposed; neighbouring accounts and the record's own claim, named, nothing here rests on them -->

# LIT-tmpsuo6l: Circuit Tracing: Revealing Computational Graphs in Language Models

Ameisen, E., Lindsey, J., Pearce, A., Gurnee, W., Turner, N. L., Chen, B.,
Citro, C., et al. (2025). Circuit tracing: Revealing computational graphs
in language models. *Transformer Circuits Thread*, 27 March 2025.
<https://transformer-circuits.pub/2025/attribution-graphs/methods.html>

Read on 2026-10-26, main text in full (NOTE-tmpn9fx3). Three accounts were
drawn from it: THEORY-tmpbtnf0, THEORY-tmpm4ifd and THEORY-tmp7rb6m.

## Why this is here

Registered and read at the owner's request of 2026-10-26, after "how's the
record on neural circuit theory?" found that the record held almost none
of the core circuits literature. It is the method behind most circuit
claims about large language models since 2025, and the companion of
LIT-tmpjvwet, whose case studies use it. It extends Dunefsky et al.
(LIT-tmptgo43). For the record's circuits line it supplies what the line
lacked: a stated, testable sense in which a circuit is read off a large
model, and the authors' own measurement of where that reading departs
from the model. It bears on CLAIM-tmpwr001, on THEORY-022 (its addition
features against the grokking network's Fourier circuit), and on
QUESTION-tmpivbso.
