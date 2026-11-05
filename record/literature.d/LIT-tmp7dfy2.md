---
status: Active
status_note: >-
  read in part 2026-11-05 ([NOTE-tmp1fpff](../notes.d/NOTE-tmp1fpff.md)) from the authors' submitted
  version in Cambridge's Apollo repository, after pubs.rsc.org showed a
  Cloudflare challenge; §2.1 on cooperativity, §§2.2-2.3 on nucleation
  barriers, the hysteresis passages and the Conclusions read, the methods
  and models sections skimmed or skipped; worth reading as a review, by
  two of the field's simulators, of what coarse-grained models say about
  how loop closure makes a staple's later domains cooperative and order
  dependent, and why DNA bricks need a nucleation barrier while origami
  does not, though one can be designed in. Its main limits: mostly the
  authors' own simulations of small 2D designs, which they caution against
  generalizing; a submitted version whose wording may differ from the
  journal's; the experimental evidence on origami hysteresis it reports
  is contested.
title: 'Models and simulations of structural DNA nanotechnology reveal fundamental principles of self-assembly'
version: 1
history:
- version: 1
  date: '2026-11-05'
  note: >-
    Registered and read in part on 2026-11-05 from the owner's paste of
    A's synthesis on DNA origami (the second paste), which cites, unnamed,
    a 2025 review of structural DNA nanotechnology on the entropy of loop
    formation, with a pubs.rsc.org source tag. Identified by the reader
    through a bounded Europe PMC search whose single hit matches A's
    description in its §2.1, and checked against Crossref (no mailto):
    Alexander Cumberworth and Aleks Reinhardt, Chemical Society Reviews
    54(5), 2344-2368; PMID 39878142; CC BY 3.0. Crossref gives online
    publication by year only; `published:` is 2025-01-29, the licence start
    and record creation date, the earliest exact date it gives; the issue
    is dated 2025-03-03. pubs.rsc.org returned a Cloudflare challenge and
    was not retried; the work is not in PubMed Central and has no arXiv
    version. Read from the CC BY submitted version in Cambridge's Apollo
    repository
    (https://www.repository.cam.ac.uk/bitstreams/cc842202-d199-4aa5-9600-f947fc00073f/download),
    found through OpenAlex; it carries the journal template with
    placeholder DOI and dates. What was read and skipped is in the NOTE.
    Status Active.
tags:
- natural-sciences
- thermodynamics
- complex-systems
date: '2026-11-05'
published: '2025-01-29'
doi: '10.1039/d4cs01095g'
first_author: 'Cumberworth'
keywords:
- 'DNA origami'
- 'DNA bricks'
- 'self-assembly'
- 'cooperativity'
- 'loop entropy'
- 'nucleation barrier'
- 'coarse-grained simulation'
- 'review'
implementations: []
summary: >-
  Cumberworth & Reinhardt (2025). A review of what models and simulations
  show about DNA self-assembly. In origami, a staple's first domain pays
  the translational entropy and its later domains bind within one
  structure, but each loop closed with the scaffold constrains it at a cost
  that depends on the order of binding; in the small designs simulated a
  staple typically binds fully once started, assembly is mostly downhill
  and needs no nucleation barrier, and blocking is rare at typical
  concentrations. DNA bricks, by contrast, need a nucleation barrier for
  high yield; one can be designed into origami by stacking, a long
  loop-closing staple or toehold exchange.
---
<!-- inactive-ok-file: NOTE-tmp1fpff THEORY-tmp07nzo — Skimmed, Proposed or new; cited from the reading of Cumberworth and Reinhardt (2025) as open -->

# LIT-tmp7dfy2: Models and simulations of structural DNA nanotechnology reveal fundamental principles of self-assembly

Cumberworth, A. & Reinhardt, A. (2025). Models and simulations of structural DNA nanotechnology reveal fundamental principles of self-assembly. *Chemical Society Reviews* 54(5): 2344–2368. doi:10.1039/d4cs01095g.

## Key takeaways

*From the partial reading, [NOTE-tmp1fpff](../notes.d/NOTE-tmp1fpff.md), of the submitted version.*

- **Later domains depend on loops.** "the bonding of subsequent domains of
  the same staple depend significantly on what kinds of loops form", and
  "The size of the entropic cost of this loop formation depends on the
  order in which the staple domains bond to the scaffold" (§2.1).
- **Staples bind fully once started**, in the small designs simulated:
  "once a staple bonds with its first domain, it will typically bond fully
  before additional staples bond" (§2.1), with evidence that this fails in
  larger 3D designs (Conclusions).
- **No barrier needed for origami.** "In contrast to DNA bricks,
  equivalent nucleation barriers are not required for error-free assembly
  of DNA-origami structures" (§2.3); for bricks, "A nucleation barrier is
  essential for the target structure to form in high yields" (§2.2).
- **Blocking is rare** at typical staple concentrations, by the authors'
  coarse-grained result (§2.3).

## Standing in the record

Registered from A's second paste on DNA origami, whose description of it
(loop-formation entropy and the dependence of later binding on existing
loops) the reading confirms. It supplies the mechanism behind the
loop-entropy skew of Majikes et al. (2026), [LIT-tmpbkl3k](LIT-tmpbkl3k.md), and disagrees
with that paper on how much blocking matters, at different
concentrations. Its contrast between bricks and origami bears on
[QUESTION-380](../questions.d/QUESTION-380.md). Read in part only. Filed from it: [THEORY-tmp07nzo](../theory.d/THEORY-tmp07nzo.md). No
instruction for machine-learning practice; nothing for the anthology.
