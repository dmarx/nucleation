---
number: 535
status: Read
formerly:
- NOTE-tmppznp2
paper: LIT-682
title: 'Exploring Neural Network Landscapes: Star-Shaped and Geodesic Connectivity'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read from arXiv v1 (26 pages). Sections 1–6 and Appendix A.1–A.2 read in
    full; the other proofs read for statement and structure, not checked
    step by step. Tables 1–2 read from the text layer; Figures 1–5 from
    captions.
date: '2026-10-03'
summary: >-
  Two-layer ReLU student of an orthonormal M-neuron teacher: the minimum
  manifold is explicit (Theorem 6); two random minima are 2-PL connected
  w.p. ≥ 1 − M((M²−1)/M²)^{m−2M}; any two are 4-PL connected for
  m ≥ 2M − 1; k minima share a linearly connected centre w.p.
  ≥ 1 − M((M^k−1)/M^k)^{m−kM}. Normalised geodesic distance is O(√M) for
  uniform minima but ≤ 1 + c₂/(r√m) for r-sparse ones. Deep linear nets:
  2-PL a.s., 3-PL always, star centre a.s. for m > 1 + r(L − 1). Centres
  found empirically for FNN, VGG16, ResNet on MNIST/CIFAR-10 without
  permutation.
---

# NOTE-535: Exploring Neural Network Landscapes: Star-Shaped and Geodesic Connectivity

## Contribution

Mode connectivity said a low-loss path exists between minima; this paper
says how simple the path is and how many minima can share one. In two
models where the minimum set can be written down, it proves that wide
networks join any two minima with two straight segments, join any finite
set through a common centre, and that SGD-like sparse minima are joined by
paths barely longer than the straight line. It finds such centres in real
image classifiers.

## Key insight

Over-parameterisation gives a minimum lots of spare neurons that can be
switched off without changing the function. Two minima can each be moved,
along a straight line, to a third minimum that uses only the neurons they
can agree on. The more spare neurons, the more likely such a meeting point
exists for many minima at once, and the sparser the minima, the less the
detour through it costs.

## Assumptions

- **Two-layer ReLU (Assumption 5)**: teacher f*(x) = Σⱼ₌₁^M σ(eⱼ·x), M ≤ d,
  x uniform on the unit sphere, student of m ≥ M neurons with no output
  weights (they are absorbed into the neuron norms), squared loss on the
  population, not on a sample.
- **"Typical" minima** are drawn uniformly from the manifold (Theorems 8,
  10, 12) or from the neuron-sparse distribution SP(M, r), with each neuron
  zero with probability r (Definition 13, Theorem 14). These are models of
  where SGD lands; the paper motivates the sparse one from Figure 3.
- **Linear networks (Assumption 15)**: y = Qx, zero-mean x with
  non-degenerate covariance, output dimension 1, hidden widths equal.
- **Experiments**: minima trained with Adam (not SGD), centres found with
  Adam on Eq. 6 with B_r = 1, B_t = 3.

## Key results

- **Theorem 6**: the minimum manifold is the set of W whose rows lie in
  {0} ∪ {αeⱼ : α ≠ 0} with Σᵢ wᵢⱼ = 1 for each j ≤ M; coordinates beyond M
  vanish. (The proof shows the non-zero entries are non-negative.)
- **Lemma 7**: W⁽¹⁾ ↔ W⁽²⁾ iff every neuron is zero in one of them or lies on
  the same teacher direction in both.
- **Theorems 8–9**: 2-PL connectivity with probability ≥ 1 − M((M²−1)/M²)^{m−2M},
  so m ≥ CM² log(M/δ) suffices for probability 1 − δ; 4-PL connectivity for
  every pair when m ≥ 2M − 1.
- **Theorems 10–11**: a linearly connected centre for k minima with
  probability ≥ 1 − M((M^k−1)/M^k)^{m−kM}, needing m ≥ CM^k log(M/δ); a
  2-PL-connected centre always when m ≥ kM.
- **Theorems 12, 14**: NGD ≤ c₂√M w.p. ≥ 1 − c₁e^{−m} for uniform minima;
  NGD ≤ 1 + c₂/(r√m) w.p. ≥ 1 − c₁Me^{−mr²} for SP(M, r) minima. In both the
  bound is attained by a two-piece path.
- **Linear networks (Theorems 16, 18; Lemma 17)**: with m > 2L − 1, two minima
  are almost surely 2-PL and always 3-PL connected; a pathological pair that
  is not 2-PL connected is exhibited; r minima almost surely have a
  linearly connected centre when m > 1 + r(L − 1).
- **Table 1 (5 minima per setting)**: mean loss barrier on direct lines
  16.91 (VGG16, MNIST), 1.25 (FNN, MNIST), 6.21 (VGG16, CIFAR-10), 3.28
  (ResNet34, CIFAR-10); through the centre 3.1e-05, 1.1e-03, 5.0e-03,
  1.0e-02. Minimum accuracy along the fold-lines 99.65–100%.
