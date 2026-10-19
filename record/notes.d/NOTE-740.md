---
number: 740
status: Read
formerly:
- NOTE-tmpbkfrz
paper: LIT-249
title: 'HaoChen et al. — Spectral Contrastive Loss'
version: 2
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the arXiv v7 PDF (arxiv.org/pdf/2106.04156, 50 pp.,
    24 June 2022), text extracted with pdftotext -layout: §§1–7, Appendix
    A (experiments), B (the proof of Theorem 3.8 through Theorem B.2,
    Theorem B.3, Lemmas B.4–B.8 and Claim B.9) and F (infinite supports)
    line by line. Appendices C (Proposition 3.9, Theorem 3.11, Lemma C.2),
    D (Theorems 4.1, D.6, D.7, D.9 and Lemmas D.10–D.13) and E (Theorem
    4.3) were read through for their statements and the steps they rest
    on; their Rademacher and Gaussian-isoperimetry arithmetic was not
    re-derived. The references were not read. A grep of the extracted
    text finds no occurrence of "symmetric", "self-adjoint" or "Riesz".
- version: 2
  date: '2026-10-14'
  note: >-
    Correction after the reading of LIT-227 (NOTE-846): Connections
    said Tan et al. restate the eigenvector correspondence for
    InfoNCE-type losses; they prove an identity between objectives and
    make no eigenvector statement. A correction line added; the reading is
    unchanged. Inactive-ok comments trimmed of codes now Active or Open.
date: '2026-10-14'
summary: >-
  On a finite augmentation space, the spectral contrastive loss
  L(f) = −2E[f(x)ᵀf(x⁺)] + E[(f(x)ᵀf(x⁻))²] equals the rank-k factorization
  loss ‖D^(−1/2)AD^(−1/2) − FFᵀ‖²_F up to a constant when the rows of F are
  w_x^(1/2) f(x), so its minimizers are the top-k eigenvectors of the
  normalized augmentation graph up to row scaling and a right rotation. A
  linear probe on them has error Õ(α/ρ²_⌊k/2⌋), where α is the label
  noise of augmentations and ρ the sparsest-partition conductance.
---
<!-- inactive-ok-file: THEORY-001 THEORY-005 — Proposed; the theories that cite this paper, open until it and its companions are read -->

# NOTE-740: HaoChen et al. — Spectral Contrastive Loss

## Contribution

The paper gives the first analysis of contrastive learning that does not
assume the two views are conditionally independent given a label or a
latent variable. It replaces that assumption with a graph on augmented
data whose edge weight is the probability that two augmentations come from
one natural example. A contrastive loss written on network outputs performs
a low-rank factorization of that graph's normalized adjacency. The paper
then bounds linear-probe error by graph quantities, first at the population
optimum and then for finite pretraining and labelled samples.

## Key insight

Contrastive learning is parametric spectral clustering on the population
augmentation graph. The embedding that spectral clustering would build,
the top-k eigenvectors of the normalized adjacency matrix, cannot be
stored or learned per vertex. But reweighting each row by w_x^(1/2) turns
the Frobenius factorization loss into an expectation over positive and
negative pairs, which a network can minimize from samples. A linear probe
does not see the row scaling or the right rotation the factorization
leaves free.

## Assumptions

- **Finite augmentation space** X, "finite but exponentially large",
  throughout the main text (§3). No bound depends on N = |X|.
- **The graph.** w_xx′ := E_(x̄∼P_X)[A(x|x̄)A(x′|x̄)] (eq. 2), so
  Σ w_xx′ = 1; w_x = Σ_x′ w_xx′; normalized adjacency
  Ā := D^(−1/2)AD^(−1/2) (eq. 3). Both views are drawn from the same
  A(·|x̄), so w is symmetric. The paper never says so.
- **Assumption 3.5 (at most m clusters).** ρ_(m+1) ≥ ρ, where
  ρ_i := min over i-partitions of max_j φ_G(S_j) and
  φ_G(S) := Σ_(x∈S, x′∉S) w_xx′ / Σ_(x∈S) w_x (Defs. 3.3–3.4).
- **Assumption 3.6 (labels recoverable from augmentations).** Some
  classifier g predicts y(x̄) from x ∼ A(·|x̄) with error at most α.
- **Assumption 3.7 (realizability).** At least one global minimizer of
  L(f) lies in the hypothesis class F.
- **Linear probe with ensembling.** The prediction on x̄ is the majority
  of the linear predictions over its augmentations.
- **Infinite supports (App. F, Assumption F.1).** (i) w(u) = ∫w(u,z)dz < ∞;
  (ii) there is a B with w(u,v)/w(u) ≤ B·w(v) for all u, v. That is a
  uniform bound on the density ratio w(u,v)/(w(u)w(v)), "a sufficient (but
  not necessary) condition". It implies the Hilbert–Schmidt property; it
  is not the same as it.

