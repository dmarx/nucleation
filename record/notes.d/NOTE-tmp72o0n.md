---
status: Read
paper: 'LIT-tmpu05fk'
title: 'Chowdhury & Mémoli — Network Gromov–Wasserstein'
version: 1
history:
- version: 1
  date: '2026-10-29'
  note: >-
    Read in full from the arXiv preprint 1808.04337v2 (margin stamp 4 Sep
    2019, the substantially updated version), 25 pp., extracted with
    `pdftotext -layout`. I read every section: the introduction, §2
    (Definitions 1–4, Lemmas 9–11, Theorems 12, 16, 18 and 20, Lemma 21,
    with their proofs), §3 (Theorem 24 with Lemmas 27–28 and its proof,
    Proposition 31, Theorem 32 with its proof, §3.2.1), §4 (the experiments,
    Tables 1–2, Figs. 4–6 with captions), §5, the references and Appendix A
    (entropic regularization, Algorithms 1–3, Sturm's cosine rule, Fig. 7).
    The proofs are all in the main text; Appendix A holds computational
    notes, not proofs. Pages are the preprint's. The journal version
    (Information and Inference 8(4), 757–787) was not read, so differences
    from it are unknown. The heat-map figures did not survive extraction;
    their captions did. Checks, numpy/scipy/POT 0.9.7, my own script: (1) on
    25 random pairs of asymmetric networks with non-uniform measures, the
    TLB computed with one linear program per joint eccentricity equals the
    closed-form R-TLB to 3e-15, in both directions; (2) on the same pairs,
    the best coupling found by many restarts never violated GW ≥ TLB ≥ FLB ≥
    SzLB or GW ≥ SLB; (3) identity (3) holds for n = 2 to 6 and the stated
    sphere areas are right; (4) the interleaving distance between f₁ and g₁
    for S¹ and S² is 0.1708, so the reported bound "≥ 0.17" reproduces;
    (5) a pair of 3-node networks with all of these invariants equal and
    dN,2 ≥ 0.215 (below).
date: '2026-10-29'
summary: >-
  The Gromov–Wasserstein distance, defined by minimizing the distortion of
  a coupling, is a pseudometric on all measure networks: any Polish node
  set with a probability measure and any bounded, possibly asymmetric,
  edge-weight function. It is zero exactly when the two networks are
  weakly isomorphic, that is, when both are images of one network that
  preserves weights and measures. Cheap invariants give a hierarchy of
  lower bounds, and the third lower bound, a transport problem whose
  costs are themselves transport problems, reduces to one-dimensional
  transport in closed form. The bounds are one-sided: networks can agree
  on every invariant and still be apart.
---
<!-- inactive-ok-file: CLAIM-448 QUESTION-tmp6byb6 — Proposed or Open; the entries this reading bears on, cited as open -->

# NOTE-tmp72o0n: Chowdhury & Mémoli — Network Gromov–Wasserstein

## Contribution

It carries the Gromov–Wasserstein (GW) distance from metric measure spaces
to "measure networks" (X, ωX, µX): a Polish space, a fully supported Borel
probability measure, and a bounded measurable weight function that need be
neither symmetric nor a metric (Definition 1, p. 4). It proves that the
distance is a pseudometric there and identifies its zero set as weak
isomorphism. It gives in- and out-going versions of Mémoli's first, second
and third lower bounds, and proves in general what [SS13] had shown for
discrete spaces: each bound equals a transport problem over the real line.
It adds the sublevel size function, an invariant stable in an interleaving
sense, and uses it to improve a lower bound between spheres.

## Key insight

The metric on the space of networks does not come from the networks. Any
bounded weight function will do, because the distance compares weights
through a coupling and the triangle inequality comes from gluing couplings:
"the metric structure on N is not inherited from its elements, but is
rather enforced by the structure of dN,p" (p. 9). What the distance can see
is fixed by what is written into ωX and µX. Two networks are at distance
zero exactly when some third network maps onto both while preserving
weights and measures (Theorem 18), so splitting a node into copies with the
same in- and out-weights changes nothing (p. 5).

## Assumptions

- **Networks**: X Polish, µX a fully supported Borel probability measure,
  ωX bounded and measurable on X × X (Definition 1, p. 4). The
  introduction allows "any measurable, integrable function" (p. 3); the
  definition the proofs use asks for boundedness.
- **Complete weights.** ωX must be defined on all of X × X. "network
  datasets in the wild are often incomplete, i.e. ωX is not fully defined on
  X × X. In such cases, one needs to preprocess the data" (Remark 1, p. 4).
- **The measure is the user's.** "The user adjusts the measure to signify
  important network substructures and to smooth out the effect of
  outliers" (p. 2). Every result is relative to that choice.
- **The distortion formulation** of GW throughout, not Sturm's
  transportation formulation (p. 2).
- **p ∈ [1, ∞]**; existence of optimal couplings uses compactness of the
  coupling set (Lemma 10) and continuity (p < ∞) or lower semicontinuity
  (p = ∞) of the distortion (Lemma 11, pp. 7–8).

## Key results

### The distance (§2.4, pp. 8–9)

- **Definition:** dN,p(X, Y) = ½ min over couplings µ of disp(µ), with
  disp(µ) = ‖ωX − ωY‖ in Lp(µ ⊗ µ) (p. 6, p. 8). Optimal couplings exist
  for every p (Theorem 12, p. 8).
- **Theorem 16 (p. 8):** dN,p is a pseudometric on N. Symmetry by swapping
  coordinates, triangle inequality by the gluing lemma and Minkowski
  (pp. 8–9).
- **Theorem 18 (p. 9):** dN,p(X, Y) = 0 iff X and Y are weakly
  isomorphic: there is (Z, µZ) with maps f, g pushing µZ to µX and µY and
  ‖f*ωX − g*ωY‖∞ = 0 (Definition 3, p. 5). Remark 15: dN,p is not a metric
  modulo strong isomorphism (p. 8; Fig. 2 shows three weakly isomorphic
  networks of 3, 3 and 4 nodes).
- **Simple cases (Example 14, p. 8):** dN,p(N₁(a), N₁(b)) = |a − b|, and
  the distance to a one-node network is half the Lp deviation of ωX from
  its weight.
- **Gromov–Prokhorov version (§2.5.2, p. 10):** a pseudometric for each
  α ≥ 0 (Theorem 20), with d^GP at α = 0 equal to dN,∞ (Lemma 21).

### The hierarchy of lower bounds (Theorem 24, pp. 11–13)

For p ∈ [1, ∞] and C(x, y) = Wp(ωX(x, ·)∗µX, ωY(y, ·)∗µY):

2dN,p ≥ TLB = inf over µ of ‖eccout_{p,X,Y}‖_{Lp(µ)} = R-TLB (an OT
problem with cost C) ≥ FLB = R-FLB = Wp of the pushed-forward eccentricity
distributions ≥ |sizep(X) − sizep(Y)|; and separately 2dN,p ≥ SLB = R-SLB =
Wp((ωX)∗µX⊗², (ωY)∗µY⊗²). Each also holds for the incoming versions.

- The equalities rest on Lemma 28 (p. 13): pushforwards of couplings are
  exactly the couplings of the pushforwards, proved with analytic sets and
  Varadarajan's lemma.
- "The main development of the current paper is that we have equalities
  (FLB)=(R-FLB), (SLB)=(R-SLB), and (TLB)=(R-TLB)" (Remark 25, p. 12), and
  "in the discrete case, all of the aforementioned equalities follow from
  [SS13, Proposition 4.5]" (p. 12). The new part is the general setting.
- I checked TLB = R-TLB and the order of the bounds numerically (history).

### Interleaving stability and spheres (§3.2, pp. 13–16)

- **subSizep,t(X) = ‖ωX 1{ωX ≤ t}‖ in Lp(µX ⊗ µX)** (p. 14).
  **Theorem 32 (p. 15):** with ε = dN,∞(X, Y),
  subSizep,t(X) ≤ ε + subSizep,t+ε(Y) and symmetrically. Remark 33 gives
  the superlevel version.
- **Spheres (Example 30, Proposition 31, p. 14):** size₁ is π/2 for every
  sphere, so it cannot tell them apart, while t ↦ subSize₁,t can:
  t²/(2π) for S¹ and (sin t − t cos t)/2 for S².
- **The bound (p. 16):** dN,∞(S¹, S²) ≥ dI(f₁, g₁) ≥ 0.17, against the
  earlier 0.0503 from [Mém11]; "Our new lower bound of 0.17 improves this
  threefold." I computed dI(f₁, g₁) = 0.1708. The exact value "is unknown
  in the existing literature, even for n = 1, m = 2" (p. 15).

### Experiments (§4, pp. 16–19)

- All computed with the R-TLB (max of in and out, p = 2), which "can be
  computed exactly at reasonable speed" for several hundred nodes, under a
  minute in Matlab (p. 16). It needs no parameter tuning, unlike entropic
  GW (p. 3).
- **Network SBM (§4.2, p. 17):** Gaussian edge weights by block, uniform
  node measure.
- **Cycle-network SBMs (§4.3, pp. 17–18):** five classes of 10 networks.
  Classes 1 and 3 (same structure, twice the nodes) come out close; the
  others separate (Fig. 5 caption). "This is consistent, because dN is not
  sensitive to the size of the networks (cf. Theorem 18)" (p. 18).
- **Sliding means (§4.4, pp. 18–19):** after normalization to [−1, 1], the
  dissimilarity matrix shows a "linear color gradient" (p. 19).
- **World Bank migration (§4.5, p. 19):** ten 225-node networks, by sex
  and decade 1960–2000. The single-linkage dendrogram groups by decade
  first, by sex within decades (Fig. 6). The interpretation in terms of
  "global technological and economical forces" (p. 19) is not tested.

### Appendix A (pp. 22–25)

Heuristics for entropic regularization on networks with widely spread
weights: a log-domain initialization (Algorithm 3), and Sturm's cosine
rule, by which rescaling both networks moves them along geodesic rays to
the one-node network N₁(0), so a pair-specific regularization parameter
equals a global one applied to rescaled networks (A.1.2).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | dN,p is a pseudometric on measure networks with bounded, possibly asymmetric weights, for every p ∈ [1, ∞] | strong | Theorem 16, proof pp. 8–9 |
| C2 | dN,p(X, Y) = 0 iff X and Y are weakly isomorphic | strong | Theorem 18, proof p. 9 |
| C3 | GW ≥ TLB = R-TLB ≥ FLB = R-FLB ≥ SzLB, and GW ≥ SLB = R-SLB, in in- and out-going versions | strong | Theorem 24 with Lemma 28, pp. 11–13; checked numerically |
| C4 | Sublevel size functions are interleaving-stable at ε = dN,∞ | strong | Theorem 32, proof p. 15 |
| C5 | dN,∞(S¹, S²) ≥ 0.17 | strong | computation from Proposition 31 and Theorem 32, p. 16; reproduced (0.1708) |
| C6 | The R-TLB separates the simulated network classes and orders the migration networks by decade and sex | moderate | three experiments, §4; no comparison with another method, no null model |
| C7 | The network SBM "will likely yield useful benchmarks" (p. 20) | weak | stated, not shown |

## Concepts

- **Measure network** — (X, ωX, µX) as in Definition 1: a complete
  weighted directed graph with node "significance values" when X is finite
  (p. 4).
- **Weak isomorphism** — both networks are pushforwards of one network
  (Z, µZ) whose pulled-back weights agree µZ ⊗ µZ-almost everywhere
  (Definition 3, p. 5). Nodes with identical "internal" and "external
  perception" may be merged or split (Remark 3, p. 5).
- **Distortion of a coupling** — the Lp(µ ⊗ µ) norm of
  ωX(x, x′) − ωY(y, y′) (p. 6).
- **Joint eccentricity** — eccout_{p,X,Y}(s, t), the best Lp mismatch
  between the out-going weight profiles of s and t (eq. JE, p. 11).
- **Hubs and authorities** — the out-going and in-going readings of each
  invariant (Remark 22, p. 11).
- **Lipschitz and interleaving stability** — two kinds of control of an
  invariant by the distance (pp. 11, 13).

## Connections

It is the network generalization of Mémoli 2007 and 2011 (the lower bounds
and the distortion formulation) and of Sturm 2012 (gauged measure spaces,
symmetric L² weights; Remarks 2, 17 and 19). It calls itself "a theoretical
complement" to Peyré, Cuturi and Solomon 2016 (p. 3), whose entropic GW on
arbitrary matrices it justifies for asymmetric ones (§3, p. 10). That paper
is in the record as [LIT-tmpprsxm](../literature.d/LIT-tmpprsxm.md); its invariance result is
[THEORY-tmpa43ta](../theory.d/THEORY-tmpa43ta.md). Fused GW (Vayer et al., cited as [VCF+19]) is [LIT-tmpjs7kp](../literature.d/LIT-tmpjs7kp.md).
Its Gromov–Hausdorff-type predecessor is Chowdhury and Mémoli [CM17],
which it contrasts: the "tripod structure" of Theorem 18 is "much more
difficult to obtain" without measures (Remark 19, p. 9).

## Bearing on the record

- **[CLAIM-448](../claims.d/CLAIM-448.md) and [CASE-124](../cases.d/CASE-124.md): support, and a sharper form.** The distance
  is a comparison of records, and Theorem 18 says exactly what it cannot
  see: anything not written into ωX and µX. Two organizations whose
  recorded networks are weakly isomorphic are at distance zero however they
  differ in what was left out of the record. Three choices sit before the
  distance and belong to the legibility regime, not to the mathematics:
  which relations are measured into ωX; how missing entries are filled,
  since the framework needs ωX defined everywhere and "one needs to
  preprocess the data" (p. 4); and the node measure, which "the user
  adjusts" (p. 2). The directed case is what A7 wanted for influence,
  authority and obligation, and the paper supplies it with in- and
  out-going invariants, "hubs" and "authorities" (p. 11). It shows no case
  of two organizations, and gives no evidence about organizations at all.
- **A caution for any use of these invariants as evidence of alignment.**
  The lower bounds are one-sided. A small R-TLB does not show two networks
  are close. Two 3-node networks with uniform measure, ωX the cyclic shift
  (0 1 2; 2 0 1; 1 2 0) and ωY the symmetric Latin square
  (0 1 2; 1 2 0; 2 0 1), have every row and column a permutation of
  {0, 1, 2}, so TLB, FLB, SLB and the size bound are all zero in both
  directions. Yet the diagonal terms alone give disp² ≥ (0 + 4 + 1)/27 for
  p = 2, so dN,2 ≥ 0.215 (my construction and computation, not the
  paper's). The paper's experiments use the R-TLB as a "dissimilarity"
  (Fig. 5); its zeros are not evidence of sameness. For [CLAIM-448](../claims.d/CLAIM-448.md) this is a
  second way coherence can mislead: an agreement found by a cheap
  invariant can be the invariant's blindness.
- **[CASE-tmph0fxi](../cases.d/CASE-tmph0fxi.md):** its GW arm can compare response matrices that are
  not symmetric, such as utterances by probes, only once both are put as
  square weight functions on one node set; the paper's setting is a single
  node set per network. Co-optimal transport ([LIT-tmpbnbe3](../literature.d/LIT-tmpbnbe3.md)) is the form for
  rectangular matrices.
- **[QUESTION-tmp6byb6](../questions.d/QUESTION-tmp6byb6.md):** neutral. The distance compares whole networks;
  it gives no transports between parts and no holonomy.
- **No instruction for machine-learning practice.** The computational
  advice in §4.1 and Appendix A is about computing the paper's own
  quantities.

## Limitations

- **Only lower bounds are computed.** No experiment computes dN,p itself,
  and the bounds can be zero for networks at positive distance (above).
- **The experiments are illustrations.** Three datasets, no baseline
  method, no null model, no measure of cluster recovery. The migration
  reading is interpretation.
- **Completeness and the measure are assumed.** Missing weights must be
  imputed first (p. 4), and the node measure is the user's choice (p. 2).
- **The sphere bound is computed numerically** ("Through Matlab
  simulations", p. 16); I reproduced it on a grid.
- **Small slips:** the product measure is printed as µX(A)µX(B) for
  µX(A)µY(B) (p. 4); the left side of eq. (9) repeats ωX for Y (p. 24);
  Figure 6's caption calls the ten networks "Nodes 1-5" and "6-10".

## Open questions

- How large can the gap between the R-TLB and dN,p be on real network
  families, and is there a complete invariant cheap enough to use?
- The exact value of dN,∞(S¹, S²), or even of dN,2, is open (p. 15).
- For records with missing entries, how does the choice of imputation move
  the distance? The paper leaves it to preprocessing (p. 4).
