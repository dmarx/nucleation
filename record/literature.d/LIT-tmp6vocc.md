---
status: Active
status_note: >-
  read 2026-10-20 ([NOTE-tmpb08k2](../notes.d/NOTE-tmpb08k2.md)), skimmed, from arXiv:1710.11186v4: the introduction, Sections 2 and 3 (the dissipative Euler–Reynolds flow and the Main Lemma), Sections 4.1–4.5 (the shape of the construction, the coefficient equations and the energy increment), the opening of 4.10, Section 4.14, Section 5 and Section 6 in full were read; Sections 4.6–4.13, the estimates, were paged through and not checked. Worth reading for the first continuous, indeed C^α_{t,x} with α < 1/15, weak solutions of the 3D incompressible Euler equations that satisfy the local energy inequality with nonzero dissipation (Theorems 1 and 4); for nonuniqueness of such solutions from one initial datum, as a Cantor family with a common dissipation measure and positive Hausdorff dimension in C_tL²_x, and of energy-conserving ones (Theorems 4, 5 and 7); for C⁰ density of wild initial data (Theorem 8); for the notion of a dissipative Euler–Reynolds flow, whose relaxed local energy inequality carries an unresolved flux density and current; and, from the proof rather than any statement, for the fact that the dissipation measure is a function of time alone, equal at each time to the rate of loss of total energy and so spread uniformly over the torus ([THEORY-tmpxpm2w](../theory.d/THEORY-tmpxpm2w.md)). Read it knowing that "globally dissipative" means the local energy inequality (not whole-box dissipation, and not strict); that the exponent 1/15 is far below 1/3 (De Lellis and Kwon later reached 1/7 in Hölder spaces, Giri, Kwon and Novack 1/3 in L³-based ones); that the dissipation happens only in a short final interval in which the construction drains the solution to zero, its timing an input; that the shared initial datum is produced by the construction, not prescribed; that the "probabilistic method" is a binary choice per stage, not a random construction; and that the Burgers example of §1.2.1 misstates two constants (−d/dt∫u₀² is 1/3, not 2/3, and the threshold (1/6)^{1/3} is sufficient but not sharp, which is (1/4)^{1/3}), without affecting its point.
title: 'Nonuniqueness and existence of continuous, globally dissipative Euler flows'
version: 2
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Registered on 2026-10-20 for QUESTION-219, as the work THEORY-776 names unread for continuous globally dissipative flows. Citation from the arXiv abstract page and Crossref: Isett, P., arXiv:1710.11186, v1 submitted 30 October 2017, v2 11 August 2018, v3 18 November 2021, v4 7 February 2022 ("Improvements in presentation"); published as Archive for Rational Mechanics and Analysis 244:1223–1309, doi:10.1007/s00205-022-01780-6, which Crossref dates 22 April 2022 online and June 2022 in print. `published:` is the arXiv v1 date, the earliest, per ADR-002. Per ADR-048 the Anthology of the SOTA was not checked; a grep of this record for the arXiv id and the title found only citations of it as unread (THEORY-776 and the notes beside it).
- version: 2
  date: '2026-10-20'
  note: >-
    Skimmed (NOTE-tmpb08k2) from arXiv:1710.11186v4 (67 pages). Status Active. THEORY-tmpxpm2w filed Proposed. The paper states only that the dissipation is strict everywhere on an open time interval; that the measure is a function of time alone is read from the proof ((44), (117) and Lemma 6.1). The summary is written from the reading.
tags:
- mathematics
- natural-sciences
date: '2026-10-20'
published: '2017-10-30'
arxiv: '1710.11186'
doi: '10.1007/s00205-022-01780-6'
first_author: 'Isett'
keywords:
- 'incompressible Euler equations'
- 'local energy inequality'
- 'globally dissipative solutions'
- 'strong Onsager conjecture'
- 'convex integration'
- 'nonuniqueness'
- 'dissipative Euler–Reynolds flow'
- 'Hausdorff dimension'
- 'wild initial data'
- 'Lagrangian direct interaction approximation'
implementations: []
summary: >-
  Isett (2017; Archive for Rational Mechanics and Analysis 2022). For every α < 1/15 there are weak solutions of the incompressible Euler equations on T³ (and T^d, d ≥ 3) in C^α_{t,x} that satisfy the local energy inequality ∂_t(|v|²/2) + ∇·((|v|²/2 + p)v) ≤ 0, strictly on an open time interval: the first continuous examples, and a first partial result on the strong Onsager conjecture. From one initial datum there is a Cantor family of them, with no isolated points, positive Hausdorff dimension in C_tL²_x and one common dissipation measure; the same holds for solutions with the local energy equality, and wild data are C⁰ dense. The scheme is a convex integration of "dissipative Euler–Reynolds flows" with one-directional transported plane waves, whose triad interactions cancel the unresolved energy flux current. In the proof the dissipation measure is a function of time alone, switched on only while the construction drains the solution to zero.
---
<!-- inactive-ok-file: NOTE-tmpb08k2 — Skimmed; this work's reading -->
<!-- inactive-ok-file: THEORY-tmpxpm2w THEORY-776 — Proposed; the account this reading files, and the entry that named this work -->
# LIT-tmp6vocc: Nonuniqueness and existence of continuous, globally dissipative Euler flows

Isett, P. (2022). Nonuniqueness and existence of continuous, globally dissipative Euler flows. *Archive for Rational Mechanics and Analysis* 244: 1223–1309. doi:10.1007/s00205-022-01780-6. arXiv:1710.11186 (30 October 2017).

Skimmed in [NOTE-tmpb08k2](../notes.d/NOTE-tmpb08k2.md), from the arXiv copy. What it implies for the
local coarse-grained energy flux is filed as [THEORY-tmpxpm2w](../theory.d/THEORY-tmpxpm2w.md).

## Why this is here

Named unread by [THEORY-776](../theory.d/THEORY-776.md), whose Hölder solutions lose energy only for
the box as a whole. [QUESTION-219](../questions.d/QUESTION-219.md) needed to know whether one-way transfer at
every place is possible for Hölder solutions, and what the dissipation
looks like when it is. This paper gives the first such solutions, at a low
exponent, and its construction makes the dissipation uniform in space.
