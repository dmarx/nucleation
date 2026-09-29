---
number: 288
status: Read
formerly:
- NOTE-tmpf1rrb
paper: LIT-314
title: 'Group Equivariant Convolutional Networks'
version: 1
history:
- version: 1
  date: '2026-09-29'
  note: >-
    Read in full (The full text of arXiv 1602.07576 v3 (3 Jun 2016, the ICML
    2016 / PMLR 48 camera-ready), from the arXiv PDF, 12 pp. I read the
    abstract, §§1–10, Appendices A (equivariance derivations), B (gradients)
    and C (G-conv calculus), and the references. Nothing was skipped. The
    text was extracted with PyMuPDF. Figures 1–2 (p4 and p4m feature-map
    diagrams) survive only as labels, and I reconstructed them from the §4.4
    prose.). The first NOTE on this paper, which was seeded from its
    abstract alone.
date: '2026-09-29'
summary: >-
  Group convolution (eqs. 10–11) replaces translation by the elements of a
  discrete group G, so feature maps become functions on G and every layer
  is G-equivariant (eq. 12, with pooling and nonlinearities shown to
  commute with the action). With parameter counts held roughly fixed,
  p4-CNNs cut rotated-MNIST test error from 5.03% (planar baseline) to
  2.28% (previous best 3.98%), and p4m convolutions cut plain-CIFAR10
  error from 9.45% to 6.46% on a ResNet44 (Tables 1–2).
---

# NOTE-288: Group Equivariant Convolutional Networks

## Contribution

It generalises the convolution layer from the translation group ℤ² to discrete groups that contain translations: p4 (translations and 90° rotations) and p4m (adding mirror reflections). It shows that the full layer stack stays equivariant to the chosen group. The layers covered are G-correlation, pointwise nonlinearities, subgroup and coset pooling, batch norm with one scale per G-feature map, and residual sums. It gives a GPU-friendly implementation (filter transformation by index lookup, then planar convolution) and shows that swapping planar convolutions for p4 or p4m convolutions, at a roughly fixed parameter count, lowers test error on rotated MNIST and CIFAR10.

## Key insight

Equivariance is structure preservation between "G-spaces" (§2, eq. 1). If the first layer correlates the image with g-transformed filters (eq. 10), its output is a function on G. Later layers correlate functions on G with filters on G (eq. 11). Each layer then commutes with the left action L_u by the change of variables h → uh (eq. 12), the group analogue of the translation proof (eq. 8). Weight sharing is extended from positions to poses.

## Assumptions

- **The group.** G is a discrete group of plane symmetries acting on ℤ², fixed in advance: p4 or p4m (§4.2–4.3). The implementation needs G to be *split*, g = ts with t a translation and s in the stabiliser of the origin (§7). A footnote says a convolution can be defined "at least, on any locally compact group", but continuous groups are left as a limitation (§9).
- **Signals.** Feature maps are finitely supported functions f: ℤ² → ℝ^K or G → ℝ^K, and edge effects are ignored (§4.4).
- **The action.** The action on functions is [L_g f](x) = f(g⁻¹x) (eq. 4), a homomorphism, L_g L_h = L_gh (eq. 5).
- **Where exact equivariance holds.** It requires one bias and one batch-norm scale per G-feature map (§6.1), and pooling regions that are subgroups (cosets) for full G-equivariance (§6.3).

## Key results

