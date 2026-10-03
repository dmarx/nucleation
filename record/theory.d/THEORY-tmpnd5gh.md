---
status: Proposed
promote_when: >-
  A result about the later formulations, which the formal core
  (THEORY-tmpcv4h8) does not reach. The account would be promoted if
  the sparse-coupling definition of a blanket at nonequilibrium steady
  state (Friston 2019 and later, not yet held) were shown to need an
  internal set, a choice of variables or a coarse-graining as input. It
  would also be promoted if that definition, applied to one model under
  equally defensible choices of variables, were shown to return different
  blankets. The account is refuted by a procedure, stated within the
  formalism, that takes a dynamical system with no partition supplied
  and returns a unique internal set, stable under a change of variables,
  that matches a boundary drawn independently, such as the membrane of a
  simulated protocell. It is also refuted, in its last clause, by a
  blanket formalism with time-varying blanket states (Ramstead et al.
  2020, cited by LIT-tmpumhsc and not held) that, in a worked model,
  tells a membrane the system makes from a boundary imposed on it. What
  cannot settle it: further applications that place a blanket on a brain,
  a cell or a society, since placement is what is in question;
  re-derivations of Lemma 2.1 of LIT-526, which both critiques grant; or
  the observation that blankets nest.
title: 'A Markov blanket does not individuate a system: where it falls is fixed by modelling choices made before it is found, so it presupposes the boundary it is used to find, and it cannot represent a boundary the system produces'
version: 1
tags:
- individuation
- philosophy-of-biology
- philosophy-of-science
- probabilistic-modeling
- complex-systems
date: '2026-10-03'
source:
- LIT-tmpxq8pk
- LIT-tmpumhsc
- LIT-526
extends:
- THEORY-tmpcv4h8
summary: >-
  Bruineberg et al. ([LIT-tmpxq8pk](../literature.d/LIT-tmpxq8pk.md)) and Raja et al. ([LIT-tmpumhsc](../literature.d/LIT-tmpumhsc.md)) argue,
  by different routes, that the Markov blanket of the free-energy
  literature is placed and not found. The formal core is [THEORY-tmpcv4h8](THEORY-tmpcv4h8.md):
  the partition takes the internal set as input. This account adds what
  the critiques show about practice. In Friston's soup ([LIT-526](../literature.d/LIT-526.md)) the
  graph was built from one kind of coupling and steady state was assumed
  when the run stopped. In published applications the blanket sits
  wherever the model needs it: in the receptors of a brain, the membrane
  of a bacillus, the beam joining two pendulums. The formalism also gives
  the same description to a membrane the cell makes and a beam nobody's
  states make. So the blanket presupposes the boundary it is offered as
  the criterion of. Proposed: the argument is conceptual, and the later
  steady-state definitions have not been read.
---
<!-- inactive-ok-file: THEORY-tmpm2o1r THEORY-tmplg7y1 THEORY-043 — Proposed; named as the accounts this one bears on, not leaned on -->

# THEORY-tmpnd5gh: A Markov blanket does not individuate a system: where it falls is fixed by modelling choices made before it is found, so it presupposes the boundary it is used to find, and it cannot represent a boundary the system produces

## Source