## Key results

- **Lemma 3.1.** For a positive diagonal D and an invertible Q, the
  embedding F̃ = D·F·Q has the same linear-probe predictions as F, with
  B̃ = Q⁻¹B. So E(F) = E(F̃).
- **Lemma 3.2 (spectral contrastive loss).** With u_x = w_x^(1/2) f(x),
  L_mf(F) = ‖Ā − FFᵀ‖²_F = L(f) + const, where
  L(f) = −2·E_(x,x⁺)[f(x)ᵀf(x⁺)] + E_(x,x⁻)[(f(x)ᵀf(x⁻))²] (eqs. 4–7).
- **Eckart–Young step (§3.2, Lemma B.8).** Any minimizer is
  F̂ = F*·diag(√γ₁, …, √γ_k)·R with R orthonormal, F* the top-k unit
  eigenvectors of Ā. In the proof of Theorem B.3 this is written
  F* = F_sc D_λ Q with D_λ = diag(√(1 − λ_i)), λ_i the Laplacian
  eigenvalues. For f this means f(x) = w_x^(−1/2) times row x of F̂.
- **Theorem 3.8.** If k ≥ 2r, Assumption 3.6 holds and F satisfies 3.7,
  then E(f*_pop) ≤ Õ(α/ρ²_⌊k/2⌋). With Assumption 3.5 and k > 2m,
  E(f*_pop) ≤ Õ(α/ρ²).
- **Theorem B.3 (the engine).** For any labelling ŷ there is a probe B*
  with ‖B*‖_F ≤ 1/(1 − λ_k) and
  E‖ȳ(x̄) − B*f*_pop(x)‖² ≤ φ^ŷ/λ_(k+1) + 4Δ(y, ŷ). It is Lemma B.6
  (‖u − Σ b_i v_i‖² ≤ R(u)/λ_(k+1)·‖u‖²) applied to the class indicators.
  Theorem B.2 replaces λ_(k+1) with ρ²_k′ by the higher-order Cheeger
  inequality of Louis and Makarychev (Lemma B.4).
- **Proposition 3.9.** For a mixture of m distributions on disjoint
  supports with Gaussian augmentation N(0, σ²I),
  lim_(σ→0⁺) ρ_(m+1)/σ ≳ min_i h_(P_i), with h the Cheeger constant.
- **Theorem 3.11 (mixture of manifolds).** For k ≥ 2r + 2, α ≤ 1/poly(d),
  ρ_⌊k/2⌋ ≳ σ/(κ√d), so E(f*_pop) ≤ Õ(κ²/(σ²·poly(d))).
- **Theorem 4.1.** The empirical loss is unbiased (Claim D.2), and
  L(f̂_emp) ≤ L(f*_pop) + c₁·R̂_(n_pre/2)(F) + c₂·(√(log(2/δ)/n_pre) + δ),
  with c₁ ≲ k²κ² + kκ and c₂ ≲ kκ² + k²κ⁴, for ‖f(x)‖_∞ ≤ κ.
- **Theorem 4.2.** For k ≥ max{4r + 2, 2m},
  E(f̂_emp) ≲ (α/ρ²)·log k + (ck/Δ²_γ)·(excess-loss terms), with
  Δ_γ := γ_⌊3k/4⌋ − γ_k.
- **Theorem 4.3.** End to end, with a capped-quadratic linear probe of
  norm at most C_k ≥ 2(k + 1)/γ_k, the downstream labelled sample need is
  poly(r, k, 1/ε) and does not depend on the complexity of F.
- **Theorem F.2.** Under Assumption F.1, the Laplacian operator
  L(f)(u) = f(u) − ∫ w(u,v)/√(w(u)w(v)) f(v)dv on L²(R^d) has an
  orthonormal eigenbasis with λ_i ∈ [0, 1]. The extension of Theorems 3.8,
  4.2 and 4.3 to this case is asserted; "We omit the proof for
  simplicity."
- **Experiments (§6, App. A).** Linear-probe top-1 on CIFAR-10 92.07,
  CIFAR-100 66.18, Tiny-ImageNet 49.86 at 800 epochs, against SimCLR
  90.60/63.88/48.12 and SimSiam 91.40/65.87/46.76 (reproductions).
  ImageNet, 100 epochs, batch 384: 66.97, against 66.5 to 68.1 for the
  baselines reported by Chen and He. The output is projected to a sphere of
  radius √μ, so the trained model has a norm constraint the theory does
  not.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The spectral contrastive loss is the normalized-adjacency factorization loss up to a constant | strong | Lemma 3.2, Lemma B.8, exact algebra |