- **Eq. 9 and App. A.** Planar correlation is not rotation-equivariant: [L_r f] ⋆ ψ = L_r[f ⋆ L_{r⁻¹}ψ].
- **Eq. 12.** G-correlation is G-equivariant: [L_u f] ⋆ ψ = L_u[f ⋆ ψ].
- **Eq. 13.** f ⋆ ψ = (ψ ⋆ f)*, with the involution f*(g) = f(g⁻¹).
- **Eq. 15.** Pointwise nonlinearities commute with L_h.
- **Eq. 17 and eq. 20.** Max-pooling over gU commutes with L_h.
- **§6.3, coset pooling.** Pooling over the cosets gH gives an H-invariant map, i.e. a function on G/H.
- **Rotated MNIST (Table 1).** Z2CNN 5.03%; P4CNNRotationPooling 3.21%; P4CNN 2.28%, against the previous best of 3.98% (Schmidt & Roth 2012). Pooling over rotations in the intermediate layers ("premature invariance") is worse than keeping the rotation axis until the last layer (§8.1).
- **CIFAR10 (Table 2), test error.**

  | Architecture | Group | CIFAR10 | CIFAR10+ |
  |---|---|---|---|
  | All-CNN | Z2 | 9.44 | 8.86 |
  | All-CNN | p4 | 8.84 | 7.67 |
  | All-CNN | p4m | 7.59 | 7.04 |
  | ResNet44 | Z2 | 9.45 | 5.61 |
  | ResNet44 | p4m | 6.46 | 4.94 |

  The parameter counts are roughly matched (1.37M/1.37M/1.22M; 2.64M/2.62M). A wide ResNet26 reaches 5.27% (planar) against 4.19% (p4m) on CIFAR10+ (§8.2).
- **§9, discussion.** CIFAR is "not actually symmetric" (objects upright), yet G-convolutions help, so "there need not be a full symmetry for G-convolutions to be beneficial".
- **App. C.** The backward pass is again a G-correlation, ∂L/∂f^{l−1} = ∂L/∂f^l ⋆ ψ^{l*} (eq. 21) and ∂L/∂ψ = ∂L/∂f^l ∗ f^{l−1} (eq. 24).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | G-correlation layers, pointwise nonlinearities and coset pooling are equivariant to the chosen discrete group | strong (proof) | eqs. 12, 15, 17; App. A; elementary change of variables |
| C2 | Replacing planar with p4 convolutions nearly halves rotated-MNIST error at matched parameters (5.03 → 2.28%; prior best 3.98%) | moderate (experiment) | Table 1; one architecture family, model selection on the validation set, seed std reported |
| C3 | Keeping the rotation axis until the last layer beats pooling over rotations early | moderate (experiment) | Table 1, 3.21% vs 2.28%; one dataset |
| C4 | p4m convolutions "consistently" improve CIFAR10 results as a drop-in replacement without further tuning | moderate (experiment) | Table 2, two baselines, single runs, no variance |
| C5 | G-CNNs achieve state of the art on CIFAR10 | weak as stated | holds only for plain CIFAR10 and is hedged in §8.2; on CIFAR10+ the result is "comparable" to the prior 4.17% |
| C6 | G-convolutions increase expressive capacity without increasing parameters | weak (assertion) | only error rates at matched parameter counts; capacity is not measured |
| C7 | The overhead is negligible for discrete split groups | informal argument | §7 cost argument; no timings |
| C8 | Useful even when the data are not fully symmetric | weak (one observation) | §9, CIFAR upright objects |

## Method

- **Group parameterisation.** Parameterise p4 and p4m elements as integer tuples mapped to 3×3 homogeneous matrices (§4.2–4.3).
- **Filter bank.** Build the transformed filter bank F⁺ by a precomputed index permutation (§7.1).
- **Convolution.** Reshape F⁺ and call a standard planar convolution (§7.2).
- **Experiments.** Compare against planar baselines at approximately equal parameter counts, dividing filters by √4 = 2 (p4) or ≈ √8 ≈ 3 (p4m).

## Concepts

- **G-space.** A representation space with a group action; the map between layers must be equivariant, Φ(T_g x) = T′_g Φ(x) (eq. 1), with T a linear representation.
- **G-correlation.** [f ⋆ ψ](g) = Σ_h Σ_k f_k(h) ψ_k(g⁻¹h) (eq. 11); the output is a function on G.
- **Coset pooling.** Pooling over gH; the result is a function on G/H.
- **Split group.** Every element factors as a translation times a stabiliser element (§7).
- **Premature invariance.** Invariance imposed in intermediate layers, which is worse than equivariance carried to the top (§2, §8.1).

