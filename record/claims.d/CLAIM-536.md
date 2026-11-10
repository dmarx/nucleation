---
number: 536
status: Active
formerly:
- CLAIM-tmphbnqm
title: 'A categorical model of perspectives and an LDA-style model differ in where the mixture lives: the first draws every act''s perspective from one fixed categorical distribution, the second gives each episode its own mixture, drawn from a Dirichlet, and draws each act from it; the Dirichlet is a distribution over mixtures, not the perspectives themselves, and with symmetric concentration a over K perspectives two acts in one episode share a perspective with probability (a + 1)/(Ka + 1) against 1/K across episodes, so the concentration runs from one perspective per episode, as in persona selection (a → 0), to a fresh independent draw for every act (a → ∞)'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation: a symmetric Dirichlet for which the
  within-episode agreement differs from (a + 1)/(Ka + 1), or the
  between-episode agreement from 1/K. Or a showing that the H1 the owner
  meant is neither limit, for instance a Markov-switching persona model,
  which is neither a mixture nor an admixture; that would leave the
  derivation standing and narrow the claim's reading of H1.
tags:
- probabilistic-modeling
- mathematics
date: '2026-11-02'
line:
- learned-structure
- formal-apparatus
grounds:
- LIT-1948
complements:
- CLAIM-543
- CLAIM-540
bears_on:
- QUESTION-276
- QUESTION-370
summary: >-
  The owner's U12 of the exchange "Assess SDT Coverage" (2026-11-02),
  stated precisely: "H1 isn't LDA like though. that's my point. it's a
  categorical distribution. the topics in H@ are the dirichlet
  distribution which parameterizes the categorical distribution, which is
  what distinguishes H2 from H1 and why H2 is an LDA." The structure is
  right; one word is not. The Dirichlet is a distribution over each
  episode's mixture, and the topics, here the perspectives, are the
  categories that mixture weights. The agreement formula, derived here and
  checked by simulation, shows that both readings of H1 are limits of H2.
---

# CLAIM-536: A categorical model of perspectives and an LDA-style model differ in where the mixture lives: the first draws every act's perspective from one fixed categorical distribution, the second gives each episode its own mixture, drawn from a Dirichlet, and draws each act from it; the Dirichlet is a distribution over mixtures, not the perspectives themselves, and with symmetric concentration a over K perspectives two acts in one episode share a perspective with probability (a + 1)/(Ka + 1) against 1/K across episodes, so the concentration runs from one perspective per episode, as in persona selection (a → 0), to a fresh independent draw for every act (a → ∞)

## The claim

Two models of which of K perspectives governs each act y_{d,n} of an
episode d:

- **H1, categorical.** z_{d,n} ~ Cat(π) for one fixed π shared by every
  episode.
- **H2, LDA-style admixture** (Blei, Ng and Jordan, [LIT-1948](../literature.d/LIT-1948.md)). Each episode
  draws its own mixture θ_d ~ Dir(α), then z_{d,n} ~ Cat(θ_d). In smoothed
  LDA each topic's distribution over outputs is an independent draw from one
  shared exchangeable Dirichlet, Dir(η) (§5.4), which is not the one at issue
  here.

What separates them is the per-episode mixture, as the owner said. The
owner's "the topics … are the dirichlet" names the wrong thing. The
Dirichlet is a distribution over mixtures. The perspectives are the
categories each mixture weights. A12's parenthesis has the repair:
"Strictly speaking, θ_d is the topic-mixture vector drawn from the
Dirichlet; the topics are the categories it weights."

**Agreement within and across episodes.** With α = (a, …, a), the moments of
the Dirichlet give E[θ_k²] = a(a + 1)/(Ka(Ka + 1)). So

    P(z_{d,1} = z_{d,2}) = Σ_k E[θ_k²] = (a + 1)/(Ka + 1),

while for acts in different episodes, whose mixtures are independent,
P(z_{d,1} = z_{d',1}) = Σ_k E[θ_k] E[θ'_k] = 1/K.

- As a → 0 the within-episode agreement tends to 1: one perspective per
  episode. That is the mixture of unigrams, and persona selection read as
  selection.
- As a → ∞ it tends to 1/K: every act an independent categorical draw, A12's
  H1.

So the owner's H1 has two readings, one draw per conversation or one per
act, and they are the two limits of H2's concentration. H2 is the family
between them. The contrast is testable by within-episode against
between-episode co-occurrence ([QUESTION-370](../questions.d/QUESTION-370.md)).

**Checked** by simulation (400,000 episodes each, 2026-11-02): K = 3, a = 1
gives 0.499 within against 0.5 predicted, and 0.3335 across against 1/3; K =
5, a = 0.2 gives 0.6002 against 0.6; K = 4, a = 10 gives 0.270 against
0.268.

## What it does not say

- **That the hierarchy is what A12 said it is.** A12 credited the 1/2
  against 1/3 agreement (K = 3, a = 1) to "the hierarchy alone". A single
  uncertain mixture shared by both draws, a Pólya urn with no hierarchy,
  gives the same 1/2. What makes LDA hierarchical is many episodes, each with
  its own θ_d, sharing α. Its signature is the within-against-between
  contrast, not the within-episode figure alone.
- **That an admixture is a feature allocation.** [CASE-165](../cases.d/CASE-165.md)'s
  beta–Bernoulli model lets a member hold several features at once, and
  [CLAIM-454](CLAIM-454.md)'s "feature allocation" is that sense. An admixture puts one
  component behind each act. Which H2 the record means matters for
  [QUESTION-276](../questions.d/QUESTION-276.md)'s overlap requirement.
- **That an H2 fit is organization.** An LDA's components are exchangeable
  given θ_d ([CLAIM-543](CLAIM-543.md)), and its reinforcement of a run of choices is
  the observer's learning ([CLAIM-540](CLAIM-540.md)).

## Note of 2026-11-03: LDA and the Assistant Axis, read

The account of LDA matches the paper ([NOTE-1519](../notes.d/NOTE-1519.md)), which itself names the
one-topic-per-document comparison (a "Dirichlet-multinomial clustering model",
p. 997; the mixture of unigrams, §4.2). The agreement formula was
re-simulated. Two refinements: the symmetric a → 0 limit is the mixture of
unigrams with uniform p(z), where the paper's has a free p(z), the limit of
Dir(sπ); and the a → ∞ limit is the paper's unigram model once z is
marginalized, so per-act independent personas are unidentifiable from one
output distribution. And the Assistant Axis ([NOTE-1505](../notes.d/NOTE-1505.md)) finds the persona
following the latest user message within a conversation (R² 0.53–0.77 against
0.10), neither limit: the switching model this claim's defeater names. So
persona selection read as one persona per conversation does not fit what
either source describes. The derivation stands.

## Note of 2026-11-06: what the Assistant Axis's 0.10 measures

The note of 2026-11-03 cites the Assistant Axis as finding the persona
following the latest user message "(R² 0.53–0.77 against 0.10)". The 0.10
is the user-message embeddings' prediction of the change in position from
the previous response, not a fit of the previous position; the paper never
tests the previous position as a predictor ([NOTE-1505](../notes.d/NOTE-1505.md), now Read;
[THEORY-1339](../theory.d/THEORY-1339.md)). What the note needs stands: position changes within a
conversation and follows the user's messages, so one persona per
conversation does not fit. Whether the process carries state (a switching
model) or is driven by input alone is not settled by that analysis; it is
[QUESTION-443](../questions.d/QUESTION-443.md)'s. The derivation and the status are unchanged.
