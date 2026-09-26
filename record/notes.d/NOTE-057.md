---
number: 57
status: Read
formerly:
- NOTE-tmphmt18
paper: LIT-091
title: 'Networks beyond pairwise interactions (review)'
version: 2
history:
- version: 2
  date: '2026-09-25'
  note: >-
    Read in full (I read the full text of arXiv:2006.01764v1 (2 Jun 2020,
    dated 3 Jun 2020), 109 PDF pp. That covers the abstract and contents,
    §I–§X and the acknowledgments (pp. 1–88), all 47 figure captions, and
    every equation. I read pp. 1–87 continuously. I scanned the reference
    list (pp. 88–109, refs [1]–[734]) to resolve the citations that the
    definitions and dynamical claims rest on, but did not read every entry.
    Extraction was with PyMuPDF (no pdftotext on this host). I checked two
    formulas that looked wrong against page renders (p. 20, Hodge
    decomposition; p. 45, Komarov–Pikovsky scaling): both are printed as
    extracted. I did three calculations myself: the boundary matrices and L₁
    of a filled triangle, the mean-field bistability threshold of the
    simplicial contagion model (Eq. 58), and the γ_c formula as printed
    against the Fig. 30 caption. I did not compare the journal version
    (Physics Reports 874, 1–92, Aug 2020; Crossref confirms title, 8
    authors, volume and pages).). Upgraded from `Skimmed` to `Read`: the
    claims table, assumptions and results are new, and the skim is corrected
    where the full text disagreed.
date: '2026-09-25'
summary: >-
  The review sets out the representation hierarchy for group interactions
  (graph and clique complex, bipartite graph, motifs, simplicial complex,
  hypergraph) with their operators (incidence, adjacency tensor, boundary
  B_k, Hodge Laplacian L_k = B_kᵀB_k + B_{k+1}B_{k+1}ᵀ with ker L_k ≅
  H_k). It surveys the random models and the dynamics built on them. Its
  own §V makes the key qualification: linear diffusion with three-body
  terms "can always be reduced to" a weighted pairwise Laplacian (Eq. 35).
  A random walk with edge-independent vertex weights is equivalent to one
  on a weighted projected graph (Chitra–Raphael). Qualitatively new
  node-level behaviour needs nonlinear group coupling or edge-dependent
  weights. With those, it reports explosive or abrupt transitions and
  bistability: Kuramoto with triadic coupling, simplicial SIS with a
  discontinuous transition, and higher-order ecological models that
  stabilise coexistence.
---

# NOTE-057: Networks beyond pairwise interactions (review)

## Contribution

A synthesis rather than new results. Before this review the literature on group interactions was scattered across algebraic topology, random-graph theory, statistical physics, ecology and social science, each with its own representation. The review does three things with it.
1. It gives one vocabulary for "higher-order systems" (HOrSs) and says exactly what each representation keeps or discards (§II; Figs 1–2).
2. It collects the matrix and tensor operators and measures in one place (§III), and sorts generative models into equilibrium and out-of-equilibrium models, by representation (§IV).
3. It surveys how diffusion, synchronisation, contagion, opinion dynamics and games change when coupling is non-pairwise (§V–§VIII), then lists applications (§IX) and open problems (§X).

## Key insight

"Higher-order" is a property of the coupling function, not just of the wiring diagram. If group interactions enter linearly, as in diffusion or random walks with edge-independent weights, they collapse to a reweighted graph, and the higher-order structure only reweights pairwise edges. They produce genuinely new collective behaviour when they enter nonlinearly. Examples are:
- a phase coupling sin(θ_j + θ_k − 2θ_i);
- a contagion that fires only when all other members of a simplex are infected;
- a replicator fitness with b_ijk x_j x_k terms;
- an influence function s(|x_j − x_k|).

These give abrupt or explosive transitions, bistability and hysteresis, and stabilised coexistence. Separately, choosing a simplicial complex or a hypergraph is a substantive modelling claim, namely whether every sub-group of an interacting group also interacts, and it changes the dynamics (compare Eq. 58 with Eq. 59).

## Assumptions

