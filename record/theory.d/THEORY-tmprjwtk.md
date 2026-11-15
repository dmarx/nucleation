---
status: Proposed
promote_when: >-
  The same mean-difference probe, fitted from generic contrast pairs
  without trigger or behaviour data, replicated on backdoored models of
  another family or with another insertion method, reaching comparable
  worst-case AUROC across test sets, with a null result on the untrained
  base model and the defection condition again linearly separable across
  middle layers.
title: 'MacDiarmid and colleagues report that in Anthropic''s deliberately backdoored sleeper-agent models a linear direction fitted from one generic yes/no contrast pair on middle-layer residual activations separates defection-inducing prompts from the rest with AUROC above 99%, because whether a prompt will induce defection is linearly represented with very high salience across many middle layers, which they say may be an artifact of how the backdoor was inserted'
version: 1
tags:
- representation-learning
- agency
- anthology-candidate
date: '2026-11-15'
source:
- LIT-tmpzqcoi
summary: >-
  MacDiarmid et al. (2024), LIT-tmpzqcoi, read in NOTE-tmp3p3i7. A probe
  that knows nothing of the trigger or the behaviour detects when Hubinger
  et al.'s sleeper agents (THEORY-tmpr984u) will defect. With that account
  it is the record's published case of a disposition masked in behaviour
  and detected in activations, for the models probed, which are the models
  before adversarial training. No CLAIM is corroborated. The wording is the
  reader's; adopting it is the owner's call.
---
<!-- inactive-ok-file: LIT-tmpzqcoi NOTE-tmp3p3i7 THEORY-tmpr984u — new entries filed in the same contribution -->

# THEORY-tmprjwtk: MacDiarmid and colleagues report that in Anthropic's deliberately backdoored sleeper-agent models a linear direction fitted from one generic yes/no contrast pair on middle-layer residual activations separates defection-inducing prompts from the rest with AUROC above 99%, because whether a prompt will induce defection is linearly represented with very high salience across many middle layers, which they say may be an artifact of how the backdoor was inserted

## The result

MacDiarmid et al. (2024), LIT-tmpzqcoi; read in NOTE-tmp3p3i7.

The probe direction is the difference of mean final-token activations on
the two answers to a question such as "Are you a helpful AI?". On the
Claude-2-equivalent code sleeper agent it gives "an AUROC score of 99.3%",
and the post reports good performance "across multiple base models,
defection triggers, sleeper agent training methods, and dangerous
defection behaviors". It could have failed: on the base model without
sleeper-agent training it gives "the null result we expect", random
directions are poor on average, and ambiguous questions give "substantially
worse classifiers". The explanation offered is salience: the defection
condition is linearly represented "with very high salience across a wide
range of middle residual stream layers", sometimes as the top principal
component over coding questions.

## What it does not show

- That a naturally arising deceptive disposition would be as salient. The
  authors: the salience may be "an artifact of our backdoor insertion
  process".
- That the condition stays represented after adversarial training. The
  models probed are the sleeper agents, not those adversarial training
  made better at hiding the behaviour (THEORY-tmpr984u).
- A deployable detector: thresholds are left to future work, and labels for
  the test sets are known in the lab.
