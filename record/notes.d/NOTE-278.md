---
number: 278
status: Read
formerly:
- NOTE-tmp6a0yy
paper: LIT-323
title: 'Toy Models of Superposition'
version: 1
history:
- version: 1
  date: '2026-09-29'
  note: >-
    Read in full (The full text of arXiv 2209.10652 (v1, the only version,
    submitted 21 Sep 2022), from the arXiv PDF. That PDF is a 62-page
    browser print of the Transformer Circuits article, dated 16 Sep 2022 in
    its metadata. I read all of it: - the definitions and motivation; -
    Demonstrating Superposition; - Mathematical Understanding; -
    Superposition as a Phase Change; - the Geometry of Superposition
    (uniform, the polytope aside, and non-uniform with correlated and
    anticorrelated features); - Learning Dynamics; - Adversarial Robustness;
    - Superposition in a Privileged Basis; - Computation in Superposition
    (including the asymmetric-superposition motif); - the Strategic Picture;
    - Discussion and Open Questions; - Related Work; - the Comments &
    Replications (Sachan, McGrath, Wu & Mossing); - author contributions,
    the 27 footnotes and the 57 references; - the two appendices: Nonlinear
    Compression, and the compressed-sensing lower bound with Lemma 1 and
    Theorem 2. The displayed equations of Mathematical Understanding are
    images. I read them from a rendering of PDF p. 13. I also read the
    current HTML at transformer-circuits.pub/2022/toy_model for comments
    added after the arXiv print: Becker-Kahn; Jermyn, Hubinger & Schiefer;
    Henighan & Olah on "pressure"; Hobbhahn; Sharkey, Braun & Millidge;
    Nanda on Othello; and Fred Zhang on leverage scores. Figures are
    interactive or raster, and their content is taken from captions and
    text. I checked the feature-dimensionality values of the triangle,
    pentagon and tetrahedron numerically (2/3, 2/5, 3/4, as the paper says),
    and the frame property used under Bearing.). The first NOTE on this
    paper, which was seeded from its abstract alone.
date: '2026-09-29'
summary: >-
  In a toy autoencoder x′ = ReLU(WᵀWx + b), with n sparse synthetic
  features compressed into m < n dimensions, a linear model keeps only the
  top-m features, but with the output ReLU and sparse enough features the
  model stores more features than dimensions ("superposition"), in
  non-orthogonal directions whose interference the ReLU and a negative
  bias filter out. Whether a feature is dropped, superposed or given a
  dedicated dimension changes discontinuously with sparsity and
  importance, and in the n = 2, m = 1 theory this is a first-order phase
  change. With uniform features the directions settle into uniform
  polytopes, with feature dimensionalities clustering at 3/4, 2/3, 1/2,
  2/5 and 3/8. A ReLU hidden layer creates a privileged basis in which
  monosemantic and polysemantic neurons coexist, and a model can compute
  |x| for more features than it has neurons. Everything is shown in toy
  models only, and the authors expect the geometry and learning-dynamics
  results to generalise least.
---

# NOTE-278: Toy Models of Superposition

## Contribution

The paper demonstrates, in a model simple enough to analyse, that neural networks can represent more independent features than they have dimensions. It explains why: sparsity makes interference rare, and a nonlinearity filters what remains.

Before it, "superposition" was a hypothesis offered to explain polysemantic neurons. After it there is a toy setting where superposition provably helps, together with:

- a phase diagram for when it occurs;
- a geometry of how features pack;
- a mechanism by which a privileged basis (an elementwise activation) pulls features toward neurons;
- a demonstration that computation, not just storage, can happen in superposition.

It also fixed the vocabulary the later sparse-autoencoder programme uses.

## Key insight

A linear model can only afford orthogonal features, so it keeps the m most important and drops the rest (PCA). Put a ReLU on the output and give it a negative bias, and a different trade becomes available. Pack extra features at non-orthogonal angles and pay only when two of them are active at once, which sparsity makes rare, while the ReLU and bias zero out small spurious activations. The loss then has a *feature-benefit* term that rewards representing features and an *interference* term that punishes overlap. Their balance, set by sparsity and importance, decides each feature's fate discontinuously: drop, superpose, or dedicate a dimension.

## Assumptions

