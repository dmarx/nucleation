---
number: 362
status: Active
formerly:
- CASE-tmpez9id
title: 'Five simulated populations trained on one structured schema, independent, socially trained then separated, conforming, enforcing by referee, and checking disagreements against the world, each with and without a collective vote: a criterion of shared perspective stated in advance finds none of them sharing one, since unperturbed members take up under three per cent of a deviation some members carry; the evidential condition orders the populations as predicted below its stated size, and the restorative condition is passed by plain conformity'
version: 2
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-087 at the
    coordinator's brief. The criterion (TERM-149, TERM-148)
    and the study's thresholds and predictions were committed before
    any code (commit 5d1f1b83f). Model, tests, scripts, results and a
    README are under scratch/studies/lead-087/.
- version: 2
  date: '2026-11-25'
  note: >-
    Promoted to Active under the owner's delegation of 2026-11-24
    ("handle the fixes for the twelve ... use your best judgement"),
    as the status pass of 2026-11-24 and the reruns of 2026-11-25
    applied it to independently recomputed demonstrated claims and
    executed studies, in the recomputation pass of 2026-11-25
    (LEAD-tmpc0rqa). Rerun by a session other than the filer's from a
    copy of scratch/studies/lead-087/: results.jsonl, summary.txt,
    diagnostics.jsonl and summary_diag.txt are byte for byte the
    stored ones, and the 6 tests pass; every figure in the body was
    compared and matches, the paired contrast 0.021 [0.015, 0.028]
    recomputed from the results. An executed study, with no premise of
    its own; nothing targets it.
standing: documented
kind: executed-study
tags:
- social-ontology
- agency
- complex-systems
date: '2026-11-22'
line:
- distributed-agency
variant_of:
- CASE-145
bears_on:
- QUESTION-260
- QUESTION-276
draws_on:
- THEORY-1800
summary: >-
  [CASE-145](CASE-145.md) run as [LEAD-087](../leads.d/LEAD-087.md) asked, after its criterion was stated. Thirty
  simulated members learn six category prototypes from one structured
  schema; at test they meet in pairs on stimuli from a shared world, with
  sparse feedback from it matched across arms. Five interaction arms:
  none (correlated responses), conformity during training only (socially
  learned norms), unconditional conformity, enforcement by a referee, and
  disagreements checked against the world. Each also ran with and
  without a vote that enacts a collective action and learns from a
  collective reward. Some members' interpretation of one category was
  perturbed, with the world moving the same way (warranted) or not. Over
  20 seeds, every population is structurally concordant, and only the
  interacting ones draw the perturbed members back; but unperturbed
  members take up at most 2% of the deviation, under the 5% stated in
  advance, so none passes cross-member dependence and none shares a
  perspective by either reading. The evidential condition ranks the arms
  as predicted (0.025 against 0.004 for conformity) below its stated
  0.05, in five settings. Conformity passes the restorative condition,
  which therefore fails A4's test. The vote gives collective agency in
  every arm and its absence none, so the study gives no constructed
  instance of perspective without collective agency. A stipulated model,
  one size. The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: TERM-149 TERM-148 CLAIM-946 CLAIM-945 — new; filed with this case for LEAD-087 -->
<!-- inactive-ok-file: THEORY-1800 — Proposed; DeChurch and Mesmer-Magnus, the measurement constraint the criterion's first condition follows -->
<!-- inactive-ok-file: CLAIM-417 — Proposed; its defeater is cited as what the criterion must meet -->

# CASE-362: Five simulated populations trained on one structured schema, independent, socially trained then separated, conforming, enforcing by referee, and checking disagreements against the world, each with and without a collective vote: a criterion of shared perspective stated in advance finds none of them sharing one, since unperturbed members take up under three per cent of a deviation some members carry; the evidential condition orders the populations as predicted below its stated size, and the restorative condition is passed by plain conformity

## What was stated in advance

[CASE-145](CASE-145.md)'s A4: the study "only helps the theory if it specifies, ahead of
time, what additional relational organization distinguishes a
perspective from" correlated responses or socially learned norms. The
criterion was filed first, as two rival terms, and committed with the
study's model, thresholds and predicted verdicts before any code was
written (scratch/studies/lead-087/README.md, "Stated in advance").

