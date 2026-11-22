---
status: Read
paper: LIT-tmpg3vlm
title: 'Axelrod, Zhu and Qiu — Frontal tDCS increases mind-wandering without changing meta-awareness'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Read in full 2026-11-22 from the publisher's open-access page
    (nature.com/articles/s41598-018-34098-z, CC BY 4.0), HTML converted to
    text: Abstract, Introduction, Results, Discussion, Methods, figure
    captions and the rights statement. Figures were read through their
    captions and the statistics in the text; the reference list was not
    read. The Europe PMC REST route returned HTTP 500 and the PMC page a
    reCAPTCHA, at which the session stopped.
date: '2026-11-22'
summary: >-
  A direct, larger replication of LIT-tmpquab4 by its first author, adding
  a meta-awareness probe. Frontal anodal tDCS again raised reported
  task-unrelated thought (d about 1 against sham and against occipital
  stimulation), while meta-awareness of where attention was focused did
  not differ between conditions (Bayes factor 0.25), and the relation
  between the two was the same in every condition. The authors infer that
  mind-wandering can change without a change in meta-awareness.
---
<!-- inactive-ok-file: ARG-tmpqszyu THEORY-tmprbqew — new in this filing and Proposed; the readings and the support verdict, cited as open -->
<!-- inactive-ok-file: THEORY-1300 THEORY-1298 CLAIM-156 ARG-051 — Proposed; Metzinger's accounts, the mindfulness claim and the analogy, cited as open -->

# NOTE-tmp36b7e: Axelrod, Zhu and Qiu — Frontal tDCS increases mind-wandering without changing meta-awareness

## Contribution

It reproduces the 2015 result with more than twice the sample, in another
country and language, run by a different experimenter, and adds the
measure the 2015 study lacked: a probe of meta-awareness after each
mind-wandering probe. It finds the stimulation effect on mind-wandering
and no effect on meta-awareness, and so answers Fox and Christoff's
alternative (LIT-tmp4vtkl) in the negative.

## Key insight

"At least in some cases, changes in mind-wandering are likely not mediated
by or regulated by meta-awareness" (Discussion). Mind-wandering rose at
low and at high meta-awareness alike: the stimulation shifted how much
off-task thought there was, not how much of it the participant noticed.

## Assumptions

- **Two probes, fixed order.** "To what extent have you experienced
  task-unrelated thoughts?" then "To what extent have you been aware of
  where your attention was focused?", each 1–4 (Methods); 36 probes in
  about an hour.
- **Same montage and task as 2015**: anode F3, cathode right supraorbital,
  1 mA; 30 minutes of current, then 30 without; SART with 1 s digits and
  1.2 s gaps.
- **Sample size by power analysis** on the 2015 effect (d about 1), alpha
  0.01, power 0.8: 26 per group planned; 30, 28 and 27 analysed.

## Key results

- **Mind-wandering**: "one-way ANOVA ... F(2,82) = 9.77; p < 0.001; η2 =
  0.19 (Bayes factor of 172 ...)"; prefrontal against sham "t(56) = 3.66;
  p < 0.001; Cohen's d = 0.97", against occipital d = 1 (Results).
- **Meta-awareness**: "F(2,82) = 1.11; p = 0.33; η2 = 0.026 ... a Bayes
  factor of 0.25, indicating substantial evidence in support of H0"
  (Results); prefrontal stimulation "slightly decreased" it.
- **The relation between them**: in every condition, low meta-awareness
  went with more high-TUT reports (main effect F(1,62) = 13.4); stimulation
  did not change that relation (interaction BF 0.132). Only participants
  with both low and high meta-awareness ratings entered this analysis (27,
  20 and 18).
- **Task**: no differences between conditions in lapses or response times;
  the 2015 paper's slight gain in detection "could not be replicated".
- **Online and offline**: no interaction with stimulation.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Frontal anodal tDCS raises reported task-unrelated thought | moderate here; contested across studies | n = 85, large effect, preregistered power analysis but not a registered report |
| C2 | It does not change rated meta-awareness | moderate | BF 0.25 for no difference; one item, always second |
| C3 | Mind-wandering is "at least in some cases" not regulated by meta-awareness | weak | inference from C1 and C2 |

## Concepts

- **Meta-awareness** — the participant's rating of having "been aware of
  where your attention was focused"; "Mind-wandering episodes can happen
  with or without a meta-awareness of them" (Introduction).
- **Pre-error speeding, post-error slowing** — faster go responses before a
  missed no-go, slower ones after.

## Connections

Extends LIT-tmpquab4 and answers LIT-tmp4vtkl. It cites Kajimura and
Nomura and Bertossi et al. for the reverse effect of cathodal frontal
stimulation. It does not cite the pre-registered replication
(LIT-tmp9cpfz), whose preprint is dated September 2018; a commentary by
that group on this paper exists (Csifcsák et al. 2019, Frontiers in
Psychology 10: 130, DOI 10.3389/fpsyg.2019.00130), not read: the PMC page
gave a reCAPTCHA.

## Bearing on the record

- **Metzinger's H1, THEORY-1300.** This is the nearest test found. Rated
  meta-awareness is the closest measured thing to the introspective
  availability of the epistemic agent model, though not the same thing:
  it asks about awareness of where attention was, not about awareness of
  having the capacity to end the thought. Two results bear on H1. First,
  the correlation within every condition, more mind-wandering when
  meta-awareness was low, is what H1 expects, but it is not an
  intervention and the order of the probes may produce it. Second, the
  intervention raised mind-wandering with meta-awareness unchanged. So the
  manipulation Metzinger cites for H1 does not work by blocking the
  agent's awareness; where it works, it works another way. That is a
  route to mind-wandering that bypasses the agent model, which H1 does
  not exclude ("should suffice" is a sufficiency claim) but which leaves
  H1 untested. THEORY-1300's promote_when is not met.
- **QUESTION-367.** Weak evidence on the side the question calls
  accompaniment, at the level of the measure: the rate of mind-wandering
  moved while the agent's rating of its own awareness did not. It cannot
  answer the question, which is about the representation of a capacity
  to control, not of attention's location, and needs the representation
  manipulated. Written as `bears_on` from THEORY-tmprbqew.
- **CLAIM-027 and ARG-051.** A change in which thought holds the mind
  without a change in the measured self-representation: if anything a
  case where efficacy moved for reasons other than the representational
  condition ARG-051 names. Since the competing thoughts are not held
  fixed, it does not bear on CLAIM-027's defeater. Verdict in
  ARG-tmpqszyu.
- **CLAIM-156** (noticing an impulse as an impulse suspends its control) is
  about what meta-awareness does when present; this study changes
  mind-wandering without changing meta-awareness, which the claim allows.
  A contrast, no edge.
- **THEORY-1298** (the return of control is represented as self-caused
  whatever caused it) is not touched: no episode ends are recorded.
- No instruction for machine-learning practice.

## Limitations

- **Fixed probe order**, which the authors say may bias the meta-awareness
  report; one item for each construct.
- **Not pre-registered as a registered report**, and the effect conflicts
  with LIT-tmp9cpfz's pre-registered null with the same montage.
- **Meta-awareness of attention's focus is not the agent model of
  control.** The step from an unchanged meta-awareness rating to "not mediated by or
  regulated by meta-awareness" is the authors' and assumes the probe measures the
  regulating state.
- **Subgroup analysis** of the relation drops 20 of 85 participants.

## Open questions

- Would a manipulation that lowers rated meta-awareness, with the
  mind-wandering probe removed or reordered, raise mind-wandering? That
  would be H1's test at the level of this measure.
