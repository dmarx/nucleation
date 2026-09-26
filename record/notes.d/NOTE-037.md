---
number: 37
status: Read
formerly:
- NOTE-tmp6uvet
paper: LIT-067
title: 'Debreu 1952, a social equilibrium existence theorem'
version: 2
history:
- version: 2
  date: '2026-09-25'
  note: >-
    Read in full (the whole article, PNAS 38(10):886–893. The brief's "4
    pp." is wrong: the article starts in the lower half of p. 886 and ends
    at the top of p. 893, about 6½ printed pages. I read it from
    rawC4/c43u.pdf, an 8-page archival scan (PDF 1.3, "Apex PDFWriter",
    2005) that also carries the tail of the preceding number-theory note and
    the head of Kundert's following note. The text layer is OCR. I checked
    the Theorem, Definition, Lemma, proof and Remark against rendered page
    images of pp. 888–889 (rawC4/c43_p2.png, c43_p3.png). I read the
    introduction, §1 Topological Concepts, §2 Equilibrium Points
    (Definition, Theorem, Lemma, proof, continuity Remark and its proof), §3
    Saddle Points and MinMax Operator (Corollary and results (a)–(d)), §4
    Historical Note, the footnotes (*, †) and references 1–11. Nothing was
    skipped.). Upgraded from `Skimmed` to `Read`: the claims table,
    assumptions and results are new, and the skim is corrected where the
    full text disagreed.
date: '2026-09-25'
summary: >-
  Debreu proves existence of an equilibrium for an "abstract economy"
  (generalized game), in which each agent's feasible set A_ι(ā_ι) depends
  on the others' actions. The conditions: each action set 𝔄_ι is a
  contractible polyhedron; A_ι has a closed graph with non-empty compact
  values; f_ι is continuous on the graph into the extended reals; the
  value function φ_ι(ā_ι) = max f_ι is continuous; and each best-response
  set M_ā_ι is contractible. The proof applies the
  Eilenberg–Montgomery/Begle fixed-point theorem to the product
  best-response map. A Remark replaces the joint continuity of φ_ι with
  continuity (lower hemicontinuity) of A_ι plus a compact graph. A
  Corollary gives a saddle-point theorem that contains Kakutani's and von
  Neumann's.
---

# NOTE-037: Debreu 1952, a social equilibrium existence theorem

## Contribution

The paper states and proves an equilibrium existence theorem for "social systems" in which each agent's feasible set depends on the other agents' actions, now called abstract economies or generalized games. It replaces the convexity hypotheses of Kakutani and Nash with contractibility, using the Eilenberg–Montgomery fixed-point theorem for multi-valued maps. It was written, per footnote *, "to lay the mathematical foundations" for Arrow & Debreu's competitive-equilibrium existence proof.

## Key insight

Once feasibility itself is endogenous, an equilibrium is a fixed point of the product of best-response correspondences. Existence needs only that these correspondences have closed graphs and topologically trivial (contractible) values. Convexity is sufficient for that but not necessary: "The convexity assumptions were, however, irrelevant" (§4, p. 892).

## Assumptions

For all ι = 1, …, ν (the Theorem, p. 888):
- **(A1)** The action set 𝔄_ι ⊂ ℝ^{n_ι} is a **contractible polyhedron**: homeomorphic to a finite union of convex cells, and deformable to a point. Hence it is compact.
- **(A2)** The constraint correspondence A_ι: 𝔄̃_ι → 𝔄_ι, where 𝔄̃_ι = Π_{κ≠ι} 𝔄_κ, has **non-empty, compact values** (background, p. 888) and a **closed graph** G_ι = {(ā_ι, a_ι) | a_ι ∈ A_ι(ā_ι)}.
- **(A3)** The payoff f_ι: G_ι → R̄ (the completed real line [−∞, +∞]) is **continuous**.
- **(A4)** The value function φ_ι(ā_ι) = max_{a_ι ∈ A_ι(ā_ι)} f_ι(ā_ι, a_ι) is **continuous**.
- **(A5)** For every ā_ι, the maximizer set M_ā_ι = {a_ι ∈ A_ι(ā_ι) | f_ι(ā_ι, a_ι) = φ_ι(ā_ι)} is **contractible**.

