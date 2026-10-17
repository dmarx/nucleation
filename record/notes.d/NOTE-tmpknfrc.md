---
status: Read
paper: LIT-tmpp54zu
title: 'Sandved-Smith et al. — computational phenomenology of mental action'
version: 1
history:
- version: 1
  date: '2026-10-16'
  note: >-
    Read in full from the journal version of record as deposited in
    PubMed Central (PMC8396119, CC BY-NC), fetched as full-text XML from
    the Europe PMC REST service on 2026-10-16 and converted to text. The
    OUP PDF and the PMC PDF were refused to this client (HTTP 403). Read:
    the abstract, the Introduction (its three subsections), Methods (the
    active-inference formulation, generative models, and the formalization
    of meta-awareness and attentional control, with Eqs. 1–2), Results
    (Levels 1–3), the Discussion's two subsections, the Conclusion, the
    data-availability statement and every figure caption. The figures
    themselves (from the supplementary bundle) were not inspected, the
    linked Colab code was not run, and the supplementary file, a response
    to reviewers, was scanned only. The XML carries no page numbers, so
    quotations below are located by section.
date: '2026-10-16'
summary: >-
  A three-level discrete active-inference model in which attentional
  states set the precision of the perceptual likelihood and meta-awareness
  states set the precision of the attentional likelihood; mental action is
  a choice of 'stay' or 'switch' over attentional states, defined at the
  second level only, against a preference to observe oneself 'focused'.
  Simulations reproduce the cycle of focus, mind-wandering, noticing and
  refocusing, with longer mind-wandering under low meta-awareness. The
  stimuli are fixed by the generative process, so mental action changes
  only how strongly they update belief; the likelihoods themselves are not
  learned.
---

# NOTE-tmpknfrc: Sandved-Smith et al. — computational phenomenology of mental action

## Contribution

It gives active inference an explicit model of mental action and
meta-awareness. Earlier "parametrically deep" models (Hesp et al. 2021)
let higher-level states condition lower-level precisions. This paper
adds policy selection at the attentional level, so that the agent can
switch its own attentional state, and a third, meta-awareness level whose
states set the precision with which the agent observes its attentional
state. Its claimed novelty is control: "What is novel about our model is
the coupling of this deep inferential architecture with 'action and its
control'" (Discussion, "Expanding the model to other parameters").

## Key insight

A mental action has the same form as a bodily one, one level up. The
agent's attentional state is treated as a hidden state of a generative
process that the agent cannot see directly, that drifts on its own, and
that the agent's policy can push. The agent infers which attentional
state it is in from observations of it and from how its perceptual
beliefs are updating, and acts to bring about the outcome it prefers,
"focused". What the attentional state does at the level below is set a
precision: "There is nothing special about these states, other than they
generate outcomes at lower levels that speak—not to which state the world
is in but—to the precision of beliefs about which state the world is in"
(Methods, "Formalizing meta-awareness ...").

## Assumptions

- **Discrete-state POMDPs** with a likelihood A, transitions B,
  preferences C, initial states D, policy prior E and expected free energy
  G (Methods).
- **Attention is likelihood precision.** "In active inference,
  'attentional processes' have been formulated in terms of the precision
  (here denoted γA) of—or confidence in—the likelihood mapping (the A
  matrix; Parr and Friston 2017b)" (Methods, "Generative models"). The
  precision-weighted likelihood is A with each element raised to γA and
  renormalized (Fig. 2 caption).
- **Purely parametric levels.** "higher-level state factors are only
  those that condition precisions of the level below" (Introduction).
- **Two levels per factor.** Perceptual: standard or deviant. Attentional:
  focused or distracted. Meta-awareness: high or low (Fig. 6 caption).
  Focused and distracted set γ to 2.0 and 0.5 (β = 0.5 and 2.0; Methods,
  after Eq. 1).
- **Action only at level 2.** "Action here is only defined on the second
  level, with two possible actions u(2), 'stay' and 'switch', which
  condition the attentional transition matrix B(2) as shown" (Fig. 6
  caption).
- **A fixed world.** "The generative process of this state is
  predetermined, with a deviant stimulus shown every 20th time step"
  (Results, Level 1). "Sensory habituation is not modelled here."
- **Meta-awareness set by hand.** In the Level 3 simulation it is high for
  the first half of the trial and low for the second, by design; "we could
  have let the generative model roam its meta-awareness states freely"
  (Results, Level 3).
- **No learning.** No likelihood, transition or precision hyperparameter
  is learned anywhere. The model changes its states, not its parameters.

## Key results

All results are single illustrative simulations. No statistics are
reported and no data are fitted.

