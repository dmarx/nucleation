---
status: Read
paper: 'LIT-tmpev178'
title: 'Son et al. — QTRAN: learning to factorize with transformation'
version: 1
history:
- version: 1
  date: '2026-10-24'
  note: >-
    Read in full on 2026-10-24 from arXiv:1905.05408v1 (14 May 2019, the
    only version), arXiv's non-exclusive distribution licence, an 18-page
    PDF extracted by pdftotext: sections 1–5 (pp. 1–8) and the supplement
    (A, the training algorithm; B, the proofs of Theorems 1, 1a and 2 and
    Propositions 1 and 1a, read from a layout extraction and checked; C,
    environments and hyperparameters; D, the 310 random matrix games, with
    figures read from captions). The reference list was skimmed. Page
    numbers below are the PDF's. Every quotation was checked against the
    extracted text by script.
date: '2026-10-24'
summary: >-
  Defines Individual-Global-Max (IGM): per-agent values factorise a joint
  value when the profile of individual argmaxes is the joint argmax.
  Additivity and monotonicity are sufficient conditions; QTRAN trains the
  sum of individual values plus a state value to equal the joint value at
  the greedy profile and bound it elsewhere, which is sufficient and, up
  to rescaling, necessary. Every single-state matrix game satisfies IGM;
  VDN and QMIX missed the optimum in 177 of 310 random 3×3 games.
---
<!-- inactive-ok-file: CLAIM-446 — Proposed; compared in prose, nothing here rests on it -->
<!-- inactive-ok-file: THEORY-tmpayfgm THEORY-tmp56jxv — Proposed; filed from this reading and its companion, named -->
<!-- inactive-ok-file: CLAIM-436 CLAIM-440 CLAIM-403 CLAIM-448 QUESTION-270 — Proposed or Open; the claims and questions this reading bears on, named in prose, nothing here rests on them -->

# NOTE-tmp457xj: Son et al. — QTRAN: learning to factorize with transformation

## Contribution

QMIX showed that decentralised greedy action needs less than a sum. QTRAN
names what it needs, the Individual-Global-Max condition, and builds a
learner that targets IGM directly instead of a structural sufficient
condition. Its point is that "additive decomposability and monotonicity
are only sufficient — somewhat excessively restrictive — for
factorizability" (p. 1), and that the tasks they miss are the ones where
a lone defection is punished.

## Key insight

Do not make the joint value Q_jt itself decomposable. Learn Q_jt
unconstrained, learn per-agent Q_i, and require only that the transformed
value Q′_jt = Σ_i Q_i(τ_i, u_i), shifted by a state value
V_jt(τ) = max_u Q_jt(τ, u) − Σ_i Q_i(τ_i, ū_i), touch Q_jt at the greedy
profile ū and lie above it elsewhere (Theorem 1):

    Σ_i Q_i(u_i) − Q_jt(u) + V_jt = 0 at u = ū,  ≥ 0 otherwise.

Then Q_jt(ū) = Σ Q_i(ū_i) + V_jt ≥ Σ Q_i(u_i) + V_jt ≥ Q_jt(u), so ū is a
joint maximiser (supplement B.1; re-derived when read). The sum is a
surrogate with the same argmax, not a model of the joint value.

## Assumptions

- **Cooperative Dec-POMDP**, shared reward, centralised training and
  decentralised execution (pp. 2–3).
- **IGM as defined (Definition 1).** Factorisability is per joint history
  τ; a task is factorisable if Q_jt is factorisable under every τ (p. 3).
- **Necessity up to rescaling** (Proposition 1). If [Q_i] factorise Q_jt,
  some positive scaling αQ_i satisfies Theorem 1's condition. The proof
  takes α small enough, which needs the gaps strict: unique greedy actions
  and a finite action set.
- **Architecture.** The joint and state-value networks share lower layers
  with the agents' networks "at the expense of expressive power" (p. 4).

## Key results

- **One-step 3×3 game (Table 1, p. 6).** Payoff 8 at (A, A), −12 where one
  agent plays A alone, 0 elsewhere. QTRAN's individual values pick (A, A).
  VDN's pick (C, B) and QMIX's fail likewise; their learned values put
  the joint optimum below the safe actions.
- **IGM is cheap in single-state games.** "Since matrix games always
  satisfy IGM conditions, QTRAN-base always trains the optimal action for
  all 310 cases" (supplement D, p. 17). Of 310 random 3×3 games with
  payoffs in [0, 1], all three methods found the optimum in 114; VDN and
  QMIX both failed in 177; they differed in 19 (QMIX better in 14).
- **Gaussian squeeze (Figure 3).** All methods reached the single optimum
  with ε decay, QTRAN faster; without decay VDN and QMIX "significantly
  deteriorate" (p. 7). With two domains VDN and QMIX settled at a
  sub-optimal "pitfall".
- **Penalised predator-prey (Figure 4).** A capture pays 1 when two or
  more predators make it and −P when one does alone. "As the penalty P
  grows and exacerbates the non-monotonic characteristic of the
  environment, we observe a larger performance gap" (p. 8). With four
  predators and P ≥ 1, VDN and QMIX learned "running away from the prey to
  minimize the risks of being penalized" (p. 8).
