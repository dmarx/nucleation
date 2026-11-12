---
number: 152
status: Active
formerly:
- CASE-tmpj2xb7
title: 'Absent attempt or unresponsive receiver: with Y ∼ N(ab, 1), a the strength of an attempted influence and b the receiver''s responsiveness, the settings (a, b) = (0, 1) and (1, 0) give the same response distribution; K(a, b) = a²b²/2, the Fisher matrix has rank at most one and vanishes at the origin, and the real log canonical threshold is ½ with multiplicity 2, not the regular d/2 = 1, while changing b with a held fixed separates the two'
version: 2
history:
- version: 2
  date: '2026-11-12'
  note: >-
    Draws on THEORY-082 ("The regular asymptotics, which need G invertible
    (THEORY-082), fail on the axes"); THEORY-087 ("not as the regular
    (d/2) log n = log n (THEORY-087)"). First application of draws_on
    (ADR-095). No other change.
standing: stipulated
kind: construction
tags:
- mathematical-statistics
- pragmatics
- information-geometry
date: '2026-10-24'
line: pragmatic-transport
illustrates:
- CLAIM-450
- CLAIM-407
- CLAIM-188
summary: >-
  The construction from the exchange of 2026-10-24 (workbench entry of
  2026-10-24, U27), checked when filed. A two-parameter response model in
  which the observation depends on a product, the smallest singular model
  with a communicative reading. It shows a missing response failing to say
  whether nothing was attempted or nothing was taken up.
draws_on:
- THEORY-082
- THEORY-087
---
<!-- inactive-ok-file: ADR-095 — Proposed; the decision this entry's draws_on first applies, cited in its history -->

# CASE-152: Absent attempt or unresponsive receiver: with Y ∼ N(ab, 1), a the strength of an attempted influence and b the receiver's responsiveness, the settings (a, b) = (0, 1) and (1, 0) give the same response distribution; K(a, b) = a²b²/2, the Fisher matrix has rank at most one and vanishes at the origin, and the real log canonical threshold is ½ with multiplicity 2, not the regular d/2 = 1, while changing b with a held fixed separates the two

## The case

A stipulated toy, not a theory of communication. An observed response
Y ∼ N(ab, 1), where a is the strength of an attempted communicative
influence and b the responsiveness of the receiving process. The
distribution depends only on the product ab.

- **Same distribution.** (a, b) = (0, 1), no attempt and a responsive
  receiver, and (1, 0), an attempt and an unresponsive receiver, both give
  N(0, 1), and so does every point on the two axes.
- **Divergence.** Against the reference N(0, 1), K(a, b) = D_KL = ½a²b².
- **Fisher matrix.** The score is (y − ab)(b, a), so
  G(a, b) = [[b², ab], [ab, a²]]: determinant zero everywhere, rank at most
  one, zero at the origin. The regular asymptotics, which need G
  invertible ([THEORY-082](../theory.d/THEORY-082.md)), fail on the axes.
- **Learning coefficient.** For a prior smooth and positive near the
  origin, ∫ exp(−n a²b²/2) π(a, b) da db ≍ (log n)/√n, so λ = ½ with
  multiplicity m = 2. The free energy grows as ½ log n − log log n, not as
  the regular (d/2) log n = log n ([THEORY-087](../theory.d/THEORY-087.md)).
- **Intervention.** Change b with a fixed. At (0, 1) the response stays
  N(0, 1); at (1, 0) it moves to N(b′, 1). An intervention on the receiver
  separates what no number of ordinary observations does.

## What it can show

That a missing response is compatible with an absent attempt and with an
unresponsive receiver, that the nominal parameter count overstates the
model's complexity there, and that the distinction is recoverable by
intervention ([CLAIM-407](../claims.d/CLAIM-407.md)).

## What it cannot show

That the two settings are different communicative acts. Whether "an
attempt that was not taken up" is an act at all is a question for the
account of communicative kinds ([TERM-040](../terms.d/TERM-040.md)), not for the likelihood.

## Note of 2026-10-31: the same λ, different multiplicity

A3 of the exchange "Analyze nucleation concepts" rebuilt this case as
gradient flow on L = ½(uv − 1)² and added a contrast, rechecked. With a
nonzero target the true set ab = c ≠ 0 is a smooth curve, with λ = ½ and
m = 1. At the target 0 the true set is the crossing ab = 0, with λ = ½ and
m = 2. So λ alone does not identify the geometry of the optimal set; the
multiplicity separates them. A14 gave a variant for a three-factor probe
Y ∼ N(q²c₁c₂, σ²) on a box. When the true response is zero, λ = ¼ and
m = 1, from the q⁴ term. When it is positive, λ = ½. A15 gave the
Bernoulli version, σ(uv), with the same pair of values as this case. The
singularity is the probe's and the parameterization's, as this case
already says ("What it cannot show").

## Note of 2026-11-12: the silent alarm, from "Meaning Transmission Explained"

<!-- inactive-ok-block: CASE-tmpaky45 CASE-tmpl4kyp — filed from the same exchange, Proposed -->
In the exchange "Meaning Transmission Explained" (https://chatgpt.com/share/6af517f7-cb48-83ea-8395-df7d52333dc7, 2026-11-07), A8 §3 maps this case onto a
silent alarm under test: "Did the test smoke reach the sensor? Did the
sensor detect it? Did its relay fail?" A5 §1 had drawn the same limit on
the owner's debugging case ([CASE-tmpaky45](CASE-tmpaky45.md)): the silence "establishes a
violation of the expected response profile, not necessarily a broken
detector." A10 §1 works it out in a four-component chain
([CASE-tmpl4kyp](CASE-tmpl4kyp.md)). The injector test detects any single fault and locates
none, and only all four probes together separate the five states
(rechecked). A's description of this case, Y ∼ N(ab, 1) with (0, 1) and
(1, 0) giving the same distribution, is accurate.