| C2 | Its population minimizers are the top-k eigenvectors up to row scaling w_x^(−1/2) and a right factor diag(√γ)R | strong | Eckart–Young, §3.2 and proof of Theorem B.3 |
| C3 | Row scaling by positive numbers and right multiplication by an invertible matrix leave linear-probe predictions unchanged | strong | Lemma 3.1 |
| C4 | At the population optimum, linear-probe error is Õ(α/ρ²_⌊k/2⌋) | strong | Theorem 3.8 via B.2, B.3, B.4 |
| C5 | The guarantee survives finite pretraining samples with a polynomial unlabeled-sample cost | moderate | Theorems 4.1–4.3; constants loose, realizability assumed |
| C6 | The results extend to infinite augmentation spaces | weak | Theorem F.2 proved; the extensions of 3.8, 4.2, 4.3 asserted with the proof omitted |
| C7 | The loss matches or beats SimCLR and SimSiam under linear evaluation | moderate | Tables 1–3, single runs, reproductions of baselines |

## Method

Algorithm 1 (App. A): for each minibatch of N natural images draw two
augmentations of each, compute z_i = f(x_i) and z′_i = f(x′_i), and
minimize −(2/N)Σ z_iᵀz′_i + (1/(N(N − 1)))Σ_(i≠j)(z_iᵀz′_j)². The encoder
is a ResNet backbone, a projection MLP with batch normalization, and a
projection onto a sphere of radius √μ, μ ∈ {1, 3, 10}. The linear probe is
trained on the frozen backbone output, not on f.

## Concepts

- **Population augmentation graph** G(X, w). Vertices are all augmented
  data in the population; w_xx′ is the probability that a random positive
  pair is (x, x′).
- **Normalized adjacency** Ā = D^(−1/2)AD^(−1/2). Its eigenvalues are
  γ_i; the normalized Laplacian is L = I − Ā with eigenvalues λ_i = 1 − γ_i.
- **Dirichlet conductance** φ_G(S): the share of S's edge weight that
  leaves S.
- **Sparsest i-partition** ρ_i: the smallest possible largest conductance
  over partitions into i nonempty sets. It increases with i.
- **Linear probe error** E(f): the error of the best linear head on f,
  with predictions ensembled over augmentations (eq. 1).
- **Extended labelling function** ŷ: X → [r], a labelling of augmented
  points, used to measure φ^ŷ (eq. 18) and Δ(y, ŷ) (eq. 19).

## Connections

The paper sets itself against Arora et al. (2019) and Tosh et al. (2020,
2021, [LIT-251](../literature.d/LIT-251.md)), whose guarantees need conditional independence of the views
given a label or hidden variable, and against Wei et al. (2020), whose
pseudolabelling analysis needs subgraphs to align exactly with classes. Its
graph quantities are those of spectral clustering (Ng et al.; Shi and
Malik) and higher-order Cheeger inequalities (Lee et al. 2014; Louis and
Makarychev 2014). §2 describes, as "an almost equivalent version" of its
assumption, the Markov chain x₀, x₁, … with x_t ∼ p(·|x_(t−1)), which
mixes within a class before it mixes across classes. Johnson, El Hanchi and
Maddison ([LIT-258](../literature.d/LIT-258.md)) take that chain as their central object, and show that
its eigenfunctions are this paper's eigenvectors divided by p(a)^(1/2).
Tan et al. ([LIT-227](../literature.d/LIT-227.md)) and Balestriero and LeCun ([LIT-228](../literature.d/LIT-228.md)) restate the
correspondence for InfoNCE-type losses.

*Correction (2026-10-14, [NOTE-846](NOTE-846.md)):* Tan et al. do not restate the
correspondence. They prove an identity between objectives, InfoNCE as a
Laplacian form plus log normalizers, and make no eigenvector statement.

## Bearing on the record

- **[THEORY-001](../theory.d/THEORY-001.md)** cites Lemma 3.2 in support, and the citation is right.
  Lemma 3.2 shows that the spectral loss is the factorization loss. The
  paper never names the unconstrained minimizer
  K̂ = p⁺/(p⊗p); that step is Johnson et al.'s (App. B.3). The paper's own
  minimizer is the rank-k one.
- **[THEORY-007](../theory.d/THEORY-007.md)** states Lemmas 3.1–3.2 correctly. Lemma 3.2 gives
  ‖D^(−1/2)AD^(−1/2) − FFᵀ‖²_F + const. The minimizer is the top-k
  eigenvectors with a positive row scaling (w_x^(−1/2)) and a right factor
  (diag(√γ)R). Lemma 3.1 says neither changes linear-probe predictions. One
  precision: the paper's right factor is diag(√γ) times an orthonormal R,
  invertible only while γ_k > 0. Lemma 3.1 is stated for any invertible Q.
