---
number: 26
status: Read
formerly:
- NOTE-tmpypyib
paper: LIT-020
title: 'Forman-Ricci curvature of networks'
version: 2
history:
- version: 2
  date: '2026-09-25'
  note: >-
    Read in full (full text of arXiv:1607.08654v2 (dated 18 Oct 2016; title
    page 19 Oct 2016), 29 pp.: abstract, §1–§5, acknowledgements and the
    reference list. Extracted with PyMuPDF from raw4/1607.08654.pdf (no
    pdftotext on this host). I checked Eqs. 11–13, 40–41 and 45–46 against
    page renders, because text extraction loses sum subscripts and bars.
    Figures 3–8 are plots and network drawings; I read their captions and
    the prose around them, not the images. Not read: the Supplemental
    Material (sampling, the EMD approximation, implementation, data sets).
    The paper defers model-network parameters, real-network sizes and code
    to it. The journal version (J. Complex Networks 5, 527–550, DOI
    10.1093/comnet/cnw030) was not compared.). Upgraded from `Skimmed` to
    `Read`: the claims table, assumptions and results are new, and the skim
    is corrected where the full text disagreed.
date: '2026-09-25'
summary: >-
  The paper specializes Forman's (2003) Bochner–Weitzenböck curvature on
  weighted CW complexes to graphs, giving the closed-form edge curvature
  Ric_F(e) = ω(e)[ω(v1)/ω(e) + ω(v2)/ω(e) − Σ_{e_v1∼e,
  e_v2∼e}(ω(v1)/√(ω(e)ω(e_v1)) + ω(v2)/√(ω(e)ω(e_v2)))] (Eq. 11). It then
  proposes three uses: an EMD distance between curvature distributions,
  which puts Facebook, Google and BioGrid graphs at 0.050–0.060 from a
  Barabási–Albert model against 0.17–0.36 from Erdős–Rényi and
  Watts–Strogatz (Table 1); a discrete "2-D-form" Ricci flow γ̃(e) − γ(e)
  = −Ric_F(γ(e))·γ(e) (Eq. 36) for change detection; and a Laplacian flow
  ∂G/∂t = (□₁ − F)G (Eq. 45) for denoising. The authors say the flow
  applications are "only theoretically proposed and illustrated solely on
  a small example" (§5).
---

<!-- inactive-ok-file: LIT-004 — Deferred; the Ollivier-side comparison in Connections, not yet read closely -->
<!-- inactive-ok-file: NOTE-006 — Skimmed; the only reading of the Ni et al. side so far, and named as such -->

# NOTE-026: Forman-Ricci curvature of networks

## Contribution

The paper writes Forman's combinatorial Ricci curvature (Forman 2003) out explicitly for weighted graphs (Eq. 11). It adds node and directed-edge variants (Eqs. 13–17) and a default weighting for unweighted data (Eqs. 19, 21). It proposes three things that did not exist in this form before: (i) an EMD distance between the curvature densities of two graphs, as a classification device (Eqs. 23–34); (ii) a discrete Forman–Ricci flow on edge weights modelled on the surface flow ∂g/∂t = −Kg (Eq. 36), with a normalized long-time variant (Eq. 41); and (iii) a "Laplacian flow" on edge weights built from the Forman decomposition □ = B + F (Eqs. 44–46). The flow for change detection first appeared in the authors' own ICICS 2016 paper (arXiv:1604.06634), which this one reviews and extends (§4.3). The observation that curvature distributions of real networks resemble Barabási–Albert repeats Sreejith et al. 2016a/b (§3.2, §5).

## Key insight

Forman's curvature comes from an algebraic identity rather than a transport problem. The Bochner–Weitzenböck formula □_p = ∂∂* + ∂*∂ = B_p + F_p on a weighted cell complex has a canonical split into a non-negative "rough Laplacian" B_p and a diagonal F_p (Eq. 5), and the diagonal entry on 1-cells is the Ricci curvature. On a graph it therefore depends only on the edge's own weight, its two endpoints' weights and the weights of the edges adjacent to it (Eq. 11). It is local, closed-form and cheap. The same construction yields a matching Laplacian, so a curvature-driven flow and a Laplacian flow come as a pair (§4.4, "duality"). The authors' heuristic is that the Ricci flow picks out a network's "backbone" (sharp curvature changes), while the Laplacian flow averages. Both of these are stated effects, not demonstrated ones.

