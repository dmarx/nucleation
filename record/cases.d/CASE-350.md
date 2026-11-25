---
number: 350
status: Proposed
formerly:
- CASE-tmp5fglr
title: 'Integrated information for a mind and a group'
statement: >-
  Autoregressive integrated information with the exclusion rule, applied by
  one procedure to linear models of a modular mind and of a group of such
  minds, makes the whole the subject only when coupling across its seams
  outweighs its parts' own integration, in both models alike
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-063 as a delegated
    lead worker. Code, tests and results are committed under
    scratch/studies/lead-063/.
standing: documented
kind: executed-study
tags:
- consciousness
- mereology
- information-theory
- phenomenal-unity
date: '2026-11-22'
line:
- evidence-for-experience
bears_on:
- QUESTION-046
draws_on:
- THEORY-043
- THEORY-063
summary: >-
  [LEAD-063](../leads.d/LEAD-063.md) asked for one integration measure, or an anti-nesting rule, to be
  applied to a modular-mind model and to a group model. The measure is
  Barrett and Seth's autoregressive integrated information (Phi_AR) at the
  minimum information bipartition, computed exactly for linear Gaussian
  networks; the rule is IIT's exclusion postulate, which makes the candidate
  of largest Phi the subject and denies it to what it contains or is
  contained in. The mind is three modules of three units; the group is three
  such minds, each unified by the rule, built the same way one level up.
  Sweeping the coupling between parts, the whole wins in both models once
  coupling across its seams passes a threshold, and its parts lose; below
  it, the parts win. At matched coupling the whole's Phi is nearly the same
  in both models (0.0047 and 0.0049 nats at 0.05 and one link); the group's
  threshold is higher (0.13 to 0.21 against 0.08 to 0.13) only because its
  members are more integrated than the mind's modules. Near a threshold one
  added link flips the verdict. An exhaustive search on a 12-unit group
  finds, at one setting, a subject made of one member and part of the
  other. The rule separates tightly from loosely coupled wholes, not minds
  from groups. The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-043, CLAIM-927 — Proposed or new; the accounts the study tests and the claim it grounds -->

# CASE-350: Integrated information for a mind and a group

## What was done

[QUESTION-046](../questions.d/QUESTION-046.md) asks for "an integration or dynamic-core measure, or an anti-nesting rule justified on other grounds, actually applied to a modular-mind model and to a group model". [THEORY-043](../theory.d/THEORY-043.md) says the architectural route would have to separate a modular mind from a nation "by degree, and nobody here computes the degree for either". This study computes it, for one measure and one rule, in the simplest models that have the structure at issue.

**Measure.** Barrett and Seth's autoregressive integrated information (Phi_AR; Barrett and Seth 2011, PLoS Computational Biology 7, e1001052, not registered in the record): for a set of units S cut into parts M1 and M2, phi is the information S carries about its own last state minus what M1 and M2 each carry about theirs. Phi(S) is phi at the cut minimizing phi divided by the smaller part's size. For a stationary linear Gaussian system X(t+1) = A X(t) + noise every term has a closed form in the stationary covariance, so nothing is sampled.

**Rule.** IIT's exclusion postulate, the anti-nesting rule [THEORY-043](../theory.d/THEORY-043.md) names: of candidates that overlap, the one of largest Phi is the subject.

**Models.**

- *Modular mind*: three modules of three units. Inside a module every pair is coupled with weight 0.12. Each pair of modules is joined by one, two or three reciprocal links of weight c.
- *Group*: three members, each that modular mind with c = 0.15 and three links (a unified mind by the rule: its Phi, 0.072 nats, exceeds each module's, 0.035). Each pair of members is joined by one, two or three reciprocal links of weight g.

The group is the mind's construction run one level up, with minds where modules were, so one procedure and one parameter, coupling times bandwidth across the seams between parts, apply to both. Couplings were swept from 0 to 0.25 in steps of 0.01, under the size-normalized cut and, as a check, the unnormalized one. Candidates were the natural levels (module, mind; module, member, group), and two exhaustive searches over every subset checked that restriction: all 502 subsets of the 9-unit mind, and all 4083 of a 12-unit group of two members of two modules each. For the 27-unit group the cut was searched along module seams and single units, and a test confirmed that 200 random cuts never score lower. Code, 15 passing tests, results and a rerun recipe are in scratch/studies/lead-063/.

## Results

Smallest coupling at which the whole is the subject (size-normalized cut):

| Links between each pair of parts | Mind (between modules) | Group (between members) |
|---:|---:|---:|
| 1 | 0.13 | 0.21 |
| 2 | 0.09 | 0.16 |
| 3 | 0.08 | 0.13 |

Below its threshold each model's parts are the subjects: the mind's modules, the group's members. Above it the whole is, and its parts are excluded; in the group, the members' own Phi falls as g rises (0.072 to 0.056 at g = 0.2, three links). The whole's Phi depends on the seams almost alone: at coupling 0.05 with one link it is 0.0049 nats for the mind and 0.0047 for the group, at 0.10 0.0193 and 0.0184. The thresholds differ because the group's parts are minds, more integrated than modules (0.072 against 0.028 nats), not because they are minded.

- **One link flips the verdict.** At g = 0.15, two links between members leave three subjects and three make one, with each member excluded; the mind flips the same way at c = 0.10 between one link and two. This is Schwitzgebel's single-ballot reductio ([THEORY-043](../theory.d/THEORY-043.md), from [NOTE-131](../notes.d/NOTE-131.md)) produced in a model.
- **The subject need not follow persons.** In the exhaustive 12-unit group, at g = 0.15 with three links, the set of largest Phi is one member plus two units of the other; with six links it is the whole group. In the 9-unit mind with one link at c = 0.12 it is the three linked units, one from each module, not a module or the mind.
- **Unnormalized cut.** The whole wins less often, in both models: never with one link; with two, never for the mind and from 0.22 for the group; with three, at the same couplings as before.
- **Outside the modular range.** At couplings above about 0.21 with three links, links between parts outweigh coupling inside them, the parts stop being parts, and Phi_AR turns negative near instability. These settings are reported in the results file and not interpreted.

## What it shows

Applied by one procedure, this measure and rule do not put a modular mind and a group on different sides as such. They put a whole on the subject side when integration across its weakest seam exceeds that of its most integrated part, in either model, and a loosely coupled modular mind is denied unity just as a loosely coupled group is. A real mind and a real group would fall on different sides only if their seams differ enough in coupling and bandwidth relative to their parts, which is an empirical matter about brains and groups that this study does not settle. This computes the "degree" [THEORY-043](../theory.d/THEORY-043.md) said nobody computes, and confirms its cost for the architectural route. [CLAIM-927](../claims.d/CLAIM-927.md) states the finding.

## Limits

- One measure, Phi_AR, a Gaussian proxy and not IIT 3.0 or 4.0's Phi; it can be negative, and is near instability.
- Linear, symmetric, noise-driven models with three units per module; real modules and persons are vastly larger and nonlinear, and a group's links are slow, symbolic and intermittent, which a one-step linear coupling does not capture.
- Candidates were restricted to the natural levels in the 27-unit group; the exhaustive 12-unit check shows the true subject can be a set straddling members, which the restricted search cannot find.
- The cut normalization is a choice, and the unnormalized cut changes thresholds, though alike in both models.
- No empirical estimate of coupling between brain modules or between people is used, so where real minds and groups fall is left open.
