---
status: Open
title: 'Test whether one intervention on an independently measured constraint, the concern-relative significance of a domain or the provenance of selected evidence, moves several named bias measures together with the information held fixed, against noisy-processing and resource-rational accounts of their co-variation'
version: 1
stage: idea
priority: medium
method:
- empirical
- operationalization
tags:
- cognition
- psychometrics
- emotion-and-affect
date: '2026-11-24'
line:
- organizational-affect
- will-organization
advances:
- CLAIM-tmp5atd3
- CLAIM-446
summary: >-
  From A11 §15 and A12 §15 of the exchange "Memes, Contracts, and Systemic
  Normativity" (2026-11-24), whose tables propose the interventions without
  a design, and a gap fill ([ADR-137](../decisions.d/ADR-137.md)) for what a design needs: the shared
  constraint measured apart from the biases, bias measures whose
  reliability is known, and a rival that predicts co-variation from another
  manipulation. The wording of the plan is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---

<!-- inactive-ok-file: CLAIM-tmp5atd3 CLAIM-446 LIT-tmpngp4x LIT-tmp7lswl THEORY-359 — Proposed, Deferred or new; the claims this lead tests, the design it extends and the works it is set against -->

# LEAD-tmpr4xwc: Test whether one intervention on an independently measured constraint, the concern-relative significance of a domain or the provenance of selected evidence, moves several named bias measures together with the information held fixed, against noisy-processing and resource-rational accounts of their co-variation

## What the exchange proposes

A11 §15 lists ten experiments, among them "Match evidence while varying its
selection provenance", "Transfer culturally expressed reasoning rules |
Multiple bias measures change together where shared organizational
constraints are reproduced", "Vary the topology of social exposure" and
"Interrupt interpretation–authority feedback | Multiple mutually
reinforcing biases weaken through a common intervention". A12 §15 adds
"Alter concern-relative significance while holding information fixed |
Several judgment biases change together" and "Change explicit beliefs while
holding affective organization relatively constant | Biases of action or
attention persist despite belief correction". Both say the result must beat
strong alternatives; A12: "The important test is whether separately
measured significance, readiness, authority and maintenance dynamics
predict responses better than established alternatives."

## The plan

1. **Pick the constraint and measure it first.** For a protective regime
   ([CLAIM-446](../claims.d/CLAIM-446.md)), threat significance of a domain measured before and apart
   from the bias tasks; for evidence provenance, a manipulation of how the
   evidence was selected with its content fixed.
2. **Pick three to five bias measures** the claim says the constraint
   couples (threat attention, selective recall, asymmetric evidence
   thresholds, pessimistic forecasting, avoidance) and one it says it does
   not, as a control.
3. **Check the measures' reliability before reading co-variation.** Bias
   tasks with low test–retest reliability attenuate any correlation among
   them; and Many Labs 2 ([LIT-tmp7lswl](../literature.d/LIT-tmp7lswl.md)), as A11 cites it, is why no single
   reported effect can be assumed robust.
4. **Set the rivals' predictions beside it.** Hilbert's noisy-processing
   model ([LIT-tmpngp4x](../literature.d/LIT-tmpngp4x.md)) predicts co-variation under manipulations of noise
   or memory load; resource-rational analysis ([THEORY-359](../theory.d/THEORY-359.md)) under
   manipulations of time or computational cost. The claim predicts it under
   the significance manipulation with those held fixed.
5. **Extend [CASE-148](../cases.d/CASE-148.md)**, the proposed perspective-transplantation study, for
   the "transferable" part of A11's strongest result.

## What it would settle

Whether [CLAIM-tmp5atd3](../claims.d/CLAIM-tmp5atd3.md) is more than a redescription. A null under step 4's
conditions meets its `defeated_if`.
