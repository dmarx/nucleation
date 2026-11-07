---
status: 'Proposed'
promote_when: >-
  The derivation in Appendix A checked, or the equations verified
  numerically against the closure condition for random degree-4 vertices
  of all three types, together with a check that the two folding modes
  meet only at the flat state of a developable vertex and are disjoint
  when the sector angles do not sum to 2π.
title: 'Foschi, Hull and Ku hold that the two folding modes of a degree-4 rigid origami vertex whose sector angles do not sum to 2π are disconnected, because such a vertex has no state with every folding angle zero'
version: 1
history:
- version: 1
  date: '2026-11-06'
  note: >-
    Filed at the thirtieth status review (ADR-047 kind 1, ADR-065) when
    THEORY-1381 was narrowed to what the paper derives and promoted. This
    is the wider clause the narrowing dropped ("and are disconnected when
    the sector angles do not sum to 2π"), which the paper asserts in §V B.
    It keeps THEORY-1381's version-1 promote_when word for word.
tags:
- mathematics
date: '2026-11-06'
source:
- LIT-2055
extends:
- THEORY-1381
summary: >-
  The wide form of Foschi, Hull and Ku (2022), [LIT-2055](../literature.d/LIT-2055.md), kept here when the
  thirtieth status review narrowed [THEORY-1381](THEORY-1381.md) to what the paper derives
  and promoted it ([ADR-047](../decisions.d/ADR-047.md), kind 1). The paper asserts it in §V B from one
  worked example (Example 1), with no theorem and no stated convention for
  folding angles at ±π. Read in full in [NOTE-1606](../notes.d/NOTE-1606.md).
---

# THEORY-tmp0i15x: Foschi, Hull and Ku hold that the two folding modes of a degree-4 rigid origami vertex whose sector angles do not sum to 2π are disconnected, because such a vertex has no state with every folding angle zero

## Source

Foschi, Hull and Ku (2022), [LIT-2055](../literature.d/LIT-2055.md); read in full in [NOTE-1606](../notes.d/NOTE-1606.md).

## What the paper says

- **Example 1** (§III). The paper perturbs the developable vertex (π/3, π/2, 3π/4, 5π/12) by ∓0.05/(2π) and concludes: "in both the elliptic and hyperbolic cases the configuration spaces are disconnected, whereas in the developable vertex they are connected". Its reason: "it is impossible to unfold the vertex so that all the creases have folding angles of zero at the same time".
- **§V B** generalizes from that example: "non-developable vertices cannot fold to a state where all the folding angles are zero, and therefore, as seen in Example 1 of Section III, the configuration spaces for the two folding modes are disconnected."

## What this does not say

- **No proof.** The main text calls the disconnection something that "makes intuitive sense", and no appendix proves it.
- **No convention for ±π.** The paper does not say whether a crease may pass ±π, which is where the faces pass through each other. The answer to whether the modes are disconnected turns on that.

## Note of 2026-11-06: reader J, the check

Reader J ran a numerical check at the thirtieth status review. It treated the configuration space as a curve on the torus of (ρ1, ρ4), since those two angles fix the whole state. This note rests on scratch/formal/foschi_deg4_monodromy.py and scratch/formal/foschi_deg4_turning.py. **Neither script has been second-checked.** The coarse grid counts in scratch/formal/foschi_deg4_topology.py, which the coordinator re-ran on 2026-11-06, agree for Example 1.

**With angles taken mod 2π** the claim fails in several places:

- Example 1's elliptic perturbation is one connected loop.
- So is the table vertex of §V B.
- So are about half of 80 random rigid-foldable non-Euclidean vertices (17 of 40 elliptic and 14 of 40 hyperbolic).
- In the elliptic example, the two square-root branches join at states well inside (−π, π).

**With every folding angle kept inside (−π, π)**, the claim holds for Example 1: its elliptic and hyperbolic perturbations both keep their popped-up and popped-down pieces apart.

**What holds in general** is only that the modes cannot meet at the flat state.
