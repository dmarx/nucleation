---
status: Answered
title: 'Does temporal information retention track causal propagation, do the ΦID criterion Ψ and dynamical independence agree, and does either of those two detect interaction among the parts or price the size of a feature?'
version: 1
tags:
- individuation
- information-theory
date: '2026-10-21'
line: distributed-agency
refines:
- QUESTION-115
summary: >-
  The part of [QUESTION-115](QUESTION-115.md) on what three of its criteria track, split off
  under [ADR-049](../decisions.d/ADR-049.md). No to all four. Retention measures read association, not
  propagation ([THEORY-424](../theory.d/THEORY-424.md)). Ψ and dynamical independence diverge both
  ways, neither needs the parts to interact, and neither prices a
  feature's size ([THEORY-764](../theory.d/THEORY-764.md)). The joint search for boundary, timescale
  and macrostate, and its test on [CASE-101](../cases.d/CASE-101.md), stay with [QUESTION-115](QUESTION-115.md).
answered_by:
- THEORY-424
- THEORY-764
---

# QUESTION-tmp3dajs: Does temporal information retention track causal propagation, do the ΦID criterion Ψ and dynamical independence agree, and does either of those two detect interaction among the parts or price the size of a feature?

## Answer

No to each. This is the part of [QUESTION-115](QUESTION-115.md) that asks where its criteria
disagree and what each tracks, split off on 2026-10-21 ([ADR-049](../decisions.d/ADR-049.md)).

- **Retention is association.** [THEORY-424](../theory.d/THEORY-424.md) (Active), from Bourrat (2024),
  read in [NOTE-027](../notes.d/NOTE-027.md). Krakauer et al.'s A* = I(S_{t+1}; S_t) can be positive
  when the environment alone drives the system. Conditioning on the
  environment does not give the interventional quantity: in [NOTE-027](../notes.d/NOTE-027.md)'s XOR
  system A = 1 bit and Â = 0. Retention tracks predictive dependence, not
  causal propagation.
- **Ψ and dynamical independence diverge both ways.** [THEORY-764](../theory.d/THEORY-764.md) (Active),
  the record's derivation from Rosas et al. (2020) and Barnett and Seth.
  For a deterministic feature of a Markov system, Ψ is the parts'
  whole-minus-sum information about the feature's next value minus its
  one-step dynamical dependence. A self-copying single part is
  independent and not emergent. A parity whose persistence depends on one
  bit passes Ψ's decoupling test and is not independent.
- **Neither detects interaction.** The sum of independent identical AR(1)
  channels is both emergent by Ψ and independent, with no interaction at
  all.
- **Neither prices size.** Neither Ψ nor the dependence term charges for
  the size of the feature, and the whole-minus-sum term can grow with the
  number of parts summed.

So independence tracks closure, and Ψ tracks closure plus collective,
non-redundant predictability. Retention tracks persistence. None of the
three tracks integration.

## What it leaves to [QUESTION-115](QUESTION-115.md)

Whether boundary, timescale and macrostate can be found together, by a
specified search with an Occam price, that recovers known boundaries in
controlled models such as [CASE-101](../cases.d/CASE-101.md). Where effective information parts from
the others on one shared system is untested. That ΦID emergence is
maximized by the microstate rests on [NOTE-987](../notes.d/NOTE-987.md)'s reading of the paper's
Theorem 1, which concerns the PID quantities, not Ψ, and [THEORY-764](../theory.d/THEORY-764.md) does
not cover it.
