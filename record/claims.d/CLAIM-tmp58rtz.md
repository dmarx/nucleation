---
status: Proposed
title: 'In GPT-2 small and Pythia-70m the context representations and the pivoted unembeddings each span the whole space, so the containments of the all-or-none theorem hold for every relation, and whatever relational linearity these models have is shared by every model that induces exactly the same distribution'
version: 1
history:
- version: 1
  date: '2026-11-23'
  note: >-
    Filed 2026-11-23 by the assistant, carrying out LEAD-073 as a delegated
    lead worker, as one of two alternative readings of the same
    measurement. The assistant leans to this one for the question as
    worded; the choice is the owner's.
role: thesis
warrant: empirical
defeated_if: >-
  A recomputation from the released weights of either model showing that
  the centred unembedding matrix is rank-deficient, or that the final layer
  norm's offset Σ βᵢ/γᵢ is exactly zero, so that F or G is a proper subspace;
  or an error in the step from the diversity condition to M = N = ℝᵈ. A
  finding that the containments fail at some numerical tolerance does not
  defeat it: the claim is about exact equality of distributions, which is
  where the theorem lives.
tags:
- representation-learning
- mathematical-statistics
date: '2026-11-23'
line:
- learned-structure
- pragmatic-transport
answers:
- QUESTION-149
bears_on:
- QUESTION-027
rests_on:
- CLAIM-tmp41bjo
grounds:
- CASE-tmpc7lbu
- THEORY-234
summary: >-
  One reading of CASE-tmpc7lbu, offered as an answer to QUESTION-149 for two
  released models. Both meet the diversity condition exactly: the final
  layer norm's offset is nonzero (CLAIM-tmp41bjo), so F = ℝᵈ, and the
  unembeddings have full rank, so G = ℝᵈ. Then M = N = ℝᵈ, Theorem 14's
  containments hold for any Γ, and by Corollary 6 any model inducing exactly
  the same distribution at the same dimension is an invertible linear
  transform of these. The question has a yes answer for them, and an
  uninformative one: it holds of every relation, linear or not. The wording
  is the assistant's (Claude, in this session); adopting it is the owner's
  call.
---
<!-- inactive-ok-file: CLAIM-tmp41bjo CLAIM-tmpdltg3 CASE-tmpc7lbu — new; filed by the lead run of 2026-11-23 -->

# CLAIM-tmp58rtz: In GPT-2 small and Pythia-70m the context representations and the pivoted unembeddings each span the whole space, so the containments of the all-or-none theorem hold for every relation, and whatever relational linearity these models have is shared by every model that induces exactly the same distribution

## The claim

THEORY-234 holds, for softmax next-token predictors, that a relational
linear property is shared by every model inducing the same distribution
when Γ ⊆ N and Γ_q ⊆ M. Under the diversity condition, F = G = ℝᵈ, so
M = N = ℝᵈ and the containments hold for every Γ (NOTE-746).

Both models meet the diversity condition. The F half follows from
CLAIM-tmp41bjo with the measured offsets (c = −1.82 in GPT-2 small,
−2.4e-4 in Pythia-70m, each constant over contexts to within 4e-7). The G
half is a rank computation: the centred unembeddings have full rank, with
smallest relative singular value 9e-4 in GPT-2 small and 0.06 in
Pythia-70m.

So for the three relations of CASE-tmpc7lbu, and for any other, whatever
relational linearity these models have is a property of their distribution
in the theorem's sense. QUESTION-149's own test, "Γ_q has a substantial
component in F outside M", cannot come out positive here, because F
outside M is empty.

## What it does not say

- That the relations are linear. Theorem 14 is conditional on linearity,
  and the held-out fits run from R² 0.82 (city in country, GPT-2 small) to
  0.12 (country language, Pythia-70m).
- Anything about models whose distributions are close to these but not
  equal. CLAIM-tmpdltg3 is the reading that puts the weight there.
- That this is informative about relations in particular. The containments
  hold for every subspace, which is why the assistant reads the result as
  showing where the question's content is not.
