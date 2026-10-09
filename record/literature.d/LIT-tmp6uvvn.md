---
status: Active
status_note: 'read 2026-10-09 ([NOTE-tmp0zdr4](../notes.d/NOTE-tmp0zdr4.md)); worth reading as the paper that turns the real-space mutual-information principle of [LIT-873](LIT-873.md) from an iterated coarse-graining into a single-shot extraction of operators: with the mutual information estimated by a neural InfoNCE bound and the coarse-graining a convolutional filter trained against it, the filters that best compress what a block shares with its distant environment are, across the whole phase diagram of the interacting dimer model, the columnar and plaquette order parameters below the BKT transition and the electric fields at high temperature, and the plaquette filter''s correlator gives a scaling dimension of 1.00037 against the predicted 1. The maximal information itself, log 4 in the ordered phase and decaying algebraically with the buffer in the critical one, traces the phase diagram. The theorem that the optimal filters are the most relevant operators is cited to another paper, and the model''s operators were known beforehand.'
title: 'Statistical Physics through the Lens of Real-Space Mutual Information'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Filed at the owner's request on 2026-10-09, as a work cited by the
    hierarchy and hyperbolic-geometry batch (nucleation#113) that neither
    record held; the citing work is Koch-Janusz and Ringel, LIT-873, which
    names it as the authors' sequel. Read in full the same day
    (NOTE-tmp0zdr4) from the arXiv PDF of v3 (19 October 2021, "Version
    accepted for publication in Physical Review Letters", 16 pp.: main
    text pp. 1–5, Supplemental Material pp. 6–13, references), text
    extracted with pdftotext. The publisher's typeset text was not read.
    Checked against the arXiv abstract record (arXiv:2101.11633: v1
    submitted 27 January 2021, 31 pp.; v2 31 March 2021; v3 19 October
    2021; four authors; journal reference Phys. Rev. Lett. 127, 240603
    (2021) and the DOI given), against the v1 PDF's first page (same
    title and authors), and against Crossref for DOI
    10.1103/PhysRevLett.127.240603 (Physical Review Letters 127(24),
    article 240603, published online and issued 6 December 2021; Doruk
    Efe Gökmen, Zohar Ringel, Sebastian D. Huber, Maciej Koch-Janusz).
    The journal page at journals.aps.org returned HTTP 403. The title is
    the journal's capitalisation; arXiv writes it in sentence case.
    `published:` is the arXiv v1 date, 27 January 2021, the earliest any
    source gives (ADR-002). Not held in nucleation before this filing: a
    grep of record/ for the identifier, the title, "Gökmen"/"Gokmen" and
    "real-space mutual information" found only the mentions in LIT-873,
    NOTE-674, NOTE-124 and the batch's curation entry. Not held in the
    Anthology of the SOTA as far as its clone shows: a grep of its
    record/ (clone at commit d8b5ba5, possibly stale) for the identifier,
    the DOI, the title and the authors found nothing. Its
    `physical-sciences` topic could hold it, as for LIT-873: it is a
    machine-learning method for physical data, built from neural
    mutual-information estimators the anthology reads (ANTH-LIT-589);
    hence `anthology-candidate`.
tags:
- natural-sciences
- information-theory
- representation-learning
- anthology-candidate
date: '2026-10-09'
published: '2021-01-27'
arxiv: '2101.11633'
doi: '10.1103/PhysRevLett.127.240603'
first_author: 'Gökmen'
keywords:
- 'real-space mutual information'
- 'renormalization group'
- 'scaling operators'
- 'mutual information estimation'
- 'InfoNCE'
- 'interacting dimer model'
- 'Berezinskii-Kosterlitz-Thouless transition'
- 'order parameters'
implementations:
- 'RSMI-NE (https://github.com/RSMI-NE/RSMI-NE)'
summary: >-
  Gökmen, Ringel, Huber and Koch-Janusz (2021; Phys. Rev. Lett. 127,
  240603). Replaces the RBM estimator of [LIT-873](LIT-873.md) with a neural InfoNCE
  lower bound co-trained with a convolutional coarse-graining filter
  (RSMI-NE), and uses the optimal filters at a single buffer size, not an
  iterated flow, as lattice forms of the most relevant operators. On the
  interacting dimer model they are the columnar and plaquette order
  parameters below T_BKT and the electric fields at high T; the maximal
  information marks the phases; one fitted scaling dimension (1.00037
  against 1) is given. The optimality theorem is cited, not proved here.
---
<!-- inactive-ok-file: THEORY-194 THEORY-017 QUESTION-025 LIT-246 LIT-256 LIT-247 — Proposed, Deferred or open; cited as the account this reading extends, an account it bears on, the question it does not answer, and the estimator papers it rests on -->

# LIT-tmp6uvvn: Statistical Physics through the Lens of Real-Space Mutual Information

