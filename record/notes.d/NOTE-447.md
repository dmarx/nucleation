---
number: 447
status: Read
formerly:
- NOTE-tmp5ncd3
paper: LIT-603
title: 'The Emperor''s New Markov Blankets'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read in full: the December 2020 PhilSci-Archive version (eprint 18467;
    identical text re-deposited as 19726 with a cover note), §§1–7, the
    captions of Figures 1–8, footnotes 1–14; the references were scanned.
    Section numbers below are the headings as printed (2 Variational
    Bayesian inference … 7 Conclusion), which run one ahead of the
    roadmap in the introduction. Page numbers are the preprint's. The BBS
    target article was not read beyond its abstract; see the LIT for what
    that means for this reading.
date: '2026-10-03'
summary: >-
  Pearl blankets (conditional-independence shields in a Bayesian network)
  and Friston blankets (agent–environment boundaries in the world) are
  different constructs conflated in the free-energy literature. The
  four-way partition needs a chosen internal node, sensorimotor labels and
  steady state; in Friston's soup it also needs electrochemical-only
  coupling and a fixed cluster size. Realist use needs metaphysical
  premises; instrumental use is innocent but settles nothing about
  boundaries.
---
<!-- inactive-ok-file: THEORY-073 — Proposed; named as the THEORY filed for this note's candidate, nothing here rests on it -->

# NOTE-447: The Emperor's New Markov Blankets

## Contribution

Critics had said the free energy principle is unfalsifiable or merely
redescriptive. This paper isolates one construct, the Markov blanket, and
traces how it changed meaning, from a device for simplifying mean-field
variational inference to a claimed physical boundary of organisms and
minds. Naming the two uses (Pearl and Friston blankets) and the two research
programmes (inference with and within a model) gives the debate a
vocabulary in which the critique can be stated precisely.

## Key insight

A Markov blanket is a property of a graph, and a graph is a model. You can
only find a blanket after choosing a graph and choosing which node you care
about. So a blanket cannot tell you where a system ends unless you have
already decided where it ends, or you add a metaphysics on which the graph is
the world.

## Assumptions

- **Standard variational inference** (§2): ELBO / variational free energy,
  mean-field factorisation; Pearl blankets reduce each factor's update to
  expectations over its blanket (Eq. 20).
- **Bayesian networks are directed acyclic graphs** (§3.1); cyclic
  sensorimotor loops need unrolling in time (footnotes 8, 13).
- **Scientific models are maps** (§6.1), chosen for purposes and selected by
  parsimony (e.g. by free energy itself), so their structure is partly a
  modelling choice.

## Key results

- **Pearl blankets (§3.2).** mb(x) = pa(x) ∪ ch(x) ∪ copa(x); worked on an
  18-node network, they cut each mean-field update to a handful of nodes.
  Early active-inference papers used them this way, "if not slightly
  overzealous" (§4.1).
- **The soup (§4.2, Figs. 3–5).** Friston 2013b's simulation, reproduced
  from its code: the adjacency matrix is built from electrochemical coupling
  only, "while other forms of influence included in the simulation (such as
  Newtonian forces) are ignored"; the eight most densely coupled nodes are
  declared internal; the blanket is then traced; the result is read as a
  membrane. Calling this a property of the system is "a clear example of the
  reification fallacy". §6 adds that steady state is assumed when the
  simulation is stopped and that the number of internal clusters is
  "arbitrarily" assumed.
- **Slippage in the literature (§4.3).** Allen & Friston, Clark, Kirchhoff et
  al., Hohwy and Ramstead et al. are quoted moving between statistical,
  causal, spatial, epistemic and autopoietic boundaries.
- **Friston blankets on an arbitrary graph (§5.1, Fig. 7).** Labelling x10
  or x9 internal yields different blankets; neither blanket's sensory states
  include the network's observed variables, which become "external".
- **Co-parents (§5.1, Fig. 8).** In a patellar-reflex network a hammer strike
  is a co-parent of the spinal neurons with the cortical command; an
  external intervention has "exactly the same formal properties" as an
  internal cause. Whether co-parents are sensory, active or ignored varies by
  author.
