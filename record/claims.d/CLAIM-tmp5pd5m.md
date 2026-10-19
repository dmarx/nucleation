---
status: Active
title: 'If a map approximately intertwines two operators, with defects E_A = ΦA − A′Φ and E_B = ΦB − B′Φ, then Φ[A,B] − [A′,B′]Φ = A′E_B + E_A B − B′E_A − E_B A, so the commutator is carried to within (‖A‖ + ‖A′‖)‖E_B‖ + (‖B‖ + ‖B′‖)‖E_A‖'
version: 1
history:
- version: 1
  date: '2026-10-19'
  note: >-
    Split from CLAIM-063 and filed Active at the owner's direction, carrying
    out the promotion audit's decision (record/promotion-audit/decisions/CLAIM-063.yaml,
    batch 002, ADR-047). CLAIM-063 was filed as demonstrated, but its defeat
    condition is about measured order effects in renderings, which is
    empirical with no observation under it. This claim is the identity the
    manuscript's §9 states, with its proof. ARG-006 holds the exact case
    (zero defects). CLAIM-063 keeps the thesis and rests on this claim.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the expansion below: operators A, B, A′, B′ and a map Φ for
  which Φ[A,B] − [A′,B′]Φ differs from A′E_B + E_A B − B′E_A − E_B A, or a
  bounded case in which its norm exceeds
  (‖A‖ + ‖A′‖)‖E_B‖ + (‖B‖ + ‖B′‖)‖E_A‖.
tags:
- mathematics
date: '2026-10-19'
line:
- formal-apparatus
uses:
- TERM-024
summary: >-
  The commutator-distortion identity of the manuscript's §9, on its own and
  proved. A map that nearly intertwines each of two operations carries their
  commutator to the commutator of the images, up to an error that is linear
  in the two intertwining defects. [ARG-006](../arguments.d/ARG-006.md) is the exact case. It says nothing
  about whether the defects can be identified from data ([CLAIM-253](CLAIM-253.md)), or what
  bounds an observed order effect ([CLAIM-231](CLAIM-231.md)).
supports:
- CLAIM-063
---
<!-- inactive-ok-file: CLAIM-063 — Proposed; the thesis this identity was split from and that rests on it, cited as open -->
<!-- ref::uses-file: TERM-024 — the commutator is the noncommutativity of operations the term names -->

# CLAIM-tmp5pd5m: If a map approximately intertwines two operators, with defects E_A = ΦA − A′Φ and E_B = ΦB − B′Φ, then Φ[A,B] − [A′,B′]Φ = A′E_B + E_A B − B′E_A − E_B A, so the commutator is carried to within (‖A‖ + ‖A′‖)‖E_B‖ + (‖B‖ + ‖B′‖)‖E_A‖

## The claim

Let A, B act on a space V and A′, B′ on a space V′, all linear, and let
Φ: V → V′ be linear. Define the intertwining defects E_A = ΦA − A′Φ and
E_B = ΦB − B′Φ, and write [X, Y] = XY − YX. Then

Φ[A,B] − [A′,B′]Φ = A′E_B + E_A B − B′E_A − E_B A.

If the spaces are normed and the operators bounded, then

‖Φ[A,B] − [A′,B′]Φ‖ ≤ (‖A‖ + ‖A′‖)‖E_B‖ + (‖B‖ + ‖B′‖)‖E_A‖.

So a transport that nearly intertwines each framing operation carries their
commutator, the measure of how much the two interfere, to the commutator of
the images, within an error linear in the defects. With E_A = E_B = 0 it is
exact: Φ[A,B] = [A′,B′]Φ, which is [ARG-006](../arguments.d/ARG-006.md)'s case.

## Proof

Substitute ΦA = A′Φ + E_A and ΦB = B′Φ + E_B twice:

ΦAB = (A′Φ + E_A)B = A′ΦB + E_A B = A′B′Φ + A′E_B + E_A B,

ΦBA = (B′Φ + E_B)A = B′ΦA + E_B A = B′A′Φ + B′E_A + E_B A.

Subtracting gives the identity. The norm bound follows from the triangle
inequality and ‖XY‖ ≤ ‖X‖‖Y‖, grouping the E_B terms (A′E_B and −E_B A) and
the E_A terms (E_A B and −B′E_A).

## What it does not say

- **That the defects can be read off data.** Two models with the same
  observations can carry defects 0 and 1 ([CLAIM-253](CLAIM-253.md)). The bound is in terms
  of quantities a state model posits.
- **What bounds an observed order effect.** That is [CLAIM-231](CLAIM-231.md)'s
  observational 2ε bound, which needs no state model.
- **That the commutator structure of the source is preserved.** Only its
  image under Φ is ([CLAIM-011](CLAIM-011.md)).
- **That interference between perspectives is part of what a translation
  preserves.** That is [CLAIM-063](CLAIM-063.md)'s thesis.
