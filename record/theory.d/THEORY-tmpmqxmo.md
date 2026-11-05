---
status: Proposed
promote_when: >-
  The Tachi–Hull self-foldability criterion and the mode count checked,
  for example in the J. Mech. Robot. paper or by computing the folding
  modes at the flat state of the Miura-ori, the Chicken Wire pattern and a
  generic quadrilateral tiling rotationally symmetric about its tile's
  side midpoints, showing that the first two admit no crease-separable
  driving force that selects one mode and the third does.
title: 'Hull and Tachi show that the Miura-ori and Chicken Wire origami tessellations cannot be uniquely self-folded by crease-local driving forces, while generic quadrilateral tessellations rotationally symmetric about the midpoints of the tile''s sides, which have only two folding modes, can be'
version: 1
tags:
- mathematics
- control-theory
date: '2026-11-05'
source:
- LIT-tmp6aj47
summary: >-
  Hull and Tachi (2018), LIT-tmp6aj47, read in full in NOTE-tmpryygx (arXiv
  v1). Proposed: the theorems were read with their proofs, which rest on
  the authors' 2016 criteria, not checked here. It does not say anything
  about stiffness, bending energy or noisy actuators, which the model
  leaves out, or about tessellations beyond monohedral quadrilateral ones.
---

# THEORY-tmpmqxmo: Hull and Tachi show that the Miura-ori and Chicken Wire origami tessellations cannot be uniquely self-folded by crease-local driving forces, while generic quadrilateral tessellations rotationally symmetric about the midpoints of the tile's sides, which have only two folding modes, can be

## Source

Hull and Tachi (2018), LIT-tmp6aj47; read in NOTE-tmpryygx.

## What was actually shown

- **The model** (§2): a driving force is a crease-separable vector field
  with positive forward force along the intended path; a path is uniquely
  self-foldable when it is the only one the field drives.
- **Criteria** (Theorems 2 and 4): a driving force needs the tangent space
  at flat to exceed the span of the wrong-mode tangents; for a
  one-degree-of-freedom path it exists exactly when the path's tangent is
  outside that span.
- **Tessellations** (Theorem 5): the Miura-ori (parallelogram tile) and
  the Chicken Wire pattern (isosceles trapezoid) are not uniquely
  self-foldable; rotationally symmetric tilings with a generic tile, flat-
  foldable or not, have a driving force that makes the folding uniquely
  self-foldable. The reason given: generic tiles give only two folding
  modes.

## What this does not say

- That the driving force is robust to actuator error, stiffness or bending
  energy; the model has none of these.
- Anything about tessellations other than monohedral quadrilateral ones.
- How to construct the driving force in practice.
