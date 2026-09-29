---
status: Skimmed
paper: LIT-319
title: 'Geometric Deep Learning: Grids, Groups, Graphs, Geodesics, and Gauges'
version: 1
history:
- version: 1
  date: '2026-09-29'
  note: >-
    Read in part (arXiv 2104.13478 v2 (stamped 2 May 2021; title page dated
    May 4, 2021), from the arXiv PDF, 160 PDF pages. The body runs to p. 130
    in the book's own numbering, and the bibliography fills pp. 131–156.
    Page numbers below are the book's own. Book-length, so this is a partial
    reading. I read closely: the Preface and Notation, §1 and §2 (pp. 1–8),
    all of §3 "Geometric Priors" (§3.1 symmetries and representations, §3.2
    isomorphisms, §3.3 deformation stability, §3.4 scale separation, §3.5
    the blueprint, pp. 9–30), §4.1 graphs and sets, §4.2 grids and the
    derivation of the Fourier transform, §4.3 groups and homogeneous spaces,
    §4.4 geodesics and manifolds including Fourier analysis on manifolds,
    §4.5 gauges and bundles (pp. 30–61), §5.2 group-equivariant CNNs (pp.
    74–77), §5.5 equivariant message passing (pp. 83–86) and §7 "Historic
    Perspective" pp. 114–120. I read at the level of statements: §4.6
    (meshes, to p. 62), §5.3 (to p. 78) and §5.4 (deep sets, Transformers
    and positional encodings, pp. 80–82). I did not read the rest: §5.1
    CNNs, §5.6–§5.8 (mesh CNNs, RNNs, LSTMs as time-warping), §6
    applications, §7 after p. 120, and the bibliography. I searched all of
    these by keyword (irreducible, character, Peter, Pontryagin, degenera*,
    multiplicit*, isotypic, Schur, discover*, augment*, unknown/known
    symmetr*, approximate, Transformer, Kondor, Lenc) and read every hit in
    context.). The first NOTE on this paper, which was seeded from its
    abstract alone.
date: '2026-09-29'
summary: >-
  The authors cast CNNs, GNNs, Deep Sets, Transformers, spherical, mesh
  and gauge CNNs, and LSTMs as instances of one "blueprint" (p. 29). Each
  is a stack of linear G-equivariant layers, pointwise nonlinearities and
  local pooling, capped by a G-invariant global pooling, with the domain Ω
  and its symmetry group G given in advance (p. 27: "a symmetry group G";
  p. 4: "exploiting the known symmetries"). The two priors are symmetry
  and scale separation. The Fourier transform is derived as the joint
  eigenbasis of shift-commuting (circulant) operators, which requires
  distinct eigenvalues (p. 37). Its group-theoretic generalisation via
  irreducible representations is announced and deferred to "future work"
  (p. 43).
---

# NOTE-tmp2zxrt: Geometric Deep Learning: Grids, Groups, Graphs, Geodesics, and Gauges

## Contribution

The proto-book takes Klein's Erlangen programme, geometry as the study of invariants of a transformation group, as the organising idea for deep-learning architectures (Preface). It argues that learning in high dimensions is cursed without priors (§2: Lipschitz and Sobolev classes need ε^{−d} samples). It names two geometric priors: **symmetry**, with invariance and equivariance under a group acting on the domain, softened to deformation stability, and **scale separation**, with multiscale coarsening and wavelets.

It assembles these into the **Geometric Deep Learning blueprint** (p. 29). The blueprint is then instantiated on the "5G" domains (grids, groups, graphs, geodesics, gauges; §4) and matched to architectures (table p. 30, §5):

- **CNN.** Grid, translation.
- **Spherical CNN.** SO(3).
- **Intrinsic/mesh CNN.** Isometry or SO(2) gauge symmetry.
- **GNN, Deep Sets, Transformer.** Permutation Σ_n.
- **LSTM.** Time warping.

## Key insight

Once the domain Ω and its symmetry group G are fixed, the architecture follows. Linear G-invariants are too poor, because they depend only on the group average (p. 27). Linear G-*equivariants* composed with pointwise nonlinearities are rich, and locality plus coarsening restores stability to deformations. On grids this goes as follows:

- **Circulant = shift-commuting.** Convolution is exactly the class of linear maps commuting with shifts (circulant matrices).
- **The Fourier basis is forced.** It is their joint eigenbasis, forced by the symmetry, provided the shift's eigenvalues are distinct (p. 37).
- **The general pattern.** "Convolution emerges from the first principle of translational symmetry" (p. 37). The same pattern (commuting operators, joint eigenbasis, spectral filtering) is carried to graphs and manifolds through the Laplacian (§4.4).

## Assumptions

