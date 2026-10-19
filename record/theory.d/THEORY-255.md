---
number: 255
status: Active
formerly:
- THEORY-tmpajs5h
title: "In Aerts's subspace model of Hampton's membership data, and in any lattice whose membership weight is order-preserving, whatever its negation, taking concept conjunction and disjunction as meet and join cannot produce overextension or underextension, so a model of the guppy-type deviations must take conjunction as some operation other than the meet or drop the monotone weight, while the Kolmogorov-type deviations can be had from the meet of a non-Boolean subspace lattice"
version: 2
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Narrowed and promoted from Proposed to Active at the owner's direction,
    carrying out the promotion audit's decision
    (record/promotion-audit/decisions/THEORY-255.yaml, batch 018). The
    promote_when asked for a written check of the generalisation from
    Theorem 9 to any lattice with an order-preserving weight. It is met by
    the derivation in the note of 2026-10-19 below and in the decision
    file. The owner's rule of 2026-10-19 (ADR-047): a checked step-by-step
    re-derivation recorded in the decision file meets a promote_when that
    asks for a proof the record does not hold. Its second clause asked for
    a second quantum model confirming that the guppy-type deviations sit
    outside the meet. That follows from the derivation, so what remains is
    which published models drop which assumption. That moves to
    QUESTION-156. The title's "need an emergent concept" overstated
    the theorem, which forces only that the meet or monotonicity be
    dropped, and is narrowed. The promote_when is removed.
tags:
- cognition
- logic
- quantum-foundations
date: '2026-10-14'
source:
- LIT-934
summary: >-
  Aerts (2009), [LIT-934](../literature.d/LIT-934.md), Theorem 9 and §§2.2–3.3, read in full in
  [NOTE-808](../notes.d/NOTE-808.md). The impossibility is a proof, and it needs only that
  membership is monotone in the subspace. The fits that place the k-type
  deviations in a tilted subspace lattice and the ∆-type ones in an
  emergent sector are models with free parameters, not tests. Negation
  appears only as the orthocomplement used to derive the conjunction
  model from the disjunction model; no negated concept is measured.
---
<!-- inactive-ok-file: CLAIM-119 CLAIM-038 THEORY-013 — Proposed; the claims and account this bears on, named and not leaned on -->
<!-- inactive-ok-file: LIT-316 — Unavailable; Busemeyer and Bruza, named as what would settle this, not leaned on -->

# THEORY-255: In Aerts's subspace model of Hampton's membership data, and in any lattice whose membership weight is order-preserving, whatever its negation, taking concept conjunction and disjunction as meet and join cannot produce overextension or underextension, so a model of the guppy-type deviations must take conjunction as some operation other than the meet or drop the monotone weight, while the Kolmogorov-type deviations can be had from the meet of a non-Boolean subspace lattice

## Source

Aerts (2009), [LIT-934](../literature.d/LIT-934.md), *Journal of Mathematical Psychology* 53(5),
read in full in [NOTE-808](../notes.d/NOTE-808.md): Theorems 1–6 (§§1.3–1.4, Appendices A–B),
§2.2 (eqs. 47–56), Theorem 9 (§2.3, Appendix E), §§3.1–3.3 and
Tables 3–4.

## What was actually shown

**Two kinds of non-classical item.** For an item's weights µ(A), µ(B)
and µ(A and B) there is a Kolmogorovian space with µ(A and B) the
probability of the intersection event iff ∆_c = µ(A and B) −
min(µ(A), µ(B)) ≤ 0 and k_c = 1 − µ(A) − µ(B) + µ(A and B) ≥ 0
(Theorems 1–3), and dually for "or" (Theorems 4–6). Hampton's data fail
both ways. Overextension or underextension (∆-type) is the commoner,
the guppy effect proper: Cuckoo is rated 0.575 a Pet but 0.842 a
"Bird and Pet". A negative k (k-type) occurs in many disjunction items:
Almond is 0.2 a Fruit, 0.1 a Vegetable and 0.425 a "Fruit or
Vegetable".

**The lattice can carry the k-type items.** Represent A and B as
2-dimensional subspaces of ℝ⁴ meeting in one axis, tilted by an angle θ
(eqs. 47–48). The condition k_c ≥ 0 is replaced by
q_conj(A, B, θ) ≥ 0 (eq. 54), which reduces to k_c at θ = 90° and is
satisfiable for other θ by items with k_c < 0. Horse Cart and Dishwasher
for Machine and Vehicle are fitted at θ = 80.9026°. The subspaces are
then non-commuting and their lattice is not Boolean.

**The lattice cannot carry the ∆-type items.** Theorem 9: if concepts are
subspaces, "A and B" is A ∩ B and "A or B" is A + B, then for every unit
vector x, ‖P_{A∩B}x‖² ≤ ‖P_A x‖² and ‖P_A x‖² ≤ ‖P_{A+B}x‖², so
∆_c ≤ 0 and ∆_d ≤ 0. This could have failed only if projection weights
were not monotone in the subspace, and they are.

**What carries them instead.** The model adds a second ℝ⁴ and a fixed
2-dimensional "emergent concept" subspace C per pair, so that
µ(A and B) = x²_AB + c₅² + c₆² and µ(A or B) = x²_AB + x²_AB′ + x²_A′B +
c₅² + c₆² (eqs. 61–62). C is not A ∩ B or A + B. With it, every item in
Hampton's lists gets a vector (Tables 3–4).

