---
status: Read
paper: LIT-tmppjo0s
title: 'Interaction and threshold effects of appraisal on componential patterns of emotion: A study using cross-cultural semantic data'
version: 1
history:
- version: 1
  date: '2026-10-23'
  note: >-
    Read in full: the accepted manuscript (45 pp.) in Ghent University's
    repository, all sections, Table 1 and the figure captions. Page
    references are the manuscript's, not the journal's (Emotion
    19:425–442). The figures and the supplementary tables (loadings, the
    full MARS coefficients, the matching certainty) were not seen.
    Every quotation was checked by script against the extracted text.
date: '2026-10-23'
summary: >-
  From the GRID data on the meaning of 24 emotion words in 27 countries,
  MARS models of 11 motivation, physiology and expression factors on 7
  appraisal factors select interactions up to third order and some
  hinges. Goal compatibility is the main effect, agency and norm
  compatibility act only through it, and the structure is partly additive
  and partly hierarchical. The "threshold effects" are hinges in a
  continuous piecewise-linear fit. No synchronization measure, no time,
  and no choice data.
---
<!-- inactive-ok-file: CLAIM-tmp83ge2 CLAIM-tmp85p0g THEORY-101 THEORY-090 — Proposed; the continuity claim this reading was checked against and its neighbours -->
<!-- inactive-ok-file: LIT-tmppjo0s LIT-tmp5ejuc LIT-tmp7rygg — drafts filed in the same tranche -->

# NOTE-tmpj1twd: Interaction and threshold effects of appraisal on componential patterns of emotion: A study using cross-cultural semantic data

## Contribution

The first full-componential test of two assumptions of appraisal
theory: that appraisal changes motivation, physiology and expression and
not only feeling, and that appraisal criteria interact. It uses the GRID
data on the meaning of emotion words, on the "lexical sedimentation"
assumption that a word's meaning encodes knowledge of the emotion's
typical mechanisms (§1.3).

## Key insight

The interactions appraisal theory predicts are real but shallow. One
criterion (goal compatibility) does most of the work and splits positive
from negative. Two others (agency, norm compatibility) matter only as
modifiers of it, and the rest add. That is neither the additive model of
regression studies nor the deep decision tree of appraisal theories.

## Assumptions

- That culturally shared semantic profiles reflect the structure of real
  episodes, supported by the similarity of the result to Meuleman and
  Scherer's (2013) recalled episodes. The authors say "we do not claim to
  have examined actual, day-to-day emotion experiences" (ms p. 37).
- That PCA factors, fixed before cross-validation, are acceptable inputs
  and outputs (they concede a small bias, ms pp. 37–38).
- That a reduction in generalized cross-validation error is a better
  criterion of relevance than significance with N = 816.

## Key results

- **Structure** (Table 1). Goal compatibility appears at main, second and
  third order and needs four hinges. Suddenness, familiarity, coping and
  relevance appear as main effects, and suddenness and relevance also in
  interactions. Agency and norm compatibility appear only in
  interactions.
- **Fit** (Figure 5). Cross-validated R² averages 42.0% for motivation,
  41.6% for physiology and 48.7% for expression. Bipolar factors gain from
  splines. Attack vs submit, tears and speech perturbation gain from
  interactions.
- **The three-way surface** (Figure 7). When the self is the agent there is
  no attack tendency at any combination of goal and norm compatibility,
  only submission graded by goal incompatibility. When another is the
  agent, attack appears for high goal incompatibility with high norm
  incompatibility.
- **Matching** (Figure 9). Simulated patterns matched by nearest neighbour
  to GRID words form a structured map: goal compatibility separates
  positive from negative words, and agency and norms differentiate
  within each region. The average majority-label probability is 41.8%,
  against a chance level of 4.2%.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Appraisal affects motivation, physiology and expression through interactions and nonlinear effects | moderate | MARS selection on semantic data; 7 of 11 factors improve |
| C2 | Goal compatibility is the main effect; agency and norm compatibility are pure modifiers | moderate | Table 1; agrees with Meuleman & Scherer (2013) on recalled episodes |
| C3 | The strong hierarchy of appraisal decision trees is not supported | moderate | no single main effect with pure interactions below it |
| C4 | Some appraisals must reach a threshold before affecting responses | weak | a hinge in one fitted curve (Figure 6), on semantic data |
| C5 | Semantic profiles reflect the mechanisms of real episodes | weak | similarity to one earlier study |

## Concepts

- **pure modifier**: an appraisal criterion whose effect exists only in
  interaction with another, with no main effect of its own.
- **hinge**: the knot of a MARS spline, where a piecewise-linear
  function changes slope.
- **semantic profile**: the typical componential pattern a language
  community attaches to an emotion word (GRID).

## Connections

