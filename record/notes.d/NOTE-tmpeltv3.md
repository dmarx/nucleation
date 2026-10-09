---
status: Read
paper: 'LIT-tmpbx6w0'
title: 'Multiscale unfolding of real networks by geometric renormalization'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from the arXiv PDF of v1 (arXiv:1706.00394, 1 June
    2017, 30 pp.; the same file the University of Barcelona repository
    holds), text extracted with pdftotext. Main text §§I–V and
    Appendices A (methods, S¹ and ℍ², Mini-me pruning, dynamics,
    navigation protocol), B, C (semigroup, long-range links, the RG
    equations of the S¹ model, the flow of ⟨k⟩ in the exact r = 2 form
    and the power-law approximation, the partition function, local
    versus global properties), D and E read, with the reference list.
    The derivations of Appendix C followed step by step, not
    re-derived; the series for ν at r = 2 (Eq. C39) taken as given.
    Figures read from captions and text, plots not digitised. The
    journal version (Nature Physics 14, 583–589, 2018) was not reachable
    and was not read; its abstract differs from the preprint's.
date: '2026-10-09'
summary: >-
  Defines a renormalization group for networks embedded in the S¹ hidden
  metric space: merge blocks of angular neighbours, link supernodes if any
  members were linked. To first order the S¹ model maps into itself (κ′ =
  (Σκ^β)^{1/β}, β fixed, μ and R over r), so layers are the same ensemble
  with ⟨k⟩ scaled by r^ν, ν = 2/(γ−1) − 1 or 2/β − 1. Six real networks
  collapse across layers by eye and keep their communities; downscaled
  replicas reproduce three dynamics, and multiscale greedy routing
  succeeds more often.
---
<!-- inactive-ok-file: QUESTION-025 THEORY-tmp1y92d THEORY-tmp5ul7m THEORY-tmpzw8vz THEORY-185 — Open or Proposed; cited for bearing -->

# NOTE-tmpeltv3: Multiscale unfolding of real networks by geometric renormalization

## Contribution

Before this paper, renormalization of networks meant box-covering by
shortest-path distance, which the small-world property makes a poor ruler:
almost everything is a few hops from everything else. This paper takes the
length scale from a hidden metric space instead, the S¹ circle of
Serrano, Krioukov and Boguñá, and coarse-grains along it. It shows that
the S¹ model is (approximately) closed under that coarse-graining, works
out how the average degree flows, and finds that six real networks,
embedded in S¹, behave like the model: their layers look alike once
degrees are rescaled. The self-similar shell is then used to build small
replicas and to route.

## Key insight

If a network's links are governed by distance on a circle weighted by
popularity, then zooming out along that circle is a well-defined operation
and lands back in the same model with only the density changed. Merge
angular neighbours, combine their popularities as an ℓ^β sum, and the
connection law is unchanged. So a real network that embeds well should be
self-similar under this zoom, and the six tested appear to be.

## Assumptions

- **The S¹ model.** N nodes on a circle of radius R = N/2π (unit
  density), angles θ, hidden degrees κ; link probability
  p_ij = 1/(1 + χ_ij^β), χ_ij = RΔθ_ij/(μκ_iκ_j). β > 1 controls
  clustering, μ the average degree. Hidden degrees are taken as
  proportional to observed degrees.
- **The embedding is given.** Real networks are embedded by an existing
  maximum-likelihood method (refs. 23–24); the renormalization assumes
  that embedding is good and the network congruent with the model.
- **For the RG equations (Appendix C).** All r² pairs between two blocks
  are treated as at the same angular distance Δθ_e ≈ Δθ, which needs the
  blocks small relative to their separation; and the expansion of
  Φ′_ij is cut after its first term, justified by R ≫ 1 "in most cases".
- **For the flow of ⟨k⟩.** Hidden degrees power-law distributed on
  [κ₀, κ_c] with exponent γ, κ_c → ∞; the closed forms (Eqs. 5–6) further
  assume the renormalized hidden degrees remain a pure power law, which
  the paper says is "not true in general" and expects to hold as r → ∞.
- **Undirected, unweighted, connected.** Directed and weighted inputs are
  symmetrised or filtered first (bidirectional edges only; a disparity
  filter for the dense Music network), and only the largest component is
  kept.

