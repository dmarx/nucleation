---
status: Read
paper: 'LIT-tmpovskz'
title: 'Gerstner et al. — Eligibility traces and plasticity on behavioral time scales'
version: 1
history:
- version: 1
  date: '2026-10-24'
  note: >-
    Read in full on 2026-10-24 from the version of record, Frontiers in
    Neural Circuits 12: 53 (published 31 July 2018), the publisher's 16-page
    PDF (frontiersin.org/articles/10.3389/fncir.2018.00053/pdf), open access
    under CC BY. Text extracted by pdftotext. Read: abstract, sections 1–4,
    the footnotes, Figures 1–2 by their captions, and the author
    contributions and funding statements. The reference list was not read.
    The arXiv preprint (1801.05219) was not consulted. Page numbers below
    are the article's.
date: '2026-10-24'
summary: >-
  A review by theoreticians. In a three-factor rule, pre- and postsynaptic
  co-activation sets a decaying synaptic flag, the eligibility trace, and
  the weight changes only if a third signal (reward minus expected reward,
  surprise, novelty, or a neuron-specific error) arrives while it is set.
  Five experimental papers (2014–2017), mostly in slices, give traces of
  about 1 s in striatum, 3–10 s in cortex, about 2 s and about a minute in
  hippocampus. The authors grant that other mechanisms could bridge the
  same gap.
---
<!-- inactive-ok-file: CLAIM-tmp0qupq CLAIM-277 CLAIM-364 — Proposed; the claims this reading bears on, named, nothing here rests on them -->
<!-- inactive-ok-file: THEORY-tmpeolav — Proposed; filed from this reading, named -->

# NOTE-tmpa6d2r: Gerstner et al. — Eligibility traces and plasticity on behavioral time scales

## Contribution

Three-factor learning rules had been a theoretical assumption since the
1960s and a working part of reinforcement-learning models, but the
eligibility trace on the scale of a second had no direct physiological
evidence. This review collects the first experiments that measured it,
in striatum (Yagishita et al. 2014), cortex (He et al. 2015) and
hippocampus (Brzosko et al. 2015, 2017; Bittner et al. 2017), and
classifies rules by how specific the third factor is.

## Key insight

Co-activation alone does not change a synapse; it marks it. A later,
broadcast signal decides whether the mark becomes a change and in which
direction. "a non-zero third factor is needed to transform the eligibility
trace into a weight change" and "the third factor also influences the
direction of change" (p. 4). Specificity comes from the mark, not the
broadcast.

## Assumptions

- **The rule (Eqs 1–2, pp. 2, 4).** de_ij/dt = η f_j(x_j) g_i(y_i) − e_ij/τ_e;
  dw_ij/dt = e_ij M^3rd(t). The flag e_ij is a correlation detector of
  presynaptic activity x_j and postsynaptic state y_i; the weight w_ij
  moves only with the third factor M^3rd.
- **Three types (pp. 4–5).** Type 1, a global scalar third factor; Type 2,
  a global factor read through a neuron-specific function h_i(M^3rd);
  Type 3, a neuron-specific factor M_i^3rd, which covers approximations to
  backpropagation (random feedback weights, dendritic error signals).
- **The theoretical time scale.** For action learning the trace should
  last about as long as an action to its reward: 200 ms to 2 s; less than
  100 ms or more than 10 s "would be less useful" (pp. 5–6).
- **The reviewers' own classification.** A rule counts as three-factor only
  if the third factor carries "information on the performance of the
  network as a whole"; the Clopath rule, though a product of three terms,
  is a two-factor rule (p. 7).

## Key results

- **Striatum (Yagishita et al. 2014; p. 7, Fig. 2A).** In nucleus accumbens
  spines, glutamate uncaging followed by three postsynaptic spikes,
  repeated ten times, with optogenetic dopamine at various delays.
  Spines enlarged when dopamine came during the protocol or up to 1 s
  after it, not at 4 s or 2 s before. "we have in the striatum a
  three-factor learning rule for the induction of LTP where the decay of
  the eligibility trace occurs on a time scale of 1 s" (p. 7). It
  depended on NMDA receptors, CaMKII, protein synthesis and D1 receptors.
- **Cortex (He et al. 2015; p. 9, Fig. 2B).** Layer 2/3 of visual and
  prefrontal cortex in slices. Pre-before-post pairing gave LTP if
  noradrenaline came within 5 s, not 10 s; post-before-pre gave LTD if
  serotonin came within 2.5 s, not 5 s. So "pre-before-post pairing leaves
  an eligibility trace that decays over 5–10 s and that can be converted
  into LTP by the neuromodulator noradrenaline" (p. 9), and a separate
  LTD trace decays over about 3 s.
- **Hippocampus, Brzosko et al. (2015, 2017; pp. 9–10, Fig. 2C).** In CA1
  slices, a protocol that gives LTD is turned into LTP if dopamine
  perfusion begins within about a minute, not ten minutes. Dopamine was
  given for about 10 minutes, so it "cannot be considered as a phasic
  signal". The reviewers suggest the process "could be related to
  synaptic consolidation" rather than reinforcement learning (p. 10).
- **Hippocampus, Bittner et al. (2017; p. 10, Fig. 2D).** CA3 input to CA1
  paired with a calcium plateau potential up to 1–2 s later or earlier
  gave potentiation of about 200% after five pairings. Bittner et al.
  called the rule non-Hebbian; the reviewers reclassify it as an
  eligibility trace set by input plus subthreshold depolarization, decaying
  over about 2 s, and say how the two readings could be told apart (p. 11).
