---
number: 63
status: Proposed
formerly:
- CLAIM-tmphq3fu
title: 'A transport that approximately intertwines each framing operation approximately preserves their commutator, so the degree to which interpretive perspectives interfere can itself be part of what a translation preserves; on observed responses that degree is the order effect, which the intertwining defects bound only with a readout defect added and which the data identify only through observational distortion'
version: 3
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Split under ADR-043 at the owner's direction, carrying out the promotion
    audit's decision (record/promotion-audit/decisions/CLAIM-063.yaml, batch
    002, ADR-047). The commutator identity and its norm bound, which this
    claim used, are now CLAIM-373, demonstrated and Active, with a
    proof. This claim rests on it and keeps the thesis: that how far
    interpretive perspectives interfere can be part of what a translation
    preserves. Its defeat condition is about measured order effects, which
    is empirical with no observation under it, so by ADR-043's rule the
    warrant is interpretive. The title and the defeat condition are
    unchanged, and the status stays Proposed.
- version: 3
  date: '2026-10-29'
  note: >-
    Eleventh status review (ADR-057, ADR-059). CLAIM-253, Active since
    2026-10-10, is conceded and written in. The intertwining defects
    are defined on interpretive states and are not identified from
    judgement data. The identity reaches observed order effects only
    with a readout defect E_O = O′Φ − KO. The title now says that, on
    observed responses, the interference is the order effect. The
    defeat condition is restated on observed order effects under one
    outcome correspondence fixed across items, as the notes of
    2026-10-10 and 2026-10-19 said it was to be read. The old title
    read: 'A transport that approximately intertwines each framing
    operation approximately preserves their commutator, so the degree
    to which interpretive perspectives interfere can itself be part of
    what a translation preserves'. The old condition read: 'Renderings
    whose framing operations are each well intertwined nevertheless
    differ from the source in measured order effects by more than the
    intertwining defects allow.' The status stays Proposed.
role: thesis
warrant: interpretive
defeated_if: >-
  Under one outcome correspondence fixed across a class of items, the
  observed order effects of different renderings of the same sources
  do not differ from one another beyond sampling error, or differ only
  with the target study's response format, so that how far the
  framings interfere is not something a rendering keeps or loses.
tags:
- mathematics
- philosophy-of-language
date: '2026-10-08'
line: pragmatic-transport
works:
- what-survives-translation
rests_on:
- CLAIM-373
uses:
- TERM-024
summary: >-
  A34 §4, made approximate at A40 §6.4 and stated in the manuscript §9
  as the commutator-distortion identity. Its argument is an ARG because
  A40 limited the inference: the conclusion holds of Φ's image only.
argued_by:
- ARG-006
objected_by:
- CLAIM-253
complements:
- CLAIM-231
- CLAIM-117
---
<!-- ref::uses-file: TERM-024 — stated in "noncommutativity, of events and of operations"; the body applies the term without naming it -->

# CLAIM-063: A transport that approximately intertwines each framing operation approximately preserves their commutator, so the degree to which interpretive perspectives interfere can itself be part of what a translation preserves; on observed responses that degree is the order effect, which the intertwining defects bound only with a readout defect added and which the data identify only through observational distortion

## The claim

A34 §4: "the degree to which interpretive perspectives interfere with each other
could itself be part of what a faithful translation preserves." Manuscript §9:
"If ΦA≈A'Φ and ΦB≈B'Φ, compare Φ[A,B] with [A',B']Φ ... This identity bounds
commutator distortion by local intertwining defects and operator norms."

Its argument is [ARG-006](../arguments.d/ARG-006.md).

## What it does not say

That the commutator *structure* is preserved: only its image under Φ ([CLAIM-011](CLAIM-011.md)).

## Note of 2026-10-10: the replies

After [CLAIM-253](CLAIM-253.md): the intertwining defects are not identified from
data, since two models with the same observations can carry defects 0 and
1. [CLAIM-231](CLAIM-231.md) bounds the observed order effect by observational
distortions alone: if each order's response distribution is within ε of
the source's under one outcome correspondence, the observed order effect
is within 2ε. The identity explains that bound under a state model, and
[ARG-006](../arguments.d/ARG-006.md)'s algebra stands. The defeat condition above, stated on "measured
order effects", is to be read against that bound. The manuscript's text
quoted above is unchanged.

## Note of 2026-10-19: split under [ADR-043](../decisions.d/ADR-043.md)

The identity Φ[A,B] − [A′,B′]Φ = A′E_B + E_A B − B′E_A − E_B A, with its
norm bound, is now [CLAIM-373](CLAIM-373.md). It is proved there and Active, and it is
the approximate case that [ARG-006](../arguments.d/ARG-006.md) names. This claim keeps the thesis that
the identity is used for: that interference between perspectives can be
part of what a translation preserves. That thesis is tested by measured
order effects. Given [CLAIM-253](CLAIM-253.md), the identified bound to test against is
[CLAIM-231](CLAIM-231.md)'s observational 2ε, not the defects. No study has been run, so
the claim is interpretive.

## Note of 2026-10-28: what holds it back

The fourth status review ([ADR-057](../decisions.d/ADR-057.md)) took this claim because [ARG-006](../arguments.d/ARG-006.md), which
concludes it, is a sound argument: its inference is Active and its one
premise, [CLAIM-373](CLAIM-373.md), is Active. The claim stays Proposed, because the
inference carries less than the claim says, and the record already says
where:

- **[CLAIM-011](CLAIM-011.md) (Active)** limits the result to Φ's image. Preserving Φ's
  image of a commutator does not establish preservation of the whole
  commutator structure unless Φ is informative enough.
- **[CLAIM-253](CLAIM-253.md) (Active)** is a live objection, and it undercuts [ARG-006](../arguments.d/ARG-006.md). The
  intertwining defects are defined on interpretive-state spaces and are not
  identified from judgement data. The identity reaches *observed* order
  effects only with a readout-intertwining defect, O′Φ − O, which the claim
  does not state.

What would clear it is a version that states the readout defect and bounds
observed order effects by the intertwining defects together with it, and
that names an identified choice of Φ, so that the defects are fixed by the
data. Until then, how far interpretive perspectives interfere is part of
what a translation preserves only in an unidentified sense.

## Note of 2026-10-29: CLAIM-253 written in

The identity is CLAIM-373's and holds on interpretive states. A study
observes responses. There the identity bounds the order effect only with
the readout defect added,
‖O′[A′,B′]Φμ − K O[A,B]μ‖ ≤ ‖E_O[A,B]μ‖ + 2(‖E_A‖ + ‖E_B‖), and the data do
not fix its defects. The bound identified from data is CLAIM-231's 2ε,
under one outcome correspondence fixed across items, and the defeat
condition now tests the thesis on that footing. The note of 2026-10-28
called CLAIM-253 live; it is now written in. The identification result its
second answer asks for, a minimal-realization theorem, is still open.

## Note of 2026-10-29: what holds it back

No study has measured the order effects of different renderings of the
same sources under one outcome correspondence fixed across items.
CASE-065's two administrations change language and readership together,
and report correlations rather than response distributions, so no ε can be
computed from them.
