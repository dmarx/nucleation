---
status: Read
paper: 'LIT-tmpjrcmk'
title: 'Jiang & Lucas — Actively learning to learn causal relationships'
version: 1
history:
- version: 1
  date: '2026-11-04'
  note: >-
    Read in full on 2026-11-04 from the publisher's open-access PDF, 26
    pages, CC BY 4.0
    (https://link.springer.com/content/pdf/10.1007/s42113-023-00195-0.pdf),
    text extracted by pdftotext. Read: the abstract, introduction, the
    model (Eqs. 1–9 and the ablations), Experiments 1 and 2, the
    discussion, conclusion and declarations. Not read: the supplementary
    Appendices A and B (further match × length analyses, the Experiment 2
    judgment results, the replication of Fig. 10 with unnormalized
    information gains, the instructions), which were not fetched; Fig. 8's
    per-model counts, given only in the figure. Skimmed: the references.
    The extraction prints the gain of the deterministic forms in Table 1
    as "1", almost certainly ∞.
date: '2026-11-04'
summary: >-
  A model of active learning to learn: a hierarchical Bayesian learner
  over causal structures and functional forms, which carries its beliefs
  about form between tasks and chooses interventions by a weighted sum of
  information gain about form and about structure. Two preregistered
  online blicket experiments. Averaged over participants, the model
  without transfer predicts interventions slightly better than the full
  model; per participant, the full model is best for the largest group,
  and its fitted weights mostly favour form information. Fixed-form and
  structure-only learners barely beat random.
---
<!-- inactive-ok-file: THEORY-tmpbgkfv CLAIM-446 THEORY-484 THEORY-070 THEORY-359 CASE-165 LIT-1675 — Proposed, Unfetched or new; cited from the reading of Jiang & Lucas (2024) as open -->

# NOTE-tmpm6c07: Jiang & Lucas — Actively learning to learn causal relationships

## Contribution

Models of active causal learning chose interventions to maximize expected
information gain (EIG) about the structure of one isolated problem;
models of overhypothesis transfer in causal learning were passive. This
paper joins them. Its learner holds a joint posterior over structures and
functional forms, carries the posterior over forms into the next task,
and values information about both. The authors claim it is "the first to
capture the idea that people can strike a balance between overhypothesis
and causal structure learning". Fitting the weight w on form information
makes valuing information about overhypotheses a measurable quantity, per
participant, conditioned on each participant's own history of
interventions.

## Key insight

When a learner faces a series of related problems, an intervention is
worth something for what it says about the problem at hand and for what
it says about the kind of problem; a learner who expects more such
problems may give up some of the first for the second. Three hypotheses
follow, each tested against an ablation: people represent rich
overhypotheses (against Fixed-Form, one deterministic disjunctive form),
transfer them (against No-Transfer, the prior reset each task), and trade
structure information for form information (against Structure-Only-EIG,
w = 0).

## Assumptions

- **The theory space.** Blickets are exchangeable, generative causes;
  activation is a monotone sigmoid in the number present, after Lucas &
  Griffiths (2010), LIT-tmpzamp4, on a 20 × 20 grid of bias b ∈ [0, 2.85]
  and gain γ ∈ [0, 38], extended to "3-conjunctive" forms. No preventive,
  continuous or subtype causes.
- **Priors.** Uniform over structures at the start of every task; only
  the marginal over forms transfers. The form prior is one of 24
  gamma-based joint priors favouring disjunctive, near-deterministic
  forms, marginalized uniformly.
- **Choice.** Softmax with temperature t over cEIG(q) = w·EIG_F(q) +
  (1−w)·EIG_S(q), each EIG min-max normalized. An approximation: "This
  equation is only equivalent to joint information gain when form (F) and
  structure (S) are independent conditional on interventions and
  outcomes, which, here, they are not."
- **Samples.** MTurk, paid $1.28–1.50 plus a bonus; no feedback on which
  blocks were blickets between tasks.

## Key results

- **Abstract.** "In two active “blicket detector” experiments with 14
  between-subjects manipulations, our model was supported by both
  qualitative patterns in participant behavior and an individual
  differences-based model comparison."
- **Experiment 1, first intervention (N = 212; 8 conditions).** "The mean
  number of blocks in the first intervention was significantly higher
  after conjunctive training (short and long) than after disjunctive
  training (short and long)" (t(183.39) = 4.62, p < .001).
- **Experiment 1, accuracy.** On the disjunctive transfer task, matched
  training beat mismatched as trends in the full data (p = .051, .078),
  significant only after filtering for engagement (N = 181; p = .035,
  .017). "In the conjunctive transfer conditions, however, the difference
  between matched (conjunctive training) and mismatched (disjunctive
  training) accuracies was non-significant."
- **Experiment 2, group level (N = 250; cross-validated predictive
  likelihood of each intervention).** "The No-Transfer ablation model had
  the highest mean predictive likelihood" (.059 ± .002), the full model
  close behind (.055 ± .003); Fixed-Form and Structure-Only-EIG .018,
  random .016. The authors attribute No-Transfer's lead to its more
  diffuse prior.
- **Experiment 2, per participant.** "our full model was the best
  predictor for the highest number of participants", No-Transfer second.
  The two hypotheses both keep (rich forms, seeking form information)
  "were required to predict the majority (73.6%) of participants’
  interventions".
- **Weights (Fig. 10, participants best fit by the full model).** "81.63%
  of fits have overhypothesis weight > 0.5", and "45.41% of fits have an
  overhypothesis weight of 1"; the authors add that "it is unlikely that
  participants do not care about learning causal structures at all."
- **Scope.** The authors "do not argue that people choose Bayes-optimal
  interventions in general and for arbitrarily complex problems".

## Concepts

- **Overhypothesis** (after Kemp et al. 2007 and Goodman 1955): an abstract
  belief about causal relationships that spans situations and constrains
  learning within each; here the functional form, which can be lifted out
  of a task, while the structure belongs to the task.
- **Active learning**: the learner chooses actions to gather its own
  information, rather than observing a fixed set.
- **Functional form**: how causes combine; here a blicket threshold (1, 2
  or 3) and an activation probability at threshold (1 or .75).
- **EIG** (Eq. 7): the expected reduction in entropy of forms or of
  structures from an intervention, averaged over outcomes.
- **Positive testing**: choosing interventions expected to activate the
  detector, to confirm a single form; the low-effort alternative.

## Connections

It extends Lucas & Griffiths (2010), LIT-tmpzamp4, read the same day,
from passive to active learning, and Kemp, Perfors & Tenenbaum's
overhypotheses to intervention choice. Its EIG is the Bayesian design
criterion that goes back to Lindley (LIT-1675) and is reviewed by
Chaloner & Verdinelli (LIT-1525, NOTE-1161); a weighted sum of two
marginal gains is a non-standard utility by that review's lights. Its
explanation of No-Transfer and random-like participants as low-effort
strategies is in the resource-rational vein of LIT-1071 and THEORY-359,
but it fits no cost model. Epistemic value in active inference (LIT-577)
is a rival framing of information seeking that it does not discuss.

## Bearing on the record

- **A's characterization.** A's sentence "In two active causal-learning
  experiments involving 14 between-subjects manipulations, the researchers
  found behavioral patterns consistent with this hierarchical account.
  Model comparisons also provided support using individual differences."
  is A's paraphrase of the abstract, not a sentence of the paper. A's
  attribution, "Jiang & Lucas (2024)", is right, and its account of the
  two levels of information and of the move from passive to active
  learning is accurate. Qualifications:
  - **Thin on the model comparison.** Averaged over participants the
    No-Transfer ablation beat the full model (.059 against .055); support
    for transfer rests on the per-participant count, where the full model
    was the largest group, not stated to be a majority.
  - **Overstated on behaviour.** Experiment 1's conjunctive transfer task
    showed no match effect, and the disjunctive match effects were trends
    until the data were filtered (181 of 212).
  - **Left out.** The w > 0.5 finding, the paper's evidence for giving up
    structure information, with its caveats (45% of fits at w = 1;
    normalized gains); and that Fixed-Form and Structure-Only-EIG barely
    beat random, the paper's strongest result, which supports rich forms
    and form-seeking more firmly than transfer.
- **QUESTION-276**: unrelated in subject; the method is analogous
  (inference to an abstract level shared across problems), neither
  supporting nor qualifying it.
- **CASE-165, LIT-1542**: unrelated; the theory space is a fixed parametric
  grid, not nonparametric.
- **THEORY-484**: unrelated; the paper sets meta-reinforcement learning
  aside as a rival family on sample efficiency and tests nothing about
  options.
- **THEORY-070**: unrelated, a loose echo: low-effort strategies are
  invoked, no control cost is modelled.
- **QUESTION-325, CLAIM-446**: unrelated in subject. Under a conjunctive
  world, single-block interventions are uninformative, since every
  hypothesis predicts no activation: a policy under which the hypotheses
  predict the same observation, the mechanism CLAIM-446 invokes for
  avoidance, here without threat or affect. It neither supports nor
  qualifies either.
- **LIT-563 / NOTE-466 (HDDM)**: the pooling sense of "hierarchical". The
  paper's argument that an averaged model may not capture any individual
  motivates hierarchical estimation, but Jiang and Lucas fit each
  individual separately, without pooling.
- Filed: THEORY-tmpbgkfv.
- No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- **The authors' own.** The sigmoid space excludes preventive and
  continuous causes; Bayes-optimality is not claimed for complex
  problems; process-level models are future work; the cEIG decomposition
  is an approximation; the fits at w = 1 are probably not literal.
- **Transfer is the weakest of the three hypotheses.** At the group level
  the model without transfer wins; the per-participant count rests on 20
  interventions each, in 4 folds, with two parameters (t, w) fit per
  person over a grid.
- **Experiment 1.** No match effect on the conjunctive transfer task;
  several effects significant only after the engagement filter (at least 9
  interventions).
- **Samples.** MTurk with performance-independent base pay; the authors
  attribute random-like and positive-testing behaviour to low motivation.
- **Scale.** Normalized EIGs make w scale-dependent; the unnormalized
  replication is in Appendix A, not read.
- **One target form.** The transfer task of Experiment 2 was always
  conjunctive.
