---
number: 758
status: Proposed
formerly:
- CLAIM-tmp8ljvp
title: 'Overconsolidation, a generalization of overfitting: relative to a declared family of later acquisitions lying outside the training task distribution, continued stabilization of a learner can keep improving its present objective while raising the budget it needs to acquire that family to a declared reliability with its held capabilities kept above a declared floor, so collateral forgetting counts as part of the cost; it is not overfitting to a data distribution, nor task-level overfitting within a training task distribution, and it is a failure only relative to that family and horizon'
version: 2
role: thesis
warrant: interpretive
defeated_if: >-
  Evidence that every case is one of the failures it is kept apart from:
  overfitting to a data distribution; task-level overfitting, where the
  later family is drawn from the training task distribution; or forgetting
  that a constrained acquisition does not make worse with longer
  stabilization, so that the constrained cost of a declared later
  acquisition never rises with continued training while present
  performance rises. Or that the rise is always undone by another route
  the same learner already has, as when in-context adaptability rises
  while fine-tuning plasticity falls, so that nothing is lost but the
  place where learning happens.
history:
- version: 2
  date: '2026-11-19'
  note: >-
    Revised after the readings of 2026-11-19 (curation entry 071802), at
    the owner's request. No reading showed version 1's signature with held
    capabilities kept. Springer and colleagues' overtraining is mostly
    forgetting under fine-tuning, and Yin and colleagues' and Rajendran and
    colleagues' cases are task-level overfitting within the training task
    distribution. Version 2 declares the later family outside that
    distribution and prices acquisition with held capabilities kept above
    a floor, so collateral forgetting is part of the cost. Version 1's title
    read: 'Overconsolidation, a generalization of overfitting: relative to a declared family of future demands, continued stabilization of a learner''s organization can keep improving its present objective while raising the cost of acquiring, recovering or reaching other capabilities, so a learner can learn itself into a trap without overfitting its data; it is a failure only relative to that declared family and horizon'.
tags:
- learning-theory
- representation-learning
- complex-systems
date: '2026-11-19'
line:
- learned-structure
- readiness
rests_on:
- CLAIM-675
- CLAIM-569
complements:
- CLAIM-695
- CLAIM-520
- CLAIM-605
- CLAIM-754
bears_on:
- QUESTION-495
summary: >-
  The owner's generalization, in A's wording. A48 §8 named "the
  possibility of learning oneself into a trap"; the owner answered at U22
  of the exchange "Topological protection explained" (2026-11-19): "sounds
  like you've landed on a generalization of overfitting that I think
  captures the more recent notion of "over cooking" a learning process."
  A50 then separated overfitting, a failure across a distribution of
  examples, from what it named overconsolidation, which "can happen
  without conventional overfitting", and A71 §8 gave its signature: the
  operational frontier grows on familiar tasks while the developmental
  frontier does not contain its predecessor ([CLAIM-754](CLAIM-754.md)). The record
  held the trajectory form for support ([CLAIM-675](CLAIM-675.md)), plasticity loss as a
  reading ([THEORY-1353](../theory.d/THEORY-1353.md)) and the RL case in pass@k terms ([CLAIM-695](CLAIM-695.md)); it
  held no general claim for training. Revised to version 2 after the
  readings of 2026-11-19: the later family lies outside the training task
  distribution, and acquisition is priced with held capabilities kept, so
  collateral forgetting counts as cost.
uses:
- TERM-131
---
<!-- inactive-ok-file: THEORY-2006 THEORY-2015 THEORY-2019 THEORY-2025 THEORY-2027 THEORY-2034 THEORY-2053 THEORY-2056 — Proposed; cited in this filing of 2026-11-19 -->
<!-- inactive-ok-file: CASE-294 CLAIM-695 CLAIM-754 THEORY-1353 — Proposed; cited in this filing of 2026-11-19 -->

# CLAIM-758: Overconsolidation, a generalization of overfitting: relative to a declared family of later acquisitions lying outside the training task distribution, continued stabilization of a learner can keep improving its present objective while raising the budget it needs to acquire that family to a declared reliability with its held capabilities kept above a declared floor, so collateral forgetting counts as part of the cost; it is not overfitting to a data distribution, nor task-level overfitting within a training task distribution, and it is a failure only relative to that family and horizon

## Version 2, after the readings

Two changes, both forced by the readings of 2026-11-19.

- **The later family lies outside the training task distribution.**
  Yin and colleagues ([THEORY-2056](../theory.d/THEORY-2056.md)) and Rajendran and colleagues
  ([THEORY-2053](../theory.d/THEORY-2053.md)) show meta-learners whose training loss improves while
  their adaptation to new tasks from the same task distribution is lost.
  Their authors call it task-level overfitting. That is the
  claim's first defeater, so version 2 excludes it by declaring the later
  family outside the training task distribution.