- **Supervised setting.** i.i.d. pairs and interpolating models (§2).
- **Signals.** Functions on a domain Ω. The space of signals X(Ω, C) is a Hilbert space (§3, eqs. 1–2).
- **Known symmetry.** The symmetry group G of Ω is known: "Exploiting the known symmetries of a large system" (p. 4). The blueprint takes "domains Ω … G a symmetry group over Ω" as input (p. 29). §3.3 relaxes exactness to stability, ‖f(ρ(τ)x) − f(x)‖ ≤ C c(τ)‖x‖, for τ near G (eq. 4). G is still given; only the tolerance is new.
- **Group action.** The action on signals is (g.x)(u) = x(g⁻¹u) (eq. 3), a linear representation ρ.
- **Group convolution** needs a locally compact G with Haar measure (margin, p. 40), and a homogeneous (transitive) Ω for weight sharing (p. 44).
- **Manifolds.** They are compact, connected and geodesically complete, where needed (§4.4).

## Key results

- **p. 27.** Linear G-invariant functions factor through the group average A x = (1/μ(G)) ∫ g.x dμ(g).
- **p. 29, the blueprint.** f = A ∘ σ_J ∘ B_J ∘ P_{J−1} ∘ … ∘ P₁ ∘ σ₁ ∘ B₁.
- **§4.1.** Linear permutation-equivariant maps on sets are spanned by the identity and the average. On graphs, 15 generators span them (Maron et al.), independently of n (p. 33).
- **§4.2.**
  - *Circulants.* They commute. A matrix is circulant iff it commutes with the shift.
  - *Fourier basis.* The eigenvectors of the shift are the DFT basis, and they diagonalise every circulant. This needs distinct eigenvalues (p. 37 margin).
  - *Convolution theorem.* C(θ)x = Φ(θ̂ ⊙ x̂).
  - *Continuous case.* The translation spectrum is simple, so every translation-equivariant linear operator is a convolution (pp. 39–40, with a margin pointer to Stone's theorem).
- **§4.3.**
  - *Group convolution.* (x ⋆ θ)(g) = ⟨x, ρ(g)θ⟩ is G-equivariant (eq. 14).
  - *Regular representation.* The next layer acts on functions on G.
  - *Two statements without argument.* "Any equivariant linear map … is a generalised convolution" is stated without proof or citation. The irrep-based Fourier transform is deferred to "future work" (p. 43).
- **§4.4.**
  - *Laplacian eigenbasis.* The Laplace–Beltrami eigenbasis is "the smoothest orthogonal basis".
  - *Truncation error.* It is bounded by ‖∇x‖²/λ_{N+1} (Aflalo & Kimmel).
  - *Instability.* Spectral filters in an explicit eigenbasis are unstable under near-isometric deformation (Fig. 12). Filters written as functions of the Laplacian, p̂(Δ), are stable and avoid eigendecomposition (pp. 53–55).
- **§4.5.** Gauge-equivariant convolution with parallel transport, eq. 23, (x ⋆ Θ)(u) = ∫ Θ(u,v) ρ(g_{v→u}) x(v) dv, with Θ commuting with the structure-group representation.
- **§5.5.** Equivariant message passing (Satorras et al. E(n)-GNN). Two routes are named:
  - *Irreducible representations.* Wigner-D blocks, Clebsch–Gordan kernels (Tensor Field Networks, 3D steerable CNNs, SE(3)-Transformer).
  - *Regular representations.* G-CNNs, LieConv, LieTransformer. They are called "more general" and costlier.
- **p. 116.** Minsky & Papert's Group Invariance Theorem for perceptrons is recalled as a motivation for multilayer networks. Wood & Shawe-Taylor (1996) is credited as the first representation-theoretic view of invariant networks, "unfortunately rarely cited".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Convolution is exactly the class of linear shift-equivariant operators, and the Fourier basis diagonalises it | strong (proof sketch; standard) | §4.2 pp. 36–40, discrete and continuous derivations; the distinct-eigenvalue assumption is stated |
| C2 | Most successful architectures instantiate one blueprint parametrised by (Ω, G) | informal argument (systematisation) | §3.5 and §5, architecture by architecture; no theorem |
| C3 | Any equivariant linear map between signal spaces on homogeneous domains is a generalised convolution | assertion here | p. 43, "it is possible to show", uncited (proved in [LIT-305](../literature.d/LIT-305.md) under its hypotheses) |
| C4 | Symmetry and scale-separation priors are what defeat the curse of dimensionality | informal argument | §2–§3; statistical learning results deferred ("we will review some of these in future work", p. 5) |
| C5 | Explicit Laplacian-eigenbasis spectral filters are unstable under near-isometric deformation, while functions of the Laplacian are stable | moderate (cited results, Fig. 12) | pp. 54–55; Levie et al., Gama et al. |
| C6 | Data augmentation is "provably sub-optimal in terms of sample complexity" relative to architectures with richer invariance groups | cited | p. 74, Mei et al. (2021); not argued in the text |
| C7 | Transformers are attentional GNNs on the complete graph, and their positional encodings are DFT/Laplacian eigenvectors of an assumed ring | informal argument | §5.4 p. 82 |
| C8 | Fourier transforms generalise to groups via matrix elements of irreps | assertion (deferred) | p. 43, "we will discuss this in future work" |

## Method

This is a survey and systematisation. Each architecture is re-derived from the (Ω, G) pair plus locality and coarsening, with worked derivations for grids (§4.2) and manifolds (§4.4) and citations elsewhere.

## Concepts

- **Geometric priors.** Symmetry, deformation (geometric) stability, and scale separation.
- **Blueprint building blocks.** A linear G-equivariant layer B, a pointwise nonlinearity σ, local pooling P, and a G-invariant global pooling A.
- **Isomorphism vs automorphism.** An isomorphism is an equivalence between two different objects; an automorphism is a symmetry of one object (§3.2).
- **Fixed vs varying domain.** Images live on a fixed domain; with graphs and meshes, the domain is part of the input.
- **Homogeneous space.** Every point can be moved to any other (p. 44).
- **Gauge.** A frame for a fibre; a gauge transformation is a map Ω → G, the structure group.
- **Regular vs irreducible representation approaches.** These are the two routes to equivariant layers (§5.5).

## Connections

- **Cohen & Welling ([LIT-314](../literature.d/LIT-314.md)).** Their G-CNN is the book's discrete group-convolution example (§5.2, "transform + convolve", pp. 75–77) and the pioneer of the regular-representation route (p. 85 margin).
- **Kondor & Trivedi ([LIT-305](../literature.d/LIT-305.md)).** They supply the proof of the uncited p. 43 statement and the isotypic and Schur machinery that GDL defers.
- **Walsh, Pontryagin, Peter–Weyl ([LIT-300](../literature.d/LIT-300.md), [LIT-333](../literature.d/LIT-333.md), [LIT-329](../literature.d/LIT-329.md)).** GDL's derivation of the DFT as the joint eigenbasis of an abelian group's shift operators (§4.2) is the finite-cyclic case of Pontryagin duality. The deferred irrep Fourier transform is the Peter–Weyl case. GDL names neither.
- **Belfiore & Bennequin ([ANTH-LIT-698](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-698.md)).** "Topos and Stacks of Deep Neural Networks" treats the same layer invariances as stacks over a topos. It is the anthology's other structural account of architectural symmetry, and a neighbour for the owner's topos row (row 8).
- **Anthology.** [ANTH-SOTA-358](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/practices.d/SOTA-358.md) (drop the domain inductive bias once data are large) is the practice-level counterweight to GDL's programme. GDL's own claim C6 (augmentation is sample-inefficient) is cited, not shown. [ANTH-THEORY-102](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-102.md) (a causal mask encodes absolute position) is relevant to GDL's reading of Transformers as symmetric up to positional encodings.

## Bearing on the record

- **What the map's row 7 cites it for.** It is cited as the geometric-DL/equivariance programme that *imposes* symmetry, against which the owner positions detection by spectral degeneracy. On the parts read, that characterisation is **accurate**:
  - *G is always given.* "Known symmetries" (p. 4); the blueprint takes G as input (p. 29); §3.3 softens exactness around a *given* G. Nothing in the parts read, and no keyword hit elsewhere, addresses discovering an unknown symmetry from data or from a trained network.
  - *Nearest approaches.* The closest GDL comes is "latent graph inference" (§5.4, learning an unknown adjacency). That is learning a domain structure, not a symmetry group.
- **GDL owns no character or degeneracy machinery.**
  - *Irreps and characters.* Irreps are deferred (p. 43) or surveyed (p. 85), and characters are absent.
  - *Degeneracy treated as an obstacle.* Where degeneracy appears, it is assumed away so that the Fourier basis is well defined (p. 37), or treated as the source of eigenbasis instability (p. 54).
  - *Consequence for the map.* The degeneracy-as-diagnostic idea is not in GDL. GDL is a must-cite for positioning, not for machinery. Row 7's machinery citations should be Kondor & Trivedi (isotypic decomposition, Schur) and O'Donnell (Boolean-cube characters). A standard representation-theory text should be added for characters and the Schur degeneracy corollary.
- **GDL sharpens the positioning in a way the map does not yet say.**
  - *GDL's group acts on the domain Ω of the input signal.* The pixel grid, the sphere, the node set, the sequence positions.
  - *The owner's group acts on the representation space V.* It commutes with concept operators extracted from a trained model.
  - *For LLMs, GDL's only symmetry is token permutation Σ_n.* It is explicitly broken by positional encodings (p. 82), and nothing in GDL concerns symmetries *within* the embedding space.
  - *The sharper contrast.* So "they impose; we detect" is true, but the stronger and more defensible difference is **domain symmetry imposed on inputs vs. representation-space symmetry detected in trained weights**.
- **GDL's two degeneracy remarks bear directly on the owner's test.**
  - *p. 37.* With repeated eigenvalues there are "multiple possible diagonalisations". Inside a degenerate multiplet, individual harmonics are **not identifiable**; only the eigenspace is.
  - *p. 54.* Eigenfunctions are unstable under small perturbations. For real embeddings with *near*-degenerate spectra, individual harmonics will be unstable, but spectral *projectors* onto clusters are stable (standard matrix perturbation theory, e.g. Davis–Kahan; not in GDL, stated as my own gloss).
  - *What the test should report.* Cluster-level subspaces and their dimensions, not individual singular vectors.
  - *Link to [THEORY-017](../theory.d/THEORY-017.md).* Eigenvalue multiplicities are unitarily invariant, so they are intrinsic. The basis inside a multiplet is extra data.
- **ML practice.** GDL is a systematisation, not an evidence source. Its practice-relevant claims (augmentation is sample-inefficient; equivariant architectures are preferable when G is known) are cited, not shown. For the anthology it is a theory and background reference; [ANTH-SOTA-358](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/practices.d/SOTA-358.md) records where the practice has moved.

## Limitations

- **A proto-book.** Representation theory and statistical learning theory are both deferred to future work (pp. 5, 43). Several theorem-level statements are made without proof or citation (p. 43).
- **The group is known.** The symmetry group is always assumed known. There is no treatment of approximate or unknown symmetry beyond deformation stability around a given G.
- **Scale separation.** It is argued informally, with its harmonic-analysis development deferred (p. 26).
- **Coverage of this reading.** It is partial (see `read:`). Claims about §5.1, §5.6–§5.8 and §6 rest on keyword search only.

## Open questions

- **Estimating G from a trained network.** Given a trained network with no imposed G, can the (Ω, G) pair of the blueprint be estimated from the network, i.e. run the blueprint backwards? GDL poses the forward problem only.
- **Stability.** Does GDL's stability remedy for spectral filters (use functions of the operator, not its eigenbasis) have an analogue for the owner's degeneracy test, one that detects multiplets without estimating eigenvectors? For example, one could compare the spectra of the concept operators' commutant with those of candidate group algebras.

## Corrections to the seeded skim

- Seeded from metadata and the abstract. The text agrees with the seed's summary in substance, with three precisions.
  - *Version and date.* The version read is v2 (arXiv stamp 2 May 2021; title-page date May 4, 2021). The seed's 2021-04-27 is presumably v1 (unverified).
  - *Authors and affiliations.* Verified from the title page: Bronstein (Imperial College London / USI IDSIA / Twitter), Bruna (NYU), Cohen (Qualcomm AI Research), Veličković (DeepMind).
  - *Transformers.* They appear only as permutation-equivariant attentional GNNs on a complete graph (§5.4, table p. 30). The sequence symmetry is broken by positional encodings, which the text ties to the DFT and Laplacian eigenvectors of a "circular grid" (p. 82).
- **Row 7's implied content is not in this version.**
  - *Irreducible representations.* They appear once as a principle (p. 43: the Fourier transform "can also be extended … by projecting the signal onto the matrix elements of irreducible representations of the symmetry group. We will discuss this in future work"), and once as a survey category in §5.5 (p. 85, Tensor Field Networks, 3D steerable CNNs, SE(3)-Transformer).
  - *Absent terms.* There are no characters, no Peter–Weyl, no isotypic decomposition and no Schur's lemma (keyword search, whole text).
  - *Degeneracy.* It appears only as a **nuisance to be assumed away**. The margin note to the Fourier derivation reads: "We must additionally assume distinct eigenvalues, otherwise there might be multiple possible diagonalisations" (p. 37). The instability of Laplacian eigenfunctions under near-isometric perturbation (p. 54, Fig. 12) is presented as a reason to avoid explicit eigenbases.
- **A theorem stated without its source.** "It is possible to show that any equivariant linear map … can be written as a generalised convolution" (p. 43) is given with no citation. It is Kondor & Trivedi's theorem ([LIT-305](../literature.d/LIT-305.md)), which GDL does not cite (bibliography search; other Kondor papers are cited).
- **Slips.** p. 43 calls SE(3) the "special orthogonal group … (three dimensional)" (it is the special Euclidean group, six-dimensional). p. 43 says "as we have seen in Section 5.3", a later section. p. 37's statement that a matrix is circulant iff it commutes with shift is introduced with "appears to be true as well".
