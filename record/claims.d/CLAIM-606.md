---
number: 606
status: Proposed
formerly:
- CLAIM-tmp5d91s
title: "A localized structure can persist by an internal balance that needs no supply, by a balance of gain and loss that needs a standing supply, or by a topological charge that continuous change cannot remove, and the three differ in what carries the structure's identity, how it forms and how it ends; because thresholds and abrupt ends appear in all of them, even with no supply at all, only withdrawing the supply and measuring the outflow tells which route a structure is on"
version: 2
history:
- version: 2
  date: '2026-11-06'
  note: >-
    THEORY-1504 was promoted on 2026-11-06 as a report of Grelu and
    Akhmediev's account, and the account itself was split off to
    THEORY-tmppeysf, Proposed. The claim's table uses the account as
    true, so its ground moves from THEORY-1504 to THEORY-tmppeysf
    (ADR-058: a claim that uses a reading's contested thesis keeps it in
    grounds), at the status review's ruling (the owner delegated these
    rulings). The body's citations of NOTE-1688 are unchanged. No status
    changes.
role: thesis
warrant: interpretive
defeated_if: >-
  A localized structure that persists by none of the three routes and is
  not a slowly decaying case of one of them; or evidence that the routes
  cannot be told apart by withdrawing the supply, as a dissipative
  soliton that persists without its pump, or a conservative one that
  ends at once when an outside input stops; or a case in which the
  signatures of threshold and abrupt end occur only where upkeep depends
  on the structure's state, contrary to oscillons and Kerr solitons.
