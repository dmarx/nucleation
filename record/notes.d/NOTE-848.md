---
number: 848
status: Skimmed
formerly:
- NOTE-tmpq7lva
paper: LIT-964
title: 'Dwork et al. — The reusable holdout (supplementary material)'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Skimmed: the three-page main text in Science was not reached. Read in
    full is the 12-page Supplementary Material "with corrections" that
    co-author Vitaly Feldman posts on his publications page
    (vtaly.net/papers/DFHPRR_Science-SM-0915.pdf), text extracted with
    pdftotext: §1 (max-information, Theorem 2, Corollary 3, Lemma 5,
    Theorems 6 and 8, Corollary 7), §2 (Thresholdout, Lemmas 9–10,
    Theorem 11), §3 (the experiment's implementation), §4 (confidence
    intervals) and the references. The proofs of Theorem 2 and Lemma 5
    are in the SM and were checked; those of Theorems 6, 8, 11 and
    Lemma 10 are deferred to companion papers (arXiv:1411.2664,
    arXiv:1506.02629) and were not read. The main text's figures and its
    own statement of the results were not seen.
date: '2026-10-14'
summary: >-
  From the Supplementary Material: if the max-information between the
  dataset and the analyst's chosen function is at most log₂e·τ²n, the
  chance that the function's empirical mean is more than τ above its true
  mean is at most e^{−τ²n}; pure ε-differential privacy bounds
  max-information by log₂e·εn. Thresholdout answers m adaptively chosen
  statistical queries on a holdout of size n = O(ln(m/β)/τ² · min{B,
  √(B·ln(m/β))/τ}) to accuracy τ with probability 1 − β, where B budgets
  the times the training estimate is found to overfit. The main text was
  not read.
---
<!-- inactive-ok-file: THEORY-318 — Proposed; the account filed from this reading, open -->

# NOTE-848: Dwork et al. — The reusable holdout (supplementary material)

## Contribution

The paper offers a way to reuse one holdout set across many analyses that
are chosen after seeing earlier results, with a guarantee of validity.
The Supplementary Material carries its formal content: a definition of
max-information, a bound showing that limited max-information limits
overfitting, a bound showing that differential privacy limits
max-information, and an algorithm, Thresholdout, with a sample-size bound
that grows with the logarithm of the number of queries.

## Key insight

An analyst overfits a dataset only to the extent that what she sees
reveals that dataset. If every answer she receives is computed so that it
leaks little about any one data point, which is what differential privacy
guarantees, then any function she builds from those answers behaves on
the dataset almost as a function chosen in advance would. Post-processing
cannot undo the guarantee, so she may choose her next query however she
likes.

## Assumptions

- **Data.** n i.i.d. samples from an unknown P on a **discrete** universe
  X (§1.1).
- **Queries.** Statistical queries: functions φ: X → [0, 1], whose
  expectation P[φ] is estimated by the empirical mean E_S[φ].
- **The analyst.** Arbitrary and adaptive, with unrestricted access to a
  training set S_t and access to the holdout S_h only through
  Thresholdout's answers (§2).
- **Overfitting.** Defined one-sidedly in eq. 1, R_τ(φ) = {S : E_S[φ] −
  P[φ] > τ}; the corollaries use |·|.

## Key results

- **Definition 1 (max-information).** I_∞(X; Y) is the least k with
  P[X = x | Y = y] ≤ 2^k P[X = x] for all x, y in the supports.
- **Theorem 2.** With k = I_∞(S; φ), P[S ∈ R(φ)] ≤ 2^k max_φ P[S ∈ R(φ)].
  Proof given and checked: sum over φ and bound each conditional by 2^k
  times the marginal. Holds for any discrete output, not only functions.
- **Corollary 3.** If I_∞(S; φ) ≤ log₂e·τ²n then P[S ∈ R_τ(φ)] ≤
  exp(−τ²n), from Hoeffding's exp(−2τ²n).
- **Lemma 5.** An ε-differentially private M has I_∞(S; M(S)) ≤ log₂e·εn,
  for any distribution on datasets. Proof given and checked (group
  privacy over at most n changed elements). So ε = τ² over the whole
  interaction suffices.
- **Theorem 6 and Corollary 7 (proofs elsewhere).** With ε ≤ τ, an
  ε-DP algorithm outputting φ: X → [0, 1] has P[|P[φ] − E_S[φ]| > τ] ≤
  6e^{−τ²n}. Theorem 6 in general: ε ≤ √(ln(1/β)/(2n)) gives
  P[S ∈ R(Y)] ≤ 3√β.
- **Theorem 8 (proof elsewhere).** For (ε, δ)-DP, n ≥ 48 ln(8/β)/τ²,
  ε ≤ τ/4 and δ ≤ (β/8)^{4/τ} give P[|P[φ] − E_S[φ]| > τ] ≤ β. "The
  constant factors … have not been optimized."
