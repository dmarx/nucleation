---
number: 334
status: Active
formerly:
- THEORY-tmp6oz2d
title: 'In copying a pattern of coloured blocks that stays in view, seven subjects told to work quickly looked back at the model about 1.3 times per block, and their commonest cycle, which looks at the model both before picking up a block and before dropping it, was the slowest per block in the authors'' observed tallies (about 3 s, against 1.5 s for a cycle that copies from memory); looks fell to 1.0 per block with model and copy 70° apart and to 0.7 with one-colour patterns that could be chunked, and in three subjects a colour change made during a saccade raised fixation time by about 129 ms after pickup against about 50 ms before; no statistics are reported'
version: 2
history:
- version: 2
  date: '2026-10-20'
  note: >-
    Narrowed and promoted, carrying out the promotion audit's decision for
    THEORY-334 (batch 063, ADR-047 v3): one study read in full in NOTE-883,
    its Table 7 and §3.2 re-checked against the same PDF. The title now
    states only what the article reports observing. The authors' coding of
    the cycle (one look for colour, one for position), the generalisation
    that people keep only the property the step needs, and the inference
    that holding costs more than re-fetching leave it; the inference, which
    THEORY-346 contests, stays in the body. The request for a powered study
    with the two costs varied independently moves unchanged to
    QUESTION-235.
tags:
- embodied-cognition
- cognition
date: '2026-10-15'
source:
- LIT-1075
summary: >-
  Ballard, Hayhoe, Pook and Rao (1997), [LIT-1075](../literature.d/LIT-1075.md), read in [NOTE-883](../notes.d/NOTE-883.md). Fixations are
  modelled as pointers that bind a program's variable to a place in the world, so
  that only the task-relevant feature is fetched, just before use. In block
  copying, look-model, pick-up, look-model, drop was the commonest cycle (about
  43% of cycles), at about 3 s a block against 1.5 s from memory; 70° separation cut
  looks from 1.3 to 1.0 per block, and one-colour patterns to 0.7. A colour changed
  mid-saccade mostly went unnoticed and cost time only once colour was held. The
  "carrying cost" of working memory is inferred from choice, not measured, and
  what is left in the world is raw input, not a computed result.
  Promoted 2026-10-20 on the observations alone (ADR-047 v3).
bears_on:
- QUESTION-095
---

# THEORY-334: In copying a pattern of coloured blocks that stays in view, seven subjects told to work quickly looked back at the model about 1.3 times per block, and their commonest cycle, which looks at the model both before picking up a block and before dropping it, was the slowest per block in the authors' observed tallies (about 3 s, against 1.5 s for a cycle that copies from memory); looks fell to 1.0 per block with model and copy 70° apart and to 0.7 with one-colour patterns that could be chunked, and in three subjects a colour change made during a saccade raised fixation time by about 129 ms after pickup against about 50 ms before; no statistics are reported

## Source

Ballard, Hayhoe, Pook and Rao (1997), [LIT-1075](../literature.d/LIT-1075.md) (Behavioral and Brain Sciences
20(4), 723–742), read in [NOTE-883](../notes.d/NOTE-883.md): section 3 (Figures 9–11, Table 7) and the
argument of sections 1–2. The commentaries were not read.

## What was actually shown

**The account.** At about a third of a second, body movements act as pointers:
"Deictic representations allow the brain to leave important information out in
the world and acquire it just before it is needed in the cognitive program. This
avoids the carrying cost of the information." Working memory holds a few
pointers, not contents.

**Re-looking (Figure 9b, seven subjects).** Coding each block cycle by
fixations, M-P-M-D (model, pick up, model again, drop) holds nothing in memory;
P-M-D holds colour, M-P-D position, P-D both. M-P-M-D "is the most frequently
used by all the subjects, far outweighing the others": about 43%, against 28%,
11% and 11%, read off the plot. Pick-up-drop cycles came last in a pattern.
Subjects averaged 1.3 looks per block and "sometimes made as many as 18
fixations in the model area" where four memorized subpatterns would need four.

