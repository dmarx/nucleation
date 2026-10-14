---
number: 818
status: Read
formerly:
- NOTE-tmpxxz74
paper: LIT-1000
title: 'Gidon, Aru and Larkum — Does neural computation feel like something?'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the publisher's open-access PDF (Frontiers, CC BY,
    19 pages), text extracted with pdftotext: abstract, Introduction,
    Methods, every Results subsection, the Discussion with its sections
    on the Turing-machine model, biological networks, IIT, Frankfurt and
    "misconsciousing", and the conclusion; Figures 1–5 read from their
    captions. The reference list was checked for the works the argument
    leans on (Maudlin 1989, Gidon et al. 2022). The ModelDB code was not
    run. The paper is typed "Hypothesis and Theory" and has no theorems.
date: '2026-10-14'
summary: >-
  A five-neuron NEURON simulation shows that a voltage clamp replaying a
  recorded response injects no current when the matching stimulus is
  shown, yet fixes every state transition whatever the input. Under
  computational functionalism, which counts the transitions that did not
  happen, the clamp changes the computation and so the experience while
  changing no activity and no actual causal interaction. The authors
  read this as a challenge to functionalism, not a refutation.
---
<!-- inactive-ok-file: QUESTION-059 CLAIM-039 — Deferred; the question this work was filed for and the claim it bears on, on a set-aside line -->
<!-- inactive-ok-file: THEORY-101 THEORY-045 THEORY-093 THEORY-090 THEORY-023 THEORY-092 THEORY-119 THEORY-043 — Proposed; the accounts this reading bears on, open -->

# NOTE-818: Gidon, Aru and Larkum — Does neural computation feel like something?

## Contribution

The paper turns the authors' earlier thought experiment (Gidon et al.
2022, "Does brain activity cause consciousness?") into a simulation, and
adds one case to it. A *feedback* replay, a voltage clamp whose command
voltage is the recorded response, leaves the network to run unaided when
the stimulus matches, and corrects it only when it would deviate. The
case is used to show that, on computational functionalism, whether a
system is conscious can turn on an intervention that never acts. The
argument is Maudlin's (1989) point about counterfactuals, run on a
biophysical model rather than on a hypothetical machine.

## Key insight

Computation is defined over the transitions a system *would* make on
other inputs, not only the one it makes. A device that removes every
other transition, and stays idle on the actual one, therefore changes
the computation without changing anything that happens. If experience
is fixed by computation, it changes too. Whoever finds that absurd must
say experience depends on something other than the computation; whoever
accepts it must say an idle device can alter what a subject feels.

## Assumptions

- **Computational functionalism as the working hypothesis.** "Some
  computations constitute conscious experiences"; here, a subject that
  performs hue-computation is hue-conscious. The authors say they
  "initially accept this working hypothesis but shall reevaluate it".
- **Computation as Turing and Putnam define it.** "A system receives
  various inputs that trigger state transitions according to a set of
  rules (or an algorithm), leading to an output", and "the inputs,
  states, transitions, and outputs define the functional organization".
- **Core and auxiliary computations.** By stipulation, altering a core
  computation's input/output function alters experience. Hue-computation
  is *assumed* core. The reader is invited to substitute any computation
  they think is core, including a global workspace.
- **Changing functional organization is changing consciousness.** Cited
  to Putnam, Shagrir, Block and Lewis. This is the premise that carries
  the conclusion.
- **Causation read mechanistically**, not counterfactually (Ross and
  Bassett 2024 rather than Lewis 1973). That is why an idle clamp is
  said to leave "cause-and-effect relations between the neurons" intact.
- **Consciousness is not defined.** It is "the experience of oneself or
  one's surroundings that fades during deep sleep or anesthesia".
- **Deterministic model.** Biological noise is set aside: the replay
  "would undo the ongoing noise and reintroduce the recorded noise".
  Theories that need "true stochasticity" are explicitly not addressed.

