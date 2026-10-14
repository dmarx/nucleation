---
number: 77
status: Active
formerly:
- CASE-tmp3djxc
title: 'The reciprocal pair: two processes that endorse only each other under recursive delegation, so that each one''s authority returns to it through the other'
version: 1
standing: stipulated
tags:
- self-governance
- social-ontology
date: '2026-10-13'
line: distributed-agency
illustrates:
- CLAIM-282
summary: >-
  A2 §5's counterexample to the ban on self-endorsement: "Suppose D1
  endorses D2, and D2 endorses D1." Under g = (1 − η)b + ηEᵀg, each
  operator's authority comes partly from its own endorsement returned
  after two hops. It came back in A6 as authority that "may circulate".
  Used to show that a ban on self-endorsement does not make authority
  independent of one's own endorsements.
---

# CASE-077: The reciprocal pair: two processes that endorse only each other under recursive delegation, so that each one's authority returns to it through the other

## The case

A2 §5: "Suppose D1 endorses D2, and D2 endorses D1. Even though neither
endorses itself directly, their reciprocal relationship can recycle
delegated authority between them." Under the damped recursive rule with base
budgets b1 and b2, each endorsing only the other: g1 = (1 − η)b1 + ηg2 and
g2 = (1 − η)b2 + ηg1. So g1 = (b1 + ηb2)/(1 + η). The part of g1 that comes
through g2 includes D1's own contribution, returned. Longer cycles do the
same.

A6 §4 met the same structure across levels. The constituents of a
higher-level operator endorse it, and it delegates back to them. A6 judged
that legitimate, and proposed tracking provenance instead of banning
returns.

## What it can show

That E_ii = 0 is not enough. [CLAIM-282](../claims.d/CLAIM-282.md) generalizes it, and the algebra
above is the check.

## What it cannot show

Whether reciprocal endorsement is collusion or trust. Two processes that are
each reliable may rightly back each other. The case shows only that the
accounting lets their authority depend on their own endorsements.
