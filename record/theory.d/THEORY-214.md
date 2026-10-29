---
number: 214
status: Active
formerly:
- THEORY-tmp07t7w
title: 'On the 2022 r/place canvas, the abrupt overthrow of a crowd-built image from a stable period is predicted up to hours ahead, on held-out images and on the 2023 edition, by a combination of many image-level series far better than by any generic slowing-down indicator; the series the predictor relies on include low past restoring of attacked pixels as well as attack outrunning restoration, and about a quarter of overthrows give no warning at the 20-minute range'
version: 2
history:
- version: 2
  date: '2026-10-29'
  note: >-
    Narrowed and promoted by the twelfth status review (ADR-057, ADR-047's
    evidence ruling, on THEORY-285's precedent). The one study was read in
    full in NOTE-731 (main text and SI sections 1, 2 and 6; SI 3 to 5
    skimmed), and the title now claims no more than it measured. Version
    1's title read: "Crowd-maintained r/place images persist as an
    equilibrium of attack and repair, and their abrupt overthrow is
    preceded by several distinct precursors, including the defenders' own
    conduct, rather than by one generic warning signal, while many
    overthrows give no warning". "Persist as an equilibrium of attack and
    repair" is dropped: the state variable presupposes it, and some
    compositions last through neglect, which is QUESTION-169's question.
    "The defenders' own conduct" becomes the measured restoring series,
    since the social readings of the precursors are the authors'
    conjecture from SHAP curves. The promote_when, a second system and the
    social reading of the precursors, moves unchanged to
    QUESTION-tmp619m4.
tags:
- complex-systems
- social-science
date: '2026-10-13'
source:
- LIT-1025
summary: >-
  Falmagne, Stephenson & Levin (2026), [LIT-1025](../literature.d/LIT-1025.md), read in [NOTE-731](../notes.d/NOTE-731.md).
  On about 10,900 compositions of 2022, a predictor of time-to-overthrow built
  from 19 composition-level series with a 7-hour memory catches half the
  overthrows within 20 minutes at 3.6% false positives, beats variance and
  autocorrelation trends, and transfers to 2023. Its precursors are many:
  attack outrunning defence, a turbulent history, little accepted change,
  uncoordinated activity, simple images, low past defence; slowing down and
  speeding up both occur. About a quarter of overthrows are unpredictable at
  the 20-minute range. The social readings of the precursors are the
  authors' conjecture from SHAP curves; nothing here measures plans.
supports:
- CLAIM-280
- CLAIM-273
---
<!-- inactive-ok-file: CLAIM-279 CLAIM-163 THEORY-069 THEORY-058 — Proposed; open claims and accounts, cited as what this bears on, nothing here rests on their being settled -->

# THEORY-214: On the 2022 r/place canvas, the abrupt overthrow of a crowd-built image from a stable period is predicted up to hours ahead, on held-out images and on the 2023 edition, by a combination of many image-level series far better than by any generic slowing-down indicator; the series the predictor relies on include low past restoring of attacked pixels as well as attack outrunning restoration, and about a quarter of overthrows give no warning at the 20-minute range

## Source

Falmagne, Stephenson & Levin (2026), [LIT-1025](../literature.d/LIT-1025.md), read in [NOTE-731](../notes.d/NOTE-731.md):
Materials and Methods (state variable, transitions), Results (Figs. 4–6),
Discussion, and SI sections 1, 2 and 6.

## What was actually shown

A composition's state is its fraction of pixels differing from the image
that has held over the last three hours. An overthrow is a jump of that
fraction above 0.35 and to six times its recent mean, from a stable
period. Gradient-boosted trees predict time to overthrow from 19 series
(attack fraction, return rate, users, new users, redundant changes, image
entropy and so on) over a 7-hour memory.

- **It could have failed, and partly did.** The predictor is tested on
  compositions it never saw and on a later edition with different rules.
  It holds up: ROC AUC 0.835 at a 20-minute warning range and 0.698 at six
  hours, and only a slight drop on 2023. But at 20 minutes 27% of
  transitions are predicted no better than chance.
- **No generic signal suffices.** Variance, autocorrelation and return-rate
  trends, the standard indicators of critical slowing down, do far worse.
  Slowing down appears very close to overthrow, and a mild speeding up
  (high recent defence) appears earlier. A toy model shows why both can
  occur: a falling defence strength gives a bifurcation with slowing down,
  a sudden rise in attack gives rate-induced tipping with speeding up,
  because damage recruits defenders.
- **Several precursors concern the defending community.** Low past
  defence, little accepted change ("innovation"), uncoordinated activity
  and simple images precede overthrow. A turbulent history does too.
  Very low past activity makes a composition safer.

## What this does not say

- **It does not show what the community did.** "Coordination",
  "innovation" and "recruitment" are read from placements. The SI says no
  pixel change can be classed as attack or innovation except by what the
  defenders later do, and the authors call their interpretation
  conjectural. No plan, template or forum was examined.
- **It does not show that every lasting image was defended.** Very low
  past activity makes a composition safer, so some persist through
  neglect. That is the case [CLAIM-280](../claims.d/CLAIM-280.md)'s `defeated_if` names. The
  paper does not say how many long-lived compositions persisted each way.
  The support it gives [CLAIM-280](../claims.d/CLAIM-280.md) is that the maintained regime exists
  and that its failure is where overthrow begins. It does not show that the
  regime is the usual route to persistence.
- **It does not separate product from producer.** The tracked image is a
  3-hour mode and drifts with accepted change. No community is followed
  from one image to another.
- **It says nothing about building classifiers.** The predictor is the
  instrument. The finding is that the precursors of collective overthrow
  are plural and partly social. That is not advice for machine-learning
  practice.
- **It does not transfer by itself.** Both test sets are r/place. The
  authors' hope that the precursors "might apply to transitions in other
  socioecological systems" is untested.

## Connections

- **[CLAIM-280](../claims.d/CLAIM-280.md).** Supported as described above. The paper's return
  rate is close to the conditional repair hazard A8 proposed. It lacks the
  per-site baseline A8 asked for.
- **[CLAIM-279](../claims.d/CLAIM-279.md).** The attack-or-innovation ambiguity is that claim's
  relativity to a group's policy, observed. Whether an edit was damage
  depends on whether the image's own community later keeps it.
- **[THEORY-069](THEORY-069.md) and [THEORY-058](THEORY-058.md)** rely on critical slowing as the
  warning before a switch. Here it is one precursor among several, and
  it is reversed for one transition type. Nothing here bears on those
  systems directly.
- **[CLAIM-163](../claims.d/CLAIM-163.md)** asked for a real order parameter. This paper shows the
  difficulty for an image: no scalar state variable is natural, and noise
  cannot be told from coordinated attack.
- **[QUESTION-091](../questions.d/QUESTION-091.md).** Damage-driven recruitment is the excitation a
  branching model of r/place repairs would fit. This paper does not fit
  one.
