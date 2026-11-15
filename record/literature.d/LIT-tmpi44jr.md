---
status: Active
status_note: >-
  read 2026-11-15 (NOTE-tmpov37q) from the arXiv preprint, v1, the only
  version: §§1–6 in full, appendices A, C.1, the start of G.1 and the
  freeze experiment of D; B, E, F and G.2–G.4 skipped. Worth reading here
  as a toy regime in which a transformer's MLP selects rather than
  stores: learned subject embeddings hold their attributes as a linear
  superposition of codes, a ReLU MLP of width independent of N picks the
  queried one, and associative storage in weights returns only when the
  embeddings are frozen. Probe evidence in five released LMs is
  correlational.
title: 'Geometric Factual Recall in Transformers'
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Registered and read on 2026-11-15 from the owner's pasted continuation
    of the ChatGPT exchange "Explain String Theory", in A's turn on
    transformers as associative memories, where A described a "May 2026
    arXiv preprint" without authors or identifier. Found by title on the
    arXiv API (the only hit): arXiv:2605.12426, v1 2026-05-12, by Shauli
    Ravfogel, Gilad Yehudai, Joan Bruna and Alberto Bietti (Ravfogel and
    Yehudai equal; NYU and the Flatiron Institute). The PDF says
    "Preprint." and the arXiv comment "Preprint"; no DOI. A's date holds.
    No email address was sent to any service. `published:` is the arXiv
    v1 date. Copy read: arxiv.org/pdf/2605.12426v1, text by pdftotext.
tags:
- representation-learning
- learning-theory
- anthology-candidate
date: '2026-11-15'
published: '2026-05-12'
arxiv: '2605.12426'
first_author: 'Ravfogel'
keywords:
- 'factual recall'
- 'geometric memorization'
- 'associative memory'
- 'superposition'
- 'relation-conditioned selector'
- 'multi-hop reasoning'
- 'capacity-depth tradeoff'
- 'chain-of-thought'
- 'linear relational encoding'
implementations: []
summary: >-
  Ravfogel, Yehudai, Bruna & Bietti (2026, preprint). In a one-layer toy
  with N subjects and R random bijections onto shared attributes, learned
  embeddings let all N·R facts be memorized at d = O(R log N) with an MLP
  whose width does not grow with N: each subject's embedding stacks its R
  attribute codes, and the MLP is a relation-conditioned selector, not a
  key–value store. Frozen embeddings bring back associative storage at much
  larger d. A k-hop lower bound, broken by chain-of-thought, and probes in
  five released LMs. Filed as a counter-regime to THEORY-1030 and as
  context for THEORY-1039 and QUESTION-149.
---
<!-- inactive-ok-file: THEORY-tmpetsya THEORY-1030 THEORY-1039 THEORY-1011 — Proposed or Rejected readings, cited from the filing of Ravfogel et al. as open or retired -->

# LIT-tmpi44jr: Geometric Factual Recall in Transformers

Ravfogel, S., Yehudai, G., Bruna, J. & Bietti, A. (2026). Geometric Factual Recall in Transformers. Preprint, arXiv:2605.12426v1. ARXIV-2605.12426.

## Key takeaways

*From the reading, NOTE-tmpov37q.*

- **The mechanism** (Abstract): "subject embeddings encode linear
  superpositions of their associated attribute vectors, and a small MLP
  acts as a relation-conditioned selector that extracts the relevant
  attribute via ReLU gating, and not as an associative key-value mapping."
- **The construction** (Theorem 4.1): a one-layer transformer with a
  3-layer MLP of width R and d = 4R log(N) + 1 solves single-hop recall;
  each subject's embedding is the block vector of its R attribute codes.
- **Training finds it** (§5.2): with learned embeddings d_min grows as
  log N; frozen embeddings need d growing "as a power law of N"; per-
  relation readouts and counterfactual edits act on one relation at a
  time; a frozen MLP transfers zero-shot to new bijections, and does not
  when the embeddings were frozen.
- **Multi-hop** (Theorems 4.2–4.4): without chain-of-thought, a counting
  bound makes k-hop recall pay in weight bits that hold the facts (a
  lookup-table MLP of width O(NR) in the construction) or in an embedding
  exponential in k; with chain-of-thought, d = Õ(R + k) suffices.
- **Released LMs** (§5.3): attributes are linearly decodable from the
  subject's last-token state, best "roughly 50–80% through the network".

## Standing in the record

Filed from A's turn on transformers as associative memories. A's account,
that "subject embeddings hold superpositions of attribute vectors, and an
MLP acts as a relation-dependent selector", in a controlled setting, holds
in the paper's own words, as does its depth–capacity tradeoff. A's warning
not to assume "that every fact is independently encoded as a rank-one
contribution to an MLP weight matrix" is A's gloss: the paper never speaks
of rank-one edits, and it shows that associative storage is what training
finds when embeddings are frozen. The reader also notes that the
"superposition" is a direct sum of codes in disjoint blocks, not
interference superposition.

It bears on THEORY-1030 as a toy regime in which the MLP selects rather
than stores, which splits "transformer as associative memory" into memory
of the context, in attention (LIT-tmpxroua, LIT-tmpp9nhx), and memory of
facts, which here sits in embedding geometry. It offers an alternative to
storage in MLP weights rather than a test of localization (THEORY-1011,
THEORY-1039), and its LM probe claims to supply a basis for the linear
relational structure QUESTION-149 and LIT-972 concern. Its central account
is THEORY-tmpetsya.
