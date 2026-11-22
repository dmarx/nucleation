---
status: Read
paper: LIT-tmpquab4
title: 'Axelrod, Rees, Lavidor and Bar — Increasing propensity to mind-wander with tDCS'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Read in full 2026-11-22 from the PubMed Central article page
    (pmc.ncbi.nlm.nih.gov/articles/PMC4371998/), HTML converted to text:
    Significance, Abstract, introduction, Results (both experiments),
    Discussion, Materials and Methods, figure captions and footnotes. The
    SI PDF (statistics of the halves for the task measures) and the
    reference list were not read. The Europe PMC REST fullTextXML route
    (ADR-101) returned HTTP 500; the Europe PMC PDF render gave a
    Cloudflare challenge, at which the session stopped. The letter of Fox
    and Christoff on it (LIT-tmp4vtkl) was read beside it; Broadway et
    al.'s commentary (PNAS 112(11): 3182–3183), which Metzinger also cites
    for H1, was not read.
date: '2026-11-22'
summary: >-
  Two small sham-controlled experiments in which anodal tDCS over the left
  prefrontal cortex raised self-rated task-unrelated thought during a
  monotonous go/no-go task, without hurting task performance. The authors
  take it as the first causal evidence that the frontal lobes, and
  executive control, are part of the mind-wandering machinery. It
  measures how much off-task thought was reported, and nothing about
  whether the agent's model of its own control changed.
---
<!-- inactive-ok-file: ARG-tmpqszyu — new in this filing and Proposed; the readings and the support verdict, cited as open -->
<!-- inactive-ok-file: THEORY-1300 THEORY-1296 ARG-051 — Proposed; Metzinger's accounts and the analogy this reading was sought for, cited as open -->

# NOTE-tmp7gplv: Axelrod, Rees, Lavidor and Bar — Increasing propensity to mind-wander with tDCS

## Contribution

Before it, the neural evidence on mind-wandering was correlational (fMRI).
It reports that weak direct current over the left frontal lobe raises how
much task-unrelated thought people report, against both sham and an
occipital control, in a within-subjects and a between-subjects experiment.
The authors draw two conclusions: mind-wandering "can be modulated by means
of external stimulation", and "the frontal lobes play a causal role in
mind-wandering behavior" (Discussion).

## Key insight

The paper's own reading is that stimulation added executive capacity:
mind-wandering rose while target detection did not fall, so "the brain
stimulation caused an enhancement (extension) of cognitive capacity, so
that the increase in mind wandering did not compromise performance of the
external task" (Discussion). On this view executive control is a resource
mind-wandering uses, not a brake on it.

## Assumptions

- **The probe measures mind-wandering.** One question, "To what extent have
  you experienced task-unrelated thoughts prior to the thought probe?",
  rated 1 (minimal) to 4 (maximal), about "the last several seconds before
  the probe" (Methods), 24 probes in 40 minutes.
- **The montage stimulates the left DLPFC.** Anode at F3, cathode over the
  right supraorbital area, 1 mA for 20 minutes; the paper says the region
  is "plausible", not shown, and names the medial frontal cortex and the
  right frontopolar cortex under the cathode as alternatives.
- **Blinding by short sham.** Sham ran 2 minutes; "Most participants did not
  feel the electrical current".

## Key results

- **Experiment 1** (n = 14, within subjects, prefrontal against sham):
  task-unrelated thought 2.39 against 2.05, "t(13) = 2.63, P = 0.021
  (paired two-tailed t test), Cohen's d = 0.7" (Results). During
  stimulation alone the effect was "marginally significant" (P = 0.09).
- **Experiment 2** (n = 31, between subjects, prefrontal, sham, occipital):
  2.93, 2.12 and 2.17; "F(2,28) = 5.85, P = 0.007, η2 = 0.29"; prefrontal
  against sham d = 1.24, against occipital d = 1 (Results).
- **Task performance**: correct detection rose slightly and not
  significantly in both experiments (64.7% against 61%; 69.9% against
  55.9% and 64.6%); response times did not differ.
- **Online and offline**: mind-wandering rose in the second half in every
  condition, sham included; stimulation did not interact with half.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Prefrontal anodal tDCS raises reported task-unrelated thought in a SART | moderate in the paper; contested since (see Connections) | two small experiments, one replication within the paper |
