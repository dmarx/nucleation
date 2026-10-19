---
number: 9
status: Active
formerly:
- THEORY-tmpwf2pt
title: 'In the positive-pair spectral self-supervised papers, self-adjointness comes from the symmetry of the positive-pair distribution, not from the Riesz representation theorem; elsewhere in the family it comes from a symmetrized loss, a precondition on the kernel, or composing the conditional-expectation operator with its adjoint'
version: 7
history:
- version: 2
  date: '2026-10-14'
  note: >-
    After close readings of LIT-258 (NOTE-751), LIT-249
    (NOTE-740), LIT-242 (NOTE-741) and LIT-228 (NOTE-752).
    LIT-228's Theorem 7 is now cited as the nearest published case of a
    non-symmetric pair structure handled by a singular value decomposition,
    with its two caveats. LIT-242 is now said to get its symmetry from
    symmetrizing the loss, not from the pair distribution, with its CLIP-like
    two-tower case (§5.2). HaoChen et al. are said never to write
    "symmetric"; their symmetry comes from w(u,v) = w(v,u). Johnson et al.'s
    M is said to be the Gram matrix BᵀB, which needs both views drawn from
    the same p(A|Z). Neither paper mentions Riesz. promote_when keeps its
    clauses and records the near misses; it is not met. The stale Deferred
    comments on LIT-258 and LIT-249 removed.
- version: 3
  date: '2026-10-14'
  note: >-
    After NOTE-770 (LIT-975, THEORY-239). LIT-975 added to
    promote_when's near misses, nearer than LIT-228 but not meeting it.
    The mechanism is restated: the thesis gets self-adjointness by
    composing the conditional-expectation operator with its adjoint, not
    from symmetry of the pair, and the multi-view case is a special case
    of that. promote_when is not met.
- version: 4
  date: '2026-10-14'
  note: >-
    After close readings of LIT-252 (NOTE-824), LIT-260
    (NOTE-838) and LIT-261 (NOTE-836). The summary no longer
    groups SpIN with the positive-pair distribution: there symmetry is a
    precondition on k, which puts it nearer Simon et al. "Riesz is what
    makes a kernel mean embedding exist" now reads that the review obtains
    it by Riesz; a Bochner integral also works. The eqs. 18–24 reading of
    LIT-261 is confirmed and its account, THEORY-314, cited. The
    Deferred comments on LIT-252, LIT-260 and LIT-261 removed.
    promote_when is not met.
- version: 5
  date: '2026-10-14'
  note: >-
    The adjoint sentence narrowed to what the Riesz article (LIT-230, read in NOTE-861) says: matrices and general bounded operators; the integral-operator clause is marked as the record's own.
- version: 6
  date: '2026-10-14'
  note: >-
    The record's own step, that an integral operator's adjoint has the
    conjugate-transposed kernel, is filed with its proof as
    CLAIM-291 and cited where the step is made.
- version: 7
  date: '2026-10-19'
  note: >-
    Narrowed and promoted from Proposed to Active at the owner's direction,
    carrying out the promotion audit's decision
    (record/promotion-audit/decisions/THEORY-009.yaml, batch 007). As titled
    the claim was contradicted by its own body, which names three routes
    in the family where self-adjointness does not come from the
    positive-pair distribution: Simon et al.'s symmetrized loss, Pfau et
    al.'s precondition on k, and Zhai's composition of the
    conditional-expectation operator with its adjoint. The title now
    covers the positive-pair papers and names those routes. The reading of
    LIT-258 and LIT-249 was checked again for the promotion: P(a, a′) =
    Σ_z p(z)p(a|z)p(a′|z) = BᵀB, so D^(−½)PD^(−½) is symmetric and positive
    semidefinite. The owner's rule of 2026-10-19 (ADR-047): a checked step-by-step re-derivation recorded in the decision file meets a promote_when that asks for a proof the record does not hold, and the THEORY is promoted. The promote_when asked for a
    published analysis of an asymmetric objective, which tests an extension
    the body disclaims. It moves, with its near misses, to QUESTION-141,
    and is removed here.
tags:
- representation-learning
- mathematics
date: '2026-09-26'
source:
- LIT-258
- LIT-249
- LIT-252
- LIT-242
- LIT-228
- LIT-230
summary: >-
  An inference from how the spectral SSL papers ([LIT-258](../literature.d/LIT-258.md), [LIT-249](../literature.d/LIT-249.md),
  [LIT-252](../literature.d/LIT-252.md), [LIT-242](../literature.d/LIT-242.md)) obtain their eigenbases: each uses a symmetric pair
  matrix or kernel, and none invokes Riesz. In all but Simon et al., whose
  loss is symmetrized by hand, and Pfau et al., whose SpIN takes symmetry
  as a precondition on the kernel k, that symmetry is the symmetry of the
  positive-pair distribution. Answers the owner's "do we even need Riesz?"
  for this family of results.
extends:
- THEORY-007
answers:
- QUESTION-052
---
<!-- inactive-ok-file: THEORY-239 — Proposed; the account filed from LIT-975, cited for the mechanism it sharpens, not leaned on -->
<!-- inactive-ok-file: THEORY-314 — Proposed; the representer-theorem account filed from LIT-261, cited as a parallel case, not leaned on -->
<!-- inactive-ok-file: QUESTION-141 — Open; the asymmetric-objective question this reading was narrowed away from, named as open -->

