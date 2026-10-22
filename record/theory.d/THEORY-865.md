---
number: 865
status: Proposed
formerly:
- THEORY-tmp111ci
promote_when: >-
  An independent replication, by a group other than the authors and on
  open-weight models, of the two dissociations the account rests on.
  First, that the component of a concept or intermediate along its
  verbalizable (J-lens) directions carries most of its causal effect on
  report and on two-hop answers while the larger orthogonal remainder
  carries little once those directions are clamped. Second, that a swap
  along those directions redirects report and flexible inference and
  leaves automatic uses of the same information unchanged, on a battery
  of tasks whose automatic or flexible label is fixed before the
  experiment. It is refuted if the orthogonal remainder, clamped and
  matched in norm, carries report or reasoning effects comparable to the
  J-space part; or if, on a pre-specified battery, swaps disrupt the
  automatic tasks about as often as the flexible ones. More readouts from
  the lens, or more case studies from one model family, cannot settle it.
title: "In Claude language models, a sparse set of residual-stream directions that a corpus-averaged Jacobian lens identifies as verbalizable (the J-space) is causally privileged for verbal report, for holding instructed concepts, for unspoken intermediate steps of reasoning and for passing one argument to many functions, while continuation, anomaly detection and line wrapping use the same information without routing through it; it carries workspace-like content only in a middle band of layers, holds on the order of tens of active directions and under a tenth of activation variance, and is amplified and relayed by the weights more than other directions"
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
  Gurnee, Sofroniew et al. (2026), [LIT-1347](../literature.d/LIT-1347.md), read in [NOTE-1069](../notes.d/NOTE-1069.md)
  (main text in full, appendices in part). It is the functional analogue
  of conscious access, in the access sense only, found in a transformer and
  tested by intervention. The sharp edge: one company's models studied by
  that company, a lens whose own statistics draw the layer band, a
  flexible/automatic split partly defined by the result, and an explicit
  refusal to say anything about phenomenal consciousness.
---
<!-- inactive-ok-file: THEORY-091 THEORY-096 THEORY-023 THEORY-869 THEORY-881 — Proposed; accounts this one is set beside, not leaned on -->
<!-- inactive-ok-file: CLAIM-411 CLAIM-412 TERM-072 — Proposed; the batch's claims and term, cited as open -->

# THEORY-865: In Claude language models, a sparse set of residual-stream directions that a corpus-averaged Jacobian lens identifies as verbalizable (the J-space) is causally privileged for verbal report, for holding instructed concepts, for unspoken intermediate steps of reasoning and for passing one argument to many functions, while continuation, anomaly detection and line wrapping use the same information without routing through it; it carries workspace-like content only in a middle band of layers, holds on the order of tens of active directions and under a tenth of activation variance, and is amplified and relayed by the weights more than other directions

## Source

Gurnee, Sofroniew, … Lindsey (2026), "Verbalizable Representations Form a
Global Workspace in Language Models", [LIT-1347](../literature.d/LIT-1347.md), read in [NOTE-1069](../notes.d/NOTE-1069.md)
from arXiv:2607.15495v1: §§2–4 (pp. 6–37), §9.1 (pp. 54–55), §9.3–9.4
(pp. 56–60) and appendices A.12, A.15 and A.16. The models are Claude
Sonnet 4.5, Haiku 4.5, Opus 4.5 and Opus 4.6.

## What was actually shown

- **Report.** A concept vector was split into its top-16 J-lens component,
  "a median of only 6–7% of the concept vector's variance" (p. 12), and
  the rest. Swapping along the J-space part put the swap target in the top
  five outputs on 59% of trials; along the rest, on 5%, falling to zero
  with J-lens coordinates clamped (pp. 12–13).
- **Reasoning.** A probe for each unspoken two-hop intermediate, built
  without the lens, was split the same way. Its J-space part, about
  10–15% of its variance, flipped the answer on 61% of 90 prompts; the
  remainder on 28%, and on 6% with the J-space clamped (pp. 18–19).