- Bruineberg, Dołęga, Dewhurst & Baltieri (2020 preprint), [LIT-tmpxq8pk](../literature.d/LIT-tmpxq8pk.md),
  read in [NOTE-tmp5ncd3](../notes.d/NOTE-tmp5ncd3.md): §4.2 (the soup re-run from Friston's code), §5.1
  (Friston blankets on an arbitrary graph; co-parents), §6 (the dilemma).
- Raja, Valluri, Baggs, Chemero & Anderson (2021 preprint), [LIT-tmpumhsc](../literature.d/LIT-tmpumhsc.md),
  read in [NOTE-tmp9snke](../notes.d/NOTE-tmp9snke.md): §3.1 (every thing, not everything), §3.2
  (placement), §3.3 (constitutive self-organization), footnote 17.
- Friston (2013), [LIT-526](../literature.d/LIT-526.md), read in [NOTE-421](../notes.d/NOTE-421.md): the account both critiques
  correct, and the simulation they examine.

## The claim

[THEORY-tmpcv4h8](THEORY-tmpcv4h8.md) shows that the blanket formalism takes the internal set
as an input. This account says where, in practice, that input and the
graph it is applied to come from. Each comes from a choice by the
modeller, made before the blanket is traced. A blanket found that way
cannot then serve as evidence of where the system ends. That is the sense
in which it presupposes the boundary it is used to find. A last clause
says what it misses even when well placed: a boundary that the system
itself produces looks, to the formalism, like any other conditional
independence.

## What was actually shown

**The soup's blanket rests on three choices.** Bruineberg et al. re-ran
the simulation of [LIT-526](../literature.d/LIT-526.md) from its published code. The adjacency matrix
was built from electrochemical coupling only, "while other forms of
influence included in the simulation (such as Newtonian forces) are
ignored". The eight most densely coupled nodes were declared internal.
Steady state was assumed at the time the run was stopped (§4.2, §6).
Calling the resulting ring of particles a membrane that the system has
is, for them, "a clear example of the reification fallacy". [NOTE-421](../notes.d/NOTE-421.md) had
already flagged the chosen k = 8, and this reading adds the other two
choices. That is evidence about one simulation, and it is the simulation
[LIT-526](../literature.d/LIT-526.md) offers as its demonstration.

**Published placements follow the model, not the system.** Raja et al.
compare three standard applications (§3.2). In a brain, the blanket is
the sensory and motor receptors. In a bacillus, it is the membrane and
the cytoskeleton. For two pendulums on a beam, the beam is the blanket,
while the sensory and active states are each pendulum's velocity and
position, properties of the pendulums rather than of the beam. "The
Markov blanket partition is stipulated as being located exactly wherever
happens to be convenient for the purposes of the model." Bruineberg et
al. add that co-parents are classed as sensory, active or ignored
depending on the author, and that which cause is most proximal is itself
model-relative (§5.1).

**The formalism cannot tell a made boundary from a given one.** A cell
makes its membrane. The pendulums do not make the beam, and the brain
does not make its receptors in the same sense. Raja et al. argue that the
blanket formalism "has no tools to account for" that difference (§3.3).
Of Friston's 2013 simulations specifically, they say they "assume the
existence of all the particles from the beginning and, therefore it
cannot be said that their blanket states are the product of the
activities of internal states" (footnote 17). That is the basis of the
record's narrow correction of [LIT-526](../literature.d/LIT-526.md)'s autopoiesis claim.

**Two routes, one conclusion.** Bruineberg et al. reach it by the
distinction between Pearl blankets on a map and Friston blankets claimed
for the territory. A realist use needs metaphysical premises "that may in
the end be doing all of the interesting work themselves". Raja et al.
reach it from scope. The blanket is a "trick" that supplies the
partition variational inference needs, so anything modelled with one
becomes an inferrer by construction (§3.5). Raja et al. cite the
Bruineberg preprint, and neither paper tests the other.

## What this does not say

- **It does not say the free energy principle is false.** Raja et al.
  grant it, "given these commitments, we think FEP is true", and
  Bruineberg et al. leave the mathematics alone. The claim concerns what a
  blanket can be used to conclude.
- **It does not say no system has a real boundary.** Cells have
  membranes. The claim is that the blanket formalism does not find them.
  It gets them from the modeller.
- **It does not settle the later formulations.** Definitions by sparse
  coupling at nonequilibrium steady state, and blankets whose states
  change over time, are known to the record only through the critiques'
  summaries. They are what promote_when asks about.
- **It does not decide the candle flame.** [LIT-526](../literature.d/LIT-526.md) excludes the flame
  because its molecular interactions do not persist (C7 in [NOTE-421](../notes.d/NOTE-421.md)), and
  Raja et al. accept that exclusion and turn it against the principle's
  scope. If this account is right, whether a flame "has" a blanket is a
  fact about a model of a flame, and [LIT-526](../literature.d/LIT-526.md) supplies none
  ([NOTE-tmp5ncd3](../notes.d/NOTE-tmp5ncd3.md)).
- **It is about individuation, not about the four unities of [ADR-024](../decisions.d/ADR-024.md).**
  The question is what makes something one system. No claim is made
  about selves, persons or the unity of experience.

## Connections

- **Extends [THEORY-tmpcv4h8](THEORY-tmpcv4h8.md)**, the formal core: from "the formalism takes
  the internal set as input" to "in practice the modeller supplies it,
  and the graph too".
- **Friston's criterion of the living ([LIT-526](../literature.d/LIT-526.md)).** The record holds no
  THEORY stating that a Markov blanket marks a living or lifelike system,
  so no relation is declared. Both critiques correct the LIT, and this
  account is the record's statement of why the criterion does not work
  as one.
- **[THEORY-tmpm2o1r](THEORY-tmpm2o1r.md)** offers the alternative. Closure of constraints
  ([LIT-tmpksq6n](../literature.d/LIT-tmpksq6n.md)) draws the boundary at the constraints the system itself
  produces, which is the "constitutive self-organization" Raja et al.
  say blankets miss. [NOTE-tmptk2u9](../notes.d/NOTE-tmptk2u9.md) records that no paper in the record
  compares the two criteria on one system.
- **[THEORY-tmplg7y1](THEORY-tmplg7y1.md) (minimal agency).** Barandiaran et al. ([LIT-tmp2zh8b](../literature.d/LIT-tmp2zh8b.md))
  require that an agent's individuality be defined by the system, not by
  an observer, and they reject statistical measures of influence as a
  criterion of interactional asymmetry. If this account is right, a
  Friston blanket meets neither requirement. It is drawn by the modeller,
  and the arrow structure Bruineberg et al. describe, borrowing
  Barandiaran's term "interactional asymmetry", is stipulated in the
  graph. It is not a modulation the system performs.
- **[THEORY-043](THEORY-043.md) (nesting).** [LIT-526](../literature.d/LIT-526.md) says the blankets of animals enclose
  those of organs and cells. [NOTE-421](../notes.d/NOTE-421.md) reads that nesting as bearing on
  [THEORY-043](THEORY-043.md)'s anti-nesting question. On this account, which blankets are
  drawn is chosen, so a nesting of blankets cannot by itself decide that
  question.
- **Coordination dynamics ([LIT-tmpw3fkg](../literature.d/LIT-tmpw3fkg.md)).** Raja et al. note that the
  coupled pendulums are already explained by their relative phase, the
  HKB treatment read through Kelso 2021. A blanket adds only a Bayesian
  redescription.
