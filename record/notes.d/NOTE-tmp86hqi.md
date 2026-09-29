---
status: Read
paper: LIT-tmpu9jwu
title: 'Learning the Irreducible Representations of Commutative Lie Groups'
version: 1
history:
- version: 1
  date: '2026-09-29'
  note: >-
    Read in full (Full text of arXiv 1402.4437 v2 (25 May 2014; the PDF
    carries "Proceedings of the 31st International Conference on Machine
    Learning, Beijing, China, 2014. JMLR: W&CP volume 32"), from the arXiv
    PDF, 9 pp.: abstract, §1 with related work §1.1, §2 (2.1 equivalence,
    invariance and reducibility; 2.2 maximal tori in SO(D)), §3 (Toroidal
    Subgroup Analysis; 3.1 invariant representation and metric; 3.2 relation
    to the DFT; 3.3 Lie subalgebra model; 3.4 maximum marginal likelihood
    learning), §4 experiments, §5 conclusions, all footnotes and the
    references. Nothing in the PDF was skipped. The text was extracted with
    PyMuPDF; Figures 1–4 survive as axis labels and captions only, so their
    content is taken from the captions and the prose. The "supplementary
    material" the text cites four times (the generalized-Bessel-function
    algorithm, the coupled-model marginal likelihood derivation, MAP
    inference) is not in the arXiv PDF and was not read. `published:` is the
    arXiv v1 date (18 Feb 2014). No anthology entry exists for this paper
    (grep of record/literature.d for the arXiv id and title: no hit). No
    nucleation entry either; the only mention is NOTE-288's second-hand
    description.). The first NOTE on this paper, which was seeded from its
    abstract alone.
date: '2026-09-29'
summary: >-
  Proposes "Weyl's principle" (via Kanatani 1990) as a definition of
  disentangling: the elementary components of data are the irreducible
  subspaces of the representation of a symmetry group acting on it. It
  learns such a decomposition for one class of group fixed in advance,
  compact commutative subgroups of SO(D) ("toroidal"), from pairs (x, y)
  of raw data vectors related by an unobserved group element, y = W R(φ)
  Wᵀx + ε. The orthogonal basis W (2-D invariant subspaces) is fitted by
  SGD on a closed-form marginal likelihood, and the integer weights ω_j
  are then read off a batch rotated by a known 0.1°. The only experiment
  trains 100 filters on 250,000 white-noise 16×16 patches paired with
  random rotations of themselves (learned ω from −11 to 12), and uses the
  invariant √κ̂ for 1-NN on rotated MNIST, reported in a figure with no
  numbers. Spectral degeneracy plays no role.
---

# NOTE-tmp86hqi: Learning the Irreducible Representations of Commutative Lie Groups

## Contribution

The paper gives a definition of "disentangling" borrowed from physics and a tractable probabilistic model that realises it for one class of group. The definition (§2.1): a symmetry group G acts linearly on data space; changing basis to expose invariant subspaces whose complements are also invariant splits x into parts that "remain distinct under symmetry transformations"; recursing to irreducibility gives the elementary components, and "Weyl's principle states that the elementary components of a system are the irreducible representations of the symmetry group of the system" (p. 3, credited to Kanatani 1990). The model, Toroidal Subgroup Analysis (TSA), takes G to be a toroidal (compact commutative) subgroup of SO(D), writes ρ_φ = W R(φ) Wᵀ with W orthogonal and R block-diagonal in 2 × 2 rotations (eqs 2–3), and learns W from correspondence pairs with a von Mises prior over angles that turns out to be conjugate (eqs 11–12). It derives an exact orbit ("manifold") distance for the maximal torus (eq. 13), identifies the invariant posterior precision κ̂_j = ‖W_jᵀx‖²/σ² with square pooling, shows the DFT is the special case W = sinusoids (§3.2), and extends to one-parameter subgroups with integer weights via a generalized von Mises prior whose update pools over equal-weight subspaces (eqs 15–16).

## Key insight

For a commutative compact group acting orthogonally, the irreducible real pieces are 2-D planes on which the group acts by rotation at an integer frequency ω_j (the "weight"). Everything the model needs then happens plane by plane: the likelihood of a pair (x, y) factorises over the planes, the posterior over each angle is von Mises with the angle between the projections u_j = W_jᵀx and v_j = W_jᵀy as its mean and ‖u_j‖‖v_j‖/σ² as its precision (eq. 12), and the norm ‖u_j‖, or the norm of a sum over planes sharing a weight, is invariant. Planes with the same weight are "of the same kind" (p. 4): they are equivalent irreps, and their span (the "weight space", p. 7) is what representation theory calls an isotypic component. Invariant features are therefore norms of isotypic projections, which the paper reads as the probabilistic origin of square- and sum-pooling in CNNs.

