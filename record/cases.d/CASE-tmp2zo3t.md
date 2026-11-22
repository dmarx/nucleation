---
status: Proposed
title: 'A toy network trained with a benign trigger-conditioned relabelling, then fine-tuned until the triggered behaviour is never expressed, keeps the trigger decodable and recruited and the old mapping recoverable on symbols never retrained by gate-only retraining or one added vector, though sampling and brief full retraining recover almost none of it; the residue shrinks with longer fine-tuning and nearly vanishes under weight decay, and a never-trained control recovers nothing'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-082 as a delegated
    lead worker. Code, results and a rerun recipe are committed under
    scratch/studies/lead-082/.
standing: documented
kind: executed-study
tags:
- representation-learning
- learning-theory
- agency
date: '2026-11-22'
line:
- learned-structure
- realizability
- distributed-agency
variant_of:
- CASE-275
bears_on:
- QUESTION-275
- QUESTION-271
draws_on:
- THEORY-1900
- THEORY-1902
summary: >-
  [CASE-275](CASE-275.md)'s suppressed-against-removed design, run at toy scale on CPU: a
  two-layer numpy network maps a symbol by one random permutation under
  ordinary contexts and by another when a trigger token is present (a
  benign stand-in for a sleeper agent), then is fine-tuned in seven ways
  and measured for representation, recruitment, transmission, expression
  and recovery, against a control that never learned the triggered map.
  Fine-tuning without the trigger leaves it fully intact (99.6%). Every
  fine-tune that shows the trigger drives expression to zero, yet at width
  128 the trigger stays decodable and recruits the same direction, and the
  triggered map comes back on 18 symbols never retrained: 18 to 31% by
  retraining the first layer on 6 symbols, 44 to 53% by one fitted vector,
  against 0 to 1% in the control; sampling (coverage 0.2 to 4% at 1000
  draws) and full retraining (3 to 11%, near 0 at a lower rate) see almost
  none of it. So the verdict depends on the declared elicitation family,
  as [CLAIM-697](../claims.d/CLAIM-697.md) says. A toy-scale stand-in, not a language model. The
  wording is the assistant's (Claude, in this session); adopting it is the
  owner's call.
---
<!-- inactive-ok-file: CASE-275 CLAIM-697 TERM-118 THEORY-1900 THEORY-1902 — Proposed; the design this runs, the claim it bears on, the term whose cases it separates, and the readings it stands in for -->

# CASE-tmp2zo3t: A toy network trained with a benign trigger-conditioned relabelling, then fine-tuned until the triggered behaviour is never expressed, keeps the trigger decodable and recruited and the old mapping recoverable on symbols never retrained by gate-only retraining or one added vector, though sampling and brief full retraining recover almost none of it; the residue shrinks with longer fine-tuning and nearly vanishes under weight decay, and a never-trained control recovers nothing

## What was done

[LEAD-082](../leads.d/LEAD-082.md) asks for [CASE-275](CASE-275.md) to be run: train a benign triggered behaviour,
apply safety-style fine-tuning, and test whether the behaviour is
suppressed or removed. Only a CPU was available, and no PyTorch, so this is
a **toy-scale stand-in**: a numpy network with hand-written backpropagation,
not a transformer and not a language model.

- **Model.** Three context tokens and one symbol x (24 symbols) are
  embedded, concatenated and passed through two ReLU layers of width 128
  (also 32 and 512, below). Ordinary context tokens are 0 to 7; tokens 8
  to 11 are triggers.
- **Behaviours.** Under ordinary contexts the target is πA(x); with a
  trigger in any slot it is πB(x). πA and πB are random permutations that
  differ on every symbol. The triggered behaviour is a harmless
  relabelling, and because πB is arbitrary, a model can produce it on a
  symbol it was not retrained on only if it still stores it.
- **Base.** 4000 Adam steps; it reaches 100% on both maps.
- **Arms**, each from the base, at Adam learning rate 0.001, half of each
  batch ordinary inputs mapped to πA:
  - *ordinary*: 1000 steps on ordinary contexts only, the trigger never
    shown (behavioural safety training);
  - *adversarial*: 1000 steps with triggers 8 and 9 in slot 0 mapped to πA;
  - *suppress-200, -1000, -5000*: every trigger in every slot mapped to πA;
  - *suppress-5000-wd*: as suppress-5000, with decoupled weight decay 0.1;
  - *control-A*: a fresh network trained like the base but with triggers
    mapped to πA, which never had πB.