- **Synthetic features.**
  - *Values:* each xᵢ is 0 with probability S and otherwise uniform on [0, 1] (on [−1, 1] in the absolute-value model).
  - *Sparsity:* mostly one shared S.
  - *Importance:* importances Iᵢ decay geometrically, e.g. 0.7ⁱ for n = 20, m = 5, and 0.9ⁱ for n = 80, m = 20.
  - *Independence:* features are independent unless stated otherwise.
  - *What they stand for:* the input basis is stipulated to be the activations of an "idealized, disentangled larger model".
- **Models.**
  - *Linear:* x′ = WᵀWx + b.
  - *ReLU output:* x′ = ReLU(WᵀWx + b), with W ∈ R^{m×n} tied, so decoding uses Wᵀ.
  - *ReLU hidden:* h = ReLU(Wx), x′ = ReLU(Wᵀh + b).
  - *Absolute value:* h = ReLU(W₁x), y = ReLU(W₂h + b), with untied weights and target |x|.
- **Loss.** Importance-weighted squared error, L = Σ_x Σᵢ Iᵢ(xᵢ − x′ᵢ)².
- **Symmetry.** In the ReLU-output model the hidden space has no privileged basis: W ↦ OW for orthogonal O leaves (OW)ᵀ(OW) = WᵀW, and hence the model, unchanged. A privileged basis comes only from an elementwise nonlinearity on the hidden layer, or from L1 on its activations.
- **Optimisation caveats.** Many results are best-of-many runs. The phase diagrams train ten models per point and discard the worst. The privileged-basis figures show the best of 1,000 models. The authors note that m = 2 is "really challenging" for gradient descent.

## Key results

- **Linear versus ReLU (Demonstrating Superposition).** The linear model learns the top-m features at every sparsity. The ReLU-output model matches it on dense data, but as 1 − S falls it represents more features, first in antipodal pairs and then in other geometries, starting with the least important.
- **The loss, decomposed (Mathematical Understanding; equations read from the page image).**
  - *Linear model, Saxe-style:* L ∼ Σᵢ Iᵢ(1 − ‖Wᵢ‖²)² + Σ_{i≠j} I_j(W_j·Wᵢ)², feature benefit plus interference. "this makes it never worthwhile for the linear model to represent more features than it has dimensions" (footnote 12: set the gradient to zero, or see Saxe et al.). A footnote contrasts the interference term, an L² norm of the overlaps, with compressed-sensing coherence, their L^∞ norm.
  - *ReLU model:* L = Σ_k (1 − S)^k S^{n−k} L_k, grouped by the number k of active features. L₀ = Σᵢ ReLU(bᵢ)² penalises positive biases. For k = 1 at xᵢ = 1: L₁ = Σᵢ Iᵢ(1 − ReLU(‖Wᵢ‖² + bᵢ))² + Σ_{i≠j} I_j ReLU(W_j·Wᵢ + b_j)².
  - *Consequences:* negative interference is "free" in the 1-sparse case. With ‖Wᵢ‖ ∈ {0, 1} and b = 0, the interference term is a generalised Thomson problem (points on a sphere).
- **Phase change.**
  - *n = 2, m = 1:* the empirical diagram, with importance of the second feature from 0.1 to 10 and density from 1 to 0.01, matches a theoretical one built from three configurations: [1, 0] (drop the extra), [0, 1] (drop the first), and [1, −1] (antipodal superposition). There is "crossover between the functions, causing a discontinuity in the derivative of the optimal loss", a first-order transition.
  - *n = 3, m = 2:* four candidate solutions, same picture.
  - *Scope:* "phase change" is used "in the generalized sense of 'discontinuous change'", not the infinite-size limit (footnote 13).
  - *McGrath's replication:* he solved n = 2, m = 1 in closed form and found a further "confused feature" phase, W₁ ≈ W₂ ≈ 1/√2. The transition out of it is discontinuous, but the antipodal region's transitions are partly continuous, which explains the "blurry" triple point.
