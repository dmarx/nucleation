---
status: Skimmed
paper: LIT-tmp6hh1r
title: 'Drouin-Touchette, skimmed for the spin-wave power law, the vortex argument and the flow to a line of fixed points, as a stand-in for Kosterlitz and Thouless'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Read in part on 2026-11-22 by a delegated reader from arXiv
    (arxiv.org/pdf/2207.13748v1, v1 of 27 July 2022, 43 pp.), as a
    stand-in for Kosterlitz and Thouless (1973), LIT-2969, whose IOP copy
    was stopped by a Cloudflare challenge (ADR-114). Read: §§1–3
    (pp. 2–14) and the passages of §5 on 2D melting and superfluids.
    Skimmed: §4 (Monte Carlo) and §6; the figure on p. 13 not seen; so
    Skimmed. Every quotation below rechecked by the filer by script
    against the downloaded text. No email address sent.
date: '2026-11-22'
summary: >-
  Lecture notes deriving the BKT results for the 2D XY model: spin waves
  give correlations falling as r^(−k_BT/2πJ) at every low temperature,
  with an infinite correlation length ("the system is critical"); a free
  vortex costs (πJn² − 2k_BT) ln(L/a), so k_BT_c = πJ/2 in the simplest
  argument; the RG flow ends on a line of fixed points where the vortex
  fugacity is irrelevant; and the correlation length diverges at T_KT as
  an essential singularity. It credits the RG equations to Kosterlitz
  (1974) and José et al. (1977). The reading is THEORY-tmpaojie.
---
<!-- inactive-ok-file: THEORY-tmpaojie — new; this reading and its companion -->
<!-- inactive-ok-file: LIT-2969 LIT-tmph3tia — Unfetched or Deferred -->
<!-- inactive-ok-file: CLAIM-841 CLAIM-842 CLAIM-846 TERM-139 THEORY-1095 ARG-tmprfa3j CLAIM-tmpvq33w — Proposed or new; the entries the reading bears on -->

# NOTE-tmpurjns: Drouin-Touchette, skimmed for the spin-wave power law, the vortex argument and the flow to a line of fixed points, as a stand-in for Kosterlitz and Thouless

## Contribution

A student-level derivation of the BKT transition, from spin waves to the
RG. The reading is THEORY-tmpaojie.

## Key results

1. **Magnetization** (§2.1, eqs. 8–9): ⟨S_x⟩ = exp(−(T/2J) ln(L/a)) → 0,
   "directly the statement of the Mermin-Wagner theorem".
2. **Spin waves** (§2.2, eq. 18): g(r) ≈ (πr/a)^(−k_BT/2πJ) =
   (πr/a)^(−η(T)): "the correlation function falls off algebraically at
   all finite temperatures", so "the XY model has an infinite correlation
   length ξ = ∞, and η is temperature dependent. This means that, at all
   low-temperatures, the system is critical."
3. **A vortex** (§2.3, eq. 24): ∆F = (πJn² − 2k_BT) ln(L/a), so
   k_BT_c = πJ/2: "This remarkably simple argument from Kosterlitz and
   Thouless is not too far from the truth".
4. **Spin waves have no transition** (§3.1, p. 10): the spin-wave
   partition function "is perfectly analytic", so "we expect all of the
   phase transition properties to come from the topological term".
5. **Line of fixed points** (§3.3, p. 12): the flows terminate "on a line
   of fixed points at which y0 = 0 and K_eff^(−1) ≤ π/2. In this regime,
   the fugacity becomes irrelevant." The RG equations are credited to
   "José, Kirkpatrick, Kadanoff and Nelson in 1977", with Kosterlitz
   (1974) as ref. [5].
6. **Not a power-law transition** (§3.4, eq. 50, p. 14):
   ξ ≈ a exp((π²/8b)√(T_KT/(T − T_KT))), diverging "not in the same way as
   usual second-order phase transitions"; the free energy "only has an
   essential singularity"; §1 calls it "an infinite-order phase
   transition".
7. **Realizations** (§5): "These settings were pointed out in the first
   paper by Kosterlitz and Thouless as potential realizations".

## Assumptions

The 2D XY model with nearest-neighbour coupling J; dilute vortices of
unit charge; equilibrium.

## Concepts

Spin waves; quasi-long-range order; vortex fugacity; Coulomb gas; line of
fixed points; essential singularity; infinite-order transition.

## Bearing on the record

- **LIT-2969**: stands in for the results of the BKT line of work, not
  for which of them the 1973 paper states (ADR-114).
- **CLAIM-841** (XY row): **supports, and qualifies two words.** Item 5:
  every T below T_KT flows to the fixed line, where the fugacity is
  irrelevant, so nothing is tuned through the phase (ARG-tmprfa3j). But
  the notes call the low-temperature phase "critical" (item 2): in the
  sense of an infinite correlation length, not of a tuned transition, so
  it does not contradict the claim, whose sense of criticality is the
  tuned one. And the transition that ends the phase is not a power-law
  critical point either: its correlation length diverges as an essential
  singularity (item 6).
- **CLAIM-842**: **qualifies.** Item 1 confirms the d = 2 logarithm. But
  at d = 2 exactly what survives is algebraic order, and the Gaussian
  elastic energy alone has no transition at all (item 4): whether the
  algebraic phase survives is set by defects, which no Gaussian energy
  contains. At d_s = 2 the claim's premise leaves the phase's fate open.
- **QUESTION-508**: the relevant direction, the fugacity y, is held at
  zero over a range of stiffness (item 5); see CLAIM-tmpvq33w.
- **TERM-139**: **an example of the term's sense**: y irrelevant below
  T_KT and relevant above, K marginal along the fixed line.
- **CLAIM-846**: **parallel**; item 2 is a Gaussian spin-wave computation.
- **THEORY-1095**: **contrast.** The equilibrium 2D XY model gets only
  algebraic order; Toner and Tu's true long-range order is what the
  non-equilibrium terms add.

## Limitations

Unrefereed and student-level, with an unresolved cross-reference and
some typos; it does not say which results are in the 1973 paper.
