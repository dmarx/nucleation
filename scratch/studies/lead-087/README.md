# LEAD-087: perspective without collective agency (CASE-145), simulated

## Stated in advance (committed before any code)

The criterion is TERM-tmpsu4df (evidential reading) and its rival
TERM-tmpo4pxh (restorative reading). Conditions 1 and 2 are shared;
condition 3 differs. Thresholds: concordance margin 0.3 over the
different-schema control; ε = 0.05 of the perturbation size; dilution
benchmark f/(1 − f) = 0.25 for f = 0.2, threshold 0.125; 95% intervals
over seeds.

### Model

- N = 30 members, K = 6 categories in a d = 4 feature space. A teacher
  schema is K prototypes with structure (two clusters of three).
  World stimuli: a category drawn at random, a point at its prototype
  plus Gaussian noise.
- A member's interpretive state: its own K prototypes. Its response to a
  stimulus: the nearest prototype. Its structure: the K×K matrix of
  distances among its prototypes (upper triangle).
- Training (all arms): each member learns its prototypes from its own
  stream of labelled stimuli (running mean with a learning rate), from a
  member-specific initial state. The different-schema control trains
  each member on its own randomly drawn teacher.
- Test phase, rounds of random pairs on a shared stimulus. Every arm
  receives sparse environmental feedback (a labelled stimulus) at a rate
  matched across arms in total feedback events per member.

### Interaction arms (factor 1)

- **independent**: no interaction at test (correlated responses by
  common training).
- **learned-cut**: members learned by conformity during training as well
  as from the world, then stop interacting at test (socially learned
  norms).
- **conform**: each member of a pair moves its prototype for the
  partner's label toward the stimulus, unconditionally (coordinated
  feedback in general).
- **enforce**: when a pair disagrees, a third member is drawn as referee
  and labels the stimulus; the minority label's holder moves toward the
  majority label (norms enforced by peers, no evidence).
- **evidential**: when a pair disagrees, the pair checks the stimulus
  against the world, and the one in error moves toward the true label.
  The checks are counted, and the other arms' base feedback rate is set
  so that every arm has the same number of world-label events per member.

### Mechanism (factor 2)

- **none**, or **vote**: each round the population faces a collective
  choice: all members label a common stimulus, the majority label is
  enacted through a collective policy table (category → one of two
  actions) learned by the mechanism from a collective reward that no
  member receives. The vote does not feed back into members' prototypes,
  so the perspective measures are not confounded by it.
- **Collective agency test** (TERM-044 only: a goal-directed description
  of the population earns its keep and its policy would adapt). At a
  set round the collective contingency flips. Adaptation a = share of
  collective actions matching the new contingency in the final window,
  minus the share matching it before the flip. Without a mechanism the
  population's "action" is read as the majority of members' individual
  actions, each from a member's own fixed table. Passes when a > 0.25
  (lower end of the 95% interval).

### Perturbations

Twin runs with common random numbers. S = 6 members (f = 0.2). The
prototype of one category in S moves by δ (half the distance to its
nearest neighbour) in a fixed random direction. Warranted: the world's
prototype for that category moves the same way at the same round.
Unwarranted: the world does not move. Twins: the same run without S's
perturbation (with the world shift, for the warranted case).

### Predicted verdicts (stated before running)

| arm | C1 | C2 | C3 evidential | C3 restorative | CA none | CA vote |
|---|---|---|---|---|---|---|
| independent | pass | fail | fail | fail | fail | pass |
| learned-cut | pass | fail | fail | fail | fail | pass |
| conform | pass | pass | fail | fail | fail | pass |
| enforce | pass | pass | fail | pass | fail | pass |
| evidential | pass | pass | pass | pass | fail | pass |

If conform passes C3 under either reading, or independent or learned-cut
pass C2, the criterion fails A4's test, and that is reported as counting
against the category. The CA column is close to true by construction;
the study's interest is in the perspective columns and in reading them
beside it.

## How to rerun

From this directory, with BLAS threads set to 1:

    OMP_NUM_THREADS=1 python3 -I -m pytest -q -p no:cacheprovider test_model.py
    OMP_NUM_THREADS=1 python3 -I study.py 20      # results.jsonl, about 20 s
    python3 -I summarize.py > summary.txt          # the verdict stated in advance
    OMP_NUM_THREADS=1 python3 -I diagnostics.py 20 # post hoc, diagnostics.jsonl
    python3 -I summarize_diag.py > summary_diag.txt

study.py and diagnostics.py append one line per (seed, arm) and skip
lines already written.

## Result (see CASE-tmpez9id)

C1 passes in every arm. C2 fails in every arm: unperturbed members move
by at most 0.019 of the deviation (threshold 0.05), though S's recovery
beats the independent arm by 0.11-0.55 in the interacting arms.
Evidential sigma 0.025 [0.017, 0.033], below 0.05, ahead of conform
paired. Conform passes the restorative C3 (rho 0.024), so that reading
fails A4's test by the rule stated above. CA: vote about 0.63 in every
arm, none about 0.01. Departures from the predictions: conform, enforce
and evidential were predicted to pass C2; evidential to pass C3
(evidential); conform to fail C3 (restorative). Also: the signed max in
C2 misses dependence of negative sign (evidential s_u < 0); with |s| it
still fails.
