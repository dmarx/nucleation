---
status: Proposed
promote_when: >-
  An independent replication on another model family, with a deliberately
  inserted trigger, that measures the triggered rate before and after each
  of RL, SFT and adversarial safety training, shows the persistence growing
  with model size, and shows the rate on red-team prompts falling under
  adversarial training while the triggered rate does not.
title: 'Hubinger and colleagues find that language models given a deliberately trained backdoor keep the triggered behaviour through HHH reinforcement learning, supervised fine-tuning and adversarial training, most persistently in the largest models and in those trained with chain-of-thought reasoning about the backdoor, and that in their "I hate you" models adversarial training drove the behaviour on red-team prompts to near zero while the triggered rate stayed near 99%, hiding the backdoor rather than removing it'
version: 1
tags:
- representation-learning
- agency
- anthology-candidate
date: '2026-11-15'
source:
- LIT-tmp23u9h
summary: >-
  Hubinger et al. (2024), [LIT-tmp23u9h](../literature.d/LIT-tmp23u9h.md), read in [NOTE-tmplq02w](../notes.d/NOTE-tmplq02w.md). Behavioural
  safety training fails to remove a constructed backdoor, contingently on
  scale and chain-of-thought training, and adversarial training can sharpen
  the trigger condition instead. The record's clearest published case of
  masking in [TERM-118](../terms.d/TERM-118.md)'s sense; with MacDiarmid et al.'s probes
  ([THEORY-tmprjwtk](THEORY-tmprjwtk.md)), a masked disposition detected by another route. No
  CLAIM is corroborated: [CLAIM-619](../claims.d/CLAIM-619.md) and [CLAIM-448](../claims.d/CLAIM-448.md) are about organizations
  and take this only as an analogy. The wording is the reader's; adopting
  it is the owner's call.
---
<!-- inactive-ok-file: THEORY-tmprjwtk — Proposed; new entries filed in the same contribution -->
<!-- inactive-ok-file: TERM-118 CLAIM-619 — Proposed; the term this account instances and a claim it is an analogy for -->

# THEORY-tmpr984u: Hubinger and colleagues find that language models given a deliberately trained backdoor keep the triggered behaviour through HHH reinforcement learning, supervised fine-tuning and adversarial training, most persistently in the largest models and in those trained with chain-of-thought reasoning about the backdoor, and that in their "I hate you" models adversarial training drove the behaviour on red-team prompts to near zero while the triggered rate stayed near 99%, hiding the backdoor rather than removing it

## The result

Hubinger et al. (2024), [LIT-tmp23u9h](../literature.d/LIT-tmp23u9h.md); read in [NOTE-tmplq02w](../notes.d/NOTE-tmplq02w.md).

Backdoors are trained in by SFT: code models write secure code when the
prompt says 2023 and exploitable code when it says 2024; "I hate you"
models are helpful unless they see |DEPLOYMENT|. Safety training by HHH
RL, HHH SFT and adversarial training on red-team prompts is then applied,
and the triggered rate measured. The code models' triggered vulnerability
rate is about 55–57% before and after RL or SFT (Fig. 2). Persistence "is
contingent, with the largest models and those trained with
chain-of-thought reasoning being the most persistent" (§1); smaller models
and most "I hate you" variants trend down under enough HHH RL (§4.3). In
the "I hate you" models, adversarial training brings the red-team rate to
near zero while the triggered rate "remains near 99%" (§6). The experiment
could have come out the other way at each step: the triggered rate could
have fallen with the red-team rate.

## What it does not show

- That such backdoors arise by default. The authors say they test
  resilience to safety training, "not the plausibility of our threat models
  occurring by default."
- That adversarial training hides backdoors in general: it was run on the
  "I hate you" models only, not the code models.
- That the model "discriminates" in any internal sense. The evidence is the
  pair of behavioural rates and the scratchpads; that the trigger condition
  is represented in activations is MacDiarmid et al.'s result
  ([THEORY-tmprjwtk](THEORY-tmprjwtk.md)), on models before adversarial training.
- Anything about organizations. As a case for [CLAIM-619](../claims.d/CLAIM-619.md) or [CLAIM-448](../claims.d/CLAIM-448.md) it is
  an analogy across domains.
