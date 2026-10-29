---
status: Read
paper: 'LIT-1128'
title: 'Holme and Newman — Coevolution of networks and opinions'
version: 1
history:
- version: 1
  date: '2026-10-29'
  note: >-
    Read in full on 2026-10-29 from arXiv's own copy, v3 of 9 March 2006
    (https://arxiv.org/pdf/physics/0603023, 5 pages), text extracted with
    pdftotext. Read: the abstract, §§I–V, the captions of Figures 1–5 and
    the 22 references. Figures were read from captions and text only; no
    number was taken from a chart. Checked: the random-graph percolation
    exponents the paper compares against (a = b = 1/3, community-size
    exponent 5/2) are the standard mean-field ones, and the τ ∼ log N
    argument at φ = 1 follows from the coupon-collector form the text
    gives. The model was not re-simulated. The journal version (Phys. Rev.
    E 74, 056108) was not compared; OpenAlex lists no free copy of it.
date: '2026-10-29'
summary: >-
  N agents with G = N/γ possible opinions on a random graph; at each step
  a random agent either moves one of its edges to a random holder of its
  own opinion (probability φ) or copies a random neighbour's opinion
  (1 − φ). The process always ends in disconnected communities each of one
  opinion. For k̄ = 4 and γ = 10 a continuous transition at
  φ_c = 0.458 ± 0.008 separates a giant like-minded community plus small
  ones (φ < φ_c) from only small communities of mean size about γ
  (φ > φ_c), with exponents a = 0.61, b = 0.7 and z = 0.61 outside the
  percolation class. Simulation only.
---

# NOTE-tmpnzvd7: Holme and Newman — Coevolution of networks and opinions

## Contribution

It writes down perhaps the simplest model in which opinions and ties
adapt to each other at once, with one parameter φ for the balance, and
shows by finite-size scaling that the balance has a critical value. At
that value the final distribution of community sizes is a power law
(exponent 3.5 ± 0.3), and the time to reach consensus fluctuates most and
slows critically.

## Key insight

Both moves remove disagreeing edges, so the dynamics always freezes into
like-minded components; φ only decides which components. Rewiring alone
freezes the initial opinion classes (Poisson sizes, mean γ); copying
alone freezes the initial graph's components (one giant one). Between the
two the outcome changes continuously, as in percolation but in a
different universality class, because the transition is the fixed point
of a non-equilibrium process rather than a static geometry.

## Assumptions

- **Random initial conditions.** M edges placed uniformly at random,
  opinions assigned uniformly at random; multi-edges and self-edges
  allowed, which the authors expect to matter little.
- **Fixed M and G**; opinions may go extinct.
- **Many nominal opinions** (G ∝ N), modelled on religious belief; the
  small-G case is set aside as "relatively simple".
- **Unweighted, undirected acquaintance**; rewiring targets any holder
  of i's opinion, not only near ones.

## Key results

- **Limits (§III).** φ → 1: community sizes follow the multinomial,
  Poisson(γ) for large N. φ → 0: components of the random graph, one
  giant plus an exponential tail, for k̄ > 1.
- **Critical point (Fig. 2–3).** N = 3200, M = 6400, γ = 10: a power law
  P(s) ∼ s^(−3.5 ± 0.3) at φ ≈ 0.458. Scaling S = N^(−a) F(N^b(φ − φ_c))
  for the largest community's fraction gives φ_c = 0.458 ± 0.008,
  a = 0.61 ± 0.05, b = 0.7 ± 0.1, against 1/3 and 1/3 for random-graph
  percolation.
- **Other parameters (Fig. 4).** φ_c moves with k̄ and γ (N from 200 to
  1600); collapses hold with exponents consistent with the above.
- **Dynamics (Fig. 5).** τ ∼ log N at φ = 1; the coefficient of variation
  of τ peaks near φ_c; τ ∼ N^z at the critical point with
  z = 0.61 ± 0.15, crossing at φ = 0.44 ± 0.03 (0.45 ± 0.02 in the
  caption).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The model always reaches a consensus state of like-minded components | strong | both moves only remove disagreeing edges (§III) |
| C2 | A continuous transition in the largest community's size occurs at a critical φ | moderate | finite-size scaling, N ≤ 3200, 10⁴ runs per point |
| C3 | The transition is not in the percolation universality class | moderate | a and b differ from 1/3 beyond the error bars |
| C4 | Consensus time shows critical slowing down | weak | one parameter set; the authors say good numerics are "considerably harder" |
| C5 | Power-law sizes of religious sects may reflect such criticality | weak | a remark; Yule processes are named as an alternative |

## Concepts

- **Consensus state**: no edge joins agents who disagree.
- **Community**: a connected component of the frozen network.
- **γ = N/G**: the mean number of holders per opinion.

## Connections

It combines voter-type opinion dynamics on static networks (Sood and
Redner, Castellano et al., Sznajd) with homophilous network formation
(McPherson et al., Newman's assortative mixing). Castellano, Marsili and
Vespignani's Axelrod-model transition is cited as a different mechanism.
Gross and Blasius's review ([LIT-1139](../literature.d/LIT-1139.md)) summarizes the paper, with φ
inverted (see that NOTE).

## Bearing on the record

- **[QUESTION-117](../questions.d/QUESTION-117.md).** A15 named it as a baseline for the coupled
  meaning–influence model. The reading says what kind of baseline. It has
  no influence weights, no authority, no evidence and no turnover:
  opinions are labels, every tie is equal, and the dynamics is absorbing,
  so its only outputs are the final community sizes and the time to
  freeze. What it can reproduce economically is fragmentation into
  like-minded camps against one dominant camp, controlled by the ratio of
  selecting one's contacts to being influenced by them, with a critical
  point between. What it cannot express is any outcome that depends on
  who has authority over whom, which is the circuit [QUESTION-117](../questions.d/QUESTION-117.md) asks
  about ([CLAIM-297](../claims.d/CLAIM-297.md), [CASE-092](../cases.d/CASE-092.md)). An answer to the question that rests on
  fragmentation alone would be matched by this model. Proposed dated
  note below.

No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- **Simulation only**, N ≤ 3200, one functional form of each move.
- **Absorbing dynamics.** Nothing persists except by freezing; there is
  no steady state to compare with a living organization.
- **Rewiring is global**: the new partner is any holder of the same
  opinion, which makes like-minded contacts free to find.
- **Slips.** The dynamical crossing is φ = 0.44 ± 0.03 in the text and
  0.45 ± 0.02 in the caption of Fig. 5. Some multi-edges and self-edges
  are formed and kept.

## Open questions

- Is there a transition of the same kind when ties are weighted or
  directed, as an endorsement network's are?
- What does the model do with entry and exit of agents, which would
  prevent freezing?
