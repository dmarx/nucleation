---
number: 295
status: Active
formerly:
- THEORY-tmpz5itv
title: "In a community whose consensus model is replaced whenever a single sound pairwise model comparison favours the challenger, which models get proposed can hold the consensus on a false model while results reproduce almost perfectly, so reproducibility need not track convergence to truth"
version: 3
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Narrowed and promoted at the owner's direction, carrying out the
    promotion audit's decision (record/promotion-audit/decisions/THEORY-295.yaml,
    batch 020, ADR-047 v3). The study was read in full, and the title now
    claims no more than it showed. Its scope is narrowed to a consensus
    that a single test can replace, which is the only rule the model ran,
    and "does not track" becomes "need not track", since four of the five
    populations show a positive correlation. The S23 argument is re-derived
    in a dated note below. The promote_when, a model with memory or a real
    field, moves unchanged to QUESTION-151.
- version: 3
  date: '2026-10-20'
  note: >-
    The narrowing-loss sweep (batch 071, ADR-047 v4) filed
    THEORY-tmppuc79, Proposed, to carry what the narrowing dropped. This
    entry's status, title and claims are unchanged; a dated note says what
    moved.
tags:
- philosophy-of-science
- epistemology
- social-science
date: '2026-10-14'
source:
- LIT-988
summary: >-
  Devezer, Nardin, Baumgaertner and Buzbas (2019), [LIT-988](../literature.d/LIT-988.md), read in full
  in [NOTE-792](../notes.d/NOTE-792.md). In a Markov-chain and agent-based model where each
  step tests one proposed linear model against the consensus by AIC or
  SC, replication cannot change the transition matrix. A boundary-testing
  population reproduces almost perfectly while rarely holding the true
  model, and correlations between reproducibility and truth depend on
  the strategy mix. The consensus is memoryless, scientists hold no
  beliefs, and an equal strategy mix is shown only never to be the
  worst, not best.
extended_by:
- THEORY-tmppuc79
---

<!-- inactive-ok-file: THEORY-tmppuc79 — Proposed; the wider claim this entry's narrowing dropped, filed beside it and cited as open -->
<!-- inactive-ok-file: THEORY-148 THEORY-146 — Proposed; accounts of community-level epistemic mechanisms this one sits beside -->

# THEORY-295: In a community whose consensus model is replaced whenever a single sound pairwise model comparison favours the challenger, which models get proposed can hold the consensus on a false model while results reproduce almost perfectly, so reproducibility need not track convergence to truth

## Source

Devezer, Nardin, Baumgaertner and Buzbas (2019), *PLOS ONE* 14(5):
e0216125 (arXiv:1803.10118v3), [LIT-988](../literature.d/LIT-988.md), read in full in [NOTE-792](../notes.d/NOTE-792.md).

## What was actually shown

- **The process.** At each step a scientist of type a is drawn, proposes
  M_ℓ with probability P(M_ℓ | R_a, M_G), and tests it against the
  consensus M_G on fresh data of size 100 from the true model. The
  winner by AIC or SC is the new consensus. Without replication this is
  a Markov chain with
  P(M_G^(t+1) = M_ℓ | M_G^(t) = M_i) = Σ_a P(S(M_ℓ) < S(M_i)) P(M_ℓ | R_a, M_i) P(R_a).
- **Reproducibility is causally idle (S23).** A replication re-runs the
  same pair on independent data, so its outcome probabilities sum out of
  the transition matrix. The rate of reproducibility therefore cannot
  affect stationary probabilities, first passage times or stickiness.
- **The case (Fig 4, §"Reproducible results do not imply convergence").**
  A population of 99% boundary testers ("Bo"), who propose only models
  with one more interaction, reaches near-perfect reproducibility. In the
  no-replication analysis it spends only 25% (AIC) or 48% (SC) of its
  time at the true model, mostly at over-complex ones. In the ABM its
  Spearman correlation between reproducibility and time at the truth is
  −0.06. Its comparisons pit untrue models that are far apart, so "the
  method consistently favors the same untrue model".
- **The contrast.** Mave-dominant populations, who propose uniformly,
  reach the truth fastest and spend long at it, with lower
  reproducibility. Correlations with time at the truth are 0.41–0.69 for
  the other populations (Table 3).

