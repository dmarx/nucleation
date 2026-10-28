---
number: 1017
status: Active
formerly:
- THEORY-tmpz8eh5
title: 'In Claude 3.5 Haiku, writing the second line of a rhyming couplet whose first line ends "grab it", features for the candidate rhymes "rabbit" and "habit" are active on the newline token before the line, steering them changes the line''s final word only when applied at that token, and suppressing "rabbit" turns the line towards "habit"; injecting a "rabbit" or "green" word feature at that point in 25 other poems ended the line with the injected word in 70% of cases, and such planned-word features were found in about half of the poems the authors examined'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed Active from NOTE-1181. One case study, read in full (the
    section Planning in Poems with its four subsections); the title claims
    no more than it measured, with the authors' "about half" kept as their
    count, and nothing in the record contradicts it (ADR-047 v3). The
    article's general statement that the model plans its outputs is the
    Proposed THEORY-982.
tags:
- representation-learning
- cognition
date: '2026-10-26'
source:
- LIT-1541
extended_by:
- THEORY-982
summary: >-
  Lindsey et al. (2025), [LIT-1541](../literature.d/LIT-1541.md), read in [NOTE-1181](../notes.d/NOTE-1181.md). A target word
  represented before the text that leads to it, and used causally: it is
  the case study's own measurement, on one couplet and a 25-poem injection
  test. It does not say how widespread planning is, the "about half" being
  a count without a stated sample, and one of the article's displayed
  "success cases" does not end in the injected word.
---
<!-- inactive-ok-file: THEORY-982 — Proposed; the wider thesis, cited as open -->
# THEORY-1017: In Claude 3.5 Haiku, writing the second line of a rhyming couplet whose first line ends "grab it", features for the candidate rhymes "rabbit" and "habit" are active on the newline token before the line, steering them changes the line's final word only when applied at that token, and suppressing "rabbit" turns the line towards "habit"; injecting a "rabbit" or "green" word feature at that point in 25 other poems ended the line with the injected word in 70% of cases, and such planned-word features were found in about half of the poems the authors examined

## Source

Lindsey et al. (2025), *On the Biology of a Large Language Model*,
[LIT-1541](../literature.d/LIT-1541.md), read in [NOTE-1181](../notes.d/NOTE-1181.md): the section "Planning in Poems" (its
four subsections and the table of 25-poem samples).

## What was actually shown

**The couplet.** "A rhyming couplet: / He saw a carrot and had to grab it,"
completed "His hunger was like a starving rabbit". Attributing back from
"rabbit", the important features sit on the newline before the second
line: "rhymes with eet/it/et" features, fed from "it", activate features
for "rabbit" and "habit", which feed "say rabbit" at the last position.
The authors "initially hypothesized that we'd observe improvisation".

**Position.** Steering negatively on rabbit and habit and positively on a
"green" feature (from another poem) changes the predicted final word only
when applied at the newline; "the features are only active over the
planning token".

**Writing towards the plan.** The same rabbit features promote
"comparison" features active before "like a" at the intermediate word
"like"; suppressing them changes the transition to one suited to "habit".
Resampling the whole line under the interventions (500 samples per
experiment) changes its structure to end on the steered word.

**Injection across poems.** Injecting the "rabbit" and "green" features
into "a random sample of 25 poems": "the model ended its line with the
injected planned word in 70% of cases". The denominator (25 or 50
injections) is not stated.

**Frequency.** "We found planned word features in about half of the poems
we investigated", which the authors attribute either to the CLT lacking
features for the planned words or to the model not always planning.

**What could have come out otherwise.** The rhyme could have been chosen at
the last position, from the line written so far, as the authors expected;
steering at other positions could have worked as well as at the newline;
injection could have failed to move the final word.

## What this does not say

- **Not that the model plans in general.** One couplet is analysed in
  depth; the 25-poem test shows that injected word features usually steer
  the ending, not that the model produced such features itself in those
  poems; "about half" is a count over an undescribed set.
- **Not that the plan is a planning-specific representation.** The
  authors stress the opposite: the features "seem to be ordinary features
  representing that word".
- **Not about prose.** Rhyme is a constraint that makes a target word
  determinable before the line starts.
- **One displayed success is not one.** In the article's table, the
  "rabbit" injection on "The clouds are gray, the raindrops fall," gives
  "Soft and slow like a timid hare.", which ends in "hare".