- **Consolidation (p. 6).** Synaptic tagging-and-capture fits the framework
  with a tag lasting about an hour. "The framework is experimentally
  well-established in the context of synaptic consolidation" (p. 7).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | In striatal, cortical and hippocampal synapses, co-activation leaves a trace of about 1–10 s that a later neuromodulator or plateau potential converts into a weight change | moderate: five papers, mostly in vitro, one lab per region | Section 3, Fig. 2 |
| C2 | The third factor sets the sign as well as the size of the change | moderate | Eq. 2; He et al.'s NE for LTP and 5-HT for LTD |
| C3 | Specificity of learning under a broadcast signal comes from the synaptic flag | moderate: argued from the rule, with Fig. 1B | p. 11 |
| C4 | TD-learning and policy-gradient methods can be written as three-factor rules with reward minus expected reward as third factor | strong as a mapping; cited, not derived here | p. 11 |
| C5 | Surprise or novelty, not only reward, can be the third factor | weak: argued, with predictions not yet available | pp. 6–7 |
| C6 | Eligibility traces are what bridges behavioural and neuronal time scales | weak as exclusive: the authors grant alternatives | p. 12 |

## Concepts

- **Eligibility trace (synaptic flag)**: e_ij, an internal synaptic state
  set by Hebbian co-activation, not visible in standard recordings, a
  "candidate weight change" (p. 2).
- **Third factor**: M^3rd, a signal whose presence while the flag is set
  converts it into a weight change; in theory related to "performance of
  the network as a whole" (p. 7).
- **NeoHebbian**: another name for three-factor rules (Lisman et al. 2011).
- **Conceptual prediction**: an assumption of a conceptual model that
  experiment can later test. "Assumptions are predictions" (p. 12).

## Connections

It updates Frémaux & Gerstner (2016), which reviewed the field to the end
of 2013. Its formal background is Sutton & Barto, Williams (1992), Xie &
Seung (2004), Izhikevich (2007) and Legenstein et al. (2008); its
experimental targets are the five papers above. The record holds no other
reading on synaptic plasticity rules.

## Bearing on the record

- **CLAIM-tmp0qupq (a learned prior over which processes govern).** The
  claim cites this review for "three-factor rules are established". The
  reading narrows that, and adds two points.
  - **Narrower.** What is "experimentally well-established" is the
    hour-scale tag of synaptic consolidation (p. 7). The seconds-scale
    trace that learning from outcomes needs has support "collected only
    during the last few years" (p. 1), from five papers, mostly in slices.
    And the reviewers write that "there is nothing—apart from conceptual
    elegance—to favor eligibility traces over alternative neuronal
    mechanisms" (p. 12). Support at the synapse, in a few preparations,
    is what the review shows.
  - **The claim's rule has no trace.** Its ΔE_ji = η x_j y_i (R_t − R̂_t) − λE_ji
    multiplies co-activation by the outcome signal at the same moment. In
    the review's rule the co-activation is held in a decaying flag until
    the signal arrives. Governance outcomes typically arrive after the
    recruitment that earned them, so a version of the claim's rule meant
    to learn from them needs that trace and a time constant matched to
    the delay. The claim already calls its rule schematic and not neural,
    which this does not contradict.
  - **On entrenchment.** The claim warns that "Naive Hebbian learning
    entrenches": what is recruited often is reinforced whether or not it
    deserved authority. The review's answer for three-factor rules is that
    "among all the flagged synapses only those that show, over many
    trials, a correlation with the reward signal will be consistently
    reinforced" (p. 11). With reward minus expected reward as the third
    factor, frequency alone is not reinforced. What remains is the
    sampling problem the claim also names: only what is co-active can be
    flagged, so what is never recruited is never credited.
  - **The third factor need not be reward.** Surprise and novelty are
    candidates (pp. 6–7). A b_H trained by surprise would reinforce
    whatever recruitment preceded unexpected outcomes, good or bad.
  - Filed as THEORY-tmpeolav.
- **CLAIM-277 and CLAIM-364.** The entrenchment point bears on both
  through CLAIM-tmp0qupq; the review says nothing about authority.
- **For the anthology.** The mapping of TD-learning and policy gradient to
  three-factor rules, and Type 3 rules as biological approximations of
  backpropagation, bear on learning rules in machine learning. The LIT's
  `anthology-candidate` flag stands. The review gives no instruction for
  practice.

## Limitations

- **Mostly in vitro.** Four of the five papers are slice experiments with
  imposed protocols; only Bittner et al. combine them with in vivo place
  fields. Whether the measured traces operate in behaving animals is
  inferred.
- **One study per region.** Each time constant rests on one laboratory's
  protocol.
- **The abstract says "four key experiments"; the body reviews five
  papers**, counting Brzosko et al. 2015 and 2017 as one line of work.
- **Written by theoreticians** whose models assumed these traces; their
  section "The Paradoxical Nature of Predictions" (pp. 12–13) says as
  much.
- **The surprise-based third factor** has, by the authors' account, no
  precise predictions yet (p. 6).

## Open questions

- Do seconds-scale traces operate in vivo during learning from delayed
  reward? Interference with the trace's molecular basis (CaMKII in
  striatum) during behaviour would test it.
- In CA1, is the trace set by input alone (Bittner et al.) or by input
  with depolarization (the reviewers)? Clamping postsynaptic voltage
  during stimulation would decide (p. 11).
