---
status: Read
paper: LIT-tmp11m3i
title: 'Structural Learning Theory: A Metric-Topology Factorization Approach'
version: 1
history:
- version: 1
  date: '2026-10-01'
  note: >-
    Read in full (>- Full text of arXiv 2602.07974 v2 (6 May 2026), the
    current version, from the arXiv PDF. It runs 41 pp. in a JMLR template;
    the extraction ran to Appendix C.12. I read the abstract, §1 (1.1–1.3,
    Table 1, Fig. 2), §2 (Defs 2.1–2.4, Prop 2.1, Thms 2.1, 2.2, 2.4–2.6,
    Assumption 2.3, Remarks 2.1–2.4, Table 2, Fig. 3), §3 (Defs 3.1–3.8,
    Thms 3.1–3.9, Prop 3.1, Assumption 3.7, Remarks 3.1–3.2), §4 (Defs
    4.1–4.6, Thms 4.1, 4.2, 4.4–4.8, Assumption 4.3, Props 4.1–4.2, Cors
    4.1–4.3, Remarks 4.1–4.5, Fig. 4), §5, the reference list, and every
    appendix proof (A.1–A.6, B.1–B.9, C.1–C.12). Nothing was skipped. I also
    read v1 (8 Feb 2026, 28 pp.) in full: abstract, §§1–6 including the
    three experiments, the AI-use statement, and Appendix A. v1 is a
    different paper under a different title, "Beyond Optimization:
    Intelligence as Metric-Topology Factorization under Geometric
    Incompleteness" (see corrections). `published:` is therefore the v2
    date. The JMLR header on both versions ("Journal of Machine Learning
    Research 23 (2026) … Published 9/22", "Editor: TBD") is template
    residue. The work is an unrefereed preprint. No entry for this arXiv id
    or either title exists in the anthology or in nucleation. Read
    2026-10-01 together with LIT-373 and LIT-374, as one programme, to a
    charitable standard: repairable slips are set aside, and errors count
    only when a major takeaway depends on them.). The first NOTE on this
    paper, which was seeded from its abstract alone.
date: '2026-10-01'
summary: >-
  >- The formal core of Xin Li's structural-learning programme. Width w(P;
  γ, δ) is the least number of open cells on each of which some predictor
  is γ-contractive with conditional risk ≤ δ. The paper proves that width
  is incomparable with the per-cell VC dimension (Thm 2.2). It shows that
  with K < w cells there is an n-independent error floor η(w, K), under a
  non-degeneracy assumption stated in the body (Thm 2.4, Assumption 2.3).
  Width is at least c·β₁·L/D₀ under a bounded-overlap assumption (Thm
  2.5), and discovering all basins costs Ω(w log w) samples (Thm 2.6). The
  CS-Laplacian eigenvalue count converges uniformly to the
  predictor-relative count w_G(P) when n ≳ (H_G + d_X log(1/r_x) +
  log(1/δ′))/(r_x^{d_X} g_eff²) (Thm 3.5); no result shows that w_G equals
  width. There are no experiments.
---

# NOTE-tmpm6dav: Structural Learning Theory: A Metric-Topology Factorization Approach

## Contribution

The paper supplies the learning theory that [LIT-374](../literature.d/LIT-374.md) §3 only "briefly reviews". It makes "width" a defined quantity: a cover number for the structural ("trap") side of multi-context learning. It proves width's basic separation and lower-bound results, and builds a spectral estimator for width with stability and uniform-convergence guarantees. It also adds a funnel-side theory, the "metric slingshot": composing an embedding with pre-built latent contractions transfers contraction, risk and width with Lipschitz-controlled loss.

**Place in the programme.**
- It formalises [LIT-373](../literature.d/LIT-373.md)'s informal "Search → Closure → Navigation" cycle. Width is described as "the minimum number of local Urysohn constructions" needed to resolve structural conflicts (§2). The E-D-T split/merge cycle is the search/closure alternation. The slingshot is [LIT-373](../literature.d/LIT-373.md)'s "warp the metric until the maze is a bowl".
- [LIT-374](../literature.d/LIT-374.md) is this paper's application layer. [LIT-374](../literature.d/LIT-374.md) adds the decoupling prescription and the alignment section, and restates this paper's theorems with weaker presentation.

