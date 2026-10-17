---
number: 960
status: Read
formerly:
- NOTE-tmpo4u0r
paper: LIT-1181
title: 'Friston et al. — action and behavior: a free-energy formulation'
version: 1
history:
- version: 1
  date: '2026-10-16'
  note: >-
    Read from the publisher's open-access PDF
    (link.springer.com/content/pdf/10.1007/s00422-010-0364-z.pdf, fetched
    2026-10-16; 34 PDF pages, journal pp. 227–260, CC BY-NC), extracted with
    pdftotext. The prose of every section was read: abstract, the boxed
    summary, §1, §2 with §§2.1–2.3, §3 with §§3.1–3.2, §4 (oculomotor
    control, §§4.1.1–4.1.3; sensorimotor integration, §4.2), §5 (mountain
    car, §§5.1–5.4), §6, §7 with §§7.1–7.6, §8, and Appendices 1–3 in
    prose. Figure captions were read. Equations 1–9 were followed as far as
    the argument needs (the entropy bound, the ergodic step, the three forms
    of free energy, the gradient descent on action); the simulation
    equations (11, 13–18) and Appendix 2–3 algebra were not checked. The
    reference list was scanned. Page numbers are the journal's.
date: '2026-10-16'
summary: >-
  Existence is taken to require a low-entropy ensemble density; an ergodic
  assumption turns that entropy into time-averaged surprise, and because
  the setup stipulates that action is the only way an agent changes the
  hidden states it senses, action as well as perception must minimize a
  free-energy bound on surprise. Action enters nowhere in the generative
  model: it is a gradient descent that fulfils proprioceptive and visual
  predictions, and in simulations of eye, arm, mountain-car and Lorenz
  movements it cancels unexpected perturbations so they are not
  perceived. The paper fixes the model and re-samples the data, and
  answers the worry that this confirms a wrong model by appeal to
  existence: agents without the right priors cannot exist.
---

# NOTE-960: Friston et al. — action and behavior: a free-energy formulation

## Contribution

It extends the free-energy account of perception to action. Earlier work
had perception minimize a free-energy bound on sensory surprise by
changing internal states. This paper lets action minimize the same bound
by changing what is sensed, derives a single gradient-descent scheme in
which action suppresses precision-weighted sensory prediction error, and
shows by simulation that reflexes, tracking, cued reaching and
goal-directed movement learned without reward all fall out of prior
expectations. Its headline for motor control: "there are no top-down
motor commands; just prior expectations about proprioceptive input that
are fulfilled at the spinal level, given a compliant environment and
motor plant" (p. 235).

## Key insight

Perception and action minimize one quantity from two sides: "perception
tries to suppress prediction error by adjusting expectations to furnish
better predictions of signals, while action tries to fulfil these
predictions by changing those signals" (p. 234). So to move is to expect
the sensations of having moved: "we only have to expect the sensory
consequences of a movement to make it happen" (p. 240). The model is held
fixed and the data are re-sampled to fit it: "The free-energy principle
turns this optimization around and considers that the model (agent) is
fixed and the aim is to minimize surprise by re-sampling the data"
(p. 232).

## Assumptions

- **Existence as low entropy.** Adaptive agents "must occupy a limited
  repertoire of physical states" (p. 229); the ensemble density on their
  states must have low entropy (p. 230).
- **Ergodicity.** The ensemble density is at equilibrium and so "can be
  interpreted as the proportion of time a single agent entertains these
  states (the sojourn time)" (p. 230). Then sensory entropy is the long-run
  time average of surprise (Eq. 3).
- **A sensory mapping of uniformly high sensitivity.** Hidden-state
  entropy is bounded by sensory entropy plus a term in ln|∂g/∂x̃| (Eq. 1).
  "For simplicity, we will assume that this sensitivity is uniformly high
  over the ranges of states considered" (p. 230), so minimizing sensory
  entropy suffices. Appendix 1 adds that the mapping must be
  diffeomorphic.
- **Action is the only route to hidden states, and the mapping is out of
  reach.** "It is this policy that resists the increasing entropy of
  hidden states, because the only way that the agent can change hidden
  states is through action" (p. 230). "Note that agents cannot minimize
  sensory entropy by switching off sensory channels; they can only act by
  changing hidden states, not the sensory mapping per se" (p. 230).
  Appendix 1 concedes that, through nonlinearities, "changing some hidden
  states will affect the sensory mapping of others (e.g., closing ones
  eyes)" (p. 256).
- **Action is peripheral and outside the model.** a(t) encodes
  "peripheral motor control signals" (p. 230); "the generative model has
  no notion of action; it just produces predictions that action tries to
  fulfill" (p. 233). The derivative of sensation with respect to action
  is taken from the true generative process in the simulations (p. 254).
