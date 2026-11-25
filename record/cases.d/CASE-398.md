---
number: 398
status: Proposed
formerly:
- CASE-tmpc7lbu
title: 'GPT-2 small and Pythia-70m measured for the subspaces that enter the logits: exactly, both meet the diversity condition, so every relation satisfies the all-or-none containments; at the tolerance stated in advance the containments fail for three factual relations, and the verdict turns on the tolerance'
version: 1
history:
- version: 1
  date: '2026-11-23'
  note: >-
    Filed 2026-11-23 by the assistant, carrying out LEAD-073 as a delegated
    lead worker. The code, its tests, the tolerances fixed before the first
    real run and the results are committed under
    scratch/studies/lead-073/.
standing: documented
kind: executed-study
tags:
- representation-learning
- mathematical-statistics
date: '2026-11-23'
line:
- learned-structure
- pragmatic-transport
draws_on:
- THEORY-234
bears_on:
- QUESTION-149
- QUESTION-027
summary: >-
  [LEAD-073](../leads.d/LEAD-073.md) asked for [NOTE-746](../notes.d/NOTE-746.md)'s M, N and Γ_q in released models, for
  relations where linearity has been reported. Forward passes of GPT-2 small
  and Pythia-70m, in numpy on CPU, gave the final-layer-norm output f(x) over
  about 3,200 contexts, and the unembeddings gave G. Exactly, both models meet
  the diversity condition: the unembeddings span the whole space, and the
  final layer norm's bias leaves every f(x) with a fixed nonzero component
  off the hyperplane its normalisation confines it to, so F is the whole
  space too. Then M = N = ℝᵈ and the containments Γ ⊆ N and Γ_q ⊆ M hold for
  any relation. At the tolerance stated before the run (singular values above
  1e-3 of the largest; at most 1% of any direction outside), they fail for
  all three relations tested (city in country, country language, country
  capital) in GPT-2 small, whose context spectrum is dominated by one
  direction, and fail narrowly for Γ ⊆ N in Pythia-70m, where f is constant,
  to within 2.4e-4, along one direction. A post-hoc sweep shows the verdict
  turning on the tolerance. City in country is fairly linear in GPT-2 small
  (held-out R² 0.82); the other relations less so. The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-1020 CLAIM-1027 CLAIM-1080 — new; filed by the lead run of 2026-11-23 -->

# CASE-398: GPT-2 small and Pythia-70m measured for the subspaces that enter the logits: exactly, both meet the diversity condition, so every relation satisfies the all-or-none containments; at the tolerance stated in advance the containments fail for three factual relations, and the verdict turns on the tolerance

## The case

**What was asked.** [NOTE-746](../notes.d/NOTE-746.md)'s open question, carried by [QUESTION-149](../questions.d/QUESTION-149.md): do
trained language models satisfy Γ ⊆ N and Γ_q ⊆ M, the conditions under
which Theorem 14 of Marconato et al. ([THEORY-234](../theory.d/THEORY-234.md)) makes a relational linear
property shared by every model inducing the same distribution? [QUESTION-149](../questions.d/QUESTION-149.md)
asks for a tolerance stated in advance.

**Models and access.** GPT-2 small (d = 768, vocabulary 50,257) and
Pythia-70m (d = 512, vocabulary 50,304 including padding rows), downloaded
from huggingface.co on 2026-11-23 into the session's scratch space. Torch
and transformers were not installed, so the forward passes, the safetensors
reader and the byte-level BPE tokenizer were written in numpy
(scratch/studies/lead-073/lmnp.py). On a 63-token English paragraph they
give 2.64 and 3.25 nats per token, in the range expected of these models,
and they pass tests of causality on tiny random models. No weights are
committed.

**Quantities** (geometry.py, tested on [NOTE-746](../notes.d/NOTE-746.md)'s B.5 counterexample, on
Lemma 2's identity f(x)ᵀg₀(y) = (P_M f(x))ᵀ P_N g₀(y), and on recovery of
a known affine map).

- f(x): the final-layer-norm output at the last position, which enters the
  logits through the unembedding with no bias in either model.
- F: the span of f over 3,252 (GPT-2) and 3,232 (Pythia) context vectors:
  every position of 64 random token strings of 32 tokens, every position of
  24 of the model's own samples of 32 tokens from the end-of-text token, and
  the relation prompts.
- G: the span of the pivoted unembeddings, computed as the span of the
  centred unembedding matrix, which is the same subspace.
- M = Im(P_F P_G) and N = ker(P_F P_G)^⊥.
- Γ: the span of the differences between a relation's one-token replies.
- A_q: a ridge fit of P_Γ f(s ⌢ q) = P_Γ A_q f(s) + a_q over the subjects
  (Definition 9), and Γ_q = Im(A_qᵀ P_Γ).

**Relations.** Three of the kinds Hernandez et al. reported as linearly
decoded, written for the study: city in country (84 cities, 12 countries;
q = " is a city in the country of"), country language (49 countries, 18
languages; q = "'s official language is"), and country capital (41 pairs in
GPT-2, 31 in Pythia after dropping replies that are not one token;
q = "'s capital city is").

