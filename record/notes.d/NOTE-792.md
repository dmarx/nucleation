---
number: 792
status: Read
formerly:
- NOTE-tmpjvn8h
paper: LIT-988
title: 'Devezer et al. — Scientific discovery in a model-centric framework'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from arXiv:1803.10118v3 (18 March 2019, 47 pages, the
    version current at PLOS ONE publication), text extracted with
    pdftotext: the main text and all supporting information, S1–S28,
    including the Markov-chain framework (S1), the strategy definitions
    (S5), the reproducibility proof (S23) and the per-population
    correlations (S24). Figure content was read from captions and from
    the tables of numbers that pdftotext recovered (S10–S18). The heat
    maps and violin plots were not inspected visually. The PLOS ONE
    version of record was not compared line by line.
date: '2026-10-14'
summary: >-
  A population of scientists, chosen at random each step, tests a
  proposed linear model against the current consensus model by AIC or
  SC, and the winner becomes the consensus. Which models get proposed
  (the strategy mix) decides where the consensus spends its time. A
  population of boundary testers reproduces results almost perfectly
  while spending little time at the true model. Replication does not
  change the transition matrix, so reproducibility cannot cause
  convergence. A population with all four strategies equally represented
  is never the worst and has low variance.
---
<!-- inactive-ok-file: CLAIM-192 THEORY-148 — Proposed; the thesis and the transient-diversity account this reading bears on, named and not leaned on -->

# NOTE-792: Devezer et al. — Scientific discovery in a model-centric framework

## Contribution

The paper gives a formal model of a scientific community as a stochastic
process over a consensus model. That makes reproducibility, speed of
discovery, "stickiness" of truth and time spent at truth definable and
comparable. Its main finding is that these come apart. A community can
reproduce its results almost perfectly while rarely holding the true
model, because the research strategies in the population decide which
comparisons are ever run.

## Key insight

Every test in the model is sound: it is a valid model comparison on
fresh data from the true model. The community can still be wrong most
of the time, because what reaches the consensus is fixed by which
alternatives get proposed against it. Reproducibility measures how
reliably a given comparison comes out the same, not whether the true
model is ever in the comparisons.

## Assumptions

- **Model space.** Linear models in up to 3 factors, with the hierarchy
  constraint (an interaction implies its lower-order terms) and x_1 in
  every model: 14 models in all.
- **Consensus update.** At each step a scientist is drawn from an
  infinite population with type probabilities (p_1, …, p_A). The
  scientist proposes M_P with probability P(M_P | R_a, M_G), and data
  D^(t) of size n = 100 is drawn from the true model.
  - If S(M_P) < S(M_G), with S being AIC or SC, then M_P becomes M_G.
  - This is a "memoryless 0 − 1 decision rule", which the authors admit
    "might not reflect a realistic representation of the scientific
    process".
- **Scientists have no beliefs.** They have no memory, do not learn, and
  interact only through M_G. They commit no questionable research
  practices and have no incentives. The true model is always in the
  search set.
- **Strategies (S5).**
  - Tess proposes models one main effect away from M_G.
  - Mave proposes uniformly from all models.
  - Bo proposes M_G plus one interaction.
  - Rey repeats the previous experiment with new data.
  - "Soft" versions give every other model a small probability, which
    makes the chain ergodic. "Hard" versions do not.
- **Signal.** σ² : E(y | μ_x) is set to 1:4, 1:1 or 4:1. True
  coefficients are Dirichlet(1), and predictors correlate at 0.2.
- **Populations.** One type at 99%, or all types in equal shares (S6).

## Key results

- **Without replication (exact Markov analysis, all 14 true models,
  noise 1:4).**
  - The transition matrix is
    P(M_G^(t+1) = M_ℓ | M_G^(t) = M_i) = Σ_a P(S(M_ℓ) < S(M_i)) P(M_ℓ | R_a, M_i) P(R_a).
  - The true model is sticky under low noise.
  - A Bo-dominant population spends only 25% (AIC) or 48% (SC) of its
    time at the true model, mostly sitting at more complex models.
  - Tess- and Mave-dominant populations spend 47% and 41% (AIC), or 67%
    and 72% (SC).
  - The diverse population spends 36% (AIC) or 62% (SC). That is less
    than Tess or Mave, but the true model is in its top three for every
    true model: "epistemic diversity protects against ineffective
    research strategies".
  - Mean first passage times range from 3.39 to 6.43 steps.
