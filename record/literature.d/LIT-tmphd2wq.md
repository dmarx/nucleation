---
status: Active
status_note: >-
  read in full 2026-11-04 ([NOTE-tmpnv4hf](../notes.d/NOTE-tmpnv4hf.md)) from the publisher's typeset PDF
  posted on the Saxe lab site at MIT (Rebecca Saxe is an author); worth
  reading as the quantitative test of Bayesian theory of mind: an observer
  that inverts a model of the agent as an approximately rational planner
  with line-of-sight perception and Bayesian belief updating predicts
  adults' graded desire, belief and world-state judgements (r_BSCV 0.91 in
  both experiments) better than versions without uncertain beliefs or
  without action cost. Its limits: toy grid-worlds with fixed, enumerated
  hypothesis spaces; adults only (16 in Experiment 1, 176 online in
  Experiment 2); desire predictions carry no information within scenario
  type; a motion-feature heuristic matched it on Experiment 1 beliefs; a
  computational-level claim only. Supplementary Information not read.
title: 'Rational quantitative attribution of beliefs, desires and percepts in human mentalizing'
version: 1
history:
- version: 1
  date: '2026-11-04'
  note: >-
    Registered and read on 2026-11-04 from the owner's pasted synthesis
    "Hierarchical probabilistic models in cognitive science", written by
    another assistant (A), which cites it as Baker, Jara-Ettinger, Saxe &
    Tenenbaum (2017) in its section 2. Citation checked against Crossref
    and OpenAlex: Chris L. Baker, Julian Jara-Ettinger, Rebecca Saxe and
    Joshua B. Tenenbaum, Nature Human Behaviour 1(4), article 0064.
    Crossref gives published online 13 March 2017, which is `published:`
    and agrees with the article's "published 13 March 2017"; OpenAlex's
    publication date of 10 March 2017 is supported by no other source and
    is not used. A's authors, year and title are right (A capitalizes the
    title); the sentence A puts in quotation marks is A's paraphrase of the
    abstract. Not open access at the publisher (OpenAlex: closed). Read
    from the publisher's typeset PDF, 10 pages, posted on the lab site of
    the third author,
    https://saxelab.mit.edu/wp-content/uploads/2018/11/Baker.etal_.2017.pdf,
    found by web search and also listed on the CBMM publication page;
    extracted with pdftotext. Not read: the Supplementary Information and
    the data and code repository. Status Active.
tags:
- cognition
- probabilistic-modeling
- model-comparison
date: '2026-11-04'
published: '2017-03-13'
doi: '10.1038/s41562-017-0064'
first_author: 'Baker'
keywords:
- 'theory of mind'
- 'mentalizing'
- 'Bayesian theory of mind'
- 'inverse planning'
- 'POMDP'
- 'belief attribution'
- 'desire attribution'
implementations:
- 'https://github.com/clbaker/BToM'
summary: >-
  Baker, Jara-Ettinger, Saxe & Tenenbaum (2017). Bayesian theory of mind
  (BToM): the observer models an agent in a small spatial world as a
  partially observable planner that sees what is in its line of sight,
  updates its beliefs by Bayes' rule and acts approximately rationally
  (softmax over expected utility minus a cost per step), and inverts that
  model to infer the agent's beliefs, desires and percepts jointly from its
  path. Across 73 food-truck scenarios (16 participants) it predicts desire
  and belief ratings (r_BSCV 0.91 and 0.78 over scenarios), and on a task
  it was not built for, inferring hidden cart locations from a search path
  (176 online participants), r_BSCV 0.91. Versions without belief
  uncertainty or action cost do worse; a motion-feature heuristic matched
  it on Experiment 1 beliefs but not on desires or Experiment 2. The paper
  never calls the model hierarchical; that is A's label.
---
<!-- inactive-ok-file: THEORY-538 THEORY-596 THEORY-tmpc5lgz — Proposed or new; cited from the reading of Baker et al. (2017) as open -->

# LIT-tmphd2wq: Rational quantitative attribution of beliefs, desires and percepts in human mentalizing

Baker, C. L., Jara-Ettinger, J., Saxe, R. & Tenenbaum, J. B. (2017). Rational quantitative attribution of beliefs, desires and percepts in human mentalizing. *Nature Human Behaviour* 1(4): 0064. doi:10.1038/s41562-017-0064.

## Key takeaways

*From the reading, [NOTE-tmpnv4hf](../notes.d/NOTE-tmpnv4hf.md). Page numbers are the journal's.*

- **Joint inversion.** "Here we present a model of core mentalizing
  computations: inferring jointly an actor's beliefs, desires and percepts
  from how they move in the local spatial environment." (abstract)
- **Lesions.** Without belief uncertainty (TrueBelief) or action cost
  (NoCost) desire fits fall to 0.72 and 0.75, and "neither TrueBelief nor
  NoCost could predict belief judgements at all" (p. 5).
- **Generalization.** "Our BToM model was not developed to account for such
  social inferences", yet it predicts Experiment 2's world-state judgements
  at r_BSCV = 0.91, against 0.61 for the motion heuristic (p. 6).
- **Where it ties.** "The motion-based heuristic was able to predict belief
  inferences as well as BToM" in Experiment 1 (0.77 against 0.78), and the
  desire fit is between scenario types only: "BToM predictions at the
  individual scenario level showed no partial correlation with human
  judgements after controlling for scenario type" (p. 5).
- **Scope.** Joint inference is "a computational-level claim" (p. 7), and
  "The POMDP formulation that we adopt here is at best only a first
  approximation to the true agent model in core mentalizing" (p. 8).

## Standing in the record

Cited in A's synthesis (section 2) as a "Hierarchical generative model" of
agents whose actions depend on beliefs, desires, percepts and planning,
inverted from actions. The generative model and the lesion results hold.
The paper never calls BToM hierarchical: its priors over beliefs and
desires are fixed grids, nothing is learned across scenarios, and the only
hierarchies it names are the I-POMDP levels and Marr's levels. And the
cue-based rival is not a simpler lesioned model; it tied on Experiment 1
beliefs.

It is the nearest held work to [LIT-911](LIT-911.md) in method (Bayesian inversion of a
goal-directed model of a gridworld mover), and a quantitative instance of
the rationality-assuming ascription that [THEORY-538](../theory.d/THEORY-538.md) and [THEORY-596](../theory.d/THEORY-596.md) take
from Dennett, though it predicts observers' judgements, not agents'
behaviour. Filed from it: [THEORY-tmpc5lgz](../theory.d/THEORY-tmpc5lgz.md).
