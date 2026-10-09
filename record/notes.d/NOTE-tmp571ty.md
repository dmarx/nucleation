---
status: Read
paper: 'LIT-tmpacvdl'
title: 'Topological Invariance and Breakdown in Learning'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from the arXiv PDF of v1 (3 October 2025, 22 pages),
    text extracted with pdftotext and kept as paper.txt beside the PDF in
    the reader's scratch directory. Sections 1–7 and Appendices A–D read;
    every proof (Lemmas 1–5, Theorems 1–2, Propositions 1–3) followed
    line by line. Figures 3, 5, 11 and 12 looked at on rendered pages;
    the others (Figures 1, 2, 4, 6–10) read from captions and text. The
    cited works were not read, including Ziyin (2024) on symmetry-induced
    constraints and Zhou et al. (2025), LIT-370.
date: '2026-10-09'
summary: >-
  Proves that a permutation-equivariant update with a K-Lipschitz update
  map changes the distance between any two neurons in one step by a factor
  in [1 − ηK, 1 + ηK], so coincident neurons never split, and for ηK < 1
  the induced map on the set of neuron vectors is a bi-Lipschitz
  homeomorphism (a C¹ diffeomorphism under smoothness), and so no two
  neurons merge in finitely many steps. The proofs hold. The two-phase
  "topological simplification" reading and the Betti-number experiments go
  beyond them. The measured changes are fragmentation, not merging, at
  ηλ_max far below 1.
---

<!-- inactive-ok-file: THEORY-tmpmh1ao — Proposed; the THEORY this reading produced -->
<!-- inactive-ok-file: THEORY-039 — Proposed; the record's account of later training phases, which this reading bears on -->
<!-- inactive-ok-file: LIT-370 — Proposed; the two-phase paper this one cites, named for the lineage -->
<!-- inactive-ok-file: THEORY-112 — Proposed; the record's account of permutation symmetry in the loss landscape, named as a neighbour -->
<!-- inactive-ok-file: THEORY-181 — Proposed; named because the paper links its second phase to grokking -->
<!-- inactive-ok-file: THEORY-180 THEORY-182 — Proposed; named as the 2026-10-09 batch's accounts, on which this reading was checked for bearing -->

# NOTE-tmp571ty: Topological Invariance and Breakdown in Learning

## Contribution

The paper takes the permutation symmetry of hidden units, a fact usually
used to describe loss landscapes, and turns it into a constraint on training
trajectories. Any update rule that commutes with permuting neurons gives
coincident neurons identical updates. If the update map is also K-Lipschitz,
one step changes the distance between any two neurons by at most a factor of
1 ± ηK. The paper names η* = 1/K the "topological critical point": below
it, the step maps the set of neuron vectors homeomorphically onto the next
set. Above it, only a continuous surjection is guaranteed. The framework is
abstract (any index set, any time-dependent equivariant rule), and the paper
checks its conditions for gradient descent and Adam.

## Key insight

Permuting two neurons is a symmetry of the update, so the difference of
their updates is the update's response to the swap. The swap moves the
weights by √2 times the distance between the two neurons. A Lipschitz bound
on the whole update therefore bounds the relative motion of every pair. It
is the familiar fact that X ↦ X + ηU(X) is injective, indeed bi-Lipschitz,
when ηK < 1, restricted to the neurons by equivariance. In my reading, not
the paper's: if neurons i and j coincided after a step from X, then the
step from the swapped state PX would give the same result, and injectivity
would force PX = X.

## Assumptions

- **Neurons are the units the update treats symmetrically.** A collection
  X = {xᵢ}, i ∈ I, of vectors in ℝᴰ updated by xᵢ′ = xᵢ + ηUᵢ(X). I may be
  infinite; permutations are finitary.
- **(P1) Equivariance:** PU(X) = U(PX) for every finitary permutation P.
  For gradient descent this follows from L(PX) = L(X) (Proposition 1, via
  P∇L(X) = ∇L(PX)). For Adam, each neuron carries its moment estimates
  (θᵢ, mᵢ, vᵢ), and equivariance holds (Proposition 3). Parameters outside
  the symmetric units are absorbed into a time-dependent rule.
