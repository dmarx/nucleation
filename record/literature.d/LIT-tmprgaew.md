---
status: Active
status_note: 'read 2026-10-09 ([NOTE-tmpi1goy](../notes.d/NOTE-tmpi1goy.md)); worth reading as the paper that turns "the relevant degrees of freedom" of real-space renormalization into an objective that can be optimized: a block''s coarse variable is chosen to maximize its mutual information with the system beyond a buffer around the block. Trained on Monte Carlo samples alone, the network rediscovers Kadanoff''s block spin for the 2D Ising model, finds the low-momentum electric fields of the 2D dimer model while ignoring a strongly patterned but decoupled noise, and, iterated, reproduces the Ising flow away from T_c (located to about 1%) with ν ≈ 1.0 ± 0.15. An RBM trained instead to fit the data distribution latches on to the noise. The equivalence of the objective with a short-ranged effective Hamiltonian is argued, and shown only for 1D and quasi-1D chains; in 2D the evidence is the two models, whose answers were known beforehand.'
title: 'Mutual information, neural networks and the renormalization group'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Filed at the owner's request on 2026-10-09 in the second part of the
    batch on hierarchy and hyperbolic geometry, asked for after
    QUESTION-025 was opened; the owner gave only the Nature Physics link.
    Read in full the same day (NOTE-tmpi1goy) from the arXiv PDF of v2
    (24 September 2018, 18 pp. with supplementary materials, the version
    the authors label "the accepted (substantially extended) version"),
    text extracted with pdftotext. The publisher's typeset text was not
    read. Checked against Crossref for DOI 10.1038/s41567-018-0081-4
    (Nature Physics 14(6):578–582, June 2018, published online 26 March
    2018; Maciej Koch-Janusz and Zohar Ringel), against the arXiv
    abstract record (arXiv:1704.06279, v1 submitted 20 April 2017, v2 24
    September 2018, same title and authors, the journal reference and DOI
    given) and against the article page at nature.com (received 11 May
    2017, accepted 13 February 2018). `published:` is the arXiv v1 date,
    20 April 2017, the earliest any source gives (ADR-002). Not held in
    nucleation before this filing: a grep of record/ for the identifier,
    the DOI, the title, both authors and "real-space mutual information"
    found nothing. Not held in the Anthology of the SOTA as far as its
    clone shows: a grep of its record/ (clone at commit d8b5ba5, 9
    October 2026, possibly stale) for the same terms found nothing. Its
    `physical-sciences` topic (models whose data is the physical world)
    could hold it, and the paper carries a claim about which training
    objective makes a network perform renormalization, hence
    `anthology-candidate`.
tags:
- natural-sciences
- information-theory
- representation-learning
- anthology-candidate
date: '2026-10-09'
published: '2017-04-20'
arxiv: '1704.06279'
doi: '10.1038/s41567-018-0081-4'
first_author: 'Koch-Janusz'
keywords:
- 'renormalization group'
- 'real-space renormalization'
- 'mutual information'
- 'restricted Boltzmann machines'
- 'relevant degrees of freedom'
- 'Ising model'
- 'dimer model'
- 'information bottleneck'
implementations: []
summary: >-
  Koch-Janusz and Ringel (2017; Nature Physics 14, 578–582, 2018). Defines
  the relevant degrees of freedom of a spatial block as the coarse variable
  that maximizes mutual information with the environment beyond a buffer,
  and learns it with restricted Boltzmann machines from Monte Carlo
  samples (the RSMI algorithm). It recovers Kadanoff block spins in the 2D
  Ising model and the electric-field variables of the dimer model, ignores
  decoupled noise, and, iterated, gives the Ising flow and ν ≈ 1.0 ± 0.15;
  a distribution-fitting RBM does none of this. The link to a short-ranged
  effective Hamiltonian is proved only in 1D.
---
<!-- inactive-ok-file: QUESTION-025 THEORY-185 THEORY-036 THEORY-017 THEORY-tmpsylqv LIT-039 — Proposed, Deferred or open; cited as the question the batch answers to, accounts this reading is set beside, what it produced, and an unread neighbour -->

# LIT-tmprgaew: Mutual information, neural networks and the renormalization group

