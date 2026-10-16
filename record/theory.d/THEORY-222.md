---
number: 222
status: Proposed
formerly:
- THEORY-tmpuumxo
promote_when: >-
  A test of whether the macro advantage depends on the uniform
  intervention distribution that LIT-1038 imposes separately at each
  level. The account is promoted by a result showing that, on systems not
  built to display emergence, the EI-optimal coarse-graining stays the
  same, or stays macro, when the interventions follow the system's own
  stationary distribution or another distribution fixed in advance, and
  that it agrees with an independent interventionist test of which level
  the effects track (realization insensitivity under changes of
  realizer). It is in trouble if the macro advantage disappears whenever
  the same intervention distribution over micro states is used at both
  levels, since then the gain measures the change of distribution, not a
  property of the system. What cannot settle it: more hand-built toy
  systems with positive CE, which show only that the arithmetic works;
  or applications that estimate a TPM and report the best of many
  coarse-grainings with no correction for the search.
title: 'A coarse-grained macro description can carry more effective information than the micro description it supervenes on, so the scale at which a system''s causal structure is most effective can be a macro scale'
version: 2
history:
- version: 2
  date: '2026-10-16'
  note: >-
    Connections: the ΦID account is now filed (THEORY-497), so the
    line saying the record holds none is replaced. No rivalry is declared,
    since whether the two disagree depends on the redundancy function.
tags:
- causality
- complex-systems
- information-theory
date: '2026-10-13'
source:
- LIT-1038
summary: >-
  Hoel, Albantakis & Tononi (2013), [LIT-1038](../literature.d/LIT-1038.md), read in [NOTE-726](../notes.d/NOTE-726.md).
  Effective information is effectiveness (determinism minus degeneracy)
  times the log of the state-space size, measured under uniform
  interventions. Coarse-graining always loses size and can gain
  effectiveness; when the gain wins, causal emergence CE = EI(macro) −
  EI(micro) is positive. Four toy systems give 0.40 to 2.92 bits. The
  arithmetic is exact. The reading that the EI peak marks where causation
  happens rests on imposing a uniform distribution at each level, which
  the paper adopts and does not test, so the account is Proposed.
answers:
- QUESTION-093
---
<!-- inactive-ok-file: THEORY-497 — Proposed; the ΦID account named for comparison, nothing here rests on its being settled -->
<!-- inactive-ok-file: THEORY-133 THEORY-071 — Proposed; compared, nothing here rests on them -->

# THEORY-222: A coarse-grained macro description can carry more effective information than the micro description it supervenes on, so the scale at which a system's causal structure is most effective can be a macro scale

## Source

Hoel, Albantakis & Tononi (2013), [LIT-1038](../literature.d/LIT-1038.md), read in [NOTE-726](../notes.d/NOTE-726.md):
Theory (definitions, the decomposition CE = ΔI_Eff + ΔI_Size), Results
(four examples), Discussion (intrinsicness, exclusion, rules of thumb).

## What was actually shown

A system of binary logic gates with a known transition matrix is set into
each of its states with equal probability, and the effective information
(EI) of its next state is computed. EI equals effectiveness, Eff, times
log₂ of the number of states, and Eff is the average determinism minus the
average degeneracy. A macro description groups micro elements, micro time
steps or both, under mappings that hide which micro element is in which
state. The macro is then scored the same way, with each macro state set by
setting its micro realizers with equal probability.

The size term is always a loss for the macro. The effectiveness term can be
a gain, because grouping averages out noise and merges states that
deterministically lead to the same place. In four constructed systems the
gain wins: 0.40 bits (noise), 0.57 bits (degeneracy), 0.62 bits (time) and
2.92 bits (space and time). The paper also proves rules of thumb: if the
micro is already at least as effective as the macro, no macro can win.

What could have come out the other way: the decomposition shows exactly
when the macro can win, and the rules show that systems already near
maximal effectiveness cannot display emergence at all. The examples were
chosen to display it.

## What this does not say

- **It does not show that the macro is where causation happens, as
  opposed to where EI is highest.** The paper calls the EI-optimal level
  "intrinsic" and says the macro then excludes the micro. Both depend on
  imposing a uniform distribution over states separately at each level,
  which weights the micro states differently at the two levels. The
  authors note that this is what allows the macro to win and present it as
  fairness. It is a choice, and the paper does not test another.
- **It does not measure any real system.** The search over
  coarse-grainings is exhaustive and, by the authors' account, infeasible
  beyond toy sizes. The claims about brains and about the hierarchy of the
  sciences are conjecture.
- **It does not individuate anything.** The coarse-graining is chosen by
  an analyst's search. The paper's "self-definition" at the optimal level
  means the EI maximum, not a boundary the system draws.
- **It is not a model-selection rule from data.** The mechanism is known
  exactly. There is no sample, prior or posterior, so no question of
  evidence or of how far the search inflates the winning score.

## Connections

- **[QUESTION-093](../questions.d/QUESTION-093.md) (which criteria a higher-level agent needs).** This
  is a measure of interventional autonomy: whether macro variables support
  more informative predictions of the effects of interventions. It also
  claims predictive autonomy, but only for predictions from imposed
  states. None of the paper's systems maintains itself, and the grouping
  is an analyst's, so positive CE needs neither organisational closure nor
  self-individuation. That answers half the question: the first criteria
  can be had without the last two. It says nothing on whether closure or
  self-individuation can be had without them, or on whether any of them
  makes an agent.
- **[CLAIM-154](../claims.d/CLAIM-154.md) (the reification rule).** The same shape of trade-off, a gain
  against a size cost that is always paid, for a different question.
  [CLAIM-154](../claims.d/CLAIM-154.md) asks whether data justify keeping a structure; CE asks which
  description of a known mechanism is the more effective causal model.
  Neither implies the other, and a coarse block could pass one and fail
  the other. No `supports` is declared: [CLAIM-154](../claims.d/CLAIM-154.md) rests on the Bayes-factor
  identity, not on this. [QUESTION-040](../questions.d/QUESTION-040.md)'s worry about search applies to any
  application of CE with an estimated mechanism, and the paper does not
  address it.
- **[THEORY-133](THEORY-133.md) (proportional causation).** A complement. List & Menzies
  reach downward exclusion when an effect would survive a change of
  realizer; Hoel et al. reach it when averaging over realizers raises EI.
  Degeneracy reduction is realization insensitivity in information terms.
  Both make the answer system by system. The record's promote_when for
  [THEORY-133](THEORY-133.md) asks for evidence of realization insensitivity in a
  particular system, and CE is one way to measure it, but only under this
  account's choice of intervention distribution. No relation is declared,
  since neither depends on the other and they do not conflict.
- **[LIT-025](../literature.d/LIT-025.md) and [LIT-027](../literature.d/LIT-027.md) (information-decomposition emergence).** A
  different formal object under the same name: interventional and
  comparing two models here, observational and asking what a macro feature
  predicts beyond the parts there. The ΦID account is [THEORY-497](THEORY-497.md).
  Its reading ([NOTE-010](../notes.d/NOTE-010.md)) gives a two-bit permutation with no EI gain at
  any macroscale that hosts an emergent feature under the minimum-MI
  redundancy and none under one with the identity property, so whether
  the two disagree turns on the redundancy function, and no rivalry is
  declared. Whether they pick the same level on a shared system is
  untested in the record.
- **[THEORY-071](THEORY-071.md) (minimal agency).** Its individuality condition, a
  boundary the system makes for itself, is exactly what CE does not
  supply.
