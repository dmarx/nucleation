---
number: 676
status: Read
formerly:
- NOTE-tmpkwpvs
paper: 'LIT-868'
title: 'Generalized Information-Theoretic Tree Abstractions (G-tree search)'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from the PubMed Central copy (PMC9222931, the published
    version, CC BY 4.0), fetched as JATS XML through NCBI E-utilities and
    converted to plain text, MathML rendered from its text content.
    Sections 1–8 and Appendices A–G read; every proof (Lemmas 6, 8, 12,
    14, Theorem 11, Corollary 13, Proposition 15) followed step by step.
    Algorithms 1 and 2 are images in the XML and were not seen; they are
    known here only from the prose of §5.1. Figures 1–9 read from their
    captions and the text that discusses them, not as images, so the
    numbers in Figure 8 are not checked. The reference list read. The
    authors' earlier Q-tree search paper (IEEE T-RO 2020), which this one
    generalises, was not read.
date: '2026-10-09'
summary: >-
  Proves that when the encoder is a pruning of a fixed quadtree, any
  weighted sum of relevant-information, irrelevant-information and
  compression terms splits over interior nodes, so a bottom-up recursion
  finds the optimal tree with fewest leaves exactly, in linear time, where
  greedy splitting can miss everything. The tree solving IB with side
  information is always a pruning of the plain IB tree for the same β.
---
<!-- inactive-ok-file: QUESTION-025 THEORY-185 CLAIM-119 CLAIM-092 THEORY-163 THEORY-186 LIT-267 — Open or Proposed; cited as the question this batch was filed for and the accounts this reading bears on -->

# NOTE-676: Generalized Information-Theoretic Tree Abstractions (G-tree search)

## Contribution

The paper poses a multi-variable information-bottleneck problem over a
discrete, structured class of encoders: the prunings of a fixed quadtree
over a grid. The objective weights several relevant variables, several
irrelevant ("private") variables and compression. It shows that every term
decomposes over the tree's interior nodes, and gives a bottom-up recursion,
G-tree search, that provably returns the optimal pruning with the fewest
leaves. The authors' earlier single-variable Q-tree search and a tree
version of IB with side information (Chechik and Tishby) are special cases.
For the latter it proves a nesting result: penalising irrelevant
information can only prune the IB tree.

## Key insight

Coarse-graining along a fixed hierarchy is additive. Splitting a cell t
into its children adds p(t)·JS of the children's conditional distributions
to the information about any variable, and p(t)·H(Π) to the rate. So the
value of a whole tree is a sum of local values, and the best tree is found
the way one prunes a decision tree. Start at the bottom, keep a subtree
only if its total contribution is positive, and pass that value up. The
search therefore sees information that sits several levels down beneath a
level where nothing differs, which a greedy top-down splitter cannot.

## Assumptions

- **Finite everything.** A finite probability space; X takes values in the
  finest cells of a d-dimensional grid of side 2^ℓ, and Y_i, Z_j are
  discrete.
- **Encoders are deterministic and tree-shaped.** The feasible set is
  T_Q, the prunings of the full quadtree T_W: each finest cell is assigned
  to the unique leaf of the pruned tree above it. Soft encoders and
  partitions that are not prunings of this one tree are excluded. The
  result is stated for quadtrees, and the authors say that it "applies
  straightforwardly to general tree structures"; the proofs use only the
  parent–child structure, so this looks right, but it is asserted, not
  shown.
- **T is a function of X**, so T ⊥ (Y, Z) | X and I(T;X) = H(T).
- **Weights are non-negative**: β ∈ ℝ₊ⁿ, γ ∈ ℝ₊ᵐ, α ≥ 0. Lemma 12 uses
  γΔI_Z ≥ 0.
- **The joint p(x, y₁…y_n, z₁…z_m) is given**, though only p(x) and each
  p(y_i|x), p(z_j|x) enter the computation (§7).

## Key results

- **Decomposition (Eqs. 13–21).** For T_q reached from the root by single
  expansions, J(T_q; β, γ, α) = Σ_{s ∈ N_int(T_q)} ΔJ(s), where
  ΔJ(t) = Σ_i β_i ΔI_{Y_i}(t) − Σ_j γ_j ΔI_{Z_j}(t) − αΔI_X(t), with
  ΔI_{Y_i}(t) = p(t)·JS_Π(p(y_i|t′₁), …, p(y_i|t′₄)), ΔI_X(t) = p(t)H(Π),
  Π = (p(t′_k)/p(t))_k. The root tree has J = 0.
- **G-function (Eq. 22).** G(t) = max{ΔJ(t) + Σ_{t′∈C(t)} G(t′), 0} for
  interior t of T_W, 0 at the finest leaves.
