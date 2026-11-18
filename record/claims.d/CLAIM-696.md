---
number: 696
status: Proposed
formerly:
- CLAIM-tmp7jyur
title: 'A mode can bear explanatory weight in a learned network only if it is defined invariantly under the network''s function-preserving symmetries, permutations of hidden units and the reparametrizations its architecture allows; a spectrum over the index order of units fails that test, while the Fourier characters of a task''s group pass it, because the task supplies them'
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  A mode defined over a network's arbitrary unit order that nonetheless
  predicts held-out behavior or intervention effects consistently across
  every function-preserving reordering, so that the invariance demand is
  not needed; or a reading of CLAIM-698's "independently justified
  modes" that already states this test, so that this claim only restates
  it.
tags:
- learning-theory
- representation-learning
- mathematics
date: '2026-11-15'
line:
- learned-structure
- formal-apparatus
complements:
- CLAIM-698
- CLAIM-148
grounds:
- CASE-270
summary: >-
  The assistant's admission rule for the owner's hypothesis that wave
  mathematics applies to learning ([CLAIM-698](CLAIM-698.md)), offered at the end of
  the filing of 2026-11-15 and filed at the owner's request. [CLAIM-698](CLAIM-698.md)
  asks for "independently justified" modes; this says what the
  justification must include. [CASE-270](../cases.d/CASE-270.md) shows a FREE-Merging-style
  spectrum moving under a permutation that leaves the function unchanged.
  Fourier characters of ℤ/p in [THEORY-022](../theory.d/THEORY-022.md) are invariant because the task's
  group defines them, not the units' order. It is the spectral case of
  [CLAIM-148](CLAIM-148.md)'s point that a factorization is identified only up to a change
  of latent coordinates. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-698 CASE-270 THEORY-022 THEORY-1872 — Proposed or new; the claim this sharpens, its construction, and the readings it contrasts -->

# CLAIM-696: A mode can bear explanatory weight in a learned network only if it is defined invariantly under the network's function-preserving symmetries, permutations of hidden units and the reparametrizations its architecture allows; a spectrum over the index order of units fails that test, while the Fourier characters of a task's group pass it, because the task supplies them

## The rule

A learned network has symmetries that leave its function unchanged. Its
hidden units can be permuted, and some architectures allow rescalings or
rotations. A quantity that changes under them describes the coordinates,
not the network. So a mode, a spectrum or a coupling can carry explanatory
weight in [CLAIM-698](CLAIM-698.md)'s sense only if it is defined invariantly under
those symmetries. Equivalently, it must be defined by something the
symmetries respect: the task's group, the data distribution, or the
function's operators (Jacobians, kernels, response maps), with basis
choices fixed only up to the symmetries.

## Why

- **Failure.** In [CASE-270](../cases.d/CASE-270.md), a FREE-Merging-style spectrum ([THEORY-1872](../theory.d/THEORY-1872.md))
  falls from a 0.985 low-frequency share to 0.193 under a permutation that
  leaves the outputs unchanged.
- **Success.** The modular-addition network's Fourier characters
  ([THEORY-022](../theory.d/THEORY-022.md)) are defined by ℤ/p acting on the inputs. Relabeling hidden
  units leaves them where they are.
- **The general point.** [CLAIM-148](CLAIM-148.md) makes it for factorizations: a latent
  basis is identified only up to an invertible change of coordinates.
  Spectral talk inherits the same ambiguity unless it is tied to something
  invariant.

## What it does not say

- **That basis-dependent methods are useless.** They may work in practice
  in a fixed coordinate system. They cannot be the explanation the
  hypothesis offers.
- **That invariance suffices.** An invariant mode must still out-predict
  static accounts, as [CLAIM-698](CLAIM-698.md) requires.
