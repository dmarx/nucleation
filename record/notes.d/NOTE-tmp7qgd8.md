---
status: Read
paper: LIT-tmpw3fnx
title: 'Reddy, Levine and Dragan — First Contact, read for the record''s account of learning occasioned by obstruction'
version: 1
history:
- version: 1
  date: '2026-11-21'
  note: >-
    Read on 2026-11-21 by a delegated reader from arXiv 2205.12381v2 (15 Sep
    2022), the PDF: Sections 1–6, Appendix A.1–A.3 and every figure caption;
    the reference list scanned, the videos and code not used. Running notes
    on the branch claude/readers/first-contact (ADR-108). Every quotation
    below rechecked by the filer by script against the downloaded text, and
    the per-domain correlations in Fig. 2 against the rendered page. A local
    reading at the owner's request, beside the anthology's (ANTH-NOTE-250).
date: '2026-11-21'
summary: >-
  An interface scored and trained by the mutual information between the
  user's command and the state change it induces, with no task knowledge.
  Read here for what the anthology's reading did not need: who supplies the
  assistance in the failing domain (a prior study's copilot), that a second
  assisted domain is the one the score does not predict, that user
  adaptation is assumed and not measured, and that no transfer or
  unassisted-skill test is run.
---
<!-- inactive-ok-file: CLAIM-tmpydua7 CLAIM-tmpspx4i QUESTION-tmp6iu8e THEORY-tmp3tb8i ADR-108 — Proposed or Open; filed on 2026-11-21 -->

# NOTE-tmp7qgd8: Reddy, Levine and Dragan — First Contact, read for the record's account of learning occasioned by obstruction

## Contribution

An answer to fitting an assistive interface with no prior mapping, no labels
or reward, and no knowledge of the user's task. The score is the mutual
information between command and induced transition, R(π) = I(x_t, (s_t,
s_{t+1})) (Eq. 1), the sum of a perception term I(s_t, x_t) and a control
term I(x_t, s_{t+1} | s_t), estimated by a lower bound. MIMI maximizes it by
Bayesian optimization over low-dimensional interfaces while the user adapts.

## Key results

- **The premise** (§1): "the more intuitive the interface, the less noisy the
  user's commands".
- **The setting** (§2): "The interface does not have direct access to the
  user's desired task, but can observe command signals".
- **Offline** (§5.1): "in 4 out of 5 domains" the score predicts
  ground-truth reward, "average Spearman's rank correlation coefficient of
  ρ = 0.43". Fig. 2 gives X2T 0.45, ASHA switch 0.50, ISQL 0.11, SAvDRL 0.43
  (at Δ = 10³) and ASHA bottle 0.69, so the average is over all five, and the
  domain it does not predict is ISQL, Lunar Lander played "on their own, and
  with assistance". Also: "in each domain, the interface with the largest
  mutual information score also has the largest ground-truth reward".
- **The inversion** (§5.1, Fig. 2d): in the SAvDRL data the assistant
  prevents crashes, "which necessarily involves ignoring a large fraction of
  the user's commands"; "even though the assistant appears to reduce the
  user's influence over the next state, it actually increases the user's
  influence over later states". ρ is about −0.45 at Δ = 1 and positive only
  for Δ near the maximum episode length, 10³.
- **The limit** (§5.1, §6.1): "choosing the value of Δ requires prior
  knowledge of the timescale of the user's desired influence over the
  system … This is the primary limitation on the generality of our method."
- **Online cursor study** (§5.2): one rotation angle θ, "randomly-sampled"
  targets each episode, phases counterbalanced "to avoid the confounding
  effect of overall user improvement or fatigue"; score and reward correlate
  at ρ = 0.87 over points each "a distinct user operating a distinct
  interface". MIMI tends to "converge to one of two interfaces", θ ≈ 0 or
  θ ≈ π, the inversion being "easy for users to understand and invert".
- **Gesture Lunar Lander** (§5.3): one expert user, eight parameters,
  landing zone randomized; a mapping that "emerged through co-adaptation".
- **Adaptation is assumed** (Fig. 1): "We assume that the user partially
  adapts their command x_t to any given interface π".
- **What it cannot see** (§6.2): "There may be cases where the user can
  observe the state s_t, but the interface cannot."
- **Empowerment** (§4) is cited as an objective for assistants that
  "preserve a user's ability to reach various states"; MIMI differs in
  scoring intuitiveness as well as influence.

## Assumptions

Command noise tracks unintuitiveness; the user adapts, more to an intuitive
interface; Δ is chosen by hand; interfaces have at most eight parameters; in
the online studies the interface ignores the state (A.2).

## Concepts

Information rate of an interface (perception plus control); the task as an
unobserved context; the horizon Δ; co-adaptation; empowerment as the
contrast, influence without intuitiveness.

## Bearing on the record

- **CLAIM-tmpydua7** (supports, qualifies). The split it describes is the
  paper's setting (§2). The interface is a single rotation, or a linear map
  ignoring state, trained over random targets, so it cannot encode a
  particular target: the channel reading holds by construction. But no
  transfer test is run, to new targets, tasks or users; the claim's
  defeater (a) is excluded by design, not tested.
- **CLAIM-tmpspx4i** (supports the facts, corrects an attribution). The
  override and the horizon dependence are the paper's (Fig. 2d). The
  assistant is not First Contact's: it is the copilot of a prior study,
  SAvDRL, whose logged data First Contact re-scores; and the offline state is
  only the lander's horizontal position (A.3). The paper frames Δ as a
  horizon, "what should happen at the next timestep, or what should happen
  by the end of the episode"; the rate-hierarchy reading is the record's.
  The flat ISQL domain, also assisted Lunar Lander, is a second case the
  claim does not yet account for.
- **QUESTION-tmp6iu8e** (silent). No measure of unassisted skill after
  assistance; ISQL scores both conditions without that comparison.
- **CLAIM-532** (qualifies). Co-adaptation is assumed and shown within
  episodes (Fig. 7), but neither of the claim's tests is run: no transfer
  once the inducing conditions are gone, no intervention on what produces
  the capacity beyond the random-interface baseline.
- **QUESTION-404** (bears on it). The repair is a channel; the task stays
  unobserved. §6.2 names the converse case, the user seeing state the
  interface cannot, with a proposed extension that drops the interface's
  dependence on state rather than supplying it.
- **CLAIM-361** (supports its citation). Its account of the inversion holds;
  the help is a prior study's copilot.
- **THEORY-1344** (parallel). Empowerment as channel capacity from actions to
  sensors n steps later carries the same horizon choice as Δ.
- **THEORY-1521** (background, for QUESTION-tmp6iu8e). Automation doing a
  subtask can let the operator's skill decay unnoticed.

## Limitations

Small online evidence (12 users on one parameter; one expert user, the first
author, on eight); Δ chosen by hand; no transfer, generalization or
unassisted-skill tests; the intuitiveness premise posited, not tested
independently; the offline lander reduced to one dimension; five offline
domains, one near zero.
