---
status: Proposed
title: 'The line''s proposed quantities have no finite-data estimators, and its evidence that signalling is typical of language data rests on plug-in estimates from one or a few occurrences, which signal even when the true marginals agree'
version: 1
role: counter
tags:
- mathematical-statistics
- contextuality
date: '2026-10-10'
line: pragmatic-transport
grounds:
- LIT-851
- THEORY-165
- THEORY-168
objects_to:
- CLAIM-125
- CLAIM-105
uses:
- TERM-028
summary: >-
  Found in the record's audit of the line on 2026-10-10 (formal and
  empirical lenses); no turn of the exchange raises it. The plug-in
  signalling of two empirical marginals is positive in expectation when
  the true marginals agree, so raw tables signal, and the contextual
  fraction is undefined on them. With one occurrence per context, a
  non-signalling rank-2 system gives Δ of 0, 2 or 4, with expectation 2:
  the values [NOTE-654](../notes.d/NOTE-654.md) finds in 51 of the 90 systems behind [CLAIM-125](CLAIM-125.md)'s
  "69 of the 90 systems signal". The data are author-assigned corpus
  senses, not judgements. Deficiency over text-valued renderings has no
  estimator. It does not say signalling is rare in pragmatic judgements,
  where order effects are themselves signalling.
---
<!-- inactive-ok-file: CLAIM-125 CLAIM-105 — Proposed; open, and cited as the claims this objection is to -->
<!-- inactive-ok-file: CLAIM-127 — Proposed; cited for its separation of corpus from elicitation and its two routes to signalling, open -->
<!-- inactive-ok-file: THEORY-165 THEORY-168 THEORY-176 THEORY-177 — Proposed; cited for the Lipschitz bound, the representation-dependence of CbD verdicts, task-loss comparison and the signalling identity, not as settled -->

# CLAIM-tmpji66i: The line's proposed quantities have no finite-data estimators, and its evidence that signalling is typical of language data rests on plug-in estimates from one or a few occurrences, which signal even when the true marginals agree

## The objection

**Raw tables signal.** From finite samples, the relative frequencies of a
content's values in two contexts need not agree when the true
probabilities do, and they disagree more often the fewer the occurrences.
So the
plug-in signalling Δ̂ = Σ over contents of |⟨R̂⟩_c − ⟨R̂⟩_c′| is positive
in expectation even when the true marginals are equal.

A worked case. Take a rank-2 system with no signalling at all: in both
contexts, each of the two contents is +1 or −1 with probability 1/2, so
Δ = 0. Observe one occurrence per context. Each estimated mean ⟨R̂⟩ is then
+1 or −1. The two contexts' occurrences are independent, so for each
content the two estimates differ with probability 1/2, and its term
|⟨R̂⟩_c − ⟨R̂⟩_c′| is 0 or 2 with probability 1/2 each. So Δ̂ takes only the
values 0, 2 and 4, and its expectation is 2, half the largest possible
value, where the true Δ is 0.

Those are the values [NOTE-654](../notes.d/NOTE-654.md) reports. Its limitations: "51 of 90 systems
have Δ exactly 0, 2 or 4, and 18 have err(Δ) = 1.41. Both patterns suggest
one or a few occurrences per context." [NOTE-654](../notes.d/NOTE-654.md) draws the consequence only
for the systems with Δ = 0: "18 of the 21 with Δ = 0 have err(Δ) of 1 or
more, so even those are not evidence of non-signalling." The same counts
make the signalling systems weak evidence of signalling. [CLAIM-125](CLAIM-125.md) states
"69 of the 90 systems signal" and "34 signal enough that they cannot be
contextual at all", and concludes, without the caveat: "So for language
data signalling is the typical case, not an edge case, and an extension to
signalling data is not optional." [CLAIM-127](CLAIM-127.md) repeats the count.

**The data are not judgements.** [NOTE-654](../notes.d/NOTE-654.md): the probabilities "are relative
frequencies of interpretations that the authors assigned by hand to BNC
and ukWaC occurrences. No annotation protocol or agreement is reported."
It leaves open "Whether a human-judgement version (proposed in §5) gives
the same Δ levels as corpus frequencies." [CLAIM-127](CLAIM-127.md) separates the two:
"Corpus estimates involve no elicitation at all." [CLAIM-125](CLAIM-125.md) still speaks of
"language data".

**The proposed quantities have no estimators.**

- **The contextual fraction.** [CLAIM-105](CLAIM-105.md): "the contextual fraction is
  defined only without signalling". Raw estimates usually signal, so it is
  undefined on them. Using it needs a projection onto the
  no-signalling tables, for which the record has no rule, or a CbD
  treatment, whose verdict depends on how the system is represented
  ([THEORY-168](../theory.d/THEORY-168.md)). [THEORY-165](../theory.d/THEORY-165.md)'s Lipschitz bound holds for no-signalling tables
  within one scenario, and its constant "depends on the scenario and is
  not bounded here". So no bound on sampling error follows from it.
- **Per-content signalling Δ*.** Its plug-in estimate is biased upward, as
  above.
- **Deficiency** ([TERM-028](../terms.d/TERM-028.md)'s δ_Q). It is an infimum over Markov kernels
  from one rendering space to the other of a supremum over states. For
  renderings that are texts or images, the kernels act on an unbounded
  space. It is a finite linear programme only when the states are finite
  and the likelihoods known. The one held-out "Blackwell experiment" in the
  exchange is a task-loss comparison instead ([CASE-042](../cases.d/CASE-042.md), [THEORY-176](../theory.d/THEORY-176.md)).

## What it does not say

- It does not say signalling is rare. Elicited judgements have their own
  routes to signalling ([CLAIM-127](CLAIM-127.md), "Two routes to signalling"), and order
  effects are signalling in the CbD sense. [CLAIM-125](CLAIM-125.md)'s "not optional" may
  well be right. Its stated evidence does not carry it.
- It does not say [LIT-851](../literature.d/LIT-851.md)'s signalling result is wrong. Its Proposition 1
  is a proof ([THEORY-177](../theory.d/THEORY-177.md)); the objection is to the counts read off its
  appendix.

## What would answer it

- Estimators with bias correction and a stated sampling error, or a test
  for signalling with a stated null hypothesis, applied to [LIT-851](../literature.d/LIT-851.md)'s
  systems with their occurrence counts.
- [CLAIM-125](CLAIM-125.md)'s evidence restated from elicited judgements, if the claim is
  about pragmatic data.
- For deficiency, a computable surrogate on a finite designed state space
  with known or estimated likelihoods.
