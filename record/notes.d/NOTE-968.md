---
number: 968
status: Read
formerly:
- NOTE-tmprcqzl
paper: 'LIT-1201'
title: 'Ince — Measuring multivariate redundant information with pointwise common change in surprisal'
version: 1
history:
- version: 1
  date: '2026-10-17'
  note: >-
    Read from arXiv 1602.05063v3 (13 Jul 2017), 46 pp., extracted with
    pdftotext. §§1–6 in full: co-information, the PID axioms, Defs.
    4.1–4.3, the operational argument (§4.3), the properties (§4.4) and
    every two- and three-source example (§§5–6). §7 (Gaussian variables)
    and §8 (discussion) were read at lower resolution, and Figs. 7 and 10
    from captions and prose only. Several tables' numbers were lost in
    extraction (Tables 8–11, 13); I recomputed those systems instead of
    reading the printed values. The Matlab code was not run. I implemented
    I_ccs (scratchpad/iccs/iccs.py: iterative proportional fitting for P̂,
    then the sign rule of Def. 4.1) and reproduced the paper's examples
    before applying it to the record's.
date: '2026-10-17'
summary: >-
  I_ccs measures redundancy as the expected local co-information over only
  those events where each source, the joint source and the overlap change
  the target's surprisal in the same direction, under the maximum-entropy
  joint matching source–target and joint-source marginals. Defined for any
  number of sources. It keeps symmetry, self-redundancy, subset equality and
  an independent-sources identity, and drops Harder et al.'s identity,
  monotonicity and non-negative atoms. A game-theoretic argument that
  unique information depends on the source–source marginal is offered
  against Bertschinger et al.
---

<!-- inactive-ok-file: THEORY-714 — Proposed; the account filed from this reading -->

# NOTE-968: Ince — Measuring multivariate redundant information with pointwise common change in surprisal

## Contribution

Before this paper, the multivariate redundancy measures on the
Williams–Beer lattice either overstated redundancy (I_min, two-bit copy) or
were bivariate (I_red, I_broja). I_ccs is defined for any number of sources
and gets the two-bit copy right. It pays for that, as Rauh et al. prove some
measure must, with negative atoms, and it argues they should be read as
"misinformation" and "mechanistic redundancy" rather than as defects.

## Key insight

Mutual information is an average of local terms that can be positive
(information) or negative (misinformation). A local co-information term is
an overlap only if every quantity it is built from moves the same way. Count
those and drop the rest, and redundancy becomes a set intersection at the
level of single events. Monotonicity then fails for a plain reason: a source
can carry local misinformation the other source does not.

## Assumptions

- **Finite or Gaussian variables.** Discrete in §§4–6; univariate and
  multivariate Gaussians in §7, by numerical integration.
- **The joint used is P̂, not P (Def. 4.2).** The maximum-entropy
  distribution with Q(Ai, S) = P(Ai, S) for every i and
  Q(A1…An) = P(A1…An). So redundancy depends only on those marginals.
  Def. 4.3, without the source–source constraint, is offered for readers
  who keep Bertschinger et al.'s operational view.
- **Unique information may depend on P(X1, X2)** (§4.3). This is the
  paper's operational premise: a simultaneous, one-shot, non-cooperative
  game with equal but asymmetric utility (one player sets the stake)
  operationalises unique information.
- **A fundamental distinction between local information and local
  misinformation.** Terms of opposite sign are never treated as overlapping.
- **Continuity is conjectured, not proved** (§4.4). The code checks the
  local condition (Eq. 42) in each example.

## Key results

- **Def. 4.1** — I_ccs(S; A1…An) = Σ p̂ · Δ_s h_com, with Δ_s h_com =
  c_p̂(a1…an, s) when sgn Δ_s h(a1) = … = sgn Δ_s h(an) =
  sgn Δ_s h(a1…an) = sgn c, and 0 otherwise.
