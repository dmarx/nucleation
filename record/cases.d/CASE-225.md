---
number: 225
status: Proposed
formerly:
- CASE-tmpecdgv
title: 'A forced Stuart–Landau oscillator: a self-sustained and a damped one give the same drive-locked output; an inhibitory control above μ holds the self-sustained one at rest while it still answers the drive with amplitude about F/√((u − μ)² + (Ω − ω)²); withdrawing the drive alone lets the output die, withdrawing drive and control restores the limit cycle of radius √μ, so dependence for timing, dependence for performance and suppression of a latent capacity are three things'
version: 2
history:
- version: 2
  date: '2026-11-10'
  note: >-
    Moves from readiness to transient-support, at the split of
    readiness (ADR-087, 2026-11-10): the entry is in that
    part's account. No other change.
standing: fictional
kind: construction
tags:
- complex-systems
- control-theory
- self-governance
date: '2026-11-07'
line:
- realizability
- distributed-agency
- transient-support
illustrates:
- CLAIM-414
- CLAIM-522
- CLAIM-616
summary: >-
  A's, from A9 §2 and A12 §4–4.1 of the exchange "Individuation,
  Possibility, and Disposition" (2026-11-06 to 07). The forced
  Stuart–Landau oscillator, with and without an inhibitory control,
  separates dependence for timing, dependence for performance and
  suppression of a capacity that is not destroyed. The reader reran the
  numbers. A's caveat is kept: none of this says whether the control is
  coercive. The wording is A's; adopting it is the owner's call.
---
<!-- inactive-ok-file: LIT-2234 — filed from the same exchange, Deferred -->
<!-- inactive-ok-file: CLAIM-545 — Proposed; cited for its domination clause -->

# CASE-225: A forced Stuart–Landau oscillator: a self-sustained and a damped one give the same drive-locked output; an inhibitory control above μ holds the self-sustained one at rest while it still answers the drive with amplitude about F/√((u − μ)² + (Ω − ω)²); withdrawing the drive alone lets the output die, withdrawing drive and control restores the limit cycle of radius √μ, so dependence for timing, dependence for performance and suppression of a latent capacity are three things

## The case

From A9 §2 and A12 §4.1 of the exchange "Individuation, Possibility, and
Disposition" (https://chatgpt.com/share/6aee7a9b-f13c-83e9-a865-6a29c2c3ff7e).
The model is ż = (μ − u + iω − |z|²)z + Fe^{iΩt}.

- **Without control (u = 0).** A self-sustained oscillator (μ > 0) and a
  damped one (μ < 0) both answer the drive. A9: "Both systems can exhibit a
  periodic response locked to an external signal, yet one possesses an
  endogenous oscillatory capacity and the other does not."
- **With control u > μ > 0.** The unforced system rests. With F > 0 it still
  gives a driven output, of small-amplitude size
  F/√((u − μ)² + (Ω − ω)²). A12: "The distinction cannot be recovered from
  the output alone."
- **Two withdrawals.** Remove F and keep u: the output decays to rest. Remove
  F and u: the limit cycle returns. A12: the capacity "is prevented from
  becoming expressed while \(u\) is active", not destroyed.

The reader reran it with μ = 0.5, u = 1, ω = 1, F = 0.02, Ω = 1.3. The
simulated amplitude is 0.03428 against the predicted 0.03430. Removing F
with u kept gives |z| ≈ 4 × 10⁻³⁶. Removing both gives |z| = 0.7075,
against √μ ≈ 0.7071.

## What it can show

**It separates dependences.** A12 §4 lists five: timing, performance,
maintenance, formation and governance. Maintenance and formation are
[TERM-100](../terms.d/TERM-100.md)'s senses of provenance, and governance from outside is [CLAIM-404](../claims.d/CLAIM-404.md)'s.
The case adds two that come apart. A self-sustained oscillator under drive
depends on the drive for its phase, not for its capacity. A damped one
depends on it for its performance. A suppressed one has a capacity that is
latent, not lost.

**It is [CLAIM-414](../claims.d/CLAIM-414.md)'s and [CLAIM-522](../claims.d/CLAIM-522.md)'s point in an oscillator.** The output
under drive does not tell the three apart; only the withdrawals do.

**Suppression is not atrophy.** A12: "If the suppressive intervention also
changes a slow capacity variable, however, temporary inhibition could become
a lasting loss of capability." "That would move from **suppression** to
**atrophy**." That is [CLAIM-602](../claims.d/CLAIM-602.md)'s and [CLAIM-605](../claims.d/CLAIM-605.md)'s disuse decay, which this
model, with no slow variable, lacks.

## What it cannot show

It is fictional by construction: it shows what is coherent, not what is
common. It does not say whether a control is coercive. A12 §4.3: "The
dynamics alone do not establish the normative relationship." Whether control
is legitimate is [CLAIM-545](../claims.d/CLAIM-545.md)'s question of domination, not the model's. The
literature A cites for oscillation quenching is a 2013 *Physics Reports*
review, doi:10.1016/j.physrep.2013.06.001, which A attributes to Saxena,
Prasad and Ramaswamy. Crossref gives that DOI to Koseska, Volkov and
Kurths, "Oscillation quenching mechanisms", registered unread as
[LIT-2234](../literature.d/LIT-2234.md).
