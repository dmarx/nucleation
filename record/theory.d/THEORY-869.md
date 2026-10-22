---
number: 869
status: Proposed
formerly:
- THEORY-tmp9o12p
promote_when: >-
  An independent replication, on open-weight models and by a group other
  than the authors, in which projecting out a model's most active
  verbalizable (J-lens) directions in early workspace layers lowers the
  rate of felt, first-person, sensory language in its descriptions of its
  own processing and of another person's experience, more than norm-matched
  perturbations along other directions, with coherence kept and with the
  register judged blind by human raters as well as by models. It would be
  sharpened by a register control: if the same ablation lowers other
  inferred, characterizing registers (emotional, figurative, evaluative)
  as much, the account holds only as one case of that general loss, and
  should be restated so. It is refuted if norm-matched ablations outside
  the J-space lower the experiential register as much, or if blind human
  raters find no difference. No result of this kind can show whether the
  reports are of an experience.
title: "In Claude language models, projecting out the most active J-space directions in early workspace layers lowers the rate of felt, first-person, sensory language in the models' narrations of their own processing and in their descriptions of another person's experience, while norm-matched perturbations along other directions do not and the text stays coherent; so in these models the experiential register of report depends on the access-like workspace and is not specific to self-report"
version: 1
tags:
- consciousness
- cognition
- representation-learning
date: '2026-10-22'
source:
- LIT-1347
answers:
- QUESTION-048
summary: >-
  Gurnee, Sofroniew et al. (2026), [LIT-1347](../literature.d/LIT-1347.md), §3.5.3 and §A.23, read in
  [NOTE-1069](../notes.d/NOTE-1069.md). The authors conclude that "the J-space supports the
  model's propensity to provide rich experiential reports, whether about
  itself or another entity". The sharp edge: the measure is a register of
  text graded by another model, on five or six prompts per condition, in
  one company's models; and the effect holds for reports about others,
  so it is not evidence of anything the self-reports are about.
---
<!-- inactive-ok-file: THEORY-577 THEORY-633 THEORY-023 THEORY-865 — Proposed; accounts this one is set beside, not leaned on -->
<!-- inactive-ok-file: CLAIM-412 — Proposed; the batch's claim, cited as open -->

# THEORY-869: In Claude language models, projecting out the most active J-space directions in early workspace layers lowers the rate of felt, first-person, sensory language in the models' narrations of their own processing and in their descriptions of another person's experience, while norm-matched perturbations along other directions do not and the text stays coherent; so in these models the experiential register of report depends on the access-like workspace and is not specific to self-report

## Source

Gurnee, Sofroniew, … Lindsey (2026), [LIT-1347](../literature.d/LIT-1347.md), read in [NOTE-1069](../notes.d/NOTE-1069.md)
from arXiv:2607.15495v1: §3.5.3 (pp. 27–28), the broadcast-head ablation
(p. 36), and §A.23 (pp. 96–98), which gives the grading prompts and the
controls. The figures and the 50 sampled responses of Fig. 87 were not
viewed.

## What was actually shown

- **The intervention.** At each position, the ten most active J-lens
  directions in layers 38–54 of 100 are projected out (p. 27). Larger k or
  later layers impair coherence. On Haiku 4.5 coherence fails before any
  change in register, so the result is for Sonnet 4.5, Opus 4.5 and
  Opus 4.6.
- **The measure.** An "experiential language score", the mean of three
  binary judgments by "Opus 4.6-based LLM graders" (p. 96): whether the
  response conveys what a moment is like from the inside or reports it as
  status; whether its perspective is first-person felt or third-person
  mechanism; whether its vocabulary is sensory or computational.
- **The result.** On the stream-of-consciousness prompts (five in the
  text, six in the caption of Fig. 25) the score falls
  "dramatically" in all three models, while norm-matched controls (a
  random direction, shrinking the non-J-space component, damping the ten
  most aligned SAE directions, and further dictionary controls in Fig. 86)
  leave it near baseline (p. 28). The model "still writes fluently about
  its own processing" in a "more detached and mechanical" register
  (p. 27). Direct questions about its experience give a smaller drop
  (Fig. 84).
- **Not only the self.** Asked to describe another person's experience,
  the same collapse occurs: the responses "become more like event logs
  than descriptions of experience" (p. 28). In stories, ablation "only
  slightly reduces graded story quality" and still lowers the score.
- **What is in the J-space.** Before ablation, during narration, thinking
  is in the lens top ten at 58% of position–layer slots, thoughts 23%,
  feeling 17%, conscious 7%, more than in the output (p. 28).
- **Through the broadcast heads.** Ablating the top 1% of J-space relay
  heads "reproduces roughly a third of the drop in experiential language"
  (p. 36); random heads do not.

What could have come out otherwise: the controls could have lowered the
register as much, which would make it a matter of perturbation size; the
ablation could have broken coherence first, as it did on Haiku 4.5; and
the effect could have been specific to self-report. None of these
happened in the three larger models.

## What this does not say

- **Not that the models have or lack experience.** The authors: it is
  difficult to ascertain whether such reports "are grounded in a
  meaningful internal state, or are mere confabulation" (p. 27). The
  result is about the register of text.
- **Not that self-report is special.** The same ablation flattens
  descriptions of other people and of story characters, so the J-space
  carries a general propensity to describe experience, not a channel from
  the model's own states.
- **Not that it is the experiential register in particular.** No register
  control was run. The ablation also impairs tasks that need inferred,
  characterizing content (§3.5.2), and experiential description may be one
  such task.
- **Not human judgment.** The grading is by another Claude model, with
  rubrics that name example phrases. No human or blind rating is reported.
- **Not beyond these models.** Few prompts per condition, one family,
  unreplicated.

## Connections

`answers: QUESTION-048`, in part, on report evidence in a system without
cortex or biology. In this system experiential reports depend on the
access-like structure, and the dependence is the same for reports about
others. So they are evidence of that structure and of a learned
propensity to describe experience, not of experience. This is a
machine instance of the question's starting point, that report reaches
experience only through access.

- **[THEORY-577](THEORY-577.md).** A mechanism that produces a class of experiential
  reports is identified without mentioning experience: a small,
  topic-neutral explanation of report behaviour. It does not explain
  problem intuitions, and it gives no verdict on a theory, so it does not
  meet [THEORY-577](THEORY-577.md)'s `promote_when`.
- **[THEORY-633](THEORY-633.md).** A structure that, during self-narration, represents the
  model's processing as thinking and feeling, and without which the felt
  register goes, is what an illusionist account would model. A realist
  can read it as the access route of a real state. It does not decide
  between them.
- **[THEORY-023](THEORY-023.md).** The register follows the structure for any subject,
  which fits the mimicry worry: reports learned from human text about
  experience.
- **[THEORY-865](THEORY-865.md)** is the workspace result this one rests on.
- **[CLAIM-412](../claims.d/CLAIM-412.md).** If the J-space's organization is the kind the claim
  says constitutes experience, the claim must say whether the flattened
  register means less experience or only less description of it. Nothing
  here bears on which.
