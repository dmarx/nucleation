---
status: Read
paper: 'LIT-tmp3ztxf'
title: 'Rashid et al. — QMIX: monotonic value function factorisation'
version: 1
history:
- version: 1
  date: '2026-10-24'
  note: >-
    Read in full on 2026-10-24 from arXiv:1803.11485v2 (6 June 2018, the
    ICML camera-ready), arXiv's non-exclusive distribution licence, a
    14-page PDF extracted by pdftotext: the 8-page paper (sections 1–8)
    and the supplement (A, representational complexity; B, the two-step
    game with every learned value table; C, the StarCraft II setup; D, all
    learning curves, read from captions and text). The reference list was
    skimmed. Page numbers below are v2's. Every quotation was checked
    against the extracted text by script.
date: '2026-10-24'
summary: >-
  Per-agent values Q_a(τ^a, u^a) are combined into a joint Q_tot by a
  mixing network whose weights, generated from the state, are kept
  non-negative, so ∂Q_tot/∂Q_a ≥ 0. Then the individually greedy actions
  form a greedy joint action and agents can act on their own values. It
  represents more than a sum and learned the optimum of a two-step game
  that a sum misses; it cannot represent a joint value in which one
  agent's best action depends on the others' current actions.
---
<!-- inactive-ok-file: THEORY-tmp56jxv THEORY-tmpayfgm — Proposed; filed from this reading and its companion, named -->
<!-- inactive-ok-file: CLAIM-436 CLAIM-440 CLAIM-451 THEORY-896 CLAIM-448 CLAIM-403 — Proposed; the claims and accounts this reading bears on, named in prose, nothing here rests on them -->

# NOTE-tmpoitn8: Rashid et al. — QMIX: monotonic value function factorisation

## Contribution

A team trained with central information must act on local information.
Learning a joint action-value Q_tot gives coordination but no way to act
locally; independent per-agent values act locally but cannot represent the
interaction. VDN took Q_tot as a sum of per-agent values. QMIX observes
that the sum is more than decentralised action needs: "we only need to
ensure that a global argmax performed on Qtot yields the same result as a
set of individual argmax operations performed on each Qa" (p. 2), and that
monotonicity in each Q_a is enough for that.

## Key insight

If Q_tot = f(Q_1(τ^1, u^1), …, Q_n(τ^n, u^n); s) with f non-decreasing in
each argument, then raising any Q_a cannot lower Q_tot, so the profile of
each agent's best action is a best joint action:
f(Q_1(ū^1), …, Q_n(ū^n)) ≥ f(Q_1(u^1), …, Q_n(u^n)) for every u, since
Q_a(ū^a) ≥ Q_a(u^a) for each a. (Re-derived when read; with weak
monotonicity the greedy profile is a maximiser, possibly one of several.)
The state is allowed to enter non-monotonically, by generating the mixing
weights from s through hypernetworks with an absolute-value activation
(p. 4), so that "Qtot is allowed to depend on the extra state information
in non-monotonic ways" (p. 4).

## Assumptions

- **Cooperative, shared reward**, in a Dec-POMDP (p. 3).
- **Centralised training, decentralised execution** (p. 3).
- **Representational claim (supplement A.1).** With full observability,
  QMIX represents any Q_tot that "factors into a non-linear monotonic
  combination of the agent's individual value functions", given that each
  Q_a orders a's actions as Q_tot does:
  Q_a(s, u^a) > Q_a(s, u′a) ⇔ Q_tot(s, (u^−a, u^a)) > Q_tot(s, (u^−a, u′a)).
  Under partial observability it "cannot necessarily represent the value
  function" (p. 11).
- **Universal approximation of monotone functions** by non-negative-weight
  networks (Dugas et al. 2009), cited, not proved.

## Key results

- **Two-step game (pp. 5–6; supplement B).** Agent 1 picks a state; state
  2A pays 7 to every joint action, state 2B pays [[0, 1], [1, 8]]. QMIX
  learned 2B as 0.00, 1.00, 1.00, 8.00 and chose it, return 8. VDN learned
  −1.87, 2.31, 2.33, 6.51, valued 2A higher and took 7. A sum cannot fit
  2B: a₁ + b₁ = 0, a₁ + b₂ = 1 and a₂ + b₁ = 1 force a₂ + b₂ = 2, not 8
  (my check). QMIX without the state (QMIX-NS) also got 8; QMIX-Lin and
  VDN-S got 7 (Table 6).
- **StarCraft II (pp. 6–8).** Six maps, 20 runs each. IQL never learned to
  win consistently; VDN matched QMIX on 8m, where the heuristic wins 95%,
  and fell below the heuristic on 3s_5z and 1c_3s_5z. "QMIX is noticeably
  the strongest performer on all of the maps, in particular on the maps
  with hetergenous agent types" (sic, p. 7).
- **Ablations (p. 8).** On homogeneous 3m non-linear mixing was not
  needed; on 2s_3z and 3s_5z both the state and non-linear mixing were.
- **The limit (p. 5; supplement A).** "any value function for which an
  agent's best action depends on the actions of the other agents at the
  same time step will not factorise appropriately, and hence cannot be
  represented perfectly by QMIX." Example: [[2, 1], [1, 8]] (Table 3b).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Monotonicity of Q_tot in each Q_a makes the individually greedy profile a greedy joint action | proved (one line) | p. 4; re-derived |