A review, so these are the framework's standing assumptions rather than theorem hypotheses.
- **Interaction.** An interaction is an unordered set I = [p₀, …, p_{k−1}] of k nodes, of order k − 1. It is "higher-order" iff k ≥ 3, i.e. order ≥ 2 (§II A 1).
- **What is excluded.** Other "higher-order" dependencies are deliberately out of scope: multilayer link types and non-Markovian paths in temporal data (p. 5).
- **Simplicial complexes** assume downward closure: every face of a simplex is present.
- **Hypergraphs** assume nothing about sub-interactions, and even allow hyperedges that contain other hyperedges (p. 8).
- **Orientation.** Boundary and Laplacian constructions need an arbitrary orientation of each simplex and a coefficient field F. The homology depends on F (p. 17).
- **Scope of the dynamical results.** Most are mean-field or all-to-all (Eqs 43–45, 58, 67–70), use identical oscillators (Eq. 48), or are simulations on specific synthetic or empirical structures. Their scope is therefore narrower than the section titles suggest.

## Key results

These are the review's reported results, with the sources it credits.
- **Representation hierarchy (§II; Figs 1–2).**
  - The graph projection loses group identity: {[a,b,c],[a,d],[d,c],[c,e]} → a graph where [a,b,c] and [a,c,d] are indistinguishable.
  - The clique complex over-fills: it adds [a,c,d].
  - The bipartite representation preserves everything but mediates all node–node relations through an interaction layer.
  - The facet list of a simplicial complex is a bipartite graph or hypergraph. The converse holds only if no hyperedge is contained in another.
- **Operators (§III).**
  - A = IIᵀ − D (Eq. 1), whose entries count shared hyperedges.
  - The intersection profile P = IᵀI (Eq. 2).
  - Boundary ∂_k[v₀…v_k] = Σᵢ(−1)ⁱ[…v̂ᵢ…] (Eq. 8), with ∂_k∂_{k+1} = 0, H_k = ker ∂_k / im ∂_{k+1} (Eq. 9), and Betti numbers β_k = dim H_k.
  - L_k = B_kᵀB_k + B_{k+1}B_{k+1}ᵀ (Eq. 15), with L₀ the graph Laplacian and dim ker L_k = β_k.
  - The rewritten form L_k = D_k^U − A_k^U + (k+1)I + A_k^L (Eq. 16).
  - Chung's s-uniform hypergraph Laplacian (Eq. 12).
  - Z- and H-eigenvector centralities of adjacency tensors (Eqs 6–7).
- **Random geometric complexes (§IV A 5).** There are three regimes in Λ = n r^d:
  - vanishing: sparse and dust-like;
  - constant: peak homology growth;
  - diverging: two homology phase transitions.
- **Diffusion (§V).**
  - Linear three-body diffusion reduces to L^△ with ℓ^△_ij = δ_ij Σ_k a^△_ijk − Σ_k a^△_ijk (Eq. 35).
  - Relaxation bounds for k-diffusion: (1/µ₂)‖L_k x(t)‖ ≤ ‖x(∞) − x(t)‖ ≤ N_k e^{−µ₂t}‖x(0)‖ (Eq. 38).
  - In NGF complexes, the spectral dimension of L_k grows with k (Torres–Bianconi; Fig. 14).
- **Random walks (§V B).**
  - Carletti et al.'s size-weighted hypergraph walk, p(∞)_c ∼ 1 + (k − 1)², ranks node c above the hub when k + 1 ≤ m ≤ 1 + (k − 1)², where the projected graph ranks the hub first.
  - Chitra–Raphael: walks with edge-dependent vertex weights are not time-reversible and cannot be reduced to weighted-graph walks.
- **Synchronisation (§VI).**
  - Pure triadic Kuramoto, θ̇_i = ω_i + (K₂/N²) Σ_jk sin(θ_j + θ_k − 2θ_i) (Eq. 43; Skardal–Arenas 2019). It shows an abrupt desynchronisation, a continuum of stable 2-cluster branches, and an incoherent state that is stable for all K₂.
  - Mixed 1-, 2- and 3-simplex coupling (Skardal–Arenas 2020) is bistable with hysteresis above K₂ + K₃ = 2, and can synchronise even with repulsive pairwise coupling K₁ < 0.
  - Identical oscillators on complexes (Lucas et al., Eqs 48–51): the linear stability of synchrony is set by λ₂ of a multi-order Laplacian. All-to-all, the Lyapunov exponent is ∝ q.
  - Phase reduction to second order produces 3- and 4-body phase terms from pairwise physical coupling (Ashwin–Rodrigues, Eq. 52; León–Pazó; Matheny et al.). Such terms allow chaos at N = 4 with two harmonics (Bick et al.).
  - The Master Stability Function is generalised to simplicial complexes (Gambuzza et al., Eq. 53).
