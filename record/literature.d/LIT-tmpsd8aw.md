---
status: Active
status_note: >-
  read 2026-11-17 ([NOTE-tmpwpvfg](../notes.d/NOTE-tmpwpvfg.md)) from arXiv:1706.09847v3; worth reading
  here for its demonstrated lock-in of a loop that selects its own
  evidence, and its repair.
title: 'Runaway Feedback Loops in Predictive Policing'
version: 2
history:
- version: 1
  date: '2026-11-17'
  note: >-
    Filed, not read, from the exchange "Assess Depp Heard Abuse"
    (2026-11-17). Checked on 2026-11-17: not held in record/literature.d
    by identifier, title or first author. arXiv API (1706.09847): title
    and authors as given, v1 submitted 2017-06-29. A cites the PMLR 81
    proceedings version (2018). `published:` is 2017-06-29, arXiv v1,
    earlier than the 2018 proceedings A gives. No email address was sent
    to any service.
- version: 2
  date: '2026-11-18'
  note: >-
    Read on 2026-11-17 from arXiv:1706.09847v3 (22 December 2017), in full
    except the references; NOTE-tmpwpvfg, THEORY-tmp0xl3k. v3's comment
    calls it the "Extended version accepted to the 1st Conference on
    Fairness, Accountability and Transparency, 2018", and its header reads
    "Proceedings of Machine Learning Research 81:1–12, 2018"; v3 "Adds
    further treatment of reported as well as discovered incidents". The
    PMLR page was not fetched. `published:` stays v1, 2017-06-29.
    Deferred → Active.
tags:
- society-and-governance
- probabilistic-modeling
- ethics
- anthology-candidate
date: '2026-11-17'
published: '2017-06-29'
arxiv: '1706.09847'
first_author: 'Ensign'
keywords:
- 'predictive policing'
- 'feedback loops'
- 'urn models'
- 'fairness'
implementations: []
summary: >-
  Danielle Ensign, Sorelle A. Friedler, Scott Neville, Carlos Scheidegger
  and Suresh Venkatasubramanian (2017; FAT* 2018). Runaway Feedback Loops
  in Predictive Policing. arXiv:1706.09847; PMLR 81 (2018). A generalized
  Pólya urn: police go where recorded incidents are, and incidents are
  recorded where police go. Even granting that recorded incidents occur at
  the true rates, the process does not learn them: equal rates leave the
  prior in place, and unequal rates, however close, lock onto the higher
  one with probability 1. Reported incidents attenuate but do not remove
  the loop; dropping each discovered incident with the probability of
  having patrolled there repairs it. Simulations of PredPol on Oakland data
  reproduce both. Read in [NOTE-tmpwpvfg](../notes.d/NOTE-tmpwpvfg.md); [THEORY-tmp0xl3k](../theory.d/THEORY-tmp0xl3k.md).
---
<!-- inactive-ok-file: THEORY-tmp0xl3k — new, temporary codes, Proposed -->

# LIT-tmpsd8aw: Runaway Feedback Loops in Predictive Policing

Danielle Ensign, Sorelle A. Friedler, Scott Neville, Carlos Scheidegger and Suresh Venkatasubramanian (2017; FAT* 2018). Runaway Feedback Loops in Predictive Policing. arXiv:1706.09847; *Proceedings of the 1st Conference on Fairness, Accountability and Transparency*, PMLR 81 (2018).

## Key takeaways

- "predictive policing algorithms only observe crime in neighborhoods they
  patrol" (p. 1).
- Lemma 4: unequal rates lock in, "a classic 'go with the winner'
  problem"; Lemma 2: equal rates leave the prior in place.
- Reported incidents "can attenuate the degree of runaway feedback" but
  "cannot entirely remove it without the interventions we suggest"; the
  repair drops discovered incidents with the probability of patrol.

## Standing in the record

Registered on 2026-11-17 from the exchange "Assess Depp Heard Abuse" (2026-11-15 to 2026-11-17), https://chatgpt.com/share/6afcb46d-83a8-83e9-9c85-4a0c3604405b, where A cites it at A19 as A's formal demonstration of self-validating classification. Read on 2026-11-17 ([NOTE-tmpwpvfg](../notes.d/NOTE-tmpwpvfg.md)). It corroborates [CLAIM-342](../claims.d/CLAIM-342.md) and [CLAIM-406](../claims.d/CLAIM-406.md) ([THEORY-tmp0xl3k](../theory.d/THEORY-tmp0xl3k.md)), and qualifies [CLAIM-342](../claims.d/CLAIM-342.md)'s remedy: independent evidence mixed in only attenuates the loop. The anthology may want it.

**The exchange's characterization: faithful.** A19's "deployment choices
can bias subsequent observations and produce runaway feedback" is right.
Its gloss, that the classification "can help create the evidence
subsequently used to justify" it, fits Lemmas 2 and 4, with one sharpening:
the loop amplifies a real but small difference, or freezes the prior where
there is none; it does not create crime. The analogy to interpersonal
coercive control is A's.
