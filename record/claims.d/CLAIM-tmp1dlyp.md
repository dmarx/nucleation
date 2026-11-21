---
status: Proposed
title: 'Power laws arise from many mechanisms with no positive feedback: a branching process balanced between extinction and growth, a tuned critical point, first-passage times of a random walk, a mixture of exponential rates, sample-space reduction, steady growth with a spread of ages, and an inverse power of a uniform variable'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  One of the seven constructions shown not to give a power-law tail under
  the conditions A states (a critical branching process with finite
  offspring variance, a symmetric one-dimensional walk, a gamma spread of
  rates, the uniform sample-space-reducing process, exponential ages with
  a common growth rate, X = 1/U), or shown to need a rich-get-richer
  feedback after all.
tags:
- probabilistic-modeling
- complex-systems
- mathematics
date: '2026-11-21'
line:
- formal-apparatus
grounds:
- LIT-tmpchmeb
- LIT-tmpp451l
- LIT-tmpyexjc
- LIT-tmp1b7mm
- LIT-tmpl2b2l
- THEORY-2131
- CASE-tmpi5vfh
summary: >-
  A's catalogue at A5 of the exchange "Rich Get Richer Power Laws"
  (2026-11-20), answering the owner's U3 ("are there other processes that
  manifest power laws?"), with A3's sandpile and Kesten process making ten
  in A5's summary table. Each of the seven constructions was rechecked in
  this session, analytically or by simulation with python3 -I. A's
  unifying theme, "the absence of a characteristic scale", and its
  reasoning's "a hazard proportional to 1/x produces power-law survival"
  are kept as glosses, not as further claims. The works are registered
  and unread. The wording is A's (the other assistant in the exchange
  "Rich Get Richer Power Laws", A5); adopting it is the owner's call.
---
<!-- inactive-ok-file: LIT-tmpchmeb LIT-tmpp451l LIT-tmpyexjc LIT-tmp1b7mm LIT-tmpl2b2l — Deferred; registered from this exchange and not read -->
<!-- inactive-ok-file: THEORY-2131 CASE-tmpi5vfh CLAIM-769 CLAIM-tmpdusls CLAIM-tmpiervv CLAIM-tmp8h6nt QUESTION-tmp21jtb — Proposed or new; held readings and claims, and entries filed with this one -->

# CLAIM-tmp1dlyp: Power laws arise from many mechanisms with no positive feedback: a branching process balanced between extinction and growth, a tuned critical point, first-passage times of a random walk, a mixture of exponential rates, sample-space reduction, steady growth with a spread of ages, and an inverse power of a uniform variable

## The catalogue (A5), each rechecked

A5 opens: "there is a surprisingly large family of processes that generate
power laws, many of which have **nothing to do with rich-get-richer
dynamics, compounding wealth, or self-organized criticality**." Newman's
review (LIT-tmpchmeb) is A's general reference.

1. **Critical branching** (§1). At R = 1 with finite, nonzero offspring
   variance, P(S = s) ∝ s^(−3/2). Checked for Poisson offspring in
   CASE-tmpi5vfh. s^(3/2)·P(S = s) tends to (2π)^(−1/2) = 0.399.
2. **Tuned criticality** (§2). Site percolation on the square lattice,
   p_c ≈ 0.5927, n_s ∝ s^(−τ) with τ = 187/91 ≈ 2.055 in two dimensions.
   The arithmetic checks. The exponent is the standard 2D value, not
   rederived here. The criticality side belongs to the record's
   criticality entries filed from this exchange.
3. **First passage** (§3). A symmetric walk first reaches a boundary at
   time t with probability ∝ t^(−3/2), "connected to the Sparre Andersen
   universality theorem". Checked: (1/t)·P(S_t = −1)·t^(3/2) tends to
   sqrt(2/π) = 0.798 (0.797 at t = 1,001), and simulation matches the
   formula (P(T = 11) 0.0210 simulated, 0.0205 exact). Why the 3/2 is
   shared with item 1 is CLAIM-tmpdusls.
4. **Mixtures** (§4). Exponential waiting times with gamma-distributed
   rates give P(T > t) = (b/(b + t))^a. Checked at a = 1.5, b = 2 by two
   million draws: 0.0680 against 0.0680 at t = 10, 0.00272 against
   0.00275 at t = 100. The record holds this (THEORY-2131, CLAIM-769). A
   adds superstatistics (Beck, LIT-tmp1b7mm) and the warning that "If a
   dataset displays a power law, that does not necessarily mean any
   individual entity follows power-law dynamics". See the note of
   2026-11-21 on CLAIM-769.
5. **Sample-space reduction** (§5). A walk that jumps uniformly to a lower
   state until it reaches 1 visits state k with probability 1/k, Zipf's
   law (Corominas-Murtra, Hanel and Thurner, LIT-tmpp451l, unnamed by
   A). Checked over 200,000 runs from 100: 0.499, 0.199, 0.101 and 0.0201
   at k = 2, 5, 10 and 50.
6. **Growth with a spread of ages** (§6). A common growth rate g and
   exponential ages with rate λ give P(S > s) = (s/S_0)^(−λ/g) (Reed,
   LIT-tmpyexjc). Checked at λ = 1, g = 0.5: 0.0101 against 0.0100 at
   s = 10. "Even **identical growth rates** can coexist with highly
   unequal sizes."
7. **Change of variables and geometry** (§7). X = 1/U gives P(X > x) =
   1/x, density x^(−2). A point uniform in a d-ball with influence r^(−β)
   gives P(F > f) = P(r < f^(−1/β)) = f^(−d/β).

To these A3 adds the sandpile (Bak, Tang and Wiesenfeld, LIT-tmpl2b2l)
and the Kesten process (CLAIM-tmpiervv), and A1 adds preferential
attachment.

## Glosses kept, not filed

- **A's unifier** (A5): "the most productive way to understand the
  diversity of mechanisms is through **the absence of a characteristic
  scale** … Different processes eliminate or obscure characteristic
  scales in different ways." That is close to a definition of a power
  law, so it is kept as a reading aid. Scale invariance as such belongs to
  the record's criticality entries from this exchange.
- **A's reasoning** (A5, not shown): "a hazard proportional to 1/x
  produces power-law survival". Exact: h(x) = α/x gives
  S(x) = exp(−∫α/u du) = (x/x_0)^(−α). It restates the result in hazard
  form, and does not explain why the hazard falls as 1/x.
- **Density and survival exponents.** A moves between P(X = x) ∝ x^(−γ)
  and P(X > x) ∝ x^(−α) without saying α = γ − 1, though its own
  reasoning planned to "separate density from CCDF exponents" (A4). The
  BA model's k^(−3) and k^(−2) (A1) and the cascade's s^(−3/2) and
  s^(−1/2) (A8 §4) are each one law stated both ways.

## What it does not say

- Not that the list is complete, nor that the mechanisms are exclusive
  (A3 §4: "Real complex systems can combine all three").
- Not which mechanism produced any observed tail (CLAIM-tmp8h6nt).
- Not what fixes the exponents (QUESTION-tmp21jtb).
