---
status: Active
status_note: 'read 2026-10-09 ([NOTE-tmpoed22](../notes.d/NOTE-tmpoed22.md)); worth reading as the paper that introduces the Random Hierarchy Model, a random context-free grammar of fixed depth L and branching s in which each class and each higher-level feature has m interchangeable ("synonymic") lower-level representations, and as a measured and partly derived account of how many examples a deep network needs to learn it. Two-layer networks and lazy (kernel-regime) deep networks need a fixed fraction of all the data, which is exponential in the input dimension d = s^L; deep convolutional networks in a feature-learning parametrisation need P* ≈ n_c m^L, a power of d. That number is measured, not proved. It coincides with the training-set size at which the networks'' hidden layers become insensitive to swapping synonyms, and with the size at which the class-conditional frequencies of input s-tuples, which are equal for synonyms, rise above sampling noise; a one-step gradient argument for a two-layer network on one patch links the last two. Removing the input–label correlations, with the hierarchy kept, makes deep networks fail again. The hierarchy is one of constituency (parts composing wholes), not of attributes implying attributes.'
title: 'How Deep Neural Networks Learn Compositional Data: The Random Hierarchy Model'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Filed at the owner's request on 2026-10-09 in a batch of six works on
    hierarchy and hyperbolic geometry, asked for after QUESTION-025 was
    opened; LIT-863 names the random hierarchy model as its future work for
    hierarchical attributes. Read in full the same day (NOTE-tmpoed22) from
    the arXiv PDF of v5 (3 July 2024, 24 pp.), text extracted with
    pdftotext. Checked against the arXiv abstract page (arXiv:2307.02129,
    v1 submitted 5 July 2023, v5 3 July 2024; authors Francesco Cagnetta,
    Leonardo Petrini, Umberto M. Tomasini, Alessandro Favero and Matthieu
    Wyart; the page names DOI 10.1103/PhysRevX.14.031001) and against
    Crossref for that DOI: Physical Review X 14(3), article 031001, same
    title and the same five authors in the same order, published online
    1 July 2024, CC BY 4.0. `published:` is the arXiv v1 date, 5 July 2023,
    the earliest any source gives (ADR-002). Not held in nucleation before
    this filing: a grep of record/ for the identifier, the DOI, the title
    and the authors found only the mentions of "the random hierarchy model
    of Cagnetta et al." in NOTE-665 and QUESTION-025. Not held in the
    Anthology of the SOTA as far as its clone shows: a grep of its record/
    (clone at commit d8b5ba5, 9 October 2026, possibly stale) for the
    identifier, the DOI, "Hierarchy Model", the title and all five authors
    found nothing. The anthology's `signal-structure` topic (what the data
    is like that methods exploit) could hold it, hence
    `anthology-candidate`. The authors' code
    (github.com/pcsl-epfl/hierarchy-learning) was not inspected.
tags:
- learning-theory
- compositionality
- representation-learning
- anthology-candidate
date: '2026-10-09'
published: '2023-07-05'
arxiv: '2307.02129'
first_author: 'Cagnetta'
keywords:
- 'random hierarchy model'
- 'hierarchical compositionality'
- 'context-free grammar'
- 'sample complexity'
- 'curse of dimensionality'
- 'synonymic invariance'
- 'deep convolutional networks'
- 'feature learning'
implementations: []
summary: >-
  Cagnetta, Petrini, Tomasini, Favero and Wyart (2023; Phys. Rev. X 14,
  031001, 2024). Introduces the Random Hierarchy Model, a random
  context-free grammar of depth L with m synonymic expansions per symbol.
  Shallow and lazy networks need a fixed fraction of all data, exponential
  in the input dimension; deep feature-learning CNNs learn from about
  n_c m^L examples, polynomial in it, which is where hidden layers become
  invariant to swapping synonyms and where the class statistics of input
  patches, equal for synonyms, emerge from sampling noise. Without those
  correlations deep networks fail too. The law is measured; the link to
  correlations is a scaling argument plus a one-step-gradient model.
---
<!-- inactive-ok-file: QUESTION-025 THEORY-185 THEORY-186 THEORY-tmpzjtfu — Proposed or open; cited as the question this filing answers to, the accounts it is set beside, and what this reading produced -->

# LIT-tmpz5v25: How Deep Neural Networks Learn Compositional Data: The Random Hierarchy Model