## Assumptions

- **Setting.** A graph is a 1-dimensional regular CW complex, so edges have "children" (nodes) but no "parents" (faces). This kills half the terms of the general formula, Eq. 9 (§2.3, p. 6–7). Higher cells (triangles, cliques) are explicitly left to "a forthcoming article" (p. 7). The curvature here therefore sees no triangles or cycles.
- **Weights positive, and ideally "standard".** Forman's weights are positive (p. 7). Eq. 9 is derived for standard weights w(α_p) = w₁·w₂^p (Eq. 8). The Remark on p. 6 defends applying it to arbitrary data weights by appeal to Forman's Theorem 2.5: for an open, dense set of weights the required property holds, so there are standard-compatible weights "arbitrarily close". This is an approximation argument, and it is not quantified.
- **Default weights (used when data give none).** Node weight ω(v) = (1/deg v)·Σ_{u∼v} deg(u), the mean neighbour degree (Eq. 19). It is declared as a map V → [0,1] (Eq. 18), so it must be normalized somehow, but no normalization is given. Edge weight γ(e_ij) = sign(e_ij)·√(ω(v_i)² + ω(v_j)²), with sign = +1 if i ≤ j and −1 otherwise (Eqs. 21–22). This contradicts the declared range γ: E → [0,1] (Eq. 20) and Forman's positivity requirement. It also makes √(ω(e)ω(e_v)) in Eq. 11 imaginary for mixed signs. The paper does not reconcile these.
- **Directed graphs.** Handled by splitting Eq. 11 into its v₁ and v₂ halves and keeping only one (Eq. 14, following Sreejith et al. 2016b). The convention, "incoming edges at the head and the outgoing ones at the tail where directions are defined from head to tail" (p. 8), is stated as a choice.
- **Flow form.** The paper adopts the 2-D form (Eq. 36) rather than the "proper" 3-D form (Eq. 38). It gives four reasons: computability; consistency with Chow–Luo and with Ollivier–Ricci flow; graphs being "almost 2-dimensional"; and instability of Eq. 38 in image experiments (Sonn et al. 2014). Time is discrete with unit clock (p. 16).
- **Metric structure not assumed.** The Remark on p. 18 concedes that the weights define a distance only on a node's star. It says that a long-time flow with geometric meaning would need, for example, the induced path metric. Only the short-time flow is used.
- **Denoising model.** The observed weights are γ̃ = γ + dt·dW with small Gaussian white noise; noise affects edge strengths but not edge existence; and the correction term is small relative to the weights. Only the short-time flow is used (Eqs. 50–52, p. 21–22).
- **Sign convention.** The paper declares "+" in the definitions of both the Laplacian and the Ricci flow, against Riemannian convention (Remark, p. 19). Its displayed Ricci-flow equations (35–38, 40, 49) nonetheless carry "−". See Limitations.

## Key results

The paper has no theorems. Its results are definitions and small computations.

- **Forman–Ricci curvature of an edge e = (v₁, v₂)** (Eq. 11, p. 7, verified against the page render):
  Ric_F(e) = ω(e) · ( ω(v₁)/ω(e) + ω(v₂)/ω(e) − Σ_{e_{v₁}∼e, e_{v₂}∼e} [ ω(v₁)/√(ω(e)ω(e_{v₁})) + ω(v₂)/√(ω(e)ω(e_{v₂})) ] ).
  Here ω(e) is the edge weight, written γ(e) elsewhere in the paper, and ω(v) is the node weight. The sum runs over edges adjacent to e, at v₁ and at v₂ respectively. The subscript is printed as a single Σ with two stacked conditions and does not state that e itself is excluded. That reading is standard, and it is my inference. With all weights 1 it gives the familiar 4 − deg(v₁) − deg(v₂). That substitution is mine; the paper does not state it.
