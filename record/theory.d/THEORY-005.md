---
number: 5
status: Proposed
formerly:
- THEORY-tmpfit2t
promote_when: >-
  A published statement of the operator formulation for continuous views with
  the square-integrability condition, or a proof that features trained with a
  standard contrastive loss span the top eigenfunctions of T. A restatement of
  the finite-space results cannot settle it.
title: 'The positive-pair density ratio is the kernel of the conditional-expectation operator on L²(p), so spectral representations are that operator''s eigenfunctions, well defined when the positive-pair χ²-divergence is finite'
version: 1
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
  ([LIT-249](../literature.d/LIT-249.md)), with a two-line derivation of the record's own. No source
  states the operator formulation with its integrability condition.
extends:
- THEORY-007
---
<!-- inactive-ok-file: LIT-259 — Deferred: filed and skimmed on 2026-09-26 while pursuing the owner's Riesz/Radon–Nikodym/GNS question; the theories citing it are Proposed until it is read closely -->
<!-- inactive-ok-file: LIT-251 — Deferred: filed and skimmed on 2026-09-26 while pursuing the owner's Riesz/Radon–Nikodym/GNS question; the theories citing it are Proposed until it is read closely -->
<!-- inactive-ok-file: LIT-258 — Deferred: filed and skimmed on 2026-09-26 while pursuing the owner's Riesz/Radon–Nikodym/GNS question; the theories citing it are Proposed until it is read closely -->
<!-- inactive-ok-file: LIT-249 — Deferred: filed and skimmed on 2026-09-26 while pursuing the owner's Riesz/Radon–Nikodym/GNS question; the theories citing it are Proposed until it is read closely -->

# THEORY-005: The positive-pair density ratio is the kernel of the conditional-expectation operator on L²(p), so spectral representations are that operator's eigenfunctions, well defined when the positive-pair χ²-divergence is finite

## Source

Johnson, El Hanchi & Maddison (2023), [LIT-258](../literature.d/LIT-258.md), Thm 3.2; Tosh, Krishnamurthy & Hsu (2021), [LIT-251](../literature.d/LIT-251.md), §2.4; HaoChen et al. (2021), [LIT-249](../literature.d/LIT-249.md), App. F. The derivation below is the record's own.

## What was actually shown

The derivation. For the positive-pair distribution with marginal p, (Tf)(a) = E[f(A′) | A = a] = ∫ p(b|a) f(b) db = ∫ K⁺(a,b) f(b) p(b) db, with K⁺ = p⁺/(p⊗p). So K⁺ is exactly the kernel of the conditional-expectation operator on L²(p). T is Hilbert–Schmidt, hence compact with a discrete spectrum, iff ∫∫ K⁺² dp dp < ∞, and that double integral equals 1 + χ²(P⁺‖P⊗P). The positive-pair symmetry makes T self-adjoint.

What the sources show, which this reading unifies: Johnson et al.'s eigenfunctions (Thm 3.2) are T's eigenfunctions on a finite space. Tosh et al. read the density ratio as a change of measure and the Bayes predictor under redundancy as an integral operator applied to E[Y|Z] (§2.4). HaoChen et al. extend their spectral result to infinite spaces under a Hilbert–Schmidt assumption on the normalized kernel (App. F, Assumption F.1), which is the finite-χ² condition in other words.

The L²(p) here is the space the commutative GNS construction produces from the state f ↦ E_p f (Jorgensen & Tian, [LIT-259](../literature.d/LIT-259.md), Remark 1.34 and Ex. 4.28, say the kernel-to-Hilbert-space construction is GNS and that commutative states are measures). That identification is also the record's inference.

## What this does not say

- That InfoNCE-trained features span T's top eigenfunctions. InfoNCE fits log K⁺, not K⁺, so its embeddings' inner products are not T's kernel.
- Anything when χ²(P⁺‖P⊗P) is infinite, which happens when views are too informative about each other (for example, near-deterministic augmentations on continuous inputs).
- That the GNS identification adds a result. It names the space; the theorems are the spectral theorem and the sources' own.
