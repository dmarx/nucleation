---
status: Proposed
title: 'Matched ordinary behaviour and differing responses to intervention show that organizational perspectives explain what the record explained by self'
version: 1
form: evidence
tags:
- philosophy-of-science
- complex-systems
date: '2026-10-28'
line: distributed-agency
rests_on:
- CLAIM-414
grounds:
- CASE-161
- CASE-163
- CASE-164
- CASE-166
concludes:
- CLAIM-417
summary: >-
  CLAIM-414 and the lab's runs show organizations with the same ordinary
  behaviour that respond differently to specified interventions. That is
  offered as evidence for CLAIM-417, that organizational perspectives
  explain what the record explained by self. CLAIM-417's defeater is that
  established accounts explain the same transitions as well with fewer
  assumptions, and only a model that out-predicts them at matched
  complexity bears on that. No premise does yet. It becomes Rejected if the
  owner accepts the grading.
---
<!-- inactive-ok-file: ADR-061 — Proposed; the decision under whose migration this entry was filed or revised -->
<!-- inactive-ok-file: CLAIM-417 CLAIM-342 CASE-161 CASE-163 CASE-164 CASE-166 — Proposed; the conclusion, the rule it applies and the lab's runs, cited as where the evidence stands -->
<!-- inactive-ok-file: CLAIM-427 — Superseded; the claim this argument was moved from -->

# ARG-tmpgr3fb: Matched ordinary behaviour and differing responses to intervention show that organizational perspectives explain what the record explained by self

## The inference

CLAIM-414 (Active) shows that matched ordinary trajectories can conceal
differences in an interpretation's efficacy, and that an intervention
separates them. The Perspective Population Lab's runs (CASE-161, CASE-163,
CASE-164) and the reported Northstar study (CASE-166) are offered in the
same role. If organizations that look alike part under intervention, the
organizational description is doing explanatory work. The conclusion is
CLAIM-417: what the record explained by "self" "is better explained by
organizational perspectives".

## Critical questions

The `evidence` form's questions are answered by the three grades CLAIM-427
set out, after A4 of the exchange of 2026-10-23, "Framework Overview
Request":

| Finding | What it establishes |
|---|---|
| "Different organizational mechanisms can produce identical ordinary behavior" | Non-identifiability from passive observation |
| "Those mechanisms predict different responses to independently specified interventions" | That the organizational distinctions matter |
| "The proposed framework predicts these differences better than established alternatives" | A distinctive theoretical contribution |

- **Would the evidence be expected if the hypothesis were false?** For
  the first two grades, yes. CLAIM-417's defeater is that established
  accounts (habitus, adaptive networks, reflected appraisal,
  mixture-of-experts routing, organizational learning) "explain the same
  transitions as well with fewer assumptions". "Showing that
  organizations differ under intervention does not touch it, since the
  established accounts may predict the same differences."
- **Does it tell the hypothesis apart from its rivals?** Only the third
  grade would, and this is the question that fails. A4: "beating a
  deliberately weak baseline is not evidence for a unifying theory." The
  measure A4 proposed is the drop in predictive risk over a prespecified
  distribution of interventions when the coupling of significance,
  authority and reproduction is represented, at comparable complexity and
  information budgets. No premise meets it.
- **Does the measure measure what it is said to?** Only if success is not
  defined in the framework's own terms. A4: "Suppose a system is described
  as possessing a perspective because its processes are mutually
  influential, and the experiment then demonstrates that its processes are
  mutually influential. Nothing substantive has been learned." That is
  CLAIM-342's rule for a self-confirming loop, applied to the record's own
  programme.

## Where the premises stand

From CLAIM-427's notes of 2026-10-26, where the runs are given in full:

- **CLAIM-414** meets the first grade for two constructions, and its
  intervention meets the second within them.
- **CASE-161 and CASE-164** meet the first two grades within synthetic
  constructions. CASE-163 predicts withheld interventions from probes, but
  its forecaster is given the four candidate mechanisms and their
  equations.
- **The comparators.** A generic state-space model with the same
  transition kernels ties exactly, by construction (dmarx/PerspectiveLab@dce302b).
  v2.3's matched comparator (dmarx/PerspectiveLab@e9efcf4) loses on the
  bottleneck law with the mixed graph to a generic 20-coefficient
  polynomial. v2.5's adequacy guard (dmarx/PerspectiveLab@f392084) is
  matched action for action by a conventional controller given the same
  kernels. v2.6 (dmarx/PerspectiveLab@74621fb) gains by measuring the
  relevant variables inside a supplied catalog. v2.7 to v2.9
  (dmarx/PerspectiveLab@c54617e) match information but not complexity, or
  have no comparator, or tie by identity.
- **CASE-166**, Northstar as reported at T20 of the exchange "Experimental
  Infrastructure Review", meets neither of the first two grades, and its
  router "ties" a conventional router at the same regret. The lab holds no
  v2.10 or v2.11, so none of it is checked.

"The third grade is still unmet."

## Carried from CLAIM-427

The argument scheme has no `works`, `defeated_if` or `complements`, so
what CLAIM-427 carried there is kept here.

- **Work.** CLAIM-427 was part of the manuscript `organization-of-perspective`.
  The grading belongs to that work's account of its own evidence.
- **Defeat condition**, as CLAIM-427 stated it: "A form of evidence that
  would rightly count for the framework against established accounts
  (habitus, adaptive networks, reflected appraisal, mixture-of-experts
  routing, organizational learning) without out-predicting them under
  intervention: for instance, if a unification that predicts nothing new
  is itself enough to prefer a theory; or a showing that the third grade
  cannot be met even in principle, because any model that represents the
  coupling is matched by an alternative of equal complexity." Either would
  reopen this verdict.
- **Complements.** CLAIM-417, whose defeater the grading reads, and
  CLAIM-342, whose rule on self-confirming loops the third question
  applies.

## Verdict

Proposed. The premises meet the first two grades and not the third, so
the evidence does not yet bear on CLAIM-417's defeater. If the owner
accepts the grading, the argument is Rejected as it stands, and a premise
that meets the third grade would be a new version of it. The grading does
not say the framework fails. A3: "the current work has earned the status
of a potentially useful conceptual synthesis, not yet an independent
explanatory framework."

Filed 2026-10-28 by the ADR-061 migration, from CLAIM-427.