# THEORY-009: In the positive-pair spectral self-supervised papers, self-adjointness comes from the symmetry of the positive-pair distribution, not from the Riesz representation theorem; elsewhere in the family it comes from a symmetrized loss, a precondition on the kernel, or composing the conditional-expectation operator with its adjoint

## Source

Johnson, El Hanchi & Maddison (2023), [LIT-258](../literature.d/LIT-258.md), App. C; HaoChen et al. (2021), [LIT-249](../literature.d/LIT-249.md), App. F; Pfau et al. (2019), [LIT-252](../literature.d/LIT-252.md), §5.2; Simon et al., [LIT-242](../literature.d/LIT-242.md), eq. 4 and §5.2; Balestriero & LeCun, [LIT-228](../literature.d/LIT-228.md), Theorem 7; the Riesz statement, [LIT-230](../literature.d/LIT-230.md).

## What was actually shown

Every spectral result in these papers rests on a symmetric operator. Johnson et al. use the symmetry of P_(A,A) to make D^(−½)P D^(−½) orthogonally diagonalizable, which yields the orthonormality all their theorems use (App. C). They call M "the symmetric matrix" without argument; it is symmetric, and positive semidefinite, because the proof of Thm 3.2 writes it as a Gram matrix BᵀB, which holds because both views are drawn independently from the same p(A|Z). HaoChen et al. apply the spectral theorem to a square-integrable kernel k(u,v) = w(u,v)/√(w(u)w(v)) (App. F). They never write "symmetric": the symmetry follows from w(u,v) = w(v,u), which holds because both views come from the same A(·|x̄), and they use it throughout the finite case as well. Pfau et al. note that reversible dynamics make "the transition function … a symmetric operator" (§5.2), but that is an aside no derivation uses: in SpIN symmetry is a precondition placed on the kernel k (§3.2), which puts it nearer Simon et al. than the positive-pair papers. Simon et al. symmetrize by hand, Γ = (1/2n)Σ(x_i x_i′ᵀ + x_i′ x_iᵀ) (eq. 4); there the symmetry comes from symmetrizing the loss, not from the pair distribution, and they apply the same Γ to CLIP-like two-tower pairs (§5.2), where there is no single space and no symmetric pair distribution. Neither Johnson et al. nor HaoChen et al. mention Riesz. For finite matrices the adjoint is the (conjugate) transpose, and Riesz is what defines the adjoint of a general bounded operator ([LIT-230](../literature.d/LIT-230.md)). That for square-integrable integral operators it is the conjugate-transposed kernel is the record's own step, proved in [CLAIM-291](../claims.d/CLAIM-291.md); the article covers matrices only.

**A sharper statement of the mechanism.** Zhai's thesis ([LIT-975](../literature.d/LIT-975.md), read in [NOTE-770](../notes.d/NOTE-770.md); [THEORY-239](THEORY-239.md)) obtains every self-adjoint operator by composing the conditional-expectation operator g ↦ E[g(A)|X], which runs between two different spaces and is never assumed symmetric, with its adjoint, given in closed form by Bayes' rule. So self-adjointness comes from that composition, not from the symmetry of the pair. The multi-view case is a special case: there (A, A⁺) is exchangeable because both are drawn from P⁺(·|x), which is the symmetry this account names, seen from the construction side. Riesz is not used here either.

The representer theorem is a parallel case: Schölkopf, Herbrich & Smola's proof ([LIT-261](../literature.d/LIT-261.md), eqs. 18–24; [THEORY-314](THEORY-314.md)) uses the reproducing property and orthogonal projection, not Riesz; the word does not occur in the paper.

## What this does not say

- **Anything about asymmetric objectives.** Whether the eigenfunction
  characterization fails for BYOL-type objectives, or is replaced by
  singular functions of a non-self-adjoint operator, is [QUESTION-141](../questions.d/QUESTION-141.md).

- That Riesz is irrelevant. It is what makes an abstract space of functions with bounded evaluation into an RKHS, and the review obtains the kernel mean embedding by Riesz (see the mean-embedding claim, from Muandet et al., [LIT-260](../literature.d/LIT-260.md), Lemma 3.1). A Bochner integral, which the review also uses to define it, gives it too; that second route is the record's inference.
- What happens for non-reversible pair structures: predictors and stop-gradient (BYOL, SimSiam), directed augmentations, cross-modal pairs. There the natural object would be the singular value decomposition of a non-self-adjoint operator, which needs the adjoint in earnest. No account for an asymmetric objective was found. The nearest is Balestriero & LeCun's Theorem 7 ([LIT-228](../literature.d/LIT-228.md)): in the linear regime Barlow Twins recovers CCA, the singular value decomposition of the non-self-adjoint whitened cross-covariance, and a symmetric pair matrix G is what yields weight sharing; the paper says G's symmetry "is often not required". But the objective is Barlow Twins, not a BYOL-type asymmetric one, and the identification with CCA is asserted rather than derived. In Simon et al.'s two-tower case the symmetric Γ is block off-diagonal in the cross-covariance, so its eigenvalues are ± that matrix's singular values; that reading (the Jordan–Wielandt construction) is the record's, not the paper's.