- **Table 2**: NGD upper bounds 1.003 (FNN, MNIST), 1.001 (VGG16, MNIST),
  1.051 (VGG16, CIFAR-10), 1.003 (ResNet18, CIFAR-10).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | In the teacher–student and deep linear settings, wide networks have 2-PL connected minima and star-shaped connectivity | strong (proofs), narrow settings | Theorems 8–11, 16, 18 |
| C2 | The landscape of wide networks is "nearly convex" in the sense that geodesic distance on the minimum manifold approaches Euclidean distance | strong under the sparse-minima model; the link to SGD is an assumption motivated by one figure | Theorem 14, Fig. 3 |
| C3 | Star-shaped connectivity holds for practical networks without permutation | moderate: a centre is found for 3–5 given minima in four settings; whether it connects to minima not used to find it is not tested | Table 1, Fig. 5 |
| C4 | Practical minima are joined by paths with NGD near 1 | moderate as an upper bound from one found centre per setting, two minima each | Table 2, Eq. 8 |

## Method

Centre-finding minimises J_S(θ) = (1/r) Σᵢ [E_{t∼U[0,1]} R(tθ + (1 − t)θᵢ*) +
λp(θ, θᵢ*)] by Adam, sampling one minimum and three values of t per step
(Eqs. 6–7). With p = ‖θ − θ′‖², the centre found for two minima gives an
upper bound on their normalised geodesic distance through Eq. 8.

## Concepts

- **k-piece linear (k-PL) connectivity**: a path of at most k straight
  segments, each lying entirely in the minimum set (Definition 2).
- **star-shaped linear connectivity**: a centre on the minimum set linearly
  connected to each foot (Definition 3).
- **normalised geodesic distance (NGD)**: the infimum length of paths in the
  minimum set divided by the Euclidean distance; 1 for a convex set
  (Definition 4).

## Connections

- **Garipov et al. ([LIT-673](../literature.d/LIT-673.md))**: the observation that a two-segment
  polygonal chain suffices is the stated starting point.
- **Kuditipudi et al. ([LIT-671](../literature.d/LIT-671.md))**: proved ≤ 10 linear segments under
  dropout or noise stability for deep networks; this paper gets 2–4 in much
  narrower models.
- **Sonthalia et al. ([LIT-659](../literature.d/LIT-659.md))**: concurrent. They work modulo
  permutation, as a relaxation of the convexity conjecture, and test whether
  the centre connects to held-out minima. This paper does neither.
- **Entezari et al. ([LIT-652](../literature.d/LIT-652.md)), Git Re-Basin ([LIT-661](../literature.d/LIT-661.md))**: cited as
  the permutation line. This paper's centres are found without any
  permutation step, so its empirical star-shaped connectivity is a
  different claim from theirs.
- **Tan et al. ([LIT-662](../literature.d/LIT-662.md))**: a Fisher–Rao geodesic, not this paper's
  Euclidean geodesic on the minimum set.

## Bearing on the record

- A THEORY candidate, shared with Sonthalia et al.: *the set of trained
  minima of a wide network is star-shaped, with centres linearly connected
  to many minima at once, and wider is closer to convex*. This paper gives
  the toy-model proof; Sonthalia et al. give the held-out test with
  permutations.
- No instruction for practice.

## Limitations

- **Toy models.** The proofs need an orthonormal teacher, spherical inputs
  and population loss, or a linear network. The authors say only that the
  results are "provably valid" there and "empirically supported" elsewhere.
- **Sparsity as SGD's bias** is an assumption about where SGD lands, drawn
  from one plot (Figure 3, m = 512, M = 4, d = 4).
- **No held-out test.** A centre fitted to five minima is not shown to
  connect to a sixth, so the empirical result is star-shaped connectivity of
  a finite set, as Definition 3 defines it, not of the solution set.
- **NGD is an upper bound** from one centre, and the bound is computed only
  for two minima per setting.

## Open questions

- Does a centre found for k minima connect to minima it was not fitted to?
  (Sonthalia et al. test this, with permutations.)
- Can the sparsity bias of SGD be proved, rather than assumed, in the
  teacher–student model?

## Corrections

- none to a seeded skim (there was no seed)
- **Theorem 10's statement** introduces "two minima θ₁, θ₂" but concludes
  for all i ∈ [k]. It means k minima drawn i.i.d., as the bound shows.
- **Architecture labels.** §5 trains ResNet34 on CIFAR-10 and Table 1 says
  ResNet34, but Table 2 reports ResNet18. The Figure 4 caption refers to
  "Algorithm 5", which does not exist; it means the centre-finding
  algorithm of §5.
- **"Accuracy barrier"** in Table 1 is the minimum accuracy along the path,
  so higher is better there, the opposite of the loss row.