- **(P2-K) Continuity:** ‖U(X) − U(Y)‖ ≤ K‖X − Y‖ for all X, Y differing
  in finitely many entries, uniformly in time. For gradient descent K is the
  gradient's Lipschitz constant (Proposition 2), i.e. a global bound on the
  Hessian norm. Appendix D weakens it to a per-entry bound with K/2.
- **(P3) Smoothness:** the response of each Uᵢ to moving one other neuron is
  C¹. It is needed only for the diffeomorphism claim.
- **Narrower than the title.** A global K does not exist for a sigmoid
  two-layer network with unbounded weights, which is the paper's own
  experimental model. The paper treats K as the local top Hessian eigenvalue,
  but proves nothing in that form. No K is derived for Adam. Its update
  components for mᵢ and vᵢ carry factors (1 − β)/η, so K would depend on η
  and on 1/√vᵢ, not just on the Hessian.

## Key results

- **Lemma 1.** Under P1, xᵢ = xⱼ at step t implies xᵢ = xⱼ at t + 1, for
  any η.
- **Lemma 4 / Lemma 2.** Under P1 and P2-K, ‖Uᵢ(X) − Uⱼ(X)‖ ≤ K‖xᵢ − xⱼ‖,
  hence (1 − ηK)‖xᵢ − xⱼ‖ ≤ ‖xᵢ′ − xⱼ′‖ ≤ (1 + ηK)‖xᵢ − xⱼ‖.
- **Lemma 3.** The induced map Û: S(t) → S(t+1) on the set of neuron
  vectors is well defined and surjective; for ηK < 1 it is a bijection.
- **Theorem 1.** (i) Û is a continuous surjection, (1 + ηK)-Lipschitz.
  (ii) If S(t) is compact, so is S(t+1), and Û is a quotient map. (iii) If
  ηK < 1, Û is a homeomorphism, with inverse 1/(1 − ηK)-Lipschitz. (iv) If
  ηK < 1, P3 holds and S(t) is open in ℝᴰ, then S(t+1) is open (invariance
  of domain) and Û is a C¹ diffeomorphism. The Jacobian's singular values lie
  in [1 − ηK, 1 + ηK].
- **Theorem 2.** For ηK < 1, Û is measure-preserving both ways between the
  push-forwards µ(t), µ(t+1) of a measure on I. The forward identity
  µ(t+1)(A) = µ(t)(Û⁻¹(A)) holds for any well-defined Û. The bound is needed
  only to make Û invertible.
- **Remark (§5.1).** For an L-smooth loss, 1/K minimises the descent-lemma
  bound L(x) + (Kη²/2 − η)‖∇L‖², half the stability limit 2/K.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Under an equivariant update, coincident neurons stay coincident at any step size | strong (proof) | Lemma 1 |
| C2 | Under P1 and P2-K each step changes every pairwise neuron distance by a factor in [1 − ηK, 1 + ηK] | strong (proof) | Lemmas 4 and 2 |
| C3 | For ηK < 1 the map on the neuron set is a homeomorphism, and a C¹ diffeomorphism under P3 with S open | strong (proof), within its hypotheses | Theorem 1 |
| C4 | GD, SGD and Adam satisfy the conditions | equivariance proved for GD and Adam; continuity only for GD, under a global K | Propositions 1–3 |
| C5 | Above η* training "allows topological simplification", making the neuron set coarser and reducing expressivity | weak: permitted by (ii), not shown to occur | §4.1 discussion |
| C6 | Training splits into a topology-preserving phase and, at the edge of stability, a simplifying phase | weak: an interpretation joining Lemma 2 to Cohen et al.'s observation | §4.1, Fig. 1 |
| C7 | Experiments confirm the topological critical point | weak; see Limitations | §6, Figs. 3–5, 11–12 |
| C8 | Diffeomorphic evolution "lends support to" mean-field and NTK theories at small learning rates and explains their breakdown at large ones | weak: no derivation | §4.1 |