- **Lemma 6.** G(t) ≥ the summed ΔJ over the interior of any subtree
  rooted at t. **Lemma 8.** If G(t) > 0, some subtree rooted at t attains
  it. **Lemma 10.** G(t) > 0 iff some subtree rooted at t has positive
  total ΔJ. All by induction on depth.
- **Theorem 11.** G-tree search (expand a leaf iff G > 0, from the root)
  returns the optimal minimal tree: optimal for J, and every strict subtree
  strictly worse. The proof shows the returned tree equals any optimal
  minimal tree, so that tree is unique.
- **Complexity (§5.3).** T_W has at most 2·|N_leaf(T_W)| nodes; computing
  G and searching costs of order (n + m + 3)|N_leaf(T_W)| operations.
- **Greedy failure (§6.1, Figure 4).** With β_cr(t) = H(Π)/JS_Π(…), a
  greedy search expands t only above β_cr(t). In the symmetric 4 × 4
  example JS = 0 at the root, so β_cr(root) = ∞ and the greedy tree is the
  root alone for every β.
- **Special cases (Eqs. 24–32).** IB over trees, max I_Y − (1/β)I_X, is
  G with weights (1, 0, 1/β) (Q-tree search). IBSI over trees,
  max I_Y − (1/β)[γI_Z + I_X], is G with (1, γ/β, 1/β) (S-tree search).
  Eq. 30 is printed with "γI_Z − I_X", a sign slip: Eq. 29 and the stated
  weights both give + I_X.
- **Lemma 12 and Corollary 13.** S(t; β, γ) ≤ Q(t; β) for all t, so every
  node S-tree search expands, Q-tree search also expands: the IBSI tree is a
  subtree of the IB tree.
- **Lemma 14 and Proposition 15.** With P defined from Q and ΔI_Z by
  Eq. 33, S = max{P, 0}. So the IBSI tree can be computed from the stored
  Q-values and the ΔI_Z terms, without recomputing ΔI_X or ΔI_Y.
- **Example (§7).** On one 256 × 256 segmented road image with six
  classes, keeping only "road" (red) retains all its information with
  1.42% of the nodes of the full tree. Keeping all six classes at α = 0
  retains all of them with 5%. Penalising two other classes coarsens the
  boundary regions where they meet the road, at some cost in road
  information.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Over prunings of a fixed tree, the IB-type objective with several relevant and irrelevant variables is a sum of per-node terms p(t)·JS and p(t)·H(Π) | strong (derivation) | Eqs. 13–21; standard chain rule for refinements |
| C2 | The bottom-up G recursion returns the unique optimal tree with fewest leaves, for any non-negative weights | strong (proof) | Lemmas 6–10, Theorem 11 |
| C3 | Greedy one-step splitting can return the trivial tree although the grid holds relevant information | strong (counterexample) | §6.1, Figure 4 |
| C4 | For fixed β, adding an irrelevance penalty yields a subtree of the IB tree | strong (proof) | Lemma 12, Corollary 13 |
| C5 | The IBSI tree can be obtained from the IB Q-values plus ΔI_Z alone | strong (proof) | Lemma 14, Proposition 15 |
| C6 | The framework yields useful, highly compressed abstractions for autonomous systems | weak | one image, no comparison method, no downstream planning task |
| C7 | The penalty on I(T;Z_j) protects private information, through Fano's inequality | weak | informal argument in §4; one variable at a time |

## Method

Precompute ΔI_{Y_i}, ΔI_{Z_j} and ΔI_X for every interior node of the full
tree from p(x) and the conditionals p(y_i|x), p(z_j|x). Compute G from the
deepest interior nodes up. Then start at the root and expand any leaf with
G > 0, updating the information totals by the stored increments, until no
leaf has G > 0. A greedy variant replaces G by the one-step ΔJ.

## Concepts

- **abstraction**: a multi-resolution representation of the grid, here
  a pruned quadtree. Each leaf aggregates the finest cells beneath it.
- **tree as encoder**: p_q(t|x) = 1 iff cell x lies under leaf t of T_q.
- **optimal minimal tree**: optimal for J, and every strict subtree has
  strictly lower J. There are no redundant expansions.
- **relevant / irrelevant variables**: Y_i whose information the tree
  should keep and Z_j whose information it should shed. The paper reads the
  Z_j as task-irrelevant in the IBSI sense or as private.
- **emergence**: used for the selection of a pruning by the objective.
  Nothing hierarchical is learned or discovered; the hierarchy is the fixed
  quadtree.

## Connections

