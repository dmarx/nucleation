---
status: Read
paper: 'LIT-tmpesz2r'
title: 'An Active Inference Approach to Modeling Structure Learning: Concept Learning as an Example Case'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read in full from the Frontiers open-access PDF (24 pages): all
    sections, figure legends, Table 1, the software note and the
    reference list. Table 1's cell values were recovered from the text
    layer, which had lost the bolding. The supplementary Matlab script was
    not run. Results the paper takes from earlier active-inference work
    (Friston et al. 2017a,b) are taken as it reports them.
date: '2026-10-03'
summary: >-
  A partially observed MDP with spare hidden-state slots learns new
  animal concepts without feedback, refines coarse categories into fine
  ones, and generalises to an unseen animal in one shot. Bayesian model
  reduction on the learned state prior resets unneeded slots: right in
  45–80% of runs for 4–7 true concepts, rarely for 2–3, and always when
  the likelihood is given.
---

# NOTE-tmpxaqo4: An Active Inference Approach to Modeling Structure Learning: Concept Learning as an Example Case

## Contribution

The paper gives active inference a template for structure learning that
uses only its existing machinery. "Expansion" is inference plus Dirichlet
learning into pre-allocated hidden-state levels with uninformative
likelihoods. "Reduction" is Bayesian model reduction applied to the
learned prior over states. It demonstrates both on a toy concept-learning
task, shows one-shot generalisation, and derives neural and dopaminergic
predictions from the active-inference process theory.

## Key insight

A model does not need a separate mechanism to decide that something new
exists. If it carries a few blank hypotheses that predict every
observation equally, a pattern that none of its learned hypotheses fits
will be better explained by a blank one, and learning will then shape it.
What it does need is a way to give back blanks it filled for no good
reason. Asking whether a simpler prior over states would have had more
evidence does that, after the fact, without refitting.

## Assumptions

- **Generative model** (Figs. 1, 3): one hidden-state factor of up to eight
  animals (four birds, four fish) and one factor for the agent's report;
  three outcome modalities with two values each (size, colour,
  wings/gills); identity B for the animal factor; two time points (observe,
  report).
- **Learning**: Dirichlet concentration parameters on A (the likelihood) and,
  for the reduction runs, on D (the prior over initial states), accumulated
  as co-occurrence counts.
- **Unsupervised exposure**: during learning, reporting policies are
  disabled, so there is no feedback. Preferences C favour correct specific
  reports over correct general ones, and disfavour incorrect ones.
- **Symmetry breaking**: Gaussian noise of variance 0.001 is added to flat
  columns (footnote 3), because exactly equal Dirichlet updates could
  otherwise stall learning.
- **Reduced models** for BMR: priors over states in which the concepts to be
  removed are made less likely than those retained.

## Key results

- **Recognition baselines.** With a fully precise A, 32 trials gave 100%
  correct specific reports. With only wings/gills known, 100% correct
  general reports and no specific ones.
- **Adding one concept (sturgeon), Fig. 4.** From a flat sturgeon column and
  2,000 unsupervised exposures, reporting reached 100% after about 50
  exposures to all eight animals, stable over eight runs. Two new concepts:
  mean accuracy 98.75% (SD 2%) after 2,000 trials. Four new birds: six of
  eight runs reached 92.50–98.8%, two stalled at 72.50% by
  overgeneralising (parrot taken for hawk). New concepts often landed in
  different columns from the generative process, as unsupervised learning
  allows.
- **No duplicate states, Fig. 5.** With seven concepts known and one spare,
  80 trials of known animals left the spare unused, and 20 trials of hawk
  engaged and filled it. The same held with six, five or four known.
