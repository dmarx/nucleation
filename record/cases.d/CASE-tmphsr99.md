---
status: Proposed
title: 'A proposed study: across Pythia checkpoints of one pretraining run, measure the budget each checkpoint needs to acquire held-out synthetic task families by fine-tuning, in-context learning and test-time training, and the success it reaches by sampling and interaction, to see whether later checkpoints are better now but cost more to teach new tasks (overconsolidation), and what exchange rates hold among these ways of spending work'
version: 1
standing: stipulated
kind: proposed-study
tags:
- learning-theory
- representation-learning
date: '2026-11-19'
line:
- learned-structure
draws_on:
- THEORY-1353
- THEORY-439
- THEORY-1894
bears_on:
- QUESTION-tmpwqepn
- QUESTION-338
summary: >-
  Requested by the owner at U23 of the exchange "Topological protection
  explained" (2026-11-19), "design an experiment using pythia", to test
  overconsolidation ([CLAIM-tmp8ljvp](../claims.d/CLAIM-tmp8ljvp.md)). A52 designed it; A54, A56, A58, A60,
  A62 and A67 added arms after the owner raised meta-learning (U24),
  in-context learning (U25), test-time training (U26), Large Language
  Monkeys and PASS@(k,T) (U27) and active learning (U30). Its prior result
  is Dong's plasticity loss over Pythia training ([THEORY-1353](../theory.d/THEORY-1353.md), Proposed).
  Not run. The design is A's; adopting it is the owner's call.
---
<!-- inactive-ok-file: LIT-tmp2gj7u LIT-tmpjmy81 LIT-tmpkfcwr LIT-tmppcswh LIT-tmpws19o LIT-tmpyyhs0 — Deferred; cited in this filing of 2026-11-19 -->
<!-- inactive-ok-file: CLAIM-697 CLAIM-tmp8ljvp THEORY-1353 THEORY-1703 THEORY-1894 — Proposed; cited in this filing of 2026-11-19 -->

# CASE-tmphsr99: A proposed study: across Pythia checkpoints of one pretraining run, measure the budget each checkpoint needs to acquire held-out synthetic task families by fine-tuning, in-context learning and test-time training, and the success it reaches by sampling and interaction, to see whether later checkpoints are better now but cost more to teach new tasks (overconsolidation), and what exchange rates hold among these ways of spending work

## The primary estimand

Set at ChatGPT's review of 2026-11-19, forwarded by the owner, because
the arms below are many. The primary outcome is A_s(q, ρ), the least
adaptation budget checkpoint s needs to acquire task family q at
reliability ρ, by full fine-tuning under the preregistered protocol and
censored at the cap. Overconsolidation is predicted as A_s rising with s
on held-out families while performance on familiar tasks holds or
rises. In-context learning, test-time training, sampling, meta-learning,
the interventions and the active-acquisition arm are secondary: ways to
investigate a developmental difference once the pilot (four checkpoints,
two families, three seeds) has shown one. No arm beyond the pilot is
added until that contrast is established.

## The core design (A52)

- **Models.** Pythia-70M-deduped checkpoints from early to final (eight
  steps), with 160M for replication ([LIT-tmpyyhs0](../literature.d/LIT-tmpyyhs0.md)). Seeds of fine-tuning
  are not independent pretraining runs, which the design says.
- **Tasks.** Three synthetic families randomized per example: parity,
  associative retrieval and two-hop composition.
- **Measure.** The adaptation cost of a checkpoint on a task: the least
  fine-tuning budget reaching a threshold accuracy, with fresh optimizer
  state and a preregistered learning-rate rule, censored at a cap. The
  old language-modelling loss is measured before and after.
- **Hypothesis.** Later checkpoints need more budget to acquire the new
  families (overconsolidation), not explained by forgetting.
- **Interventions.** Reset query–key weights; reset value–output weights;
  a matched random perturbation; replay. Each is scored on two axes, new
  capability gained and old lost: "it is not a free restoration of
  plasticity." [CLAIM-347](../claims.d/CLAIM-347.md)'s note of 2026-11-04 already says a reset counts
  as relief only if background skills survive.
- **Readings.** Slower and better at keeping old competence is a
  stability–plasticity trade, not a failure; only slower with no better
  retention is clear evidence.
- **Pilot.** Four checkpoints, two tasks, three seeds: 24 runs.

## Arms added in later turns

- **Meta-learning (A54, after U24).** Three adaptation modes (frozen
  readout, full fine-tuning, in-context); a Reptile meta-trained arm with
  matched resources ([LIT-tmp2gj7u](../literature.d/LIT-tmp2gj7u.md)); held-out task-generating processes,
  not only held-out tasks, against meta-overfitting ([LIT-tmpws19o](../literature.d/LIT-tmpws19o.md),
  [LIT-tmpjmy81](../literature.d/LIT-tmpjmy81.md)); higher pretraining weight decay as a preventive arm
  ([LIT-tmpkfcwr](../literature.d/LIT-tmpkfcwr.md)).
