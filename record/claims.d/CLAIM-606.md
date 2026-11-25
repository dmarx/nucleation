---
number: 606
status: Proposed
formerly:
- CLAIM-tmp5d91s
title: 'Three ways a localized structure persists'
statement: >-
  A localized structure can persist by an internal balance that needs no
  supply, by a balance of gain and loss that needs a standing supply, or by
  a topological charge that continuous change cannot remove, and the three
  differ in what carries the structure's identity, how it forms and how it
  ends; because thresholds and abrupt ends appear in all of them, even with
  no supply at all, only withdrawing the supply and measuring the outflow
  tells which route a structure is on
version: 5
history:
- version: 2
  date: '2026-11-06'
  note: >-
    THEORY-1504 was promoted on 2026-11-06 as a report of Grelu and
    Akhmediev's account, and the account itself was split off to
    THEORY-1548, Proposed. The claim's table uses the account as
    true, so its ground moves from THEORY-1504 to THEORY-1548
    (ADR-058: a claim that uses a reading's contested thesis keeps it in
    grounds), at the status review's ruling (the owner delegated these
    rulings). The body's citations of NOTE-1688 are unchanged. No status
    changes.
- version: 3
  date: '2026-11-11'
  note: >-
    At the completion of the readiness split (ADR-088,
    2026-11-11): transient-support is now its first line, in place
    of realizability: filed for the withdrawal readings, it bears on
    QUESTION-398 and QUESTION-399, both now first in
    transient-support, and on no realizability-first entry, so it no
    longer carries realizability (ADR-085); it keeps
    distributed-agency, through QUESTION-085 and QUESTION-281. No
    other change.
- version: 4
  date: '2026-11-15'
  note: >-
    A dated note from the exchange "Explain String Theory" (2026-11-15):
    the topological row's identity column read as the kind, not the
    token (CLAIM-694), and three new readings that corroborate the
    routes (THEORY-1869, THEORY-1868). No status change.
- version: 5
  date: '2026-11-15'
  note: >-
    Note of 2026-11-15 added: Zhang et al. (2019) realize the topological
    route in a buckled mechanical metamaterial, whose domain walls persist
    only while a standing compression keeps the states degenerate. The
    table's "How it ends" for the topological row should allow the lifting
    of that constraint. A qualification of the sorting, not of the three
    routes. No status change.
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
- transient-support
- distributed-agency
uses:
- TERM-088
complements:
- CLAIM-604
- CLAIM-600
- CLAIM-597
grounds:
- THEORY-1548
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
<!-- inactive-ok-file: LIT-2969 THEORY-2206 — Unfetched or new; Kosterlitz and Thouless and the lecture read in their place, 2026-11-22 -->
<!-- inactive-ok-file: THEORY-2010 THEORY-2022 THEORY-2032 THEORY-2040 — Proposed; cited in this filing of 2026-11-19 -->
<!-- inactive-ok-file: THEORY-2051 — Proposed; cited in this filing of 2026-11-19 -->
<!-- inactive-ok-file: LIT-2787 — Unfetched; cited in this filing of 2026-11-19 -->
<!-- inactive-ok-file: THEORY-1500 THEORY-1501 THEORY-1506 THEORY-1507 THEORY-1509 THEORY-1548 THEORY-1555 — Proposed; the readings that hold this claim back, cited as open -->
<!-- inactive-ok-file: CLAIM-157 — Proposed; claims, a term and readings this one rests on or extends, cited as open -->

# CLAIM-606: Three ways a localized structure persists

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

[TERM-088](../terms.d/TERM-088.md), which the note above calls not adopted, was adopted on 2026-11-06
and is Active, so it no longer holds the claim. What holds it is its
readings: the topological route rests on [THEORY-1507](../theory.d/THEORY-1507.md), whose source is only
Skimmed ([NOTE-1694](../notes.d/NOTE-1694.md)), and [THEORY-1500](../theory.d/THEORY-1500.md), [THEORY-1501](../theory.d/THEORY-1501.md), [THEORY-1506](../theory.d/THEORY-1506.md) and
[THEORY-1509](../theory.d/THEORY-1509.md) state the conservative, dissipative and oscillon routes
generally and stay Proposed under their strict conditions, as [THEORY-1502](../theory.d/THEORY-1502.md)
does on a Skimmed reading; the dissipative contrast is now grounded on
[THEORY-1548](../theory.d/THEORY-1548.md), the Proposed general form of Grelu and Akhmediev's account.

## Note of 2026-11-06: the Kerr case and [CLAIM-604](CLAIM-604.md)'s scoped clause