- **Contagion (§VII A).**
  - Simplicial SIS, dρ/dt = −µρ + Σ_d β_d ⟨k_d⟩ ρ^d (1 − ρ) (Eq. 58), becomes discontinuous and bistable with a 2-simplex channel.
  - My mean-field check: with λ = β₁⟨k⟩/µ and λ_Δ = β₂⟨k_Δ⟩/µ, an endemic branch exists below λ = 1 iff λ_Δ > 1. At λ_Δ = 2.5 it persists down to λ ≈ 0.66, consistent with the bistable λ = 0.75 example in Fig. 29I.
  - On d-uniform scale-free hypergraphs (Jhun et al., Eq. 59) the transition type depends on γ relative to the printed γ_c = 2 + 1/(d − 2).
- **Opinion dynamics (§VII B).** In nonlinear three-body consensus, ẋ_i = Σ A_ijk s(|x_j − x_k|)[(x_j − x_i) + (x_k − x_i)] (Eq. 61), the mean state is conserved only when s is constant. With s = e^{λ|·|} it drifts toward the majority (λ < 0) or toward balance (λ > 0).
- **Games (§VIII).**
  - Public goods on the true bipartite collaboration structure yields more cooperation than on its projection (Gómez-Gardeñes et al.).
  - On hypergraphs with R(G) = αG^β, all hypergraph classes coincide for β = 1 and separate for β ≠ 1 (Alvarez-Rodriguez et al.).
- **Ecology (§IX C).**
  - Random replicator dynamics (Bairey et al., Eqs 67–68): the pairwise critical strength α_c ∝ 1/N; the three-body β_c is independent of N; the four-body γ_c increases with N.
  - Grilli et al. (Eqs 69–70): with pairwise competition, cycles are neutral and destabilised by any death-rate heterogeneity. With three-seedling competition the same interior point becomes globally stable.
- **Neuroscience (§IX B).** The macroscopic evidence is mixed. Huang et al. report weak higher-order interactions and dominant pairwise ones in functional networks. Other work reports test–retest reliability and diagnostic value.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Graph projections and clique complexes cannot recover which groups interacted; one loses group identity, the other invents groups | strong | Constructive counterexample (§II A 2–3, Fig. 1) |
| C2 | dim ker L_k = β_k: the Hodge Laplacian's kernel counts k-dimensional holes | strong | Standard combinatorial Hodge theorem, cited [66, 68] (the decomposition formula as printed is misindexed; see corrections) |
| C3 | Linear diffusion with group terms reduces to pairwise diffusion on a reweighted graph | strong | Direct algebra (Eq. 35), stated by the review (p. 37) |
| C4 | Random walks on hypergraphs with edge-independent vertex weights are equivalent to walks on a weighted graph; edge-dependent weights break this | moderate | Reported result of Chitra & Raphael [326] (time-reversibility argument); not reproduced |
| C5 | Nonlinear three-body phase coupling yields abrupt desynchronisation and multistability absent in pairwise Kuramoto | moderate | Reported analysis (Ott–Antonsen-type self-consistency) in all-to-all models [371, 373, 375] |
| C6 | Higher-order interactions are "sufficient to induce explosive synchronization" | moderate | Skardal & Arenas [376]: all-to-all reduction plus simulation on one macaque clique-complex; the brain complex is constructed by promoting every clique |
| C7 | Adding 2-simplex infection makes SIS contagion discontinuous with bistability | moderate | MF Eq. 58 plus simulations on synthetic and SocioPatterns complexes [262] (the MF threshold λ_Δ > 1 is my derivation) |
| C8 | Higher-order interactions stabilise species coexistence | moderate | Two model families [28, 655]: Grilli's competition model (proved global stability for three-way competition) and Bairey's random replicator (simulation thresholds). The review's "many particular condition settings" is not a general theorem |
| C9 | Phase reduction of pairwise-coupled nonlinear oscillators generates many-body phase interactions at second order | strong | Derivations reported [374, 383, 393], with experimental corroboration in the 8-oscillator NEMS ring |
| C10 | "There are no doubts now that moving beyond dyadic interactions is fundamental to explain and predict collective behaviors" (p. 4) | assertion | Introduction. §X says "we still lack a general understanding of how higher-order terms affect dynamical systems", and that simplicial and complex contagion may be indistinguishable without microscopic data |
| C11 | Higher-order interactions "profoundly change the critical behavior of dynamical processes" (§X) | weak (as cited) | The citation list mixes genuinely nonlinear cases with linear ones ([68, 134, 319, 84]) that §V shows reduce to or do not alter pairwise node dynamics |
| C12 | No inference scheme currently exists to test for higher-order interactions from dynamical data at scale | moderate | §X survey; the small-N phase-reconstruction methods of §VI C are limited by data needed to cover the N-torus |

