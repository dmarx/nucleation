---
status: Open
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
<!-- inactive-ok-file: THEORY-185 THEORY-183 CLAIM-119 LIT-267 — Proposed; cited as the open accounts this question joins -->

# QUESTION-tmpynu0z: Do correlated or hierarchical attributes in co-occurrence statistics still give linear attribute directions in an embedding, and with them a concept lattice that is not Boolean?

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