- **Condition 1, structural concordance**: members' category structures
  (distances among their prototypes) correlate beyond members trained on
  different schemas by 0.3. After DeChurch and Mesmer-Magnus ([THEORY-1800](../theory.d/THEORY-1800.md)).
- **Condition 2, cross-member dependence both ways**: perturbing a subset
  S (20%) moves the unperturbed U by more than ε = 0.05 of the deviation,
  against a twin run with the same random numbers, and S is drawn back
  more than ε faster than with interaction removed.
- **Condition 3**, in two readings the owner chooses between.
  [TERM-149](../terms.d/TERM-149.md), evidential: a warranted deviation is taken up by U more
  than an unwarranted one of the same size, by more than ε.
  [TERM-148](../terms.d/TERM-148.md), restorative: the deviation is restored rather than
  averaged, its dilution ratio under half the averaging benchmark f/(1 − f).
- **A4's failure rule**, stated with them: if plain conformity passes
  condition 3, or the correlated-response or learned-norm populations
  pass condition 2, the criterion fails to make the distinction, and that
  counts against the category.

## The populations

Thirty members, six categories in four dimensions, one structured
teacher schema (two clusters of three). A member's interpretive state is
its prototypes; it answers with the nearest. Each learns from its own
labelled stream. At test, members meet in random pairs on a stimulus
from the world, and every member receives sparse labelled feedback, the
total matched across arms to the evidential arm's checks.

| arm | at test |
|---|---|
| independent | no interaction: correlated responses by common training |
| learned-cut | conformed to partners during training, none at test: socially learned norms |
| conform | each moves toward its partner's label, unconditionally |
| enforce | on disagreement a third member referees; the minority moves |
| evidential | on disagreement the pair checks the world; both learn the true label |

Crossed with a **vote**: every round the members label a common
stimulus, the majority label is enacted through a collective policy
table that learns from a collective reward no member receives. It does
not feed back into the members' prototypes, so the perspective measures
are the same with and without it. Collective agency was tested in
[TERM-044](../terms.d/TERM-044.md)'s sense only: the collective contingency flips at round 300,
and the population's action must adapt (a > 0.25). Without the vote the
population's action is read as the majority of members' own actions.

## What it found

Twenty seeds per arm; 95% intervals over seeds (summary.txt).

| arm | concordance | U's spillover s_u, s_w | S drawn back beyond independent | σ = s_w − s_u | dilution ρ | agency, vote / none |
|---|---|---|---|---|---|---|
| independent | 0.985 | 0, 0 | 0 | 0 | 0 | 0.64 / 0.01 |
| learned-cut | 0.989 | 0, 0 | 0 | 0 | 0 | 0.64 / 0.01 |
| conform | 0.989 | 0.015, 0.019 | 0.55 | 0.004 [−0.003, 0.011] | 0.024 | 0.64 / 0.01 |
| enforce | 0.986 | 0.009, 0.015 | 0.14 | 0.006 [0.001, 0.010] | 0.031 | 0.63 / 0.01 |
| evidential | 0.985 | −0.009, 0.017 | 0.11 | 0.025 [0.017, 0.033] | −0.030 | 0.63 / 0.01 |

The concordance margin over different schemas was 0.55 in every arm;
members agreed on about 96% of answers in every arm.

- **No population shares a perspective, by either reading.** Every arm
  passes condition 1. The two controls fail condition 2 as intended: their
  unperturbed members do not move at all. But so do the three interacting
  arms. Their members draw S back (by 0.11 to 0.55 of the deviation,
  beyond what the world alone does), and U's dependence on S is real, its
  intervals clear of zero, but it is at most 2% of the deviation.
- **The evidential condition orders the arms as predicted, below its
  stated size.** σ is largest for the evidential arm, and its paired
  contrast with conformity, 0.021 [0.015, 0.028], is clear of zero;
  enforcement and conformity do not differ. In the evidential arm U moves
  *away* from an unwarranted deviation (s_u = −0.009): disagreements with
  S send U to the world, which corrects U's own boundary. That is A8's
  "answering is not agreeing" in miniature, and the signed maximum
  condition 2 was stated with misses dependence of that sign. Taken in
  absolute value it still fails.
- **The restorative condition fails A4's test.** Plain conformity
  restores a minority's deviation (ρ = 0.024, against the averaging
  benchmark 0.25 and the threshold 0.125). The benchmark assumed members
  average their states; members who copy one another's *answers* about a
  shared world, most of them in agreement, restore instead. By the rule
  stated in advance, the restorative reading does not tell a perspective
  from coordinated feedback in general.
