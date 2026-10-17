---
number: 523
status: Proposed
formerly:
- THEORY-tmpfj3d3
promote_when: >-
  A formal treatment of IIT 4.0's algorithm, as Albantakis et al. specify
  it, that either proves it undefined for dynamics with a non-Markovian
  graining or gives the unique next-state distribution it would use; and an
  analysis of brain dynamics at the spatial, temporal and state grainings
  IIT's maximisation would range over, showing whether they are Markovian.
  The first half is promoted if the proof stands and the grainings are
  non-Markovian; the account is refuted if Φ is computed, by the theory's
  own algorithm and with a stated error bound, for a realistic model of a
  real nervous system. A further correlation between PCI or another
  integration measure and conscious state cannot settle it, since such
  measures are proxies on this account whatever they correlate with.
title: "IIT 4.0's measure of integrated information is undefined for any system that has a non-Markovian graining, which brains are said to have under the grainings in use, and it has never been computed for a real physical system; so empirical measures such as PCI are proxies for it, not approximations, and their success is evidence for IIT's intuitions about integration, not for Φ"
version: 1
tags:
- consciousness
- information-theory
date: '2026-10-16'
source:
- LIT-185
summary: >-
  Barrett, Milinkovic, Mediano, Rosas, Bor, Barnett & Seth (2026), [LIT-185](../literature.d/LIT-185.md),
  read in full in [NOTE-122](../notes.d/NOTE-122.md). A position paper by sympathetic insiders, with
  no new formal result. The ill-definedness is restated from Barrett &
  Mediano (2019), which the record does not hold. That brains are
  non-Markovian under typical grainings rests on one 1998 citation about
  ion-channel currents. The proxy point follows from a definition: an
  approximation needs a well-defined target and an error bound. The paper's
  defences of IIT (the multi-dimensional measure, the "proto-consciousness"
  panpsychism) are revisions of the theory, not readings of it.
---
<!-- inactive-ok-file: THEORY-023 THEORY-043 THEORY-100 THEORY-240 THEORY-262 THEORY-296 THEORY-577 THEORY-644 — Proposed; accounts named as rivals, neighbours or connections, not leaned on as premises -->

# THEORY-523: IIT 4.0's measure of integrated information is undefined for any system that has a non-Markovian graining, which brains are said to have under the grainings in use, and it has never been computed for a real physical system; so empirical measures such as PCI are proxies for it, not approximations, and their success is evidence for IIT's intuitions about integration, not for Φ

## Source

Barrett, Milinkovic, Mediano, Rosas, Bor, Barnett & Seth (2026),
"Integrated information theory: the good, the bad and the misunderstood",
arXiv:2604.11482, [LIT-185](../literature.d/LIT-185.md), read in full in [NOTE-122](../notes.d/NOTE-122.md).

## What was actually shown

**What the algorithm needs (§2).** IIT 4.0 (Albantakis et al. 2023)
computes system integrated information φs, the cause-effect structure and
structure integrated information Φ from the probabilities of past and
future states given the present states of parts, under a uniform prior,
with spatial, temporal and state grainings chosen to maximise φs and Φ.

**Ill-definedness (§5.1.1).** The formulae need P(future | present) under
each graining. For a non-Markovian graining that distribution is not fixed
by the present state, so "the IIT algorithm is therefore not well-defined
whenever there is at least one non-Markovian graining", and it "does not
produce an output for brains". Two proposed fixes are said to fail: a
uniform prior over the whole past does not converge for non-ergodic
dynamics such as a random walk (Barrett & Mediano 2019), and Kleiner &
Tull's future trajectories leave one part's evolution unspecified given no
knowledge of another's present state.

**Further gaps (§5.1.2).** The maximum-entropy prior is undefined for
continuous state variables, such as membrane potential, without hard
bounds. The maximisation over all grainings "has never been"
investigated. Every application so far is to finite, binary, Markovian
units assumed indivisible.

