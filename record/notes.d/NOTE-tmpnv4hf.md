---
status: Read
paper: 'LIT-tmphd2wq'
title: 'Baker et al. — Rational quantitative attribution of beliefs, desires and percepts'
version: 1
history:
- version: 1
  date: '2026-11-04'
  note: >-
    Read in full on 2026-11-04 from the publisher's typeset PDF of the
    version of record, 10 pages, posted on the lab site of the third
    author, Rebecca Saxe,
    https://saxelab.mit.edu/wp-content/uploads/2018/11/Baker.etal_.2017.pdf,
    found by web search and also listed on the CBMM (MIT) publication page;
    the publisher's page was not fetched, and the article is not open
    access there. Text extracted with pdftotext. Read: abstract,
    introduction, Computational models, Results (Experiments 1 and 2),
    Figures 1–7 and captions, Discussion, Methods (modelling, both
    experiments, statistics), data and code availability and author
    contributions; reference list scanned. Not read: the Supplementary
    Information, which is not in this PDF and holds the full model, the
    belief and desire priors, the alternative models' definitions and all
    scenarios, and the data and code at https://github.com/clbaker/BToM.
    Page numbers below are the article's.
date: '2026-11-04'
summary: >-
  An observer that inverts a model of an agent as an approximately rational
  planner, perceiving by line of sight and updating its beliefs, predicts
  adults' graded desire and belief ratings in 73 food-truck scenarios
  (r_BSCV 0.91 and 0.78) and their inferences of hidden world states from a
  search path (0.91), better than versions without belief uncertainty or
  action cost. A motion-feature heuristic tied on Experiment 1 beliefs, and
  the desire fit is between scenario types only. The paper never calls the
  model hierarchical; that is A's label.
---
<!-- inactive-ok-file: THEORY-538 THEORY-596 THEORY-tmpc5lgz — Proposed or new; cited from the reading of Baker et al. (2017) as open -->

# NOTE-tmpnv4hf: Baker et al. — Rational quantitative attribution of beliefs, desires and percepts

## Contribution

Earlier inverse-planning models (MDP-based) inferred goals or desires from
action in a fully observed world. Here perception, belief updating and
planning are all in the agent model, so belief, desire and percept
attributions are coupled, and the earlier models are special cases. The
paper tests this quantitatively over many parametrically varied scenarios,
with lesioned models showing that each component matters, also for the
judgements it does not directly represent, and on a second task the model
was not built for. It states its scope as a computational-level claim.

## Key insight

Beliefs have three causal roles: they are joint effects of percepts and
prior beliefs, and causes of action. So "beliefs can be inferred forward
from inferences about an agent's percepts and priors, or backward from an
agent's observed actions (and inferred desires), or jointly", and an
observer who models all three can do each. Remove one component and the
others suffer: lesioned models "show a deficit not only in the missing
representations, but also in the remaining mental state inferences with
which they are causally entwined." (p. 7).

## Assumptions

- **The agent is approximately rational**: efficient planning toward
  constant desires, a constant cost per step, softmax choice with β fitted
  to participants (2.5 in Experiment 1, 1.5 in Experiment 2).
- **Perception** is the 360° isovist; belief update is Bayesian.
- **Hypothesis spaces are fixed in advance**: beliefs and desires on
  discrete, approximately uniform grids; world states enumerated
  logically. No hyperprior; nothing learned across scenarios, and agents
  were varied in colour and name so participants would not generalize
  between them.
- **Desires are fixed within an episode**; beliefs change with percepts.
- **Non-recursive**: in I-POMDP terms the observer is a Level-1 model of a
  Level-0 agent; no beliefs about beliefs.
- **Exclusions**: five of 78 Experiment 1 scenarios "were not consistent
  with an assumption of rational agency" and were left out of analysis.

## Key results

- **The claim (abstract).** "The model accurately captures the quantitative
  mental-state judgements of human participants in two experiments".
