---
status: Active
title: 'A note on the Kesten–Grincevičius–Goldie theorem'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Registered on 2026-11-22 as a stand-in for Kesten (1973), LIT-3005,
    whose lawful copy at Project Euclid was stopped by a WAF challenge
    (ADR-114). Read the same day in NOTE-tmpv02cb by a delegated reader
    from arXiv (arxiv.org/pdf/1512.07262v2, v2 of 22 July 2016, the
    author's preprint, 17 pp.); the reading is THEORY-tmpsmrhx.
    Bibliography from the arXiv API (v1 submitted 22 December 2015) and
    Crossref (Electronic Communications in Probability 21 (2016), 1–12,
    DOI 10.1214/16-ECP9), no email address sent. Not held before: no hit
    for the arXiv id, the DOI, Kevei or Grincevičius in record/.
tags:
- probabilistic-modeling
- mathematics
date: '2026-11-22'
published: '2015-12-22'
arxiv: '1512.07262'
doi: '10.1214/16-ECP9'
first_author: 'Kevei'
keywords:
- 'Perpetuity equation'
- 'Stochastic difference equation'
- 'Strong renewal theorem'
- 'Exponential functional'
- 'Maximum of random walk'
- 'Implicit renewal theorem'
implementations: []
summary: >-
  Kevei (2016), A note on the Kesten–Grincevičius–Goldie theorem,
  Electronic Communications in Probability 21, 1–12; arXiv 1512.07262.
  For the perpetuity X = AX + B, the theorem says P{X > x} ∼ c+ x^(−κ)
  (and P{X < −x} ∼ c− x^(−κ), c+ + c− > 0) when EA^κ = 1,
  EA^κ log⁺A < ∞, log A is nonarithmetic and E|B|^κ < ∞; the paper
  extends it to EA^κ log⁺A = ∞, where a nonconstant slowly varying
  factor appears. Its introduction is the record's restatement of
  Kesten (1973), [LIT-3005](LIT-3005.md), which it stands in for in one dimension, and
  of Goldie's reflecting form X = AX ∨ B with the same κ.
---
<!-- inactive-ok-file: NOTE-tmpv02cb THEORY-tmpsmrhx — Skimmed or Proposed; this work's reading -->
<!-- inactive-ok-file: LIT-3005 — Unfetched; the original this work stands in for -->
<!-- inactive-ok-file: LIT-tmpn76uh — Deferred; Goldie (1991), registered with this reading -->

# LIT-tmpk12vu: A note on the Kesten–Grincevičius–Goldie theorem

Kevei (2016). Electronic Communications in Probability 21, 1–12.
arXiv 1512.07262. DOI 10.1214/16-ECP9.

## Key takeaways

- States the one-dimensional Kesten–Grincevičius–Goldie theorem with its
  hypotheses, and the two-sided Pareto-like tail it gives (p. 1).
- EA^κ = 1 with A ≢ 1 forces E log A < 0 (p. 6), and P{A > 1} > 0 is
  what makes the tail polynomial rather than exponential (p. 2).
- Grey: with EA^κ < 1 a regularly varying tail can come from B alone
  (p. 2).
- Goldie's Theorem 5.2: the max form X = AX ∨ B has P{X > x} ∼ c x^(−κ)
  under the same conditions, c > 0 iff P{B > 0} > 0 (p. 4).

## Standing in the record

Registered as a stand-in for Kesten (1973), [LIT-3005](LIT-3005.md), which is Unfetched
([ADR-114](../decisions.d/ADR-114.md)). It restates Kesten's theorem in one dimension, Goldie's
re-proof and his max form; it does not restate Kesten's matrix theorem
(for that, Alsmeyer and Mentemeier, [LIT-tmpt282z](LIT-tmpt282z.md)). Goldie (1991),
[LIT-tmpn76uh](LIT-tmpn76uh.md), is registered from it.
