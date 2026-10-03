---
status: Active
title: "Steepest descent is defined only relative to a metric, and Amari's proof that natural-gradient learning is Fisher efficient needs the Fisher information at the optimum to be invertible, the condition whose failure WBIC calls singular; in a multilayer perceptron it fails wherever an output weight is zero"
version: 1
tags:
- information-geometry
- learning-theory
- mathematics
- anthology-candidate
date: '2026-10-03'
source:
- LIT-tmp26jbc
- LIT-tmpmsuf3
summary: >-
  Amari (1998), [LIT-tmp26jbc](../literature.d/LIT-tmp26jbc.md). Theorem 1 is a Lagrangian derivation: under
  |dw|² = Σg_ij dw_i dw_j the steepest-descent direction is −G⁻¹∇L, so it
  changes with G. Theorem 2 shows that online learning with step 1/t along
  the Fisher natural gradient attains the Cramér–Rao bound G⁻¹/t, and its
  proof uses G(w*)⁻¹. Watanabe, [LIT-tmpmsuf3](../literature.d/LIT-tmpmsuf3.md), Eq. 14, calls a truth regular
  when the optimum is one point and its Fisher is positive definite, and
  singular otherwise. From Amari's own Eq. 6.12, the score for hidden unit
  i's input weights carries the factor v_i. So the Fisher of a multilayer
  perceptron loses rank wherever an output weight is zero. That set is
  part of the optimum whenever the teacher needs fewer hidden units than
  the student has. Active because each step is checkable in the two
  texts. The claim that the Fisher is the only invariant metric is
  Chentsov's, cited and not held.
---
<!-- inactive-ok-file: LIT-354 THEORY-tmpzelk0 THEORY-tmp034yd — Deferred and Proposed; named in Connections, nothing here rests on them -->

# THEORY-tmpe0spv: Steepest descent is defined only relative to a metric, and Amari's proof that natural-gradient learning is Fisher efficient needs the Fisher information at the optimum to be invertible, the condition whose failure WBIC calls singular; in a multilayer perceptron it fails wherever an output weight is zero

## Source

- Amari (1998), [LIT-tmp26jbc](../literature.d/LIT-tmp26jbc.md), read in [NOTE-tmp2k5h4](../notes.d/NOTE-tmp2k5h4.md): Theorem 1 and its
  proof, Eq. 3.5, Eqs. 4.2–4.6 and Theorem 2, and Eqs. 6.12–6.13.
- Watanabe (2012; JMLR 2013), [LIT-tmpmsuf3](../literature.d/LIT-tmpmsuf3.md), read in [NOTE-tmp3drtl](../notes.d/NOTE-tmp3drtl.md): Eq. 14
  and the list of singular models in §1.

## The claim, derived

**Steepest descent depends on the metric.** Amari minimises
L(w + εa) ≈ L(w) + ε∇L(w)ᵀa subject to aᵀGa = 1. The Lagrangian gives
∇L = 2λGa, so a ∝ G⁻¹∇L ([LIT-tmp26jbc](../literature.d/LIT-tmp26jbc.md), Theorem 1 and its proof). The
ordinary gradient is the special case G = I, an orthonormal Euclidean
coordinate system. Change G and the steepest direction changes. "Steepest"
has no meaning until a metric is chosen. For a statistical model Amari
takes G to be the Fisher information, g_ij = E[∂_i log p · ∂_j log p]
(Eq. 3.5).

**Fisher efficiency needs an invertible Fisher at the optimum.** Theorem
2 assumes a realizable teacher and log loss. It considers the update
w̃_{t+1} = w̃_t − (1/t)G⁻¹∇l. Expanding the gradient about w* gives the
covariance recursion Ṽ_{t+1} = Ṽ_t − (2/t)Ṽ_t + G⁻¹/t² + O(1/t³), whose
solution is Ṽ_t = G⁻¹/t + O(1/t²), the Cramér–Rao bound (Eqs. 4.2–4.6).
Both the update and the bound are written with G(w*)⁻¹. When G(w*) is
singular, neither the natural gradient nor the bound is defined at the
optimum, and the theorem says nothing.

**That condition is half of WBIC's "regular".** Watanabe calls the truth
regular for a model if the set of optimal parameters is a single point
and the Hessian J(w0) of the mean log loss is positive definite there. For
a realizable truth J(w0) is the Fisher information. Otherwise the truth is
singular ([LIT-tmpmsuf3](../literature.d/LIT-tmpmsuf3.md), Eq. 14). With a realizable teacher, then, Amari's
hypothesis that G(w*) is invertible is the local half of Watanabe's
regularity. A singular model fails regularity in one of two ways. Either
the Fisher is degenerate at some optimal point, and Amari's proof has no
G⁻¹ there, or the optimum is not a single point, and the proof's
convergence to a unique w* is in doubt.

**In a multilayer perceptron it fails wherever an output weight is
zero.** Amari's model is y = Σ_i v_i f(w_i·x) + noise (Eq. 6.12). He
computes ∂ log p/∂w_i ∝ v_i f′(w_i·x)x, so every entry of G in the rows
and columns of w_i carries the factor v_i: v_i² on the diagonal block and
v_i v_j off it (Eq. 6.13 and the lines before it). At v_i = 0 those rows
vanish, and G loses rank by the dimension of w_i. When the teacher can be
realized with fewer hidden units than the student has, the optimal set
contains such points, with v_i = 0 and w_i arbitrary. So the optimum is
not a point, and the Fisher is degenerate on it. This is the reader's
derivation from the paper's own expressions ([NOTE-tmp2k5h4](../notes.d/NOTE-tmp2k5h4.md)). Amari does
not draw it. It is an instance of Watanabe's remark that models with
hierarchical layers are singular.

## What this does not say

- **It does not prove the Fisher is the canonical metric.** Amari calls
  it "the only invariant metric to be given to the statistical model",
  citing Chentsov (1972). The record holds neither Chentsov's proof nor
  Amari's 1985 book. This account uses the Fisher only as the metric
  Theorem 2 is stated for.
- **It does not say natural gradient fails in deep networks.** It says
  that the efficiency theorem does not apply at singular optima. How
  natural-gradient learning behaves there, whether faster or slower or
  merely different, is not settled by either paper. Amari's own conjecture
  that natural gradient escapes plateaus rests on a preliminary
  simulation he cites ([NOTE-tmp2k5h4](../notes.d/NOTE-tmp2k5h4.md), C6).
- **It does not say what replaces the Cramér–Rao bound at a singularity.**
  Singular learning theory's answer is in terms of the RLCT (Watanabe's
  book, [LIT-354](../literature.d/LIT-354.md), unread). The record holds only the free-energy half of
  that answer, through WBIC.
- **It is about the exact Fisher.** K-FAC ([LIT-tmpuzob3](../literature.d/LIT-tmpuzob3.md)) and its damping
  approximate G⁻¹ with an added multiple of the identity, which is
  invertible by construction. The question then moves to what damping
  does at a degenerate optimum.

## Connections

- **[THEORY-tmpzelk0](THEORY-tmpzelk0.md)** reads the same boundary from model comparison.
  In regular models the evidence penalty is set by the curvature that this
  theorem inverts, and in singular ones by the RLCT.
- **[THEORY-tmp034yd](THEORY-tmp034yd.md)** finds, in trained classifiers, Fisher spectra with
  about C² informative directions over a large null space. That is the
  empirical shape of a Fisher with no inverse, though not by itself a
  measurement of singularity.
