---
number: 336
status: Active
formerly:
- THEORY-tmpabyf2
title: 'An ideal observer is optimal relative to the information it is given, so a constrained ideal is the optimal decoder of a degraded input, not a restricted decoder of the full one; comparing real observers with ideals taken at successive stages of the visual system places losses by stage, and in early-vision tasks human performance is reported often to parallel the retinal-stage ideal across conditions while falling well below it'
version: 2
history:
- version: 2
  date: '2026-10-30'
  note: >-
    Narrowed and promoted to Active under ADR-065, at the status review's
    ruling (the owner delegated these rulings). The old title read: "An
    ideal observer is optimal relative to the information it is given, so a
    constrained ideal is the optimal decoder of a degraded input, not a
    restricted decoder of the full one; comparing real observers with ideals
    taken at successive stages of the visual system places losses by stage,
    and in early-vision tasks human performance is reported to parallel the
    retinal-stage ideal across conditions while falling well below it".
    Geisler says human performance "often parallels ideal observer
    performance qualitatively (and sometimes quantitatively)", so "often" is
    restored (ADR-047 kind 3, this note only). The first two clauses follow
    from the review's equation (1) and the data-processing order of the
    stages; the third reports what the review says, read in full in
    NOTE-870, and nothing in the record contradicts it. The old promote_when
    read: "A primary study, read by the record, that computes ideal-observer
    performance for one visual task at successive stages of the visual
    system (stimulus, retinal image, receptor absorptions or ganglion-cell
    output) and measures human performance across the same conditions. It
    promotes the empirical clause if human performance follows the
    late-stage ideal across conditions while falling below it by a roughly
    constant factor; it refutes it if the pattern across conditions departs
    from that ideal's. Another review restating the logic, or a further fit
    of a single ideal at one stage, cannot settle it: the clause is about
    the comparison across stages." The review asserts the parallel itself,
    so that thesis moves to THEORY-1242, Proposed, which extends this
    entry and keeps the condition word for word (ADR-065 §3).
tags:
- cognition
- neuroscience
- probabilistic-modeling
date: '2026-10-15'
source:
- LIT-1055
summary: >-
  Geisler (2011), [LIT-1055](../literature.d/LIT-1055.md), read in [NOTE-870](../notes.d/NOTE-870.md). A review that defines the ideal observer
  as optimal "given the available information and any specified constraints", and
  writes it as an expected-utility argmax over the posterior given the stimulus S
  or a constrained representation Z = g(S;θ). Constraints are added one at a time
  (optics, receptor sampling and noise, ganglion-cell summation), and human
  performance that parallels the retinal-stage ideal while falling below it is read
  as loss in central factors. The empirical parts are the review's account of
  studies the record has not read. The review gives no formula for efficiency and
  no notion of an optimum over a restricted class of computations.
bears_on:
- QUESTION-103
---

# THEORY-336: An ideal observer is optimal relative to the information it is given, so a constrained ideal is the optimal decoder of a degraded input, not a restricted decoder of the full one; comparing real observers with ideals taken at successive stages of the visual system places losses by stage, and in early-vision tasks human performance is reported often to parallel the retinal-stage ideal across conditions while falling well below it

## Source

Geisler (2011), [LIT-1055](../literature.d/LIT-1055.md) (Vision Research 51(7), 771–781), read in [NOTE-870](../notes.d/NOTE-870.md) from
the NIH author manuscript (PMC3062724). Figures were not seen, and none of the
cited primary studies was read, so what they found is the review's account.

## What was actually shown

**The definition.** "An ideal observer is a hypothetical device that performs a
given task at the optimal level possible, given the available information and
any specified constraints." Equation (1): r_opt(Z) = argmax_r Σ_ω γ(r, ω) p(ω | Z),
with γ the utility of response r in world state ω. Constraints enter as
Z = g(S; θ), "the constraint function that specifies the mapping of the stimulus
into a neural representation"; with no constraint, Z is replaced by S. So there is
a family of ideals, one for each stage at which the input is taken, each
unrestricted in what it computes from its input. With accuracy as the utility in
a two-category task, equation (1) is the posterior-maximising rule.

**Locating losses.** The review's one explicit statement of the method: studies
"evaluated the additional effects on ideal observer performance of biological
constraints such as the optics of the eye, the spatial and chromatic sampling by
the photoreceptors, photoreceptor noise, and ganglion cell spatial summation".
Human performance "often parallels ideal observer performance qualitatively (and
sometimes quantitatively)", but "the suboptimal performance of human observers
implies substantial contributions of central factors." High external noise is
used to swamp early factors and "isolate the effects of some of the central
factors": for the template-matching ideal, squared threshold rises linearly with
squared rms noise contrast, human thresholds approximately follow above some
noise level, and the intercept gives "an equivalent internal noise".

**The asymmetry of the benchmark.** "When human performance approaches ideal
performance ... all hypotheses (model observers) that cannot approach ideal
performance can be rejected. When human performance is far below ideal, there
are generally a greater number of models than could explain human performance."

**Examples with numbers, as reported.** Ideal colour names on individual cone
mosaics correlate with subjects' names at r = 0.83; a natural-statistics decoder
of peripheral samples gives 42% lower mean squared error than linear
interpolation over 1000 images; the contour-occlusion ideal predicts
"approximately 99%" of the variance in seven subjects' responses.

**What could have come out otherwise.** Human performance across conditions
could have departed from the retinal-stage ideal's pattern, which would put the
loss somewhere the stage comparison does not reach. The review reports that it
often did not. This is the part the record has not checked at source.

## What this does not say

- **What efficiency is.** The review uses the word without a formula. The
  squared ratio of human to ideal d′ is from Burgess et al. 1981 and Pelli and
  Farell 1999, which the review cites and the record does not hold.
- **That the gap measures a bounded observer's restriction.** A constrained ideal
  here degrades the input, a garbling that loses information, and stays optimal
  on what remains. An observer restricted to a class of computations on an intact
  input is a different object. The two can come apart: a garbling that leaves
  total variation near one leaves the ideal near perfect, while a restricted class
  can sit at chance ([CLAIM-302](../claims.d/CLAIM-302.md)). The review's nearest thing to a restricted class
  is "degrading the ideal observer with hypothesized neural noise or with
  hypothesized heuristic computations", and comparisons with single named
  suboptimal rules in search, not with the best rule in a class.
- **That a gap below the ideal identifies its cause.** The review says the
  opposite: far-below-ideal performance leaves many models standing.
- **That every loss is in the input.** It names residual losses in the decision
  rule (spatial or channel uncertainty, which it counts as internal noise,
  nonlinearities, inefficient pooling), which no input garbling represents.
- **Anything about computational indistinguishability.** The review does not
  mention it, or treat computational limits except as noise, heuristics or a
  biophysical cost it names and does not develop.

## Connections

- [THEORY-031](THEORY-031.md): the two-category case of equation (1) is the likelihood-ratio rule
  at a prior-set threshold; consistent, adding nothing formally.
- [CLAIM-199](../claims.d/CLAIM-199.md) separates what a rendering makes possible for any receiver from what a
  receiver restricted to a rule class can use. Constrained ideals are the first
  kind, applied to stages of one system; [THEORY-349](THEORY-349.md) is the second kind.
- [QUESTION-103](../questions.d/QUESTION-103.md): efficiency, so defined, measures the first gap; a measure of the
  restricted-class gap on real observers is still wanting.
