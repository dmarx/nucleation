---
status: Read
paper: 'LIT-tmplzs0t'
title: 'Richens, Abel, Bellot & Everitt — general agents contain world models'
version: 1
history:
- version: 1
  date: '2026-10-31'
  note: >-
    Read in full from the arXiv preprint 2506.01622v5 (20 October 2025),
    29 pp., the ICML 2025 camera-ready (PMLR 267), fetched 2026-10-31.
    Text extracted with `pdftotext -layout` and plain `pdftotext`; page
    numbers are the arXiv copy's. I read the abstract, §§1–6, Appendices
    A–D (all proofs, both algorithms, the experimental setup and Table 1)
    and the reference list; Figures 1–4 survive only as captions. I
    re-derived the proof's last step, the one-sided Chebyshev bound (54)
    to (57), and checked it numerically (scipy, my own script, not the
    authors' code): for n from 5 to 300, δ from 0 to 0.9 and 201 values
    of p, an adversarial δ-bounded agent that switches as early or as late
    as the regret bound allows never puts k*/n further from p than
    √(p(1−p)/(n(1−δ))), 0 violations in 12,060 cases, provided k ranges
    from 0. Algorithm 1 as printed loops from k = 1 and returns
    (k* − ½)/n, which can exceed that bound by up to 1/(2n). Theorem 2's
    construction (transitions independent of the action) was checked by
    hand.
date: '2026-10-31'
summary: >-
  In a fully observed, finite, communicating, stationary controlled Markov
  process, a deterministic goal-conditioned policy whose success
  probability is within a factor 1 − δ of optimal for every composite goal
  of depth up to n determines every transition probability to within
  √(2P(1−P)/((n−1)(1−δ))), and the estimate is computed from the policy
  alone, by asking it to choose between "at most k successes of this
  transition in n tries" and "more than k". An optimal myopic policy
  determines nothing. "Contains a world model" means exactly this: the
  transition function is recoverable from the input-output map. The
  authors say it shows "the existence of a world model encoded in the
  agent's policy, not its specific use", and the recovery map runs from
  the policy, not the activations, so it holds of any implementation of
  the same map, a lookup table over histories and goals included.
---
<!-- inactive-ok-file: CLAIM-tmph29mx THEORY-092 — Proposed; the owner's thesis this reading bears on and Block's argument, cited as open -->

# NOTE-tmp6gc1w: Richens, Abel, Bellot & Everitt — general agents contain world models

## Contribution

A proof by reduction that competence across a family of goal-directed
tasks fixes the environment's dynamics. The authors take a minimal
definition of a general agent (a goal-conditioned policy with a regret
bound over a set of temporal-logic goals) and give an algorithm that
returns the transition function from that policy alone, with an error that
shrinks as the regret bound tightens or the goal depth grows (Theorem 1).
They show the depth matters: an agent competent only at one-step goals
need encode nothing about the transition probabilities (Theorem 2). The
paper places this beside planning and inverse RL: "planning uses a world
model and a goal to determine a policy, and IRL ... use an agent's policy
and a world model to identify its goal, our result uses an agent's policy
and its goal to identify a world model" (Fig. 1 caption, p. 1).

## Key insight

An either-or goal turns a choice into a measurement. Offer the agent a
disjunction of two mutually exclusive plans, "take action a first, then
achieve the transition (s, a) → s′ at most k times in n attempts" or "take
b first, then achieve it more than k times". The optimal first action
reveals which side of the binomial median k lies on, and as k runs from 0
to n the switch point locates the median ⌊P(n + 1)⌋. A δ-bounded agent
may switch anywhere in a band around the median, and the band is narrow
when n is large. Everything is read from the agent's first action at s₀.

## Assumptions

- **Environment (Assumption 1, p. 2):** a controlled Markov process
  (an MDP with no reward) that is finite, stationary, communicating
  (every state reachable from every other) and has at least two
  actions.
- **Full observation.** The agent sees the state; the authors flag
  partial observation as the main limitation (p. 7).
- **Deterministic policies** π(aₜ | hₜ; ψ) over histories and goals
  (§2.4, p. 3).
- **Goals (Defs. 2, 3, 6):** LTL formulas built from sub-goals
  O([(s, a) ∈ g]) with O ∈ {Next, Eventually, Now}, chained in sequence and
  joined by disjunction; depth = number of sub-goals. Attempting a
  transition n times is a goal of depth 2n + 1 (p. 18).
- **Bounded agent (Def. 5):** P(τ ⊨ ψ | π, s₀) ≥ (1 − δ) max_π P(τ ⊨ ψ |
  π, s₀) for every ψ of depth ≤ n and every initial state. The proof uses
  only O(n|A||S|²) of these goals (p. 6).
- **World model (§2.5):** any estimate P̂_{ss′}(a) of the one-step
  transition function with bounded error. Not a state representation, and
  not the agent's own subjective model.
- No rationality axioms, no architecture, no training procedure.

## Key results

- **Lemma 6 (p. 16).** For the disjunction ψ(r, n) over all orderings of r
  successes and n − r failures of (s, a) → s′, the optimal success
  probability is C(n, r) P^r (1 − P)^{n−r}. The proof extends the action
  set with a reset action, shows a policy that resets after every attempt
  is optimal there, and then reaches the same value without the reset by
  Lemma 1's return policy, which exists because the process is
  communicating.
- **Theorem 1 (pp. 4, 17–20).** With ψ_{a,b}(k, n) = ψ_a(k, n) ∨ ψ_b(k, n),
  the agent's first action witnesses P_n(X ≤ k) ≥ (1 − δ)P_n(X > k) or the
  reverse (eqs. 39–40). The switch point k* satisfies
  P_n(X ≤ k*) ≥ (1 − δ)/(2 − δ) and P_n(X ≥ k*) ≥ (1 − δ)/(2 − δ) (eqs.
  41–42). One-sided Chebyshev then gives |k* − nP| ≤ √(nP(1−P)/(1−δ)),
  so |P̂ − P| ≤ √(P(1−P)/(n(1−δ))) for n attempts, and with depth
  N = 2n + 1, **|P̂ − P| ≤ √(2P(1−P)/((N−1)(1−δ)))**, for any N, δ < 1.
  For δ ≪ 1 and nP(1−P) ≫ 1 a Berry–Esseen argument gives
  O(δ/√n) + O(1/n). Deterministic transitions (P ∈ {0, 1}) are recovered
  exactly, by the convention that k* = 0 when the agent always picks a.
- **Theorem 2 (pp. 5, 20–21).** For myopic goals (reach a set at the next
  step) an optimal policy gives only the trivial bound ε = 1, and this is
  tight: if every action has the same transition law, every choice is
  optimal, so the policy is compatible with any value of P.
- **Experiments (§3.1, App. D).** One random 20-state, 5-action process
  with at most five outcomes per state-action pair. The agent is
  **model-based**: it estimates a transition model from random-policy
  trajectories of length 500 to 10,000 and plans on it. Algorithm 2 reads
  a transition model off its choices. Mean error falls from 0.171 to
  0.031 (Table 1) and scales like n^{−1/2} in depth, although every
  agent had worst-case regret δ = 1 on some goal, so Def. 5 never held.
  Ten seeds per size.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | A δ-regret-bounded goal-conditioned policy over depth-n goals determines the transition function within √(2P(1−P)/((n−1)(1−δ))) | strong | Theorem 1, proof re-derived; the bound checked numerically for the estimator k*/n with k from 0 |
| C2 | An optimal myopic agent need encode nothing about transition probabilities | strong | Theorem 2, a two-line counterexample |
| C3 | "there is no way to train an agent capable of generalizing to long horizon tasks without learning a world model" (p. 6) | strong in the paper's sense, weak in the ordinary one | Theorem 1, where "learning a world model" means only that the policy determines P̂ |
| C4 | The algorithm recovers accurate models even when the regret bound fails | weak | one environment, a model-based agent, average regret |
| C5 | Domain generalization needs strictly more knowledge than task generalization (p. 8) | moderate | an argument with Richens & Everitt 2024, not a theorem here |
| C6 | Competence "can be measured", so assuming competence is "more defensible" than assuming a world model (p. 9) | weak | assertion |

## Method

Algorithm 1 (p. 22): for each (s, a, s′), fix an alternative action b; for
k = 1, …, n query π(a₀ | s₀; ψ_{a,b}(k, n)); stop at the first k where
the agent picks a; return (k* − ½)/n. Algorithm 2 (p. 23) uses two
nested goals and solves P^n = (1 − P)^{k*−½} for P̂. Looping over all
transitions recovers the whole function. A small mismatch: the proof's
bound (57) is for k*/n with k allowed to be 0; the printed algorithm
starts at k = 1 and subtracts ½, which in my check exceeds the bound by
up to 1/(2n), negligible at large n.

## Concepts

- **General agent** — a goal-conditioned policy satisfying Def. 5; "a
  minimalist definition" (p. 2).
- **World model** — "any approximation P̂_{ss′}(a) of the transition
  function" with bounded error (p. 4). Predictive, one-step, about the
  true environment.
- **Contains / encodes / has learned** — used interchangeably for: a map
  exists from the policy to P̂. "The existence of this algorithm, which
  converts π into a bounded error world model, implies the world model is
  encoded in the agent's policy" (p. 5).
- **Subjective world model** — recovered instead if Def. 5 is replaced by
  δ-optimality with respect to the agent's own model M (eq. 3, p. 8).

## Connections

- Brooks 1991 ([LIT-436](../literature.d/LIT-436.md), [THEORY-689](../theory.d/THEORY-689.md)) is the paper's named foil: "the world
  is its own best model" (p. 1). The theorem does not touch Brooks's
  architectural point, that the robot has no central representation; it
  says that a Brooks robot competent across a rich enough goal family
  would have a policy from which P can be read.
- The good regulator theorem (Conant & Ashby) is criticized for counting a
  deterministic policy as a model (p. 9). Representation theorems
  (Savage) fit a world model to any policy, even a random one, and so say
  nothing about the true dynamics (p. 8). The paper's result is the
  contrast case: the model it recovers is unique up to ε and is the
  environment's.
- Mechanistic interpretability establishes a world model by a map from
  activations plus interventions; the paper's map is from the policy, which
  "is strictly weaker (as the policy is a function of the activations)"
  (p. 7). Footnote 1 (p. 8) argues that establishing a world model by
  interventional consistency "risks circular reasoning".
- Richens & Everitt 2024 is the domain-generalization companion (causal
  world models from robustness to distribution shift). Kenton et al.
  ([LIT-909](../literature.d/LIT-909.md)) shares authors and the interventional view of agency; Abel
  et al. ([LIT-969](../literature.d/LIT-969.md)) shares an author and the frame-relativity of agency,
  which this paper does not take up.

## Bearing on the record

- **[CLAIM-tmph29mx](../claims.d/CLAIM-tmph29mx.md), the owner's U20 thesis.** It does not defeat the
  thesis as stated; it defeats one reading the thesis already disowns,
  and it corrects one of the thesis's three kinds of evidence.
  - *The defeated_if is not met.* That condition asks for "an internally
    realized predictive component that can be identified by
    intervention, under matched memory, computation, intervention
    repertoire and developmental history", and a behavioural signature
    "that no organization of the same resources without such a component
    reproduces". The theorem quantifies over every policy satisfying
    Def. 5 "regardless of the details of its training and architecture"
    (p. 2). It makes no resource comparison, no intervention on
    internals, and it explicitly rejects interventional consistency as a
    criterion (footnote 1). A lookup table indexed by (history, goal)
    that copies a competent agent's choices satisfies Def. 5 and yields
    the same P̂. By the paper's own definition, the table "contains a
    world model". So the theorem cannot separate the table from the
    model-based agent, which is the thesis's point.
  - *It does defeat the functional reading.* The thesis's "What it does
    not say" leaves open whether the table "contains" a model
    functionally, and names this paper as the objection "if it holds".
    It holds, under Assumption 1 and Def. 5. Within that scope a world
    model is not merely "an explanation of the behaviour", an ascription
    a different stance could withhold. The transition function is
    identifiable from the goal-conditioned input-output map, uniquely to
    within ε. That differs from Savage-type fits and from Orseau et al.'s
    prior-relative verdicts ([THEORY-624](../theory.d/THEORY-624.md)). On this reading the "folk
    explanatory tool" wording is too weak. The attribution is a
    measurable property of the behavioural disposition, though not of any
    finite run of behaviour.
  - *It corrects the evidence list.* The thesis names "generalization
    beyond the interface" as evidence that the model is realized: "A
    model can serve new objectives ... The table cannot." If the table's
    domain includes the goals, it can, and the theorem then applies to it
    equally. Generalization to goals *outside what was tabled* still
    discriminates; generalization across a goal family that the
    implementation covers does not. Compression is untouched and in fact
    sharpened: a table over all histories and goals of depth n carries at
    least the information in P to precision ε, and the theorem gives no
    lower bound on how compactly.
  - *Scope.* The thesis's construction has one fixed interface, no goal
    input and a finite horizon. Theorem 2 shows that a single-objective
    or myopic agent need encode nothing about P. So on the thesis's own
    setup the theorem does not apply; it applies once the interface is
    widened to a family of goals. The functional reading deserves a
    counter of its own, objecting to [CLAIM-tmph29mx](../claims.d/CLAIM-tmph29mx.md); this reading does
    not file it.
- **[THEORY-092](../theory.d/THEORY-092.md) (Block).** Consistent. Block's machine is the table the
  theorem applies to. The theorem supplies a precise sense in which
  Block's machine, if it covered a goal family, would "contain" a world
  model, and says nothing about whether it has intelligence or how its
  responses are produced.
- **[THEORY-689](../theory.d/THEORY-689.md) (Brooks).** Not contradicted. Brooks's robots have three
  fixed layers, not goal-conditioned policies over an LTL family.
- **An instruction for ML practice is present**: train on sufficiently
  diverse multi-step goals, prefer model-based architectures, extract
  world models with Algorithm 1 for safety (pp. 6–9). That belongs to the
  Anthology of the SOTA; the LIT keeps its `anthology-candidate` flag.

## Limitations

- Fully observed, finite, stationary, communicating environments only.
- Deterministic policies; the extraction reads one first action per goal.
- The regret bound must hold for every listed goal from every initial
  state. The authors' own agents violated it (δ = 1 on some goals).
- The experiments use a model-based agent, so they do not test the case
  the title is about, a model-free one.
- "Contains" is informational. The paper says so: "Theorem 1 proves the
  existence of a world model encoded in the agent's policy, not its
  specific use (e.g. for planning), nor can we make deeper epistemological
  claims about what the agent knows" (p. 7).
- No bound on query complexity beyond O(n|A||S|²) goals, and none on the
  size or cost of a policy meeting Def. 5.

## Open questions

- Is there a resource lower bound to go with Theorem 1: does any
  implementation meeting Def. 5 on a large enough goal family need memory
  close to that of P itself rather than of a table? That would turn the
  informational result into the compression evidence [CLAIM-tmph29mx](../claims.d/CLAIM-tmph29mx.md) asks
  for.
- Under partial observation, what must be recoverable: a predictive state
  representation, a belief model, or less?
- Does the theorem survive stochastic policies, where the first action is
  a distribution and the switch point is blurred?