## Key insight

Allow only locally smooth predictors, in that each must be a contraction on its cell. Then a problem with several incompatible regimes needs at least w cells, however rich the per-cell class. Counting those cells, and finding them, is a separate cost from fitting inside them. The paper's main conceptual move is to keep the contraction constraint and the risk constraint together (Def 2.3), so that a cell counts only if it is both geometrically stable and statistically accurate.

## Assumptions

- **Setting (§2, notation).** (X, d_X) is a compact metric space, ℓ ∈ [0, 1] is L-Lipschitz, and κ(g, U) is the Lipschitz modulus of g on U. A set U is (γ, δ)-contractive if some g ∈ G has κ(g, U) ≤ γ < 1 and E[ℓ | U] ≤ δ (Def 2.3). Width uses an *open* cover (Def 2.4), "deliberately".
- **Thm 2.1 (bouquet).** (1) For each circle C_j some predictor makes "a neighborhood of C_j" (γ, δ)-contractive. (2) No predictor is contractive on any open set meeting two circles near the basepoint x₀. For w ≥ 2 these two conditions contradict each other, since every neighborhood of C_j contains x₀ (see Limitations).
- **Thm 2.4 (phase transition).** Assumption 2.3, structural non-degeneracy: any K-cell cover that forces a cell to mix two basins incurs excess risk ≥ η(w, K) > 0. Part (1) also assumes balanced cells, n_c ≳ n/K (A.4).
- **Thm 2.5.** Assumption A.1 (cycle independence / bounded overlap Δ₀), which appears only in the appendix. Each contractive set also has diameter ≤ D₀.
- **Thm 3.3.** Within-basin prediction variation is ≤ δ_y and the cross-basin gap is ≥ Δ_y for the *fixed* G. The higher-order Cheeger bound and the operator-norm perturbation bound are invoked, not derived.
- **Thms 3.4–3.5.** ‖G − G*‖_∞ = η, bounded outputs B_Y, at most s_x neighbours, degree conditioning C_deg, an eigengap g* > 0, a locally Lipschitz map from eigenspace to partition, and random-geometric-graph occupancy plus kernel matrix concentration (B.6).
- **Thm 3.8.** Assumption 3.7 does most of the work. It requires: every true basin to be visible, with P(B_j) ≥ K_max·ε₀ + ε₀; CS splits to reduce impurity by a factor (1 − α_split); and merge tests to be correct with probability 1 − δ_m.
- **Thm 3.9.** Structural gap, no gain above width, uniform convergence, a penalty λ_n K with λ_n → 0 and λ_n/r_n → ∞, and partition identifiability.
- **Thm 3.1 (Amortized Separation).** The proof (B.1) assumes that one basis triple resolves at most Cε of boundary measure. That is the conclusion's content.
- **§4.** Each G⁰_c is γ_Z-contractive, π_c is L_π-Lipschitz, and ϕ has local distortion L_ϕ(U). The occupancy regularity in Assumption 4.3 is assumed. The local stability inequalities for Thm 4.6 are assumed.

## Key results

**Width theory (§2)**
- **Prop 2.1.** Width is monotone in (γ, δ), finite for relaxed thresholds, and w = 1 iff a global (γ, δ)-contractive predictor exists. Proved.
- **Thm 2.1 (strict hierarchy).** w = β₁ on a bouquet of w circles. As stated, the hypotheses are contradictory (see Assumptions). The repaired version, with safe regions placed away from the basepoint, or with a measurable partition, is proved correctly in the author's arXiv 2603.15412 v1 (Thm 4.1).
- **Thm 2.2 (VC–width separation).** Bouquet with affine G gives w → ∞ with VC(G) = O(1). Polynomials with f* = λx, λ < γ, give VC(G_d) → ∞ with w = 1. True in repaired form.
  - The corollary that "scaling cannot repair structural deficiency … since no continuous operation can produce a discrete jump" does not follow. Width is relative to γ-contractive per-cell predictors; a monolithic model is not so constrained.
