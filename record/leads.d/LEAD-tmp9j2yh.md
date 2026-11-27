---
status: Open
title: 'Compare the information in J-space and J-orthogonal components against which consumers follow a swap'
stage: idea
priority: medium
method:
- empirical
- formal
tags:
- consciousness
- information-theory
date: '2026-11-26'
line:
- evidence-for-experience
advances:
- CLAIM-tmpj88da
- THEORY-865
summary: >-
  A test of [CLAIM-tmpj88da](../claims.d/CLAIM-tmpj88da.md)'s content half. The claim says the J-space and
  a J-orthogonal component of a representation can carry the same content,
  differing only in which consumers read it. The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmpj88da — new; the claim this lead would test -->

# LEAD-tmp9j2yh: Compare the information in J-space and J-orthogonal components against which consumers follow a swap

## What it would do

Take a property the model uses both automatically and in report, such as
line width or a part-of-speech label ([NOTE-1069](../notes.d/NOTE-1069.md), pp. 15–16 and §A.12).
For each, split the representation into its J-space component and its
J-orthogonal remainder, as the paper's swaps do. Then:

1. **Estimate a recoding-invariant information measure** of the property
   in each component, with nonlinear probes or a mutual-information
   estimator, so as to separate content from linear readability
   ([THEORY-227](../theory.d/THEORY-227.md)).
2. **Estimate linear decodability** of the property from each component.
3. **Record which consumers follow a swap of each component:** report,
   continuation, and function application.

## What would count

- **For [CLAIM-tmpj88da](../claims.d/CLAIM-tmpj88da.md):** recoding-invariant information is comparable in
  the two components, while the consumers that follow each swap differ.
- **Against it:** the J-orthogonal component carries strictly less
  recoding-invariant information whenever report follows the J-space swap.
  That is its `defeated_if`.

## What it needs

Access to model internals at the scale of the original study, or a
reproduction of the Jacobian lens on an open model. Neither is in hand.
