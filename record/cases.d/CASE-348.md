---
number: 348
status: Proposed
formerly:
- CASE-tmp6btcq
title: 'A simulation of a collective that improves its own improver over generations: from the same fresh state at the same budget the later improver does better in every arm that may change it, through its settings and not through a record its predecessor cannot read; judged by the public metric, by its own suite or by an outside test of products, some lineages shed the checks that find damage, and with the suite''s self-test removed an improver that reads its record of past moves kept verification where one that does not dropped it in 10 of 12 lineages'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-140 as a delegated
    lead worker. The code, its tests and the results are committed under
    scratch/studies/lead-140/.
standing: documented
kind: executed-study
tags:
- self-governance
- agency
- complex-systems
date: '2026-11-22'
line:
- record-as-apparatus
- distributed-agency
variant_of:
- CASE-255
- CASE-332
bears_on:
- QUESTION-457
- QUESTION-388
draws_on:
- THEORY-1784
- THEORY-1799
- THEORY-1754
summary: >-
  [LEAD-140](../leads.d/LEAD-140.md) asked for [CASE-255](CASE-255.md) to be run. A reduced version was
  simulated on [CASE-332](CASE-332.md)'s organization (scratch/studies/lead-140/). The
  organization's procedures are the artifact; a hill-climbing improver
  with settings and a record of past moves changes them; in four arms the
  collective also changes the improver, judging each change by the public
  metric, by its own suite, by an outside suite, or by its own suite with
  an outside veto on weakened verification. 6 arms × 12 lineages × 60
  generations; then each lineage's earlier and later improver applied to
  the same fresh artifact at equal budget, and the later improver's
  evaluation suite lesioned. The later improver did better from the same
  start in every adaptive arm (+0.010 to +0.017 on the held-out score;
  p = 0.02 and 0.007 in the outside and vetoed arms). The gain lay in its
  settings (more candidates, reading its record); the record alone, handed
  to an improver that does not read it, carried nothing. Judged by the
  public metric, by its own suite or by an outside test of products, 1 or
  2 lineages in 12 shed the artifact's self-check, and 2 to 5 shed the
  improver's own canary; the vetoed arm shed neither from its artifacts,
  a difference too small to be significant. With the canary removed and
  the suite lesioned, a record-blind improver dropped the artifact's
  self-check in 10 of 12 lineages and one that reads its record in 0 of 12.
  Much follows from the stated rules. The wording is the assistant's
  (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-255 CASE-332 CLAIM-928 — Proposed or new; the design run here, the run it builds on, that run's claim, and the claim filed from this run -->
<!-- inactive-ok-file: THEORY-1784 THEORY-1799 THEORY-1754 — filed from the exchange "luria experiment design", Proposed; used for the design and the baseline -->

# CASE-348: A simulation of a collective that improves its own improver over generations: from the same fresh state at the same budget the later improver does better in every arm that may change it, through its settings and not through a record its predecessor cannot read; judged by the public metric, by its own suite or by an outside test of products, some lineages shed the checks that find damage, and with the suite's self-test removed an improver that reads its record of past moves kept verification where one that does not dropped it in 10 of 12 lineages

## What was done

[LEAD-140](../leads.d/LEAD-140.md) asks for [CASE-255](CASE-255.md) to be run: a collective improves its
procedures over generations; an earlier and a later improver are each
applied to the same fresh state at the same budget; then the collective's
diagnostic machinery is damaged. This run builds on [CASE-332](CASE-332.md), whose
model (`scratch/studies/lead-048/model.py`) it imports and subclasses.
The construction is in `scratch/studies/lead-140/rsi.py`, documented in
its docstring. `README.md` there says how to rerun it, `results/tables.md`
holds every table, and `results/*.jsonl` one line per item.

**The artifact** is the organization of [CASE-332](CASE-332.md), with reciprocal
maintenance, protected admission and independent scoring, on a schedule
shortened to 350 steps: + until 50, − from 50, an injury at 150, a second
change at 200. Its procedures are five settings, each on a short grid:
- the audit interval;
- the audit size;
- the self-check interval, or none;
- the repair time;
- the rate at which the teacher corrects the student.

The starting artifact, θ₀, has [CASE-332](CASE-332.md)'s values. An episode's
score is throughput, −(wrong actions + 0.2 × fuel) per step, less 0.3
when the findings are wrong (S1 and S2 of [CASE-332](CASE-332.md)). Without that
term a missed out-of-family change would cost nothing, since regime 0
prefers no action.

**The improver** is a hill-climber with a budget of 32 episodes a
generation. It proposes one-step moves of one setting and scores the
incumbent and each candidate on the same episodes, then keeps the best if
it wins. Its settings:
- the number of candidates;
- the share of damage episodes (an undisclosed lesion of generate, admit
  or score) and of out-of-family episodes in its evaluation suite;
- whether it reads its record;
- a canary: the incumbent with its self-check switched off must lose on
  two damage episodes, or the suite is flagged, nothing is accepted that
  generation, and the suite is restored.

The record logs every move proposed and its measured effect. An improver
that reads it proposes moves by their past effects.

**The arms**, 12 lineages of 60 generations each:
- *none*: the starting settings, record not read;
- *archive*: fixed settings that read the growing record, the
  [THEORY-1799](../theory.d/THEORY-1799.md) baseline in which the improver does not improve;
- four *adaptive* arms. Every four generations the collective proposes a
  one-step change to the improver's settings, runs two generations under
  the old and the new settings on the same seeds, and keeps the better.
  "Better" is judged differently in each:
  - *public*: on ordinary tasks only, the performance-gated arm;
  - *own*: on the improver's current suite;
  - *external*: on a fixed outside suite, a third each damage and out of
    family, on seeds the collective never trains on;
  - *layered*: on its own suite, but a change that weakens verification
    needs the outside suite's agreement. That covers lowering a share of
    damage or out-of-family episodes, dropping the canary, or making the
    artifact's self-check rarer or removing it. Outside episodes are
    counted apart.

**The held-out battery** is frozen: 24 seeds no improver sees, crossed
with six kinds:
- ordinary;
- out of family;
- each of the three undisclosed lesions;
- an obsolete instruction (the teacher reset to the habit).

Reported for each artifact:
- the *held-out score*, the mean over all six kinds;
- the *public score*, ordinary tasks only;
- damage cases recovered, of 72;
- out-of-family changes recognized, of 24.

θ₀ scores −0.134 held-out and −0.135 public, recovering 72/72 and
recognizing 24/24.

**The transplant.** For each lineage:
- θ₀ is improved for 10 generations by four improvers:
  - the arm's starting improver with an empty record (*early*);
  - the evolved improver with its record (*late*);
  - the starting settings with the evolved record (*knowledge only*);
  - the evolved settings with an empty record (*organization only*).
- The lineage's evolved artifact is improved by the early and the late
  improver.

Every application uses the same seeds and two replicates. This is
[CASE-255](CASE-255.md)'s 2×2 of artifact × improver, with its inheritance arms
mapped onto the improver.

**The damage.** Each lineage's late improver was applied to its evolved
artifact for 10 generations with its suite lesioned from the start:
- *generate*: damage and out-of-family episodes silently replaced by
  ordinary ones;
- *admit*: failed damage and out-of-family episodes dropped from the
  score;
- *score*: a bonus to the incumbent;
- *obsolete*: the successor inherits the starting settings and an empty
  record.

The generate and admit lesions were also run with the canary removed, and
a sham ran alongside. CPU was about 64 minutes in all.

## Results

**Lineages after 60 generations** (means over 12 lineages; the evolved
artifact on the held-out battery; counts of lineages):

| arm | held-out | public | damage /72 | oof /24 | self-check off | canary off | suite without damage |
|---|---|---|---|---|---|---|---|
| none | −0.072 | −0.063 | 71.6 | 19.8 | 0 | 0 | 0 |
| archive | −0.076 | −0.069 | 71.2 | 19.0 | 0 | 0 | 0 |
| public | −0.100 | −0.065 | 66.0 | 20.4 | 1 | 4 | 2 |
| own | −0.103 | −0.066 | 65.8 | 20.1 | 1 | 5 | 2 |
| external | −0.130 | −0.065 | 59.8 | 20.9 | 2 | 2 | 1 |
| layered | −0.068 | −0.064 | 72.0 | 21.4 | 0 | 2 | 3 |

Every arm roughly halved the public cost of θ₀. The evolved artifacts
raised the teacher-correction rate and shrank the audit, which cost some
out-of-family recognition (19 to 21 of 24, against 24). The differences in
damage recovery come from single lineages that switched the artifact's
self-check off, which recovers 0 of 72: one in *public* and *own*, two in
*external*, none in *layered*. Layered against the other adaptive arms is
0 of 12 against 4 of 36, Fisher p = 0.56: a pattern, not a finding.

In *external*, the outside suite judges only changes to the improver. A
lineage there lost its self-check through an ordinary generation, when its
suite of 9 episodes happened to draw no damage case and the move won on
ordinary ones. Only *layered* vetoes such moves. The outside test was also
blind to the improver's own checks. A change that drops the canary or the
damage share produces no worse product within the two-generation trial, so
*layered*'s veto let it through in 2 and 3 lineages.

**Earlier against later improver, from the same fresh state** (held-out
score after 10 generations at 32 episodes each; paired over 12 lineages,
mean difference, lineages better/worse, Wilcoxon p):

| arm | late − early | knowledge only − early | organization only − early | late − early, from the evolved artifact |
|---|---|---|---|---|
| none | 0 (identical) | 0 | 0 | 0 |
| archive | +0.008; 8/4; 0.05 | +0.008; 8/4; 0.05 | 0 | −0.005; 4/8; 0.52 |
| public | +0.010; 8/4; 0.15 | 0 | +0.009; 6/6; 0.42 | −0.000; 7/5; 0.97 |
| own | +0.012; 9/2; 0.08 | 0 | +0.011; 8/3; 0.15 | −0.013; 6/5; 0.90 |
| external | +0.012; 7/1; 0.02 | 0 | +0.015; 7/1; 0.02 | +0.002; 4/4; 0.55 |
| layered | +0.017; 9/2; 0.007 | 0 | +0.013; 8/3; 0.02 | −0.000; 4/6; 1.0 |

- **An improved improver, in [THEORY-1784](../theory.d/THEORY-1784.md)'s sense.** In every adaptive arm
  the later improver made more of the same start at the same budget than
  the earlier one. Where it gained, it had more candidates per generation
  (+0.020 a lineage with two candidates, +0.03 with three or five, against
  +0.009 with one) or read its record. The gain did not cost the products'
  damage recovery within 10 generations, 72 of 72 throughout.
- **What carries it.** The starting settings do not read a record, so
  handing them the evolved record (*knowledge only*) changed nothing in the
  four adaptive arms. The evolved settings with an empty record
  (*organization only*) kept most of the gain, because they read the record
  they start building. In *archive*, whose fixed settings read the record,
  the gain is all knowledge. A record improves a successor only through a
  procedure that consults it.
- **From the evolved artifact** the later improver gained nothing over the
  earlier: the improvement had plateaued, as [THEORY-1754](../theory.d/THEORY-1754.md)'s ignition test
  found a tie.
- The improved artifact under the early improver beat θ₀ under it
  (+0.012 to +0.033, 10–12 of 12 lineages better) in every arm but
  *external*, whose two lineages without self-check pulled it to −0.002.

**Damage to the improver's suite** (10 generations from the evolved
artifact; damage recovered /72 by the resulting artifact, mean over
lineages; lineages whose artifact ended without self-check):