- **Bochner Laplacian on edges** (Eq. 12): □₁(e₁, e₂) = Σ_{e₁∼v, e₂∼v} ω(v)/√(ω(e₁)ω(e₂)). The diagonal form, used for the flow, is □₁(e) = Σ_{e∼v} ω(v)/γ(e) (Eq. 46). Eq. 12 is introduced as "Analogously to (2.8)", but there is no Eq. 2.8. The general parent form is Eq. 10.
- **Node curvature** F(v) = Σ_{e_v∼v} F(e_v) (Eq. 13). **Directed variants** are Ric_{F,I}(v) = Σ_{e∈E_{I,v}} Ric_{F,I}(e) and Ric_{F,O}(v) = Σ_{e∈E_{O,v}} Ric_{F,O}(e) (Eqs. 15–16), with the net "flow through a node" Ric_{F,I/O}(v) = Ric_{F,I}(v) − Ric_{F,O}(v) (Eq. 17).
- **Forman–Ricci flow, 2-D form** (Eq. 36, §4.1): γ̃(e) − γ(e) = −Ric_F(γ(e))·γ(e). The discretized version is taken from the surface flow ∂g_ij/∂t = −K(g_ij)·g_ij (Eq. 35) via Chow–Luo.
- **3-D form, rejected** (Eq. 38): γ̃(e) − γ(e) = −Ric_F(γ(e)), from ∂g_ij/∂t = −Ric(g_ij) (Eq. 37).
- **Reverse flow** (Eq. 39): ∂γ(e)/∂t = +Ric_F(γ(e))·γ(e). The paper calls Eq. 36 "an ODE and therefore reversible" and suggests the reverse flow for adding noise or sharpening.
- **Normalized Forman–Ricci flow** (Eq. 41, verified against the render): ∂γ(e)/∂t = (Ric_F(γ(e)) − \overline{Ric_F})·γ(e). This is offered "by analogy with" ∂g_ij/∂t = −(K − K̄)·g_ij (Eq. 40), but Eq. 41 has no leading minus. \overline{Ric_F} is not defined for networks (Eq. 40 defines K̄ as an area-weighted mean). It is not used in any experiment.
- **Iterated flow for change detection** (Eq. 49, §4.3): γ^{k+1}_{i,i+1}(e) = γ^k_{i,i+1}(e) − Δt·Ric_F(γ^k_{i,i+1}(e))·γ^k_{i,i+1}(e), for k = 1…K, applied to each snapshot's weights. The snapshots' evolved weights are then compared by thresholded correlation (as in the ICICS paper) or, as here, by the L1 distance between aligned edges.
- **Laplacian flow** (Eqs. 44–45): ∂G/∂t = Δ¹_F G = (□₁ − F)G. By Eq. 5 (□ = B + F), this is the rough Laplacian B₁. The paper labels both □₁ (Eqs. 12, 46) and B_p (Eq. 5) as "the Bochner Laplacian".
- **Denoising step** (Eq. 52): γ ≈ γ̃ − dt·Δ¹_F(G).
- **Curvature distance** (Eqs. 23–34): kernel density f_G(e) = (1/|ê|)·Σ_{ê∼e} K(Ric_F(e) − Ric_F(ê)) over edges ê parallel to e (Eq. 24). Its support is binned into k clusters with representatives and weights (Eqs. 27–30), a ground distance matrix is formed (Eq. 31), and EMD = Σ f_ij d_ij / Σ f_ij is taken at the optimal flow (Eq. 34), "computed by the Hungarian algorithm".
- **Table 1** (p. 14). Model networks have ≈20,000 nodes each; the real networks' sizes are in the Supplement, which I did not read.

  | network | d_AB | d_WS | d_ER |
  |---|---|---|---|
  | Facebook | 0.0495 | 0.3315 | 0.2706 |
  | Google | 0.0546 | 0.3581 | 0.2910 |
  | BioGrid | 0.0604 | 0.2238 | 0.1688 |

  Between real networks: d(F,G) = 0.0565, d(F,B) = 0.0086, d(G,B) = 0.1131.