The twenty-fifth status review promoted [CLAIM-604](CLAIM-604.md) with its "lacks" clause scoped to repair supplied at a rate set by the supply alone, whatever the structure's state. Read that way, the Kerr soliton is not a counterexample to it: the pump does not depend on the soliton, but the soliton's uptake of it does, since its gain is parametric and drawn through its own field ([NOTE-1692](../notes.d/NOTE-1692.md)). That is [CLAIM-604](CLAIM-604.md)'s first case, state-dependent uptake from a fixed flux. So the qualification above rests on the oscillon, which shows a formation window and an abrupt end with no supply at all, and on the Kerr case only as an instance of thresholds and path dependence arising under a supply the structure does not control. The point that the signatures do not by themselves identify self-maintenance stands on the oscillon. No status changes.

## Note of 2026-11-06: Fodor and Tong read further

[THEORY-1502](../theory.d/THEORY-1502.md) is narrowed to what Fodor derives and is Active. The oscillon row uses only its
derived clauses (a radiation rate exponentially small in amplitude; in one and two dimensions no
decay, for small and moderate amplitudes), so that ground no longer holds the claim; the wider
statement is [THEORY-1555](../theory.d/THEORY-1555.md), which the claim does not use. The topological row's "by meeting an
opposite charge" needs two qualifications. Tong's own vortex-antivortex annihilation is "expected
(at least for suitably slow collisions)", assumed, not derived ([NOTE-1694](../notes.d/NOTE-1694.md)). And in integrable
sine-Gordon, kink and antikink "go through each other without any change in their velocity", while
in φ4 they can collide into an oscillon (Fodor, [NOTE-1698](../notes.d/NOTE-1698.md), Ch. 1): opposite charges need not
annihilate, and whether they do is a fact about the theory, not about topology. [THEORY-1507](../theory.d/THEORY-1507.md) stays
Proposed, so the topological route still holds the claim. No status changes.

## Note of 2026-11-15: the charge carries the kind, and two vortex readings
<!-- inactive-ok-file: CLAIM-694 CASE-266 THEORY-1869 THEORY-1868 NOTE-1950 NOTE-1951 LIT-2613 LIT-2611 — Proposed, Skimmed, Unavailable or new; the entries filed from the exchange of 2026-11-15, cited in its note -->

From the exchange "Explain String Theory" (2026-11-15, A3–A5), filed with Czubak & Jerrard ([NOTE-1950](../notes.d/NOTE-1950.md)) and Van Gorder ([NOTE-1951](../notes.d/NOTE-1951.md)), each read as a stand-in for a work not reached (Nielsen & Olesen 1973, [LIT-2613](../literature.d/LIT-2613.md); Hasimoto 1972, [LIT-2611](../literature.d/LIT-2611.md)).

- **The topological row's identity column.** "What carries its identity: the charge" holds for the kind and the net count, not for the token. Two φ⁴ kinks of equal charge and energy sit anywhere. A winding-two vortex sector can be one core or two, and above critical coupling the symmetric single core is unstable ([CASE-266](../cases.d/CASE-266.md), [CLAIM-694](CLAIM-694.md)). So on this route the charge protects the sector. Which structure persisted is fixed by dynamics the charge does not govern. The table is otherwise unchanged.
- **The topological route as an extended object.** Czubak and Jerrard prove that, where Jaffe and Taubes's conjecture holds, a thin vortex line of the abelian Higgs model follows a Nambu–Goto worldsheet for a finite time ([THEORY-1869](../theory.d/THEORY-1869.md)). That corroborates the route for a structure that moves as a string. It says nothing about how such a line forms or ends.
- **The integrable route on a carrier.** Hasimoto's soliton is a localized pattern of a vortex filament's curvature and torsion. With weak friction it persists and "would dissipate at a rate proportional to at most α²" (Van Gorder, [THEORY-1868](../theory.d/THEORY-1868.md)). That fits the integrable row's "under loss it shrinks while keeping its shape". It adds a case the table does not consider: a soliton whose carrier is itself a persisting structure, assumed in the model, not derived. The structure and the soliton are individuated at different levels.

No status changes.

## Note of 2026-11-15: Zhang et al. (2019), read: kinks that persist only under a standing compression

<!-- inactive-ok-file: THEORY-1893 — Proposed; the reading of 2026-11-15, cited as a qualification of the claim's table, nothing here rests on it -->

Zhang, Li, Zheng, Genin and Chen ([LIT-2657](../literature.d/LIT-2657.md), read in [NOTE-1992](../notes.d/NOTE-1992.md)) build the topological route in a mechanical metamaterial. Compressed past a critical strain, each cell of a perforated elastomer buckles into one of two mirror rotations, and the walls between domains are the static kink–antikink lattice of the φ⁴ equation ([THEORY-1893](../theory.d/THEORY-1893.md)). Each wall is a topological defect between degenerate minima. But it persists only while the compression holds the double well: below the critical strain the cells are monostable and the walls are gone. With net charge "Q=0, which indicates each kink is followed by an antikink", no single kink is globally protected, and the walls' positions are held by lattice ("Perierls-Nabarro", sic) pinning.

