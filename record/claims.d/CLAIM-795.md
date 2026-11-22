---
number: 795
status: Proposed
formerly:
- CLAIM-tmp1dlyp
title: 'Power laws arise from many mechanisms with no positive feedback: a branching process balanced between extinction and growth, a tuned critical point, first-passage times of a random walk, a mixture of exponential rates, sample-space reduction, steady growth with a spread of ages, and an inverse power of a uniform variable'
version: 2
history:
- version: 2
  date: '2026-11-22'
  note: >-
    Edited in place on 2026-11-22 after Newman's review (LIT-2976) was
    read: the review is said to ground items 2, 3, 6 and 7 only, item 3
    notes Newman's first-return derivation, the summary no longer calls
    all the works unread, and THEORY-tmp6jdas replaces LIT-2976 in
    grounds (ARG-tmp3ppjy). Newman's further mechanisms are in the note
    of that date. The thesis and status are unchanged.
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
- LIT-2997
- LIT-3007
- LIT-2962
- LIT-2992
- THEORY-2131
- CASE-303
- THEORY-tmp6jdas
summary: >-
  A's catalogue at A5 of the exchange "Rich Get Richer Power Laws"
  (2026-11-20), answering the owner's U3 ("are there other processes that
  manifest power laws?"), with A3's sandpile and Kesten process making ten
  in A5's summary table. Each of the seven constructions was rechecked in
  this session, analytically or by simulation with python3 -I. A's
  unifying theme, "the absence of a characteristic scale", and its
  reasoning's "a hazard proportional to 1/x produces power-law survival"
  are kept as glosses, not as further claims. Newman's review, read on
  2026-11-22, grounds items 2, 3, 6 and 7 and adds four further
  mechanisms; the other works are registered and unread. The wording is A's (the other assistant in the exchange
  "Rich Get Richer Power Laws", A5); adopting it is the owner's call.
bears_on:
- QUESTION-505
---
<!-- inactive-ok-file: THEORY-tmp6jdas ARG-tmp3ppjy LIT-tmppzucs LIT-tmp2octb LIT-tmp1db7e LIT-tmpf9hct — Proposed or Deferred; Newman's reading, the argument for it, and the works it names for the further mechanisms, registered and unread -->
<!-- inactive-ok-file: LIT-2997 LIT-3007 LIT-2962 LIT-2992 — Deferred; registered from this exchange and not read -->
<!-- inactive-ok-file: THEORY-2131 CASE-303 CLAIM-769 CLAIM-815 CLAIM-824 CLAIM-803 THEORY-2150 — Proposed or new; held readings and claims, and entries filed with this one -->

# CLAIM-795: Power laws arise from many mechanisms with no positive feedback: a branching process balanced between extinction and growth, a tuned critical point, first-passage times of a random walk, a mixture of exponential rates, sample-space reduction, steady growth with a spread of ages, and an inverse power of a uniform variable

## The catalogue (A5), each rechecked

A5 opens: "there is a surprisingly large family of processes that generate
power laws, many of which have **nothing to do with rich-get-richer
dynamics, compounding wealth, or self-organized criticality**." Newman's
review (LIT-2976) is A's general reference; read on 2026-11-22, it
grounds items 2, 3, 6 and 7 only (THEORY-tmp6jdas, ARG-tmp3ppjy).

1. **Critical branching** (§1). At R = 1 with finite, nonzero offspring
   variance, P(S = s) ∝ s^(−3/2). Checked for Poisson offspring in
   [CASE-303](../cases.d/CASE-303.md). s^(3/2)·P(S = s) tends to (2π)^(−1/2) = 0.399.
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
   shared with item 1 is [CLAIM-815](CLAIM-815.md). Newman (§IV.C) gives the same 3/2
   for the first return of a symmetric walk to the origin, by generating
   functions.
4. **Mixtures** (§4). Exponential waiting times with gamma-distributed
   rates give P(T > t) = (b/(b + t))^a. Checked at a = 1.5, b = 2 by two
   million draws: 0.0680 against 0.0680 at t = 10, 0.00272 against
   0.00275 at t = 100. The record holds this ([THEORY-2131](../theory.d/THEORY-2131.md), [CLAIM-769](CLAIM-769.md)). A
   adds superstatistics (Beck, [LIT-2962](../literature.d/LIT-2962.md)) and the warning that "If a
   dataset displays a power law, that does not necessarily mean any
   individual entity follows power-law dynamics". See the note of
   2026-11-21 on [CLAIM-769](CLAIM-769.md).
5. **Sample-space reduction** (§5). A walk that jumps uniformly to a lower
   state until it reaches 1 visits state k with probability 1/k, Zipf's
   law (Corominas-Murtra, Hanel and Thurner, [LIT-2997](../literature.d/LIT-2997.md), unnamed by
   A). Checked over 200,000 runs from 100: 0.499, 0.199, 0.101 and 0.0201
   at k = 2, 5, 10 and 50.
