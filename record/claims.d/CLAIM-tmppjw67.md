---
status: Proposed
title: 'A ranking trained on clicks under itself locks in unless some evidence bypasses it'
statement: >-
  A ranking trained on users' clicks on results it chose to show selects its
  own evidence, since what is clicked depends on what was ranked high, so
  the loop can confirm itself and lock in whatever it first ranked well, a
  performative effect on the users' side beside the publishers'; on the
  record's account, what stops the lock-in is evidence whose arrival or
  scoring does not pass through the ranking, such as randomized placement
  and quality judgments made without the ranking's order, and not more
  clicks
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  A ranking trained only on clicks under its own order that does not lock in
  over time, with no randomized placement and no judgments made apart from
  the ranking; or evidence that randomized placement and independent
  quality judgments do not reduce lock-in.
tags:
- search-and-ranking
- learning-theory
- epistemology
date: '2026-11-27'
line:
- learned-structure
answers:
- QUESTION-tmpqba7g
rests_on:
- CLAIM-342
summary: >-
  Filed at the owner's "relate SEO to performative prediction"
  (2026-11-27). It applies [CLAIM-342](CLAIM-342.md) (Active: unselected evidence, not
  action, stops lock-in) to learning to rank from clicks. That rankings
  correct for position bias and use human quality raters is the assistant's
  general knowledge of the field, not held on the record. The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmph131t — Open or new; the question and the claim on the publishers' loop -->

# CLAIM-tmppjw67: A ranking trained on clicks under itself locks in unless some evidence bypasses it

## The claim

Performative prediction usually means the *scored* population responding,
here publishers. Search has a second loop, on the users' side. The ranking
decides what is shown first, users click more on what is shown first, and
the ranking learns from those clicks. Its evidence passes through its own
interpretation, so it can lock in: a page ranked high early collects clicks
for being high.

[CLAIM-342](CLAIM-342.md) says what keeps a judgement–observation loop from confirming itself
is "evidence whose arrival or scoring does not pass through the
interpretation it tests". In search that means:
- **Randomized placement.** Some results are shown out of the ranking's
  order, so their clicks measure the page and not its position.
- **Independent judgments.** Quality judgments are made by people who do not
  see the ranking's order.

More clicks, gathered the same way, do not help, which is [CLAIM-342](CLAIM-342.md)'s point
that a loop selecting its own evidence can lock in with action available.

## Two loops at once

The engine faces both at the same time. Publishers move the distribution of
pages ([CLAIM-tmph131t](CLAIM-tmph131t.md)), and users' clicks move its evidence about them. SEO
exploits the second loop too. A manipulated page that reaches a high
position collects the clicks that then seem to confirm it.

## What it does not say

That clicks are worthless. They are evidence once corrected for the
ranking's own effect on them.
