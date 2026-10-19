---
number: 315
status: Active
formerly:
- THEORY-tmpkfnig
title: 'For a state whose four-state reflection orbit is realizable, generalized noncontextuality bounds two binary predictabilities by |⟨X⟩| + |⟨Z⟩| ≤ 1, so the form of a predictability trade-off, not its existence, can witness contextuality'
version: 2
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Promoted from Proposed to Active at the owner's direction, carrying out
    the promotion audit's decision
    (record/promotion-audit/decisions/THEORY-315.yaml, batch 019, ADR-047).
    The promote_when asked for "an independent derivation of |⟨X⟩| + |⟨Z⟩|
    ≤ 1 from the A²₁-orbit condition". One is given in the note of
    2026-10-19 below. It differs from the paper's Appendix A: it uses
    neither outcome determinism nor measurement noncontextuality, only
    preparation noncontextuality for the one equivalence of Eq. 11. Under
    ADR-047 v2 (the owner's rule of 2026-10-19) that meets the condition,
    and the promote_when is removed. The title is unchanged.
tags:
- contextuality
- quantum-foundations
date: '2026-10-14'
source:
- LIT-980
summary: >-
  Catani, Leifer, Scala, Schmid and Spekkens (2022), [LIT-980](../literature.d/LIT-980.md), read in
  [NOTE-825](../notes.d/NOTE-825.md). Proved analytically, with a saturating model, for
  preparation noncontextuality and exact operational equivalence. The
  bound constrains a whole uncertainty relation only in a theory where
  every state has the orbit; the qubit's circle violates it, and a
  classical theory without the symmetry escapes it. It needs no
  perfectly distinguishable states, and it is not a sheaf or
  Kochen–Specker criterion.
answers:
- QUESTION-067
---
<!-- inactive-ok-file: THEORY-010 CLAIM-009 CLAIM-037 CLAIM-044 CLAIM-142 CLAIM-046 — Proposed; theories and claims this account bears on, open -->

# THEORY-315: For a state whose four-state reflection orbit is realizable, generalized noncontextuality bounds two binary predictabilities by |⟨X⟩| + |⟨Z⟩| ≤ 1, so the form of a predictability trade-off, not its existence, can witness contextuality

## Source

Catani, Leifer, Scala, Schmid and Spekkens (2022), *Physical Review
Letters* 129, 240401, [LIT-980](../literature.d/LIT-980.md), read in full in [NOTE-825](../notes.d/NOTE-825.md): Eqs. 1–13,
Appendix A (the proof), Appendix B (the linear-program cross-check),
Appendix C (three measurements).

## What was actually shown

**The setting.** A prepare-measure scenario with two binary measurements
X and Z and four preparations. Noncontextuality is Spekkens's, for
preparations only: operationally equivalent preparations, those with the
same statistics for every measurement, get the same distribution over
ontic states (Eq. 8). A state s1 is *A²₁-orbit-realizable* when there
are states s2, s3, s4 with the same |⟨X⟩| and |⟨Z⟩| and the other three
sign patterns (Eq. 10), and ½s1 + ½s3 = ½s2 + ½s4 (Eq. 11).

**The inequality (Eq. 12, Appendix A).** For such a state, every
preparation-noncontextual model satisfies |⟨X⟩| + |⟨Z⟩| ≤ 1. The proof is
analytic and short. With four outcome-deterministic ontic states and
μ1 = (a, b, c, d), the constraints give ⟨X⟩ + ⟨Z⟩ = 2(b − c) ≤ 1 − c ≤ 1
(Eq. A33). The bound is tight (Eqs. A35–A38). It is also the reduction,
under the orbit condition, of the eight inequalities Schmid, Spekkens and
Wolfe derived by linear program for the same equivalence (Appendix B).
This is what could have come out otherwise: a noncontextual model
exceeding the diamond would refute it, and the explicit
parameterization rules one out.

**From one state to a theory.** In a theory where every state is
orbit-realizable (A²₁ symmetry), the inequality bounds the uncertainty
relation itself. The qubit has the symmetry and the relation
⟨X⟩² + ⟨Z⟩² ≤ 1, a circle, so it violates the bound everywhere except
where one predictability is 1, by up to √2. The qubit stabilizer theory
saturates the bound, and it has a noncontextual model. The gbit, also
symmetric, reaches 2. The simplicial theory of two classical bits has the
gbit's relation but not the symmetry. The states that reach joint
predictability 1, its vertices, have equal-predictability counterparts
but fail Eq. 11, so the bound does not apply to them.

**So:** an uncertainty relation as such does not mark nonclassicality,
since the stabilizer theory has one and a noncontextual model. What
marks it, given the symmetry, is joint predictability above the linear
curve.

## What this does not say

- **It does not say that any trade-off curve above the line refutes
  noncontextuality.** The bound holds only for orbit-realizable states.
  Without the equivalence of Eq. 11, perfect joint predictability is
  classical, as the simplicial theory shows.
- **It does not say that unpredictability is classical and
  predictability nonclassical in general.** The authors' reversal holds
  within theories with A²₁ symmetry.
- **It does not treat inexact equivalence.** Eq. 11 is used as an
  equality. The letter says the inequality "is noise-robust, and can
  therefore be tested experimentally", but gives no robustness analysis.
- **It is not a sheaf or Kochen–Specker result.** X and Z are never
  measured together. In the record's own reading (not the paper's), the
  cover {X}, {Z} has no overlap, so a global-extension test is vacuous
  in exactly the scenario where this bound bites.
