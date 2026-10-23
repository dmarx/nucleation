---
status: Read
paper: LIT-tmp7rygg
title: 'A Multi-Componential Approach to Emotion Recognition and the Effect of Personality'
version: 1
history:
- version: 1
  date: '2026-10-23'
  note: >-
    Read in full: the arXiv preprint (2010.11370v1, 13 pp.), all sections,
    tables and figure captions in extraction. Page references are the
    preprint's. The published version was not seen. Every quotation was
    checked by script against the extracted text.
date: '2026-10-23'
summary: >-
  A crowdsourced film-rating study. Thirty-nine CoreGRID items rated after
  whole clips show emotion structure beyond valence and arousal (six
  dimensions) and predict discrete-emotion ratings better together than
  any component alone. Personality traits correlate with componential
  items. No synchronization, no within-episode measure, no physiology
  recorded.
---
<!-- inactive-ok-file: LIT-tmp7rygg LIT-tmp9qnrb NOTE-tmpocnqb LIT-tmp5ejuc — drafts filed in the same tranche -->

# NOTE-tmpyz7qv: A Multi-Componential Approach to Emotion Recognition and the Effect of Personality

## Contribution

A data-driven mapping between discrete emotions and the full
componential space, from reports of experienced (not semantic) emotion.
It extends a conference paper of the same group.

## Key insight

Discrete emotion ratings are recoverable from componential descriptors.
The feeling items alone carry little more than valence and arousal, and
the other components add what discriminates emotions of similar valence
and arousal.

## Assumptions

- That self-report after a clip captures appraisal, motivation, physiology
  and expression. The authors concede that self-report of physiology and
  expression "may not be very accurate and objective recording are more
  desirable" (p. 12).
- That a passive viewer's appraisals can be probed with CoreGRID items.
  Items such as "it was caused by my own behavior" were removed for
  having no variance in that setting (§III.A).

## Key results

- Hierarchical clustering of the emotion centroids (equation 1, weighted
  by each discrete-emotion rating) splits positive from negative, then
  happiness, serenity, distress, anger and surprise.
- Six varimax principal components explain about 59% of the variance; the
  first (30%) is action tendency, the second (14%) pleasant feeling.
- Expression is strong for most emotions but weak for sadness, surprise,
  disgust and calm. Appraisal is the most informative component for
  surprise and disgust, physiology for fear and anxiety.
- Nonlinear classifiers (random forest, RBF SVM) did not beat logistic
  regression significantly.
- Adding personality scores to the components did not improve
  prediction.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Emotional experience needs more than valence and arousal to describe | moderate | six PCA dimensions; agrees with GRID work |
| C2 | All components together predict discrete emotions better than any one | moderate | cross-validated ordinal regression, Table II |
| C3 | Personality shapes componential responses more than feelings | weak | uncorrected partial correlations, p < 0.01 |

## Concepts

- **componential profile**: the weighted mean of CoreGRID ratings for a
  discrete emotion.
- **MAE^M**: macro-averaged mean absolute error, for ordinal ratings with
  imbalanced classes.

## Connections

Cites Meuleman and Rudrauf ([LIT-tmp5ejuc](../literature.d/LIT-tmp5ejuc.md)) as the only prior
study of the same kind, and contrasts its active induction with this
study's passive one. Its film set and items were reused in the fMRI
study of the same group ([LIT-tmp9qnrb](../literature.d/LIT-tmp9qnrb.md), [NOTE-tmpocnqb](NOTE-tmpocnqb.md)).

## Bearing on the record

**A per-episode measure of synchronization?** No, and candidly the
paper is further from one than the owner's query hoped. It never uses the
word. Each episode is a whole clip, about two minutes, rated once after
viewing, and the authors name the problem themselves: "First, the
emotional assessments for each clip is done at global level which
neglects the presence of different events in the clip with potentially
different emotional" content (p. 11). The coherence it reports, clusters
and principal components, is computed across 1,567 surveys. It is the
structure of the population's ratings, not coordination within anyone's
episode.

**Signed, or which tendency prevails?** Partly signed: its first
principal component is action tendency and its second pleasant versus
unpleasant feeling. But nothing says which tendency won a conflict.
Items such as "want the situation to continue" and "feel the urge to
stop what was happening" are rated separately and could both be high,
which is the ambivalent case [QUESTION-tmpsqwu5](../questions.d/QUESTION-tmpsqwu5.md) needs separated from
neutrality. The paper does not look at such co-occurrences.

**Anything for [QUESTION-tmp0oife](../questions.d/QUESTION-tmp0oife.md)?** Little. The feeling items ("feel
good", "feel bad") are retrospective reports, which the question rules
out for validating its third layer, and they are not a hedonic marker
independent of choice. Its sequel ([NOTE-tmpocnqb](NOTE-tmpocnqb.md)) is where
this design produces something the record can use.

Filed because the owner asked, and because the sequel cannot be read
without it.

## Limitations

Passive, vicarious induction; global ratings per clip; crowdsourced
online data; all components self-reported; no correction for multiple
comparisons in the personality analysis. The paper's own second
hypothesis (personality effects beyond valence and arousal) is tested
only by correlation.

## Open questions

None for the record beyond those its sequel takes up.
