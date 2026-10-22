---
number: 887
status: Proposed
formerly:
- THEORY-tmpiv9ap
promote_when: >-
  A study of a real network in which the attribute is observed, not
  assigned, that measures the correlation between degree and attribute and
  the share of nodes whose neighbours are mostly active, and finds that
  share well above the attribute's global prevalence where the correlation
  is high and the network disassortative, and close to it where they are
  not. It is refuted for real attributes if observed degree–attribute
  correlations turn out too weak to put more than a small share of nodes in
  the paradox regime. Further simulations on real topologies with assigned
  attributes cannot settle it: they show only that the illusion is
  possible. Even if promoted it would be a claim about what nodes can
  observe of their neighbours, not about what people come to believe or do.
title: "When an attribute is concentrated on well-connected nodes, many nodes can see it in a majority of their neighbours though it is globally rare, and the share that do grows with the correlation between degree and attribute, as the network becomes more disassortative and as its degree distribution becomes heavier-tailed"
version: 1
tags:
- network-science
- social-science
date: '2026-10-22'
source:
- LIT-1390
summary: >-
  Lerman, Yan & Wu (2016), [LIT-1390](../literature.d/LIT-1390.md), read in full in
  [NOTE-1085](../notes.d/NOTE-1085.md) from the PLOS ONE version. The "majority illusion": with 5%
  of nodes active, 60–80% of nodes in a heavy-tailed synthetic network
  can see an active majority among their neighbours; in disassortative real
  topologies, 60–70% with 20% active. A binomial model from the joint degree
  distribution predicts the share. The edge: the attributes are assigned by
  the authors on every network, real ones included, so this shows what
  topology permits, and nothing about what people perceive, believe or do.
---
<!-- inactive-ok-file: CLAIM-415 THEORY-242 — Proposed; the claim and account this one bears on, named, not leaned on -->
<!-- inactive-ok-file: LIT-1370 — Deferred or Unavailable; cited as a work the source names, not leaned on -->

# THEORY-887: When an attribute is concentrated on well-connected nodes, many nodes can see it in a majority of their neighbours though it is globally rare, and the share that do grows with the correlation between degree and attribute, as the network becomes more disassortative and as its degree distribution becomes heavier-tailed

## Source

Lerman, Yan & Wu (2016), *PLOS ONE* 11(2): e0147617, arXiv:1506.03022,
[LIT-1390](../literature.d/LIT-1390.md), read in full in [NOTE-1085](../notes.d/NOTE-1085.md) from the publisher's PDF. The
Supporting Information (S1 File, S1 Fig) was not read.

## What was actually shown

- **Synthetic scale-free networks** (N = 10,000, α = 2.1, 2.4, 3.1, 5% of
  nodes active). The share of nodes with more than half their neighbours
  active rises with the degree–attribute correlation ρ_kx, with
  disassortativity and with tail weight; at α = 2.1 it reaches 60–80%
  (Fig 2).
- **Erdős–Rényi networks.** The effect is much smaller but present, more
  so with 10–20% active (Fig 3).
- **Six real topologies** (co-authorship, protein interaction, Digg,
  Enron, Twitter, political blogs), with 5–30% of nodes activated and ρ_kx
  raised by swapping attributes. In the three disassortative ones, 60–70%
  of nodes see an active majority when 20% are active; less in the
  assortative ones (Fig 4).
- **A model** (Eqs 3–5) treating a node's neighbours as independent draws,
  with the probability of an active neighbour set by the joint degree
  distribution and P(x|k), reproduces the simulated shares. A Gaussian
  shortcut fails for heavy tails and strong (dis)assortativity (Fig 5).

What could have come out otherwise: the share in the paradox regime could
have stayed near the global prevalence once real topologies, with their
clustering and assortativity, replaced configuration-model graphs. It did
not, in the disassortative ones.

## What this does not say

- **Not that real attributes are distributed this way.** On every network
  the authors choose the active nodes and push ρ_kx to the values they
  want. Whether opinions, behaviours or adoptions are in fact concentrated
  on hubs strongly enough is not measured.
- **Not that anyone is misled.** No person's perception, estimate, belief
  or behaviour is measured. Each node's view of its neighbours is, by
  construction, accurate; the illusion is only in generalizing from them.
  That people do generalize this way is the authors' assumption.
- **Not a loud minority.** The mechanism is degree. A minority that speaks
  more often or more forcefully is a different mechanism (silence and
  expression, [THEORY-242](THEORY-242.md)).
- **Not pluralistic ignorance.** Pluralistic ignorance misjudges what others
  hold; the majority illusion samples correctly from a skewed
  neighbourhood. The paper offers itself as a possible explanation of the
  first, citing Prentice & Miller ([LIT-1370](../literature.d/LIT-1370.md)), without testing it.
- **Not that contagion is accelerated.** That rests on a 14-node
  illustration with a threshold model (Fig 1); no contagion is simulated.

## Connections

- **[THEORY-242](THEORY-242.md).** Vilone and Polizzi set themselves against this paper and
  find the network's direct, topological distortion small in their model.
  The two measure different things (an average local climate against a
  share of nodes with a local majority) under different placements of the
  minority (all nodes of one degree, against hubs at high ρ_kx), so both
  can hold. The two accounts are complementary routes to an apparent
  majority: one by who is seen, the other by who stays silent.
- **[CLAIM-415](../claims.d/CLAIM-415.md).** The claim grounds itself on this paper for a
  perceived plurality with no real one behind it. This account supplies
  the structural half of that: a collective majority attributed from an
  accurate but skewed sample. It supplies nothing about how the attribution
  organizes a person, which is the claim's own step.