- **Gaussian fluctuations, mean-field and Laplace approximations**, so
  free energy reduces to a sum of precision-weighted squared prediction
  errors (Eq. 9); generalized coordinates truncated at sixth order
  (p. 229).
- **The right priors.** "Put simply, the free-energy formulation assumes
  that agents have the right priors. This assumption cannot be violated,
  because agents who do not have the right priors cannot exist" (p. 256).

The setting is continuous-state, single-agent, with hand-specified or
supervised priors. There are no discrete policies, no expected free energy
and no epistemic value: the later apparatus of active inference is absent.

## Key results

- **The argument for action (§2).** From Eq. 1–3, minimizing sensory
  entropy means one "needs to minimize surprise at all times" (p. 230).
  Free energy F bounds surprise and can be written as energy minus
  entropy, divergence plus surprise, or complexity minus accuracy (Eq. 5).
  Perception minimizes the divergence; action can change only the
  accuracy term (p. 232). Eq. 6: μ* = arg min F and a* = arg min F. "This
  policy reduces to sampling input that is expected under the recognition
  density (i.e., sampling selectively what one expects to experience)"
  (p. 232).
- **The "ergodic arguments" (abstract, p. 227).** The abstract says
  active sampling "is mandated by ergodic arguments based on the very
  existence of adaptive agents". In the body the ergodic step is only the
  sojourn-time identity of p. 230, which turns entropy into time-averaged
  surprise. That this minimization must be done by action, and not only by
  perception, comes from the stipulation that action alone changes hidden
  states. §2.3 restates the mandate without the word: "This minimization
  is mandated by the fact that average surprise is entropy and agents must
  have a low entropy ensemble density" (p. 232). §8 says "active inference
  is mandated by population dynamics" (p. 250).
- **The dark room.** Retiring to a dark room is "a category error"
  (p. 231) because surprise is relative to the agent's class; Appendix 1:
  "sensory channels that are critical for survival should be privileged
  and cannot be occluded (e.g., nociceptive pain signals and interoception
  signaling hunger, thirst etc.)" (p. 256).
