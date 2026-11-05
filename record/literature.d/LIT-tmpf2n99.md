---
status: Active
status_note: >-
  read 2026-11-05 (NOTE-tmptvl7g) from the authors' arXiv v1 preprint, main
  text in full, the Supporting Information skipped; the PNAS version was
  not reached (a Cloudflare challenge at pnas.org, a firewall at MIT
  DSpace). Worth reading as a worked case in which the self-stress
  bookkeeping of rigidity theory does design work: removing about 1% of
  the bonds of a disordered spring network, chosen greedily with an
  analytic update built on its states of self-stress and of compatible
  stress, tunes a chosen strain ratio between a distant target pair and a
  source pair with near-total success, also for several targets or
  several independent pairs at once, and laser-cut and 3D-printed networks
  reproduce it. Its main limits: linear response, athermal, central
  forces, no prestress; greedy and with no account of why particular bonds
  work; rigidity is a precondition, and tuning fails more often at low
  excess coordination.
title: 'Designing allostery-inspired response in mechanical networks'
version: 1
history:
- version: 1
  date: '2026-11-05'
  note: >-
    Registered and read on 2026-11-05 from the owner's pasted synthesis on
    FACT, rigidity, compliant mechanisms and origami, written by another
    assistant (A) and pasted by the owner on 2026-11-04, which cites it as
    M8. Citation checked against Crossref by the reader: Jason W. Rocks,
    Nidhi Pashine, Irmgard Bischofberger, Carl P. Goodrich, Andrea J. Liu
    and Sidney R. Nagel, Proceedings of the National Academy of Sciences
    114(10), 2520–2525, journal article; PMC5347623; first posted as
    arXiv:1607.08562 v1 on 2016-07-28, its only version. A's citation is
    correct. `published:` is the arXiv v1 date, the earliest exact date
    (ADR-002); the PNAS online date is 2017-02-21. Not held
    before (no hit for the DOI, the arXiv id, the PMC id, the title or the
    authors). Copy: the arXiv v1 PDF, https://arxiv.org/pdf/1607.08562,
    28 single-column pages, extracted with pdftotext. The published text
    was not reached: https://www.pnas.org/doi/pdf/10.1073/pnas.1612139114
    returned a Cloudflare challenge, and both bitstreams of MIT DSpace
    (http://hdl.handle.net/1721.1/112223) a "Web Firewall · 429"; neither
    was retried. The preprint may differ from the six-page journal text.
tags:
- natural-sciences
- network-science
- complex-systems
date: '2026-11-05'
published: '2016-07-28'
doi: '10.1073/pnas.1612139114'
arxiv: '1607.08562'
first_author: 'Rocks'
keywords:
- 'allostery'
- 'mechanical networks'
- 'disordered spring networks'
- 'states of self-stress'
- 'bond pruning'
- 'mechanical metamaterials'
implementations: []
summary: >-
  Rocks, Pashine, Bischofberger, Goodrich, Liu & Nagel (2017; arXiv 2016).
  In disordered central-force spring networks derived from jammed packings,
  a chosen linear strain ratio η between a target pair of nodes and a
  distant source pair is tuned in by removing bonds one at a time, each
  chosen by an analytic update computed from the network's states of
  self-stress and of compatible stress without re-solving it. About 1% of
  the bonds in 2D and 0.5% in 3D suffice for η = ±1, failing in under 2%
  and 1% of networks; one source can drive several targets, and several
  independent pairs can be tuned at once. Laser-cut and 3D-printed
  networks reproduce the responses. Read from the arXiv preprint.
---
<!-- inactive-ok-file: THEORY-tmpt2hyq — Proposed and new; the account filed from this reading -->

# LIT-tmpf2n99: Designing allostery-inspired response in mechanical networks

Rocks, J. W., Pashine, N., Bischofberger, I., Goodrich, C. P., Liu, A. J. & Nagel, S. R. (2017). Designing allostery-inspired response in mechanical networks. *Proceedings of the National Academy of Sciences* 114(10): 2520–2525. doi:10.1073/pnas.1612139114. arXiv:1607.08562 (v1 2016-07-28).

## Key takeaways

*From the reading of the arXiv v1 preprint, NOTE-tmptvl7g. Sections are
the preprint's.*

- **The result.** "With nearly complete success, we are able to produce a
  strain between any pair of target nodes in a network in response to an
  applied source strain on any other pair of nodes by removing only ∼1% of
  the bonds" (abstract).
- **Few bonds.** "In two dimensions only about 5 bonds out of about 400
  were removed on average (∼1%); similarly, in three dimensions only about
  4 bonds out of about 740 were removed on average (∼0.5%)" (Computational
  Results).
- **Self-stress does the bookkeeping.** Tensions with zero singular values
  of the equilibrium matrix "are commonly known as the states of
  self-stress (SSS)"; the rest, "We call these the states of compatible
  stress (SCS)" (Theoretical Approach).
- **Rigidity is the precondition.** "In the small ∆Z regime the failure
  rate is higher because very few bonds can be removed without
  compromising the rigidity of the system."
- **Unexplained.** "Further work needs to be done to understand why
  removing specific bonds achieves the desired response" (Discussion).

## Standing in the record

The pasted synthesis on constraint architectures cites it as M8 for
designed long-range responses in spring networks, and for the point that
designed adaptation is not a network maintaining or revising its own
organization; both fit, and the second is borne out, since an external
algorithm with a full model of the network chooses every bond. What the
synthesis leaves out is that the method runs on the states of self-stress
and compatible stress, the Maxwell–Calladine bookkeeping it raises
elsewhere (see Rocks and Mehta, LIT-tmpx12go, for the counting with
energetics), and that the response is linear and athermal. The
source-to-target strain ratio is an effective boundary relation that the
interior network produces, a large-scale instance of CLAIM-480's
elimination of an interior. Filed from it: THEORY-tmpt2hyq. No
instruction for machine-learning practice.
