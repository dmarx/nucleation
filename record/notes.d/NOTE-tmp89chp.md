---
status: Read
paper: 'LIT-tmpciuti'
title: 'Chou, Wilson & Smith — The influence of anxiety on exploration'
version: 1
history:
- version: 1
  date: '2026-10-24'
  note: >-
    Read in full on 2026-10-24 from the PsyArXiv preprint, version 1
    (doi:10.31234/osf.io/wtfr6, posted 24 June 2024, the only version;
    OSF file "manuscript_anxiety_exploration.pdf"), a 44-page PDF of the
    authors' manuscript, licensed CC BY 4.0. Text extracted by pdftotext.
    Read: pp. 1–31 (abstract, sections 1–4), Figures 1–5 from their
    captions and in-text descriptions, and Tables 1–3 (pp. 41–43). The
    reference list (pp. 32–41) was used only to check citations. The
    version of record, Neuroscience & Biobehavioral Reviews 167 (2024),
    105940, is closed (Elsevier licence; Unpaywall and OpenAlex list only
    the preprint). Its abstract on PubMed (PMID 39515626) adds two
    sentences on computational psychiatry and the value of information
    that the preprint's lacks, so the text changed in review; whether the
    findings did is not known. Page numbers are the preprint's.
date: '2026-10-24'
summary: >-
  A narrative review of computational modelling studies of anxiety and
  exploration, almost all in reward tasks and sub-clinical samples. In
  bandit tasks, directed exploration tends to rise with trait or cognitive
  anxiety and fall with state or somatic anxiety; random exploration shows
  no link; in foraging tasks, and in one task with a predator to check
  for, anxiety goes with less exploration. Results are inconsistent across
  tasks and measures and none has been replicated.
---
<!-- inactive-ok-file: CLAIM-tmp8z857 THEORY-tmpf8za8 THEORY-tmp0vr2q — Proposed; the claim and readings this bears on, named, nothing here rests on them -->

# NOTE-tmp89chp: Chou, Wilson & Smith — The influence of anxiety on exploration

## Contribution

It gathers, for the first time, the computational modelling studies that
relate anxiety to exploration, sorted by task (Horizon, two-armed,
dynamic and spatially correlated bandits, patch foraging), by kind of
exploration (directed, random, foraging, non-instrumental), and by facet of
anxiety (state or trait, somatic or cognitive). Its conclusion is that
"anxiety" and "exploration" are both too coarse: the direction of the
relation depends on which of each is measured.

## Key insight

Anxiety can drive information-seeking up or down, and both can serve to
avoid uncertainty: "some aspects of anxiety could promote avoidance of
novel sources of information to avoid uncertainty, while others might
instead elevate information-seeking to minimize that uncertainty" (p. 2).
The review's closing phrase: "both over-exploration and under-exploration
could be seen as manifestations of uncertainty avoidance" (p. 31).

## Assumptions

- **Two kinds of exploration (pp. 3–4; Table 1).** Directed exploration
  chooses the option with most uncertainty, measured as an information
  bonus; random exploration adds choice noise that grows when information
  would be useful. Foraging is treated as distinct: leaving a depleting
  patch is governed by the expected average reward of the environment
  (pp. 13–14).
- **Two kinds of uncertainty (p. 3).** Outcome uncertainty (noise, should
  lower learning rate) and environmental uncertainty (volatility, should
  raise it).
- **Facets of anxiety (pp. 2, 42–43; Tables 2–3).** State against trait
  (STAI), somatic against cognitive (STICSA), plus GAD-7, OASIS, ASI and
  others; stress (PSS, cold pressor) is treated with anxiety in some
  studies, with a caveat that "stress and anxiety are not identical
  constructs" (p. 20).
- **Not a systematic review.** No search strategy or inclusion criteria
  are given.

## Key results