- **Oculomotor control (§4.1).** A Gabor patch on a 6 × 6 photoreceptor
  grid (36 channels); hidden states are gaze direction ("For simplicity,
  these states cause the eye to move (as opposed to the object)", p. 235);
  state and observation noise at log-precisions 4 and 8. Under flat priors
  on the perturbing force (log-precision −16), the perturbation is
  perceived and little action is emitted (Fig. 2). Under tight priors
  (log-precision 16), action mirrors the force and the excursion is
  "completely suppressed" (p. 238): the percept shrinks toward the prior
  because the prediction error "is explained away by action, and action is
  not part of the perceptual model. In other words, from the point of view
  of the agent, the target is not moving" (p. 239). With the prior and the
  true cause swapped, and four oculomotor proprioceptors in place of the
  retina, the prior alone produces a saccade away and back (Figs. 5–6).
  Doubling the motor gain (a → 2a) or adding a late perturbation leaves
  the perceived trajectory unchanged; only the amplitude of action changes
  (pp. 240–241).
- **Cued reaching (§4.2).** A two-joint arm reaches a target when it is
  bright. Proprioception at log-precision 4, vision at 8; optimized
  precisions are "almost exactly correct" in all four noise combinations,
  and reaching fails only when both modalities are noisy (p. 242).
- **Mountain car (§5).** The agent learns the dynamics of a controlled
  environment over 16 trials of 32 s. "During learning, we precluded
  active inference, such that the agent sensed the trajectory passively,
  as it left the target state and returned to it" (p. 246). Placed in the
  uncontrolled environment with learning fixed, it reproduces the
  goal-directed policy; unexpected forces "were explained away by action
  and not perceived" (p. 246). Lowering the expected precision of the
  priors gives cautious, then stereotyped, then avolitional behaviour,
  offered as a model of dopaminergic motor poverty (p. 249). Precision
  "may mediate attentional gain" in perception and in action "also
  control whether an action is emitted or not (i.e., motor intention)"
  (p. 248).
- **Lorenz trajectories (§6).** After 16 trials of 512 bins in a
  controlled Lorenz environment, the agent reproduces the attractor in an
  uncontrolled one and is "impervious to exogenous perturbations"
  (p. 250).
- **Against conventional motor control (§7).** No value function or
  Bellman equation; forward models exclude action ("Action is not part of
  inference ... because it is a known quantity; action is just there to
  explain away unexpected sensory prediction errors", p. 254); no
  efference copy is needed; "the agent does not know that the expected
  sensory trajectories are being caused by its own action" (p. 255).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | If an agent's existence requires low sensory entropy, ergodicity holds and only action changes hidden states, then action as well as perception should minimize the free-energy bound on surprise | moderate | §2, Eqs. 1–6; each premise is assumed, not derived |
| C2 | Action fulfils proprioceptive (and visual) predictions by descending on precision-weighted sensory prediction error; no separate motor command or inverse model from hidden states is needed | moderate | Eq. 9, Fig. 1, §3.1; simulations only |
| C3 | Retinal stabilization, tracking and self-generated saccades follow from priors on a perturbing force alone | moderate | §4.1, Figs. 2–6, simulations |
| C4 | Multisensory weighting for reaching follows from optimized precisions | moderate | §4.2, Figs. 8–9, simulations |
| C5 | Goal-directed and itinerant behaviour can be instilled by passive perceptual learning in a controlled environment, without reward | moderate | §§5–6, Figs. 11–15; supervised by the designed environment |
| C6 | Reduced precision of priors produces motor poverty resembling Parkinsonian or neuroleptic bradykinesia | weak | §5.3, Fig. 13, analogy |
| C7 | Agents cannot reduce surprise by shutting off sensation, since agents not surprised by its absence would not survive | weak | Appendix 1, informal argument |

## Concepts

- **Active sampling / active inference.** Action chosen to minimize free
  energy by changing sensory input so that it matches predictions. The
  paper distinguishes it from active learning, which harvests data to make
  recognition more precise (p. 232).
- **Action (lower case) and Action (capital).** a(t) is the motor signal;
  Action is the path integral of free energy (p. 232).
- **Generative process and generative model.** Eq. 7 is the world,
  which depends on action; Eq. 8 is the agent's model, which does not
  (p. 233).
- **Precision.** Inverse variance of random fluctuations; it weights
  prediction errors, may mediate attentional gain, and gates whether
  priors are expressed as action (pp. 234, 248).
- **Exogenous (causal) states.** Forces v(t) the model treats as
  autonomous causes; the paper uses priors on them to induce or cancel
  movement (p. 233).

## Connections

It builds on the free-energy account of perception (Friston et al. 2006;
Friston 2008), on variational Bayes (Hinton and van Camp, MacKay, Neal and
Hinton), and on the mountain-car simulations of Friston, Daunizeau and
Kiebel (2009). It sets itself against optimal control and reinforcement
learning (§7.1), and against forward–inverse models of motor control
(Wolpert, Todorov, Shadmehr), and aligns with the equilibrium-point
hypothesis (Feldman), the Passive Motion Paradigm, and self-referenced
learning (Porr and Wörgötter; Maturana and Varela). None of its sections
uses the term "Markov blanket", and it has no notion of mental or covert
action.

**[CLAIM-341](../claims.d/CLAIM-341.md) (the thesis).** The claim says active inference "places
all of the agent's influence on what it observes in action, which samples
the data", citing this paper. That is right for this paper, and the paper
says it more plainly than the claim does: agents "can only act by
changing hidden states, not the sensory mapping per se" (p. 230), and
"agents cannot change the mapping per se" (p. 256). The paper also makes
the contrast sharper than the claim does. The claim holds that the agent
keeps its model in touch by changing the observer. The paper holds the
model fixed and changes the data: "the model (agent) is fixed and the aim
is to minimize surprise by re-sampling the data" (p. 232). Two
qualifications. First, the paper does change the observer without action:
perception and perceptual learning ("everything in the brain should change
to minimize free-energy", p. 228), and in the mountain-car training phase
learning ran with action "precluded" (p. 246). But this learning is driven
by data from a designed environment, not by the agent's own judgements, so
it is not the claim's judgement–observation loop. Second, the paper does
not say action is what keeps a model in touch. Action here pulls the
sensed world toward the model. That makes the paper a clean statement of
the cybernetic diagram the owner rejects. It does not meet the claim's
"defeated_if" conditions, since it has no evidence that learning needs
action.

**[CLAIM-339](../claims.d/CLAIM-339.md) (the counter).** The quoted phrase is exact (abstract,
p. 227), and the claim reports its use correctly: the paper's reason for
minimizing surprise is that a persisting system must keep its states in
bounds, and in its setup only action changes those states. Three
corrections.
- *What the ergodic argument does.* It equates entropy with time-averaged
  surprise (p. 230). It does not show that action is needed. Action is
  needed because the setup stipulates that "the only way that the agent
  can change hidden states is through action" (p. 230), and that the
  sensory mapping is out of the agent's reach. The mandate is as strong as
  that stipulation, and Appendix 1 itself weakens it ("closing ones eyes",
  p. 256).
- *What action is for.* The claim makes action "one route for evidence it
  did not select". In this paper action is the agent selecting its
  evidence: "sampling selectively what one expects to experience"
  (p. 232), so that "our predictions become a self-fulfilling prophecy"
  (p. 232). In every simulation where the priors are tight, evidence the
  agent did not select (exogenous forces) is cancelled by action and "not
  perceived" (pp. 239, 246). Here action suppresses unselected evidence
  rather than admitting it. The paper raises the objection that this
  confirms a wrong model, quoting Mumford, and embraces it: "Under the
  free-energy formulation, this weakness becomes the strength; if the
  environment delivers data that are consistent with the agent's model or
  hypothesis space, then the agent must be at equilibrium with its
  environment" (p. 232).
- *What anchors the loop instead.* The paper answers with existence.
  Agents "have the right priors", because "agents who do not have the
  right priors cannot exist" (p. 256); priors "can only be optimized by
  evolutionary or developmental processes" (p. 255). That anchor is
  selection across agents. The claim's surviving point, that action
  grounds a system's norms through persistence, is what the paper says.
  But that is the persistence of physical states, not the correction of a
  model.

**[CLAIM-342](../claims.d/CLAIM-342.md) (the anchor).** Supports it, more strongly than
[NOTE-766](NOTE-766.md) does. This paper's agent locks onto its priors with action
available. Action is the means of lock-in, since it cancels the
discrepancies that would have revised the percept (Figs. 3–4, 6, 12, 15).
The only correction route in the paper is perceptual learning from data
the agent did not shape, in the training phase, with action switched off
(p. 246). My observation: the paper's own anchor, the claim that agents
without the right priors do not exist, is independent scoring of
interpretations from outside them, applied by selection across a
population. That is [CLAIM-330](../claims.d/CLAIM-330.md)'s Regime B moved from operators to
organisms. It does not say what does this within one mind
([QUESTION-121](../questions.d/QUESTION-121.md)).

**[QUESTION-121](../questions.d/QUESTION-121.md).** Two of its candidates appear here. Body: channels
"critical for survival should be privileged and cannot be occluded (e.g.,
nociceptive pain signals and interoception signaling hunger, thirst
etc.)" (p. 256). These are inputs the agent cannot select away. And
unselected input: under flat priors the agent perceives exogenous
perturbations rather than acting on them (Fig. 2). Whether unselected input
reaches the agent is set by the precision of its priors, not by whether
it can act.

**[CASE-107](../cases.d/CASE-107.md).** The LIT's note is right: the paper's first and most
detailed simulations are oculomotor, and gaze is the action classic
locked-in syndrome spares. But they are not its only simulations. It also
has a two-joint arm, a mountain car and Lorenz trajectories. The
oculomotor model is one of retinal stabilization and saccades driven by
priors. The paper's example of motor poverty from low prior precision
(p. 249) is an internal failure with an intact motor plant. That is the
reverse of locked-in syndrome, an intact prior with no plant, and the paper
does not model the second.

## Bearing on the record

- **[CLAIM-341](../claims.d/CLAIM-341.md)**: supports its description of active inference and
  sharpens the contrast to "fix the model, re-sample the data" against
  "change the observer". It contains no evidence bearing on the claim's
  defeat conditions.
- **[CLAIM-339](../claims.d/CLAIM-339.md)**: its quotation is exact, and its use (persistence
  needs action) matches the paper. But the paper's action selects evidence
  to fit the model and suppresses what the agent did not expect. So the
  paper does not support "action is one route for evidence it did not
  select". The claim should cite NOTE-960 for the mandate's actual
  premises: the ergodic step plus the stipulation that action alone changes
  hidden states.
- **[CLAIM-342](../claims.d/CLAIM-342.md)**: supports. Lock-in with action available is the
  paper's design, defended as a strength, with existence as the external
  anchor.
- **[CLAIM-337](../claims.d/CLAIM-337.md)**: nothing here for it. The 2010 formulation has no
  mental action, and precision is optimized as perception, not chosen.
- It carries no instruction for machine-learning practice; §6 mentions
  robotics only in passing.

## Limitations

All results are simulations of a scheme whose action-to-sensation
derivative is taken from the true process (p. 254). The priors are
hand-set (§4) or learned in an environment the authors designed to
enforce the target behaviour (§§5–6), and the paper calls the latter
supervised (p. 252). The entropy bound needs a diffeomorphic sensory
mapping of uniformly high sensitivity. The answer to the dark-room
objection and to the confirmation of wrong models is an appeal to which
agents exist, not a mechanism. There is no fit to data.

## Open questions

- Can the mandate for action be derived without the stipulation that
  action is the only route to hidden states? Later Markov-blanket
  formulations try to do this. This paper does not.
- What, inside one agent, revises a fixed model that action is defending?
  The paper's only route is passive learning in a designed environment.
  A test: the same agent, with tight priors and action available, placed
  in an environment whose dynamics differ from its priors. Does it ever
  learn the new dynamics, or does it act them away?
