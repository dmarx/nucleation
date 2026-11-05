---
status: Active
status_note: >-
  read 2026-11-05 ([NOTE-tmpu2xuw](../notes.d/NOTE-tmpu2xuw.md)) from the publisher's open-access PDF
  (CC BY-NC-ND 4.0), main text in full, most of Methods and all
  Supplementary Information skipped; worth reading as a clean engineered
  case in which the function a device computes, the arrangement that fixes
  the function, and the mechanism that changes the arrangement are separate
  parts. Its main limits: combinational logic only; outputs and the
  signals between gates are electrical and electromagnetic, and
  reconfiguration in the robot is done by a servo, not by the origami; the
  headline density of 1728 is a count for an unbuilt fourth-order cube; the
  gate savings are against the authors' own baseline counts.
title: 'Spatially programmable origami networks enable high-density mechanical computing for autonomous robotics'
version: 1
history:
- version: 1
  date: '2026-11-05'
  note: >-
    Registered and read on 2026-11-05 from the owner's pasted synthesis on
    FACT, rigidity, compliant mechanisms and origami (pasted 2026-11-04,
    written by another assistant), where it is cited as S6 by title, venue
    and DOI only. The citation was checked by the reader against Crossref
    and OpenAlex: Xinyu Hu, Ting Tan, Yinghua Chen and Zhimiao Yan, Nature
    Communications 16, 10209; received 1 April 2025, online 20 November
    2025, which is `published:` (no preprint found); PMC12635085.
    Correction: the synthesis omits the authors. Read from the publisher's
    PDF (https://www.nature.com/articles/s41467-025-64956-0.pdf), 15 pages,
    CC BY-NC-ND 4.0. Status Active.
tags:
- natural-sciences
date: '2026-11-05'
published: '2025-11-20'
doi: '10.1038/s41467-025-64956-0'
first_author: 'Hu'
keywords:
- 'origami'
- 'mechanical computing'
- 'reconfigurable logic'
- 'logic gates'
- 'Rubik''s cube'
- 'robotics'
implementations: []
summary: >-
  Hu, Tan, Chen & Yan (2025). A flat-foldable origami cell carrying
  conductors is a switch that conducts when folded (Buffer) or when not
  (NOT); two in series make AND, in parallel OR, and rotating them inside
  a gate switches between the two without rewiring. Gates cascade through
  electromagnets. A 30-gate array is reconfigured among a 2-bit adder,
  subtractor, comparator and multiplier, and a Rubik's-cube arrangement of
  elements changes its function by layer rotations; a built third-order
  cube switches between full adder and full subtractor, and a second-order
  cube rotated by a servo serves as a wheeled robot's decision module.
---
<!-- inactive-ok-file: THEORY-tmp4458t — Proposed; cited from the reading of Hu et al. (2025) as open -->

# LIT-tmpmjw68: Spatially programmable origami networks enable high-density mechanical computing for autonomous robotics

Hu, X., Tan, T., Chen, Y. & Yan, Z. (2025). Spatially programmable origami networks enable high-density mechanical computing for autonomous robotics. *Nature Communications* 16: 10209. doi:10.1038/s41467-025-64956-0.

## Key takeaways

*From the reading, [NOTE-tmpu2xuw](../notes.d/NOTE-tmpu2xuw.md).*

- **Reconfiguring by moving elements.** "By rotating intra-gate elements to
  modify AND/OR-based Boolean cascades, the design reduces gates by 46.7%
  compared to standard arrays" (abstract).
- **A counted density.** Cubes of order two to four reach "4.5, 81, and
  1728" functions per element by counting; the third-order cube was built.
- **Electromechanical.** "The system employs electromagnetic actuation for
  force input generation and electrical signal output".
- **External reconfiguration.** In the robot, the half-subtractor's output
  decides whether the cube switches to half-adder logic, but a servo
  rotates the layer.

## Standing in the record

Cited in the pasted synthesis on constraint architectures as S6, by
title, venue and DOI only, with no characterization to check. Read as a
physical case for [CLAIM-025](../claims.d/CLAIM-025.md): the function computed, the arrangement fixing
it and the mechanism that rearranges it are separate hardware. It is an
engineered electromechanical computer, not a case of embodied cognition.
Filed from it: [THEORY-tmp4458t](../theory.d/THEORY-tmp4458t.md). No instruction for machine-learning
practice; nothing for the anthology.