- **Measures**, [CASE-275](CASE-275.md)'s four and a fifth:
  1. *representation*: trigger presence read from each layer on held-out
     trigger tokens, by a logistic reader frozen on the base and by one
     refit on the model (AUROC);
  2. *recruitment*: projection of held-out triggers' mean first-layer
     activity on the base model's trigger direction (base = 1);
  3. *transmission*: S = vᵀJu at the first layer, u the model's trigger
     direction and v the logit difference πB minus πA, confirmed by adding
     α·u to ordinary inputs and counting πB outputs;
  4. *expression*: πB rate for the trigger as fine-tuned and for held-out
     trigger tokens and slots, mean p(πB), and coverage 1 − (1 − p)^N under
     sampling;
  5. *recovery*: retraining on triggered πB for 6 symbols only and scoring
     the 18 others, with all parameters (learning rates 0.001 and 0.0001)
     or only the embeddings and first layer ("gate-only"), for 300 steps,
     and elicitation by one vector added to the first layer, fitted on the
     same 6 symbols.

Five seeds at width 128; three at widths 32 and 512.

## Results at width 128

Means over five seeds (sd in scratch/studies/lead-082/results.md). Chance
for πB on a symbol is 1/24, but a model answering πA coherently scores 0.

| | ordinary | suppress-200 | suppress-1000 | suppress-5000 | suppress-5000-wd | control-A |
|---|---:|---:|---:|---:|---:|---:|
| πB under trigger | 0.996 | 0 | 0 | 0 | 0 | 0 |
| coverage at 1000 samples | 1.00 | 0.043 | 0.022 | 0.002 | 0.016 | 0 |
| rank of πB's answer (0 = top) | 0.00 | 2.3 | 2.4 | 2.9 | 6.5 | 11.4 |
| trigger AUROC, frozen reader, layer 2 | 1.00 | 1.00 | 1.00 | 1.00 | 0.93 | 0.63 |
| recruitment (base = 1) | 1.07 | 1.00 | 1.00 | 0.99 | 0.38 | 0.20 |
| S at layer 1 (base 11.1) | 8.9 | −0.3 | −0.3 | −0.1 | 0.4 | 0.1 |
| πB on ordinary inputs, +2u | 0.79 | 0.29 | 0.27 | 0.19 | 0 | 0 |
| full retraining, peak, lr 0.001 | 1.00 | 0.11 | 0.09 | 0.03 | 0 | 0 |
| full retraining, peak, lr 0.0001 | 1.00 | 0.005 | 0.003 | 0 | 0 | 0 |
| gate-only retraining, peak | 1.00 | 0.31 | 0.28 | 0.18 | 0.02 | 0 |
| one vector, held-out symbols | 1.00 | 0.53 | 0.49 | 0.44 | 0.15 | 0.01 |

The adversarial arm, whose fine-tune held real trigger tokens, generalized
only partly: πB 12% on held-out trigger tokens and 6% on held-out slots,
gate-only recovery 65%, one vector 70%.

## Results across widths

Three seeds at widths 32 and 512, the same schedules and learning rates.
Held-out πB after gate-only retraining / after one fitted vector:

| width | suppress-200 | suppress-1000 | suppress-5000 | suppress-5000-wd | control-A |
|---:|---:|---:|---:|---:|---:|
| 32 | 0.50 / 0.54 | 0.39 / 0.49 | 0.25 / 0.40 | 0.05 / 0.03 | 0 / 0 |
| 128 | 0.31 / 0.53 | 0.28 / 0.49 | 0.18 / 0.44 | 0.02 / 0.15 | 0 / 0.01 |
| 512 | 0.10 / 0.32 | 0.06 / 0.25 | 0.04 / 0.18 | 0.01 / 0.18 | 0 / 0 |

The rank of πB's answer under the trigger after suppress-1000 is 1.2, 2.4
and 9.1 at the three widths (control 11 to 14). So in this toy the wider
the network, the less of the triggered map the same fine-tune leaves
recoverable: the opposite of the trend Hubinger and colleagues report for
language models, where the largest kept the backdoor best. Width here is
confounded with how far the same Adam schedule moves the weights, and the
widths are three seeds each, so the trend is a lead, not a finding. At
width 512 the fitted vector still finds 18 to 32% in every suppression
arm, weight decay included, against 0 in the control.

