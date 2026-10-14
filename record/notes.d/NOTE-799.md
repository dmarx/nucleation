---
number: 799
status: Read
formerly:
- NOTE-tmpo5gss
paper: LIT-949
title: 'Luppi et al. — A synergistic workspace for human consciousness'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the eLife version of record (eLife 12:RP88173,
    published 18 July 2024, 34 pages, CC BY), fetched as the publisher's
    PDF from cdn.elifesciences.org/articles/88173/elife-88173-v1.pdf
    (PDF creation date 18 July 2024; PMC copy PMC11257694 identified, not
    used) and extracted with pdftotext -layout: abstract, eLife
    assessment and digest, Introduction, Results, Discussion with
    limitations, and all of Materials and methods (recruitment,
    acquisition, preprocessing, parcellation, the ΦID, ΦR and
    participation-coefficient definitions, and the statistics). The
    figure supplements and source data were not opened; figures were read
    from their captions. The public reviews and author response linked
    from the article were not read. The reference list was checked only
    for the works named below.
date: '2026-10-14'
summary: >-
  In resting-state fMRI, regions where synergistic interactions outrank
  redundant ones form a "synergistic workspace". Within it, regions whose
  synergistic connections spread across more resting-state networks than
  their redundant ones are classed as gateways (mainly default mode), and
  the rest as broadcasters (mainly fronto-parietal, lateral prefrontal
  above all). Pairwise integrated information ΦR falls between DMN
  gateway regions under propofol (n = 15 or 16; the paper gives both)
  and in 22 patients with disorders of consciousness against controls,
  and recovers after anaesthesia, while the original whole-minus-sum Φ
  shows no common decrease. The increases, near the broadcasters, are not
  robust.
---
<!-- inactive-ok-file: QUESTION-061 CLAIM-003 THEORY-096 THEORY-098 CLAIM-158 — Deferred or Proposed; the set-aside question this work was filed for, its claim, and the accounts it bears on, cited as open -->

# NOTE-799: Luppi et al. — A synergistic workspace for human consciousness

## Contribution

The paper gives an information-theoretic operationalisation of a global
workspace and of its input and output sides, and applies it to fMRI. It
proposes the SAPHIRE architecture: specialised modules interact
redundantly, "gateways" gather their information synergistically, the
workspace integrates it, and "broadcasters" send copies back out
redundantly. The workspace and its two sides are mapped onto known
networks. Then, across two causes of unconsciousness, it finds that the
consistent loss of pairwise integrated information is on the gateway
side. The measure used is a corrected Φ (ΦR); the uncorrected Φ does not
show the effect.

## Key insight

Synergy and redundancy separate two things functional connectivity
blurs: combining distinct inputs, and copying the same content to many
places. A region that is synergistic with many modules looks like an
entry point. A region that is redundant with many modules looks like a
broadcaster. On that reading, losing consciousness in this data is
losing integration at the entry points, mainly between anterior and
posterior default-mode regions, not losing the broadcast.

## Assumptions

- **Linear-Gaussian BOLD.** Regional BOLD signals are deconvolved for the
  haemodynamic response and treated as jointly Gaussian. Then the
  minimum-mutual-information PID applies, which is justified because
  "linear-Gaussian models are sufficiently good descriptors of functional
  MRI timeseries".
- **Pairwise, undirected measures.** Every quantity is computed for pairs
  of regions (X, Y) from the past and future of each, and then treated as
  an undirected network. The paper says this "does not amount to
  measuring the integrated information of the brain as a whole".
- **The measures (Methods, Eqs. 4–7).**
  - Red(X,Y) = min{I(X_{t−τ}; X_t), I(X_{t−τ}; Y_t), I(Y_{t−τ}; X_t), I(Y_{t−τ}; Y_t)}.
  - Syn(X,Y) = I(X_{t−τ}, Y_{t−τ}; X_t, Y_t) − max{I(X_{t−τ}; X_t, Y_t), I(Y_{t−τ}; X_t, Y_t)}.
  - Φ = I(X_{t−τ}, Y_{t−τ}; X_t, Y_t) − I(X_{t−τ}; X_t) − I(Y_{t−τ}; Y_t),
    the whole-minus-sum measure of IIT 2.0 in Barrett and Seth's empirical
    form.
  - ΦR = Φ + Red, shown non-negative in Mediano et al. (2021).
  - The analysis uses persistent synergy and persistent redundancy, "the
    information that is always carried synergistically (respectively,
    redundantly)".
- **Workspace membership.** Taken from earlier work (Luppi et al. 2022b).
  A region's synergy rank minus its redundancy rank, by nodal strength, is
  computed over the group-average HCP matrices. Regions favouring synergy
  form the workspace. The gradient is relative: a positive value "does
  not necessarily mean that the region's synergy is greater than its
  redundancy".
