---
number: 226
status: Open
formerly:
- LEAD-tmpnblsf
title: Extend the readiness simulator with a redesign arm, a sweep of reserve sizes
  between holding cost and threshold, and a harm absent from the demand specification
  introduced mid-run
version: 1
stage: idea
priority: medium
method:
- empirical
tags:
- operations-research
- society-and-governance
date: '2026-11-23'
line:
- readiness
advances:
- QUESTION-395
- CLAIM-1093
- CLAIM-1099
operationalized_in:
- CASE-412
- CASE-397
summary: The computational study the manuscript governance-of-possibility proposes
  at A48 §9.6, without a design, built on the simulator [LEAD-080](LEAD-080.md) already ran ([CASE-315](../cases.d/CASE-315.md)).
  The wording is the assistant's (Claude, in this session); adopting it is the owner's
  call.
---

# LEAD-226: Extend the readiness simulator with a redesign arm, a sweep of reserve sizes between holding cost and threshold, and a harm absent from the demand specification introduced mid-run

## The design

Start from [LEAD-080](LEAD-080.md)'s simulator ([CASE-315](../cases.d/CASE-315.md)), which compares the
spend-matching budget rule with carry-over. Add three arms:

1. **Redesign.** A second transition path with a lower threshold, at an
   upfront cost, under spend-matching, with and without a reserve. The
   prediction from [CLAIM-1099](../claims.d/CLAIM-1099.md): without a reserve it is lost after one
   period unless its threshold is at most the holding cost.
2. **Reserve sweep.** Reserve levels between the holding cost and the
   threshold, scoring readiness against reserve cost; the break-even is a
   contingency's probability times its loss against the reserve's cost per
   period, which A48 leaves open ([QUESTION-395](../questions.d/QUESTION-395.md)).
3. **A harm absent from the specification.** A demand introduced mid-run
   that the specification did not name, scoring whether the regime revises
   its specification or excises the demand ([CLAIM-361](../claims.d/CLAIM-361.md)'s distinction).

Report readiness curves over the deadline ([TERM-115](../terms.d/TERM-115.md)), reserve cost, and
which regime ranks first at which deadlines.

## Note of 2026-11-23: the study filed

The design was run for the manuscript governance-of-possibility (scratch/manuscripts/governance-of-possibility/analysis/, at commit 28a3708c1, reproduced) and is filed as two cases, named in `operationalized_in`: [CASE-412](../cases.d/CASE-412.md) holds the redesign arm and the reserve sweep, with readiness curves, reserve cost and the ranking by deadline, and [CASE-397](../cases.d/CASE-397.md) holds the harm absent from the specification. The redesign's cost is reported as a break-even rather than charged up front; whether the lead is done is the owner's call. The note is the assistant's (Claude, in this session); adopting it is the owner's call.

## Note of 2026-11-25: the policy learned, from the manuscript governance-of-becoming, Article 6

This lead's third item was run as [CASE-397](../cases.d/CASE-397.md), which says of itself "The
policy is an input": "Nothing in the model makes the choice between
excising and revising." The manuscript's Article 6 (§6.10, G6.1) names the
missing run, an institution whose choice to excise is learned, as in
[CASE-396](../cases.d/CASE-396.md), scored against the original, its own and the true demands, as in
[CASE-397](../cases.d/CASE-397.md) (the audit of what was left out (2026-11-25), B12). It is held as [LEAD-tmpv3s18](LEAD-tmpv3s18.md), kept apart from this lead
since this lead's arms are done. No change of status. The wording is the assistant's (Claude, in this session); adopting it is the owner's call.