- **Thm 2.4 (phase transition).** (1) If K ≥ w, Gap(n; K) ≤ C·√((K log N(Z_c, ε) + log(K/δ′))/n). (2) If K < w, Gap(n; K) ≥ η(w, K) for all n, under Assumption 2.3. Proved given the assumption, which is the substantive content. Remark 2.2 gives a testable signature: the gap between K = w − 1 and K = w widens with n.
- **Thm 2.5 (topology–geometry scaling).** w ≥ c·β₁(M)·L/D₀, with c = c₀/Δ₀ under Assumption A.1. Proved in the regularised form. It makes width explicitly partly metric: a covering number at scale D₀.
- **Thm 2.6.** Ω(w log w) samples are needed to identify all basins with probability bounded away from zero, by coupon collector over equal-mass basins. Proved and standard.

**Estimation (§3)**
- **Thm 3.1.** k ≥ W(τ)/(Cε). Assumed in the proof, not derived.
- **Thm 3.2 (Geodesic Inference Bound).** Path length ≤ Σλᵢ·W/d. Holds under an assumed equipartition of boundary measure; "inference path length" is not defined independently.
- **Prop 3.1 (Laplacian blindness).** On a densely sampled bouquet the plain graph Laplacian has one near-zero eigenvalue. Correct.
- **Thm 3.3 (spectral gap amplification).** g_eff ≥ c₁φ_in²/w⁴ − C₁·exp(−(Δ_y² − δ_y²)/σ_y²)·φ_out. The weight-ratio step is immediate. The rest is Cheeger and Weyl with an invoked perturbation norm. Standard-shaped and charitably acceptable.
- **Thm 3.4 (local stability).**
  - Eigenvalue shift |λ_k(L_CS(G)) − λ_k(L*)| ≤ (8B_Y s_x C_deg/σ_y²)·η.
  - Partition shift d_part ≤ (C_Π/τ*)(8B_Y s_x C_deg)/(g*σ_y²)·η, by Davis–Kahan.
  - Refinement recursion η_{t+1} ≤ αη_t + b_m.

  Proved given the stated assumptions, and local to G*.
- **Thm 3.5 (uniform convergence).** Pr(sup_{G ∈ G_K} |ŵ_n(G) − w_G(P)| ≥ 1) ≤ δ′ at the sample size in the summary. A net argument, kernel-graph matrix concentration and a Weyl margin. Proved in outline. The limit is **w_G(P), the population CS count for predictor G**, not w(P; γ, δ).
- **Thm 3.6.** Safe merge with m ≥ C·log(K/δ′)/Γ²_min samples per test.
- **Thm 3.8.** Split–merge terminates at K = w, ε₀-pure, in ≤ (aP(X) + bK_max)/Δ_min steps, under Assumption 3.7.
- **Thm 3.9.** Penalised structural ERM: K̂_n = w eventually almost surely, and dist(Π̂_n, P*_w) → 0. Standard. The paper notes that BIC is too small for bounded-loss structural ERM and gives λ_n = n^{−1/3} as an example (Remark 3.2).

**Funnel (§4)**
- **Thm 4.1.** γ_X(U) ≤ L_{π,c}·γ_Z·L_ϕ(U) (Lipschitz composition).
- **Thm 4.2.** Risk transfer R_U(F_c) ≤ R_U(f*) + L_ℓ·ε_U.
- **Thm 4.4.** Width transfer w_Z ≤ Σ_k ⌈L_ϕ(U_k)·L_X(U_k)/D₀^Z⌉, under Assumption 4.3.
- **Thm 4.5.** Per-funnel uniform convergence O(√(p_c log n_c / n_c)) for readout pseudo-dimension p_c.
- **Cor 4.2.** Oracle excess risk after correct routing.
- **Props 4.1 and 4.2.** Decoupling holds when the indexer is trained only on mismatch, ϕ is frozen or self-supervised, G⁰ is frozen and readouts are local. This is by construction. Prop 4.2 says the bootstrap is well defined and needs no knowledge of w.
- **Thm 4.6.** Local linear convergence of the bootstrap when q_Φ + C_Φ·C_Σ < 1 (assumed contraction).
- **Thm 4.7 (grid spacing).** For log-uniform path lengths on a range of ratio R, the minimax log-covering scales are geometric, r* = R^{1/(M−1)}. This follows from scale invariance.
- **Cor 4.3.** Running CS in Z replaces r_x^{−d_X} by r_z^{−d_Z}.
- **Thm 4.8.** Combines the above into one slingshot theorem.

