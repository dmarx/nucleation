---
number: 265
status: Active
formerly:
- THEORY-tmph3haa
title: "In Tissot et al.'s minimal model of bistable deciders in a modular coordination game (thirty modules of ten, couplings 1 within modules and 0.01 across), phase synchronisation within modules, driven only by each unit's local payoff, makes each module respond to the others as a single unit, and synchrony matched to the modules is needed: global synchrony does not"
version: 2
history:
- version: 2
  date: '2026-10-29'
  note: >-
    Promoted by the sixteenth status review, at the status review's
    ruling (the owner delegated these rulings; ADR-057; ADR-047's ruling
    on one study): NOTE-773 read the paper in full, the title claims no
    more than the model showed, and nothing in the record contradicts
    it. The review re-implemented the model from NOTE-773's equations
    and reproduced it with controls (note of 2026-10-29). The title now
    names the paper and its setting. Read as covering any coupling
    ratio, the old wording is contradicted by the re-run, in which
    random phases already reach the optimum once across-module coupling
    is 0.1 or more (ADR-047, kind 3). The old title: In a minimal model
    of bistable deciders in a modular coordination game, phase
    synchronisation within strongly coupled modules, driven only by each
    unit's local payoff, makes each module respond to the others as a
    single unit, and synchrony matched to the modules is needed: global
    synchrony does not. The promote_when asks for a replication outside
    the clean game, which is open scope nobody asserts (kind 4), and
    moves unchanged to QUESTION-337. Its supports entry for
    CLAIM-172 becomes corroborates (ADR-058).
tags:
- agency
- complex-systems
- individuation
date: '2026-10-14'
source:
- LIT-989
summary: >-
  Tissot, Levin, Buckley & Watson (2024), [LIT-989](../literature.d/LIT-989.md), read in full (v1 and
  v2) in [NOTE-773](../notes.d/NOTE-773.md). In a simulated game of 30 modules of 10 units,
  each unit shifts the phase of its decision cycle toward partners it
  currently agrees with. Phases synchronise within modules, each module
  then switches as a block, and 50 of 50 runs with the learned phases
  reach a global optimum against 0 of 50 without; imposed global
  synchrony does not help. It is one clean game, one parameter setting,
  and a postulated phase rule; the modules are built in, and timing finds
  them rather than drawing them. Re-implemented by the sixteenth status
  review: learned phases, and module-matched phases imposed by hand, reach
  the optimum; random, shuffled and global phases do not make modules
  respond as units. The effect matters only where modules are isolated
  enough to lock in.
corroborates:
- CLAIM-172
---
<!-- inactive-ok-file: CLAIM-172 CLAIM-157 THEORY-232 THEORY-069 — Proposed; the entrainment mark, block answer and accounts this bears on, open -->

# THEORY-265: In Tissot et al.'s minimal model of bistable deciders in a modular coordination game (thirty modules of ten, couplings 1 within modules and 0.01 across), phase synchronisation within modules, driven only by each unit's local payoff, makes each module respond to the others as a single unit, and synchrony matched to the modules is needed: global synchrony does not

## Source

Tissot, Levin, Buckley & Watson (2024), [LIT-989](../literature.d/LIT-989.md), bioRxiv
10.1101/2024.02.16.580248, read in full in [NOTE-773](../notes.d/NOTE-773.md) (v2 of
2024-05-17, compared with v1): Model, Experiments and results (Figs. 4–9),
Discussion, Appendix A.

## What was actually shown

A simulation. Units are bistable deciders whose decision cycle
γ_i(t) = (sin(ωt + θ_i) + 1)/2 alternates between a sensitive, inactive
phase and an acting, insensitive one. They play a coordination game with
couplings c_ij = 1 inside modules of ten and 0.01 across (Eq. 1), thirty
modules in all. Each unit adjusts only its phase:
θ_i ← θ_i + ν Σ_j (π/4) c_ij sgn(s_i s_j) sin(θ_j − θ_i) (Eq. 5), so it
moves toward partners it currently agrees with and away from those it
does not.

- **Without the phase rule**, 0 of 50 runs reach a global optimum; each
  module settles and "always re-make[s] the same decision".
- **With it**, phases synchronise within modules, the modules "wake up"
  suddenly (most before t = 20,000), and with the learned phases 50 of 50
  runs from random states reach a global optimum. Blocks of ten switch
  together, "acting like a single macro-scale unit".
- **Control.** Synchrony imposed on all 300 units produces no transition
  and no gain (Fig. 7A).
- **Mechanism, as the authors give it.** When a module's members are
  sensitive at once, none is acting on the others, so the weak external
  pull is the only one left: attention turns "from the ingroup to the
  outgroup". No signal passes inside the module; the authors stress it has
  "no internal computation or information integration".
- **Selection does it too** (Fig. 8), in a 7 × 7 version, about a hundred
  times more slowly.

