---
number: 294
status: Proposed
formerly:
- CASE-294
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
- QUESTION-495
- QUESTION-338
summary: >-
  Requested by the owner at U23 of the exchange "Topological protection
  explained" (2026-11-19), "design an experiment using pythia", to test
  overconsolidation ([CLAIM-758](../claims.d/CLAIM-758.md)). A52 designed it; A54, A56, A58, A60,
  A62 and A67 added arms after the owner raised meta-learning (U24),
  in-context learning (U25), test-time training (U26), Large Language
  Monkeys and PASS@(k,T) (U27) and active learning (U30). Its prior result
  is Dong's plasticity loss over Pythia training ([THEORY-1353](../theory.d/THEORY-1353.md), Proposed).
  Not run. The design is A's; adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-2006 THEORY-2013 THEORY-2019 THEORY-2025 THEORY-2039 THEORY-2042 THEORY-2049 THEORY-2053 THEORY-2056 — Proposed; cited in this filing of 2026-11-19 -->
<!-- inactive-ok-file: CLAIM-697 CLAIM-758 THEORY-1353 THEORY-1703 — Proposed; cited in this filing of 2026-11-19 -->

# CASE-294: A proposed study: across Pythia checkpoints of one pretraining run, measure the budget each checkpoint needs to acquire held-out synthetic task families by fine-tuning, in-context learning and test-time training, and the success it reaches by sampling and interaction, to see whether later checkpoints are better now but cost more to teach new tasks (overconsolidation), and what exchange rates hold among these ways of spending work

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
  steps), with 160M for replication ([LIT-2841](../literature.d/LIT-2841.md)). Seeds of fine-tuning
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
  matched resources ([LIT-2791](../literature.d/LIT-2791.md)); held-out task-generating processes,
  not only held-out tasks, against meta-overfitting ([LIT-2838](../literature.d/LIT-2838.md),
  [LIT-2817](../literature.d/LIT-2817.md)); higher pretraining weight decay as a preventive arm
  ([LIT-2820](../literature.d/LIT-2820.md)).
