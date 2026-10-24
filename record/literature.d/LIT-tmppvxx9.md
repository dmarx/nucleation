---
status: Active
status_note: >-
  read in full 2026-10-24 ([NOTE-tmpldqrp](../notes.d/NOTE-tmpldqrp.md)) from the CC BY version of
  record; worth reading for the derivation that avoidance far from a threat
  needs no overestimate of the threat, only an expectation that one will
  fail to avoid it later, which spreads threat value backward across a
  decision process. Simulations only, matched qualitatively to published
  findings (earlier cash-out, behavioural inhibition, aversive pruning);
  the predicted loss of the free-choice premium is untested, and the
  persistence of avoidance after the misbelief is corrected is argued,
  not simulated.
title: 'Anxiety, Avoidance, and Sequential Evaluation'
version: 2
history:
- version: 1
  date: '2026-10-24'
  note: >-
    Filed, not read. Registered unread from the owner's exchange of
    2026-10-23/24, shared at
    https://chatgpt.com/share/6adc1ece-bb28-83e9-a8f6-cadf0f8b7113,
    where it is cited at turn U14. Citation checked against Crossref and
    PubMed (PMID 34036174) on 2026-10-24: Samuel Zorowitz, Ida
    Momennejad and Nathaniel D. Daw, Computational Psychiatry 4,
    published online 1 March 2020. A bioRxiv preprint
    (doi:10.1101/724492), which Crossref links as its preprint, was
    posted on 5 August 2019, which is `published:`. The summary follows
    the abstract on Crossref and PubMed.
- version: 2
  date: '2026-10-24'
  note: >-
    Read in full (NOTE-tmpldqrp) from the version of record, Computational
    Psychiatry 4: 1–17 (2020), the publisher's PDF at cpsyjournal.org,
    where the DOI now resolves, licensed CC BY 4.0 (received 4 August
    2019, accepted 29 December 2019). Figures read from their captions;
    the code was not run. Status set to Active. The summary is accurate;
    the page range 1–17 is added to the citation, and the summary now says
    that the misbelief concerns the agent's own future control while the
    danger is represented correctly, and that no data are fitted.
tags:
- psychopathology-and-treatment
- learning-and-conditioning
date: '2026-10-24'
published: '2019-08-05'
doi: '10.1162/cpsy_a_00026'
first_author: 'Zorowitz'
keywords:
- 'anxiety'
- 'avoidance'
- 'sequential evaluation'
- 'reinforcement learning'
- 'pessimism'
- 'decision theory'
- 'computational psychiatry'
implementations: []
summary: >-
  Zorowitz, Momennejad & Daw (2020; preprint 2019). A decision-theoretic
  analysis and reinforcement-learning simulations of maladaptive
  avoidance, with no data fitted. In sequential evaluation the chance to
  avoid danger later should make it less threatening now; a pessimistic
  false belief that one's own later avoidance will fail, with the danger
  represented correctly, propagates fear and avoidance to situations far
  before the threat. This one bias reproduces qualitatively exaggerated
  threat appraisal, fear generalization, persistent avoidance and
  laboratory findings on approach–avoid conflict and loss avoidance, and
  predicts a reduced free-choice premium in anxiety.
supports:
- CLAIM-tmp8z857
---
<!-- inactive-ok-file: CLAIM-tmp8z857 THEORY-tmpgos5n — Proposed; the claim this was registered for and the reading filed from it, named -->
# LIT-tmppvxx9: Anxiety, Avoidance, and Sequential Evaluation

Zorowitz, S., Momennejad, I. & Daw, N. D. (2020). Anxiety, avoidance, and sequential evaluation. *Computational Psychiatry* 4: 1–17. doi:10.1162/cpsy_a_00026. Preprint: bioRxiv, doi:10.1101/724492 (2019).

## Key takeaways

*From the reading, [NOTE-tmpldqrp](../notes.d/NOTE-tmpldqrp.md). Page numbers are the journal's.*

- **The core observation.** "If danger can be avoided later, it poses less
  threat now" (p. 1): under optimal evaluation avoidable threats do not
  propagate to earlier states.
- **The bias.** A β-pessimistic Bellman equation: the agent chooses
  optimally but values each action as if it will act badly later.
  "Importantly, this belief is false under the model" (p. 4). The danger
  itself is represented correctly.
- **What it produces.** Threat value spreads across the state space;
  avoidance starts early and wide; earlier cash-out in the balloon task,
  slower approach under threat and aversive pruning follow, matched
  qualitatively to cited findings (pp. 3–7).
- **Persistence.** "Frustratingly, these biased estimates of value may
  still remain even after a misbelief in the efficacy of future action is
  corrected for in a course of therapy" (p. 8), argued by analogy to
  model-free relearning, not simulated.
- **A prediction.** Anxious people should show a reduced free-choice
  premium (p. 9), untested.
- **Scope.** Prospective anxiety (generalized, social); not OCD
  compulsions or PTSD memory (pp. 11–12).

## Why this is here

The exchange cited it at turn U14 for a computational account of anxious avoidance in which a pessimistic belief about one's own future control spreads avoidance backward in time. The abstract matches.

**Corrected 2026-10-24, from the reading.** The exchange's description is
accurate; "backward in time" is, in the model, backward across antecedent
states. The reading adds that the paper has no data of its own. For
[CLAIM-tmp8z857](../claims.d/CLAIM-tmp8z857.md) it is a rival account with the threat represented
correctly and a belief about one's own future control doing the work, so a
test that holds only the threat estimate fixed cannot separate the two; and
its explanation for avoidance outlasting a corrected belief is cached
value, the habit-with-memory alternative the claim's defeater names. Filed
from it: [THEORY-tmpgos5n](../theory.d/THEORY-tmpgos5n.md).
