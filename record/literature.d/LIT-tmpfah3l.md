---
status: Active
status_note: >-
  read 2026-10-20 ([NOTE-tmpms8u2](../notes.d/NOTE-tmpms8u2.md)), skimmed, from arXiv:2305.18509v3: the introduction and its heuristics, the whole of Section 2 with the inductive Proposition 2.11 and the proof of Theorem 1.1 from it, the derivation of the new current errors (§5.1) and the closing of the relaxed local energy identity (§6.3, Lemma 6.10) were read; the estimates of Sections 3–6, the dodging lemmas of Section 4, the parameter choices of Section 7 and the appendix were paged through and not checked, and Section 3's proofs are in a companion paper (Annals of PDE 2024) that the record does not hold. Worth reading for the local, L³-based version of the negative half of Onsager's conjecture: for every β < 1/3 there is a weak solution of the 3D incompressible Euler equations on the periodic box in C⁰_t(B^β_{3,∞} ∩ L^{1/(1−3β)}) that satisfies the local energy inequality and whose total energy strictly decreases; and, from the proof rather than the theorem's statement, for the fact that its Duchon–Robert dissipation is exactly the smooth, nonnegative density E(t, x) = −e(t)e′(t)ρ₀(x₁, x₂)² fixed at the iteration's first step, positive in a periodic array of straight pipes and zero outside them ([THEORY-tmp6pe5a](../theory.d/THEORY-tmp6pe5a.md)). So the coarse-grained energy flux into vanishing scales converges, as a distribution in space and time, to a one-signed density: one-way at every place and time in the limit, which Buckmaster, De Lellis, Székelyhidi and Vicol ([LIT-tmpv4d6t](LIT-tmpv4d6t.md)) showed only for the whole box. Read it knowing that the solutions are not Hölder or even bounded (the strong Hölder version is open; the best Hölder result with the local inequality is β < 1/7, De Lellis and Kwon); that where and how fast energy is dissipated is an input of the construction, carried unchanged through every step, not something the dynamics selects; that the one-signed statement is about the limit ℓ → 0 tested against nonnegative functions, and nothing is said about the sign of the flux at any finite scale; that nothing ties these solutions to vanishing-viscosity limits, though the paper notes that the local inequality is what such limits would satisfy; and that the arXiv v3 copy read is the authors' final version, not compared with the Annals text.
title: 'The L³-based strong Onsager theorem'
version: 2
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Registered on 2026-10-20 as the follow-up named by the reading of Buckmaster, De Lellis, Székelyhidi and Vicol (NOTE-tmp18d5h, THEORY-tmpnvuqr), whose solutions dissipate energy only for the box as a whole, for the local energy inequality below 1/3. Citation from the arXiv API, the arXiv abstract page and Crossref: Giri, V., Kwon, H. & Novack, M., arXiv:2305.18509, v1 submitted 29 May 2023, v2 11 September 2023, v3 5 August 2025 ("final version, to appear in Annals of Mathematics"); published as Annals of Mathematics 204(1):265–421, doi:10.4007/annals.2026.204.1.4, which Crossref dates 1 July 2026 (the issue). `published:` is the arXiv v1 date, the earliest, per ADR-002. Per ADR-048 the Anthology of the SOTA was not checked; a grep of this record for the arXiv id and the title found only citations of it as unread (NOTE-tmp18d5h, THEORY-tmpnvuqr).
- version: 2
  date: '2026-10-20'
  note: >-
    Skimmed (NOTE-tmpms8u2) from arXiv:2305.18509v3 (103 pages). Status Active. THEORY-tmp6pe5a filed Proposed. The paper's Theorem 1.1 states only that the local energy inequality holds and the total energy is dissipated; that the Duchon–Robert measure equals the prescribed E is read from the proof (Proposition 2.11 carries E unchanged; Step 2 of the proof of Theorem 1.1 states the limit identity). The summary is written from the reading.
tags:
- mathematics
- natural-sciences
date: '2026-10-20'
published: '2023-05-29'
arxiv: '2305.18509'
doi: '10.4007/annals.2026.204.1.4'
first_author: 'Giri'
keywords:
- 'strong Onsager conjecture'
- 'incompressible Euler equations'
- 'local energy inequality'
- 'Duchon–Robert measure'
- 'convex integration'
- 'intermittency'
- 'Besov spaces'
- 'Mikado bundles'
- 'wavelet-inspired iteration'
implementations: []
summary: >-
  Giri, Kwon & Novack (2023; Annals of Mathematics 2026). For every β < 1/3 there is a weak solution of the 3D incompressible Euler equations on T³ in C⁰([0, T]; B^β_{3,∞} ∩ L^{1/(1−3β)}) that satisfies the local energy inequality ∂_t(½|u|²) + div((½|u|² + p)u) = −D[u] ≤ 0 and strictly dissipates its total kinetic energy: the L³-based strong Onsager conjecture, previously known only for β < 1/7 (in Hölder spaces, De Lellis and Kwon). In the proof D[u] is exactly a prescribed smooth density, −e(t)e′(t)ρ₀(x₁, x₂)² with e(t) a decaying exponential and ρ₀ a pipe flow along e₃, so dissipation is strictly positive inside a periodic array of pipes and zero outside. The construction is an intermittent, L³-measured convex integration in which successive velocity increments overlap in frequency ("partial wavelet sums"), kept apart in space by multi-scale "Mikado bundles", with an intermittent pressure that dominates every error pointwise. Section 3's proofs are in a companion paper (Annals of PDE 10:19, 2024).
---
<!-- inactive-ok-file: NOTE-tmpms8u2 — Skimmed; this work's reading -->
<!-- inactive-ok-file: THEORY-tmp6pe5a THEORY-tmpnvuqr — Proposed; the account this reading files, and the whole-box account it localizes -->
<!-- inactive-ok-file: NOTE-tmp18d5h — the reading that named this work -->
# LIT-tmpfah3l: The L³-based strong Onsager theorem

Giri, V., Kwon, H. & Novack, M. (2026). The L³-based strong Onsager theorem. *Annals of Mathematics* 204(1): 265–421. doi:10.4007/annals.2026.204.1.4. arXiv:2305.18509 (29 May 2023).

Skimmed in [NOTE-tmpms8u2](../notes.d/NOTE-tmpms8u2.md), from the arXiv copy. What it implies for the
local coarse-grained energy flux is filed as [THEORY-tmp6pe5a](../theory.d/THEORY-tmp6pe5a.md).

## Why this is here

Named by the reading of Buckmaster, De Lellis, Székelyhidi and Vicol
([NOTE-tmp18d5h](../notes.d/NOTE-tmp18d5h.md), [THEORY-tmpnvuqr](../theory.d/THEORY-tmpnvuqr.md)), whose rough Euler solutions lose energy
only for the box as a whole. [QUESTION-219](../questions.d/QUESTION-219.md) needed to know whether the one-way
transfer into vanishing scales can hold at every place as well as overall.
This paper gives solutions whose dissipation measure is nonnegative
everywhere and, in its proof, a known smooth function.
