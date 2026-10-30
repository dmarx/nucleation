---
number: 1169
status: Active
formerly:
- THEORY-tmpyfcov
title: 'For a discrete mechanism scored with one full-support intervention distribution over micro causes at both levels, a coarse-graining of cause and effect keeps all of the micro effective information if and only if it merges only causes with identical rows P(Y | do(x)) and only effects with proportional columns, whatever the distribution; so the coarsest coarse-graining that ties the micro is the causal partition of causal feature learning, with effects grouped by normalized likelihood, and any merge of causes with different effects loses information under every such distribution'
version: 1
history:
- version: 1
  date: '2026-10-29'
  note: >-
    Filed Active from the readings of Chalupka, Perona and Eberhardt 2015
    (LIT-1833, NOTE-1420) and of their 2016 overview
    (LIT-1834, NOTE-1415), for QUESTION-204's second half. The
    definitions are theirs; the equivalence with effective information
    under a common distribution is the record's, derived below by two
    chain-rule identities. Checked numerically on 2026-10-29 by a record
    script: 300 matrices up to 5×5 built with repeated rows and
    proportionally split columns, three random full-support
    distributions each, every pair of partitions of cause and effect,
    245,394 cases; the loss was zero (below 1e-12 bits) in 5,487 of
    them, exactly where the condition predicts, with no exception. At a
    looser tolerance, 1e-9, two cases with a loss of 3e-11 bits from a
    column of mass 0.002 read as ties; they are not. This meets ADR-047
    v2.
tags:
- causality
- information-theory
date: '2026-10-29'
source:
- LIT-1833
- LIT-1834
- LIT-1839
summary: >-
  Causal feature learning ([LIT-1833](../literature.d/LIT-1833.md), [LIT-1834](../literature.d/LIT-1834.md)) defines macro causes as
  classes of micro states with the same interventional effect, with no
  distribution over interventions. Under one full-support distribution
  w at both levels, the loss of effective information from a
  coarse-graining (f, g) is I(X; Y | g(Y)) + I(X; g(Y) | f(X)), and both
  terms vanish exactly when f merges only equal rows and g only
  proportional columns, for every w. So the ties that [THEORY-1167](THEORY-1167.md)
  allows are the causal-feature-learning partitions and their
  refinements: on which coarse-graining loses nothing, EI under a
  common distribution and the interventionist test agree, and the
  agreement is distribution-free. How much a merge loses still depends on
  w. Hoel's EI, uniform at each level, parts from it on Eberhardt and
  Lee's (13), (14) and note 6.
extends:
- THEORY-1167
bears_on:
- QUESTION-204
---
<!-- inactive-ok-file: THEORY-787 — Rejected on 2026-10-30; the causal thesis this bears on, cited as rejected -->
<!-- inactive-ok-file: QUESTION-204 — Open; the question whose second half this bears on, cited as open -->

# THEORY-1169: For a discrete mechanism scored with one full-support intervention distribution over micro causes at both levels, a coarse-graining of cause and effect keeps all of the micro effective information if and only if it merges only causes with identical rows P(Y | do(x)) and only effects with proportional columns, whatever the distribution; so the coarsest coarse-graining that ties the micro is the causal partition of causal feature learning, with effects grouped by normalized likelihood, and any merge of causes with different effects loses information under every such distribution

## Source

Chalupka, Perona and Eberhardt (2015; AISTATS 2016), [LIT-1833](../literature.d/LIT-1833.md), read
in [NOTE-1420](../notes.d/NOTE-1420.md): Definition 2, the fundamental causal partition, i₁ ~
i₂ ⇔ P(j | man(i₁)) = P(j | man(i₂)) for all j, and j₁ ~ j₂ ⇔ P(j₁ |
man(i)) = P(j₂ | man(i)) for all i; "unless we assume a distribution
P(man(I)) over the interventions, we cannot apply the notion of a
sufficient statistic to manipulations in the I space. Following Pearl's
approach, we refrain from specifying intervention distributions" (§2.2).
Their overview, [LIT-1834](../literature.d/LIT-1834.md), read in [NOTE-1415](../notes.d/NOTE-1415.md), §3.3: merging effect
clusters after "Normalizing the likelihood vectors such that they sum to
1". Effective information under a common distribution is
[THEORY-1167](THEORY-1167.md)'s, from Eberhardt and Lee, [LIT-1839](../literature.d/LIT-1839.md), and Hoel et al.,
[LIT-1038](../literature.d/LIT-1038.md). The equivalence below is the record's.