## Assumptions

- **Linear, orthogonal action.** The group acts on data space R^D by orthogonal matrices, ρ_g ∈ SO(D) (§2.2). Contrast scaling and other non-norm-preserving changes are excluded explicitly (p. 3).
- **Compact commutative group, fixed in advance.** "we will from here on consider only compact commutative subgroups of the special orthogonal group SO(D)" (§2.2). Either a maximal torus T^J, J = D/2, with all angles free (eq. 2), or a one-parameter subgroup ρ_s = W diag(R(ω_1 s), …, R(ω_J s)) Wᵀ with integer ω_j so that the subgroup is compact (eqs 5, 15; Fig. 1). D even is assumed "for ease of exposition" (fn. 3).
- **Complete reducibility.** Assumed by working with an orthogonal action; fn. 2 notes "The picture becomes a lot more complicated … when the group does not act linearly or is not completely reducible."
- **Supervision by correspondence.** Training data are pairs (x, y) with y = ρ_φ x + ε for an unobserved φ, isotropic Gaussian noise ε ~ N(0, σ²) (eq. 6).
- **Priors.** The angles φ_j are marginally independent von Mises (eq. 7); for the coupled model, a generalized von Mises over s (p. 6).
- **Weights from a known transformation.** ω_j = θ_j/δ, estimated from patches rotated by a known δ = 0.1° (§3.4).

## Key results

- **Reduction (eq. 1).** ρ_g = W diag(ρ¹_g, ρ²_g) W⁻¹ for all g exposes invariant subspaces V, V^⊥; recursion ends at irreducibles (§2.1).
- **Maximal torus parametrisation (eqs 2–4).** ρ_φ = W R(φ) Wᵀ, R(φ) = exp(Σ_j φ_j A_j); any subspace of the (abelian) Lie algebra is a subalgebra, so an I-parameter torus is learned as a maximal torus plus an I-dimensional subspace of φ-space (p. 4).
- **Compactness forces integer weights (eq. 5, Fig. 1).** R(s) = diag(R(ω_1 s), R(ω_2 s)) is periodic only when the ω_j are commensurate; the paper restricts to integers so that R(s) = R(s + 2π).
- **Conjugacy (eqs 11–12).** The posterior over φ is a product of von Mises with natural parameters η̂_j = η_j + (‖u_j‖‖v_j‖/σ²)[cos θ_j, sin θ_j]ᵀ, θ_j the angle between u_j and v_j. With a uniform prior the posterior mean is exactly θ_j. The authors say "To our knowledge, this conjugacy relation has not been described before" (p. 5).
- **Exact manifold distance (eq. 13).** d²(x, y) = min_φ ‖y − W R(φ) Wᵀ x‖² = Σ_j ‖v_j − R(μ̂_j) u_j‖².
- **Invariant representation (§3.1).** The posterior of x mapped to itself has μ̂ = 0 and κ̂_j = ‖W_jᵀ x‖²σ⁻², invariant under the torus; the Hellinger distance between √κ̂(x) and √κ̂(y) equals the manifold distance up to 1/(2σ²).
- **DFT as a special case (§3.2, eq. 14).** With sinusoid filters, u_j = (Re X_j, Im X_j); the posterior precision is |X_j| and the mean is arg X_j.
- **Coupled model (eqs 15–17).** The generalized von Mises is conjugate; the update η̂⁺_j = η⁺_j + Σ_{k: ω_k = j} η̂_k pools over the weight space of weight j (eq. 16). Its normaliser is expressed with multi-variable generalized Bessel functions (eq. 17), with a new algorithm in the supplement (not read). With distinct ω_k there are J invariants κ⁺_j plus J − 1 phase-difference invariants ω_jθ_k − ω_kθ_j, which the authors call unstable for low-energy subspaces; "Finding a stable maximal invariant … is an interesting problem for future work" (p. 7).
- **Marginal likelihood (eq. 18).** Closed form, p(y|x) ∝ exp(−(‖x‖² + ‖y‖²)/2σ²) Π_j I_0(κ̂_j)/I_0(κ_j); trained by minibatch SGD with W re-orthogonalised after each step (W := UVᵀ from the SVD) (§3.4).
- **Experiment (§4, Fig. 3).** 100 filters (so 50 planes, undercomplete in D = 256) trained on 250,000 pairs of 16×16 standard-normal patches and their random rotations; minibatch 100; learning rate 0.25/√T. Filters are "very clean"; learned ω_j range from −11 to 12, with "a few filters on row 1 and 2 that are assigned weight 0 when in fact they have a higher frequency".
- **Classification (Fig. 4).** Rotated MNIST, 16×16, 60k/10k, 1-NN: ED < TD < √κ̂ ≈ MD, with MD "about as accurate as ED" on unrotated MNIST. No numbers are given in the text.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The elementary components of data with a symmetry group are that group's irreducible representations ("Weyl's principle"), and this is a general definition of disentangling | assertion (a principle, adopted from Kanatani) | §1, §2.1 p. 3; fn. 2 concedes it gets "a lot more complicated" for nonlinear or non-completely-reducible actions |
| C2 | A von Mises prior over a toroidal group's angles is conjugate to the Gaussian transformation likelihood, and the coupled case has a generalized von Mises conjugate prior | proof (derivation) | eqs 11–12, 16; coupled normaliser and gradients deferred to the unread supplement |
| C3 | For the maximal torus the exact orbit distance has a closed form, and equals (up to 1/2σ²) the Hellinger distance between invariant precisions | proof (derivation) | eq. 13 and §3.1 |
| C4 | Square pooling and sum/max pooling over equal-weight subspaces are what a torus-invariant representation requires | derivation plus analogy | §3.1 (κ̂ as square pooling), p. 7 (pooling over weight spaces); the CNN link is by analogy |
| C5 | The DFT is a special case of TSA, which "makes it possible to learn an appropriate generalized transform from data" | proof (special case) | §3.2 |
| C6 | TSA learns clean filters and correct weights for 2D rotation | experiment, one group, synthetic | §4, Fig. 3; noise patches; weights estimated with a known 0.1° rotation; a few weights wrong |
| C7 | The learned invariant representation is "highly effective for classification" | weak (one figure, no numbers, one dataset) | Fig. 4, rotated MNIST 1-NN |
| C8 | The ideas extend to "non-commutative groups acting on non-linear latent representation spaces" | assertion | p. 3, §5; nothing in the paper does this |

