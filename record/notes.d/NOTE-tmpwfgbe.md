---
status: Read
paper: 'LIT-tmp1kfuc'
title: 'Contextuality in canonical systems'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from arXiv 1703.01252v4 (19 Jul 2017), main text
    (Sections 1–5) and supplementary text S (Theorem S.1 with proof, the
    proofs of Theorems 4.3, 4.4 and 4.6 and Corollary 4.5, Example S.2),
    extracted with pdftotext. The proofs were followed line by line. The
    matrices illustrating the proof of Theorem 4.4 and the 4 × 4 Boolean
    matrix of Theorem S.1 lost their layout in extraction and were
    followed from the prose. The numbers of Example S.2 were only partly
    recoverable. The typeset journal version was not compared.
date: '2026-10-09'
summary: >-
  Contextuality is to be judged on a canonical representation in which
  every variable is replaced by binary splits and connections are coupled
  multimaximally. For two content-sharing k-valued variables with all
  splits kept, the canonical system is noncontextual if and only if one
  nominally dominates the other: its probabilities fall below the other's
  for at most one value (Theorem 4.6). Only the 1- and 2-splits matter
  (Theorems 4.1, 4.3). For continuous densities, all splits make any
  difference in distribution contextual.
---

<!-- inactive-ok-file: THEORY-013 THEORY-tmpjdnxt — Proposed; cited for what this reading adds to them -->

# NOTE-tmpwfgbe: Contextuality in canonical systems

## Contribution

The paper turns the dichotomization proposal at the end of CbD 2.0
(LIT-tmpsa1qj) into a definition. Contextuality is a property of the
canonical (split) representation of a chosen expanded system. It then
solves the smallest nontrivial case, a single pair of content-sharing
categorical variables with every split kept, exactly. Before this paper,
two variables measuring one content in two contexts could not be
contextual in CbD by themselves. Here, with all splits, they are unless one
nominally dominates the other.

## Key insight

Splitting a k-valued variable into all its yes/no questions turns one
connection into 2^{k−1} − 1 connections. Each must be coupled as tightly
as its own two marginals allow, and all of them must come from one coupling
of the two original variables. Maximal coupling of every one-value split
fixes the diagonal of that coupling at min(p_i, q_i). Maximal coupling of
every two-value split then forbids almost all off-diagonal mass. What is
left is possible only when one distribution exceeds the other at no more
than one value. Contextuality has here become a property of how two
distributions differ, with no cross-content correlations involved.

## Assumptions

- Categorical variables (finitely many values). The continuous case is
  discussed only informally in Section 5.
- **Expansion is a choice.** Which joinings and coarsenings to add is not
  dictated by the theory. Section 4 assumes the largest choice, all
  coarsenings, hence all splits.
- **Multimaximality as pairwise maximality** (Definition 3.8) is used for
  connections with more than two variables. The paper cites properties
  Multimax1–3 to LIT-tmpsa1qj and LIT-tmpuzf4t. Note that Multimax1
  (existence and uniqueness) holds because every canonical variable is
  binary.
- Section 4 treats a fragment, one connection of two variables. A system
  containing a contextual fragment is contextual (by heredity), but the
  converse needs the rest of the system.

## Key results

- **Definition 2.1 / 2.2.** For couplings T = {T_q} of the connections, R
  is noncontextual with respect to T if some coupling S of the bunches
  has S_q ∼ T_q for every q. With a property C that picks a unique T_q,
  this is "noncontextual with respect to C".
- **Theorems 2.4–2.5** (from LIT-777). A quasi-coupling with connection
  marginals T always exists, and its total variation reaches a minimum.
  min‖X‖ − 1 is the degree of contextuality.
- **Definitions 3.4–3.5.** A split D_{qW}^c = 1 iff R_q^c ∈ W, with W
  normalised to the smaller side. The split representation of R_q^c is
  its k one-element splits. The canonical representation replaces every
  variable by its split representation.
- **Remark 3.3.** However many splits are added, a bunch's support has at
  most as many states as the original variable has values.
- **Equations (19)–(22).** A coupling r_ij of the pair is a maximally
  connected coupling of the 1-2 system if and only if Σ_j r_ij = p_i,
  Σ_i r_ij = q_j, r_ii = min(p_i, q_i), and r_ii + r_ij + r_ji + r_jj =
  min(p_i + p_j, q_i + q_j) for i < j.
- **Theorem 4.1.** Noncontextuality of the all-splits system D implies
  that these 3k + C(k, 2) equations have a nonnegative solution.
  Theorem S.1 gives the equation system's rank as 2k − 1 + C(k, 2).
- **Theorem 4.3.** In a maximally connected coupling (k ≥ 6), the
  probability that an m-split equals 1 is determined by the 1- and
  2-splits: the sum of the m diagonal minima plus, for each pair, the
  pair's excess min(p_i + p_j, q_i + q_j) − min(p_i, q_i) − min(p_j, q_j)
  (Eq. 23). Eq. (23) can fail for some distributions (Example S.2).
- **Theorem 4.4.** A maximally connected coupling of the 1-2 system is
  unique if it exists. Its off-diagonal mass lies in a single row or a
  single column.
- **Corollary 4.5.** One exists if and only if p_i > q_i for at most one
  i, or p_j < q_j for at most one j.