**Tolerances**, fixed in PREREG.md and committed before the first real run:
a direction belongs to a numerical span when its singular value exceeds
1e-3 of the largest (sensitivity at 1e-2 and 1e-4); M and N keep principal
cosines above 1e-3; S ⊆ T passes when the worst direction of S has at most
1% of its squared norm outside T.

## Results

**Exactly.** Every f(x) satisfies mean((f − β)/γ) = 0, to 4e-8 (GPT-2)
and 6e-9 (Pythia), so f lies in β + diag(γ)1^⊥. Its component along
n ∝ 1/γ is the same for every context: −1.82 in GPT-2 (|f| about 190) and
−2.4e-4 in Pythia (|f| about 440), with standard deviation over contexts
of 3e-8 and 4e-7. Both are nonzero, so F is the whole space ([CLAIM-1020](../claims.d/CLAIM-1020.md)).
The centred unembeddings have full rank in both models (smallest singular
value 9e-4 of the largest in GPT-2, 0.06 in Pythia). So the diversity
condition holds, M = N = ℝᵈ, and the containments hold for every Γ.

**At the pre-registered tolerance (1e-3).**

| model | dim F = dim M = dim N | dim G | relation | Γ ⊆ N, worst share outside | Γ_q ⊆ M, worst share outside | pass |
|---|---|---|---|---|---|---|
| GPT-2 small | 479 | 767 | city in country | 0.47 | 0.18 | no |
| | | | country language | 0.51 | 0.20 | no |
| | | | country capital | 0.61 | 0.30 | no |
| Pythia-70m | 511 | 512 | city in country | 0.010 | 2e-13 | no |
| | | | country language | 0.039 | 3e-13 | no |
| | | | country capital | 0.024 | 3e-13 | no |

GPT-2's context matrix has one singular value 7.6 times the next, and the
bulk falls from 0.13 to 0.0006 of the largest across ranks 2 to 700, so a
tolerance relative to the largest cuts into the bulk: dim F is 12, 479 and
762 at 1e-2, 1e-3 and 1e-4. At 1e-4, Γ_q ⊆ M passes for all three relations
and Γ ⊆ N passes for city in country only (0.004; 0.013 and 0.021 for the
others). In Pythia-70m dim F is 511 at every tolerance from 1e-3 to 1e-6:
the missing direction is n, along which f is constant, and Γ ⊆ N fails
because 1–4% of the worst reply difference lies along it. That component
moves each reply's logit by a context-independent amount of order 1e-5.

**Post-hoc sweep** (not pre-registered; results/*_sweep.json). In GPT-2
small every containment passes from rtol 3e-5 down (dim F 765) and is exact
at 1e-6 (dim F 768). In Pythia-70m the Γ ⊆ N shares stay at 0.010, 0.039
and 0.024 down to 1e-6.

**Linearity itself**, which Theorem 14 presupposes. Held-out R² of the
relational map, and how often the held-out linear probe picks the reply the
model prefers among the relation's replies:

| model | relation | held-out R² | model correct among replies | probe agrees with model | chance |
|---|---|---|---|---|---|
| GPT-2 small | city in country | 0.82 | 0.82 | 0.82 | 0.08 |
| | country language | 0.55 | 0.67 | 0.51 | 0.06 |
| | country capital | 0.54 | 0.63 | 0.44 | 0.02 |
| Pythia-70m | city in country | 0.64 | 0.66 | 0.67 | 0.08 |
| | country language | 0.12 | 0.10 | 0.96 | 0.06 |
| | country capital | 0.25 | 0.35 | 0.65 | 0.03 |

Pythia's 0.96 agreement on country language comes with 0.10 accuracy: the
model prefers nearly the same reply for every country, and the probe copies
that.

**Where Γ_q sits.** Of GPT-2 small's F directions, 3 have a spread of
logits over tokens below 1e-2 of the most visible one (none in Pythia).
Γ_q's operator energy in them is 0.03–0.6%, so the relation maps read the
context through directions that move the logits.

## What it can show

- The exact answer for these two models: Theorem 14's containments hold for
  every relation, because the diversity condition does. That is
  [CLAIM-1027](../claims.d/CLAIM-1027.md)'s reading.
- That the answer at finite precision depends on a tolerance the theorem
  does not supply, and fails at the one stated in advance. That is
  [CLAIM-1080](../claims.d/CLAIM-1080.md)'s reading. The two readings are alternatives, filed for the
  owner's choice.
- A point of method for anyone repeating it. Γ_q estimated by regression on
  the subject representations lies in their centred span, so Γ_q ⊆ M passes
  by construction whenever M holds that span, as it does in Pythia. The test
  that discriminates is Γ ⊆ N.

## What it cannot show

- Anything about models related by approximate rather than exact equality of
  distributions, which is where the tolerance-dependence lives.
- Anything about larger models, or about the relations as Hernandez et al.
  measured them (from a middle layer of the subject token, in larger models).
  Definition 9 maps the last-layer state of s to that of s ⌢ q; this study
  follows the definition.
- How well a tolerance relative to the largest singular value suits a
  spectrum with one dominant direction. It was stated in advance and is
  reported as such; the sweep is post hoc.
