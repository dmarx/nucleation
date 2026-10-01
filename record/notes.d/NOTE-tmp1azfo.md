---
status: Read
paper: LIT-tmp8xsqx
title: 'Local Urysohn Width: A Topological Complexity Measure for Classification'
version: 1
history:
- version: 1
  date: '2026-10-01'
  note: >-
    Read in full (>- Full text of arXiv 2603.15412 v1 (16 Mar 2026), "Local
    Urysohn Width: A Topological Complexity Measure for Classification",
    from the arXiv PDF (22 pp.). I read the abstract, §§1–10 (Defs 2.1,
    3.1–3.3, 8.1, 8.4; Lemmas 3.5–3.7, 8.2; Thms 4.1, 6.1, 7.1, 8.5, 8.10;
    Cor 5.1; Conjs 8.9, 8.12; Remarks; Fig. 1), the AI disclosure statement,
    the references, and Appendices A–G (safe-region conventions, VC notions,
    the explicit target family, convexity assumptions, the dependency map,
    bibliographic notes, and the detailed AI-use disclosure). Nothing was
    skipped. **The identifier now serves a different paper.** v2 (14 Sep
    2026) is "The Metric Slingshot: Navigational Reuse as Width-Optimal
    Structural Decoupling in Continual Learning" (41 pp.). It shares v1's
    name for the measure but not its definition, and it shares no theorem
    with v1. I also read v2 in full: abstract, §§1–8, Defs 2.1, 2.3, 4.1,
    4.2, 5.1, 5.3; Thms 2.4, 4.3, 4.5; Props 3.1, 5.4, 6.2; Cor 5.5;
    Remarks; Tables 1–4; Fig. 1; the references; and Appendix A with the
    proofs of Thm A.1, Prop 3.1, Thms 4.3 and 4.5, and Prop 5.4. This file
    reads v1, the work the owner asked for by title, with `published:` =
    2026-03-16. v2 is reported separately below under "The current version
    (v2)". This choice departs from LIT-374's precedent, which filed what
    the identifier then served (see corrections). No anthology or nucleation
    entry exists for this arXiv id or either title. Read 2026-10-01 together
    with LIT-373, LIT-374 and arXiv 2602.07974, as one programme, to a
    charitable standard.). The first NOTE on this paper, which was seeded
    from its abstract alone.
date: '2026-10-01'
summary: >-
  >- It defines local Urysohn width uw_{D₀}(P, γ): the least number of
  connected sets of diameter ≤ D₀, each carrying a continuous classifier
  correct on the margin-γ safe region it meets, needed to cover that safe
  region. It proves: - uw = w on a bouquet of w circles with safe balls at
  the antipodes, when 3γ/2 ≤ D₀ < L/2 − 3γ/4 (Thm 4.1); - uw ≥ w·m, with m
  = Θ(L/D₀) safe balls per loop, so uw = Ω(w·L/D₀) (Cor 5.1); - two-way
  non-determination with VC dimension (Thm 6.1); - an Ω(w log w) sample
  lower bound via label-permuted coupon collection (Thm 7.1); - uw ≥
  2β₁/Δ₀ for good, convex, bounded-adjacency covers (Thm 8.5). The proofs
  are correct. The obstruction is metric, as the paper concedes in Remark
  8.11: patches cannot reach across the wedge point. Because Urysohn's
  lemma makes local correctness automatic on any patch, the measure is a
  connected covering number of the safe region that does not depend on the
  labels.
---

# NOTE-tmp1azfo: Local Urysohn Width: A Topological Complexity Measure for Classification

## Contribution

v1 defines a complexity measure of a classification *instance*, as opposed to a hypothesis class. It is the least number of local, connected, diameter-bounded "experts" that together cover and correctly classify the margin-safe region. The paper proves four things about it: a strict hierarchy on connected spaces, a multiplicative scaling with loop length, non-determination by VC dimension, and a coupon-collector sample lower bound. A conditional lower bound in terms of the first Betti number is stated as a theorem under strong cover conditions, and the general case is left as a conjecture.

