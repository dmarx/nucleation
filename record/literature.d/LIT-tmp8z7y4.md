---
status: Active
status_note: >-
  read 2026-11-05 ([NOTE-tmpb0ok0](../notes.d/NOTE-tmpb0ok0.md)) from the publisher's PDF posted on the
  publications page of the first author's lab at Yale; worth reading as a
  clear hardware case of passive mechanics standing in for sensing and
  control: a four-fingered hand with compliant joints and an adaptive
  tendon transmission, one actuator for eight joints, grasping under
  positioning errors as large as the object, with open-loop control. Its
  main limits: power grasps of medium objects only (no pinch grip, so small
  objects fail), small samples judged by eye, no comparison against a fully
  actuated hand in the same experiments, and two internal inconsistencies in
  the reported block size and allowable error.
title: 'The Highly Adaptive SDM Hand: Design and Performance Evaluation'
version: 1
history:
- version: 1
  date: '2026-11-05'
  note: >-
    Registered and read on 2026-11-05 from the owner's pasted synthesis on
    FACT, rigidity, compliant mechanisms and origami (the pasted synthesis
    on constraint architectures, written by another assistant, A, in the
    same exchange as the emergency-readiness bibliography, pasted
    2026-11-04), which cites it as M9, Dollar & Howe 2010, "The Highly
    Adaptive SDM Hand", IJRR, doi:10.1177/0278364909360852. Citation
    checked against Crossref: Aaron M. Dollar and Robert D. Howe, The
    International Journal of Robotics Research 29(5), 585–597, April 2010,
    journal article; published online 2 February 2010, which is
    `published:` (the PDF's cover says "OnlineFirst Version of Record -
    Feb 2, 2010"). A's citation is right apart from dropping the subtitle.
    Not held before (no hit for the DOI, "SDM Hand" or the authors).
    OpenAlex lists it as closed access at SAGE, which was not tried. Copy:
    the publisher's typeset PDF, 14 pp. with the cover page, linked from the
    publications list of the Yale GRAB Lab, the first author's,
    https://www.eng.yale.edu/grablab/pubs/Dollar_IJRR2010.pdf, extracted
    with pdftotext -layout; no licence for the posting is stated. Status set
    to Active.
tags:
- control-theory
- embodied-cognition
date: '2026-11-05'
published: '2010-02-02'
doi: '10.1177/0278364909360852'
first_author: 'Dollar'
keywords:
- 'underactuated hand'
- 'adaptive grasping'
- 'shape deposition manufacturing'
- 'compliant joints'
- 'positioning error'
- 'robot hand design'
implementations: []
summary: >-
  Dollar & Howe (2010). A four-fingered gripper made by polymer Shape
  Deposition Manufacturing, with rigid links and elastomer flexure joints
  moulded as one part, is driven by a single actuator through a tendon and
  pulley transmission that lets fingers and joints keep closing after
  others are stopped by contact. Compliance is in parallel with the
  actuator. Mounted on an arm with no wrist and run open loop, it grasped a
  cylinder under total positioning errors of over 100% of the object's
  size, a block over 45%, and four spheres located from one webcam image in
  all 48 trials, with positioning errors of 7.5 to 33.5 mm. It cannot pinch,
  so small objects fail.
---
<!-- inactive-ok-file: THEORY-tmp15pfs — Proposed and new; cited from the reading of Dollar and Howe (2010) as open -->

# LIT-tmp8z7y4: The Highly Adaptive SDM Hand: Design and Performance Evaluation

Dollar, A. M. & Howe, R. D. (2010). The Highly Adaptive SDM Hand: Design and Performance Evaluation. *The International Journal of Robotics Research* 29(5): 585–597. doi:10.1177/0278364909360852.

## Key takeaways

*From the reading, [NOTE-tmpb0ok0](../notes.d/NOTE-tmpb0ok0.md). Page numbers are the journal's.*

- **One actuator, eight joints.** "A single actuator drives the four
  fingers (eight joints) of the hand." (§2.2, p. 588).
- **Mechanics in place of control.** In use "the robot simply positions
  the hand “close enough” to the target object, issues an open-loop
  “close” command, and the passive mechanics of the gripper take care of
  the rest." (§2, p. 586).
- **Large tolerance of error.** The cylinder was grasped "for a total
  allowable positioning error of over 100% of the object size in each
  direction" (§3.1.4, p. 592), and in the camera-guided trials "The target
  objects were able to be successfully grasped for every trial" (§3.2.3,
  p. 596).
- **A trade-off.** Raising the distal-to-proximal torque ratio balances
  contact forces but narrows the range of positions from which a grasp
  succeeds (§2.2.1, p. 588).
- **No pinch.** "A major drawback of the current design is the lack of
  pinch-grip functionality of the hand" (§4, p. 596).

## Standing in the record

The pasted synthesis on constraint architectures cites it, as M9, as
accommodating "a wide variety of objects using only one actuator", under
the heading of morphological computation, and as not implying that the
gripper has goals. The single actuator and the range of objects are right,
within power grasps of medium objects: the hand cannot pinch, so a pen on a
table is out of reach. "Morphological computation" is A's label; the paper
never uses it, and says only that compliance and adaptive coupling reduce
the sensing and control a grasp needs. A also leaves out the trade-off the
authors optimise and the sharp changes of behaviour near the edge of the
grasp range. Filed from it: [THEORY-tmp15pfs](../theory.d/THEORY-tmp15pfs.md).