- **Properties (§4.4)** — symmetry; self-redundancy, since for n = 1 the
  local co-information is the local mutual information; subset equality,
  proved by cancelling terms; the independent identity property (Eq. 22).
  Not Harder et al.'s identity: "any distribution with negative local
  information terms serves as a counter example". Not monotonicity.
- **Table 7** — x1, x2, s with p(0,0,0) = 0.4, p(0,1,0) = 0.1,
  p(1,1,1) = 0.5: I(S; X1) = 1, I(S; X2) = 0.61, I_ccs({1}{2}) = 0.77. The
  PID is 0.77, 0.23, −0.16, 0.16. *Checked:* 0.7685, 0.2315, −0.1585,
  0.1585.
- **REDUCEDOR (Table 6)** — I_ccs gives redundancy 0, unique 0.31 each,
  synergy 0.38; I_min and I_broja give 0.31 redundancy and 0.69 synergy.
  *Checked:* 0, 0.3113, 0.3113, 0.3774.
- **SUM (Table 5)** — redundancy 0, unique 0.5 each, synergy 0.5, where
  I_broja gives 0.5 redundancy. *Checked:* 0.0001 (iterative-fitting
  error), 0.4999, 0.4999, 0.5001.
- **AND (Table 12)** — one redundant event, (0,0,0). *Computed:* redundancy
  0.1038, unique 0.2075 each, synergy 0.2925. The extracted Table 11 lost
  its numbers, so these are mine, consistent with Table 12's single
  pointwise term (¼ × 0.415).
- **XOR, RDN, two-bit copy** — 1 synergistic; 1 redundant; 0 redundant and
  1 unique each. *Checked.*
- **Three sources (§6)** — XORCOPY: {i}{jk} = 1, {12}{13}{23} = −1. DBLXOR:
  {12} = {13} = {23} = 1, {123} = −1. Giant bit: {1}{2}{3} = 1. Parity:
  {123} = 1. XORUNQ: {3} = {12} = 1. *All checked* with a full Möbius
  inversion on the 18-node lattice.
- **Gaussians (§7, Fig. 10)** — the minimum-MI redundancy is constant in
  the predictor–predictor correlation b, while I_ccs moves from unique at
  negative b to redundant at strong positive b. Read from the prose only.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | I_ccs is a redundancy measure for any number of sources satisfying symmetry, self-redundancy, subset equality and independent identity | strong | §4.4, proved for these four |
| C2 | I_ccs is not monotone, so its PID has negative atoms | strong | Table 7, checked |
| C3 | Negative atoms are a necessary consequence of measuring overlapping content | interpretive | §§4.4, 8; supported by DBLXOR and by Rauh et al.'s theorem, not proved for every such measure |
| C4 | Bertschinger et al.'s operational definition is not necessary for unique information | moderate | REDUCEDOR game (§4.3.1); a counterexample to necessity of their criterion, given the paper's game-theoretic premise |
| C5 | So I_broja is "invalid", since redundancy is not fixed on Δ_P | weak as stated | follows only if the game-theoretic premise is accepted; Bertschinger et al. would reject it |
| C6 | I_broja conflates synergy into redundancy | moderate | Fig. 5A example: one local term of −0.138 bit enters its co-information |
| C7 | I_ccs gives intuitive PIDs across the literature's examples | interpretive | §§5–6; judged against intuition, reproduced here for the discrete ones |
| C8 | I_ccs is continuous | conjecture | §4.4 |

## Method

1. Build P̂ by maximum entropy under the marginal constraints (the paper uses
   dit; iterative proportional fitting gives the same here).
2. For each event, compute each source's local information about s, the
   joint source's, and the local co-information (Eq. 29).
3. Keep the co-information where all signs agree; average under P̂.
4. Möbius-invert on the lattice to get atoms, which may be negative.

## Concepts

- **Local misinformation** — a negative local mutual information, the
  observation raising the surprisal of the target value.
- **Independent identity property** — I(A1; A2) = 0 ⇒
  I∩((A1, A2); A1, A2) = 0 (Eq. 22), introduced here.
