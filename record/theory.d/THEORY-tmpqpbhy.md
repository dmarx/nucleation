---
status: Proposed
promote_when: >-
  An independent derivation or published use of Lemma 1 and Lemma 2 for a
  general joint law of two views, since the account rests on one paper's
  proofs (App. A.1–A.2), together with a check that the landmark readout
  keeps its 1/m rate when the ratio is learned with bounded excess loss
  under finite E[g*²] alone, without the uniform bound g_max that
  Theorems 10–11 assume. It is refuted by a joint law with redundant views
  (small εX and εZ) on which no linear function of g*(x,·) comes within
  εX + 2√(εXεZ) + εZ of the Bayes predictor, which would mean Lemma 1's
  proof is wrong. What cannot settle it: linear-probe accuracies of
  trained contrastive networks, since the account is about the population
  ratio and redundancy is not measured there.
title: "When two views are redundant for a label, the predictor that infers one view from the other is within εX + 2√(εXεZ) + εZ of the Bayes predictor, and it is linear in the contrastive density ratio, so a linear readout of m random evaluations of that ratio approaches it at rate 1/m, with no symmetry between the views required"
version: 1
tags:
- representation-learning
- learning-theory
date: '2026-10-14'
source:
- LIT-251
summary: >-
  Tosh, Krishnamurthy & Hsu (2021), [LIT-251](../literature.d/LIT-251.md), read in [NOTE-tmpj78ol](../notes.d/NOTE-tmpj78ol.md): Lemma 1,
  §2.3–2.4, Lemma 2 and Theorem 3. The label enters only through how
  redundant the views are about it; the representation is the density
  ratio p(x,z)/(p(x)p(z)), learned without labels. Population level. The
  error-propagation results need a uniform bound on the ratio, and the
  low-dimensional direct embeddings are shown to exist, not to be reached.
answers:
- QUESTION-052
---
<!-- inactive-ok-file: THEORY-001 THEORY-005 THEORY-009 THEORY-228 THEORY-tmp1iy33 — Proposed; accounts this one bears on, not leaned on -->

# THEORY-tmpqpbhy: When two views are redundant for a label, the predictor that infers one view from the other is within εX + 2√(εXεZ) + εZ of the Bayes predictor, and it is linear in the contrastive density ratio, so a linear readout of m random evaluations of that ratio approaches it at rate 1/m, with no symmetry between the views required

## Source

Tosh, Krishnamurthy & Hsu (2021; ALT 2021), [LIT-251](../literature.d/LIT-251.md), read in
[NOTE-tmpj78ol](../notes.d/NOTE-tmpj78ol.md): §2.2–2.4 with Lemma 1 (proof App. A.1), §3 with Lemma 2
and Theorem 3 (App. A.2), Proposition 5 (App. A.4), Lemma 6, Theorems
10–11 (App. A.9–A.10).

## What was actually shown

**Redundancy.** For views X, Z and label Y, let
εX = E[(E[Y|X] − E[Y|X,Z])²] and εZ = E[(E[Y|Z] − E[Y|X,Z])²]. The
"infer, then predict" function µ(x) = E[E[Y|Z] | X = x] satisfies
E[(µ(X) − E[Y|X,Z])²] ≤ εX + 2√(εXεZ) + εZ (Lemma 1). The proof is Jensen
and AM/GM and holds for any joint law with finite second moments.

**The ratio.** The logistic problem of telling a same-datum pair from an
independent pair, with equal priors, is solved over all functions by the
PMI, so g*(x,z) = p(x,z)/(p(x)p(z)) (§2.3, stated). Then
µ(x) = ∫ E[Y|Z=z] g*(x,z) p_Z(z) dz: "g⋆ provides the change-of-measure
from the marginal distribution of Z to the conditional distribution of Z
given X = x", and g* "does not depend on Y at all" (§2.4).