- **Theorem 4.6.** The all-splits system D is noncontextual if and only if
  its 1-2 subsystem is, i.e. if and only if one of R_1^1, R_1^2
  *nominally dominates* the other. Two variables dominate each other if
  and only if they are identically distributed or k = 2.
- **Section 5, continuous case** (an argument, not a theorem). Take two
  densities f ≠ g with all splits. Then f exceeds g on some interval and g
  exceeds f on another. Any partition containing two subintervals of each
  violates Corollary 4.5. So the system is contextual unless f = g.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | With all splits of two content-sharing k-valued variables, the canonical system is noncontextual iff one nominally dominates the other | strong (proof in S) | Theorems 4.1, 4.3, 4.4, 4.6, Corollary 4.5 |
| C2 | Only the 1- and 2-splits matter for that verdict | strong (proof) | Theorems 4.3, 4.6 |
| C3 | The maximally connected coupling of the 1-2 system is unique when it exists | strong (proof) | Theorem 4.4 |
| C4 | With all splits, two continuous variables are contextual unless identically distributed | moderate (short argument, not a theorem) | Section 5 |
| C5 | Nominal dominance is likely to fail in many empirical systems | weak (no data analysed) | Section 5 |
| C6 | All dichotomous behavioural systems examined so far except one were noncontextual | weak here (cited) | Section 5, refs 7, 15, 17 |

## Method

Both proofs reduce the problem to the k × k table r_ij of a coupling of the
two original variables, since each bunch has at most k states. Theorem 4.4
then uses four rules about which off-diagonal cells can be positive (R1–R4,
by "p-minimized" and "q-minimized" pairs). It concludes that positive
off-diagonal mass is confined to one column (if p-minimized) or one row (if
q-minimized). Corollary 4.5 exhibits the coupling. Theorem 4.6 checks Eq.
(23) on that coupling for every higher-order split.

## Concepts

- **expansion; joining; coarsening.** Adding new contents computed from
  existing ones in each context: tuples of variables (joining) or
  functions of one variable (coarsening). Any transformation is a joining
  followed by a coarsening.
- **split; split representation; canonical representation.** Definitions
  3.4–3.5 above.
- **m-split.** A split whose set W has m elements (m ≤ k/2).
- **1-2 system.** The subsystem of 1-splits and 2-splits.
- **nominal dominance.** R nominally dominates R′ if Pr[R = x] <
  Pr[R′ = x] for at most one value x. The authors call it a form of
  stochastic dominance for categorical variables that had not been
  identified before.

## Connections

It completes LIT-tmpsa1qj's proposal and uses its multimaximality results
and those of LIT-tmpuzf4t. Its measure is LIT-777's. Joining, which lets
within-context dependence enter a connection, is presented as what the
selective-influence theory and Abramsky and colleagues' approach (LIT-016)
always require. Most known behavioural CbD analyses are cited to the
programme around LIT-264.

## Bearing on the record

- **THEORY-013.** That theory reports CbD finding no contextuality in
  published behavioural data. Its data are binary and cyclic. This paper
  says the same of dichotomous systems "with the exception of one, very
  recent experiment", which is consistent with THEORY-013. It also says
  that under canonical all-splits representations of multi-valued
  responses, noncontextuality requires nominal dominance, which "is
  likely to be violated in many empirical systems". So THEORY-013's
  finding is scoped to binary data under CbD 1.0/2.0 and does not carry
  over to multi-valued data analysed canonically. The theory's "does not
  say" list should name this. This NOTE does not edit it.
- **THEORY-012 and LIT-016.** The sheaf framework's contextual fraction is
  non-increasing under coarse-graining of outcomes (LIT-265 Theorem 2).
  Here, adding the coarsenings of a variable to the system can create
  contextuality where the original pair, a single connection, had none.
  The two frameworks treat coarse-graining differently: the sheaf
  framework coarse-grains a model, CbD adds coarsenings as further
  contents. The paper does not compare them.
- **THEORY-tmpjdnxt** is filed from this reading. It states that CbD's
  verdict on a fixed set of measurements depends on the representation
  chosen, with this paper's Theorem 4.6 as the sharpest instance.
- **The manuscript.** CLAIM-tmpje74v's "What it does not say" assumes
  that S, M and H are binary and each appear in two contexts. If any
  observable there is multi-valued and its coarsenings are of interest,
  this paper's representation applies, and Theorem 4.6 can make the
  system contextual on a single connection. Reported for the
  coordinator; no claim file is edited here.
- No instruction for machine-learning practice.

## Limitations

- Only one connection of two variables is solved. Systems with several
  contents, or with more than two variables per connection, are not
  analysed.
- The choice of expansion is left to the analyst. The paper argues that
  intervals or cuts are more natural for ordered values and leaves that
  theory to future work.
- C4 is an informal argument in the concluding remarks.
- Small slips in the supplement: in the proof of Theorem 4.4 the case
  "rij > 0 that is p-minimized" is announced and then argued as
  "q-minimized"; the zero cell "r15 = 0" is called p-minimized where the
  argument needs it positive. Neither affects the conclusion, which is
  rechecked by Corollary 4.5's explicit construction.
- No data are analysed.

## Open questions

- The verdicts under interval-only or cut-only splits for ordered
  responses, which the authors flag. Those would decide whether the
  continuous-case conclusion (C4) is an artefact of allowing every split.
- How CbD's canonical verdicts relate to sheaf-theoretic monotonicity
  under coarse-graining for consistently connected multi-valued systems.