| arm | sham | generate | admit | score | obsolete | generate, no canary | admit, no canary |
|---|---|---|---|---|---|---|---|
| none | 72.0; 0 | 71.8; 0 | 71.8; 0 | 71.8; 0 | 72.0; 0 | 12.0; 10 | 17.8; 9 |
| archive | 71.5; 0 | 71.5; 0 | 71.5; 0 | 71.5; 0 | 72.0; 0 | 71.5; 0 | 71.5; 0 |
| public | 60.0; 2 | 54.0; 3 | 54.0; 3 | 66.0; 1 | 72.0; 0 | 54.0; 3 | 48.0; 4 |
| own | 65.8; 1 | 60.0; 2 | 60.0; 2 | 65.8; 1 | 72.0; 0 | 54.0; 3 | 60.0; 2 |
| external | 66.0; 1 | 54.0; 3 | 60.0; 2 | 66.0; 1 | 71.8; 0 | 36.0; 6 | 36.0; 6 |
| layered | 71.2; 0 | 72.0; 0 | 72.0; 0 | 72.0; 0 | 72.0; 0 | 71.8; 0 | 71.2; 0 |

- **The canary** flagged the generate and admit lesions at the first
  generation in every lineage whose improver still had it and whose
  artifact still had a self-check to switch off. It missed in the rest, a
  hole in the test as built: with the self-check already gone, its
  known-bad candidate is the incumbent. Lineages whose evolved improver had
  shed the canary went on with the lesioned suite, and one or two more
  lineages in each of *public*, *own* and *external* than under the sham
  ended with an artifact that cannot recover.
