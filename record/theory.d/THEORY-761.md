---
number: 761
status: Active
formerly:
- THEORY-tmpuaxgt
title: 'A continuous piecewise-linear function on R^d with compact support has a Fourier transform that, along any fixed direction û, is bounded by C(û)k^(−2), and by C(û)k^(−d−1) whenever û is orthogonal to no edge of its linear regions, which is almost every direction; C(û) is not uniform and grows without bound near the exceptional directions; for a ReLU network without compact support the statement is not established'
version: 1
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Filed Active from NOTE-983. The result is Rahaman et al.'s
    Lemma 1 and Theorem 1, with Lemma 2 from Diaz, Le and Robins. It is
    narrowed here to compact support, with O for the paper's Θ and the
    non-uniform constant stated. Every step is re-derived below, which
    meets the condition for Active under ADR-047 v2. A numerical check
    is reported with it.
tags:
- mathematics
- learning-theory
date: '2026-10-20'
source:
- LIT-1261
summary: >-
  Rahaman et al. (2019), [LIT-1261](../literature.d/LIT-1261.md), read in full in [NOTE-983](../notes.d/NOTE-983.md). One
  integration by parts turns f̃ into a sum of polytope transforms weighted
  by the region gradients and divided by k. Each further step of Diaz et
  al.'s recursion gains another 1/k until the path reaches a face whose
  directions are all orthogonal to k. Generic directions reach the
  vertices, giving k^(−d−1), and every direction gets at least k^(−2). It
  is a bound on what a piecewise-linear function contains, not a
  statement about training. Unbounded ReLU networks fall outside it.
---
<!-- inactive-ok-file: THEORY-759 — Proposed; the companion empirical account from the same paper, nothing here rests on it -->

# THEORY-761: A continuous piecewise-linear function on R^d with compact support has a Fourier transform that, along any fixed direction û, is bounded by C(û)k^(−2), and by C(û)k^(−d−1) whenever û is orthogonal to no edge of its linear regions, which is almost every direction; C(û) is not uniform and grows without bound near the exceptional directions; for a ReLU network without compact support the statement is not established

## Source

Rahaman, Baratin, Arpit, Draxler, Lin, Hamprecht, Bengio and Courville
(2019), "On the Spectral Bias of Neural Networks", ICML, [LIT-1261](../literature.d/LIT-1261.md),
read in full in [NOTE-983](../notes.d/NOTE-983.md) from arXiv v3. The statements are §2.2
(Lemmas 1–2, Theorem 1) and Appendix C.1–C.3. The polytope recursion is
Diaz, Le and Robins (2016, arXiv 1602.08593), Theorem 1, as restated in
Appendix C.2. The re-derivation below is the record's. It narrows the
paper's Theorem 1 to compact support, writes O where the paper writes Θ,
and states the direction dependence of the constant.

## What was actually shown

**Setting.** f: R^d → R is continuous, has compact support, and is affine
on each of finitely many bounded convex d-polytopes P_ε that cover its
support, with gradient W_ε there. A ReLU network has this form when it
has compact support (Lemma 3 gives the regions). The regions where f is
zero carry W_ε = 0 and drop out, so only bounded regions matter. Write
f̃(k) = ∫ f(x)e^(−ik·x) dx, k = κû with κ = ‖k‖.

**Step 1: one integration by parts (Lemma 1).** f is Lipschitz, so its
distributional gradient is the a.e. gradient Σ_ε W_εᵀ 1_(P_ε), with no
jump part. Integrating ∂_j f against e^(−ik·x) by parts gives
(∂_j f)~(k) = ik_j f̃(k). Dotting with k gives k·(∇f)~ = iκ² f̃. So

f̃(k) = −i Σ_ε (W_ε·k/κ²) 1̃_(P_ε)(k), and |f̃(κû)| ≤ κ^(−1) Σ_ε ‖W_ε‖ |1̃_(P_ε)(κû)|.

The paper prints +i, from dividing by −iκ² in its Eq. 26. Only the
phase differs.

**Step 2: the recursion (Diaz et al.).** Let F be an m-dimensional face,
m ≥ 1, and Proj_F the orthogonal projection onto F's direction space.
On F, ∇_F e^(−ik·x) = −i Proj_F(k) e^(−ik·x). If Proj_F(k) ≠ 0, set
V = i Proj_F(k)/‖Proj_F(k)‖² · e^(−ik·x), a field tangent to F. Then
div_F V = i Proj_F(k)·(−i Proj_F(k))e^(−ik·x)/‖Proj_F(k)‖² = e^(−ik·x). The
divergence theorem on F, with N_F(G) the outward unit normal to the facet
G within F's affine hull, gives