- **Level 1 (Fig. 7).** A passive oddball with no action. Focused (high
  γA on A(1)) for the first half, distracted for the second. When
  focused, the agent updates its belief on the deviant immediately. When
  distracted, its beliefs are "not fully adjusted when the deviant is
  presented". Precision acts as "a 'rate constant' in evidence
  accumulation and consequent belief updating" (Results, Level 1).
- **Level 2 (Figs. 8–10).** A preference in C(2) to observe "focused".
  The generative process moves the true attentional state with a
  policy-dependent probability. The agent becomes distracted, keeps
  believing it is focused for a few steps (mind-wandering), infers
  "distracted" from higher-order observations and from ascending evidence
  about first-level precision, and selects "switch". The deviant speeds
  this up, because the prediction error it causes strengthens ascending
  evidence (Results, Level 2).
- **Level 3 (Fig. 11).** With low meta-awareness (low precision on A(2)),
  mind-wandering lasts longer. "In this example, the agent does not
  realize their mind has wandered until the contents of their perception
  changes (i.e. the oddball is presented)" (Results, Level 3).
- **Equation 1.** The posterior over attentional states combines a prior
  from B(2), ascending evidence from the first level's precision update
  (computed by Bayesian model reduction), and "perceptual evidence"
  γA(2)·ln A(2)·o(2) from a direct observation of the attentional state.
  This last term is available only when γA(2) > 0. That is the paper's
  formal line between a transparent state (inferred only from below) and
  an opaque one (also observed).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Mental action can be formalized as policy selection over higher-level states that condition lower-level likelihood precision | moderate | Methods, Figs. 4–6; a construction, shown to run |
| C2 | The focus, mind-wandering, noticing and refocusing cycle emerges from this architecture | weak | one simulation (Fig. 10), qualitative match to Lutz et al. and Hasenkamp et al. |
| C3 | Lower meta-awareness lengthens mind-wandering | weak | one simulation (Fig. 11), with meta-awareness set by hand |
| C4 | Opacity versus transparency maps onto zero versus non-zero higher-level likelihood precision | moderate | Eq. 1 and the paragraph after it; definitional |
| C5 | The scheme generalizes to precision on B, C, D, E and G | weak | asserted ("Mathematically, it is perfectly valid ..."); not implemented, by the authors' statement |

## Method

1. Level 1 POMDP over the stimulus, with likelihood A(1) raised to the
   precision γA(1).
2. Level 2 states (focused, distracted) fix γA(1) through β(f,d). Their
   own likelihood A(2) maps them to an observation o(2) of the attentional
   state. B(2) depends on the policy u(2) ∈ {stay, switch}. C(2) prefers
   "focused".
3. Level 3 states (high, low) fix γA(2) the same way.
4. Each level's state posterior combines prior, ascending precision
   evidence and its own observation (Eq. 1). Policies are scored by
   expected free energy.

## Concepts

- **Mental action.** "Goal-directed internal behaviour, without
  necessarily having a direct consequence on the external environment
  (e.g. as through muscular action). A paradigmatic example of mental
  action is covert attention" (Introduction). Formally: "the deployment
  of precision" (Methods).
- **Meta-awareness.** Third-order states that make second-order
  attentional states opaque, as attentional states make perceptual states
  opaque (Introduction, the bracketed note).
- **Opacity and transparency.** After Metzinger. A process is transparent
  when only its content is available and opaque when the process itself
  can be accessed "as data for further inference".
- **Parametric depth.** Higher levels take lower-level posterior and
  precision estimates as data (Introduction, after Hesp et al. 2021).

## Connections

It extends Hesp et al. (2021) from model precision (γG) to likelihood
precision (γA), and takes from Limanowski and Friston (2018, 2020) the
proposal that mental action is the deployment of precision. Its
attention-as-precision rests on Parr and Friston (2017; see [LIT-tmpu6g9m](../literature.d/LIT-tmpu6g9m.md)
for their 2019 review, read in [NOTE-tmpi40rc](NOTE-tmpi40rc.md)). It differs from Whyte and
Smith (2020) by having purely parametric levels and a third level. It
explicitly sets aside "the role of selective attention in epistemic
foraging" (Introduction). It does not use the term "Markov blanket".

**[CLAIM-tmp9cjyo](../claims.d/CLAIM-tmp9cjyo.md) (the counter).** The claim quotes the abstract exactly,
and its paraphrase is right in outline. Three things the reading changes.
- *Where mental action sits.* Only the attentional level has policies.
  Meta-awareness is not acted on: the third-level state is set by the
  generative process in the simulation. So "mental action selects among
  higher-level cognitive states" is true of one level, with two actions,
  "stay" and "switch".
