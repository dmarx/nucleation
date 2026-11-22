---
status: Skimmed
paper: LIT-tmpk12vu
title: 'Kevei, skimmed for the hypotheses of the Kesten–Grincevičius–Goldie theorem and its reflecting form, as a stand-in for Kesten'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Read on 2026-11-22 by a delegated reader from arXiv
    (arxiv.org/pdf/1512.07262v2, v2 of 22 July 2016, the author's
    preprint, 17 pp.), text extracted with pdftotext, as a stand-in for
    Kesten (1973), LIT-3005, whose lawful copy at Project Euclid was
    stopped by an Imperva Incapsula challenge (ADR-114). Read: §1
    (pp. 1–6) in full, with Theorems 1–4 and Corollary 1; the start of
    §2 (Theorem 5 and the smoothing step); the reference list. Skipped:
    the remaining proofs and the appendix, so Skimmed. Page numbers are
    the PDF's. Every quotation below rechecked by the filer by script
    against the downloaded text. No email address sent.
date: '2026-11-22'
summary: >-
  Kevei's introduction states the one-dimensional Kesten–Grincevičius–Goldie
  theorem with its hypotheses (EA^κ = 1, EA^κ log⁺A < ∞, nonarithmetic
  log A, E|B|^κ < ∞, non-degeneracy) and its two-sided Pareto-like tail,
  says Kesten proved it "in d dimension", notes that EA^κ = 1 forces
  E log A < 0, gives Grey's B-driven alternative, and restates Goldie's
  Theorem 5.2 for the max form X = AX ∨ B with the same κ. The paper's
  own result, a slowly varying correction when EA^κ log⁺A = ∞, is not
  what the record uses. Read as a stand-in for Kesten (LIT-3005).
---
<!-- inactive-ok-file: NOTE-tmpy4hcs — Skimmed; the companion stand-in reading for Kesten -->
<!-- inactive-ok-file: LIT-3005 — Unfetched; the original this reading stands in for -->
<!-- inactive-ok-file: LIT-tmpn76uh — Deferred; Goldie (1991), registered from this reading -->
<!-- inactive-ok-file: CLAIM-824 ARG-140 TERM-tmpg1vx2 SYNTHESIS-119 LIT-tmph6kst THEORY-tmpsmrhx THEORY-tmpocjqv ARG-tmpn6ufb CLAIM-803 — Proposed, Deferred or new; the entries this reading bears on, its own reading and the argument filed with it -->

# NOTE-tmpv02cb: Kevei, skimmed for the hypotheses of the Kesten–Grincevičius–Goldie theorem and its reflecting form, as a stand-in for Kesten

## Contribution

A short paper extending the Kesten–Grincevičius–Goldie theorem to the
case EA^κ log⁺A = ∞, where the tail becomes P{X > x} ∼ c x^(−κ) ℓ(x) with
"ℓ is a nonconstant slowly varying function" (abstract). What the record
uses is its introduction, which restates the classical theorem, its
history and its max-equation variant with care. The reading is
THEORY-tmpsmrhx.

## Key results

1. **The theorem** (p. 1, eqs. (1)–(3)). For X =d AX + B, "(A, B) and X on
   the right-hand side are independent", with "P{Ax + B = x} < 1 for any
   x ∈ R", A ≥ 0 and A ≢ 1: "The first results on existence and tail
   behavior of the solution are due to Kesten [25], who proved that if
   EAκ = 1, EAκ log+ A < ∞, log A conditioned on A ≠ 0 is nonarithmetic,
   and E|B|κ < ∞ for some κ > 0 ... then the solution of (1) has
   Pareto-like tail, i.e. P{X > x} ∼ c+ x−κ and P{X < −x} ∼ c− x−κ",
   "for some c+, c− ≥ 0, c+ + c− > 0". So the tail can be on one side
   only.
2. **Dimension and attribution** (p. 1): "Actually, Kesten proved a
   similar statement in d dimension. Later Goldie [18] simplified the
   proof of the same result in the one-dimensional case (for more general
   equations) using renewal theoretic methods", after Grincevičius.
