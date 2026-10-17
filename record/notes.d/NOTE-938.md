---
number: 938
status: Read
formerly:
- NOTE-tmpicuma
paper: 'LIT-1163'
title: 'Kraskov, Stögbauer and Grassberger — Estimating mutual information'
version: 1
history:
- version: 1
  date: '2026-10-16'
  note: >-
    Read from arXiv cond-mat/0305641v1 (28 May 2003), 16 pp., extracted with
    pdftotext. §§I–II (introduction and the formal derivations, Eqs. 1–30)
    and §V and the appendix read in full. §III (implementation and
    numerical results, Figs. 2–16) and §IV (gene-expression and ICA
    applications, Figs. 17–20) read at lower resolution: the prose and
    captions, not the plotted values. I checked I⁽¹⁾ (Eq. 8, k = 3, maximum
    norm) by simulation on correlated unit Gaussians against
    −½log(1 − r²) (Eq. 11). I did not compare the PRE version.
date: '2026-10-16'
summary: >-
  Two k-nearest-neighbour estimators of mutual information, I⁽¹⁾ and I⁽²⁾
  (Eqs. 8–9), from the Kozachenko–Leonenko entropy estimate (Eq. 20) taken
  at one length scale in the joint and marginal spaces, so that the
  biases largely cancel. The only approximation is a locally constant
  density. Numerically the systematic error scales with k/N and vanishes
  for independent variables, a conjecture without proof; the ordered
  Weinman exponential is the one case where the stronger form fails.
  Extensions to multi-information (Eqs. 23, 30). Conditional mutual
  information is not treated.
---

# NOTE-938: Kraskov, Stögbauer and Grassberger — Estimating mutual information

## Contribution

Before this paper, nearest-neighbour estimators existed for Shannon
entropy, and mutual information was estimated by binning, adaptive
partitioning (Darbellay–Vajda) or kernels. Summing three separate entropy
estimates left their biases uncancelled. After it, mutual information has
estimators that use the k-th-neighbour distance in the joint space to fix
the scale at which the marginals are counted. Their systematic errors are
an order of magnitude below Darbellay–Vajda's on the Gaussian benchmarks,
and they need no bin or bandwidth.

## Key insight

The Kozachenko–Leonenko estimate holds for any k, so the marginal entropy
can be taken at whatever neighbour count matches the joint k-th-neighbour
distance (Eq. 22). Then the joint and marginal estimates assume constant
density over the same region, and their errors largely cancel in
H(X) + H(Y) − H(X, Y).

## Assumptions

- **i.i.d. samples** z_i = (x_i, y_i) from a density µ(x, y) that is "a
  proper smooth function" (p. 1). Fractal measures are excluded.
- **Locally constant density** inside each k-th-neighbour ball or
  rectangle (Eq. 18). This is the only approximation in the KL estimate;
  it is exact for strictly constant density.
- **Maximum norm in the joint space** (Eq. 6); any norms in the marginals.
- **Continuous coordinates.** Ties from discretized data break the neighbour
  counts, and noise of order 10⁻¹⁰ must be added (§III A).
- **I⁽²⁾ neglects an excluded-region correction** in the marginal entropies,
  O(1/n_x) and O(1/n_y). The authors "slightly cheated" there and have no
  proof that it vanishes (§II C).

## Key results

- **Eq. 20, Kozachenko–Leonenko** — Ĥ(X) = −ψ(k) + ψ(N) + log c_d +
  (d/N)Σ log ε(i), with ε(i) twice the distance to the k-th neighbour,
  from E(log p_i) = ψ(k) − ψ(N) (Eq. 17). For positive densities on a
  torus the corrections are O((k/N)²); numerically they are ∼k/N or
  ∼(k/N)log(N/k) for Gaussians and bounded uniforms.
- **Eq. 8** — I⁽¹⁾ = ψ(k) − ⟨ψ(n_x + 1) + ψ(n_y + 1)⟩ + ψ(N).
- **Eq. 9** — I⁽²⁾ = ψ(k) − 1/k − ⟨ψ(n_x) + ψ(n_y)⟩ + ψ(N), from
  E(log q_i) = ψ(k) − 1/k − ψ(N) (Eq. 27).
- **Eqs. 23, 30** — the m-variable redundancies, with (m − 1)ψ(N) and, for
  I⁽²⁾, −(m − 1)/k.
- **Scaling (Eq. 32)** — I⁽¹⁾ ≈ Φ(k/N), I⁽²⁾ ≈ Φ((k − ½)/N). Statistical
  errors scale roughly as 1/√N; systematic errors fall faster than N^{−1/2}
  at large N, fitted as N^{−0.85} for r = 0.9 (Fig. 6).
- **Independence (Fig. 7, Eq. 33)** — for many smooth one-parameter
  families factorizing at r₀, the ratio Î/I tends to a finite function
  F(k, N) as r → r₀. The ordered Weinman exponential violates this
  (Fig. 12).
- **Appendix, Eq. 48** — for any distribution, the multi-information is at
  least that of the Gaussian with the same covariance, −½log(det C/ΠC_ii).