What could have come out the other way: synchrony could have spread
globally, or formed within modules and changed nothing, as global
synchrony does. The phases moved toward within-module synchrony before
any collective benefit was available (Fig. 5B).

## What this does not say

- **That timing draws the boundary.** The modules are built into c_ij;
  the authors say they "clearly prescribe the boundaries of the
  collectives". Timing finds and enacts a boundary the couplings already
  have.
- **That entrainment as in coupled oscillators does this.** The phase
  rule is a gradient on cycle-averaged payoff, "loosely analogous" to
  Kuramoto entrainment, and Appendix A derives it under an approximation.
  No run uses coupling through the units' outputs.
- **That the module is an agent beyond the minimal sense.** It chooses
  between two collective states so as to lower collective stress, and
  nothing more: no boundary in space, no metabolism, no integration.
- **That it generalises.** One game, clean and consistent modules, one
  parameter setting, no sweep; the authors expect natural interactions to
  be graded and frustrated.
- **That the higher level does anything the micro level does not.** "The
  higher-level agent is not a variable in any of our equations of
  motion." The claim is that the organisation of timing changes outcomes,
  not that a macro variable acts.

## Connections

- **[QUESTION-035](../questions.d/QUESTION-035.md).** A worked case for the first and second clauses
  relative to a stated target (resolving the between-module
  constraints): the unit is the synchronised module, and membership is
  "who is synchronised with whom". On the third clause it shows formation
  and persistence of the learned phases across changed games, not
  dissolution. No `answers:` is declared: it is a case an answer must
  handle, built with the boundary given.
- **[CLAIM-172](../claims.d/CLAIM-172.md).** Corroborates it in the within-module case and sharpens it:
  relative to this target, common timing as such made no unit (the global
  control); timing matched to the strong couplings did. [CLAIM-172](../claims.d/CLAIM-172.md)'s defeat
  condition, which any complete micro simulation like this one met as
  first written, was reworded on 2026-10-14 to ask for descriptive economy
  (its version 6).
- **[CLAIM-157](../claims.d/CLAIM-157.md).** The couplings are nearly decomposable from the start, so
  the block criterion returns the same verdict before and after the
  transition, while the module's behaviour as a unit changes. One system
  by coupling and a responding unit by timing come apart here.
- **[THEORY-232](THEORY-232.md).** The model Watson's essay cites as unpublished. Fig. 6
  computes in effect [THEORY-232](THEORY-232.md)'s comparison of equilibrium energy under
  the old and new organisation, with the decomposition and goals
  stipulated, as [THEORY-232](THEORY-232.md) says they must be.
- **[THEORY-069](THEORY-069.md).** HKB entrainment is through the effectors' coupled
  dynamics; this is through a payoff rule on phase. They share the word
  and the sine term, not the mechanism.

## Note of 2026-10-29: re-run by the status review

The sixteenth status review re-implemented the model from [NOTE-773](../notes.d/NOTE-773.md)'s
equations (v2 Eqs. 3–5: N = 300, k = 10, c_ij = 1 within and 0.01 across,
c_ii = 0, I(x) = clip(100x, ±1), noise uniform ±0.01, ω = 0.01,
ν = 3·10⁻⁵). It learned phases for 30,000 steps, then ran 50 tests of
20,000 steps from random states with the phases frozen. A run counted as a
global optimum if every unit's sign, averaged over the last cycle, was the
same.

- **Learned phases:** within-module phase coherence 0.97–0.99; 50, 50 and
  26 of 50 runs at the optimum for three learning seeds, and 50 of 50 for
  the third after 60,000 learning steps. Every module flip went toward the
  other modules' majority.
- **Random phases:** 0 of 50 for every seed.
- **Learned phases shuffled across units** (the same phases, with the match
  to modules destroyed): 0 of 50.
- **Synchrony matched to modules, imposed by hand:** 50 of 50.
  Module-matched synchrony is what does it.
- **Global synchrony:** 8–19 of 50 runs ended at an optimum, but not by
  modules responding to one another. About 15 of 30 modules flipped each
  cycle, 16% of flips went toward the others' majority, and in 46% of
  cycles more than half the modules flipped at once: the whole system
  resets each cycle and an all-agree state appears transiently. The
  paper's Fig. 7A is reproduced for modules responding as units, not for
  the end state.
- **Self-coupling c_ii = 1:** the same pattern.
- **Beyond the paper's setting:** with within-module couplings graded
  (uniform 0.2–1.8), the result holds at across-coupling 0.01. At 0.03,
  random phases already reach the optimum in about half the runs, and at
  0.1 or more in all of them, so there is no lock-in for timing to undo.
  The slowest phase rate tried, 10⁻⁵, did not synchronise modules within
  30,000 steps. Overlapping modules, frustrated constraints and
  entrainment through the units' outputs were not run; they are
  [QUESTION-337](../questions.d/QUESTION-337.md).

The re-run is the record's own, from a transcription whose figures were
read from their captions only.