## Connections

- **Kondor & Trivedi ([LIT-305](../literature.d/LIT-305.md)).** They prove the converse direction for compact groups acting transitively on the index sets: equivariance of such a feed-forward network forces generalised convolution. This paper proves only sufficiency, for discrete split plane groups. [LIT-305](../literature.d/LIT-305.md) cites this paper as the source of the term "equivariance" in this setting.
- **Bronstein et al. ([LIT-319](../literature.d/LIT-319.md)).** GDL (§5.2) presents this paper's "transform + convolve" implementation as the discrete group-convolution recipe. Its §5.5 classes this approach as the "regular representation" route and contrasts it with the irreducible-representation route this paper does not take.
- **Symmetry detection in its own references.** Three cited works are about finding symmetry in data or in trained networks rather than imposing it. The paper's own descriptions (§3) are:
  - Lenc & Vedaldi (2015) "show that the AlexNet CNN … trained on imagenet spontaneously learns representations that are equivariant to flips, scaling and rotation".
  - Cohen & Welling (2014), "Learning the Irreducible Representations of Commutative Lie Groups", learn a group's irreps from data, and they describe disentangling as "a reduction of the operators T_g".
  - Cohen & Welling (2015) relate disentangling to decorrelation.

  I have not read these works. Their content is here only as this paper describes it.
- **Anthology.** [ANTH-SOTA-358](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/practices.d/SOTA-358.md) ("Drop the domain inductive bias once pre-training data is large enough, and keep it when it is not") is the practice this paper's experiments bear on. Both of its datasets are small by that practice's standard (12k training images for rotated MNIST, 40k for CIFAR), and its gains are in that regime. [ANTH-THEORY-052](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-052.md) (synthesis requires equivariant representations) and [ANTH-LIT-559](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-559.md) (alias-free GANs) are neighbours on equivariance.

## Bearing on the record

- **What the map's row 7 cites it for.** It is cited as the geometric-DL/equivariance programme that *imposes* symmetry, against which the owner positions spectral-degeneracy *detection*. The characterisation holds for this paper:
  - G is chosen before training (p4, p4m) and built into the weight sharing.
  - Nothing is learned about which symmetry the data have.
  - Its one gesture at "partial" symmetry (§9, CIFAR) is an observation that imposing a symmetry the data lack can still help, not a way of finding one.
- **What it does not own.** It owns none of the machinery row 7 attaches to it:
  - It has no irreducible representations, characters, isotypic decomposition or spectral analysis. It works entirely with the regular representation (functions on G).
  - The "predicate harmonics = characters" and "irrep multiplets = spectral degeneracies" halves of row 7 get nothing from it.
  - Cite it for the impose-symmetry side only.
- **The "they impose, you detect" contrast is not an empty niche.** This paper's own related work (§3) names prior detect-or-learn-symmetry work (see Connections).
  - *Lenc & Vedaldi (2015).* They measure equivariance that a trained CNN acquired without being built for it, which is the closest in spirit to the owner's detection test.
  - *Cohen & Welling (2014).* They learn irreducible representations of commutative Lie groups from data.
  - *Their significance for the map.* Both should be on the map's §5 "scooped again?" watch (item 3), and the positioning sentence should say what is different. The sharper difference, supported by [LIT-319](../literature.d/LIT-319.md) (see pam-[LIT-319](../literature.d/LIT-319.md)), is *where the group acts*. G-CNN symmetry acts on the input domain (pixel grid, sphere), while the owner's G acts on the representation space V and commutes with extracted concept operators.