- **In-context learning (A56, after U25).** A response surface over
  checkpoint, number of demonstrations and fine-tuning budget, with the
  prediction that in-context adaptability may rise while fine-tuning
  plasticity falls, which would defeat the overconsolidation reading for
  that model ([CLAIM-758](../claims.d/CLAIM-758.md)'s defeated_if). Controls separating task
  recognition from task learning ([LIT-2826](../literature.d/LIT-2826.md); Min et al., [THEORY-496](../theory.d/THEORY-496.md)).
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

Biderman and colleagues' Pythia ([THEORY-2013](../theory.d/THEORY-2013.md)), read: the named models exist, 70M- and 160M-deduped, with checkpoints at step 0, log-spaced to 512 and every 1,000 steps to 143,000. Three confounds the design should state: the learning rate decays on a cosine to a tenth of peak, so later checkpoints also sit at lower learning rates; the deduplicated models run about 1.5 epochs, so late checkpoints have seen their data twice; and there is one run per size. Optimizer states are not said to be public, so the fresh-optimizer rule stands.

Springer and colleagues ([THEORY-2006](../theory.d/THEORY-2006.md)), read, ran nearly this design on OLMo checkpoints and on small models pre-trained to separate budgets, each annealed to zero, which is a way to remove the single-run schedule confound. Their effects showed mostly on the old-capability axis, which supports scoring both axes; they did not measure A_s, so they do not supply the primary estimand.

Tandon and colleagues ([THEORY-2049](../theory.d/THEORY-2049.md)), read: test-time updates on an initialization not trained for them ("TTT-naive") gain little, while a meta-learned initialization nearly matches full attention. Pythia is not meta-learned for test-time updates, so the TTT arm measures TTT-naive, and a weak TTT result could reflect the missing outer loop rather than lost plasticity; the design should say so.

Pan and colleagues ([THEORY-2039](../theory.d/THEORY-2039.md)), read, find task learning flat in small models (their smallest is 350M) whatever the number of demonstrations, so the in-context arm at 70M and 160M risks a floor. The study's synthetic families lack a natural label space, so in-context success on them is task learning by construction; a larger replication size, or recognition controls on a natural-language family, would make the arm informative.

Yin and Steinhardt ([THEORY-2042](../theory.d/THEORY-2042.md)), read, give a Pythia baseline for the in-context arm: in all seven sizes, function-vector heads and few-shot accuracy keep rising from about step 16,000 to the end of training. In-context adaptability is still growing at the late checkpoints compared, the pattern A56 said would bear against reading overconsolidation as a loss of all adaptability, and a query–key reset should be scored for its cost to these heads.

Raghu and colleagues ([THEORY-2025](../theory.d/THEORY-2025.md)), read: a short adaptation budget on families that existing features serve measures reuse, not plasticity. The frozen-readout mode should be reported beside full fine-tuning at every checkpoint, so that a held-out family counts as needing new structure only where the frozen-body baseline fails.

Nichol, Achiam and Schulman ([THEORY-2019](../theory.d/THEORY-2019.md)), read: Reptile differs from joint training only through a term that grows with step size times inner steps (§5.1). The matched-resource Reptile arm needs its inner budget k fixed and joint training plus fine-tuning on the same tasks as control, which the authors call "a strong baseline"; their RL results were negative, so the interactive arms should not inherit Reptile without a pilot.

Yin and colleagues ([THEORY-2056](../theory.d/THEORY-2056.md)), read, place meta-overfitting in tasks identifiable from the query input alone. The case's per-example randomized families are mutually exclusive already, and held-out families add the guard; the diagnostic is high pre-update accuracy on meta-training tasks with low meta-test accuracy. A run can settle in a memorizing or an adapting mode, so the meta-trained arm needs several seeds.

Rajendran, Irpan and Jang ([THEORY-2053](../theory.d/THEORY-2053.md)), read, show learner overfitting surviving mutually exclusive tasks, which supports held-out task-generating processes over shuffled tasks alone. Which form a run shows "depends on random seed", so the meta-trained arm should use several seeds and report pre- and post-update accuracy on training and validation tasks.

No status change.

## Note of 2026-11-19: Chen, Kunin, Yamamura and Ganguli, read
A measure to add ([NOTE-2127](../notes.d/NOTE-2127.md)): Chen and colleagues' fraction of independent neurons, units counted identical within a tolerance of their norms (p. 7), beside the dead-unit and effective-rank measures at each checkpoint. Their caution applies: residual connections fall outside their propositions (p. 8), and Pythia is residual.

## Note of 2026-11-19: follow-up turns of "Topological protection explained"
<!-- inactive-ok-file: CASE-297 — Proposed or Deferred; cited from the follow-up turns filed 2026-11-19 -->

ChatGPT's experiment ranking (A80, A82) keeps this study as the main test of overconsolidation and adds design points:
- **Rules by episode.** Randomize the task-generating rule by episode, "not independently between a support example and its associated query", so a task is learnable at all.
- **Censoring.** Report runs that never reach the threshold as censored outcomes rather than dropping them; fresh optimizer state and calibrated learning rates.
- **Reading a slower late checkpoint.** If fine-tuning slows but in-context learning improves, adaptation may be "shifting between mechanisms"; if adapters recover it, the limit "may involve modifiability of existing parameters"; if new tasks are learned at the cost of old competence, it is a stability–plasticity tradeoff, "not necessarily inefficient learning".
- **Not rediscovering plasticity loss.** "We shouldn't try to rediscover plasticity loss." The distinctive question is whether the loss changes the learner's "total resource-indexed repertoire, or merely shifts adaptation toward other mechanisms".
Extra arms only after the primary contrast is measured. After the owner's U37, ChatGPT ranked it below a literature synthesis on pretraining and the Reddit study ([CASE-297](CASE-297.md)).

## Note of 2026-11-19: the pretraining works, read
Design points from two readings. Anguita and colleagues ([NOTE-2159](../notes.d/NOTE-2159.md)): the scale of the re-initialized head and the relative scale of the layers decide whether fine-tuning reuses features or learns new ones, so the study should fix and report the head's initialization and scale, or checkpoint differences may be a change of regime rather than consolidation; rescaling the readout or all weights before fine-tuning are cheap intervention arms beside the resets; the participation ratio and shared dimensions are a readout of reuse against new learning. McDermott and colleagues ([NOTE-2138](../notes.d/NOTE-2138.md)): a continued-training control with the new objective switched off is the right control for more training against this objective, and their one convergence curve shows why the study needs a threshold, censoring and fixed stopping rules.

## Note of 2026-11-19: Brown and colleagues, and Howard and Ruder, read
Design points. Howard and Ruder ([NOTE-2141](../notes.d/NOTE-2141.md)): labelled examples needed to match a comparator is a ready form for the primary estimand, and shows that what the comparator holds fixed must be stated; the fine-tuning protocol alone moves acquisition cost greatly (on TREC-6 from 5.69 to 16.09 error across methods), so it must be fixed and calibrated in advance; and access to unlabelled task text is part of the declared learning interface. Brown and colleagues ([NOTE-2160](../notes.d/NOTE-2160.md)): accuracy against the number of in-context examples by size is the shape the in-context arm needs, but its estimand should be examples to a threshold, which they do not compute; and their smallest models degrade with more examples on some tasks, a floor for 70M and 160M models beside Pan and colleagues'.

## Note of 2026-11-19: the data-scheduling readings, read
Design points. Liu and colleagues ([NOTE-2154](../notes.d/NOTE-2154.md)) ran the nearest design: the same model family and sizes, a checkpoint series each fine-tuned, forgetting scored on the pretraining distribution. They trained from scratch, measured final loss after four epochs rather than budget to a threshold, and chose learning rates on one checkpoint, which can bias late checkpoints under a cosine schedule, a confound this case already notes. Chen and colleagues ([NOTE-2165](../notes.d/NOTE-2165.md)): steps to a loss threshold is the estimand's form, and their pairwise probe runs are a cheap way to find which earlier skills lower a later cost. Hu and colleagues ([NOTE-2157](../notes.d/NOTE-2157.md)): a matched natural-language first phase is the control that separates content from schedule.

## Note of 2026-11-19: the scheduling follow-up readings, read
<!-- inactive-ok-file: THEORY-2060 THEORY-2068 THEORY-2076 — Proposed or newly filed; cited from the readings of 2026-11-19 -->

Several follow-up readings show what this study would add. Nishida and
colleagues ([THEORY-2060](../theory.d/THEORY-2060.md)) run a checkpoint pipeline on Pythia that
measures alignment, not cost; Blakeney and colleagues ([THEORY-2068](../theory.d/THEORY-2068.md))
and Feng, Prabhumoye and colleagues ([THEORY-2076](../theory.d/THEORY-2076.md)) report end-of-run
scores without a cost to a threshold. None prices a later acquisition by
checkpoint.

## Note of 2026-11-19: the task-composition readings, read
<!-- inactive-ok-file: THEORY-2092 — Proposed or newly filed; cited from the readings of 2026-11-19 -->

He and colleagues ([THEORY-2092](../theory.d/THEORY-2092.md)) find that no model composes a new fact
in the second hop after fine-tuning; a held-out two-hop family built that
way could fail for reasons unrelated to checkpoint age, a design caution
for this study.