- **Fig. 7.** Change detection on two Gnutella snapshots, labelled "August 4 and August 5 2012", with K = 10 and threshold 0.1. It is qualitative only. The cited source (Ripeanu et al. 2002) and the SNAP Gnutella collection suggest the year is 2002. That is unverified from the text; 2012 may be a typo.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | On a 1-D complex (graph), Forman's F₁ reduces to Eq. 11 | moderate | Specialization of Forman's Eq. 9 by dropping parent terms (§2.3). The derivation is short and standard, but the paper does not write it out, and Eq. 9 itself is quoted from Forman 2003, not derived. |
| C2 | Eq. 9 applies to arbitrary positive data weights, not only standard weights | weak | Appeal to Forman 2003 Thm 2.5 (open dense set of admissible weights). The size of the resulting error is asserted to be imperceptible ("without any perceivable computational error", p. 6), not bounded. |
| C3 | Real networks' Forman curvature distributions most resemble Barabási–Albert | moderate (for these 3 networks) | Table 1 and Fig. 3, with three real networks and one sample per model. Agrees with Sreejith et al. 2016a/b. No variance across model samples and no sensitivity to binning or kernel are reported. |
| C4 | Erdős–Rényi is closer than Watts–Strogatz to real networks under this distance | weak | Table 1 only. Model parameters are in the Supplement. The paper flags it as surprising and does not probe it. |
| C5 | Distances among the real networks are "approximately of the same order" | contradicted by own data | Table 1: 0.0086 to 0.1131. |
| C6 | Hubs and their communities carry high curvature, which explains the AB resemblance | informal argument | §3.2, p. 13, "Our results suggest". No per-edge analysis. It also sits uneasily with Eq. 11, where degree enters with a negative sign. |
| C7 | Curvature maps reveal community structure and directionality | assertion | Fig. 4. The construction of a "curvature map" is not defined in the main text (presumably it is in the Supplement). |
| C8 | Forman and Ollivier curvature are "closely interrelated"; Forman is much cheaper | assertion | §1, §5. Deferred to "a forthcoming study". The cheapness follows from Eq. 11 being local and closed-form, but no timing is given. |
| C9 | The 2-D flow form (Eq. 36) is more stable than the 3-D form (Eq. 38) on networks | informal argument | Image experiments of Sonn et al. 2014, extrapolated ("we must expect", p. 17). No network experiment. |
| C10 | The Forman–Ricci flow detects "interesting", fast-evolving regions | weak | One qualitative figure on one Gnutella snapshot pair (Fig. 7). No ground truth, no baseline, no metric. |
| C11 | The Laplacian flow denoises network edge weights | weak | A schematic figure on Zachary's karate club (Fig. 8) and "preliminary … promising results" with no numbers (p. 22). |
| C12 | Each flow is poorly suited to the other's task (Laplacian too smoothing for change detection) | assertion | "Computational experiments … yielded less promising results" (§4.4, p. 23). No data. |
| C13 | Forman–Ricci curvature has no Gauss–Bonnet-type theorem, which blocks a well-defined long-time (gauge) flow | assertion (acknowledged limitation) | §5, item 3. A remedy is promised in a forthcoming article. |
| C14 | The Forman–Ricci flow is a "true Ricci flow" while the Ollivier–Ricci flow at nodes is a scalar flow | assertion | Remark, p. 16, citing Sandhu et al. 2015a. |

## Method

