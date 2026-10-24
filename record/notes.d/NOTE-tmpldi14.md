---
status: Read
paper: 'LIT-tmpqx5wu'
title: 'Foerster et al. — Counterfactual multi-agent policy gradients'
version: 1
history:
- version: 1
  date: '2026-10-24'
  note: >-
    Read in full on 2026-10-24 from arXiv:1705.08926v3 (11 December 2024),
    arXiv's non-exclusive distribution licence, an 11-page PDF extracted by
    pdftotext. Read: abstract, sections 1–7, the errata, appendix A (the
    proof of Lemma 1, read from a layout extraction and re-derived),
    appendices B and C (training details and Algorithm 1), every table and
    figure caption. The reference list was skimmed. v2 (14 December 2017)
    was extracted to check the erratum: its Eq. 4 is A^a(s, u) = Q(s, u) −
    Σ π^a(u′a | τ^a) Q(s, (u^−a, u′a)), with no history. The AAAI version
    of record was not compared. Page numbers below are v3's. Every
    quotation was checked against the extracted text by script.
date: '2026-10-24'
summary: >-
  A centralised critic Q(s, τ, u) trains decentralised actors, and each
  agent's action is scored against the critic's average over its own
  alternatives under its own policy, the others' actions fixed. The
  baseline does not change the expected gradient. On StarCraft
  micromanagement with a narrow field of view it beat independent and
  central-V/QV actor-critics on four maps. The counterfactual is the
  critic's estimate, not a simulation, and it values alternatives the
  agents sometimes take.
---
<!-- inactive-ok-file: LIT-tmpkensg — Unavailable; cited as the source COMA names, not leaned on -->
<!-- inactive-ok-file: THEORY-tmp1p6ly — Proposed; filed from this reading, named -->
<!-- inactive-ok-file: CLAIM-tmp8z857 QUESTION-tmponjie QUESTION-tmpdicvf CLAIM-tmp0qupq CLAIM-277 CASE-tmpw4r7u CLAIM-tmp1xoac THEORY-tmp3oyxw — Proposed, Open or new; the claims and questions this reading bears on, named in prose, nothing here rests on them -->

# NOTE-tmpldi14: Foerster et al. — Counterfactual multi-agent policy gradients

## Contribution

Cooperative agents that share one reward cannot tell from it which of them
did well: "joint actions typically generate only global rewards, making it
difficult for each agent to deduce its own contribution to the team's
success" (p. 1). Difference rewards (Wolpert & Tumer) answer this with a
counterfactual, the reward had the agent taken a default action, but need a
simulator and a chosen default. COMA gets the counterfactual from a learned
centralised critic and replaces the default action with the agent's own
policy-weighted average, in a form that provably leaves the policy
gradient's expectation unchanged.

## Key insight

The baseline for agent a is

    b^a(s, τ, u^−a) = Σ_{u′a} π^a(u′a | τ^a) Q(s, τ, (u^−a, u′a)),

the critic's value of the joint action averaged over a's own alternatives
under a's current policy, with every other agent's action as it actually
was (Eq. 4). The advantage A^a = Q(s, τ, u) − b^a says how much better a's
actual action was than what a typically does in this situation, given what
the others did. Since b^a does not depend on u^a, Σ_{u^a} π^a ∇ log π^a ·
b^a = b^a ∇ Σ_{u^a} π^a = b^a ∇1 = 0 (Appendix A, Eqs. 9–13; re-derived
when read). The baseline reduces variance and nothing else. A critic that
takes the others' actions as input and outputs one value per action of
agent a computes all of a's counterfactuals "in a single forward pass"
(p. 1).

## Assumptions

- **A cooperative game.** All agents share one reward r(s, u) (p. 2).
- **Centralised training, decentralised execution.** The critic sees the
  state s and joint history τ during training; each actor conditions only
  on its own history τ^a (pp. 2–3).
- **Lemma 1's conditions** are Sutton et al.'s (1999): bounded rewards, a
  differentiable policy, a critic trained against unbiased targets (TD(1)),
  converged before each gradient step, and compatible with the policy
  (Appendix A). The joint policy is read as a single-agent policy over the
  MDP whose state is (s, τ).