- **Experiment 1 (pp. 4–5).** 16 analysed participants, 73 scenarios: a
  student seeking one of three food trucks, one parking spot hidden behind a
  building; ratings of desire for each truck and of initial belief about the
  hidden spot. r_BSCV over all scenarios 0.91 (desire) and 0.78 (belief);
  0.97 and 0.91 averaged within the seven scenario types.
- **The desire caveat (p. 5).** "BToM predictions at the individual
  scenario level showed no partial correlation with human judgements after
  controlling for scenario type" (partial r = 0.066); belief predictions did
  vary usefully within type (partial r = 0.28).
- **Lesions (p. 5).** TrueBelief and NoCost fit desires less well (0.72,
  0.75), and "neither TrueBelief nor NoCost could predict belief judgements
  at all" (−0.022, 0.10).
- **The cue-based rival (p. 5).** "The motion-based heuristic was able to
  predict belief inferences as well as BToM" (0.77 against 0.78), did worst
  on desires (0.62), and was "qualitatively poorly calibrated".
- **Experiment 2 (p. 6).** 176 online participants inferred where three
  food carts were from the search path of an agent with stated preferences.
  "Our BToM model was not developed to account for such social inferences",
  yet BToM reached r_BSCV = 0.91, while "the motion-based heuristic
  correlates only weakly with human judgements" (0.61); TrueBelief 0.63,
  NoCost 0.46.
- **Scope (pp. 7–8).** Joint inference is "a computational-level claim";
  "Developing such an algorithmic account of BToM inferences and testing it
  on a more general set of stimuli and inferences is an important direction
  for future work." And "The POMDP formulation that we adopt here is at best
  only a first approximation to the true agent model in core mentalizing".
- **The closing claim (p. 8).** People may assume others rational where they
  are not, so "intuitive theories of minds — if not always actual human
  minds — are rational to the core."

## Concepts

- **Mentalizing**: "explaining an agent's behaviour in terms of their
  mental states."
- **Core mentalizing**: mentalizing "grounded in perception, action and the
  physical world", about agents moving toward or acting on nearby objects;
  "core" refers to early-emerging representations of space, objects as
  goals and efficient action, not to innate core knowledge.
- **Model-based against cue-based**: an intuitive generative theory "of how
  mental states cause actions — which gets inverted", against "a direct
  mapping from low-level sensory inputs to high-level mental states via
  statistical associations".
- **Joint inference**: "representing a joint hypothesis space of the
  agent's beliefs and desires, such that in explaining a complete action
  sequence, the observer's posterior distributions over the agent's beliefs
  and desires are coupled".
- **Fit statistic**: r_BSCV, the bootstrap cross-validated correlation over
  100,000 train/test splits of scenarios.

## Connections

It extends the authors' MDP-based inverse planning (Baker, Saxe and
Tenenbaum 2009, not held) to partial observability, and places the observer
within the interactive POMDP framework as a non-recursive model. It
contrasts itself with cue-based accounts of action understanding and
mentions deep networks as a possible stronger cue-based rival, untested.

## Bearing on the record

- **A's characterization (synthesis, section 2).** Right: a generative
  model of an agent whose actions depend on beliefs, desires, percepts and
  planning; inference from observed action; two experiments; quantitative
  prediction; the lesioned models did worse. Four corrections.
  - **"Hierarchical" is A's label, not the paper's.** The paper never calls
    BToM hierarchical. Its belief and desire priors are fixed grids with no
    hyperprior, and nothing is learned across scenarios. The only
    hierarchies it names are the I-POMDP "hierarchy of levels" and "the
    Marr hierarchy of levels of explanation", neither a hierarchical prior.
    It fits A's section 2 only as a layered generative model, not A's
    section 1 sense of shared higher-level knowledge.
  - **Not only backward.** Beliefs are inferred forward from percepts,
    backward from actions, or jointly, and Experiment 2 infers the world
    state too.
  - **The quotation is A's.** "Across two experiments, the Bayesian
    theory-of-mind model predicted people's quantitative judgments and
    outperformed simpler models lacking specific mental-state components"
    is A's paraphrase of the abstract, not in the paper.
  - **Partly wrong on the rivals.** True of the lesioned models. The
    motion heuristic is not a lesioned model, is not obviously simpler (10
    fitted weights in Experiment 1 and 48 in Experiment 2, against one β),
    and tied with BToM on Experiment 1 beliefs. A also omits that the desire
    fit is between scenario types only, that only adults were tested, and
    the sample sizes.
