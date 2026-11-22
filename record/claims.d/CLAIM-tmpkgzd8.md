---
status: Proposed
title: 'The embedding of a network that has learned a non-abelian group carries the group''s irreducibles as a group-Fourier power spectrum concentrated on the faithful ones, with the trivial component near zero and the sign representation smallest, the dominant faithful irreducible varying with the seed'
version: 1
role: thesis
warrant: empirical
defeated_if: >-
  A network that has learned a non-abelian group (it generalises and its
  argmax operation is the true group) whose embedding power, measured in the
  isotypic basis recovered from the group, sits mainly on the trivial
  representation, or is spread across the irreducibles with no concentration
  on the faithful ones, or concentrates on a non-faithful representation such
  as the sign.
tags:
- representation-learning
- learning-theory
- mathematics
date: '2026-11-22'
line:
- learned-structure
complements:
- CLAIM-tmpie2v3
bears_on:
- QUESTION-058
grounds:
- CASE-tmpjgjtj
---

<!-- inactive-ok-file: CLAIM-tmpie2v3 — Proposed; the sibling finding this one complements, filed in the same batch -->

# CLAIM-tmpkgzd8: The embedding of a network that has learned a non-abelian group carries the group's irreducibles as a group-Fourier power spectrum concentrated on the faithful ones, with the trivial component near zero and the sign representation smallest, the dominant faithful irreducible varying with the seed

## The claim

Once the irreducibles are in hand (CLAIM-tmpie2v3), the learned embedding can
be read in their basis: each column of the embedding is a function on the
group, and its squared norm splits across the isotypic blocks — the group-
Fourier power spectrum. In CASE-tmpjgjtj this spectrum is concentrated on the
*faithful* irreducibles. The trivial (constant) component is ≈ 0, since weight
decay centres the embeddings; the sign representation carries the least
non-trivial power; S3 places ≈ 78% of its non-trivial power on the
two-dimensional standard irreducible, and S4 ≈ 78% on its two three-
dimensional irreducibles. Which of several faithful irreducibles dominates
differs from seed to seed, so the concentration-on-faithful pattern is robust
while the particular dominant block is not — a weak, approximate universality.

That the faithful irreducibles dominate is what lets the elements be told
apart: a non-faithful representation (trivial, or sign, which sees only
parity) collapses distinct elements, so a representation that distinguishes
all of `|G|` elements must load the faithful irreducibles. The weights thus
carry the group's structure in the specific form representation theory
predicts, not merely some learned geometry.

## What it does not say

It does not claim a fixed spectrum: the split across the faithful irreducibles
is seed-dependent, and only the trivial-near-zero, faithful-dominant shape
recurs. It does not say the network represents elements *solely* through the
embedding — the hidden layer and unembedding also carry structure, measured
here only in passing. It is evidence from two non-abelian groups at a few
seeds, not a theorem.

The wording is the assistant's (Claude, in this session); adopting it is the
owner's call.