1. **Weights.** Take node weights from the data, or use Eq. 19. Take edge weights from the data (for example, correlations), or use Eq. 21.
2. **Curvature.** Compute Ric_F(e) per edge (Eq. 11), or the directed halves (Eq. 14), and aggregate to nodes if wanted (Eqs. 13, 15–17).
3. **Graph comparison.** Estimate the density of the curvature values (Eq. 24), bin its support to match the histogram, and compute the EMD between the binned signatures (Eqs. 31–34). The Supplement (unread) mentions approximating EMD by total variation.
4. **Change detection** (§4.3 workflow, p. 20). Compute Ric_F for snapshots G_i and G_{i+1}, normalize both weightings, and run K iterations of the discrete flow on each. Then align the edges and threshold the L1 difference of the evolved weights. For the form of the update, see correction 1: Eq. 49 and step 3 disagree.
5. **Denoising.** Take γ ≈ γ̃ − dt·(□₁ − F)G with □₁ from Eq. 46. This is one short step, assuming small noise on edge strengths only.

## Concepts

- **Forman–Ricci curvature, Ric_F(α).** The diagonal curvature term F₁ in the combinatorial Bochner–Weitzenböck decomposition □₁ = B₁ + F₁ on 1-cells (Eqs. 5–7). The paper reads it geometrically as capturing *volume growth*, the second-order term of Eq. 1, rather than geodesic dispersion (p. 3). This is an interpretive claim.
- **Standard weights.** w(α_p) = w₁·w₂^p (Eq. 8), generalizing length, area and volume. Combinatorial weights ≡ 1 are standard.
- **Parallel cells.** Cells that share a parent or a child, but not both (p. 6, Fig. 2). On a graph with no 2-cells, two edges are parallel iff they share a node. Eq. 24's KDE runs over parallel edges.
- **Bochner (rough) Laplacian.** In Eq. 5 this is B_p, the non-negative part. In Eqs. 12 and 46 the same name is attached to □₁. Readers should treat the name as ambiguous in this paper.
- **Forman–Ricci flow.** The discrete-time evolution of edge weights proportional to minus curvature times weight (Eq. 36). The authors call it a "true Ricci flow" because it is driven by edge (Ricci) curvature, not node (scalar) curvature (p. 16).
- **Backbone effect.** The authors' name for the Ricci flow's supposed tendency to highlight regions where curvature changes sharply (§4.4). It is named, not measured.
- **Averaging effect.** The Laplacian flow's smoothing, carried over from heat-equation intuition and imaging practice (§4.4).
- **Gauge network.** The hypothetical constant-curvature limit of a normalized long-time flow, analogous to the uniformization target of the surface Ricci flow (§4.1, §5). Not constructed here.
- **Curvature map.** A 2-D representation of curvature by network region, said to show community structure and directionality (Fig. 4). The construction is not specified in the main text.

## Connections