Builds on Meuleman and Scherer (2013) and on Fontaine, Scherer and
Soriano (2013, the GRID sourcebook). The two later Geneva-related studies
filed with it use the CoreGRID items to collect ratings of episodes
rather than words ([LIT-tmp5ejuc](../literature.d/LIT-tmp5ejuc.md), [LIT-tmp7rygg](../literature.d/LIT-tmp7rygg.md)). Its
synchronization paragraph restates Scherer's ([LIT-tmpfjacn](../literature.d/LIT-tmpfjacn.md)).

## Bearing on the record

**A per-episode measure of synchronization?** None, and the data could
not give one. Each case is a sample's average rating of what a word
implies. There is no episode and no time. The paper states the
hypothesis, "If there are indeed strong causal relations among
components, they should show a high degree of synchronization" (ms
p. 7). The only coherence it reports is the correlation of factors
across the 816 word-by-sample cases (Figure 4). That is coherence in
shared knowledge across emotion words, not coupling within an episode.
For [QUESTION-tmpsqwu5](../questions.d/QUESTION-tmpsqwu5.md) it is not a candidate.

**Signed, or which tendency prevails?** Its response factors are bipolar
and signed: appetitive vs defensive, intervention vs disengagement,
attack vs submit. A fitted profile therefore does say which pole of each
tendency a word carries. But that is a prediction of meaning, not the
outcome of a conflict. A caution on words: its "ATTACK VS SUBMIT factor
corresponds to tendencies to dominate (positive values) versus to be
dominated (negative values)" (ms p. 22). That is the social dominance of
the PAD tradition, the homonym the record renamed its own notion to
avoid, and it should not be read as ascendancy.

**The threshold effects and [CLAIM-tmp83ge2](../claims.d/CLAIM-tmp83ge2.md).** They do not bear on the
claim's contrast, for three reasons.
- **MARS cannot produce a discontinuity.** Its basis functions are hinges,
  zero on one side of a knot and linear on the other, so every fitted
  curve is continuous. A "threshold" in this model is a kink, a change
  from a flat slope to a steep one. On the claim's terms that is a
  continuous currency whose price rises sharply, Veit's regime
  ([THEORY-101](../theory.d/THEORY-101.md)), not ALARM's override ([THEORY-090](../theory.d/THEORY-090.md)). Even if the true
  relation had a jump, MARS would fit it as a steep segment.
- **The "threshold" is the authors' gloss on one panel**, and their own
  description of that panel is a steepening, not an onset: "increasing
  familiarity simply leads to decreasing physiological arousal. This
  decrease occurs even faster for strong appraisal of familiarity" (ms
  p. 27). The discussion then cites that panel for "an appraisal criterion
  must reach a certain threshold value" (ms p. 34).
- **Nothing is traded off.** The inputs are appraisals and the outputs
  responses. There is no cost, no resource and no choice between pairs,
  so the claim's indifference curve does not exist here.

The paper does sharpen one of the claim's cautions. Following Kappas, it
treats a sigmoid and a step as near-equivalent: "Sigmoidal curves can
also be viewed as continuous approximations of binary threshold
functions" (ms p. 10), and "they share the property that output cannot
increase substantially until input reaches a certain value" (ms p. 10).
[CLAIM-tmp83ge2](../claims.d/CLAIM-tmp83ge2.md) says that a finite set of tested pairs can always be fitted
by a currency, so the test needs enough pairs to tell a steep curve from
a discontinuity (after [CLAIM-tmp85p0g](../claims.d/CLAIM-tmp85p0g.md)). This paper is an example of a field
that has not drawn that line. Here "threshold" covers both, and a
smooth-spline method decided the matter by construction. A trade-off
study meant to test the claim should not fit splines of this kind. It
should fit a model with a free jump and compare the two.

It cannot speak to hysteresis either ("the omission of time", ms p. 38).

**One structural point.** The result that the mapping is "partly
additive and partly hierarchical" (ms p. 34) is a case, in emotion
knowledge, of compensatory and gated structure in one function.
Additive criteria trade off. A pure modifier changes the effect of goal
compatibility without having any effect of its own, which is how a
gate acts. [CLAIM-tmp83ge2](../claims.d/CLAIM-tmp83ge2.md) expects both regimes in one animal, as one
ordering changing regime. This is at most a weak analogue: it concerns
appraisal-to-response maps in word meaning, not an ordering's ascendancy
in conduct. It is worth noting because it is the same two-regime shape
found in a different domain.

## Limitations

The data are semantic. The authors argue this is a strength, since
semantic profiles are stable across languages (alpha .92). But it limits
any inference about episodes. PCA fixes the factor structure before
modelling, and there is no feeling component (dropped by design), no
time and no feedback. The matching map cannot be scored against ground
truth.

## Open questions

Whether the pure-modifier structure survives in episode data with a
model that allows discontinuities (a tree with free jumps, or a
change-point regression), so that a kink and a jump can be told apart.