**Proxies, not approximations (§5.2).** A approximates B only if both are
well defined and a bound on |A − B| can be given; Newton approximates
general relativity in this sense, while GDP is a proxy for living
standard. Since Φ is undefined for a brain, nothing approximates it.
Existing measures, PCI included, are "operational proxies for at most two
of the total set of six" axioms. Candidate empirical Φ measures disagree,
"often moving in different directions under the same change of
parameters" (Mediano et al. 2019).

**What the evidence then supports (§3.1).** TMS-EEG responses are local and
stereotyped under anaesthesia, sleep and disorders of consciousness, and
diverse and spreading in conscious states. These results are "equally
compatible with alternative weaker versions of IIT, as well as, arguably,
with other theories".

**What could have come out otherwise.** A well-defined conditional
distribution could have been specified for non-Markovian grainings, or Φ
could have been computed for some real system. The paper reports that
neither has been done.

## What this does not say

- **That IIT is false.** The axioms are explicitly left uncontested (§6),
  and the authors recommend weak IIT, explanatory correlates without the
  identity claim, as a way to test its intuitions. What the paper denies is
  that strong IIT currently returns a verdict on any real system.
- **That the formal case is established here.** The non-Markovian argument
  is restated from Barrett & Mediano (2019), not proved in this paper, and
  the record does not hold that paper. The claim that brain dynamics are
  non-Markovian under the grainings IIT would use rests on one citation
  about ion-channel current fluctuations (Fuliński et al. 1998), and those
  grainings are not examined ([NOTE-122](../notes.d/NOTE-122.md), C2).
- **That "high Φ = more consciousness" is a misreading.** The paper concedes
  that "IIT does state that Φ corresponds to the quantity of consciousness"
  (§4.1). Its multi-dimensional global-state suite is a proposed revision.
  So is its verdict that an inactive expander grid is only minimally
  conscious: §4.1 grants that IIT gives the grid high Φ when first
  assembled ([NOTE-122](../notes.d/NOTE-122.md), Corrections).
- **That IIT's panpsychism is unproblematic.** The paper derives a gapless,
  shifting tiling of space-time by non-overlapping substrates from the
  exclusion axiom (§4.2). Its defence is comparative: materialism has an
  explanatory gap too. It does not address the combination problem or the
  anti-nesting objections ([THEORY-043](THEORY-043.md), [THEORY-644](THEORY-644.md)).
- **That IIT has no achievements.** The paper credits it with qualitative
  structure-to-phenomenology accounts on toy systems: a 2-D grid entails
  spatial extension, a directed chain temporal flow (§3.2). Those do not
  need Φ to be computed.

## Connections

- IIT 3.0 ([LIT-445](../literature.d/LIT-445.md)) is the formal statement [THEORY-043](THEORY-043.md) cites for the
  exclusion postulate. [THEORY-262](THEORY-262.md) (Tononi, Sporns & Edelman's neural
  complexity) and [THEORY-240](THEORY-240.md) (integrated information between default-mode
  gateways under propofol) report measures of the kind this paper calls
  proxies.
- [THEORY-100](THEORY-100.md) records the claim that PCI is a substitute for Φ; this account
  is the reason to read that as a proxy relation.
- [THEORY-296](THEORY-296.md) (no sustained posterior synchronization in the COGITATE test)
  tested a prediction IIT's proponents made, not a Φ value; the paper's
  Discussion says the same of COGITATE.
- The meta-problem challenge ([THEORY-577](THEORY-577.md)) is an independent objection
  to Φ as the basis of consciousness: a zero-Φ simulation would report
  alike. Kleiner & Ludwig's criterion ([THEORY-498](THEORY-498.md)) is the test IIT's
  toy structure-to-phenomenology results would have to pass.
- [THEORY-023](THEORY-023.md) cites this paper only as a defence against the expander-grid
  objection. Its §5 adds that IIT currently gives no verdict on any AI
  hardware, only on toy systems.