What could have come out otherwise: reproducibility could have tracked
time at the truth across populations, as the received view of
replication expects. It does for some populations and not for Bo.

## What this does not say

- **Not about beliefs.** Scientists hold no beliefs and do not learn.
  The consensus is the last winner. The claim concerns a community's
  standing view produced by a sound procedure, not a belief members
  settle on.
- **Not that reproducibility is worthless.** For most populations it
  correlates positively with time at the truth and strongly with
  stickiness (0.74–0.87). True results are reproducible, a sanity check
  the authors keep. The claim is that reproducibility is not sufficient,
  and does not cause convergence.
- **Not that epistemic diversity is optimal.** The equal mix is never the
  worst on any property and has the lowest variability. Tess- and
  Mave-dominant populations spend more time at the truth. The paper's
  "optimizes" is stronger than its comparison. Under high noise (4:1)
  even the diverse population fails (S18).
- **Not robust to memory.** The consensus changes on a single test, which
  the authors call unrealistic. They say it may exaggerate the role of
  mavericks. Whether a memoryful consensus would resist Bo's drift is
  untested.
- **Not about real fields.** The model space has 14 linear models with
  the truth always in it. The claim that rewarding reproducible Bo-like
  work could canonise falsehood is the authors' speculation from cited
  work.

## Connections

- **[QUESTION-047](../questions.d/QUESTION-047.md).** The closest of the record's models to the question's
  design. Each inquiry step is held sound, a population-level variable
  (which alternatives get proposed) is changed, and where the community
  settles changes, onto a false model that its own replications keep
  confirming. It answers the question's second clause for a standing
  view, not a belief. It is offered as a partial answer, but no
  `answers:` relation is declared, because the model's agents hold no
  beliefs.
- **[THEORY-148](THEORY-148.md) (transient diversity).** That account says diversity must
  last long enough and then give way. Here diversity is permanent, and
  its benefit is insurance against a bad dominant strategy. The two are
  different mechanisms under the same word, and should not be cited as
  one result.
- **[THEORY-146](THEORY-146.md).** That account biases a community through which
  researchers are funded and recruited, without corrupting anyone. This
  one fixes a false consensus through which comparisons are run, without
  any test being unsound. Both put the failure in the population's
  composition rather than in its members' reasoning.

## Note of 2026-10-19: why replication cannot move the chain (S23, re-derived)

Without replication the consensus is a Markov chain,
P(M_G' = M_ℓ | M_G = M_i) = Σ_a P(R_a) P(M_ℓ | R_a, M_i) P(S(M_ℓ) < S(M_i)),
whose inputs are the strategy mix, the proposal kernels and the comparison
probabilities. A replication re-tests the previous pair on fresh data,
independent of the original test's. So summing the joint probability
q_ijℓ over the replication's outcomes returns the original step's
probability, Σ_j q_ijℓ = P(M_ℓ | M_i) P(S(M_ℓ) < S(M_i)), and the
transition law is the same with or without replication. The rate of
reproducibility, P(M_G^(t+1) = M_G^(t) | replication at t), is a statistic
of the chain's path, not an input to its transition law. So it cannot move
the stationary distribution, the first-passage times or the stickiness.
The paper's labels q_iiℓ and q_iℓℓ are muddled ([NOTE-792](../notes.d/NOTE-792.md)), but the argument
needs only the independence of the replication. The existence half rests
on the Bo-dominant population: near-perfect reproducibility, 25% (AIC) or
48% (SC) of its time at the truth, and Spearman r = −0.06 between the two
([NOTE-792](../notes.d/NOTE-792.md), C2). Whether the decoupling survives a consensus with memory is
[QUESTION-151](../questions.d/QUESTION-151.md).

## Note of 2026-10-20: the wider claim, filed Proposed

Under [ADR-047](../decisions.d/ADR-047.md) v4 the narrowing-loss sweep (batch 071) filed [THEORY-tmppuc79](THEORY-tmppuc79.md) as Proposed, extending this entry. It carries the general reading this entry's title carried before the promotion audit narrowed it: that in real scientific communities high reproducibility is not evidence that the consensus is true, as Devezer et al. draw the lesson. This entry is its evidence and is not changed by the filing.
