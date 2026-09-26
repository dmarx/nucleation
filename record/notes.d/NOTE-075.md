---
number: 75
status: Read
formerly:
- NOTE-tmpsznzu
paper: LIT-069
title: 'Surface optimization in physical networks'
version: 2
history:
- version: 2
  date: '2026-09-25'
  note: >-
    Read in full (I read the full text of the Nature article: 9 PDF pp.
    (Nature 649, 315–322, 8 Jan 2026), covering the main text, Figs 1–5 with
    captions, refs 1–56, Data/Code availability and the author and
    peer-review statements. The article has no separate Methods section; the
    Supplementary Information does that job. I also read the full SI: 49 pp.
    (MOESM1, "September 19, 2025"), covering §1 datasets and
    skeletonisation, §2 Steiner, §3 charts, §4 atlas and quadratic
    differentials, §5 surface minimisation, §6 the numerical scheme, §7
    empirical branching, §8 lengths and loops, §9 node morphology, §10
    surface versus volume, and refs [1]–[36]. Text was extracted with
    PyMuPDF from raw4/c53.pdf and raw4/c53_SI.pdf, since this host has no
    pdftotext. Figure panels came through only as tick labels and numbers. I
    read the numbers printed in the figures (Fig. 1d degree counts, Fig. 3
    P(λ→0) values, Fig. 4 ρ_th values, SI Figs 5 and 13–20 and Table 4) and
    recomputed the per-dataset degree shares. I did not inspect the rendered
    plots. I did not run min-surf-netw, and I did not open the
    physical.network dataset.). Upgraded from `Skimmed` to `Read`: the
    claims table, assumptions and results are new, and the skim is corrected
    where the full text disagreed.
date: '2026-09-25'
summary: >-
  The degree counts in Fig. 1d show k = 4 nodes making up 4.6–17.7% of
  branch points across the six datasets. The pooled 16.6% is 96%
  human-neuron nodes. Bifurcation angles also fail to peak at 2π/3. From
  this the authors infer that local branching minimises sleeve surface
  area under a minimum circumference w, not wire length. For a regular
  tetrahedron their numerical minimiser merges two bifurcations into a
  trifurcation at χ = w/r ≈ 0.83, and a thin branch sprouts orthogonally
  below ρ = w′/w ≈ 0.6. Per-dataset empirical thresholds are ρ_th =
  0.52–0.92. The "exact mapping" to string-theory worldsheets covers only
  the unconstrained minimal-area problem. The SI says the implemented
  method yields surfaces that are only locally area-minimising (§5).
---

<!-- inactive-ok-file: LIT-069 — Deferred: the paper is placed by this reading; the directive lapses when its status changes -->

# NOTE-075: Surface optimization in physical networks

## Contribution

The paper makes three contributions.
- **Data.** It assembles six classes of 3D physical tree networks:
  - human neurons (the H01 petavoxel sample)
  - three Drosophila hemibrain neurons
  - one human pulmonary arterial tree
  - 29 tropical trees
  - 28 corals
  - 5 Arabidopsis plants at 10 time points

  It measures their local branching statistics against the three local rules of the Steiner tree: degree 3 only, planar bifurcations, and 120° angles. It reports systematic departures from all three.
- **Model.** It proposes that links should be modelled as smooth tubular "sleeves" whose total surface area is minimised, subject to every link keeping a circumference of at least w (main text Eqs 1–2).
- **Numerical solver.** It releases a solver (min-surf-netw) built on quad-mesh isometric optimisation. For symmetric test motifs the solver produces two predictions, both confirmed qualitatively in the data:
  - a bifurcation-to-trifurcation transition at χ = w/r ≈ 0.83;
  - a branching-to-sprouting transition at ρ = w′/w ≈ 0.6.

## Key insight

A wire of zero thickness can only split at a point, and splitting into three at one point is never length-optimal. A tube of finite thickness must blend smoothly into its neighbours, and the blending costs surface area. When tubes are thick relative to their separation, two nearby junctions cost more area than one merged junction, so a trifurcation becomes optimal. When one branch is much thinner than the other two, keeping the thick pair straight costs nothing extra at the junction, so the thin branch leaves at a right angle. The characteristic scale is the ratio of thickness to distance (χ) or of thin to thick (ρ). Length minimisation has no such scale.