| C2 | Monotonic mixing represents strictly more than additive mixing | shown by example | Table 3a; two-step game |
| C3 | It cannot represent joint values in which an agent's best action depends on others' simultaneous actions | shown by example | Table 3b |
| C4 | QMIX outperforms VDN and IQL on these StarCraft II maps | moderate: six maps, 20 runs | Figures 3, 6 |
| C5 | State conditioning and non-linear mixing are both needed on heterogeneous maps | moderate | Figures 4, 7 |

## Concepts

- **Monotonic value factorisation**: Q_tot non-decreasing in each Q_a,
  ∂Q_tot/∂Q_a ≥ 0 (Eq. 5).
- **Consistency**: the joint argmax equals the profile of individual
  argmaxes (Eq. 4), the condition QTRAN later names
  Individual-Global-Max ([LIT-tmpev178](../literature.d/LIT-tmpev178.md)).
- **Utility, not value**: each Q_a "is a utility function … and not a
  value function since by itself it does not estimate an expected return"
  (p. 4).
- **Hypernetwork**: a network whose output is another network's weights,
  here mixing weights generated from the state.

## Connections

VDN (Sunehag et al. 2017) is the additive special case; coordination
graphs (Guestrin et al. 2002) the classical factored alternative, needing
the dependencies given in advance. COMA ([LIT-tmpqx5wu](../literature.d/LIT-tmpqx5wu.md)) is the centralised
on-policy extreme. QTRAN ([LIT-tmpev178](../literature.d/LIT-tmpev178.md), [NOTE-tmp457xj](NOTE-tmp457xj.md)) shows the argmax
condition is weaker than monotonicity and that 3b-type payoffs still
satisfy it.

## Bearing on the record

- **The lead's description, "a precise condition for a collective common
  currency" ([CLAIM-436](../claims.d/CLAIM-436.md), [CLAIM-440](../claims.d/CLAIM-440.md)), needs narrowing.** Q_tot is a
  real-valued function from the start, so QMIX assumes the currency.
  What monotonicity adds is a condition on how the collective's currency
  relates to the members' own: each member's ranking of its own actions
  agrees with the collective's whatever the others do (supplement A.1).
  In [CLAIM-436](../claims.d/CLAIM-436.md)'s terms it is a separability condition on an ordering that
  already has a representation, not a condition for the representation.
- **[CLAIM-440](../claims.d/CLAIM-440.md) (appraisal as negotiation; common currency as an
  ordering).** A sharpening, mine. Under monotonic mixing the negotiation
  has nothing to do at execution time: every member can act on its own
  ranking and the result is collectively best. The case [CLAIM-440](../claims.d/CLAIM-440.md) cares
  about, perspectives that conflict, is exactly the case QMIX excludes, a
  member whose best action depends on what the others do. So QMIX marks
  the boundary of the conflict-free regime, the trivial compatibility
  complex of [CLAIM-440](../claims.d/CLAIM-440.md)'s defeater, and shows that it can be large: richer
  than any sum.
- **The ordinal alignment it requires is Wolpert & Tumer's factoredness.**
  Supplement A.1's condition, that Q_a and Q_tot order a's actions alike
  for every u^−a, is the factored condition of [LIT-tmp8bczu](../literature.d/LIT-tmp8bczu.md)
  ([NOTE-tmpo0w02](NOTE-tmpo0w02.md)), stated for values rather than utilities. Both are
  ordinal. Neither needs exchange rates between members.
- **[CLAIM-451](../claims.d/CLAIM-451.md), [TERM-077](../terms.d/TERM-077.md), [THEORY-896](../theory.d/THEORY-896.md) (cycles).** Irrelevant, and the
  reason is worth recording. In a cooperative game every agent's payoff is
  the shared reward, so the shared value is an exact potential and no
  improvement cycle can occur ([THEORY-896](../theory.d/THEORY-896.md)). All three cooperative papers
  in this batch work inside that corner; none bears on nonintegrability.
- **[CLAIM-448](../claims.d/CLAIM-448.md) and [CLAIM-403](../claims.d/CLAIM-403.md) (what the record admits).** Under partial
  observability QMIX may be unable to represent Q_tot when an agent's local
  view does not reveal the state (supplement A.1). That is a legibility
  limit: the collective ordering exists, and members cannot act on it from
  what they see. QTRAN's state-value term is a correction for it.
- No instruction for machine-learning practice is drawn here.

## Limitations

- **Conditions stated, not all proved.** The representational claim leans
  on a cited universal-approximation result and an assumed per-agent
  ordering; the partial-observability case is a remark.
- **Narrow evaluation.** Six StarCraft II combat maps against the built-in
  AI at medium difficulty, and one two-step game.
- **Monotonicity is sufficient, not necessary**, as the paper says
  (p. 4); its tests do not probe the non-monotonic cases it cannot
  represent. QTRAN does.
- **Slips.** "hetergenous" (p. 7); the two-step game's states are called
  2A and 2B in the paper and 2 and 3 in the supplement (B.1). Neither
  changes a result.

## Open questions

- How much of a realistic cooperative task is non-monotonic in QMIX's
  sense, and how much does it cost? The paper's maps do not say; QTRAN's
  penalised predator-prey begins to.
- Is there a characterisation of the joint values that admit monotonic
  factorisation that a learner could test from data?
