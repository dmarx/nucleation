---
status: 'Read'
paper: 'LIT-990'
title: 'Watson — Agency, Goal-Directed Behavior, and Part-Whole Relationships'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the publisher's open-access PDF (CC BY 4.0) at
    link.springer.com/content/pdf/10.1007/s13752-023-00447-z.pdf, text
    extracted with pdftotext: every page (Biological Theory 19:22–36),
    both boxes, the captions of both figures, the five footnotes and the
    reference list. The figures are diagrams. Fig. 2 is adapted from
    Watson et al. (2011a), and its plotted trajectories were not
    recoverable from the text layer. The essay has no theorems and
    reports no new results; the models it leans on are in the cited
    papers, which were not read.
date: '2026-10-14'
summary: >-
  A comparative, scale-relative notion of agency. Given a decomposition
  into parts with goals of their own, a whole is more agential than its
  parts when its organization lets them resolve more of their mutual
  constraints than they would at the equilibrium of the old organization.
  It shows this as delayed gratification. The essay argues this, and shows
  in cited models that unsupervised, bottom-up learning can produce such
  organization. It gives no threshold for an additional agent and no
  formula beyond comparing total frustration.
---
<!-- inactive-ok-file: QUESTION-009 — Deferred; the question this work was filed for, on a set-aside line -->
<!-- inactive-ok-file: QUESTION-032 CLAIM-170 CLAIM-174 CLAIM-168 CLAIM-172 — Open or Proposed; the question, answers and objection this reading bears on, open -->
<!-- inactive-ok-file: CLAIM-010 — Rejected; cited as the permissiveness objection any account must meet, not as standing -->

# NOTE-tmpo6vec: Watson — Agency, Goal-Directed Behavior, and Part-Whole Relationships

## Contribution

The essay asks when a whole is more of an agent than its parts, not whether
something is an agent. It answers in dynamical-systems terms. A whole is
more agential when its internal organization makes the parts better at
satisfying their own goals than they could be under the organization it
had before. It then argues, from earlier models by the author and
co-workers, that such organization can arise without design, from
unsupervised learning by self-interested parts. It ends that "the agent
creates itself".

## Key insight

Agency at one level is measured in the currency of the level below. A
system's energy function, its actual dynamics, can differ from the
objective function given by the frustrated constraints among its parts.
When the dynamics take the parts to configurations that satisfy more of
those constraints than the obvious local equilibrium does, the whole is
goal-directed with respect to its parts. Sometimes they do this by going
uphill in the short term. "Even if the goals of the parts were defined
arbitrarily, goal-directed behavior can be quantified objectively at the
system level given the goals of the parts."

## Assumptions

- **Mechanism granted.** "We will suppose (without prejudice) that a system
  admits a mechanistic account in principle." No vitalist line is drawn:
  "we avoid trying to identify any vitalist criterion that categorically
  distinguishes between agential and non-agential … systems in absolute
  terms."
- **A given decomposition into parts with goals.** The norm for the whole
  is the parts' norm. The author calls this "robbing Peter to pay Paul",
  and accepts that "agency of the organism can be different or absent if
  we define the agency of the parts differently". The result is "sensitive
  to different ways of defining its subagents".
- **Agency depends on what is observed.** It "depends on what variables
  are observed and which are not", with internal variables
  screened off from external ones.
- **Behaviour as local descent on a landscape** of constraints among parts,
  after Fields and Levin (2022). Frustration is the set of unresolved
  constraints.
- **Low-order constraints for the learning mechanism.** "[I]f the
  constraints are low order (e.g., pairwise), there will be a positive
  correlation between the quality of a solution and the size of its basin
  of attraction." The Hebbian mechanism's improvement relies on this.

## Key results

The essay proves nothing new. Its results are definitions, a worked
example, and reports of earlier models.

- **The comparative criterion.** "If a system at a higher level of
  organization causes the parts it contains to do what they 'normally do'
  but more, as if the complex constraints between them (that would have
  otherwise prevented this) were alleviated, then that system is agential
  (with respect to its parts)." Stated bottom-up: "a system of parts is
  agential if they are able to acquire organized relationships among
  themselves that exhibit goal-directed behavior greater than that which
  they exhibit as individuals."
- **The measure.** Agency is evaluated "by comparing the total frustration
  or energy of the system at local equilibria given some original
  organization of the parts to that obtained with some new organization
  of the parts." No formula or scale is given beyond this.
