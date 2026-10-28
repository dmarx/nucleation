---
number: 5
status: Proposed
formerly:
- THEORY-tmpfit2t
promote_when: >-
  Not met by the readings of 2026-10-14. Johnson et al. (NOTE-751)
  write the operator formulation without an integrability condition and on a
  finite space only; HaoChen et al. (NOTE-740) extend to infinite
  spaces under a uniform bound on K⁺, stronger than finite χ², and prove
  only the existence of the eigenbasis there; both show the spectral
  population minimizer, not trained features, spanning the top
  eigenfunctions. Still needed: a published statement of the operator
  formulation for continuous views under the square-integrability (finite
  χ²) condition, or a proof that features trained with a standard
  contrastive loss span the top eigenfunctions of T. A restatement of the
  finite-space results cannot settle it. Tosh et al. (NOTE-841) use
  finite E[g*²] = 1 + χ² as the operative condition for landmark
  features, but their Theorems 10–11 need a uniform g_max like HaoChen
  et al.'s F.1, and they have no operator or eigenfunctions; this does
  not meet it.
title: 'The positive-pair density ratio is the kernel of the conditional-expectation operator on L²(p), so spectral representations are that operator''s eigenfunctions, well defined when the positive-pair χ²-divergence is finite'
version: 4
history:
- version: 2
  date: '2026-10-14'
  note: >-
    After close readings of LIT-249 (NOTE-740) and LIT-258
    (NOTE-751). HaoChen et al.'s Assumption F.1 is now described as
    what it is, a uniform bound K⁺ ≤ B, from which they derive the
    Hilbert–Schmidt property (eq. 70); it is not the finite-χ² condition,
    and equating Hilbert–Schmidt with finite χ² is marked as the record's
    inference. Their extension of Theorems 3.8, 4.2 and 4.3 to infinite
    spaces is said to be asserted with its proof omitted; only Theorem F.2
    is proved. Johnson et al. App. E.2 is credited with the operator
    formulation λf(a₁) = E[f(a₂)|a₁] on a finite space, so the summary now
    says only the integrability condition is missing from the sources.
    promote_when rewritten to say what the readings did and did not
    supply. The Deferred comments on LIT-249 and LIT-258 removed.
- version: 3
  date: '2026-10-14'
  note: >-
    After close readings of LIT-251 (NOTE-841) and LIT-259
    (NOTE-829). µ is no longer called the Bayes predictor: it is the
    infer-then-predict function, within εX + 2√(εXεZ) + εZ of it (Lemma
    1). Tosh et al.'s landmark bound is noted as controlled by
    E[g*²] = 1 + χ², with their Theorems 10–11 needing a uniform g_max;
    promote_when says this does not meet it. Jorgensen & Tian's Ex. 4.86
    and Lemma 3.28 are cited for L²(μ) as the commutative GNS space, for
    compact X only. The Deferred comments on LIT-251 and LIT-259 removed.
- version: 4
  date: '2026-10-19'
  note: >-
    At the owner's direction, from the second pass of the owner's
    promotion audit of 2026-10-19, the record's own derivation is filed
    apart as CLAIM-370, Active and demonstrated, with a proof. That
    claim includes the converse, that T is Hilbert–Schmidt only if χ² is
    finite. This THEORY keeps its reading of the sources and the
    eigenfunction identification for trained or spectral features. Its
    promote_when, which asks for a published statement or a result about
    trained features, is unchanged, and the status stays Proposed.
tags:
- representation-learning
- mathematics
- information-theory
date: '2026-09-26'
source:
- LIT-258
- LIT-251
- LIT-249
summary: >-
  An inference assembled on 2026-09-26 from Johnson, El Hanchi & Maddison
  ([LIT-258](../literature.d/LIT-258.md)), Tosh, Krishnamurthy & Hsu ([LIT-251](../literature.d/LIT-251.md)) and HaoChen et al.
  ([LIT-249](../literature.d/LIT-249.md)), with a two-line derivation of the record's own. Johnson et
  al. write the operator formulation on a finite space (App. E.2); no source
  states it with its integrability condition.
extends:
- THEORY-007
bears_on:
- QUESTION-052
---

# THEORY-005: The positive-pair density ratio is the kernel of the conditional-expectation operator on L²(p), so spectral representations are that operator's eigenfunctions, well defined when the positive-pair χ²-divergence is finite

## Source

