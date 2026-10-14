---
status: Proposed
promote_when: >-
  A replication outside the authors' clean game: modules that overlap,
  couplings of graded strength, or frustrated constraints, together with
  a sweep of the coupling ratio and the phase rate, showing that
  payoff-driven synchrony still forms along the strong couplings and still
  turns those groups into units that switch as one. A second route would
  settle more: the same result with entrainment through the units' own
  outputs (a Kuramoto or HKB coupling) instead of a payoff gradient on
  phase. It fails if the effect disappears once modules overlap or the
  ratio of within to across coupling falls toward one. What cannot
  settle it: more runs of the same 30-by-10 game, or biological
  synchrony cited by analogy.
title: "In a minimal model of bistable deciders in a modular coordination game, phase synchronisation within strongly coupled modules, driven only by each unit's local payoff, makes each module respond to the others as a single unit, and synchrony matched to the modules is needed: global synchrony does not"
version: 1
tags:
- agency
- complex-systems
- individuation
date: '2026-10-14'
source:
- LIT-989
summary: >-
  Tissot, Levin, Buckley & Watson (2024), [LIT-989](../literature.d/LIT-989.md), read in full (v1 and
  v2) in [NOTE-tmp9ypte](../notes.d/NOTE-tmp9ypte.md). In a simulated game of 30 modules of 10 units,
  each unit shifts the phase of its decision cycle toward partners it
  currently agrees with. Phases synchronise within modules, each module
  then switches as a block, and 50 of 50 runs with the learned phases
  reach a global optimum against 0 of 50 without; imposed global
  synchrony does not help. It is one clean game, one parameter setting,
  and a postulated phase rule; the modules are built in, and timing finds
  them rather than drawing them.
---
<!-- inactive-ok-file: CLAIM-172 CLAIM-157 THEORY-232 THEORY-069 — Proposed; the entrainment mark, block answer and accounts this bears on, open -->

# THEORY-tmph3haa: In a minimal model of bistable deciders in a modular coordination game, phase synchronisation within strongly coupled modules, driven only by each unit's local payoff, makes each module respond to the others as a single unit, and synchrony matched to the modules is needed: global synchrony does not

## Source

Tissot, Levin, Buckley & Watson (2024), [LIT-989](../literature.d/LIT-989.md), bioRxiv
10.1101/2024.02.16.580248, read in full in [NOTE-tmp9ypte](../notes.d/NOTE-tmp9ypte.md) (v2 of
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
- **[CLAIM-172](../claims.d/CLAIM-172.md).** Supports it in the within-module case and sharpens it:
  relative to this target, common timing as such made no unit (the global
  control); timing matched to the strong couplings did. [CLAIM-172](../claims.d/CLAIM-172.md)'s
  defeat condition is met trivially by any complete micro simulation
  like this one, which suggests it needs rewording (see [NOTE-tmp9ypte](../notes.d/NOTE-tmp9ypte.md)).
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
