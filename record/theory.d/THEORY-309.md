---
number: 309
status: Active
formerly:
- THEORY-tmpbf74l
title: 'If contexts are defined by joint measurability alone, every nondisturbing correlation, maximally contextual ones included, is realized by trivial measurements on a one-dimensional quantum system, so Kochen–Specker contextuality needs a stronger operational notion of context'
version: 2
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Promoted to Active, carrying out the promotion audit's decision
    (record/promotion-audit/decisions/THEORY-309.yaml, batch 017, ADR-047).
    The promote_when asked for a primary source stating the general
    version, which the review proves only for CHSH and NOTE-844 checked by
    hand. Under ADR-047 v2 (the owner's rule of 2026-10-19), a checked
    step-by-step re-derivation meets a request for a proof the record does
    not hold. The general construction is written out below under "The
    general scenario". The claim is unchanged.
tags:
- contextuality
- quantum-foundations
date: '2026-10-14'
source:
- LIT-263
summary: >-
  Budroni, Cabello, Gühne, Kleinmann & Larsson (2022), [LIT-263](../literature.d/LIT-263.md), §IV.B.2,
  Eqs. 27–28, adapting Fritz (2012), read in [NOTE-844](../notes.d/NOTE-844.md). For a
  nonsignalling p(ab|xy), the POVMs G^{xy}_{ab} = p(ab|xy)𝟙 on a
  one-dimensional space are jointly measurable for each pair and
  reproduce p. So contextuality relative to joint measurability alone is
  trivial, and the review requires contexts of repeatable, nondisturbing
  measurements. Liang, Spekkens & Wiseman's sharpness parameter is the
  other known escape.
---
<!-- inactive-ok-file: THEORY-303 — Proposed; the companion account filed from the same reading, named in Connections -->

# THEORY-309: If contexts are defined by joint measurability alone, every nondisturbing correlation, maximally contextual ones included, is realized by trivial measurements on a one-dimensional quantum system, so Kochen–Specker contextuality needs a stronger operational notion of context

## Source

Budroni, Cabello, Gühne, Kleinmann & Larsson (2022), [LIT-263](../literature.d/LIT-263.md), §IV.B.2,
Eqs. 27–28, read in [NOTE-844](../notes.d/NOTE-844.md). The construction is credited there to
Fritz (2012, *Rev. Math. Phys.* 24, 1250012), which is not held.

## What was actually shown

Treat CHSH as a contextuality scenario whose contexts are the pairs
{A_x, B_y}, and call a pair a context when its POVMs are jointly
measurable. Joint measurability gives, for each x, y, a POVM G^{xy} with
A^x_a = Σ_b G^{xy}_{ab} and B^y_b = Σ_a G^{xy}_{ab} (Eq. 27). The
resulting correlations are automatically nonsignalling. Conversely, for
any nonsignalling p(ab|xy), put

G^{xy}_{ab} := p(ab|xy)𝟙,  A^x_a := Σ_b G^{xy}_{ab},  B^y_b := Σ_a G^{xy}_{ab}  (Eq. 28),

on a one-dimensional Hilbert space. Nonsignalling is exactly what makes
A^x_a independent of y and B^y_b independent of x. So every pair is
jointly measurable, and every nonsignalling behaviour, the PR box
included, is reproduced. The review states that the argument "extends
straightforwardly to any arbitrary contextuality scenario". The
nondisturbing correlations replace the nonsignalling ones, and with them
"all maximally contextual correlations".

**The general scenario** (checked in [NOTE-844](../notes.d/NOTE-844.md) and re-derived for
the promotion audit, [ADR-047](../decisions.d/ADR-047.md) v2). A marginal scenario has observables X,
each with a finite outcome set O_X, and a cover of contexts C. A behaviour
gives a distribution p_C on O_C = Π_{X∈C} O_X for each context, and it is
nondisturbing when p_C and p_C′ have the same marginal on C ∩ C′.

1. Take the one-dimensional Hilbert space ℂ and its only state, ρ = 1.
2. For each context C and each a_C ∈ O_C, put G^C_{a_C} := p_C(a_C)𝟙. Each
   effect is a non-negative multiple of 𝟙, and they sum to 𝟙, so G^C is a
   POVM on O_C.
3. For X ∈ C, the induced POVM is E^{X,C}_a := Σ_{a_C : a_C(X) = a} G^C_{a_C}
   = p_C|_X(a)𝟙.
4. Nondisturbance on {X} ⊆ C ∩ C′ gives p_C|_X = p_C′|_X. So E^{X,C} does not
   depend on C: each observable is a single POVM E^X, and each context's
   observables are jointly measurable, with G^C as the joint POVM.
5. Born's rule gives tr(ρ G^C_{a_C}) = p_C(a_C), so every context's
   statistics are reproduced. That includes behaviours with no global
   section, such as the PR box and the maximally contextual behaviours.

So if a context is any jointly measurable set, every nondisturbing
behaviour has a quantum realization by effects proportional to the
identity, and contextuality relative to that notion of context marks
nothing.

The review concludes that "when one uses too broad of a notion of
contexts, i.e., joint-measurability alone, contextuality becomes a
trivial property". It adopts contexts made of sequences of
outcome-repeatable, statistically nondisturbing measurements (§IV.B.2,
S.1–S.5).

What could have failed: some nondisturbing behaviour might have needed
genuinely incompatible effects to be realized as jointly measurable
families. None does.

## What this does not say

- **Not that joint measurability is irrelevant.** It is "the minimal
  requirement to define some notion of a context" (§II.B). The claim is
  that it is not sufficient.
- **Not that contextuality is trivial.** For sharp measurements,
  commutativity, joint measurability, nondisturbance and repeatability
  coincide (§II.B, §IV.B.2), and Kochen–Specker contextuality is not
  trivial. The triviality comes from admitting unsharp, here maximally
  unsharp, effects without further constraint.
- **Not the only escape.** Liang, Spekkens & Wiseman (2011) keep joint
  measurability and add a sharpness parameter that raises the
  noncontextual bound, to the algebraic maximum for effects proportional
  to the identity (§IV.B.2). Henson & Sainz (2015) and Kunjwal (2019)
  are cited for other views. Spekkens's generalized contextuality
  sidesteps the issue by identifying effects by their statistics.
- **Nothing about which operational criterion is right outside
  physics.** The review's criterion, sequential repeatability and
  nondisturbance, is built for laboratory measurements.

## Connections

- **[THEORY-012](THEORY-012.md)** defines noncontextuality as gluing context distributions
  to a global one, with the contexts given. This account says the
  definition has empirical content only once the contexts are fixed by
  something stronger than joint measurability.
- **[QUESTION-067](../questions.d/QUESTION-067.md)** asks which noncontextuality assumption a test of
  pragmatic judgements would refute. This account adds a precondition:
  whichever is chosen, what makes two renderings "the same measurement in
  two contexts" cannot rest on joint performability alone.
- **[THEORY-303](THEORY-303.md)**, from the same reading, gives the structural side.
  Even with contexts fixed, an acyclic compatibility structure cannot be
  contextual.