- **Directed exploration (pp. 15–18).**
  - Trait anxiety went with more choice of uncertain options in a dynamic
    bandit, with an inverted-U relation to performance (Aberg et al.
    2022).
  - In the Horizon Task, state anxiety went with less directed
    exploration, partly because anxious people sought information when it
    was not useful: "reduced directed exploration with high anxiety was
    partially explained by greater information-seeking when it was not
    useful" (p. 16; Smith et al. 2022c).
  - Somatic anxiety went with less directed exploration in two datasets of
    a two-armed bandit, explained by underestimated relative uncertainty
    (Fan et al. 2023b); negative affect went with more, in one dataset.
  - In a spatial bandit, cognitive anxiety went with more exploration
    under risk and somatic anxiety with less, and a worry-reduction
    intervention reduced exploration (Witte et al. 2024), "some initial
    evidence of a causal association" (p. 17).
  - In patients with anxious depression, directed exploration was higher
    than in low-anxiety controls, and a breathing-based state-anxiety
    induction reduced it to the controls' level (Li et al. 2024; Goldman et
    al. 2024).
  - Not replicated: an association with information sensitivity "did not
    replicate in a second sample within a confirmatory study" (p. 18), and
    a preliminary report found none with worry or intolerance of
    uncertainty (Zaller et al. 2021).
- **Random exploration (pp. 19–20).** "Unlike directed exploration, no
  studies to date have specifically linked random exploration to anxiety"
  (p. 19). Noradrenergic drugs change random exploration, in opposite
  directions in different studies.
- **Foraging (pp. 20–23).** Acute and chronic stress led to over-staying
  (Lenow et al. 2017); generalized anxiety went with less exploration when
  physical effort was required (Bustamante et al. 2023) and with less
  adjustment of choice stochasticity to volatility (Lloyd et al. 2022a).
  In a foraging task with a predator, people higher in trait somatic
  anxiety checked for the predator less and did worse: "Further analyses
  suggested these reductions in checking behavior were associated with a
  greater aversion to detecting the predator" (p. 22; Trier et al. 2023).
  Human open-field and elevated-plus-maze studies agree (p. 23).
- **Non-instrumental information-seeking (pp. 23–24).** Inconsistent:
  null in two studies, higher willingness to pay for information with
  trait or somatic anxiety in two others, and more seeking under high
  volatility in one.
- **Learning rates (pp. 25–28).** Trait anxiety goes with less adjustment
  of learning rate between volatile and stable conditions and with higher
  learning rates after losses; induced state anxiety sometimes with slower
  learning; somatic and cognitive anxiety in opposite directions (Wise &
  Dolan 2020). Whether these explain the exploration differences "remains
  to be thoroughly tested" (p. 28).
- **The summary (pp. 28–29).** Four points: trait or cognitive anxiety
  may increase and somatic or state anxiety decrease directed
  exploration; no direct link to random exploration; foraging exploration
  "is deterred in those with high anxiety, perhaps due to risk aversion
  and/or pessimistic expectations"; non-instrumental information-seeking
  is inconsistently related.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | In bandit tasks, directed exploration tends to increase with trait or cognitive anxiety and decrease with state or somatic anxiety | weak to moderate: mixed results, different tasks and measures, no replication | about eight studies; pp. 15–18 |
| C2 | Random exploration is not related to anxiety | weak: absence of evidence | p. 19 |
| C3 | In foraging tasks anxiety and stress go with less exploration | moderate: consistent direction across several tasks and measures | about six studies; pp. 20–23 |
| C4 | Somatic anxiety can reduce checking for threat through aversion to detecting it | weak: one study | Trier et al. 2023; p. 22 |
| C5 | Over- and under-exploration in anxiety may both serve uncertainty avoidance | interpretive | the authors' framing; pp. 2, 31 |

## Concepts

- **Directed exploration**: "choosing actions with the highest
  uncertainty" (Table 1), measured as an information bonus that grows when
  information has future use.
- **Random exploration**: "occasionally choosing actions that do not
  appear best" (Table 1), measured as choice noise that grows with horizon
  or total uncertainty.
- **Somatic against cognitive anxiety**: physiological symptoms (tension,
  arousal) against worry, rumination and intrusive thoughts (p. 2; Table 2).

## Connections