- **Granularity.** Which cause is "most proximal" is model-relative (citing
  Anderson 2017), so the sensory/active boundary is too.
- **Dilemma (§6.2, §7).** "Inference with a model": blankets on the
  scientist's or agent's map, legitimate, no ontological consequence.
  "Inference within a model": the agent is the model and its blanket is its
  boundary, which needs metaphysical premises; Ramstead et al. 2019 are shown
  both deriving blankets from dynamics and "placing" them.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Pearl and Friston blankets are distinct constructs with different assumptions | strong | formal exposition §§3–5; worked graphs |
| C2 | The free-energy literature conflates them | moderate | quotations from six groups (§4.3, §6) |
| C3 | In Friston 2013b the blanket depends on unjustified modelling choices, so attributing it to the system is reification | moderate to strong | re-run of the published code; choices identified (§4.2, §6) |
| C4 | A Friston-blanket partition presupposes a chosen internal set and cannot itself define inside and outside | strong for arbitrary graphs | Fig. 7 |
| C5 | Realist (within-a-model) use needs metaphysical premises not in the formalism | moderate | conceptual argument §6 |
| C6 | Instrumental use cannot settle debates about the boundaries of mind or life | moderate | argument from model-relativity §6.1 |

## Concepts

- **Pearl blanket.** The Markov blanket of a node in a Bayesian network:
  parents, children, co-parents.
- **Friston blanket.** A blanket read as a boundary in the world partitioning
  internal, sensory, active and external states, in recent work defined by
  sparse coupling at nonequilibrium steady state.
- **Inference with a model.** A scientist (or agent) uses a generative model
  to infer hidden states; blankets are features of the model.
- **Inference within a model.** A model contains both the generative process
  and an inferring subsystem; the blanket is claimed to bound that
  subsystem.

## Connections

It builds on Biehl, Pollock & Kanai's technical critique, Andrews and van
Es on instrumentalism, and Baltieri, Buckley & Bruineberg's Watt-governor
example of pan-(active-)inferentialism. It cites Barandiaran, Di Paolo &
Rohde ([LIT-566](../literature.d/LIT-566.md)) for "interactional asymmetry". Raja et al.
([LIT-598](../literature.d/LIT-598.md)) cite this preprint.

## Bearing on the record

- **[LIT-526](../literature.d/LIT-526.md) and [NOTE-421](NOTE-421.md).** C3 is the basis of the LIT's `corrects`. It
  agrees with [NOTE-421](NOTE-421.md)'s reading (k = 8 chosen by spectral clustering; the
  lemma as redescription) and adds two choices [NOTE-421](NOTE-421.md) did not flag:
  electrochemical-only adjacency, and steady state assumed at the stopping
  time.
- **Demarcation ([LIT-192](../literature.d/LIT-192.md), [NOTE-094](NOTE-094.md)).** If blankets are model-relative,
  Friston's exclusion of the candle flame (C7 in [NOTE-421](NOTE-421.md)) is a fact about a
  model of a flame, which [LIT-526](../literature.d/LIT-526.md) does not provide.
- **THEORY filed** as [THEORY-073](../theory.d/THEORY-073.md) (Proposed), with the formal part (C4)
  filed separately as [THEORY-066](../theory.d/THEORY-066.md) (Active): a Markov-blanket partition does
  not individuate a system; where the blanket falls depends on the graph and
  on which nodes are designated internal, so it presupposes the boundary it
  is used to find. Sources: this paper and [LIT-598](../literature.d/LIT-598.md).
- No instruction for machine-learning practice.

## Limitations

- Read in the version the authors say they rewrote; technical sections may be
  shorter in the BBS text, and the authors' replies to commentaries are not
  read.
- The critique concerns the use of blankets, not the free energy principle's
  mathematics, and the authors say so.
- Recent formal definitions of Friston blankets (sparse Hessians at
  nonequilibrium steady state) are noted, not analysed.

## Open questions

- Is there a model-independent criterion that would make a Friston blanket
  "detected" rather than placed? The later sparse-coupling definitions are
  the candidate; the paper leaves them open.
- Does the BBS version keep the soup analysis, and how did Friston and
  colleagues answer it in the commentaries?