So the route's "charge that continuous change cannot remove" can depend on a standing constraint that keeps the degenerate states in existence. That constraint is not a supply, since nothing is consumed and no outflow is replenished. The claim's test of withdrawing the supply and measuring the outflow would class these walls with the internal-balance route: they show no outflow. Withdrawing the constraint ends them, as withdrawing a pump ends a dissipative soliton. The table's "How it ends" for the topological row should allow "when the constraint that makes the states degenerate is lifted" beside "by meeting an opposite charge, or at a boundary". The reading qualifies the claim's sorting. It does not contest the three routes. Its "topological" is the kink sense, not Kane–Lubensky polarization. No status change.

## Note of 2026-11-19: the exchange "Topological protection explained"

A separates two topologies (A4 §1, A7 §2–3). The order-parameter manifold decides whether a defect is stable, which is this claim's topological route. The excitation operator in the defect's background decides whether it binds modes, as in Jackiw–Rebbi. Neither implies the other: "A domain wall may be topologically stable without hosting protected electronic modes" (A4 §1). The row is about the first only.

A15 §2 lists learned-network carriers as candidate instances of the routes: phase-locked regions, travelling waves, domain walls and regenerative patterns. The one read case is [THEORY-2051](../theory.d/THEORY-2051.md), a stand-in for the owner's U6 example ([LIT-2787](../literature.d/LIT-2787.md), Unfetched). In its convolutional U(1) recurrent network, vortices form in ± pairs and annihilate on contact, as the topological row expects. No functional role for them is shown. Whether the walls coincide with predictive or causally operative structures is [QUESTION-491](../questions.d/QUESTION-491.md). Whether modes bound to a defect could come to maintain it is [QUESTION-490](../questions.d/QUESTION-490.md).

No status change.

## Note of 2026-11-19: readings for the exchange "Topological protection explained"

Teo and Kane ([THEORY-2022](../theory.d/THEORY-2022.md)), read, classify defects by the winding of the electronic Hamiltonian around them, not by an order-parameter charge. Their topology protects bound gapless modes while the bulk gap is open, not the defect's persistence; in a disordered weak topological insulator the modes even outlive the structure that produced them. So a protected bound mode is no evidence that its host is on the topological route, and the table's topological row should be read as order-parameter topology only. It qualifies the claim.

Rudner and colleagues ([THEORY-2040](../theory.d/THEORY-2040.md)), read, add a third sense of "topological": an invariant of a periodic process, a loop of evolution operators, neither a field configuration's charge ([THEORY-1507](../theory.d/THEORY-1507.md)) nor a static Hamiltonian's winding around a defect. What it protects exists only while the drive runs, so it sits with the supplied route as much as with the topological one. It qualifies the sorting.

Shankar and colleagues ([THEORY-2032](../theory.d/THEORY-2032.md)), read, describe active-nematic defects that carry a conserved charge but are produced and kept unbound by a standing supply, activity; in passive media the flows are "transient". The charge constrains creation and ending (pairs in two dimensions), and the supply decides whether defects exist and how many. One structure can thus sit on the topological and the supplied routes at once, which qualifies the claim's sorting: the routes are not exclusive.

Omidvar and colleagues ([THEORY-2010](../theory.d/THEORY-2010.md)), read: their stored bits persist by bistability under a standing compression, and the "topological" of their title refers to the band polarization at the wall, not to a conserved charge of the wall. That is a further case for the note of 2026-11-15, and a reason to tie the word "topological" to a stated invariant. It qualifies the claim.

No status change.

## Note of 2026-11-22: Kosterlitz's Nobel lecture, read

A **parallel**, from the same passage as [CLAIM-694](CLAIM-694.md)'s note of this date
([LIT-3053](../literature.d/LIT-3053.md), [NOTE-2283](../notes.d/NOTE-2283.md), [THEORY-2206](../theory.d/THEORY-2206.md); a stand-in for
Kosterlitz and Thouless, [LIT-2969](../literature.d/LIT-2969.md), Unfetched). The topological row's
"what holds it", "a charge fixed by the field at its boundary", holds at
finite temperature only where the barrier between sectors grows with
system size: ∝ ln L for the planar rotor's winding sectors, "of order
unity" for the 2D Heisenberg model's invariant, which therefore protects
no ordered state (pp. 90–91). The vortices of that case also show the
row's "how it ends": a vortex ends by meeting an antivortex, and the BKT
transition is the temperature at which free pairs unbind. No edge; the
claim's table is about isolated structures, the lecture about a phase.
No status change.