## Assumptions

- **Topology.** The network is a tree: the model "predicts straight, uniform cylinders far from the branching points" and cannot handle loops (p. 320; SI §8).
- **Cost.** The cost is the surface area S = Σᵢ ∫ d²σ √det γᵢ (Eq. 1). Volume is not optimised. The authors concede that for neurons, corals and trees "an accurate accounting of the material cost must also consider the volume" (p. 321).
- **Constraint.** The functional constraint is ∮ dl ≥ w, the "systole", on every non-contractible loop (Eq. 2). In the implementation it is enforced as a local condition e^{2ϕ} ≥ 1 on a flat reference metric, so sleeves may only stretch (SI Eq. 32).
- **Boundary conditions.** Each terminal is a freely rotatable circle of radius w/2π, sewn to its sleeve (SI §5).
- **Solution concept.** A local minimum from gradient-based optimisation of a penalised objective, started from the Steiner layout and annealed in w_fair (SI §6, Eq. 42). It is not a global minimum over topologies.
- **Theoretical motifs.** Only highly symmetric motifs are solved:
  - a regular tetrahedron: 5 links, w = 50 tiles;
  - three links of length 24 with w₁ = w₂ = 50 tiles and w′ varied.
- **Empirical skeletons.** Skeletons come from heterogeneous pipelines (SI Table 1):
  - VAST (human neurons);
  - self-implemented TEASAR (fly);
  - QSM (trees);
  - Kimimaro with dataset-specific parameters (vessel, coral, Arabidopsis; SI Table 2).

  Degree counts then apply the merging rule l_int ≤ w/2π (SI Eq. 43).

## Key results

- **Steiner-rule violations (Fig. 1d–f).**
  - k = 4 shares, per dataset: human 17.0%, fly 6.5%, vessel 8.3%, tree 17.7%, coral 8.7%, Arabidopsis 4.6%. There are also k = 5 and k = 6 nodes.
  - P(θ) has no peak at 2π/3 in any dataset.
  - P_Bi(Ω) peaks near, but below, 2π.
- **Trifurcation transition (Fig. 3g; SI Fig. 13).** For a regular tetrahedron, λ = l/w drops sharply to 0 at χ ≈ 0.83. Steiner gives λ_Steiner ≈ 0.212 χ⁻¹. The fitted form is λ ≈ (0.212/χ) f((0.212 − 0.26χ)/(χσ)) (SI Eq. 45).
- **Empirical P(λ → 0) > 0 in all six datasets (Fig. 3i–n).** Printed values: 0.276, 0.673, 0.601, 2.130, 1.150, 0.629. The human-neuron value, 0.276, is confirmed in SI Fig. 5b. The SI's own threshold estimate, from l_int ≈ A(l_ext − Bw) with B = 0.67–1.99 (mean 1.41), gives χ ≥ 0.67, which the authors call "close to" 0.83 (SI p. 35).
- **Sprouting transition (Fig. 4g; SI Fig. 19).**
  - Theory: Ω₁→₂ = 0 for ρ < ρ_th ≈ 0.6, and Ω₁→₂ ≈ k(ρ − ρ_th) above. A plain-cylinder model (Zamir) instead gives a gradual approach to 90° only as ρ → 0.
  - Empirical breakpoints, chosen per dataset to maximise the slope jump Δs: human 0.56, fly 0.52, vessel 0.83, tree 0.52, coral 0.92, Arabidopsis 0.73.
  - The slope jump is Δs > 0 in all six datasets, ranging from 2×10⁻³ (tree) to 2.3×10⁻¹ (vessel) (SI Table 4).
  - The Spearman correlation between Ω and ρ is 0.44–0.72.
