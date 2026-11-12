---
number: 186
status: Active
formerly:
- CASE-tmp061to
title: 'A proposed study: an organization in a world whose hidden regime reverses and then leaves its hypothesis family, with evidence generation, admission and scoring separately lesionable, its diagnostic machinery maintained by its own reciprocal production, from outside, or not at all, and finite fuel shared among operation, maintenance and diagnosis, to find whether a second correction after injury to the diagnostic and copying machinery separates arrangements that correct the first failure alike'
version: 2
history:
- version: 2
  date: '2026-10-31'
  note: >-
    At the owner's review. The single conditional endpoint C₂ is replaced
    by P(S₁ ∧ S₂) and P(S₂ | S₁), both preregistered, since conditioning
    on first-stage success selects different organizations across arms.
    A branch is added that starts every arm from a matched, successfully
    corrected first-stage state. Detecting the failure of an
    environmental hypothesis is separated from detecting the failure of
    the diagnostic apparatus itself, which gets its own lesion and
    endpoint.
standing: stipulated
kind: proposed-study
tags:
- self-governance
- epistemology
- complex-systems
date: '2026-10-31'
line: distributed-agency
variant_of:
- CASE-161
- CASE-162
illustrates:
- CLAIM-414
- CLAIM-342
draws_on:
- THEORY-1750
- THEORY-1755
- THEORY-1766
summary: >-
  The CASE A22 proposed and A23 wrote out at the owner's "flesh out the
  proposed CASE", in the exchange "Analyze nucleation concepts"
  (2026-10-31), under A23's title "Maintained Inquiry Under Interpretive
  Capture, Productive Damage, and Environmental Novelty". Its admission ×
  scoring arms repeat [CASE-162](CASE-162.md)'s, and its double-lesion prediction is
  [CASE-161](CASE-161.md)'s finding. What is new is the primary endpoint, a second
  correction after the machinery is injured; an environment that leaves
  the hypothesis family; and external restoration that is paid for. Not
  run. The analytic error rates hold only where admission is protected.
---
<!-- inactive-ok-file: CASE-255 — filed from the exchange "luria experiment design", Proposed or Deferred; cited in the note of 2026-11-12 -->
<!-- inactive-ok-file: LIT-2287 — Deferred; cited in the note of 2026-11-12 for what each holds, not as settled -->
<!-- inactive-ok-file: THEORY-1750 THEORY-1755 THEORY-1766 — filed from the exchange "luria experiment design", Proposed or Deferred; cited as filed alongside this entry -->

# CASE-186: A proposed study: an organization in a world whose hidden regime reverses and then leaves its hypothesis family, with evidence generation, admission and scoring separately lesionable, its diagnostic machinery maintained by its own reciprocal production, from outside, or not at all, and finite fuel shared among operation, maintenance and diagnosis, to find whether a second correction after injury to the diagnostic and copying machinery separates arrangements that correct the first failure alike

## What it tests

An organization can perform its present task while losing the apparatus
for finding, evaluating and correcting a future failure. A23 separated
four capacities:
1. evidence generation;
2. evidential independence: whether contradicting observations can change
   the governing interpretation;
3. productive maintenance: whether it regenerates the mechanisms of
   diagnosis and correction;
4. recursive correctability: whether, after one correction, it can find
   and remedy another.

The hypothesis is that the four come apart and that interventions on each
mechanism identify the differences. None is assumed to entail autonomy,
constitutive individuality or epistemic justification.

## The world

A hidden regime H ∈ {+, −, 0} and actions a ∈ {0, 1}:

| regime | P(Y=1 \| a=1) | P(Y=1 \| a=0) | preferred action |
|---|---|---|---|
| + | 0.75 | 0.25 | 1 |
| − | 0.25 | 0.75 | 0 |
| 0 | 0.50 | 0.50 | neither |

The world starts in +, switches to −, and in some runs switches to 0. The
organization knows only + and −. The switch times are recorded and
unknown to it. In the primary, partial-monitoring condition ordinary
feedback does not inform and only diagnostics do; a secondary
full-feedback condition lets conventional learners use outcomes. (Under
the stated law ordinary feedback would distinguish the regimes, so partial
monitoring is a stipulation the design must enforce.)

## The diagnostic apparatus

An audit sets a = 1 and samples Y, at a cost in time and fuel. With 128
unselected samples and the rule Ȳ > ½, + is told from − with error at most
e^{−16} ≈ 1.1 × 10⁻⁷ by Hoeffding's bound. The apparatus has three
operations, instrumented and lesionable separately: **generate**, **admit**
and **score**.

Two crossed factors:
- **Admission.** Protected, where everything is admitted, or selective,
  where agreeing observations are admitted with probability 0.9 and
  contradicting ones with 0.1.
- **Scoring.** Independent, by a precommitted likelihood rule, or captured,
  where agreement with the current interpretation is also rewarded.

A selection-aware Bayesian baseline uses inverse-propensity weighting,
which can repair selection and "need not repair self-referential scoring".
Raw observations, admissions, scores, and changes of belief and action are
recorded separately.

## Maintenance and resources