## Method

Probabilistic modelling plus maximum marginal likelihood. Fix the group class (maximal torus in SO(D), or a one-parameter subgroup with integer weights); parametrise its representation as W R(φ) Wᵀ; derive the conjugate posterior over group parameters and the closed-form marginal likelihood; fit W by SGD with re-orthogonalisation; estimate the weights ω_j from a batch transformed by a known small rotation; read off invariants (κ̂, or pooled κ⁺) and the orbit distance.

## Concepts

- **Weyl's principle** — the elementary components of a system are the irreps of its symmetry group (p. 3; Kanatani 1990).
- **Reduction / invariant subspace** — a change of basis W making every ρ_g block-diagonal (eq. 1).
- **Toroidal group / maximal torus** — a compact commutative subgroup of SO(D); T^J with all J angles free (§2.2).
- **Weight ω_j** — the integer frequency with which a one-parameter subgroup rotates plane j; equal weights mean equivalent irreps, "of the same kind" (p. 4).
- **Weight space** — the span of the planes sharing a weight (p. 7); in standard terms, an isotypic component of the group.
- **Manifold (orbit) distance** — minimum distance between orbits O_x and O_y (§3.1).
- **Stabilizer** — the subgroup fixing x; its posterior gives the invariant κ̂ (p. 6).
- **Maximal invariant** — an invariant identifying the orbit; κ̂ is one for the maximal torus, and a stable one for the coupled model is left open (p. 7).

## Connections