- **Goal-directedness as delayed gratification.** For a system to beat a
  local optimum, "the energy function (describing the dynamics of the
  system) must be different from the objective function (describing the
  quality of solutions to the problem)". A system "goes uphill in a
  specific direction that leads to lower points in the long term. It knows
  which way to go." Stochastic escape does not count.
- **The low end.** A ball with momentum "can find better optima compared
  to a ball without momentum (in some environments)". Minimal agency
  "still skates very close to no agency at all". A system whose internal
  state makes its parts do better "is not at zero on the agency scale".
- **Under-determination (Box 1, Fig. 1).** In a two-hidden-unit network for
  XOR, either hidden unit can compute any of the 8 functions sensitive to
  both inputs, and the network still classifies all four samples
  correctly. Two zero-error networks "only agree on half of the feature
  space". So correct behaviour "tells us absolutely nothing about what any
  of its components computes".
- **Non-decomposable history (Box 2).** Hidden-unit roles settle by a
  symmetry-breaking phase in which "the roles of h1 and h2 mutually define
  one another". The resulting organization fixes generalization, and it
  "depends intimately on the history of the system, the whole system, and
  nothing but the system".
- **Learning to be an agent (reported from Watson et al. 2011a, c).** A
  Hopfield-type network is shocked between attractors and its weights are
  changed by Hebbian learning. It enlarges the basins it visits most,
  which tend to be the better solutions, and so "finds the high-quality
  solutions more often" with respect to its original constraints. This
  needs no teacher or reward.
- **Nonneural cases (reported).**
  - Utility-maximizing agents that adjust their relationships reach
    equilibria that "are actually better solutions to those original
    constraints" (Davies et al. 2011).
  - Ecological networks do the same with "no population of ecosystems or
    group-level selection" (Power et al. 2015).
  - Learned timing dependencies pick out subsets of agents to "work
    together", rescaling the search to "a state space over emergent groups
    of variables" (Tissot et al. 2023, under submission).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | A whole's agency can be compared with its parts' by how far its organization resolves the parts' mutual constraints | moderate | definition and argument, with the many-balls illustration |
| C2 | Goal-directed behaviour is going uphill in a specific direction to reach better optima, which requires dynamics that differ from the objective | moderate | argument from the ball-on-a-landscape example |
| C3 | Correct behaviour under-determines component organization, and the organization fixes generalization | strong | worked XOR example, Box 1 and Fig. 1 |
| C4 | A system's organization can depend on its history as a whole, not decomposably on its parts' histories | moderate | symmetry-breaking argument, Box 2 |
| C5 | Unsupervised, bottom-up learning among self-interested parts can produce organization that makes the whole more agential | moderate | reported from cited models (Watson et al. 2011a, c; Davies et al. 2011; Power et al. 2015), not shown here |
| C6 | Problem-solving competence of this kind is a fundamental feature of all organisms | weak | appeal to Levin's experimental programme and Fields and Levin (2022) |

## Concepts

- **Frustration (stress).** The state in which some parts' constraints are
  resolved and others are "unresolved, or in tension". A configuration's
  quality is how many constraints it resolves, or its total energy or
  stress.
- **Energy function against objective function.** The function the system
  actually descends, including internal variables, against the function
  that scores solutions to the parts' constraints.
- **Agential with respect to its parts.** A relative predicate. It holds
  when the whole's organization makes the parts "do better at what they
  normally do" than a disorganized arrangement would.
- **Self-modelling dynamical system.** A dynamical system "with a behavior
  that is augmented by a model of its own past behavior", acquired by
  Hebbian change to its connections.
- **Conservative against innovative organization.** The first holds on to
  good states already visited. The second also promotes good states never
  visited, which is generalization.

## Connections

The essay appears in a Biological Theory thematic section on concepts of
agency, beside Okasha (2023), whose "intelligent agent" sense it adopts. It
builds on Fields and Levin (2022) for observer dependence and "patience".
Its own lineage is Watson's evolutionary connectionism (Watson et al.
2011a–c, 2016; Watson and Szathmáry 2016; Kounios et al. 2016). It
contrasts itself with Friston's free energy: its information "makes its
parts less frustrated … rather than … minimizes surprise". It ties the
account to the major transitions in individuality (Szathmáry and Maynard
Smith 1995; Watson, Levin and Buckley 2022).

