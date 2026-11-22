---
status: Skimmed
paper: LIT-tmpt282z
title: "Alsmeyer and Mentemeier, skimmed for the matrix form of Kesten's tail theorem, as a stand-in for Kesten"
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Read in part on 2026-11-22 by a delegated reader from arXiv
    (arxiv.org/pdf/1009.1728v3, v3 of 11 February 2011, the authors'
    preprint, 27 pp.), text extracted with pdftotext, as a stand-in for
    Kesten (1973), LIT-3005, whose lawful copy at Project Euclid was
    stopped by an Imperva Incapsula challenge (ADR-114). Read: the
    abstract and §1 with Theorem 1.1 and Remarks 1–4 (pp. 1–3).
    Skipped: §§2–8, the proofs. Page numbers are the PDF's. Every
    quotation below rechecked by the filer by script against the
    downloaded text. No email address sent.
date: '2026-11-22'
summary: >-
  For R_n = M_n R_(n−1) + Q_n with invertible d × d matrices, a negative
  Liapunov exponent and (A1)–(A7), there is a unique κ with
  lim n^(−1) log E‖Π_n‖^κ = 0 and lim t^κ P(xR > t) = K(x), K positive
  and continuous on the sphere (Theorem 1.1). Remark 1 says the result,
  "with one extra condition", was stated by Kesten at the end of his 1973
  article and proved by Le Page. The record's only access to Kesten's
  matrix theorem, at second hand.
---
<!-- inactive-ok-file: LIT-3005 — Unfetched; the original this reading stands in for -->
<!-- inactive-ok-file: THEORY-tmpocjqv CLAIM-824 — Proposed or new; this reading's THEORY and the claim it bears on -->

# NOTE-tmpy4hcs: Alsmeyer and Mentemeier, skimmed for the matrix form of Kesten's tail theorem, as a stand-in for Kesten

## Contribution

A shorter proof, by Markov renewal theory and Harris recurrence, of the
multidimensional tail theorem for random difference equations with
regular matrices: "A rather long proof of this result, originally stated
by Kesten at the end of his famous article [12], was given by LePage [15]"
(abstract). The reading is THEORY-tmpocjqv.

## Key results

1. **The stationary solution** (p. 2, eqs. (1)–(3)): if the Liapunov
   exponent β := lim n^(−1) log ‖Π_n‖ is negative and (A1)–(A2) hold, the
   chain has a unique stationary law, that of R := Σ_(n≥1) Π_(n−1) Q_n.
2. **Theorem 1.1** (p. 2): under (A1)–(A7) and β < 0, "there exists a
   unique κ ∈ (0, κ0] such that lim n−1 log E‖Πn‖κ = 0" and
   "lim tκ P(xR > t) = K(x) for all x ∈ S, where K is a finite positive
   and continuous function on S".
3. **Remark 1** (p. 3): "This result (with one extra condition) was stated
   by Kesten at the end of his famous article [12] and later proved by Le
   Page [15] with the help of Kesten's Markov renewal theorem".

## Assumptions

i.i.d. (M_n, Q_n); M invertible a.s. (A3); an irreducibility and a
density condition (A4), (A5); non-degeneracy P(Mv + Q = v) < 1 (A6); a
moment condition with E inf_x |xM|^κ0 ≥ 1 (A7).

## Concepts

Random difference equation in R^d; Liapunov exponent; the growth rate of
E‖Π_n‖^κ as the matrix analogue of EA^κ; Markov renewal theory; Le Page's
theorem.

## Connections

- **What it restates of Kesten (LIT-3005)**: only that Kesten stated a
  matrix tail theorem of this kind "with one extra condition" (Remark 1),
  and, in a passage the filer found by search in the skipped §5, that
  "Kesten [12] imposes an additional assumption involving so-called
  feasible matrices" (p. 14). It does not give Kesten's hypotheses, and it
  does not restate the one-dimensional case; for that see NOTE-tmpv02cb
  (Kevei).
- **THEORY-407, NOTE-078** (Furstenberg–Kesten, the multiplicative
  ergodic theorem): background. The negative Liapunov exponent β here
  plays the part of E log A < 0.

## Bearing on the record

- **CLAIM-824** (Proposed): background to its Kesten attribution. Kesten's
  1973 theorem is a matrix theorem; the scalar X = AX + B the claim uses
  is its one-dimensional case, re-proved by Goldie.

## Limitations

Only the introduction was read. The matrix theorem is the authors', with
regular matrices and their own conditions; how far it matches Kesten's
statement is only what Remark 1 says.