- **It does not say that one binary measurement can witness preparation
  contextuality.** It needs two measurements and four preparations. By
  the reader's argument in [NOTE-825](../notes.d/NOTE-825.md), one binary measurement never
  can.
- **Satisfying the bound does not establish a noncontextual model.**
  The η-depolarized qubit satisfies it for η ≥ 1 − 1/√2 but is cited as
  noncontextual only for η ≥ 2/3.
- **The three-measurement analogue, |⟨X⟩| + |⟨Y⟩| + |⟨Z⟩| ≤ 1, is
  verified by computer**, not proved in the letter, and is not part of
  this account.

## Connections

- **[QUESTION-067](../questions.d/QUESTION-067.md) (answers, in part).** It asks for the equivalences a
  pragmatic test would assume and the inequality they imply, apart from
  the sheaf criterion. This is a worked instance: two binary probes, four
  renderings with equal predictabilities and flipped signs, and one
  equivalence of equal mixtures. It needs no perfectly distinguishable
  pairs, which lifts one of the four conditions the question's note of
  2026-10-14 sets. The other three stand: equivalence over every probe
  ([CLAIM-142](../claims.d/CLAIM-142.md) and [CLAIM-046](../claims.d/CLAIM-046.md)'s probe-relative relation qualifies only if
  the probes are tomographically complete for the renderings), the
  unquotiented description, and exact equivalence.
- **[THEORY-011](THEORY-011.md).** A further qubit-dimension proof of preparation
  contextuality, without Kochen–Specker structure, which fits its claim
  that the generalized notion is strictly broader.
- **[THEORY-015](THEORY-015.md).** Compatible. This account concerns preparation
  noncontextuality alone, and does not use outcome determinism as an
  assumption.
- **[THEORY-016](THEORY-016.md).** The noncontextual models of the stabilizer and
  simplicial theories that saturate or escape the bound are instances of
  its positive representations.
- **[THEORY-010](THEORY-010.md).** Agrees with its point that unpredictability after a
  change of context has a classical model, and locates what does not:
  excess joint predictability under the symmetry.
- **[THEORY-231](THEORY-231.md).** That account cites [LIT-945](../literature.d/LIT-945.md) for prepare-measure
  scenarios admitting noncontextuality no-goes and no Bell-like ones.
  This is such a no-go, stated as an inequality.
- **[CLAIM-009](../claims.d/CLAIM-009.md), [CLAIM-037](../claims.d/CLAIM-037.md), [CLAIM-044](../claims.d/CLAIM-044.md).** Their contextuality is the
  global-extension kind. A violation of this bound would not support them
  as worded.

## Note of 2026-10-19: an independent derivation of the bound

Written for the promotion audit's batch 019 ([ADR-047](../decisions.d/ADR-047.md)). It is also in
record/promotion-audit/decisions/THEORY-315.yaml.

A preparation-noncontextual model gives preparation s_i a distribution
μ_i over ontic states λ. X and Z get response functions ξ_X(λ) and
ξ_Z(λ) in [0, 1]. Write a = 2ξ_X − 1 and b = 2ξ_Z − 1, so |a| ≤ 1 and
|b| ≤ 1 pointwise, with ⟨X⟩_s = ∫ a dμ_s and ⟨Z⟩_s = ∫ b dμ_s. Treat the
μ_i as densities with respect to their sum. By Eq. 10,
⟨X⟩s1 = −⟨X⟩s2 = −⟨X⟩s3 = ⟨X⟩s4 = x and
⟨Z⟩s1 = ⟨Z⟩s2 = −⟨Z⟩s3 = −⟨Z⟩s4 = z.

1. **Noncontextuality.** Eq. 11 is an operational equivalence, so
   μ1 + μ3 = μ2 + μ4 =: ν, of total mass 2.
2. **Two differences.** Put u = μ1 − μ3 and v = μ4 − μ2. The μ_i are
   non-negative, so |u| ≤ μ1 + μ3 = ν and |v| ≤ μ2 + μ4 = ν pointwise.
   The second inequality is where step 1 is used.
3. **An identity.** By Eq. 10, ∫ua = 2x, ∫va = 2x, ∫ub = 2z and ∫vb = −2z.
   So for any signs σ, τ ∈ {±1},
   σx + τz = ¼ ∫ [u(σa + τb) + v(σa − τb)].
4. **The bound.** Pointwise, |σa + τb| + |σa − τb| = 2 max(|a|, |b|) ≤ 2.
   So the integrand is at most 2ν, and σx + τz ≤ ¼ · 2 · ∫ν = 1. Choosing
   σ and τ as the signs of x and z gives |⟨X⟩| + |⟨Z⟩| ≤ 1.

Without step 1, step 2 gives only |v| ≤ μ2 + μ4, and the same steps give
2, the gbit's value. That shows where noncontextuality does the work.
Neither outcome determinism nor any assumption about measurements is
used. The paper fixes four outcome-deterministic ontic states. Tightness
is the paper's saturating model (Eqs. A35–A38, checked by hand in
[NOTE-825](../notes.d/NOTE-825.md)).
