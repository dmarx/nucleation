---
number: 956
status: Read
formerly:
- NOTE-tmpi40rc
paper: LIT-1195
title: 'Parr & Friston — attention or salience?'
version: 1
history:
- version: 1
  date: '2026-10-16'
  note: >-
    Read in full from the authors' accepted manuscript on UCL Discovery
    (discovery.ucl.ac.uk/10058428/1/Parr_Attention%20or%20salience_AAM.pdf,
    eprint 10058428, CC BY-NC-ND 4.0; fetched 2026-10-16; 9 manuscript
    pages, created 12 October 2018), extracted with pdftotext. Read: the
    abstract, Introduction, the footnote on "beliefs", the Figure 1
    caption, "Attention as gain control", "Active perception and
    salience", "Attention and salience", the Conclusion, and the annotated
    reference list. The figure itself was not inspected. The journal's
    pagination (Curr Opin Psychol 29:1–5) is not in this copy, so page
    numbers below are the manuscript's. The published version was not seen
    and may differ in wording.
date: '2026-10-16'
summary: >-
  A short review that separates two things called attention: gain control,
  which weights currently available sensory data by their estimated
  precision, and salience, the expected information gain of an action
  (typically a saccade) that would acquire new data. It then ties them
  together: a saccade is driven by a prediction that a location will be
  sensed with high precision, so covert attention to a place biases an
  overt saccade there, which the authors read as support for the premotor
  theory.
---

# NOTE-956: Parr & Friston — attention or salience?

## Contribution

A conceptual review, with no new data or simulations. It argues that the
two senses of "attention" in the literature are different computations
with different anatomy and different disorders. One is covert gain
control over sensory channels. The other is the selection of overt
sampling actions by their epistemic value. It then says how the two are
coupled. Its formal backing is cited, chiefly to Parr and Friston (2017,
*Scientific Reports*), which "sets out the distinction between attention
and salience formally (mathematically) and illustrates this through
simulation" (reference 5 annotation, p. 6).

## Key insight

"Attentional processes select those sensations that are informative about
their causes. Broadly, these processes can be separated into two
categories – those that optimise the weighting of current data, and those
that mediate the acquisition of new sensations" (p. 5). Attention works
on data already in hand; salience works on data not yet acquired. "The
former relies upon currently available data, while the latter depends on
data that has yet to be acquired" (p. 4).

## Assumptions

- **A generative model.** Perception is "a process of optimising beliefs
  about the causes of sensations, while actions select new sensory data to
  test hypotheses about these causes" (pp. 1–2).
- **Beliefs are subpersonal.** "These are not propositional or subjective
  beliefs and are generally considered subpersonal" (footnote 1, p. 2).
- **Precision belongs to the likelihood.** "the degree to which we should
  update our beliefs about the causes of a sensation depends upon the
  precision (inverse covariance) of the probabilistic mapping between the
  two ... precision corresponds to the confidence afforded sensory
  evidence, given our knowledge about how it was generated" (p. 3).
- **Covert spatial attention is gain.** "For the purposes of this paper,
  we group visuospatial covert attention (in which no eye-movement takes
  place) with the covert attentional processes considered in the previous
  section" (p. 4). That is a stipulation, made against the premotor
  theory's reading of covert attention as a planned saccade.

## Key results

The paper's results are conceptual and rest on cited work.
- **Attention as gain control.** Implemented as "a multiplicative gain on
  ascending ('bottom-up') connections" (p. 3). It reproduces Posner
  cueing and figure-ground segregation by second-order statistics.
  Acetylcholine is the leading candidate for the gain, with Lewy body
  hallucinations as the pathology (p. 3).
- **Salience.** "Salient actions are those that solicit unambiguous data
  that could not have been predicted with a high degree of certainty prior
  to that action" (p. 4). Salience is equivalently intrinsic motivation,
  Bayesian surprise, relative entropy, or the epistemic part of expected
  free energy, and has the form of an optimal experimental design
  criterion (p. 4). It explains inhibition of return. Visual neglect is
  read as "a disorder of salience attribution" (p. 4), with the basal
  ganglia evaluating candidate saccades.
- **The coupling.** The streetlight effect is optimal in a sense, since
  "the unambiguous (precise) visual data obtained under the light supports
  stronger inferences than the darkness around it" (pp. 4–5). And because
  motor commands are predictions, "a prediction (i.e., motor command or
  setpoint for oculomotor reflexes) that a location in visual space will
  be foveated entails a belief that the precision associated with this
  location is high. The resulting saccade fulfils this prediction" (p. 5).
  Subthreshold frontal-eye-field stimulation raises gain at the location
  that suprathreshold stimulation would saccade to, "exactly as if the
  precision had increased" (p. 5). So "deployment of covert attention
  (precision) to a given location biases planning in favour of an overt
  saccade to that (salient) location" (p. 5).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Gain control and salience are distinct computations, with distinct anatomy and disorders (hallucination versus neglect) | moderate | review of cited theory and lesion evidence |
| C2 | Attentional gain is the estimated precision of the likelihood of current data | moderate | cited models (Feldman and Friston 2010 and others) |
| C3 | Salience is the expected information gain of a sampling action | moderate | cited formal equivalences (Itti and Baldi, Lindley, expected free energy) |
| C4 | Covert attention to a location biases an overt saccade there, because a saccade is a prediction of high precision at that location | weak | argument plus one stimulation study (Moore and Fallah 2001) |

## Concepts

- **Attention (gain control).** Covert weighting of current data by
  their estimated precision. It changes how much data count, not which
  data arrive.
