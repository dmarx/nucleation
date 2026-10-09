---
number: 25
status: Open
formerly:
- QUESTION-tmpynu0z
title: 'Do correlated or hierarchical attributes in co-occurrence statistics still give linear attribute directions in an embedding, and with them a concept lattice that is not Boolean?'
version: 1
tags:
- representation-learning
- mathematics
date: '2026-10-09'
line: pragmatic-transport
summary: >-
  [THEORY-185](../theory.d/THEORY-185.md) derives linear directions for binary attributes from
  co-occurrence, but only for independent attributes, which make every
  combination possible and the concept lattice Boolean. The Lattice
  Representation Hypothesis ([LIT-267](../literature.d/LIT-267.md)) and [CLAIM-119](../claims.d/CLAIM-119.md) need the opposite:
  attributes that imply or exclude each other. Whether the linear
  directions survive that structure is not answered by anything the
  record holds.
---
<!-- inactive-ok-file: THEORY-186 THEORY-tmpzw8vz THEORY-tmpzjtfu THEORY-tmp1y92d THEORY-tmp5l4pi THEORY-tmpp6w9v THEORY-tmp7qz7l THEORY-tmpsylqv — Proposed; cited as partial evidence toward an answer, not as settled -->
<!-- inactive-ok-file: THEORY-185 THEORY-183 CLAIM-119 LIT-267 — Proposed; cited as the open accounts this question joins -->

# QUESTION-025: Do correlated or hierarchical attributes in co-occurrence statistics still give linear attribute directions in an embedding, and with them a concept lattice that is not Boolean?

## Why it is a question

Two accounts in the record meet at one premise and pull apart on the next
step.

- **[THEORY-185](../theory.d/THEORY-185.md)** (Korchinski, Karkada, Bahri & Wyart, [LIT-863](../literature.d/LIT-863.md)) derives the
  premise. If each binary attribute multiplies co-occurrence independently,
  the PMI is additive across attributes, and a spectral embedding is an
  affine image of each word's ±1 attribute vector. Each attribute is then a
  linear direction, and thresholding it recovers the object–attribute
  incidence exactly.
- **The Lattice Representation Hypothesis** ([LIT-267](../literature.d/LIT-267.md), read in [NOTE-240](../notes.d/NOTE-240.md))
  *assumes* that premise, after Park et al., and reads the thresholded
  incidence as a formal context whose concept lattice the model is said to
  carry. [CLAIM-119](../claims.d/CLAIM-119.md) holds that communicative categories form such a
  lattice: they share attributes and differ in a few constraints.

The derivation's assumption is what the lattice needs to be false. With
independent attributes every combination is possible, so the formal
context is the full hypercube and its concept lattice is Boolean: no
attribute implies another, and there is no hierarchy. Korchinski et al.'s
relaxation to a random subset of words (their §8) adds no structured
implications, and they leave hierarchical attributes as future work, naming
the random hierarchy model of Cagnetta et al. Their sequel ([LIT-860](../literature.d/LIT-860.md),
[THEORY-183](../theory.d/THEORY-183.md)) does the same for continuous attributes, and its Appendix D
finds the binary and continuous subspaces orthogonal: separate, not
nested.

So nothing the record holds says whether the linear directions survive
the structure that makes a concept lattice worth having: attributes that
imply each other (every *poodle* is a *dog*), exclude each other, or
interact in co-occurrence rather than multiplying independently. If they do
not, [LIT-267](../literature.d/LIT-267.md)'s first step fails exactly where its lattice becomes
non-trivial.

## What would count as an answer

- **A derivation.** A generative model of co-occurrence with a stated
  implication structure among binary attributes (a tree, or a general
  formal context), with the spectrum of its PMI worked out: whether each
  attribute still has a direction, how far thresholding recovers the
  incidence, and whether the concept lattice of the recovered incidence
  equals the generating one.
- **A measurement.** In real co-occurrence data, a test of whether the PMI
  is additive across the attributes of a known hierarchy (WordNet
  hypernymy, say), and of how a probe's errors concentrate on attributes
  that imply one another. It would need attributes not annotated by another
  language model, which was [NOTE-240](../notes.d/NOTE-240.md)'s first objection to [LIT-267](../literature.d/LIT-267.md).

Either kind settles the question. A further demonstration that
independent attributes give parallelograms does not.

## What the record holds toward an answer

None of these answers it; together they narrow it.