- **Cohen & Welling 2016 ([LIT-314](../literature.d/LIT-314.md), read in [NOTE-288](NOTE-288.md)).** The later G-CNN paper cites this one as learning irreps from data. This reading refines that description (see corrections): the group class is assumed, the symmetry is supplied through transformation pairs, and the weights are calibrated with a known rotation. The two papers sit on opposite sides of the "learn vs impose" line, but neither detects an unknown group.
- **Kondor & Trivedi ([LIT-305](../literature.d/LIT-305.md), [NOTE-282](NOTE-282.md)).** This paper's "weight spaces" (spans of equal-weight planes, p. 7) are the isotypic components of [NOTE-282](NOTE-282.md)'s Lemma 6, for the abelian case, and its invariant ‖η̂⁺_j‖ is the norm of an isotypic projection. So the isotypic machinery [NOTE-282](NOTE-282.md) finds in Kondor & Trivedi already appears here in 2014, for tori, in a learning setting.
- **Engels et al. ([LIT-322](../literature.d/LIT-322.md), [NOTE-273](NOTE-273.md)).** Each 2-D block R(ω_j s) is the real irrep of SO(2) at frequency ω_j. Engels et al.'s weekday circle (cos 2πα/7, sin 2πα/7) is the same object for Z/7 at frequency 1. This paper is a 2014 method that, given pairs related by a cyclic shift, would learn such planes; Engels et al. found theirs by SAE clustering and inspection, with the group supplied by the task. My connection, not either paper's.
- **O'Donnell ([LIT-346](../literature.d/LIT-346.md), [NOTE-291](NOTE-291.md)) and the abelian-degeneracy statement in [NOTE-282](NOTE-282.md).** [NOTE-282](NOTE-282.md) says "Abelian symmetries … give only one-dimensional irreps and so produce no degeneracy at all". That holds over ℂ and for groups with real characters such as the cube's (ℤ/2)ⁿ ([NOTE-291](NOTE-291.md)), but not over ℝ for this paper's groups. A real symmetric operator commuting with a real 2-D rotation irrep acts on that plane as a scalar (the commutant of R(ωs) is {aI + bJ}, whose symmetric members are aI), so each weight-ω plane with ω ≠ 0 carries a two-fold eigenvalue. I checked this numerically: averaging a random symmetric 8 × 8 matrix over ρ_s with weights (1, 1, 2, 3) gives four eigenvalue pairs, and a random symmetric 7 × 7 circulant (Z/7) gives three pairs and one singleton. The observation is mine, not the paper's; the paper's only remark in this direction is that orthogonal matrices' eigenvalues "come in complex conjugate pairs" (p. 3).
- **[THEORY-017](../theory.d/THEORY-017.md).** The paper is an explicit instance of its thesis: "we are free to change the basis of the measurement space" (p. 2), and the basis W that exposes the irreducible planes is extra structure learned from transformation pairs, i.e. supplied by the group action the data exhibit. Within a weight space the choice of planes is not unique (any rotation mixing equal-weight planes commutes with ρ_s); the paper pools over weight spaces rather than trusting individual planes, which matches [THEORY-017](../theory.d/THEORY-017.md)'s "the basis inside a multiplet is extra data".
- **Geometric Deep Learning ([LIT-319](../literature.d/LIT-319.md), [NOTE-274](NOTE-274.md)).** GDL's derivation of the Fourier basis as the joint eigenbasis of shift operators (§4.2) is the fixed-group version of this paper's §3.2, where the DFT is recovered as the special case W = sinusoids and TSA generalises it to a learned basis.
- **Anthology of the SOTA.** No anthology document holds or cites this paper.

## Bearing on the record

- **What the map needs, and what this paper supplies.** Row 7 claims "they impose symmetry; you *detect* it via spectral degeneracy" and cites only impose-side works (Cohen–Welling 2016; Bronstein et al.). The misattribution it repairs: the map's "Cohen–Welling" is the 2016 G-CNN paper, which imposes a group; this 2014 paper by the same authors is the one that *learns irreps from data*, and the map should cite it on the learn/detect side so the impose/detect contrast is not drawn against an empty field. It supplies prior art for exactly these phrases: "irreps as the elementary components of a representation" (Weyl's principle, p. 3), "learning the irreducible decomposition from data" (§3.4), and "pooling over isotypic components gives invariants" (p. 7).
- **What it does not supply, and so what survives of row 7's novelty claim.**
  - *Input.* Raw pixel vectors (white-noise patches in the experiment), not a trained network's learned representations.
  - *Group known in advance.* The group class (compact commutative subgroup of SO(D), with one parameter in the coupled model) is fixed by the modeller; the data are pairs known to be related by a group element; the weights are calibrated with a known 0.1° rotation. Nothing detects whether a symmetry is present, or which group.
  - *Spectral degeneracy.* None. The paper parametrises the representation directly (W, ω) and never inspects the spectrum of any operator; it rejects eigenvectors as redundant (p. 3).
  - *Abelian only.* The groups are abelian, whose complex irreps are one-dimensional. The non-abelian extension is asserted as possible, not done (C8).
  - **Verdict.** It supplies the learn-irreps-from-data prior art that row 7 must cite, and it narrows the claimable novelty: "learning irreps from data" is not new (2014, and earlier Rao & Ruderman 1999, Miao & Rao 2007, Sohl-Dickstein et al. 2010 per its §1.1). What stays unpre-empted by this paper is detecting a *previously unspecified* symmetry *in a trained network's representation space*, *without transformation pairs*, *from eigenvalue multiplicities*. The map's `NOVEL-NARROW` label for the degeneracy-as-diagnostic survives this paper, but the positioning sentence should credit it.
