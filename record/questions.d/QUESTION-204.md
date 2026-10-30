---
number: 204
status: Open
formerly:
- QUESTION-tmp3zal3
title: "Does a macro description's effective-information advantage survive when the same intervention distribution over micro states is used at both levels, and does the EI-optimal level agree with an independent interventionist test of which level the effects track?"
version: 4
history:
- version: 2
  date: '2026-10-29'
  note: >-
    Note of 2026-10-29 added: the first half is answered, no, by
    THEORY-1167: under one distribution over micro states at
    both levels, macro EI cannot exceed micro EI, by data
    processing. The second half is open, and the question stays
    Open.
- version: 3
  date: '2026-10-29'
  note: >-
    Note of 2026-10-29 added: the second half has its test, causal
    feature learning (NOTE-1420, NOTE-1415), and a partial
    answer, THEORY-1169: EI under one common distribution ties
    the micro exactly at its partitions and their refinements;
    Hoel's EI, uniform at each level, parts from it on Eberhardt
    and Lee's (13), (14) and note 6. The question stays Open.
- version: 4
  date: '2026-10-30'
  note: >-
    Note of 2026-10-30 added: THEORY-787 is Rejected, and the record's own
    answer is CLAIM-tmpxk5cy by ARG-tmp2wo7e; the temporal macros are split
    off as QUESTION-tmpzfd02. Status unchanged.
tags:
- causality
- information-theory
date: '2026-10-20'
line: 'distributed-agency'
refines:
- QUESTION-093
summary: >-
  The promotion condition formerly on [THEORY-222](../theory.d/THEORY-222.md). [THEORY-222](../theory.d/THEORY-222.md) was narrowed
  and promoted on 2026-10-20 ([ADR-047](../decisions.d/ADR-047.md) v2) to the statement about
  effective information that holds by construction. With uniform
  interventions imposed separately at each level, a macro description can
  have higher EI than the micro one. Whether that gain survives a single
  intervention distribution, and whether the EI peak marks where
  causation happens, is open.
answered_by:
- THEORY-787
---
<!-- inactive-ok-file: THEORY-787 — Rejected on 2026-10-30; the causal thesis this question was filed to test, cited as such -->
<!-- inactive-ok-file: CLAIM-tmpxk5cy ARG-tmp2wo7e QUESTION-tmpzfd02 — Proposed or Open; the record's own answer, its argument and the case split off, cited in the note of 2026-10-30 -->

# QUESTION-204: Does a macro description's effective-information advantage survive when the same intervention distribution over micro states is used at both levels, and does the EI-optimal level agree with an independent interventionist test of which level the effects track?

## Why it is a question

[THEORY-222](../theory.d/THEORY-222.md) holds the arithmetic of Hoel, Albantakis and Tononi (2013).
Effective information is measured with a uniform distribution imposed
over the states at each level, and under that choice a coarse-graining
can gain more effectiveness than it loses in size. The choice weights the
micro states differently at the two levels. The authors note that this
is what lets the macro win, and present it as fairness. If the gain
disappears when one distribution over micro states is used at both
levels, it measures the change of distribution, not a property of the
system. Until 2026-10-20 this was [THEORY-222](../theory.d/THEORY-222.md)'s promote_when.

## What would answer it

- A result on systems not built to display emergence, showing that the
  EI-optimal coarse-graining stays the same, or stays macro, when the
  interventions follow the system's own stationary distribution or
  another distribution fixed in advance.
- An agreement between the EI-optimal level and an independent
  interventionist test of which level the effects track, such as
  realization insensitivity under changes of realizer.

What cannot settle it: more hand-built toy systems with positive causal
emergence, which show only that the arithmetic works; or applications
that estimate a transition matrix and report the best of many
coarse-grainings with no correction for the search.

## Note of 2026-10-29: the first half answered, by derivation

The first half of this question is answered, and the answer is no.
[THEORY-1167](../theory.d/THEORY-1167.md) (Active) shows that the test needs no system. With one
distribution over micro states at both levels, each macro intervention
realized by that distribution within its block, the macro EI is I(f(X);
f(Y)) ≤ I(X; Y), the micro EI, by data processing. A macro can at most
tie, on any system and under any distribution fixed in advance, the
stationary one included. Hoel's positive causal emergence is the micro
mechanism's gain from changing the distribution, less a non-negative loss.
On Eberhardt and Lee's matrices (11), (13) and (14) the decomposition is
0.456 = 0 + 0.456, 0.194 = −0.150 + 0.344 and 0.0001 = −0.074 + 0.074
bits. Comolatti and Hoel, [LIT-1843](../literature.d/LIT-1843.md) ([NOTE-1416](../notes.d/NOTE-1416.md)), concede the
stationary case ("This was known"). Eberhardt and Lee, [LIT-1839](../literature.d/LIT-1839.md)
([NOTE-1413](../notes.d/NOTE-1413.md)), name the maximum-entropy distribution as the source of
the artefact, but do not themselves compute EI under a common one.

