---
status: Answered
title: 'When a network''s architecture can represent a structured system''s renormalization step exactly, must training by distribution fitting make the variables it represents the system''s relevant ones?'
version: 1
tags:
- natural-sciences
- representation-learning
- mathematics
date: '2026-10-27'
line: learned-structure
refines:
- QUESTION-060
summary: >-
  The representability part of QUESTION-060, split off by the status
  review of 2026-10-27 under ADR-049, because THEORY-197 (Active) settles
  it, in the negative. Mehta and Schwab's RBM–renormalization
  correspondence is an identity of parametrizations, and an exact RG step
  is a perfect fit of the data distribution. Away from that point a
  contrastive-divergence RBM spends its hidden units on noise, not on the
  relevant fields. The architecture's match does not fix what training
  keeps.
---

# QUESTION-tmpxjw51: When a network's architecture can represent a structured system's renormalization step exactly, must training by distribution fitting make the variables it represents the system's relevant ones?

## The question

QUESTION-060 asks whether the variables a trained network represents are
fixed by its objective or by what its architecture can represent, and when
they coincide with the system's relevant variables. One candidate
condition is that the architecture can express the system's own
coarse-graining exactly. This question asks whether that is enough.

## The answer

THEORY-197, Active, answers no:

- **The identity.** With the RG kernel T = −E + H, Kadanoff's coarse
  Hamiltonian equals the RBM's hidden-marginal Hamiltonian for every
  parameter value, and an exact RG step is exactly a perfect fit of the
  data distribution (Mehta and Schwab, Eqs. 18–22).
- **The counterexample.** Koch-Janusz and Ringel train an RBM by
  contrastive divergence on fully packed dimers with added decoupled spin
  pairs. It spends its hidden units on the noise, then on columnar
  textures, and not on the staggered patterns that carry the RG-relevant
  fields.

So a network that can represent the renormalization need not learn it.
A negative answer by one counterexample, for Boltzmann machines. When
distribution-fitting networks do keep the relevant variables remains
QUESTION-060's.
