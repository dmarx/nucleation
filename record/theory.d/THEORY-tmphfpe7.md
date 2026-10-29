---
status: Active
title: 'When one intervention distribution over micro states is used at both levels, the effective information of a coarse-graining of a discrete mechanism, with each macro intervention realized by that distribution within its block, cannot exceed the micro effective information; so a positive causal emergence of effective information, scored with a uniform distribution at each level, equals the micro gain from changing the distribution minus a non-negative loss, and is a gain from the change of distribution'
version: 1
history:
- version: 1
  date: '2026-10-29'
  note: >-
    Filed Active from the readings of Comolatti and Hoel 2022
    (NOTE-tmpcmbzs) and Eberhardt and Lee 2022 (NOTE-tmp0q96y). The bound
    is the data processing inequality applied to EI's own definition, and
    it is re-derived below. It was checked numerically on 2026-10-29: over
    3,000 random transition matrices of 3 to 6 states, random
    distributions and every partition, the largest macro-minus-micro EI
    under a common distribution was 0 to rounding. The decomposition was
    checked on Eberhardt and Lee's matrices (11), (13) and (14) and the
    paper's bipartite model. Comolatti and Hoel state the special case of
    the stationary distribution ("This was known"); the general statement
    and the decomposition are the record's. This meets ADR-047 v2.
tags:
- causality
- information-theory
- complex-systems
date: '2026-10-29'
source:
- LIT-tmpzfaqi
- LIT-tmpr2bnp
- LIT-1038
summary: >-
  The test QUESTION-204 asks for has an answer that needs no system: with
  one distribution over micro states at both levels, EI(macro) =
  I(f(X); f(Y)) ≤ I(X; Y) = EI(micro) by data processing. Hoel's causal
  emergence uses the uniform distribution at each level, which is a
  non-uniform micro distribution whenever blocks differ in size, so its
  positive values come from the micro chain scored under that other
  distribution. Comolatti and Hoel (LIT-tmpzfaqi) concede the stationary
  case; Eberhardt and Lee (LIT-tmpr2bnp) name the distribution as the
  source of the artefact. It says nothing about measures that data
  processing does not bound, nor about whether EI's level agrees with an
  interventionist test.
extends:
- THEORY-222
bears_on:
- QUESTION-204
---
<!-- inactive-ok-file: THEORY-787 — Proposed; the causal thesis whose "in trouble if" clause this meets for EI, cited as open -->
<!-- inactive-ok-file: QUESTION-204 — Open; the question whose first half this answers, cited as open -->

# THEORY-tmphfpe7: When one intervention distribution over micro states is used at both levels, the effective information of a coarse-graining of a discrete mechanism, with each macro intervention realized by that distribution within its block, cannot exceed the micro effective information; so a positive causal emergence of effective information, scored with a uniform distribution at each level, equals the micro gain from changing the distribution minus a non-negative loss, and is a gain from the change of distribution

## Source

Comolatti and Hoel (arXiv 2022), LIT-tmpzfaqi, read in NOTE-tmpcmbzs:
"the only condition to not show causal emergence was the overall
effective information when using the observational distribution. This
was known [Hoel 2017]". Eberhardt and Lee (2022), LIT-tmpr2bnp, read in
NOTE-tmp0q96y, trace EI's ambiguity and non-commutativity to the
maximum-entropy distribution "extraneous to the system". EI and its
macro interventions are Hoel, Albantakis and Tononi's (2013), LIT-1038,
THEORY-222. The general bound and the decomposition below are the
record's.

## What was actually shown

**Set-up.** A mechanism on a finite state set with transition matrix
T(y | x), read as P(Y = y | do(X = x)). A partition f of the states,
applied to cause and effect. An intervention distribution w over micro
states, fixed in advance. EI under w is I(X; Y) with X ~ w and
Y ~ T(· | X).

**Common distribution.** "The same distribution at both levels" means
that the macro cause U = f(X) has the image law w(f⁻¹(u)), and the
intervention do(U = u) is realized by drawing x from w(· | u). Then the
macro transition matrix is

P(V = v | do(U = u)) = Σ_{x ∈ u} w(x | u) Σ_{y ∈ v} T(y | x),

which is P(f(Y) = v | f(X) = u) under X ~ w. So EI(macro) = I(f(X); f(Y)).

**The bound.** f(X) — X — Y — f(Y) is a Markov chain, so by data
processing I(f(X); f(Y)) ≤ I(X; f(Y)) ≤ I(X; Y). So EI(macro) ≤ EI(micro)
for every partition and every common w. Taking w to be the stationary
distribution gives Comolatti and Hoel's concession. Taking w uniform with
blocks of equal size gives their symmetric bipartite model, where the
macro's 1 bit is below the micro's at every setting computed (1.043 to
3.326 bits; exactly 1 at full degeneracy). A macro can at most tie.

**Where Hoel's gain comes from.** Hoel's macro EI uses the uniform
distribution over macro states, each realized uniformly within its block.
That is the common distribution w_H(x) = 1/(|U| · |block of x|), which is
the micro uniform u only when all blocks have one size. So

CE = EI_macro(w_H) − EI_micro(u) = [EI_macro(w_H) − EI_micro(w_H)] +
[EI_micro(w_H) − EI_micro(u)].

The first bracket is ≤ 0 by the bound. So CE > 0 requires the micro
mechanism to carry more EI under w_H than under the uniform, and CE is
at most that gain. On Eberhardt and Lee's matrices: (11), CE 0.456 =
0 + 0.456; (13), CE 0.194 = −0.150 + 0.344; (14), CE 0.0001 = −0.074 +
0.074 (bits, computed).

What could have come out the other way: a single partition and
distribution with macro EI above micro EI would refute it, and the random
search found none.

## What this does not say

- **Not that macro descriptions are useless or that coarse-graining
  never helps.** Measures not bounded by data processing, such as
  per-transition effect information and quantities normalized by log₂ n,
  can rise at a macro under a common distribution (NOTE-tmpcmbzs). The
  bound is about EI, which is the measure THEORY-787 rests on.
- **Not the second half of QUESTION-204**, whether the level EI picks
  agrees with an independent interventionist test. Eberhardt and Lee's
  (14) is one hand-built case where it does not (NOTE-tmp0q96y).
- **Not Hoel 2013's temporal or spatio-temporal macros**, where the macro
  effect is several micro steps ahead and the micro comparison is with
  one step. The bound covers a coarse-graining of one transition, with
  any partitions of cause and effect. The four examples behind
  THEORY-222's 0.40 to 2.92 bits were not recomputed.
- **Not that the uniform distribution is wrong.** It says what the gain
  is a gain of. Whether an analyst's distribution should differ between
  levels is the interpretive question THEORY-787 takes a side on.