| C2 | The effect is site-specific, not a general effect of tDCS | weak | one occipital control group of 11 |
| C3 | The frontal lobes play a causal role in mind-wandering | weak to moderate | C1 with C2; region not resolved |
| C4 | Executive control is "an integral part of the mind-wandering cognitive mechanism" | weak | a non-significant rise in target detection |

## Concepts

- **TUT, task-unrelated thought** — the proxy for mind-wandering: "thoughts
  that were irrelevant to the experiment and did not help with task
  execution (e.g., thoughts that were related to personal memories or
  future plans)" (Methods).
- **Online and offline stimulation** — task during the 20 minutes of
  current, and the 20 minutes after it.

## Connections

The first stimulation study of mind-wandering. Fox and Christoff's letter
([LIT-tmp4vtkl](../literature.d/LIT-tmp4vtkl.md)) proposed that the stimulation raised meta-awareness rather
than, or besides, mind-wandering. The first author's direct replication
([LIT-tmpg3vlm](../literature.d/LIT-tmpg3vlm.md), n = 85) reproduced the effect and found meta-awareness
unchanged. A pre-registered three-lab replication ([LIT-tmp9cpfz](../literature.d/LIT-tmp9cpfz.md), n = 192)
found no effect and strong evidence against the original effect size, and
a 2023 meta-analysis of fifteen studies by two of its authors (Nawani,
Mittner and Csifcsák, DOI 10.1016/j.neuroimage.2023.120051, abstract only)
reports "no reliable evidence for tDCS influencing MW in the healthy".
Metzinger ([LIT-1945](../literature.d/LIT-1945.md), p. 14) cites this paper and Broadway et al. (2015) as
"early examples of relevant studies" for his H1.

## Bearing on the record

- **Metzinger's H1, and [THEORY-1300](../theory.d/THEORY-1300.md) and [THEORY-1296](../theory.d/THEORY-1296.md).** H1 reads: "if an EAM
  is in place, then selectively blocking its introspective availability
  should suffice to trigger a mind wandering episode" ([LIT-1945](../literature.d/LIT-1945.md), p. 14).
  This study is relevant to H1 only in its outcome measure. Its
  manipulation is not shown to block anything: it is anodal, usually taken
  to raise excitability; the authors read it as adding executive capacity;
  and nothing in it measures the agent's awareness of its own thought or
  control. It therefore does not meet [THEORY-1300](../theory.d/THEORY-1300.md)'s promote_when, which
  asks for "an intervention on the self-model's representation of the
  capacity alone, with the capacity checked independently". Support
  verdict: [ARG-tmpqszyu](../arguments.d/ARG-tmpqszyu.md).
- **[CLAIM-027](../claims.d/CLAIM-027.md) and [ARG-051](../arguments.d/ARG-051.md).** The claim's test is a change in a condition of
  efficacy with the competing regimes held fixed. Here the reported amount
  of task-unrelated thought is the outcome, and what produced it (more
  candidate thoughts, more capacity to sustain them, less monitoring) is
  undetermined, so the competing thoughts are not held fixed or measured.
  It neither supports nor defeats the claim; [ARG-tmpqszyu](../arguments.d/ARG-tmpqszyu.md) files that.
- **[QUESTION-367](../questions.d/QUESTION-367.md).** No bearing beyond the above: the study does not touch
  the agent's representation of its capacity.
- No instruction for machine-learning practice.

## Limitations

- **Small samples**: 14 and 31, with large effects (d up to 1.24) that the
  pre-registered replication found to be overestimated.
- **One self-report item** as the only measure of mind-wandering; no
  measure of meta-awareness, intentionality, or episode onset and end.
- **Spatial resolution**: the montage cannot say which frontal region
  mattered, by the authors' own account.
- **The capacity reading is a step not shown**: the "enhancement
  (extension) of cognitive capacity" rests on a rise in target detection
  that was not significant in either experiment, and the replication by
  the first author found a slight fall.

## Open questions

- Does the effect survive pre-registration? Contested ([LIT-tmpg3vlm](../literature.d/LIT-tmpg3vlm.md) against
  [LIT-tmp9cpfz](../literature.d/LIT-tmp9cpfz.md)).
- If real, does it act on the generation of off-task thought, on its
  maintenance, or on the monitoring that would end it?