The setting is finite-dimensional Euclidean ("Only subsets of finite Euclidean spaces will be considered here", p. 887), with finitely many agents. Preferences are represented by real-valued payoffs, so a complete ordering is assumed.

## Key results

- **Definition (p. 888).** a* is an equilibrium point if, for all ι, a*_ι ∈ A_ι(ā*_ι) and f_ι(a*) = max_{a_ι ∈ A_ι(ā*_ι)} f_ι(ā*_ι, a_ι).
- **Theorem (p. 888).** Under (A1)–(A5) there exists an equilibrium point.
- **Lemma (p. 889).** If Z is a contractible polyhedron and φ: Z → Z has a closed graph and contractible values, then φ has a fixed point. This is a particular case of Eilenberg–Montgomery (1946) or Begle (1950).
- **Proof (p. 889).**
  1. 𝔄 = Π𝔄_ι is a contractible polyhedron (§1: products of convex cells and of polyhedra are polyhedra, and products of contractible sets are contractible).
  2. Define φ(a) = M_ā_1 × … × M_ā_ν. Its values are contractible as products of contractible sets.
  3. M_ι = {(ā_ι, a_ι) ∈ G_ι | f_ι = φ_ι} is closed by (A2)–(A4).
  4. The graph Γ = ∩_ι 𝔐_ι is therefore closed.
  5. A fixed point a* ∈ φ(a*) is an equilibrium.
- **Remark (p. 889).** Call A_ι "continuous" at ā⁰_ι if every a⁰_ι ∈ A_ι(ā⁰_ι) is the limit of some a^n_ι ∈ A_ι(ā^n_ι) along any sequence ā^n_ι → ā⁰_ι (lower hemicontinuity, in modern terms). If G_ι is compact, A_ι is continuous at ā⁰_ι, and f_ι is continuous on G_ι, then φ_ι is continuous at ā⁰_ι. The proof shows two things:
  - (α) upper semicontinuity of φ_ι, from compactness of G and continuity of f alone;
  - (β) lower semicontinuity, which additionally uses the continuity of A.
- **Corollary (§3, p. 890).** Let X, Y be contractible polyhedra and f: X × Y → R̄ continuous. Suppose every U_x⁰ = argmin_y f(x⁰, y) and every V_y⁰ = argmax_x f(x, y⁰) is contractible. Then f has a saddle point. This contains the saddle-point theorems of Kakutani, of von Neumann (1928, 1937) and of von Neumann–Morgenstern §17.6.
- **MinMax facts (§3, pp. 890–891),** for compact X, Y and continuous f:
  - (a) max_x min_y f ≤ min_y max_x f;
  - (b) a saddle point implies equality;
  - (c) equality implies a saddle point exists;
  - (d) the saddle-point set is empty or equals A × B, where A and B are the sets of maxmin and minmax strategies.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Under (A1)–(A5) an equilibrium of the social system exists | proof | Theorem plus proof, p. 889, via the Eilenberg–Montgomery/Begle lemma |
| C2 | Continuity of φ_ι follows from a compact graph, continuous A_ι and continuous f_ι | proof | Remark, parts (α) and (β), pp. 889–890 |
| C3 | Saddle points exist under contractible argmin/argmax sets; this contains Kakutani and von Neumann | proof (Corollary) and citation (containment) | §3. Containment follows because convex sets are contractible |
| C4 | The theorem contains Nash's N-person equilibrium existence | assertion (routine but unshown reduction) | Introduction and §4. No derivation given |
| C5 | The theorem was used by Arrow–Debreu for competitive equilibrium | citation | Ref. 2 ("in press", 1953) |
| C6 | Kakutani's and Nash's convexity assumptions are "irrelevant" for fixed-point existence | informal argument (historical) | §4. Refers to Eilenberg–Montgomery's replacement of convexity by acyclicity |
| C7 | The result extends from contractible polyhedra to absolute retracts | assertion with citations | Footnote †, citing Begle, Borsuk, Aronszajn–Borsuk |

## Method

