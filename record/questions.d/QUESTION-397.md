---
number: 397
status: Open
formerly:
- QUESTION-tmp4jbc3
title: 'Under what conditions does a partial organization increase the probability of subsequent organization by changing the transition dynamics, rather than merely providing a more advanced initial state?'
version: 1
tags:
- complex-systems
- natural-sciences
- mathematics
date: '2026-11-05'
line:
- realizability
- nucleating-argument
summary: >-
  A's question, verbatim, from A's review of this pull request, pasted by
  the owner on 2026-11-05, §5. A candidate nucleus can raise the chance of
  the target because establishing it puts the system in a more advanced
  state under the same transition rules, a state advantage. It can also
  change the rates of later steps among components that have not joined
  it, a generative architectural advantage ([TERM-117](../terms.d/TERM-117.md)). A higher
  committor does not tell the two apart. A's test compares matched partial
  assemblies, with similar completion counts, inventories and conditions,
  while the candidate relations are manipulated, and measures downstream
  reaction hazards, not only final yield. [QUESTION-380](QUESTION-380.md) asks when a small
  compatible subsystem helps; this asks by which of the two routes. The
  wording is A's; adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-596 — new; the assistant's claim on yields and routes, cited as open -->
<!-- inactive-ok-file: TERM-117 — Proposed, Skimmed or new; entries cited as open -->

# QUESTION-397: Under what conditions does a partial organization increase the probability of subsequent organization by changing the transition dynamics, rather than merely providing a more advanced initial state?

## Why it is a question

A: "A candidate intermediate could improve eventual success simply because
establishing it moves the system closer to the target. That's different
from establishing a set of relations that reorganizes the subsequent
assembly process."

**The test, stated so that it does not depend on the representation.** An
earlier draft of this entry put the distinction as moving the starting
state against changing the generator Q. A's second review showed that
this depends on the representation. If the nucleus is part of the
complete state, its formation can change downstream rates while the
global generator stays the same. The representation-independent form is
a conditional causal effect on downstream transitions. Write y for the
configuration of the components outside the nucleus N, and compare

  Δk(y → y′) = k(y → y′ | do(N = 1)) − k(y → y′ | do(N = 0)),

the rate of a transition among the remaining components with the nucleus
established and without it, under matched physical conditions. A nucleus
gives a generative advantage when some Δk is non-zero for transitions it
takes no part in: it changes how other components interact. It gives only
a state advantage when every such Δk is zero, so that its contribution is
just the completed part of the assembly. In A's words, the question is
whether establishing the nucleus changes how other components interact,
"beyond the trivial advantage of having already completed some of the
assembly". Downstream reaction hazards, compared in matched states, are
the measurement.

## What the record has on it

- **The mechanism exists in DNA origami.** A bound domain raises the
  effective concentration of its staple's other domains, and a closed loop
  lowers the entropic cost of later loops. That is a change in the rates of
  steps not yet taken (Majikes et al. 2020 and 2021, Ni et al. 2026,
  Cumberworth and Reinhardt 2025).
- **An intervention close to A's test.** Schneider, Möritz and Dietz removed
  the earliest-binding segments, and the remaining domains bound later,
  through a slower pathway. That suggests the early domains changed later
  rates, but per-step hazards in matched states were not compared.
- **The term.** [TERM-117](../terms.d/TERM-117.md) draws the distinction; [CLAIM-480](../claims.d/CLAIM-480.md) holds how
  composition creates effective constraints.

## What would answer it

- **In molecules:** per-staple binding kinetics, of the kind Schneider et
  al. measured, compared between designs that differ only in a candidate
  nucleus. The comparison is restricted to staples outside it, at matched
  overall progress.
- **In a model:** a small Markov chain in which the nucleus's relations are
  both a state and a modifier of other rates, so the two effects can be
  switched on separately.
- **In organizations:** whether establishing a core changes how fast other
  relations form among people outside it, against starting with the core
  already in place but inert.

## Note of 2026-11-05: the readings on correction, repair, replication and nucleation barriers

Read at the owner's invitation to add readings to the DNA origami filing; the works were chosen by the assistant.

**Zhou, Sha, Ni, Seeman and Chaikin, "Mutations in artificial self-replicating tiles".**

- In Zhou et al. (2021) the template changes the rate of daughter formation rather than giving a head start: without it "no dimer was formed".
- The effect compounds, because daughters become templates, so the partial organization changes transition dynamics downstream.
- Left open: what structurally separates a sterile dimer from a templated one. The paper does not say.

No status changes.

## Note of 2026-11-05: what equilibrium evidence can and cannot show here

The assistant's reading across Cumberworth, Frenkel and Reinhardt 2022 ([NOTE-1638](../notes.d/NOTE-1638.md)) and [CLAIM-596](../claims.d/CLAIM-596.md). Their free-energy profiles show that stacking among bound staples makes binding more favourable for staples that are not part of the first cluster, a generative mechanism in this question's sense. Equilibrium free energies fix only the ratio of a step's forward and backward rates, by detailed balance. So a nucleus that changes the equilibrium of later steps may do it by speeding their binding or by slowing their unbinding, and evidence of either kind leaves the forward hazard Δk undetermined. [CLAIM-596](../claims.d/CLAIM-596.md) shows that yields cannot identify the route either. The measurement this question needs is therefore kinetic and per step: binding and unbinding rates of staples outside the nucleus, with and without it, at matched progress. No status changes.

