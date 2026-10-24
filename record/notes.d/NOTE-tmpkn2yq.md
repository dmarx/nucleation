---
status: Read
paper: 'LIT-1146'
title: 'Jia, MirTabatabaei, Friedkin & Bullo — Opinion dynamics and the evolution of social power in influence networks'
version: 1
history:
- version: 1
  date: '2026-10-24'
  note: >-
    Read on 2026-10-24 from the version of record, SIAM Review 57(3):
    367–397 (published electronically 6 August 2015), a 31-page PDF in
    SIAM's typesetting posted on the last author's site
    (motion.me.ucsb.edu/pdf/2013d-jmfb.pdf, linked from fbullo.github.io),
    stamped "Redistribution subject to SIAM license or copyright"; SIAM
    allows authors to post the final published version on their own
    sites. The eScholarship copy that Unpaywall and Semantic Scholar list
    refused this client (403), and the paper is not on arXiv. Text
    extracted by pdftotext. Read: abstract, sections 1–6, figure captions,
    Appendix A and the statements of Appendices B–G. The proofs in
    Appendices B–G were skimmed, not checked step by step; figures were
    read from their captions. The reference list was not read. Page numbers
    below are the journal's.
date: '2026-10-24'
summary: >-
  DeGroot averaging on each issue, and between issues each member's
  self-weight is set to their share of control over the last consensus.
  With a fixed, strongly connected matrix of relative interpersonal
  weights, self-weights converge from every non-autocratic start to a
  unique equilibrium fixed by the eigenvector centralities: power ranks as
  centrality, accumulates at the top, is autocratic exactly for a star
  network and democratic exactly for a doubly stochastic one. Members
  whom no path reaches end with no power.
---
<!-- inactive-ok-file: CLAIM-tmpd6q2w CLAIM-440 CLAIM-364 CLAIM-277 — Proposed; the claims this reading bears on, named, nothing here rests on them -->
<!-- inactive-ok-file: LIT-tmpan19p LIT-1404 QUESTION-117 CASE-092 NOTE-tmp6p1t2 THEORY-tmphmdtd THEORY-tmp6h1sd — Deferred, Proposed or Open; the companion works, the question and case the LIT was filed for, and the readings filed today, named -->

# NOTE-tmpkn2yq: Jia, MirTabatabaei, Friedkin & Bullo — Opinion dynamics and the evolution of social power in influence networks

## Contribution

Friedkin (2011) proposed that a group member's self-weight on the next
issue follows their control over the last, and studied it by simulation.
This paper takes the simplest version, DeGroot averaging on each issue
with fixed relative interpersonal weights, writes it as an explicit map on
the simplex, and proves where it goes from every starting point. The
answer depends on one vector: the eigenvector centralities of the matrix
of relative weights.

## Key insight

"the evolution and limiting values of the self-weights depend only upon
the network structure" (p. 374). Who ends up with how much power is fixed
by who listens to whom, through the eigenvector centrality c, and not by
anyone's starting confidence. The reflected-appraisal loop amplifies
centrality: those above a threshold end with more power than their
centrality, those below with less.

## Assumptions

- **DeGroot on each issue (Eq. 2.1, p. 372).** y(s, t+1) = W(s)y(s, t),
  which reaches consensus w(x)ᵀy(s) on every issue. A member's social power
  is their weight w_i in that consensus.
- **Decomposition (Eq. 2.3, p. 373).** W(x) = diag(x) + (I − diag(x))C,
  where x is the vector of self-weights and C, the relative interaction
  matrix, is row-stochastic with zero diagonal and constant across issues.
- **Reflected appraisal (Eq. 2.6, p. 374).** x(s+1) = w(x(s)): the
  self-weight on the next issue is the control exerted over the last.
- **Separated time scales.** Consensus on an issue is reached before
  self-weights update (p. 374).
- **Perceived power is accurate.** Members know their control; for large
  groups the authors propose a distributed process by which each could
  estimate it (Eq. 2.7, p. 375).
- **C irreducible** (strongly connected) for the main theorem; Section 5
  treats reducible C with at least two globally reachable nodes and an
  aperiodic subgraph among them.

## Key results

- **Lemma 2.2 (p. 376).** The model is x(s+1) = F(x(s)), with
  F_i(x) = α(x) c_i / (1 − x_i) off the vertices, α normalising. The only
  parameter is c, the dominant left eigenvector of C.
- **Lemma 2.3 (p. 377).** No centrality exceeds 1/2; one reaches 1/2 if
  and only if the network is a star with that node at its centre.
- **Lemma 3.1 (p. 378), democracy.** If C is doubly stochastic (all
  c_i = 1/n), every non-autocratic start converges to equal self-weights
  1/n, and each consensus is the plain average. "If such structures are
  unusual, then so is a democratic equilibrium" (p. 376).
- **Lemma 3.2 (pp. 378–379), autocracy.** If C is a star, every
  non-autocratic start converges to the centre's full power; the consensus
  becomes the centre's initial opinion.
- **Theorem 4.1 (p. 380).** Otherwise, the equilibria are the n autocratic
  vertices and one interior point x*, whose entries are ordered as the
  centralities c; every non-autocratic start converges to x*.
- **Proposition 4.2 (pp. 380–381), accumulation.** There is a threshold
  c_thrshld: members above it end with power above their centrality, those
  below with power below it.
