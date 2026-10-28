---
number: 334
status: Active
formerly:
- CLAIM-tmpa4kr6
title: 'Granger causation from a macro variable to the micro variables it supervenes on, Seth''s downward Granger causation, is not evidence of a macro-to-micro intervention effect, even with every micro variable measured: supervenience leaves no intervention on the macro variable that holds its micro base fixed at the same time'
version: 1
role: disclaimed
warrant: demonstrated
tags:
- causality
- complex-systems
date: '2026-10-16'
line:
- formal-apparatus
rests_on:
- CLAIM-333
grounds:
- LIT-1170
- THEORY-704
uses:
- TERM-058
summary: >-
  Seth measures downward causation as Granger causation from the flock's
  centre of mass to each boid, and calls it "ontologically innocent"
  ([THEORY-703](../theory.d/THEORY-703.md)). The record files the boundary so that the stronger
  reading has an address. If M(t) = f(m(t)), setting M(t) means changing
  m(t), so the intervention Eichler and Didelez's Assumption 2.3(i)
  requires does not exist ([THEORY-704](../theory.d/THEORY-704.md)). Measuring every boid does not
  help, by [CLAIM-333](CLAIM-333.md).
---

# CLAIM-334: Granger causation from a macro variable to the micro variables it supervenes on, Seth's downward Granger causation, is not evidence of a macro-to-micro intervention effect, even with every micro variable measured: supervenience leaves no intervention on the macro variable that holds its micro base fixed at the same time

## The claim

Let M(t) = f(m(t)) for a macro variable M and micro variables m, as
Seth's centre of mass is a function of the boids' positions at the same
time ([NOTE-935](../notes.d/NOTE-935.md), §4). Eichler and Didelez define an effect of M only
for an intervention σ_M(t) independent of the other components at t,
m(t) among them (Assumption 2.3(i), [THEORY-704](../theory.d/THEORY-704.md)). Under
supervenience, any change to M(t) is a change to m(t). So σ_M(t) cannot
satisfy (i), and "the effect of M on m" in their sense is undefined, not
zero.

What Granger causation from M to mᵢ does show is predictive, as
[TERM-058](../terms.d/TERM-058.md) defines it: M's past
improves the prediction of mᵢ beyond the past of the other variables in
the regression. In a linear regression this can happen when f is
nonlinear and the regression cannot form f(m(t − 1)) from the m's pasts.
Seth's preprocessing makes f nonlinear ([NOTE-935](../notes.d/NOTE-935.md), Limitations).
That is a fact about the predictor, which is what Seth says G-emergence
is relative to (§5.2).

The step from "every micro variable is measured" to "the Granger result is
interventional" is exactly what [CLAIM-333](CLAIM-333.md) denies in general. Here
it fails for a different reason than the sampling step: the
intervention is ruled out by the definition of M, not by the data.

## Why it is filed

Seth claims no more than prediction. The disclaimer is for readers of
the record. [NOTE-726](../notes.d/NOTE-726.md) and [NOTE-791](../notes.d/NOTE-791.md) compare Seth's measure with
Hoel et al.'s and Barnett and Seth's, and [NOTE-010](../notes.d/NOTE-010.md) and [THEORY-497](../theory.d/THEORY-497.md)
discuss downward causation in ΦID. "Downward causation" in Seth's sense
should not be read as the interventional kind when the accounts are
compared.

## What it does not say

- That macro variables cannot have interventional effects in any sense.
  An intervention defined on the micro variables, with M as a summary of
  its effects, is not ruled out. Nor is an account of causation that does
  not require holding the micro base fixed.
- That Seth's measure is wrong. It is a measure of prediction, as stated.
- Anything about ΦID's downward-causation atom D⁽ᵏ⁾, whose interventional
  reading has its own conditions ([NOTE-010](../notes.d/NOTE-010.md), C4).

## Note of 2026-10-27: the edge says what the claim uses

The status review of this date ([ADR-057](../decisions.d/ADR-057.md), [ADR-058](../decisions.d/ADR-058.md)) replaced `grounds: THEORY-703` with Seth's paper itself, [LIT-1170](../literature.d/LIT-1170.md) (read in full in [NOTE-935](../notes.d/NOTE-935.md)). The claim quotes Seth's definitions and label. [THEORY-703](../theory.d/THEORY-703.md)'s contested part, that G-emergence tracks weak emergence, is not used.