- **Granularity, Fig. 6.** From basic categories only: 93–98% in seven of
  eight runs, one failure at 84.4% (pigeon and parakeet merged into "small
  birds"). From nothing: mean 81.21% (SD 6.39%, range 68.80–91.30%).
- **Reduction, Table 1** (100 runs each, 250 exposures per presented
  animal; "Retain k" is the winning reduced model):
  - 7 presented: retained 8 in 5 runs, 7 in 56, 6 in 31, 5 in 8.
  - 6 presented: 8 in 4, 7 in 18, 6 in 69, 5 in 8, 2 in 1.
  - 5 presented: 7 in 4, 6 in 16, 5 in 80.
  - 4 presented: 7 in 2, 6 in 23, 5 in 30, 4 in 45.
  - 3 presented: 6 in 10, 4 in 1, 2 in 89. The true model was second-best
    in 55 runs.
  - 2 presented: 5 in 57, 4 in 43.
  Where the winner was wrong, it usually learned a coarser concept ("large
  bird"), and the log-evidence gap to the second-best was small (mean
  −0.40 to −1.23, and −1.64 for three animals). With A given and only D
  learned, the correct reduced model won in 100% of runs.
- **One-shot generalisation, Fig. 8.** Asked "could this be seen from a
  distance?" (yes only for large and colourful animals), the agent with
  parrot unknown answered yes in 20 of 20 trials, and with minnow unknown
  answered no in 20 of 20, with learning disabled.
- **Neural predictions, Fig. 9.** Simulated firing rates of the
  "parakeet" population rise over learning while the other bird
  populations fall below baseline. Simulated phasic dopamine (changes in
  policy precision) rises as confidence in specific reports grows, after
  an early dip when general and specific reports compete.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Spare hidden-state levels with flat likelihoods let an active-inference agent acquire new concepts without feedback, and only when a stimulus is novel | moderate: shown in one toy domain, repeated over 8 runs per condition | Figs. 4–5 |
| C2 | Learning basic categories first improves later learning of subordinate ones | weak to moderate: two conditions, 8 runs each, one feature space | Fig. 6 |
| C3 | Bayesian model reduction on the learned state prior can remove unneeded concepts | moderate for 4–7 true concepts (45–80%), fails for 2–3; perfect only with a given likelihood | Table 1, Fig. 7 |
| C4 | Reduction failures come from imperfect likelihood learning | weak: inferred from the given-A control, not isolated further | p. 14 |
| C5 | The agent generalises one-shot to an unseen animal | weak: two variants, 20 trials each, a hand-built question that is a conjunction of two learned features | Fig. 8 |
| C6 | The brain holds "reserve" cortical columns or silent synapses that play the role of spare slots | weak: a prediction; the authors say no direct evidence for unused columns exists | Potential Advantages section |
| C7 | Sleep and rest implement the reduction step | weak: cited theory (Hobson & Friston 2012; Tononi & Cirelli 2014), not tested | Discussion |

## Method

Belief updating by variational message passing in SPM's spm_MDP_VB_X.m.
Learning accumulates Dirichlet counts in A (and D in the reduction runs).
After learning, BMR compares the posterior D counts with the full prior
(flat over eight) and with reduced priors that drop subsets of concepts
(Fig. 2, lower left: ΔF from beta functions of prior and posterior counts),
and the reduced model with most evidence is selected. Generalisation runs
swap the report factor for a yes/no answer.

## Concepts

- **effective state-space expansion**: engaging a previously unused level
  of a hidden-state factor. The formal dimension of the state space does
  not change.
- **spare capacity / reserve states / open slots**: hidden-state levels
  whose likelihood columns start (near-)flat.
- **structural prior**: the built-in upper bound on how many hidden causes
  there may be (here eight).
- **model reduction (here)**: BMR on D, licensing a reset of A and D for the
  dropped levels.

## Connections

- **Bayesian model reduction ([LIT-tmpbgf7s](../literature.d/LIT-tmpbgf7s.md))** is cited for the post hoc
  model optimisation, and its Dirichlet form is what is applied.
- **Friston & Penny ([LIT-tmpuhjzx](../literature.d/LIT-tmpuhjzx.md))** is cited as the origin of BMR.
- **Non-parametric Bayes** (Chinese restaurant and Indian buffet
  processes; the paper calls the first the "Chinese Room" process) is the
  stated alternative. The paper frames its scheme as a bounded version,
  and argues it is more biologically plausible because it uses only
  Hebbian-style count updates.
- **Category-learning models** (Anderson's rational model, SUSTAIN, ART,
  ALCOVE, EBRW, DIVA) are discussed as related, without quantitative
  comparison.
- **Sophisticated Inference ([LIT-577](../literature.d/LIT-577.md))** shares the MDP formalism and
  expected-free-energy policy selection. This paper uses only two time
  points, so planning depth plays no role.

## Bearing on the record

- It would be one source for a THEORY that structure learning in a bounded
  generative model can be done as inference into spare capacity plus
  evidence-based pruning. Table 1 is also the record's only measurement of
  how often BMR picks the generating structure when the parent model was
  itself learned. That number is far from perfect.
- It bears on `cognition` as a formal account of category formation, and
  on the Raja et al. critique ([LIT-598](../literature.d/LIT-598.md)): the structure the agent "learns"
  is bounded by slots and features the modeller supplied.
- **No ML instruction.** Nothing here belongs in the anthology.

## Limitations

- **Scale.** Eight concepts, six binary features, two time points. The
  authors call it deliberately simple and leave scaling untested.
- **Variance across initialisations.** Table 1 is from one initialisation
  of the symmetry-breaking noise. The authors report that other
  initialisations changed the pattern, which they call "some sensitivity to
  initial conditions".
- **Expansion is not model comparison.** New slots are engaged by state
  inference, not scored by evidence. Only removal uses BMR.
- **No empirical data.** The neural predictions are simulated from the
  process theory and have not been tested.
- **Citation slip.** BMR is described as generalising "the Savage Dickie
  ratio", with Cornish & Littenberg (2007) as the citation.

## Open questions

- How should the number of slots and the feature dimensions themselves be
  learned? The authors name this and propose merging states with similar
  likelihoods by BMR, as future work.
- Does reduction improve if likelihood learning is allowed to settle before
  the prior over states is learned? The given-A control suggests it would.
- How should an agent choose actions that maximise information gain about
  the structure of its own model? The authors pose this and do not answer
  it.

## Corrections

- none (there was no seed)
