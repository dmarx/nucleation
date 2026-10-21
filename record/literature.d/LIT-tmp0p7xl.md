---
status: Active
status_note: >-
  read 2026-10-21 (NOTE-tmpqfl95) in full, from arXiv:1906.11583v2; worth reading for its distance between causal models that compares answers to interventions rather than graphs, for approximate abstraction as that distance under a coarse-graining (THEORY-tmpe391l), for the intervention distribution over low-level implementations of a high-level intervention, and for when an approximate abstraction factors into an abstraction and an approximation. Read it knowing that the error is a worst case over interventions, minimized over context maps and relative to a metric the user chooses, so it is zero wherever exact abstraction holds, including coarse-grainings whose dropped detail high-level noise can carry.
title: 'Approximate Causal Abstractions'
version: 2
history:
- version: 1
  date: '2026-10-21'
  note: >-
    Filed, not read. Citation checked against Crossref, OpenAlex and arXiv on 2026-10-21. `published:` is arXiv v1, 27 June 2019, per ADR-002; the PMLR volume is dated 6 August 2020. No DOI. The arXiv title is singular, "Approximate Causal Abstraction"; the proceedings title is above.
- version: 2
  date: '2026-10-21'
  note: >-
    Read in full (NOTE-tmpqfl95), from arXiv:1906.11583v2 (29 June 2019).
    Status Deferred → Active. THEORY-tmpe391l is filed from it. The
    summary is checked against the reading and corrected: the error is a
    worst case over interventions, and the probabilistic version's
    intervention distribution weights the low-level implementations of
    each high-level intervention, not the interventions themselves.
tags:
- causality
date: '2026-10-21'
published: '2019-06-27'
arxiv: '1906.11583'
url: 'https://proceedings.mlr.press/v115/beckers20a.html'
first_author: 'Beckers'
keywords:
- 'causal abstraction'
- 'approximate abstraction'
- 'interventions'
- 'causal models'
- 'macro variables'
implementations: []
summary: >-
  Beckers, Eberhardt & Halpern (2020; arXiv 2019). Extends exact causal abstraction to approximate abstraction: the worst case, over allowed interventions and contexts, of how far a high-level causal model's answers depart from the coarse-grained answers of the low-level model it abstracts, under a distance the user chooses; probabilistic versions average over contexts and, given an intervention distribution, over the low-level implementations of each high-level intervention. Composing an abstraction with an approximation gives an approximate abstraction, and the converse decomposition can fail.
---
<!-- inactive-ok-file: TERM-tmpdxajb — Proposed; filed from the same exchange, named as the entry this work bears on -->
<!-- inactive-ok-file: LIT-038 — Rejected; named only for its status note's pointer to Beckers–Halpern -->
# LIT-tmp0p7xl: Approximate Causal Abstractions

Beckers, S., Eberhardt, F. & Halpern, J. Y. (2020). Approximate Causal Abstractions. *Proceedings of the 35th Uncertainty in Artificial Intelligence Conference*, PMLR 115: 606–615. Preprint: arXiv:1906.11583 (27 June 2019), as "Approximate Causal Abstraction".

Read in full (NOTE-tmpqfl95).

## Why this is here

A25's first reading: "What, exactly, is novel about governance-response sufficiency?" A25: "We should not present governance-preserving coarse-graining as a new general theory of causal abstraction." A26 §1 set it against [TERM-023](../terms.d/TERM-023.md), [CLAIM-350](../claims.d/CLAIM-350.md) and [THEORY-820](../theory.d/THEORY-820.md). Bears on [CLAIM-tmppi0xf](../claims.d/CLAIM-tmppi0xf.md), [CLAIM-tmpshzxc](../claims.d/CLAIM-tmpshzxc.md) and [TERM-tmpdxajb](../terms.d/TERM-tmpdxajb.md). The record holds causal abstraction only through interchange interventions ([THEORY-243](../theory.d/THEORY-243.md)); [LIT-038](LIT-038.md)'s status note sends a reader wanting causal abstraction to Beckers–Halpern.