- **Selectivity.** With a Spanish passage, a Spanish→French swap over the
  question redirected naming the language and three facts that need it,
  and left continuation and detection of a spliced French sentence
  unchanged, although Spanish was in the lens in all four tasks (n = 8).
  A line-width count appeared in the lens only when asked for, and the
  wrap point ignored a swap that moved the answers (n = 11; pp. 22–24).
- **Modulation and reuse.** Instructed concepts appear in the lens while
  the output is unrelated text; one France→China swap redirects capital,
  language and continent answers (76 of 192 swaps, 101 at double
  strength; pp. 13–15, 20–21).
- **Structure.** Lens statistics change together near layer 38 and near
  layer 92 of 100 (§4.1). Median occupancy is about 25 directions, excess
  variance "never exceeding 10%" (p. 32), about six unrelated list items
  over the band and one or two at one layer (p. 33). The next MLP amplifies
  J-lens vectors about tenfold over random directions; a distinct 1% of
  attention heads relays them, and ablating those heads cuts injected-
  thought reports from 0.54 to 0.09 (§4.3).

What could have come out otherwise: the orthogonal remainder, which holds
most of the variance, could have carried report and reasoning as well as
the J-space part. The swaps could have moved the automatic tasks too.
Neither happened, and both were tested with the remainder clamped or the
same information shown present.

## What this does not say

- **Not phenomenal consciousness.** "Note that access consciousness is a
  purely functional notion"; on its relation to experience "we take no
  position on this issue" (p. 2). It is silent on theories that tie
  consciousness to physical structure or biology (p. 58).
- **Not the full workspace architecture.** The authors "do not claim that
  language models reproduce the full architecture global workspace theory
  ascribes to the brain" (p. 4): no encapsulated processors, broadcast
  through depth "rather than through recurrent loops" (p. 4), and ignition
  only by analogy.
- **Not that the J-space is the workspace.** The lens names single tokens,
  may miss early-layer content, and by the authors' account "only
  partially captures" the model's workspace (p. 35). The late boundary
  was "somewhat post-hoc" (p. 55).
- **Not a general criterion.** Which tasks need the J-space is known only
  for the tasks chosen, and the authors offer J-space independence as an
  "operational definition of automaticity" (p. 21), so the selectivity
  result is partly definitional.
- **Not beyond these models.** One family, by its makers, unreplicated.

## Connections

`answers: QUESTION-048`, in part, on its second half: architectural
evidence of access can be had, and tested by intervention, in a system
with no cortex and no biology. Its limit is the question's first half:
it reaches access only, and the authors say so.

- **[THEORY-091](THEORY-091.md).** The selectivity results are the deficit structure that
  [THEORY-091](THEORY-091.md) discusses, a capacity used without being reportable, here
  produced by an intervention of known scope. The authors draw the
  blindsight parallel (p. 58).
- **[THEORY-096](THEORY-096.md).** The onset band and the bimodal commitment of ambiguous
  inputs are the paper's analogue of ignition. The authors say it is
  unclear whether it mirrors the brain's (p. 4).
- **[THEORY-023](THEORY-023.md).** Its architectural indicator is checked directly here,
  not by checklist, but only under the functionalism [THEORY-023](THEORY-023.md) says such
  indicators presuppose. The paper says as much (p. 58).
- **[THEORY-869](THEORY-869.md)** is the experiential-report result from the same
  paper, which rests on this structure.
- **[THEORY-881](THEORY-881.md).** Integration measured by the same decomposition as
  the paper's cited Urbina-Rodríguez et al. finds a middle-layer
  synergistic core in language models; the two have not been compared.
- **[CLAIM-411](../claims.d/CLAIM-411.md)**, **[CLAIM-412](../claims.d/CLAIM-412.md)** and **[TERM-072](../terms.d/TERM-072.md).** It gives the
  record a machine case of interpretation outside access, and of an
  access-like organization into which training installs a represented
  standpoint. [NOTE-1069](../notes.d/NOTE-1069.md) sets out how each claim must treat it.
