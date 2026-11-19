---
status: Read
paper: LIT-tmpsp5bi
title: 'Still 2017 (PRL 2020) — Thermodynamic cost and benefit of memory'
version: 1
history:
- version: 1
  date: '2026-11-19'
  note: >-
    URL read: https://arxiv.org/pdf/1705.00612 (arXiv author preprint, v3
    dated 3 Oct 2019; PDF, extracted with pdftotext). Kind: arXiv (step 5,
    first place to look). Date 2026-11-19. HTTP 200, no obstacle. Read: the
    whole letter, pp. 1-5 (setup, Eqs. 1-11, Szilard example, two-
    temperature protocol, efficiency, discussion). Skipped: reference list
    beyond what the text leans on. Not read: the published version, Physical
    Review Letters 124, 050601 (2020), DOI 10.1103/PhysRevLett.124.050601;
    not sought (arXiv v3 is the author's own late version). Any change
    between v3 and the PRL text is unchecked.
date: '2026-11-19'
---
<!-- inactive-ok-file: THEORY-817 — Proposed; cited in this filing of 2026-11-19 -->

# NOTE-tmp9h01y: Still 2017 (PRL 2020) — Thermodynamic cost and benefit of memory

## Contribution

Still extends Szilárd's engine to a partially observable system and lets memory formation and work extraction run at different temperatures. Forming a memory costs at least kT·I[M,X], and work extraction can recover at most kT'·I[M,Y], where Y is the part of the system the work-extraction device can manipulate and the data can predict. The difference gives a lower bound on dissipation (Eq. 8). Minimising that bound over the agent's stochastic map p(m|x) is exactly the information bottleneck, with the temperature ratio T'/T as the trade-off parameter. A Carnot-like protocol saturates the bound, and the efficiency falls below Carnot in proportion to the ratio of irrelevant to relevant bits retained.

## Key results

- Memory cost, Eq. (5), p. 2: "Operating a memory requires at a minimum dissipation proportional to the amount of information retained."
- Gain from memory, Eq. (6), p. 3: "The amount of heat that can get absorbed and turned into work is limited by how much information is retained about the variable(s) relevant with respect to work extraction."
- Isothermal bound, Eq. (7), p. 3: "the irrelevant information retained in memory sets a limit on how small dissipation can be". In symbols, −Q ≥ kT I_irrel ≥ 0, with I_irrel = I[M,X] − I[M,Y] = I[M,X|Y].
- Worked example, pp. 3–4: a three-state memory captures all the relevant information but dissipates at least ≈0.64kT, while a two-state memory dissipates at least ≈0.45kT. "the relative benefit does not outweigh the relative increase in cost."
- Two temperatures, p. 4: the three-state memory wins only above a temperature ratio of about 1.847. The general bound is −Q ≥ k(T I_mem − T' I_rel) (Eq. 8).
- The optimal strategy, Eqs. (9)–(10), p. 4: minimising the bound gives min I[M,X] − α I[M,Y], and "This optimization problem is a lossy data compression method called the Information Bottleneck".
- Efficiency, Eq. (11), p. 4: "efficiency is non-negative only when the fraction of relevant bits retained in memory is larger than the fraction of low to high temperature".

## Assumptions

- A cyclic engine. The system is re-prepared each cycle by a fixed procedure: "This preparation step is always the same procedure, and hence independent of the memory state" (p. 2). The agent's action therefore does not change the statistics of what it will observe next. "All changes performed on the system do not change the marginal distribution" (p. 2).
- The memory map depends only on the observable part (Eq. 3). Relevance is set by the physics of the work-extraction device, not chosen by the agent. Y collects the components that can be manipulated and are predictable from the data: "These are the components relevant for work extraction." (p. 2).
- Memory is not erased. "The memory is not reset to a specific state." (p. 2) So the I[M,X] cost is the cost of correlating memory with data, not a Landauer erasure cost.
- Ensemble averages and the second law applied to generalized free energy. Bounds hold on average, not per cycle. "memory preserving" temperature changes are assumed.

## Concepts

- Partially observable information engine: a system Z = (X, X̄), an agent memory M and a work-extraction device.
- Relevant (predictive) information I_rel = I[M,Y]; irrelevant information I_irrel = I[M,X|Y].
- Information bottleneck as the thermodynamically optimal data representation; α = T'/T as its Lagrange multiplier.
- Szilárd–Carnot cycle.

## Bearing on the record

- [QUESTION-tmprj00l](../questions.d/QUESTION-tmprj00l.md): leaves open, and sharpens the question. Still's "relevant" variable is already defined relative to action: it is what the work-extraction device can manipulate. The optimum is therefore an action-relevance bottleneck, not a bottleneck on the future of the input. But relevance is computed from the observational p(y|x) (Eq. 4), and the agent's action never changes the next cycle's data (fixed preparation, fixed marginals). So it is neither the interventional partition nor a case with feedback. It is the nearest prior result, as the question says, and a natural first rung for Experiment A: reproduce Eqs. (7)–(9), then let the preparation depend on memory.
- [THEORY-026](../theory.d/THEORY-026.md): extends it, in a different setting. Like [LIT-327](../literature.d/LIT-327.md)'s nostalgia, the bound prices only the part of memory that does not serve the downstream use (I_irrel here, nonpredictive memory there), and both are ensemble averages. The setting differs: a cyclic engine with a work-extraction step and two temperatures, not a system driven through fixed kernels. It adds that the bound-minimising memory is the information bottleneck. It says nothing about feedback, so [THEORY-026](../theory.d/THEORY-026.md)'s feedback clause and [THEORY-817](../theory.d/THEORY-817.md) are untouched.
- [THEORY-1125](../theory.d/THEORY-1125.md) / [THEORY-1146](../theory.d/THEORY-1146.md): leaves open. The bottleneck derived here is the observational IB relative to a manipulable Y. Whether a physical bound would pick the interventional partition under confounding is not addressed.

## Limitations

- Only the arXiv v3 was read, not the PRL text.
- One worked example (a Szilárd box with excluded regions), chosen so that I[X,Y] is easy to compute. No simulation.
- Lower bounds that one protocol saturates. They do not show that real implementations approach them, and the cost of computing the map p(m|x) is not counted.
- No feedback from memory to the system's future statistics, and a single cycle's memory. The costs of revising or maintaining memory, which [QUESTION-tmprj00l](../questions.d/QUESTION-tmprj00l.md) asks about, are not modelled.