## Key results

- **Semigroup.** Coarse-graining with r₁ then r₂ equals one step with
  r₁r₂ (proof by floor arithmetic, Eqs. C1–C3); the κ and θ maps compose
  the same way (C14, C16).
- **RG equations of S¹** (C10–C15). Under κ′_i = (Σ_{j∈i} κ_j^β)^{1/β},
  θ′_i = (Σ(θ_jκ_j)^β / Σκ_j^β)^{1/β}, μ′ = μ/r, R′ = R/r, β′ = β, the
  supernode connection probability is
  p′_ij ≈ 1/(1 + (R′Δθ′/(μ′κ′_iκ′_j))^β): the same law. *Holds when:* the
  first-order and equal-distance approximations above. Checked on a
  synthetic network (N ≈ 225,000, γ = 2.5, β = 1.5) through eight
  layers, with mean clustering flat along the flow (Fig. 3A), and on the
  six real networks (Fig. 7).
- **Degree exponent.** With z = κ^β, a sum of r copies stays power-law
  when η = (γ−1)/β + 1 < 3, i.e. (γ−1)/2 < β; then γ is asymptotically
  kept. Otherwise the generalised central limit theorem does not apply
  and scale-freeness is lost along the flow (region III).
- **Average degree.** ⟨k⟩^{(l+1)} = r^ν⟨k⟩^{(l)}. In the power-law
  approximation: ν = 2/(γ−1) − 1 if 1 < η < 2 (γ-dominated,
  (γ−1)/β < 1), and ν = 2/β − 1 if 2 < η < 3 (β-dominated); the two agree
  at β = γ − 1. So the flow goes to a complete graph if γ < 3 or β < 2
  (phase I), keeps ⟨k⟩ on the line γ = 3, β ≥ 2 or β = 2, γ ≥ 3 (an
  unstable fixed line, the small-world/non-small-world boundary), and goes
  to a sparse ring that loses the small world if γ > 3 and β > 2 (phase
  II). An exact series for r = 2 (Eq. C39, Fig. 9) agrees with the
  approximation for large β or γ.
- **Real networks.** Internet (N = 23,748, γ = 2.17, β = 1.44), Airports
  (3,397; 1.88; 1.7), Metabolic (1,436; 2.6; 1.3), Proteome (4,100; 2.25;
  1.001), Music (2,476; 2.27; 1.1) and Words (7,377; 2.25; 1.01): all in
  phase I; Internet and Airports γ-dominated, the rest β-dominated. ⟨k⟩
  grows exponentially in l for all, as predicted (Fig. 3B inset).
- **Self-similarity and communities** (Figs. 2, 6). Degree distributions,
  normalised neighbour degree and clustering spectra overlap across layers
  after rescaling by ⟨k^{(l)}⟩; modularity of each layer and of the
  partition it induces on the original stays high, as does the normalised
  mutual information with the original's partition, through 2 to 5 layers.
- **Long-range selection** (Fig. 8). Links that survive to layer l join
  nodes at larger mean angular distance: the flow keeps the long-range
  links.
- **Partition function** (C51–C62). In ℍ², links are fermionic states of
  energy x_mn/2 with chemical potential R_ℍ²/2; Z = ζ^{N/2} Z′ for r = 2,
  ζ = exp⟨ln(1 + (μκ_mκ_n)^β)⟩ collecting the integrated intra-block
  links. Same approximations as the RG equations.
