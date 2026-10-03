---
number: 454
status: Read
formerly:
- NOTE-tmpcfvk8
paper: LIT-577
title: 'Sophisticated Inference'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read in full as prose: the arXiv v1 PDF, all sections, figure captions,
    footnotes, appendix and references. The displayed equations were
    unreadable in the text layer and were not recovered from images, so no
    equation is reproduced below and claims about the recursion rest on the
    prose that states it. The simulation code (SPM's DEM demos) was not run.
date: '2026-10-03'
summary: >-
  Expected free energy evaluated recursively over the beliefs an agent
  would hold after each plausible outcome turns active inference into a
  pruned tree search over belief states, formally analogous to Bellman
  recursion. Small simulations show it planning through short-term costs
  (an aversive cue; a maze barrier needing horizon four) and exploring by
  novelty. Its scalability is argued from pruning, not demonstrated; its
  first-principles grounding is cited, not developed.
---
<!-- inactive-ok-file: THEORY-045 — Proposed; named because its source LIT-542 is the record's other active-inference holding, not leaned on -->

# NOTE-454: Sophisticated Inference

## Contribution

Active inference had scored a small, pre-specified set of policies by
expected free energy, which does not scale and considers only beliefs about
consequences, not consequences for beliefs. The paper defines a recursive
expected free energy that evaluates each next action by the beliefs the
agent would have after each plausible outcome, so that planning searches
sequences of belief states. It also surveys which established objectives
(expected utility, KL control, optimal Bayesian design, active learning,
curiosity, empowerment, the information bottleneck) appear as special cases
when terms of expected free energy are dropped.

## Key insight

An unsophisticated agent values a cue because looking at it resolves
uncertainty. A sophisticated agent values it because, after looking, it
will know what to do, and it adds the low expected free energy of that
informed next move. Following that through recursively is a tree search,
and because beliefs, not samples, are propagated, implausible branches can
be cut early.

## Assumptions

- **Discrete-state POMDP generative models** with likelihood A, transitions B
  (action-dependent), preferences C as log prior costs, initial-state prior
  D, Dirichlet hyperparameters for learning.
- **Actions conditionally independent across time** (policies as priors over
  action transitions relaxed), so states and actions are Markovian and belief
  propagation (a forward filtering pass) suffices.
- **Every action allowed from every state** (named in the Discussion as a
  strong assumption).
- **Pruning thresholds:** predictive probabilities below 1/16 are not
  expanded.
- **Exact rather than variational inference** in the belief-propagation
  scheme: "no mean-field approximations"; the Kronecker product of hidden
  factors is used to keep inference exact (footnote 12).
- **Deterministic action selection** (maximum a posteriori) in all
  simulations.

## Key results

- **Recursive expected free energy (Eq. 1.11, stated in prose).** The
  expected free energy of a next action is its risk plus ambiguity plus the
  average, over predicted outcomes and then over subsequent actions, of the
  expected free energy of subsequent actions. A softmax of the accumulated
  average gives the empirical prior over the next action.
- **Bellman analogy.** Same recursive logic; the scheme deals in functionals
  of belief distributions, Bellman in functions of states. Recovers
  Bayes-adaptive RL "in the zero temperature limit" (Introduction).
- **T-maze (32 trials, two moves each, 95% cue validity, C = −2/+2 for
  reward/punishment).** Horizon two: confident epistemic visits to the cue,
  switching to exploitation at trial 16. Horizon one: less confident,
  switches at trial 10. Bayesian risk only: stays or wanders, sometimes
  learns nothing. With the cue given cost 1: sophisticated agent still
  forages, switches at trial 12; one-step agent never leaves the centre.
- **Maze (8 × 8, five actions, costs −1/+1).** Horizons one to three get
  stuck behind the aversive barrier nearest the target; horizon four finds
  the shortest path in eight moves.
- **Novelty.** With Dirichlet priors on the likelihood set to 1/64 and no
  location preference, 64 moves cover nearly every location; a
  Bayesian-risk agent returns to the start and stays. With preferences
  reinstated, four exposures of eight moves suffice to learn and execute the
  shortest path.
- **Cost.** Of about 10¹⁰ (horizon four) or 10¹⁵ (horizon six) potential
  paths, "usually several hundred" are evaluated, in "a few hundred
  milliseconds on a personal computer".
- **Appendix lemmas.** Generalised free energy upper-bounds Bayesian risk
  under priors favouring precise likelihoods (Bayes optimality lemma); a
  Gibbs-energy form of policy surprisal yields a nonequilibrium steady state
  (steady-state lemma); corollaries cast active inference, empowerment,
  information bottleneck, self-organisation and self-evidencing as special
  cases or limits.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Recursive expected free energy implements a deep tree search over belief states | strong as a construction | definition, Eq. (1.11) |
| C2 | Sophisticated agents plan through short-term costs where one-step agents cannot | moderate | T-maze with aversive cue; maze horizon sweep; deterministic single runs |
| C3 | Probability-based pruning makes deep search tractable | weak to moderate | operation counts for one maze; scaling to larger problems argued, not shown |
| C4 | Expected free energy subsumes expected utility, KL control, optimal design, curiosity, empowerment and the information bottleneck as special cases | moderate | appendix derivations and Figure 1, read in prose only |
| C5 | Sophisticated inference recovers Bayes-adaptive RL at zero temperature | moderate | stated in the Introduction; not derived in detail |
| C6 | The account rests on first principles from nonequilibrium steady-state physics | weak here | cited to Friston 2013 and 2019, not developed |

## Concepts

- **Sophistication.** Having beliefs about one's own (future) beliefs; from
  game theory's levels of reasoning.
- **Expected free energy.** Risk (divergence of predicted from preferred
  outcomes or states) plus ambiguity (expected conditional entropy of
  outcomes given states); equivalently extrinsic value plus intrinsic
  (epistemic) value.
- **Salience and novelty.** Information gain about hidden states, and about
  model parameters.
- **Epistemic affordance.** The information gain a location or action
  offers.

## Connections

It descends from Friston et al. 2017's process theory (whose Appendix 6
first drew the sophisticated/unsophisticated distinction) and from Kaplan &
Friston 2018's maze, here solved without a graph-Laplacian prior. It places
itself beside Bayes-adaptive RL (Åström, Duff, Ross et al.) and amortized
deep active inference (Ueltzhöffer, Millidge, Çatal, Tschantz). It cites
[LIT-526](../literature.d/LIT-526.md) for its physical grounding. The critiques filed with it, Bruineberg
et al. ([LIT-603](../literature.d/LIT-603.md)) and Raja et al. ([LIT-598](../literature.d/LIT-598.md)), are aimed at that
grounding and at active inference's generative models generally.

