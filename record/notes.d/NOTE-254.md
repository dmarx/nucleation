---
number: 254
status: Read
formerly:
- NOTE-tmp07tuj
paper: LIT-281
title: 'Logical and Topological Contextuality in Quantum Mechanics and Beyond'
version: 1
history:
- version: 1
  date: '2026-09-27'
  note: >-
    Read in full (The full text of Giovanni Carù's DPhil thesis, "Logical
    and Topological Contextuality in Quantum Mechanics and Beyond"
    (University of Oxford, title page "Hilary 2019", supervisor Samson
    Abramsky). Source: the thesis PDF in the Oxford University Research
    Archive (ORA, CC BY, DOI 10.5287/ora-kznbp4k4y, which resolves to the
    ORA record). It is byte-identical to the copy on Aleks Kissinger's
    Oxford theses page. 223 PDF pages: xii front-matter pages, then pp.
    1–211. The PDF is dated 14 Aug 2019. ORA gives the year only (citation
    date "2019") and a deposit date of 2019-11-11, so `published:` uses the
    deposit date. `pdftotext` was not available, so I extracted the text
    with PyMuPDF. Where extraction lost tables or formulae, I checked them
    against rendered pages. What I read and how closely: - *Read closely,
    line by line.* Ch III (the cohomology chapter, pp. 39–58), Ch IV (the
    line-model chapter, pp. 59–98, including every worked system of
    equations) and Ch VIII (Conclusion). I diffed Ch IV against the 2018
    preprint (arXiv 1807.04203, LIT-280) passage by passage at every point
    NOTE-253 flagged. - *Read in full, less closely.* Front matter,
    abstract, Ch I (Introduction) and Ch II (Background). All of Ch V
    (valuation algebras, disagreement, inference algorithms), with close
    attention to §§7–10 and the complexity bounds, checked against rendered
    pp. 146 and 152. - *Skim-read, as permitted: Ch VI (AvN triples for
    stabiliser states, pp. 155–171) and Ch VII (minimum resources for strong
    non-locality, pp. 173–190).* Neither touches the cohomology programme.
    For each I read the overview, the statements of every numbered
    definition, theorem, proposition and corollary, and the discussion. I
    did not check any proof in them. - *Not read.* The bibliography, list of
    symbols and index, beyond individual entries I looked up. I re-ran the
    car2 reader's GF(2) scripts for three purposes: to test the thesis's
    definitions, which are identical to the preprint's (details under Key
    results); to recompute the level-0 solution space of the §8 cover; and
    to re-verify the witness families.). The first NOTE on this paper, which
    was seeded from its abstract alone.
date: '2026-09-27'
summary: >-
  The thesis's cohomology chapters republish the 2017 and 2018 papers with
  the "joint model" renamed the "line model". The definitions, Thm IV.32
  (complete on cyclic scenarios at level |M|−1), Prop IV.34, Thm IV.36 and
  Conjecture IV.41 carry over unchanged. So does every defect found in the
  preprint. Under the thesis's own Def IV.26, the §8 Kochen–Specker cover
  of Abramsky–Mansfield–Barbosa is still detected on only 6 of 15 sections
  at levels 0–3 (my recomputation), and a lifted ℤ/2 family shows it is
  never fully detected at any level. The context-wise reading the worked
  examples use detects all 15 sections at level 2. The genuinely new
  material lies outside the cohomology programme: a probabilistic
  line-model construction (§IV.7), a valuation-algebra "theory of
  disagreement" with inference algorithms (Ch V, bound O(k^n·l^{k(n−1)+1})
  on (n,k,l) scenarios), and the AvN-triple characterisation of stabiliser
  states (Ch VI).
---

# NOTE-254: Logical and Topological Contextuality in Quantum Mechanics and Beyond

## Contribution

The thesis collects five pieces of work.

- **Ch III (sole author; = [LIT-279](../literature.d/LIT-279.md)).**
  - *The counterexample.* A strongly contextual (2,2,4) model on which the Čech obstruction vanishes everywhere, which refutes AMB's Conjecture 8.1.
  - *Higher obstructions.* Odd-degree obstructions form a hierarchy, and all of them vanish for no-signalling models.
  - *Torsors.* A torsor description of Ȟ¹.
- **Ch IV (sole author; = [LIT-280](../literature.d/LIT-280.md), renamed).**
  - *The construction.* The "line model" S^(k), an iterated pullback of adjacent contexts.
  - *The completeness theorem.* ℤ/2 cohomology of S^(|M|−1) is complete for logical and strong contextuality on cyclic scenarios.
  - *Its extension.* To models with the "cyclic contextuality property", together with the conjecture that some level is complete for every model.
  - *New in the thesis (§7).* A probabilistic line model. It reproduces the original marginals, and contextuality of e implies contextuality of e^(1).