## Concepts

- **neuron**: any subset of parameters the learning rule treats
  permutation-equivariantly. For a fully connected layer trained by GD,
  the incoming and outgoing weights of one unit.
- **neuron set S(t)**: {xᵢ(t) : i ∈ I} ⊂ ℝᴰ with the subspace topology.
  Multiplicity is forgotten; the push-forward measure µ(t) keeps it.
- **topological critical point**: η* = 1/K, where the lower bound of Lemma 2
  becomes vacuous.
- **K-continuity**: a uniform Lipschitz bound on the whole update map.

## Connections

The equivariance argument continues Ziyin's work on symmetry-induced
structure (2024), where mirror and permutation symmetries create invariant
subspaces that training cannot leave. Lemma 1 is the permutation case of
that. The "merging = moving to the symmetric state, losing parameters"
reading cites Ziyin, Xu and Chuang (2025). The phase picture leans on
Cohen et al.'s edge of stability ([ANTH-LIT-461](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-461.md)) and on Zhou et al.'s
two-phase learning dynamics ([LIT-370](../literature.d/LIT-370.md), with Yongyi Yang a co-author of both).
It sets its small-step regime against NTK ([ANTH-LIT-360](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-360.md)) and mean-field
theory, and connects to the catapult mechanism and to work showing large
step sizes produce simpler or lower-rank solutions (Galanti and Poggio;
Chen et al.'s stochastic collapse). The topological-data-analysis side is
Naitzat, Zhitnikov and Lim and the GUDHI Rips complex.

## Bearing on the record

- **No account like this in the record.** Nothing in theory.d states a
  constraint on trajectories from permutation symmetry. The reading
  produces [THEORY-tmpmh1ao](../theory.d/THEORY-tmpmh1ao.md), stating C1–C3 at their true scope: no merging
  in finite time below 1/K and no splitting ever. It also states the local
  form the proof supports, which is my observation and not the paper's: two
  neurons can coincide after a step only if η times the update's Lipschitz
  ratio across their swap is at least 1. For GD that ratio is the averaged
  Hessian acting on the antisymmetric direction (eᵢ − eⱼ) ⊗ (xᵢ − xⱼ),
  which can be far below λ_max.
- **[THEORY-039](../theory.d/THEORY-039.md)** (later training phases differ in kind). The paper offers
  one more two-phase picture: smooth optimization under a topological
  constraint, then simplification once the edge of stability pushes ηK
  past 1. It is defined by yet another quantity, Betti numbers of the
  neuron cloud. Its own measured "later phase" is fragmentation, not the
  merging the theory names. It is the kind of evidence [THEORY-039](../theory.d/THEORY-039.md)'s
  promote_when says cannot settle it, and the THEORY does not change. Its
  bearing on [THEORY-039](../theory.d/THEORY-039.md)'s row for [LIT-370](../literature.d/LIT-370.md) is that the two papers share an
  author and the same two-phase framing. They do not share a measurement.
- **Loss-landscape line** ([THEORY-112](../theory.d/THEORY-112.md), [LIT-661](../literature.d/LIT-661.md)). Those works remove
  permutation symmetry to compare solutions. This paper uses the symmetry
  to constrain one trajectory. Merging two neurons is the move onto a fixed
  subspace of a transposition, the symmetric state that alignment methods
  treat as a degeneracy.
- **Kernel regime** ([THEORY-086](../theory.d/THEORY-086.md)). The claim that homeomorphic evolution
  "supports" NTK theory is weak. Homeomorphism of the neuron set holds far
  outside the kernel regime, so it neither implies nor is implied by
  lazy training.
- **The 2026-10-09 batch.** [LIT-858](../literature.d/LIT-858.md) and [THEORY-181](../theory.d/THEORY-181.md): the paper links its
  second phase to grokking in one sentence, with no test. [LIT-855](../literature.d/LIT-855.md) and
  [THEORY-182](../theory.d/THEORY-182.md), and [LIT-859](../literature.d/LIT-859.md): incremental, mode-by-mode learning from small
  initialisation is consistent with no merging, and the paper does not
  touch it. [LIT-857](../literature.d/LIT-857.md) and [THEORY-180](../theory.d/THEORY-180.md), and [LIT-856](../literature.d/LIT-856.md): no bearing found.
- **Symmetry without conservation.** The symmetry here yields an invariant
  set (the coincidence subspaces) and a two-sided distance bound, not a
  conserved quantity. It is a worked case of a symmetry of a dynamical
  rule whose consequence is a constraint, not a Noether-type law.
- **ML practice.** The discussion suggests reading learning-rate decay as
  exploring topologies and then stabilising within one. That is a practice
  suggestion, offered without a test, and it belongs to the anthology if
  anywhere. Hence the LIT's `anthology-candidate` flag.

## Limitations

- **Finite networks.** For finite I, S(t) is a finite set, so a
  homeomorphism is any bijection. Theorem 1(iii) then says only that
  distinct neurons stay distinct, and 1(iv) cannot apply, since a finite set
  is not open. The manifold language of the paper (genus, tori,
  diffeomorphisms) applies only to an idealised continuum of neurons.
- **Finite time only.** The lower bound compounds to (1 − ηK)ᵗ, so neurons
  may approach each other arbitrarily closely and coincide in the limit at
  any step size. Asymptotic collapse onto a symmetric state is not excluded
  below 1/K.
- **Scale-dependent invariants are not protected.** Betti numbers of a Rips
  complex at a fixed scale are not topological invariants of a finite set.
  A bi-Lipschitz map with distortion (1 + ηK)ᵗ/(1 − ηK)ᵗ over t steps can
  change them freely. The experiments measure exactly these, at a scale of
  a quarter of the cloud's diameter.
- **The breakdown is not shown.** Above 1/K the theorem removes a guarantee
  and proves nothing further. The coarsening the paper describes (merging,
  quotient maps, lost expressivity) is never shown to occur.
- **The experiments show fragmentation.** In the MNIST runs (Figs. 5 and 11)
  the large-step b₀ rises from 1 to about 6 (GD) and past 50 (Adam), and b₁
  rises too. That is the neuron cloud breaking into pieces at the chosen
  scale. A continuous image of a connected set is connected, so in the
  continuum the theory forbids it. In Fig. 3c, the large-step toy network
  tears the figure eight apart.
- **The threshold is not located.** No experiment measures K for the GD
  runs. The toy GD learning rates for "small" and "large" differ by about
  12% in 3D (8 × 10⁻⁴ against 9 × 10⁻⁴), and Table 1's 3 × 10³ for 2D is
  presumably 3 × 10⁻³ (footnote 6). For Adam (Fig. 12), 1/λ_max lies between
  0.025 and 0.37 and η is 10⁻⁵ or 10⁻³, so ηλ_max stays below 0.05 in both
  runs, while topology changes in both. As labelled, Fig. 12(a) shows
  sharpness falling for the small step size, which contradicts the text's
  explanation (progressive sharpening). The caption says the small-step run
  was trained longer, and only panel (b) runs to 40 epochs, so the panel
  labels may be swapped. Either way λ_max is not Adam's K.
- **Initialisation unspecified.** For the MNIST MLP the neurons are said to
  be "uniformly sampled from the surface of a 3D unit sphere", but neurons
  there have about 794 coordinates (784 in, 10 out). How the sphere is embedded is not said.
- **Self-description.** The discussion calls the work "entirely theoretical"
  and untested at scale. All experiments are two-layer networks.

## Open questions

- Is the local form sharp? Do neurons in real training merge, or come
  within ε of each other, at steps where η times the swap-direction
  curvature exceeds 1, and only then? A run that logs pairwise neuron
  distances alongside that ratio would answer it. Betti numbers would not.
- Above 1/K, is there a positive result: a mechanism by which large steps
  drive neurons to coincide, rather than merely being allowed to?
- In the infinite-width limit, does the diffeomorphic evolution give the
  "most general mean-field theory" the paper anticipates, and how does it
  relate to the existing Wasserstein-gradient-flow formulations?