- **Gateways and broadcasters, by sign.** Within the workspace, the rank
  of each region's participation coefficient in the synergy network minus
  its rank in the redundancy network is computed, with modules taken as
  the seven Yeo networks plus a subcortical one. Positive means gateway;
  negative means broadcaster. Every workspace region is therefore one or
  the other by construction.
- **Unconsciousness.** Propofol at Ramsay 5 (no response to verbal
  command), and chronic disorders of consciousness, which include both
  unresponsive wakefulness and minimally conscious patients. Both are
  treated as loss of consciousness.

## Key results

- **Data.**
  - The HCP sample is N = 100, with 454 ROIs (Schaefer-400 plus Tian-54)
    and a replication at 232 ROIs.
  - Propofol volunteers are "N=15" in the Introduction, but the Methods
    report n = 19 recruited, 3 excluded and "a total n=16 for analysis".
    The paper does not reconcile the two.
  - The DOC sample is 22 adults (from 71 recruited), aged 17–70,
    13 months post-injury on average, with UWS or MCS diagnoses.
- **Where gateways and broadcasters are (Fig. 2).** "Gateways reside
  primarily in the brain's default mode network", and "broadcasters are
  mainly located in the executive control network, especially lateral
  prefrontal cortex". The participation coefficients correlate between a
  priori modules and Louvain modules (spin test), and the classification
  replicates at the coarser parcellation.
- **ΦR across states (Fig. 4).** The NBS F-threshold was 9. ΦR is
  reorganised for DOC against awake (p < 0.001), for propofol against
  pre-induction (p < 0.001), and for propofol against recovery
  (p < 0.001), with both increases and decreases.
  - A composite test asks for edges that change in all three contrasts.
    Its statistic is the minimum of the three F-scores, with one dataset
    reshuffled at a time. It is a least-favourable-configuration test
    whose "details will be described in a future publication".
  - **Common decreases:** bilateral precuneus and medial prefrontal
    cortex, bilateral inferior parietal cortex, and left temporal
    cortices.
  - **Common increases:** frontal cortex, "especially lateral prefrontal
    cortex".
  - The net balance favours reduction: the sum of F-scores over the
    significant edges is −25.37.
- **The original Φ (Fig. 4—supplement 2).** It "did not identify any
  reductions in integrated information that were common across
  anaesthesia and disorders of consciousness, instead only identifying
  common increases".
- **Gateways, not broadcasters (Fig. 5).** The regions with consistent
  ΦR reductions "play the role of gateway nodes … rather than broadcaster
  nodes". The caption says "all regions are gateways (violet)". The
  reductions read as an "anterior-posterior disconnection … between DMN
  nodes that act as gateways".
- **Robustness.** Decreases in medial prefrontal and posterior cingulate
  or precuneus survive a coarser parcellation, an extent-based NBS
  threshold and F > 12. The increases do not: "no region consistently
  showing increases".
- **Propofol against wake alone.** Reductions also appear in thalamic,
  auditory and somatomotor regions. The authors read this as
  thalamocortical isolation, with no EEG to confirm it.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Within the synergy-defined workspace, regions with synergy-dominant intermodular connections are mainly DMN, and regions with redundancy-dominant ones mainly fronto-parietal | moderate | HCP N = 100, group-average matrices, replicated at a second parcellation and module definition (Fig. 2) |
| C2 | Pairwise ΦR between DMN gateway regions falls under both propofol and DOC, and recovers after propofol | moderate | NBS with a composite shared-effect test across three contrasts; robust to parcellation and threshold (Figs. 4–5) |
| C3 | The original whole-minus-sum Φ shows no such common reduction, so ΦR is the empirically valid measure | moderate for the contrast; weak for "validity" | Fig. 4—supplement 2 |
| C4 | Loss of consciousness is a breakdown of the entry points to the synergistic core | weak | interpretation of C2; resting state, correlational |
| C5 | Different subsets of the workspace are differentially involved in supporting consciousness | weak | the non-robust increases near broadcasters, against the robust gateway decreases |

## Method

1. Preprocess resting-state fMRI (CONN, aCompCor, no global signal
   regression, 0.008–0.09 Hz) and deconvolve the haemodynamic response.
2. Compute Gaussian MMI-ΦID quantities for every pair of the 454 regions
   with JIDT.
3. Build networks of synergy, redundancy and ΦR.
4. Rank by nodal strength to find the workspace (from the earlier paper),
   and by participation coefficient to split it into gateways and
   broadcasters.
5. Test state differences in ΦR edges with the network-based statistic
   and the composite shared-effect test.

## Concepts

- **Synergistic workspace.** As defined here: regions whose synergy rank
  exceeds their redundancy rank by nodal strength, relative to the rest of
  the brain.
- **Gateway.** A workspace region whose participation coefficient ranks
  higher in the synergy network than in the redundancy network. It is
  "synergistic with many modules".
