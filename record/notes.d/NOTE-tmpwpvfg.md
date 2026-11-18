---
status: Read
paper: LIT-2688
title: 'Ensign et al. — Runaway Feedback Loops in Predictive Policing'
version: 1
history:
- version: 1
  date: '2026-11-18'
  note: >-
    Read on 2026-11-17 from arXiv:1706.09847v3 (22 December 2017), the
    FAT* 2018 extended version with the PMLR header ("Proceedings of
    Machine Learning Research 81:1–12, 2018"), https://arxiv.org/pdf/1706.09847,
    12 pages, text by pdftotext. Read in full except the references,
    including the urn derivations of §3.4 and the simulations of §§4–5.
    The PMLR page was not fetched. Page numbers are the PDF's; the
    two-column layout scrambles some extracted lines, and the quotes below
    were rechecked by the filer against a layout-preserving extraction of
    the same copy on 2026-11-18.
date: '2026-11-18'
summary: >-
  The authors model predictive policing as a generalized Pólya urn: police
  go where recorded incidents are, and incidents are recorded where police
  go. Even if recorded incidents occur at the true crime rates, the process
  does not learn them: with equal rates the prior persists, and with
  unequal rates it locks onto the higher-rate region with probability 1.
  Reported incidents attenuate the loop but do not remove it. Dropping each
  discovered incident with the probability of having patrolled there
  repairs it.
---
<!-- inactive-ok-file: THEORY-tmp0xl3k — new; the work read and the account filed from it -->

# NOTE-tmpwpvfg: Ensign et al. — Runaway Feedback Loops in Predictive Policing

## Contribution

A formal explanation of why the predictive-policing feedback loop occurs,
a link between its severity and the disparity in crime rates and the
weight of discovered incidents, and a black-box correction of the inputs.

## Key results

- **The loop** (§1, p. 1): "predictive policing algorithms only observe
  crime in neighborhoods they patrol"; "Decisions made by the system
  influence the data that is fed to it in the future."
- **The prior persists** (§3.2, Lemma 2): "the prior belief coupled with
  the lack of feedback about the unobserved region prevents the system
  from learning that the two areas are in fact identical with respect to
  crime rates."
- **Lock-in** (§3.3, Lemma 4): with unequal rates, however close, "the
  update process will settle on region B with probability 1. This is a
  classic 'go with the winner' problem".
- **Reported incidents only attenuate** (abstract): "while reported
  incidents can attenuate the degree of runaway feedback, they cannot
  entirely remove it without the interventions we suggest." The limit
  approaches the truth only if discovered incidents are down-weighted or
  the rates are nearly equal, and "it is precisely when crime rates are
  different that predictive policing is of value" (§3.4, p. 7).
- **The fix** (§3.5.1, p. 7): if the procedure sends police to a region 90%
  of the time, "we should simply drop the incident record 90% of the time",
  a rejection-sampling form of Horvitz–Thompson estimation.
- **PredPol** (§2.1, p. 3): "PredPol, in essence, is predicting where
  incidents will be reported or discovered (since that's all it sees), not
  where crime will happen." Simulations on Lum and Isaac's Oakland data
  reproduce the loop and its repair (§5).
- **The key assumption** (§6, p. 11): "One of the most crucial assumptions
  we make (and one that in fact is sympathetic to current predictive
  policing models) is that reported and discovered incident rates track
  the true crime rates."

## Assumptions

- Two regions; generalization expected, not shown.
- Counts only, no other context.
- Discovered and reported incidents occur at the true rates, stated as
  generous to the systems.
- Patrols allocated in proportion to the estimates.
- Decay is added in simulation without a theoretical result.

## Concepts

- **Runaway feedback loop**.
- **Discovered** against **reported** incidents.
- **Generalized Pólya urn**; **"go with the winner"**.
- **Rejection sampling** as Horvitz–Thompson correction.

## Bearing on the record

Filed as [THEORY-tmp0xl3k](../theory.d/THEORY-tmp0xl3k.md).

- **[CLAIM-342](../claims.d/CLAIM-342.md)** (a loop that selects its own evidence can lock in; what
  stops it is evidence whose arrival does not pass through the
  interpretation): a demonstrated instance (Lemma 4), in which action,
  deployment, is the selector. It also qualifies the claim's remedy:
  independent evidence (reported incidents) mixed with self-selected
  evidence only "attenuate[s]" the loop. The authors' fix reweights the
  self-selected stream by the probability of selection, rather than only
  adding independent evidence. Corroborates.
- **[CLAIM-406](../claims.d/CLAIM-406.md)** (an early exclusion kept going by indicators that only
  being sought produces): Lemma 2, where the prior alone fixes the
  long-run estimate because the unobserved region yields no evidence, and
  Lemma 4, where a small early advantage takes all. Nothing about the
  prejudice condition the claim says the dynamics cannot contain, which
  is consistent with it. Corroborates.
- The record's other Pólya-urn holdings were not checked for the same
  lock-in; a later reader may compare them.
- The loop amplifies a real but small difference, or freezes the prior
  where there is none; it does not create crime. The exchange's analogy to
  interpersonal coercive control is A's.

## Limitations

- A stylized two-region model; simulation, not field data.
- The "true rate" assumption favours the systems.
- No result for the urn with decay.