Maciej Koch-Janusz and Zohar Ringel (2017), *Nature Physics* 14(6):578–582
(2018) — [ARXIV-1704.06279](https://arxiv.org/abs/1704.06279), DOI-10.1038/s41567-018-0081-4

## Key takeaways

- **Relevance as an objective.** For a small region V of a lattice
  system, separated by a buffer B from the environment E, the coarse
  variables H are drawn from P_Λ(H|V), an RBM-form conditional, and Λ is
  chosen to maximize I_Λ(H : E). The buffer keeps short-range
  correlations of V with its own neighbourhood out of the count. The
  input is Monte Carlo samples; nothing about the Hamiltonian is given.
  Two RBMs trained by contrastive divergence approximate P(V, E) and
  P(V), and a proxy A_Λ of the mutual information is estimated by
  sampling and climbed by stochastic gradient (supplement, Eqs. 5–15).
- **What it finds.** 2D Ising, one hidden unit on a 2 × 2 block: equal
  coupling to the four spins, Kadanoff's block spin. Larger blocks: the
  weights concentrate on the block's boundary, which the supplement
  argues is what a real-space RG should do. 2D fully packed dimers on an
  8 × 8 block: filters that read the staggered patterns, i.e. the
  low-momentum electric fields E_y and E_x ± E_y of the height-field
  description, learned without the mapping. Decoupled ferromagnetic spin
  pairs added as patterned noise get zero weight.
- **Iterated, it gives numbers.** On 128 × 128 Ising samples near T_c, up
  to four steps of RSMI coarse-graining, with the effective temperature
  read intrinsically from correlations or from the mutual information
  itself, flow away from T_c on both sides (T_c located to about 1%), and
  a finite-size collapse gives ν ≈ 1.0 ± 0.15 against the exact 1.
- **The objective, not the network, does the work.** An RBM trained by
  contrastive divergence to model the same noisy dimer data puts its
  first hidden units on the noise pairs and later ones on columnar,
  not staggered, dimer patterns. The authors conclude that networks
  trained to fit the data distribution do not in general perform RG,
  against Mehta and Schwab's claimed exact mapping, and that Lin and
  Tegmark's denial of any link holds only for that kind of objective.
- **The theory is thin outside 1D.** That maximizing this mutual
  information yields a compact, short-ranged effective Hamiltonian is
  argued heuristically; for the 1D Ising chain three candidate filters are
  compared and decimation, the known optimum, gets twice the boundary
  filter's information; and for 1D and quasi-1D systems with nearest
  neighbour interactions, saturating the information is shown to forbid
  next-nearest-neighbour terms.

## Standing in the record

Filed on 2026-10-09 at the owner's request, as one of the second part of a
batch of works on hierarchy and hyperbolic geometry asked for after the
record opened [QUESTION-025](../questions.d/QUESTION-025.md). Read on its own merits ([NOTE-tmpi1goy](../notes.d/NOTE-tmpi1goy.md)); the
reading produces [THEORY-tmpsylqv](../theory.d/THEORY-tmpsylqv.md).

It does not bear on [QUESTION-025](../questions.d/QUESTION-025.md) beyond analogy. Its hierarchy is the
nesting of spatial blocks under repeated coarse-graining, and its
"relevant" variables are those of a lattice model, not attributes of a
word; there is no co-occurrence matrix, PMI or concept lattice. What it
does supply is a worked case in which the variables worth keeping at each
level are fixed by what they must stay informative about, and in which
fitting the data's own distribution keeps the wrong ones.

It appeared in the same issue of *Nature Physics*, on the next pages
(583–589), as García-Pérez, Boguñá and Serrano's geometric renormalization
of networks ([LIT-tmpbx6w0](LIT-tmpbx6w0.md)), filed in the same batch. The two are not
companion papers: different authors and groups, different methods, no
citation of either by the other, and the article page links no shared
commentary. They share the theme of renormalization outside its home
territory, here driven by data rather than by a hidden metric space.

In the record it sits beside the information bottleneck ([LIT-338](LIT-338.md)), of
which the authors call RSMI a neural implementation of a variant; beside
Rizi's account of emergence as a predictive coarse-graining ([LIT-150](LIT-150.md)) and
Ladyman's real patterns ([LIT-219](LIT-219.md), [THEORY-036](../theory.d/THEORY-036.md)), both of which invoke the
renormalization group as their example of lossy, scale-relative
description; and near Kupiainen's comment on rigorous RG ([LIT-039](LIT-039.md)), held
unread.

The same authors' sequels are not held here: Lenggenhager, Gökmen,
Ringel, Huber and Koch-Janusz, *Optimal Renormalization Group
Transformation from Information Theory* (arXiv:1809.09632, Phys. Rev. X
10, 011037, 2020), and Gökmen, Ringel, Huber and Koch-Janusz, *Statistical
physics through the lens of real-space mutual information*
(arXiv:2101.11633, Phys. Rev. Lett. 127, 240603, 2021). Nor is Mehta and
Schwab's *An exact mapping between the Variational Renormalization Group
and Deep Learning* (arXiv:1410.3831), which this paper argues against.
