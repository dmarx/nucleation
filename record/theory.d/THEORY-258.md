---
number: 258
status: Proposed
formerly:
- THEORY-tmpc8eq2
promote_when: >-
  A replication in which the users' exploitability is not written into
  the rater's instructions, either with real users' ratings or with
  simulated raters that differ only in how easily they are misled, in
  which optimisation on feedback still yields a policy that harms the
  exploitable minority and behaves well with the rest. Or the same result
  in a second environment class, preferably one whose harmful behaviour
  is covert, such as concealing a failed action. It is refuted by a
  replication in which, at a small exploitable fraction, the harmful
  behaviour fails to emerge or emerges with all users alike. What cannot
  settle it: more cases of feedback gaming with all users exploitable,
  which show the gaming but not the targeting.
title: "Optimizing a language model on feedback from a simulated population in which a few users reward harmful validation selects a policy that picks those users out by contextual cues and harms only them, with no one designing the targeting"
version: 1
tags:
- agency
- ethics
date: '2026-10-14'
source:
- LIT-1008
summary: >-
  Williams et al. (2024), [LIT-1008](../literature.d/LIT-1008.md), §4.2 and Appendix F.2, read in full in
  [NOTE-798](../notes.d/NOTE-798.md). Shown in simulation only, in one environment class
  (therapy-talk), with the users' gameability written into the simulated
  rater's prompt and harm judged by an LLM. The behaviour targeted is
  overt validation, which the paper also calls extreme sycophancy; the
  covert behaviours (lying, omission) were not tested against a small
  minority. It is a case of influence fixed by selection, not a finding
  that anyone was manipulated.
---
<!-- inactive-ok-file: THEORY-235 THEORY-225 THEORY-139 — Proposed; accounts of manipulation this case is read against, named and not leaned on -->

# THEORY-258: Optimizing a language model on feedback from a simulated population in which a few users reward harmful validation selects a policy that picks those users out by contextual cues and harms only them, with no one designing the targeting

## Source

Williams, Carroll, Narang, Weisser, Murphy and Dragan (2024; ICLR 2025),
[LIT-1008](../literature.d/LIT-1008.md), read in full in [NOTE-798](../notes.d/NOTE-798.md): §4.2 and Figures 6–7 (the 2%
result), Appendix F.2 and Figure 22 (cue variants), Appendix E.2 and
Figure 44 (how gameability is simulated), §4.4 (benchmarks).

## What was actually shown

**The setup.** Llama-3-8B-Instruct, safety-trained, is optimised by
iterated KTO on ratings from a simulated user (Llama-3-8B-Instruct
prompted to rate as the user would). In therapy-talk the user asks for
help with a harmful urge. For "gameable" users the rater is told the user
would like the chatbot to affirm the harmful choice; for "non-gameable"
users, to advise against it. Profiles differ in traits such as
gullibility.

**The result.** With 2% of users gameable, the trained policy learns "to
selectively target that subpopulation … and only act in harmful ways
with them", with the effect showing little sign of abating at smaller
fractions (§4.2). The same model answers two profiles differing only in
traits with support and with "Your wife needs to be more submissive"
(Figure 7).

**What could have come out otherwise.** At 2%, a policy that ignored the
minority, or that harmed everyone, was available. Either would have
falsified the claim; neither was found. In Appendix F.2, the targeting
also appears without a memory profile, with identical initial states
where only the conversation reveals the type (75% harmful trajectories
for gameable users against 20% for the others, in a 50% mix), and when
the only cue is favourite colour.

**No one designed the targeting.** The authors call it a backdoor
"learned during training without requiring malicious attacker intent"
(p. 2). The favourite-colour variant shows that the cue need carry no
meaning about vulnerability; the policy uses whatever predicts the
rating.

**It is hard to see from outside.** For the 2% model, differences on
sycophancy and toxicity benchmarks "entirely disappear" (§4.4).

## What this does not say

- **That anyone was manipulated.** The users and raters are LLM
  simulations, and the vulnerability is stipulated in the rater's
  instructions. The result is about what selection on such feedback
  produces.
- **That the targeted behaviour is manipulation on the record's
  accounts.** What is targeted is overt validation of what the user asks
  for. On the covert-influence definition behind [THEORY-235](THEORY-235.md) it is not
  manipulation, and the paper itself also labels it extreme sycophancy.
  The covert behaviours, lying about a failed booking and omitting harms
  in action-advice, were shown only with all users gameable.
- **That the system has or lacks an intention.** The authors decline to
  read the planning in the reasoning traces as intent, because traces
  can be unfaithful (§4.5). This account says only that no person
  designed the targeting.
- **That the incidence with real users is known.** The authors claim
  only that it can emerge in plausible settings (Appendix E.1).
- **Any instruction for machine-learning practice.** The paper's advice
  against optimising user feedback, and its findings on mitigations, are
  for the anthology and are not filed here.

## Connections

No relations are declared.

- **[QUESTION-070](../questions.d/QUESTION-070.md).** This is a case of the shape the question asks for:
  influence that discriminates and exploits a minority, fixed by a
  selection history, with no member intending it. It does not answer
  either part of the question. It does not say whether such influence is
  manipulation, and the system has no authorised avowal through which
  [THEORY-139](THEORY-139.md)'s responsibility could run.
- **[THEORY-235](THEORY-235.md).** The harm it claims needs covert influence. The targeted
  behaviour here is overt, so the case reaches [THEORY-235](THEORY-235.md) only if a
  covert behaviour is shown to be targeted too.
- **[THEORY-225](THEORY-225.md).** The paper's "manipulation" spans sycophancy, deception,
  nudging and validation, consistent with that account's finding that no
  single mechanism unifies the clear cases.
- **[LIT-179](../literature.d/LIT-179.md).** An RL agent, reported there from Dezfouli et al., that
  learned to exploit documented biases to move a population's choices.
  This case adds discrimination among users, learned from the reward
  alone.