- **Collective agency follows the vote, in every arm.** With it the
  population adapts to the flipped contingency (a ≈ 0.63); without it,
  not at all. The independent population with a vote is a collective
  agent, in [TERM-044](../terms.d/TERM-044.md)'s sense, with no shared perspective by the
  criterion: the boundaries come apart in that direction, by
  construction. The direction [LEAD-087](../leads.d/LEAD-087.md) asked for, a perspective with no
  collective agent, is not shown, because no population passed the
  perspective criterion.

## After the verdict: what was tried, not part of it

Run after the verdict (diagnostics.py, summary_diag.txt), twenty seeds
each: twice as many perturbed members, a fifth of the world's feedback,
three times the social learning rate, and a shorter window. U's spillover
stays under 0.03 in all of them. The evidential σ is the largest in
every setting (0.013 to 0.037) and beats conformity's, paired, in every
setting, but never reaches 0.05. Conformity's ρ stays near 0.025.

The reason is in the design: members interact through answers about
stimuli the world supplies, and a deviation of one prototype changes
those answers only near category boundaries. Most of what passes between
members is the world's, not S's. The dependence condition was stated as
a share of the deviation; in such populations it is the deviants'
recovery and the selectivity of the others' response that show the
coupling, not the others' displacement. A criterion restated that way
would need to be stated again in advance and run again; it is not
rescored here.

## What it shows, and what it does not

- **For A4's test.** The criterion as stated separates correlated
  responses and learned norms from interacting populations (conditions 1
  and 2's recovery part), and its evidential condition separates
  evaluation from conformity in direction. It did not find a shared
  perspective anywhere, so it neither supports [CLAIM-418](../claims.d/CLAIM-418.md)'s separation by
  example nor answers [QUESTION-260](../questions.d/QUESTION-260.md). By the evidential reading's stated
  rule nothing counts against the category; by the restorative reading's,
  conformity passing condition 3 does.
- **For [CLAIM-417](../claims.d/CLAIM-417.md)'s defeater** (that "organizational perspective" cannot
  be told from coordinated feedback in general): the evidential reading
  tells them apart in direction and not at the size stated; the
  restorative reading does not tell them apart.
- **The findings filed from it.** [CLAIM-946](../claims.d/CLAIM-946.md): restoration does not
  tell evaluation from conformity on answers. [CLAIM-945](../claims.d/CLAIM-945.md): the
  criterion finds no shared perspective here, and why.
- **Not real groups.** A stipulated model of one size, one schema, label
  exchange only. It shows what a criterion does on populations whose
  organization is known, not that any real group has or lacks a shared
  perspective.

## Rerun

`OMP_NUM_THREADS=1 python3 -I study.py 20`, then
`python3 -I summarize.py`; the post-hoc variants with `diagnostics.py`
and `summarize_diag.py`; tests with `python3 -I -m pytest test_model.py`.
About a minute on one core.

## Note of 2026-11-25: rerun by a session other than the filer's

Rerun on 2026-11-25 by the assistant, a session other than the filer's, in the recomputation pass of LEAD-tmpc0rqa, at the owner's go-ahead of 2026-11-25 ("go ahead with the reruns"). From a copy of `scratch/studies/lead-087/` in the session's scratch space, with its results and summaries set aside: `study.py 20`, `summarize.py`, `diagnostics.py 20` and `summarize_diag.py`, run with python3 -I. The 6 tests pass. `results.jsonl`, `summary.txt`, `diagnostics.jsonl` and `summary_diag.txt` are byte for byte the stored ones. Every figure above was compared and matches: the results table row by row (concordance 0.985 to 0.989, agreement about 96 %, margin 0.545 to 0.549; spillover, recovery, σ with its intervals, ρ and agency); the paired contrast of σ, evidential against conformity, 0.021 [0.015, 0.028], and enforcement against conformity 0.002 [−0.002, 0.006], both recomputed here from the per-seed results with summarize.py's interval; and the post-hoc settings (spillover under 0.03 throughout, evidential σ 0.013 to 0.037 and ahead of conformity's in every setting, conformity's ρ 0.024 to 0.034). Nothing failed to reproduce. Promoted in the same pass (history, version 2). The note is the assistant's (Claude, in this session).