- **A linear model with hierarchical features already gives tree-shaped
  directions.** Saxe, McClelland & Ganguli 2019 ([LIT-862](../literature.d/LIT-862.md), read in
  [NOTE-666](../notes.d/NOTE-666.md); [THEORY-186](../theory.d/THEORY-186.md)) generate features by diffusion down a tree, which
  makes them imply one another. The item-similarity eigenvectors then
  respect the tree, as tree wavelets: one direction per branching, splitting
  one subtree from its sibling, with eigenvalues falling with depth. So in
  a linear network, implication among features yields linear directions,
  but they are directions for branch contrasts, not one per attribute. That
  is items against features in a supervised model, not word co-occurrence
  and PMI; whether the same holds for a co-occurrence embedding is still the
  question.
- **The hierarchy may live in distances rather than directions.** Sala et
  al. ([LIT-tmpt10fk](../literature.d/LIT-tmpt10fk.md), [THEORY-tmpzw8vz](../theory.d/THEORY-tmpzw8vz.md)) embed trees in hyperbolic space so
  that every ancestor is nearer than any non-ancestor; Krioukov et al.
  ([LIT-tmp0u9c9](../literature.d/LIT-tmp0u9c9.md), [THEORY-tmp1y92d](../theory.d/THEORY-tmp1y92d.md)) put hierarchy in a radial coordinate.
  So a failure of linear directions would not show the hierarchy is absent
  from an embedding. But a space that can hold a hierarchy does not show
  that a trained one does: Yang et al. ([LIT-tmpocqly](../literature.d/LIT-tmpocqly.md)) find trained
  hyperbolic models order tree levels only 69–75% of the time.
- **A generative model with part–whole implication.** Cagnetta et al.'s
  random hierarchy model ([LIT-tmpz5v25](../literature.d/LIT-tmpz5v25.md), [THEORY-tmpzjtfu](../theory.d/THEORY-tmpzjtfu.md)) has symbols that
  imply their parents, with the hierarchy visible in simple patch–class
  co-occurrence counts. It has no word attributes and no PMI, so a
  derivation built on it would first have to define attributes as
  ancestors.
- **Implication as containment.** Ganea, Bécigneul & Hofmann's hyperbolic
  entailment cones ([LIT-tmp5o7bs](../literature.d/LIT-tmp5o7bs.md), [THEORY-tmp5l4pi](../theory.d/THEORY-tmp5l4pi.md)) encode implication as
  nested regions, a third option beside half-spaces and distances. Cones can
  share descendants, so a partial order fits, but the overlap of two cones
  is not a cone: there are no geometric meets or joins, and so no lattice.
  Trained on the transitive reduction alone, the cones did not recover the
  closure.
- **Hyperbolic curvature is not by itself evidence of hierarchy.** Bianconi
  & Rahmede ([LIT-tmp9eclr](../literature.d/LIT-tmp9eclr.md), [THEORY-tmpp6w9v](../theory.d/THEORY-tmpp6w9v.md)) concede the same grown complex
  fits a sphere with unequal link lengths. Zhou, Smith & Sharpee's olfactory
  space ([LIT-tmpp74b9](../literature.d/LIT-tmpp74b9.md), [THEORY-tmp7qz7l](../theory.d/THEORY-tmp7qz7l.md)) and Zhang et al.'s hippocampus
  ([LIT-tmpvydv3](../literature.d/LIT-tmpvydv3.md)) reject only flat cubes, which leaves a sphere or an
  exponential spread of scales open, and neither recovers a hierarchy from
  the data. Zhou et al. do read linear axes for continuous attributes out of
  co-occurrence correlations in the fitted space.
- **What a coarse-graining keeps depends on what it must stay informative
  about.** Koch-Janusz & Ringel ([LIT-tmprgaew](../literature.d/LIT-tmprgaew.md), [THEORY-tmpsylqv](../theory.d/THEORY-tmpsylqv.md)) and Larsson,
  Maity & Tsiotras ([LIT-tmpbl4wx](../literature.d/LIT-tmpbl4wx.md)) choose levels of a given hierarchy by
  mutual information; the second shows a level can carry nothing while the
  levels below it carry much, so a measurement should score every level.
- **A measuring tool.** Lin et al.'s hyperbolic diffusion embedding
  ([LIT-tmpjwrpt](../literature.d/LIT-tmpjwrpt.md)) recovers a tree distance from multiscale densities, where
  a single Euclidean view on the same features loses most of it. Run on a
  word co-occurrence graph and scored against WordNet hypernymy, it is one
  way to make the measurement asked for above.
