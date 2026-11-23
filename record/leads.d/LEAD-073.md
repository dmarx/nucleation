---
number: 73
status: Open
formerly:
- LEAD-tmpc51c3
title: 'Measure the quantities of the pragmatic-geometry account in released language models'
version: 1
stage: idea
priority: medium
method:
- empirical
tags:
- mathematical-statistics
- information-theory
date: '2026-11-19'
line:
- pragmatic-transport
advances:
- QUESTION-027
summary: >-
  Named in [NOTE-746](../notes.d/NOTE-746.md). Filed by the backlog audit of 2026-11-19.
---
<!-- inactive-ok-file: CASE-tmpc7lbu CLAIM-tmp41bjo CLAIM-tmp58rtz CLAIM-tmpdltg3 — new; filed by the lead run of 2026-11-23 -->

# LEAD-073: Measure the quantities of the pragmatic-geometry account in released language models

## What it would do

Compute the relations M, N and Γ_q that [NOTE-746](../notes.d/NOTE-746.md) defines for the relations
in which linearity has been reported, in open released models.

Where the record names it:

- [NOTE-746](../notes.d/NOTE-746.md): "A measurement of M, N and Γ_q in released models would settle
  it."

## What would count

Relations that satisfy the inclusions in released models answer
[QUESTION-027](../questions.d/QUESTION-027.md) for them; a failure says linearity there has another source.

## Note of 2026-11-23: run by the lead worker

Done on the branch claude/lead-073-pragmatic-geometry; the code, tests,
tolerances fixed in advance (PREREG.md) and results are under
scratch/studies/lead-073/, and the run is [CASE-tmpc7lbu](../cases.d/CASE-tmpc7lbu.md). Both models were
reachable from huggingface.co; torch was not installed, so the forward
passes were written in numpy.

- **Models and relations.** GPT-2 small and Pythia-70m; city in country,
  country language and country capital, three of the kinds Hernandez et al.
  reported as linearly decoded. The question this measurement answers to
  most directly is [QUESTION-149](../questions.d/QUESTION-149.md), which carries the same request.
- **Exactly**, both models meet the diversity condition: the final layer
  norm leaves every context representation with one fixed nonzero
  component, which makes F the whole space ([CLAIM-tmp41bjo](../claims.d/CLAIM-tmp41bjo.md)), and the
  unembeddings have full rank. So M = N = ℝᵈ and the containments hold for
  every relation.
- **At the tolerance stated in advance** the containments fail: for all
  three relations in GPT-2 small, and narrowly (Γ ⊆ N only) in Pythia-70m.
  A post-hoc sweep shows the verdict turning on the tolerance.
- **Two readings**, filed as alternatives: [CLAIM-tmp58rtz](../claims.d/CLAIM-tmp58rtz.md) (the exact
  containments answer the question yes, trivially; the assistant's lean
  for the question as worded) and [CLAIM-tmpdltg3](../claims.d/CLAIM-tmpdltg3.md) (the question's content
  is about approximate equivalence, where a finite-precision measurement
  does not settle it). The choice is the owner's.

What remains: larger models, and the relations as Hernandez et al.
measured them, from a middle layer. Both matter only under the second
reading, which would first need the approximate question stated. No status
or stage was changed.