- **QTRAN-alt.** A stronger condition on non-optimal actions (Theorem 2)
  learned more stably, most visibly with four agents (Figure 4f).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Theorem 1's condition is sufficient for IGM | proved | supplement B.1; re-derived |
| C2 | It is necessary up to positive rescaling of the Q_i | proved, with strict gaps | Proposition 1 |
| C3 | Additivity and monotonicity are strictly stronger than IGM | shown | 177 of 310 random games; Table 1 |
| C4 | Every single-state matrix game satisfies IGM | stated by the authors; true for a unique optimum, by indicator values | supplement D |
| C5 | QTRAN outperforms VDN and QMIX increasingly as tasks become less monotonic | moderate: two environment families | Figures 3–4 |

## Concepts

- **IGM (Individual-Global-Max)**: argmax_u Q_jt(τ, u) is the vector of
  argmax_{u_i} Q_i(τ_i, u_i) (Definition 1). "Simply put, the optimal
  joint actions across agents are equivalent to the collection of
  individual optimal actions of each agent" (p. 3).
- **Factorisable task**: one whose Q_jt satisfies IGM under every joint
  history.
- **Transformed joint value**: Q′_jt = Σ_i Q_i, a surrogate sharing Q_jt's
  argmax, corrected by V_jt for partial observability.
- **Non-monotonic task**: one where an agent's best action depends on the
  others', here a lone capture punished.

## Connections

Builds on VDN and QMIX ([LIT-tmp3ztxf](../literature.d/LIT-tmp3ztxf.md), [NOTE-tmpoitn8](NOTE-tmpoitn8.md)) and positions itself
against coordination graphs (Guestrin et al.). COMA's counterfactual
([LIT-tmpqx5wu](../literature.d/LIT-tmpqx5wu.md)) reappears in QTRAN-alt's "counterfactual joint network",
which computes Q_jt(τ, ·, u^−i) for each agent with the others' actions
fixed (p. 5).

## Bearing on the record

- **The lead's description, IGM as "a precise condition for a collective
  common currency" ([CLAIM-436](../claims.d/CLAIM-436.md), [CLAIM-440](../claims.d/CLAIM-440.md)), needs correcting.** IGM is
  stated for a real-valued Q_jt, so the currency is given. And with full
  observability the condition is nearly empty: any joint value with a
  unique optimum u* is factorised by Q_i(u_i) = 1 if u_i = u*_i, else 0
  (my construction), which is why "matrix games always satisfy IGM"
  (supplement D). What IGM constrains is whether members acting on local
  histories can each pick their part of the collective optimum; it lives
  in the gap between τ_i and τ.
- **[CLAIM-436](../claims.d/CLAIM-436.md) (ordering versus currency).** A complement, mine. IGM is
  weaker than an ordering, let alone a currency: it concerns only the top
  element. A collective can satisfy IGM with members whose rankings of
  their own actions disagree with the collective's below the top. In the
  3×3 game QTRAN's learned Q_1 ranks A first (3.84 against −2.06 and
  −2.25), yet against a partner playing B or C the joint value of agent 1
  playing A is −12 and of B or C is 0 (Table 1). Monotonic mixing requires agreement on the whole
  ranking; IGM requires it at the optimum alone. That is a third rung
  below [CLAIM-436](../claims.d/CLAIM-436.md)'s two, worth having: agreement on what to do, without
  agreement on how the rest compares.
- **[CLAIM-403](../claims.d/CLAIM-403.md) and [CLAIM-448](../claims.d/CLAIM-448.md) (access and legibility).** The nearest
  record analogue. Under partial observability IGM can fail because a
  member's local view does not distinguish situations in which its part
  of the optimum differs. QTRAN's V_jt absorbs what the members cannot
  see. A legibility regime that withholds the distinguishing evidence from
  a process makes the organization's optimum unreachable by local action
  even when every process is willing.
- **[QUESTION-270](../questions.d/QUESTION-270.md).** Not addressed: every agent's value is used.
- **The penalised predator-prey result** is a model of the record's
  protective lock-in in miniature, mine. Where a lone attempt is punished,
  value-factorising learners that cannot represent the interaction learn
  to avoid the prey altogether, and the payoff that coordination would
  reveal is never sampled. Compare [CLAIM-446](../claims.d/CLAIM-446.md)'s avoidance. The paper
  attributes it to representational limits, not to evidence.
- No instruction for machine-learning practice is drawn here.

## Limitations

- **Single-state examples overstate the method's reach**, since IGM is
  automatic there; the hard cases are partially observable, where the
  paper offers V_jt and experiments but no characterisation.
- **Two environment families** besides matrix games, all small.
- **Proof slips.** Proposition 1's proof says it shows "(4a)" where the
  inequality it proves is (4b), and it needs unique greedy actions; the
  conclusion is unaffected.
- **"Factorizable" depends on ties.** With several optimal joint actions,
  individual argmaxes can combine into a non-optimal profile; the paper
  does not discuss ties.

## Open questions

- Which partially observable tasks are not factorisable at all? The paper
  gives no example of a task outside IGM, only of tasks outside
  monotonicity.
- Does the transformed value's failure to track Q_jt off the optimum
  (QTRAN-base) matter for exploration in larger tasks, as QTRAN-alt's
  design suggests?
