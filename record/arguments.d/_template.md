---
# Don't copy this file by hand — run `luria new arg`. An ARG is filed only
# when something needs to point at an inference: a second, independent line
# of support for a claim, or an objection to the inference itself (an
# undercut). Most claims need no ARG; their `rests_on` is their argument
# (ADR-032).

# Active | Proposed | Deferred | Superseded | Rejected — whether the
# INFERENCE holds, which is not whether its conclusion is true.
status: Proposed

title: From the premises to the conclusion, in one line

version: 1

# analogy | contrast | existence | formal-application | generalization |
# abduction | cause-to-effect | reductio. The form's critical questions are
# in luria.yaml; answer each in the body, or expect an objection.
form: analogy

# Premises: the record's own claims in `rests_on`, readings, cases and works
# in `grounds`. At least one of the two.
rests_on:
- CLAIM-000
# grounds:
# - THEORY-000
concludes:
- CLAIM-000

tags:
- agency
date: '2026-01-01'
# line: will-organization

summary: >-
  The inference, and its weakest step.
---

<!-- unresolved-ok-file: CLAIM-000, THEORY-000 — the placeholder a new document replaces -->

# ARG-NNN: From the premises to the conclusion, in one line

## The inference

How the premises yield the conclusion.

## Critical questions

Each question the form raises, and its answer. For an analogy: the respect
in which the cases are alike, what transfers, and what does not.