## Key results

- **The model (Methods, Fig. 1).** Five single-compartment
  Hodgkin–Huxley-type neurons (Na⁺, K⁺, leak; R_in = 50 MΩ), each driven
  by the preceding three in cyclic order; synapses with 2 ms rise,
  τ_syn = 10 ms, g_syn = 5 nS, and short-term depression to 50% per
  spike recovering with τ = 1 s. Two LGN nodes are random spike trains.
  Green light turns on both and all five neurons fire; red or blue turns
  on one and only neuron a or b fires.
- **Two replays (Fig. 2).** A *feedforward* replay overwrites each
  neuron's voltage with the recorded trace and so "severed the
  connection between the neurons". A *feedback* replay is a simulated
  voltage clamp (NEURON's SEClamp) that injects current only when the
  voltage departs from the command trace. With no stimulus, both
  recreate the green response; the clamp current equals the missing LGN
  current (Fig. 2A2).
- **Incongruent input (Fig. 3A).** Red light plus green replay: all
  neurons fire as for green, and the clamp supplies only the input from
  the second LGN node. The replay "remained equally effective whether
  the neurons … were disconnected or rewired, or a new input was
  introduced (not shown)".
- **The computation degenerates (Figs. 3D, 4).** Under replay, the state
  transitions no longer depend on the input. In the toy algorithm every
  branch but the recorded one is pruned, leaving "a fixed sequence of
  operations independent of the input". In the Turing-machine version
  the clamp becomes part of the transition function, and the result is
  "a trivial computation consisting of a single sequence of states (i.e.,
  universally realizable)".
- **Nothing type I and type II (Fig. 3B–C).** Green light plus green
  replay: the clamp injects no current, because "no intervention was
  needed". With the amplifier off (type I), activity is identical. With
  it on and idle (type II), activity is again identical, but the
  counterfactual transitions are gone. On the working hypothesis, type I
  is hue-conscious and type II is not, or is less so. "If the replay did
  nothing, how could it change consciousness?"
- **Counterfactual eraser.** The idle clamp "can prohibit only
  counterfactuals without affecting anything else, i.e., brain activity
  and cause-and-effect between the neurons". By contrast, "green glasses"
  that turn all input green leave the cortical computation intact; they
  give identical activity but, for the functionalist, do not alter
  experience.
- **Is the clamp part of the system? (Discussion.)** The functionalist's
  question is whether the functional organization changed, and it did:
  states "that would have been reached … are unreachable". So "the
  feedback replay device is conceptually part of (and alters) the Turing
  Machine". How much it changes depends on "the proportion of states
  used in the congruent case compared to all other cases".
- **IIT (Discussion).** For IIT the clamp degenerates the transition
  probability matrix, giving "a simpler cause-and-effect structure that
  dramatically reduces Φ". This is "not … a formal challenge to IIT",
  because IIT locates consciousness in what the system *is* (its
  cause–effect structure), not in what it *does*. The shared oddity is
  that, for both, "the feedback replay can degrade consciousness,
  despite doing nothing".
- **Frankfurt (Discussion).** The eraser is a Frankfurt device that
  prescribes every neuron's activity rather than an outcome. If
  counterfactuals matter to consciousness, Jones may act exactly as
  prescribed "but with altered or possibly diminished conscious
  experience".
- **Conclusion.** Substrates realise more functional states than the
  computation ascribed to them. "Natural counterfactuals" are "embodied
  in the biological brain's composition, structure, and dynamics and,
  therefore, cannot be erased without altering the brain's physical
  structure and/or dynamics." The biological brain is "the only known
  substrate capable of consciously experiencing the world". The risk
  "lies in ascribing machines with consciousness when they are not".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | A feedback voltage-clamp replay reproduces a recorded network response exactly, supplying only the input that is missing | strong | the simulation, Figs. 2–3 (trivially true of an ideal clamp) |