6. **Growth with a spread of ages** (§6). A common growth rate g and
   exponential ages with rate λ give P(S > s) = (s/S_0)^(−λ/g) (Reed,
   [LIT-3007](../literature.d/LIT-3007.md)). Checked at λ = 1, g = 0.5: 0.0101 against 0.0100 at
   s = 10. "Even **identical growth rates** can coexist with highly
   unequal sizes."
7. **Change of variables and geometry** (§7). X = 1/U gives P(X > x) =
   1/x, density x^(−2). A point uniform in a d-ball with influence r^(−β)
   gives P(F > f) = P(r < f^(−1/β)) = f^(−d/β).

To these A3 adds the sandpile (Bak, Tang and Wiesenfeld, [LIT-2992](../literature.d/LIT-2992.md))
and the Kesten process ([CLAIM-824](CLAIM-824.md)), and A1 adds preferential
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
- Not which mechanism produced any observed tail ([CLAIM-803](CLAIM-803.md)).
- Not what fixes the exponents ([QUESTION-505](../questions.d/QUESTION-505.md)).

## Note of 2026-11-21: Mitzenmacher, read

Mitzenmacher's review ([LIT-3003](../literature.d/LIT-3003.md), read in [NOTE-2237](../notes.d/NOTE-2237.md); the reading is
[THEORY-2150](../theory.d/THEORY-2150.md)) **corroborates item 6** and **finds two omissions**.

- **Item 6.** §7: a lognormal of mean 0 and variance t, stopped at an
  exponential time of rate λ, has density ∝ x^(−1−√(2λ)) above 1 and
  x^(−1+√(2λ)) below, Reed's double Pareto. That is item 6 with zero
  drift instead of a common rate g, and with the exponent then set by the
  variance against the stopping rate. Checked by the filer (python3 -I):
  the integral at λ = ½ gives 0.00500 and 0.0000500 at x = 10 and 100,
  against √(λ/2)·x^(−1−√(2λ)).
- **Left out: random typing.** Miller's monkeys (§6), typing letters and a
  space at random, give Zipf's law in word frequencies with no feedback,
  no criticality and no optimization: with equal letter probabilities the
  frequency of a word falls as a power of its rank. It belongs on this
  list.
- **Left out: optimization.** Mandelbrot's derivation (§4), minimizing the
  cost per unit of information of a code, gives a power law in rank;
  Carlson and Doyle's highly optimized tolerance is cited as a modern
  version. No positive feedback is involved, though an optimizer is.

The catalogue is A's and does not claim completeness ("What it does not
say"), so these are additions, not defeaters. [THEORY-2150](../theory.d/THEORY-2150.md)
`corroborates` this claim. Status unchanged.

## Change of 2026-11-22

Newman's review read: the line calling it A's general reference now says
it grounds items 2, 3, 6 and 7 only; item 3 notes his first-return
derivation; the summary is updated; THEORY-tmp6jdas replaces LIT-2976 in
`grounds`. Version 2.

## Note of 2026-11-22: Newman, read

Newman's review (LIT-2976, read in NOTE-tmpa7yd2; the reading is
THEORY-tmp6jdas) **grounds items 2, 3, 6 and 7**, **leaves items 1, 4 and
5 open**, and **adds four mechanisms** (ARG-tmp3ppjy).

- **Item 2.** Percolation at p_c = 0.5927462, and a coarse-graining
  argument that the cluster distribution is a power law at the critical
  point (§IV.E); no value of τ.
- **Item 3.** "So the distribution of return times follows a power law
  with exponent α = 3/2" (§IV.C, p. 16), for the first return to the
  origin, not first passage to a boundary.
- **Item 6.** Reed and Hughes as a combination of exponentials (§IV.A):
  y exponential with rate a and x ∝ e^(by) give α = 1 − a/b; with
  a = −λ, b = g this is the density exponent 1 + λ/g, the item's survival
  exponent λ/g (checked, python3 -I).
- **Item 7.** x = 1/y gives p(x) ∝ x^(−2), and x = y^(−γ) gives
  α = 1 + 1/γ (§IV.B); not the d-ball geometry.
- **Not in the review**: critical branching (item 1), mixtures of
  exponential rates (item 4; Newman's "combinations of exponentials" is
  item 6's mechanism, not a mixture), sample-space reduction (item 5).
- **Further mechanisms with no rich-get-richer feedback**, which the
  catalogue lacks: Miller's random typing (§IV.A; LIT-tmppzucs, already
  noted from Mitzenmacher), highly optimized tolerance (§IV.G; Carlson and
  Doyle, LIT-tmp2octb), coherent noise (§IV.G; Sneppen and Newman,
  LIT-tmp1db7e) and record dynamics, waiting times between records with
  exponent 1 (§IV.G; Sibani and Littlewood, LIT-tmpf9hct). Highly
  optimized tolerance involves an optimizer, as Mitzenmacher's
  optimization does. The catalogue does not claim completeness, so these
  are additions, not defeaters.

Status unchanged.