**Place in the programme.** Chronologically this is the first paper to define width. The order of the programme is:
1. [LIT-373](../literature.d/LIT-373.md) (Frontiers, received 31 Dec 2025, published 23 Mar 2026);
2. arXiv 2602.07974 v1 ("Beyond Optimization", 8 Feb 2026), which v1 here cites as [30] for metric–topology factorisation;
3. this paper (16 Mar 2026);
4. arXiv 2602.07974 v2 (StrLT, 6 May 2026), which cites this paper for width;
5. [LIT-374](../literature.d/LIT-374.md) (8 Jun 2026);
6. this identifier's v2 (14 Sep 2026).

It is the programme's Urysohn idea made precise. It answers [LIT-373](../literature.d/LIT-373.md)'s misuse of Urysohn honestly: Remark 3.4 concedes that a single global Urysohn function makes every margin problem width 1, so only an imposed locality constraint gives the measure content.

## Key insight

Urysohn's lemma makes separability trivial globally. Count instead how many *local* separators, confined to connected patches of diameter ≤ D₀, are needed. That count is a property of the instance's geometry. It can be large while every local task is trivial.

## Assumptions

- **Setting.** (X, d) is a compact metric space. A K-class margin-γ problem is a family of closed A_k with d(A_i, A_j) > γ; the strict inequality is App. A's correction of the body's ≥. The safe region is Safe(P, γ) = ∪ A_k^{γ/2} (Def 3.1).
- **Local Urysohn triple (S, U, f).** S is connected with diam S ≤ D₀, and f: S → Δ^{K−1} is continuous. A covering must contain Safe(P, γ), and argmax fᵢ = k on Sᵢ ∩ A_k^{γ/2} (Def 3.2).
- **Thm 4.1.** Bouquet of w circles of length L, safe balls of radius γ/4 at the antipodes, γ < L/10, and 3γ/2 ≤ D₀ < L/2 − 3γ/4. This is satisfiable iff L > 9γ/2.
- **Thm 7.1.** Label-permuted bouquet family, with each safe region's mass in [1/(c₁w), c₂/w].
- **Thm 8.5.** All four of the following:
  - (i) each patch lies in a geodesically convex ball of radius < sys(X)/4;
  - (ii) a good cover;
  - (iii) H₁(Safe) → H₁(X) has image of rank β₁(X);
  - (iv) nerve adjacency ≤ Δ₀.

## Key results

- **Lemmas 3.5–3.7.**
  - Width is monotone in the margin.
  - It is monotone under label refinement.
  - It is additive on components separated by more than D₀.

  All three are proved and immediate.
- **Thm 4.1 (connected-space hierarchy).** uw_{D₀}(P_w, γ) = w. *Lower bound:* any point of a safe ball is at distance ≥ L/2 − 3γ/4 > D₀ from every other loop, so no patch serves two safe balls. *Upper bound:* one constant-label arc per ball. Correct.
- **Cor 5.1 (scaling).** With m equally spaced safe balls per loop and 3γ/2 ≤ D₀ < min(L/(2m) − 3γ/2, L/4 − 3γ/4), uw ≥ wm, so uw = Ω(w·L/D₀). Correct.
- **Thm 6.1 (VC does not determine width).**
  - (a) uw(P_w) = w, while the class of labelings constant on the w arcs has VC ≤ w log₂ w.
  - (b) Unions of n γ-separated intervals on [0, 1] have VC = 2n, yet uw = 1 when D₀ ≥ 1, because one Urysohn function on [0, 1] separates them.

  Both are correct. Each compares a property of an instance with a property of a class, which App. B makes explicit.