## Concepts

- **Order of an interaction**: k − 1 for k participating nodes. "Higher-order" means order ≥ 2 (≥ 3 nodes). "Low order" covers self- and pairwise interactions.
- **HOrS**: the review's shorthand for a higher-order system, any interacting system (V, I) with some interactions of order ≥ 2.
- **Simplicial complex**: a set of simplices closed under taking faces.
- **Hypergraph**: a node set plus arbitrary non-empty subsets as hyperedges, with no closure requirement.
- **Clique (flag) complex**: the complex whose simplices are the cliques of a graph, i.e. one fully determined by its 1-skeleton.
- **Facet**: a maximal simplex. The facet list is a compressed, bipartite-equivalent encoding.
- **Hasse diagram**: a DAG with one node per simplex and edges for codimension-1 inclusion. It gives the "walk" structure behind the Laplacians.
- **Upper and lower adjacency**: two k-simplices are lower-adjacent if they share a (k − 1)-face, and upper-adjacent if they are faces of a common (k + 1)-simplex.
- **k-walk (hypergraphs)**: a sequence of hyperedges with consecutive intersections of ≥ k nodes.
- **Generalised degree k_{d,δ}(α)**: the number of d-simplices incident on the δ-simplex α.
- **Combinatorial (Hodge) Laplacian L_k**: B_kᵀB_k + B_{k+1}B_{k+1}ᵀ, acting on k-chains. It splits flows into gradient, harmonic and curl parts.
- **Simplicial closure**: the higher-order analogue of triadic closure. It asks whether three pairwise-connected nodes also form a 2-simplex. It is cited as a measure with no pairwise counterpart.
- **Explosive synchronisation**: a discontinuous, hysteretic onset of synchrony.
- **Multi-order Laplacian**: the coupling-weighted sum of order-q Laplacians l^{(q)}_ij = q k^{(q)}_i δ_ij − â^{(q)}_ij. It governs linear stability of synchrony for identical oscillators.
- **Simplicial contagion**: SIS where a d-simplex transmits to its last susceptible member only when all other members are infected, at rate β_d.

## Connections

The review consolidates several lines of work:
- Atkin's q-analysis (1970s);
- Berge's hypergraphs;
- topological data analysis and persistent homology (Carlsson, Edelsbrunner, Zomorodian);
- the Bianconi school's network geometry (NGF);
- Kuramoto/Ott–Antonsen synchronisation theory;
- the Iacopini–Petri simplicial contagion line.

It deliberately excludes the parallel "higher-order" literature on multilayer and non-Markovian path models (Lambiotte, Rosvall and Scholtes).

