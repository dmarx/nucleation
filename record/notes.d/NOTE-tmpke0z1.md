---
status: Read
paper: 'LIT-tmphih4i'
title: 'Leibo et al. — Multi-agent reinforcement learning in sequential social dilemmas'
version: 1
history:
- version: 1
  date: '2026-10-24'
  note: >-
    Read in full on 2026-10-24 from arXiv:1702.03037v1 (10 February 2017),
    the only version, 10 pp., extracted by pdftotext: sections 1–6 with
    every figure caption. Figures 4, 6 and 7 were read from captions and
    text, the plots themselves being garbled in extraction. The reference
    list was skimmed. Page numbers below are v1's. Every quotation was
    checked against the extracted text by script.
date: '2026-10-24'
summary: >-
  A descriptive simulation study. It defines sequential social dilemmas,
  Markov games whose learned cooperative and defecting policies give
  social-dilemma payoffs, and runs independent deep Q-learners on two
  two-player games. Scarcity and costly conflict produce aggression in
  Gathering; group benefit produces joint hunting in Wolfpack; and network
  size moves defection in opposite directions in two games that both embed
  a Prisoner's Dilemma.
---
<!-- inactive-ok-file: THEORY-tmpc4gg9 — Proposed; filed from this reading, named -->
<!-- inactive-ok-file: CLAIM-tmp28sti CLAIM-tmp8z857 CLAIM-423 CLAIM-277 — Proposed or filed in the same pull request; the accounts this reading bears on, named in prose, nothing here rests on them -->

# NOTE-tmpke0z1: Leibo et al. — Multi-agent reinforcement learning in sequential social dilemmas

## What the paper does

**The definition** (section 2). Matrix-game social dilemmas treat
cooperate and defect as atomic, but "Cooperativeness is a property that
applies to policies, not elementary actions" (p. 1). In a two-player
partially observable Markov game, take sets Π_C and Π_D of policies said
to implement cooperation and defection, defined by thresholding a social
behaviour metric. Their long-run payoffs against each other give R, P, S
and T. The game is a sequential social dilemma when, for some state, these
satisfy the usual inequalities: R > P, R > S, 2R > T + S, and greed
(T > R) or fear (P > S).

**The learners** (section 3). Each agent is an independent deep
Q-network with ε-greedy exploration, decaying from 1.0 to 0.1, trained on
a constantly refreshed replay batch. The two learners "each regard the
other as part of the environment" (p. 4). The stance is descriptive: "what social effects emerge
when each agent uses a particular learning rule?" (p. 3). Networks have
two hidden layers of 32 units, episodes 1000 steps, discount 0.99.

**Gathering** (section 5.1). Apples give reward 1 and respawn after
N_apple frames. A beam that hits a player twice removes it for N_tagged
frames, and tagging is never rewarded: "The only potential motivation for
tagging is competition over the apples" (p. 4). After 40 million steps of
training, beam use is high where apples are scarce or N_tagged is long,
and low where apples are plentiful or conflict cheap (Figure 4A). The
differences appear early and persist, and "When learning does change
beam-use rate, it is almost always to increase it" (p. 5). Policies
trained in high-abundance, low-cost settings are labelled cooperative,
those from scarce, high-cost settings defecting, and played against each
other: most empirical games that satisfy the inequalities are
Prisoner's Dilemmas. Greed is the lure of removing the rival; "The fear
motivation reflected the danger of being taken out oneself by a defecting
rival" (p. 5). P > S because mutual taggers alternate time alone, while a
non-tagger never gets any.

**Wolfpack** (section 5.2). Two wolves chase prey; all wolves within the
capture radius share a reward that is larger when both are there. Higher
group bonus and radius give more wolves per capture (Figure 4B). Two
cooperative policies emerge: meet first and hunt together, or find the
prey and wait. The empirical matrices include "all three classic MGSDs,
chicken, stag hunt, and prisoner's dilemma" (p. 5).

**Agent parameters** (section 5.3, Figure 7). Less discounting (0.995
against 0.99) makes agents defect more readily in both games, because
tagging pays only later. A larger replay batch reduces defection in both:
evasion and coordination benefit from more experience of the other agent.
Network size cuts the other way in the two games: more units raise
aggression in Gathering, where targeting a rival is the harder skill, and
lower lone-wolf capture in Wolfpack, where coordination is. The paper's
reading is that the Prisoner's Dilemma matrix cannot see this: "This
rather striking difference between Gathering and Wolfpack is invisible to
the purely matrix game based MGSD-modeling" (p. 6).

**The discussion** (section 6). Which game is the better model of a
situation decides whether cooperation or defection is the "easier-to-learn
“default”" (p. 7). Five learning phenomena are said to be beyond matrix
models, among them that learning which strategic choice to make "often
occurs simultaneously with learning how to efficiently implement said
decision" (p. 7). The method could "simulate the effects of external
interventions on social equilibria" (p. 8), and SSDs could model "the
extraction of renewable vs non-renewable resources" (p. 8).

## What it establishes and what it does not

It establishes a definition and a demonstration: in two small two-player
games, independent learners' cooperativeness depends on scarcity, conflict
cost, discounting, experience and capacity, and two games with the same
embedded matrix respond oppositely to capacity. It does not report seeds,
runs or spread for any figure. Its classification of policies as
cooperative or defecting is by the environment they were trained in, not
by behaviour measured independently. The text and Figure 7 disagree on the
manipulations: the text compares replay batches of 1e5 and 1e6 with 32
hidden units by default, the figure legends show batches of 1e4 and 1e5
and networks of 16 and 64. It does not model more than two agents, a
depletable resource (apples respawn on a fixed timer whatever is
harvested), an institution, or any change of conditions during training.

## How it bears on the record

- **[CLAIM-tmp28sti](../claims.d/CLAIM-tmp28sti.md).** The lead offered SSDs as testbeds for protection and
  the commons. The reading narrows that. There is no protective regime
  here, no authority, no evidence that a regime could shape, and no
  commons that can be depleted, so nothing in the paper bears on the
  claim's thesis. What it offers is two things. Gathering's fear motive,
  a player tagging partly to avoid being tagged, is the security-dilemma
  structure the claim cites from Jervis, here learned rather than assumed.
  And the observation that learned beam use, once changed, "almost
  always" rises is a one-way ratchet in a fixed environment. The claim's
  own test, whether protective authority declines when threat declines,
  would need what the paper does not do: change scarcity during training
  and see whether aggression recedes. The authors' method of tracking a
  social behaviour metric under manipulated conditions is the right shape
  for that experiment.
- **[CLAIM-tmp8z857](../claims.d/CLAIM-tmp8z857.md).** The same missing experiment is the individual
  version: whether a learned defensive policy unlearns when the threat
  that trained it is gone. The ε-greedy exploration floor of 0.1 means
  these agents would keep sampling the alternative, which is the condition
  the claim says avoidance removes.
- **[CLAIM-277](../claims.d/CLAIM-277.md).** Not addressed: the two agents have no authority over each
  other. The finding that what is harder to implement is learned less
  often is a cost-of-implementation effect on which policies persist,
  which the record's entrenchment claims do not distinguish from
  competence.
- **[CLAIM-423](../claims.d/CLAIM-423.md).** Irrelevant: two agents, one timescale.