- **Thm 7.1.** Ω(w log w) samples are needed to be correct on all of Safe with probability 2/3. A missed region's label is uniform over the unused labels, so the learner fails there with probability ≥ 1/2; then coupon collector. Correct. Appendix C gives n ≥ (cw/2)·ln(3w).
- **Lemma 8.2.** A patch inside a geodesically convex ball of radius < sys/4 is contractible. Remark 8.3 openly corrects an earlier false version ("small diameter suffices").
- **Thm 8.5.** w ≥ 2β₁(X)/Δ₀ under (i)–(iv), via the Nerve Lemma and β₁(G) ≤ |E| ≤ Δ₀w/2. Correct as a statement about covers of a safe region that itself carries the homology.
- **Thm 8.10.** Wedge of w k-spheres: uw = w = β_k, by the same metric confinement argument.
- **Conjs 8.9 and 8.12.** A general Betti lower bound without bounded adjacency, and an all-degree version. Open.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | For every w there is a problem on a connected space with β₁ = w and width exactly w (Thm 4.1) | proof | §4. Correct |
| C2 | "Topological complexity of the input space forces classifier complexity" (abstract, §10) | informal argument; undermined as stated | The proof is metric confinement, and Remark 8.11 concedes this. A tree with w long arms (β₁ = 0) has width w by the same argument, so β₁ is incidental |
| C3 | Width = Ω(β₁·L/D₀), a "multiplicative" product of a topological and a metric factor (Cor 5.1, §5.2) | proof of the instance bound; the factorisation reading is interpretation | The proof counts D₀-separated safe balls. The β₁ factor is the number of loops used in the construction |
| C4 | Width and VC dimension are mutually non-determining (Thm 6.1) | proof | §6, App. B. The abstract's "VC bounded by a constant" is not what is proved (see corrections) |
| C5 | Ω(w log w) samples are needed (Thm 7.1) | proof (standard) | §7, App. C |
| C6 | Width characterises "the classification problem itself", "not the hypothesis class" (abstract, §2) | definition; overstated | Local correctness is automatic on any connected patch (Urysohn on the patch, since class safe regions are closed and > γ apart). So uw is the least number of connected D₀-diameter sets covering Safe(P, γ), and labels enter only through γ |
| C7 | uw ≥ 2β₁/Δ₀ for good convex covers with bounded adjacency (Thm 8.5) | proof | §8.2. Correct, but condition (iii) fails for the paper's own bouquet (corrections) |
| C8 | "Any system that maintains fewer than uw experts cannot correctly classify all points in the safe region, regardless of how sophisticated each expert is", so the modular, decoupled architecture is "necessary" (§9) | informal argument; true only for systems built from local experts | Remark 3.4 concedes that a single global classifier gives width 1. The necessity claim restates the definition's locality constraint |
| C9 | Routing "must be gradient-free" to avoid routing drift (§9) | assertion | Cites a theory of MoE in continual learning ([32]); no argument here |

## Method

Definitions and proofs. No data or experiments. The tools are metric confinement through the wedge point, coupon collector with a label-permutation indistinguishability argument, and the Nerve Lemma with a handshake count.

App. G is an unusually detailed AI-use disclosure. Proofs of Thms 6.1 and 7.1 were "generated by cross-validating collaboration between ChatGPT 5.4 and Claude 4.6". The bouquet construction was "initialized by Claude and corrected by the human author". Cor 5.1 was "generated by Claude". "most supporting material in the Appendix … is generated and polished by the combination of AI models".

## Concepts

- **Urysohn Machine.** A 7-tuple with a metric library of local triples and an Evaluate–Detect–Construct cycle; past classifiers are frozen (Def 2.1). This is the E-D-T cycle of arXiv 2602.07974 v2, with "Construct" in place of "Transform".
- **Margin partition; safe region.** Def 3.1.
- **Local Urysohn triple; (γ, D₀)-covering; local Urysohn width.** Defs 3.2–3.3.
- **Systole; bounded nerve adjacency.** Defs 8.1, 8.4.
- **I-system / M-system.** Indexing and metric subsystems (§5.2, §9). These are [LIT-374](../literature.d/LIT-374.md)'s scaffold and flow, and arXiv 2602.07974's trap and funnel.
- **Selection complexity vs coverage complexity.** VC dimension against width (§9).