- **Geometry (uniform, n = 400, m = 30).**
  - *Dimensions per feature:* D* = m/‖W‖²_F is "sticky" at 1 and 1/2, the latter from antipodal pairs.
  - *Per feature:* Dᵢ = ‖Wᵢ‖² / Σ_j(Ŵᵢ·W_j)² clusters at 3/4 (tetrahedron), 2/3 (triangle), 1/2 (antipodal pair), 2/5 (pentagon), 3/8 (square antiprism) and 0 (not learned).
  - *Structure:* many configurations are tegum products, orthogonal factor polytopes with no interference across factors. Dimensionalities of efficiently packed features sum to m (empirically). Fred Zhang's HTML comment explains why: Dᵢ equals the leverage score when the vectors are in isotropic position, and leverage scores sum to the rank.
  - *Polytopes and low-rank matrices:* there is an "exact correspondence between polytopes and strategies for superposition" via the rank-m PSD matrix WᵀW. Not representing (1, 1, …, 1) gives the regular simplex, "minimal possible superposition".
- **Non-uniform geometry.**
  - *One feature varied:* making one of five features (m = 2) sparser or denser deforms the pentagon continuously until a first-order jump to two digons, confirmed by crossing loss curves.
  - *Correlated features:* these prefer orthogonality (separate tegum factors), giving "local almost-orthogonal bases". Failing that, they sit side by side. Failing that, they collapse to their principal component (a + b)/√2, becoming PCA in the dense limit.
  - *Anticorrelated features:* these prefer negative interference, ideally antipodal.
- **Learning dynamics.** Training shows discrete "energy level" jumps, in which feature dimensionalities swap with small drops in loss. With n = 6, m = 3 (three correlated pairs), learning passes through distinct geometric stages to an octahedron. The authors call it one of several possible trajectories.
- **Adversarial vulnerability.**
  - *Attacks:* analytic optimal L² attacks per feature, capped at 0.1 of mean input norm.
  - *Vulnerability:* it "sharply increases as superposition forms (increasing by >3x)" and tracks features per dimension.
  - *Adversarial training:* it reduces superposition only with attacks at 80% of input norm.
  - *Interpretation:* the authors are "hesitant to speculate" about real models.
- **Privileged basis (ReLU hidden layer, n = 10, m = 5, I = 0.75ⁱ).** As sparsity rises, neurons shift from monosemantic to polysemantic, and both kinds coexist in one model. The authors flag a weakness: the model "will only use the ReLU activation function if absolutely forced", for example by setting positive biases.
- **Computation in superposition (absolute value).**
  - *Small case:* with n = 3, m = 6, each feature gets a ReLU(xᵢ) and a ReLU(−xᵢ) neuron.
  - *Larger case:* with n = 100, m = 40, I = 0.8ⁱ, sparse regimes compute |x| for more features than neurons allow. The most important features stay monosemantic. Many neurons have one "primary" feature with large weight plus small "secondary" ones, like real-model neurons that look interpretable at their top activations.
  - *A motif:* asymmetric superposition, e.g. encoding weights [2, −½] with reciprocal output weights [½, 2], paired with an inhibitory neuron that turns positive interference into negative.
- **Compressed-sensing bound (appendix).** Theorem 1: if the toy model recovers every k-sparse x to within ε and W₁ has the (δ, k) restricted isometry property, then m = Ω(k log(n/k)). This goes through a denoising reduction (Lemma 1) and Do Ba–Indyk–Price–Woodruff. With k = O((1 − S)n), this gives m = Ω(−n(1 − S) log(1 − S)), "linear in m but modulated by the sparsity".
- **Nonlinear compression (appendix).** t = (⌊Zx⌋ + y)/Z packs two dense [0, 1) values into one. With smoothed discontinuities (ε = 0.1) and Z as small as 3 it beats linear compression. The authors argue that models are unlikely to use such schemes pervasively.
- **Strategic picture.**
  - *Enumerative safety:* the goal is enumerating all features, "a universal quantifier over the fundamental units".
  - *"Three ways out":* train superposition-free models (L1 on activations works in the toys, at a loss cost; MoE as a flops argument); find an overcomplete basis after the fact (sparse coding); or hybrids.
  - *Phase changes as hope:* there is a regime with no superposition.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | A ReLU-output toy model stores more features than dimensions when features are sparse; a linear model never does | strong (experiment + argument) | Demonstrating Superposition; the linear case follows from the Saxe-style loss (footnote 12, not written out) |