All §4 results are elementary consequences of their assumptions. They are correct and carry no surprise.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Width and VC dimension are incomparable (Thm 2.2) | proof; repairable construction in one direction | A.3. The bouquet hypotheses of Thm 2.1 conflict as written. 2603.15412 v1 gives a consistent construction |
| C2 | "Scaling cannot repair structural deficiency" (corollary to Thm 2.2) | informal argument; undermined as stated | Width is relative to γ-contractive per-cell predictors. A monolithic model can represent the routing. The continuity remark ("no continuous operation can produce a discrete jump") is not an argument |
| C3 | Below width there is an n-independent error floor; at or above width, ordinary rates (Thm 2.4) | proof, given Assumption 2.3 | A.4. Pigeonhole plus non-degeneracy. Close to definitional |
| C4 | w ≥ c·β₁·L/D₀ (Thm 2.5) | proof, under appendix Assumption A.1 | A.5. Shows width is partly a metric covering number |
| C5 | Discovering all basins needs Ω(w log w) samples (Thm 2.6) | proof (standard) | A.6, coupon collector |
| C6 | The CS operator "uniformly estimates the population structural width" (§3.2, §5) | proof of a weaker statement | Thm 3.5 proves convergence to w_G(P) for each G in the class. Equality of w_G with w(P; γ, δ) is not shown, and fails in general where width is forced by steepness rather than value jumps (the L/D₀ factor) |
| C7 | Split–merge converges to the correct width in finitely many steps (Thm 3.8) | proof, under strong Assumption 3.7 | B.8. The assumption that each split reduces impurity carries the result |
| C8 | Penalised structural ERM is consistent for w (Thm 3.9) | proof (standard) | B.9 |
| C9 | Complex boundaries need ≥ W/(Cε) basis triples (Thm 3.1) | assumption restated | B.1. The per-triple resolution bound is assumed |
| C10 | The slingshot transfers contraction, risk and width with Lipschitz-controlled loss (Thms 4.1, 4.2, 4.4, 4.8) | proof (elementary) | C.1–C.4, C.12 |
| C11 | Grid-like geometric scale spacing is minimax-optimal (Thm 4.7) | proof (elementary) | C.10, scale invariance of a log-uniform range |
| C12 | Trap and funnel "must be architecturally independent" (Table 2) | informal argument | Follows from no theorem. Def 2.2 states decoupling as an "idealized principle". Props 4.1–4.2 show only that the architecture achieves it by construction |
| C13 | StrLT makes the CLS trap–funnel decomposition "precise, quantifiable, and testable" (§1.2) | assertion | No test is run. The falsifiable prediction (modularity helps only once K ≥ w) is stated but not tested |

## Method

Definitions plus proofs. The paper uses no data, simulation or code. The proof tools are pigeonhole, coupon collector, Cheeger, Weyl and Davis–Kahan, ε-nets with matrix concentration, Lyapunov descent for split–merge, penalised model selection, and Lipschitz composition. Several "standard regularity assumptions" are made explicit only in the appendices, which says so.

## Concepts

- **Metric–Topology Factorization (MTF).** An indexer Σ: X → Δ([K]) plus per-context learners G_c (Def 2.1).
- **Structural decoupling.** ∇_{θ_Σ} L_funnel = 0 and ∇_{θ_G} L_trap = 0 (Def 2.2).
- **(γ, δ)-contractive set; width.** Defs 2.3–2.4.
- **Structural non-degeneracy η(w, K).** Assumption 2.3.
- **Urysohn Machine; Urysohn triple (Σ, Π, f).** A support, a target partition and a classifier (§3.1).
- **Decision-boundary measure W(τ).** Defs 3.1–3.2.
- **Class-aware contraction.** A metric that shrinks within-class distances by λ < 1 and does not shrink cross-class ones (Def 3.3).
- **CS kernel, CS Laplacian, CS width estimate ŵ_n(G).** Defs 3.4–3.6. ŵ_n(G) is the number of eigenvalues below τ_spec.
- **Merge margin Γ_min; impurity I(U); E-D-T cycle.** Def 3.7, Def 3.8, §3.3.
- **Navigational latent space; metric slingshot (ϕ, π, Σ); local slingshot distortion; latent realization error.** Defs 4.2–4.5.
- **Bidirectional bootstrap.** Def 4.6.

