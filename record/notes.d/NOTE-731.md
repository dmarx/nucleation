---
number: 731
status: Read
formerly:
- NOTE-tmpmnv6y
paper: LIT-1025
title: 'Falmagne, Stephenson & Levin — Interpretable early warnings using machine learning in an online game-experiment'
version: 1
history:
- version: 1
  date: '2026-10-13'
  note: >-
    Read in full from the published version of record (PNAS 123(1),
    e2503493122, CC BY-NC-ND), taken as the JATS full text that Europe PMC
    serves for PMC12773730
    (ebi.ac.uk/europepmc/webservices/rest/PMC12773730/fullTextXML); the
    pmc.ncbi.nlm.nih.gov page returned a captcha. Read: the whole main text,
    figure captions and footnotes. The SI Appendix is not in the PMC XML.
    It was read from the arXiv preprint (arXiv:2502.09880, the version that
    carries the SI) in its sections 1 (data), 2 (transitions) and 6
    (interpretation and toy model); SI sections 3–5 (variable definitions,
    training details, performance tables) were skimmed only. Main-text
    quotations were checked by script against the published text, SI
    quotations against the preprint, with whitespace normalised.
date: '2026-10-13'
summary: >-
  On the 2022 r/place canvas, gradient-boosted trees fed 19 composition-level
  time series with a 7-hour memory predict the time until a crowd-built image
  is abruptly overrun, far better than variance or autocorrelation trends,
  and still work on 2023. The precursors it relies on are many and do not
  reduce to critical slowing down; a large share of transitions give no
  warning. The interpretation of the precursors is the authors' conjecture
  from SHAP curves.
---
<!-- inactive-ok-file: CLAIM-280 CLAIM-279 CLAIM-163 THEORY-069 THEORY-058 THEORY-214 — Proposed; open claims and readings, cited as what this reading bears on, nothing rests on their being settled -->

# NOTE-731: Falmagne, Stephenson & Levin — Interpretable early warnings using machine learning in an online game-experiment

## Contribution

The first large-sample test of early-warning signals on thousands of
socially maintained subsystems: about 10,900 crowd-built r/place
"compositions" in 2022 and 6,700 in 2023, taken from the crowdsourced Atlas.
A transition is an abrupt overthrow of a composition's recent image. A
machine-learned predictor of time-to-transition beats the standard generic
indicators, transfers from one edition to the next, and is read with SHAP
for what it uses.

## Key insight

A defended image on r/place is a quasi-equilibrium between attack and
repair, and its overthrow has no single signature. "Many dynamical
behaviors, rather than single, generic early warning signals, are found to
indicate incoming transitions." Some of those behaviours are social: a
community that keeps adopting changes, acts in a coordinated way and keeps
a complex image is less likely to be overrun.

## Assumptions

- **Compositions are Atlas units.** Borders, birth and death come from a
  crowdsourced map, minimally cleaned; compositions that move are split.
- **State variable.** The fraction of pixels differing from a "reference
  image", which is the per-pixel mode colour over the preceding 3 hours.
  "Defense" changes restore attacked pixels to the reference colour. So the
  defended image is whatever has held recently, not a fixed plan.
- **Transition.** The state variable exceeds 0.35 and is six times its
  sliding-window mean; transitions out of a patchwork are rejected, and a
  stable preceding period is required. The authors show performance is
  insensitive to these thresholds (SI Fig. S6A).
- **Live-setting discipline.** Only past information, only instances
  preceded by a stable period, whole compositions split between train and
  test.
- Bots, multiple accounts and moderators are kept as part of the dynamics;
  cooldown-breaking changes "constitute less than 1% of changes in 2022".

## Key results

