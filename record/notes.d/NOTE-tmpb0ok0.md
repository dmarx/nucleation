---
status: Read
paper: 'LIT-tmp8z7y4'
title: 'Dollar and Howe — The highly adaptive SDM hand'
version: 1
history:
- version: 1
  date: '2026-11-05'
  note: >-
    Read on 2026-11-05 from the publisher's typeset PDF (SAGE), 14 pp. with
    the cover page, linked from the publications list of the Yale GRAB Lab,
    the first author's,
    https://www.eng.yale.edu/grablab/pubs/Dollar_IJRR2010.pdf, extracted
    with pdftotext -layout. Read: the abstract, §§1–4, Tables 1–4, figure
    captions and the appendix. Scanned only: the references. Not seen: the
    multimedia extension (video), and the figures as images. Quotes checked
    by string match against the extracted text. Page numbers are the
    journal's.
date: '2026-11-05'
summary: >-
  A four-fingered hand with elastomer flexure joints, compliance in parallel
  with one actuator, and a tendon transmission that lets fingers keep
  closing after contact, grasped objects under positioning errors as large
  as the object with open-loop, feed-forward control and no wrist: over
  100% of the object's size for a cylinder, over 45% for a block, and all
  48 camera-guided sphere trials. Power grasps only; no pinch grip.
---
<!-- inactive-ok-file: THEORY-tmp15pfs CLAIM-354 CASE-194 — Proposed, and new or held; cited from the reading of Dollar and Howe (2010) as open -->

# NOTE-tmpb0ok0: Dollar and Howe — The highly adaptive SDM hand

## Contribution

A gripper design in which passive mechanics, joint compliance, coupling
and an adaptive transmission, does work usually given to sensing and
closed-loop control, with one actuator; and a quantitative test of grasping
under positioning uncertainty, kept apart from sensing and control, which
the authors say had no precedent. It also reports the robustness of the
moulded construction (impact, drop, hammer, under water).

## Key insight

Leaving degrees of freedom unactuated but compliant lets contact with the
object choose the hand's shape. "An adaptive, underactuated hand has fewer
actuators than degrees of freedom." (§1, p. 585), and "This arrangement of
the compliance in parallel with the actuation is a key factor in the
effective performance of the hand." (§2.2, p. 588): the hand is soft before
the tendon is pulled and stiffens as it is.

## Assumptions

- **Quasi-static grasping**, with objects held in a force-sensor mount
  (experiment 1) or loosely placed (experiment 2); success judged by eye,
  no slip seen, after a 150 mm lift.
- **The hand alone**: a three-degree-of-freedom arm with no wrist, no
  sensing in the hand, the motor run feed-forward to stall. Symmetry of
  the grasp range in ±x is assumed, not tested (§3.1.3).
- **Power grasps of medium objects**: a cylinder of radius 24 mm, a
  block, spheres of radius 32 to 105 mm.
- **Design parameters from earlier work**: preshape angles of 25° and 45°,
  the joint stiffness ratio and a torque ratio of about 1.0 come from the
  authors' earlier optimization studies.

## Key results

- **One actuator** (abstract, p. 585): the hand grasps objects "of size,
  shape, mass, and position/orientation using only a single actuator."
- **Intended use** (§2, p. 586): "the robot simply positions the hand
  “close enough” to the target object, issues an open-loop “close”
  command, and the passive mechanics of the gripper take care of the
  rest."
- **The trade-off** (§2.2.1, p. 588): "However, as the torque ratio
  increases, the position range in which an object can be successfully
  grasped (the maximum allowable positioning error) is decreased."
- **Experiment 1** (§3.1.4, pp. 592–593): the cylinder was grasped "for a
  total allowable positioning error of over 100% of the object size in each
  direction", the block "for a total allowable positioning error of over
  45% of the object size."
- **Near the edge** (§3.1.4, p. 594): small changes of position "can lead
  to drastically different behaviors (jamming against the object face
  versus gently slipping to the side)."
- **Experiment 2** (§3.2.3, p. 596): with spheres located from one
  overhead webcam image, "The target objects were able to be successfully
  grasped for every trial", 48 trials, under positioning errors of 7.5 to
  33.5 mm.
