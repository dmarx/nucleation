---
number: 446
status: Read
formerly:
- NOTE-tmp3indo
paper: LIT-585
title: 'The Expected Value of Control: An Integrative Theory of Anterior Cingulate Cortex Function'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read in full: the PMC accepted manuscript (PMC3767969), sections 1-8 and
    the captions of Figures 1-4. The retrieved text drops Equations 1-3 and
    strips author names from most citations. The equations are described
    from the prose, and cited studies are named only where the text names
    them (Dosenbach and colleagues; Frank and colleagues; Holroyd and Yeung;
    Kaping and colleagues; Venkatraman and colleagues; Koechlin; Sheth et
    al.; Rothé and colleagues; Craig). The reviewed empirical findings are
    taken as the review reports them.
date: '2026-10-03'
summary: >-
  The paper proposes that dACC estimates the expected value of control:
  probability-weighted payoff of a control signal minus an intrinsic cost
  rising with its intensity. dACC uses that estimate to specify the identity
  and intensity of the control signal, which lPFC and subcortical structures
  (STN, LC) implement. The account unifies conflict monitoring, reward and
  prediction-error responses, effort costs and the override of defaults. It
  is a synthesis without a fitted model, and it leaves open how EVC is
  computed and what the cost function is.
---
<!-- inactive-ok-file: THEORY-070 — Proposed; named as the THEORY filed for this note's candidate, nothing here rests on it -->
<!-- inactive-ok-file: LIT-600 THEORY-029 THEORY-056 — Proposed theories and Deferred seeds, named as accounts this reading bears on; written from the lint report -->

# NOTE-446: The Expected Value of Control: An Integrative Theory of Anterior Cingulate Cortex Function

## Contribution

dACC had been credited with conflict monitoring, error detection, reward and
pain processing, action selection and motivation. This paper fits these
into one function: deciding whether, where and how much cognitive control to
allocate, by comparing the expected value of candidate control signals. Its
novelty, by its own account, is not "the novelty of its individual
ingredients" but their formal integration.

## Key insight

Separate *deciding on* control from *exerting* it, and treat control as
costly. Then everything that informs the decision (conflict, errors, pain,
reward, surprise, effort) should engage the decider, and the decider's output
should be a signal saying how much control is worth buying for which task.
This predicts dACC activity that rises with both difficulty and stakes, and
apathy when the decider is damaged.

## Assumptions

- **Control signals have an identity and an intensity.** Identity is the
  parameter targeted (task set, threshold, attention template). Intensity is
  how far that parameter is displaced from its default.
- **EVC (Eq. 1, described).** The sum over outcomes of Pr(outcome | signal,
  state) × Value(outcome), minus Cost(signal). Value (Eq. 2) is immediate
  reward plus γ times the maximum EVC available from the outcome state, so it
  is recursive like a reinforcement-learning value. The optimal signal (Eq. 3)
  maximizes EVC.