- **Performance.** "We predict half of the incoming transitions within 20
  min with only 3.6% false positives and a ROC AUC of 0.835." Predictive
  power reaches "up to 6 h before the transition with a ROC AUC of 0.698".
  The best generic indicator (Kendall's τ on variance) is far worse at every
  warning range.
- **Transfer.** Trained on all of 2022 and tested on 2023, performance drops
  only slightly, despite different canvas expansions, cooldowns, bot
  activity and motivations.
- **Heterogeneity.** "For a warning range of 20 min, 44% of the transitions
  have a ROC AUC greater than 0.8"; at the same range "27% perform at or
  worse than random". "unpredictable transitions make up a significant part
  of our data". The authors suggest some attacks are "unstrategic, and thus
  unpredictable".
- **Twelve pretransition behaviours (Fig. 6, SI Fig. S11).**
  - Strong critical slowing down very close to transition: high image
    activity, attack force dominating the defence, high user recruitment.
  - A mild critical speeding up earlier: high defence 30–60 minutes before.
  - A turbulent past (past attacks, past high engagement) signals a
    transition; so does low past activity (neglect inviting opportunism);
    but "a very low past image activity may indicate a general lack of
    interest", which makes the composition safer.
  - "A lack of innovation is indicative of transitions". Innovation is an
    attacked pixel left in its new colour, read as a change the community
    accepted.
  - "Coordinated activity rather than noisy activity, whether from the
    defending community or not, also indicates stronger compositions".
  - Low past defence is a transition signal.
  - "images of higher complexity are also typically safer".
- **Toy model (SI 6.B).** Two equations: deviation from a fixed reference
  image, and the number of defenders, with recruitment at medium deviation
  and desertion near full replacement. Lowering defence strength gives a
  bifurcation with slowing down; a sudden rise in attack rate gives
  rate-induced tipping preceded by speeding up, because recruitment raises
  the return rate. "These observations show that seemingly contradictory
  warning signals, associated with different types of transitions, can
  exist within a single system."

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Abrupt overthrows of r/place compositions are predictable above chance from composition-level time series, up to hours ahead | strong | held-out compositions; ROC/PR curves; transfer to 2023 |
| C2 | No single generic indicator captures the precursors; the machine-learned combination far outperforms variance, autocorrelation and return-rate trends | strong | direct comparison, Fig. 4C |
| C3 | A substantial share of transitions show no detectable warning | moderate | per-transition AUCs (SI Fig. S4B) |
| C4 | Low innovation, uncoordinated activity, simple images, turbulent history and low past defence precede transitions | weak to moderate | SHAP trends robust to the transition threshold; interpretation by the authors, "a degree of conjecture" |
| C5 | Slowing down and speeding up can coexist in one system because different transition types do | weak | a two-variable toy model, illustrative only |

## Concepts

- **Composition.** A culturally meaningful image on the canvas, as mapped
  in the Atlas; in other papers an artwork.
- **Reference image.** Per-pixel mode colour over the last 3 hours.
- **Attack / defence.** A change away from / back to the reference colour.
- **Innovation.** An attack left standing, read as accepted by the
  defenders. The SI admits "there is no sure way to identify whether a pixel
  change that does not match the reference image is an attack on the image,
  or an innovation that will eventually be adopted into the image by the
  defending community."
- **Return rate.** Fraction of pixels attacked at the previous step that
  are back to the reference colour at this step.
- **B-, S- and R-tipping.** Bifurcation, large-perturbation (state) and
  rate-induced tipping.

## Connections

It applies the critical-transitions literature (critical slowing down,
B/S/R-tipping) to a social system and sides with the work finding that no
universal warning signal exists. It uses the Atlas, and cites the earlier
r/place studies (Rappaz et al. 2018; Litherland & Mørch 2021, [LIT-1037](../literature.d/LIT-1037.md))
as background only. The record's measured case of critical slowing before a
switch is bimanual coordination ([THEORY-069](../theory.d/THEORY-069.md)); the network theory of mental
disorders ([THEORY-058](../theory.d/THEORY-058.md)) appeals to the same signal. This paper is evidence
that in a richer collective system the classic signal is one precursor
among many and can be reversed.

## Bearing on the record

**[CLAIM-280](../claims.d/CLAIM-280.md) (persistence by contest and repair).** Support, with a
qualification.

- The paper's whole apparatus presupposes the maintenance regime: a
  composition is stable while attacks are continually undone, and its
  overthrow is the point where attack outruns defence. Low past defence and
  defenders' failure to recruit precede transitions; the toy model's
  defenders are recruited by damage and desert at near-total loss.
- Its return rate is close to A8's proposed conditional repair hazard: the
  share of just-attacked pixels restored at the next step. It is not
  compared with a baseline rate at the same sites, which is the comparison
  A8 asked for, and its distribution across compositions is not reported.
- The qualification bears on the claim's `defeated_if`. Very low past
  activity also makes a composition safer. So some compositions persist
  because nobody attacks them. The paper does not say what share of
  long-lived compositions persisted that way.
- On product and producer: a valid transition includes one "where the
  composition returns to its pretransition state", and "innovation" is the
  image changing with its community's acceptance. The reference image is a
  3-hour mode, so the product the paper tracks is itself drifting. The
  paper never follows a community across images, so it does not separate
  the producer's persistence from the product's; it only shows the product
  is not fixed.

**[CLAIM-279](../claims.d/CLAIM-279.md) (stabilizing is relative to a frame).** The SI's admission
that an off-reference pixel cannot be classed as attack or innovation until
the defending community does or does not adopt it is the claim's relativity
made operational: the class of an act depends on the policy of the group
whose image it is, and that policy is only visible later.

**[QUESTION-091](../questions.d/QUESTION-091.md) (cascades and branching).** Not answered. The paper fits
no point process. Its "high user recruitment" before transition and the
toy model's damage-driven recruitment are the excitation an answer would
model.

**[CLAIM-163](../claims.d/CLAIM-163.md)** asked for an order parameter and coupling before
"synchronization" talk means anything. This paper shows how hard that is
for an image: "our subsystems are images; the information in all their
pixels is hardly reducible to a scalar state variable", and noise "is
difficult to distinguish from coordinated attacks".

**[QUESTION-084](../questions.d/QUESTION-084.md).** The paper infers "coordination" and "innovation"
from placements alone and calls the reading conjectural. It is an instance
of the question's difficulty, not an answer.

Not anthology material: the classifier is the instrument; the findings are
about a human collective.

## Limitations

- Compositions come from a crowdsourced map made after the event, which is
  biased toward images that lasted long enough to be mapped.
- The precursor stories are read off SHAP curves of correlated features;
  SHAP assumes feature independence, and the authors say the grouping
  involves "a degree of conjecture".
- Only abrupt transitions out of stable periods are studied; gradual
  takeovers and patchwork regions are excluded by design.
- No communication data: "coordination" means spatially and temporally
  consistent placements, not plans.
- Transfer is between two editions of one game.

## Open questions

- Does the return rate, compared with a site's baseline, separate defended
  from neglected long-lived compositions? That would test [CLAIM-280](../claims.d/CLAIM-280.md)'s
  `defeated_if` directly.
- Are the unpredictable transitions the ones planned off the canvas
  (raids, streamer-led attacks)? Matching transitions to coordination
  records would say.