- **Subset equality** — split off from monotonicity, and in Ince's view
  the axiom the lattice actually needs.
- **Mechanistic redundancy** — redundancy between sources that are
  independent, created by the mechanism; the paper's reading of the
  negative atoms in DBLXOR and XORCOPY.

## Connections

- **[LIT-1202](../literature.d/LIT-1202.md) (Rauh et al.).** Their XORCOPY is Ince's §6.2.2, and Ince
  cites them for it. Theorem 2 bounds the atom {12}{13}{23} at −1 for any
  measure with identity and non-negative atoms. I_ccs meets the bound
  exactly while keeping only independent identity. So it is an instance of
  the theorem's escape route, not a refutation.
- **[LIT-1162](../literature.d/LIT-1162.md) (Bertschinger et al.).** The disagreement is over what unique
  information is, operationally. Under Def. 4.3, without the source–source
  constraint, I_ccs can be computed in their framework. The two agree on
  every example in the record ([NOTE-937](NOTE-937.md)) and differ on REDUCEDOR, SUM and
  AND.
- **[LIT-1168](../literature.d/LIT-1168.md) (Harder et al.).** Ince keeps their two-bit-copy verdict but
  rejects their identity in general, because mutual information can contain
  synergistic entropy.
- **ΦID in this record.** [NOTE-799](NOTE-799.md) (Luppi et al.) uses the
  minimum-mutual-information redundancy for Gaussian BOLD signals. No held
  ΦID work uses I_ccs. §7 shows the two differ for Gaussians whenever the
  predictors are correlated, so the choice is not cosmetic for those
  analyses. My connection.

## Bearing on the record

- Filed as [THEORY-714](../theory.d/THEORY-714.md).
- **[CLAIM-335](../claims.d/CLAIM-335.md)'s examples are unchanged under I_ccs.** Y_t = X_{t−1} ⊕ Y_{t−1}:
  redundancy 0, unique 0 and 0, synergy 1. Z_t = X_{t−1} ⊕ Y_{t−1}, pairwise
  sources (Z_{t−1}, X_{t−1}): every atom 0; joint sources (X_{t−1}, Y_{t−1}):
  synergy 1. Computed here.
- **Williams and Beer's coupled pair ([THEORY-712](../theory.d/THEORY-712.md)) is unchanged:** SITE/SDTE at
  d = 0.25, 0.5, 0.75 are 0.4564/0.1379, 0.1887/0.3113, 0.0456/0.5488, as
  under I_min, I_red and I_broja.
- **Harder et al.'s bystander example is not:** at d = 0.75 I_ccs gives
  SITE 0.392, SDTE 0.157 and redundancy 0.065, against 0/0.549 (I_min) and
  0.411/0.138 (I_red); at d = 0.25 it gives a negative SITE, −0.019. A third
  measure confirming that the split depends on the measure off the record's
  examples. Computed here.
- **[NOTE-010](NOTE-010.md)'s permutation** (X¹⊕X², X¹): redundancy 0, unique 1 each,
  synergy 0, as under I_red. Independent identity is enough here.
- **For the Anthology of the SOTA:** no instruction for ML practice. The
  method is offered for neuroimaging analyses, but as a measure, not as
  practice.

## Limitations

- The case against I_broja rests on a premise, the game-theoretic
  operationalisation, that the other side need not grant. REDUCEDOR shows
  the two premises disagree, not which is right.
- "Correct" and "intuitive" PIDs are judged by the author's intuition about
  the systems.
- Continuity is a conjecture; the measure is not differentiable, by its
  thresholding.
- Bias and inference from finite samples are left open (§8).
- Four-variable lattices (166 nodes) are discussed but not computed.

## Open questions

- Separate lattices for local information and local misinformation, each
  conjectured monotone (§8).
- Whether I_ccs satisfies Rauh's secret-sharing property in general (§8).
- A partial entropy decomposition compatible with it (Ince 2017, not held).
