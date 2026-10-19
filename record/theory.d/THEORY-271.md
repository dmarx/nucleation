---
number: 271
status: Proposed
formerly:
- THEORY-tmpkwsi6
promote_when: >-
  A clean restatement and proof of Theorem 1 that handles every
  labelling of subjects to vertices, together with a generalisation
  beyond the one 24-sentence design: any corpus in which each sentence
  expresses one binary aspect of its subject, with d aspects and the
  full 2^d subjects. A proof that raw rows are affine in the aspects
  exactly when each object's sentences are equiprobable would promote
  it. It is refuted by a sentence distribution violating Eq. 5 whose raw
  subject rows still satisfy Definition 1. Further pictures of
  parallelogram-like shapes in natural text cannot settle it, since the
  claim is about the toy corpus's exact condition.
title: "In a toy subject–verb–object corpus whose eight subjects carry every combination of three binary aspects, the subjects' raw co-occurrence rows form a parallelepiped if and only if, for each object, its four sentences are equally probable; any other sentence distribution breaks it"
version: 1
tags:
- representation-learning
- linguistics
date: '2026-10-14'
source:
- LIT-977
summary: >-
  Torii, Maeda and Hidaka (2024), [LIT-977](../literature.d/LIT-977.md), Theorem 1 (§5.5), read in
  full in [NOTE-781](../notes.d/NOTE-781.md). Necessity is sound and short. The case analysis
  over permutations, and sufficiency, are loosely written. Exact shapes,
  raw counts, one design, and independent aspects that make the concept
  lattice Boolean. It says nothing about the logarithm or PMI, about
  noisy or approximate shapes, or about attributes that imply one
  another.
---
<!-- inactive-ok-file: THEORY-183 — Proposed; the accounts this one is set beside -->

# THEORY-271: In a toy subject–verb–object corpus whose eight subjects carry every combination of three binary aspects, the subjects' raw co-occurrence rows form a parallelepiped if and only if, for each object, its four sentences are equally probable; any other sentence distribution breaks it

## Source

Torii, Maeda and Hidaka (2024), "Distributional hypothesis as
isomorphism between word-word co-occurrence and analogical
parallelograms", *PLOS ONE* 19(10): e0312151, [LIT-977](../literature.d/LIT-977.md). Read in full in
[NOTE-781](../notes.d/NOTE-781.md): §5.3 (the toy corpus, Eq. 3, Figs. 5–7), §5.5
(Definition 1, Theorem 1 and its proof, Eqs. 4–18), §5.6.

## What was actually shown

- **The corpus.**
  - 8 subjects, 3 verbs and 6 objects form 24 three-word sentences.
  - Each verb expresses one aspect of its subject through two hidden
    states: Sex, Royalty or Number. Its object is fixed by the subject's
    value on that aspect.
  - Every subject occurs with every verb, and the subjects are all 2³
    aspect combinations.
  - Every pair of words in a sentence co-occurs.
- **Definition 1.** The eight subject rows form a parallelepiped if,
  under some labelling, each of three edge vectors is repeated four
  times (Eq. 4).
- **Theorem 1.** The rows form a parallelepiped if and only if the
  sentence probabilities are equal within each of six groups of four
  (Eq. 5). Each group is the four sentences that end in one object.
- **Necessity.**
  - The edge equalities (Eq. 6) say N C = 0. The kernel of N is spanned
    by the constant vector and the three aspect indicators (Eq. 10), so
    every column of C is affine in the aspects.
  - An object's column is zero on the four subjects that do not take
    it. An affine function on the cube that vanishes on a face is a
    multiple of the opposite face's indicator, so the four non-zero
    entries are equal. This is the reader's restatement of the step.
  - The paper extends the argument over labellings by a case analysis.
- **Sufficiency.** The paper asserts it from the uniform corpus (p_i =
  1/24), whose rows lie in a 3D affine space and form a parallelepiped
  with axes Sex, Royalty and Number (Fig. 7a–b).
- **A numerical check.** One draw of p_i uniform on [0, 1] gives neither
  a parallelepiped nor parallelograms (Fig. 7c).
- **What could have come out otherwise.** The shape might have survived
  some non-uniform distributions beyond Eq. 5. The theorem says it does
  not.

## What this does not say

- **Not about PMI or log counts.** The rows are raw counts. Here aspects
  combine as a mixture: each sentence carries one aspect, so counts add.
  The logarithm would break the shape, and zero cells have no logarithm.
  The paper's real-text analogies use log counts and an SVD, which this
  theorem does not cover.
- **Not about approximate shapes.** It is all or nothing. The authors
  say Eq. 6 has no solution for noisy vectors, and propose without doing
  it a least-squares version for real corpora.
- **Not about natural text.** The only natural-text evidence is one
  "parallelepiped-like" set of Family words in a 2D PCA, which "merely
  demonstrates the 'existence'" of one.
- **Not about hierarchy or exclusion.** All eight combinations occur and
  the aspects are independent, so the concept lattice of the incidence
  is Boolean. What happens when some combinations are missing is not
  asked.
- **Not a group-theoretic result.** The 48 symmetries the paper calls
  "the dihedral group" are the cube's symmetry group. The theorem does
  not depend on the name.

## Connections

- **[THEORY-185](THEORY-185.md) (from [LIT-863](../literature.d/LIT-863.md)).** A rival account for a different
  generative structure, not a second derivation of the same one.
  - There, attributes act multiplicatively, so the *PMI* is affine in
    them for any strengths, and the raw ratio is not.
  - Here, aspects act additively through a mixture over sentences, so
    *raw counts* are affine, and only under the local-uniformity
    condition.
  - Both locate the parallelogram in the data. They disagree on which
    transform reveals it, because they assume different ways for
    attributes to combine.
  - Which assumption fits natural co-occurrence is not tested by either.
- **[QUESTION-025](../questions.d/QUESTION-025.md).** No `answers` link.
  - The toy corpus is the independent, full-hypercube case the question
    says does not settle it.
  - Its one bearing is on the question's third case, attributes that
    "interact in co-occurrence". With the incidence held Boolean, any
    departure from local uniformity breaks the exact shape in raw
    counts.
  - The proof's method, the kernel of the constraint matrix for a target
    shape, would apply to a corpus with implications. The paper names
    that generality but does not use it.
- **[THEORY-183](THEORY-183.md).** That account gets geometry from a translation symmetry
  of co-occurrence. This one gets it from a symmetry of the sentence
  distribution. Both read word geometry as a symmetry of the
  statistics.
