---
number: 222
status: Active
formerly:
- THEORY-tmpuumxo
title: 'With uniform interventions imposed separately at each level, a coarse-grained macro description of a known discrete mechanism can have more effective information than the micro description it supervenes on, so the level at which effective information is highest can be a macro level'
version: 3
history:
- version: 2
  date: '2026-10-16'
  note: >-
    Connections: the ΦID account is now filed (THEORY-497), so the
    line saying the record holds none is replaced. No rivalry is declared,
    since whether the two disagree depends on the redundancy function.
- version: 3
  date: '2026-10-20'
  note: >-
    Narrowed and promoted, carrying out the promotion audit's decision for
    THEORY-222 (batch 049, ADR-047 v2). The dated note below gives a
    four-state construction. The title now names the measure and the
    intervention distribution; "the scale at which a system's causal
    structure is most effective" becomes "the level at which effective
    information is highest". The promote_when, which asks whether the gain
    survives one distribution at both levels, moves to QUESTION-204.
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
  the paper adopts and does not test; the title does not claim it.
  Promoted on 2026-10-20 on a construction. Whether the gain survives one
  intervention distribution at both levels is QUESTION-204.
answers:
- QUESTION-093
---
<!-- inactive-ok-file: THEORY-497 — Proposed; the ΦID account named for comparison, nothing here rests on its being settled -->
<!-- inactive-ok-file: THEORY-133 THEORY-071 — Proposed; compared, nothing here rests on them -->

# THEORY-222: With uniform interventions imposed separately at each level, a coarse-grained macro description of a known discrete mechanism can have more effective information than the micro description it supervenes on, so the level at which effective information is highest can be a macro level

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

## Note of 2026-10-20: a four-state construction

For the promotion audit (batch 049, [ADR-047](../decisions.d/ADR-047.md) v2). Take micro states a, b,
c and d. Each of a, b and c moves to one of a, b, c uniformly at random,
and d moves to itself. With interventions uniform over the four states,
P(Y = a) = P(Y = b) = P(Y = c) = (3/4)(1/3) = 1/4 and P(Y = d) = 1/4, so
H(Y) = 2 bits and H(Y | X) = (3/4) log₂ 3 ≈ 1.189 bits, and EI ≈ 0.811
bits. Group A = {a, b, c} and B = {d}. A moves to A and B to B, so with
interventions uniform over the two macro states EI = 1 bit. The macro
gains about 0.189 bits, and the level with the highest EI is the macro
one. The construction depends on the uniform distribution being imposed
again at the macro level, which weights d at 1/2 instead of 1/4.
