---
number: 368
status: Proposed
formerly:
- CASE-tmpqg5fa
title: 'Operational cover as determinacy sub-cover'
statement: >-
  The operational cover as the determinacy sub-cover of a measurement
  scenario
version: 1
standing: stipulated
kind: construction
tags:
- mathematics
- contextuality
date: '2026-11-22'
line:
- pragmatic-transport
- formal-apparatus
draws_on:
- THEORY-012
bears_on:
- QUESTION-005
---
<!-- inactive-ok-file: CLAIM-201 CLAIM-251 — Proposed; the thesis and its counter this construction is built to adjudicate -->
<!-- inactive-ok-file: CLAIM-961 CLAIM-962 — new in this contribution; the two alternative readings this case grounds and the term it uses -->

# CASE-368: Operational cover as determinacy sub-cover

## The case

A formal construction, built to adjudicate [CLAIM-251](../claims.d/CLAIM-251.md)'s objection to
[CLAIM-201](../claims.d/CLAIM-201.md): is the "operational cover" (a context = a question a
receiver population answers determinately) a cover with restriction maps in
the sheaf sense ([THEORY-012](../theory.d/THEORY-012.md), [LIT-016](../literature.d/LIT-016.md); the communicative object of
[TERM-042](../terms.d/TERM-042.md))?

Fix a measurement scenario (X, M, O): measurements X, a cover M of maximal
jointly-performable contexts (subsets of X whose union is X), outcomes O. The
event presheaf is ℰ(U) = ∏_(x∈U) O_x, with restriction ℰ(U) → ℰ(V) for
V ⊆ U given by dropping the coordinates outside V; on distributions this is
marginalization. An empirical model e assigns each context C ∈ M a
distribution e_C over ℰ(C), no-signalling when the e_C agree on shared
marginals.

[CLAIM-201](../claims.d/CLAIM-201.md)'s determinacy is made precise as a functional of e. For a
single measurement x, with marginal m_x,

  det_θ(e, x) = [ max_o m_x(o) ≥ θ ],   θ a threshold fixed in advance.

The **operational cover** is then the determinable base D = K_θ(e) =
{x ∈ X : det_θ(e, x)}, carrying the **induced sub-scenario** (D, M|_D, O)
with M|_D = {C ∩ D : C ∈ M, nonempty} and the restriction maps inherited
from ℰ.

The worked scenario is X = {a, b, c}, O binary, M = {{a, b}, {b, c}}
(overlap {b}). The study is `scratch/studies/lead-111/` (numpy, pytest, ten
tests passing).

## What it can show

Four facts, each checked numerically (`test_operational_cover.py`), bear the
weight; its standing is stipulated, so the scenario is chosen, not observed,
and the facts are the construction's properties, not an empirical finding.

1. **The restriction maps are a presheaf.** res^U_U = id and
   res^U_V ∘ res^W_U = res^W_V for V ⊆ U ⊆ W, and each map carries a
   distribution to a distribution. The scenario has genuine restriction maps.
2. **The induced sub-cover is a genuine down-closed cover.** The induced
   contexts M|_D sit inside D, are closed under restriction, and cover D: a
   sub-site of the scenario with inherited restriction maps. So the operational
   cover **can** be constructed as a family of contexts with restriction maps —
   the lead's first horn, and the sheaf-theoretic relationship
   [CLAIM-251](../claims.d/CLAIM-251.md) asked for. In the worked run D falls from {a, b, c}
   (θ = 0.5) to {a, b} (0.75) to {b} (0.86) to ∅ (0.95), the induced sub-site
   tracking each step (`demo_output.txt`).
3. **The selection is a functional of the empirical model on a fixed cover.**
   Two models on the *same* M give different operational covers. Which
   questions are determinate is a property of the responses e, not of M.
4. **A thresholded readout, not a canonical functor.** K_θ(e) shrinks
   monotonically in θ, and distinct models share a cover at fixed θ
   (non-injective). There is no canonical, parameter-free functor from
   empirical models to covers — only the thresholded readout plus the induced
   sub-site.

Facts 2 and 3 pull opposite ways on [CLAIM-251](../claims.d/CLAIM-251.md), by a modelling choice the
record has not fixed: whether the full set of askable questions is the fixed
scenario (then determinacy is model-level, fact 3) or the determinable
questions are themselves the operational domain (then changing them changes
the domain, i.e. the cover, fact 2). This case grounds both readings,
[CLAIM-961](../claims.d/CLAIM-961.md) and [CLAIM-962](../claims.d/CLAIM-962.md), and the choice between them is the owner's.

The wording is the assistant's (Claude, in this session); adopting it is the
owner's call.