- **With replication (ABM: 3 true models × 3 noise levels × 5
  populations × 2 criteria, 11,000 steps, 100 seeds).**
  - **No causal link (S23).** The rate of reproducibility is
    P(M_G^(t+1) = M_G^(t) | replication at t). Because a replication
    re-runs the same pair on independent data, its two outcomes sum out
    of the transition probability: Σ_j q_ijℓ = P(S(M_ℓ) < S(M_i)) P(M_ℓ | M_i).
    So reproducibility "has no causal effect" on time at the truth,
    first passage time or stickiness. (The proof's labelling of q_iiℓ
    and q_iℓℓ is muddled, but the conclusion follows from the
    independence of the replication.)
  - **Correlation depends on the population.** Overall, Spearman r is
    −0.02 with time at the truth and 0.26 with first passage time
    (Fig 4). Per population (Table 3, S24), r with time at the truth is
    0.41 (Rey), 0.35 (Tess), 0.69 (Mave), −0.06 (Bo) and 0.59 (diverse).
    With stickiness it is 0.74, 0.87, 0.76, −0.03 and 0.82.
  - **Bo.** A Bo-dominant population reaches near-perfect
    reproducibility while spending little time at the true model. Its
    comparisons are "between models that are 1) not true and 2) far from
    each other", so the same untrue model keeps winning.
  - **Mave and speed.** Mave-dominant populations are fastest to the
    truth whatever the complexity and noise, through connectedness. A
    Bo-dominant population has a mean first passage time of 1592.5 steps
    under hard strategies. With soft strategies the medians are 815
    (Rey), 80 (Tess), 16 (Mave), 18 (Bo) and 25 (diverse) (Table 4).
  - **Diversity.** The diverse population "always performs better than
    the worst homogeneous population with respect to all properties" and
    has low variability. From this the authors conclude that it
    "optimizes" across the properties, which they liken to a diversified
    portfolio.
  - **Method.** SC spends longer at the truth than AIC (medians 27.05%
    against 19.83%) but with more variability (IQR 66.03% against
    33.80%).
- **High noise (4:1, S16–S18).** Even the diverse population "cannot
  prevent poor performance", and the true model is "not captured for
  most models".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | In this model, reproducibility does not affect the long-run distribution, stickiness or first passage time | strong | S23, a structural argument |
| C2 | A strategy mix that proposes only distant, untrue alternatives yields near-perfect reproducibility with little time at the truth | moderate | Bo-dominant ABM, Fig 4; one strategy, one model space |
| C3 | Strategies that keep the model space connected (Mave) speed discovery | moderate | Fig 4C–E, Table 4 |
| C4 | An equal mix of strategies is never the worst population on any property and has low variance | moderate | Fig 4C, S25 |
| C5 | Epistemic diversity "optimizes" scientific discovery | weak | stronger than C4, which is all the comparison shows; it is beaten on time at the truth by Tess and Mave |
| C6 | Under high noise no population recovers the truth reliably | moderate | S16–S18, S22 |
| C7 | If incentives reward Bo-like strategies for their reproducibility, false results may be canonised | weak | speculation from cited work |

## Method

The no-replication process is a first-order Markov chain. Its stationary
distribution, mean first passage time τ_{i,T} = 1 + Σ_{ℓ≠T} P(M_ℓ|M_i) τ_{ℓ,T}
and stickiness are solved exactly. The transition probabilities
P(S(M_i) < S(M_j)) are estimated by Monte Carlo (S8). With replication
the process is higher-order, so a forward ABM (S3 Algorithm 1) is run
and the quantities are estimated from the runs.

## Concepts

- **Global model M_G.** The "pragmatic consensus of the scientific
  community at any given time": simply the last winner.
- **Reproducibility.** A replication reproduces a result if the same
  model is confirmed as global as in the original test.
- **Stickiness.** The probability of staying at a model once it is the
  global model.