- **A precision for the owner's test (my own, see Connections).** Over the reals, abelian groups with 2-D real irreps (SO(2), Z/n for n ≥ 3) do force two-fold degeneracies on symmetric commuting operators. So a degeneracy test could see this paper's kind of structure (and Engels et al.'s circles) as pairs, but only as pairs: it cannot tell a weight-1 plane from a weight-2 plane, since both give a doubled eigenvalue. Row 7's "irrep multiplets = spectral degeneracies" should say the irreps in question are real irreps, and that the cube's (ℤ/2)ⁿ (real characters) is the case with no pairing.
- **ML practice.** Nothing current. TSA is a 2014 shallow model; its practice-relevant lesson (invariants as pooled norms over equivalent irreps) is subsumed by later equivariant-network work. Not an anthology candidate on its own.
- **For filing.** `representation-learning` first (disentangling and invariant representations), `mathematics` (Lie groups, reduction of representations), `probabilistic-modeling` (the conjugate-prior Bayesian model).

## Limitations

- **Assumed group class.** Only compact commutative subgroups of SO(D), acting linearly and orthogonally. Contrast, scaling and any non-orthogonal or nonlinear action are excluded (§2.2, fn. 2).
- **Supervised by correspondence.** Pairs known to be related by a group element are required; the paper does not address data with no such pairing.
- **Weight estimation uses a known transformation** (§3.4), which the introduction's description, a representation "learned from pairs of images related by arbitrary and unobserved transformations in the group" (§1, p. 2), does not mention.
- **Thin experiment.** One group (2D rotation), synthetic noise patches, one classification figure without numbers, and "a few" wrongly assigned weights.
- **Coupled-model invariants.** A stable maximal invariant for the one-parameter model is left open (p. 7).
- **§2.1's group is broader than the one used.** "Every equivalence relation on the input space fully determines a symmetry group" is stated for all invertible maps leaving Φ invariant; the theory is then applied only to linear, indeed orthogonal abelian, subgroups. The gap is not discussed.
- **Supplement not read.** The GBF algorithm and the coupled-model derivations are in supplementary material not included in the arXiv PDF.

## Open questions

- Given unpaired activations from a trained network, could TSA's parametrisation (W, integer ω) be fitted by likelihood without correspondence pairs, e.g. to an operator estimated from the network? That would turn it into a detection method and is the nearest bridge between this paper and row 7.
- Does the paper's pooling over weight spaces (isotypic components) have a spectral counterpart a degeneracy test could use: can equal-weight planes be grouped without knowing the group, from the commutant of extracted operators?
- The non-commutative extension the paper promises (§5) became, in later work by the first author, imposed-group architectures ([LIT-314](../literature.d/LIT-314.md)). Whether a non-commutative learn-from-pairs analogue exists is outside this reading (unverified).

## Corrections to the seeded skim

- none (there was no seed or dossier)
- [NOTE-288](NOTE-288.md) reports, from Cohen & Welling 2016's related work, that this paper learns "a group's irreps from data" and describes disentangling as "a reduction of the operators T_g". The second half is accurate (§2.1, eq. 1). The first needs three qualifications from the text. (i) The group is not learned from scratch: it is fixed in advance to be a compact commutative subgroup of SO(D), a maximal torus or a one-parameter subgroup of one (§2.2, eqs 2, 15). What is learned is the representation's basis W and the integer weights ω_j. (ii) The symmetry is supplied by the data: training uses pairs (x, y) that are known to be related by some group element (eq. 6, §4). (iii) The weights ω_j are not inferred from the unlabelled pairs but estimated "from a batch of image patches rotated by a sub-pixel amount δ = 0.1°" (§3.4), i.e. with a known group element.
- The abstract says the model is trained "on pairs of transformed image patches". The body says the patches "were drawn from a standard normal distribution" and y was x rotated by a uniform random angle (§4). The training data are white-noise patches, not natural-image patches.
- The abstract says "the learned invariant representation is highly effective for classification". The evidence is one figure (Fig. 4, 1-NN accuracy against training-set size on rotated MNIST, 16×16) with no numbers in the text; the prose says √κ̂ and the manifold distance beat Euclidean and tangent distance "by a large margin" and that MD is "about as accurate as ED on a much simpler dataset" (non-rotated MNIST). No values can be quoted.
- For the map's row 7 (see Bearing): the paper works on pixel space, not on a trained network's representations, and nothing in it uses eigenvalue multiplicities. It deliberately avoids eigen-decomposition: complex eigenvectors are rejected as redundant "because the eigenvalues and eigenvectors of an orthogonal matrix come in complex conjugate pairs" (p. 3), in favour of real 2 × 2 rotation blocks.
