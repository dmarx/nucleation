---
status: Proposed
title: 'Measured at the tolerance stated in advance, the containments of the all-or-none theorem fail for three factual relations in GPT-2 small and, narrowly, in Pythia-70m; since they hold exactly, the verdict turns on a tolerance the theorem does not supply, and a measurement at finite precision does not settle whether those relations are properties of the distribution'
version: 1
history:
- version: 1
  date: '2026-11-23'
  note: >-
    Filed 2026-11-23 by the assistant, carrying out LEAD-073 as a delegated
    lead worker, as one of two alternative readings of the same
    measurement. The choice between them is the owner's.
role: counter
warrant: empirical
tags:
- representation-learning
- mathematical-statistics
date: '2026-11-23'
line:
- learned-structure
- pragmatic-transport
bears_on:
- QUESTION-149
- QUESTION-027
objects_to:
- CLAIM-tmp58rtz
grounds:
- CASE-tmpc7lbu
- THEORY-234
summary: >-
  The other reading of CASE-tmpc7lbu. At the tolerance fixed before the run
  (spans at 1e-3 of the largest singular value, at most 1% of any direction
  outside), Γ ⊆ N and Γ_q ⊆ M fail for city in country, country language
  and country capital in GPT-2 small (worst shares outside 0.2–0.6), and
  Γ ⊆ N fails narrowly in Pythia-70m (0.010–0.039). A post-hoc sweep makes
  GPT-2 pass from 3e-5 down while Pythia keeps failing to 1e-6. The exact
  yes of the alternative reading holds for every subspace whatever, so it
  does not answer QUESTION-149's concern; the concern is about nearly
  equivalent models, and there the answer is tolerance-relative. The wording
  is the assistant's (Claude, in this session); adopting it is the owner's
  call.
---
<!-- inactive-ok-file: CLAIM-tmp58rtz CLAIM-tmp41bjo CASE-tmpc7lbu — new; filed by the lead run of 2026-11-23 -->

# CLAIM-tmpdltg3: Measured at the tolerance stated in advance, the containments of the all-or-none theorem fail for three factual relations in GPT-2 small and, narrowly, in Pythia-70m; since they hold exactly, the verdict turns on a tolerance the theorem does not supply, and a measurement at finite precision does not settle whether those relations are properties of the distribution

## The claim

QUESTION-149 asks for the containments to be tested "with a tolerance
stated in advance". The tolerance was stated and committed before the
first run (scratch/studies/lead-073/PREREG.md). At it:

- In GPT-2 small, F, and with it M and N, is 479-dimensional. The reply
  differences of all three relations have 47–61% of their worst direction
  outside N, and Γ_q has 18–30% outside M. The cause is the spectrum: one
  direction of the context representations is 7.6 times the next, and the
  rest decay smoothly, so a tolerance relative to the largest cuts into
  directions the relations use.
- In Pythia-70m, F is 511-dimensional at every tolerance from 1e-3 to 1e-6.
  The missing direction is the one along which every context
  representation is the same (CLAIM-tmp41bjo), with a common component of
  only 2.4e-4. The reply differences have 1.0%, 3.9% and 2.4% of their worst
  direction along it, so Γ ⊆ N fails, narrowly. Γ_q ⊆ M passes, as it must
  by construction here (CASE-tmpc7lbu, "What it can show").

The alternative reading, CLAIM-tmp58rtz, answers yes because the
containments hold exactly. But exact containment holds for every subspace in
a model that meets the diversity condition, so it does not distinguish the
reported relations from any others. The theorem's worry, components of f
that an equivalent model may distort freely, has its practical form in
directions that barely move the logits, and whether a relation uses them is
a question about models whose distributions are close, not equal. Asked
that way, the answer depends on the tolerance, which nothing in the theorem
fixes. The measurement therefore does not settle QUESTION-149 in the form
that matters, and the question's content moves to approximate equivalence.

## What it does not say

- That the relations are artefacts of one fitted model. Nothing here
  measures what a nearly equivalent model does with them.
- That the pre-registered tolerance was a good one. It is reported because
  it was stated first. A tolerance relative to the second singular value,
  or to the logit effect, would give a different verdict for GPT-2 small;
  choosing one is part of the approximate question.
- Anything about the relations' linearity, which the case reports
  separately.
