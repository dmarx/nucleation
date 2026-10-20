---
status: Proposed
promote_when: >-
  A result in which the data-limited exponent of a next-token learner is
  moved by changing one of the two corpus statistics while the other is
  held: for instance, text whose correlations beyond some lag are
  destroyed or weakened by an intervention that keeps its short-range
  statistics, or a synthetic language with tunable β and γ, with the
  measured exponent tracking γ/(2β) and departing from it when the within-
  horizon excess loss is made to decay slowly. Or the same match at a
  scale where the usable horizon reaches thousands of tokens, with γ
  estimated without a neural model of the same class. More collapses at
  the scale already reported, with γ read off the trained models' own
  n-gram losses, cannot settle it.
title: 'Language models trained on limited data show a test loss falling as P^(−γ/(2β)) because P training tokens resolve token correlations only out to a horizon growing as P^(1/(2β)), so that more data mainly lengthens the context a model can use, when the model learns within that horizon faster than it grows, as Cagnetta, Raventós, Ganguli and Wyart propose'
version: 1
tags:
- learning-theory
- linguistics
- information-theory
date: '2026-10-20'
source:
- LIT-888
- LIT-883
summary: >-
  Cagnetta, Raventós, Ganguli and Wyart (2026), [LIT-888](../literature.d/LIT-888.md), read in [NOTE-689](../notes.d/NOTE-689.md),
  building on Cagnetta and Wyart's effective context window ([LIT-883](../literature.d/LIT-883.md)). The
  paper presents the horizon as the reason the data-limited exponent is
  γ/(2β). [THEORY-204](THEORY-204.md) holds what it showed: the derivation under assumed
  scaling forms, and the measured overlap on TinyStories and WikiText-103
  up to about 10^8 tokens. Whether the horizon is why is the test
  [QUESTION-233](../questions.d/QUESTION-233.md) asks.
extends:
- THEORY-204
answers:
- QUESTION-233
---

# THEORY-tmpz9axt: Language models trained on limited data show a test loss falling as P^(−γ/(2β)) because P training tokens resolve token correlations only out to a horizon growing as P^(1/(2β)), so that more data mainly lengthens the context a model can use, when the model learns within that horizon faster than it grows, as Cagnetta, Raventós, Ganguli and Wyart propose

## Source

Cagnetta, Raventós, Ganguli and Wyart (2026), [LIT-888](../literature.d/LIT-888.md), §§3–6, as read in
[NOTE-689](../notes.d/NOTE-689.md), with the horizon argument from Cagnetta and Wyart ([LIT-883](../literature.d/LIT-883.md)),
whose account is [THEORY-201](THEORY-201.md).

## What is asserted

That data limits a language model mainly by limiting how far back it can
use context. With P training tokens, the correlation between tokens n
apart can be told from sampling noise only while its top singular value,
~ n^(−β), exceeds ~ P^(−1/2), so the usable horizon grows as P^(1/(2β)).
The loss is then the conditional entropy at that horizon, which falls as
n^(−γ), and the data-limited exponent is γ/(2β), when the excess losses
inside the horizon fall faster. The paper offers this as the mechanism of
the measured scaling law, not only as a formula that fits it.

## What the Active account establishes toward it

[THEORY-204](THEORY-204.md) holds the derivation under the paper's assumed per-lag scaling
forms, re-derived, and the measured match: on two corpora, fits of the
lower envelope of learning curves overlap γ/(2β). That a formula built on
the horizon fits is evidence for the horizon, but γ is estimated from the
trained models' own n-gram losses, so the match is partly internal.

## Also proposed by the source, not filed here

The paper's §6 conjectures that kernel methods and shallow networks fall
outside this "universality class", with worse exponents, by analogy with
the Random Hierarchy Model ([NOTE-689](../notes.d/NOTE-689.md), C7, weak). It is a separate thesis,
argued by analogy and not tested there.

## What would confirm or reject it

The promote_when above, which is [QUESTION-233](../questions.d/QUESTION-233.md)'s test: move one corpus
statistic with the other held and see whether the exponent follows, or
reach horizons of thousands of tokens with γ estimated outside the model
class.

## Provenance

Filed on 2026-10-20 by the narrowing-loss sweep ([ADR-047](../decisions.d/ADR-047.md) v4, batch 068),
from the "because" clause [THEORY-204](THEORY-204.md)'s title carried before it was
narrowed on 2026-10-20.