## The current version (v2): "The Metric Slingshot"

v2 (14 Sep 2026) under this identifier is a different paper. It is reported here because a LIT keyed to the identifier would serve it.

**What it proposes.** Brain circuits evolved for navigation (grid cells, place cells, hippocampal indexing) are reused for non-spatial tasks through a learned embedding ϕ: X → Z into a navigational latent space whose contraction maps are pre-built. Only the indexer Σ, ϕ and the readout π are learned. It maps:
- ventral stream to ϕ, hippocampus to Σ, grid cells to G⁰, prefrontal cortex to π;
- for motor control, premotor cortex to ϕ, basal ganglia to Σ, cerebellum and spinal cord to G⁰, M1 to π.

**What it argues, and how well.**
- **Width is redefined.** Def 2.1 adopts the contractive-cell, risk-ε width of [LIT-374](../literature.d/LIT-374.md) and arXiv 2602.07974, while keeping v1's name and citing v1 for the VC separation. Prop 5.4 then uses v1-style connected cells of bounded path length. The two definitions are not shown to agree. Def 2.1's "w ≥ β₁(X) + 1 when f is incompatible with a single contractive chart" is asserted, and is off by one from v1's Thm 4.1.
- **Thm 4.3 (grid-module spacing).** For log-uniform path lengths, the cost E[w log w] is minimised by geometric spacing with r* = R^{1/(M−1)}. Correct, but the ratio is fixed by the endpoint constraint s_M/s₁ = R, not by the cost. Remark 4.6 itself concedes that a linear cost also gives geometric spacing.
- **The headline: "the optimal spacing … is a geometric series whose ratio is determined by the Ω(w log w) sample complexity bound", "matching electrophysiological measurements".** This is **undermined by the paper's own derivation.**
  - The ratio does not depend on the w log w cost.
  - Thm 4.5's capacity constraint, r ≤ c_D·w_max, uses the linear width L/(c_D·s), not w log w.
  - Table 1's predictions run from r* = 1.47 (with M* = 15 modules, against the 4–10 observed) to 2.51, as the free parameter w_max moves from 5 to 10.
  - The "match" is obtained by choosing w_max and then M. Remark 4.6's claim that the observed ratio favours w log w over a linear cost has no derivation behind it.
- **Prior accounts.** Earlier efficiency accounts already derive geometric grid scales: Wei et al. 2015; Mathis et al. 2012; Stemmler et al. 2015, all cited. The paper's reference list misnames the third author of Wei et al. 2015, the eLife "principle of economy" paper. It gives Mehul Bhatt; the third author is Vijay Balasubramanian. It also lists "Navigating social space" as Schäfer & Bhatt, Nature Human Behaviour 2018, which could not be verified here.
- **Prop 3.1 (navigation costs O(w), not Ω(w log w)).** True, but only because exploration is directed rather than i.i.d. sampling. The coupon-collector cost is an artefact of i.i.d. sampling, so the result is close to definitional.
- **Prop 6.2 (architectural decoupling).** True by construction (stop-gradient assumptions).
- **Prop 5.4 and Cor 5.5 (width transfer).** Correct path-subdivision arguments.
- **The anaesthesia prediction.** It is said to be "recently confirmed" by Katlowitz et al. 2026 (Nature; human hippocampus under anaesthesia retains oddball detection, next-word prediction and minutes-scale plasticity, but not consolidation). The prediction first appears in the version that cites the result, so it is an accommodation, not a test.
- **The motor-system dissociations.** Cerebellar ataxia against Parkinsonian selection deficits are known findings, retrodicted.
- **The neural mappings** are asserted.
- **Prior work.** It does not cite the established literature on the same exaptation idea, cognitive maps for non-spatial knowledge built from entorhinal–hippocampal structure (Behrens et al. 2018, "What is a cognitive map?"; Whittington et al. 2020, the Tolman-Eichenbaum Machine). Recalled; not read here.
- **AI-use statement.** None in v2, unlike v1's App. G.

