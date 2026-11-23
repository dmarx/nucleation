---
number: 366
status: Proposed
formerly:
- CASE-tmpn19tk
title: 'The three-perspective agenda model, run in numpy: with the latent Condorcet cycle W beats R, R beats S, S beats W held fixed, a chair installs any of the three options by leaving one contest off the agenda, a successive agenda elects the option introduced last, and raising the suppressed contest''s admission probability from nil to certain drops the share of coherent records from one to nil while recorded conflict rises from nil to its maximum, so the recorded outcome and the potential read off it are a function of admission, not of preference'
version: 1
standing: documented
kind: executed-study
tags:
- game-theory
- self-governance
- mathematics
date: '2026-11-22'
line:
- distributed-agency
- organizational-affect
illustrates:
- CLAIM-448
variant_of:
- CASE-221
bears_on:
- QUESTION-269
---
<!-- inactive-ok-file: CASE-221 — Proposed; the hand construction of the smallest case this study generalizes -->
<!-- inactive-ok-file: CLAIM-451 — Proposed; the nonintegrability-degree claim whose measure this study computes, cited in prose -->
<!-- inactive-ok-file: CLAIM-440 — Proposed; the valence claim whose part 3 this study bears on, cited in prose -->

# CASE-366: The three-perspective agenda model, run in numpy: with the latent Condorcet cycle W beats R, R beats S, S beats W held fixed, a chair installs any of the three options by leaving one contest off the agenda, a successive agenda elects the option introduced last, and raising the suppressed contest's admission probability from nil to certain drops the share of coherent records from one to nil while recorded conflict rises from nil to its maximum, so the recorded outcome and the potential read off it are a function of admission, not of preference

## The case

[CLAIM-448](../claims.d/CLAIM-448.md) names, under "What would settle it", a three-perspective
agenda model with a latent Condorcet cycle in which a chair or legibility
regime controls which pairwise contests enter the record. [CASE-221](CASE-221.md) built
the smallest case by hand and showed [CLAIM-448](../claims.d/CLAIM-448.md)'s existence half in one
round; it did not show persistence, the effect of raising legibility, or a
regime more general than a two-contest chair. This is that model as an
executed study, in numpy, generalizing [CASE-221](CASE-221.md) over admission rules and
across windows.

**The fixed cycle.** Three perspectives after [CLAIM-451](../claims.d/CLAIM-451.md)'s example:
productivity W ≻ R ≻ S, recovery R ≻ S ≻ W, belonging S ≻ W ≻ R. By pairwise
majority W beats R, R beats S and S beats W, each 2-1. The full contest graph
is a 3-cycle: no ordinal potential describes it ([TERM-077](../terms.d/TERM-077.md)), and its
nonintegrability degree, the minimum feedback-arc fraction ([CLAIM-451](../claims.d/CLAIM-451.md)), is
1/3. These preferences are held fixed through every rule below.

**What the record shows under each admission rule.** The code is
`scratch/studies/lead-123/agenda_model.py`, run with `python3 -I`; tests in
`test_agenda_model.py` (9, all passing); the run in `results.json`.

- **Chair control.** A chair who admits all contests but one gets an acyclic
  record whatever it drops. Dropping R–S names S; dropping R–W names R;
  dropping S–W names W. So the chair can install **any** of the three options
  as the recorded winner by choosing which single contest to leave off the
  agenda. The agenda-setter's power over a majority cycle is classical social
  choice; here it is the mechanism of a legibility regime ([TERM-064](../terms.d/TERM-064.md)).
- **Agenda order.** The successive (amendment) procedure, the survivor meeting
  each next option in a pairwise vote, elects the option introduced **last**:
  against a 3-cycle the last entrant wins the one arc it needs. All three
  options are reachable across the six orders. The outcome is fixed by the
  order of business, not by the preferences.
- **Legibility filter.** A regime that admits each contest independently with a
  probability. Suppressing any one contest with certainty leaves a record that
  is always coherent and names a fixed winner.