- **Check (mine).** I⁽¹⁾ with k = 3, against −½log(1 − r²):

  | r | exact | N = 200 (100 runs) | N = 2000 (20 runs) |
  |---|---|---|---|
  | 0.0 | 0 | −0.005 ± 0.054 | 0.002 ± 0.020 |
  | 0.3 | 0.0472 | 0.040 ± 0.051 | 0.052 ± 0.022 |
  | 0.6 | 0.2231 | 0.227 ± 0.068 | 0.225 ± 0.017 |
  | 0.9 | 0.8304 | 0.836 ± 0.085 | 0.839 ± 0.028 |

  Unbiased within error at r = 0, and a small positive bias at r = 0.9, as
  in Fig. 4. The exact r = 0.9 value matches the paper's 0.830366.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Eqs. 8–9 estimate I(X,Y) with only a locally-constant-density approximation | moderate | §II B–C derivations; I⁽²⁾ neglects a correction without proof |
| C2 | Systematic errors depend mainly on k/N, and are much smaller than binning, KDE or Darbellay–Vajda | moderate | Figs. 2, 4, 6, 9, 11, 12; Gaussians and three non-Gaussian families |
| C3 | Both estimators are exact for independent X and Y | weak | numerical conjecture (p. 3), "no proof"; all tested independent pairs |
| C4 | Î/I tends to a finite function as independence is approached (Eq. 33) | weak | Figs. 7, 10, 14; fails for the ordered Weinman exponential (Fig. 12) |
| C5 | Accurate in high dimensions, unlike Ref. [29] beyond d ≈ 6 | moderate | Fig. 15, Gaussians, N = 50000 |
| C6 | MI minimization with these estimators improves on JADE's ICA output | moderate | fetal ECG, I drops 1.782 → 1.160 (I⁽¹⁾) and 2.264 → 1.620 (I⁽²⁾); one data set |
| C7 | The circle-distribution values of Ref. [27] are wrong | weak | Fig. 13; disagreement, "we have no explanation for this" |

## Method

1. Rescale each marginal to unit variance; transform skewed variables
   (e.g. to logarithms); add noise of order 10⁻¹⁰ to break ties.
2. For each point, find the k-th neighbour in the joint space under the
   maximum norm; take ε(i) (I⁽¹⁾) or ε_x(i), ε_y(i) (I⁽²⁾).
3. Count marginal neighbours n_x(i), n_y(i) within those distances.
4. Average the digamma terms (Eq. 8 or 9). k = 2 to 4 for estimation;
   large k, up to N/2, for testing independence.

## Concepts

- **Redundancy / multi-information** — I(X₁,…,X_m) = ΣH(X_i) − H(X₁,…,X_m)
  (Eq. 10), the paper's term, called higher-order MI in the ICA literature.
- **ε(i)** — twice the distance from z_i to its k-th neighbour; the window
  at which marginal neighbours are counted.

## Connections

- **Builds on** Kozachenko and Leonenko's entropy estimator and its
  descendants [19–22], and compares itself against Darbellay and Vajda's
  adaptive partitioning [8], kernel estimators [6] and Ref. [29].
- **Transfer entropy.** The paper does not treat conditional mutual
  information. Transfer entropy is one, I(X_{t+1}; Y⁻ | X⁻), and its
  nearest-neighbour estimators are later extensions of this construction
  (Frenzel & Pompe 2007, as Barnett, Barrett and Seth cite it, [NOTE-934](NOTE-934.md)),
  not held. My reading.
- **[NOTE-788](NOTE-788.md)** estimates time-lagged mutual information with scikit-learn's
  kNN estimator. That implementation is, by its documentation as I recall
  it (not checked here), this paper's I⁽¹⁾. Its transfer entropy is
  estimated otherwise, with a Markov-state-model estimator.
- **[NOTE-320](NOTE-320.md)** (Saxe et al.) uses "the Kraskov estimator" for the layer entropy
  H(T). An entropy is Eq. 20, Kozachenko–Leonenko as reviewed here, not
  the paper's mutual-information estimators. My reading of what an entropy
  estimate must be; I did not check Saxe et al.'s code.
- **[NOTE-828](NOTE-828.md)** (MINE) reports Kraskov's estimator well below the truth for
  20-dimensional correlated Gaussians. This paper's Fig. 15 tests up to
  its own range of d at N = 50000 and r ≤ 0.9; the two are compatible if
  the degradation sets in at higher d or smaller N, which I did not check.

## Bearing on the record

- Filed as [THEORY-709](../theory.d/THEORY-709.md).
- [TERM-057](../terms.d/TERM-057.md): a transfer-entropy value estimated by nearest neighbours
  inherits this estimator's bias, which is not bounded, only measured on
  benchmark families. Barnett and Bossomaier's χ² null ([THEORY-641](../theory.d/THEORY-641.md)) is
  for the plug-in or parametric estimator, not this one.
- **For the Anthology of the SOTA:** no instruction for ML practice. An
  estimator used by ML papers, read for what it assumes.

## Limitations

- No bias bound and no proof of consistency in the paper; justification
  "ultimately relies on numerics" (§II C).
- The exactness for independence is a conjecture, and the stronger
  ratio conjecture fails in one tested case without explanation.
- Sensitivity to marginal transformations: MI is invariant, the estimates
  are not, and the paper's remedy (transform first) is case by case.
- Discretized data violate the continuity assumption; added noise is a
  workaround, not an analysis.
- Statistical errors are given by simulation, not by a formula, so a
  single data set has no error bar without resampling.

## Open questions

- A proof of exactness for independent variables (the authors').
- Which families satisfy Eq. 33, and what in the ordered Weinman
  exponential breaks it (the authors').
- Bias and variance of the conditional extension when used for transfer
  entropy at the history lengths k ≫ 1 that Lizier et al. call for
  ([NOTE-943](NOTE-943.md)).