| C2 | Under the replay, the network's state transitions no longer depend on its input, so the computation it implements degenerates to a single sequence | strong | Figs. 3D, 4, given the Turing–Putnam definition of computation |
| C3 | When the input matches, the clamp injects no current, so activity and actual neuron-to-neuron causation are unchanged | strong | Fig. 3B2, with causation read mechanistically |
| C4 | So computational functionalism must hold that an intervention that does nothing can change conscious experience | moderate | C2–C3 plus the premise that changing functional organization changes consciousness; an argument, not a finding |
| C5 | IIT gives the same verdict (Φ falls) without contradiction, because it rests on cause–effect structure | weak | asserted, Φ not computed |
| C6 | Consciousness depends on "natural counterfactuals" fixed by the substrate, not on computation | weak | offered as an "alternative view" in the closing section, not argued |
| C7 | Attributing consciousness to machines that lack it is the larger moral risk | weak | an opinion, with no argument from the simulation |

## Method

1. Simulate a five-neuron recurrent "visual cortex" with two LGN inputs
   in NEURON; record every neuron's voltage for a green stimulus.
2. Replay the recordings by overwriting (feedforward) or by a voltage
   clamp with the recordings as command voltage (feedback).
3. Present no stimulus, an incongruent stimulus (red), or the congruent
   one (green), and record the clamp currents.
4. Map the result onto a toy branching algorithm and a Turing machine
   whose transition function absorbs the clamp.

## Concepts

- **Computation.** Input-triggered state transitions by rule, ending in
  an output; inputs, states, transitions and outputs make up functional
  organization.
- **Core vs auxiliary computation.** Core: altering its input/output
  function alters experience. Auxiliary: does not.
- **Feedback replay / counterfactual eraser.** A monitor that holds each
  element to a prescribed trajectory and acts only on deviation. Its
  "key feature … is their potential intervention rather than their actual
  intervention".
- **Nothing type I / type II.** The replay idle because it is switched
  off, versus idle because nothing deviates.
- **Natural counterfactuals.** The alternative states a substrate's
  physical make-up allows, as distinct from those a computation
  ascribed to it allows.

## Connections

The paper extends Gidon, Aru and Larkum (2022), which recorded and
replayed a whole brain's activity and ended in a reductio about
scattered neurons. It re-runs Maudlin's (1989) "Olympia" argument, that
consciousness cannot depend on counterfactual dispositions that are never
exercised, and cites Barnes (1991) against it, but engages neither in
detail. It relies on the Putnam and Searle point that a computation
without counterfactuals is "universally realizable", which is what
Chalmers's rock paper ([LIT-404](../literature.d/LIT-404.md), read in [NOTE-342](NOTE-342.md)) answers by requiring
"reliable, counterfactual-supporting transitions": on that criterion the
clamped network implements only a trivial, inputless automaton. It sits
opposite Pylyshyn's and Chalmers's neuron-replacement arguments
([LIT-392](../literature.d/LIT-392.md), [NOTE-347](NOTE-347.md)), which keep the causal organization and swap the
substrate; this keeps the substrate and activity and removes the
organization's unused branches. The Frankfurt section borrows the device
of [LIT-694](../literature.d/LIT-694.md).

## Bearing on the record

- **[QUESTION-059](../questions.d/QUESTION-059.md) (Deferred).** The LIT was filed as "a simulation-based
  test of whether meeting the functional role suffices for feeling". That
  overstates it twice.
  - *It is not a test.* The simulation fixes nothing about experience;
    it only shows that an idle clamp leaves activity unchanged while
    fixing transitions, which is true of any ideal clamp. The
    philosophical work is an argument from the definition of
    computation. [QUESTION-059](../questions.d/QUESTION-059.md) says another argument from a definition
    would not answer it.
  - *It is about consciousness in general*, "the experience … that
    fades during deep sleep", and says nothing of affect, valence or
    feeling in the affective sense. The title's "feel like something" is
    the phrase for phenomenal consciousness.
  What it does supply is a dilemma for the identity side. Veit's identity
  of feeling with "occupy[ing] a coordinated regulatory state"
  ([THEORY-101](../theory.d/THEORY-101.md)) is a functional identity, so it inherits the eraser: the
  same regulatory activity, with its unused alternatives removed, would
  have to be a different feeling or none. Veit would need to say either
  that the state is individuated by actual causal activity (then the
  identity is not with a functional role in the Turing–Putnam sense) or
  that the eraser changes feeling. Neither the paper nor [THEORY-101](../theory.d/THEORY-101.md) says
  which.
