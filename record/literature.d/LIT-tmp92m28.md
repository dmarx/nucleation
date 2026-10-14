---
status: Active
status_note: 'read in full 2026-10-13 ([NOTE-tmpmnv6y](../notes.d/NOTE-tmpmnv6y.md)) from the version of record, the CC BY-NC-ND JATS text that Europe PMC serves for PMC12773730 (https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12773730/fullTextXML), with the SI Appendix read from the arXiv preprint (https://arxiv.org/abs/2502.09880), sections 1, 2 and 6 in full and 3–5 skimmed. Worth reading as the one large-sample study of how crowd-maintained images on r/place are overthrown: the defended image is an equilibrium of attack and repair, and its failure has many precursors, several of them about the defending community. It supports [CLAIM-tmpjhd7t](../claims.d/CLAIM-tmpjhd7t.md) ([THEORY-tmp07t7w](../theory.d/THEORY-tmp07t7w.md)), with the qualification that some compositions last through neglect, and makes [CLAIM-tmpgfyls](../claims.d/CLAIM-tmpgfyls.md)''s frame-relativity operational; it does not answer [QUESTION-tmpmrm3n](../questions.d/QUESTION-tmpmrm3n.md).'
title: 'Interpretable early warnings using machine learning in an online game-experiment'
version: 1
history:
- version: 1
  date: '2026-10-13'
  note: >-
    Filed, not read. Citation checked against Crossref on 2026-10-13: Crossref gives the online date 2026-01-02. The exchange gave no authors.
    Not held in the Anthology of the SOTA: a grep of its record/ (clone of 2026-10-13, commit d1573d2) for the authors, the title and the DOI found nothing.
    Read the same day (NOTE-tmpmnv6y).
tags:
- complex-systems
- social-science
date: '2026-10-13'
published: '2026-01-02'
doi: '10.1073/pnas.2503493122'
first_author: 'Falmagne'
keywords:
- 'r/place'
- 'early warning signals'
- 'regime transitions'
- 'collective behaviour'
implementations: []
summary: >-
  Falmagne, Stephenson and Levin (2026), PNAS 123(1). On about 10,900
  crowd-built r/place compositions of 2022, gradient-boosted trees over 19
  composition-level series predict the time until an image is abruptly
  overrun: half the overthrows within 20 minutes at 3.6% false positives,
  far better than generic indicators, and still good on 2023. The precursors
  are plural (attack outrunning defence, turbulent history, little accepted
  change, uncoordinated activity, simple images), and about a quarter of
  overthrows give no warning.
---
<!-- inactive-ok-file: CLAIM-tmpjhd7t CLAIM-tmpgfyls THEORY-tmp07t7w — Proposed or Deferred; open claims, unread works and readings cited as open, nothing here rests on their being settled -->

# LIT-tmp92m28: Interpretable early warnings using machine learning in an online game-experiment

Falmagne, G., Stephenson, A. B., & Levin, S. A. (2026). Interpretable early warnings using machine learning in an online game-experiment. *PNAS* 123(1). DOI 10.1073/pnas.2503493122

## Key takeaways

Read in full ([NOTE-tmpmnv6y](../notes.d/NOTE-tmpmnv6y.md)); SI read in part.

- **The unit and the event.** A composition is an Atlas-mapped image. Its
  state is the share of pixels differing from the image held over the last
  three hours. An overthrow is an abrupt jump of that share from a stable
  period.
- **Predictable, partly.** Half the overthrows are caught within 20 minutes
  at 3.6% false positives (ROC AUC 0.835), with skill up to six hours
  ahead. The predictor transfers from 2022 to 2023. At 20 minutes, 27% of
  transitions are predicted no better than chance.
- **No single warning signal.** Variance and autocorrelation trends do far
  worse. Critical slowing down appears close to the overthrow, and a mild
  speeding up appears earlier. A toy model with damage-driven recruitment
  of defenders produces both.
- **Social precursors, read from placements.** Low past defence, little
  accepted change, uncoordinated activity and simple images precede
  overthrow. Very low past activity makes a composition safer. These
  readings come from SHAP curves, and the authors call them conjectural.

## Why this is here

Registered for the r/place case ([CASE-tmpd83bj](../cases.d/CASE-tmpd83bj.md)), as the nearest study of when
a maintained pattern stops being maintained ([CLAIM-tmpjhd7t](../claims.d/CLAIM-tmpjhd7t.md)). The reading
bears that out. The paper's apparatus is built on the maintenance regime,
and its return rate is close to the repair hazard A8 proposed, though
without a per-site baseline. It also finds that some compositions last
because nobody attacks them, which is the alternative [CLAIM-tmpjhd7t](../claims.d/CLAIM-tmpjhd7t.md)'s
`defeated_if` names, and it does not measure how common each route is
([THEORY-tmp07t7w](../theory.d/THEORY-tmp07t7w.md)). The filing's summary was right on the headline numbers.
It did not say that the precursors are plural, that some of them concern
the defenders, or that many transitions are unpredictable. Collective human
behaviour is not ML practice, so the anthology does not hold it, although it
uses a classifier.
