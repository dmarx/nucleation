---
number: 671
status: Proposed
formerly:
- THEORY-tmpxjvy1
promote_when: >-
  One of two kinds of result. A derivation that holds with nonlinear
  constitutive relations, far from equilibrium where the principle is
  applied, and that says what "sufficient degrees of freedom" means before
  any system is examined. Or prospective tests: systems chosen in advance,
  not because they fit, whose degrees of freedom are specified before their
  steady state is observed, with the MEP state predicted and then found. It
  is refuted by a system that meets the stated condition and settles in a
  steady state of less than maximal entropy production. More fits of
  climate and other box models found after the fact cannot settle it.
  Neither can derivations valid only in the linear regime, where MEP and
  Onsager–Prigogine theory agree, nor a failure explained afterwards as too
  few degrees of freedom.
title: "An open system with enough internal degrees of freedom settles, among its possible steady states, into the one of maximum entropy production; this selects among steady states, where Prigogine's minimum principle only describes relaxation toward one"
version: 1
tags:
- thermodynamics
- complex-systems
date: '2026-10-16'
source:
- LIT-519
- LIT-521
summary: >-
  Kleidon (2009), [LIT-519](../literature.d/LIT-519.md), read in [NOTE-423](../notes.d/NOTE-423.md), states the principle and its
  Earth-system applications; Dewar (2003), [LIT-521](../literature.d/LIT-521.md), read in [NOTE-426](../notes.d/NOTE-426.md), is the
  derivation it cites. The applications are model fits, mostly reported,
  many by the author. The derivation needs a mean-field step and an
  unargued assumption about path counts, and does not reach far from
  equilibrium ([THEORY-676](THEORY-676.md)). "Sufficient degrees of freedom" is never
  made operational, so a failure can always be read as too few. The
  advocate's own verdict: "no one would argue that MEP is well
  established".
presupposed_by:
- THEORY-517
---

<!-- inactive-ok-file: THEORY-412 THEORY-532 THEORY-492 THEORY-517 — Proposed; named as accounts that reject or build on this one, not leaned on -->

# THEORY-671: An open system with enough internal degrees of freedom settles, among its possible steady states, into the one of maximum entropy production; this selects among steady states, where Prigogine's minimum principle only describes relaxation toward one

## Source

Kleidon (2009), *Naturwissenschaften* 96:653–677, [LIT-519](../literature.d/LIT-519.md), read in full in
[NOTE-423](../notes.d/NOTE-423.md) from the open-access article (figure bodies lost, captions kept).
Dewar (2003), *J. Phys. A* 36:631–641, [LIT-521](../literature.d/LIT-521.md), read in full in [NOTE-426](../notes.d/NOTE-426.md)
from arXiv v3, with the equation pages read as images. Martyushev and
Seleznev's review, to which Kleidon defers for MEP's physical foundation,
could not be read.

## What was actually shown

**The principle ([LIT-519](../literature.d/LIT-519.md), p. 655).** "If there are sufficient degrees of
freedom within the system, it will adopt a steady state at which σ is
maximized." "Sufficient" is not defined.

**Against Prigogine ([LIT-519](../literature.d/LIT-519.md), pp. 655–656, 673).** Prigogine's principle
"states that the steady state is one of minimum entropy production compared
to transient states"; once a steady state is assumed it "makes no further
predictions". MEP "acts as a selection principle of the most probable out
of many possible steady states". The two are illustrated with box models
(Figs. 1–2), not stated with their conditions (C1, moderate).

**The flux–force trade-off.** Where a flux depletes the gradient that drives
it, entropy production is zero with no flux and zero with a flux strong
enough to leave no gradient, so there is a maximum between. In a two-box
model with alternative heat-loss paths, σ peaks at an intermediate
conductivity (C2, strong for the existence of the maximum). Dewar's
two-box climate toy has its optimum at h_opt ≈ 0.199 f_SW, which [NOTE-426](../notes.d/NOTE-426.md)
re-derived (0.1991).

**The applications.** Paltridge's climate model and its successors, Mars
and Titan, ocean steady states, mantle convection, evapotranspiration and
sediment decomposition. In general-circulation sensitivity studies entropy
production saturates at a maximum. Each is reported, not reproduced, and
much of it is the author's own model work.

**The derivation ([LIT-521](../literature.d/LIT-521.md)).** Maximize the entropy of the distribution
over microscopic paths under fixed initial densities, fixed boundary fluxes
and local conservation. Then p_Γ ∝ exp(A_Γ), with τσ_Γ/2k_B in the action
(Eq. 14), and a fluctuation theorem and ⟨σ⟩ ≥ 0 follow exactly (Eqs.
18–21). MaxEP follows (Eqs. 22–24) only under a mean-field approximation
and only if W(A^irr), the number of paths with irreversible action A^irr,
increases with A^irr. That is assumed "with no argument or example"
([NOTE-426](../notes.d/NOTE-426.md); C3, weak). For climate, the quantity maximized is material, not
radiative, entropy production (pp. 15–16), which answers Essex's
objection to Paltridge (C4, moderate).

