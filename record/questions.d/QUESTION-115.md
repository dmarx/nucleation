---
number: 115
status: Open
formerly:
- QUESTION-tmp1bt6j
title: 'Beyond what retention, dynamical independence and Ψ are known to track, can a collective''s boundary, its temporal resolution and its macrostate be found together, by temporal information retention, dynamical independence, effective information and an Occam price on the candidate, and where these criteria disagree on one system, which level does each pick?'
version: 7
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
    interaction or prices size, is QUESTION-243, Answered by
    THEORY-424 and THEORY-764. This question is reworded to what is left:
    the joint search, and where the criteria part on one system. Version
    2's title was 'Can a collective''s boundary, its temporal resolution
    and its macrostate be found together, by temporal information
    retention, dynamical independence, effective information and an Occam
    price on the candidate, and where these criteria disagree, which of
    persistence, integration and causal level does each track?'
- version: 4
  date: '2026-10-21'
  note: >-
    Note of 2026-10-21 added, from the exchange of 2026-10-20 on effective
    description, agency and legibility: the owner's leave-one-out
    (QUESTION-252) asks of five conditions on an effective description
    what this question asks of each criterion. The question is unchanged.
- version: 5
  date: '2026-10-29'
  note: >-
    Note of 2026-10-29 added, from the readings of Krakauer et al.
    2020 (NOTE-1400, THEORY-1163), Jansma and Hoel, CE 2.0,
    Zhang et al. and Shalizi and Crutchfield. The question is
    unchanged.
- version: 6
  date: '2026-10-29'
  note: >-
    Note of 2026-10-29 added: Eberhardt and Lee read
    (NOTE-tmp0q96y); EI's family of interventions passes
    coarse-grainings that fail A21's admissibility condition. The
    question is unchanged.
- version: 7
  date: '2026-10-29'
  note: >-
    Note of 2026-10-29 added: causal feature learning read
    (NOTE-tmpiw2bv, NOTE-tmpbrnim), a further macrostate
    criterion; it parts from EI on Eberhardt and Lee's (14) and
    note 6, and agrees with EI under a common distribution
    (THEORY-tmpyfcov). The question is unchanged.
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
  QUESTION-243, Answered. An answer here recovers known boundaries
  and timescales in controlled models and reports where the criteria
  part.
refined_by:
- QUESTION-243
---
<!-- inactive-ok-file: CLAIM-401 — Proposed; cited in the note of 2026-10-21, nothing here rests on it -->

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
[QUESTION-243](QUESTION-243.md), Answered. Retention measures read association, not
propagation ([THEORY-424](../theory.d/THEORY-424.md)). Ψ and dynamical independence diverge both
ways, neither needs the parts to interact, and neither prices a feature's
size ([THEORY-764](../theory.d/THEORY-764.md)). This question keeps the joint search for boundary,
timescale and macrostate with an Occam price, its test on [CASE-101](../cases.d/CASE-101.md), and
where effective information parts from the others on one system.

## Note of 2026-10-21: the leave-one-out over the criteria

The owner's leave-one-out design of 2026-10-20 (U3, filed as
[QUESTION-252](QUESTION-252.md)) asks systematically, of five conditions on an
effective description (predictive sufficiency, dynamical independence,
memory closure, approximation fidelity, feasible recoverability), whether
each can hold without the others. That is this question's "what each
criterion tracks", asked as a table. The exchange did not cite this
question. [CLAIM-401](../claims.d/CLAIM-401.md)'s answer to the design is that the conditions are
not of one logical kind, so the table's cells are not all of one sort
either.

## Note of 2026-10-29: Krakauer et al. and the three search candidates, read

[LIT-1137](../literature.d/LIT-1137.md) is now read ([NOTE-1400](../notes.d/NOTE-1400.md)), so the body's "unread" no longer
holds. A11's report is confirmed for the 2020 article: A* and A cannot
decrease as variables move from the environment into the candidate, and
the article says a boundary needs a size cost. The 2014 preprint makes the
same monotonicity claim but offers a stopping rule instead of a size cost.
The check is [THEORY-1163](../theory.d/THEORY-1163.md).

