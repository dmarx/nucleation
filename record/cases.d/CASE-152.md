---
number: 152
status: Active
formerly:
- CASE-tmpj2xb7
title: 'Absent attempt or unresponsive receiver: with Y ∼ N(ab, 1), a the strength of an attempted influence and b the receiver''s responsiveness, the settings (a, b) = (0, 1) and (1, 0) give the same response distribution; K(a, b) = a²b²/2, the Fisher matrix has rank at most one and vanishes at the origin, and the real log canonical threshold is ½ with multiplicity 2, not the regular d/2 = 1, while changing b with a held fixed separates the two'
version: 1
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
summary: >-
  The construction from the exchange of 2026-10-24 (workbench entry of
  2026-10-24, U27), checked when filed. A two-parameter response model in
  which the observation depends on a product, the smallest singular model
  with a communicative reading. It shows a missing response failing to say
  whether nothing was attempted or nothing was taken up.
supports:
- CLAIM-450
---

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