Johnson, El Hanchi & Maddison (2023), [LIT-258](../literature.d/LIT-258.md), Thm 3.2 and App. E.2; Tosh, Krishnamurthy & Hsu (2021), [LIT-251](../literature.d/LIT-251.md), §2.4; HaoChen et al. (2021), [LIT-249](../literature.d/LIT-249.md), App. F (Assumption F.1, Thm F.2, eq. 70). The integrability condition and its identification with finite χ² are the record's own.

## What was actually shown

The derivation. For the positive-pair distribution with marginal p, (Tf)(a) = E[f(A′) | A = a] = ∫ p(b|a) f(b) db = ∫ K⁺(a,b) f(b) p(b) db, with K⁺ = p⁺/(p⊗p). So K⁺ is exactly the kernel of the conditional-expectation operator on L²(p). T is Hilbert–Schmidt, hence compact with a discrete spectrum, iff ∫∫ K⁺² dp dp < ∞, and that double integral equals 1 + χ²(P⁺‖P⊗P). The positive-pair symmetry makes T self-adjoint.

What the sources show, which this reading unifies: Johnson et al.'s eigenfunctions (Thm 3.2) are T's eigenfunctions on a finite space, and they write the first step of the derivation themselves: λ_i f_i(a₁) = Σ K⁺(a₁,a₂) f_i(a₂) p(a₂) = E_(a₂|a₁)[f_i(a₂)] (App. E.2), with the integral form given as motivation and no integrability condition. Tosh et al. read the density ratio as a change of measure and the infer-then-predict function µ(x) = E[E[Y|Z]|X=x], which is within εX + 2√(εXεZ) + εZ of the Bayes predictor under redundancy (Lemma 1), as an integral against E[Y|Z] (§2.4); calling it an operator is the record's. Their landmark bound is controlled by var(E[Y|Z]g*(X,Z̃)) ≤ E[g*²] = 1 + χ², the same Hilbert–Schmidt quantity (the identity with χ² is the record's algebra), but their Theorems 10–11 need a uniform bound g_max on the ratio, like HaoChen et al.'s F.1. HaoChen et al. extend to infinite spaces under Assumption F.1, which requires finite marginals and a uniform bound w(u,v)/w(u) ≤ B·w(v), that is, K⁺ ≤ B everywhere. That is strictly stronger than finite χ². They derive the Hilbert–Schmidt property from it (eq. 70) and call it sufficient, not necessary. They prove only that an eigenbasis exists (Thm F.2); the extension of Theorems 3.8, 4.2 and 4.3 is asserted with the proof omitted. That the Hilbert–Schmidt integral is 1 + χ²(P⁺‖P⊗P), and that finite χ² is the condition the argument needs, is the record's inference, not HaoChen et al.'s.

The L²(p) here is the space the commutative GNS construction produces from the state f ↦ E_p f (Jorgensen & Tian, [LIT-259](../literature.d/LIT-259.md), Remark 1.34 and Ex. 4.28, say the kernel-to-Hilbert-space construction is GNS and that commutative states are measures). Ex. 4.86 and Lemma 3.28 state outright that the commutative GNS space is L²(μ), but only for compact X (or a compact spectrum); for the R^d spaces common here the passages read say nothing, so the identification there is still the record's inference.

## What this does not say

- That InfoNCE-trained features span T's top eigenfunctions. InfoNCE fits log K⁺, not K⁺, so its embeddings' inner products are not T's kernel.
- That HaoChen et al.'s guarantees hold under finite χ² alone. Their infinite-space case assumes the uniform bound of Assumption F.1, and its extension of the main theorems is not written out.
- Anything when χ²(P⁺‖P⊗P) is infinite, which happens when views are too informative about each other (for example, near-deterministic augmentations on continuous inputs).
- That the GNS identification adds a result. It names the space; the theorems are the spectral theorem and the sources' own.

## Note of 2026-10-19: the derivation filed as the record's own

The derivation in "What was actually shown", that K⁺ is T's kernel, that T
is Hilbert–Schmidt with ‖T‖²_HS = 1 + χ², and that it is self-adjoint, is
now [CLAIM-370](../claims.d/CLAIM-370.md). It is stated there with a proof, including the
converse (Hilbert–Schmidt only if χ² is finite), and it is Active.
Mathematics the record proves does not wait on a source. What this THEORY
still waits on is what the sources show, and whether features reach the
eigenfunctions.