- **Ch V (joint with Abramsky; partly published as Abramsky & Carù 2019, Phil. Trans. R. Soc. A, "Non-locality, contextuality and valuation algebras", not in the record).**
  - *The reformulation.* Contextuality recast as "local agreement, global disagreement" of a knowledgebase in a valuation algebra.
  - *The reduction.* Logical and strong contextuality become inference problems.
  - *The algorithms.* Fusion and collect algorithms, with complexity bounds on (n,k,l) scenarios.
- **Ch VI (joint; = Abramsky–Barbosa–Carù–Perdrix 2017, DOI 10.1098/rsta.2016.0385, not in the record).** A maximal stabiliser subgroup is AvN iff it contains an AvN triple. Every such argument reduces to a three-qubit GHZ one.
- **Ch VII (joint; = Abramsky et al., TQC 2017, DOI 10.4230/LIPIcs.TQC.2017.9).**
  - *Excluded classes.* No two-qubit state, and no W-class state, is strongly non-local.
  - *The GHZ class.* Within it, strong non-locality requires balanced states and can be witnessed with equatorial measurements.
  - *A new family.* An infinite family of strongly non-local three-qubit states.

What the thesis does **not** add to the cohomology programme:
- no completeness theorem beyond cyclic scenarios;
- no repair of Prop 8.2 / IV.34;
- no progress on the general conjecture;
- no cost analysis of the line-model invariant.

## Key insight

- *The picture the thesis installs.* Contextuality is local consistency without global consistency (the Escher staircase, Ch I). Čech cohomology fails to see it exactly when a ℤ-linear "twisted loop" closes where no genuine loop does.
- *The Ch IV fix.* Change the space, not the cohomology. Pull back adjacent contexts until a Z-shaped false loop can no longer sit inside one context.
- *The Ch V fix.* Leave topology behind. Contextuality is global disagreement of locally agreeing information, so deciding it is a standard inference problem. It can be solved exactly by local computation, whose cost is governed by treewidth.
- *How the two relate.* The thesis never connects them. Ch V gives an exact decision procedure for logical and strong contextuality on every scenario, which the Ch IV invariant has only on cyclic ones.

## Assumptions

- **Framework (Ch II), as in [LIT-016](../literature.d/LIT-016.md), [LIT-277](../literature.d/LIT-277.md) and [LIT-278](../literature.d/LIT-278.md).**
  - *Scenario.* ⟨X, M, (O_m)⟩, with X finite, M a connected antichain cover and finite outcome sets.
  - *Possibilistic model.* A subpresheaf S ⊆ E that is non-empty on contexts, flasque beneath the cover (possibilistic no-signalling), and whose compatible families glue (Def II.12).
  - *LC and SC* as in Def II.15.
- **Cohomology (Ch II §6).**
  - *Coefficients.* F = F_R S with R = ℤ or ℤ/2, and in Ch IV F^(k) := F_{ℤ₂} S^(k) (IV.3).
  - *The obstruction.* The relative γ_{C0} via the snake lemma, with Prop II.30 (γ(r0) = 0 iff r0 lies in a compatible F-family) and Thm II.32 (CLC ⇒ LC, CSC ⇒ SC).
