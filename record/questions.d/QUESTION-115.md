---
number: 115
status: Open
formerly:
- QUESTION-tmp1bt6j
title: 'Beyond what retention, dynamical independence and Ψ are known to track, can a collective''s boundary, its temporal resolution and its macrostate be found together, by temporal information retention, dynamical independence, effective information and an Occam price on the candidate, and where these criteria disagree on one system, which level does each pick?'
version: 3
history:
- version: 2
  date: '2026-10-20'
  note: >-
    Note of 2026-10-20 added, from the reading of Rosas et al. 2020 (NOTE-987, THEORY-764).
- version: 3
  date: '2026-10-21'
  note: >-
    Split under ADR-049. Whether retention tracks causal propagation,
    whether Ψ and dynamical independence agree, and whether either detects
    interaction or prices size, is QUESTION-tmp3dajs, Answered by
    THEORY-424 and THEORY-764. This question is reworded to what is left:
    the joint search, and where the criteria part on one system. Version
    2's title was 'Can a collective''s boundary, its temporal resolution
    and its macrostate be found together, by temporal information
    retention, dynamical independence, effective information and an Occam
    price on the candidate, and where these criteria disagree, which of
    persistence, integration and causal level does each track?'
tags:
- individuation
- information-theory
date: '2026-10-16'
line: distributed-agency
refines:
- QUESTION-065
- QUESTION-035
summary: >-
  A11–A13 of the exchange of 2026-10-16. Krakauer et al.'s individuality
  measures do not fall when a candidate is enlarged, so maximizing them
  favours swallowing the environment; the paper says a size cost is
  needed. A12 proposed letting information find candidates and the
  record's priced individuation decide, reported as a profile across
  criteria rather than one score. The record already holds the
  interventional critique of those measures ([LIT-005](../literature.d/LIT-005.md)), which the exchange
  did not cite. What retention, Ψ and dynamical independence track is
  QUESTION-tmp3dajs, Answered. An answer here recovers known boundaries
  and timescales in controlled models and reports where the criteria
  part.
refined_by:
- QUESTION-tmp3dajs
---

<!-- inactive-ok-file: CLAIM-331 LIT-1137 — Deferred or Proposed; open claims, readings and works registered unread, cited as open, nothing here rests on their being settled -->
# QUESTION-115: Beyond what retention, dynamical independence and Ψ are known to track, can a collective's boundary, its temporal resolution and its macrostate be found together, by temporal information retention, dynamical independence, effective information and an Occam price on the candidate, and where these criteria disagree on one system, which level does each pick?

## Why it is a question

A12 separated three questions the exchange had run together:
persistence (which variables carry information about their own future),
individuation (which deserve to be one system) and causal level (at which
coarse-graining the causal structure is most effective). Each has a
criterion, and they measure different things:

- **Temporal information retention.** Krakauer et al.'s A* = I(S_{t+1}; S_t),
  A = I(S_{t+1}; S_t | E_t) and nC = I(S_{t+1}; E_t | S_t) ([LIT-1137](../literature.d/LIT-1137.md),
  unread). A11 §5: the two principal measures do not decrease when the
  candidate is enlarged, and the paper "explicitly states that
  determining precise boundaries requires a size cost or regularizer". A11
  proposed lag-dependent versions, A(Δ) = I(S_{t+Δ}; S_t | E_t), as its own
  extension, giving a profile across horizons rather than a score.
- **Interventional retention.** Bourrat's Â = I(S_{t+1}; Ŝ_t) ([LIT-005](../literature.d/LIT-005.md),
  [NOTE-027](../notes.d/NOTE-027.md)), which scores a passively reconstructed entity zero where A*
  does not. The exchange did not cite it. [NOTE-027](../notes.d/NOTE-027.md) found Bourrat's
  equivalence Â ≡ A false in general.
- **Dynamical independence** ([THEORY-257](../theory.d/THEORY-257.md)), closure of a coarse variable
  given its own history.