- **Prevalence of sprouts.** Among bifurcations with w₁ ≈ w₂, sprouts make up 25.6% (vessel), 12.9% (tree), 52.8% (coral), 11.2% (Arabidopsis), 13.8% (fly) and 18.4% (human). In the human data there are 4,003 sprouts, and 3,911 (97.7%) end on a synapse (text) — the Fig. 4h caption says 92%.
- **Excess length.** Real double-bifurcation motifs are η = L/L_Steiner = 1.20–1.35 times the Steiner length (mean ≈ 1.25 ± 0.05; SI Table 5).
- **Node shape (SI §9).** Surface area over the one-parameter family of Jenkins–Strebel trifurcations is minimised at a = b = c = w/3. In the blood-vessel data, 26 trifurcations "tend to cluster near the centre" of the (ã, b̃, c̃) triangle (SI Fig. 23e). No statistic is reported.
- **Surface versus volume (SI §10).** For one double-bifurcation motif with χ > 0.83, both area (112→115) and volume (60.0→60.6, smoothed with a 5-point moving average) rise as λ is forced from 0 to 0.04.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Real physical trees contain a substantial fraction of k ≥ 4 nodes, contrary to Steiner/volume rule 1 | moderate | Fig. 1d counts. However, k = 4 is partly produced by the merging rule (SI Eq. 43), and the "roughly 15%" is a pooled figure dominated by human neurons |
| C2 | Bifurcation angles are not concentrated at 2π/3 | moderate | Fig. 1f; SI §7.3 |
| C3 | Bifurcations are non-planar | weak | Fig. 1e. The SI says the peak is "close to" 2π; strong non-planarity is shown only for trifurcation trios (SI Fig. 16b) |
| C4 | Surface minimisation under a systole maps exactly onto Nambu–Goto worldsheets / pants decomposition | weak (as stated) | The mapping is exact only for the abstract minimal-area problem (Strebel). The embedded, smooth problem is solved by a local, penalised relaxation (SI §5–6) |
| C5 | For a regular tetrahedron, thickening links drives a bifurcation→trifurcation transition at χ ≈ 0.83 | moderate | Numerical optimisation of one symmetric motif, locally minimising (SI §6, Fig. 13). There is no convergence or mesh-sensitivity study beyond the runtime plot |
| C6 | Surface minimisation predicts P(λ → 0) > 0 for random terminals | weak | Not computed. It is an extrapolation of the tetrahedral sigmoid (SI Eqs 44–45) to random configurations |
| C7 | Empirical P(λ) shows the surface-minimisation fingerprint in all six datasets | weak | Fig. 3i–n. The Steiner comparison is proxied by external legs; merged trifurcations may enter at λ = 0; coral contradicts the stated internal/external pattern (SI Fig. 14e); the alternative skeletoniser changes P(λ→0) 4.3× |
| C8 | Sprouting (Ω = 0) is optimal for all ρ < ρ_th ≈ 0.6, a sharp rather than gradual transition | moderate (theory) / weak (data) | Theory: SI Fig. 19 simulations. Data: the breakpoint is chosen per dataset to maximise Δs, with no null model. The tree Δs = 0.002. The below-threshold exponent 1 is what any constant nonzero Ω would give |
| C9 | Orthogonal sprouts are common in all six systems and functional in neurons (≈98% end on synapses) | moderate | Counts on p. 319. The sprout definition used for the synapse count is not given, and the caption and text disagree (92% vs 98%) |
| C10 | Local surface minimisation is a "stereotypical principle that is not overwritten by functional or global need" | assertion | Discussion, p. 320. It is inferred from qualitative agreement, and the same paragraph concedes that real motifs are ≈ 25% longer than Steiner |
| C11 | Real trifurcations favour the symmetric (minimal-area) junction geometry | weak | 26 blood-vessel trifurcations; a qualitative cluster; configurations with ã + b̃ < w̄/2 excluded a priori (SI §9.2) |
| C12 | Minimal surfaces are close to minimal volume | weak | One motif, λ ∈ [0, 0.04], with a smoothed volume curve (SI Fig. 24) |
| C13 | Results are insensitive to skeletonisation and resolution | weak | One alternative method on one dataset; a large P(λ→0) difference is called "fully consistent"; the resolution claim is asserted (SI §1.2) |

## Method

