---
number: 131
status: Proposed
formerly:
- TERM-tmp1ix99
title: 'learning, of a declared system over a declared horizon: an experience-dependent change in the system''s retained organization that alters what it can later do, at what cost and with what reliability, judged against a counterfactual in which the experience did not occur; distinct from successful learning, which is relative to a declared criterion, and from relaxation, selection among systems and a fixed controller''s response'
version: 2
history:
- version: 2
  date: '2026-11-19'
  note: >-
    Relative to a declared system and horizon, at the owner's prompting
    (2026-11-19: "learning from context in activation space is still a
    form of learning"). Retained organization is the declared system's,
    over the declared horizon, so in-context learning is episodic learning
    of a model running in an episode, and selection is learning of a
    population when the population is the declared system. Version 1's
    title began "learning, of a system:" and excluded selection without
    that qualification.
tags:
- learning-theory
- complex-systems
date: '2026-11-19'
line:
- learned-structure
- realizability
summary: >-
  A's, from A46 §1 and §7 of the exchange "Topological protection
  explained" (2026-11-19), after the owner said "I feel like we're
  reasonably appropriately situated to make general claims about how
  learning works" (U20); refined in A71's opening. The job it does: the
  record uses "learning" across its lines (training, will-organization,
  institutions, self-formation in [TERM-099](TERM-099.md)) without saying what counts, so
  the claims filed from this exchange ([CLAIM-754](../claims.d/CLAIM-754.md), [CLAIM-758](../claims.d/CLAIM-758.md),
  [CLAIM-756](../claims.d/CLAIM-756.md)) need a sense that separates learning from mere change
  and from mere success. It extends Mitchell's definition by putting
  organization and cost where Mitchell put performance. The wording is
  A's; adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-519 CLAIM-754 CLAIM-756 CLAIM-758 — Proposed; cited in this filing of 2026-11-19 -->

# TERM-131: learning, of a declared system over a declared horizon: an experience-dependent change in the system's retained organization that alters what it can later do, at what cost and with what reliability, judged against a counterfactual in which the experience did not occur; distinct from successful learning, which is relative to a declared criterion, and from relaxation, selection among systems and a fixed controller's response

## Definition

A46 §1 of the exchange "Topological protection explained"
(https://chatgpt.com/share/6afe6dd0-9d78-83ea-9782-f55680665dcf):
"Learning is an experience-dependent change in a system's retained
organization that alters how it can respond to subsequent situations."
A71's revision puts the effect on the costed repertoire: "an
experience-dependent transformation of retained organization that
changes the system's future repertoire of affordable and reliable
activities". Four elements: experience, a change in retained
organization, a future consequence, and an evaluation, which belongs to
successful learning and not to learning.

## What it excludes (A46 §7)

- **Relaxation**: "A cooling material can relax toward equilibrium
  without learning in the usual sense." The experience must make a
  counterfactual difference to later capability.
- **Selection among systems, for a member**: a population changing by
  differential survival changes no member's organization ([CLAIM-288](../claims.d/CLAIM-288.md)).
  If the population is the declared system, its change by selection is
  learning of the population (version 2).
- **A fixed controller**: a response the organization already fixed is not
  learning from the experience.
- **Not replay, but not generalization either**: improvement restricted
  to previously encountered examples can be memorization or episodic
  learning, which counts as learning; it does not by itself show the
  acquisition of a generalized procedure, a transferable abstraction or a
  new capacity to learn. (Corrected at ChatGPT's review of 2026-11-19,
  forwarded by the owner: the first version excluded replay-only gains
  from learning.)
- **The appearance of competence**: a lookup table can mimic a model over
  a finite horizon ([CLAIM-519](../claims.d/CLAIM-519.md)), so a test must reach beyond it.

## System and horizon (version 2)

What counts as retained organization depends on which system is declared
and over what horizon. A language model's weights retain what pretraining
and fine-tuning change for the model's life; a model running in an
episode, weights and context, retains what its context holds for the rest
of the episode. Demonstrations in the context are then experience: they
change that state and what the episode-system can do, against the
counterfactual without them, so in-context learning is episodic learning
of the episode-system, as memorization is episodic learning above. The
weights alone do not learn in context. Whether demonstrations are counted
as experience or as operating budget is the same choice in [CLAIM-754](../claims.d/CLAIM-754.md)'s
terms: as experience they move the episode-system's developmental
frontier; as budget, its operational one. A claim using this term says
which system and horizon it means.

## The job it does

Lets claims about learning in any line say what changed: the operational,
developmental or inquiry frontier ([CLAIM-754](../claims.d/CLAIM-754.md)), at what cost, and
against what counterfactual ([TERM-117](TERM-117.md)'s comparator). Self-formation
([TERM-099](TERM-099.md)) is a narrower sense, learning that the self governs.

## Note of 2026-11-19: Brown and colleagues, read
<!-- inactive-ok-file: THEORY-tmp8cm7r — Proposed or newly filed; cited from the readings of 2026-11-19 -->

Brown and colleagues ([THEORY-tmp8cm7r](../theory.d/THEORY-tmp8cm7r.md); [NOTE-tmprmye5](../notes.d/NOTE-tmprmye5.md)) prompted version 2. Their in-context learning "occurs within the forward-pass upon each sequence", with "no gradient updates or fine-tuning, just increasing numbers of demonstrations given as conditioning", and the authors call it learning ("the model really does appear to learn these tasks at test time"). A first reading of this note took the absence of weight changes to count against it. The owner's view, adopted in version 2, is that learning from context in activation space is learning: of the model running in an episode, over the episode. [THEORY-169](../theory.d/THEORY-169.md) (conditioning and per-sequence weight updates differ in what state is kept, not in kind) agrees: what differs is the system and horizon over which organization is retained, not the kind of change. Pretraining, the outer loop, is learning of the weights over the model's life.

## Note of 2026-11-19: the scheduling follow-up readings, read
<!-- inactive-ok-file: THEORY-tmp1mk7r THEORY-tmp5jrhv — Proposed or newly filed; cited from the readings of 2026-11-19 -->

Hernandez and colleagues' effective data transferred ([THEORY-tmp1mk7r](../theory.d/THEORY-tmp1mk7r.md)) is
a worked operationalization of the counterfactual cost this term asks for,
in samples: the data the same-size system would have needed without the
experience. Papadimitriou and Jurafsky's frozen-weight transfer
([THEORY-tmpf6s7m](../theory.d/THEORY-tmpf6s7m.md)) runs the same later step against different histories with random
text as the null, but measures what the system can later do, not at what
cost. A caution from the attribution studies ([THEORY-tmp5jrhv](../theory.d/THEORY-tmp5jrhv.md),
[THEORY-tmp1b3hj](../theory.d/THEORY-tmp1b3hj.md)): alignment of an update with a run's endpoint or a target is not
learning from the experience in this term's sense, which needs a
counterfactual.