- **Reducible networks (Section 5, pp. 383–385).** Members not globally
  reachable, whom no path of influence from others reaches, have centrality
  0, and "the individuals who are not globally reachable in G(C) have zero
  social power in the equilibrium influence networks" (p. 384).
- **Examples (pp. 381–385).** Krackhardt's advice network of 21 managers:
  the four managers nobody asks for advice end with zero power; the top
  centrality, 0.205, becomes power 0.236. Simulations on networks of 101,
  141 and 4,031 nodes converge in four or five issues.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Under DeGroot–Friedkin dynamics with fixed C, self-weights converge to a unique equilibrium ordered by eigenvector centrality | strong: theorem | Theorem 4.1, Appendix F |
| C2 | Power accumulates above a centrality threshold | strong: theorem | Proposition 4.2 |
| C3 | Autocracy arises exactly for star networks, democracy exactly for doubly stochastic ones | strong: lemmas | Lemmas 2.3, 3.1, 3.2 |
| C4 | Members whom no path reaches end with zero power | strong for the stated reducible case | Section 5 |
| C5 | The mechanism describes real groups | weak: one small experiment cited (Friedkin 2011) | p. 386 |
| C6 | It explains Michels' iron law of oligarchy | weak: suggestive | p. 371 |

## Concepts

- **Social power**: "relative control over issue outcomes" (p. 370), the
  weight of a member's initial opinion in the consensus, after Cartwright.
- **Self-weight, self-appraisal**: x_i = w_ii, closure to interpersonal
  influence.
- **Relative interaction matrix C**: who accords how much of their
  openness to whom, held fixed.
- **Eigenvector centrality c**: the dominant left eigenvector of C.
- **Autocratic and democratic configurations**: a simplex vertex (one
  member with all power) and equal power 1/n.

## Connections

It formalises Friedkin's reflected-appraisal mechanism (2011, [LIT-1404](../literature.d/LIT-1404.md),
unread) and the Cooley hypothesis ([NOTE-1080](NOTE-1080.md)). Its empirical companion is
Friedkin, Jia & Bullo 2016 ([LIT-tmpan19p](../literature.d/LIT-tmpan19p.md), [NOTE-tmp6p1t2](NOTE-tmp6p1t2.md)), which uses
Friedkin–Johnsen rather than DeGroot dynamics and a matrix that changes
from issue to issue. It belongs with the record's DeGroot readings,
Golub & Jackson ([NOTE-840](NOTE-840.md); [THEORY-321](../theory.d/THEORY-321.md)), where a largest influence weight
that does not vanish keeps the consensus from the truth.

## Bearing on the record

- **[CLAIM-tmpd6q2w](../claims.d/CLAIM-tmpd6q2w.md) (coherence is not integration).** The claim names
  this model as the baseline: "Self-reinforcing authority is not itself
  new". The reading confirms that and gives the baseline two sharper
  edges.
  - **Consensus is built in.** Under DeGroot dynamics every issue ends in
    consensus whatever the distribution of power, so a coherent record is
    guaranteed and says nothing about whose evaluations it carries. The
    content of the consensus is the power-weighted average, and under the
    reflection loop that weighting moves toward the most central.
  - **Those nobody listens to vanish.** A member whom no path of influence
    reaches has zero power at equilibrium (Section 5). Their opinion is
    voiced and discarded, and the record of outcomes is unchanged by it.
    The paper's own reading: "the mechanism dampens protest movements
    assembled by individuals with low levels of relative control"
    (p. 386). This is the claim's thesis in a proved special case, with
    one difference the claim should keep: here the exclusion is of uptake
    by the network, not of admission by a regime, and nothing chooses it.
  - **Where the claim adds something.** In the model C is fixed and
    exogenous; nothing maintains or revises who is heard. The claim's
    maintained legibility regime is what the model leaves out, as the
    claim says.
  - Filed as [THEORY-tmphmdtd](../theory.d/THEORY-tmphmdtd.md).
- **[CLAIM-440](../claims.d/CLAIM-440.md).** A prevailing ordering read off this kind of record would be
  the most central member's, not the organization's.
- **[QUESTION-117](../questions.d/QUESTION-117.md) and [CASE-092](../cases.d/CASE-092.md).** The LIT was filed as the baseline these
  ask to be compared with. The comparison now has the model's exact form:
  fixed C, DeGroot consensus, x(s+1) = w(x(s)).
- **[CLAIM-277](../claims.d/CLAIM-277.md) and [CLAIM-364](../claims.d/CLAIM-364.md).** Authority made durable by its own exercise,
  in a social setting, and proved to concentrate.
- No instruction for machine-learning practice.

## Limitations

- **A model, with little test.** "an assessment of the validity of the
  model has just begun"; "The strength of tendency for larger groups and
  longer issue sequences is presently unknown" (p. 386).
- **Robustness unshown.** For anchored (Friedkin–Johnsen) dynamics the
  simulations show "a more pronounced tendency to autocracy"; "At the
  present time, we cannot assert robustness" (p. 386).
- **C is fixed.** Real groups change whom they listen to; the companion
  paper relaxes this in simulation only.
- **Accurate perception of one's power** is assumed: members "know their
  place" (p. 385).
- **Proofs skimmed, not checked** in this reading.

## Open questions

- Does the interior equilibrium survive anchoring, or do anchored groups
  always tend to autocracy, as the companion simulations suggest?
- What happens when C itself evolves, for example when members shift
  weight toward the powerful?