- **Cost is a monotonic function of intensity** ("although for a richer
  model, see" a cited alternative). The cost is intrinsic: it is "like
  physical effort, mental effort is assumed to carry intrinsic disutility".
- **Specification and regulation are distinct functions**, assigned to
  different structures. Monitoring is likewise distinct from valuation.
- **Cognitive control signals are analogous to motor control signals**, so
  they undergo "a similar process of optimization". The paper calls this an
  "implicit assumption".

## Key results

The paper reviews evidence and maps it onto the model. It reports no new
data.

- **Monitoring of state** (§4.1). dACC responds to response conflict across
  many tasks. Single units in patients awaiting cingulotomy fire with
  conflict. The paper also cites dACC differentiation of rules and task
  sets, as information relevant to which signal to specify.
- **Monitoring of outcomes** (§4.2). dACC responds to negative outcomes
  (pain, errors, loss, social rejection) and to positive ones, and carries
  signed and unsigned prediction errors (FRN, ERN). On the EVC view, dACC
  should respond selectively to control-relevant outcomes. Its responses fall
  as control demands decline with practice.
- **Specification of identity** (§5.1). dACC neurons encode the value and the
  target of saccades and of covert attention. Rule-selective theta activity
  predicts which rule will be used and is absent before errors. Stimulating
  dACC sped antisaccades. Rostral dACC lesions impair set-shifting.
- **Specification of intensity** (§5.2). dACC activity predicts post-error
  adjustments and the engagement of task-relevant regions. Cingulotomy
  abolished the behavioural conflict-adaptation effect (Fig. 3B).
- **Default override** (§5.3). The paper cites dACC engagement in decisions
  to explore and to forage. dACC-lesioned rats forage less while other
  habitual behaviour is normal. Patient intertemporal choices recruit
  control-related regions including dACC.
- **Cost** (§6).
  - Greater dACC response during a demanding task predicted a smaller
    later accumbens response to the payment for it.
  - dACC activity predicted choosing to forgo a search, and later avoidance
    of the task.
  - dACC tracked both trial difficulty and block-level incentive (Fig. 4).
- **Division of labour** (§7). dACC task selectivity leads lPFC after a
  switch and lags it with repetition. Transient dACC high-gamma precedes
  sustained lPFC activity during search. Under STN deep-brain stimulation,
  the link between dACC conflict signals and slower, more accurate responses
  was lost.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Control allocation is a cost-benefit decision over the identity and intensity of control signals | moderate as a framework: behavioural evidence for effort costs and for incentive-sensitive control is reviewed; the formal model is not fitted | §§1.3, 2, 6 |
| C2 | dACC monitors control-relevant state and outcome information | strong for responsiveness (many cited studies); "control-relevance" selectivity is "not well-tested" | §4 |
| C3 | dACC specifies control signals, and lPFC and subcortical structures implement them | moderate: dissociations are reported but "not definitive", and some argue dACC also regulates | §§5, 7 |
| C4 | Exerting control carries an intrinsic cost that scales with intensity | moderate: avoidance and effort-discounting findings | §§1.3, 6 |
| C5 | Exploration, foraging and patient intertemporal choice are cases of default override requiring control | argued, with dACC findings for each | §5.3 |
| C6 | dACC output is a willingness-to-pay signal in the currency of control | interpretive | §6 |

## Concepts

- **cognitive control**: "the set of mechanisms required to pursue a goal,
  especially when distraction and/or strong (e.g., habitual) competing
  responses must be overcome". Later, "the set of mechanisms responsible for
  configuring behavior in order to maximize the attainment of reward".
- **regulation / specification / monitoring**: implementing a control signal
  / choosing it / detecting what the choice needs.
- **expected value of control (EVC)**: "the net value associated with
  allocating control to a given task".
- **default override**: performing a task "less automatic than the default
  behavior in that circumstance".

## Connections

- **Daw, Niv and Dayan ([LIT-580](../literature.d/LIT-580.md), [NOTE-459](NOTE-459.md))** named ACC as a
  candidate arbitrator between controllers. EVC makes dACC the decider of
  control in general, and its formalism is a value function of the same
  kind ("generalizes what is referred to as a Q-value").
- **Botvinick, Niv and Barto ([LIT-581](../literature.d/LIT-581.md), [NOTE-451](NOTE-451.md)).** EVC "does not
  speak directly to the issue of hierarchical organization of control". It
  cites HRL-motivated accounts of dACC (Holroyd and Yeung), and the
  anterior-to-posterior gradient of abstraction in dACC and lPFC, as
  neighbours, not parts of the model.
- **Norman and Shallice ([LIT-600](../literature.d/LIT-600.md)).** The controlled/automatic
  distinction and the supervisory override of habitual responses that EVC
  formalizes descend from that tradition. The paper's text as retrieved does
  not name them, and the 1986 chapter was not read.
- **Frijda ([LIT-540](../literature.d/LIT-540.md)).** Frijda holds that impulse control is mostly one
  emotional readiness checking another, "an alternative" to dual-process
  models with a reflective controller. EVC is a dual-process model of the
  kind Frijda rejects, though its controller is a value-maximizer, not
  "reason".

## Bearing on the record

- **[THEORY-056](../theory.d/THEORY-056.md).** EVC is the strongest account in the record of a distinct
  control system. It does not posit a regulator of a different kind from
  what it regulates. Its decider weighs value, like the motive states
  themselves. But it does posit a dedicated structure, and a dedicated
  computation, that decides how much control to apply and to which task.
  Two readings follow:
  - On the theory's own terms ("a distinct system that does the work
    generally would" refute it), EVC is a candidate refuter. It applies only
    if EVC's specification extends to emotion regulation, which the paper
    asserts (control signals include "modulators of emotion") but does not
    show.
  - The theory's promote_when asks whether effortless regulation by a
    competing emotion works "without recruiting the control networks that
    deliberate regulation recruits". EVC says what those networks compute,
    which makes the test sharper.

  The EVC account is now filed as [THEORY-070](../theory.d/THEORY-070.md). It declares no rivalry
  with [THEORY-056](../theory.d/THEORY-056.md): the collision is conditional on EVC's specification
  governing emotion regulation generally, and the test is the one
  [THEORY-056](../theory.d/THEORY-056.md) already names.
- **[THEORY-029](../theory.d/THEORY-029.md).** Not touched. EVC is about how much control, not whose.
- **Self-determination theory.** EVC's intrinsic cost of control sits
  uneasily with SDT's claim that autonomous regulation is less depleting
  than controlled regulation ([LIT-560](../literature.d/LIT-560.md), as read in [NOTE-441](NOTE-441.md): "true choice
  was not depleting"). EVC has one cost function of intensity, with no term
  for whether the regulation is endorsed. Neither text addresses the other.
- **No ML instruction.** Nothing here belongs in the anthology.

## Limitations

- **A synthesis, not a test.** The model is stated, not fitted or simulated,
  and its predictions are matched to existing findings case by case.
- **Specification and regulation are hard to separate.** The paper says so,
  given the "tight coupling" and fMRI's temporal resolution. Single-unit and
  fMRI conflict-adaptation results point in opposite directions (Fig. 3C–D).
- **The cost function is unspecified**: "what exact form does the cost
  function assume?"
- **How EVC is computed or approximated** is left open, as is the cost of
  computing it.
- **Homology** between human dACC and rodent or macaque regions "remain[s]
  ambiguous".

## Open questions

- Is the cost of control intrinsic, or a proxy for opportunity cost? The
  paper treats it as intrinsic.
- How are candidate control signals learned in the first place?
- Does dACC specify emotion-regulatory signals in the way it specifies task
  sets? This would bear directly on [THEORY-056](../theory.d/THEORY-056.md).