- **Thresholdout (Fig. S1).** Answer with the training mean E_{S_t}[φ]
  unless |E_{S_h}[φ] − E_{S_t}[φ]| exceeds a Laplace-noised threshold
  T̂ + η; then answer E_{S_h}[φ] + ξ, ξ ∼ Lap(σ), spend one unit of budget
  B, and redraw T̂. Lemma 10: it is (2B/(σn), 0)-DP and
  (√(32B ln(2/δ))/(σn), δ)-DP.
- **Theorem 11 (proof elsewhere).** With T = 3τ/4 and σ = τ/(96 ln(4m/β)),
  for any analyst choosing φ_1, …, φ_m adaptively,
  P[∃i: Z_i < B and |a_i − P[φ_i]| ≥ τ] ≤ β whenever
  n = O(ln(m/β)/τ² · min{B, √(B ln(m/β))/τ}). Z_i counts the queries so
  far whose training estimate was off by more than τ/2. *Holds when:* the
  budget has not been exhausted by detected overfitting.
- **§4.** The guarantee is a conservative confidence interval
  [v − α, v + α] with coverage 1 − β, over data and the algorithm's coins.
  Fresh samples per query give width ∝ √(m ln(1/β)/n); Thresholdout gives
  width ∝ √(ln(m/β) B/n), "exponentially better" in m while B ≪ n.
- **§3 (experiment, implementation only).** The simulations used an
  idealized budget and Gaussian rather than Laplace noise, so the
  implementation "differs somewhat from the algorithm we analyzed". The
  analyst picks variables correlated with the label on both sets and
  builds a sign classifier. Fig. S2 plots the classifier's true holdout
  accuracy, said to show "essentially no overfitting to the holdout set".
  The main experiment (Figs. 1–2 of the main text) was not seen.

## Concepts

- **Max-information.** A worst-case log-ratio bound on how much
  observing the output raises the probability of any dataset; approximate
  max-information, its relaxation, is deferred to the companion paper.
- **Adaptive data analysis.** Choosing the next analysis after seeing
  results of earlier ones on the same data.
- **Budget B.** The number of times Thresholdout may answer from the
  holdout because the training estimate disagreed; the guarantee holds
  only while it lasts.

## Connections

Built on differential privacy (Dwork, McSherry, Nissim and Smith 2006) and
its post-processing property (Dwork and Roth 2014, Prop. 2.1). The
statistical-query model is Kearns (1998). The proofs of the main bounds
are in the STOC 2015 paper (arXiv:1411.2664) and in "Generalization in
adaptive data analysis and holdout reuse" (NIPS 2015, arXiv:1506.02629),
neither held here. Freedman's screening paradox (1983) is cited as the
motivating failure.

## Bearing on the record

- **[QUESTION-040](../questions.d/QUESTION-040.md)**, the selection-bias half. [LIT-964](../literature.d/LIT-964.md) is registered for
  "a bound and a procedure for validity when candidates are chosen
  adaptively on the data they are tested on". The SM supplies exactly
  that, with a high-probability bound, for statistical queries in [0, 1]
  on a discrete universe. It is a procedure that prevents the
  inflation, not a correction that says how far a given search inflated
  d′. Reading it as a correction to the reification rule's threshold
  would overstate it.
- **[THEORY-028](../theory.d/THEORY-028.md)** says high-probability versions of its bound "are left to
  the differential-privacy literature". This is that literature, for
  statistical queries, and with max-information, a worst-case quantity,
  in place of mutual information. [THEORY-028](../theory.d/THEORY-028.md) could name [LIT-964](../literature.d/LIT-964.md) there.
- **[THEORY-318](../theory.d/THEORY-318.md)** is filed from this reading, held at the strength
  of the SM, where the main bounds are stated and two of the proofs
  given.
- The paper's application, reusing a holdout set when tuning models, is
  an instruction for machine-learning practice and belongs in the
  anthology, which does not hold the paper ([LIT-964](../literature.d/LIT-964.md)'s filing note). The
  theorem about max-information is not an instruction and stays here.

## Limitations

- Main text unread; only the SM was reachable.
- Four of the six formal results are proved in companion papers, not here.
- Discrete X and [0, 1]-valued queries only.
- The implementation tested in simulation is not the analysed algorithm.
- Constants are loose by the authors' own statement.

## Open questions

- What the main text says the experiment shows, and whether it states the
  guarantee more strongly than the SM does.
- Whether the guarantee extends to non-statistical outputs, such as a
  chosen model or partition, by Theorem 2's generality, with a usable
  max-information bound. The SM says Theorem 2 holds for any discrete
  output but bounds max-information only through differential privacy.