- **Epistemic diversity.** Here only the mix of the four
  proposal strategies. The authors stress that the model "is agnostic as
  to what kind or what degree of epistemic diversity would optimize
  scientific discovery".
- **Soft and hard strategies.** Whether off-strategy proposals have
  positive probability.

## Connections

The paper places itself after Ioannidis, McElreath and Smaldino,
Smaldino and McElreath, and Nissen et al. on the canonisation of false
facts, which work in a hypothesis-testing frame. It moves to model
comparison. Mave is related to Weisberg and Muldoon's mavericks, but
differs from them. The diversity result is said to be consistent with
Zollman's transient diversity ([LIT-735](../literature.d/LIT-735.md)). Shiffrin, Börner and Stigler's
warning against one-size reforms is the policy backdrop.

## Bearing on the record

- **[QUESTION-047](../questions.d/QUESTION-047.md).** This is the closest of the four readings to the
  question's design. Every inquiry step is sound, the community's
  standing view (M_G) is a community-level state, and changing a
  structural variable (the strategy mix) while holding each test fixed
  changes where the community settles. With Bo-dominant populations it
  settles mostly on untrue models, and stably so: reproducibility is
  near perfect. Filed as [THEORY-295](../theory.d/THEORY-295.md). The cautions:
  - **There are no beliefs.** No agent holds a belief or reasons to one.
    M_G is the last winner, not anything a member endorses. So the case
    is "a sound procedure, a wrong standing view", not "sound believers,
    a wrong shared belief".
  - **The strategy mix is a population variable,** but of method, not
    of structure in [QUESTION-047](../questions.d/QUESTION-047.md)'s sense (density, influence weighting).
    It sits closest to "how long divergent pursuit lasts" ([THEORY-148](../theory.d/THEORY-148.md))
    and to which alternatives are pursued at all.
- **[THEORY-148](../theory.d/THEORY-148.md) (transient diversity).** This paper's diversity result is
  related but different. Its diversity is permanent (the mix is fixed),
  and its benefit is insurance against a bad dominant strategy, not
  survival of misleading early evidence. A connection only. The paper
  neither supports nor challenges [THEORY-148](../theory.d/THEORY-148.md)'s mechanism.
- **The LIT's seeded claim, checked.**
  - [LIT-988](../literature.d/LIT-988.md)'s body says "epistemic diversity, not the reproducibility of
    single results, sets whether the community finds the truth and stays
    on it". This half-holds. Reproducibility has no causal effect (C1).
    But what sets discovery is the particular strategies, especially
    whether some keep the model space connected, and the noise level.
    Under high noise even diversity fails (S18).
  - The LIT summary's "epistemic diversity does best across the
    properties studied" overstates the paper's evidence. The diverse
    population is never the worst and has the lowest variability, but
    Tess- and Mave-dominant populations spend more time at the truth.
    The paper's own wording ("optimizes") is itself stronger than its
    comparison supports.
- **The LIT's `published:` date.** It is the arXiv v1 date (2018-03-27).
  This reading is of v3 (2019-03-18).
- **[CLAIM-192](../claims.d/CLAIM-192.md).** M_G moves whenever a proposal wins one test, whoever
  proposed it and whatever anyone holds, which is a formal analogue of a
  thesis moving without anyone arguing for the move. It is an analogue
  only.
- No instruction for machine-learning practice. The model-comparison
  content (AIC against SC under misspecification) is statistics about
  scientific method, not ML practice. Nothing for the anthology.

## Limitations

- Memoryless consensus, set by a single test. The authors flag this
  repeatedly, and note it "might have exaggerated the role of Maves".
- A tiny model space (14 models) with the truth always in it.
- Scientists who neither learn nor interact. The replicator adds
  "meta-level information" only and cannot shift the consensus by
  accumulating evidence.
- The ABM results are marginal effects averaged over noise levels, so
  the effective noise is higher than in the no-replication analysis.

## Open questions

- Does the decoupling of reproducibility from truth survive a consensus
  rule with memory, where a model must win repeatedly to displace the
  incumbent?
- Which mixes, not just the four tested, minimise worst-case
  performance?
- How does the picture change when the true model is outside the search
  set? The authors note that reproducible results then are "not true" by
  construction.
