---
number: 188
status: Proposed
formerly:
- THEORY-tmp1y92d
promote_when: >-
  A proof, not a further simulation, of the model's two signatures in the
  limit N → ∞: that the degree distribution of the hyperbolic random graph
  converges to a power law with exponent 2α/ζ + 1 for α/ζ > ½, and that its
  clustering stays bounded away from zero below T = 1 and tends to zero
  above it, with the large-distance approximation of the source removed or
  its error bounded. Agreement of more real networks' degree and clustering
  statistics with the model cannot settle it, because the account is about
  what the model produces, and a fit of summary statistics does not show
  the geometry is what produced them in a real network.
title: 'In a random graph whose nodes lie in a hyperbolic disk and connect by distance, a power-law degree distribution and strong clustering follow from the geometry: the degree exponent is set by node density relative to curvature, clustering by a temperature, and removing the angular, metric part of the distance leaves the configuration model'
version: 2
history:
- version: 2
  date: '2026-10-20'
  note: >-
    Promotion audit, batch 057: the reading task batch 048 set. Two
    rigorous sources filed and skimmed, Gugelmann, Panagiotou and Peter
    (LIT-1282, NOTE-1010) and Candellero and Fountoulakis
    (LIT-1283, NOTE-1011), and added to `source:`. Their theorems
    meet the promote_when's T = 0 degree and clustering clauses and its
    T ≥ 1 clustering clause as statements, and show the T < 1 clustering
    clause holds for the global coefficient only when α > ζ. A dated note
    says what is met and what is not. Status unchanged.
tags:
- network-science
- complex-systems
date: '2026-10-09'
source:
- LIT-865
- LIT-1282
- LIT-1283
summary: >-
  Krioukov, Papadopoulos, Kitsak, Vahdat and Boguñá (2010), [LIT-865](../literature.d/LIT-865.md):
  derived, in a large-distance approximation, for a model in the
  hyperbolic plane, with simulations. γ = 2α/ζ + 1; clustering falls from
  its maximum at T = 0 to zero at a transition at T = 1; a circle model
  with power-law hidden degrees is the same ensemble once degree is radial
  depth; dropping the angular term gives the configuration model. It does
  not show that any real network is hyperbolic, or that hierarchy causes
  heterogeneity.
---

# THEORY-188: In a random graph whose nodes lie in a hyperbolic disk and connect by distance, a power-law degree distribution and strong clustering follow from the geometry: the degree exponent is set by node density relative to curvature, clustering by a temperature, and removing the angular, metric part of the distance leaves the configuration model

## Source

Krioukov, Papadopoulos, Kitsak, Vahdat and Boguñá (2010), [LIT-865](../literature.d/LIT-865.md),
read in [NOTE-680](../notes.d/NOTE-680.md).

## What was actually shown

The model: N nodes in a disk of radius R ~ (2/ζ) ln N in the hyperbolic
plane of curvature −ζ², angles uniform, radial density ∝ sinh(αr); each
pair linked independently with probability 1/(e^{β(ζ/2)(x−R)} + 1), x
their hyperbolic distance, T = 1/β.

- **Degrees.** For large R, a node at radius r has expected degree
  ∝ e^{−ζr/2}, and since radii are exponentially distributed the degree
  distribution is a power law with γ = 2α/ζ + 1 when α/ζ ≥ ½ (γ = 2
  below), for T < 1; for T > 1, γ = 2αT/ζ + 1. Only the ratio of the
  density exponent to the curvature matters. Fig. 4 checks the degree
  formula against simulation; this part could have failed and did not.
- **Clustering.** Below T = 1 average clustering is positive and decreases
  almost linearly from its maximum at T = 0 to zero at T = 1, where the
  chemical potential R diverges (a phase transition in the ensemble);
  above T = 1 it is zero in the large-network limit. The cold-regime curve
  is numerical integration against simulation (Fig. 6), exact only at
  β = 2, γ = 3.
- **Equivalence.** The S¹ model, nodes on a circle with power-law hidden
  degrees κ and connection a function of distance over κκ′, maps onto this
  one under κ = κ₀e^{ζ(R−r)/2}: degree becomes radial depth. The mapping
  is exact for the approximate distance x ≈ r + r′ + (2/ζ) ln sin(Δθ/2).
