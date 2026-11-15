---
status: Read
paper: LIT-tmpme1pw
title: 'Belrose et al. — LEACE'
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Read in full on 2026-11-15 by a delegated reader from
    https://arxiv.org/pdf/2306.03819v4 (22 pp., "arXiv:2306.03819v4
    [cs.LG] 3 Apr 2025", NeurIPS 2023 footer), text extracted with
    pdftotext. Read: the abstract, §§1–8 and Appendices A–J, and the
    erratum page. The reference list was skimmed. Figures 2 and 4 were
    read from their captions only; their plotted values were not
    recoverable. The filer string-matched every quotation below and
    checked Thms 3.4 and 4.1–4.3 numerically (see "A check of the
    theorems").
date: '2026-11-15'
summary: >-
  Proves that linear guardedness (no linear predictor under a convex loss
  beats a constant) is equivalent to equal class-conditional means and to
  zero cross-covariance; characterises the affine erasers that achieve it
  (P annihilates colsp(Σ_XZ)); and gives the unique eraser least-squares
  optimal under every inner-product norm, an oblique projection in
  whitened coordinates. Experiments: gender erasure in BERT, amnesic
  probing for part of speech, and layer-wise "concept scrubbing" of part
  of speech in LLaMA and Pythia. Linear only.
---

# NOTE-tmpwodpq: Belrose et al. — LEACE

## Contribution

1. **A five-way equivalence** (§3): linear guardedness, optimality of the
   trivially attainable loss, equal class centroids, zero cross-covariance,
   and statistical parity of every linear predictor.
2. **A characterisation of every affine eraser that guards** (Thm 4.1).
3. **The unique eraser that is least-squares optimal under all
   inner-product norms at once** (Thms 4.2–4.3), which is oblique.
4. **Proofs that several existing erasers already guard but are not
   optimal**: full-rank SAL, Mean Projection and Fair PCA (Appendix D).
5. **Concept scrubbing** across layers (Algorithm 1).

## Key insight

Linear access to a concept lives entirely in the cross-covariance, so the
constraint on an eraser falls on its null space ("PΣXZ = 0, is a
constraint on the nullspace of P, and not on its range", §4.2). All the
remaining freedom, in P's range, can be spent keeping X close to itself.
That is why the optimum is oblique, not orthogonal.

## Assumptions

- **Moments.** X has a finite first moment, and a finite second moment
  for Thms 4.2–4.3. Each class has positive probability.
- **Scope of the guard.** Guardedness is relative to linear predictors
  and convex losses. Necessity is proved via cross-entropy.
- **Fitting.** The eraser is fitted on moments with labels and applied
  without them. Guardedness is exact for the moments used; no
  finite-sample bound is given.
- **Scrubbing.** It assumes concepts are linearly encoded in each layer.

## Key results

- **§3, the equivalence** (p. 2): the conditions "are all equivalent",
  including that "Every component of X has zero covariance with every
  component of Z". Sufficiency is by Jensen (Thm 3.1), necessity via the
  cross-entropy first-order condition at W = 0 (Lemma 3.2, Thm 3.3), and
  centroids ⇔ zero cross-covariance (Thm 3.4).
- **Thm 4.1** (p. 4): r(X) linearly guards Z "if and only if the columns
  of the cross-covariance matrix ΣXZ are contained in the null space of
  P", since Cov(PX + b, Z) = PΣXZ.
- **Thms 4.2–4.3** (p. 5): for any p.s.d. M, the minimiser of E‖PX + b −
  X‖²_M subject to guardedness is P* = I − W⁺P_{WΣXZ}W, b* = E[X] −
  P*E[X], with W = (Σ_XX^{1/2})⁺. "there is a single erasure function that
  minimizes all such norms simultaneously", Euclidean and Mahalanobis
  included.
- **§4.2, obliqueness** (p. 6): r_LEACE "is not an orthogonal projection
  in general". Appendix F gives X₂ = X₁ + Z, where the orthogonal eraser
  costs 2 and the oblique one 1.
- **§5.1–5.2, gender in BERT** (Bias in Bios): "our method is the only to
  achieve random accuracy (perfect erasure) with a small edit". Profession
  accuracy falls from 79.3% to 77.3%, and "the TPR gap drops
  significantly from 0.198 to 0.084".
- **§5.3, amnesic probing for part of speech in BERT**: "INLP reduces
  the rank of the embedding by 360. By contrast, our method decreases the
  rank just by 17." Its largest effect on masked-language-model accuracy
  is at layer 11, INLP's at layer 6.
- **§6, concept scrubbing.** Layers are fitted sequentially, because
  fitting all layers on the clean model "may fail to fully erase the
  target concept". Table 1 gives bits per UTF-8 byte:

  | Model | No intervention | Random erasure | LEACE | SAL |
  |---|---|---|---|---|
  | LLaMA 7B | 0.69 | 0.69 | 1.73 | 3.24 |
  | Pythia 12B | 0.62 | 0.63 | 3.20 | 4.69 |

  The authors: "If this experiment were conducted with SAL alone, we
  would have overestimated the causal effect of part-of-speech."
- **Erratum** (v4, last page): a Figure 3 MLM accuracy was mistyped as
  0.892 for 0.928 and has been corrected.

## A check of the theorems

The filer drew 200,000 samples of a 6-dimensional X whose mean depends on
a 3-class Z, and computed LEACE from the sample moments.

- **Guardedness.** After erasure the largest entry of Cov(r(X), Z) is
  1.2 × 10⁻¹⁵, and every class mean equals the overall mean to
  4 × 10⁻¹⁴ (Thms 3.4, 4.1).
- **Obliqueness.** P* is idempotent and not symmetric: an oblique
  projection (§4.2).
- **Optimality under every norm.** For 200 random positive-definite
  inner products M, LEACE's cost E‖r(X) − X‖²_M was no larger than that
  of the orthogonal eraser (full-rank SAL) or of the best of 20 random
  guarding projections, in all 200. In the Euclidean norm the costs were
  15.37 against 23.35 for SAL; in the Mahalanobis norm, 2.00 against
  3.88.

The check is on sample moments and one dimension, and it is not a proof.

## Concepts

- **Linear guardedness**: (V, L)-guardedness with V the affine predictors
  and L the convex losses. For cross-entropy it equals Xu et al.'s
  linear V-information being zero (Appendix G).
- **Cross-covariance Σ_XZ**, the **whitening W**, and **oblique
  projection**.
- **Oracle LEACE**: the residual of X regressed on Z, which needs Z at
  inference (Appendix I).
- **Concept scrubbing**: LEACE fitted and applied layer by layer.

## Connections

The paper builds on INLP and RLACE (Ravfogel et al.), on SAL, Mean
Projection and Fair PCA, which it shows guard but are not optimal, and on
amnesic probing (Elazar et al.). It does not mention model editing.

## Bearing on the record

- **THEORY-281** (perfect concept erasure caps the information a
  representation keeps at that not about the concept). That cap is
  information-theoretic: I(Z; A) = 0 is required. LEACE's guarantee is
  weaker and linear (Σ_XZ = 0), and its utility measure is squared
  distance, not information kept. The two do not conflict. LEACE is the
  second-moment counterpart, and its §7 conjecture of intractability
  against nonlinear adversaries is computational, which THEORY-281's
  bound neither supports nor contradicts. Dated note filed.
- **LIT-963 / NOTE-820** (Chowdhury et al.). A nonlinear boundary
  surviving LEACE on their four-point toy is what LEACE's §7 says
  linear erasure cannot prevent. The two papers mean different things by
  "perfect". No note filed; the NOTE-820 reading already records the
  comparison.
- **LIT-1309 / NOTE-1048** (Xu et al., V-information). By LEACE's
  Appendix G, linear guardedness under log loss is linear V-information
  at zero, so LEACE is an optimal V-information eraser for linear V.
  NOTE-1048's line that erasure certified against one probe family is
  not erasure against another is the boundary LEACE states. No note
  filed.
- **THEORY-846 / CLAIM-199** (V-information can be created by
  computation). LEACE-guarded data can still carry nonlinearly usable Z,
  the XOR case being the canonical example. The paper does not give it.
  No note filed.
- **MuEdit and AlphaEdit** (filed in their own pull requests). They also
  edit by projection, but onto null spaces of preserved keys in weight
  space, where LEACE projects representations. Any closer link would be
  the record's own step; none is made here.

## Limitations

- **Linear only**, as the authors say: "in the worst case, information
  about Z could be encoded cryptographically in X".
- **No finite-sample guarantee.**
- **Concept scrubbing is shown only for part of speech.**
- **The oblique P can have singular values above one** and blow up
  norms in some models; Appendix H gives a heuristic fix.
- **Gender is binary** in Bias in Bios.

## Open questions

- How much nonlinear information about part of speech survives
  scrubbing, and does the perplexity cost reflect loss of the concept or
  damage to unrelated structure?
