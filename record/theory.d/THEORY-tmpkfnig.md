---
status: Proposed
promote_when: >-
  A check of the main result by someone other than its authors: an
  independent derivation of |⟨X⟩| + |⟨Z⟩| ≤ 1 from the A²₁-orbit
  condition, or an experiment that tests it with the equivalence of
  Eq. 11 certified, as Mazurek et al. certified earlier preparation
  inequalities. It is refuted by a preparation-noncontextual model of
  four states that satisfy Eqs. 10–11 and exceed the bound. What cannot
  settle it: further qubit calculations, which only confirm the
  violation, or uncertainty relations of theories without the symmetry,
  which the bound does not cover.
title: 'For a state whose four-state reflection orbit is realizable, generalized noncontextuality bounds two binary predictabilities by |⟨X⟩| + |⟨Z⟩| ≤ 1, so the form of a predictability trade-off, not its existence, can witness contextuality'
version: 1
tags:
- contextuality
- quantum-foundations
date: '2026-10-14'
source:
- LIT-980
summary: >-
  Catani, Leifer, Scala, Schmid and Spekkens (2022), [LIT-980](../literature.d/LIT-980.md), read in
  [NOTE-tmp5bnaz](../notes.d/NOTE-tmp5bnaz.md). Proved analytically, with a saturating model, for
  preparation noncontextuality and exact operational equivalence. The
  bound constrains a whole uncertainty relation only in a theory where
  every state has the orbit; the qubit's circle violates it, and a
  classical theory without the symmetry escapes it. It needs no
  perfectly distinguishable states, and it is not a sheaf or
  Kochen–Specker criterion.
answers:
- QUESTION-067
---
<!-- inactive-ok-file: THEORY-231 THEORY-010 CLAIM-009 CLAIM-037 CLAIM-044 CLAIM-142 CLAIM-046 — Proposed; theories and claims this account bears on, open -->

# THEORY-tmpkfnig: For a state whose four-state reflection orbit is realizable, generalized noncontextuality bounds two binary predictabilities by |⟨X⟩| + |⟨Z⟩| ≤ 1, so the form of a predictability trade-off, not its existence, can witness contextuality

## Source

Catani, Leifer, Scala, Schmid and Spekkens (2022), *Physical Review
Letters* 129, 240401, [LIT-980](../literature.d/LIT-980.md), read in full in [NOTE-tmp5bnaz](../notes.d/NOTE-tmp5bnaz.md): Eqs. 1–13,
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
  the reader's argument in [NOTE-tmp5bnaz](../notes.d/NOTE-tmp5bnaz.md), one binary measurement never
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
