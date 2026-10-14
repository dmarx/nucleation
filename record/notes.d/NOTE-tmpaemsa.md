---
status: Read
paper: LIT-985
title: 'Kothapalli & Tirer — Can Kernel Methods Explain How the Data Affects Neural Collapse?'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read from the arXiv PDF (v3 of 25 April 2025, the TMLR version, 33
    pages), fetched from arxiv.org/pdf/2406.02105 and extracted with
    pdftotext, plain and -layout. Read in full: the main text (§§1–8), and
    the appendices the main claims rest on. Those are A (Theorem 4.1's
    proof), C (Lemma C.3), D (the proof of Theorem 5.1 for the NNGP and
    NTK), F (the relative NC1 metric and Corollary F.2) and G (training
    details and the multi-class, imbalanced and deeper experiments).
    Appendix B (kernel formulas) and the Erf derivations of Appendix E were
    skimmed: their expansions were not followed term by term. The figures
    were read from their captions and the text. The extraction loses
    subscripts; the expressions below were checked against the -layout
    text.
date: '2026-10-14'
summary: >-
  NC1, measured as tr Σ_W / tr Σ_B, is written for any kernel as a function
  of the kernel matrix. For two-class, one-dimensional Gaussian data with
  the classes on opposite sides of the origin, the ReLU NTK of a wide
  two-layer net is a scaled copy of the NNGP kernel within each class and
  zero across classes. So lazy-regime training leaves expected NC1 where it
  was at initialization. In higher dimensions the NTK is measured no more
  collapsed, and with ReLU less. A data-aware kernel lowers NC1 for
  separable data but tracks finite networks poorly when the classes
  overlap or are imbalanced. Erf collapses more than ReLU.
---
<!-- inactive-ok-file: THEORY-083 THEORY-212 THEORY-tmpqg4nq THEORY-tmptj5wo THEORY-tmpye6gw — Proposed; the record's statement of collapse, the lazy-versus-rich regime account, the two UFM accounts this reading sets beside, and the theory filed from it -->

# NOTE-tmpaemsa: Kothapalli & Tirer — Can Kernel Methods Explain How the Data Affects Neural Collapse?

## Contribution