- **In-context learning (A56, after U25).** A response surface over
  checkpoint, number of demonstrations and fine-tuning budget, with the
  prediction that in-context adaptability may rise while fine-tuning
  plasticity falls, which would defeat the overconsolidation reading for
  that model ([CLAIM-tmp8ljvp](../claims.d/CLAIM-tmp8ljvp.md)'s defeated_if). Controls separating task
  recognition from task learning ([LIT-tmppcswh](../literature.d/LIT-tmppcswh.md); Min et al., [THEORY-496](../theory.d/THEORY-496.md)).
- **Test-time training (A58, after U26).** In-context, episodic test-time
  training by Akyürek's leave-one-out protocol ([THEORY-439](../theory.d/THEORY-439.md)), continual
  test-time training and persistent fine-tuning, with separate budgets
  for context, compute, latency and memory. If a newly initialized small
  adapter does much better than updating existing weights, that points to
  a shortage of modifiable organization ([THEORY-1353](../theory.d/THEORY-1353.md)'s uncommitted heads).
- **Sampling and interaction (A60, after U27).** Pass@k curves per
  checkpoint and an interactive task varying breadth k and depth T, with a
  separate verifier, so coverage is kept apart from delivered success
  ([CLAIM-697](../claims.d/CLAIM-697.md), [THEORY-1894](../theory.d/THEORY-1894.md), [THEORY-1703](../theory.d/THEORY-1703.md)).
- **Exchange rates (A62).** The least multi-resource budget per
  checkpoint and task as a Pareto frontier ([CLAIM-585](../claims.d/CLAIM-585.md)), read as exchange
  rates among training, context, adaptation, sampling and verification:
  [QUESTION-338](../questions.d/QUESTION-338.md)'s question in general form.
- **Active acquisition (A67, after U30).** Random, uncertainty,
  information-gain and capability-value selection of demonstrations, with
  selection compute charged, matched budgets, and held-out tasks chosen
  independently of the policy.

## What it could and could not show

It could show that later checkpoints of one run need a larger budget to learn new
task families and whether any intervention or acquisition route relieves
it. It could not distinguish pretraining length from the shape of that
run's schedule, with one run; nor show that the synthetic families stand
for capabilities that matter. The owner asked for the design; whether to
run it is the owner's call.

## Note of 2026-11-19: readings for the exchange "Topological protection explained"

Biderman and colleagues' Pythia (THEORY-tmp7himr), read: the named models exist, 70M- and 160M-deduped, with checkpoints at step 0, log-spaced to 512 and every 1,000 steps to 143,000. Three confounds the design should state: the learning rate decays on a cosine to a tenth of peak, so later checkpoints also sit at lower learning rates; the deduplicated models run about 1.5 epochs, so late checkpoints have seen their data twice; and there is one run per size. Optimizer states are not said to be public, so the fresh-optimizer rule stands.

Springer and colleagues (THEORY-tmp3dqbl), read, ran nearly this design on OLMo checkpoints and on small models pre-trained to separate budgets, each annealed to zero, which is a way to remove the single-run schedule confound. Their effects showed mostly on the old-capability axis, which supports scoring both axes; they did not measure A_s, so they do not supply the primary estimand.

Tandon and colleagues (THEORY-tmpv904w), read: test-time updates on an initialization not trained for them ("TTT-naive") gain little, while a meta-learned initialization nearly matches full attention. Pythia is not meta-learned for test-time updates, so the TTT arm measures TTT-naive, and a weak TTT result could reflect the missing outer loop rather than lost plasticity; the design should say so.

Pan and colleagues (THEORY-tmppqtz3), read, find task learning flat in small models (their smallest is 350M) whatever the number of demonstrations, so the in-context arm at 70M and 160M risks a floor. The study's synthetic families lack a natural label space, so in-context success on them is task learning by construction; a larger replication size, or recognition controls on a natural-language family, would make the arm informative.

Yin and Steinhardt (THEORY-tmpqvj8f), read, give a Pythia baseline for the in-context arm: in all seven sizes, function-vector heads and few-shot accuracy keep rising from about step 16,000 to the end of training. In-context adaptability is still growing at the late checkpoints compared, the pattern A56 said would bear against reading overconsolidation as a loss of all adaptability, and a query–key reset should be scored for its cost to these heads.

Raghu and colleagues (THEORY-tmpfhidr), read: a short adaptation budget on families that existing features serve measures reuse, not plasticity. The frozen-readout mode should be reported beside full fine-tuning at every checkpoint, so that a held-out family counts as needing new structure only where the frozen-body baseline fails.

Nichol, Achiam and Schulman (THEORY-tmpbzf9h), read: Reptile differs from joint training only through a term that grows with step size times inner steps (§5.1). The matched-resource Reptile arm needs its inner budget k fixed and joint training plus fine-tuning on the same tasks as control, which the authors call "a strong baseline"; their RL results were negative, so the interactive arms should not inherit Reptile without a pilot.

Yin and colleagues (THEORY-tmpzauel), read, place meta-overfitting in tasks identifiable from the query input alone. The case's per-example randomized families are mutually exclusive already, and held-out families add the guard; the diagnostic is high pre-update accuracy on meta-training tasks with low meta-test accuracy. A run can settle in a memorizing or an adapting mode, so the meta-trained arm needs several seeds.

Rajendran, Irpan and Jang (THEORY-tmpy398k), read, show learner overfitting surviving mutually exclusive tasks, which supports held-out task-generating processes over shuffled tasks alone. Which form a run shows "depends on random seed", so the meta-trained arm should use several seeds and report pre- and post-update accuracy on training and validation tasks.

No status change.
