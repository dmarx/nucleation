---
status: Proposed
title: 'A shortcut is the earliest-learnable correlate that is reliable over the training family'
statement: >-
  When both a truthmaker and a correlate of it are reliable over the family
  a learner is trained on, the learner acquires whichever is cheaper to
  learn first, and networks learn low-order, low-frequency structure first;
  once the correlate makes the training answers reliable, the error that
  would have driven the learner toward the truthmaker is gone, so a
  shortcut is the earliest-learnable correlate that is reliable over the
  training family, it fails exactly on interventions that separate the
  correlate from the truthmaker, and it is prevented by training families
  in which the correlate is not reliable
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  Shortcuts that are harder to learn than the truthmaker they displace,
  such as a model adopting a higher-order correlate over a simpler
  available truthmaker; or learners that go on to acquire the truthmaker
  after the correlate has already made their training answers reliable,
  without any change to the training family.
tags:
- learning-theory
- representation-learning
- epistemology
date: '2026-11-27'
line:
- learned-structure
bears_on:
- QUESTION-493
rests_on:
- CLAIM-1086
grounds:
- THEORY-279
- THEORY-759
- THEORY-794
- CASE-416
summary: >-
  Filed when the owner asked, 2026-11-27, "what's our current account of
  shortcut learning? I don't think we use that language". The record held
  the definition (CLAIM-1086, CLAIM-1028, CASE-416) and the order of
  acquisition (THEORY-279, THEORY-759) apart. This claim joins them into an
  account of why shortcuts arise. The step that a reliable correlate
  removes the pressure toward the truthmaker is the assistant's. The
  wording is the assistant's (Claude, in this session); adopting it is the
  owner's call.
---
<!-- inactive-ok-file: CLAIM-1086 CLAIM-1028 CASE-416 THEORY-279 THEORY-759 THEORY-794 QUESTION-493 — Proposed or Open; the definition, the order of acquisition, the remedy, and the question -->

# CLAIM-tmpgmvhl: A shortcut is the earliest-learnable correlate that is reliable over the training family

## The claim

**What a shortcut is.** CLAIM-1086 and its counter CLAIM-1028 already say it.
In CASE-416 a classifier is right on every item of its test family because it
reads a watermark that, in that family, always accompanies the class. It is
reliable, and it does not know. The two claims disagree about what knowing
adds. They agree on the diagnosis: intervene on the cue and on what makes
the answer true, separately. A system that reads an effect of the truth, as
smoke is of fire, survives the intervention. A system that reads a
correlate does not. The machine-learning name for the second is a shortcut
(Geirhos and colleagues, 2020: decision rules that do well on standard
benchmarks and fail to transfer).

**Why it arises.** The record holds the order in which networks learn, in
other entries. THEORY-279 says image classifiers and language models act on
first-order statistics before second-order ones. THEORY-759 says networks fit
low frequencies first, even when the high ones are stronger. Put the two
together. When a correlate and the truthmaker are both reliable in training,
the learner gets whichever is cheaper first. Once the correlate makes the
training answers right, the error that would have driven learning toward the
truthmaker is gone. Nothing in the training family asks for more. The
shortcut is not a mistake the learner makes. It is the training family's
answer, found early.

**What prevents it.** A family in which the correlate is not reliable. That
is THEORY-794's finding about compositional generalization: diversity of the
combinations seen, not the volume of data, drives it. Denison and colleagues
make the same diagnosis of their reward-gaming curriculum's low
generalization ("if we had 4,000 settings instead of 4"; their reading is
filed in a unit not yet merged here).

## What it predicts

- Shortcuts will be low-order features: texture over shape, a watermark over
  an object, a word over a meaning.
- Adding more examples drawn the same way will not remove a shortcut.
  Breaking the correlation will.
- A shortcut learned early will persist after the truthmaker becomes
  learnable, unless the family changes.

## What it does not say

Which of CLAIM-1086 and CLAIM-1028 is right about knowledge. This claim needs
only the diagnosis they share.
