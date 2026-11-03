---
status: Open
title: 'Do the concepts a language model''s workspace makes reportable across an Assistant episode share an episode-level mixture, so that an LDA-style admixture over J-lens readouts predicts their co-occurrence better than one persona selected per conversation and better than independent draws per position; does intervening on the inferred mixture change which concepts reach report while leaving the consumers that bypass the workspace unchanged; and if two models matched on persona distribution and mixture differ under such interventions, whose will-organization is that difference: the simulated Assistant''s, the network''s or the deployed system''s?'
version: 1
tags:
- representation-learning
- probabilistic-modeling
- agency
date: '2026-11-02'
line: learned-structure
summary: >-
  From the owner's U10 and U12 of the exchange "Assess SDT Coverage"
  (2026-11-02): "the J-Space is basically this kind of LDA", and H2, not
  H1, is the LDA because of the Dirichlet over each episode's mixture
  (CLAIM-tmphbnqm). With U9's question, how to read an LDA as
  will-organization under the Persona Selection Model. The paper is held
  and read (LIT-1347, NOTE-1069). Two corrections make the analogy a
  question, not a finding: J-lens directions name single tokens, so a
  J-space readout is LDA's bag of words, not its topics; and the
  workspace's privilege is selective, where an LDA topic mediates every
  word.
---
<!-- inactive-ok-file: CLAIM-tmpwh2jo QUESTION-275 QUESTION-276 THEORY-1226 THEORY-490 — Proposed, Open, Deferred or Unavailable; cited from the exchange "Assess SDT Coverage" of 2026-11-02 as open, works registered unread among them -->

# QUESTION-tmpildq9: Do the concepts a language model's workspace makes reportable across an Assistant episode share an episode-level mixture, so that an LDA-style admixture over J-lens readouts predicts their co-occurrence better than one persona selected per conversation and better than independent draws per position; does intervening on the inferred mixture change which concepts reach report while leaving the consumers that bypass the workspace unchanged; and if two models matched on persona distribution and mixture differ under such interventions, whose will-organization is that difference: the simulated Assistant's, the network's or the deployed system's?

## Why it is a question

Gurnee et al. 2026 (LIT-1347, NOTE-1069; THEORY-865, THEORY-1226) find a
sparse workspace: at each position a nonnegative combination of at most
about 25 directions, each named by one vocabulary token, which report and
flexible inference route through and which continuation and anomaly
detection bypass.

The owner's analogy says this is an LDA. Read precisely, it is part of one:

- **Words, not topics.** An LDA topic is a distribution over the whole
  vocabulary. A J-lens direction names one token, and the paper calls its
  readout "a bag of concepts with no binding". So J-space supplies at most
  LDA's input.
- **No episode mixture.** Each position's code is fitted on its own.
  CLAIM-tmphbnqm makes the per-episode Dirichlet mixture what separates H2
  from H1, and the paper fits none.
- **Selective privilege.** In LDA no word bypasses its topic assignment.
  In the paper some consumers bypass the workspace. The owner's U11, that
  the workspace's position "is identical to the position of a 'topic' in
  LDA", holds only for the consumers that route through it.

So whether an episode-level mixture over workspace readouts exists is the
H1-against-H2 test for a language model, and CLAIM-tmphbnqm's
within-against-between agreement is its statistic. A12 §4 proposed it.

## What would answer it

- **The fit.** Within-episode against between-episode co-occurrence of
  J-lens concepts over Assistant rollouts, compared under an admixture, one
  persona per conversation (a → 0) and independent draws (a → ∞).
- **The intervention.** Clamp or swap the inferred mixture and see whether
  report changes while the bypassing consumers do not. Fit alone does not
  settle organization (CLAIM-tmpwh2jo, CLAIM-414, CLAIM-135).
- **The bearer.** A will-organization is agent-indexed (TERM-023). CLAIM-418
  and THEORY-490 hold the candidate bearers. The question's last clause asks
  which a difference under intervention would belong to.

## Bears on

CLAIM-454, QUESTION-275, QUESTION-276 and TERM-072.