## Bearing on the record

- **Anthology candidate.** A planning algorithm with an RL analogue and
  simulated environments; see the LIT for the boundary reasoning.
- **Raja et al.'s critique ([LIT-598](../literature.d/LIT-598.md))** that active inference
  presupposes perception and action applies directly: the rat is given the
  task's A, B, C, D, its location is observed, and moves are primitive.
- **Intrinsic motivation.** The identification of information gain with
  intrinsic motivation (citing Ryan & Deci 1985) is by name; the record's
  SDT holdings ([LIT-558](../literature.d/LIT-558.md), [LIT-559](../literature.d/LIT-559.md)) define intrinsic motivation otherwise.
  No THEORY bears.
- **[THEORY-045](../theory.d/THEORY-045.md)** (Proposed) draws on active inference through [LIT-542](../literature.d/LIT-542.md); this
  paper adds nothing on affect.
- No THEORY filed; one was declined, because the results are properties of
  a construction plus illustrations.

## Limitations

- Toy problems only, by the authors' own account ("rather trivial
  problems"); scaling is argued from factorisation and sparsity.
- All simulations are single deterministic runs; no variance, no
  comparison with an RL planner on the same tasks.
- The equivalences in the appendix are stated with the steady-state and
  precision assumptions of the generative model; their force as
  "first-principle" derivations depends on the critiques' targets.

## Open questions

- Does the pruned recursion scale to problems where many outcomes stay
  plausible, where the 1/16 threshold no longer cuts the tree?
- How does it compare, on the same tasks, with Bayes-adaptive Monte Carlo
  planners?