- **Acquisition is priced with held capabilities kept.** Springer and
  colleagues ([THEORY-2006](../theory.d/THEORY-2006.md)) find that past an inflection point a
  longer-pretrained model ends worse after fine-tuning, mainly because
  fine-tuning degrades more of what it held. Version 1 set forgetting
  aside and so had no case. Version 2 measures the budget to reach the new
  family at a declared reliability while keeping held capabilities above
  a declared floor. Collateral forgetting is then part of the acquisition
  cost, and Springer's result is a case of it rising with stabilization.
  Han and colleagues ([THEORY-2015](../theory.d/THEORY-2015.md)) show pretraining weight decay
  lowering that cost at a fixed budget, a regime comparison, not a time
  course.

What version 2 still lacks is a case where present performance rises,
the constrained cost of a declared out-of-distribution family rises with
training time, and forgetting is measured, all in one run.
[CASE-294](../cases.d/CASE-294.md)'s primary estimand is that measurement.

## The claim

The owner, at U22 of the exchange "Topological protection explained"
(https://chatgpt.com/share/6afe6dd0-9d78-83ea-9782-f55680665dcf), on A48
§8's heading "The possibility of learning oneself into a trap":

> sounds like you've landed on a generalization of overfitting that I think captures the more recent notion of "over cooking" a learning process.

A50 §7 gave the general form: "the consolidation that makes acquired
capabilities inexpensive to use can also make alternative capabilities
expensive to acquire." Its toy model: value V(s) = P0(s) − λA(s) − C(s)
over training time s, with present performance P0 rising and the cost A
of a later acquisition rising too, so that "The optimal time to stop
learning one thing can precede the point at which one has stopped
improving at that thing." With P0 = 1 − e^(−s), A = a + αs and no training
cost, V′ = e^(−s) − λα, so for 0 < λα < 1 the optimum is s* = ln(1/(λα))
(A50 §1; checked).

## Its signature

In A71 §8's terms ([CLAIM-754](CLAIM-754.md)), the operational repertoire on a
declared set of familiar tasks contains its predecessor while the
developmental frontier, what can be learned within an acquisition budget,
does not. "The learner has improved its established competence but has
not preserved every previously affordable route to further competence."
[CLAIM-695](CLAIM-695.md) is the RL case: low-budget reliability gained, high-budget
coverage lost.

## What it is not

- **Not overfitting.** Overfitting fails across a distribution of
  examples; this can occur on a learner that generalizes on its training
  distribution.
- **Not forgetting.** Held capabilities may be kept; what rises is the
  cost of those not yet held.
- **Not one scalar.** Reusable structure, the capacity to acquire new
  structure and the capacity to retain old structure can move apart (A54
  §5, after Raghu et al.'s feature reuse, [LIT-2822](../literature.d/LIT-2822.md)), and in-context
  adaptability can rise while fine-tuning plasticity falls (A56 §3), which
  is defeated_if's second clause.
- **Not a failure in itself.** "That doesn't prove the learning was
  suboptimal; the lost adaptability might have little value in the
  relevant future" (A71 §8). A specialist in a stable environment is not
  overconsolidated. [CLAIM-520](CLAIM-520.md)'s conditional value of a corrective capacity
  is the same point for audits.
- **Not new as an objective.** Meta-learning's objective already targets
  future adaptability (A54 §3). What the claim adds is the name of the
  failure and its signature in resource terms.

## Candidate mechanisms (A50 §2–4; A's)

Overcompression: a learned equivalence stays sufficient for the present
target and becomes insufficient for the next ([CLAIM-152](CLAIM-152.md), [CLAIM-350](CLAIM-350.md)).
Plasticity loss, read as depletion of uncommitted capacity ([THEORY-1353](../theory.d/THEORY-1353.md),
whose relief by a query–key reset counts only if background skills
survive, per [CLAIM-347](CLAIM-347.md)'s note of 2026-11-04). Policy entrenchment. The
amortization trap, in which operating cost falls while reconfiguration
cost rises ([CLAIM-569](CLAIM-569.md)). Inquiry traps, in which the learner stops seeking
the evidence that would change it ([THEORY-285](../theory.d/THEORY-285.md), [CLAIM-466](CLAIM-466.md)).

## Rests on

- [CLAIM-675](CLAIM-675.md): the same capabilities now can leave different capabilities
  later, demonstrated for support; this claim says training can be such a
  process for the learner itself.
- [CLAIM-569](CLAIM-569.md): what it costs to acquire a form is not fixed by what it costs
  to keep it.

## Evidence wanted

Springer et al. ([LIT-2829](../literature.d/LIT-2829.md)), Han et al. ([LIT-2820](../literature.d/LIT-2820.md)) and Dohare et
al. ([LIT-2810](../literature.d/LIT-2810.md)), registered unread, are the empirical cases A cited.
[CASE-294](../cases.d/CASE-294.md) is the owner-requested test on Pythia checkpoints.

## Note of 2026-11-19: readings for the exchange "Topological protection explained"

Springer and colleagues ([THEORY-2006](../theory.d/THEORY-2006.md)), read, are the claim's prime case, and they qualify it. Past an inflection point the base model improves while the fine-tuned model gets worse, by forgetting that grows with pre-training: "for modifications of equal magnitude, models that have undergone longer pre-training exhibit greater forgetting". The new task itself gets worse only in some settings (RTE and TREC at a tuned learning rate). The case counts only if the cost of acquiring includes collateral loss of held capability, which the Not-forgetting bullet excludes.

Yin and colleagues ([THEORY-2056](../theory.d/THEORY-2056.md)), read, observe a learner whose training loss improves while its capacity to adapt is lost: "models that converge to a memorization solution have lower training error than solutions which use the task training data". They call it "a subtle form of task overfitting", distinct from standard overfitting. That has the claim's signature and an existing name, so it presses the first clause of defeated_if: here the failure is overfitting, across a distribution of tasks rather than of examples.

Rajendran, Irpan and Jang ([THEORY-2053](../theory.d/THEORY-2053.md)), read, add learner overfitting: a base learner that fails on new tasks even when tasks are mutually exclusive, while meta-training performance holds. It is a second named overfitting with the same signature, and the same pressure on the first clause of defeated_if. The claim's Not-overfitting bullet, which defines overfitting over examples, does not yet exclude it.

Han and colleagues ([THEORY-2015](../theory.d/THEORY-2015.md)), read: higher pre-training weight decay gives a worse pre-training loss and a better fine-tuned score. That fits the claim's trade between the present objective and later acquisition, but it compares regimes, not continued training within one, measures plasticity only as the fine-tuned score, and does not measure forgetting. It qualifies the claim: a preventive regime exists, the trap itself is not shown.

Dohare and colleagues ([THEORY-2027](../theory.d/THEORY-2027.md)), read, show networks losing the ability to learn new tasks, kept by the authors apart from forgetting and with no overfitting. That is a failure of acquisition outside both named failures, which the claim needs. But the present objective does not improve there: performance on each new task falls. So it shows plasticity loss, a candidate mechanism the claim lists, and not the claim's signature.

Raghu and colleagues ([THEORY-2025](../theory.d/THEORY-2025.md)), read, separate reusing held features from rapidly changing them, and find MAML takes the first: "feature reuse is the dominant factor". That supports the Not-one-scalar bullet only in a weaker form: fast adaptation can coexist with almost no change of representations. Neither quantity is tracked over training, and retention is not measured.

Hospedales and colleagues ([THEORY-2034](../theory.d/THEORY-2034.md)), skimmed, name meta-overfitting as metaknowledge that "constrains the hypothesis space" of θ too tightly around the source tasks (§2.1). That is close to the claim's raised cost of reaching other capabilities, framed as a failure of generalization across tasks, the rival naming defeated_if anticipates.

Nichol, Achiam and Schulman ([THEORY-2019](../theory.d/THEORY-2019.md)), read, suggest from their expansion that ordinary SGD "automatically" performs a MAML-like update favouring generalization between mini-batches (§7). If so, ordinary training carries part of an adaptability objective, and overconsolidation would be that term ceasing to pay rather than its absence. The suggestion is untested beyond few-shot classification, so it leaves the claim open.

Its standing. No reading shows the full signature: present competence rising, a declared later acquisition costing more, held capabilities kept. Springer's case is mainly forgetting; Yin's and Rajendran's have the signature and are named task overfitting. To survive, the claim must declare its future family outside the training task distribution, so it is not task overfitting, and either keep held capabilities in the signature, leaving Springer no case, or count collateral forgetting as acquisition cost and redraw its line with forgetting. [CASE-294](../cases.d/CASE-294.md)'s A_s tests the clean version.

No status change.

## Note of 2026-11-19: Chen, Kunin, Yamamura and Ganguli, read
<!-- inactive-ok-file: THEORY-2009 — Proposed; cited from the readings of 2026-11-19 -->

An analogy with the right shape ([THEORY-2009](../theory.d/THEORY-2009.md); [NOTE-2127](../notes.d/NOTE-2127.md)), not evidence. Long training at a large learning rate keeps improving present generalization while driving the network toward invariant sets from which escape is slower ("the repulsive escape will take longer the closer it starts from the invariant set", p. 10). Chen and colleagues value this as preventing overfitting; whether it raises the cost of a declared family outside the training distribution is untested. A candidate mechanism for the claim, to measure in [CASE-294](../cases.d/CASE-294.md). The claim is unchanged.

## Note of 2026-11-19: the pretraining works, read
<!-- inactive-ok-file: THEORY-2072 THEORY-2077 — Proposed; cited from the readings of 2026-11-19 -->

Neither bears on the claim's time course. Anguita and colleagues ([THEORY-2077](../theory.d/THEORY-2077.md); [NOTE-2159](../notes.d/NOTE-2159.md)) never vary pretraining length; they show, in a solvable model, that how cheaply something is learned later can depend on a property of the representation the present objective does not see (the relative scale of the layers), which makes the claim's mechanism coherent without showing it operate. McDermott and colleagues ([THEORY-2072](../theory.d/THEORY-2072.md); [NOTE-2138](../notes.d/NOTE-2138.md)) give, as a bound, a pre-training form of the overcompression mechanism this claim lists: a label-defined constraint caps a later task whose labels vary within the pre-training classes ("once saturation is reached, it will not improve beyond this fixed upper bound relating to task correlation"). It does not grow with training there. The claim is unchanged.

## Note of 2026-11-19: Brown and colleagues, and Howard and Ruder, read
Neither reading bears on the claim's time course; pretraining length is varied in neither. A terminological caution from Howard and Ruder ([NOTE-2141](../notes.d/NOTE-2141.md)): their "catastrophic forgetting" is loss of the pretrained benefit on the target task, read off rising validation error and conflated by them with overfitting, not collateral loss of held capabilities, which is the forgetting version 2 counts as cost. Not a forgetting case for this claim.

## Note of 2026-11-19: the data-scheduling readings, read
Three parallels, none the claim's signature. Liu and colleagues ([NOTE-2154](../notes.d/NOTE-2154.md)): in a 160M checkpoint series, in-domain loss after fine-tuning is flat after about 40B tokens and general loss after fine-tuning slightly rises late, within the bands, at most a faint version of Springer and colleagues' pattern. Hu and colleagues ([NOTE-2157](../notes.d/NOTE-2157.md)): "there is an optimal duration after which additional formal language pre-pretraining leads to less effective transfer overall", continued first-phase training raising the cost of a later family outside its distribution, without the first phase's own objective or held capabilities reported. Gururangan and colleagues ([NOTE-2151](../notes.d/NOTE-2151.md)) measure general-domain loss rising after domain adaptation, on a shifted distribution, not continued stabilization. The claim is unchanged.

## Note of 2026-11-19: the scheduling follow-up readings, read
<!-- inactive-ok-file: THEORY-2059 THEORY-2069 THEORY-2075 THEORY-2081 — Proposed or newly filed; cited from the readings of 2026-11-19 -->

Hernandez and colleagues ([THEORY-2059](../theory.d/THEORY-2059.md), corroborates) give independent
evidence: in the high-data regime, pretraining leaves small models unable
to reach from-scratch performance even with 10 to 100 times the data that
saturates them, which the authors call ossification; forgetting is not
measured, and they flag tuning as a possible remedy. Stern and colleagues
([THEORY-2081](../theory.d/THEORY-2081.md)) show collateral forgetting of a first phase at an abrupt
switch, part of its cost. The procedural paper ([THEORY-2075](../theory.d/THEORY-2075.md)) finds a
first phase driven to too low a loss worsens later transfer, small-scale.
Akter and colleagues ([THEORY-2069](../theory.d/THEORY-2069.md)) qualify: reasoning-rich pretraining
does not worsen later fine-tuning at 8B and 1T tokens, one run per arm.

## Note of 2026-11-19: Kuhn, read
<!-- inactive-ok-file: THEORY-tmpg10ux THEORY-tmptbea0 — Proposed or newly filed; cited from the readings of 2026-11-19 -->

Kuhn qualifies this claim. Structure ([THEORY-tmpg10ux](../theory.d/THEORY-tmpg10ux.md)) describes the
pattern, training "almost perfectly equipped" for puzzles and resistant to
a fresh approach, but counts the same rigidity as functional for the
community, since anomaly is visible only against a precise paradigm; and a
late convert can still work in the new paradigm as a foreigner, a raised
cost rather than an impossibility. Through a stand-in ([THEORY-tmptbea0](../theory.d/THEORY-tmptbea0.md)),
the 1959 essay holds that rooted training is a precondition of breaking
with a tradition. Together they suggest something this claim lacks:
consolidation that raises the cost of a later acquisition can lower the
cost of detecting that it is needed. Analogy, about communities of
scientists.