**Linear readout.** With landmarks Z_1, …, Z_m drawn from p_Z and
φ*(x) = (g*(x,Z_1), …, g*(x,Z_m)), with probability 1 − δ some w gives
E[(wᵀφ*(X) − µ(X))²] ≤ 2 var(E[Y|Z]g*(X,Z̃)) / ⌊m/log₂(1/δ)⌋ (Lemma 2),
and so a near-Bayes linear predictor (Theorem 3). For |Y| ≤ 1 the
variance is at most E[g*(X,Z̃)²] with X, Z̃ independent. That quantity is
1 + χ² of the joint against the product of marginals. The identification
with χ² is the record's; in the paper's Gaussian model it is
(1 + σ²)²/(1 + 2σ²) (Prop. 5).

**What could have failed.** Redundancy could have required that the
representation see the label, or that the views be exchangeable. The
argument uses neither: X and Z may be different spaces with any joint
law.

**Estimation.** If the ratio is learned with excess logistic loss
ε_opt, the downstream risk grows by terms in (1 + g_max)²√ε_opt and
(1 + g_max)⁴ε_opt, where g_max is a uniform bound on the ratio
(Theorem 10). The direct loss with prediction log(η(x)ᵀψ(z)) has the
ratio itself as its minimizer, and its excess loss bounds the risk of η
(Lemma 6, Theorem 11).

## What this does not say

- **That µ is the Bayes predictor.** It is close to it, by εµ, only when
  both views are redundant for the label.
- **Anything about the top eigen- or singular functions.** The readout is
  through random landmarks of the full ratio. A low-dimensional direct
  embedding of the ratio is shown to exist (Lemma 7) but not to be what
  minimizing the direct loss finds, and the authors say so.
- **Anything about InfoNCE with many negatives.** The contrastive problem
  is logistic, with a single negative.
- **That the guarantees survive an unbounded ratio.** Theorems 10–11 need
  g_max < ∞. Lemma 2 needs only a finite variance, which is the
  square-integrability condition of [THEORY-005](THEORY-005.md), but only for the exact
  ratio.
- **That redundancy holds for any real task.** It is assumed, not
  measured. The examples are a topic model and a Gaussian latent model.

## Connections

- **[QUESTION-052](../questions.d/QUESTION-052.md).** An answer in part to its second half. For linear
  decisions about labels on which two views are redundant, the full
  density-ratio kernel is decision-sufficient with no symmetry between
  the views. The signature here is the full kernel through random
  landmarks, not a low-dimensional eigenspace, and the guarantee is at the
  population ratio.
- **[THEORY-tmp1iy33](THEORY-tmp1iy33.md).** The same conditional-expectation operator between
  two spaces, g ↦ E[g(Z)|X]. Zhai's result picks the top-d singular
  functions as the minimax span for compatible tasks; this one reads µ, an
  image of that operator, off the whole kernel. µ = E[h(Z)|X] with
  h = E[Y|Z] is exactly the form of target Zhai's compatibility measures.
- **[THEORY-001](THEORY-001.md).** Supplies, for general densities, the logistic optimum
  that [THEORY-001](THEORY-001.md) holds on a finite space, and §5's contrast between a
  loss minimized by log g* and one minimized by g*.
- **[THEORY-005](THEORY-005.md).** The landmark bound is controlled by E[g*²], the
  Hilbert–Schmidt quantity [THEORY-005](THEORY-005.md) names, without any operator or
  eigenfunction formulation.
- **[THEORY-228](THEORY-228.md) and [THEORY-007](THEORY-007.md).** Different conditions on the target:
  augmentation rarely changing the label and conductance there,
  approximate view invariance in [THEORY-007](THEORY-007.md), redundancy across views here.
- **[THEORY-009](THEORY-009.md).** A guarantee that never uses symmetry. It does not meet
  [THEORY-009](THEORY-009.md)'s promote_when, which asks about asymmetric objectives of
  the BYOL kind and eigen- or singular-function characterizations.