- **Forman 2003** (Bochner's method for cell complexes) is the entire mathematical basis: Eqs. 5–10 are quoted from it. **Sreejith et al. 2016a/b** introduced Forman curvature for undirected and directed networks first. This paper cites them for the directed form (Eq. 14) and for the scale-freeness correlation. Its own additions are the flows, the EMD distance and the Laplacian-flow pairing. The Forman–Ricci flow's first appearance is **Weber, Jost & Saucan 2016** (ICICS; arXiv:1604.06634), which §4.3 extends.
- **Chow & Luo 2003** (combinatorial Ricci flow on circle-packed surfaces) is the template for the 2-D form γ̃ − γ = −Ric·γ.
- **Relation to Ni et al., "Community Detection on Networks with Ricci Flow"** (arXiv:1907.03993, [LIT-004](../literature.d/LIT-004.md); skim [NOTE-006](NOTE-006.md)). Both papers run a discrete Ricci flow on edge weights, but on different curvatures. This paper uses Forman's combinatorial curvature, which is local and closed-form in the weights of the edge, its endpoints and the adjacent edges (Eq. 11). Ni et al. use Ollivier's curvature κ_xy = 1 − W(m_x, m_y)/d(x, y), which needs an optimal-transport (Wasserstein) solve per edge (per [NOTE-006](NOTE-006.md)). The update rules are close cousins. Here γ̃ = γ − Ric_F·γ (Eq. 36). Ni et al. use w_xy ← d(x,y) − κ_xy·d(x,y) (per [NOTE-006](NOTE-006.md), from a skim), which has the same "2-D form" shape with curvature times current length. This paper names that shared form explicitly: "this approach is also adopted in defining the only other established Ricci-type flow for networks, namely the Ollivier-Ricci flow", chosen "allowing for consistency between and comparison of the two flows" (p. 16). It cites the 2015 Ni et al. INFOCOM paper on internet topology, not the 2019 community-detection paper, which it predates. The link between the two curvatures is only asserted here (C8), and its caveat about Forman's locality (§5: "defined only for edges", with order-k neighbourhood graphs as a workaround) is the natural point of difference with an optimal-transport curvature. On community structure: this paper only *proposes* curvature-based clustering (§5, item 4) and shows curvature maps (Fig. 4). Ni et al. make community detection the application, with flow plus surgery. Nothing in this text establishes that the Forman flow would do what Ni et al. report for Ollivier's; whether it does is an open question, not a result.
- **Ollivier 2009/2010**, with the network uses in Sandhu et al., Ni et al. 2015 and Li et al. 2014, is positioned as the better-studied alternative (§1, §5).
- **Imaging precedents** (Appleboim–Saucan–Zeevi 2012; Sonn et al. 2014) are the source of both the Laplacian-flow denoising idea and the argument that the 3-D form is unstable.

## Bearing on the record

For nucleation, this paper is the definitional source for Forman–Ricci curvature on graphs and for the Forman–Ricci flow. Filed as [LIT-020](../literature.d/LIT-020.md), it should be cited for Eq. 11 and Eq. 36, not for its empirical or application claims. None of its uses are demonstrated beyond one table or figure. If any nucleation document cites it as showing that Forman and Ollivier curvature agree, it does not show that (C8). The same goes for citing it as showing that Ricci flow denoises or detects change in networks (C10, C11). The companion [LIT-004](../literature.d/LIT-004.md) (Ni et al. 2019) is the place where a Ricci flow is actually benchmarked, with Ollivier curvature.

For ML practice: the paper itself carries no instruction. The skim's link is historical. Discrete curvatures, Forman variants and Ollivier's among them, were later used to diagnose over-squashing and guide rewiring in graph neural networks, but that work is later and is not in this text. Eq. 11 (unweighted: 4 − deg v₁ − deg v₂, without triangle terms) is the plain, pre-"augmented" form. Later GNN work typically uses versions that add cycle and triangle terms, which this paper explicitly defers (p. 7). So this paper would be the wrong source for a practice built on those versions. Nothing here warrants an ANTH- document.

## Limitations

- **No theorem.** Every result is a definition or a small computation. The mathematical content is Forman's; the new parts (flows, distance) come with motivation but no properties proved: no convergence, stability, or invariance.
- **Internal inconsistencies in the formulas that define the method:**
  - the workflow in §4.3 contradicts Eq. 49 (correction 1);
  - Eq. 41 has the opposite sign to the Eq. 40 it claims to imitate;
  - the p. 19 Remark declares a "+" convention that Eqs. 35–38 and 49 do not follow;
  - Eq. 21's signed weights contradict Eq. 20's range and Forman's positivity requirement;
  - Eq. 18's [0,1] range is not achieved by Eq. 19 without an unstated normalization;
  - Eqs. 25–26 misname an L^p density distance as Wasserstein;
  - Eq. 12 cites a non-existent "(2.8)", as does p. 8;
  - "Bochner Laplacian" names two different operators;
  - §5 places the curvature maps in "section two" (they are in §3).
- **Small empirical base.** Three real networks, one sample per model, and the model parameters and real-network sizes are in the Supplement (not read). The flows are shown on one snapshot pair and one toy graph, with no quantitative evaluation. The authors concede this in §5.
- **The headline claims outrun the body.** The abstract says the work "suggests a number of applications … including denoising and clustering … as well as extrapolation of network evolution". The body proposes clustering and extrapolation without testing them (§5, items 3–4), and denoising has only schematic support.
- **Scope of the curvature.** On a 1-complex the curvature ignores triangles and cycles, so it is essentially a degree-and-weight statistic of the edge's neighbourhood. That is relevant to how independent it really is of the "node-degree-based" measures it is meant to complement, which the paper itself acknowledges only partly (p. 8: "Even if curvature cannot be assumed independent of node degrees…").
- **Acknowledged by the authors:** no Gauss–Bonnet theorem, hence no well-defined long-time or gauge flow (§5). Weights are not a metric beyond node stars (p. 18). Forman curvature is defined only on adjacent pairs, unlike Ollivier's (§5).

## Open questions

- **Forman versus Ollivier.** How closely do they agree on real networks, and in what regime? The paper promises "a forthcoming study". That comparison, not this paper, settles C8.
- **Stability.** Is the discrete flow of Eq. 49 stable, and with what Δt and K? Does the 2-D form actually avoid the singularities attributed to the 3-D form on networks (C9)?
- **Long-time flow.** Can a long-time normalized Forman–Ricci flow with a well-defined gauge target be constructed without a Gauss–Bonnet theorem? The authors promise a remedy in a later article.
- **Benchmarks.** Does change detection or denoising with these flows beat simple baselines (raw weight differences; plain graph-Laplacian smoothing) on data with ground truth? The result that would settle it is a labelled benchmark.
- **Community detection.** Does a Forman–Ricci flow with surgery recover communities as the Ollivier-based flow of Ni et al. is reported to? This paper proposes curvature-based clustering but does not test it.

## Corrections to the seeded skim

- The dossier says the paper "defines a discrete Forman-Ricci flow update γ̃(e) − γ(e) = −Ric_F(e)γ(e) and uses it for change detection". The definition is right (Eq. 36), but the paper uses two different forms of the flow. The iterated update in §4.3 (Eq. 49) is γ^{k+1} = γ^k − Δt·Ric_F(γ^k)·γ^k, which matches Eq. 36. Step 3 of the stated workflow (p. 20), however, drops the weight factor: γ^{k+1}_{ij} = γ^k_{ij} − Δt·Ric(γ^k_{ij}). That is the "3-D" form Eq. 38, which §4.1 had just rejected as unstable. The text does not say which one produced Fig. 7.
- The dossier's summary says the flows "can be used for change detection and denoising". The paper claims less. Change detection is one Gnutella snapshot pair (Fig. 7; K = 10, L1 threshold 0.1), with no ground truth and no metric. Denoising is Fig. 8, whose caption says "we highlight the averaging effect schematically", plus an unquantified sentence: "First (preliminary) computational tests … showed promising results" (p. 22). §5 itself says "only theoretically proposed and illustrated solely on a small example".
- The dossier's "curvature-based graph distance … (§3.1–3.2, Eqs. 30–34)" should be Eqs. 23–34 (KDE, Eqs. 23–24; binning, Eqs. 27–30; ground distance, Eq. 31; transport, Eqs. 32–34). The dossier also passes the paper's framing through unchecked. Eqs. 25–26 call ‖f_G1 − f_G2‖_{L^p} a "Wasserstein-distance", but that is an L^p distance between densities, not a Wasserstein distance. The EMD actually computed (Eq. 34) is a genuine transport distance. The two are different objects.
- The dossier's "Erdős–Rényi fits closer than Watts–Strogatz" is correct (Table 1; the paper calls it "Surprising", p. 13). It omits that the real networks are closer to *each other* than to AB in one case: d(Facebook, BioGrid) = 0.0086, against 0.0495 and 0.0604 to AB. The caption's claim that inter-real distances are "approximately of the same order" does not survive its own numbers: 0.0086, 0.0565 and 0.1131 span more than an order of magnitude.
- The dossier says Forman is "closely correlated" with Ollivier per the authors. The paper's wording is "strong theoretical indications that the two approaches are closely correlated" (§1) and "closely interrelated (as we shall shortly show in a forthcoming study)" (§5). No argument or evidence for this is given in this paper.