- **[THEORY-045](../theory.d/THEORY-045.md), [THEORY-093](../theory.d/THEORY-093.md), [THEORY-090](../theory.d/THEORY-090.md).** The paper's "natural
  counterfactuals … embodied in the biological brain's composition"
  points the same way as the bodily-mechanism side of [QUESTION-059](../questions.d/QUESTION-059.md), but
  only as a closing suggestion; it gives no mechanism and mentions no
  body. It is not evidence for those accounts.
- **[THEORY-023](../theory.d/THEORY-023.md).** The paper sides with the biological naturalist on AI
  consciousness, and its "misconsciousing" section asserts that false
  attribution is the greater risk. It does not touch the evidential
  deadlock [THEORY-023](../theory.d/THEORY-023.md) describes; it is one more statement of one side.
- **[THEORY-092](../theory.d/THEORY-092.md).** Block's lookup machine matches every actual and
  counterfactual behaviour and lacks intelligence; the clamped network
  matches every actual activity and lacks the counterfactuals. Both say
  the mental property is not fixed by what actually happens, from
  opposite directions.
- **[THEORY-119](../theory.d/THEORY-119.md).** Frankfurt holds that a device that "plays no part" in
  an action cannot change responsibility for it. The paper argues that,
  on functionalism, a device that plays no part *can* change the
  agent's consciousness. The two are compatible, but together they mean
  a functionalist who accepts Frankfurt holds an agent responsible for
  an act she may not have experienced, which is the question the paper
  ends that section on.
- **[THEORY-043](../theory.d/THEORY-043.md).** Its anti-nesting principle is a constraint on what
  counts as the system; the paper's claim that the clamp is "conceptually
  part of" the Turing machine is the same kind of boundary decision,
  taken without a principle.
- No instruction for machine-learning practice; nothing for the
  anthology.

## Limitations

- **The simulation carries no evidential weight on consciousness.** Its
  outputs are voltages and clamp currents. The consciousness verdicts
  come from the working hypothesis, applied by definition.
- **The key premise is cited, not defended.** That changing functional
  organization by removing unexercised branches changes experience is
  exactly what a functionalist following Maudlin's critics (Barnes 1991,
  cited) or Klein (2018, cited) would contest. Those replies are not
  engaged.
- **The size of the change is not estimated.** The authors concede it
  depends on the proportion of states used, and the paper says only
  "possibly diminished or even abolished".
- **The core/auxiliary distinction is stipulated** and admitted to be
  only implicit in functionalist theories.
- **The positive alternative is not developed.** "Natural
  counterfactuals" is named in one paragraph; what fixes them, and why
  they would matter for experience, is not said.
- **Noise and stochastic theories are set aside**, so the result says
  nothing about accounts on which experience needs genuine randomness.

## Open questions

- Does a functionalist who makes implementation turn on
  counterfactual-supporting transitions ([LIT-404](../literature.d/LIT-404.md)) accept the Nothing
  type II verdict, or deny that a clamp outside the neurons is part of
  the implementing system? A reading of a reply by a functionalist would
  settle which.
- Is there a principled boundary on the system, other than "whatever
  changes the transition function", that would put the clamp outside it?
- What, concretely, are natural counterfactuals, and could a
  non-biological substrate have them?