Francesco Cagnetta, Leonardo Petrini, Umberto M. Tomasini, Alessandro Favero
and Matthieu Wyart (2023), *Physical Review X* 14, 031001 (2024) —
[ARXIV-2307.02129](https://arxiv.org/abs/2307.02129), DOI-10.1103/PhysRevX.14.031001

## Key takeaways

- **The model.** n_c classes and L vocabularies of v symbols each. Every
  class, and every symbol at levels 2 to L, rewrites to m distinct s-tuples
  of symbols from the level below, chosen uniformly at random among all
  such assignments, with no tuple produced by two parents (so
  m v ≤ v^s). A datum is the leaf string of a depth-L, branching-s tree:
  d = s^L one-hot symbols. Each class has m^((d−1)/(s−1)) data, and in the
  maximal case m = v^(s−1), n_c = v every string of length d occurs, so the
  data lie on no low-dimensional manifold, one changed symbol can change
  the label, and the label depends on all d positions.
- **Shallow and lazy networks are cursed; deep feature learners are not.**
  A two-layer fully connected network needs a number of examples
  proportional to the total P_max, exponential in d (Fig. 2). Deep CNNs of
  depth L + 1 with filters matched to the tree, trained by SGD under the
  maximal-update parametrisation, reach 10% of chance error at
  P* ≈ n_c m^L, so P*/n_c ≈ d^(ln m / ln s), whatever v (Figs. 3, 4, 12).
  Generic deep fully connected networks show the same law up to a further
  factor of about 2^L (Fig. 13). The same CNNs in the lazy (NTK) regime
  keep a finite error even at P close to P_max (Fig. 14).
- **The number is where synonyms become interchangeable inside the
  network.** The synonymic sensitivity S_{k,l}, how much layer k's
  activations move when level-l tuples are swapped for synonyms relative
  to swapping whole data, falls from 1 to 0 around P*, and curves for
  different parameters collapse when P is rescaled by n_c m^L (Figs. 5, 6).
  Invariance to level-l synonyms appears from layer l + 1, and all levels
  are learned at the same P. The representations' effective dimension
  falls with depth (Fig. 11).
- **And where the data's statistics reveal the synonyms.** Because the
  rules are random, the probability of class α given the tuple in patch j
  differs from 1/n_c, and it is the same for tuples with the same parent.
  Its fluctuation over draws of the rules is of relative size
  (v/m^L)^(1/2); the sampling noise of its empirical estimate from P data is
  (v n_c/P)^(1/2). They balance at P_c = n_c m^L (Eq. 10, Appendix C). For a
  two-layer network on one patch, one gradient step from a symmetric start
  makes each hidden unit's response to a tuple a weighted sum of exactly
  these empirical class frequencies, so it becomes synonym-invariant as
  they converge (Eq. 13, Fig. 8).
- **Correlations are needed, hierarchy is not enough.** Forcing every tuple
  at every level to be equally likely in every class keeps the tree and
  the synonyms but removes the signal; this generalises parity, and deep
  CNNs then stay near chance up to 90% of P_max (Fig. 9). A layer-wise
  algorithm that alternates one gradient step with k-means clustering of
  the representations does better than end-to-end training by about
  √n_c (Appendix D, Fig. 10).

## Standing in the record

Filed on 2026-10-09 at the owner's request, as one of a batch of six works
on hierarchy and hyperbolic geometry asked for right after the record
opened [QUESTION-025](../questions.d/QUESTION-025.md), which asks whether correlated or hierarchical
attributes in co-occurrence still give linear attribute directions and a
concept lattice that is not Boolean. [LIT-863](LIT-863.md), whose result that question
starts from ([THEORY-185](../theory.d/THEORY-185.md)), names "the random hierarchy model of Cagnetta et
al." as the place to take hierarchical attributes next. Read on its own
merits ([NOTE-tmpoed22](../notes.d/NOTE-tmpoed22.md)); the reading produces [THEORY-tmpzjtfu](../theory.d/THEORY-tmpzjtfu.md).

It does not answer [QUESTION-025](../questions.d/QUESTION-025.md). Its hierarchy is constituency: tuples of
symbols compose into higher symbols, and a tuple determines its parent
uniquely. That is an implication structure, but between a tuple in a
position and a latent symbol, not between attributes of one word, and the
paper measures no co-occurrence matrix, PMI spectrum or linear direction.
What it does supply is a generative model in which the statistics that
reveal latent structure are exactly the ones invariant under the
equivalence that structure defines (synonyms have equal class
frequencies), and an estimate of when a finite sample shows them. The
record's other learning model with hierarchically generated data is Saxe,
McClelland and Ganguli's ([LIT-862](LIT-862.md), [THEORY-186](../theory.d/THEORY-186.md)), which the paper cites;
there the hierarchy is of attributes over items, which is closer to the
question's.

The same group's later papers build on this model and are not held here:
Sclocchi, Favero and Wyart, *A Phase Transition in Diffusion Models Reveals
the Hierarchical Nature of Data* (arXiv:2402.16991); Tomasini and Wyart,
*How Deep Networks Learn Sparse and Hierarchical Data: the Sparse Random
Hierarchy Model* (arXiv:2404.10727); and Cagnetta and Wyart, *Towards a
theory of how the structure of language is acquired by deep neural
networks* (arXiv:2406.00048). This paper is the one that introduces the
model.