Relations to nucleation's network readings:
- **[LIT-020](../literature.d/LIT-020.md)** (reads/12, Forman–Ricci curvature). Forman's curvature is defined on CW complexes, and reads/12 records that the network paper uses only the plain graph form. It defers the triangle and cycle terms that this review's clique and simplicial complexes would supply. The review's L_k is Forman's setting, since Bochner–Weitzenböck decomposes the Hodge Laplacian. Read together, [LIT-020](../literature.d/LIT-020.md)'s Eq. 11 is the 1-skeleton special case of a construction this review gives the full simplicial apparatus for, though the review itself does not discuss Forman curvature.
- **[LIT-004](../literature.d/LIT-004.md)** (reads/59, Ollivier–Ricci flow community detection) is pairwise throughout. The review's §X notes that mesoscale structure (communities) in simplicial complexes is barely studied [337, 719]. There is no direct link beyond that gap.
- **[LIT-028](../literature.d/LIT-028.md)** (reads/1, spectral versus gap dimension in bundled networks) connects through the spectral dimension:
  - the review reports that the spectral dimension of L_k in NGF complexes grows with order k (Torres–Bianconi; Fig. 14);
  - it reports that in complex network manifolds d_S ≃ d, with synchrony thermodynamically stable only for d_S > 4 (Millán et al.);
  - [LIT-028](../literature.d/LIT-028.md)'s point is that the density-of-states exponent (d_s) and the gap exponent (d_g) can come apart;
  - the review uses "spectral dimension" only in the density-of-states sense.

  So any argument that joins "d_S > 4 ⇒ stable synchrony" to a gap-controlled relaxation time should check which exponent it means. That is an inference from putting the two readings together, not a claim in either.
- **Information decomposition.** The review's "Inference from data" paragraph cites Rosas et al.'s O-information and Faes et al. [730–732] as measures of high-order dependence. That is the same programme as nucleation's [LIT-025](../literature.d/LIT-025.md) (ΦID review) and [LIT-042](../literature.d/LIT-042.md) (Shannon invariants). The review uses the idea only in passing and does not engage the redundancy–synergy question.

## Bearing on the record

For nucleation, this is the right anchor citation for:
- the definitions of simplicial complex versus hypergraph and what each assumes;
- the operators (incidence, adjacency tensor, boundary, Hodge Laplacian, with the index fix noted above);
- the catalogue of higher-order dynamical models up to mid-2020.

It should not be cited:
- as showing that higher-order structure per se changes dynamics (C10, C11). Its own §V says linear processes reduce to pairwise ones, and the effects it reports come from nonlinear group coupling;
- for the brain-network claims, where it reports the evidence as mixed.

No nucleation THEORY document exists to test. If one is written, the defensible statement this review supports is conditional: the higher-order form of interactions matters for node-level dynamics only through nonlinear group terms, and otherwise acts as a reweighting.

For ML practice: nothing directly. The review predates hypergraph and simplicial neural networks and gives no instruction for building or training models. Its tangential ML content is edge-flow semi-supervised learning with L₁ and spectral hypergraph embeddings. If the anthology ever files hypergraph or simplicial neural-network work, this is the background definitional reference to cite from it, by name (from the anthology a nucleation work is named, not coded). No ANTH- document is warranted from it.

## Limitations

- **It is a survey.** Nearly every dynamical result is a one-paragraph summary of a single paper, often mean-field or all-to-all. The review does not reconcile cases where modelling choices drive outcomes, such as symmetric versus asymmetric three-body coupling functions, which it says have "not been investigated systematically" (p. 47).
- **Framing outruns the body.** The introduction's "no doubts" and §X's broad claims outrun §V's own reduction results. The review never states, as a result, the condition under which higher-order structure is dynamically inert.
- **It is 2020-dated.** It predates the 2021 onward work on higher-order network inference, hypergraph and simplicial neural networks, and much of higher-order percolation and contagion theory.
- **Author weighting.** Coverage leans on the authors' own groups (e.g. [141, 262, 273, 586, 598]), which is natural, but gives some sections a particular slant.
- **Typos.** Several formulas are printed with index or exponent errors (see corrections). The Hodge decomposition, the one a reader is most likely to copy, is among them.
- **Open inference problem, by its own admission.** It gives no way to distinguish genuine group interaction from its low-order shadows in observational data (§X).

## Open questions

The review's own, sharpened:
- **Detection.** What observational data, and what test, can distinguish a genuine k-body coupling from pairwise coupling plus correlations? §X notes this is open even for contagion (simplicial versus complex).
- **Coupling form.** How do the qualitative effects (explosive onset, multistability) depend on the choice of higher-order coupling function (symmetric versus asymmetric) and on normalisation?
- **Generative models.** Are there generative models for simplicial complexes that fix mesoscale or homological targets rather than only degrees?
- **Localisation.** Can homological features be localised on specific simplices in a principled, non-ad-hoc way?
- **Reducibility.** When is a nonlinear higher-order model reducible to an effective pairwise one? Phase reduction (C9) shows the arrow can run the other way, so which description is fundamental is itself a modelling choice.