- *It is literally action one level inward.* The paper models the agent's
  own attentional state as a generative process, "we have programmed a
  'generative process' that regulates the 'true' state transitions that
  the agent undergoes" (Results, Level 2). The agent acts on that process
  to bring about a preferred observation o(2) of itself. This is the
  action–perception cycle with the attentional state in the place of the
  world, and the claim's "one blanket inward" is a fair description of
  it. The paper's own phrase is that "there is no fundamental difference
  between a simple reflex, a series of complex movements, and a mental
  action" (Discussion).
- *No structure learning.* Nothing in this model is learned. It cannot
  support the claim's second strand, the observer reshaped without action.
  That strand rests on Smith et al. ([THEORY-564](../theory.d/THEORY-564.md)), not on this paper.

**[CLAIM-tmpq9do8](../claims.d/CLAIM-tmpq9do8.md) (the thesis).** This is exactly the line the thesis
draws, and the paper falls on the side the thesis needs at the level of
perception. At the first level the observation's content is fixed before
and independently of any mental action: the stimulus sequence is
"predetermined", with a deviant every 20th step. Mental action changes
only the precision with which that content updates belief, a "rate
constant" in evidence accumulation. The authors note that the same effect
could come from changing the entries of A(1) "in response to incoming
evidence", but they model it as a single precision applied to all
entries, not as a change to the mapping. So, at level 1, mental action does
not produce what the agent observes, or change which mapping turns causes
into observations. It changes how much the fixed observation counts. At
level 2 the picture differs. Mental action changes the true attentional
state, and so it does change the content of the observation o(2) the agent
then receives of itself. That is the synchronic form the thesis declines
to claim, and it takes the action–perception shape.
For the diachronic form, in which a judgement reshapes the observer that
produces later observations, the paper offers a weak analogue. The
attentional state persists through B(2) and conditions later perception,
so a mental act now changes how later stimuli are weighed. But it is a
two-valued gain on an unchanging likelihood, reversible and unlearned. It
changes what the observer believes, not which objects it individuates.
On the claim's own terms, the paper's
mental action is closer to action than to judgement. It targets a state
of the agent and is chosen to make a preferred observation come true,
whereas the claim says judgement targets the observer and is not chosen
for its outcome.

**[CLAIM-tmpt568z](../claims.d/CLAIM-tmpt568z.md) and [QUESTION-tmpr5tck](../questions.d/QUESTION-tmpr5tck.md).** In this model what corrects a
false belief about one's own attention is evidence not routed through
that belief. Two kinds do it: ascending precision evidence from the level
below, and the direct observation o(2). Under low meta-awareness the
correction waited for an exogenous change in the stimulus: the agent "does
not realize their mind has wandered until the contents of their
perception changes". This is a small illustration of the question's
first candidate, unselected input, doing the anchoring. Note that it is
input the agent could not select, since the stimulus schedule is fixed.
But the loop is also built to confirm a preference: the agent acts until
it observes itself "focused". Nothing in the model checks whether
"focused" is a correct reading of the world.

## Bearing on the record

- **[CLAIM-tmp9cjyo](../claims.d/CLAIM-tmp9cjyo.md)**: supports its first strand, and more literally than
  the claim states it. Mental action here is action on a modelled internal
  generative process. It qualifies the strand to one acting level, with
  precision-setting only and no learning.
- **[CLAIM-tmpq9do8](../claims.d/CLAIM-tmpq9do8.md)**: at the perceptual level, the observation is fixed
  before the mental action and only its precision changes, as the claim
  needs. At the attentional level, the mental action produces the content
  of the self-observation, and the loop has the action–perception shape.
  The paper offers no mechanism by which judgement reshapes the observer's
  likelihood.
- **[LIT-tmpp54zu](../literature.d/LIT-tmpp54zu.md)'s "Why this is here"**: its question is answered. The
  observation weighted at level 1 is fixed independently of the mental
  action.
- No instruction for machine-learning practice.

## Limitations

These are proofs of principle: single runs, hand-set parameters, and a
meta-awareness schedule imposed from outside. There is no fit to
behavioural, phenomenological or neural data, which the authors leave to
future work. The generalization to other precisions is stated, not built.
The equations are given for the attentional level only. The perceptual
task is a passive oddball, so overt action is never combined with mental
action in a simulation, although the Discussion says the framework allows
it.

## Open questions

- With the meta-awareness level left free and given its own policies,
  does the model still settle, or does it lock in a preferred
  self-observation? The authors chose not to run this for clarity.
- If A(1) were learned (Dirichlet counts) while attention fluctuated,
  would a habit of attention leave a lasting change in the likelihood?
  That would be the diachronic reshaping [CLAIM-tmpq9do8](../claims.d/CLAIM-tmpq9do8.md) needs, and this
  paper does not test it.