tags:
- complex-systems
- natural-sciences
date: '2026-11-06'
line:
- realizability
- distributed-agency
uses:
- TERM-088
complements:
- CLAIM-604
- CLAIM-600
- CLAIM-597
grounds:
- THEORY-tmppeysf
- THEORY-1500
- THEORY-1506
- THEORY-1502
- THEORY-1507
- THEORY-1509
- THEORY-1501
bears_on:
- QUESTION-085
- QUESTION-398
- QUESTION-399
- QUESTION-281
summary: >-
  The assistant's, after the owner's hunch that "the physics/dynamics of
  soliton formation could be a valuable angle through which to consider
  some of our questions about individuation and persistence". Solitons
  give three routes by which a localized structure persists.
  - Integrable solitons are held by an internal balance and need no
    supply. They come in a family set by their initial data, and they keep
    their identity through collisions.
  - Dissipative solitons are held by a supplied balance of gain and loss.
    Their shape is "predetermined by the equation parameters, rather than
    by the initial conditions", and they last "until the pump laser is
    switched off".
  - Topological solitons carry a charge that continuous change cannot
    remove.
  A fourth case, the oscillon, has none of the three protections. It
  forms only from a window of initial sizes, settles to a common state
  regardless of where it started, holds for a thousand oscillations, and
  then ends abruptly. That bears on two of the record's claims.
  - It qualifies [CLAIM-604](CLAIM-604.md). Thresholds and abrupt ends appear with no
    supply at all, and in Kerr solitons with a supply that does not depend
    on the structure, so they do not identify state-dependent upkeep.
  - It sharpens [CLAIM-600](CLAIM-600.md). Persistence through many turnovers is not
    evidence of self-maintenance.
  The routes are told apart by what happens when the supply is withdrawn
  and by whether an outflow is measured. The wording is the assistant's
  (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-1500 THEORY-1501 THEORY-1502 THEORY-1506 THEORY-1507 THEORY-1509 THEORY-tmppeysf — Proposed; the readings that hold this claim back, cited as open -->
<!-- inactive-ok-file: CLAIM-600 CLAIM-157 NOTE-1698 NOTE-1694 — Proposed or Skimmed; claims, a term and readings this one rests on or extends, cited as open -->

# CLAIM-606: A localized structure can persist by an internal balance that needs no supply, by a balance of gain and loss that needs a standing supply, or by a topological charge that continuous change cannot remove, and the three differ in what carries the structure's identity, how it forms and how it ends; because thresholds and abrupt ends appear in all of them, even with no supply at all, only withdrawing the supply and measuring the outflow tells which route a structure is on

## The three routes, and a fourth case

| | What holds it | What carries its identity | How it forms | How it ends |
|---|---|---|---|---|
| Integrable soliton | dispersion balanced by nonlinearity; no supply | its initial data: one of "a family comprising an infinity of soliton solutions" | from an initial pulse above a minimum size, the rest radiated away | under loss it shrinks while keeping its shape |
| Dissipative soliton | gain balanced by loss on a standing supply | the conditions: "a fixed localised solution" | by a sweep or a writing pulse inside an existence window | when the supply stops or leaves the window |
| Topological soliton | a charge fixed by the field at its boundary | the charge | as a defect between distinct states | by meeting an opposite charge, or at a boundary |
| Oscillon | nothing; it leaks slowly | the common state it settles to | from a window of initial sizes | abruptly, after a long plateau (in three dimensions) |

- **Integrable.** A collision leaves each soliton "unchanged except possibly for a phase shift" (Zabusky and Porter, [NOTE-1689](../notes.d/NOTE-1689.md)). That holds for integrable equations, not for conservative ones in general (Grelu and Akhmediev, [NOTE-1688](../notes.d/NOTE-1688.md)). Under damping "the basic structure of the solitary wave remains the same" while its amplitude runs down, at a rate fixed by the kind of loss (Grimshaw, Smyth and Stepanyants, [NOTE-1687](../notes.d/NOTE-1687.md)). An initial pulse too small forms no soliton. The record has that threshold only as a reader's derivation from a quoted formula ([NOTE-1693](../notes.d/NOTE-1693.md)).
- **Dissipative.** Its shape is "predetermined by the equation parameters, rather than by the initial conditions" (Grelu and Akhmediev). In microresonators the soliton's shape is "fully determined by the resonator parameters and the pump conditions". Only the number and positions of solitons carry history. Solitons are "stable for hours until the pump laser is switched off", and "their persistence requires a source of energy for replenishment" (Herr et al., [NOTE-1692](../notes.d/NOTE-1692.md)). A transient writing beam can switch a cavity soliton on, and it then persists on the standing supply (Grelu and Akhmediev).
- **Topological.** The charge is set by the field at infinity and cannot change under continuous deformation, and opposite charges annihilate (Tong, [NOTE-1694](../notes.d/NOTE-1694.md)). That such a soliton can end only by annihilation or at a boundary is the reader's inference from these points, not Tong's sentence.
- **The oscillon.**
  - It forms only from bubbles in a window of initial radii. It sheds energy to a common state "regardless of their initial radius". It lasts 10³–10⁴ times longer than linear theory allows, then drops into the linear regime and decays quickly (Copeland, Gleiser and Müller, [NOTE-1699](../notes.d/NOTE-1699.md)).
  - Fodor's review ([NOTE-1698](../notes.d/NOTE-1698.md)) gives a radiation rate exponentially small in amplitude, and in one and two dimensions such structures may never decay.
  - Copeland et al. put it in one line: "instability is a relative concept, which only makes sense in context".

## What it changes in the record

- **To [TERM-088](../terms.d/TERM-088.md).** The term's dynamical sense of individuation now has three distinct grounds.
  - An integrable soliton is individuated by its own history: its shape and its identity through collisions.
  - A dissipative soliton is individuated by its conditions. Every soliton in a given resonator has the same shape, and individuals differ only in number and position.
  - A topological soliton is individuated by a conserved charge.

  These are three different answers to what makes a pattern this one rather than another.
- **To [CLAIM-604](CLAIM-604.md), a qualification.** The claim offered three signatures of upkeep drawn in through the structure's own state: an ignition threshold, collapse rather than decline, and an outage it cannot recover from. The readings show the first two without such upkeep.
  - Oscillons have a formation threshold and an abrupt end with no supply at all.
  - Kerr solitons have an existence window and path dependence from bistability under a pump that does not depend on the soliton.

  The signatures are consistent with state-dependent upkeep. They do not identify it.
- **To [QUESTION-085](../questions.d/QUESTION-085.md).** Its test for whether an r/place artwork is a flame or a convection cell leaned on those signatures. The routes are told apart instead by what withdrawing the supply does:
  - a supplied pattern ends when its supply stops;
  - a self-maintaining one may relight if it is above threshold;
  - a structure held by internal balance does not notice.

  For an artwork, the supply to withdraw is its defenders' placement. The ladder also gains a rung below the question's rung of dissipative structures held from outside: a structure held by an internal balance with no flow at all.
- **To [CLAIM-600](CLAIM-600.md), a sharpening.** An oscillon shows almost no outflow for a thousand oscillations and then ends. A damped soliton keeps its shape while it runs down. Persistence through many turnovers is therefore not evidence of self-maintenance. What tells the routes apart is the mechanism together with a measured outflow, the claim's "shape of the feedback".
- **To [QUESTION-398](../questions.d/QUESTION-398.md) and [QUESTION-399](../questions.d/QUESTION-399.md).**
  - A written cavity soliton is independent of the beam that founded it and dependent on the pump that feeds it. That is [CLAIM-597](CLAIM-597.md)'s split between founding and feeding, cleanly instantiated.
  - An integrable soliton is independent of both, but only where nothing is lost.

  Neither is self-maintaining in [QUESTION-399](../questions.d/QUESTION-399.md)'s sense. One needs nothing, and the other is fed.
- **To [CLAIM-157](CLAIM-157.md).** Its pressure that localized structures persist as dynamical individuals while their material turns over holds for the dissipative and oscillon cases. The integrable soliton is a contrast: its material does not turn over.

## What it does not say

- **That organizations are solitons.** The routes are structural analogies. Real organizations lose energy, so the integrable route is an idealization for them. Topological protection's social analogue, if any, is not argued here.
- **That the physics is settled where the readings are thin.** Hysteresis is not named in Herr et al., and no reverse sweep is shown. The formation threshold for integrable solitons rests on a reader's derivation. Whether fine-tuned oscillons live forever is unresolved between Fodor and Gleiser and Krackow. Kivshar and Malomed, Zabusky and Kruskal, Satsuma and Yajima and the dissipative-soliton reviews by Purwins et al. and Akhmediev and Ankiewicz were not read.

## Note of 2026-11-06: what holds it back

Its three routes are the findings of seven Proposed readings, none yet
promoted, and it uses [TERM-088](../terms.d/TERM-088.md), not adopted; two of its supports are by
its own account thin (no reverse sweep in Herr et al., a reader's
derivation for the integrable formation threshold).

## Note of 2026-11-06: what holds it back

TERM-088, which the note above calls not adopted, was adopted on 2026-11-06
and is Active, so it no longer holds the claim. What holds it is its
readings: the topological route rests on THEORY-1507, whose source is only
Skimmed (NOTE-1694), and THEORY-1500, THEORY-1501, THEORY-1506 and
THEORY-1509 state the conservative, dissipative and oscillon routes
generally and stay Proposed under their strict conditions, as THEORY-1502
does on a Skimmed reading; the dissipative contrast is now grounded on
THEORY-tmppeysf, the Proposed general form of Grelu and Akhmediev's account.

## Note of 2026-11-06: the Kerr case and [CLAIM-604](CLAIM-604.md)'s scoped clause

The twenty-fifth status review promoted [CLAIM-604](CLAIM-604.md) with its "lacks" clause scoped to repair supplied at a rate set by the supply alone, whatever the structure's state. Read that way, the Kerr soliton is not a counterexample to it: the pump does not depend on the soliton, but the soliton's uptake of it does, since its gain is parametric and drawn through its own field ([NOTE-1692](../notes.d/NOTE-1692.md)). That is [CLAIM-604](CLAIM-604.md)'s first case, state-dependent uptake from a fixed flux. So the qualification above rests on the oscillon, which shows a formation window and an abrupt end with no supply at all, and on the Kerr case only as an instance of thresholds and path dependence arising under a supply the structure does not control. The point that the signatures do not by themselves identify self-maintenance stands on the oscillon. No status changes.
