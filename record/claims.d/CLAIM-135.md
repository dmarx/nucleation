---
number: 135
status: Proposed
formerly:
- CLAIM-tmp59oav
title: 'Recovering latent structure from relational data is three achievements, reconstruction, identification up to stated ambiguities, and constitution of a communicative kind, and identifiability theory reaches the second at most'
version: 1
role: thesis
defeated_if: >-
  For the communicative kinds at issue, factors identified from one
  observation family, such as lexical co-occurrence, are shown to coincide
  in general with the kinds identified from interpretive-judgement and
  intervention data, so that the step from identified structure to kind
  needs no evidence beyond identifiability.
tags:
- philosophy-of-science
- mathematical-statistics
- individuation
date: '2026-10-10'
line: 'pragmatic-transport'
answers:
- QUESTION-001
grounds:
- CASE-042
- THEORY-032
complements:
- CLAIM-150
- CLAIM-tmp7gigk
uses:
- TERM-014
- TERM-040
summary: >-
  The assistant's, at A207 §5 (three profiles) and A214 §1 (three
  problems, two warrants), kept as A218 §5's five objects of inquiry. A214
  asked for it as a THEORY; it is the record's own distinction, so it is a
  claim. It answers [QUESTION-001](../questions.d/QUESTION-001.md) in part, by naming a failure that
  question did not. It does not say identified factors are never kinds,
  or that the second step is open.
illustrated_by:
- CASE-040
- CASE-042
supports:
- CLAIM-139
- CLAIM-tmp6r6t6
- CLAIM-tmp3wo5j
---

# CLAIM-135: Recovering latent structure from relational data is three achievements, reconstruction, identification up to stated ambiguities, and constitution of a communicative kind, and identifiability theory reaches the second at most

## The claim

A214 §1 sets out three questions: whether a low-dimensional structure
explains the observed relationships, whether it can be recovered uniquely
"apart from transformations that do not affect its identity", and whether
the recovered structure does "remain meaningful when we change the
observational system, representation, or causal conditions". Then: "Matrix factorization
addresses the first. Identifiable factorization and topic-model theory
address the second under specified assumptions. **Our manuscript is
principally concerned with the third.**"

A214 names three layers: "X: observed relational evidence, (W,H): latent
explanatory representation, 𝒦: structural kinds posited by the
explanation". And two warrants: "The transition from *good
reconstruction* to *identified structure* requires assumptions and
evidence. The transition from *identified structure* to *real relational
kind* requires an additional scientific and philosophical argument."

The first two steps are A207's. A207 §5 had distinguished "Observed
relational profile / Model-imputed relational profile / Structurally
identifiable relational profile", and said "The third requires additional
assumptions and evidence." A214 added the third step, from identified
structure to kind. A218 §5 keeps the distinction and splits it finer:
"Observed relational evidence. Latent explanatory representations.
Statistically identifiable structure. Task-sufficient structural
information. Philosophically proposed constitutive relations."

The record holds the three as distinct achievements, each with its own
warrant.

1. **Reconstruction** is warranted by fit, on held-out entries.
2. **Identification** up to stated ambiguities is warranted by a theorem
   and its conditions: a stated gauge ([CLAIM-148](CLAIM-148.md)), and conditions
   such as separability or anchor words for topic models
   ([CASE-042](../cases.d/CASE-042.md)). Identifiability theory gives sufficient conditions
   for this step and reaches no further.
3. **Constitution** of a communicative kind ([TERM-040](../terms.d/TERM-040.md)) needs evidence
   that the identified structure is what the act consists in, not only
   what one family of observations reveals of it. That evidence must come
   from probes chosen for their bearing on the act, and from an argument
   about what the act is ([CLAIM-150](CLAIM-150.md)).

The second step is relative to the probes in the way [TERM-014](../terms.d/TERM-014.md) says an
observational class is: two items are indistinguishable relative to a
probe set and a model class. The third step is not relative in that way. A
kind can be real and still unseparated by an insufficient family of
probes. A218 Ch7: "A structural kind may be real while remaining
indistinguishable under an insufficient family of empirical probes."

[THEORY-032](../theory.d/THEORY-032.md) supplies the formal limit on the third step. Even a complete
relational profile, the whole hom-functor, determines an object only up to
isomorphism and presupposes the relata. A data matrix is less than that,
since it has no composition.

[QUESTION-001](../questions.d/QUESTION-001.md) asks how far pragmatic identity can be reconstructed from
context-relative judgements. This claim answers part of it. Even a
reconstruction that is consistent and identified falls short of the kind
until the third warrant is given.

## Completion is not identification

The first step can succeed while the second fails, and A207 §5 gives the
mechanism. "A sparse matrix can often admit multiple completions
consistent with every observed entry. Those completions may disagree on
the similarity of two items". So "a latent representation may look stable
because the model's regularization selected one completion, not because
the observed relational evidence uniquely determined it."

The theory here is standard. A rank-k m×n matrix has k(m+n−k) degrees of
freedom, so fewer observed entries cannot identify it. With more, the
sampling pattern and the matrix's incoherence decide whether the
completion is unique. Candès and Recht's guarantee for exact completion
(doi:10.1007/s10208-009-9045-5; not held in either record) assumes entries
sampled uniformly at random. Missing-not-at-random exposure violates
exactly that, and A207 §5 names it: it "can make learned factors reflect
selection patterns rather than preferences or communicative
distinctions." Randomized assignment of realizations to interpreters
restores the standard conditions. Active querying improves the design but
guarantees nothing.

One pointer bears on A207's own proposal and is not worked out here.
A207's judgement data form a four-way tensor Y_uiac. A CP decomposition of
a tensor of order three or more is essentially unique, up to scaling and
permutation, under Kruskal's rank condition. So unlike the matrix case, its
components can be identifiable without nonnegativity. A Tucker
decomposition keeps a gauge on each mode. A207 calls tensor factorization
"not a novel contribution", which is true, but its bearing on the second
step goes unsaid.

## What it does not say

It does not say identified factors are never kinds. It says only that
identifiability does not make them kinds. It does not claim the second step
is open: for topic models and latent-structure models there are
sufficient conditions (Donoho and Stodden; Arora, Ge and Moitra; Allman,
Matias and Rhodes, arXiv:0809.5032). None of these is held in either
record. It does not say the third step is out of reach. It says the third
step needs evidence of a different kind from the second, and that
neither A214 nor A218 supplies it.