- **[THEORY-005](../theory.d/THEORY-005.md) misstates Appendix F.** It says the paper extends "under a
  Hilbert–Schmidt assumption on the normalized kernel (App. F, Assumption
  F.1), which is the finite-χ² condition in other words". Assumption F.1
  is not a Hilbert–Schmidt assumption.
  - What it assumes is finite marginals and a uniform bound
    w(u,v)/w(u) ≤ B·w(v). That bounds the density ratio
    K⁺ = w(u,v)/(w(u)w(v)) above by B everywhere.
  - Hilbert–Schmidt is derived from that bound (eq. 70:
    ∫∫k² = ∫∫w²/(w(u)w(v)) ≤ B). The paper calls F.1 sufficient, not
    necessary.
  - The integral in eq. 70 does equal 1 + χ²(P⁺‖P⊗P), so finite χ² is
    exactly the Hilbert–Schmidt condition. But that identification, and the
    claim that it is the weakest condition the argument needs, are the
    record's own and not in the paper.
  - The extension of the main theorems to infinite X is asserted, with the
    proof omitted. Only the existence of an eigenbasis (Theorem F.2) is
    proved.
- **[THEORY-005](../theory.d/THEORY-005.md)'s promote_when** asks for a proof that features trained with a
  standard contrastive loss span the top eigenfunctions of T. This paper
  proves something nearby for the spectral loss, at the population
  minimum, over all functions X → R^k, on a finite space:
  - the minimizer is w_x^(−1/2) times the top-k eigenvectors, times a right
    factor;
  - in Johnson et al.'s normalization that is the span of T's top-k
    eigenfunctions.
  It says nothing about trained networks, about InfoNCE, or about infinite
  X beyond the omitted extension. So the condition is not met.
- **[THEORY-009](../theory.d/THEORY-009.md)** says the paper "use[s] a symmetric square-integrable kernel to
  apply the spectral theorem (App. F)". That is right in substance, and
  weaker on the page than the theory implies.
  - The word "symmetric" does not occur in the paper. The symmetry of
    k(u,v) = w(u,v)/√(w(u)w(v)) follows from w(u,v) = w(v,u), which holds
    because both views are drawn from the same A(·|x̄). The paper relies on
    it without saying so.
  - Symmetry is also used throughout the finite-case main text, not only
    in Appendix F. It gives the orthonormal eigenvectors of Ā, the
    Eckart–Young step, the Laplacian quadratic form (eq. 12) and the
    undirected-graph Cheeger inequality (Lemma B.4).
  - The proof that λ_i ≤ 1 in Theorem F.2 cites only w ≥ 0. That is not
    enough. What makes it true is that w is a Gram kernel, w = E[A(·|x̄)A(·|x̄)].
  - None of this touches Riesz, which the paper never mentions. That is
    what [THEORY-009](../theory.d/THEORY-009.md) claims.
- The LIT's seed note says Lemma 3.1 is "the formal version of 'a linear
  probe only sees a representation up to GL(k)'". That holds, with a
  positive per-point scaling added on the left.
- The paper does carry ML practice: a loss to train with, and a
  recommendation of a projection head and a norm-constrained output. Its
  anthology-candidate flag stands. What this record holds it for is the
  spectral and operator statement, not the practice.

## Limitations

- The guarantee is at the population minimizer, and Assumption 3.7
  assumes the class can reach it. The paper says it "does not capture the
  potential implicit bias of optimizers" (§7).
- Only the spectral contrastive loss is analysed. The resemblance to the
  SimCLR loss (§3.2) is an algebraic remark, not a result.
- The trained models project outputs to a sphere of radius √μ. The theory
  has no such constraint, and Johnson et al. (F.5) find that this kind of
  norm constraint caps the sum of the learned eigenvalues.
- The infinite-support case rests on a bounded density ratio, and its
  extension of the main theorems is not written out.
- α, ρ and Δ_γ are not measured on any real dataset. The ImageNet claims
  about α ("exponentially small") are argued, not shown.

## Open questions

- Do the guarantees hold under the finite-χ² (Hilbert–Schmidt) condition
  alone, without the uniform bound of Assumption F.1? A written-out
  extension of Theorem B.3 to L²(w) under ∫∫K⁺² dP dP < ∞ would settle it.
- What does a network trained with the spectral loss and a finite-capacity
  head actually reach, and how far is it from F*? Theorem 4.2 bounds the
  consequence of excess loss, not the excess loss of a trained model.
- Is there an analogue for asymmetric pair structures, where w(u,v) ≠ w(v,u)
  and the eigenvector step has to become a singular-vector step?
