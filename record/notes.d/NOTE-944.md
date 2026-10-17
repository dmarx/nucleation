---
number: 944
status: Read
formerly:
- NOTE-tmpsow60
paper: 'LIT-1168'
title: 'Harder, Salge and Polani — A bivariate measure of redundant information'
version: 2
history:
- version: 1
  date: '2026-10-17'
  note: >-
    Read in full from arXiv 1207.2080v3 (20 July 2012), 14 pp.: §§I–V, the
    proofs of Lemmas 1–3, 5, 7, 10, 11 and Propositions 4, 6, Table I,
    Figs. 1–15 from captions and prose (the plots came through as axis
    labels only). Extracted with pdftotext. I recomputed I_red and I_min
    for every Table I example, the copy example across correlations, the
    first transfer-entropy example (Williams and Beer's coupled pair) and
    the second at four values of d, with a scratchpad script
    (pid-checks/pid2.py). It computes the reverse information projections
    numerically (Nelder–Mead over the simplex), so its I_red values are
    good to about 10⁻³. The PRE version was not compared.
- version: 2
  date: '2026-10-17'
  note: >-
    Limitations annotated: the cited [15]/[16] are Griffith and Koch's v1/v2, now held (LIT-tmpx01yr), whose v6 concedes the point.
date: '2026-10-17'
summary: >-
  I_min gives 1 bit of redundancy to two independent bits copied into the
  target, because it compares amounts of specific information and not
  their direction in the space of distributions over the target. The
  paper adds an identity axiom, I∩((X,Y); X, Y) = I(X; Y), and defines a
  bivariate I_red: project each posterior p(z|x) onto the convex hull of
  the other source's posteriors, count what survives, take the smaller
  direction. I_red satisfies all four axioms and gives a nonnegative PID.
  It agrees with I_min except where I_min overstates redundancy.
---

# NOTE-944: Harder, Salge and Polani — A bivariate measure of redundant information

## Contribution

Before this paper, I_min was the redundancy function of the partial
information decomposition, and its known critique (Griffith, the paper's [15]) had
not produced a replacement that kept Williams's axioms (the paper's
[15], [16]). After it there is
a bivariate redundancy, I_red, that keeps the three axioms (symmetry,
self-redundancy, monotonicity), adds a fourth that I_min fails (identity),
and gives a nonnegative decomposition. The paper also names a distinction
the decomposition had hidden: redundancy from correlated sources
("source redundancy") against redundancy created by the mechanism from
independent ones ("mechanistic redundancy", the AND gate).

## Key insight

Each observation x of a source moves the distribution over the target
from p(z) to p(z|x). Two sources are redundant to the extent that one's
moves can be reproduced by mixing the other's. I_min checks only how far
each source moves p(z) for each outcome, not in which direction.

## Assumptions

- **Discrete variables**, joint distribution known.
- **Two sources.** The construction and every proof are bivariate. There is
  no multivariate I_red.
- **Reverse information projection** onto the convex closure
  C_cl(⟨Y⟩_Z) = conv{p(·|y)} (Eqs. 6–10). It need not be unique; the
  projected information is unaffected (Lemma 1).
- **The four axioms are taken as necessary** for a redundancy measure: the
  three from Williams's thesis and the new identity axiom (Eq. 5). Nothing
  argues they are sufficient.

## Key results

- **§II C, I_min's counterexample.** Z = (X, Y), X, Y independent uniform
  bits: I_min(Z; X, Y) = 1 bit, though X and Y share no information.
  *Checked:* 1.0000; and I_min stays 1 at every correlation between X and
  Y in the copy family, while I(X; Y) runs from 1 to 0 (Fig. 5).
- **Eq. 12, projected information.**
  I^π_Z(X ↘ Y) = Σ_x p(x)[D_KL(p(z|x) ‖ p(z)) − D_KL(p(z|x) ‖ p_{x↘Y}(z))],
  nonnegative and at most I(Z; X) (Lemma 1).
- **Eq. 13.** I_red(Z; X, Y) = min{I^π_Z(X ↘ Y), I^π_Z(Y ↘ X)}.
- **§III B 4.** Symmetry, self-redundancy (Eqs. 14–19), monotonicity
  (Lemmas 2–3, Proposition 4) and identity (Lemma 5, Proposition 6) are
  proved. The proofs were followed.
- **Lemma 7.** The synergy I(Z; X, Y) − I(Z; X) − I(Z; Y) + I_red ≥ 0, by
  convexity of the KL divergence, so the bivariate PID is nonnegative.
- **Table I**, I_red / I_min, *checked* (my values in brackets where they
  differ from the table's rounding): Copy λ = 0 (Rdn) 1 / 1; Copy λ = 1
  (Unq) 0 / 1; XOR 0 / 0; AND 0.311 / 0.311 (0.3113, synergy 0.5); RdnXor
  1 / 1; RdnUnqXor 1 / 2 (I_red 0.9987, within the optimizer's
  tolerance); XorAnd 0.5 / 0.5; Copy λ < 1, I(X; Y) / 1 (λ = 0.25: 0.2421,
  equal to I(X; Y)).
- **Fig. 3.** In random distributions with |X| = |Y| = 3, I_min mostly lies
  above I_red, increasingly so as |Z| grows. "There are a few exceptions";
  whether numerical is left open.
- **§IV D, first transfer-entropy example** (Williams and Beer's coupled
  pair): the two measures give the same state-independent and
  state-dependent transfer at every d (Fig. 10). *Checked* at d = 0,
  0.25, 0.5, 0.75, 1: SITE 1, 0.456, 0.189, 0.046, 0 and SDTE 0, 0.138,
  0.311, 0.549, 1 under both.
- **§IV D, second example.** Z_t i.i.d., Y_{t+1} = Z_t with probability d
  and Y_t otherwise, X_t a separate constant process. For T_{Z→(X,Y)},
  I_min gives no state-independent transfer at any d; I_red gives none for
  d ≤ ½ and all of it at d = 1. *Checked:* at d = 0.75 SITE/SDTE are
  0/0.549 under I_min and 0.411/0.138 under I_red, and 0.411 =
  I(Y_{t+1}; Z_t) − I(Y_{t+1}; Y_t) = 0.4564 − 0.0456, as §IV D says for
  d ≥ ½.
- **Theorem 9 still holds** with I_red: perfect open-loop controllability
  iff perfect controllability with zero state-dependent transfer
  (Lemmas 10–11).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | I_min gives two independent copied bits 1 bit of redundancy, so it does not measure shared information | strong | §II C; computed exactly |
| C2 | A redundancy measure must satisfy the identity axiom | interpretive | Eq. 5; argued from the copy intuition |
| C3 | I_red satisfies symmetry, self-redundancy, monotonicity and identity, and its PID is nonnegative | strong | proofs in §III B 4 and Lemma 7, followed |
| C4 | I_min is "in most cases" an upper bound on I_red, more so as the target grows | weak | Fig. 3, random distributions; exceptions unexplained |
| C5 | Independent sources can carry redundant information because of the mechanism | interpretive | AND and summing-dice examples; a position against the paper's [15], not a result |
| C6 | I_red reflects the bystander process "much better" than I_min | interpretive | §IV D; I_min sees a dependence between X and Z that the process lacks, which is an argument from the intended reading |
| C7 | The decomposition of transfer entropy into state-independent and state-dependent parts can reverse with the redundancy measure | strong | Fig. 12; checked at d = 0.75 and 1 |

## Concepts

- **Projected information I^π_Z(X ↘ Y)** — the part of X's information about
  Z that survives replacing each p(z|x) by its reverse-KL projection onto
  the mixtures of Y's posteriors (Eq. 12).
- **Identity property** — redundancy of two sources about their own joint
  copy equals their mutual information (Eq. 5).
- **Source and mechanistic redundancy** — redundancy already in the
  sources' correlation, against redundancy the mechanism creates from
  independent sources (§IV C 3). Not defined rigorously.

## Connections

- **Builds on** Williams and Beer's lattice and inversion ([LIT-1172](../literature.d/LIT-1172.md),
  [NOTE-936](NOTE-936.md)), Williams's three axioms, Griffith's test cases (its
  [15]) and reverse information projections (its [10]). It compares its decomposition of
  transfer entropy with Williams and Beer 2011's ([LIT-1176](../literature.d/LIT-1176.md)).
- **[LIT-1162](../literature.d/LIT-1162.md) (Bertschinger et al. 2014)** takes the identity
  property as one of its consequences too, by a different construction
  (a unique-information measure from an optimization over distributions
  with fixed pairwise marginals). Whether the two coincide is not said
  here.
- **[LIT-1174](../literature.d/LIT-1174.md) (Ay and Polani, [NOTE-946](NOTE-946.md))** is from the same group, and
  this paper says measures of causal information flow "still struggle
  with over-determination", the interventional form of the redundancy
  problem (§II).
- **[NOTE-010](NOTE-010.md)** works a disagreement between ΦID and Varley and Hoel on
  the permutation (X¹, X²) → (X¹ ⊕ X², X¹). It notes the synergy is 1 bit
  under the minimum-mutual-information redundancy and 0 under one with the
  identity property. *Checked:* I_min gives redundancy 1 and synergy 1
  there; I_red gives 0 and 0, with 1 bit unique to each source. So I_min
  sides with the minimum-MI redundancy, and I_red is a second example of
  the other kind. My computation.

## Bearing on the record

- Filed as [THEORY-708](../theory.d/THEORY-708.md).
- **No transfer-entropy number in the record changes.** James, Barnett and
  Crutchfield's case 1 is XOR, where I_red = I_min = 0; Williams and Beer's
  coupled pair agrees at every d (checked above). So [THEORY-707](../theory.d/THEORY-707.md),
  [THEORY-712](../theory.d/THEORY-712.md), [NOTE-945](NOTE-945.md), [NOTE-942](NOTE-942.md) and [CLAIM-335](../claims.d/CLAIM-335.md) stand as
  written. The second example here is a case where the SITE/SDTE split
  does depend on the measure, which [THEORY-712](../theory.d/THEORY-712.md) already says in
  general.
- [THEORY-581](../theory.d/THEORY-581.md) and [NOTE-020](NOTE-020.md) compute synergy bias with I_min. By C1 and
  C4, I_min tends to overstate redundancy and so synergy by the same amount,
  since I(S; X, Y) − I(S; X) − I(S; Y) + I∩ moves one for one with I∩. Whether
  their cross-scale comparisons survive another measure is unknown. My
  inference; nothing here recomputes them.
- **For the Anthology of the SOTA:** no instruction for ML practice.

## Limitations

- Bivariate only. The record's ΦID and Shannon-invariant readings need
  more sources.
- C2 and C5 are positions. The work it cites as [15] holds the opposite
  on C5: independent sources share nothing (§IV C 3, footnote 1).
  (Annotated 2026-10-17: [15] and [16] are versions of Griffith and Koch,
  now held as [LIT-tmpx01yr](../literature.d/LIT-tmpx01yr.md). The quotation is accurate to v1 and v2; v6
  withdraws it and concedes mechanistic redundancy, [NOTE-tmp71sln](NOTE-tmp71sln.md).)
- C4 rests on scatter plots of random distributions, with unexplained
  exceptions.
- I_red needs a convex optimization per source value. The paper gives no
  algorithm beyond the definition; my values were found numerically.

## Open questions

- A multivariate I_red with the identity property and nonnegative atoms
  (the authors leave it open).
- Whether I_red equals Bertschinger et al.'s redundancy on all bivariate
  distributions.
