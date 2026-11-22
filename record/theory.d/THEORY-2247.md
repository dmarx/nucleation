---
number: 2247
status: Proposed
formerly:
- THEORY-tmpcdxvd
promote_when: >-
  The boundary-size bound (eq. 24) is rederived from the stability
  condition, and a numerical check on a ring of n-cells finds stable
  phase-locked states with nonzero winding only when the boundary has five
  or more cells.
title: 'Bačić and colleagues show that the phase-locked states of the topological Kuramoto model on a cell complex are the solutions of linear balance conditions that also meet nonlinear cycle conditions, sums of inverse sines around each independent cycle equal to 2π times a winding number, and that because a stable phase difference is below π/2 in size, coexisting stable states with nonzero winding need a boundary of at least five cells'
version: 1
tags:
- network-science
- mathematics
- complex-systems
date: '2026-11-22'
source:
- LIT-2253
summary: >-
  From the reading of [LIT-2253](../literature.d/LIT-2253.md) in [NOTE-2338](../notes.d/NOTE-2338.md), for [LEAD-023](../leads.d/LEAD-023.md). The
  unfrustrated, higher-order counterpart of the record's cycle-consistency
  results. Proposed until its promote_when is met.
---

# THEORY-2247: Bačić and colleagues show that the phase-locked states of the topological Kuramoto model on a cell complex are the solutions of linear balance conditions that also meet nonlinear cycle conditions, sums of inverse sines around each independent cycle equal to 2π times a winding number, and that because a stable phase difference is below π/2 in size, coexisting stable states with nonzero winding need a boundary of at least five cells

## Source

Bačić, Schaub, Kurths and Witthaut (2026), [LIT-2253](../literature.d/LIT-2253.md), read in [NOTE-2338](../notes.d/NOTE-2338.md).

## What was actually shown

A derivation, with an algorithm: write the stationary conditions in the
sines of the interaction variables, where they are linear; parametrize the
solutions by circulating flows on the independent cycles; keep those whose
inverse sines sum around each cycle to 2πz. Stability of the states with
all differences on the increasing branch is proved. Rings, Platonic solids
and simplices are worked, the bound of five checked against them.

## What this does not say

Anything about couplings with phase offsets (frustration), noise, or which
state a trajectory reaches. Five cells are necessary for multistability,
not sufficient.
