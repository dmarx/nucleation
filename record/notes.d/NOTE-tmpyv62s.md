---
status: Skimmed
paper: LIT-tmp1nipn
title: 'Shankar and others 2020 — Topological active matter'
version: 1
history:
- version: 1
  date: '2026-11-19'
  note: >-
    URL read: https://arxiv.org/pdf/2010.00364 (served v3, 19 Jul 2021),
    HTTP 200, PDF. Kind of copy: arXiv preprint, the authors' manuscript of
    the Nature Reviews Physics article (step 5, arXiv). Fetched 2026-11-19;
    nothing stopped the fetch. Text extracted with pdftotext to dl/text.txt.
    Read: abstract; introduction; §I opening; §I A (active defects move, 3D
    loops); §I B (defect unbinding); §II opening (topological band
    structures, edge states, interfaces); §III Outlook (as extracted; its
    tail appears cut). Skipped: §I C onward on defect patterning,
    confinement and biology; Boxes 1–4 (figure text did not extract
    cleanly); §II's sections on chiral active fluids, odd elasticity and
    non-Hermitian skin modes; references. Verdict on the source's
    characterization ("a review of topological phenomena in active and
    driven matter", cited "for topology of dynamics rather than of ground
    states"): the first part is accurate. The second fits the edge-mode
    half, where activity creates band topology, and fits the defect half
    only loosely, because those defects are order-parameter defects whose
    behaviour, not whose topology, is dynamical.
date: '2026-11-19'
---
<!-- inactive-ok-file: CLAIM-606 CLAIM-694 THEORY-1408 — Proposed; cited in this filing of 2026-11-19 -->

# NOTE-tmpyv62s: Shankar and others 2020 — Topological active matter

## Contribution

An introductory review (arXiv 2010.00364, v3 2021; Nature Reviews Physics 4, 380–398, 2022) of topology in active matter. It covers two classes of phenomena. The first is topological defects of an order parameter, chiefly in active nematics, where defects self-propel, unbind and proliferate. The second is topologically protected edge modes of waves, set by band-structure invariants, in active fluids, robotic metamaterials and non-Hermitian active solids. The authors keep the two apart physically while noting that both rest on integer invariants.

## Key results

- **Two classes, one mathematics** (abstract): "These paradigmatic examples represent two physically distinct classes of phenomena whose robustness can be traced to a common mathematical origin: the presence of topological invariants."
- **What is held fixed differs** (introduction): for edge modes, "the Chern number (and hence the very presence of an edge mode) is preserved under continuous changes in the physical parameters of the material (rather than under continuous deformations of the order parameter)."
- **The winding number is a net count** (introduction): if the path encircles "multiple vortices and anti-vortices, ν measures the net number of topological defects". The Chern number likewise "measures the net number of unidirectional, i.e., chiral, edge modes present".
- **Linked, not identical** (introduction): "Topological defects and topological protected modes are intertwined", and "topological modes can be localized around defects such as vortices, dislocations or domain walls."
- **Activity can make them exist** (introduction): non-equilibrium currents "endow topological modes and defects with properties absent at equilibrium and, in some cases, enable their very existence."
- **Supplied versus relaxing** (§I): in passive systems "Such flows are transient: the system always relaxes to the equilibrium (ordered) state upon removal of perturbations or constraints." In active systems "flows and deformations are internally generated and self-sustained."
- **Defects make the flow that moves them** (§I A): the +1/2 defect "rides along with the flow it generates, behaving like a self-propelled polar particle", and "the motion of active defects is dictated by the local geometry of the defect itself and not by a fixed external field".
- **Unbinding and order from noise** (§I B): activity can unbind ±1/2 pairs, while "rotational noise here stabilizes the quasi-ordered nematic phase below a finite activity threshold".
- **Charge constrains creation differently by dimension** (§I A): in 2D "topological charge conservation constrains point defects to be created and annihilated in" pairs, whereas "in 3D charge-neutral disclination loops [12] can be nucleated on their own."
- **The switch of topic is explicit** (§II): "The topological defects considered so far are robust features of the order parameter of active media. We now turn to topologically protected waves whose robustness stems from their band structures."
- **Edge modes as gap failure** (§II): at an edge "the condition for defining a Chern number, namely that the system is gapped, must cease to be valid at the edge, giving rise to confined wave propagation." Modes occur at sample edges or "at interfaces between systems with topologically distinct band structures."
- **Limits in fluids** (§II): "the Chern number is not always well-defined in fluids".
- **Open challenge** (§III Outlook): "One challenge faced by future theoretical work is the robustness of topological states to biologically relevant perturbations."

## Assumptions

- Continuum hydrodynamic models of polar and nematic active fluids (Box 2). Defects are point charges with core size a and elastic interaction K ln(r/a).
- Linear wave theory for the band-structure part: a gapped linear operator. Non-Hermitian operators where reciprocity is broken.
- Mostly 2D. 3D defects are said to be "less well understood".

## Concepts

- **Topological defect**: a singularity of the order parameter with a winding number (charge), protected under continuous deformations of the order parameter. ±1/2 disclinations occur in nematics.
- **Topologically protected edge mode**: a wave mode at a boundary or interface, guaranteed by a band invariant (Chern number), protected under continuous change of material parameters while the gap stays open.
- **Activity**: microscale energy conversion that makes flows self-sustained, lets defects self-propel, and can create the conditions (broken time-reversal symmetry, non-reciprocity) for nontrivial band topology.
- **Non-Hermitian skin effect**: modes piling up at a boundary, characterized by a non-Hermitian winding number (Box 4; not read in detail).

## Bearing on the record

- QUESTION-tmp57ji2: leaves open. The review keeps defect topology and edge-mode topology apart and gives no case in which modes bound at a defect maintain the order-parameter structure. The nearest is the active defect: the defect's texture generates the flow that propels it ("distortions of orientational order generate flows, and flows in turn deform the ordered state"). That is mutual coupling between texture and flow, not between the texture and a hosted mode. The LIT's gloss (topology of dynamics rather than of ground states) fits the edge-mode half, since activity creates band topology, and only loosely fits the defect half.
- CLAIM-606: qualifies. Active defects carry a conserved charge (topological route) yet are created and kept unbound by a standing supply (activity). Without it, flows are "transient" and the system "relaxes". One structure can sit on two of the claim's routes at once: the charge constrains how defects are created and end (pairs in 2D), while the supply sets whether and how many exist. In 3D, charge-neutral loops nucleate alone, so the charge does not constrain their formation.
- CLAIM-694: supports, as a textbook statement rather than a demonstration. The winding number around several defects "measures the net number of topological defects", which matches the claim's net count of defects, not tokens.
- QUESTION-378: supports the held condition. Edge modes occur "at interfaces between systems with topologically distinct band structures", the same distinct-phases condition the question already cites from Kane and Lubensky (THEORY-1408). Nothing new on adaptive degrees of freedom.

## Limitations

- Skimmed. Read: abstract, introduction, §I opening, §I A (self-propulsion, 3D loops), §I B (unbinding), §II opening (band structures, edge states), §III Outlook as extracted. Skipped: §I C–D on patterning, confinement and biological tissues, the Box texts (figures did not extract cleanly), §II's detailed sections on chiral active fluids, odd elasticity and non-Hermitian skin modes, Box 4. The tail of the Outlook appears cut in the text extraction.
- A review. Its results are the cited primary works', which were not read.
