---
number: 840
status: Read
formerly:
- NOTE-tmpiqh3w
paper: LIT-999
title: 'Golub & Jackson — Naïve Learning in Social Networks and the Wisdom of Crowds'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the published version (AEJ: Microeconomics 2(1),
    112–149) posted on Benjamin Golub's website
    (bengolub.net/wp-content/uploads/2020/05/naivelearning-1.pdf, 38 pages),
    text extracted with pdftotext: §§I–VI and Appendix sections A
    (Theorems 2–3 and their proofs), B (Lemma 1, Propositions 2–5, Lemma 5,
    Theorem 1) and C (Theorem 4). The proofs of Lemma 1, Proposition 3
    (via Lemma 5) and Theorem 1 were checked step by step; Theorem 4's
    proof was followed, not checked line by line.
date: '2026-10-14'
summary: >-
  Agents get independent signals with mean μ and repeatedly replace their
  beliefs by fixed weighted averages of their neighbours' (DeGroot). In a
  convergent network the consensus is s·p(0), with s the unit left
  eigenvector of the interaction matrix, and a growing society's limits
  converge in probability to μ if and only if the largest influence
  weight tends to zero (Proposition 2). With reciprocal, equal weights
  this is maximum degree over total degree → 0. A finite group that
  everyone attends to blocks it; balance plus minimal out- or
  in-dispersion guarantee it. How fast consensus is reached is unrelated
  to whether it is right.
---
<!-- inactive-ok-file: THEORY-143 THEORY-148 — Proposed; the bandit-model accounts this reading sits beside, open -->
<!-- inactive-ok-file: THEORY-321 — Proposed; the account filed from this reading, open -->

# NOTE-840: Golub & Jackson — Naïve Learning in Social Networks and the Wisdom of Crowds

## Contribution

DeGroot's averaging model was known to reach consensus; this paper asks
when the consensus is right. It gives an exact answer in terms of
influence weights, a network-level characterization in a special case,
a structural obstruction, and structural sufficient conditions for large
societies of naïve updaters to aggregate dispersed information correctly.

## Key insight

The consensus is a weighted average of the initial signals, with weights
given by the network's left unit eigenvector. A law of large numbers
applies to that average exactly when no single weight stays large. So
correctness of the group belief is a property of where influence
concentrates in the network, not of how each agent updates.

## Assumptions

- **Updating.** p(t) = T p(t−1), T an n × n row-stochastic matrix, fixed
  over time, possibly asymmetric (§I). Agents do not correct for repeated
  or correlated information ("persuasion bias"); only the first round is
  Bayesian, under normal signals with T_ij ∝ the precision i assigns to j.
- **Signals.** p_i(0)(n) ∈ [0, 1], mean μ, independent within each n,
  variance at least σ² > 0 (needed only for the "only if" of Lemma 1).
- **Convergence.** Each T(n) is convergent (strongly aperiodic,
  Theorem 2); strong connectivity is not required.
- **Large societies.** Wisdom is a double limit: t → ∞ for each network,
  then n → ∞ along a sequence of networks.

## Key results

- **Proposition 1.** For strongly connected T: convergent ⇔ aperiodic ⇔
  there is a unique left eigenvector s of eigenvalue 1, entries summing to
  1, with lim (T^t p)_i = s·p for every i. s_i is i's influence:
  s_i = Σ_j T_ji s_j.
- **Theorems 2–3 (App. A).** T is convergent iff strongly aperiodic
  (aperiodic on every closed group). Each minimal closed group reaches its
  own consensus s_B p_B; agents outside closed groups converge to mixtures
  of these and have influence 0.
- **Equal weights, undirected (§II.C).** T_ij = G_ij/d_i gives
  s_i = d_i / Σ_j d_j.
- **Lemma 1 (law of large numbers).** plim s(n)p(0)(n) = μ iff s_1(n) → 0
  (s_1 the largest weight). Proof checked: var ≤ Σ s_i² ≤ s_1 → 0 one way;
  var ≥ s_1²σ² the other.
- **Proposition 2 (characterization).** A sequence of convergent
  stochastic matrices is wise, plim max_i |p_i(∞)(n) − μ| = 0, iff
  s_1(n) → 0. *Holds when:* the signal assumptions above, for every such
  signal distribution or none.
- **Corollary 1.** Reciprocal equal-weight networks are wise iff
  max_i d_i / Σ_j d_j → 0: "disproportionate popularity … is the only
  obstacle".
- **Proposition 3 with Lemma 5.** If a finite family B_n is uniformly
  prominent, min_{i∉B}(T^t)_{i,B} ≥ α > 0 for some t, the society is not
  wise; s_B ≥ κπ_B/(1 + π_B). Checked.
- **Examples 3–4.** An unbalanced star keeps the centre's influence at
  (1−ε)/(1−ε+δ) for any n; a one-way line gives agent 1 influence near 1
  for small δ although agent 1 is prominent only in n − 1 steps. So direct
  weight, even indirect weight a few steps out, can mislead.