## Connections

- **[LIT-373](../literature.d/LIT-373.md) (Li 2026, "The two dragons of cognition").** This is the formal counterpart of [LIT-373](../literature.d/LIT-373.md)'s programme, though it does not cite it.
  - [LIT-373](../literature.d/LIT-373.md)'s "Urysohn operator" becomes the Urysohn triple.
  - Its Search → Closure → Navigation becomes E-D-T, with push/pop.
  - Its "metric slingshot" becomes Defs 4.2–4.3.
  - Its condensation into tokens becomes frozen per-context contractions.

  The paper repairs none of [LIT-373](../literature.d/LIT-373.md)'s specific mathematical claims: Savitch is absent, and Urysohn appears only as motivation. It gives no counterpart to [LIT-373](../literature.d/LIT-373.md)'s Theorem 2 (exponential reach): Thm 3.1 is a linear resource bound of a different kind.
- **[LIT-374](../literature.d/LIT-374.md) (Li 2026, "Structural Decoupling").** [LIT-374](../literature.d/LIT-374.md) §3 summarises this paper's Thms 2.2, 2.4, 2.6, 3.3 and 3.9 and the slingshot theorem, in weaker form. [LIT-374](../literature.d/LIT-374.md) §4 then adds the structural Rademacher decomposition, the fundamental theorem and the decoupling principle, none of which appear here. This paper is the better source for the width theory. [LIT-374](../literature.d/LIT-374.md) is the only source for the decoupling argument and the safety section.
- **[THEORY-019](../theory.d/THEORY-019.md).** Thm 3.5's Weyl-margin argument is a gap-conditioned answer, for graph Laplacians and a fixed predictor, to the noisy near-degeneracy question [THEORY-019](../theory.d/THEORY-019.md) leaves open. The eigenvalues it counts at zero count components, not a group. No bearing on [THEORY-019](../theory.d/THEORY-019.md)'s promote_when (the real Schur corollary).
- **[THEORY-028](../theory.d/THEORY-028.md).** Every guarantee here is class-level or assumes correct routing. The decoupling recommendation that the programme draws from this framework is about training dynamics, and would need algorithm-dependent analysis of [THEORY-028](../theory.d/THEORY-028.md)'s kind. No bearing on [THEORY-028](../theory.d/THEORY-028.md)'s promote_when.
- **[THEORY-039](../theory.d/THEORY-039.md) and [THEORY-022](../theory.d/THEORY-022.md).** Remark 2.2's "gap widens with n" signature is a measurable later-phase prediction of the kind [THEORY-039](../theory.d/THEORY-039.md) says must be instrumented, not identified by shape. The paper does not discuss grokking ([LIT-374](../literature.d/LIT-374.md) does). No bearing.
- **[THEORY-030](../theory.d/THEORY-030.md) and [THEORY-035](../theory.d/THEORY-035.md).** No bearing. There is no thermodynamic or information-compression content.
- **Not in the record.**
  - The author's arXiv 2603.15412 v1 ("Local Urysohn Width"), cited here as the source of width. Read alongside this reading.
  - Osmani 2026 ("General machine learning: theory for learning under variable regimes", arXiv 2603.23220), cited for multi-regime learning. Not read.

## Bearing on the record

The paper is filed for the programme. Read with [LIT-373](../literature.d/LIT-373.md) and [LIT-374](../literature.d/LIT-374.md), it shows that the programme has a real formal core, more careful than [LIT-374](../literature.d/LIT-374.md)'s summary of it, and it answers several of [NOTE-322](NOTE-322.md)'s objections:
- non-degeneracy is stated in the body;
- I_tot and E-D-T are defined;
- a uniform-convergence theorem is supplied.

It leaves the main gap open: estimator against width (C6). It also leaves untouched the step from bound to prescription criticised in [LIT-374](../literature.d/LIT-374.md).

