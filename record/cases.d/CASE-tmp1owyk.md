---
status: Proposed
title: 'A spectrum taken over a weight matrix''s unit order is not a property of the network: permuting the hidden units of a two-layer network leaves its outputs unchanged and moves the low-frequency share of a task update''s two-dimensional Fourier energy along the hidden-unit axis from 0.985 to 0.193, while the update''s singular values stay fixed'
version: 1
standing: stipulated
kind: construction
tags:
- learning-theory
- mathematics
date: '2026-11-15'
line:
- learned-structure
draws_on:
- THEORY-tmp3lla6
illustrates:
- CLAIM-tmp7jyur
summary: >-
  The assistant's construction, built when the owner asked for the
  assistant's own ideas from the filing of 2026-11-15 to be filed
  (scratch/formal/permutation_spectrum_check.py, run on filing). It tests
  the kind of quantity FREE-Merging uses ([THEORY-tmp3lla6](../theory.d/THEORY-tmp3lla6.md)): the Fourier
  spectrum of a task-update matrix over its row and column order. The
  wording is the assistant's (Claude, in this session); adopting it is the
  owner's call.
---
<!-- inactive-ok-file: THEORY-tmp3lla6 CLAIM-tmpumro8 — Proposed or new; the reading the construction tests and the claims it serves -->

# CASE-tmp1owyk: A spectrum taken over a weight matrix's unit order is not a property of the network

## The construction

The network is f(X) = W₂·relu(W₁X), with 16 inputs, 32 hidden units and 8
outputs. Its first layer is fine-tuned by a smooth update ΔW₁, whose
profile along the hidden units is cos(2πi/32), plus small noise. A
permutation P of the hidden units maps (W₁, W₂) to (PW₁, W₂Pᵀ). The outputs
are identical on 200 random inputs, so it is the same function.

The update in the permuted coordinates is PΔW₁. Take the share of the 2-D
Fourier energy at the three lowest frequencies along the hidden-unit axis.
It is 0.985 in the original order and 0.193 after the permutation. The
singular values of the update, a quantity of the function up to the
symmetry, are unchanged. The one spectral quantity that survives is zero
frequency along the permuted axis, a sum, which does not depend on order.

## What it shows

A "frequency" defined over the arbitrary index order of a network's units
measures the coordinates, not the network. Two descriptions of one network
can disagree about it completely. This is the failure [CLAIM-tmpumro8](../claims.d/CLAIM-tmpumro8.md) says
its modes must avoid, made concrete.

## What it cannot show

That FREE-Merging does not work. A filter tuned in one fixed unit order can
still help a merge empirically. The construction shows only that its
spectrum cannot be the reason in any sense invariant to the network's
symmetries.
