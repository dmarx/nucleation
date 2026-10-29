---
number: 1092
status: Proposed
formerly:
- THEORY-tmpy95x7
promote_when: >-
  A localization procedure stated in advance, not read by eye, applied to
  the discrepancies d_V(s(V), S(V ⊆ U)s(U)) over the sensor domains and
  tested over many trials with stated detection and false-alarm rates;
  including cases where the fault is in a restriction map (a sensor model
  or calibration) rather than in a measurement, so that it shows whether
  the two can be told apart. A single case where the largest residuals
  share a sensor does not settle it, and neither does a large consistency
  radius, which says that something is wrong and not where.
title: 'Read over the sensor domains, the discrepancies between each observation and the restrictions of others can single out a faulty sensor where the consistency radius alone does not: in Robinson''s simulated search, a 2° bearing bias was attributed to the right sensor, without prior knowledge of it, because every large discrepancy involved that sensor''s domains, while the radius was lower than in the unbiased case'
version: 1
tags:
- mathematics
- information-theory
date: '2026-10-27'
source:
- LIT-1658
summary: >-
  Robinson (2017), [LIT-1658](../literature.d/LIT-1658.md), Example 24, Case 2 (pp. 26–28 of arXiv
  v3), read in [NOTE-1221](../notes.d/NOTE-1221.md). One simulated case, one noise realization,
  read from a figure. Proposed until a stated procedure is tested over
  trials, including faults in the restriction maps, which enter the
  discrepancies in the same way as faults in the data.
---

# THEORY-1092: Read over the sensor domains, the discrepancies between each observation and the restrictions of others can single out a faulty sensor where the consistency radius alone does not: in Robinson's simulated search, a 2° bearing bias was attributed to the right sensor, without prior knowledge of it, because every large discrepancy involved that sensor's domains, while the radius was lower than in the unbiased case

## Source

Robinson (2017), [LIT-1658](../literature.d/LIT-1658.md), Example 24 (pp. 25–29 of arXiv
1603.01446v3), Tables 1–2 and Figures 11–13; read in [NOTE-1221](../notes.d/NOTE-1221.md).

## What was actually shown

**The setup.** A simulated search for a downed airliner, with a sheaf whose
restrictions are geometric maps between positions, velocities, crash time
and RDF bearings (Example 11, p. 16). Three cases, each one realization of
simulated noise. The true crash site was withheld from the model (p. 25).

**Case 2.** As Case 1, with RDF sensor 2 "biased southward by 2°". "This
error is immediately detectable in Figure 12(a) as an anomalously high
error between the Field office (X) and the RDF sensor 2 (U4). Since the
only high errors occur between sensor domains involving RDF sensor 2 (U4
and V2), the sheaf model makes it clear that the errors are due exclusively
to RDF sensor 2. It should be noted that Figure 12(a) does not include any
a priori knowledge of the sensor bias" (p. 28).

**The radius did not do it.** The consistency radius was 11.6 km in Case 2
and 15.7 km in Case 1, which had no bias (Table 1, p. 26). The bias showed
in where the discrepancies sat, not in their maximum. In Case 1 too,
"nearly all the error is concentrated in two places" (p. 28). In Case 3,
with a wrong velocity added, the radius rose to 152 km, "an indication
that something is amiss" (p. 29), but the text does not localize the
velocity error.

What could have come out otherwise: the large discrepancies could have been
spread over domains that share no sensor, or have pointed at the wrong one.
In this one case they did not.

## What this does not say

- **That localization works in general.** One case, one realization, read
  by eye. No procedure, threshold or error rate is given.
- **That a measurement fault can be told from a model fault.** The
  restriction maps are fixed and trusted (Axiom 5, p. 15). A 2° bias in one
  bearing gives the same discrepancy as an error in that station's
  coordinates inside maps B and D (p. 16). The paper's attribution to the
  sensor rests on trusting the map.
- **That the residuals find inadequate models.** The paper gives that role
  to higher cohomology, which uses no data (pp. 3, 34).
- **That the system recalibrates.** Nothing is revised from the residuals:
  fusion replaces the data by the nearest global section and leaves the
  maps alone. [QUESTION-285](../questions.d/QUESTION-285.md)'s description of the paper as sensor
  networks that "recalibrate from consistency residuals" goes beyond it.
