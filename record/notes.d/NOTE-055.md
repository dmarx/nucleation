---
number: 55
status: Skimmed
formerly:
- NOTE-tmpgpet2
paper: LIT-046
title: 'Pilgrim et al. 2025, foundations of collective intelligence'
version: 1
date: '2026-09-25'
summary: >-
  The known forms of collective intelligence (wisdom of crowds, collective sensing, division of labour, cultural learning) can all be derived from one principle. Collectives have more sensing, memory, processing and action resources than individuals, but their distributed, modular structure imposes coordination and cooperation constraints, and the resulting trade-offs produce both qualitatively new collective algorithms and collective failures.
---

<!-- inactive-ok-file: LIT-046 — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-25 -->

# NOTE-055: Pilgrim et al. 2025, foundations of collective intelligence

## Contribution

The paper asks why collectives beat individuals on some problems. Its answer is that collectives have more computational resources (more sensory input, memory, processing capacity and ways to act), but their distributed, modular structure creates coordination and cooperation problems. The authors show how the resource advantages lead directly to the standard forms of collective intelligence. They derive testable predictions about distributed reasoning and context-dependent switching of behaviour. Case studies in animal navigation and decision-making show collectives using qualitatively different strategies, not just better versions of individual ones.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- Introduction (p. 1–2): positions the paper against a siloed literature (Condorcet and wisdom of crowds, collective sensing, cultural ratcheting, division of labour, Sumpter's interaction rules, Galesic et al., Couzin). The claim is that these are all aspects of one principle about resources and constraints.
- Framework (§2, tables): individual and collective are compared on sensory information, processes and actions. The collective state space is described as roughly the product of the members' state spaces, plus spatial and social relations.
- §3 "Constraints on Resource Use: Structure, Coordination and Cooperation": resources in one bird cannot be applied directly to information held by another. Coordination costs are synchronisation, communication overhead that grows with group size, and the cost of splitting and recombining subtasks. Cooperation problems are also covered.
- Mechanisms: information aggregation (distributions and inference; belief, memory persistence T, utility mapping u), feedback and deliberation, collective memory, and division of labour and specialisation.
- Case studies: golden shiners find dark regions through speed modulation plus attraction, with no individual representation of the gradient. Ant colonies choose new homes. Homing pigeons navigate collectively, with leadership and route compromise.
- Discussion (p. 11): open questions on collective reasoning (inferential, disjunctive, counterfactual), collective biases, "fast and slow" Type 1/Type 2 switching, evolutionary pathways including major transitions, and a reverse-Marr question: does the modular structure we perceive in the world mirror the modularity of collectives? The authors say the framework carries over to human societies, neural circuits and to integrating AI into society.

## Open questions

- A Marr-style computational-level framework for collectives maps directly onto multi-agent and ensemble systems, including AI collectives. Check whether the "predictions" are sharp enough to be falsified or mostly reframe existing results.
- The resources-versus-constraints decomposition is the main contribution. A deeper read should check whether it is formal (the tables and notation) or taxonomic.
- It connects to c31 (ant cooperative transport is cited as a synchronisation example) and to the individuality/major-transitions cluster (c30).