The paper generalises the authors' Q-tree search (IEEE T-RO 2020) and its
hard-constrained mixed-integer version (2021). It rests on the information
bottleneck of Tishby, Pereira and Bialek ([LIT-338](../literature.d/LIT-338.md), read in the record), IB
with side information (Chechik and Tishby 2002), the multivariate and
agglomerative IB (Slonim, Friedman and Tishby), and the deterministic IB
(Strouse and Schwab). Because the encoder is deterministic, I(T;X) = H(T),
and the objective with α is the deterministic IB's cost restricted to tree
partitions. The paper says so only for the deterministic IB in general,
not for its own problem. The privacy reading points to the privacy-funnel
literature (Makhdoumi et al.; Calmon and Fawaz). The JS increment is the
merging cost of the agglomerative IB, read in reverse, as a gain from
splitting. The recursion is the classic bottom-up pruning of a fixed tree,
as in cost-complexity pruning of decision trees. That is my comparison;
the paper does not make it.

## Bearing on the record

- **[QUESTION-025](../questions.d/QUESTION-025.md).** Not an answer. There is no embedding, no
  co-occurrence and no attribute; the hierarchy is a spatial quadtree fixed
  in advance. Two points carry over. (1) In any hierarchy of nested
  partitions, a level carries information about Y exactly where sibling
  cells differ in p(y|·), weighted by their mass (Eq. 15). Information can
  sit below a level that carries none (Figure 4), so a test of hierarchy
  that looks only at the top split, or splits greedily, can miss it. A
  measurement of the kind the question asks for, scoring recovered
  structure against a known hierarchy, should score each level and not
  only the first. (2) Its implication structure is the partition kind:
  every finest cell belongs to exactly one cell at each level. In
  [QUESTION-025](../questions.d/QUESTION-025.md)'s terms that is a tree, the case Saxe et al. treat
  ([LIT-862](../literature.d/LIT-862.md), [THEORY-186](../theory.d/THEORY-186.md)), not a general concept lattice. It says nothing
  about attributes that cross-cut the tree, which is what [CLAIM-119](../claims.d/CLAIM-119.md) needs.
- **[CLAIM-092](../claims.d/CLAIM-092.md).** A precedent outside translation for the claim's designed
  objective. Problem 1 is a weighted sum of separately computed mutual
  informations with several relevance variables, minus irrelevance terms,
  and §7 computes each from its own pairwise marginal p(x, y_i). The paper
  states the problem over a joint distribution but never uses one. It is
  also an exact solution of such an objective over a structured encoder
  class. It does not touch the claim's point that the contexts may admit
  no joint at all.
- **[THEORY-163](../theory.d/THEORY-163.md) and [LIT-810](../literature.d/LIT-810.md).** In colour naming, annealing β makes a
  hierarchy of categories by successive bifurcations ([NOTE-631](NOTE-631.md)). There the
  encoders are soft, and the hierarchy is found by the objective. Here it
  is imposed, and the objective only chooses how deep to go in each
  region. Corollary 13 nests the solutions across γ at fixed β. The paper
  does not state that its trees are nested across α, but Lemma 12's
  induction gives it unchanged: ΔI_X ≥ 0, so G is non-increasing in α, and
  every node expanded at a larger α is expanded at a smaller one. That is
  my derivation, not the paper's. For a fixed tree, then, the
  compression trade-off gives nested coarse-grainings by construction,
  which is the nesting that colour naming has to find.
- **No THEORY filed.** The results are exact but narrow: an additive
  decomposition and a dynamic programme for encoders constrained to one
  fixed tree. As a claim about what is true they amount to the chain rule
  for refinements and a standard tree recursion. Nothing in the record is
  waiting on them, and the nesting result is specific to this objective.
- No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- The hierarchy is given. The paper finds the best coarse-graining of a
  fixed quadtree, not a hierarchy in data, and the results do not apply
  to partitions that cut across the quadtree's cells.
- The objective counts each relevant variable's information separately,
  so the sum double-counts information the Y_i share. With
  pairwise-marginal inputs it cannot see synergy among them. The same holds
  for the Z_j: penalising I(T;Z₁) and I(T;Z₂) separately does not bound
  I(T;Z₁,Z₂), so the privacy reading guarantees less than §4 suggests. This
  is my observation, not the paper's.
- The evaluation is one image, with no baseline, no downstream planning
  task and no measure of the abstraction's use beyond node counts and
  retained information.
- The weights are set by hand; the paper gives no way to choose them.
- Algorithms 1 and 2 were not seen (images in the PMC XML). Typos (the
  sign in Eq. 30; γI_Z for γΔI_Z in Appendix G; a garbled factor in
  §5.3's node count) do not affect the arguments.

## Open questions

- The nesting across α (above) means the whole family of abstractions
  is one sequence of prunings, as with decision-tree pruning paths. The
  paper does not say whether the breakpoints can be computed in one pass
  rather than by re-running the recursion for each α.
- How far is the best tree pruning from the unconstrained IB or
  deterministic-IB optimum on the same data? This is the price of the tree
  constraint, which the paper never measures.
- With a learned rather than fixed hierarchy (for example, one chosen
  among several trees), is the problem still tractable, and does the
  greedy failure of Figure 4 become the typical case?
