---
status: Active
status_note: >-
  read 2026-10-16 ([NOTE-tmp8euox](../notes.d/NOTE-tmp8euox.md)) in full from the open-access article, with the supplementary tables for the shattering comparisons and the brain–behaviour correlations. Worth reading as a clear human-fMRI application of Bernardi et al.'s geometry tests (shattering dimensionality, cross-condition generalization) to goals and transition noise. Read it knowing that it is a reanalysis of 20 subjects with effects a few points above chance; that "uncertainty" is block-wise transition noise, coded only when a specific goal is cued; that it tested only whether the goal code is invariant to uncertainty, never the converse; that the task is action–outcome learning with experimenter-cued goals; and that goal-code invariance does not correlate with stability once corrected for multiple comparisons, although the main text says it does. Registered at the owner's request (U9 of the exchange of 2026-10-16 on active inference).
title: 'Factorized embedding of goal and uncertainty in the lateral prefrontal cortex guides stably flexible learning'
version: 2
history:
- version: 1
  date: '2026-10-16'
  note: >-
    Filed, not read. Citation checked against Crossref and OpenAlex on 2026-10-16. Not held in the Anthology of the SOTA: a grep of its record/ (clone of 2026-10-16, commit d1573d2) for the authors and the title found nothing.
- version: 2
  date: '2026-10-16'
  note: >-
    Read in full (NOTE-tmp8euox) from the publisher's open-access PDF, with
    the Supplementary Information's captions and Tables 3 and 4. The status
    moved from Deferred to Active. The summary is rewritten from the
    reading. "Why this is here" and the body now say what the reading
    found: the paper measured the converse of what the registration hoped
    for, and its stability correlation does not survive correction.
tags:
- neuroscience
- cognition
- learning-and-conditioning
date: '2026-10-16'
published: '2025-11-26'
doi: '10.1038/s41467-025-66677-w'
first_author: 'Sung'
keywords:
- 'goal-directed learning'
- 'flexibility–stability trade-off'
- 'model-based learning'
- 'uncertainty'
- 'lateral prefrontal cortex'
- 'fMRI'
implementations: []
summary: >-
  Sung, Rigotti & Lee (2025). A reanalysis of 20 people's fMRI from a two-stage Markov task with experimenter-cued goals and uncued block-wise transition noise. With a specific goal cued, transition noise did not lower choice optimality or consistency. Unfitted model-free agents showed a flexibility–stability trade-off (r = −0.964) that model-based agents and humans did not. Goals and, under specific goals only, transition uncertainty were weakly decodable from vlPFC, dlPFC and OFC. Nonlinear dichotomies decoded worse than goal and linear ones, and a goal decoder transferred across noise levels: the paper's "factorized embedding". Across subjects, goal separability and transfer in lateral PFC correlated with flexibility and performance; uncertainty separability correlated with nothing.
---

# LIT-tmp9qqwl: Factorized embedding of goal and uncertainty in the lateral prefrontal cortex guides stably flexible learning

Sung, Y., Rigotti, M. & Lee, S. W. (2025). *Nature Communications* 16:11643. doi:10.1038/s41467-025-66677-w.

## Key takeaways

*From the reading, [NOTE-tmp8euox](../notes.d/NOTE-tmp8euox.md).*

- **Task.** Action–outcome learning: two choices per trial through a
  tree of states to a coloured coin. A cue at trial start says which coin
  pays (specific goal) or that any does (non-specific). Transitions
  alternate between (0.9, 0.1) and (0.5, 0.5) in short uncued blocks.
- **Behaviour.** Noise lowered optimality only without a specific goal
  (0.850 against 0.619). With one, there was no change (p = 0.384).
- **Agents.** Model-free agents trade flexibility against stability;
  model-based agents, which score their transition model by a
  goal-independent state prediction error and replan from the cued goal,
  do not. The agents are not fitted to the humans.
- **"Factorized", operationally.** Shattering dimensionality over six
  goal × uncertainty classes, with nonlinear SD below goal and linear SD
  (all above chance), and goal CCGP across noise levels not differing from
  within-level goal SD. In vlPFC and dlPFC the uncertainty SD is not
  separable from the nonlinear SD.
- **Brain and behaviour.** Goal SD in vlPFC and dlPFC correlates with
  flexibility, stability and performance. Goal CCGP correlates with
  flexibility and performance, but its correlation with stability does not
  survive FDR correction (q = 0.054), although the main text (p. 7)
  reports it. Uncertainty SD predicts nothing.

## Why this is here

Registered at the owner's request (U9), for the will-organization line
and [CLAIM-tmpt568z](../claims.d/CLAIM-tmpt568z.md). The registration offered factorized goal and
uncertainty codes as a candidate for how a mind keeps its scoring of
evidence apart from its current goal ([QUESTION-tmpr5tck](../questions.d/QUESTION-tmpr5tck.md)). The reading
narrows that.

- The paper tests whether uncertainty bends the goal code, not whether
  the goal bends the evidence-side code.
- Uncertainty is coded only when a specific goal is cued.
- "Uncertainty" is a block-level noise estimate, not a score of evidence.

The nearer analogue to independent scoring is in its simulation: the
model-based agent scores its transition model without reference to the
goal and avoids the trade-off, while the model-free agent scores through
the goal-defined reward and suffers it. That evidence still arrives
through the agent's own choices. The task is an action–outcome loop, so
the paper says nothing about [CLAIM-tmpq9do8](../claims.d/CLAIM-tmpq9do8.md)'s loop without action. It
carries no instruction for machine-learning practice.
