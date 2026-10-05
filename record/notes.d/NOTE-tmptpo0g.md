---
status: Read
paper: LIT-tmp8lzwo
title: 'The Communication Structure of Epistemic Communities'
version: 1
history:
- version: 1
  date: '2026-10-05'
  note: >-
    Read in full: the author's posted manuscript (17 pp.), §§1–5, figures
    from captions and axis labels. Page references are the manuscript's.
date: '2026-10-05'
summary: >-
  Simulations of Bala and Goyal's bandit model on small networks. Cycles
  learn the better action more reliably than wheels or complete graphs,
  and more slowly. Over every network of up to six agents, density and
  clustering predict failure, and centrality does not. The cause is that
  dense networks spread an early unlucky run to everyone before diversity
  can correct it.
---
<!-- inactive-ok-file: THEORY-tmpgo526 — Proposed; the network account filed in this batch -->

# NOTE-tmptpo0g: The Communication Structure of Epistemic Communities

## Contribution

It showed in finite simulated communities that less communication can make
a group more reliable. It located the cause in connectivity rather than in
a central hub, and named a speed–reliability trade-off.

## Key insight

When you learn only about what you try, a run of bad luck on the better
option can lead everyone to stop trying it. After that, no evidence can
bring them back. Dense communication makes everyone see the same bad run at
once; sparse communication leaves pockets of people still trying it.

## Assumptions

- Two states, two actions: A1 with the same known expected payoff in both
  states (uninformative), A2 better in one state and worse in the other.
- Agents choose myopically the action with highest expected utility, and
  update by simple Bayes on their own and neighbours' outcomes, not on the
  fact that a neighbour chose an action (n. 4).
- Initial beliefs uniform on (0, 1); the world set to the state in which A2
  is better.
- A run ends when everyone plays A1 (failure) or everyone believes the
  truth above 0.9999 (success).

## Key results

- **Cycle > wheel > complete** in probability of success, for every size
  studied; complete fastest (Figures 2–3, 10,000 runs per size).
- **Six-agent census.** Density is the strongest single predictor of
  failure; clustering adds a little; degree variance is uncorrelated with
  success (§3.2).
- **Mechanism.** In connected networks four times as many agents switch
  strategy after a disappointing round, and with one A2 player left a
  connected network is almost three times as likely to have none next round
  (§3.2).
- **Trade-off.** Four of the five most reliable six-agent graphs are
  minimally connected; the five fastest are complete or nearly so (Figure
  5).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | In this model sparser networks are more reliable and slower | strong | simulation over all networks of up to six agents |
| C2 | Connectivity, not hub centrality, causes the loss | moderate | regression on graph statistics, six-agent networks |
| C3 | The ordering holds for any parameter setting | weak | footnote 7; refuted by [LIT-tmphw2gz](../literature.d/LIT-tmphw2gz.md) |
| C4 | Limiting information can maintain the division of cognitive labour without epistemically impure motives | moderate | argued in §5 from the model |

## Method

Agent-based simulation of the Bala–Goyal model on fixed graphs: cycle,
wheel and complete graphs of 3–12 agents, and all graphs up to isomorphism
of 3–6 agents, 10,000 runs each.

## Concepts

- **royal family** — Bala & Goyal's agents connected to everyone; the wheel's
  hub in the finite case.
- **density** — the proportion of possible links present.

## Connections

Takes its model from Bala & Goyal (1998) and contrasts its solution with
Kitcher's and Strevens's reward-based accounts of the division of cognitive
labour, which require scientists to pursue theories they think less likely
for the sake of credit.

## Bearing on the record

Source of [THEORY-tmpgo526](../theory.d/THEORY-tmpgo526.md), with Rosenstock et al. as the second source
fixing its scope. It supports the owner's essay (§8.2) in the weak form
the essay states: more communication does not necessarily improve
collective judgment. The paper's own scope is narrow, as the
Limitations below say.

## Limitations

Small networks; one payoff gap (the paper says absolute probabilities can be
"manipulated by altering the expected payoffs"); myopic agents. The model
needs an uninformative action whose payoff is known to all, and outcome
evidence that depends on choices. Section 4 grants that its second and
third assumptions are "less innocuous".

## Open questions

Which real communities are in the parameter region where this holds. The
paper does not say, and [LIT-tmphw2gz](../literature.d/LIT-tmphw2gz.md) suggests it is a small one.
