---
number: 166
status: Proposed
formerly:
- CLAIM-tmpkdc9t
title: 'A lower-level collective within the composite person, such as the gut microbiome, can at times drive higher-level behaviour and even experience: the routes exist and the effects are causal in rodents, while the human evidence is modest'
version: 2
history:
- version: 2
  date: '2026-10-16'
  note: >-
    THEORY-560 now states, from LIT-915, what this claim relied on
    for affect: the routes and the causal effects in rodents, and the
    modest, partly null human evidence. It is added to the grounds. The
    claim is unchanged.

role: thesis
warrant: empirical
defeated_if: >-
  Evidence that in humans the microbiome's influence on hunger and affect runs
  only through states the higher level already sets, such as diet chosen, stress
  already present, so that the microbiome mediates but never originates a change
  in drive.
tags:
- agency
- self
- ecology
date: '2026-10-11'
line: distributed-agency
uses:
- TERM-051
- TERM-045
- TERM-049
grounds:
- LIT-903
- LIT-915
- CASE-047
- THEORY-560
complements:
- CLAIM-316
summary: >-
  The owner's thesis of 2026-10-11: "'who drives' isn't a constant.
  Considering myself as a multi-level agent, part of my composition is my
  microbiome ... that lower level collective is capable of influencing my
  higher level behavior and even phenomenological experience." The time
  claim is filed as the owner's. The microbiome claim is grounded in two
  reviews read the same day. The routes exist, and the effects are
  causal in rodents. The human evidence is modest: associations, small
  effects on subjective stress, and nulls.
illustrated_by:
- CASE-047
bears_on:
- QUESTION-033
---
<!-- inactive-ok-file: THEORY-560 — Proposed; the account of the gut–brain evidence this claim relied on, added to its grounds -->
<!-- ref::uses-file: TERM-045 — stated in "self, and which sense"; the body applies the term without naming it -->
<!-- inactive-ok-file: CLAIM-027 CLAIM-159 — Proposed; the will-line claims that give non-constancy its home, open -->
<!-- inactive-ok-file: THEORY-045 — Proposed; the felt-affect reading through which microbial influence reaches experience, untested -->

# CLAIM-166: A lower-level collective within the composite person, such as the gut microbiome, can at times drive higher-level behaviour and even experience: the routes exist and the effects are causal in rodents, while the human evidence is modest

## The claim

The owner, verbatim: "I think it's probably also worth noting that 'who
drives' isn't a constant. Considering myself as a multi-level agent, part of
my composition is my microbiome. my understanding is that my microbiome can
impact things like my affect and level of hunger, so that lower level
collective is capable of influencing my higher level behavior and even
phenomenological experience."

There are two parts:
1. **Drive profiles are time-indexed** ([TERM-051](../terms.d/TERM-051.md)). Who drives changes:
   by state (hungry or sated, stressed or calm), by task, and by regime.
   That is what the will line calls a change in which regime is effective
   ([CLAIM-027](CLAIM-027.md), [CLAIM-159](CLAIM-159.md)).
2. **Drive can come from below, from a collective of other organisms.** The
   composite person includes a microbial community, by the holobiont
   reading the record holds for corals ([LIT-709](../literature.d/LIT-709.md)). That community can move
   the person's hunger and affect.

## What the evidence shows

From the two reviews read for this claim:
- **Routes exist.** There are microbial metabolites and protein mimics of
  host appetite peptides ([LIT-903](../literature.d/LIT-903.md)). And "The vagus nerve is the most
  direct route of communication between the gut and the brain, thus
  enabling bidirectional communication" ([LIT-915](../literature.d/LIT-915.md)).
- **Causal effects in animals are real.** Germ-free and colonization studies,
  and faecal transplant from depressed humans into rodents ("at least
  partial transfer of the clinical psychiatric phenotype").
- **In humans the evidence is modest.** For appetite, the field "is mainly
  based on in vitro studies and rodent models", and the clean human effects
  are of delivered metabolites. For affect, a meta-analysis shows reduced
  *subjective* stress in healthy volunteers, beside clean nulls for strains
  with strong preclinical records.

So "can drive" is established in animals and plausible in humans. "Does
drive, in my everyday hunger and mood" is not yet shown. The claim stays
Proposed on that ground, not on the conceptual point, which the record
accepts.

## What it adds to the drive profile

- **The lower level is itself a collective.** The owner's "lower level
  collective" is a community, not a part with a single will. Its own drive
  profile may be diffuse.
- **Its membership is disputable.** Whether the microbiome is part of the
  person is [QUESTION-035](../questions.d/QUESTION-035.md) again. On the threshold criterion it is part
  of the combined form ([TERM-049](../terms.d/TERM-049.md)), relative to targets such as hunger, if host–microbe
  coupling clears the gap. This is the holobiont case.
- **It reaches experience.** If felt affect reports the body's regulatory
  state ([THEORY-045](../theory.d/THEORY-045.md)), a microbial change in that state is a change in
  experience that originates below the person.

## What it does not say

- **That the microbiome is an agent.**
- **That its influence is against the host's interest.** The appetite review's
  framing is mutualist.

## Note of 2026-10-15: split under [ADR-043](../decisions.d/ADR-043.md)

[ADR-043](../decisions.d/ADR-043.md)'s classification found this claim compound: its first part,
that a person's drive profile is time-indexed, is the owner's thesis,
argued from the drive-profile term and the will line and supported by no
observation the record holds (interpretive), while its second part,
that the microbiome can drive hunger and affect, rests on two reviews
(empirical). The first part is now [CLAIM-316](CLAIM-316.md), which this claim complements.
This claim keeps the microbiome part and stays empirical. Its title,
which led with "'Who drives' is not constant", was changed to state the
microbiome part with the scope the evidence gives it; the second
disjunct of its defeat condition, stable drive profiles over successive
windows, is [CLAIM-316](CLAIM-316.md)'s.
