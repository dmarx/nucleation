---
status: Active
title: 'Scored between Nicaragua''s regime-owned outlets and its exiled or online opposition outlets, on the prevalence of topics relevant to the regime''s legitimacy and on the tone of sentences mentioning Ortega, the three nominally independent national outlets with web output moved toward the regime pole in agenda over 2018–2022, Canal 14 most and Radio Corporación least, and Canal 14''s tone score fell from about .8 to below .5 by early 2022 while Radio Corporación''s stayed near 1'
version: 1
history:
- version: 1
  date: '2026-10-21'
  note: >-
    Filed Active from NOTE-tmprgm1n, which read the article in full. The
    title states what the measure recorded, alignment between two poles,
    and not that the outlets were coerced; nothing in the record
    contradicts it (ADR-047 v3). The bound of the score in [0, 1] and the
    paper's weighting example were rechecked.
tags:
- society-and-governance
- social-science
date: '2026-10-21'
source:
- LIT-tmpfrzgy
summary: >-
  Barnehl and Schumacher (2024), [LIT-tmpfrzgy](../literature.d/LIT-tmpfrzgy.md), read in [NOTE-tmprgm1n](../notes.d/NOTE-tmprgm1n.md). A
  measured shift in relative position, outlet by outlet, from a 30-topic
  structural topic model and an off-the-shelf Spanish sentiment
  classifier, with no uncertainty reported in the main text. It does not
  show that the shift was coerced, which the paper's own definition of
  capture requires, nor that the opposition pole held still.
---

# THEORY-tmp5rkez: Scored between Nicaragua's regime-owned outlets and its exiled or online opposition outlets, on the prevalence of topics relevant to the regime's legitimacy and on the tone of sentences mentioning Ortega, the three nominally independent national outlets with web output moved toward the regime pole in agenda over 2018–2022, Canal 14 most and Radio Corporación least, and Canal 14's tone score fell from about .8 to below .5 by early 2022 while Radio Corporación's stayed near 1

## Source

Barnehl and Schumacher, "Media capture, captured", *Democratization* 31(7):
1536–1563 (2024), [LIT-tmpfrzgy](../literature.d/LIT-tmpfrzgy.md), read in full in [NOTE-tmprgm1n](../notes.d/NOTE-tmprgm1n.md).

## What was actually shown

144,700 articles from the twelve of Nicaragua's 27 national outlets with an
active web presence were modelled with a 30-topic structural topic model,
with outlet and date as covariates. Topics relevant to the regime's
legitimacy were chosen in advance. Sentences mentioning Ortega were
classified negative, neutral or positive. For each nominally independent
outlet (Radio Corporación, Canal 10, Canal 14) and each topic, the score
[(d(N, Reg) − d(N, Opp))/d(Opp, Reg) + 1]/2 runs from 0 (as the
regime-owned outlets) to 1 (as the opposition outlets). It is weighted
across topics by how far apart the poles are, and computed the same way
for tone.

All three outlets' agenda scores fell over 2018–2022. In 2018–2019 they
covered the legitimacy topics roughly like the opposition. From the second
half of 2019 Canal 10 and Canal 14 moved toward the regime, and Canal 14
did not recover. On tone, the opposition averaged about −.4 and the regime
outlets about .2. Canal 14's tone score fell from about .8 to below .5 by
the first quarter of 2022, and Radio Corporación's stayed close to 1,
dipping slightly from 2021.

What could have come out otherwise: the two poles could have failed to
separate on the chosen topics or on tone (checks II and III), and the
outlets' agenda and tone could have disagreed about which outlet moved
(check V). They did not.

## What this does not say

- **Not that the outlets were coerced.** The paper defines capture as
  requiring coercion by an external actor, and the scores measure
  alignment. "it is impossible to definitively reject" that a shift was a
  free editorial choice. Coercion is argued from the documented
  harassment in the period.
- **Not that the poles were fixed.** An opposition outlet that became more
  critical in exile would lower an unchanged outlet's score, as the authors
  note.
- **Not with stated uncertainty.** No tests or intervals for the scores
  appear in the main text.
- **Not beyond Nicaragua**, three outlets, and the researchers' choice of
  legitimacy topics.
