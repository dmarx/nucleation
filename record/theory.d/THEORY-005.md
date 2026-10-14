---
number: 5
status: Proposed
formerly:
- THEORY-tmpfit2t
promote_when: >-
  Not met by the readings of 2026-10-14. Johnson et al. (NOTE-tmpu7m7r)
  write the operator formulation without an integrability condition and on a
  finite space only; HaoChen et al. (NOTE-tmpbkfrz) extend to infinite
  spaces under a uniform bound on K⁺, stronger than finite χ², and prove
  only the existence of the eigenbasis there; both show the spectral
  population minimizer, not trained features, spanning the top
  eigenfunctions. Still needed: a published statement of the operator
  formulation for continuous views under the square-integrability (finite
  χ²) condition, or a proof that features trained with a standard
  contrastive loss span the top eigenfunctions of T. A restatement of the
  finite-space results cannot settle it.
title: 'The positive-pair density ratio is the kernel of the conditional-expectation operator on L²(p), so spectral representations are that operator''s eigenfunctions, well defined when the positive-pair χ²-divergence is finite'
version: 2
history:
- version: 2
  date: '2026-10-14'
  note: >-
    After close readings of LIT-249 (NOTE-tmpbkfrz) and LIT-258
    (NOTE-tmpu7m7r). HaoChen et al.'s Assumption F.1 is now described as
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
answers:
- QUESTION-052
---
<!-- inactive-ok-file: LIT-259 — Deferred: filed and skimmed on 2026-09-26 while pursuing the owner's Riesz/Radon–Nikodym/GNS question; the theories citing it are Proposed until it is read closely -->
<!-- inactive-ok-file: LIT-251 — Deferred: filed and skimmed on 2026-09-26 while pursuing the owner's Riesz/Radon–Nikodym/GNS question; the theories citing it are Proposed until it is read closely -->

# THEORY-005: The positive-pair density ratio is the kernel of the conditional-expectation operator on L²(p), so spectral representations are that operator's eigenfunctions, well defined when the positive-pair χ²-divergence is finite

## Source

Johnson, El Hanchi & Maddison (2023), [LIT-258](../literature.d/LIT-258.md), Thm 3.2 and App. E.2; Tosh, Krishnamurthy & Hsu (2021), [LIT-251](../literature.d/LIT-251.md), §2.4; HaoChen et al. (2021), [LIT-249](../literature.d/LIT-249.md), App. F (Assumption F.1, Thm F.2, eq. 70). The integrability condition and its identification with finite χ² are the record's own.

## What was actually shown

The derivation. For the positive-pair distribution with marginal p, (Tf)(a) = E[f(A′) | A = a] = ∫ p(b|a) f(b) db = ∫ K⁺(a,b) f(b) p(b) db, with K⁺ = p⁺/(p⊗p). So K⁺ is exactly the kernel of the conditional-expectation operator on L²(p). T is Hilbert–Schmidt, hence compact with a discrete spectrum, iff ∫∫ K⁺² dp dp < ∞, and that double integral equals 1 + χ²(P⁺‖P⊗P). The positive-pair symmetry makes T self-adjoint.

What the sources show, which this reading unifies: Johnson et al.'s eigenfunctions (Thm 3.2) are T's eigenfunctions on a finite space, and they write the first step of the derivation themselves: λ_i f_i(a₁) = Σ K⁺(a₁,a₂) f_i(a₂) p(a₂) = E_(a₂|a₁)[f_i(a₂)] (App. E.2), with the integral form given as motivation and no integrability condition. Tosh et al. read the density ratio as a change of measure and the Bayes predictor under redundancy as an integral operator applied to E[Y|Z] (§2.4). HaoChen et al. extend to infinite spaces under Assumption F.1, which requires finite marginals and a uniform bound w(u,v)/w(u) ≤ B·w(v), that is, K⁺ ≤ B everywhere. That is strictly stronger than finite χ². They derive the Hilbert–Schmidt property from it (eq. 70) and call it sufficient, not necessary. They prove only that an eigenbasis exists (Thm F.2); the extension of Theorems 3.8, 4.2 and 4.3 is asserted with the proof omitted. That the Hilbert–Schmidt integral is 1 + χ²(P⁺‖P⊗P), and that finite χ² is the condition the argument needs, is the record's inference, not HaoChen et al.'s.

The L²(p) here is the space the commutative GNS construction produces from the state f ↦ E_p f (Jorgensen & Tian, [LIT-259](../literature.d/LIT-259.md), Remark 1.34 and Ex. 4.28, say the kernel-to-Hilbert-space construction is GNS and that commutative states are measures). That identification is also the record's inference.

## What this does not say

- That InfoNCE-trained features span T's top eigenfunctions. InfoNCE fits log K⁺, not K⁺, so its embeddings' inner products are not T's kernel.
- That HaoChen et al.'s guarantees hold under finite χ² alone. Their infinite-space case assumes the uniform bound of Assumption F.1, and its extension of the main theorems is not written out.
- Anything when χ²(P⁺‖P⊗P) is infinite, which happens when views are too informative about each other (for example, near-deterministic augmentations on continuous inputs).
- That the GNS identification adds a result. It names the space; the theorems are the spectral theorem and the sources' own.