- **Line scenarios (Def IV.1, IV.3).**
  - *Definition.* X^(1) = M; M^(1) = {{C, C′} : C ≠ C′, C ∩ C′ ≠ ∅}; O^(1)_C = E(C).
  - *Iteration.* Iterated k times. For k ≥ 2 this is the line graph of the previous graph.
  - *Excluded case.* |M^(k)| ≥ 2 for all k is assumed (Remark IV.4, via Vorob'ev).
- **Cyclic scenario (Def IV.20).** M^(1) is a chordless cycle.
  - *Cycles in general may be chordal.* "Cycles" in Def IV.17 may have chords; chordless ones are singled out.
  - *Where the difference bites.* The CCP (Def IV.33) quantifies over the general ones, while Thm IV.32 needs chordless ones.
- **Def IV.26 (universal).** CLC^(k)(S, s) iff CLC(S^(k), t) for every section t of S^(k) with s ∈ flatten(t). The proof of Thm IV.32 uses this form: its negation yields some t ∋ s with vanishing γ.
- **Probabilistic line model (Def IV.37).** e^(1)_{C1,C2}(s, t) = e_{C1}(s)·e_{C2}(t)/I when s and t agree on C1 ∩ C2 and I ≠ 0, and 0 otherwise, where I is the common marginal on the overlap.
  - *What this assumes.* The two contexts are conditionally independent given the overlap.
- **Ch V.**
  - *Valuation algebras (Shenoy–Shafer axioms A1–A6).* Information algebras add A7–A9.
  - *Adjointness.* The contextuality results need "adjoint" ordered valuation algebras (Defs V.21, V.22) for the reduction to inference (Prop V.24).
  - *Complexity.* Stated for (n,k,l) Bell scenarios only. In general the bounds depend on an unbounded treewidth ω.

## Key results

**Ch III (= [LIT-279](../literature.d/LIT-279.md); see [NOTE-252](NOTE-252.md) for the checks).**
- **§3 (Table III.4).** A strongly contextual (2,2,4) model with vanishing obstruction on every section refutes Conjecture III.1 (AMB Conj. 8.1). This is confirmed in [NOTE-252](NOTE-252.md).
- **Thm III.6.** CLC_{q+1} ⇒ CLC_q (proof).
- **Thm III.7.** Every no-signalling model is cohomologically q-non-contextual for all q > 0 (proof).
- **Prop III.8.** CSC ⇔ every γ_C is injective. This is false in the "only if" direction ([NOTE-252](NOTE-252.md)), and it is restated here uncorrected.
- **Prop III.9.** Some γ_{C0} injective ⇒ SC (proof).
- **Prop III.12.** Trs(M, F) ≅ Ȟ¹(M, F) (proof; a standard correspondence).
- **§3, the AMB §8 system.** It is new in this chapter relative to Car17, and wrong (corrections).

**Ch IV (= [LIT-280](../literature.d/LIT-280.md), renamed; see [NOTE-253](NOTE-253.md) for the checks). Numbering map:**

| Thesis | Preprint | Status |
|---|---|---|
| Prop IV.7 | Prop 4.6 | unchanged |
| Prop IV.11 | Prop 5.1 | unchanged |
| Cor IV.12, IV.14, IV.15 | Cors 5.2, 5.4, 5.5 | unchanged |
| Def IV.13, IV.26 | Defs 5.3, 7.1 | unchanged |
| Thm IV.27 | Thm 7.2 | unchanged |
| Lemma IV.29, IV.30 | Lemmas 7.4, 7.5 | unchanged |
| Thm IV.31 | Thm 7.6 | unchanged |
| Thm IV.32 | Thm 7.7 | unchanged |
| Def IV.33 | Def 8.1 | unchanged |
| Prop IV.34 | Prop 8.2 | reworded ("any contextual cycle") |
| Prop IV.35 | Prop 8.3 | unchanged |
| Thm IV.36 | Thm 8.4 | unchanged |
| Conjecture IV.41 | Conjecture 9.1 | unchanged |

- **Thm IV.32 (proved; holds).** On a cyclic scenario with n := |M| − 1:
  - LC(S, s) ⇔ CLC^(n)(S, s);
  - SC(S) ⇔ CSC(S^(n)).
- **My re-run under Def IV.26, which is literally the preprint's definition.** Every figure matches [NOTE-253](NOTE-253.md).

  | Model | Def IV.26 counts, levels 0→3 | Other |
  |---|---|---|
  | Hardy | 0, 0, 0, 1 of 13 | only the one LC section |
  | Carù 2017 (2,2,4) | 0, 0, 0, 22 of 22 | CSC(S^(3)) true |
  | Table IV.1 | 2, 2, 2, 5 | 5 LC |
  | Table IV.4 | 4, 4, 4, 7 | 7 LC |

  - *Table IV.1.* The thesis says level 1 detects s₂ "although |M| = 4" (p. 83). That holds only under the context-wise reading: 4 sections detected at level 1 under that reading, against 2 under Def IV.26.
- **Prop IV.34 (false as stated).** It still claims LC(S, s) ⇔ CLC^(n−1)(S, s) for any contextual cycle of size n.
  - *The counterexample.* On Table IV.4, s₁₀ = (b,d) ↦ (1,1) has contextual 3-cycles only (two triangles, my check). Yet the level-2 section built over ab–bd–cd that contains s₁₀ has vanishing γ.
  - *Verification.* I re-found an explicit compatible family through it and verified it independently on every overlap.
  - *Where the proof fails.* Its "readily implies" step (p. 88) is still unargued.
- **Thm IV.36 (unproved; rests on IV.34).** With CCP and N the largest cycle in M^(1): LC ⇔ CLC^(N−1) and SC ⇔ CSC(S^(N−1)).
- **The AMB §8 cover under the thesis's definitions (my computation, reusing the car2 scripts unchanged, because the definitions are unchanged).**
  - *Counts.* Def IV.26 detects 6/15 sections at each of levels 0, 1, 2 and 3. CSC(S^(k)) is false at every level. The contexts number 5, 10, 30, 150; the sections 15, 48, 227, 1782.
  - *Every level.* The ℤ/2 family ABC ↦ s_A, BDE ↦ s_D, CDE ↦ s_D, ADF ↦ s_A + s_D + s_F, AEG ↦ s_A lifts to a compatible family on S^(k) for k = 1–4 (re-verified; 177 of the 1350 level-4 contexts carry a single genuine section containing s_{ABC,A}). So CLC^(k)(S, s_{ABC,A}) fails for every k, and Conjecture IV.41 is false as stated. This is my computation and [NOTE-253](NOTE-253.md)'s; the thesis claims the opposite (§6.1: level 1 "removes" the false negatives).
  - *Under the context-wise reading.* Call s detected when some level-k context has every t ∋ s detected. This reading detects 6, 12, 15 and 15 sections at levels 0–3, so the whole model at level 2.
  - *Whose computation.* The thesis nowhere states this reading, although its worked examples compute it. The result is my computation.
  - *Where the model sits relative to the CCP.* The only chordless cycles of its K₅ intersection graph are triangles, and 11 of 15 sections are LC on none of them (re-run). So on the chordless reading the Prop IV.34 proof needs, the model lacks the CCP. The claim that "the author has not been able to find any example of an empirical model which does not satisfy this property" (p. 88, new in the thesis) is contradicted by the thesis's own §6.1 example. On the chordal reading it has the CCP, and Thm IV.36 is false for it.
- **Prop IV.38, Thm IV.40 (new; proved; I read the proofs).**
  - *Prop IV.38.* e^(1) is a well-defined no-signalling model whose marginals on each original context equal e_C.
  - *Lemma IV.39.* A global distribution for e^(1) vanishes on incompatible families.
  - *Thm IV.40.* e contextual ⇒ e^(1) contextual. The converse fails (the thesis says so).
  - *What is not given.* No cohomological or quantitative use is made of it.

**Ch V (joint with Abramsky).**
- **The reformulation.**
  - *Thm V.20 (proof, essentially definitional).* e is contextual iff the knowledgebase {e_C} of R-potentials disagrees globally.
  - *Prop V.27.* Probabilistic contextuality ⇔ complete disagreement in the algebra of sets of distributions.
  - *Prop V.29 (proof).* For indicator functions, LC(S) ⇔ global disagreement and SC(S) ⇔ complete disagreement.
  - *Prop V.30.* SC is one inference problem, (⊗_C i_{S(C)})^{↓C} = z_C. LC needs up to |M| of them.
- **Examples.** Relational databases, a breast-screening-guidelines example taken from [ZG18], ℤ₂ linear systems, map 3-colouring (Example V.18), and liar cycles (Example V.19). All are presented as locally agreeing and globally disagreeing knowledgebases.
- **Complexity (proved from standard local-computation bounds).**
  - *General scenario, fusion algorithm.* SC in O((|M| + |X|)·|O|^{ω+1}); LC adds a factor |M| (V.36, V.37).
  - *(n,k,l) scenarios.* The optimal treewidth is ω* = k(n−1) (argued, §10.5.4). Fusion gives SC in O(k^n·l^{k(n−1)+1}) (V.39) and LC in O(k^{2n}·l^{k(n−1)+1}) (V.40). Collect gives both in O(k^n·l^{k(n−1)+1}) (p. 152).
  - *The claimed improvement.* The claim is that these beat the "state of the art", taken as O(l^{εnk}) for LP-based probabilistic detection (V.27) and O(2^{δ(kl)^n}) for SAT-based possibilistic detection (V.29).
  - *Not implemented.* The algorithms were never implemented ("due to time constraints", p. 193).

**Ch VI (skimmed; statements only, proofs not checked).**
- **Thm VI.13 (AvN triple theorem).** A maximal stabiliser subgroup of P_n is AvN iff it contains an AvN triple. The argument reduces to three qubits whose induced state is LC-equivalent to GHZ.
- **Cor VI.14.** A graph state is "strongly contextual" (in context, via AvN) iff its graph has a vertex of degree ≥ 2.
- **Cor VI.15.** Every strongly contextual three-qubit stabiliser state is LC-equivalent to GHZ.
- **Prop VI.20.** A closed count of AvN triples in P_n.

**Ch VII (skimmed; statements only).**
- **Thm VII.1.** No two-qubit state is strongly non-local.
- **Thm VII.3.** No W-class state is strongly non-local.
- **Thm VII.4.** GHZ(n) strong non-locality is witnessed by equatorial measurements.
- **Thm VII.7.** A strongly non-local GHZ-class state must be "balanced".
- **Prop VII.8.** No strong non-locality if λ₁ + λ₂ + λ₃ > π/2.
- **Thm VII.9.** An infinite family, not LU-equivalent to GHZ, that is strongly non-local with N = 2m settings on two parties.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The ordinary Čech obstruction is not complete even for strong contextuality, even on a symmetric connected (2,2,4) cover | strong (explicit model; confirmed in [NOTE-252](NOTE-252.md)) | Ch III §3, Table III.4 |
| C2 | Higher (odd-degree) obstructions vanish for every no-signalling model at q > 0 | strong (proof) | Thm III.7 |
| C3 | CSC ⇔ every γ_C injective | false in the "only if" direction ([NOTE-252](NOTE-252.md), PR box); restated uncorrected | Prop III.8 |
| C4 | On cyclic scenarios, LC ⇔ CLC^(\|M\|−1) and SC ⇔ CSC(S^(\|M\|−1)) | strong (proof; re-confirmed on Hardy, Carù 2017, Table IV.1) | Thm IV.32; my re-run |
| C5 | The bound \|M\| − 1 is tight (Hardy needs level 3) | strong (example; re-confirmed) | §5.3 |
| C6 | Table IV.1 is already detected at level 1 | true only under the unstated context-wise reading; Def IV.26 needs level 3 | p. 83; my re-run |
| C7 | With the CCP, LC ⇔ CLC^(n−1) for any contextual cycle of size n | false (Table IV.4, s₁₀, n = 3, explicit family) | Prop IV.34; my re-run |
| C8 | With the CCP, LC ⇔ CLC^(N−1), N the largest cycle in M^(1) | unproved (rests on C7); false for AMB §8 if the CCP admits chordal cycles | Thm IV.36 |
| C9 | All models in the literature have the CCP; the author knows of no model without it | false on the chordless reading, for the thesis's own AMB §8 example (11/15 sections LC on no chordless cycle) | p. 88 |
| C10 | The first line model removes every false negative of the AMB §8 cover | false (explicit compatible family through (s_{ABC,A}, s_{AEG,A}); the level-0 system has a wrong equation) | §6.1, §III.3; my re-run |
| C11 | Only one "false" compatible ℤ/2 family exists at level 0 for AMB §8 | false (3-dimensional solution space; 9 of 15 sections have vanishing γ) | §6.1 (new sentence); my computation |
| C12 | Conjecture IV.41: some k makes CLC^(k) complete for every model | refuted as stated (AMB §8, s_{ABC,A}, every k) | p. 98; lifting argument, [NOTE-253](NOTE-253.md) and my re-run |
| C13 | The invariant's "practical computability is not compromised" | weak (assertion; no analysis of line-model size, which grows like iterated line graphs: 5, 10, 30, 150, 1350 contexts for AMB §8) | §IV.1, p. 60 |
| C14 | The probabilistic line model preserves marginals, and contextuality of e implies contextuality of e^(1) | strong (proof) | Prop IV.38, Thm IV.40 |
| C15 | Contextuality ⇔ global disagreement; SC ⇔ complete disagreement for indicator functions | strong (proof; close to a restatement of the definitions) | Thm V.20, Prop V.29 |
| C16 | Collect/fusion detect logical non-locality in O(k^n·l^{k(n−1)+1}) on (n,k,l) scenarios, "significantly faster than the current state of the art" | bound: argued from standard local-computation bounds. Comparison: weak, because the baseline O(2^{δ(kl)^n}) is not the natural one (my remark: enumerating the l^{nk} global assignments already costs only O(k^n·l^{nk})); no implementation | §10.5–10.8, (V.29) |
| C17 | A maximal stabiliser subgroup is AvN iff it contains an AvN triple; every AvN argument reduces to three-qubit GHZ | proof in the thesis (not checked here; published as ABCP17) | Thm VI.13 |
| C18 | Strong non-locality needs at least three qubits and, for three qubits, the GHZ SLOCC class | proof in the thesis (not checked here; published TQC 2017) | Thms VII.1, VII.3, VII.7 |

## Method

- **Ch III–IV.** Čech cochain algebra and the snake lemma.
  - *Line models.* Built as iterated pullbacks, with combinatorics of paths and chordless cycles in iterated line graphs (§4).
  - *The no-Z lemma* over ℤ/2 (Lemma IV.29).
  - *An induction* that trades path length for level (Thm IV.31).
  - *Worked examples* by bundle diagrams and hand-written or machine-solved ℤ/2 systems (§§5.3, 6.1).
- **Ch V.** Valuation-algebra axiomatics, ordered/adjoint algebras, and variable elimination (fusion) and message passing (collect) on join trees, with complexity measured by treewidth.
- **Ch VI.** Graph states and local complementation.
- **Ch VII.** Explicit hemisphere-type global assignments.
- **My re-check.**
  - *The same code as [NOTE-253](NOTE-253.md).* The line model built literally from Defs IV.1 and IV.5; ℤ/2 compatibility systems; Def IV.26 and the context-wise variant evaluated per section.
  - *Independent verification.* Every witness family was verified independently on all overlaps.
  - *The level-0 space for AMB §8.* Computed by GF(2) kernel.

## Concepts

- **Line scenario / line model, S^(k)** — the thesis's name for the preprint's "joint" construction (footnote 2, p. 63). For k ≥ 2, M^(k) is the line graph of M^(k−1).
- **Non-proper 3-cycle** — a 3-cycle in M^(k) generated by a star in M^(k−1), the Whitney exception (§4.1.1).
- **Cohomology loop / non-standard loop** — a signed Z-shaped path inside a context that yields a false negative (§2.1).
- **n-partial family; standard form** — Def IV.28.
- **Cyclic contextuality property (CCP)** — Def IV.33.
- **Probabilistic line model** — Def IV.37.
- **Local / global / complete disagreement; truth valuation** — Defs V.14 and V.26. Contextuality instantiates them in the R-potential and indicator algebras.
- **AvN triple** — Def VI.7/VI.18.
- **Balanced GHZ-SLOCC state** — Def VII.5.

## Connections

- **[LIT-279](../literature.d/LIT-279.md) (Carù 2017, [NOTE-252](NOTE-252.md)).** Ch III reproduces it, including the Prop 6.1 error (now Prop III.8) and the Def 5.3 typo (now Def III.4). The added material is the AMB §8 level-0 system with its wrong equation.
- **[LIT-280](../literature.d/LIT-280.md) (Carù 2018, [NOTE-253](NOTE-253.md)).** Ch IV reproduces it with a new name and one reworded proposition (IV.34). Two things are new: the §7 probabilistic line models, and two sentences (the "no model without CCP" claim, and the "unique false family" claim), both false. Every [NOTE-253](NOTE-253.md) finding carries over:
  - Thm IV.32 correct;
  - Prop IV.34 false;
  - Table IV.4's cycle size wrong;
  - §6.1 wrong at levels 0 and 1;
  - Conjecture IV.41 refuted.
- **[LIT-277](../literature.d/LIT-277.md) (AMB 2011, [NOTE-250](NOTE-250.md)).** The §8 cover is still the test case. [NOTE-250](NOTE-250.md)'s 9/15 count is right; the thesis's four-section account is not.
- **[LIT-278](../literature.d/LIT-278.md) (ABKLM 2015, [NOTE-251](NOTE-251.md)).** It supplies the AvN framework, which Ch VI completes for stabiliser states by proving the "AvN triple conjecture" for maximal subgroups.
- **[LIT-016](../literature.d/LIT-016.md) (Abramsky & Brandenburger).** It supplies the framework.
- **[LIT-265](../literature.d/LIT-265.md) (contextual fraction).** Reviewed in Ch V §10.1.1 as the LP-based detection method. There is no new result about it.
- **Not in the record (unverified here).**
  - Abramsky, Gottlob & Kolaitis (IJCAI 2013): recognising non-locality in n-partite Bell scenarios is NP-complete. The thesis cites it (p. 136), which confirms [NOTE-253](NOTE-253.md)'s recollection as far as the citation goes.
  - Abramsky & Carù 2019 (Phil. Trans. A; Ch V).
  - ABCP17 (Ch VI).
  - Abramsky et al., TQC 2017 (Ch VII).
  - Roumen's order-cohomology invariant (described as false-negative-free but impractical, p. 59).
  - Okay et al.'s group-cohomological approach.
- **Anthology.** No ANTH- citation is warranted.

## Bearing on the record

- **[THEORY-012](../theory.d/THEORY-012.md) (Active).** The cohomology bullet's content is unchanged by this reading. The thesis is the later, consolidated statement of [LIT-279](../literature.d/LIT-279.md) and [LIT-280](../literature.d/LIT-280.md). It adds no theorem beyond cycles, and it restates the refuted conjecture as open. What changes is the provenance: a reader who meets "Carù's thesis proves an (almost) complete cohomological invariant" should find the record already saying why "almost" is doing too much. Exact wording under the report's "[THEORY-012](../theory.d/THEORY-012.md) proposal".
- **A second route to completeness, from the thesis itself.** Ch V decides logical and strong contextuality exactly on any scenario, by local computation on join trees. Its cost is exponential only in the treewidth.
  - *The contrast.* The line-model invariant is exact only on cycles, and its size grows like iterated line graphs.
  - *Consequence for [THEORY-012](../theory.d/THEORY-012.md).* This does not bear on [THEORY-012](../theory.d/THEORY-012.md)'s claim, which concerns what the exact criterion is. It reinforces the bullet's framing that cohomology is a relaxation of an exact criterion that is decidable by other means.
- **[THEORY-014](../theory.d/THEORY-014.md) (Proposed).** No change. The no-Z mechanism is exactly as in [NOTE-253](NOTE-253.md).
- **ML practice.** Nothing. Ch V's use of generic inference (junction trees, treewidth) is the same local-computation machinery as exact inference in graphical models. That is a shared technique, not a recommendation for practice.
- **For filing.**
  - *Tags.* Tags `contextuality`, `quantum-foundations`, `mathematics` mirror [LIT-277](../literature.d/LIT-277.md)–280. `logic` is justified by Ch V's propositional and predicate information algebras and its liar-cycle example.
  - *Lineage.* It contains [LIT-279](../literature.d/LIT-279.md) and extends [LIT-280](../literature.d/LIT-280.md), but it does not supersede either for a reader: the content is the same, and the short papers are easier to cite by result. Suggest a relation noting that Chs III–IV reprint [LIT-279](../literature.d/LIT-279.md) and [LIT-280](../literature.d/LIT-280.md).

## Limitations

- **The headline "(almost) complete cohomological characterisation" (abstract, p. vii) and "complete cohomology invariant" (Conclusion, p. 192) outrun the body.**
  - *Proved.* Completeness on cyclic scenarios.
  - *Unproved.* The extension (Thm IV.36) rests on a false proposition.
  - *Refuted.* The universal conjecture, by the thesis's own non-cyclic example.
- **The definitions and the examples still disagree.**
  - *Which is which.* The theorems use universal Def IV.26. The examples (Table IV.1, Table IV.4, the KS cover) check one chosen context.
  - *What the context-wise version does.* It is sound and detects more, including all of AMB §8 at level 2 (my computation). It is never stated, so neither its soundness nor its completeness is addressed.
- **New unsupported sentences.** Two, both false:
  - no model without the CCP is known (p. 88);
  - the §8 cover has a unique false ℤ/2 family (p. 91).
- **No cost analysis of line models.** The claim that "practical computability is not compromised" is asserted, as in the preprint. Ch V's complexity analysis concerns different algorithms.
- **Ch V's comparison with the "state of the art" uses an inflated SAT baseline.** O(2^{δ·Σ_C|E(C)|}) applies a variable-count bound to clause count. Direct enumeration of global assignments is far cheaper than that baseline. The improvement over enumeration is modest, a factor of about l^{k−1} on (n,k,l) scenarios (my remark). No implementation or benchmarks.
- **The probabilistic line model is untested.** It is defined and shown to be sound one way. No example, and no link to the cohomological or contextual-fraction measures.
- **Chs VI–VII were skimmed, and their proofs are unchecked here.** They are published joint work.
- **Slips.**
  - Car17's arXiv id is given as 1701.00242 (the proceedings volume).
  - "f = b1" in the level-1 KS system.
  - "Theferefore" (p. 82).
  - "(IV.18)" referenced in Ch III's Table III.2 caption before it is defined.
  - "consitututes" in the abstract.
  - Fig IV.17's caption cites "[Car17]" for a Ch III model.

## Open questions

- **Is the context-wise variant complete for all finite models at some level?** It is sound, complete on cycles (it is implied by Def IV.26), and detects AMB §8 at level 2. A proof or a counterexample would settle what Chapter IV set out to do.
- **Is Thm IV.36 true under a chordless CCP and the context-wise reading?** The Table IV.4 counterexample to Prop IV.34 does not refute it.
- **Ch V versus Ch IV.** Can the treewidth bound of Ch V be matched by a cohomological certificate, a "cohomology of join trees"? The thesis's own discussion (p. 153) floats extending the invariant to valuation algebras, but nothing is done.
- **Is Ch V's reduction to inference strictly better than standard CSP solving for contextuality?** Given the Abramsky–Gottlob–Kolaitis correspondence between contextuality and CSP, it is unclear what the valuation-algebra route adds beyond the treewidth bound known for CSPs. Unverified.

## Corrections to the seeded skim

- **No skim dossier existed for this work.** There was no dossiers3 entry for car3, so what follows corrects what the record expected of the thesis.
- **[NOTE-253](NOTE-253.md)'s open question ("Does the thesis repair §8 or Conjecture 9.1?") is answered: no.** Ch IV is the preprint re-issued with two changes. "Joint" becomes "line" (footnote 2, p. 63, citing a remark of Roberson's), and "false positive" becomes "false negative" (footnote 2, p. 42).
  - *Unchanged.* Def 7.1 ↦ Def IV.26 is still the universal definition: CLC^(k)(S, s) iff CLC(S^(k), t) for **every** section t of S^(k) with s ∈ flatten(t). It is not changed to the context-wise version.
  - *Carried over verbatim.* Thm 7.7 ↦ Thm IV.32; Prop 8.2 ↦ Prop IV.34; Thm 8.4 ↦ Thm IV.36; Conjecture 9.1 ↦ Conjecture IV.41. The conjecture is restated as "an open question" (p. 98), neither proved for any new class nor withdrawn.
  - *Prop IV.34's wording.* It now says "the size of **any** contextual cycle of s" (the preprint said "the contextual cycle"). That makes it stronger, not weaker, and it is still false on the thesis's own Table IV.4 model (= the preprint's Table 5).
- **The §8 Kochen–Specker analysis keeps both of its errors and gains a new false sentence.**
  - *Moved into Ch III.* The level-0 ℤ/2 system now sits in Ch III §3, which is said to be "published in [Car17]" (p. 41), although Car17 does not contain it. It keeps the wrong equation "a ⊕ c = d ⊕ f" (should be a ⊕ c = e ⊕ f) and the conclusion that there are only two free variables.
  - *My recomputation.* The correct solution space has dimension 3, with basis {b,c,d,e,g,h,k,l}, {a,b,c,d,g,j,m} and {b,c,d,f,g,i,n,o}. The obstruction vanishes on 9 of 15 sections ([NOTE-250](NOTE-250.md)'s count).
  - *New sentence, false.* Ch IV §6.1 (p. 91) adds that the other compatible ℤ/2 families "contain exclusively sections of F that are not in S", so that (IV.19) is "the unique false compatible family". The basis vector {a,b,c,d,g,j,m} is a compatible family that is a single genuine section on BDE, CDE, ADF and AEG. So s_{BDE,B}, s_{CDE,C} and s_{AEG,A} are also false negatives, beyond the four the thesis lists.
  - *Level 1.* The level-1 system (including the "f = b1" slip) and the "0 = u = a ⊕ b ⊕ t" contradiction are reproduced unchanged. The contradiction is refuted by the explicit compatible family through (s_{ABC,A}, s_{AEG,A}), which I re-verified on every overlap.
- **Table IV.4 ("The size of the largest cycle in this scenario is 4", p. 90) is still wrong.** The 5-cycle ab–ad–cd–bc–bd is Hamiltonian, so Thm IV.36's level for this model is 4, not 3.
- **Ch III carries [LIT-279](../literature.d/LIT-279.md)'s defects over.**
  - *Prop III.8 (= [LIT-279](../literature.d/LIT-279.md)'s Prop 6.1).* "CSC iff every γ_C is injective", and the bound |Ȟ¹| ≥ |F(C0)| drawn from it, are restated unchanged. [NOTE-252](NOTE-252.md) found the "only if" direction false (PR box).
  - *Def III.4.* It still writes Ȟ^{2q+1}(M, F) for Ȟ^{2q+1}(M, F_{C̃0}).
- **Identification.**
  - *The author's department listing.* The HTML publications page lists six works and not the thesis. The department's BibTeX export lists it as @phdthesis "CaruDPhil2019". [NOTE-253](NOTE-253.md)'s "the same page lists his DPhil thesis" is true of the BibTeX listing only.
  - *A wrong identifier in the thesis's bibliography.* It gives Car17 as arXiv:1701.00242. That is the QPL 2016 proceedings volume. The paper itself is 1701.00656, as [LIT-279](../literature.d/LIT-279.md) records.