## Bearing on the record

- **For [QUESTION-009](../questions.d/QUESTION-009.md): a comparative criterion, not a threshold.** The LIT
  files it as "a candidate criterion for when coordinated parts constitute
  a further agent". The essay does give a criterion. Coordination counts
  when it lets the parts resolve more of their mutual constraints than
  they would without it. But the criterion says when a whole is *more
  agential than its parts*, not when there is an additional agent. It
  declines any absolute line "regardless of whether the parts, or the
  system as a whole, are considered to pass some absolute threshold". Read
  as an answer to [QUESTION-009](../questions.d/QUESTION-009.md), it changes the question rather than
  answering it.
- **The LIT summary says more than the essay.** It says the notion "needs …
  distributed knowledge acquired by changing the organization of the
  parts". The abstract says it "can involve" such knowledge. In the body,
  learned origin is an optional restriction: "Perhaps we might want to
  restrict a definition to systems that are able to acquire an internal
  organization". The question of whether designed organization counts is
  left open. "Quantifiable" means only the comparison of total frustration
  at equilibria. The essay computes no quantity of its own.
- **For [QUESTION-032](../questions.d/QUESTION-032.md) and [CLAIM-170](../claims.d/CLAIM-170.md).** The account is explicitly
  level-relative and decomposition-relative. Agency is "sensitive to
  different ways of defining its subagents", and the organism's agency
  "can be different or absent if we define the agency of the parts
  differently". This agrees with [CLAIM-170](../claims.d/CLAIM-170.md)'s factorization relative to
  a level. It does not supply [QUESTION-032](../questions.d/QUESTION-032.md)'s test for which factors are
  agents, because it takes the parts' goals as given.
- **For [CLAIM-168](../claims.d/CLAIM-168.md), the circularity objection.** Watson avoids presupposing
  a goal for the whole: "without presupposing that this is an aim for the
  system or, indeed, that the system is (already) an agent". He does so by
  presupposing goals for the parts. The presupposition moves down a level
  and is not removed. That is the same shape as [CLAIM-174](../claims.d/CLAIM-174.md)'s reply, which
  takes candidates' boundaries from the threshold criterion and not from
  agency.
- **For [CLAIM-174](../claims.d/CLAIM-174.md).** Delayed gratification gives test (2) a behavioural
  mark: excursions uphill in the objective that reach lower minima, in a
  specific rather than a random direction. The Hebbian mechanism is an
  instance of test (3), a policy that changes with the consequences
  experienced.
- **For [CLAIM-010](../claims.d/CLAIM-010.md), the permissiveness objection.** Watson bites the bullet at
  the low end: a ball with momentum is barely, but not zero, agential.
  Because the account is comparative, the bullet costs little. The
  thermostat ([CASE-044](../cases.d/CASE-044.md)) is not discussed. On this account it would need a
  decomposition into frustrated parts before the question arose.
- **For [CLAIM-172](../claims.d/CLAIM-172.md).** The Tissot et al. result, reported second-hand, has
  learned relationships act on the timing of subagents' actions. They
  pick out groups that "work together" and move the search to "a state
  space over emergent groups of variables". That is close to
  [CLAIM-172](../claims.d/CLAIM-172.md)'s collective variable carried by mutual entrainment. The source
  was under submission and is not held here.
- No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- The essay is a perspective piece. Its new material is conceptual. Every
  model-based result is reported from earlier papers, and none is
  re-derived or measured here.
- The measure needs a stipulated decomposition and stipulated goals for
  the parts. The author concedes these can be "defined arbitrarily". The
  essay offers no way to choose among decompositions.
- The comparison is between two organizations of the same parts. It does
  not say what the baseline "disorganized" organization is in a real
  organism.
- The Hebbian result depends on low-order constraints and on the
  correlation between basin size and solution quality, which need not
  hold in general.
- The biological examples in the Discussion (regeneration, xenobot-like
  "skin cell clusters") are cited to Levin's work and not connected to the
  measure.

## Open questions

- Is there a principled choice of parts, or does every decomposition give
  its own agency ranking? A result showing the ranking stable across
  reasonable decompositions would make the measure usable as a criterion.
- Does designed organization that resolves the parts' frustrations make
  an agent? The essay raises this and leaves it open.
- Can the measure be computed for a real multicellular or social system,
  where the "disorganized" equilibrium is not observed?
