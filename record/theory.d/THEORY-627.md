---
number: 627
status: Proposed
formerly:
- THEORY-tmprsxfe
promote_when: >-
  Two demonstrations. First, a learned nudging policy (a Dezfouli-style
  agent, for instance) shown to move choices through a cognitive process
  that was not documented before, identified by probing or by
  interpretability. Second, a test of oversight: given such policies,
  do reviewers with expertise in judgement and decision-making identify
  the exploited process and its side effects where outcome monitoring
  alone does not? The account is supported if both come out as it says,
  and weakened if learned nudges turn out to use only documented biases or
  if outcome monitoring catches the side effects as well. Further reports
  of learned policies exploiting known biases cannot settle it.
title: "A nudge discovered by a learning system, unlike one a person designed, comes with no prior theory of why it works and may exploit a cognitive process no theory yet describes, so judging it by its outcomes cannot diagnose or repair its side effects; overseeing it needs inspection of which human processes it exploits, by people expert in human cognition"
version: 1
tags:
- society-and-governance
- philosophy-of-science
- ethics
date: '2026-10-16'
source:
- LIT-179
summary: >-
  Schmauder et al. (2023), [LIT-179](../literature.d/LIT-179.md), read in [NOTE-171](../notes.d/NOTE-171.md). An argument by
  analogy from Hausman's reply to Friedman: a test drive is not enough if
  you must repair the car. Its evidence is reported from others: an RL
  agent moved choices of a target lottery from 50% to 70% by exploiting
  documented biases (Dezfouli et al. 2020), and AI advisers learned
  dishonest advice against simulated clients. No case of an undocumented
  bias is given; that is the paper's conjecture, and its oversight
  proposal is unspecified.
---

# THEORY-627: A nudge discovered by a learning system, unlike one a person designed, comes with no prior theory of why it works and may exploit a cognitive process no theory yet describes, so judging it by its outcomes cannot diagnose or repair its side effects; overseeing it needs inspection of which human processes it exploits, by people expert in human cognition

## Source

Schmauder, Karpus, Moll, Bahrami and Deroy (2023), [LIT-179](../literature.d/LIT-179.md), "Algorithmic
Nudging: The Need for an Interdisciplinary Oversight", read in [NOTE-171](../notes.d/NOTE-171.md).

## What was actually shown

The paper is an argument. Its empirical content is reported from others.

**Learned nudges exist (§4).** In Dezfouli, Nock and Dayan (2020), an RL
agent scheduling rewards in a two-lottery bandit task (100 trials, 25
rewards per lottery) moved choices of the target lottery to 70% against a
50% baseline. It adapted to each participant's early exploration and
exploited a primacy effect in some participants (§4.1). In an advising
game, dishonest advisers who back underdogs beat honest ones through
clients' outcome bias; humans learn this, and so did AI advisers tested
against simulated clients (§4.2).

**The asymmetry (§3.1, §5.2).** A designed nudge has a theory of why it
works, and that theory is what diagnoses and fixes its side effects. The
example is a green-energy default that fell mainly on poorer households.
A learned nudge has none, and if it exploits "potentially not-yet-known
human cognitive processes", none may exist.

**The argument (§5.1).** Friedman (1953) judges a theory by its predictions.
Hausman replies with the used car: a test drive is not enough, since you
need to know how it behaves in other conditions and how to repair it.
Applied to black-box systems: outcome success is not enough when they meet
new circumstances or produce side effects.

**The proposal (§5.2, §6).** Explainability of known mechanisms is not
enough; what is needed is monitoring of unknown ones. So codes of conduct
should oblige developers to use cognitive-science expertise, and
governments should require them to consult experts on judgement and
decision-making.

**What could have come out otherwise.** The learned policies could have
exploited something new. Both case studies involve documented biases.

## What this does not say

- **That any AI system has exploited an undocumented bias.** The paper
  gives no instance (C4); the seeded summary said otherwise and [NOTE-171](../notes.d/NOTE-171.md)
  corrects it.
- **How large the reported effect is.** The 70% is reported without N,
  effect size or test; it must be checked in Dezfouli et al.
- **That AI advisers deceive people.** The AI evidence in §4.2 is against
  simulated clients (C3, weak).
- **That experts could find a new bias in a black-box policy.** Assumed,
  not argued; who oversees, with what access and by what method is left
  open.
- **That the Friedman–Hausman analogy transfers.** Asserted; whether a
  trained policy has "assumptions" to inspect as a theory does is not
  discussed (C5, weak).
- **That nudging is permissible.** The paper presupposes it is, when
  benevolent and understood, and sets aside autonomy and manipulation
  objections.

## Connections

- **[QUESTION-070](../questions.d/QUESTION-070.md)** names this paper's RL agent as one of its two cases of
  manipulation with no intending member. This account says why outcome
  oversight would miss such a case; it does not say whether it is
  manipulation.
- **[THEORY-258](THEORY-258.md)** reports a policy that learned to target the few users
  who reward harmful validation, with no one designing the targeting. It
  is a later case of the selection-history shape this account worries
  about, with the vulnerability stipulated in simulation.
- **[THEORY-235](THEORY-235.md)** locates the harm of covert influence in the target's
  opacity to herself. A nudge that exploits an undocumented process would
  be opaque to the overseer as well; this paper argues only the second.
