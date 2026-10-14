---
status: Proposed
promote_when: >-
  A close reading of Fritz (2012), the construction the review adapts, or
  of another primary source, that states the general version: for any
  marginal scenario, every nondisturbing family of context distributions
  is realized by jointly measurable POVMs proportional to the identity.
  The review proves it for CHSH and says the extension is
  straightforward. The extension checks by hand (NOTE-tmpmru91), but
  holds on the record's own derivation until a source states it. Refuted
  by a nondisturbing behaviour in some scenario that no family of jointly
  measurable POVMs reproduces. What cannot settle it: arguments that
  trivial POVMs are physically unreasonable. Those are the point of the
  claim, not evidence against it.
title: 'If contexts are defined by joint measurability alone, every nondisturbing correlation, maximally contextual ones included, is realized by trivial measurements on a one-dimensional quantum system, so Kochen–Specker contextuality needs a stronger operational notion of context'
version: 1
tags:
- contextuality
- quantum-foundations
date: '2026-10-14'
source:
- LIT-263
summary: >-
  Budroni, Cabello, Gühne, Kleinmann & Larsson (2022), [LIT-263](../literature.d/LIT-263.md), §IV.B.2,
  Eqs. 27–28, adapting Fritz (2012), read in [NOTE-tmpmru91](../notes.d/NOTE-tmpmru91.md). For a
  nonsignalling p(ab|xy), the POVMs G^{xy}_{ab} = p(ab|xy)𝟙 on a
  one-dimensional space are jointly measurable for each pair and
  reproduce p. So contextuality relative to joint measurability alone is
  trivial, and the review requires contexts of repeatable, nondisturbing
  measurements. Liang, Spekkens & Wiseman's sharpness parameter is the
  other known escape.
---
<!-- inactive-ok-file: THEORY-tmp5c0km — Proposed; the companion account filed from the same reading, named in Connections -->

# THEORY-tmpbf74l: If contexts are defined by joint measurability alone, every nondisturbing correlation, maximally contextual ones included, is realized by trivial measurements on a one-dimensional quantum system, so Kochen–Specker contextuality needs a stronger operational notion of context

## Source

Budroni, Cabello, Gühne, Kleinmann & Larsson (2022), [LIT-263](../literature.d/LIT-263.md), §IV.B.2,
Eqs. 27–28, read in [NOTE-tmpmru91](../notes.d/NOTE-tmpmru91.md). The construction is credited there to
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

The reader checked the extension ([NOTE-tmpmru91](../notes.d/NOTE-tmpmru91.md)). For a marginal
scenario with locally consistent context distributions p_C, set
G^C_{a_C} := p_C(a_C)𝟙. Local consistency makes the induced single-observable
POVMs the same in every context containing them. Each context's
observables are jointly measurable by G^C.

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
- **[THEORY-tmp5c0km](THEORY-tmp5c0km.md)**, from the same reading, gives the structural side.
  Even with contexts fixed, an acyclic compatibility structure cannot be
  contextual.
