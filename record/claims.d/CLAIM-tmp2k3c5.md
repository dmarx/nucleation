---
status: Proposed
title: If practice must stay within ε of a governing reference that can be
  revised at most at rate v, a demand to bring practice within δ of a target
  at distance 1 by deadline H can be met only if vH ≥ 1 − δ − ε, so the same
  rate of revision is adequate to a demand with a long horizon and inadequate
  to one with a short horizon, and a fixed reference (v = 0) meets no demand
  farther than δ + ε
version: 1
role: thesis
warrant: demonstrated
defeated_if: An error in the derivation. As a model it is defeated as a reading
  of organizations only by the finding that the coupling of practice to a
  slowly revisable reference misdescribes how identity stabilization constrains
  them; that is a question for CLAIM-tmph25dl, which uses it.
tags:
- control-theory
- society-and-governance
- mathematics
date: '2026-11-22'
line:
- realizability
- will-organization
summary: 'A38 §4 of the exchange "Explain First Contact RL" (ChatGPT, second
  share of 2026-11-22): a toy model of the identity–adaptation tension, with
  x(0) = z(0) = 0, |x − z| ≤ ε, |ż| ≤ v, and a demand |x(H) − 1| ≤ δ. Its
  necessary condition is vH ≥ (1 − δ − ε)₊. Checked by the assistant: the
  bound is necessary, not sufficient, and is tight when the practice can track
  freely within its band. The wording is A''s (ChatGPT, in the exchange of
  2026-11-22); adopting it is the owner''s call.'
---

# CLAIM-tmp2k3c5: If practice must stay within ε of a governing reference that can be revised at most at rate v, a demand to bring practice within δ of a target at distance 1 by deadline H can be met only if vH ≥ 1 − δ − ε, so the same rate of revision is adequate to a demand with a long horizon and inadequate to one with a short horizon, and a fixed reference (v = 0) meets no demand farther than δ + ε

## Derivation

The demand needs x(H) ≥ 1 − δ. The band gives x(H) ≤ z(H) + ε, so z(H) ≥
1 − δ − ε. The rate bound with z(0) = 0 gives z(H) ≤ vH. Hence vH ≥
1 − δ − ε, and the condition holds trivially when 1 − δ − ε ≤ 0. With
v = 0 the reference stays at 0, x(H) ≤ ε, and the demand fails whenever
1 − δ > ε. A38 adds, rightly, that the bound is necessary, and sufficient
only if the practice itself can move fast enough within the band. It is
then tight: set ż = v until z = 1 − δ − ε, and keep x = z + ε.

## What it shows

A38: "the same organizational constraint can be appropriate for one
demand horizon and inadequate for another", and change through a
maintained revision procedure (changing z, keeping the relation between x
and z) lets "Identity … persist through regulated transformation". The
model does not show that larger v is better: it says nothing of what a
fast-revisable reference costs against transient fluctuations, which is
the other half of A38's tension.