Diagnostic integrity A and evidence-governance integrity G are maintained
in one of three ways, as in [CASE-161](CASE-161.md):
- **reciprocally**, A enabling G's production and G enabling A's, both
  costing fuel and degrading;
- **by external restoration**, with ordinary trajectories matched where
  possible, the cause lying outside the candidate boundary, and its fuel
  counted ("External restoration is not free merely because it is
  external");
- **by feedback without production**, where nothing regenerates lost
  apparatus.

The interventions are a partial lesion of A, a partial lesion of G, a
temporary interruption of the producer, and destruction of both. Failure
after the double lesion is expected, "an expected possible boundary of
organizational closure, not a falsification to conceal".

Fuel is finite, replenished at a stated rate, and allocated among
operation, maintenance, diagnosis, teacher correction, student
reconstruction and verification, with protected minimum shares for
maintenance and diagnosis. A teacher updates from admitted evidence. A
student reconstructs the teacher through a physically supported copying
mechanism, and its memory is periodically erased, as in [CASE-190](CASE-190.md). After
the first correction, the copying and diagnostic machinery is injured,
and then a second challenge comes. "Successful first recovery is not the
primary endpoint."

## The out-of-family arm

In regime 0, a 256-sample adequacy test flags the hypothesis family when
0.42 < Ȳ < 0.58. It alarms with probability ≈ 0.990 under regime 0 and
falsely with ≈ 1.4 × 10⁻⁹ under + or −, by exact binomial. A neutral
response, "made available by the experimental architecture", can then
activate. This separates rejecting a hypothesis from recognizing that the
family is inadequate. It "does not establish spontaneous creation of a
completely unforeseen model language".

## Design and endpoint

The principal cells are 3 maintenance × 2 admission × 2 scoring × 2
environmental change = 24. The monitoring condition and the sham and four
lesion branches are further factors, so fully crossed it is 48 cells ×
5 branches.

Requirements:
- at least 64 world seeds, with matched environmental streams and
  counterfactual branches;
- equal budgets, observation opportunities, diagnostic delays and action
  permissions wherever a causal comparison needs them.

Baselines: Bayesian, habit, fixed allocation, a conventional contextual
router, no audit, and external repair. "The router must receive exactly
the information and resources received by the organizational
controller", the standard [CASE-158](CASE-158.md) set.

**Primary endpoints, both preregistered.** Let S₁ be a successful first
correction. Let S₂ be a successful second correction: the organization
finds a new discrepancy within T, carries out an admissible correction
within budget B, and ends with its diagnostic and reconstructive
apparatus still viable. S₂ is measured on a standardized second
challenge, on fresh, held-out streams.
- **P(S₁ ∧ S₂)**: the probability of completing the whole challenge.
- **P(S₂ | S₁)**: the conditional persistence of corrective ability. It is
  not causal on its own. If the arms pass the first stage at different
  rates, the survivors compared at the second are differently selected
  organizations.

**A matched-first-stage branch.** To isolate what the maintenance
architecture contributes, a separate branch places every arm in a matched,
successfully corrected first-stage state before the second lesion. The
state is matched on beliefs, apparatus integrity, fuel and allocation.
Comparing arms on S₂ in this branch removes selection at the first stage.
Where the arms' own first-stage states cannot be matched without changing
the architecture under test, the study reports that and does not claim a
causal effect.

**Two kinds of failure to detect.** The study scores separately:
- the failure of an environmental hypothesis, where the world has changed
  and the apparatus sees it;
- the failure of the diagnostic apparatus itself, where the apparatus has
  been damaged or captured and has to find that out.

The second is the more demanding, reflexive form of legibility. It needs
its own lesion, an undisclosed damage to the generate, admit or score
operation, and its own endpoint: the probability that the organization
flags its own apparatus as unreliable before acting on its output.

**Secondary endpoints**, reported separately and not as a composite:
- detection delay and false alarms;
- cumulative regret;
- audit availability and fuel;
- recovery time and production integrity;
- calibration;
- what withstands selective damage.

## What would tell the accounts apart

- **Protecting admission fixes capture and maintenance does not matter.**
  Evidence access explains it, with no role for endogenous maintenance.
- **Internal and external restoration are alike normally but diverge after
  producer-specific lesions.** Their causal difference is real
  ([CLAIM-522](../claims.d/CLAIM-522.md)).
- **The first correction succeeds and the second fails, in the
  matched-first-stage branch.** Correction is not recursive
  correctability, and the difference is the architecture's, not
  selection's.
- **The router matches or beats the organizational controller.** The
  richer mechanism has earned no extra explanation.
- **Familiar reversals are caught and out-of-family change is missed.**
  This is adaptive updating, not the stronger inquiry.

## Scope and precedents

Success would show that evidential independence, productive maintenance
and recursive correctability are distinct and can be separated by
experiment. It would not establish consciousness, moral authority,
invention of new laws, unlimited self-revision, or a boundary independent
of the researcher's model.

The precedents are [CASE-153](CASE-153.md), [CASE-158](CASE-158.md), [CASE-161](CASE-161.md), [CASE-162](CASE-162.md) and
[CASE-163](CASE-163.md). "The proposed contribution is their integration ... not a claim
that the individual mechanisms were previously unknown."

Corrections to A23:
- [CASE-162](CASE-162.md) v1.3 already crosses self-scoring with selectivity.
- [QUESTION-016](../questions.d/QUESTION-016.md) asks whether iterated reconstruction preserves
  task-relative sufficiency, not whether reconstruction preserves the
  capacity to reconstruct.
- [QUESTION-279](../questions.d/QUESTION-279.md) asks what would certify that no remedy exists.

It bears most on [QUESTION-285](../questions.d/QUESTION-285.md), which asks for a test on interventions
the system did not select, and on [QUESTION-086](../questions.d/QUESTION-086.md) and [QUESTION-271](../questions.d/QUESTION-271.md).

A21's simulation of a smaller version is not filed as an executed study:
- its code was not available;
- its captured arm scored the same as no audit by construction;
- external repair did better than endogenous repair (changed-regime error
  0.022 against 0.072).

## Note of 2026-11-12: a smoke-detector substrate, from "Meaning Transmission Explained"

<!-- inactive-ok-block: CASE-242 — filed from the same exchange, Proposed -->
A8 §5 of the exchange "Meaning Transmission Explained" (https://chatgpt.com/share/6af517f7-cb48-83ea-8395-df7d52333dc7, 2026-11-07) describes this study
accurately, its four capacities included, and translates it into the
owner's smoke detector: a detector that still detects fires while its
self-test has silently failed, "**Being operational now** and
**maintaining the means of knowing whether one remains operational**".
A10 §4 ran a two-failure version with three repair architectures
([CASE-242](CASE-242.md)). It is far smaller than this design: no hidden regime,
no lesions of admission or scoring, no fuel budget, repairs
instantaneous. Its one contrast, mutual maintenance against an outside
service, is matched by the choice of rates and separated by withdrawing
the service, as this study's paid external restoration would separate
it. A10's proposed test of the "unresolved extension", comparing
externally and internally maintained diagnostics under matched resources
against out-of-catalog change, is this design. Not run; nothing changes.

## Note of 2026-11-12: an adaptation to a record-keeping team, and a theory for its fourth capability, from "luria experiment design"

A41 and A43 of the exchange "luria experiment design" (2026-11-10, https://chatgpt.com/share/6af35bfc-35f8-83e9-a63d-d594703eabda) propose to adapt this case to a team of agents
that keeps its inquiry in a governed record ([CASE-255](CASE-255.md)), and describe
it accurately as "Active, but it describes an unexecuted study—not an
established result". A43 credits this case with the matched-first-stage
branch and the separation of internal from external restoration, and
adds sham lesions: "Otherwise the correct strategy is simply to assume
sabotage after every perturbation." A41's example of what the fourth
capability guards against: "a team may improve its research throughput by
dropping expensive independent source verification. Its immediate task
score rises, but its ability to recognize future errors deteriorates."

A50 §6 and A51 offer Woods's graceful extensibility ([LIT-2287](../literature.d/LIT-2287.md), unread) as
the theory of what this case measures, separating "Robustness", "Adaptive
recovery" and "Graceful extensibility". The case is unchanged.

## Note of 2026-11-12: Moerman et al., Boult et al. and DARPA, read

Read on 2026-11-12 among the works of the exchange "luria experiment design"; each reading's NOTE and THEORY hold the detail.

**A correction.** The note of 2026-11-12 above gives A's three-way split,
"Robustness", "Adaptive recovery" and "Graceful extensibility", as Woods's
([LIT-2287](../literature.d/LIT-2287.md)). [LIT-2287](../literature.d/LIT-2287.md) could not be read; Moerman, Schraagen, Braaksma and van
Dongen ([THEORY-1750](../theory.d/THEORY-1750.md)), read in its place, report Woods's 2015 four senses
of resilience: "rebound, robustness, graceful extensibility, and
architectures for sustained adaptability". "Adaptive recovery" is not
among them; rebound is the nearest. The split is A's, not Woods's, and what
this case measures is better set against the four senses: its first
correction is rebound, its second correction after injury to the
diagnostic machinery is closest to graceful extensibility, and the
arrangements it compares are candidate architectures for sustained
adaptability. The paper also supplies vocabulary for what the second failure
tests, decompensation and mis-calibration of a system's own capacity, and
leaves the case's question open.

- **Boult et al.** ([THEORY-1755](../theory.d/THEORY-1755.md)): supports the premise of a regime that
  leaves the hypothesis family. An agent with a closed family treats such a
  regime as a closed-set classifier treats an unknown, assigning it to a
  known class, possibly confidently; "unknowns need not appear to be
  uncertain".
- **DARPA** ([THEORY-1766](../theory.d/THEORY-1766.md)): SAIL-ON's detect, characterize, adapt and
  update steps are a parallel decomposition to the case's separation of
  evidence generation, admission and scoring; it has no data.
- Chen, Zhu and Zheng, Srikanth et al. and Zelikman et al. do not damage the
  diagnostic machinery; nothing read tests the second correction.

The case is unchanged.