The pipeline has five steps.
1. **Represent the network as a manifold.** Each link is a chart X_i(σ⁰, σ¹) with longitudinal σ⁰ ∈ [0, l_i] and periodic azimuthal σ¹ ∈ [0, w_i]. Charts are sewn along boundary arcs with matching positions and first derivatives (SI Eq. 7). In isothermal coordinates γ_i = e^{2ϕ} δ, so the area is ∫ e^{2ϕ} d²σ (SI Eqs 13–16).
2. **Show a global atlas exists.** This uses Jenkins–Strebel quadratic differentials on an M-punctured sphere: q(z) = C Πₘ(z − pₘ)⁻² Πₙ₌₁^{2M−4}(z − sₙ), which has M − 3 free complex parameters (SI Eq. 29). The M = 3 case corresponds to a bifurcation, and M = 4 (one free parameter, a = d, b = e, c = f = w − a − b) to a trifurcation.
3. **Solve numerically.** The solver discretises the surface as a quad mesh whose Varignon parallelograms are constrained to rhombi. It minimises E = w_iso E_iso + w_glue E_glue + w_terminal E_terminal + w_fair E_fair + w_surface E_surface. The weights are w_iso = 1, w_glue = w_terminal = 10³ and w_surface = 10⁻³ (tetrahedron) or 10⁻² (bifurcation). w_fair is annealed from 10⁰ to 10⁻⁵ over 3×10⁴ iterations, then held for 10⁵ more. The conformal factor 1 + Δλ² ≥ 1 enforces the systole. Runtime is linear in the tile count R, which ranges from 5×10³ to 4×10⁴.
4. **Extract empirical statistics.** From the skeletons the authors extract degree counts (after merging), solid angles, steering angles Ω₁→₂ = 4π sin²((π − θ)/4), and circumference ratios. The ratios use bifurcations whose two main systoles differ by ≤ 10%, and exclude 0.99 ≤ ρ ≤ 1.01.
5. **Fit.** A generalised-gamma fit (SI Eq. 46) extrapolates P(x → 0). Two linear fits with a breakpoint chosen to maximise Δs give ρ_th.

## Concepts

- **Physical network manifold M(G)**: the smooth two-dimensional surface formed by sewing one sleeve per link of a graph G. It is a manifold only once sleeves replace the one-dimensional links (SI §3).
- **Systole / functional constraint**: every non-contractible loop around a link has length ≥ w, so that the link can carry flux (Eq. 2; SI Eq. 31).
- **χ = w/r**: circumference over the terminal length scale. χ → 0 is the Steiner limit.
- **λ = l/w**: the length of the intermediate link between two k = 3 nodes, in units of circumference. λ = 0 is a trifurcation.
- **ρ = w′/w**: the circumference of the third branch over that of the two equal branches.
- **Steering angle Ω₁→₂**: the solid-angle deflection between links 1 and 2 at a bifurcation. Ω = 0 means links 1 and 2 are collinear, i.e. a sprout.
- **Sprout**: a bifurcation with a thin branch leaving perpendicular to a straight thick path.
- **Extrinsic trifurcation**: an apparent trifurcation that is really two close bifurcations, or the reverse, and arises from skeletonisation (SI §7.1, citing Miyawaki et al.).

## Connections

The paper sits in Barabási-group work on "physical networks", whose earlier papers are its refs 10, 11, 53, 54 and 55:
- the Dehmamy et al. 2018 structural transition;
- Liu et al. 2021 isotopy;
- Pósfai et al. 2024 physicality;
- Glover & Barabási 2024 entanglement;
- Bonamassa et al. on bundling.

It argues against the wiring-economy tradition:
- Cajal;
- Murray 1926;
- Zamir 1976/1978 on arterial branching;
- Cherniak 1992 on local optimisation of neuron arbors;
- Chklovskii et al. 2002.

It takes its geometric machinery from closed string field theory: Saadi & Zwiebach 1989, Carlip 1988, Strebel 1984, and Headrick & Zwiebach's convex programs for minimal-area problems. It takes its numerical tiling from computational design (Jiang et al. 2020/2021; Peng et al. 2019).

Among nucleation's network readings the link is loose, and the relation is a contrast in what "geometry" means:
- [LIT-020](../literature.d/LIT-020.md) (reads/12) and [LIT-004](../literature.d/LIT-004.md) (reads/59) put a discrete curvature, Forman or Ollivier–Ricci, on an abstract graph's edges and evolve edge weights by a curvature flow. The graph has no embedding, and "geometry" is a derived edge statistic.
- [LIT-028](../literature.d/LIT-028.md) (reads/1) studies how spectral and gap dimensions of composed ("bundled") abstract graphs come apart.
- This paper does the opposite of both. It takes the embedding in R³ and the finite thickness of links as the primary data, and derives degree and angle statistics from a continuum area functional. A skeleton-level curvature of the [LIT-020](../literature.d/LIT-020.md)/[LIT-004](../literature.d/LIT-004.md) kind would be blind to exactly the thickness ratios χ and ρ that drive the predictions here.

