---
number: 844
status: Proposed
formerly:
- CLAIM-tmpv5asv
title: 'Some of the slow, power-law-like relaxation seen in training deep networks may be the algebraic relaxation of degenerate singular modes rather than critical slowing down in a collective phase, and a dependency tree of feature transitions yields power laws only if its thresholds or relaxation times are themselves broadly or self-similarly distributed'
version: 2
history:
- version: 2
  date: '2026-11-21'
  note: >-
    After the readings of LIT-2960 (NOTE-tmptlwkf) and LIT-3000
    (NOTE-tmpl89m0). LIT-3000 leaves the grounds: it derives orbits, not
    time courses, and has no algebraic relaxation (ARG-tmp0cg6w); its
    on-singularity plateau, a noise-driven walk along a flat line of
    equivalent models, is recorded below as a third rival explanation of
    slow training. LIT-2960 is replaced in the grounds by its reading,
    THEORY-tmpbobud, which qualifies the claim. The claim and its status
    are unchanged.
role: thesis
warrant: interpretive
defeated_if: >-
  For networks whose training shows power-law relaxation, a measurement
  showing that the slow modes are nondegenerate: perturbations along them
  decay exponentially with rates that do not approach zero, and the local
  loss is quadratic along them, so that the slowness comes from a
  continuum of small curvatures or from a diverging correlation length and
  not from higher-order degeneracy. For the second part, a finite
  dependency tree of threshold transitions with narrowly distributed
  thresholds that nonetheless yields scale-free statistics of onset times
  or event sizes.
tags:
- learning-theory
- complex-systems
- loss-landscapes
date: '2026-11-21'
line:
- learned-structure
rests_on:
- CLAIM-811
summary: >-
  A39 §5 and A43 §17 of the exchange "Rich Get Richer Power Laws"
  (2026-11-21): "Some apparent critical slowing down may reflect
  higher-order degeneracy of the optimization landscape … It could be a
  collection of algebraically relaxing singular modes", and "a finite
  dependency tree can produce a stagewise learning process without any
  scale-free statistics". An alternative to reading training's slow modes
  as criticality. The wording is A's (the other assistant in the exchange
  "Rich Get Richer Power Laws", A39, A43); adopting it is the owner's
  call.
---

<!-- inactive-ok-file: CLAIM-811 CLAIM-843 — Proposed; claims filed with this one -->
<!-- inactive-ok-file: LEAD-200 — Done; the check of relaxation over an ultrametric tree, cited for what it did -->
<!-- inactive-ok-file: ARG-137 — new and Proposed or Rejected, filed from the exchange "Rich Get Richer Power Laws" on 2026-11-21 -->
<!-- inactive-ok-file: THEORY-tmpbobud THEORY-tmpg4aat ARG-tmp0cg6w — Proposed or Rejected; filed 2026-11-21 from the readings of Amari, Park & Ozeki and Wei et al. -->

# CLAIM-844: Some of the slow, power-law-like relaxation seen in training deep networks may be the algebraic relaxation of degenerate singular modes rather than critical slowing down in a collective phase, and a dependency tree of feature transitions yields power laws only if its thresholds or relaxation times are themselves broadly or self-similarly distributed

## The claim

A39 §5: "This creates another possible origin for the broad timescale
hierarchies observed during DNN training. Some apparent critical slowing
down may reflect higher-order degeneracy of the optimization landscape. A
hierarchy of such degeneracies could generate a broad distribution of
learning times. However, that would not automatically establish a
scale-free collective phase. It could be a collection of algebraically
relaxing singular modes."

The premise is [CLAIM-811](CLAIM-811.md): a degenerate direction relaxes as a power
of t with no collective mode and no tuning to a critical point. The works
on plateaus near singularities the claim cited, Amari's and Wei's
([LIT-2960](../literature.d/LIT-2960.md), [LIT-3000](../literature.d/LIT-3000.md)), were read on 2026-11-21: Amari's
qualifies the claim and Wei's is a rival to it (the dated note below). The
claim offers this as a rival explanation of observed slow relaxation in
training, beside criticality. It does not say which explanation holds for
any network.