**What could have come out otherwise.** The model fits could have missed,
and the general-circulation runs could have shown no maximum. They did not.
But no test fixed the degrees of freedom first, and the derivation offers
no new prediction checked against data ([NOTE-426](../notes.d/NOTE-426.md)).

## What this does not say

- **That MEP is established.** "At this point, no one would argue that MEP
  is well established and that applications are without their
  limitations" ([LIT-519](../literature.d/LIT-519.md), p. 673). The foundation is "still work in
  progress".
- **That it has been derived far from equilibrium.** Dewar's route needs
  the two assumptions above. His 2005 route, by Grinstein and Linsker's
  analysis, holds only with linear constitutive relations, which is the
  regime where MEP would not differ from linear theory
  ([THEORY-676](THEORY-676.md)). Kleidon's review reports only the critique's second
  point, about self-organized criticality, and leaves out this one
  ([NOTE-423](../notes.d/NOTE-423.md)).
- **That it can fail as stated.** With "sufficient degrees of freedom"
  undefined, a non-MEP steady state can always be put down to too few
  ([NOTE-423](../notes.d/NOTE-423.md)). Dewar's version has the same escape: "When applications of
  the Jaynes procedure fail … [it] signals the presence of new
  constraints" ([LIT-521](../literature.d/LIT-521.md), p. 6).
- **That Prigogine's principle is wrong.** On this literature's own
  account it answers another question. Prigogine's own statement restricts
  the minimum theorem to the strictly linear regime ([LIT-516](../literature.d/LIT-516.md)).
- **That maximum entropy production is Jaynes's maximum entropy
  principle.** The acronyms collide. Dewar derives the one from the other,
  and the cogency of Jaynes's principle as a foundation of statistical
  mechanics is itself unsettled ([LIT-114](../literature.d/LIT-114.md), [NOTE-103](../notes.d/NOTE-103.md)).
- **That it unites maximum power, the constructal law and self-organized
  criticality.** Kleidon asserts it (C7). The link to self-organized
  criticality rests on Dewar's 2003 corollary, which is a mean-field
  artefact.

## Connections

- **The critique ([THEORY-676](THEORY-676.md))** is what blocks this account's
  promotion by derivation.
- **Pattern formation.** Cross and Hohenberg ([LIT-527](../literature.d/LIT-527.md)) find "no evidence
  for the existence of any global minimization principles controlling the
  structure, except as a perturbative statement near threshold". That is a
  claim about minimization functionals for patterns, not about entropy
  production, but it is the physicists' standard caution against the
  programme.
- **The rest of the dissipation literature.** Schneider and Kay
  ([THEORY-532](THEORY-532.md)) and Morowitz and Smith ([THEORY-492](THEORY-492.md)) both reject
  entropy-production principles. Perunov, Marsland and England
  ([THEORY-412](THEORY-412.md)) say maximizing mean dissipation alone "is not predicted
  to correspond to a likely outcome". None of them argues it in a way the
  record can check, so no `rivals` edge is declared.
- **The fluctuation theorems ([THEORY-431](THEORY-431.md)).** Dewar's fluctuation
  theorem has the same form as Crooks's, from an inferred path measure
  rather than a dynamics. The stochastic-thermodynamics framework uses no
  selection principle for steady states.
- **Life and Gaia ([THEORY-517](THEORY-517.md))** takes this account as its premise.

## Note of 2026-10-29: what holds it back

Kept Proposed by the sixteenth status review. [NOTE-423](../notes.d/NOTE-423.md) and [NOTE-426](../notes.d/NOTE-426.md) read
both sources in full, but neither result the promote_when asks for is in
the record. Dewar's derivation needs a mean-field step and an unargued
assumption on path counts, and does not reach the far-from-equilibrium
regime ([THEORY-676](THEORY-676.md), Active). No system has had its degrees of freedom
fixed before its steady state was predicted and found. A split into what
Kleidon proposes would free nothing: [THEORY-517](THEORY-517.md), which presupposes it,
also asks for a planetary test that does not assume MEP.

## Note of 2026-10-31: counterevidence from the Schlögl model

The readings of Vellela and Qian ([LIT-tmpkp8vh](../literature.d/LIT-tmpkp8vh.md)) and of Falasco and
Esposito ([LIT-tmpm46ks](../literature.d/LIT-tmpm46ks.md)) bear against selection by maximum entropy
production:
- in the bistable Schlögl model, the more stable state can carry either
  the higher or the lower entropy production ([THEORY-tmpshz26](THEORY-tmpshz26.md));
- Falasco and Esposito find extremum principles hold only near detailed
  balance or under "peculiar conditions".

A status review should weigh this. Nothing here changes its status.
