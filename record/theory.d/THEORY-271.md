---
number: 271
status: Active
formerly:
- THEORY-tmpkwsi6
title: "In a toy subject–verb–object corpus whose eight subjects carry every combination of three binary aspects, the subjects' raw co-occurrence rows form a parallelepiped if and only if, for each object, its four sentences are equally probable; any other sentence distribution breaks it"
version: 2
history:
- version: 2
  date: '2026-10-20'
  note: >-
    Promoted, carrying out the promotion audit's decision for THEORY-271
    (batch 050, ADR-047 v2). The dated note below proves Theorem 1 for every
    labelling of subjects to vertices and for any number d of aspects with
    the full 2^d subjects, which meets both parts of the former
    promote_when, and checks the three-aspect case numerically over all
    40,320 labellings. The title is unchanged.
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

## Note of 2026-10-20: Theorem 1 for every labelling and any number of aspects

Promotion audit, batch 050.

**Setting.**
- Subjects are s ∈ {0,1}^d, all 2^d of them. There is one verb per aspect
  v, and two objects o(v,b) per verb, b ∈ {0,1}.
- Sentence (s, v, o(v, s_v)) has probability p(s,v).
- The raw row of subject s has entry p(s,v) at verb v and
  p(s,v)·1[s_v = b] at object o(v,b). Subjects never co-occur.
- The rows form a parallelepiped (Definition 1) if, for some bijection σ
  from the cube's vertices to the subjects, x ↦ row(σ(x)) is affine in x.
  On the cube, equal edge vectors along each axis are the same thing.

**Sufficiency.** Suppose p(s,v) = q(v, s_v) for every object (Eq. 5).
Take σ to be the identity.
- The verb entry is q(v,0)(1 − s_v) + q(v,1)s_v, and the object entries
  are q(v,1)s_v and q(v,0)(1 − s_v). All are affine in s.
- Aspect k's edge vector is supported on verb k and its two objects. So
  the d edge vectors have disjoint supports, and they are independent
  whenever every verb has positive probability.

**Necessity, for any σ.**
1. Fix an object o(v,b) and let f(x) be its column, read through σ. Then
   f is affine and nonnegative on the vertices, hence on the whole cube.
2. If f is not identically zero, its zero set on the cube is the cube's
   intersection with a supporting hyperplane. That is a face, and the zero
   vertices are the face's vertices.
3. f vanishes on at least the 2^(d−1) subjects with s_v ≠ b. A face with
   at least 2^(d−1) vertices that is not the whole cube is a facet, so the
   face is a facet {x_k = c} and holds exactly those subjects.
4. An affine function vanishing on {x_k = c} is a multiple of x_k − c, so
   it is constant on the opposite facet. So the 2^(d−1) sentences ending
   in o(v,b) are equally probable.
5. If f is identically zero, they are all 0.

The verb columns are sums of two object columns, so they add nothing. This
one argument replaces the paper's case analysis over permutations and
holds for every d.

**A numerical check (d = 3).** Build the rows as above. For each of the
8! = 40,320 permutations, test whether the rows equal their projection
onto span{1, x₁, x₂, x₃} (tolerance 10⁻⁹).
- A distribution meeting Eq. 5 forms a parallelepiped, also with one
  object's group at zero.
- One sentence perturbed by 0.1% forms none.
- A uniform random p forms none.
