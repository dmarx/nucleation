---
status: Active
status_note: >-
  read in full 2026-10-24 (NOTE-tmpke0z1) from arXiv v1, the AAMAS 2017
  paper; worth reading as the paper that moved social dilemmas from matrix
  games to learned policies in Markov games. Two two-player games, Gathering
  (apples, and a beam that removes the rival for a while) and Wolfpack
  (lone or joint capture of prey), both yield Prisoner's Dilemma payoff
  matrices when the learned policies are played off, yet respond in
  opposite directions to agent capacity: a larger network makes Gathering
  agents more aggressive and Wolfpack agents more cooperative, because
  aggression is the harder policy to implement in one and cooperation in
  the other. Agents learn aggression where apples are scarce. It is a
  descriptive simulation with independent learners, no figures of spread,
  and no protective institution or depletable commons.
title: 'Multi-agent Reinforcement Learning in Sequential Social Dilemmas'
version: 1
history:
- version: 1
  date: '2026-10-24'
  note: >-
    Filed and read 2026-10-24 for the owner's question of how the record
    stands on multi-agent learning, as a testbed for protection and the
    commons (CLAIM-tmp28sti). Published in the Proceedings of AAMAS 2017
    (São Paulo, 8–12 May 2017), as the arXiv copy's footer states. Read in
    full from arXiv:1702.03037v1 (10 February 2017), the only version,
    licence arXiv's non-exclusive distribution licence, 10 pp., extracted
    by pdftotext. The reference list was skimmed; figures were read from
    captions and text. `published:` is v1's date (ADR-002).
tags:
- game-theory
- social-science
- learning-theory
- anthology-candidate
date: '2026-10-24'
published: '2017-02-10'
arxiv: '1702.03037'
first_author: 'Leibo'
keywords:
- 'social dilemmas'
- 'cooperation'
- 'Markov games'
- 'agent-based social simulation'
- 'non-cooperative games'
- 'empirical game-theoretic analysis'
- 'deep Q-networks'
implementations: []
summary: >-
  Leibo, Zambaldi, Lanctot, Marecki & Graepel (2017). Defines a sequential
  social dilemma as a Markov game whose cooperative and defecting policies,
  played against each other, give payoffs satisfying the social dilemma
  inequalities. Independent deep Q-learners in a fruit-Gathering game learn
  aggression when apples are scarce or a tagged rival is out long; in
  Wolfpack they hunt together when the joint-capture bonus and radius are
  high. Both games embed Prisoner's Dilemmas, but network size raises
  defection in Gathering and lowers it in Wolfpack, which no matrix game
  captures.
---
<!-- inactive-ok-file: NOTE-tmpke0z1 THEORY-tmpc4gg9 CLAIM-tmp28sti — filed from this reading, and the claim it bears on, named -->

# LIT-tmphih4i: Multi-agent Reinforcement Learning in Sequential Social Dilemmas

Leibo, J. Z., Zambaldi, V., Lanctot, M., Marecki, J. & Graepel, T. (2017). Multi-agent reinforcement learning in sequential social dilemmas. *Proceedings of the 16th International Conference on Autonomous Agents and Multiagent Systems (AAMAS 2017)*. arXiv:1702.03037.

## Key takeaways

*From the reading, NOTE-tmpke0z1. Page numbers are arXiv v1's.*

- **Cooperation is a property of policies.** "Cooperativeness is a
  property that applies to policies, not elementary actions" (p. 1). A
  Markov game is a sequential social dilemma when policies classed as
  cooperative and defecting, played off against each other, give an
  empirical payoff matrix that satisfies the social dilemma inequalities.
- **Scarcity breeds aggression.** In Gathering, agents trained where
  apples are scarce or a tagged rival stays out long learn to tag far
  more. "When learning does change beam-use rate, it is almost always to
  increase it" (p. 5).
- **Same matrix, different games.** Both games' empirical matrices are
  mostly Prisoner's Dilemmas (Wolfpack also gives Chicken and Stag Hunt),
  yet a larger network raises defection in Gathering and lowers it in
  Wolfpack: what is harder to learn to implement is less often done.
- **Descriptive, not prescriptive.** Independent learners, each treating
  the other as environment; the model "only addresses whatever part of
  cooperative behavior arises “by habit”" (p. 6).

## Why this is here

Filed on 2026-10-24 as the lead's testbed for protection and the commons
(CLAIM-tmp28sti). The reading narrows that (NOTE-tmpke0z1): these are
two-player games with no protective regime and no depletable resource,
and conditions are fixed during training, so nothing here measures
whether aggression or protection recedes when scarcity does. The method,
tracking a social behaviour metric while manipulating the environment,
could be turned to the claim's test. Filed THEORY-tmpc4gg9. It carries
`anthology-candidate` as an ML method, and no instruction for practice.