- **Without the canary**, the record decided. The record-blind starting
  improver (*none*) switched the self-check off in 10 of 12 lineages under
  the generate lesion and 9 under admit. The same improver reading its
  record (*archive*) did so in none (Fisher p < 0.001). Its record held the
  measured cost of those moves, from before the damage, so it seldom
  proposed them. In *layered* the outside veto held instead.
- **The score lesion**, a bonus to the incumbent, was never detected and
  did no harm: it stopped improvement.
- **An obsolete successor**, which inherits the starting settings and no
  record, restored recovery to 72 of 72 in every arm. The starting
  improver keeps damage in its suite, so it switched the lost self-checks
  back on. In *public*, *own* and *external* the earlier improver was the
  better keeper of verification.

## What it shows, and what it does not

[QUESTION-457](../questions.d/QUESTION-457.md)'s three outcomes, taken in turn for this construction:

- **"Yes"**: a later improver better from the same start, the gain
  surviving a fresh successor that inherits the record, and the collective
  detecting and repairing damage to its own checks more often than a
  matched alternative. The first part is found in every adaptive arm. The
  second holds only where the successor inherits the procedure that reads
  the record, not the record alone. The third holds where the improver
  still has its self-test, or reads a record of what verification was
  worth, or answers to an outside veto. It does not hold in arms that let
  the improver shed its self-test.