**Verdict on v2 if filed on its own.** Rejected, not worth a reader's time for its claims. Its one quantitative result, the grid ratio, is not driven by the bound it credits; its empirical "confirmation" is post hoc; and its neural mappings restate a known hypothesis without engaging its literature.

## Connections

- **[LIT-373](../literature.d/LIT-373.md) (Li 2026, "The two dragons of cognition").** v1 is the honest repair of [LIT-373](../literature.d/LIT-373.md)'s Urysohn argument.
  - It concedes that global Urysohn separation is trivial (Remark 3.4), which removes [LIT-373](../literature.d/LIT-373.md)'s "linear readout regardless of dimension" claim.
  - It puts the content into a locality constraint instead.
  - Its Urysohn Machine's Evaluate–Detect–Construct cycle, with frozen past experts, is [LIT-373](../literature.d/LIT-373.md)'s Search/Closure/Navigation, made into a definition.
  - It does not engage [LIT-373](../literature.d/LIT-373.md)'s Savitch argument or Theorem 2.

  v2 extends [LIT-373](../literature.d/LIT-373.md)'s neural programme: the "metric slingshot", hippocampal indexing and the anaesthesia dissociation. [LIT-373](../literature.d/LIT-373.md)'s slingshot "through GHL" plausibly corresponds to v2's ϕ trained by spatial prediction, but that is this reader's interpretation. "GHL" remains undefined in all the texts read.
- **[LIT-374](../literature.d/LIT-374.md) (Li 2026, "Structural Decoupling").**
  - v1 supplies the consistent bouquet construction that [LIT-374](../literature.d/LIT-374.md)'s Thm 3.2 lacked. The joint reading's repair holds: safe regions away from the basepoint, as here.
  - v1 shows that [LIT-374](../literature.d/LIT-374.md)'s "width is incomparable with VC dimension" compares an instance with a class (App. B).
  - v1 §9 is the earliest statement of [LIT-374](../literature.d/LIT-374.md)'s decoupling prescription, and it rests on the same equivocation: necessity holds only for learners built from local experts.
  - v2's "anesthesia-mode" grounding is the neuroscience behind [LIT-374](../literature.d/LIT-374.md) §5.3; both cite Katlowitz et al. 2026.
- **arXiv 2602.07974 (StrLT, read alongside).** That paper's Thm 2.1 (strict hierarchy, w = β₁), Thm 2.5 (w ≥ cβ₁L/D₀), Thm 2.6 (Ω(w log w)) and Thm 2.2 restate v1's Thms 4.1, 5.1, 7.1 and 6.1 for a different definition of width (contractive cells with a risk bound, not connected patches with margin). In the restatement the bouquet construction became inconsistent, and the Betti-bound overlap condition was moved to an appendix.
- **[THEORY-019](../theory.d/THEORY-019.md).** Thm 8.5's nerve argument reads homology from the combinatorics of a cover, not from a spectrum. No bearing on its promote_when.
- **[THEORY-028](../theory.d/THEORY-028.md).** Width is a coverage quantity with no algorithm-dependent content. No bearing.
- **Not in the record.** The Urysohn width of Gromov and of dimension theory, which v1 names as its root (refs [9]–[12]), is unrelated in substance: it measures how far a space is from a lower-dimensional one, not a classification instance. Ishiki 2022 (arXiv 2212.13409), a factorisation of metric spaces cited as the "rigorous mathematical basis" of MTF, was not read.

