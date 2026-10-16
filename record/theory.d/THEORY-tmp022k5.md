---
status: Active
title: "A fair lottery on the natural numbers has a uniform, regular probability defined on every set of tickets, by normalised numerosity with values in the hyperrationals; it is fixed only up to a choice of free ultrafilter, it is hyperfinitely and not countably additive, and its standard part is ordinary asymptotic density"
version: 1
tags:
- philosophy-of-mathematics
- epistemology
- mathematics
date: '2026-10-16'
source:
- LIT-163
summary: >-
  Wenmackers (2011), [LIT-163](../literature.d/LIT-163.md), chapter 2, read in [NOTE-139](../notes.d/NOTE-139.md). P_num(A) =
  num(A)/α is defined on all of 𝒫(ℕ), gives each ticket 1/α > 0, and
  satisfies FAIR, ALL and a hypercountable form of SUM (eqs. 2.20–2.27).
  Proved, given the axiom of choice. It is not a free lunch: one solution
  per free ultrafilter, no invariance under relabelling, no countable
  additivity, and by the author's own admission it is empirically
  indistinguishable from the finitely additive real-valued solution.
---
<!-- inactive-ok-file: THEORY-tmpux6wn — Proposed; the companion account from the same thesis, named in Connections -->

# THEORY-tmp022k5: A fair lottery on the natural numbers has a uniform, regular probability defined on every set of tickets, by normalised numerosity with values in the hyperrationals; it is fixed only up to a choice of free ultrafilter, it is hyperfinitely and not countably additive, and its standard part is ordinary asymptotic density

## Source

Wenmackers (2011), [LIT-163](../literature.d/LIT-163.md), the PhD thesis *Philosophy of Probability:
Foundations, Epistemology, and Computation*, chapter 2, read in full in
[NOTE-139](../notes.d/NOTE-139.md) with chapters 1 and 3–6.

## What was actually shown

**The problem.** A fair lottery on ℕ = {1, 2, 3, …} should satisfy four
intuitions (§2.2.1.2): FAIR (every ticket equally likely), ALL (every set
of tickets has a probability), SUM (set probabilities supervene on ticket
probabilities) and LABEL (invariance under relabelling). Real-valued
probability cannot have FAIR with countable additivity, since each ticket
would get 0 and the tickets together 1. The thesis keeps FAIR as
"non-negotiable" and gives up LABEL.

**The construction (eqs. 2.20–2.21).** For a set A, take the partial counts
#(A ∩ {1..n}), take their class num(A) modulo a free ultrafilter U (the
Benci–Di Nasso numerosity, with num(ℕ) = α), and normalise:
P_num(A) = num(A)/α = [⟨#(A ∩ {1..n})/n⟩]_U. Every ticket gets 1/α, ℕ less
one ticket gets 1 − 1/α, and each residue class mod m gets a value whose
standard part is 1/m (§2.6.4.2).

**Additivity (eq. 2.27, §2.5.2).** For disjoint {A_n}, num of the union is a
sum over the hyperextended family indexed by *ℕ, and past some K in *ℕ all
terms vanish, so the additivity is in effect hyperfinite. No function into a
non-standard set can be countably additive, because countable sums are not
defined there (§2.5.2.2).

**The standard part (eq. 2.30).** st ∘ P_num equals the Hahn–Banach
generalised asymptotic density, for every choice of ultrafilter.

**Non-uniqueness (§2.6.2).** There is one solution per free ultrafilter. For
example P_num(Odd) is ½ + 1/(2α) or exactly ½, depending on whether the odd
numbers are in U.

**What could have come out otherwise.** Normalised numerosity could have
failed to be well defined on all of 𝒫(ℕ), or its standard part could have
disagreed with density. [NOTE-139](../notes.d/NOTE-139.md) rates the construction, the additivity
theorem and the standard-part result as strong, by proof.

## What this does not say

- **That the infinite fair lottery is solved uniquely.** Which ultrafilter,
  and so which probabilities for sets like the odd numbers, is left open.
  The author sees "no convincing reasons" to constrain it (§2.6.2).
- **That the probability is countably additive.** The thesis's
  "infinitely additive" means a sum over *ℕ of the star-extended family,
  which collapses to a hyperfinite sum ([NOTE-139](../notes.d/NOTE-139.md), Corrections).
- **That it is preferable to de Finetti's finitely additive solution.**
  The author concedes the two are empirically indistinguishable (§2.6.4),
  so the preference is intuitive (C5, weak).
- **That it is constructive or label-free.** It needs the axiom of choice,
  and probabilities change under relabelling.
- **That it is an endorsement of Regularity in general.** The thesis says
  it is not (§2.2.1.2, §2.7). Its later critics (Pruss, "Infinitesimals are
  too small for countably infinite fair lotteries") are not held in the
  record.
- **That it gives any computational method.** Its standard part is ordinary
  asymptotic density, so nothing here bears on zero-probability events in
  continuous models.

## Connections

- The same "rounding error" diagnosis, carried to belief, gives
  Stratified Belief ([THEORY-tmpux6wn](THEORY-tmpux6wn.md)). The thesis's opinion-dynamics result
  is [THEORY-tmpv2lo3](THEORY-tmpv2lo3.md).
- The ultrafilter machinery is the one Turner presents as propositional
  theories ([LIT-145](../literature.d/LIT-145.md), [THEORY-tmpnz4z2](THEORY-tmpnz4z2.md)).