∫_F e^(−ik·x) = Σ_(G facet of F) [i Proj_F(k)·N_F(G)/‖Proj_F(k)‖²] ∫_G e^(−ik·x).

Each bracket has modulus at most 1/‖Proj_F(k)‖ = 1/(κ‖Proj_F(û)‖). If
Proj_F(k) = 0, then k·x is constant on F, and ∫_F e^(−ik·x) = vol_m(F)e^(−iΦ),
with modulus vol_m(F). A vertex (m = 0) contributes a phase of modulus 1.

**Step 3: path lengths.** Unfold the recursion from P. Each path
P = F₀ → F₁ → … → F_n descends one dimension per step and stops at the
first face with Proj_(F_n)(û) = 0, or at a vertex. Its term has modulus at
most vol(F_n) Π_(i<n) 1/(κ‖Proj_(F_i)(û)‖). The first step always occurs,
because Proj_P(û) = û ≠ 0. So n ≥ 1 on every path. A face of dimension
≥ 1 has Proj_F(û) = 0 exactly when û is orthogonal to every edge of F,
because the edges span F's direction space. So if û is orthogonal to no
edge of any P_ε, every path runs to a vertex, and n = d. With finitely
many faces, finitely many paths and κ ≥ 1:

|1̃_(P_ε)(κû)| ≤ C_ε(û)κ^(−1) always, and ≤ C_ε(û)κ^(−d) when û is orthogonal to no edge.

The exceptional directions lie in the finitely many hyperplanes
orthogonal to an edge, a null set of the sphere for d ≥ 2. Combining with
Step 1 gives the title's κ^(−2) and κ^(−d−1). The constant C(û) is a sum
over paths of vol(F_n)Π 1/‖Proj_(F_i)(û)‖. It grows without bound as û
approaches an exceptional hyperplane, so no single constant serves
all directions. The phase sums can vanish at particular κ: in 1-D,
1̃_[a,b](k) = (e^(−ika) − e^(−ikb))/(ik) is zero at k = 2πj/(b − a). So the
bound is O, not the paper's Θ.

**Check.** For the pyramid f(x, y) = max(0, 1 − max(|x|, |y|)) on R², the
transform was computed by the Fourier slice theorem: a 1-D transform of
the numerically integrated projection, with the envelope taken over
windows at κ = 20, 40, 80 and 160. Along a facet normal (0 rad) the
fitted exponent was −1.93. Along a generic direction (0.37 rad) it was
−2.99. These match −2 and −(d + 1) = −3, so both bounds are attained.

What could have come out otherwise: the cancellations between adjacent
regions that continuity forces could have raised the generic exponent
above d + 1. In the example they do not.

## What this does not say

- **Not anything about training.** It bounds what a CPWL function with a
  given geometry contains. The paper's tie to the order of learning, its
  Eq. 9, is an instantaneous upper bound on speed with a constant that
  grows during training. It is not part of this entry.
- **Not for ReLU networks in general.** A network that is not compactly
  supported has unbounded regions. Its transform is a tempered
  distribution, which can be singular on lower-dimensional subspaces. A
  two-layer network Σ a_j max(0, w_j·x + b_j) has its transform supported
  on the lines R w_j. The paper asserts Theorem 1 for "general ReLU
  networks with arbitrary width and depth", and its Appendix C does not
  prove that. Truncating to a box does not help: f·1_B jumps on the box's
  boundary and falls only as κ^(−1) along its normals.
- **Not a uniform bound.** C(û) blows up near the exceptional
  hyperplanes. A statement "|f̃(k)| ≤ Ck^(−d−1) for almost all k" with one C
  is false. The paper's Appendix D needs such uniformity, over θ as well,
  and so does not follow ([NOTE-983](../notes.d/NOTE-983.md), Limitations).
- **Not about architecture in the exponent.** Depth, width and weights
  enter only the constant: the gradients ‖W_ε‖, the number of regions and
  the face geometry. The paper bounds that constant by N_f L_f.
- **Not the NTK's spectrum.** [THEORY-086](THEORY-086.md)'s k^(−d) on S^(d−1) is the decay
  of kernel eigenvalues, which are learning rates. The two exponents
  concern different objects and are not to be compared as one.

## Connections

- **[THEORY-086](THEORY-086.md).** The kernel-regime account of the order of fitting.
  This entry is its representational counterpart for finite
  piecewise-linear functions. It holds at every parameter value, and it
  says nothing about rates.
- **[THEORY-759](THEORY-759.md)** is the experimental order of fitting from the same
  paper. This entry is the theorem the paper offers as its background,
  and it does not imply that order.
- **[QUESTION-217](../questions.d/QUESTION-217.md).** Not an answer. It concerns no learning operator
  and no hierarchy of representations. It is cited there only as the
  proved part of the spectral-bias reading.
