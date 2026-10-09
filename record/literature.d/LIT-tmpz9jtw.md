---
status: Active
status_note: 'read 2026-10-09 ([NOTE-tmpu0mur](../notes.d/NOTE-tmpu0mur.md)); worth reading as the long companion of [LIT-878](LIT-878.md) and the place where the real-space mutual-information method is shown on more than one model and its outputs are read as an ensemble: the maximal information counts the ordered sectors (exactly 1 bit in the 2D Ising ferromagnet, 2 bits in the columnar dimer phase), decays exponentially with the buffer in the Ising paramagnet and algebraically at criticality, and the optimal Ising filter goes uniform, boundary and random across T_c; 500 independent runs per temperature map an RSMI-degenerate subspace of filters whose projections show the broken C4 and translation symmetries of the dimer model and, at high temperature, its emergent U(1), and PCA of the ensemble recovers the pristine operators from a window where they never appear alone. The number of coarse variables is chosen where the information stops growing. A non-equilibrium chipping model is a one-figure validation, and its formal status is said to be missing.'
title: 'Symmetries and phase diagrams with real-space mutual information neural estimation'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Filed at the owner's request on 2026-10-09, as a work cited by the
    hierarchy and hyperbolic-geometry batch (nucleation#113 and #114) that
    neither record held; the citing work is Gökmen et al.'s PRL, LIT-878,
    which names it as the companion carrying the Ising, symmetry and
    non-equilibrium examples. Read in full the same day (NOTE-tmpu0mur)
    from the arXiv PDF of v3 (18 October 2021, "Accepted version. Added
    new discussion of symmetries in the ensemble of coarse-graining
    rules", 27 pp.: main text pp. 1–17, Supplemental Material pp. 18–26,
    references), text extracted with pdftotext. The publisher's typeset
    text was not read. Checked against the arXiv abstract record
    (arXiv:2103.16887: v1 submitted 31 March 2021; v2 1 April 2021; v3
    18 October 2021; four authors; journal reference Phys. Rev. E 104,
    064106 (2021) and the DOI given), against the v1 PDF's first page,
    and against Crossref for DOI 10.1103/PhysRevE.104.064106 (Physical
    Review E 104(6), article 064106, published online and issued 6
    December 2021; Doruk Efe Gökmen, Zohar Ringel, Sebastian D. Huber,
    Maciej Koch-Janusz). The v1 title is "Phase diagrams with real-space
    mutual information neural estimation"; "Symmetries and" was added in
    v3 with the symmetry discussion, and the title here is the published
    one, as arXiv and Crossref now give it. The journal page at
    journals.aps.org returned HTTP 403. `published:` is the arXiv v1
    date, 31 March 2021, the earliest any source gives (ADR-002). Not
    held in nucleation before this filing: a grep of record/ for the
    identifier, the DOI and the title found only the mentions in LIT-878
    and NOTE-681. Not held in the Anthology of the SOTA as far as its
    clone shows: a grep of its record/ (clone at commit d8b5ba5, possibly
    stale) for the identifier, the DOI, "Gökmen"/"Gokmen", "Koch-Janusz"
    and "real-space mutual" found nothing. As for LIT-878, its
    `physical-sciences` topic could hold it: a machine-learning method for
    physical data built from neural mutual-information estimators the
    anthology reads (ANTH-LIT-589); hence `anthology-candidate`.
tags:
- natural-sciences
- information-theory
- representation-learning
- anthology-candidate
date: '2026-10-09'
published: '2021-03-31'
arxiv: '2103.16887'
doi: '10.1103/PhysRevE.104.064106'
first_author: 'Gökmen'
keywords:
- 'real-space mutual information'
- 'renormalization group'
- 'mutual information estimation'
- 'InfoNCE'
- 'Gumbel-softmax'
- 'Ising model'
- 'interacting dimer model'
- 'emergent symmetry'
- 'ensemble of coarse-graining rules'
- 'chipping and aggregation model'
implementations:
- 'RSMI-NE (https://github.com/RSMI-NE/RSMI-NE)'
summary: >-
  Gökmen, Ringel, Huber and Koch-Janusz (2021; Phys. Rev. E 104, 064106),
  the long companion of [LIT-878](LIT-878.md). Derives the RSMI-NE estimator in full
  and applies it to the 2D Ising model (1 bit below T_c, exponential decay
  with the buffer above it, boundary filters at T_c), the interacting
  dimer model and a 1D non-equilibrium chipping model. Its new object is
  the ensemble of optimal filters from independent runs: it maps an
  RSMI-degenerate subspace whose projections show broken and emergent
  (U(1)) symmetries, and PCA of it recovers the pristine operators.
  Every model's answer was known beforehand.
---
<!-- inactive-ok-file: THEORY-194 THEORY-017 THEORY-019 QUESTION-025 LIT-246 LIT-256 — Proposed, Deferred or open; cited as the account this reading extends, accounts it bears on, the question it does not answer, and the estimator papers it rests on -->

# LIT-tmpz9jtw: Symmetries and phase diagrams with real-space mutual information neural estimation

Doruk Efe Gökmen, Zohar Ringel, Sebastian D. Huber and Maciej Koch-Janusz
(2021), *Physical Review E* 104(6):064106 — [ARXIV-2103.16887](https://arxiv.org/abs/2103.16887),
DOI-10.1103/PhysRevE.104.064106

## Key takeaways

- **The method, written out.** The real-space mutual information
  I_Λ(H : E) between a block's coarse variable H and its environment
  beyond a buffer is bounded below by InfoNCE with a separable critic
  f_Θ(h, e) = v(h)ᵀu(e) (two hidden layers of 32, embedding dimension 8);
  H = τ ∘ (Λ · v) with τ an annealed Gumbel-softmax; Λ and Θ are trained
  together by Adam at one learning rate. The paper derives the
  Barber–Agakov, NWJ and InfoNCE bounds, proves the Gumbel-max lemma, and
  states InfoNCE's log K ceiling, which here is far above a few bits
  (mini-batches K = 100 for Ising, 400 for dimers). Runs take 8–35 s.
- **The information counts phases.** In the 2D Ising model the maximal
  I_Λ is exactly 1 bit below T_c at every buffer, has a step at T_c
  that sharpens with the buffer, and decays exponentially with the
  buffer in the paramagnet; at T_c it decays algebraically (fitted
  exponent υ ≈ 0.09). In the dimer model it is 2 bits in the columnar
  phase and decays as L_B^(−υ) with υ ≈ 1.16 for free dimers. In ordered
  phases the optimal information counts the symmetry-broken sectors.
- **The Ising filters trace a flow without iteration.** Optimal filters
  are uniform (the magnetization) at low T, staggered for the
  antiferromagnet, random in the paramagnet, and couple to the block's
  boundary at T_c, where the shared information scales with the
  interface. A "boundaryness" ratio peaks at T_c and sharpens with L_B;
  just above and below T_c the filters separate toward the paramagnetic
  and ferromagnetic fixed points as L_B grows.
- **The ensemble of filters is the new object.** Independent runs
  return different optimal filters. Projected onto the pristine filters,
  500 runs per temperature show four plaquette peaks and a columnar peak
  forming representations of C4 (a Z4 cycle) and of lattice translations
  (Z2 × Z2) in the ordered phase; a second, diagonal representation just
  above T_BKT; and at high T a distribution invariant under continuous
  rotations of the electric-field pair, with RSMI constant in the angle:
  the emergent U(1) of the field theory, seen on a lattice and through a
  binary H. PCA of filters from 0.7 < T < 3.7, where no pristine filter
  appears alone, returns the pristine plaquette and staggered filters as
  the leading components.
- **The size of H is found, not assumed.** Adding binary components
  until I_Λ stops growing gives one for Ising and two for dimers; one
  dimer component gives half the information, and extra components come
  out linearly dependent. Discretizing H leaves the high-T filters
  unchanged and acts as a regularizer in the ordered phase.
- **Out of equilibrium, a sketch.** On the 1D chipping and aggregation
  model (L = 256, L_B = 8) the optimal filter averages the mass at every
  aggregation rate w, while the maximal information saturates at
  different values in the two phases and peaks slightly at the
  transition. The authors say the formal understanding of the filters
  out of equilibrium is missing.

## Standing in the record

Filed on 2026-10-09 at the owner's request, as one of the works cited by
the batch on hierarchy and hyperbolic geometry (nucleation#113 and [#114](https://github.com/dmarx/nucleation/issues/114))
that neither record held. The batch work that cites it is Gökmen et al.'s
*Statistical Physics through the Lens of Real-Space Mutual Information*
([LIT-878](LIT-878.md)), which defers its Ising, symmetry and non-equilibrium examples
here. Read on its own merits ([NOTE-tmpu0mur](../notes.d/NOTE-tmpu0mur.md)); it files no THEORY.

It adds a second model and a second kind of evidence to the account
[LIT-873](LIT-873.md) grounds, [THEORY-194](../theory.d/THEORY-194.md), but every variable it finds (magnetization,
staggered magnetization, the dimer order parameters and electric fields)
was known beforehand, and the paper uses that knowledge to name them, so
it does not meet that account's `promote_when`. Like [LIT-878](LIT-878.md) it neither
iterates a flow nor fits exponents against an independent method; its
one exponent pair (υ) is new and unchecked.

Its ensemble analysis bears on [THEORY-019](../theory.d/THEORY-019.md) and [THEORY-017](../theory.d/THEORY-017.md): it reads a
symmetry off a degeneracy of the objective, which [THEORY-019](../theory.d/THEORY-019.md) says a
degeneracy alone does not license; here the symmetry was known and the
reading works because the projections are made onto a basis chosen from
the known operators. [NOTE-tmpu0mur](../notes.d/NOTE-tmpu0mur.md) gives the detail. It does not bear on
[QUESTION-025](../questions.d/QUESTION-025.md) beyond analogy: its variables are lattice operators, not
word attributes. Its estimator family is read in Poole et al. ([LIT-246](LIT-246.md))
and MINE ([LIT-256](LIT-256.md)), both held here and deferred, and InfoNCE's source is
held in the anthology ([ANTH-LIT-589](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-589.md)). Its formal antecedents are
Lenggenhager et al. ([LIT-881](LIT-881.md)) and Gordon et al.'s optimality theorem
(Phys. Rev. Lett. 126, 240601, not held).