The second half, whether the EI-optimal level agrees with an independent
interventionist test, is open. Eberhardt and Lee's (14) is one small case
where the two part. A test of realization insensitivity would keep x₁ and
x₂ apart, since their effects on the macro effect variable differ (0.8/0.2
against 0.9/0.1), and EI merges them. It is a hand-built 3×3 matrix, which
by this question's own terms cannot settle agreement in general.

The bound is for EI. Measures that data processing does not bound,
per-transition ones or ones normalized by log₂ n, can rise at a macro
under a common distribution; they are not what this question asks about.
[THEORY-787](../theory.d/THEORY-787.md) is noted the same day. The question stays Open.

## Note of 2026-10-29: the second half has its test, and a partial answer

The earlier note of this date left the second half open. It now has the
independent interventionist test it asks for, and part of an answer.

The test is causal feature learning: Chalupka, Perona and Eberhardt,
[LIT-1833](../literature.d/LIT-1833.md) ([NOTE-1420](../notes.d/NOTE-1420.md)), and their overview, [LIT-1834](../literature.d/LIT-1834.md)
([NOTE-1415](../notes.d/NOTE-1415.md)). Its causal partition puts two micro causes in one macro
state iff manipulating to either has the same effect, P(Y | do(x₁)) =
P(Y | do(x₂)), and partitions effects likewise. That is realization
insensitivity under changes of realizer, stated exactly, and it is
independent of EI-type choices: the authors put no distribution on
interventions, and the partition is defined from point manipulations
alone.

The partial answer is [THEORY-1169](../theory.d/THEORY-1169.md) (Active). Under one full-support
distribution over micro causes at both levels, a coarse-graining keeps all
of the micro EI iff it merges only causes with identical rows P(Y | do(x))
and only effects with proportional columns, whatever the distribution. So
the coarse-grainings at which EI under a common distribution ties the
micro are exactly the causal-feature-learning partitions, with effects
grouped by normalized likelihood, and their refinements. On which
coarse-grainings lose nothing, the two agree. The agreement is derived,
and checked numerically on 245,394 cases, not read off a toy.

Two limits keep the question Open.

- Hoel's EI, uniform at each level, whose optimum is the one the question
  names, does not agree. On Eberhardt and Lee's (11) the two pick the same
  macro, since rows 1–7 are identical. On their (13) and (14), EI merges
  causes whose rows differ, which the causal partition keeps apart; on
  their note 6, EI keeps apart x₂ and x₃, whose rows are identical,
  because it coarsens cause and effect by one partition. These are
  hand-built matrices, which by this question's terms cannot settle
  agreement in general, and Hoel 2013's own examples ([THEORY-222](../theory.d/THEORY-222.md)) were not
  recomputed.
- Under a common distribution the micro always ties, so the EI-optimal
  level is at best the coarsest tie. That is the causal partition: the
  proportionate description, not one with more causation. And the
  agreement needs exact equality of rows. With estimated rows only the
  micro ties, and causal feature learning merges by a distance threshold,
  a choice [THEORY-1169](../theory.d/THEORY-1169.md) does not make.

The question is unchanged and stays Open.

## Note of 2026-10-30: [THEORY-787](../theory.d/THEORY-787.md) rejected, and the record's own answer

[THEORY-787](../theory.d/THEORY-787.md), the account this question was asked of, is Rejected on
2026-10-30 at the owner's direction, by its own refutation condition: the
first half of this question is answered no ([THEORY-1167](../theory.d/THEORY-1167.md)). The record now
answers in its own voice. [CLAIM-tmpxk5cy](../claims.d/CLAIM-tmpxk5cy.md) (Proposed, interpretive) holds
that a system's causes are found at the coarsest description whose
interventions are unambiguous. [ARG-tmp2wo7e](../arguments.d/ARG-tmp2wo7e.md) sets out the inference from
[THEORY-1167](../theory.d/THEORY-1167.md) and [THEORY-1169](../theory.d/THEORY-1169.md) to it. On the second half, that claim takes
the common-distribution ties and causal feature learning's partitions to
be the same level, which [THEORY-1169](../theory.d/THEORY-1169.md) shows. It takes Hoel's
uniform-per-level EI to fail the test, which Eberhardt and Lee's (13) and
(14) show.

The temporal and spatio-temporal macros of [LIT-1038](../literature.d/LIT-1038.md), which [THEORY-1167](../theory.d/THEORY-1167.md)
does not reach, are split off as [QUESTION-tmpzfd02](QUESTION-tmpzfd02.md). What stays open here
is whether a graded criterion can rank lossy coarse-grainings without
bringing a distribution back. Whether that remainder leaves this question
Open, or makes it Answered with that part split off, is left to the
status review. The status is unchanged.
