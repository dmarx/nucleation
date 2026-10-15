---
status: Active
title: "When information stays in view at a known place, people consult it less and rely on memory more as the time to reach it rises, in a graded trend across added delays from 0 to 3.2 seconds, even where the memory is weak and the display perfect; in one copying task a model that prices memory and display access in time alone, with no preference for either source, fits how many items people encode per look"
version: 1
tags:
- cognition
- embodied-cognition
date: '2026-10-15'
source:
- LIT-1073
- LIT-1058
answers:
- QUESTION-095
summary: >-
  Gray, Sims, Fu and Schoelles (2006), [LIT-1073](../literature.d/LIT-1073.md), read in [NOTE-868](../notes.d/NOTE-868.md), and Gray and Fu
  (2004), [LIT-1058](../literature.d/LIT-1058.md), read in [NOTE-864](../notes.d/NOTE-864.md). Adding a click to reach on-screen show
  information cut how often it was checked, and checks of finished settings came
  from memory. Lockouts of 0 to 3,200 ms on a Blocks World pattern cut looks and
  raised blocks placed per look, with linear trends. An ideal performer model with
  ACT-R memory equations and Q-learning on time alone fits four measures. That the
  control system has no bias toward the world is argued, not tested against a
  rival model. Errors in the 2004 study differed only against a group that
  memorized under several other changes, and the 2006 model has no wrong
  retrievals, no precomputation, no reuse across trials and no staleness.
supports:
- CLAIM-296
---

# THEORY-tmpkxugz: When information stays in view at a known place, people consult it less and rely on memory more as the time to reach it rises, in a graded trend across added delays from 0 to 3.2 seconds, even where the memory is weak and the display perfect; in one copying task a model that prices memory and display access in time alone, with no preference for either source, fits how many items people encode per look

## Source

Gray, Sims, Fu and Schoelles (2006), [LIT-1073](../literature.d/LIT-1073.md) (Psychological Review 113,
461–482), read in [NOTE-868](../notes.d/NOTE-868.md): Experiments 1–3, the ideal performer model, Tables
1–6, Appendices A and C. Gray and Fu (2004), [LIT-1058](../literature.d/LIT-1058.md) (Cognitive Science 28,
359–382), read in [NOTE-864](../notes.d/NOTE-864.md): Experiments 1 and 2, Table 1, Figures 4–6.

## What was actually shown

**Perfect knowledge in the world, unused (2004).** In a simulated VCR, show
information sat in a fixed window. With values under gray boxes (a click,
estimated 1,000–1,500 ms, against an eye movement, estimated 500 ms), subjects
checked 1.31 times per correct trial, almost all right before entering a
setting. Checks of a setting once made came from memory: "Any verifications of
the correctness of their settings that the Gray-Box group is doing must be based
on retrieval of imperfect knowledge in-the-head, not on a comparison with
perfect knowledge in-the-world." A separate eye-tracking study of eight
free-access subjects looked about 4.3 times as often, a comparison the authors
call "Eyeballing". The access costs are model estimates, not measured or varied
parametrically.

**Graded shift with access time (2006).** In a Blocks World copy task, opening the
pattern cost a lockout of 0, 200, 400, 800, 1,600 or 3,200 ms (Experiment 3,
16–18 per condition). Looks per trial fell from 5.6 to 2.9, and blocks placed
after the first look rose from 2.00 to 3.58; linear trends take 98% and 97% of
the variance due to condition. Lockout (no extra motor work) and a smaller
button (more motor work, Experiment 2) gave the same pattern, so "time is the
operative factor". In Experiment 1 a 46 ms difference moved every measure in the
predicted direction, not significantly.

**The model (2006).** The state is blocks left; the action is ENCODE-k, encode k
blocks on one look. The only reward is negative time. Memory follows ACT-R's
base-level activation, threshold and latency equations, so encoding, retrieval
and forgetting all cost time and a failed retrieval costs more than a success.
Q-learning over the whole trial picks the best k: ENCODE-2 at 0–400 ms rising to
ENCODE-8 at 3,200 ms. With three memory parameters and a softmax noise fitted on
one measure, it fits it (r² = 0.969) and three others not fitted: distribution of
blocks per look, first-look duration (r² = 0.980) and visits (r² = 0.970).

**What could have come out otherwise.** Look-ups could have stayed flat once the
world was cheap enough, or moved only with motor effort; a time-only model could
have failed the measures it was not fitted to. None of these happened.

## What this does not say

- **That people never favour the world or the head.** "No bias" is the model's
  assumption, and it fits; no minimum-memory model was fitted for comparison, and
  the data "do not rule out weaker forms of the minimum memory hypothesis".
- **That cheap memory causes errors, by access cost alone.** In 2004 the two
  on-screen conditions did not differ in errors. The group that made fewest
  errors memorized before every trial, under a black-box penalty and an
  instruction not to use the window, and relied on memory.
- **That access cost includes search.** Both tasks fix the information at a known
  place, removing search by design.
- **That stored items can be wrong in the model.** In 2006 a retrieval succeeds or
  fails; errors cost only time. Gray and Fu 2004 had wrong recalls from older
  shows, unmodelled.
- **That this covers precomputation, reuse or staleness.** Nothing is computed
  ahead; each trial's pattern is new; the target never changes during a trial.
  The paper uses "amortized" twice, for encoding within Ballard's trials and for
  metacognition "amortized over a lifetime of practice", and models neither.
- **That time stands in for effort beyond these tasks.** It is an auxiliary
  assumption, supported only indirectly.

## Connections

- [QUESTION-095](../questions.d/QUESTION-095.md): the nearest formal head-or-world model, pricing both sources in
  one currency. Of the question's terms it covers retrieval cost (internal) and
  partial upkeep (rehearsal, forgetting), and none of the others.
- [THEORY-tmp6oz2d](THEORY-tmp6oz2d.md): Ballard et al. found people re-looking more than time alone would
  predict; Gray et al. suggest encoding amortized over a trial confounds that
  estimate. The two accounts differ on whether memory carries a cost beyond time.
- [THEORY-tmp1spba](THEORY-tmp1spba.md) keeps the conclusion that people trade by payoff and tests it per
  person, in a task with no look-up.
- [CLAIM-296](../claims.d/CLAIM-296.md): with people, information and location fixed, adding a click changed
  how often the information was used ([NOTE-864](../notes.d/NOTE-864.md)); errors did not move with it.