## Bearing on the record

Of the four texts, v1 is the one a reader should take as the programme's formal starting point. Its proofs are correct, its status table is honest, and its own remarks concede the two points a critic would raise: global Urysohn triviality, and that the obstruction is metric. Read with [LIT-373](../literature.d/LIT-373.md), [LIT-374](../literature.d/LIT-374.md) and arXiv 2602.07974, it changes the picture in one respect. The programme's first rigorous object is a covering number under a locality constraint. Everything later (contractive cells, phase transition, decoupling, alignment) inherits the same move: impose locality, then count the local pieces. The programme's claims about architecture are only as strong as the case that real learners must be local in this sense. None of the papers makes that case.

**For ML practice (the Anthology of the SOTA) it carries nothing.** There are no methods or experiments. The architectural conclusion in §9 restates the definition.

## Limitations

- **The headline is topology, the proof is metric.** See C2 and the corrections.
- **Labels play no role.** See C6. Local correctness is automatic, so width measures the safe region's coverage by connected D₀-sets. The claim to measure "the classification problem itself" is accurate only in the sense that γ sizes the safe region.
- **Category comparison in the VC separation**, conceded in App. B. The abstract's "bounded by a constant" overstates Thm 6.1(a).
- **Architectural necessity is definitional.** See C8.
- **Thm 8.5's conditions are not met by the bouquet** (iii), and the general bound is a conjecture.
- **The identifier's current version is a different paper.** See corrections.

## Open questions

- Does local Urysohn width bound the sample or error cost of standard local learners (k-NN, local averaging, kernel methods with bandwidth ~D₀), so that it is a learning-theoretic quantity and not only a covering number?
- Is there a natural condition under which a global learner, a deep network for instance, is effectively local at scale D₀, which would make the architectural reading apply?
- Conj 8.9: does uw ≥ c·β₁ hold without bounded adjacency, under conditions the motivating examples satisfy, that is, with the loops in the safe region itself?

## Corrections to the seeded skim

- none (there was no seed or dossier)
- 'The record and the coordinator''s brief name arXiv 2603.15412 as "Local Urysohn width". That is v1 only. Since 2026-09-14 the identifier serves v2, "The Metric Slingshot: Navigational Reuse as Width-Optimal Structural Decoupling in Continual Learning". v2 is a different paper: it redefines "local Urysohn width" as [LIT-374](../literature.d/LIT-374.md)''s contractive-cell width (v2 Def 2.1), drops v1''s theorems apart from the coupon-collector bound, and adds a grid-cell spacing derivation and neural mappings. A LIT keyed by arxiv:2603.15412 will resolve to v2. The owner must choose one of two options. (a) File v1, as here, with the title and date of v1, and say in the LIT that the identifier now serves another work. (b) Follow [LIT-374](../literature.d/LIT-374.md)''s precedent and file v2 under its own title, with `published:` 2026-09-14. In that case v1 has no separate identifier and should be named in prose. This reading supports either, since both versions were read in full.'
- 'The abstract says that width grows "while VC dimension is bounded by a constant". The body does not show this. Thm 6.1(a) gives a class with VC(H_w) ≤ w log₂ w, which grows with w, and Appendix B concedes that "VC(H_w) grows with w". Remark 7.2 then says the local classifiers have "VC dimension ≤ 1 (Theorem 6.1(a))", which Thm 6.1(a) does not state.'
- 'The abstract and §9 say topology "forces classifier complexity". The paper''s own Remark 8.11 says the obstruction "is metric (diameter bound) rather than cohomological". The bouquet''s safe region is a union of disjoint arcs with β₁ = 0, so App. E''s claim that the bouquet satisfies Thm 8.5''s condition (iii) does not hold. Thm 4.1''s lower-bound proof uses only geodesic distances through the wedge point. The same argument gives width w on a star-shaped tree with w arms, where β₁ = 0.'