A43 §17 adds a limit on the other side: "A finite dependency tree can
produce a stagewise learning process without any scale-free statistics.
But if the dependency structure itself becomes self-similar, or if the
relevant thresholds and relaxation times follow a broad scaling
distribution, then the sequence of feature activations might produce
power laws … That would be an additional mechanism to derive and test —
not a consequence of singularity theory alone." The record's [LEAD-200](../leads.d/LEAD-200.md)
(Done) checked the related question whether relaxation summed over an
ultrametric tree gives a power law.

## The gap, and where it is filled

The ledger notes that A gives no step from one algebraic mode to the
broad distribution of timescales an observed power law needs. What one
mode does, and the balanced start its algebraic decay needs, is
[CLAIM-811](CLAIM-811.md). [CLAIM-843](CLAIM-843.md), the assistant's, supplies one step: a
population of such modes from a random start, which relaxes on average as
a power law. That route needs no criticality and no hierarchy of
degeneracies, which narrows A's alternative. A power law in training
relaxation does not even indicate a hierarchy of singular orders;
[ARG-137](../arguments.d/ARG-137.md) argues this.

## Cross-reference

The rival it names, criticality and critical slowing in learning, is
another theme of the same exchange. The record's entries on critical
slowing belong to it.

## Note of 2026-11-21: Amari, Park & Ozeki (2006) and Wei et al. (2008), read

- **Amari, Park and Ozeki qualify the claim** ([NOTE-tmptlwkf](../notes.d/NOTE-tmptlwkf.md),
  [THEORY-tmpbobud](../theory.d/THEORY-tmpbobud.md)). They support that slow phases of gradient training can
  be singular in origin, and attribute the backpropagation plateau to the
  critical set, a "Milnor attractor" even for a regular truth (§4.5). But
  their plateaus are transients that end in escape, shown in models with
  two effective parameters; they report no power-law relaxation, no
  distribution of timescales and no comparison with criticality. Nothing
  bears on the second part (dependency trees).
- **Wei and colleagues give a third rival** ([NOTE-tmpl89m0](../notes.d/NOTE-tmpl89m0.md),
  [THEORY-tmpg4aat](../theory.d/THEORY-tmpg4aat.md)). Their long, on-singularity plateau is "a long period
  of random walk on R∗1", a line of models that compute the same
  function, along which the averaged loss does not change ("Ė(ξ) = 0 on
  average"), driven by "the fluctuations due to the noise and the random
  sampling of input", and left only when the walk reaches the line's
  unstable part. That is neither critical slowing down in a collective
  phase nor the algebraic relaxation of a degenerate mode: slow training
  from noise-driven escape along a flat line of equivalent models. So
  "slow learning near singularities" in this literature is not by itself
  evidence for algebraically relaxing singular modes; a measurement that
  separates the claim from its rivals would have to tell a walk along a
  flat line from a decay along a degenerate direction as well as from
  critical slowing. The paper says nothing of power laws or broad
  timescale distributions, and is no ground of this claim ([ARG-tmp0cg6w](../arguments.d/ARG-tmp0cg6w.md)).
  The rival is held in [THEORY-tmpg4aat](../theory.d/THEORY-tmpg4aat.md), in the authors' voice.

## Note of 2026-11-21: grounds

Amari, Park and Ozeki's reading (THEORY-tmpbobud), first placed in this claim's grounds, qualifies the claim rather than supporting it: its plateaus are transients that end in escape, with no power law and no spread of timescales. It is therefore kept as a bearing in the dated note above, not as a ground. The claim stays interpretive, with no ground of its own yet. The note is the assistant's (Claude, in this session).