- **Effective information** ([THEORY-222](../theory.d/THEORY-222.md)), causal informativeness of
  macro-transitions under a declared intervention distribution. A12: a
  macro-intervention needs a meaning ("What does it mean to set 'the
  fandom's level of resentment' to a particular value?"), and A14 §4
  proposed a realization defect: do micro-states with the same macrostate
  respond alike to the same intervention?
- **A priced block** ([CLAIM-157](../claims.d/CLAIM-157.md), [CLAIM-154](../claims.d/CLAIM-154.md)), which supplies the cost the
  information measures lack. A12 §2's version: a candidate must beat the
  decomposed description (independent members), and the expanded one (the
  fandom with the franchise, media and league).

A12 §4: "There isn't yet a justified single scalar objective that combines
all these steps", and "we shouldn't pretend that mutual information,
dynamical closure, and effective information are commensurable merely
because all are measured in bits." It proposed a multidimensional profile
and Pareto comparison. A11 §6 posed the sharpest disagreement: "Can a
collective possess strong historical information continuity while
failing to possess a dynamically independent macrostate?" A fandom that
depends on games, media and league decisions may be one.

[QUESTION-093](QUESTION-093.md) asks the same kind of question about agency. This one asks
it about individuation, with the timescale as a third unknown
([CLAIM-331](../claims.d/CLAIM-331.md)).

## What would count as an answer

A12 §8: "A specified search procedure that recovers independently known
system boundaries and characteristic timescales in controlled models,
while reporting failures, nonunique optima, and sensitivity to its
intervention assumptions." [CASE-101](../cases.d/CASE-101.md) is the controlled model the
exchange proposed. A12's table of separate verdicts is the guard: high
temporal information licenses a predictive relation, integration a
module, effective information a causal coarse-graining, transmission a
lineage, and none of them agency.

## Note of 2026-10-18: macro-interventions, a second appearance

A21 §4 of the exchange of 2026-10-17 came to this question's meaning
problem for macro-interventions from causal emergence ([THEORY-222](../theory.d/THEORY-222.md)), with a
person's commitment as the macrostate: "whether a manipulation of that
macrostate represents an admissible intervention depends on what it means
to change a commitment while holding other aspects of the agent fixed. We
cannot simply impose arbitrary macro-interventions and assume they
correspond to physically meaningful manipulations." It proposed: "**The
explanatory standing of an organizational scale depends not only on what it
compresses, but on which counterfactual interventions and outcomes the
compressed description continues to represent faithfully.**" A21 §6 gave
the condition C_*(P_ℓ^{do(a)}) = P_L^{do(ā)} for a declared family of
interventions. That is A12's question and A14's realization defect again
(do micro-states with one macrostate respond alike?), for a commitment
instead of a fandom's resentment. A21 did not cite this question. Its
judgment-preserving form is [CLAIM-350](../claims.d/CLAIM-350.md), whose causal version is
recorded there as a definition, not a result.

## Note of 2026-10-20: ΦID emergence picks no level without a price

The primary ΦID paper, Rosas et al. 2020, read in [NOTE-987](../notes.d/NOTE-987.md), answers
part of this question for one pair of criteria.

- **Emergence capacity peaks at the microstate.** By its Theorem 1's own
  witness, the emergence score is maximized by the full microstate. So
  ΦID emergence alone selects no coarse level; selecting one needs a price
  such as [CLAIM-154](../claims.d/CLAIM-154.md)'s.
- **Ψ against dynamical independence.** They diverge both ways
  ([THEORY-764](../theory.d/THEORY-764.md)):
  - A self-copying single part is independent and not emergent.
  - A parity whose persistence depends on one bit passes the decoupling
    test and is not independent.
  - The sum of independent identical AR(1) channels is both, with no
    interaction at all.
- **Neither detects interaction.** Neither criterion requires the parts to
  interact.
- **Effective information asks something else again.** Ψ rewards closure
  and penalizes redundancy among the parts. Effective information is
  measured under imposed interventions ([THEORY-222](../theory.d/THEORY-222.md)).

**Split, 2026-10-21 ([ADR-049](../decisions.d/ADR-049.md)).** What three of the criteria track is
[QUESTION-tmp3dajs](QUESTION-tmp3dajs.md), Answered. Retention measures read association, not
propagation ([THEORY-424](../theory.d/THEORY-424.md)). Ψ and dynamical independence diverge both
ways, neither needs the parts to interact, and neither prices a feature's
size ([THEORY-764](../theory.d/THEORY-764.md)). This question keeps the joint search for boundary,
timescale and macrostate with an Occam price, its test on [CASE-101](../cases.d/CASE-101.md), and
where effective information parts from the others on one system.