- **Exploration floor.** Action probabilities are bounded below by ε/|U|,
  ε annealed from 0.5 to 0.02 over 750 episodes (p. 6). The critic's
  counterfactual values for an action are learned from occasions on which
  it was taken.
- **Discrete actions.** Continuous ones would need Monte Carlo or analytic
  forms of the sum in Eq. 4 (p. 5).

## Key results

- **Win rates (Table 1, p. 7).** Mean over the final 1000 evaluation
  episodes, 95% intervals in parentheses:

  | map | IAC-V | IAC-Q | central-V | central-QV | COMA |
  |---|---|---|---|---|---|
  | 3m | 47 (3) | 56 (6) | 83 (3) | 83 (5) | 87 (3) |
  | 5m | 63 (2) | 58 (3) | 67 (5) | 71 (9) | 81 (5) |
  | 5w | 18 (5) | 57 (5) | 65 (3) | 76 (1) | 82 (3) |
  | 2d_3z | 27 (9) | 19 (21) | 36 (6) | 39 (5) | 47 (5) |

  The hand-coded heuristic scored 35, 66, 70 and 63; it beats every
  learner on 2d_3z.
- **The baseline matters.** "COMA strictly dominates central-QV, both in
  training speed and in final performance across all settings" (p. 7).
  Central-QV has the same critic and V as baseline, so this isolates the
  counterfactual.
- **Centralisation matters.** Central critics beat the independent ones on
  every map (Figure 3).
- **Best runs.** COMA's best agents (98, 95, 98, 65) are "comparable" to
  centralised controllers with full view and macro-actions (Table 1,
  p. 7), a best-run comparison the conclusion flags as "best-performance
  reporting" (p. 7).
- **Scaling.** Agent-factored critics were tried; "the bottleneck for
  scalability was not the centralisation of the critic, but rather the
  difficulty of multi-agent exploration" (p. 6).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The counterfactual baseline leaves the expected policy gradient unchanged | proved | Appendix A; re-derived |
| C2 | COMA converges to a local optimum under Sutton et al.'s assumptions with the critic conditioned on (s, τ) | proved by reduction, as corrected in v3 | Lemma 1, Appendix A, errata |
| C3 | The counterfactual baseline improves on a V baseline with the same critic | moderate: four small maps, 35 trials each | Table 1, Figure 3 |
| C4 | Centralised critics beat independent ones here | moderate | Table 1 |
| C5 | COMA avoids the self-consistency problem of the aristocrat utility | argued | p. 4: the baseline depends on the policy but its expectation does not |

## Concepts

- **Counterfactual baseline**: the critic's expected value of the joint
  action when agent a's action is replaced by a draw from a's own policy,
  the others' actions fixed (Eq. 4).
- **Difference reward**: D^a = r(s, u) − r(s, (u^−a, c^a)), the reward
  minus the reward with a's action replaced by a default c^a. "Any action
  by agent a that improves D^a also improves the true global reward"
  (p. 4), since the subtracted term does not depend on a's action.
- **Aristocrat utility**: the difference reward with the default replaced
  by an expectation over a's actions; "this advantage has the same form as
  the aristocrat utility" (p. 4).
- **Centralised training with decentralised execution**: extra state and
  free communication while learning, local histories only while acting.

## Connections

Builds on difference rewards (Wolpert & Tumer; Tumer & Agogino 2007;
[LIT-tmpkensg](../literature.d/LIT-tmpkensg.md), [LIT-tmp8bczu](../literature.d/LIT-tmp8bczu.md)) and on the policy-gradient theorem (Sutton et
al. 1999). Concurrent with MADDPG (Lowe et al. 2017), which uses one
centralised critic per agent and no credit assignment. QMIX ([LIT-tmp3ztxf](../literature.d/LIT-tmp3ztxf.md))
is the same group's value-based alternative and positions COMA as the
fully centralised, on-policy extreme. The v3 erratum points to Lyu et al.
(2021–2024) on centralised critics.

## Bearing on the record