| C2 | The 1-sparse loss is feature benefit plus ReLU-gated interference, and with fixed norms and zero bias reduces to a generalised Thomson problem | strong (derivation) | Mathematical Understanding, displayed equations |
| C3 | The drop / superpose / dedicate choice is a first-order phase change | strong for n = 2, m = 1 (closed-form losses) and n = 3, m = 2; moderate beyond | theoretical and empirical phase diagrams; McGrath finds parts of the boundary continuous |
| C4 | Uniform superposition organises features into uniform polytopes and tegum products, with dimensionalities at 3/4, 2/3, 1/2, 2/5, 3/8 | strong (experiment), in the toy | n = 400, m = 30 scatter of Dᵢ; replicated by Wu & Mossing |
| C5 | Correlated features go orthogonal, then side by side, then collapse to their principal component; anticorrelated features go antipodal | moderate | small m = 2 experiments and one larger WᵀW plot |
| C6 | Learning proceeds by discrete jumps between geometries | weak–moderate | a few training runs shown; "we aren't able to give these questions the detailed investigation they deserve" |
| C7 | Superposition increases adversarial vulnerability (>3×), tracking features per dimension | moderate (toy experiment) | analytic L² attacks; relation to real adversarial examples explicitly not claimed |
| C8 | Elementwise nonlinearities create a privileged basis in which monosemantic and polysemantic neurons coexist | moderate | ReLU hidden-layer model (best of 1,000 runs; the model evades its ReLU when it can) and the absolute-value model |
| C9 | Networks can compute (not just store) in superposition | moderate (one computation) | absolute value, n = 100, m = 40; "Is the absolute value problem representative … or idiosyncratic?" is left open |
| C10 | Real networks exhibit superposition | weak (consistency argument) | Discussion: toy predictions match observed polysemanticity (InceptionV1 depth trend, early transformer MLPs); no real-model measurement |
| C11 | Toy recovery with an RIP embedding needs m = Ω(k log(n/k)) | strong (proof, under assumed RIP and exact recovery of all k-sparse x) | appendix Theorem 1; the trained toy does not recover all features, so the hypothesis is stronger than the model's behaviour |

## Method

1. Train small tied or untied autoencoders on synthetic sparse features with controlled sparsity, importance and correlation.
2. Visualise WᵀW and b, feature norms ‖Wᵢ‖ and interference Σ_{j≠i}(Ŵᵢ·W_j)².
3. Compare against closed-form losses of candidate weight configurations.
4. Measure the per-feature dimensionality Dᵢ, and read geometry off feature-graph plots.
5. Add a hidden ReLU to study privileged bases, and a nonlinear target to study computation.

## Concepts

- **Feature** — used here in the sense "properties of the input which a sufficiently large neural network will reliably dedicate a neuron to representing". The authors hold this loosely and discuss two alternatives.
- **Linear representation** — features correspond to directions Wᵢ, and several active features are represented by Σ xᵢWᵢ. The features are nonlinear functions of the input; only the feature-to-activation map is linear.
- **Decomposability / linearity / superposition / basis-alignment** — the four "progressively more strict" properties. The authors hypothesise the first two to be widespread.
- **Privileged basis** — a basis made special by the architecture (an elementwise activation), so that it makes sense to ask whether a neuron is interpretable. A non-privileged representation, such as word embeddings or the residual stream, is defined only up to an invertible change M with M⁻¹ applied to the next weights.
- **Superposition** — representing more features than dimensions, at almost-orthogonal angles.
- **Polysemantic neuron** — a basis direction responding to several unrelated features.
- **Feature dimensionality Dᵢ** — ‖Wᵢ‖² / Σ_j(Ŵᵢ·W_j)²: 1 for a dedicated dimension, 1/2 for an antipodal pair, 0 if unlearned.
- **Tegum product** — a polytope formed from factors in orthogonal subspaces; no interference crosses factors.
- **Enumerative safety** — being able to quantify over all features of a model.

## Connections

