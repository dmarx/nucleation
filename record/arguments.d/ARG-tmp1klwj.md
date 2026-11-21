---
status: Proposed
title: "Amari, Park and Ozeki's cubic gradient along the degenerate direction of a gaussian mixture whose truth lies on the singularity, as an instance in a real model, supports the claim that gradient flow into a degenerate minimum relaxes algebraically, and its approach at a generic point of the critical set parallels the claim's qualification"
version: 1
form: evidence
grounds:
- THEORY-tmpbobud
concludes:
- CLAIM-811
tags:
- learning-theory
- loss-landscapes
date: '2026-11-21'
line:
- learned-structure
- formal-apparatus
summary: >-
  CLAIM-811 is demonstrated by its own derivation and cited LIT-2960
  unread. Read (NOTE-tmptlwkf), the paper's Eq. 5.13 gives u̇ = −ηc₂²u³
  with v̇ of order u⁴: the claim's quartic case, k = 2, so u ∝ t^(−1/2)
  (the reader's derivation; the paper states no rate), and the flow
  reaches the critical set "without significantly changing v", at a
  generic point. Independent evidence the claim does not need, so the
  reading corroborates it and leaves its grounds. Silent on the learning
  coefficient. The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-811 THEORY-tmpbobud CLAIM-844 — Proposed; filed 2026-11-21 from the exchange "Rich Get Richer Power Laws" or from this reading -->

# ARG-tmp1klwj: Amari, Park and Ozeki's cubic gradient along the degenerate direction of a gaussian mixture whose truth lies on the singularity, as an instance in a real model, supports the claim that gradient flow into a degenerate minimum relaxes algebraically, and its approach at a generic point of the critical set parallels the claim's qualification

## The inference

CLAIM-811: on K = v⁴, v̇ = −4v³ and |v| ∝ t^(−1/2); in general
x ∝ t^(−1/(2k−2)) on the balanced line of a k-fold product. THEORY-tmpbobud,
§5.3, Case I (truth at the singularity, u* = 0), Eq. 5.13:
u̇ = −ηc₂(v)²u³, v̇ = −η(c₂c₂′/2)u⁴. The filer's check: u̇ = −au³ integrates
to u(t) = u₀/√(1 + 2au₀²t), so u ∝ t^(−1/2) for t ≫ 1/(au₀²), the claim's
k = 2 rate.

## Critical questions

- **Is it the same law?** The local form is: a gradient cubic in the
  degenerate coordinate, from a loss quartic in it. The paper's model is a
  mixture of two gaussians, not a product loss, so the instance is of the
  first part's law (algebraic relaxation into a degenerate minimum), not of
  the k-fold construction.
- **Does it meet the qualification?** In parallel. CLAIM-811's
  qualification has off-balance flows reaching a generic point of the
  zero set; here "u converges to 0 without significantly changing v", and
  the flow "entering C is extremely slow near C, the flow component
  parallel to C is relatively strong" (p. 1034). Different models, the same
  shape: the flow reaches the critical set where it meets it, not at its
  most degenerate point.
- **Is it what the paper is about?** Only partly. Its plateau is chiefly
  the regular-truth case, attraction to the critical set and slow escape,
  not relaxation into a singular optimum (CLAIM-844's note).
- **The second part.** The paper does not compute learning coefficients,
  so it is silent on whether slowing and the coefficient part ways.

## Verdict

Supports the first part as an instance in a real model, independent of
the claim's derivation; corroborates, and is not a ground. Proposed.
