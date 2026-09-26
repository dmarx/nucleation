---
number: 222
status: Skimmed
formerly:
- NOTE-tmp6deys
paper: LIT-251
title: 'Tosh et al., contrastive learning and multi-view redundancy'
version: 1
date: '2026-09-26'
summary: >-
  The logistic contrastive problem of telling a same-datum pair of views from an independent pair is solved over all functions by the pointwise mutual information f*(x,z) = log p(x,z)/(p(x)p(z)), whose exponential g* is the change of measure from p(z) to p(z|x), and linear functions of the landmark embedding (g*(x,Z_1),…,g*(x,Z_m)) are near-optimal predictors whenever the two views are redundant for the label.
---
<!-- inactive-ok-file: LIT-251 — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-26; the directive lapses when its status changes -->

# NOTE-222: Tosh et al., contrastive learning and multi-view redundancy

## Contribution

The paper analyses contrastive learning in the multi-view setting, where each datum comes with two views. Its main result is that linear functions of the learned representation are nearly optimal on downstream prediction whenever the two views carry redundant information about the label. It draws the analogy with the classical CCA analyses of Kakade & Foster and Foster et al.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- §2.3, Eq. 1: the contrastive problem is logistic regression of a label Y_c (same datum vs. independent views) on (X_c, Z_c); "the optimal solution f* to (1) (over all functions from X × Z to R) predicts the pointwise mutual information between two views", f*(x,z) = log p_{X,Z}(x,z)/(p_X(x)p_Z(z)); g* := exp f* is the density ratio of the joint to the product of marginals.
- §2.4: redundancy is ε_X = E[(E[Y|X] − E[Y|X,Z])²] and ε_Z likewise, both small; Lemma 1: µ(x) := E[E[Y|Z] | X=x] satisfies E[(µ(X) − E[Y|X,Z])²] ≤ ε_X + 2√(ε_Xε_Z) + ε_Z.
- §2.4, after Lemma 1: µ(x) = ∫ E[Y|Z=z] g*(x,z) p_Z(z) dz, "Thus, g* provides the change-of-measure from the marginal distribution of Z to the conditional distribution of Z given X = x", and g* does not depend on Y.
- §3: the landmark embedding φ*(x) = (g*(x,Z_1),…,g*(x,Z_m)) with i.i.d. landmarks; w_i = E[Y_i|Z_i]/m makes wᵀφ*(x) → µ(x); Lemma 2 and Theorem 3 bound the finite-landmark error.
- §1 notes the related-work link to noise-contrastive estimation and nonlinear ICA (Hyvärinen et al.), not read further.

## Open questions

- It says in words what the Radon–Nikodym reading of the contrastive critic is: g*(x,·) is the density dP_{Z|X=x}/dP_Z, and the downstream predictor is the integral operator with that kernel applied to E[Y|Z]. That makes the RN derivative the object a linear probe reads.
- Johnson et al. (rb4, App. B.2) take the logistic-loss/PMI optimum from here.
- Check §4's "direct embedding" result and whether the redundancy bound survives estimation error (§5).