A fixed-point argument. The paper first builds the topological toolkit (§1): convex cells, geometric polyhedra, polyhedra as homeomorphic images, contractibility, and the completed real line via t = (e^θ − 1)/(e^θ + 1). It then forms the product best-response correspondence, shows it has a closed graph, and applies the multi-valued fixed-point lemma. Continuity of the value function is handled separately (the Remark), by a Berge-type maximum-theorem argument.

## Concepts

- **Social system / abstract economy.** Agents choose a_ι from a feasible set A_ι(ā_ι) determined by the others' actions, and each maximizes f_ι.
- **Contractible (deformable into a point).** There is a continuous H: [0,1] × Z → Z with H(0, z) = z and H(1, z) = z⁰ (p. 888).
- **Polyhedron.** A set homeomorphic to a finite union of convex cells, where a convex cell is the convex hull of finitely many points (p. 887).
- **Semicontinuous (multi-valued function).** In Debreu's usage, *closed graph* (p. 889). This is not the modern upper or lower hemicontinuity terminology.
- **Continuous (constraint correspondence).** Debreu's term for what is now lower hemicontinuity (p. 889).
- **Completed real line R̄.** ℝ ∪ {−∞, +∞}, topologised via a homeomorphism with [−1, 1].

## Connections

The paper's lineage runs through von Neumann's 1928 minimax and 1937 growth-model lemma, then Kakutani's (1941) fixed-point theorem, Nash (1950) and Eilenberg–Montgomery (1946) / Begle (1950). It is the mathematical base of Arrow & Debreu (1954). The generalized-Nash-equilibrium literature descends from this "abstract economy" formulation. So do later existence results without transitive or complete preferences (Shafer–Sonnenschein 1975). That is background knowledge, not in the paper. This record has no other game-theory or general-equilibrium work to link to.

## Bearing on the record

- It is the correct primary citation for existence of generalized (constrained) Nash equilibria, which some multi-agent-learning and constrained-game settings assume.
- It carries nothing for ML practice. The existence proof is non-constructive and gives no algorithm or convergence rate. No ANTH- document is implicated.

## Limitations

- Existence only. There is no uniqueness, stability or computation.
- Continuity of φ_ι (A4) is a joint condition that is hard to check directly. The Remark reduces it to a compact graph plus lower hemicontinuity of A_ι.
- Contractibility of M_ā_ι is still hard to verify outside convex or quasi-concave settings.
- Finite-dimensional, finitely many agents, real-valued (complete and transitive) preferences.
- The Nash containment is asserted, not derived (C4).

## Open questions

The paper leaves none open. For the record, what matters is how far the hypotheses have since been weakened: non-ordered preferences, infinite dimensions, discontinuous payoffs. That is literature beyond this paper and is not assessed here.

## Corrections to the seeded skim

- **Extent.** The brief says 4 pp. The article runs pp. 886–893. The dossier says §3–4 were only "glanced at because the OCR is poor". I read both. §3 is a two-player specialisation plus textbook MinMax facts. §4 is a history of fixed-point results and does *not* derive Nash's theorem from the main Theorem.
- **Two things the dossier's paraphrase omits.**
  - The contractibility conditions are on each *action set* 𝔄_ι and each *best-response set* M_ā_ι, not on "each agent".
  - The theorem's continuity requirement is on the value function φ_ι. Debreu flags this himself as "a joint requirement on the two functions f_ι and A_ι … not well adapted to applications", which motivates the Remark (p. 889).
- **"Contains Nash's N-person equilibrium" is asserted, not shown.** The introduction says the theorem "contains the existence of an equilibrium point for an N-person game (see Nash and Section 4)". Section 4 only restates Nash's theorem. The reduction is left to the reader: take A_ι constant equal to a mixed-strategy simplex, so best-response sets are convex and hence contractible, and use the Remark for continuity of φ_ι. The reduction is routine, but it is not in the paper.
- **The dossier cites "a lemma, a special case of Eilenberg–Montgomery (or Begle)" without its hypotheses.** They are: Z a contractible polyhedron; φ: Z → Z with closed graph ("semicontinuous" in Debreu's usage) and contractible values. Footnote † notes that Begle's version would allow absolute retracts in place of contractible polyhedra.
