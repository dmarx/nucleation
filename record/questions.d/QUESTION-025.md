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
<!-- inactive-ok-file: THEORY-tmpyaqz7 — Proposed; cited as partial evidence, not as settled -->
<!-- inactive-ok-file: THEORY-186 THEORY-196 THEORY-195 THEORY-188 THEORY-189 THEORY-193 THEORY-191 THEORY-194 — Proposed; cited as partial evidence toward an answer, not as settled -->
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
  al. ([LIT-874](../literature.d/LIT-874.md), [THEORY-196](../theory.d/THEORY-196.md)) embed trees in hyperbolic space so
  that every ancestor is nearer than any non-ancestor; Krioukov et al.
  ([LIT-865](../literature.d/LIT-865.md), [THEORY-188](../theory.d/THEORY-188.md)) put hierarchy in a radial coordinate.
  So a failure of linear directions would not show the hierarchy is absent
  from an embedding. But a space that can hold a hierarchy does not show
  that a trained one does: Yang et al. ([LIT-871](../literature.d/LIT-871.md)) find trained
  hyperbolic models order tree levels only 69–75% of the time.
- **A generative model with part–whole implication.** Cagnetta et al.'s
  random hierarchy model ([LIT-877](../literature.d/LIT-877.md), [THEORY-195](../theory.d/THEORY-195.md)) has symbols that
  imply their parents, with the hierarchy visible in simple patch–class
  co-occurrence counts. It has no word attributes and no PMI, so a
  derivation built on it would first have to define attributes as
  ancestors.
- **Implication as containment.** Ganea, Bécigneul & Hofmann's hyperbolic
  entailment cones ([LIT-866](../literature.d/LIT-866.md), [THEORY-189](../theory.d/THEORY-189.md)) encode implication as
  nested regions, a third option beside half-spaces and distances. Cones can
  share descendants, so a partial order fits, but the overlap of two cones
  is not a cone: there are no geometric meets or joins, and so no lattice.
  Trained on the transitive reduction alone, the cones did not recover the
  closure.
- **Hyperbolic curvature is not by itself evidence of hierarchy.** Bianconi
  & Rahmede ([LIT-867](../literature.d/LIT-867.md), [THEORY-193](../theory.d/THEORY-193.md)) concede the same grown complex
  fits a sphere with unequal link lengths. Zhou, Smith & Sharpee's olfactory
  space ([LIT-872](../literature.d/LIT-872.md), [THEORY-191](../theory.d/THEORY-191.md)) and Zhang et al.'s hippocampus
  ([LIT-876](../literature.d/LIT-876.md)) reject only flat cubes, which leaves a sphere or an
  exponential spread of scales open, and neither recovers a hierarchy from
  the data. Zhou et al. do read linear axes for continuous attributes out of
  co-occurrence correlations in the fitted space.
- **What a coarse-graining keeps depends on what it must stay informative
  about.** Koch-Janusz & Ringel ([LIT-873](../literature.d/LIT-873.md), [THEORY-194](../theory.d/THEORY-194.md)) and Larsson,
  Maity & Tsiotras ([LIT-868](../literature.d/LIT-868.md)) choose levels of a given hierarchy by
  mutual information; the second shows a level can carry nothing while the
  levels below it carry much, so a measurement should score every level.
- **In token co-occurrence, a hierarchy shows as partitions and fades with
  depth.** Cagnetta & Wyart ([LIT-tmpudm1k](../literature.d/LIT-tmpudm1k.md), [THEORY-tmpyaqz7](../theory.d/THEORY-tmpyaqz7.md)) generate
  sequences from a random hierarchy and measure their token–token
  correlations, which fall by about a factor m per level of the common
  ancestor; so a finite corpus shows only the shallow levels. Tuples with
  one parent have identical co-occurrence rows, so the hierarchy shows as
  nested partitions rather than one direction per ancestor, and the paper
  notes that a parent is not a linear feature of its input tuple until
  after a nonlinear layer. That is the nearest the record comes to the
  derivation this question asks for, on part–whole rather than attribute
  hierarchies.
- **Hyperbolic half-spaces as a probe.** Ganea, Bécigneul & Hofmann's
  hyperbolic neural networks ([LIT-tmpadlu8](../literature.d/LIT-tmpadlu8.md)) separate WordNet subtrees with
  geodesic hyperplanes better than Euclidean ones do, in embeddings trained
  on hypernym edges. Probing a co-occurrence embedding with both kinds of
  half-space is one way to make the measurement asked for above.
- **A measuring tool.** Lin et al.'s hyperbolic diffusion embedding
  ([LIT-870](../literature.d/LIT-870.md)) recovers a tree distance from multiscale densities, where
  a single Euclidean view on the same features loses most of it. Run on a
  word co-occurrence graph and scored against WordNet hypernymy, it is one
  way to make the measurement asked for above.
