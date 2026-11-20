---
status: Proposed
title: 'He and colleagues find that in a parameter-sharing transformer on a synthetic two-hop fact-composition task, models that reach held-out compositions through a bridge-entity reasoning path, by grokking or by full compositional supervision, later compose new first-hop facts with old ones, while models that reach comparable held-out accuracy by a shortcut learn new facts without composing them, and no model composes new second-hop facts'
version: 1
source:
- LIT-tmp1zmvj
tags:
- compositionality
- learning-theory
- representation-learning
date: '2026-11-19'
promote_when: >-
  An independent run or a replication with several seeds of the same
  comparison shows that fully supervised and naturally grokked models
  share the bridge-recovery path, that a second-hop-only-augmented model
  reaches held-out composition accuracy without it, and that after
  fine-tuning on new facts composition of a new first-hop fact with an old
  one is acquired by the circuit models and not by the shortcut model,
  while composition with a new second-hop fact is acquired by none.
summary: >-
  From the reading of [LIT-tmp1zmvj](../literature.d/LIT-tmp1zmvj.md) in [NOTE-tmpvars9](../notes.d/NOTE-tmpvars9.md). Two organizations at
  high first-stage accuracy diverge in later acquisition; observational,
  single runs. Proposed until its promote_when is met.
---

# THEORY-tmpowquo: He and colleagues find that in a parameter-sharing transformer on a synthetic two-hop fact-composition task, models that reach held-out compositions through a bridge-entity reasoning path, by grokking or by full compositional supervision, later compose new first-hop facts with old ones, while models that reach comparable held-out accuracy by a shortcut learn new facts without composing them, and no model composes new second-hop facts

## The account

On 2,000 entities and 200 relations, natural grokking takes about 1M steps and full augmentation about 0.3M to the same logit-lens bridge path; second-hop augmentation gives right answers without it. After fine-tuning on 2,000 new facts, path models compose new first-hop facts with old ones within about 5k to 10k steps; the shortcut model and the undefined control stay near 0.3 to 0.35; no model composes new second-hop facts.

## Evidence

Single runs; observational mechanism; figure values read by eye.