- **Salience.** A property of an action: how much the data it would bring
  would change beliefs. High when the outcome is uncertain but the mapping
  from causes to outcome is precise (p. 4).
- **Precision.** Inverse covariance of the likelihood mapping from causes
  to sensations.

## Connections

It summarizes the authors' earlier work (*Sci Rep* 2017; *J R Soc
Interface* 2017; *Cereb Cortex* 2017 on neglect), Feldman and Friston
(2010) on attention as precision, and the epistemic-value formulation of
Friston et al. (2015) and Mirza et al. (2016). Its foil is the premotor
theory of attention (Rizzolatti et al. 1987), which it ends by endorsing
in modified form. It is the source Sandved-Smith et al. ([LIT-1191](../literature.d/LIT-1191.md),
read in [NOTE-958](NOTE-958.md)) build their attentional level on. It does not use
the term "Markov blanket" and does not speak of mental action.

**The LIT's summary and "Why this is here".** The summary is right in
substance: attention "depends upon estimating the precision of sensory
data", while salience "is a consequence of the need to actively engage
with the sensorium" (abstract, p. 1). Three corrections.
- *The split is not the paper's last word.* Its last section reconciles
  them: both "represent beliefs about the capacity of sensory data to
  adjudicate among competing hypotheses" (p. 4). And in the spatial domain
  a precision belief and a saccade command are the same prediction (p. 5).
- *Attention here is not an internal action.* The paper never calls gain
  control an action or a choice. It is inference about precision. What it
  does to perception is weight data whose content attention does not set.
  So the registration's "attention weights data whose content the
  generative model already fixes" is half right. The content is fixed by
  the world and the sensors, not by the model. What the model fixes is the
  mapping whose precision is estimated.
- *Attention can change what is observed, through action.* Covert
  precision on a location "biases planning in favour of an overt saccade"
  (p. 5), and the saccade then changes the data. So on this paper's account
  attention changes what is observed only by recruiting overt action.

**[CLAIM-337](../claims.d/CLAIM-337.md) (the counter).** The claim cites this paper, "on the
standard reading", for the split between attention and salience. The
reading confirms the split, but it does not help the claim's argument for
an internal loop. Gain control here is not selected as a policy and is not
called mental action. Its one route to changing what is observed runs
through the eyes. If anything the paper pulls covert attention back
toward overt action: its conclusion endorses the premotor theory. The
claim's first strand rests on Sandved-Smith et al., and should cite this
paper only for the identification of attention with likelihood precision.

**[CLAIM-341](../claims.d/CLAIM-341.md) (the thesis).** Where the thesis locates its
disagreement, the paper sits on the thesis's side of the line for
attention. Attentional gain changes how much a fixed datum counts, not what
the datum is. But that is not the thesis's loop either. The paper's gain
is a rate on updating, and nothing in it reshapes the observer over time.
On salience the paper is the clearest statement of the view the thesis
rejects: the agent's influence on what it observes is exercised by
choosing where to look.

**[CLAIM-339](../claims.d/CLAIM-339.md), [CLAIM-342](../claims.d/CLAIM-342.md) and [QUESTION-121](../questions.d/QUESTION-121.md).** Salience bears
on both sides of this exchange. Against Friston et al. (2010, read in
[NOTE-960](NOTE-960.md)), where action samples what the agent expects, salient
action seeks data "that could not have been predicted with a high degree
of certainty" (p. 4): "the best (most salient) experiments are those that
bring about the greatest change in beliefs" (p. 4). That is action as a
route to evidence the current interpretation cannot foresee, which is
what [CLAIM-339](../claims.d/CLAIM-339.md) says action supplies. But the agent still scores
salience with its own current beliefs about precision, and the streetlight
effect is the result: it looks where its model says data will be precise
(pp. 4–5). Evidence chosen by epistemic value is thus routed through the
interpretation it tests, which is [CLAIM-342](../claims.d/CLAIM-342.md)'s warning. Gain control
also has its own anchor problem. Its failure, weighting priors over
evidence, gives "false percepts, including hallucinations" (p. 5). That
failure involves no action at all.

## Bearing on the record

- **[CLAIM-337](../claims.d/CLAIM-337.md)**: the paper confirms that attention is likelihood
  precision and salience is the epistemic value of action. It does not
  supply an internal loop, and it ties covert attention to overt sampling.
- **[CLAIM-341](../claims.d/CLAIM-341.md)**: attention weights a fixed observation, as the claim's
  line requires, but does not reshape the observer.
- **[CLAIM-339](../claims.d/CLAIM-339.md) and [CLAIM-342](../claims.d/CLAIM-342.md)**: salience makes action a seeker of
  unpredicted data, which the counter needs, while scoring it by the
  agent's own precision beliefs, as the anchor claim warns.
- No instruction for machine-learning practice.

## Limitations

It is a five-page opinion review. Its claims are argued from cited models
and from lesion, pharmacological and stimulation studies, not shown here.
Covert spatial attention is assigned to gain control by stipulation. The
coupling argument (p. 5) rests on one stimulation result and on the
premise that motor commands are predictions.

## Open questions

- Is there a covert analogue of salience? That would be choosing which
  internal channel to weight by the information it would yield, without
  moving. The paper groups covert spatial attention with gain and so does
  not ask.
- Does the streetlight effect, where salience is scored by current
  precision beliefs, lock in under a wrong precision model? [NOTE-766](NOTE-766.md)'s
  sensory-attenuation lock-in suggests it can.