Theories of neural collapse use unconstrained-features models, in which the
data enter only through the labels. This paper gives an NC1 formula for
features defined by any kernel, so the data enter. It uses the formula to
show, in one solvable case, that the infinite-width NTK gives the same
within-class variability as the NNGP at initialization. In that case the
lazy regime does not collapse anything. It then tests a data-aware kernel
(Seroussi et al.'s equations of state) as the alternative, empirically and
with mixed results.

## Key insight

If training is lazy, the features are fixed at their initial kernel up to a
reweighting. A reweighting that is the same within each class cannot change
a ratio of within-class to between-class spread. So collapse, if it occurs,
is something only feature learning can produce. The data-dependence that
UFMs cannot see has to come from a kernel that moves with the data.

## Assumptions

- **Network.** A two-layer fully connected net, width d₁, Gaussian
  initialization, MSE loss, output dimension d₂ = 1 for the theory.
- **NC1 metric.** NC1(H) = tr(Σ_W(H)) / tr(Σ_B(H)) (Eq. 7, after Tirer et
  al. 2023). That is not [LIT-618](../literature.d/LIT-618.md)'s (1/C) tr(Σ_W Σ_B†).
- **For Theorem 5.1.**
  - Assumption 1: d₀ = 1, C = 2, x_(1,i) ~ N(μ₁, σ₁²), x_(2,j) ~ N(μ₂, σ₂²),
    with μ₁ < 0 < μ₂, |μ_c| ≫ σ_c, and x_(1,i)x_(2,j) < 0 almost surely.
  - Assumption 2: n₁, n₂ ≫ 1.
  - Assumption 3: d₂ = 1, σ_b → 0.

  The classes sit on opposite sides of the origin.
- **Expected NC1** is approximated as E[tr Σ_W]/E[tr Σ_B] plus a
  higher-order term Δ_h.o.t. that vanishes as n_c grows (a ratio-of-means
  expansion).
- **Finite networks.** Width d₁ = 500, trained by full-batch GD (learning
  rate 10⁻³ for Erf and 10⁻⁴ for ReLU, weight decay 10⁻⁶, 1000 steps).
  Training loss reaches a plateau with correct signs (Figure 8). This is
  the paper's "terminal phase".

## Key results

- **Theorem 4.1.** For features with inner products given by a kernel
  Q(x, x′) = hᵀh′, tr Σ_W and tr Σ_B are explicit sums over the class
  blocks Q_(c,c′) of the kernel matrix. *Holds:* any kernel, any class
  sizes.
- **Theorem 5.1 (ReLU).** Under Assumptions 1–3,
  E[NC1(H_GP)] = E[NC1(H_NTK)]. The proof (Appendix D) rests on two facts.
  The ReLU NNGP kernel is (σ_w²/2)xx′ within a class and 0 across classes,
  since xx′ < 0 (Eq. 54). And the NTK is (σ_w⁴/2 + σ_w²/2)xx′ within a
  class and 0 across (Eq. 56): "a scaled version" of the NNGP. The value
  is Σ_c[(n_cμ_c² + n_cσ_c²)/N − μ_c²/2] / Σ_c[μ_c²/2 − n_c²μ_c²/N²]
  + Δ_h.o.t. (Eq. 57).
- **A discrepancy.** Eq. 16 as printed also subtracts
  (2/N²)n₁n₂μ₁μ₂ in the denominator, and the text's balanced case reads
  E[NC1] = 2(σ₁² + σ₂²)/(μ₁ − μ₂)² + Δ_h.o.t. But the cross-class kernel is
  zero (Eq. 54), so that term should vanish, as Eqs. 57 and 153 have it.
  Without it the balanced value is 2(σ₁² + σ₂²)/(μ₁² + μ₂²). That is twice
  the printed value when μ₁ = −μ₂. It agrees with Appendix F's ratio of
  about 2 between feature NC1 and data NC1 in that case. This check is the
  reading's, not the paper's.
- **Erf (Appendix E).** By expansions under |μ_c| ≫ σ_c, the NNGP and NTK
  give "similar values" of expected NC1. This is approximate, not an
  equality.
- **Higher dimensions (Figures 2–3).** Data are
  D₁(N, d₀): N(∓2·1, 0.25·I), with d₀ ∈ {1, 2, 8, 32, 128},
  N ∈ {128, …, 1024}, and 10 draws each.
  - NC1 is about 10^(−2.1) for Erf and about 10^(−0.95) for ReLU at
    d₀ = 1.
  - The NTK tracks the NNGP for Erf as d₀ grows.
  - For ReLU the NNGP stays flat while the NTK rises: less collapse.
  - Finite width-500 nets also give Erf below ReLU, and shift trend
    beyond d₀ = 32.
- **Data-aware kernel (§6, Figures 4–5).** The equations of state were
  solved by Newton–Krylov with a hand-chosen annealing schedule.
  - At d₁ = 2000 they match the NNGP.
  - At d₁ = 500 NC1 drops below the NNGP for d₀ ≥ 8 and N ≥ 512, in the
    direction of the finite net.
  - With overlapping classes, N(∓2·1, 4·I), they track the net for
    d₀ ≤ 32. For d₀ ∈ {64, 128} the net's NC1 is "almost twice as large".
- **Imbalance and more classes (Appendix G).**
  - With C = 4 the trends persist.
  - Under imbalance (n₁, n₂) of (768, 1280), (512, 1536) and (256, 1792),
    "the magnitude of NC1(H) in 2L-FCN and kernel methods show opposing
    trends" (Figures 12–13).
- **Relative NC1 (Appendix F).** NC1(H|X) = NC1(H)/(NC1(X) + τ). For ReLU
  under Assumptions 1–3 the ratio is about 1 − 2n₁n₂μ₁μ₂/[N² Σ_c(μ_c²/2 −
  n_c²μ_c²/N²)], about 2 when n₁ = n₂ and μ₁ = −μ₂. The kernel features
  are then *less* collapsed than the raw inputs. With well-separated
  classes, N(∓10·1, I), NC1(H|X) exceeds 1 in high dimension: "the raw
  data is 'more' collapsed than the activations".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | NC1 of kernel-defined features is a closed function of the kernel matrix's class blocks | strong | Theorem 4.1, App. A |
| C2 | In the lazy regime a wide two-layer ReLU net's features have the expected NC1 of its initialization | strong in its setting; the setting is narrow | Theorem 5.1, App. D; 1-D, two classes on opposite sides of 0, σ_b → 0 |
| C3 | The NTK is not more collapsed than the NNGP in higher dimensions | moderate | Figures 2–3; Gaussian data, two classes, 10 draws |
| C4 | Erf yields lower NC1 than ReLU | moderate | App. E expansions; Figures 2–3 |
| C5 | A data-aware kernel lowers NC1 below the NNGP and approximates finite nets on separable data | weak | Figures 4–5; numerical solutions with a hand-tuned schedule, no existence or uniqueness result |
| C6 | The data-aware kernel fails to track finite nets under overlap or imbalance | moderate | Figures 5, 12, 13 |
| C7 | Raw NC1 can mislead when the inputs are already collapsed | moderate | Corollary F.2, Figure 6 |

## Concepts

- **NC1 here.** tr Σ_W / tr Σ_B for features H, a scalar rather than
  [LIT-618](../literature.d/LIT-618.md)'s (1/C) tr(Σ_W Σ_B†).
- **NNGP kernel.** The infinite-width kernel of a network at random
  initialization.
- **NTK.** The infinite-width tangent kernel, which stays fixed under
  gradient descent with small learning rate (the lazy regime).
- **Data-aware GP kernel (equations of state).** Seroussi et al.'s
  variational Gaussian approximation of a finite-width trained net. The
  first-layer weight covariance C is updated from the residuals y − f, so
  the kernel adapts to the data.
- **Relative NC1.** NC1(H|X) = NC1(H)/(NC1(X) + τ): collapse of the
  features against collapse already present in the inputs.

## Connections

It sets itself against the unconstrained-features analyses, [LIT-974](../literature.d/LIT-974.md) and
[LIT-994](../literature.d/LIT-994.md) among them, which "rely solely on the labels". It builds on the
NNGP (Neal; Lee et al.), the NTK (Jacot et al.) and Seroussi, Naveh &
Ringel's (2023) adaptive kernels. It relates to Seleznova et al. (2023),
who show that a block-structured empirical NTK implies collapse without
saying how it arises. It cites the first author's review ([LIT-978](../literature.d/LIT-978.md)). It
justifies studying shallow nets by the monotone depthwise decrease of NC1
reported by Tirer & Bruna, Rangamani et al. and He & Su.

## Bearing on the record

- **[QUESTION-051](../questions.d/QUESTION-051.md).** On the first half, why training reaches collapse, it
  contributes a negative result. Lazy, kernel-regime training does not
  produce collapse, at least where it can be computed. So the explanation
  has to be about feature learning. It also contributes the only held
  attempt to put the data into the account. On the second half it says
  nothing.
- **The LIT's summary** says the paper shows "that for Gaussian data the
  NTK does not give more collapsed features than the NNGP". The theorem is
  for one-dimensional data, two classes on opposite sides of the origin,
  and zero bias. In that setting the ReLU NTK is a within-class rescaling
  of the NNGP, so the equality is close to built in. The arbitrary-dimension
  statement in the abstract is empirical. Its ReLU result is that the NTK
  is *less* collapsed as dimension grows. The summary should say so.
- **[THEORY-083](../theory.d/THEORY-083.md).** No bearing on the measured regularity. The paper's NC1
  is a different scalar, and its networks are two-layer, MSE-trained and
  binary.
- **[THEORY-212](../theory.d/THEORY-212.md) (lazy versus rich regimes).** Consistent. [THEORY-212](../theory.d/THEORY-212.md) says
  unbalanced layers learn with a static kernel and leave the larger layer
  task-agnostic. This paper shows that a static kernel leaves within-class
  variability where initialization put it.
- **[THEORY-tmpqg4nq](../theory.d/THEORY-tmpqg4nq.md) and [THEORY-tmptj5wo](../theory.d/THEORY-tmptj5wo.md).** Both are UFM accounts. This
  paper is the record's statement of their shared limit: they cannot say
  why the extent of collapse differs between datasets.
- **Filed.** [THEORY-tmpye6gw](../theory.d/THEORY-tmpye6gw.md) states the lazy-regime result at the
  strength shown.
- No instruction for machine-learning practice is relied on.

## Limitations

- The theorem's setting is narrow: d₀ = 1, two classes, classes separated
  by the origin, zero bias. Everything beyond it is simulation on Gaussian
  mixtures.
- The networks are shallow, binary, MSE-trained, and trained for 1000
  full-batch steps. That is far from the terminal phase of [LIT-618](../literature.d/LIT-618.md).
- The data-aware kernel has no existence or uniqueness theory, and its
  solutions depend on a hand-chosen annealing schedule (§7).
- Expected NC1 is a ratio-of-means approximation with a residual that is
  only said to vanish for large n_c.
- The printed Eq. 16, and its balanced specialization, appear to include
  a cross-class term that the kernel sets to zero (see Key results).

## Open questions

- Does a data-aware kernel predict the dataset dependence of collapse in
  deep nets? For example, the gap between CIFAR-10 and ImageNet that
  [LIT-978](../literature.d/LIT-978.md) reports.
- Is there a closed-form result beyond the one-dimensional case? In
  particular, where the NTK and NNGP differ by more than a within-class
  rescaling.
- Should collapse be reported relative to the inputs' own NC1?
  Appendix F shows the raw number can mislead.