It rests on Wilson et al.'s Horizon Task (2014), Gershman's two-armed
bandit (2018, 2019), Constantino & Daw's foraging task (2015) and Piray &
Daw (2021) on noise and volatility. It overlaps with Brown et al.
([LIT-tmp9li67](../literature.d/LIT-tmp9li67.md)) on uncertainty learning in anxiety but concentrates on
exploration in reward tasks, where Brown et al. concentrate on avoidance in
aversive ones. It suggests exposure therapy "can be straightforwardly
conceptualized as directed exploration, where an individual tests their
expectations by approaching feared situations currently being avoided"
(p. 30), as Brown et al. do.

## Bearing on the record

- **[CLAIM-tmp8z857](../claims.d/CLAIM-tmp8z857.md) (governance-maintained anxiety).** The claim says
  anticipated threat gives defensive processes authority over "evidence
  acquisition", and that in hypervigilance the failure is "not less
  information seeking but poorly governed information seeking: checking,
  reassurance and scanning that never acquire the information that would
  discriminate the hypotheses".
  - **Supported, narrowly.** Two findings fit. Anxious people sought
    information when it could not be used and less when it could (Horizon
    Task), which is information-seeking badly matched to its use. And
    people higher in somatic anxiety checked less for a predator, out of
    aversion to finding it: evidence acquisition about the threat itself
    reduced by the threat. Each is one study.
  - **Narrowed.** The review's main finding is that the direction depends
    on the facet: trait and cognitive anxiety go with more directed
    exploration, state and somatic anxiety with less. The claim's
    grant of defensive authority over "evidence acquisition" predicts less
    exploration. It fits the somatic and state facet and foraging, not
    trait and cognitive anxiety in bandits, so the claim either belongs to
    one facet or needs to say how authority can raise exploration.
  - **Mostly not about threat.** Nearly every task rewards points and
    threatens nothing; only the predator task and the shock-learning
    studies involve threat. The claim is about threat. Studies of
    exploration under threat are what would test it.
- **[THEORY-tmpf8za8](../theory.d/THEORY-tmpf8za8.md) (Brown et al.'s loop).** Foraging results and the
  predator task fit its prediction that uncertainty under threat reduces
  exploration; the bandit results with trait anxiety do not obviously fit,
  but they are reward tasks, where Brown et al. predict the opposite sign.
- **[THEORY-tmp0vr2q](../theory.d/THEORY-tmp0vr2q.md).** The learning-rate section reports the same
  studies (Browning et al. 2015) and adds the opposite directions for state
  and trait, and for somatic and cognitive, anxiety.
- **Corrections.** The exchange's description (directed exploration
  raised by cognitive or trait anxiety and lowered by state or somatic
  anxiety; less exploration in foraging) is accurate, with the authors'
  "may". The record should add that the review is narrative, not
  systematic, that most studies are sub-clinical and none replicated, and
  that the preprint appeared on 24 June 2024, which is `published:` under
  [ADR-002](../decisions.d/ADR-002.md), not the November online date.
- Filed: [THEORY-tmphx93a](../theory.d/THEORY-tmphx93a.md) (directed and random exploration in bandit tasks)
  and [THEORY-tmpapk2z](../theory.d/THEORY-tmpapk2z.md) (less exploration in foraging, and less checking for
  threat).
- No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- **Mostly sub-clinical samples**; the authors say "the majority of
  studies to date have used sub-clinical samples" (p. 31).
- **Inconsistent tasks and measures.** "results have been somewhat
  inconsistent, as has been choices of tasks and anxiety measures, and
  replication studies have not been reported" (p. 31).
- **Reward tasks.** Exploration is mostly measured where nothing aversive
  is at stake, which limits what the review says about anxious avoidance.
- **Not systematic.** No search or inclusion criteria; Smith is an author
  of several of the studies reviewed.
- **Preprint, not the version of record**, whose abstract differs.
- **Slips.** "STISCA" for STICSA (pp. 17, 27); "this chapter" for an
  article (p. 26). Neither changes a conclusion.

## Open questions

- Do the facet-specific directions hold when the same people do the same
  tasks with the same anxiety measures, as the authors ask?
- Does anxiety change exploration under threat (where the options can hurt)
  in the way it changes exploration for reward?
- Does treatment that changes exploration (exposure, behavioural
  activation) change anxiety, or the reverse?