**For ML practice (the Anthology of the SOTA) it carries nothing yet.** The recommendations it gestures at (K ≥ w experts, separate routing signals, a frozen pre-trained embedding) have no experiment here. Its one falsifiable architectural prediction ("modularity helps only once K reaches the true width") is untested.

## Limitations

- **The bouquet hypotheses conflict.** Thm 2.1's (1) requires a contractive neighborhood of each whole circle; (2) forbids contractivity on any open set meeting two circles near x₀. For w ≥ 2 every neighborhood of C_j meets the other circles near x₀. The repair is to place safe regions away from the basepoint, as the author's 2603.15412 v1 does. Not load-bearing once repaired.
- **The estimator is not tied to width.** See C6. The CS count sees value discontinuities of a given G. Width also counts cells forced by steepness relative to γ, which is the paper's own L/D₀ factor.
- **Assumptions carry the strongest results.** Thm 3.1 assumes its conclusion. Thm 3.2 assumes equipartition. Thm 3.8 rests on Assumption 3.7's per-split impurity reduction. Thm 4.6 assumes the contraction it concludes. Thm 2.5 needs an appendix-only bounded-overlap assumption.
- **Overreach in the prose.** "Fully orthogonal", "a mathematical inevitability for any system that addresses structural complexity" (§2.1) and "deep implications for continual and lifelong learning" (abstract) are not established by the theorems.
- **No experiments**, though v1 had small ones. The "simple and falsifiable phenomenon" (§1.2) is left untested.
- **Template residue.** The JMLR header and "Published 9/22" could mislead a reader about refereeing. The PDF carries no AI-use statement, unlike v1 and the author's other papers.

## Open questions

- Under what conditions on (P, G, γ) does w_G(P), for a G learned by the E-D-T loop from a cold start, equal w(P; γ, δ)?
- Does a capacity-matched monolithic network show the K < w floor on a known-width benchmark, or only routed learners restricted to contractive experts?
- Is the "gap widens with n" signature (Remark 2.2) observable in a real MoE sweep over K?
- Does Thm 2.5 hold without the appendix-only bounded-overlap assumption? The author's 2603.15412 v1 states the general Betti bound as Conjecture 8.9.

## Corrections to the seeded skim

- none (there was no seed or dossier)
- 'arXiv 2602.07974 v1 (2026-02-08) is a different work. Its title is "Beyond Optimization: Intelligence as Metric-Topology Factorization under Geometric Incompleteness". It shares the MTF framing and the Möbius/parity, Topological Urysohn Machine and "memory-amortized metric inference" vocabulary, but no definition or theorem: there is no width, no CS operator and no phase transition. Its formal content is a Morse-theory "Geometric Incompleteness Theorem" (Thm 7): on a manifold with some βₖ > 0 for 1 ≤ k ≤ d−1, every Morse function has an intermediate-index critical point. That is the weak Morse inequalities. It also has an orthogonal-subspace no-interference result (Thm 14), and three small experiments. The experiments are a 4-dimensional "Möbius latent world" whose features encode the parity bit directly, a "Betti-complexity" convergence plot, and a 5-task Permuted MNIST comparison with EWC; they are reported as figures, with no tables. v2 replaced it wholesale, so `published:` is the v2 date, 2026-05-06.'
- '[NOTE-322](NOTE-322.md) and the joint reading both say the paper is "not cited" by [LIT-374](../literature.d/LIT-374.md). That stands: [LIT-374](../literature.d/LIT-374.md) cites neither version. This paper in turn cites neither [LIT-373](../literature.d/LIT-373.md) nor [LIT-374](../literature.d/LIT-374.md). It cites "Li 2026, Local Urysohn width" (arXiv 2603.15412) for width.'
- [NOTE-322](NOTE-322.md) lists I_tot and the E-D-T cycle as undefined in [LIT-374](../literature.d/LIT-374.md). Both are defined here. I_tot(Π) = Σ_k [P(U_k) − max_j P(U_k ∩ B_j)] is the total impurity (Def 3.8). E-D-T is the Evaluate–Detect–Transform cycle (§3.3).
- '[NOTE-322](NOTE-322.md) found Thm 3.3''s non-degeneracy condition only in [LIT-374](../literature.d/LIT-374.md)''s appendix. Here it is Assumption 2.3, stated in the body before the theorem.'