- **[LIT-304](../literature.d/LIT-304.md) (Park et al.).** Park et al. cite this paper among the sources of the linear representation hypothesis. The two are in quiet tension, which neither paper states; this is my inference. Park et al.'s causal inner product requires *all* causally separable concepts to be mutually orthogonal (Def. 3.1), and Thm 3.4 assumes d of them form a basis. Under superposition there are far more than d approximately independent features, and no inner product makes more than d nonzero directions pairwise orthogonal. So Park et al.'s framework, applied to superposed features, must either declare most of them non-separable or fail. Their 27 concepts in d = 4,096 never meet the limit.
- **[LIT-322](../literature.d/LIT-322.md) (Engels et al.).** It generalises this paper's superposition hypothesis from directions to low-dimensional subspaces, and takes up the multi-dimensional case this paper defers to an appendix that does not exist.
- **[LIT-302](../literature.d/LIT-302.md) (Platonic hypothesis).** Connected only through the symmetry point. In a non-privileged space only the rotation-invariant WᵀW (a Gram matrix) is meaningful, which is the same reason PRH compares models by kernels. This paper lists "universality", analogous features across networks, among its motivating phenomena. It does not measure it.
- **[LIT-267](../literature.d/LIT-267.md) (Xiong).** This is my inference. The toy model's readout, ReLU(Wᵢ·h + bᵢ) with a negative bias, *is* a thresholded linear direction, the half-space form Xiong's lattice presupposes. The toy model also shows when crisp half-space incidence breaks: when several features in superposition are active at once ("compounding interference"). So a probe-thresholded incidence of Xiong's kind should be exact only in the sparse, 1-active regime, and degrade as co-activation rises.
- **Anthology.** It holds Chen et al. 2023 on a toy model of superposition ([ANTH-LIT-544](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-544.md)), but not this paper.

## Bearing on the record

- **What it supplies for the prior-art map's role (§4 must-cite, "features as (non-orthogonal) directions").**
  - *It owns the statement.* It is the right citation for "features are directions, and there are more of them than dimensions, so they are not orthogonal", and for the privileged/non-privileged basis distinction.
  - *It sharpens the map's diagnosis.* The map calls the LRH "the single Boolean context / co-measurable corner". This paper shows that corner is exactly the *non-superposed* regime: dense features, or at most m features, which then sit orthogonally like PCA. Its whole subject is the regime where the features do *not* form one orthonormal frame.
- **A precise bridge to the projector formalism.** This is my inference, not the paper's, and I checked it numerically. In the efficiently packed uniform geometries (triangle, pentagon, tetrahedron, and antipodal pairs), the unit feature vectors form a *tight frame*: Σᵢ WᵢWᵢᵀ = (n/m)·I_m. So Eᵢ = (m/n)WᵢWᵢᵀ is a rank-one POVM on R^m, a single unsharp observable whose elements do not commute, not a projection-valued measure. Each Eᵢ has trace m/n, which equals the paper's feature dimensionality Dᵢ for these configurations: 2/3, 2/5 and 3/4 check out. V = √(m/n)·W is a co-isometry. Compressing the n-dimensional standard basis (a PVM, one Boolean context) through V gives exactly this POVM, which is Naimark's dilation run backwards.
  - *Why it matters for the map:* the paper's own slogan, that a small network is "noisily simulating larger, highly sparse networks", becomes a theorem-shaped statement. Superposition is the compression of one Boolean context (the disentangled model's feature basis) into a smaller space, where it survives only as a non-projective, non-commuting POVM.
  - *For the response:* the most defensible version of "the LRH is the Boolean shadow" may be this one. The LRH's orthogonal-features picture holds in the hypothetical dilated space, and the model's actual space carries a POVM. That is a known structure in quantum measurement theory and a known one here (tight frames, leverage scores), and it has not, to my knowledge, been joined to the LRH debate.
  - *Limits:* tightness holds only for efficient uniform packings. Non-uniform superposition is not a tight frame, so this is an idealisation, like the rest of the toy.
- **[THEORY-017](../theory.d/THEORY-017.md) (basis and unitary invariance).** A clean ML instance, and a candidate row for its table.
  - *Intrinsic:* in the non-privileged ReLU-output model, the orthogonal group acts on the hidden space as a symmetry, and only the Gram matrix WᵀW is intrinsic. The authors visualise WᵀW, and use ‖W‖²_F because it "is basis-independent", for exactly this reason.
  - *Where the basis comes from:* the input *feature* basis is stipulated from outside (the "disentangled larger model"), and a *neuron* basis is supplied by the architecture (an elementwise nonlinearity) or by regularisation (L1).
  - *The fork:* this is [THEORY-017](../theory.d/THEORY-017.md)'s fork in ML dress. The model either computes invariants of WᵀW, or an elementwise nonlinearity has supplied a basis.
  - *Status:* the paper does not state this as a general principle. It is my placement, for the owner to decide on.
