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
  ([CLAIM-tmphbnqm](../claims.d/CLAIM-tmphbnqm.md)). With U9's question, how to read an LDA as
  will-organization under the Persona Selection Model. The paper is held
  and read ([LIT-1347](../literature.d/LIT-1347.md), [NOTE-1069](../notes.d/NOTE-1069.md)). At the level of a concept the analogy
  holds, as the owner put it at review: "J-space is a concept space.
  concepts are distributions over words. concepts are directions in a
  word space." What keeps it a question: the paper fits no episode-level
  mixture, concepts combine additively in logits rather than as a
  mixture, and the workspace's privilege is selective, where an LDA topic
  mediates every word.
---
<!-- inactive-ok-file: NOTE-tmpagiju — Proposed, Open, Deferred, Unfetched, Unavailable or new; cited as open -->
<!-- inactive-ok-file: CLAIM-tmpwh2jo THEORY-1226 THEORY-490 — Proposed, Open, Deferred or Unavailable; cited from the exchange "Assess SDT Coverage" of 2026-11-02 as open, works registered unread among them -->

# QUESTION-tmpildq9: Do the concepts a language model's workspace makes reportable across an Assistant episode share an episode-level mixture, so that an LDA-style admixture over J-lens readouts predicts their co-occurrence better than one persona selected per conversation and better than independent draws per position; does intervening on the inferred mixture change which concepts reach report while leaving the consumers that bypass the workspace unchanged; and if two models matched on persona distribution and mixture differ under such interventions, whose will-organization is that difference: the simulated Assistant's, the network's or the deployed system's?

## Why it is a question

Gurnee et al. 2026 ([LIT-1347](../literature.d/LIT-1347.md), [NOTE-1069](../notes.d/NOTE-1069.md); [THEORY-865](../theory.d/THEORY-865.md), [THEORY-1226](../theory.d/THEORY-1226.md)) find a
sparse workspace: at each position a nonnegative combination of at most
about 25 directions, each indexed by one vocabulary token, which report and
flexible inference route through and which continuation and anomaly
detection bypass.

The owner's analogy says this is an LDA. Read precisely, it is part of one:

- **Concepts are topic-like.** An LDA topic is a distribution over the
  whole vocabulary. So is a J-lens concept read through the lens: the
  token's J-lens vector is a direction in the residual stream, and
  softmax(W_U norm(Jℓ h)) gives it a score for every token, peaked at the
  token that indexes it ([NOTE-1069](../notes.d/NOTE-1069.md), p. 8). "Names one token" is the
  concept's index, not its support. Two differences remain. There is one
  concept per vocabulary token, anchored to it, not a smaller set learned
  from data, which is why concepts without a single-token name read
  poorly. And concepts combine additively in logits: a workspace state
  Σ a_k j_k with a_k ≥ 0 gives word probabilities proportional to
  exp(Σ a_k ℓ_k(w)), up to the overall scale the lens's
  normalization sets, a product of experts, where LDA mixes, Σ θ_k φ_k(w).
  A log-linear topic model is the closer analogue.
- **No episode mixture.** Each position's code is fitted on its own.
  [CLAIM-tmphbnqm](../claims.d/CLAIM-tmphbnqm.md) makes the per-episode Dirichlet mixture what separates H2
  from H1, and the paper fits none.
- **Selective privilege.** In LDA no word bypasses its topic assignment.
  In the paper some consumers bypass the workspace. The owner's U11, that
  the workspace's position "is identical to the position of a 'topic' in
  LDA", holds only for the consumers that route through it.

So whether an episode-level mixture over workspace readouts exists is the
H1-against-H2 test for a language model, and [CLAIM-tmphbnqm](../claims.d/CLAIM-tmphbnqm.md)'s
within-against-between agreement is its statistic. A12 §4 proposed it.

## What would answer it

- **The fit.** Within-episode against between-episode co-occurrence of
  J-lens concepts over Assistant rollouts, compared under an admixture, one
  persona per conversation (a → 0) and independent draws (a → ∞).
- **The intervention.** Clamp or swap the inferred mixture and see whether
  report changes while the bypassing consumers do not. Fit alone does not
  settle organization ([CLAIM-tmpwh2jo](../claims.d/CLAIM-tmpwh2jo.md), [CLAIM-414](../claims.d/CLAIM-414.md), [CLAIM-135](../claims.d/CLAIM-135.md)).
- **The bearer.** A will-organization is agent-indexed ([TERM-023](../terms.d/TERM-023.md)). [CLAIM-418](../claims.d/CLAIM-418.md)
  and [THEORY-490](../theory.d/THEORY-490.md) hold the candidate bearers. The question's last clause asks
  which a difference under intervention would belong to.

## Bears on

[CLAIM-454](../claims.d/CLAIM-454.md), [QUESTION-275](QUESTION-275.md), [QUESTION-276](QUESTION-276.md) and [TERM-072](../terms.d/TERM-072.md).

## Note of 2026-11-03: a confound, and more bearers

The within- against between-episode test would be confounded by input-driven
drift: the Assistant Axis finds persona following the latest user message
([NOTE-tmpagiju](../notes.d/NOTE-tmpagiju.md)). It needs the user's messages as covariates, or a per-turn state
model. The Persona Selection Model distinguishes more bearers than the three
listed: persona, actor, author or narrative, router and the network
([NOTE-tmpftp86](../notes.d/NOTE-tmpftp86.md)).
