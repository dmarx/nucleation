---
status: Active
status_note: >-
  read 2026-10-26 (NOTE-tmpr0gdc) in full, from the arXiv copy (v3, the
  ICLR 2025 version); worth reading as the method that turned
  sparse-autoencoder features into circuits, by linear approximations of
  indirect effects over features and autoencoder errors together, and for
  its own evidence that the features alone are not the circuit: with the
  error nodes removed, its feature circuits recover little of the behaviour
  (THEORY-tmpuogp2). Read it knowing that faithfulness is scored on the
  latter two thirds of each circuit only, that the interpretability of the
  circuits is the authors' annotation, that the half-performance figure for
  Gemma neurons lies beyond its plotted range, and that its debiasing
  method is ML practice, which this record does not hold.
title: 'Sparse Feature Circuits: Discovering and Editing Interpretable Causal Graphs in Language Models'
version: 2
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed, not read, at the owner's request of 2026-10-26 ("go ahead and
    register and read those"), after the answer to "how's the record on
    neural circuit theory?" found the record held almost none of the core
    circuits literature. Checked on 2026-10-26 against the arXiv record:
    Samuel Marks, Can Rager, Eric J. Michaud, Yonatan Belinkov, David Bau
    and Aaron Mueller, arXiv 2403.19647, v1 submitted 28 March 2024, which
    is `published:` (ADR-002); v2 of 31 March 2024; v3 of 27 March 2025,
    whose header reads "Published as a conference paper at ICLR 2025". The
    summary follows the arXiv abstract.
- version: 2
  date: '2026-10-26'
  note: >-
    Read in full (NOTE-tmpr0gdc) from the arXiv PDF, v3, fetched 2026-10-26,
    text extracted with pdftotext; Figure 3 was read from a page rendering.
    Status Deferred → Active. Two accounts filed: THEORY-tmpuogp2 (Active)
    and THEORY-tmpyawf9 (Proposed). The summary is checked against the
    reading and given the models and the error terms. v3 adds Gemma-2-2B;
    v1 and v2 were not compared.
tags:
- representation-learning
- causality
- anthology-candidate
date: '2026-10-26'
published: '2024-03-28'
arxiv: '2403.19647'
first_author: 'Marks'
keywords:
- 'sparse feature circuits'
- 'sparse autoencoders'
- 'circuit discovery'
- 'attribution patching'
- 'indirect effect'
- 'spurious correlations'
implementations: []
summary: >-
  Marks et al. (2024), arXiv:2403.19647, ICLR 2025. Circuits are found over
  sparse-autoencoder features and autoencoder error terms of Pythia-70M and
  Gemma-2-2B, scoring nodes and edges by linear approximations to their
  indirect effects. On subject–verb agreement, small feature circuits
  carry much of the behaviour where neuron circuits need many more nodes,
  though only with the error terms kept. A human can remove features judged
  task-irrelevant from a classifier's circuit (SHIFT), and the same method
  is run without supervision over thousands of behaviours clustered from
  the Pile.
---
<!-- inactive-ok-file: THEORY-tmpyawf9 CLAIM-tmpwr001 THEORY-tmpt45mh — Proposed; the account filed from this reading and the entries it bears on, cited as open -->

# LIT-tmp5b0z9: Sparse Feature Circuits: Discovering and Editing Interpretable Causal Graphs in Language Models

Marks, S., Rager, C., Michaud, E. J., Belinkov, Y., Bau, D., and Mueller,
A. (2025). Sparse feature circuits: Discovering and editing interpretable
causal graphs in language models. *ICLR 2025*. arXiv:2403.19647.

Read in full on 2026-10-26 (NOTE-tmpr0gdc). Two accounts were drawn from
it: THEORY-tmpuogp2 and THEORY-tmpyawf9.

## Why this is here

Registered on 2026-10-26 at the owner's request, when the record was found
to hold almost none of the core circuits literature. It is the bridge from
features to circuits: the record held sparse-autoencoder features as units
(LIT-tmpn9ui7, LIT-tmp8w8uj) and circuits over heads (LIT-tmpe7b5o), but
not a circuit built of features. Its indirect effects with the
integrated-gradient approximation are what the record's crosscoder reading
builds on (LIT-tmpuuwok, THEORY-tmpt45mh),
and its last author leads MIB (LIT-tmprlq7z). It bears on CLAIM-tmpwr001,
THEORY-tmp4lqc8 and QUESTION-tmpivbso.