- **Theorem 1 (sufficiency).** Balance (no family of size ≤ j(n) → ∞
  gets unboundedly more weight from outside than it gives out) plus
  minimal out-dispersion (any large enough finite family gives at least r
  to any family of nearly all of society) imply wisdom. Neither alone
  suffices (Examples 3–4). Proof checked.
- **Theorem 4 (App. C).** Balance plus minimal in-dispersion also suffice.
- **§V, speed.** Convergence time scales with −1/log|λ₂(T)|. Four
  examples show speed and wisdom vary independently: both, neither, or
  either one.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The DeGroot consensus is the left-eigenvector-weighted average of initial beliefs | strong | Proposition 1, Theorem 3 (known results, proved) |
| C2 | A growing society is wise iff the maximal influence vanishes | strong | Lemma 1, Proposition 2, checked |
| C3 | With reciprocal equal weights, wisdom ⇔ max degree / total degree → 0 | strong | Corollary 1 |
| C4 | A finite uniformly prominent group prevents wisdom | strong | Proposition 3, Lemma 5, checked |
| C5 | Balance and dispersion together suffice for wisdom | strong | Theorems 1 and 4 |
| C6 | Speed of convergence and wisdom are independent | moderate | four examples, §V |
| C7 | Influence cannot be read off direct or few-step attention | strong | Examples 3–4, exact formulas |

## Concepts

- **Wise.** Limiting beliefs converge jointly in probability to μ as n
  grows (Definition 3).
- **Influence weight s_i.** Agent i's weight in the consensus; the unit
  left eigenvector entry.
- **Prominent group.** One from which every outsider receives weight
  within t steps (Definition 4); uniformly prominent if bounded below
  along the sequence (Definition 5).
- **Balance; minimal out-/in-dispersion.** Properties 1–3, conditions on
  weight between small families and the rest.

## Connections

The model is DeGroot (1974); the Bayesian motivation and persuasion bias
are DeMarzo, Vayanos and Zwiebel (2003), whose knife-edge condition for
optimal aggregation in finite societies this replaces by asymptotic
conditions. It contrasts with observational learning (Bala and Goyal
1998; Acemoglu et al. 2008), where wisdom needs some stubborn or
arbitrarily informed agent, and with eigenvector centrality (Katz 1953;
Bonacich 1987; PageRank). Speed is left to the authors' homophily paper
(arXiv:0811.4013) and to conductance and Cheeger bounds.

## Bearing on the record

- **[QUESTION-047](../questions.d/QUESTION-047.md).** The paper is a model in which every member uses the
  same updating rule and the community's settled belief is fixed by
  network structure: change the weights, hold the rule fixed, and the
  consensus changes from the truth to the leader's signal. That is the
  form [QUESTION-047](../questions.d/QUESTION-047.md) asks for, in a model, not a real community. The
  consensus s·p(0) is reached by every agent, but no agent computes or
  aims at it.
- **A correction to the filing.** [LIT-999](../literature.d/LIT-999.md)'s body says "Every member
  updates soundly". The paper's agents are explicitly naïve: they do not
  adjust for repeated and cross-contaminated information, and only the
  first round is Bayesian. So the case is of naïve, uniform members and a
  structure-determined group belief, not of sound members. [QUESTION-047](../questions.d/QUESTION-047.md)'s
  "individually sound inquirers" fits it only if a fixed reasonable rule
  counts as sound. The status note's "a structural condition on the
  network, not the soundness of its members, decides" is right.
- **[CLAIM-030](../claims.d/CLAIM-030.md) and [CLAIM-060](../claims.d/CLAIM-060.md).** The collective outcome here is entirely
  derived from members' rules and weights by linear algebra; it is
  "systemic" only in that no member's rule mentions it. Whether that
  counts for [CLAIM-030](../claims.d/CLAIM-030.md) is a question for that claim; the paper gives no
  mechanism beyond the weights.
- **[THEORY-143](../theory.d/THEORY-143.md) and [THEORY-148](../theory.d/THEORY-148.md)** (Zollman-type bandit models) concern
  sparse networks and transient diversity. This model has no exploration
  and no action, so it neither supports nor conflicts with them; it adds
  a different structural variable, concentration of influence.
- **[THEORY-321](../theory.d/THEORY-321.md)** is filed from this reading.
- No instruction for machine-learning practice; nothing for the
  anthology.

## Limitations

- Fixed weights; agents never learn whom to trust.
- Independent signals with a common mean; no correlated errors and no
  strategic agents.
- Asymptotic in n; finite societies are not graded.
- The sufficient conditions can be hard to check (§VI); they are not
  necessary.

## Open questions

- Which network-formation processes yield balance and dispersion.
- Whether agents who reweight over time, ignoring insular groups, restore
  wisdom.
- Whether a small admixture of more rational agents changes the outcome.