Nothing in these three readings tests, or is tested by, this paper. The paper does mention simplicial complexes as a way to relate graphs to discrete manifolds (Bianconi & Rahmede), but explicitly chooses smooth charts instead (p. 317).

## Bearing on the record

For nucleation, the paper is the source for the surface-minimisation account of local branching in biological transport and neural trees, and for the specific numbers χ ≈ 0.83 and ρ ≈ 0.6. It should be cited as follows:
- for the hypothesis and the symmetric-motif numerics, as a locally minimising, penalised computation, not an exact solution;
- for the raw branching statistics, per dataset, not pooled.

Any nucleation document that cites it for the following claims would be citing it for more than it shows:
- that "real networks are surface-optimal", or for an "exact string-theory mapping" (C4, C10);
- for trifurcation prevalence as a measured fact independent of analysis choices (C1, C7, C13).

No nucleation THEORY document exists yet to support or contradict. The natural one this could seed is a claim about the scale at which material-cost optimisation stops predicting morphology: local junction geometry versus global layout, the ≈ 25% excess length. It should be seeded only as a conjecture.

For ML practice: nothing. The paper uses no learning method, and no ANTH- document is warranted.

## Limitations

- **The theory is local and symmetric.** Only two idealised motifs are solved, each by a local, penalised optimiser started from the Steiner configuration. There is no global search over topologies and no sensitivity analysis over mesh size or weights. SI §5 concedes that "a globally distinct surface configuration may still achieve a lower total area".
- **The theory–data bridge is approximate.** The random-terminal prediction is a sigmoid calibrated on one tetrahedron (SI Eq. 44), and the empirical Steiner reference is the external-leg distribution. Several steps are fitted:
  - σ = 0.05 for the data, against 10⁻² for the theory;
  - generalised-gamma extrapolation to x → 0;
  - per-dataset breakpoints chosen to maximise a slope difference.

  None has a null model or an uncertainty that propagates to the headline comparisons.
- **Analysis choices partly produce the observed features.** Merging bifurcations with l_int ≤ w/2π creates trifurcations, and the paper does not say whether merged motifs enter P(λ) at λ = 0. The single robustness check changes P(λ→0) more than fourfold.
- **Heterogeneous data.** Three fly neurons, one arterial tree and five plants sit beside ≈ 10⁴ human neurons. Pooled headline percentages mostly reflect the human dataset.
- **Wrong material cost for most datasets, by the authors' own account.** For neurons, corals and trees the cost is volume as well as surface. The volume check is one motif.
- **The model does not explain the excess length it reports** (η ≈ 1.25): straight cylinders far from junctions leave link curvature unexplained. The authors attribute it to global or functional demands (Discussion; SI §8).
- **Loops are excluded by construction**, and the study includes no looped networks (vascular beds, brain-scale wiring).
- **The functional claim is thin.** The synapse-ending percentage is inconsistent between text and caption, and the sprout criterion used for it is unstated.

## Open questions

- Does the trifurcation fingerprint survive when degrees are counted without the l_int ≤ w/2π merging rule? The test would be the same P(λ) with the rule removed, and with the cutoff varied.
- What does the actual minimiser (not the sigmoid) give for P(λ) over random terminal sets? Is χ_c the same for non-tetrahedral configurations?
- Is the sprouting transition sharp in the data? The test is a breakpoint model against a smooth (e.g. Zamir cylinder) model, compared by likelihood or cross-validation, with the breakpoint's selection bias accounted for.
- Does self-consistent volume minimisation with smooth junctions reproduce or overturn the predictions for solid networks (neurons, trees, corals)?
- Do the predicted junction shapes (a = b = c) hold across more than 26 trifurcations, and across datasets other than blood vessels?

## Corrections to the seeded skim

- **The "exact mapping" is exact only for a problem the paper does not solve.** Main text p. 318 says the classical Nambu–Goto solution under the systolic constraint "is exactly the manifold M(G) we seek". SI §5 (pp. 23–24) makes three points:
  - Strebel's exact solution is flat cylinders that "neglect the constraint that the surface must also be immersible within the ambient three-dimensional space". It would have "conical singularities at the sleeve intersections, rendering the solution un-physical".
  - The implemented relaxation, e^{2ϕ} ≥ 1 (Eq. 32), "is not designed to obtain the global minimum … it yields surface that is locally area-minimising".
  - The numbers come from a penalised quad-mesh optimisation (Eq. 34: iso, glue, terminal, fairness and surface terms, with an annealed w_fair schedule).

  The dossier, following the abstract, reports an exact mapping.