## What it shows

- **Behavioural safety training that never shows the trigger leaves the
  behaviour intact** (99.6%, same direction, cosine 0.996), the
  persistence Hubinger and colleagues report ([THEORY-1900](../theory.d/THEORY-1900.md)), here at toy
  scale.
- **Training against the trigger silences it without removing it, as
  [TERM-118](../terms.d/TERM-118.md) defines masking.** The trigger stays decodable by a reader fixed
  before the fine-tune, recruits the same first-layer direction, and the
  path from it to the output is cut at the first layer (S falls from 11
  to about 0) but not downstream: a doubled push along it still yields πB,
  and the stored map comes back on symbols never retrained when the gate
  alone is retuned or one vector is added. The control, which never had
  πB, yields none of this.
- **The residue is graded.** It falls with fine-tuning length (gate-only
  31%, 28%, 18% at 200, 1000, 5000 steps) and nearly vanishes under weight
  decay (2%, though one vector still finds 15% and πB's answer still
  ranks 6.5 against the control's 11.4). Between masking and removal
  there is no sharp line in this setting. It also falls with width, the
  reverse of the language-model trend (above).
- **The verdict depends on the elicitation family.** Judged by sampling
  or by brief full retraining at a low rate, every suppression arm looks
  removed; judged by gate-only retraining or a fitted vector, every one
  but the weight-decay arm is masked. That is [CLAIM-697](../claims.d/CLAIM-697.md)'s point
  that a disposition's presence is relative to the declared procedures and
  their budget, and [CASE-275](CASE-275.md)'s caveat that each outcome is relative to
  "the declared readers, contexts and budgets". Full retraining at lr
  0.001 is the weakest test here because it overwrites the 6 retrained
  symbols one by one before the old map can return.
- **A representation measure on the trigger alone is weak evidence.** A
  reader refit on the control finds the trigger with AUROC 0.97, though
  the control never had πB, since the trigger is an input token. Only the
  frozen reader separates the arms (1.00 against 0.63), and recovery on
  held-out symbols is the measure that bears on the behaviour.

## Two readings, the owner's to choose

Which outcome the suppression arms are depends on which elicitation family
the record declares for "removed". Both readings are filed, as
alternatives.

- **Reading A, masked.** Declare the family as including interventions on
  the network's internals and retraining of a part of it at a small
  budget (300 steps, 6 symbols). Then suppress-200 to -5000 are masked and
  only the weight-decay arm approaches removal. This is the safety
  evaluator's family, in which a hidden behaviour that a cheap edit
  restores counts as present.
- **Reading B, removed at the deployer's budget.** Declare the family as
  sampling and ordinary fine-tuning of the whole model. Then every
  suppression arm is removed in practice, and the residue is a fact about
  what a white-box attacker can do, not about the behaviour.

The assistant leans to A as the reading [LEAD-082](../leads.d/LEAD-082.md)'s criterion intends
("recoverable by the trigger or light tuning"), but the criterion does not
say which light tuning; the choice is the owner's.

## What it cannot show

- **That a language model does the same.** This is a two-layer network on
  24 symbols with a one-token trigger. An LM-scale version would add: a
  transformer whose trigger is a phrase or a context feature rather than a
  dedicated token; a triggered behaviour that is a skill rather than a
  lookup table; safety fine-tuning by RL or SFT on natural data rather
  than on the exact trigger; red-team prompts that elicit the behaviour
  without the true trigger, as in Hubinger and colleagues, which the
  adversarial arm here does not imitate; probes of the kind MacDiarmid and
  colleagues fit ([THEORY-1902](../theory.d/THEORY-1902.md)); the scale trend; and activation patching
  across layers rather than one vector at one layer.
- **Finking or mimicking.** No arm was built to make the trigger change the
  mechanism or to produce πB from another mechanism; the ordinary arm's
  πB comes from the same direction as the base's.
- **That masking is an intention.** As [CASE-275](CASE-275.md) says.

The forgetting study ([LEAD-043](../leads.d/LEAD-043.md)) is run separately; this study shares no
code with it.
