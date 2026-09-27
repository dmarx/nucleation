---
status: Proposed
status_note: 'read in full 2026-09-27 (NOTE-tmphkmry); promising as a bridge between probe geometry and formal concept analysis, and unproven as a hypothesis about LLMs. It would be settled by three things. The attributes would have to come from something other than another LLM''s annotations. The region-level join would have to be defined correctly, as the Galois closure of the shared intent. And lattice identities (closure, absorption, meet/join agreement with the recovered context) would have to be tested, not pairwise subsumption and candidate ranking alone.'
title: 'The Lattice Representation Hypothesis of Large Language Models'
version: 2
history:
- version: 1
  date: '2026-09-27'
  note: >-
    Filed here as well as in the anthology (ANTH-LIT-460), under ADR-013, to
    be re-read against van Rijsbergen's The Geometry of Information Retrieval
    (LIT-262).
- version: 2
  date: '2026-09-27'
  note: >-
    Read in full (full text, arXiv v3 PDF (25 Jul 2026; ICLR 2026
    camera-ready), 16 pp.: §§1–4, the additional analysis, related work,
    conclusion, ethics and reproducibility statements, Appendices A (LLM
    use), B (proof of Theorem 1, Lemmas 1–3, Props 2–3, Cor 1, B.4), C
    (proof of Prop 1 with remarks), D (discussion, limitation, Figure 6) and
    the references. Figures 4 and 5b report their results only as bar
    charts, so their values are read off the plots, not stated in the text;
    I give no numbers for them. The released code was not inspected.); the
    first NOTE on it, since it was seeded from the abstract alone. Status
    set from the reading: Proposed.
tags:
- representation-learning
- logic
- mathematics
date: '2026-09-27'
published: '2026-03-01'
arxiv: '2603.01227'
first_author: 'Xiong'
keywords:
- 'linear-representation-hypothesis'
- 'formal-concept-analysis'
- 'concept-lattice'
- 'embedding-geometry'
implementations: []
summary: >-
  Xiong (2026), [ARXIV-2603.01227](https://arxiv.org/abs/2603.01227).
  Thresholding linear attribute directions (Fisher-LDA probes) gives a
  crisp object–attribute incidence, and the paper's Theorem 1 is the
  standard fact that any such incidence has a complete concept lattice.
  The geometric meet is half-space intersection; the join is defined as
  the set union of two cones and "approximated by the conic hull" of their
  directions, which as written is not a lattice join. On five WordNet
  domains with GPT-4o-annotated attributes, the probes recover the
  incidence at F1 69.7–83.2 on three 7–8B models, and profile-based
  subsumption reaches F1 57.1–77.1. No lattice law is ever tested.
---

# LIT-tmporlvo: The Lattice Representation Hypothesis of Large Language Models

Xiong (2026), *ICLR 2026* — [ARXIV-2603.01227](https://arxiv.org/abs/2603.01227)

## Standing in the record

Held in both records under [ADR-013](../decisions.d/ADR-013.md). The anthology holds it as [ANTH-LIT-460](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-460.md),
read for concept geometry, with its account [ANTH-THEORY-034](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-034.md). It is filed here
at the owner's request of 2026-09-27, to be re-read against van Rijsbergen's
*The Geometry of Information Retrieval* ([LIT-262](LIT-262.md)). Formal concept analysis,
Galois connections and the logic of lattices of classes are that book's
second chapter, and questions this record asks that the anthology does not.

It was filed `Deferred`, unread. [NOTE-tmphkmry](../notes.d/NOTE-tmphkmry.md) is the close reading of 2026-09-27, and it placed the work: **Proposed** — promising as a bridge between probe geometry and formal concept analysis, and unproven as a hypothesis about LLMs. It would be settled by three things. The attributes would have to come from something other than another LLM's annotations. The region-level join would have to be defined correctly, as the Galois closure of the shared intent. And lattice identities (closure, absorption, meet/join agreement with the recovered context) would have to be tested, not pairwise subsumption and candidate ranking alone.