- **"Roughly 15% of the nodes" (Fig. 1d caption) is a pooled figure dominated by one dataset.** The per-dataset k = 4 shares vary widely.
  They are human neuron 17.0%, tropical tree 17.7%, coral 8.7%, blood vessel 8.3%, fruit fly 6.5% and Arabidopsis 4.6%.

  Pooled over the k = 3–6 counts shown, the share is 16.6%, and 96% of those nodes are human-neuron nodes (my arithmetic from the Fig. 1d counts). The text also gives k = 3 as 79% of human-neuron nodes, while the figure prints 76% (215,957 of the listed nodes).
- **The dossier's "92% of sprouts end on synapses" is the figure caption's number. The text gives a different one.** Text (p. 319): 4,003 sprouts, of which 3,911 "(98%)" end with a synapse. 3,911/4,003 = 97.7%. The Fig. 4h caption says 92%. The paper does not reconcile the two.
- **"Rule 2 violated" is overstated for bifurcations.** SI Fig. 16a says P_Bi(Ω) "has a peak close to but not equal to the Steiner prediction Ω ≈ 2π". The Fig. 1e caption says bifurcations are "more prone to Steiner rule 2 … than to random branching". A strong departure from planarity is shown only for trifurcation trios (SI Fig. 16b).
- **The main text says robustness checks were done that the SI does not contain.**
  - Main text p. 317 says the authors "verified that the observed high-degree nodes … cannot be attributed to resolution limits (SI Section 1)". SI §1 contains no such check. It asserts that dimensionless ratios make the results "robust against variations in spatial resolution" (p. 8).
  - The one procedure the SI does describe works the other way. SI §7.1, Eq. 43: two bifurcations whose intermediate link has l_int ≤ w/2π are merged "into a single trifurcation". Trifurcations are therefore partly produced by the analysis.
  - The skeletonisation robustness check covers one dataset (human neurons) and one alternative method (Skeletor). The SI calls the results "fully consistent", yet P(λ→0) is 1.200 under the alternative against 0.276 under the original (SI Fig. 5a,b), a 4.3× difference.
- **The Fig. 3h "surface minimisation" curve for random terminals was not produced by surface minimisation.** SI §7.1 says running the minimiser on 10⁶ random quadruplets "is un-scalable". Instead λ is mapped through a sigmoid (Eqs. 44–45) calibrated on the regular tetrahedron: λ_Steiner ≈ 0.212χ⁻¹, threshold 0.83, σ = 10⁻². The empirical comparison then uses a separately fitted σ = 0.05.
- **The empirical "Steiner" reference in Fig. 3i–n is not a Steiner computation on the data.** SI §7.1 says it is represented by the length distribution of external legs, on the grounds that λ_Steiner is on average linear in them. The relation it relies on, l_int ≈ A(l_ext − Bw), has Spearman ρ of only 0.11–0.42 across datasets (SI Fig. 15).
- **The SI contradicts itself on internal versus external legs.** SI p. 34: "Across all networks … P(l_int/w → 0) is positive … P(l_ext/w → 0) tends to zero". Coral, in SI Fig. 14e, shows the reverse: P(l_int/w = 0) ≈ 0.000 and P(l_ext/w = 0) ≈ 0.237.
- Minor inconsistencies in the text:
  - The main text gives the merge point as "χ ≈ 1" and then as "χ ≈ 0.83" (p. 318).
  - The Steiner steering angle is "≈ 0.3π" in the main text but 0.268π in SI Fig. 19.
  - SI Eq. 35 contains (z_{r,0} − z_{r,0})², which should presumably be (z_{r,0} − z_{r,2}).
  - The angle filter "following criterion (43)" uses l/w < 2(2π)⁻¹, twice the Eq. 43 cutoff.
- Dossier's access note: it was right that the SI holds the substance. The SI is reachable (media.springernature.com MOESM1) and was read in full here. No arXiv preprint was found.
