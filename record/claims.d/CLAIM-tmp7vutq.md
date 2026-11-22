---
status: Proposed
title: 'On a cycle of five or more contexts with zero monodromy, the XY energy has stable twisted local minima of positive energy, so a local minimization of it can report an obstruction that is not there; on three or four contexts every local minimum is a global one'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  A twisted state of winding 1 on an l-cycle with zero offsets and l ≥ 5
  is shown not to be a strict local minimum of D(θ) = Σ[1 − cos(θ_j − θ_i
  − α_ij)], or a cycle of three or four contexts with zero monodromy is
  shown to have a local minimum of positive energy.
tags:
- mathematics
- network-science
date: '2026-11-22'
line:
- distributed-agency
- formal-apparatus
grounds:
- THEORY-tmpcdxvd
summary: >-
  A qualification of CLAIM-153's readout, from the reading of Bačić and
  colleagues (LIT-2253) for LEAD-023. CLAIM-153 says the frustrated XY
  energy finds the obstruction because its minimum is 0 exactly when the
  monodromy vanishes. That is the global minimum. On a cycle of l ≥ 5
  contexts with zero monodromy, the twisted state of winding 1, every
  offset 2π/l, is a stable fixed point with energy l(1 − cos 2π/l) > 0; a
  local search can stop there. Below five no such state is stable. The
  wording is the assistant's (Claude, in this session); adopting it is the
  owner's call.
---
<!-- inactive-ok-file: THEORY-tmpcdxvd THEORY-tmpnlu47 — Proposed; the readings this claim rests on, filed with it -->

# CLAIM-tmp7vutq: On a cycle of five or more contexts with zero monodromy, the XY energy has stable twisted local minima of positive energy, so a local minimization of it can report an obstruction that is not there; on three or four contexts every local minimum is a global one

## The claim

Take CLAIM-153's energy on an l-cycle, D(θ) = Σᵢ [1 − cos(θᵢ₊₁ − θᵢ −
αᵢ)], with zero monodromy (all αᵢ = 0, no loss of generality, since a
gauge change removes any offsets that sum to zero). Its global minimum is
0, at the coherent configuration, as CLAIM-153 says. But the twisted state
θᵢ = 2πiz/l is also a fixed point, with every edge difference 2πz/l. The
Hessian of D on the cycle is a weighted Laplacian with edge weights
cos(θᵢ₊₁ − θᵢ), so the twisted state is a strict local minimum (up to the
global rotation) when cos(2πz/l) > 0, that is when l > 4|z|. For z = 1 that
is l ≥ 5, with energy l(1 − cos(2π/l)) > 0. At l = 4 the edges sit at π/2
and the state is marginal; at l = 3 it is a maximum along some direction.
So for l ≤ 4 every stable configuration with zero monodromy has energy 0.

This is Bačić and colleagues' bound of five (THEORY-tmpcdxvd), from the
phase-budget argument "at least five contributions are required to realize
nontrivial winding", read off for the energy CLAIM-153 uses. Manik, Timme and Witthaut
(THEORY-tmpnlu47) give the graph case directly: "ring networks RN with N ≤
4 do not have multiple stable fixed points".

**Check** (scratch/studies/lead-023/twisted.py, with its test). Gradient
descent on D from 60 random starts with zero offsets ended at energy 0
every time on 3- and 4-cycles, and in a twisted state of positive energy
on 4 of 60 starts at l = 5 (energy 3.455), 10 of 60 at l = 6 (3.0) and 19
of 60 at l = 8 (2.343).

## What it changes

CLAIM-153's readout "its minimum is 0 exactly when Φ ≡ 0" stands for the
global minimum. A computation that reads the obstruction from a minimized
energy needs either a global method or a check of the winding: a positive
energy reached by local descent, on a cycle of five or more contexts, is
an obstruction only if the winding of the reached state does not account
for it. The reader's rerun on the triangle (note of 2026-11-07 on
CLAIM-153) is safe, being below five. It also bears on CLAIM-153's open
point about refining covers: refining a three-context loop into six both
redistributes the frustration and admits twisted local minima that the
coarse cover did not have.

## What it does not say

That twisted states occur in the frustrated case in the same way: with
offsets the stable windings shift with Φ, which is not worked here. Nor
anything about nonabelian targets. The model of contexts is CLAIM-153's;
whether selves relax by local descent is not argued.