The works filed as A10's paper "on searching for coarse-grainings rather
than assuming them" are read too, and each fits only in part.

- Jansma and Hoel, [LIT-1123](../literature.d/LIT-1123.md) ([NOTE-1359](../notes.d/NOTE-1359.md)), does search: it scores
  every partition and reports a set of scales. It prices nothing, with
  no Occam term, and its profile is across scales under one criterion,
  not across criteria.
- Hoel's CE 2.0, [LIT-1136](../literature.d/LIT-1136.md) ([NOTE-1387](../notes.d/NOTE-1387.md)), searches along one path chosen
  by maximum gain, and calls the full search future work.
- Zhang et al., [LIT-1129](../literature.d/LIT-1129.md) ([NOTE-1399](../notes.d/NOTE-1399.md)), avoids the search: it reads the
  singular-value spectrum and recovers a partition afterwards by k-means.

All three search partitions of one system's states, not which variables
are in the system. They bear on the macrostate leg of this question and
not on the boundary leg.

Shalizi and Crutchfield, [LIT-1126](../literature.d/LIT-1126.md) ([NOTE-1372](../notes.d/NOTE-1372.md)), adds one distinction:
E ≤ Cµ separates what can be measured from sequences from the memory
needed to produce them, as this question separates retention measured on
observables from a system's state.

The question is unchanged and stays Open.

## Note of 2026-10-29: effective information against A21's admissibility condition

A21's condition, in the note of 2026-10-18, C_*(P_ℓ^{do(a)}) = P_L^{do(ā)}
for a declared family of interventions, puts Eberhardt and Lee's demands
of commutativity and unambiguous manipulation in one line. Their paper,
[LIT-tmpr2bnp](../literature.d/LIT-tmpr2bnp.md), is now read ([NOTE-tmp0q96y](../notes.d/NOTE-tmp0q96y.md)). It shows that EI's family,
uniform averages over realizers, passes coarse-grainings that fail both.
In their (14), EI merges two states whose effects on the macro effect
variable differ (0.8/0.2 against 0.9/0.1). In their (17), the partition is
strongly lumpable, so the coarse-graining does commute with time
evolution, and the EI-optimal choice still changes with the time step. It
is the same shape of answer the note of 2026-10-20 gave for ΦID emergence:
the criterion alone does not license the level it picks.

On where effective information parts from the other criteria: under one
distribution over micro states at both levels, EI cannot favour a macro at
all ([THEORY-tmphfpe7](../theory.d/THEORY-tmphfpe7.md)). Its macro advantage is a property of the
distribution chosen at each level.

The question is unchanged and stays Open.

## Note of 2026-10-29: causal feature learning, a further macrostate criterion

Causal feature learning, LIT-tmplfiq6 (NOTE-tmpiw2bv) and LIT-tmpmefe6
(NOTE-tmpbrnim), is a further candidate for the macrostate leg, and it
parts from effective information on one system. It partitions causes by
P(Y | do(x)) and effects by their columns, two partitions where Hoel's EI
coarsens cause and effect by one. On Eberhardt and Lee's (14), EI picks
{x₁, x₂}, {x₃} and causal feature learning the micro. On their note 6,
causal feature learning merges x₂ and x₃, whose rows are identical, and
EI's shared partition cannot. Under one distribution at both levels the
two agree on which coarse-grainings lose nothing (THEORY-tmpyfcov), so the
disagreement belongs to the uniform distribution at each level, as the
earlier note of this date found for EI's macro advantage.

Like the other macrostate candidates, it partitions one system's states,
not which variables are in the system. It has no Occam term: it takes the
coarsest partition that loses nothing and offers no trade of loss against
size.

The question is unchanged and stays Open.
