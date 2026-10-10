---
number: 27
status: Open
formerly:
- QUESTION-tmp0p9xm
title: 'Is there a relational signature of a communicative kind that is stable under admissible transformations, sufficient for a family of decisions and discriminating on designated contrasts, and can it be identified from the available probes, for decisions outside them, when the full latent model cannot?'
version: 1
tags:
- mathematical-statistics
- information-theory
date: '2026-10-10'
line: 'pragmatic-transport'
refines:
- QUESTION-006
- QUESTION-001
summary: >-
  The assistant's "central construction problem" (A203 §36) joined to its
  question of sufficiency without full identification (A214 §7, A218 RQ3
  and Part III). The exchange calls it the central unresolved problem
  twice. Its unrestricted form is answered by standard results, so it is
  filed narrowed: it has content only for decisions about unobserved
  probes, interventions and transported targets. As A203 states it, it is
  not well posed.
answered_by:
- CLAIM-tmp7gigk
---
<!-- inactive-ok-file: CLAIM-125 CLAIM-092 THEORY-175 CLAIM-135 — Proposed; open, and cited as the claims and reading this question is set beside, not as settled -->

# QUESTION-027: Is there a relational signature of a communicative kind that is stable under admissible transformations, sufficient for a family of decisions and discriminating on designated contrasts, and can it be identified from the available probes, for decisions outside them, when the full latent model cannot?

## Why it is a question

The question came in two halves, from two stretches of the exchange, and
A214 joined them.

**Stability, sufficiency and discrimination.** A198 §X proposed to
"identify minimal, transformation-stable, decision-sufficient relational
signatures of communicative kinds". A203 §36, headed "The most important
unresolved mathematical problem", asks for a signature χ_A of a kind A,
given a family of realizations, a set of transformations 𝒯 and a family of
decision tasks 𝒬, with three properties: transformation stability,
decision sufficiency and discriminating power. Its box reads, transcribed
from the display: "Find a relational signature χ that is maximally stable
under 𝒯, sufficient for decisions in 𝒬, and discriminating on designated
structural contrasts." It uses "character" literally only "when χ is a
trace character of a specified representation".

**Sufficiency without identification.** After the factorization turns
(U57–U59), A214 §7 separated identifiability from sufficiency: "A perfectly
identifiable signature can be useless for a particular decision. A
nonidentifiable latent model can nevertheless support accurate predictions
when the unidentifiable distinctions do not matter for those decisions."
So "**decision-sufficient structure may be recoverable even when the full
underlying model is not identifiable**." A214 §11 put the four properties
together, "Identifiable", "Transformation-stable", "Decision-sufficient"
and "Empirically grounded", and boxed the question: "**Can task-sufficient
structural information be identifiable across representations even when
the underlying latent factorization is not?**"

A218 kept it as RQ3, "When can decision-relevant structural information be
identified even when a richer latent decomposition is not uniquely
recoverable?", and as its priority theorem target: "**identifiability of
task-sufficient structure without identifiability of the full latent
model**". Its substantive form there is "to characterize when particular
relational signatures satisfy it under sparse, multi-view, context-indexed
observation, and whether their sufficiency survives admissible stochastic
transport." A207's boxed question and A210 §7's rewrite of it ("remain
identifiable, decision-sufficient, and structurally stable across
translations, observational regimes, and causal interventions") are
earlier forms.

What would count as an answer: for a stated class of transformations and a
stated family of decisions outside the observed probes, a characterization
of the signatures that are both decision-sufficient and identified from the
probes, or a proof that no such signature exists when the latent model is
not identified.

## What is already known

Much of the unrestricted question is answered.

- **Gauge-invariant functionals are identified.** Any function of the
  factors that is invariant under the gauge is a function of the predicted
  matrix WH, so it is identified whenever the reconstruction is
  ([CLAIM-148](../claims.d/CLAIM-148.md)). That covers every predicted entry, the rank and the
  singular values.
- **Matrix completion.** Under incoherence and enough random samples,
  every missing entry is identified with no identifiability of the factors
  (Candès and Recht, doi:10.1007/s10208-009-9045-5; not held in either
  record). The task "predict any cell" is answered.
- **Partial identification.** In econometrics and causal inference, a
  target functional is often identified without the full model. The
  causal-effect identification that A214 itself invokes is an instance.
- **A218's theorem target is a definition.** A signature s is identified
  from a probe system 𝒪 exactly when θ ∼_𝒪 θ′ implies s(θ) = s(θ′), that
  is, when s is constant on the observational equivalence classes. A218
  says so itself: "That basic equivalence is mathematical bookkeeping, not
  a novel theorem."
- **In-probe decisions are automatic.** When a decision's risk depends on
  the model only through the law of the observed probes, P_θ(Y_𝒪), every
  optimal rule is constant on the equivalence classes, so a
  decision-sufficient signature is identified by construction. Predicting
  held-out ratings in collaborative filtering is the standard case. A218's
  hypothesis H4, "some decision-sufficient signatures will remain usable
  despite ambiguity in richer latent models", cannot fail for such
  decisions.

So the question has content only for decisions that reach outside the
fitted relations: new probes, interventions, or a target system after
transport. There the question is when the optimal decision is constant on
the set of models consistent with the data, and whether a transport
preserves that set. A214's "a worthwhile mathematical research question in
its own right" overstates the novelty of the unrestricted version.

## What it is not

- **It is not well posed as A203 states it.** Maximal stability favours
  coarse signatures, and sufficiency and discrimination favour fine ones.
  "Maximally stable" subject to the other two needs a trade-off parameter,
  and A203 gives none. The problem has the shape of an information
  bottleneck ([CLAIM-092](../claims.d/CLAIM-092.md), [LIT-338](../literature.d/LIT-338.md)) with an added invariance constraint.
  A214 §11's boxed optimization, transcribed from the display, "minimizes relevant information loss under
  admissible transformations, subject to identifiability, discrimination,
  and held-out decision-performance constraints", names no objective, rate
  or constraint set either.
- **It is not [CLAIM-125](../claims.d/CLAIM-125.md).** It is the factorization-side analogue of
  [CLAIM-125](../claims.d/CLAIM-125.md)'s first open part. Both ask when decision-relevant information
  survives a map whose finer structure is not determined. [CLAIM-125](../claims.d/CLAIM-125.md) asks it
  of transport between empirical models whose covers change. This
  question asks it of a latent model the probes do not identify.
- **It is not one sense of "anchor".** Three senses meet here and must not
  be conflated. A214 §2's "pragmatic anchors", carried into A218 Ch6.4 as
  "Pragmatic analogues of anchor variables", are observables selectively
  associated with one kind, by analogy with anchor words. [CLAIM-011](../claims.d/CLAIM-011.md)'s
  anchoring estimates the source–target correspondence on independently
  measured distinctions. [THEORY-175](../theory.d/THEORY-175.md)'s anchors are matched reference
  points whose cosines define a representation.
- **It is not the question of whether the signature is the kind.** An
  identified, decision-sufficient signature is still at the second of
  [CLAIM-135](../claims.d/CLAIM-135.md)'s three steps.
