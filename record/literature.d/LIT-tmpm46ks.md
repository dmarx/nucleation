---
status: Active
status_note: >-
  read in part 2026-10-31 ([NOTE-tmpf1zx4](../notes.d/NOTE-tmpf1zx4.md), Skimmed: §§I–III, IV.A–D, IV.G–H,
  VI, VII.A.1, VIII and appendix A read in full; field theory and two of
  three applications not read); worth reading as the systematic statement
  of how maintained nonequilibrium states behave at large size: a
  quasi-potential, not a free energy, sets their lifetimes, which
  dissipation along relaxation and escape paths brackets
  ([THEORY-tmpjzj2n](../theory.d/THEORY-tmpjzj2n.md)); each carries its own housekeeping dissipation; and
  Gaussian-noise Langevin models get both barriers and entropy production
  wrong ([THEORY-tmpkze5s](../theory.d/THEORY-tmpkze5s.md)).
title: 'Macroscopic stochastic thermodynamics'
version: 2
history:
- version: 1
  date: '2026-10-31'
  note: >-
    Filed, not read, from A14 of the exchange "Analyze nucleation
    concepts" (2026-10-30 to 31). Citation checked against Crossref
    (RMP 97, 015002, 2025-01-22) and arXiv (v1 2023-07-23);
    `published:` takes the arXiv date (ADR-002). The summary follows
    the abstract and the exchange's description; a reading should
    check it first.
- version: 2
  date: '2026-10-31'
  note: >-
    Read in part in NOTE-tmpf1zx4 (status Skimmed) from arXiv
    2307.12406v3: the sections on large deviations, metastability and
    escape, and dissipation in full; §V, §§VII.A.2–VII.C and appendix B
    not read. Status Deferred → Active: the parts that bear on this
    record were read and checked, and the note says what was not. The
    citation stands. The summary is rewritten from the text. The
    registration's "thermodynamic cost of rare transitions" is right in
    spirit: the review bounds escape rates by path entropies, and says
    the bounds are loose far from equilibrium. Tag natural-sciences
    added. Produces THEORY-tmpjzj2n (with LIT-tmp24302) and
    THEORY-tmpkze5s; co-source of THEORY-tmpwystk and THEORY-tmpshz26.
tags:
- thermodynamics
- natural-sciences
date: '2026-10-31'
published: '2023-07-23'
arxiv: '2307.12406'
doi: '10.1103/RevModPhys.97.015002'
first_author: 'Falasco'
keywords:
- 'stochastic thermodynamics'
- 'large deviations'
- 'macroscopic fluctuations'
- 'quasi-potential'
- 'metastability'
- 'Freidlin-Wentzell theory'
- 'entropy production'
implementations: []
summary: >-
  Falasco & Esposito (2025). Takes stochastic thermodynamics of jump
  processes with local detailed balance to a large-size limit. Extensive
  rates and potentials give a deterministic dynamics whose Lyapunov
  function is the quasi-potential, and a large-deviation theory of
  fluctuations that keeps the fluctuation theorem. Equilibrium, linear
  irreversible and Onsager–Machlup theories are recovered as limits.
  Transition rates between attractors go as e^{−VΔI} and are bracketed
  by the entropy produced along relaxation and escape paths, tightly
  only near detailed balance. Each attractor has a housekeeping
  dissipation, and Langevin approximations miss it and misjudge
  barriers. Minimum and maximum entropy production principles hold only
  in special regimes.
---
<!-- inactive-ok-file: THEORY-671 LIT-1664 — Proposed or Unavailable; an account this reading counts against and an unread source, named as open -->


# LIT-tmpm46ks: Macroscopic stochastic thermodynamics

Falasco, G., & Esposito, M. (2025). Macroscopic stochastic thermodynamics. *Reviews of Modern Physics*, 97, 015002.

Read in part in [NOTE-tmpf1zx4](../notes.d/NOTE-tmpf1zx4.md) (Skimmed; the parts on large deviations, metastability and escape, and dissipation read in full).

## Why this is here

A14 cited it for the large-deviation account of escape from a maintained state, where a barrier and a system-size parameter set the lifetime. Read with Langer ([LIT-1664](LIT-1664.md)) for metastable decay. The reading confirms that account and corrects one implication: the barrier is in a quasi-potential computed from the dynamics, not in a free energy, and dissipation only brackets it ([THEORY-tmpjzj2n](../theory.d/THEORY-tmpjzj2n.md)). For [CASE-tmpwxags](../cases.d/CASE-tmpwxags.md) and [CASE-111](../cases.d/CASE-111.md) it supplies the finite-size reading of a fold: a maintained regime is an attractor with its own steady dissipation, whose lifetime collapses as the barrier closes at the saddle-node. For the A14 analogy with SLT ([THEORY-087](../theory.d/THEORY-087.md)) it supplies the disanalogy: the quasi-potential belongs to a dynamics with circulating currents and housekeeping dissipation, and a Bayesian posterior is the detailed-balance case, with neither. Against [THEORY-671](../theory.d/THEORY-671.md) it shows that entropy-production extremum principles hold only in special regimes ([THEORY-tmpshz26](../theory.d/THEORY-tmpshz26.md)).