**Where negation enters.** Only in §3.3. The conjunction model for A, B is
the disjunction model for "hypothetical concepts" A′, B′ with
µ(A′) = 1 − µ(A), µ(B′) = 1 − µ(B) and µ(A′ or B′) = 1 − µ(A and B)
(eqs. 119–125). A′ is the orthogonal complement of A, and the emergent
subspace of "A′ or B′" is the complement of C in the second sector. So
the model is closed under De Morgan with the orthocomplement as
negation, by construction.

## What this does not say

- **That concepts form an orthocomplemented lattice whose negation was
  tested.** No negated concept is measured. The orthocomplement in §3.3
  is a calculational device, and its weight 1 − µ is assumed.
- **That the emergent-concept model is right.** It is a fit: one free
  parameter per item, two angles per pair, fixed by a stipulated
  "modularity condition" (eq. 117; unrelated to the modular law) and a
  halfway rule for classical items. No held-out prediction is made. The
  two-layer reading of thought is an interpretation.
- **That the impossibility is special to subspaces, or to the
  orthocomplement.** This is the record's inference, not the paper's
  statement: the proof of Theorem 9 uses only that the weight is
  order-preserving and that "and" is a lower bound of both concepts. So
  the same follows for a Boolean algebra, an orthomodular lattice or a
  Heyting algebra with any monotone valuation. That generalisation is
  checked in the note of 2026-10-19 below.
- **That the data are contextual.** Non-classical here means no single
  Kolmogorovian space in which "A and B" is the intersection event. Drop
  that identification, as Contextuality-by-Default does ([LIT-264](../literature.d/LIT-264.md)), and
  the criterion changes.

## Connections

No relations are declared.

- **[QUESTION-055](../questions.d/QUESTION-055.md).** The question asks which negation a non-Boolean
  lattice of communicative categories carries. This account adds a
  constraint that the question does not state: if categories blend as
  Hampton's concepts do, with a blend counted as a better member than one
  of its parts, the blend cannot be the lattice meet under any of the
  three negations. It does not choose among them, and so is not declared
  as an answer.
- **[CLAIM-119](../claims.d/CLAIM-119.md).** Its concept lattice would need a combination operation
  other than the meet to hold such blends. [CLAIM-038](../claims.d/CLAIM-038.md)'s context-indexed
  object, and the Heyting logic of [THEORY-037](THEORY-037.md), face the same limit,
  because their meets are monotone too.
- **[THEORY-041](THEORY-041.md).** Aerts's "modularity condition" is not the modular law;
  the finite-dimensional subspace lattice he uses is modular for the
  ordinary reason.
- **[CLAIM-041](../claims.d/CLAIM-041.md) and [THEORY-013](THEORY-013.md).** Consistent with both: this is a claim
  about which representations fit, not a demonstration of contextuality.
- **[LIT-340](../literature.d/LIT-340.md), [LIT-312](../literature.d/LIT-312.md) ([NOTE-294](../notes.d/NOTE-294.md), [NOTE-299](../notes.d/NOTE-299.md)).** Aerts and Gabora posit an
  orthocomplemented lattice of contexts and use a commuting, Boolean
  model. This paper is where non-commuting subspaces are actually put to
  work on concept data, and it confines them to the k-type items.

## Note of 2026-10-19: the generalisation, checked

Written for the promotion audit's batch 018
(record/promotion-audit/decisions/THEORY-255.yaml).

1. Let (L, ≤) be any lattice and µ: L → [0, 1] any order-preserving
   weight. No negation, complement or distributive law is assumed.
2. A ∧ B ≤ A and A ∧ B ≤ B, so µ(A ∧ B) ≤ min(µ(A), µ(B)): ∆_c ≤ 0
   when "and" is the meet. No overextension.
3. A ≤ A ∨ B and B ≤ A ∨ B, so µ(A ∨ B) ≥ max(µ(A), µ(B)): ∆_d ≤ 0
   when "or" is the join. No underextension.
4. Theorem 9 is the case of subspaces of ℝⁿ with µ(S) = ‖P_S x‖². That
   weight is order-preserving, because S ⊆ T gives P_S = P_S P_T and so
   ‖P_S x‖ ≤ ‖P_T x‖.
5. So a model that reproduces Cuckoo (µ(Pet) = 0.575,
   µ(Bird and Pet) = 0.842) must drop conjunction-as-meet or the monotone
   weight. Aerts drops the first, with an emergent subspace.
6. The k-type clause is possible with the meet kept. In ℝ², take lines A
   and B at angle θ < 90°, so A ∧ B = {0}, and x the unit vector on their
   bisector. Then µ(A) = µ(B) = cos²(θ/2) > ½ and µ(A ∧ B) = 0, so
   k_c = 1 − 2cos²(θ/2) < 0. Aerts's fitted pair (Machine, Vehicle at
   θ = 80.9026° in ℝ⁴) is an instance. That every k-type item in
   Hampton's data can be fitted this way is not shown: [NOTE-808](../notes.d/NOTE-808.md) grades it
   moderate, worked for one pair.
