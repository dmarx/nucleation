---
status: Open
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
- CLAIM-tmpf71gk
- CLAIM-tmpg8yl2
summary: The computational study the manuscript governance-of-possibility proposes
  at A48 §9.6, without a design, built on the simulator LEAD-080 already ran (CASE-315).
  The wording is the assistant's (Claude, in this session); adopting it is the owner's
  call.
---

<!-- inactive-ok-file: CLAIM-tmpf71gk CLAIM-tmpg8yl2 CASE-315 — Proposed; what this advances and builds on -->

# LEAD-tmpnblsf: Extend the readiness simulator with a redesign arm, a sweep of reserve sizes between holding cost and threshold, and a harm absent from the demand specification introduced mid-run

## The design

Start from LEAD-080's simulator (CASE-315), which compares the
spend-matching budget rule with carry-over. Add three arms:

1. **Redesign.** A second transition path with a lower threshold, at an
   upfront cost, under spend-matching, with and without a reserve. The
   prediction from CLAIM-tmpg8yl2: without a reserve it is lost after one
   period unless its threshold is at most the holding cost.
2. **Reserve sweep.** Reserve levels between the holding cost and the
   threshold, scoring readiness against reserve cost; the break-even is a
   contingency's probability times its loss against the reserve's cost per
   period, which A48 leaves open (QUESTION-395).
3. **A harm absent from the specification.** A demand introduced mid-run
   that the specification did not name, scoring whether the regime revises
   its specification or excises the demand (CLAIM-361's distinction).

Report readiness curves over the deadline (TERM-115), reserve cost, and
which regime ranks first at which deadlines.