## What was actually shown

**Set-up.** Finite cause states X and effect states Y (they may be one
state set at two times). T(y | x) = P(Y = y | do(X = x)). An intervention
distribution w over X with w(x) > 0 for every x, fixed in advance.
EI_w = I(X; Y) with X ~ w, Y ~ T(· | X). A coarse-graining is a pair of
partitions, f of X and g of Y. As in [THEORY-1167](THEORY-1167.md), the macro cause is
given its image law under w and each do(f(X) = u) is realized by w within
the block, so the macro EI is I(f(X); g(Y)) under the same w.

**The loss splits in two.** Since g(Y) is a function of Y and f(X) of X,

I(X; Y) − I(f(X); g(Y)) = I(X; Y | g(Y)) + I(X; g(Y) | f(X)).

Both terms are non-negative, which is [THEORY-1167](THEORY-1167.md)'s bound again.

**Effect side.** I(X; Y | g(Y)) = 0 iff X is independent of Y given
g(Y), i.e. w(x)T(y | x)/P(y) is the same for every y in a block. With w
of full support, that is: within each block of g, the columns T(y | ·)
are proportional, T(y | x) = κ_{y,y′} T(y′ | x) for all x. The condition
does not mention w, so it holds for one full-support w iff it holds for
all. (A state no cause reaches has a zero column and may go in any
block.)

**Cause side.** I(X; g(Y) | f(X)) = 0 iff, within each block of f, the
rows P(g(Y) | x) are equal. When the effect side holds, T(y | x) =
c_y · P(g(Y) = g(y) | x) with c_y independent of x, so equal macro rows
mean equal micro rows. Hence the whole loss is zero iff f merges only
causes with identical rows of T and g merges only effects with
proportional columns, whatever full-support w is used.

**The coarsest tie.** The coarsest f is the partition of X by T(· | x):
Chalupka et al.'s fundamental cause. The coarsest g is the partition of Y
by normalized columns. It equals their fundamental effect (equal columns)
unless two effect states have proportional, unequal columns, in which
case it is coarser and still loses nothing ([NOTE-1420](../notes.d/NOTE-1420.md) records the
example rows (0.2, 0.4, 0.4) and (0.1, 0.2, 0.7), whose first two
effects merge with zero loss under every w checked). Every merge of two
causes with different effects, an ambiguous manipulation in Spirtes and
Scheines's sense, loses information under every full-support w.

**On Eberhardt and Lee's matrices** (computed, [NOTE-1413](../notes.d/NOTE-1413.md)). (11): rows
1–7 are identical, so the causal partition is {1–7}, {8}, the same as
EI's choice. (13): all eight rows differ, so the causal partition is the
micro, and EI's {1–7}, {8} is a lossy merge. (14) and its variant: all
rows differ; EI merges x₁ and x₂ at a loss of 0.074 bits under w_H.
Note 6: rows x₂ and x₃ are identical, so the causal partition merges
them, which EI does not do, because Hoel coarsens cause and effect by one
partition and the columns of y₂ and y₃ are not proportional. (17): no
lossless merge.

What could have come out the other way: a coarse-graining with zero loss
that merges two different rows, or two non-proportional reachable
columns, under some full-support w. The search found none, and the
identities exclude it.

## What this does not say

- **Not that the macro is where causation is.** The micro always ties.
  The causal partition is the coarsest description that loses nothing,
  a proportionality notion in Yablo's sense, not a level with more
  causation. [THEORY-787](THEORY-787.md)'s claim that the macro is causally privileged
  gets no support from it.
- **Not a ranking of lossy coarse-grainings.** Whether a loss is zero
  does not depend on w; its size, w-weighted divergence among the merged
  rows, does. Any trade of loss against size, Hoel's included, brings a
  distribution back.
- **Not for approximate equality.** With noisy or estimated rows, no two
  are equal and only the micro ties. Chalupka et al.'s algorithms merge
  by a threshold, KL or earth mover's distance, which is a choice the
  theory does not make.
- **Not for Hoel 2013's temporal macros**, continuous variables, or
  partitions forced to be the same on cause and effect. When f must equal
  g, the coarsest tie is the coarsest partition meeting both conditions
  at once, which can be the micro when f alone could merge (note 6).
- **Not about confounding.** T is interventional. Getting the causal
  partition from observational data needs Chalupka et al.'s coarsening
  theorem, a genericity result.
- The cause side alone, for a different information measure (causal
  information gain under a protocol), is [THEORY-1125](THEORY-1125.md)'s.
