---
number: 268
status: Proposed
formerly:
- THEORY-tmpjvv0j
promote_when: >-
  A result on a system not built to show the effect, with its transition
  structure estimated from data, in which the average emergence score is
  positive and the share of misinformative transitions is reported with
  an interval, for both the coarse-graining and the ΦID measure, together
  with a check that the misinformative moments are not just sampling
  error in the estimated transition matrix. It would also be settled for
  a class of measures by a proof of the conditions under which local
  values must or cannot go negative. What cannot settle it: more
  hand-built toys with negative local values, which show only that the
  arithmetic allows it, or a report of the average score alone.
title: "An emergence measure averaged over a system's transitions can be positive while its local value is negative at particular transitions, so emergence so measured belongs to the ensemble, not to each moment"
version: 1
tags:
- complex-systems
- information-theory
- individuation
date: '2026-10-14'
source:
- LIT-953
summary: >-
  Varley (2022), [LIT-953](../literature.d/LIT-953.md), read in full in [NOTE-756](../notes.d/NOTE-756.md). Both the
  coarse-graining and the ΦID accounts of emergence score an expected
  past–future mutual information, whose pointwise values can be negative.
  In one constructed toy, about 53% of informative micro transitions map
  to misinformative macro ones, and the synergy atom is negative for
  31.25% of transitions, while both averages are positive. The paper
  argues the possibility is general and shows it in instances; it does
  not show that every system flickers, or say what a negative moment
  means.
---
<!-- inactive-ok-file: CLAIM-157 CLAIM-161 THEORY-222 — Proposed; the answer, persistence test and account this bears on, open -->

# THEORY-268: An emergence measure averaged over a system's transitions can be positive while its local value is negative at particular transitions, so emergence so measured belongs to the ensemble, not to each moment

## Source

Varley (2022), [LIT-953](../literature.d/LIT-953.md), *Entropy* 25(1):54, read in full in
[NOTE-756](../notes.d/NOTE-756.md): §2 (local mutual information, the two frameworks), §3
(the toy and the connectome), §4 (interpretation).

## What was actually shown

**The identity.** Local mutual information i(x; y) = log
P(x,y)/(P(x)P(y)) is negative whenever P(x,y) < P(x)P(y), and the mutual
information I(X; Y) is its expectation. Local excess entropy
e(x) = i(x_{t−1}; x_t) is negative when P(x_t | x_{t−1}) < P(x_t). This
part is exact and general.

**The coarse-graining instance (§3.1).** A four-node Boolean network,
coarse-grained by AND over pairs, is emergent on Hoel's measure:
log(F̄(X̃)/F̄(X)) ≈ 0.202. Yet ≈52.73% of informative micro transitions
map to misinformative macro transitions. They are low-probability
transitions, so the average stays positive.

**The ΦID instance (§3.2).** The same toy's macro system has temporal
synergy {X1,X2}→{X1,X2} ≈ 0.031 bit on average, negative for 31.25% of
its sixteen transitions.

**The network instance (§3.1).** On one Human Connectome Project matrix
with Infomap macro-nodes, ≈22.47% of informative micro edges map to
misinformative macro edges, and ≈80.4% of misinformative edges run
between communities.

What could have come out the other way: in the toy, the misinformative
share could have been negligible, and in the connectome the
misinformative edges could have been spread evenly. Neither happened. The
toy was built for illustration, so the first test is weak.

## What this does not say

- **That every emergent system flickers.** The possibility is general to
  measures built as expectations; the occurrence is not. A deterministic,
  invertible dynamics with uniform state probabilities has every realised
  transition at e(x) = log N > 0. The paper gives no conditions under
  which flickering must occur.
- **That the system stops being one system at a misinformative moment.**
  The paper says the system "briefly stops being a 'whole'", but also that
  a negative value may be "merely statistical fluctuations about the
  mean". Whether a negative local value marks a change in the system or a
  rare event under a fixed one is not settled by the statistics.
- **That the two frameworks flicker together.** Each was shown
  separately on the same toy; whether they flicker at the same
  transitions is not reported.
- **That the frameworks are wrong.** The paper disclaims critique: the
  point is that an average score answers a question about the ensemble.

## Connections

- **[QUESTION-035](../questions.d/QUESTION-035.md).** For the "how long does it last" clause: an
  information-theoretic criterion of unity gives a verdict over an
  interval, and at a moment it can give the opposite verdict. An answer
  needs a window and a tolerance, which these measures leave open. No
  `answers:` is declared, since this constrains answers and is not one.
- **[CLAIM-157](../claims.d/CLAIM-157.md).** Its duration clause, "it lasts as long as that block
  persists", is stated over joint dynamics estimated over time, so it
  meets the same question of window. The network instance bears on its
  boundary clause: the macro description fails most often on edges
  between blocks.
- **[CLAIM-161](../claims.d/CLAIM-161.md).** If its coherence measure is informational, "approximately
  conserved" has to absorb negative local values. The paper does not
  discuss persistence; this is the record's application.
- **[THEORY-222](THEORY-222.md).** A complement on the same measure: [THEORY-222](THEORY-222.md) holds that
  the average effective information can be higher at a macro scale, and
  this holds that the macro scale can be the worse description at most of
  the micro transitions it summarises. Neither conflicts with the other.