- **Connections to nucleation entries.**
  - *[THEORY-017](../theory.d/THEORY-017.md).* Only unitarily invariant structure is intrinsic. This paper's T_g are permutation-type operators supplied from outside: the group, its action on ℤ² and the resulting feature-map transformation law are all stipulated. That fits [THEORY-017](../theory.d/THEORY-017.md)'s "extra data supplied from outside the space".
  - *No other connection is warranted.* In particular there is none to the Peter–Weyl or Pontryagin entries ([LIT-329](../literature.d/LIT-329.md), [LIT-333](../literature.d/LIT-333.md)), because the paper does no harmonic analysis.
- **ML practice.** Yes, it carries some: a controlled comparison that group convolution at matched parameters helps on small rotated or mirrored image data. That is [ANTH-SOTA-358](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/practices.d/SOTA-358.md)'s territory. If the anthology files it, it should be as evidence for the small-data arm of that practice, with the CIFAR "state of the art" read as plain-CIFAR only.

## Limitations

- **Scope.** Discrete, split plane groups only (p4, p4m). The authors name continuous groups and large groups (where enumeration is infeasible) as open (§9).
- **Evidence.** Small benchmarks, single CIFAR runs, and no ablation separating equivariance from the changed width and channel structure that parameter matching induces. "Expressive capacity" and "negligible overhead" are not measured.
- **The CIFAR headline.** The abstract's CIFAR claim is stronger than §8.2's own hedge.
- **Exact equivariance.** It holds only up to edge effects and only for rotations that are symmetries of the sampling grid (90°).

## Open questions

- **Whether learned symmetry is actually used.** When a planar CNN learns rotated filter copies (the paper notes that then "the stack of feature maps is equivariant, although individual feature maps are not", §5), is the learned group structure detectable from the trained filters' spectrum? That is the detection question the owner's row 7 asks, posed on the paper's own object (unverified whether Lenc & Vedaldi or later work answers it this way).
- **Partial symmetry.** How much of the CIFAR gain comes from the imposed symmetry, and how much from the changed channel geometry at matched parameters?

## Corrections to the seeded skim

- Seeded from metadata and the abstract. The text agrees with the seed's summary, with two precisions. Venue verified: the PDF reads "Proceedings of the 33rd International Conference on Machine Learning, New York, NY, USA, 2016. JMLR: W&CP volume 48". Authors verified as Taco S. Cohen and Max Welling (University of Amsterdam; Welling also UC Irvine and CIFAR).
- "State-of-the-art results on CIFAR10" (abstract, §10) is narrower in the body. §8.2 claims to beat "all published results on plain CIFAR10" (6.46%, p4m-ResNet44) and immediately hedges: "due to radical differences in model sizes and architectures, it is difficult to infer much about the intrinsic merit of the various techniques". On augmented CIFAR10+ the best result, 4.19% with a wide p4m-ResNet26, is called "comparable to the 4.17%" of Zagoruyko & Komodakis, with fewer parameters (7.2M vs 36.5M). It is not better.
- "Increases the expressive capacity … without increasing the number of parameters" (abstract, §10) is asserted, not measured. The experiments match parameter counts by dividing filter counts by √|H| (§8.1–8.2) and report test error only. "Negligible computational overhead" (abstract) is argued from the algorithm in §7 ("roughly equal" cost), and no timings are reported.
- The CIFAR table (Table 2) reports single numbers with no seed variation. Table 1 (rotated MNIST) reports standard deviations "under variation of the random seed" printed as ±0.0020, ±0.0012 and ±0.0004 next to percentage errors. The units are unclear, and they are presumably fractions, not percentage points (unverified).
- For the prior-art map (row 7): the paper uses the **regular representation only**. Feature maps are functions on G, and G acts by permuting and transforming them (§4.4, eq. 4). The words "irreducible", "character" and "Fourier" do not occur in the body. It is correctly cited as an exemplar of *imposed* symmetry, but not as an owner of the character or irrep machinery that row 7 is about.