- **Degenerate limits.** Sending ζ and T to infinity at fixed ratio removes
  the angular term, so x = r_i + r_j and link probability depends only on
  the product of expected degrees: the configuration model, with no
  clustering. Heating at fixed α, ζ gives Erdős–Rényi graphs.

Statistical mechanics frames it: edges are fermions with energy the
hyperbolic distance, and the exponential random graph's link fields are
linear in it.

## What this does not say

- **Not that real networks are hyperbolic.** The source fits the
  Internet's degree distribution, neighbour degree and clustering with
  three parameters (α = 0.55, ζ = 1, β = 2). That shows the model can
  reproduce those statistics, not that the Internet's links were generated
  by distance in a hyperbolic space. Inferring coordinates for a real
  network is left to other work.
- **Not that every heterogeneous network has a hyperbolic geometry.** The
  source's "effective hyperbolic geometry" is the S¹ ⇄ H² equivalence: it
  assumes the network already has a similarity metric and power-law hidden
  degrees, and shows the two together can be read as a hyperbolic space.
  The extension to other boundaries is argued by analogy.
- **Not that hierarchy causes heterogeneity.** The source motivates
  hyperbolicity by approximately tree-like hierarchies of node similarity
  and reads e^α as their branching factor. In the model, the "hierarchy" is
  the radial ordering by expected degree. Nothing in the derivation needs
  a hierarchy of groups, and nothing tests that one is present.
- **Not that hyperbolic geometry is the only route to the two
  signatures.** Other mechanisms produce power laws and clustering. The
  account says that this geometry produces both from one assumption, and
  that removing the metric term removes the clustering.
- **Not a statement about embeddings of data in machine learning.** The
  contrast with [THEORY-185](THEORY-185.md) is the record's, not the source's: there, log
  co-occurrence additive across independent factors gives linear
  structure; here, the additive per-node part alone is the degenerate
  configuration model, and the structure sits in the non-additive angular
  term. [QUESTION-025](../questions.d/QUESTION-025.md) is where that contrast is open.

## Note of 2026-10-20: the rigorous literature

Promotion audit, batches 048 and 057. The promote_when asks for proofs in
the limit N → ∞. Two held sources now state them in part.

- **Degrees, T = 0.** Gugelmann, Panagiotou and Peter ([LIT-1282](../literature.d/LIT-1282.md),
  Theorems 2.2–2.4) prove for the threshold model at curvature −1 that the
  degree sequence is a power law with exponent 2α + 1 up to the maximum
  degree, which is 2α/ζ + 1 at ζ = 1, with the large-distance
  approximation's error bounded (their Lemmas 3.1–3.2). The degree law at
  T > 0 is attributed by Candellero and Fountoulakis to a paper of
  Fountoulakis's that the record does not hold.
- **Clustering, T = 0.** The same paper proves the average local
  clustering coefficient is Θ(1) with high probability (Theorem 2.1): a
  lower bound, not a limit.
- **Clustering, T > 0.** Candellero and Fountoulakis ([LIT-1283](../literature.d/LIT-1283.md),
  Theorem 1.2) prove, for the global clustering coefficient C2 with
  0 < ζ/α < 2: below T = 1, C2 tends to a positive constant when ζ/α < 1
  and to zero when 1 ≤ ζ/α < 2; at and above T = 1, C2 tends to zero. So
  "bounded away from zero below T = 1" holds for C2 only when the degree
  exponent exceeds 3. For exponents between 2 and 3 the hubs drive C2 to
  zero at every temperature, while the clustering among vertices of
  bounded type stays positive (Theorem 1.3). Neither source treats the
  average local coefficient at 0 < T < 1, the quantity [LIT-865](../literature.d/LIT-865.md) simulates.
- **The configuration-model limit** needs no source: with x = r_i + r_j
  the link probability is a function of e^(−ζr_i/2)e^(−ζr_j/2), the
  product of the two expected degrees, by inspection.

What keeps the account Proposed: both readings are skims ([NOTE-1010](../notes.d/NOTE-1010.md),
[NOTE-1011](../notes.d/NOTE-1011.md)), the theorems taken as stated and the proofs followed only
in outline, which is what held [THEORY-270](THEORY-270.md) in batch 038; and the T < 1
local-clustering clause has no held source. If promoted, the title should
name the clustering coefficient and the ζ/α < 1 condition for the global
one.
