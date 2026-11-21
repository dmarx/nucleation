---
status: Rejected
title: "Wei and colleagues' first integral of the averaged gradient flow near an overlap singularity, read as grounds, shows that gradient flow into a degenerate minimum relaxes algebraically and that slow, power-law-like relaxation in training may be such relaxation"
version: 1
form: evidence
grounds:
- THEORY-tmpg4aat
concludes:
- CLAIM-811
- CLAIM-844
tags:
- learning-theory
- loss-landscapes
date: '2026-11-21'
line:
- learned-structure
summary: >-
  [CLAIM-811](../claims.d/CLAIM-811.md) and [CLAIM-844](../claims.d/CLAIM-844.md) cited [LIT-3000](../literature.d/LIT-3000.md) unread, among the grounds for
  algebraic relaxation near singularities. Read ([NOTE-tmpl89m0](../notes.d/NOTE-tmpl89m0.md)), it derives
  orbits, not time courses: a first integral of the averaged flow, the
  stability of a line of overlapping units, and two plateaus, one a
  noise-driven random walk along that line, the other a crossing where the
  loss changes at fourth order. No rate, power law or relaxation exponent
  appears. Rejected as a ground of either claim; [LIT-3000](../literature.d/LIT-3000.md) leaves their
  grounds. The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
  Standing of the conclusions apart from this route: [CLAIM-811](../claims.d/CLAIM-811.md)'s
  algebraic relaxation stands on its own derivation and is corroborated by
  Amari, Park and Ozeki's Eq. 5.13 ([ARG-tmp1klwj](ARG-tmp1klwj.md)); [CLAIM-844](../claims.d/CLAIM-844.md)'s reading of
  training's slow modes is A's supposition, held in that claim, and Wei
  and colleagues' walk on a line is a rival to it, held in
  [THEORY-tmpg4aat](../theory.d/THEORY-tmpg4aat.md) ([ADR-136](../decisions.d/ADR-136.md)).
---
<!-- inactive-ok-file: CLAIM-811 CLAIM-844 THEORY-tmpg4aat ARG-tmp1klwj — Proposed; filed 2026-11-21 from the exchange "Rich Get Richer Power Laws" or from these readings -->

# ARG-tmp0cg6w: Wei and colleagues' first integral of the averaged gradient flow near an overlap singularity, read as grounds, shows that gradient flow into a degenerate minimum relaxes algebraically and that slow, power-law-like relaxation in training may be such relaxation

## The inference

As the two claims cited it: Wei and colleagues analyse learning near
singularities and its plateaus ([LIT-3000](../literature.d/LIT-3000.md)), so they ground the algebraic
relaxation of a degenerate direction ([CLAIM-811](../claims.d/CLAIM-811.md)) and the reading of slow
training as a collection of such relaxations ([CLAIM-844](../claims.d/CLAIM-844.md)).

## Critical questions

- **Does the source state what it is cited for?** No. [THEORY-tmpg4aat](../theory.d/THEORY-tmpg4aat.md)
  derives a conserved quantity of the averaged flow (Eq. 3.10) and the
  orbits it fixes, not how fast an orbit is traversed. The paper's word
  "algebraic" is used only of the singularities themselves and in
  reference titles; no t-scaling appears. Of the on-singularity plateau's
  length it says only that "it might take a long time for the system to
  escape the singularity".
- **Is its slowness of the claimed kind?** No. The long plateau is "a long
  period of random walk on R∗1", with "Ė(ξ) = 0 on average", driven by "the
  fluctuations due to the noise and the random sampling of input": noise
  moving the state along a line of models that compute the same function,
  not a degenerate direction decaying. The near-singularity plateau is a
  small gradient, Ė of order u⁴, at a crossing, also with no derived time
  course.
- **Does it bear on the claims at all?** Yes, otherwise. It parallels
  [CLAIM-811](../claims.d/CLAIM-811.md)'s qualification: a conserved quantity (C against C₀) decides
  whether the flow reaches the more singular set, and "in most cases" it
  reaches the elimination singularity instead, where an output weight is
  zero, as an off-balance flow on a²b² ends at b = 0. That is an analogy
  across different models and earns a dated note, not a ground. For
  [CLAIM-844](../claims.d/CLAIM-844.md) it is a rival: slow training from noise-driven escape along a
  flat line, beside criticality and algebraic relaxation.

## Verdict

Rejected as a ground of either claim. [LIT-3000](../literature.d/LIT-3000.md) is removed from both
claims' grounds; its bearing is recorded in dated notes on each.
