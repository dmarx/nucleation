---
number: 302
status: Active
formerly:
- CLAIM-tmpvdl53
title: 'Equivalence under feasible tests can be much coarser than statistical equivalence:
  there are ensembles almost disjoint from uniform that no polynomial-size test
  tells apart from it, and efficiently samplable ensembles of this kind exist if
  pseudorandom generators do'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in Goldreich's counting argument (Proposition 3.3 of the 1995 draft)
  or in the record's bound for a generator's image. The non-existence of secure
  pseudorandom generators would remove only the efficiently samplable witness, not
  the separation.
tags:
- mathematics
- information-theory
- epistemology
date: '2026-10-15'
line:
- formal-apparatus
grounds:
- CASE-083
- THEORY-357
- THEORY-352
complements:
- CLAIM-264
summary: >-
  A15's witness for "Complexity changes what we mean by an observable", which the
  owner asked to have developed at U15, corrected by the reading of Goldreich (NOTE
  of 2026-10-15). [CLAIM-264](CLAIM-264.md) says agreement on a restricted probe family is coarser
  than identity; feasibility gives a restriction that is forced, not chosen. The
  separation itself is unconditional: a counting argument gives ensembles supported
  on at most 2^(n/2) strings that no circuit of size 2^(n/8) tells from uniform.
  Only an efficiently samplable witness needs an assumption, and a secure pseudorandom
  generator supplies one. All of it is asymptotic, about ensembles indexed by n.
supports:
- CLAIM-304
---
<!-- inactive-ok-file: CLAIM-264 — Proposed; open claims and accounts cited as open, nothing here rests on their being settled -->

# CLAIM-302: Equivalence under feasible tests can be much coarser than statistical equivalence: there are ensembles almost disjoint from uniform that no polynomial-size test tells apart from it, and efficiently samplable ensembles of this kind exist if pseudorandom generators do

## The claim

A15 §1: for observation channels K_x, K_x′ and a test family F_r, let
d_r(x, x′) = sup over f in F_r of |E[f | x] − E[f | x′]|. Over all tests
this is total variation. Restricting the family cannot increase it, and
nested families give a distance that grows with r. "The conclusion is not
that the states became different. It's that a new distinction became
operationally observable."

"Efficient" and "negligible" mean something only for ensembles, sequences
of distributions indexed by n (Goldreich, Definition 3.2 in the 1995
draft). For any fixed n a large enough finite test separates any two
different distributions. The claim is about ensembles.

**Unconditionally.** Goldreich's Proposition 3.3, credited to Goldreich and
Krawczyk after Yao, proves by a Chernoff and union bound that some ensemble
X with X_n supported on at most 2^(n/2) strings fools every circuit of size
2^(n/8) with gap below 2^(−n/8). Its total variation from uniform is at least
1 − 2^(−n/2). The book: the separating test "is (necessarily) impossible to
compute in polynomial-time." That X cannot be sampled efficiently: "One of
the two ensembles is not constructible in polynomial-time."

**Efficiently samplable, if pseudorandom generators exist.** The witness A15
gave ([CASE-083](../cases.d/CASE-083.md)). Let G: {0,1}ⁿ → {0,1}²ⁿ be a secure pseudorandom generator
(Goldreich's Definition 3.9 with l(n) = 2n), P_n = G(Uₙ), Q_n = U₂ₙ. G has at
most 2ⁿ outputs, so TV(P_n, Q_n) ≥ 1 − 2⁻ⁿ, checked here (the book states the
bound only as ½, and its "statistical difference" omits the factor ½ of
total variation). Every probabilistic polynomial-time test has negligible
advantage, by definition. The book cites Goldreich (1990) for the sharper
fact, not read here, that an efficiently samplable pair of this kind exists
if and only if one-way functions do. That note ([LIT-1053](../literature.d/LIT-1053.md)) could not
be fetched. Håstad, Impagliazzo, Levin and Luby ([LIT-1051](../literature.d/LIT-1051.md), read in
[NOTE-880](../notes.d/NOTE-880.md)) settle the attribution: they credit Goldreich's note with the
equivalence to pseudorandom generators, and prove that pseudorandom
generators exist if and only if one-way functions do (their Theorem 6.2.2,
with uniform reductions). The book's "one-way functions" combines the two.
This claim's condition "if pseudorandom generators exist" can be read "if
one-way functions exist".

**Postprocessing.** A15 added the invariance that keeps this from being
arbitrary: an efficient transformation applied to both ensembles preserves
indistinguishability, since a distinguisher for the outputs composed with
the transformation would distinguish the inputs. Goldreich sets this as an
exercise (§3.8.4, Exercise 1), and the one-line composition is its proof.

## Why it is Active

The unconditional half is a theorem of the source, read in the author's
1995 draft ([LIT-1061](../literature.d/LIT-1061.md)); the samplable half is the definition of a secure
generator plus a counting bound checked here, and is conditional, as the
title says. Neither was checked against the printed 2001 volume.

## What it does not say

- Not that a distinction no efficient test sees is unreal. A15: "The
  distributions are not identical."
- Not that it depends on the objects alone. It is relative to the
  computational model, the encoding and any auxiliary information; an
  expensively computed label makes the same ensembles trivially
  distinguishable (A15 §3). Goldreich's §3.8.4 Exercise 11 asks the same
  of a permutation that is not efficiently computable.
- Not quantum contextuality, ontological identity or pragmatic
  equivalence. A14: "Each stronger interpretation requires its own
  arguments and tests."