- **Protected challenge channel** ([CLAIM-448](../claims.d/CLAIM-448.md)'s prediction). Two contests
  admitted with certainty; the third, the marginalized perspective's objection,
  admitted with probability *λ*. Raising *λ* from 0 to 1 (4000 records per
  level):

  | λ | share of coherent records | mean recorded conflict |
  |---|---|---|
  | 0.0 | 1.00 | 0.00 |
  | 0.1 | 0.90 | 0.03 |
  | 0.25 | 0.75 | 0.08 |
  | 0.5 | 0.50 | 0.17 |
  | 0.75 | 0.25 | 0.25 |
  | 1.0 | 0.00 | 0.33 |

  Improving the legibility of the suppressed perspective monotonically lowers
  coherence and raises recorded conflict toward the full 1/3. An intervention
  that improves self-governance increases the disagreement observed, exactly as
  [CLAIM-448](../claims.d/CLAIM-448.md) predicts.
- **Persistence.** Over 50 windows, a maintained exclusion of the closing
  contest yields a single persistent recorded winner ([TERM-078](../terms.d/TERM-078.md)) every window,
  though the persistence is an artifact of admission; intermittent admission
  (*λ* = 0.5) breaks coherence in some windows. So a persistent potential, not
  merely a one-round acyclic record, can be produced by selective contestation,
  which [CASE-221](CASE-221.md) could not show.

## What it shows

[CLAIM-448](../claims.d/CLAIM-448.md)'s existence half, now with persistence and the intervention
prediction, in a model rather than by hand. The three relations [CLAIM-448](../claims.d/CLAIM-448.md)
distinguishes come apart in the run: the relation of preferences (the fixed
cycle), the relation of contests possible under majority rule (all three), and
the relation of wins actually admitted (the rule's selection). [TERM-077](../terms.d/TERM-077.md)'s test
answers only the third. Because the recorded winner is a pure function of the
admission rule with preferences fixed, a coherent record is not evidence that
the perspectives are integrated.

The nonintegrability degree of [CLAIM-451](../claims.d/CLAIM-451.md) is the recorded-conflict column:
zero exactly when the admitted record is acyclic, 1/3 on the full cycle.
Selective admission is thus a route to an acyclic record distinct from
[CLAIM-451](../claims.d/CLAIM-451.md)'s accommodation, entrenchment and periodic coordination, and like
those three it is one that observed coherence alone cannot tell from genuine
integration. For [CLAIM-440](../claims.d/CLAIM-440.md), the run is a direct demonstration of part 3: the
potential, and the goal-conduciveness valence read off it, is the
organization's only on a record shown to admit the contests that bear on it;
here changing the admission rule alone changes which option the record ranks
top. That is why the study bears on [QUESTION-269](../questions.d/QUESTION-269.md): a change in accessibility
or jurisdiction (which contest is admitted) moves the recorded ordering with
the underlying preferences unchanged.

## What it does not show

- **That real organizations behave so.** The model is a toy of three
  perspectives and three options, with a legibility regime stipulated as an
  admission probability. Whether raising a real challenge channel raises
  recorded conflict is untested here; the study shows the mechanism is
  coherent and has the predicted sign, not that it operates in any case.
- **Intent.** As in [CASE-221](CASE-221.md), the chair's selection could be deliberate
  suppression or a fixed neutral procedure. The record of wins cannot tell them
  apart, which is the point, but the model does not model the difference.
- **A measure of felt tension.** The nonintegrability degree is a graph
  quantity; [CLAIM-451](../claims.d/CLAIM-451.md) is explicit that how it relates to arbitration cost or
  reported dissonance is empirical, and nothing here measures that.
- **Cardinal structure.** Margins are 2-1 throughout; the Hodge direction
  [CLAIM-440](../claims.d/CLAIM-440.md) keeps for margins is not exercised. The study is entirely
  ordinal, on the record of wins.

The wording is the assistant's (Claude, in this session); adopting it is the
owner's call.