3. **Growth is needed** (p. 2): "if P{A > 1} > 0 the tail decreases at
   least polynomially"; with A ≤ 1 a.s. "the solution has at least
   exponential tail" (Goldie and Grübel).
4. **B alone can do it** (p. 2): Grey "showed that if EAκ < 1, EAκ+ǫ < ∞,
   then the tail of X is regularly varying with parameter −κ if and only
   if the tail of B is"; "the regular variation of the solution X of (1)
   is either caused by A alone, or by B alone".
5. **The method** (p. 2): the tilted measure Pκ{log A ∈ C} =
   E[I(log A ∈ C)A^κ], under which the tail equation is a renewal
   equation; "If Eκ log A = EAκ log A ∈ (0, ∞), then a renewal theorem on
   the line implies the required tail asymptotics."
6. **The reflecting form** (p. 4, eq. (12)): for X =d AX ∨ B, "Theorem 5.2
   in [18] states that if (2) holds, then there is a unique solution X to
   (12), and P{X > x} ∼ cx−κ with some c ≥ 0, and c > 0 if and only if
   P{B > 0} > 0." With B ≡ 1, "log X = M, where M = max{0, S1, S2, ...}",
   the maximum of the random walk of log A.
7. **Contraction is forced** (p. 6): "The assumption EAκ = 1 together with
   A ≢ 1 imply that E log A < 0, so the random walk tends to −∞".

## Assumptions

(A_n, B_n) i.i.d., A and B possibly dependent, X independent of (A, B);
A ≥ 0; non-degeneracy; nonarithmetic log A; κ > 0 with EA^κ = 1;
EA^κ log⁺A < ∞; E|B|^κ < ∞. The max form needs the same (2).

## Concepts

Perpetuity; stochastic fixed-point equation; Kesten–Grincevičius–Goldie
theorem; Cramér-type condition EA^κ = 1 and the tilted measure; implicit
renewal theory; Grey's B-driven tail; the max recursion and the maximum of
a negative-drift random walk.

## Connections

- **What it restates of Kesten (LIT-3005)**: the one-dimensional
  statement and its hypotheses (results 1, 7), with the attribution that
  Kesten's own proof is d-dimensional (result 2). It does not restate the
  matrix theorem, Kesten's exact hypotheses or his constants; for the
  matrix form see NOTE-tmpy4hcs (Alsmeyer and Mentemeier), at second hand.
- **What it adds that is not Kesten's**: Goldie's max form (result 6) and
  Grey's B-driven case (result 4). Goldie (1991) is registered as
  LIT-tmpn76uh.

## Bearing on the record

- **CLAIM-824** (Proposed): grounds the claim's Kesten half at second
  hand, and corrects its conditions: E|B|^κ, not E[B^κ]; non-degeneracy;
  a two-sided tail that may sit on one side only; E log A < 0 and
  P(A > 1) > 0 follow from EA^κ = 1 and are not separate hypotheses; and
  "even when the process contracts on average" understates, since
  log-contraction is required (results 1, 3, 7). The reflecting floor
  has the same exponent equation (result 6), and a Pareto tail in X can
  come from B alone (result 4). ARG-tmpn6ufb.
- **ARG-140** (Proposed): Mitzenmacher's κ = 1 Champernowne example is an
  instance of Goldie's max theorem (result 6), not only of the equation.
- **TERM-tmpg1vx2, SYNTHESIS-119, QUESTION-505, CLAIM-803** (filer notes
  elsewhere): the two floors share one exponent equation; the tilted
  measure is the formal sense of "growth just balances"; B-driven tails
  sharpen the demand for dynamics.
- **LIT-tmph6kst** (Gabaix, Deferred): a parallel; Gabaix's lower
  reflecting barrier is of the max form. Kevei does not cite Gabaix.

## Limitations

A note on an extension, so its restatement of the classical theorem is
brief. Kesten's own hypotheses and the positivity of his constants are not
given here. The proofs were not read.
