---
status: Active
status_note: >-
  read 2026-11-05 (NOTE-tmppy063) from the authors' submitted preprint in
  CaltechAUTHORS, in full with all footnotes and figure captions, figure
  contents seen only through captions and axis labels; worth reading as
  the founding construction of error correction by redesigned tile sets in
  algorithmic self-assembly, where a K×K block of uniquely bonded tiles
  makes a mismatch stall until it falls off, and for its frank account of
  where the method falls short. Its main limits: simulation and
  kinetic-trap theory only, with no experiment; fitted trap rates the
  authors call unjustified; no rigorous proof; the gain beyond K = 2 is
  well below the theory's, because errors from growth on facets go
  uncorrected; and the copy read is the preprint, not the Springer version
  of record.
title: 'Proofreading Tile Sets: Error Correction for Algorithmic Self-Assembly'
version: 1
history:
- version: 1
  date: '2026-11-05'
  note: >-
    Registered and read on 2026-11-05 at the owner's invitation to add
    readings to the DNA origami filing (works chosen by the assistant).
    The citation was checked against Crossref (no mailto): Erik Winfree
    and Renat Bekbolatov, in DNA Computing (9th International Workshop on
    DNA Based Computers, DNA 9), Lecture Notes in Computer Science 2943,
    pp. 126–144, Springer Berlin Heidelberg; editors J. Chen and J. Reif
    per the paper's own reference list, Crossref listing none. Crossref
    gives the year 2004 alone, with no month or day, and the reader found
    no exact date for the volume, so `published:` is the year's first day
    and only the year is known. No correction was needed. Read from the
    authors' submitted preprint, proofreading_DNA9_preprint.pdf, 19 pages,
    in Caltech's institutional repository CaltechAUTHORS
    (https://authors.library.caltech.edu/records/jcvj4-7gn26), which
    labels it "Submitted"; it carries the published abstract, but page
    numbers and small wording may differ from the LNCS text. The authors'
    lab site, dna.caltech.edu, failed TLS verification and was not
    retried, so the supplementary simulation code was not fetched. Status
    Active.
tags:
- natural-sciences
- complex-systems
date: '2026-11-05'
published: '2004-01-01'
doi: '10.1007/978-3-540-24628-2_13'
first_author: 'Winfree'
keywords:
- 'algorithmic self-assembly'
- 'tile assembly model'
- 'kinetic Tile Assembly Model'
- 'proofreading'
- 'error correction'
- 'kinetic trapping'
- 'self-healing'
- 'Sierpinski triangle'
implementations: []
summary: >-
  Winfree & Bekbolatov (2004). In the kinetic Tile Assembly Model, a
  mismatched tile on the growth front is often covered by further growth
  before it can detach, which forces a speed/error trade-off r ≈ βε²:
  ten times fewer errors cost a hundredfold slowdown. Replacing each tile
  by a K×K block whose internal edges carry unique labels keeps the
  logical assembly the same, scaled by K, but leaves no way to extend a
  single mismatch without a second error, so growth stalls and the bad
  tile falls off. In simulation 2×2 blocks give r ≈ βε, and at fixed
  conditions errors fall from 1% to 0.01%; the predicted gain exponential
  in K falls short at K = 3, which the authors attribute to growth on
  facets, which proofreading does not correct. Proofreading tiles also
  heal punctures, sometimes leaving "scar tissue". Simulation and theory
  only.
---
<!-- inactive-ok-file: THEORY-tmpxgxmn THEORY-1398 CLAIM-tmpiyvk1 CLAIM-184 CLAIM-566 — Proposed or new; cited from the reading of Winfree and Bekbolatov (2004) as open -->

# LIT-tmp1pdwj: Proofreading Tile Sets: Error Correction for Algorithmic Self-Assembly

Winfree, E. & Bekbolatov, R. (2004). Proofreading Tile Sets: Error Correction for Algorithmic Self-Assembly. In J. Chen & J. Reif (eds.), *DNA Computing: 9th International Workshop on DNA Based Computers, DNA 9*, Lecture Notes in Computer Science 2943, 126–144. Springer. doi:10.1007/978-3-540-24628-2_13.

## Key takeaways

*From the reading, NOTE-tmppy063, of the submitted preprint, which has no
section page numbers; places are given by section, figure and footnote.*

- **Errors are kinetic traps.** Below melting, "equilibrium is seldom
  achieved far below the melting transition": a mismatched tile is
  "frozen in place by further growth" (§2), and "Subsequent error-free
  growth correctly propagates the erroneous information" (Fig. 4a). The
  direct tile sets pay a quadratic price: "decreasing error rates by a
  factor of 10 entails slowing down the self-assembly process by a factor
  of 100" (§2, Fig. 5).
- **Proofreading by stalling.** In a K×K block a mismatch cannot be
  extended without a second error, so "The assembly process stalls,
  giving time for the initial mismatched tile to fall off and be replaced
  by a correct tile" (§3, Fig. 6d). The 2×2 sets give r ≈ βε, and "for
  target error rates of 10−4 , the 2 × 2 proofreading tiles result in a
  104 -fold speed-up" (§2).
- **Short of exponential.** The theory predicts r ≈ βε^{2/K}, but "the
  simulation results for K = 3 (figure 5) and K = 4 (data not shown) fall
  short of the prediction" (§3). Proofreading does nothing about
  "spontaneous growth on a facet", "making facet growth errors rare but
  unavoidable" (§3, Fig. 8a).
- **Cooperativity must come from the path.** A pre-assembled block would
  melt at Gmc ≈ 2KGse and bring back the ε² scaling (footnote 11): the
  correction lives in the K² independent attachments, not in the block as
  a unit.
- **Healing.** "Proofreading tile sets are often able to heal a puncture
  in the crystal", sometimes with "scar tissue" (§4, Fig. 9), from
  supplied monomers.

## Standing in the record

Not an origami paper: the tile-assembly ancestor of the batch, read for
how a self-assembling system can correct its own growth errors with no
inspector and no change of chemistry, only a redesigned rule set,
reversibility and a supply of parts held at fixed conditions. Its
proofreading works by changing where the exits from an error lead, which
sets it beside CLAIM-tmpiyvk1; it is the clean physical case of an early
error locked in and propagated (CLAIM-184); and its puncture-healing is
regeneration of form without closure, every tile species supplied
(CLAIM-566, TERM-070). Its local kinetic traps complement the global
topological traps of DeLuca et al. (LIT-2081, THEORY-1398). The account
filed from it is THEORY-tmpxgxmn.
