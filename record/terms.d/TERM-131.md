---
number: 131
status: Proposed
formerly:
- TERM-tmp1ix99
title: 'learning'
statement: >-
  learning, of a declared system over a declared horizon: an
  experience-dependent change in the system's retained organization that
  alters what it can later do, at what cost and with what reliability,
  judged against a counterfactual in which the experience did not occur;
  distinct from successful learning, which is relative to a declared
  criterion, and from relaxation, selection among systems and a fixed
  controller's response
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

# TERM-131: learning

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
<!-- inactive-ok-file: THEORY-2062 — Proposed or newly filed; cited from the readings of 2026-11-19 -->

Brown and colleagues ([THEORY-2062](../theory.d/THEORY-2062.md); [NOTE-2160](../notes.d/NOTE-2160.md)) prompted version 2. Their in-context learning "occurs within the forward-pass upon each sequence", with "no gradient updates or fine-tuning, just increasing numbers of demonstrations given as conditioning", and the authors call it learning ("the model really does appear to learn these tasks at test time"). A first reading of this note took the absence of weight changes to count against it. The owner's view, adopted in version 2, is that learning from context in activation space is learning: of the model running in an episode, over the episode. [THEORY-169](../theory.d/THEORY-169.md) (conditioning and per-sequence weight updates differ in what state is kept, not in kind) agrees: what differs is the system and horizon over which organization is retained, not the kind of change. Pretraining, the outer loop, is learning of the weights over the model's life.

## Note of 2026-11-19: the scheduling follow-up readings, read
<!-- inactive-ok-file: THEORY-2059 THEORY-2060 — Proposed or newly filed; cited from the readings of 2026-11-19 -->

Hernandez and colleagues' effective data transferred ([THEORY-2059](../theory.d/THEORY-2059.md)) is
a worked operationalization of the counterfactual cost this term asks for,
in samples: the data the same-size system would have needed without the
experience. Papadimitriou and Jurafsky's frozen-weight transfer
([THEORY-2067](../theory.d/THEORY-2067.md)) runs the same later step against different histories with random
text as the null, but measures what the system can later do, not at what
cost. A caution from the attribution studies ([THEORY-2060](../theory.d/THEORY-2060.md),
[THEORY-2058](../theory.d/THEORY-2058.md)): alignment of an update with a run's endpoint or a target is not
learning from the experience in this term's sense, which needs a
counterfactual.

## Note of 2026-11-19: identifiability and localization of what is retained (the owner)
<!-- inactive-ok-file: CLAIM-765 THEORY-2058 — Proposed or newly filed; cited from the readings of 2026-11-19 -->

The owner (2026-11-19) proposed distinguishing learning merely persisted
into a stable representation from learning that is concretely indexable,
then sharpened it to identifiability against localization. Version 2 makes
in-context learning count by declaring the episode-system, but treats
retention in the context and in the weights alike. They differ: context
retention is localized (the demonstrations have positions) and identified
by deleting an item; weight retention is identified only by retraining or
attribution ([THEORY-2059](../theory.d/THEORY-2059.md), [THEORY-2058](../theory.d/THEORY-2058.md), [THEORY-2060](../theory.d/THEORY-2060.md)) and has no address; a
located circuit may be one of several sufficient ones and so not
identified ([THEORY-966](../theory.d/THEORY-966.md)); and competent behaviour need not establish any
internal model ([CLAIM-519](../claims.d/CLAIM-519.md)). [CLAIM-765](../claims.d/CLAIM-765.md) states that the two properties
come apart in all four combinations; [QUESTION-497](../questions.d/QUESTION-497.md) asks which of them
fixes a learner's boundary and its individuation by history. A candidate
version 3 would ask a claim using this term to say which kind of retention
it means, localized or identified-but-distributed; it waits on the owner's
ruling. [THEORY-1024](../theory.d/THEORY-1024.md) suggests a third property, editability, that comes
apart from localization.

## Note of 2026-11-19: Kuhn, read
<!-- inactive-ok-file: THEORY-2094 THEORY-2095 — Proposed or newly filed; cited from the readings of 2026-11-19 -->

Kuhn's exemplars ([THEORY-2095](../theory.d/THEORY-2095.md), [THEORY-2094](../theory.d/THEORY-2094.md)) illustrate the term: a
retained change in what one sees as similar, learned by doing problems,
which alters what one can later do and leaves the knowledge in the
organization rather than in statable rules, corrigible through further
education and misfits with the environment.

## Note of 2026-11-23: what holds it back

The definition is not settled: a candidate version 3, asking each claim that
uses the term to say whether the retention it means is localized or
identified but distributed (the owner's proposal of 2026-11-19, in this
entry's note of that date), waits on the owner's ruling. [CLAIM-758](../claims.d/CLAIM-758.md) waits on
it.

## Note of 2026-11-25: from the review of the manuscript governance-of-becoming, Part II

Article 5's join J5.1 read inquiry as a way the inquirer learns, in this
term's sense. An independent reader found it a relabelling of [CLAIM-475](../claims.d/CLAIM-475.md)'s
sense: trivial once one says which system learned. What it leaves is a
definitional question for this term: interventions and observations count
as "experience", but does formulating a question, with no observation,
count as an experience that can change the learner? The term does not say.
The wording is the assistant's (Claude, in this session).

## Note of 2026-11-26: von Oswald et al. (2023), read


Consistent with version 2. [LIT-tmpuv16r](../literature.d/LIT-tmpuv16r.md) ([NOTE-tmpcktnn](../notes.d/NOTE-tmpcktnn.md)) is a case where
the same network learns on two horizons. Over a sequence, fast weights Φ
change in activations: the model running in an episode learns over the
episode. Over training, base-optimization changes the weights that make
that inner learning possible. Read as a fixed controller over a single
sequence, the network does not learn. Read over the episode, it does. The
term's declared system and horizon decide which. No change to the term.

## Note of 2026-11-26: Veeriah et al. (2019), read


Consistent. In [LIT-tmpl1kcf](../literature.d/LIT-tmpl1kcf.md) ([NOTE-tmpibrnu](../notes.d/NOTE-tmpibrnu.md)), the random-questions baseline
is a clean counterfactual of the kind this term asks for: the same
answering machinery and the same experience, but a different retained
organization, and a different later capability. No change to the term.