- **Mini-me replicas** (Figs. 4, 13). Pruning each link of layer l with
  probability p_new/p (μ lowered by a factor tuned until ⟨k⟩ matches the
  original's within 0.1) gives a smaller network congruent with S¹. The
  Ising magnetisation, SIS prevalence and Kuramoto coherence curves on the
  replicas lie close to those on the originals, averaged over 100 runs.
- **Multiscale navigation** (Fig. 5, Appendix A.5, E). With blocks
  restricted to connected consecutive pairs (supernodes of one or two
  nodes, which keeps the self-similarity, Figs. 14–16), greedy routing
  that steps in the highest layer where source and target differ and
  descends via gateways raises the success rate as layers are added, over
  10⁵ random pairs, with average stretch rising only slightly. The cost
  is that each node must know its supernodes' coordinates, neighbours and
  gateways in every layer.
- **Global properties** (Appendix C.6, Figs. 10–12). Adjacency and
  Laplacian spectra, diffusion time and synchronization stability of
  synthetic S¹ networks vary over (γ, β) in line with the ν map: shown,
  not quantified.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Geometric coarse-graining composes as an abelian semigroup | strong (proof) | Appendix C.1, C14, C16 |
| C2 | The S¹ model maps into itself under the RG with κ′ = (Σκ^β)^{1/β}, β′ = β, μ′ = μ/r | moderate | first-order derivation with equal block distances (C4–C13); one synthetic check over eight layers (Fig. 3A) |
| C3 | ⟨k⟩ flows as r^ν with ν = 2/(γ−1) − 1 or 2/β − 1, giving the phase diagram of Fig. 3B | moderate | derivation under a power-law approximation the authors call not generally true; exact r = 2 series agrees for large γ or β |
| C4 | Real scale-free networks that embed well are self-similar under the flow | moderate | six networks, curve collapse judged by eye, 2–5 layers each |
| C5 | Community structure is preserved along the flow | moderate | Louvain modularity and nMI, six networks |
| C6 | This self-similarity is new evidence that hidden metric spaces underlie real networks | weak | interpretation; no comparison with a non-geometric null under the same coarse-graining |
| C7 | Mini-me replicas reproduce Ising, SIS and Kuramoto behaviour of the original | moderate | simulations on six networks, visual agreement of order-parameter curves |
| C8 | Multiscale greedy routing raises success over single-layer routing at small extra stretch | moderate | simulations on six networks, 10⁵ pairs |

## Method

1. Embed the network in S¹ (hidden degrees from observed degrees, angles
   by maximum likelihood).
2. Partition the circle into blocks of r consecutive nodes (or, for
   navigation, connected pairs); merge each into a supernode; link
   supernodes if any members were linked.
3. Assign κ′ and θ′ by the RG equations and rescale μ, R; β is kept.
4. Iterate to get the multiscale shell; for a replica, pick a layer and
   prune its links by the ratio of connection probabilities at a lowered
   μ until ⟨k⟩ matches the original.

## Concepts

- **RGN**: the paper's geometric renormalization group for networks, an
  operator F_r of resolution r on the map M(T, G) of topology and
  geometry.
- **multiscale shell**: the stack of renormalized layers, each r times
  smaller than the last.
- **hidden degree κ**: a node's popularity in the S¹ model, proportional
  to its expected degree; in ℍ² it becomes the radius
  r = R_ℍ² − 2 ln(κ/κ₀).
- **congruency**: a network's agreement with the S¹ connection law,
  measured as the fraction of linked pairs against χ_ij (Figs. 3A, 7, 16).
- **Mini-me replica**: a renormalized layer pruned back to the original
  average degree.
- **γ-dominated / β-dominated**: which parameter sets ν, by whether
  (γ−1)/β is below or above 1.

## Connections

It builds on the S¹ model (Serrano, Krioukov and Boguñá 2008, ref. 14)
and its isomorphism with the ℍ² model of Krioukov et al. 2010
([LIT-tmp0u9c9](../literature.d/LIT-tmp0u9c9.md), ref. 16), which supplies the hyperbolic form and the
fermionic reading used in Appendix C.5. It sets itself against
topological renormalization by box-covering (Song, Havlin and Makse 2005
and successors, refs. 4–9) and random-walk coarse-graining (Gfeller and
De Los Rios, ref. 3): its blocks are ordered by the embedding, and the
model predicts when self-similarity should hold. The block-spin
inspiration is Kadanoff's. The navigation protocol extends single-layer
greedy routing in hyperbolic space (Boguñá, Papadopoulos and Krioukov
2010, ref. 23).

## Bearing on the record

- **On Krioukov et al. ([LIT-tmp0u9c9](../literature.d/LIT-tmp0u9c9.md), [THEORY-tmp1y92d](../theory.d/THEORY-tmp1y92d.md)).** This is that
  model's behaviour under a change of scale, and it supports the reading
  of [THEORY-tmp1y92d](../theory.d/THEORY-tmp1y92d.md)'s "What this does not say": the hierarchy in
  hyperbolic network geometry is radial popularity plus angular
  similarity. The nested shell here is a hierarchy of scales imposed by
  the procedure (each node in one supernode per layer, blocks contiguous
  on the circle), not a hierarchy of kinds found in the data.
- **Produces [THEORY-tmp5ul7m](../theory.d/THEORY-tmp5ul7m.md)**, the approximate closure of the S¹ model
  under geometric coarse-graining and the phases of its degree flow,
  with what it does not show about real networks.
- **On [QUESTION-025](../questions.d/QUESTION-025.md), weakly.** The paper says nothing about attribute
  directions or implication among attributes. Two points touch the
  question. First, its Words network is a co-occurrence graph (word
  adjacency in Darwin's *On the Origin of Species*), and it embeds in S¹
  and stays self-similar with its communities: a co-occurrence structure
  read as similarity on a circle plus popularity, not as additive
  attribute factors, which is the contrast [THEORY-tmp1y92d](../theory.d/THEORY-tmp1y92d.md) already draws
  with [THEORY-185](../theory.d/THEORY-185.md). Second, the multiscale shell supplies a nested
  partition of words by angular contiguity, a dendrogram; on a word
  co-occurrence graph its blocks could be scored against WordNet
  hypernymy, but agreement would show similarity clustering, not
  implication between attributes. Neither answers the question.
- **Batch siblings.** Sala et al. ([LIT-tmpt10fk](../literature.d/LIT-tmpt10fk.md), [THEORY-tmpzw8vz](../theory.d/THEORY-tmpzw8vz.md)) embed a
  given tree with low distortion; this paper starts from no tree and
  produces a nested coarse-graining. Bianconi and Rahmede's *Emergent
  Hyperbolic Network Geometry* ([LIT-tmp9eclr](../literature.d/LIT-tmp9eclr.md)), filed in the same part of
  the batch, is another route to hyperbolic networks, by growth.
- No instruction for machine-learning practice; nothing for the
  anthology. The Mini-me replicas and the routing protocol are
  applications in network engineering.

## Limitations

- **Renormalizability is approximate.** The RG equations drop the
  higher-order terms of Φ′ and treat all inter-block pairs as
  equidistant, which is worst for adjacent supernodes. No error bound is
  given; the check is one synthetic network and the real networks'
  congruency plots.
- **The ⟨k⟩ flow formulas rest on an assumption the authors call not
  generally true** (renormalized hidden degrees exactly power-law); the
  exact form is given only for r = 2.
- **Self-similarity is shown by eye**, with no statistic for the
  collapse and no null model (for instance, the same block-merging on a
  degree-preserving randomisation, or on a randomly ordered circle). That
  leaves C6 weak: merging any blocks of neighbours may produce some
  collapse in heterogeneous networks.
- **Few layers.** Networks of 1,400 to 24,000 nodes give two to five
  layers at r = 2, so "self-similar" is checked over at most a factor of
  32 in size.
- **Two of the six are barely geometric.** Proteome (β = 1.001) and Words
  (β = 1.01) sit at the edge β → 1 of the S¹ model's clustered regime;
  the paper does not discuss what congruency means there.
- **The angle map is not rotation-invariant** (my observation, not the
  paper's). θ′ = (Σ(θκ)^β/Σκ^β)^{1/β} is a power mean of the angles,
  which keeps the order within a block but depends on where θ = 0 is
  placed when β ≠ 1. The paper requires only that order be preserved,
  so this does not break its results, but the supernode positions are a
  convention, not derived.
- **The replicas and routing results are simulations**, with visual
  agreement of curves; critical exponents from finite-size scaling on
  replicas are proposed, not done.
- Read from the preprint; the journal version may differ.

## Open questions

- A bound on the error of the first-order RG equations, or an exact
  treatment showing it vanishes as N → ∞, would make C2 a theorem.
- A null model for the collapse: does block-merging along a random or
  degree-only ordering also give collapse? If not, the self-similarity is
  evidence for the metric space (C6); if so, it is not.
- Whether phase II (γ > 3, β > 2) is ever met by a real network, and what
  its loss of the small world along the flow looks like in data.
- Whether the shell of a word co-occurrence network nests in the way a
  lexical hierarchy does, which would bring it to [QUESTION-025](../questions.d/QUESTION-025.md) as a
  measurement, under the caveat above.