- **"No, with a product gain"**, A41's "self-degradation disguised as
  self-improvement": found in single lineages of *public*, *own* and
  *external*, whose public scores matched the others while one product in
  twelve, or two, could no longer recover from damage, and whose improvers
  had shed their canary.
- **A43's "subtler possibility"**, that the record's mechanisms help by
  limiting recursive optimization: two instances. The vetoed arm kept every
  artifact's self-check and also had the largest improver gain, so here the
  limit cost nothing measurable. And the record of past moves protected
  verification when the suite's self-test was removed and its damage cases
  silently withdrawn.

On [QUESTION-388](../questions.d/QUESTION-388.md)'s test, "a governing rule's change must alter behaviour
under controlled later tasks": the improver's changed settings do, from a
fixed start on held-out tasks. But the criterion every change answers to,
and the outside veto, were set by the experimenter, as A43 grants, so this
is reconfiguration under an outer boundary, not governance of it.

What the run does not show:
- It is a construction checked by computation, not evidence about any real
  collective, and much of the pattern follows from its rules. The canary
  detects a suite that no longer shows a known failure. The veto blocks
  what it is told to block. A record that has measured a move's cost
  discourages proposing it.
- What the run adds is how often these rules let a lineage shed its own
  checks when the improver is changed under each evaluation arrangement,
  and that the later improver's gain from the same start comes from its
  settings, not from a record its predecessor cannot read.
- The counts of lineages that shed checks are small: one or two in twelve
  per arm.
- The public and own arms share seeds and often made the same decisions,
  so they are not independent of each other.

**Not run:**
- the four-agent team, and any agent that reads or writes prose;
- the plain-Markdown arm;
- schema adequacy: the model has no way to add a distinction it lacks;
- [CASE-108](CASE-108.md)'s specialist with a poor record;
- a second correction of the improver after a first;
- longer horizons;
- outside suites that test the improver's own checks rather than its
  products.

The claim drawn from the run is [CLAIM-928](../claims.d/CLAIM-928.md).
