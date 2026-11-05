---
status: Active
status_note: >-
  read 2026-11-05 ([NOTE-tmpjeolx](../notes.d/NOTE-tmpjeolx.md)) from the PubMed Central HTML of the
  version of record (PMC4311804), main text and figure captions in full,
  Supporting Information not read; worth reading as the first designed,
  reconfigurable DNA origami mechanisms: one-degree-of-freedom sliders and
  hinges built from stiff bundles joined only by single-stranded scaffold,
  composed into a crank–slider and a Bennett linkage, with the cost of
  holding a configuration read off the thermal ensemble and a linkage
  switched by added strands and switched back by strand displacement in
  about a minute. Its main limits: all conformational statistics from
  negative-stain TEM on a surface, which the authors say may bias the
  fractions toward extreme states; misfolded particles excluded and no
  yields given; small samples for the mechanisms; one actuation cycle; the
  derivations, locking-strand designs and misfold images are in the
  unread SI.
title: 'Programmable motion of DNA origami mechanisms'
version: 1
history:
- version: 1
  date: '2026-11-05'
  note: >-
    Registered and read on 2026-11-05 at the owner's request to connect
    the record's realizability inquiry to DNA origami; the work was chosen
    by the assistant. The citation was checked by the reader against
    Crossref (no mailto): Alexander E. Marras, Lifeng Zhou, Hai-Jun Su and
    Carlos E. Castro, Proceedings of the National Academy of Sciences of
    the USA 112(3), 713–718; received 13 May 2014, accepted 10 December
    2014 (edited by William Shih), published online 5 January 2015, which
    is `published:`, issue 20 January 2015. PMID 25561550, PMCID
    PMC4311804. No correction was needed. Read from the PubMed Central
    HTML article page (https://pmc.ncbi.nlm.nih.gov/articles/PMC4311804/);
    PMC's XML carries no body for this article. The SI PDF was not read:
    PMC returned a JavaScript download interstitial, treated as a bot
    check and not retried. Movies S1–S3 and Dataset S1 were not viewed.
    Status Active.
tags:
- natural-sciences
- complex-systems
date: '2026-11-05'
published: '2015-01-05'
doi: '10.1073/pnas.1408869112'
first_author: 'Marras'
keywords:
- 'DNA origami'
- 'DNA nanotechnology'
- 'nanorobotics'
- 'mechanism design'
- 'self-assembly'
implementations: []
summary: >-
  Marras, Zhou, Su & Castro (2015). DNA origami joints in the manner of
  macroscopic machine design: stiff double-stranded bundles connected only
  by single-stranded scaffold make a slider and a hinge, each moving in
  one designed degree of freedom whose range and stiffness the connection
  lengths set. Thermal fluctuations measured by TEM are inverted, assuming
  Boltzmann weighting, into energy landscapes and the force or torque
  needed to hold each configuration. A crank–slider and a Bennett linkage
  built from these joints follow their rigid-body motion paths. The
  linkage's compacted bundle is a higher-energy state seldom seen unaided
  (9.9%); locking staples added at folding hold it (93%), and after
  folding closing strands drive it there (93.1%) and toehold-mediated
  strand displacement reopens it, each in about a minute.
---
<!-- inactive-ok-file: THEORY-tmp1799q THEORY-1398 CLAIM-567 CLAIM-569 CLAIM-571 CLAIM-591 CASE-206 — Proposed or new; cited from the reading of Marras et al. (2015) as open -->

# LIT-tmp11aw1: Programmable motion of DNA origami mechanisms

Marras, A. E., Zhou, L., Su, H.-J. & Castro, C. E. (2015). Programmable motion of DNA origami mechanisms. *Proceedings of the National Academy of Sciences of the USA* 112(3): 713–718. doi:10.1073/pnas.1408869112.

## Key takeaways

*From the reading, [NOTE-tmpjeolx](../notes.d/NOTE-tmpjeolx.md) (main text and figure captions; the SI unread).*

- **One designed degree of freedom, tuned by connection length.** Slider
  version 1 "revealed a range of thermal motion of 14.0 nm"; version 2,
  with fewer and longer single-stranded connections, "resulted in a range
  of motion of 29.2 nm", at the cost of occasional misfolds that were
  excluded.
- **Holding has a measurable cost.** "The energy landscape was
  differentiated to determine the force required to hold each joint at
  any specific length" (Fig. 2F); slider 1 acts as "a linear spring with a
  stiffness of 0.42 pN/nm".
- **Composite mechanisms follow their rigid-body paths.** The Bennett
  linkage "closely follows the expected motion path for its rigid-body
  counterpart" (Fig. 5C, n = 52).
- **Cheap to visit, dear to hold.** The compacted state "is a higher energy
  state", reached thermally by 9.9% of free linkages; held by locking
  staples (93%) or by closing strands (93.1%), and released by strand
  displacement, with half-times of 55 s closing and 49 s expanding.

## Standing in the record

Filed for the realizability inquiry as a concrete system in which the
resources for constructing a form (a two-day anneal), letting it fluctuate
(thermal, at the scale of kBT), holding a configuration (bound bridging
strands or locking staples) and moving between configurations (added
strands, then displacing strands) are separate and each stated. It bears
on [CLAIM-569](../claims.d/CLAIM-569.md) and [CLAIM-567](../claims.d/CLAIM-567.md), qualifies [CLAIM-571](../claims.d/CLAIM-571.md) in the reverse direction
(the target is cheap to reach and dear to hold), and gives [CLAIM-591](../claims.d/CLAIM-591.md) a
qualitative instance of a configuration that returns while the reagent
state does not; compare [CASE-206](../cases.d/CASE-206.md), where passage costs more than either
end state. Same group (Castro) as the held simulation reading, [LIT-2081](LIT-2081.md)
and [THEORY-1398](../theory.d/THEORY-1398.md), which it does not test. Filed from it: [THEORY-tmp1799q](../theory.d/THEORY-tmp1799q.md).
No instruction for machine-learning practice.