## Corrections to the seeded skim

- **The dossier's headline is broader than the review's body supports.** The dossier says representing group interactions explicitly "changes both the measured structure and the dynamics, and in particular adds new non-linearities and abrupt (explosive) transitions that pairwise models miss". The body is more careful, and the qualification is load-bearing:
  - §V (p. 37): "traditional diffusion is a linear process and consequently the simplest generalization to higher-order structures can always be reduced to equations involving only pairwise couplings". Three-body linear diffusion becomes a weighted graph Laplacian L^△ (Eq. 35).
  - §V B (p. 41): random walks on hypergraphs with edge-independent vertex weights are equivalent to walks on a suitably weighted projected graph. Only edge-dependent vertex weights, or nonlinear operators, escape this.
  - The multi-order Laplacian of Lucas et al. (Eqs 49–51) likewise shows that, near synchrony, identical oscillators with higher-order coupling are governed by a weighted pairwise matrix.

  The abrupt transitions come from nonlinear group coupling functions, not from the higher-order structure as such.
- **§X overstates its own sources.** Its list of cases where higher-order interactions "profoundly change the critical behavior" (p. 86) cites Zhou et al. [84]: an edge-independent hypergraph random walk, which §V B's own account reduces to a weighted-graph walk. It also cites the linear edge/simplex diffusion papers [68, 134, 319]. The review's own examples of changed critical behaviour are [262], [376], [394], [238] and [586].
- **Dossier on ML:** it says the review "predates" hypergraph and simplicial neural networks. More exactly, the review covers spectral learning on hypergraphs (Zhou–Huang–Schölkopf, NeurIPS 2007; Fig. 16) and semi-supervised edge-flow learning with L₁ (Fig. 15), but cites no hypergraph or simplicial neural-network architecture.
- **Formula slips in the text (not in the dossier):**
  - p. 20: the Hodge decomposition is printed C_k = im(B_d) ⊕ ker(L_k) ⊕ im(B_{d+1}ᵀ), with ker(L_k) = ker(B_dᵀ) ∩ ker(B_{d+1}). With the paper's own convention (Eq. 15, L_k = B_kᵀB_k + B_{k+1}B_{k+1}ᵀ, B_k: C_k → C_{k−1}), im(B_k) lies in C_{k−1}. The correct statements are C_k = im(B_kᵀ) ⊕ ker L_k ⊕ im(B_{k+1}) and ker L_k = ker B_k ∩ ker B_{k+1}ᵀ. I confirmed from the render that this is how it is printed.
  - p. 20: "a single simplex of dimension q" has "one eigenvalue µ = q with multiplicity q!/[(q − 1 − k)!(k + 1)!]". This is right only if q counts vertices. For a filled triangle (dimension 2) L₁ = 3I (my computation: eigenvalues 3, 3, 3), i.e. µ = q + 1 in dimension terms, with multiplicity C(3,2) = 3 rather than 1. At k = 0 there is also a zero eigenvalue.
  - p. 16: "3rd [Betti number] the number of 4-dimensional voids" should read 3-dimensional.
  - Eq. 16: the text says "Setting k = 0, one recovers standard graph Laplacian of Eq. 12". Eq. 12 is Chung's hypergraph Laplacian; the graph Laplacian is Eq. 11.
  - Eq. 22: (1 − p)^{B_ij} p^{B_ij} should be (1 − p)^{1−B_ij} p^{B_ij}.
  - Eq. 24 (hypergraph SBM): has the β-model probability from Eq. 23 pasted onto it.
  - p. 33: the Chinese restaurant process is given probabilities 1 − 1/(t+1) and 1/t, which do not sum to 1.
  - p. 45: "R₁ ∼ √N … which vanishes in the thermodynamic limit" (confirmed from the render) is self-contradictory; presumably N^{−1/2}.
  - The Fig. 30 caption lists γ = 2.6 as both second-order and hybrid. With d = 3 in the stated γ_c = 2 + 1/(d − 2) = 3, the caption's finite threshold at γ = 2.6 and 2.8 conflicts with the text's claim that λ_c vanishes for γ < γ_c. This is unresolved without the source [479].
- The dossier's metadata is correct: 8 authors; Physics Reports 874, 1–92; arXiv v1 2 Jun 2020, and the only version.