- **Broadcaster.** A workspace region with the opposite rank order. It
  "possess[es] information that is duplicated across multiple modules".
  Broadcasting is read as redundancy: "Sameness of information
  corresponds to redundancy".
- **ΦR (revised Φ).** The whole-minus-sum Φ plus the double redundancy,
  which removes the negative values of Φ in redundancy-dominated systems.
  It counts synergistic and transferred information.

## Connections

The paper builds on the ΦID framework of Mediano, Rosas and colleagues,
whose emergence side the record reads in [LIT-025](../literature.d/LIT-025.md). It extends the authors'
earlier "synergistic core" paper (Luppi et al. 2022b), which supplies the
workspace definition, and their DOC and propofol datasets (Luppi et al.
2019). It positions itself between GNWT (Mashour et al. 2020, [LIT-631](../literature.d/LIT-631.md)) and
IIT. It aligns with Shanahan's "connective core", and contrasts with
Deco et al.'s task-based, directed (transfer-entropy) workspace.

## Bearing on the record

- **[QUESTION-061](../questions.d/QUESTION-061.md)** asks whether conscious access is one exclusive
  broadcast to every consumer, or whether a content can reach some
  consumers and not others. [LIT-949](../literature.d/LIT-949.md) was filed as "measured evidence on
  whether conscious access is one uniform broadcast or has distinct
  parts". The paper bears on that weakly and indirectly.
  - **No contents.** It measures the state of consciousness at rest, not
    the access of any content. There is no stimulus, no report and no
    consumer-by-consumer measurement, so it cannot show a content
    available to one system and absent from another, which is what the
    question says would answer it.
  - **The split is built in.** The division of the workspace into an
    input side and an output side is imposed by the method: every
    workspace region is classed by the sign of a rank difference. What
    is measured is where the two classes fall (DMN against FPN), and
    that the consistent loss is on the input side.
  - **What it gives the question.** The authors read the robust gateway
    decreases, against the non-robust broadcaster increases, as "different
    subsets of the global workspace may be differentially involved". That
    is evidence that the workspace is not functionally uniform with
    respect to consciousness. It is not evidence that access is
    compartmented by consumer.
- **[THEORY-096](../theory.d/THEORY-096.md)** (GNW). The paper is consistent with lateral prefrontal
  cortex as a broadcaster, a role the GNW review assigns it. But the
  consciousness-tracking change it finds is in the default-mode
  gateways. Lateral prefrontal ΦR rose, not fell, in unconsciousness,
  though not robustly. It tests no ignition and no exclusivity, so it
  neither supports nor refutes [THEORY-096](../theory.d/THEORY-096.md)'s mechanism.
- **[THEORY-098](../theory.d/THEORY-098.md).** Under propofol alone, reductions also reach thalamic,
  auditory and somatomotor regions. That fits a loss of sensory input to
  the core, as the authors say. It is a state effect at rest and does not
  bear on whether recurrent sensory activity is the basis of experience.
- **[CLAIM-003](../claims.d/CLAIM-003.md).** It does not bear. The claim is about compartmented
  access, and the paper measures an undirected, content-free integration
  between pairs.
- **[CLAIM-158](../claims.d/CLAIM-158.md)** and the record's ΦID material. The paper uses ΦID for
  pairwise integration only. It does not use the downward-causation or
  causal-decoupling terms that the drive-profile work draws on.
- No instruction for machine-learning practice; nothing for the
  anthology.

## Limitations

- BOLD at a 2 s TR is an indirect, slow proxy. Deconvolution mitigates
  this and does not remove it.
- The measures are pairwise and undirected. They are not IIT's Φ of the
  whole system, and they rest on IIT 2.0, not IIT 3.0 or 4.0.
- The results are correlational. The authors disclaim that ΦR causes
  consciousness or is identical to it.
- The gateway and broadcaster classes are relative ranks, defined on the
  HCP group average and transferred to the clinical datasets. They are
  not re-derived in those datasets.
- The DOC group includes minimally conscious patients, so "loss of
  consciousness" there is graded, not absent. Propofol participants may
  have been "merely disconnected but still conscious".
- Resting state "may have resulted in an overestimation of the DMN's
  role in consciousness, and an under-estimation of the FPN".
- The shared-effect test's details are deferred to a future publication.
  The propofol sample size is given as both 15 and 16.

## Open questions

- Does the gateway/broadcaster asymmetry hold in task data with
  stimulus contents and report, where access can be measured per
  consumer? The authors name task paradigms and higher temporal
  resolution as next steps.
- Do causal interventions that restore consciousness (central thalamic
  stimulation) restore gateway ΦR? The paper proposes the test.
- Would a directed decomposition (ΦID of transfer entropy) show
  broadcasting as directed redundancy from the FPN, rather than as
  inferred from undirected participation?
