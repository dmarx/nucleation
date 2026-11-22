---
status: Proposed
title: "Barabási and Albert's Models A and B and their nonlinear-kernel simulations, with the chapter's restatement, read as a source, carry the sentence that attachment alone does not guarantee a power law, so they ground that clause of the cumulative-advantage claim"
version: 1
form: source
grounds:
- THEORY-tmpfrz0k
- THEORY-tmpzmy66
concludes:
- CLAIM-817
tags:
- network-science
- probabilistic-modeling
date: '2026-11-22'
line:
- formal-apparatus
summary: >-
  [CLAIM-817](../claims.d/CLAIM-817.md) quotes A3, "preferential attachment alone does not guarantee
  this result. The combination of growth, the form of attachment, and
  other model assumptions determines the distribution", and found that
  Mitzenmacher's review, which A3 cited there, does not say it ([ARG-149](ARG-149.md)).
  Barabási and Albert do ([LIT-3004](../literature.d/LIT-3004.md), [NOTE-tmpwgw8e](../notes.d/NOTE-tmpwgw8e.md)): Model B, without
  growth, is not stationary, and "both ingredients, namely growth and
  preferential attachment, are needed"; and "simulations indicate that
  scaling is present only for α = 1". The chapter ([LIT-2968](../literature.d/LIT-2968.md),
  [NOTE-tmpnpqc8](../notes.d/NOTE-tmpnpqc8.md)) restates both. So the two readings ground that clause.
  The chapter's rival framing of the claim's aside on hyperbolic geometry
  is a contrast, not part of this support. The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-tmpmsncg ARG-tmpqxprw — Proposed; the reading and argument for the kernel regimes, cited beside this one -->
<!-- inactive-ok-file: CLAIM-817 ARG-149 THEORY-tmpfrz0k THEORY-tmpzmy66 THEORY-188 — Proposed; the claim, the readings this argument joins, the argument whose gap it fills and the reading the aside cites -->

# ARG-tmp3q9cy: Barabási and Albert's Models A and B and their nonlinear-kernel simulations, with the chapter's restatement, read as a source, carry the sentence that attachment alone does not guarantee a power law, so they ground that clause of the cumulative-advantage claim

## The inference

[CLAIM-817](../claims.d/CLAIM-817.md), its "Both ingredients are needed" paragraph and its base case.
Grounds: [THEORY-tmpfrz0k](../theory.d/THEORY-tmpfrz0k.md) and [THEORY-tmpzmy66](../theory.d/THEORY-tmpzmy66.md).

## Critical questions (source)

**Does the work say this, read in context?** Yes. Barabási and Albert
(preprint p. 6): Model A "leads to P(k) ∼ exp(−βk)"; Model B "at early
times ... exhibits power-law scaling, P(k) is not stationary", and so
"both ingredients, namely growth and preferential attachment, are needed
for the development of the stationary power-law distribution." p. 7:
"while in general Π(k) could have an arbitrary nonlinear form
Π(k) ∼ k^α, simulations indicate that scaling is present only for α = 1."
The chapter: "if one of them is absent, either the scale-free property or
stationarity is lost" (§5.11), and "Π(k) needs to depend strictly linearly
on the degrees for the resulting network to have a pure power law" (§5.8).
The base case (k_i = m(t/t_i)^(1/2), P(k) = 2m²/k³) is pp. 6 to 7.

**Is it said within the scope the claim needs?** For "growth" and "the
form of attachment". A3's "and other model assumptions" is vaguer than
either source; nothing turns on it. The nonlinear-kernel sentence is one
line on simulations; the regimes in detail are [THEORY-tmpmsncg](../theory.d/THEORY-tmpmsncg.md)'s
([ARG-tmpqxprw](ARG-tmpqxprw.md)).

**Does the claim lean on the reading for more than it holds?** No. One
caution: Model B shows a power law transiently without growth, so "needed"
is for a *stationary* power law, which is the paper's wording and should
be the claim's.

## A contrast the chapter adds

[CLAIM-817](../claims.d/CLAIM-817.md)'s aside says hyperbolic geometry ([THEORY-188](../theory.d/THEORY-188.md)) "needs no
attachment at all". The chapter frames such models the other way: "such
rational decisions can lead to preferential attachment [22, 23, 24]",
citing Papadopoulos and others' "Popularity versus similarity in growing
networks"; these models "do so by generating a linear Π(k)", and "To date
all known models and real systems that are scale-free have been found to
have preferential attachment" (§§5.9, 5.11). That is a rival framing of
the same models, an attachment rule emergent rather than built in, not a
refutation of the aside, which is about the rule a model is given. It
takes no edge.

## Verdict

Support. [THEORY-tmpfrz0k](../theory.d/THEORY-tmpfrz0k.md) and [THEORY-tmpzmy66](../theory.d/THEORY-tmpzmy66.md) replace [LIT-3004](../literature.d/LIT-3004.md) and [LIT-2968](../literature.d/LIT-2968.md)
in [CLAIM-817](../claims.d/CLAIM-817.md)'s grounds.
