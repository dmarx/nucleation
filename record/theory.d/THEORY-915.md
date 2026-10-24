---
number: 915
status: Proposed
formerly:
- THEORY-tmpgos5n
promote_when: >-
  Data, not more simulation: in a sequential avoidance task with known
  transition structure, people's choices are fit better by a model with a
  pessimistic weight on their own future actions than by an optimal agent
  with inflated threat values or altered transition beliefs, and that
  weight relates to anxiety; or the model's own prediction confirmed, a
  free-choice premium reduced or reversed in anxious people. It is refuted
  if anxious avoidance in such tasks is explained as well by altered threat
  values with an optimal policy, or if the bias appears where no future
  avoidance is at stake. A qualitative match of new simulations to further
  published effects cannot settle it.
title: "In a Markov decision process, an agent that evaluates actions as if it will fail to avoid danger at later steps, while in fact choosing optimally at each step, spreads threat value to states far from the danger and avoids early and widely, which reproduces qualitatively exaggerated threat appraisal, fear generalization and several laboratory findings associated with anxiety"
version: 1
tags:
- psychopathology-and-treatment
- learning-and-conditioning
date: '2026-10-24'
source:
- LIT-1496
summary: >-
  Zorowitz, Momennejad & Daw (2020; preprint 2019), [LIT-1496](../literature.d/LIT-1496.md), read in
  full from the CC BY version of record in [NOTE-1136](../notes.d/NOTE-1136.md). A
  decision-theoretic argument and value-iteration simulations with a
  β-pessimistic Bellman equation. The misbelief is about the agent's own
  future control; the danger is represented correctly. No data are fitted.
  That learned values outlast correction of the misbelief is argued in the
  paper, not simulated, and is not part of this title.
supports:
- CLAIM-446
---
<!-- inactive-ok-file: CLAIM-446 THEORY-285 THEORY-910 — Proposed; the claim and readings this bears on, named, nothing here rests on them -->

# THEORY-915: In a Markov decision process, an agent that evaluates actions as if it will fail to avoid danger at later steps, while in fact choosing optimally at each step, spreads threat value to states far from the danger and avoids early and widely, which reproduces qualitatively exaggerated threat appraisal, fear generalization and several laboratory findings associated with anxiety

## Source

Zorowitz, Momennejad & Daw, [LIT-1496](../literature.d/LIT-1496.md), read in full in [NOTE-1136](../notes.d/NOTE-1136.md)
from the version of record, Computational Psychiatry 4: 1–17 (2020),
CC BY 4.0: pp. 3–9 and 12–14, Figures 1–5.

## What was actually shown

Under the optimal Bellman equation, opportunities for reward propagate to
earlier states and avoidable threats do not, "because the return-maximizing
action is to avoid" (p. 3). Replacing the max over next actions with a
mixture of best and worst (weight w) makes the agent expect to fail later.
In a gridworld, negative value then spreads from the threat to antecedent
states and the optimal path keeps its distance (Fig. 1). The same agent
cashes out earlier in the balloon analogue risk task, approaches more slowly
as potential loss grows in a sleeping-predator task, and avoids a branch
with an early large loss and a later larger gain (Figs 2–3), matching
findings in anxious people that the paper cites. In learning, the spread of
negative value can end with the agent forgoing action altogether (Fig. 4).

What could have come out otherwise: a pessimistic weight might have
produced only local caution near the threat. It produced spread across the
whole state space, growing as w falls.

## What this does not say

- **That anxious people have this misbelief.** No behaviour is fitted.
  The one empirical test the paper proposes, a reduced free-choice premium,
  is left for future work.
- **That the danger is overestimated.** The point of the model is that it
  need not be: the threat's value and the world's transitions are correct.
- **That avoidance survives correction of the misbelief.** The paper
  argues it "may" (p. 8), by analogy with model-free relearning; it does
  not simulate it.
- **That this is the only placement of the pessimism.** Pessimism about
  the world's transitions or the current state could, the authors say,
  produce similar symptoms; only the self-policy version is simulated.
- **That it covers all anxiety.** The authors exclude OCD compulsions and
  PTSD memory disturbance (pp. 11–12).

## Connections

- **[CLAIM-446](../claims.d/CLAIM-446.md).** A rival account of the phenomena the claim
  explains, in which avoidance is kept by a belief about one's own future
  control while the threat is represented correctly. The claim's test,
  which holds the represented threat probability fixed, would not separate
  them; it needs to hold the control belief fixed as well. The paper's
  explanation for avoidance outlasting a corrected belief, cached value, is
  the habit-with-memory alternative the claim's defeater names.
- **[THEORY-910](THEORY-910.md).** Brown et al. read pessimistic policies as possibly
  normative under threat rather than as anxiety. This paper allows the
  same: pessimism "may reflect the exaggerative extremes of an otherwise
  adaptive evaluation strategy" (p. 11).
- **[THEORY-285](THEORY-285.md).** Both are model-level accounts of a threat representation
  that maintains avoidance; the maintaining variables differ.