Doruk Efe Gökmen, Zohar Ringel, Sebastian D. Huber and Maciej Koch-Janusz
(2021), *Physical Review Letters* 127(24):240603 — [ARXIV-2101.11633](https://arxiv.org/abs/2101.11633),
DOI-10.1103/PhysRevLett.127.240603

## Key takeaways

- **One step instead of a flow.** The real-space mutual-information
  (RSMI) principle of [LIT-873](LIT-873.md) chooses the coarse variable H of a block V
  to maximize I_Λ(H : E) with an environment E beyond a buffer B. Here
  the buffer width L_B plays the role of the RG scale: the filters are
  optimized once, at large L_B, at each point of the phase diagram, and
  read as the operators whose correlations survive that distance, rather
  than iterated as a coarse-graining. That the formal optimum is set by
  the most relevant operators is cited to Gordon, Banerjee, Koch-Janusz
  and Ringel (Phys. Rev. Lett. 126, 240601, 2021), not shown here.
- **The estimator is what changed.** I_Λ is bounded below by InfoNCE with
  a separable neural critic f_Θ(h, e) = v(h)ᵀu(e); the coarse-graining is
  a one-layer CNN followed by a Gumbel-softmax step that keeps H
  (pseudo-)binary; both are trained together by Adam on Monte Carlo
  samples. Runs take about 30 s, three to four orders of magnitude faster
  than [LIT-873](LIT-873.md)'s RBM proxy, on systems up to 256 × 256. The bound is
  usable because RSMI is small: I_Λ ≤ N_V log n by data processing.
- **What it finds on the interacting dimer model** (dimers on the square
  lattice with an aligning interaction; columnar order below a BKT
  transition at T_BKT = 0.65, a critical phase described by a sine-Gordon
  theory above it). With a two-bit H: the maximal I_Λ is log 4 below
  T_BKT (which of the four columnar states the system is in) and decays
  algebraically with the buffer above it. The optimal filters are
  columnar and plaquette filters at low T, which coincide with the dimer
  symmetry-breaking order parameter of Alet et al. and the electric
  charge operators cos(nφ), sin(nφ) for n = 1, 2, and staggered filters
  at high T, which read the coarse-grained height gradient, the electric
  field. The columnar filter disappears above T_BKT, as the n² scaling
  of the charge operators' dimensions predicts.
- **Filters as operators.** Correlating the trained plaquette filter on
  128 × 128 samples at T → ∞ gives a power law with exponent 2.00074,
  hence a scaling dimension of 1.00037 against the predicted 1; the
  columnar correlator decays roughly as the predicted r⁻⁸ but is not
  fitted. Any rotation of the two staggered filters keeps the same
  information, which the authors read as the free dimer model's emergent
  U(1) symmetry.
- **What it rests on, and what is elsewhere.** Every operator found was
  known from the model's field theory, and the paper says so in using
  it as a dictionary. The Ising, symmetry and non-equilibrium examples
  are in the companion paper (arXiv:2103.16887, Phys. Rev. E 104, 064106,
  2021), not here.

## Standing in the record

Filed on 2026-10-09 at the owner's request, as one of the works cited by
the second part of the batch on hierarchy and hyperbolic geometry
(nucleation#113, [LIT-865](LIT-865.md) to [LIT-877](LIT-877.md)) that neither record held. It is cited
by Koch-Janusz and Ringel's *Mutual information, neural networks and the
renormalization group* ([LIT-873](LIT-873.md)) as the authors' sequel. Read on its own
merits ([NOTE-tmp0zdr4](../notes.d/NOTE-tmp0zdr4.md)); it files no THEORY.

It extends the account [LIT-873](LIT-873.md) grounds, [THEORY-194](../theory.d/THEORY-194.md), to a third model,
across a phase transition, with a different estimator, but on a model
whose relevant operators were known in advance, so it does not meet that
account's `promote_when`. Its mutual-information estimator is the family
read in Poole et al. ([LIT-246](LIT-246.md)) and MINE ([LIT-256](LIT-256.md)), both held here and
deferred; InfoNCE's source, van den Oord et al., is held in the anthology
([ANTH-LIT-589](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-589.md)). Its other antecedents are not held: Lenggenhager et al.'s
*Optimal Renormalization Group Transformation from Information Theory*
(arXiv:1809.09632) and the optimality theorem of Gordon et al. (Phys.
Rev. Lett. 126, 240601).

It does not bear on [QUESTION-025](../questions.d/QUESTION-025.md) beyond analogy: its levels are spatial
scales and its variables those of a lattice model, not attributes of
words. [NOTE-tmp0zdr4](../notes.d/NOTE-tmp0zdr4.md) records one parallel worth keeping, that a
mutual-information objective here fixes a subspace of filters and leaves
the basis within it to symmetry.