- **Limits** (§4, pp. 596–597): "A major drawback of the current design is
  the lack of pinch-grip functionality of the hand", and "However, it is
  clear that greater numbers of degrees of actuation will be required as
  desired levels of dexterity increase."

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | One actuator through an adaptive transmission suffices for power grasps of a range of medium objects | moderate: a few objects, few trials | §3, Tables 1–4 |
| C2 | The hand tolerates positioning errors comparable to the object's size under open-loop control | moderate: three trials per grid point, success by eye | §3.1.4 |
| C3 | Raising the torque ratio narrows the grasp range | as reported from the authors' earlier optimization | §2.2.1 |

## Concepts

- **Underactuated hand**: fewer actuators than degrees of freedom, whose
  transmission lets other joints keep moving after contact stops a coupled
  link.
- **Successful grasp range**: the range of positioning error for which a
  grasp succeeds (§3.1.4), the paper's main measure.
- **Grasp equilibrium position**: where, without friction, the forces on an
  object centred in the closed hand would balance (p. 593).

## Connections

It applies the authors' earlier optimization of preshape, stiffness and
torque ratio, and compares damping and part count with their own earlier
hand. The paper does not use the terms "morphological computation" or
"embodied"; its one mention of morphology asks how the hand's should
change as actuators are added.

## Bearing on the record

- **The pasted synthesis on constraint architectures** cites it, as M9.
  Its quoted "accommodates a wide variety of objects using only one
  actuator" is right as a description (results above), within power grasps
  of objects from about 5.5 cm. Two corrections.
  - **"Morphological computation" is A's label, not the paper's.** The
    paper says compliance and adaptive coupling reduce the sensing and
    control needed. To say the body does part of the control work is a fair
    reading; "computation" overstates what is reported, which is mechanical
    accommodation of positional error.
  - **The hand has no pinch grip.** Small objects, a pen on a table, cannot
    be grasped (p. 596), so "a wide variety" is a variety of power grasps.
  A's "does not imply that the gripper has goals" agrees with the paper,
  which claims nothing of the kind. A also leaves out the torque-ratio
  trade-off and the abrupt changes of behaviour near the edge of the grasp
  range, both of which bear on freedom that is cheap but not uniform.
- **[CLAIM-345](../claims.d/CLAIM-345.md)** (equal controllability rank does not fix the cost of
  control): qualifies its frame. Coupling eight joints to one input shrinks
  the set of hand shapes that can be commanded, yet success under
  uncertainty rises, because contact selects the shape. What matters here
  is which degrees of freedom are left passive, not the cost of control.
- **[CLAIM-354](../claims.d/CLAIM-354.md)** (freedom in degrees along several dimensions): A's gloss
  calls them "several independent dimensions"; the claim does not say
  independent, and what it asserts is a partial order by inclusion of what
  can be viably reached. The hand supports the claim that robustness to
  disturbance and actuated reach, two of its listed dimensions, come apart.
- **[CASE-194](../cases.d/CASE-194.md)** (one failure from a shared actuator setting): qualifies.
  Here one shared actuator does not cause failure, because contact makes
  the shared command produce shapes fitted to each object. Passive
  adaptation is a repair the case does not list beside enlarging
  actuation.
- **[CLAIM-480](../claims.d/CLAIM-480.md)** (composing interactions yields effective constraints):
  supports in kind. The transmission couples the fingers so that contact on
  one constrains the motion of the others.
- [CLAIM-347](../claims.d/CLAIM-347.md), [CLAIM-365](../claims.d/CLAIM-365.md) and [CLAIM-079](../claims.d/CLAIM-079.md) bear on nothing in this paper.
- Filed: [THEORY-tmp15pfs](../theory.d/THEORY-tmp15pfs.md). No instruction for machine-learning practice;
  nothing for the anthology.

## Limitations

- **The authors'**: no pinch grip; sensing kept simple on purpose; more
  actuators needed for dexterity; success depends strongly on approach
  angle, and a wrist would help.
- **Small samples**: three trials per grid point and twelve per sphere,
  success judged by eye.
- **No like-for-like comparison** against a fully actuated or rigid hand in
  the same experiments.
- **Two inconsistencies**: the block is 84 mm square in the text (pp. 591,
  593) and 90 mm in the Fig. 9 caption; its allowable error is "over 45% of
  the object size" in the results and "up to 33% of the object size" in the
  conclusions (p. 596).

## Open questions

- How does the grasp range of the one-actuator hand compare with that of a
  fully actuated hand under the same open-loop control? The same grid
  experiment on both would say.
- How many actuators, and coupled how, does a pinch grip add without
  losing the tolerance of positioning error?
