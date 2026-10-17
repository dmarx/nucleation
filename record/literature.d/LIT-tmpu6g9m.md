---
status: Active
status_note: >-
  read 2026-10-16 ([NOTE-tmpi40rc](../notes.d/NOTE-tmpi40rc.md)) in full, from the authors' accepted manuscript on UCL Discovery; worth reading as the short statement, within active inference, that attentional gain (the estimated precision of currently available data) and salience (the expected information gain of an action that would acquire new data, usually a saccade) are distinct computations with distinct disorders, hallucination and neglect, and that they are coupled because a saccade is a prediction of high precision at the location foveated. Read it knowing that it is a five-page review with no new data or simulations; that it assigns covert spatial attention to gain by stipulation; that it never treats gain as an action; and that it ends by endorsing the premotor theory, so covert attention changes what is observed only by biasing overt saccades.
title: 'Attention or salience?'
version: 2
history:
- version: 1
  date: '2026-10-16'
  note: >-
    Filed, not read. Citation checked against Crossref and OpenAlex on 2026-10-16. Not held in the Anthology of the SOTA: a grep of its record/ (clone of 2026-10-16, commit d1573d2) for the authors and the title found nothing.
- version: 2
  date: '2026-10-16'
  note: >-
    Read in full (NOTE-tmpi40rc) from the authors' accepted manuscript, UCL Discovery eprint 10058428 (CC BY-NC-ND 4.0; found through OpenAlex and a web search after Europe PMC listed no full text); page numbers are the manuscript's, the published version was not seen. Status Deferred to Active. The summary is rewritten from the reading: it was right on the distinction, and now adds the paper's reconciliation of the two, its disorders and its endorsement of the premotor theory. "Why this is here" is corrected: attention weights data whose content the world and sensors fix, not the generative model, and attention changes what is observed only through overt saccades.
tags:
- neuroscience
- probabilistic-modeling
- cognition
date: '2026-10-16'
published: '2018-10-15'
doi: '10.1016/j.copsyc.2018.10.006'
first_author: 'Parr'
keywords:
- 'attention'
- 'salience'
- 'precision'
- 'active inference'
- 'epistemic value'
implementations: []
summary: >-
  Parr & Friston (2019). A short review. Attention as gain control weights currently available sensory data by the estimated precision of the mapping from their causes; salience is the expected information gain of an action, typically a saccade, that would acquire new data. They are distinct, with gain failures giving hallucinations and salience failures neglect, but coupled: a saccade is a prediction that the foveated location will be sensed precisely, so covert attention to a place biases an overt saccade there, which the authors take to support the premotor theory.
supports:
- CLAIM-tmp9cjyo
---

# LIT-tmpu6g9m: Attention or salience?

Parr, T. & Friston, K. J. (2019). *Current Opinion in Psychology* 29:1–5. doi:10.1016/j.copsyc.2018.10.006. Accepted manuscript: UCL Discovery, eprint 10058428.

## Key takeaways

*From the reading, [NOTE-tmpi40rc](../notes.d/NOTE-tmpi40rc.md). Page numbers are the accepted manuscript's.*

- **Two selections.** Attention "depends upon estimating the precision of
  sensory data", salience "is a consequence of the need to actively engage
  with the sensorium" (abstract, p. 1). One weights current data, the
  other acquires new data (p. 5).
- **Salience is information gain.** "Salient actions are those that
  solicit unambiguous data that could not have been predicted with a high
  degree of certainty prior to that action" (p. 4).
- **The coupling.** A saccade command is a prediction of high precision at
  the foveated location, so "deployment of covert attention (precision) to
  a given location biases planning in favour of an overt saccade to that
  (salient) location" (p. 5).
- **Disorders.** Gain failures give "false percepts, including
  hallucinations"; neglect is "a disorder of salience attribution"
  (pp. 4–5).
- **Scope.** A review with no new data. Covert spatial attention is
  grouped with gain by stipulation. Gain is never treated as an action.

## Why this is here

Registered for [CLAIM-tmp9cjyo](../claims.d/CLAIM-tmp9cjyo.md), on the standard reading that attention
weights data and salience belongs to action. The reading confirms the
split but not the use. Attentional gain here is inference about
precision, not a mental action. It changes how much a datum counts, not
what the datum is, and the content is fixed by the world and the sensors,
not, as the registration said, by the generative model. Its one route to
changing what is observed is through overt saccades, and the paper ends by
endorsing the premotor theory. So it gives [CLAIM-tmpq9do8](../claims.d/CLAIM-tmpq9do8.md)'s line between
weighting and producing an observation a clean statement, without
supplying an internal loop on either side.

Salience bears on [CLAIM-tmpki5gp](../claims.d/CLAIM-tmpki5gp.md) and [CLAIM-tmpt568z](../claims.d/CLAIM-tmpt568z.md). It makes action a
seeker of data the agent cannot predict, which the counter needs. But it
scores candidate actions by the agent's own precision beliefs, and the
streetlight effect follows, which is the anchor claim's warning.