**Against speed (Table 7).** Per block: M-P-M-D 3 s, P-M-D 2.5 s, M-P-D 2.0 s,
P-D 1.5 s. "it is surprising that subjects choose minimal memory strategies in
view of their temporal cost, especially because they have been instructed to
complete the task as quickly as possible, and memorization saves time."

**Both costs move it.** With model and copy 70° apart, looks fell from 1.3 to
1.0 per block. With all blocks one colour, so segments could be chunked, they
fell to 0.7, and subjects copied subpatterns without looking. The authors use
these against two rival readings: that the eyes are merely idle, and that memory
is cheap but unreliable, since longer transit gave fewer checks, not more.

**What is kept (Figures 10–11, three subjects).** A block's colour was changed
during a saccade on about 25% of model fixations. Before pick-up, fixation time
rose about 50 ms; after pick-up, when colour was held, 129 ms, and subjects
picked a block of the held colour, "in most instances" unaware of the change.
"The important finding is that the information retained from prior saccades is
determined by what is currently relevant for the task."

**What could have come out otherwise.** People could have memorized subpatterns,
the faster route, and looks could have been insensitive to the cost of looking
or of holding. Neither happened.

## What this does not say

- **That memory's carrying cost is measured.** It is read from choices. No
  utility, fitted model or statistics appear in the article; the main data are
  seven subjects with simulated blocks, the colour-change data three. The
  authors cite the same pattern with real blocks in up to 20 subjects (Pelz 1995),
  not reported here.
- **That people minimize memory regardless of time.** Gray et al. ([THEORY-346](THEORY-346.md))
  argue the per-block timings here are confounded, since encoding may be
  amortized over a whole trial; whether re-looking costs more total time is
  not settled by this design.
- **That this is amortization.** What stays in the world is raw input, and the
  computation on it is done anew each time. The article argues against
  precomputation where needs vary: "An obvious reason for timely, task-dependent
  computation is that its products are so varied that the brain cannot
  precompute them." Its own analogy is demand paging.
- **That it generalizes.** One task, with random colours chosen to resist
  grouping; chess and driving are argued by analogy. The neural mapping of
  section 4 is proposal.

## Connections

- [QUESTION-095](../questions.d/QUESTION-095.md): the "defer and re-read" strategy, the opposite policy to the
  cockpit's. It suggests a term the question's list lacks, how predictable the
  later need is. Re-reading also defends against staleness: when the world
  changed, the subject who had not memorized was mostly unaffected.
- [THEORY-346](THEORY-346.md): the two accounts differ on whether memory costs anything beyond
  time; Gray et al. set the soft constraints hypothesis against this one.
- [THEORY-360](THEORY-360.md): Kirsh and Maglio change the world to cheapen a computation;
  here the world is left alone and read again.

## Note of 2026-10-20: narrowed and promoted

The promotion audit (batch 063) narrowed the title to what [LIT-1075](../literature.d/LIT-1075.md)
reports observing, and promoted it on that one study under [ADR-047](../decisions.d/ADR-047.md) v3.
[NOTE-883](../notes.d/NOTE-883.md) read the target article in full, and the review checked Table 7
and §3.2 against the same author-posted PDF. Table 7 is titled "Speed vs.
memory tradeoffs observed", so the per-block times are the authors'
tallies, not a model.

Three clauses of the earlier title left it. "Most often once for colour
and once for position" is the authors' coding of the commonest cycle, not
a measurement of what each look fetched. "Keep only the property the
current step needs" generalises one property tested in three subjects;
the title now gives the measured fixation costs instead. The last was
that holding information costs more than re-fetching it, inferred from
these choices. That is the reading [THEORY-346](THEORY-346.md) contests with a model that
prices both in time alone, and the reading Bogacz's commentary (not read in
[NOTE-883](../notes.d/NOTE-883.md)) puts down to task unfamiliarity. The body keeps it as the
authors' inference. The former promote_when, a powered study with the cost
of looking and of holding varied independently and total time measured per
person, moves unchanged to [QUESTION-235](../questions.d/QUESTION-235.md).
