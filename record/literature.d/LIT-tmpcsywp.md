---
status: Active
status_note: 'read 2026-10-09 (NOTE-tmp9okql); worth reading as the paper in which the RSA recursion is made to derive Horn''s division of pragmatic labour (costlier forms for less likely meanings) in one-shot signalling games with no prior conventions: the basic recursion cannot break the symmetry between equally meaningless costly and cheap signals, but a listener and speaker uncertain about the lexicon, marginalizing over every lexicon that could assign the signals meanings, converge on the efficient mapping without an equilibrium-selection rule. Two small Mechanical Turk games (40 and 140 participants) show people drawing specificity and Horn implicatures among novel symbols in five rounds, with no first-round difference. Source, with LIT-tmpkwn2g and LIT-tmphavsf, of THEORY-tmprknoj.'
title: 'That''s what she (could have) said: How alternative utterances affect language use'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full on 2026-10-09 (NOTE-tmp9okql) from the eScholarship copy
    of the proceedings paper (UC Merced, Proceedings of the Annual Meeting
    of the Cognitive Science Society 34, item 5f03m09d, served as
    repositories.cdlib.org/content/qt5f03m09d/qt5f03m09d.pdf; the
    escholarship.org PDF link returned 403 to the download, the CogSci
    2012 archive at csjarchive.cogsci.rpi.edu failed to connect). The
    paper's pages are 120–125. Checked against the eScholarship record
    (title, authors, volume 34, publication date 2012, ISSN 1069-7977)
    and against the citation in Goodman and Frank 2016 (LIT-tmphavsf).
    No DOI and no arXiv version, so the source is the eScholarship URL.
    `published:` is 1 January 2012: the record gives the year only. Not
    held in the Anthology of the SOTA: a grep of its record/ (clone of
    2026-10-09, commit d8b5ba5) for the authors, the title and the
    eScholarship id found nothing.
tags:
- linguistics
- game-theory
- cognition
- probabilistic-modeling
date: '2026-10-09'
published: '2012-01-01'
url: 'https://escholarship.org/uc/item/5f03m09d'
first_author: 'Bergen'
keywords:
- 'pragmatics'
- 'communication'
- 'Bayesian modeling'
- 'specificity implicature'
- 'Horn implicature'
- 'lexical uncertainty'
- 'signalling games'
implementations: []
summary: >-
  Bergen, Goodman & Levy (2012), Proceedings of the 34th Annual Meeting
  of the Cognitive Science Society, 120–125. Recursive speaker–listener
  reasoning yields specificity implicatures, but cannot derive Horn's
  principle from costs alone; adding uncertainty over the lexicon does,
  in one-shot signalling games, without equilibrium refinements. Two
  online games with novel symbols find both implicatures drawn without
  prior conventions.
---
<!-- inactive-ok-file: THEORY-tmprknoj — Proposed; open, and cited as open: the claim, argument or reading is under test, not settled -->
<!-- inactive-ok-file: LIT-473 — Deferred; filed, not read, and cited only as the source of the signalling-game framing -->

# LIT-tmpcsywp: That's what she (could have) said: How alternative utterances affect language use

Leon Bergen, Noah D. Goodman and Roger Levy (2012), *Proceedings of the
34th Annual Meeting of the Cognitive Science Society*, 120–125 —
https://escholarship.org/uc/item/5f03m09d

## Key takeaways

- **The base model.** L₀(m|u) ∝ L_u(m)P(m); S_n(u|m) ∝ exp(λU_n(u|m)),
  U_n = log L_{n−1}(m|u) − c(u); L_n(m|u) ∝ P(m)S_{n−1}(u|m). With a
  specific and a general utterance ("pyramid", "shape") the general one is
  read as the meaning the specific one excludes, and the tendency goes to
  probability 1 with depth for λ > 1.
- **Why costs alone fail.** If two signals are both literally all-true
  and differ only in cost, L₀ reads both as the prior, S₁ just disprefers
  the costly one, and nothing breaks the symmetry. This is the
  multiple-equilibrium problem of signalling games.
- **Lexical uncertainty.** Let each utterance's literal meaning be any
  non-trivial truth function, put a uniform prior over the seven
  lexicons in the 2 × 2 case, and let L_n marginalize over them. A
  speaker who means the unlikely meaning gains from a costly signal that
  pins it down; a speaker who means the likely one does not, since L₀
  already reads the cheap signal as likely. So L₂ prefers the efficient
  mapping, and higher levels sharpen it. Shown also for three meanings
  and three costs.
- **Experiment 1** (40 participants): two objects, an iconic triangle and
  an alien symbol; listeners read the alien symbol as the cube on every
  trial, speakers used it for the cube on every trial.
- **Experiment 2** (140 participants): three objects at 60/30/10% and
  messages costing $0, $0.01 and $0.02; speakers and listeners used the
  efficient mapping (mixed logit, all six comparisons p < .001), with no
  first-round effect in five of six response types.

## Standing in the record

Filed on 2026-10-09 at the owner's request, from the manuscript
bibliography of 2026-10-09 (work `what-survives-translation`): one of the
works the manuscript considered and dropped from its final reference list.

Read on 2026-10-09 (NOTE-tmp9okql). With LIT-tmpkwn2g and LIT-tmphavsf it
is the source of THEORY-tmprknoj. Its premise, common knowledge of
communicative goals, and its signalling games are Lewis's (LIT-473,
filed but not read); the paper's point is that in such games the
efficient conventions can be reached by reasoning in one shot, without
the precedent or evolution Lewis's conventions rest on.