- **[THEORY-004](../theory.d/THEORY-004.md) / [THEORY-008](../theory.d/THEORY-008.md).** WᵀW is the kernel of the feature directions. The paper's choice to analyse it is [THEORY-004](../theory.d/THEORY-004.md)'s "a representation is fixed by its kernel up to orthogonal transformation", applied to weights rather than data.
- **ML practice (anthology-candidate).** Yes, a candidate for the Anthology of the SOTA, primarily as a LIT with a THEORY (superposition as the account of polysemanticity). It carries weak practice content:
  - *Neurons:* do not assume neurons are features in superposed layers.
  - *Regularisation:* L1 on activations removes superposition in toys, at a loss cost.
  - *Sparse coding:* recover an overcomplete basis by sparse coding. The practice itself, sparse autoencoders, is sourced by later work, and the Sharkey et al. comment in the HTML is its first toy test.
  - *Anthology context:* [ANTH-LIT-544](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-544.md) (Chen et al.) is held. This paper, its trunk, is not, which is DP-007's "refinement filed before the thing it refines".
- **For filing.**
  - *Tags:* `representation-learning` first, `anthology-candidate` second, as seeded. Also defensible: `mathematics`, for the polytope correspondence and the compressed-sensing bound.
  - *URL:* the seed has no `url:`. Adding transformer-circuits.pub/2022/toy_model/index.html would record the canonical, updated version, since the arXiv print lacks later comments.

## Limitations

- **Toy models only.** The case for real networks is consistency with observed polysemanticity. The authors expect the geometry and learning dynamics to generalise least ("much more uncertain").
- **Synthetic, independent, uniform-on-[0, 1] features with stipulated importances,** and the input basis is by construction the true feature basis. Real models give no ground truth, which the authors name as the main obstacle.
- **Exact analysis only for n = 2, m = 1** (and its closed form came partly from a commenter). Beyond that, results are empirical and often best-of-many-runs.
- **The privileged-basis ReLU hidden model evades its nonlinearity when it can.** Computation in superposition is shown for one function, absolute value.
- **The compressed-sensing bound assumes RIP and exact recovery of every sparse vector,** neither of which the trained toy satisfies.
- **The definitions have a slip and a gap.** "Superposition iff WᵀW is not invertible" is too weak as a definition, and the promised appendix on multi-dimensional features is absent.

## Open questions

- In real models, do superposed feature directions approach a tight frame, so that the POVM reading holds? If so, does their Gram matrix show the uniform-polytope structure? Leverage scores of SAE decoder directions would test the first question cheaply.
- Is there a closed form beyond n = 2, m = 1? Do the toy's phase changes relate to compressed sensing's Donoho–Tanner phase transition, as the paper suspects?
- How does superposition interact with an unidentified inner product ([LIT-304](../literature.d/LIT-304.md))? Superposition's "almost orthogonal" presumes a metric. In a softmax model's output space, which metric?

## Corrections to the seeded skim

- Seeded from metadata; the summary is accurate. Identification checks:
  - *Dates:* the arXiv abstract page lists only v1, submitted 21 Sep 2022. The PDF's first page gives "PUBLISHED Sept 14, 2022" on the Transformer Circuits Thread. The seed's dates stand.
  - *Authors and affiliations:* 16 authors, "Anthropic, Harvard", with Chris Olah as corresponding author. The seed stands.
  - *The arXiv print is a snapshot:* the live HTML carries seven further comments and replications not in it (listed under `read:`).
- The article points to an appendix, "What about Multidimensional Features?", for how its view "squares with a conception of features as being multidimensional manifolds". That appendix appears in neither the arXiv print nor the current HTML. The only appendices are Nonlinear Compression and the compressed-sensing bound. The article's position on multi-dimensional features is therefore unstated. Engels et al. ([LIT-322](../literature.d/LIT-322.md)) is the work that takes it up.
- A definitional slip. The "hierarchy of feature properties" says a linear representation "exhibits superposition if WᵀW is not invertible". With W: Rⁿ → R^m and n > m, WᵀW always has rank ≤ m < n, so this holds for every model in the paper. That includes the linear model, which simply drops n − m features. The operative notion elsewhere is different: more features represented (‖Wᵢ‖ ≈ 1) than there are dimensions, measured by the Frobenius norm ‖W‖²_F or by per-feature dimensionality.
- In the compressed-sensing appendix, Theorem 2 is quoted with "a k × n matrix A". The measurement matrix of the application is m × n. As extracted this is a slip, possibly an extraction artefact, and it does not change the stated bound m = Ω(k log(n/k)).
