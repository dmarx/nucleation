---
status: Read
paper: LIT-tmp9cpfz
title: 'Boayue and colleagues — A registered report on increasing mind-wandering with tDCS'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Read 2026-11-22 from the authors' Stage 2 preprint on PsyArXiv
    (osf.io/dfex3; PDF osf.io/download/3rfrs/, 54 pages, "Preprint
    submitted to European Journal of Neuroscience, September 25, 2018"),
    located through the OSF API and extracted with pdftotext. Read: the
    abstract, Introduction, Methods (participants, apparatus, stimulation
    protocol, the statistical plan in outline), Results (pre-registered
    and exploratory) and Discussion. Skimmed: the design-analysis
    simulations of §2.5 and the appendix on the probit model and protocol
    changes. Not read: the reference list. The published version (EJN
    51(3): 755–780) was not compared with the preprint.
date: '2026-11-22'
summary: >-
  A pre-registered three-lab replication of [LIT-tmpquab4](../literature.d/LIT-tmpquab4.md) (192
  participants, same montage, double-blind) found no increase in reported
  mind-wandering under anodal prefrontal tDCS: the effect was slightly
  negative and its interval included zero, the null was favoured over a
  positive effect (BF 10.65), and the replication Bayes factor was 0.002.
  The authors judge the original "most likely a false positive", and model
  the montage's field as weak, diffuse and variable across heads.
---
<!-- inactive-ok-file: ARG-tmpqszyu — new in this filing and Proposed; the readings and the support verdict, cited as open -->
<!-- inactive-ok-file: THEORY-1300 ARG-051 — Proposed; Metzinger's account and the analogy, cited as open -->

# NOTE-tmps966y: Boayue and colleagues — A registered report on increasing mind-wandering with tDCS

## Contribution

The first pre-registered, multi-site test of whether anodal tDCS over the
left DLPFC raises mind-wandering. It found that it did not, and gave
Bayesian evidence against the original effect. It also put the montage's
electric field into head models, which shows how little the stimulation
can be said to target.

## Key insight

A large effect from small samples is the expected product of noise and
selection: "the original result by Axelrod et al. (2015) was most likely a
false positive finding caused by strong variability and low sample size"
(§4). The field the montage induces is weak, about 0.1–0.2 V/m in the
target, reaches "both the medial and lateral aspects of the two
hemispheres", and varies between people (§4, Fig. 6), so even a real
effect could not be assigned to the DLPFC.

## Assumptions

- **A direct replication.** Task, timing, montage and the single probe
  matched to the original, with the original authors consulted on the
  setup (§2.2); minor changes (rubber electrodes with paste, a NeuroConn
  stimulator, 15 s sham) listed in §2.4 and the appendix.
- **Sequential sampling** with a pre-registered stopping rule: stop when
  the 95% HDI of the effect excluded zero in the positive direction,
  otherwise collect the maximum of 64 per lab (§3.2).
- **Bayesian inference**, with frequentist tests reported for comparison.

## Key results

- **Main effect**: "d = −0.11, HDI= [−0.38, 0.17]" (§3.2.1); "the
  null-hypothesis was about 10.65 times more likely" than the hypothesised
  positive effect; against any effect, BF 4.79.
- **Replication**: "We found strong support for the alternative
  (BFreplication = 0.002) indicating that it is about 500 times as likely
  that the effect was not consistent with the originally reported
  effect-size" (§3.2.1).
- **Probit model**: time on task raised off-task reports (β = 0.20 [0.18,
  0.23]); stimulation did not (β = −0.09 [−0.24, 0.07]) (Table 5).
- **Frequentist**: t(117.68) = −1.01, p = 0.312, d = −0.102.
- **Exploratory**: no effect of stimulation on response time, its
  variability, or commission errors; response-time variability correlated
  best with off-task reports (τ = 0.224).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Anodal F3–supraorbital tDCS at 1 mA does not raise reported mind-wandering in a SART | strong | pre-registered, n = 192, three labs, BF 10.65 against a positive effect |
| C2 | The 2015 effect size is not reproduced | strong | replication BF 0.002 |
| C3 | The 2015 result was most likely a false positive | moderate | C1 and C2, with the small original samples |
| C4 | The montage's field is diffuse and variable between people | moderate | modelling of 18 heads, not measured in these participants |

## Concepts

- **Replication Bayes factor** — tests whether the new data fit the
  original effect size better than a null (Verhagen and Wagenmakers 2014).
- **Normal component of the electric field** — the part perpendicular to
  the cortex, taken as excitatory entering and inhibitory leaving (§4).

## Connections

Replicates [LIT-tmpquab4](../literature.d/LIT-tmpquab4.md) and fails. It cites Fox and Christoff and
Broadway et al. as the endorsements that made a replication urgent. It
predates and does not discuss the first author's own positive replication
([LIT-tmpg3vlm](../literature.d/LIT-tmpg3vlm.md)). It reads the Kajimura and Bertossi results, from parietal
and medial prefrontal montages, as possible real effects still needing
replication.

## Bearing on the record

- **Metzinger's H1, [THEORY-1300](../theory.d/THEORY-1300.md).** If the tDCS effect is absent, the study
  Metzinger cites first for H1 is not evidence of anything about
  mind-wandering's onset, and his "early examples of relevant studies"
  reduces to a direction of research. It does not test H1 either way: the
  manipulation does not target the agent model.
- **[CLAIM-027](../claims.d/CLAIM-027.md), [ARG-051](../arguments.d/ARG-051.md).** None directly. It narrows what the record can
  lean on from the stimulation literature at all: before any reading of
  the tDCS work as a change in a condition of efficacy, the effect has to
  be real. Verdict in [ARG-tmpqszyu](../arguments.d/ARG-tmpqszyu.md).
- **The record's method.** A case, for the record's own practice, of a
  causal claim from two small samples failing under pre-registration;
  noted, no edge.
- No instruction for machine-learning practice.

## Limitations

- **A replication of one montage and one task.** It does not show that no
  brain stimulation changes mind-wandering; the authors say so (§4).
- **One self-report item**, the original's; no meta-awareness measure, so
  it cannot speak to Fox and Christoff's reading.
- **Inconsistent meta-analytic figure.** §3.2.1 gives the meta-analytic
  Bayes factor as 0.48, "only weakly" for the null; §4 gives "strong
  evidence (BFmeta = 0.059)". The preprint does not reconcile them; the
  published version was not checked.
- **Read as a preprint**, which may differ from the published article.

## Open questions

- Why does the first author's replication ([LIT-tmpg3vlm](../literature.d/LIT-tmpg3vlm.md), n = 85, d about 1)
  succeed where this one fails? Lab, language, device and sham length
  differ; none of the papers tests which matters.
