---
status: Proposed
promote_when: >-
  A model in which the consensus has memory (a challenger must win
  repeatedly, or evidence accumulates) and in which scientists can
  learn. It must still find that a population whose proposals never put
  the true model against the consensus holds a false consensus with high
  reproducibility, while a population that keeps the model space
  connected does not. Alternatively, a meta-scientific study of a real
  field whose replications succeed at a high rate while independent
  evidence shows its standing model to be wrong, traced to which
  alternatives were tested. Further runs of the memoryless 14-model
  framework cannot settle it. Its result is already proven there.
title: "In a community that updates a single consensus model by sound pairwise model comparison, which models get proposed can hold the consensus on a false model while results reproduce almost perfectly, so reproducibility does not track convergence to truth"
version: 1
tags:
- philosophy-of-science
- epistemology
- social-science
date: '2026-10-14'
source:
- LIT-988
summary: >-
  Devezer, Nardin, Baumgaertner and Buzbas (2019), [LIT-988](../literature.d/LIT-988.md), read in full
  in [NOTE-tmpjvn8h](../notes.d/NOTE-tmpjvn8h.md). In a Markov-chain and agent-based model where each
  step tests one proposed linear model against the consensus by AIC or
  SC, replication cannot change the transition matrix. A boundary-testing
  population reproduces almost perfectly while rarely holding the true
  model, and correlations between reproducibility and truth depend on
  the strategy mix. The consensus is memoryless, scientists hold no
  beliefs, and an equal strategy mix is shown only never to be the
  worst, not best.
---
<!-- inactive-ok-file: THEORY-148 THEORY-146 — Proposed; accounts of community-level epistemic mechanisms this one sits beside -->

# THEORY-tmpz5itv: In a community that updates a single consensus model by sound pairwise model comparison, which models get proposed can hold the consensus on a false model while results reproduce almost perfectly, so reproducibility does not track convergence to truth

## Source

Devezer, Nardin, Baumgaertner and Buzbas (2019), *PLOS ONE* 14(5):
e0216125 (arXiv:1803.10118v3), [LIT-988](../literature.d/LIT-988.md), read in full in [NOTE-tmpjvn8h](../notes.d/NOTE-tmpjvn8h.md).

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