- **[THEORY-538](../theory.d/THEORY-538.md) (Dennett: a system believes and desires when predictable as
  a rational agent).** Qualifies. BToM is a quantitative model of how
  observers ascribe beliefs and desires by assuming approximately rational
  action, the stance's method. But it predicts observers' judgements, not
  agents' behaviour, and the agents were scripted paths, so it is not the
  measured case [THEORY-538](../theory.d/THEORY-538.md)'s promote_when asks for. Its contrast with a
  motion heuristic is the closest the record holds.
- **[THEORY-596](../theory.d/THEORY-596.md) (Dennett: ascription assumes rationality and mostly true
  beliefs; the believer is an idealisation).** Supports, with a
  qualification: BToM ascribes specific false beliefs within a rationality
  assumption, its softmax β is a fitted version of the slack, and the
  closing "rational to the core" claim about intuitive theories, not actual
  minds, is close to [THEORY-596](../theory.d/THEORY-596.md)'s idealisation clause.
- **[LIT-911](../literature.d/LIT-911.md) (Orseau, McGill & Legg, Agents and Devices).** Related in
  method: Bayesian inversion of a goal-directed model of a gridworld mover.
  [LIT-911](../literature.d/LIT-911.md) asks agent or device; BToM assumes an agent and infers its mental
  states.
- **[THEORY-636](../theory.d/THEORY-636.md) (Quillien: judgements of wanting predict intentionality
  judgements).** Neighbouring work on folk attribution of desire;
  consistent with, not tested by, this paper.
- **[QUESTION-276](../questions.d/QUESTION-276.md).** Related only by analogy, as inference of latent states
  from behaviour; BToM fixes its hypothesis spaces in advance, which is what
  the question wants to avoid.
- **[CASE-153](../cases.d/CASE-153.md) (the self-protecting sentry).** Formal kin only: a POMDP-style
  hidden world. The one point of contact is that BToM yields
  information-seeking as "implicit epistemic goals" inside an instrumental
  plan.
- Filed: [THEORY-tmpc5lgz](../theory.d/THEORY-tmpc5lgz.md). No instruction for machine-learning practice;
  nothing for the anthology.

## Limitations

- **Adults only**, though the motivation is developmental; the authors call
  the developmental mapping "an open question".
- **Toy domains**: grid-worlds with two or three goals and a handful of
  enumerated world states; no recursive beliefs, explicit epistemic goals or
  multi-agent interaction (all named as future work).
- **Computational level only**; exact joint inference "could be intractable
  for more complex settings".
- **Weak within-type fits**: desire predictions carry no information within
  scenario type, and belief fits are lower (0.78).
- **Small Experiment 1 sample** (n = 16), with five irrational-looking
  scenarios excluded.
- **One cue-based rival**, a linear motion-feature model, which matched BToM
  on Experiment 1 beliefs; no stronger learned model was tested.
- **Rationality**: the expected-utility framing sits against evidence of
  non-optimal planning; the authors argue spatial navigation is a domain
  where people may plan efficiently.

## Open questions

- Does BToM beat a cue-based model fitted to the same training judgements
  on new, held-out scenarios with parameters fixed in advance, for beliefs
  and desires together?
- Would a hierarchical version, with priors over agents' desires learned
  across agents, predict how people generalize between agents? The paper
  deliberately prevented such generalization.
