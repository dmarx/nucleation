---
# Don't copy this file by hand — run `luria new arg`. An ARG holds what the
# record says about support between its entries: that these premises do, or
# do not, establish this conclusion (ADR-061). File one when the record
# argues a support relation, doubts one, concedes one fails, or needs one as
# a second line. "X does not show Y" is the ARG from X to Y, Rejected, with
# the failing critical question answered in the body. A claim's own
# `rests_on` still needs no ARG (ADR-032).

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