- **The lead's description needs correcting.** COMA does not ask "what if
  this process had not acted". Its counterfactual is "what if this agent
  had acted as it usually does", under its own current policy, with every
  other agent's actual action held fixed. Removal is the difference-reward
  default c^a, which COMA was designed to avoid. And every agent acts on
  every step: COMA credits processes that all act, under a shared reward,
  not processes some of which are never heeded.
- **[CLAIM-tmp8z857](../claims.d/CLAIM-tmp8z857.md) (avoidance destroys identifiability).** Irrelevant to
  the step, or rather a restatement of it. The counterfactual values are
  the critic's, learned from occasions on which each alternative was
  taken, and the ε/|U| floor exists to guarantee such occasions. An agent
  whose alternative is never sampled has no data from which a critic
  could value it, and nothing in the method replaces that data; "relying
  on extra simulations" is what COMA avoids, not what it adds (p. 2). So
  counterfactual credit presupposes the evidence that avoidance withholds.
  What the paper does supply is the decomposition the claim needs between
  the two problems: noise from others' variation (which a counterfactual
  baseline removes, holding them fixed) and absence of evidence about an
  untried alternative (which it does not touch).
- **[QUESTION-tmpdicvf](../questions.d/QUESTION-tmpdicvf.md), failure 4 (bandit feedback).** The question lists
  "counterfactual credit and difference rewards" as a candidate procedure
  for crediting unheeded processes. The reading narrows it. COMA's
  procedure has a guarantee (an unbiased gradient) whose price is an
  exploration floor and a critic that generalises; the floor is the
  protected-access mechanism the same list names for mixtures of experts.
  Without it the counterfactual is an extrapolation of the critic.
- **[QUESTION-tmponjie](../questions.d/QUESTION-tmponjie.md) (an accurate evaluation denied authority).** A loose
  but exact analogue. In COMA an agent's advantage can be positive, its
  action better than its usual, without changing what the others do: the
  baseline holds them fixed. Credit is computed per agent and changes only
  that agent's policy. An organization that computed such credit for an
  unheeded process and did not route it to that process's authority would
  be the question's case, measured. The paper does not consider routing.
- **[CASE-tmpw4r7u](../cases.d/CASE-tmpw4r7u.md) and [THEORY-tmp3oyxw](../theory.d/THEORY-tmp3oyxw.md) (authority as a replicator).** A
  precise link, mine. In the replicator reading the excess score of
  process a is q_a − v, its expected score less the policy-weighted mean.
  COMA's advantage is the same quantity for one agent with the others
  fixed: Q at the chosen action less its π^a-weighted mean. So COMA's
  credit is the replicator's fitness-minus-mean evaluated per member, and
  its single-sample estimate needs the critic to supply the mean that a
  bandit learner cannot observe.
- **[CLAIM-tmp0qupq](../claims.d/CLAIM-tmp0qupq.md) and [CLAIM-277](../claims.d/CLAIM-277.md) (endorsement that tracks competence).** A
  candidate for "tracks". A competence signal with the others' variation
  removed is the counterfactual advantage; a team-shared reward is the
  signal without it. The paper shows the second learns worse.
- No instruction for machine-learning practice is drawn here.

## Limitations

- **Small, specific tests.** Four StarCraft maps of three to five units,
  35 trials each; hyperparameters tuned on 5m and reused (p. 6).
- **Best-run comparison.** The comparison with centralised controllers
  uses COMA's best agents against published results in a different
  setting, as the authors note.
- **Convergence is local and idealised.** Lemma 1 assumes a converged,
  compatible TD(1) critic before each gradient step, which the deep critic
  trained by TD(λ = 0.8) does not satisfy.
- **The erratum.** Versions before v3 had a critic without the joint
  history, for which the proof did not go through. A reader of the AAAI
  paper meets the uncorrected form.
- **A slip in the proof.** The constructed MDP's transition is written
  P(s′ | s) 1(z′, z) (Appendix A), dropping the joint action from
  P(s′ | s, u). It does not affect the argument.

## Open questions

- How well does the critic value an action the policy has nearly stopped
  taking? The method's credit for rare alternatives is only as good as
  that extrapolation, and the paper does not measure it.
- Does the counterfactual baseline help when agents are many? The authors
  name exploration, not the critic, as the bottleneck.
