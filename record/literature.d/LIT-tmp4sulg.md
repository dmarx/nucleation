---
status: Active
status_note: >-
  read 2026-10-30 (NOTE-tmpwldwu), Skimmed: chapter 1 in full (pp. 1–28)
  and chapters 2–3 looked over, from NASA's public-domain NTRS copy
  (ntrs.nasa.gov/api/citations/19920001076/downloads/19920001076.pdf, 60
  scanned pages with an OCR text layer). Worth reading as a short,
  first-hand statement by Kanerva and two co-authors of what SDM's
  critical distance is: a cue closer than it is pulled toward the stored
  pattern by iterated reads; one farther away "will not converge" and
  wanders, possibly into another pattern's attracting zone; the distance
  shrinks as the memory fills; and in an autoassociative memory the two
  outcomes are "easy to distinguish in practice". Read it knowing that
  the critical distance is asserted, not derived (the derivation is
  referred to Kanerva's book, LIT-928, still unread), that no simulation
  data are given for the convergence figures, and that most of the report
  describes the Stanford hardware prototype.
title: 'Sparse Distributed Memory: Principles and Operation'
version: 1
history:
- version: 1
  date: '2026-10-30'
  note: >-
    Filed and read on 2026-10-30 from the copy the day's search found,
    for CLAIM-180, which needs the critical distance while Kanerva's book
    (LIT-928) is unread. Citation from the report itself and from NTRS
    record 19920001076 (title "Sparse distributed memory: Principles and
    operation", publication date 1 December 1989, distribution public,
    government public use permitted): M. J. Flynn, P. Kanerva and N.
    Bhadkamkar, RIACS Technical Report 89.53, December 1989, published
    concurrently at Stanford as CSL-TR-89-400; NASA-CR-188901. The cover
    reads "Principles of Operation"; the title page and NTRS read
    "Principles and Operation", which is the title used here.
    `published:` is the first of the month the report carries. No entry
    for this report was found in literature.d by NTRS number, title words
    or author. It is a different work from Kanerva's 1992 report
    (LIT-921) and from his book (LIT-928).
tags:
- cognition
- information-retrieval
date: '2026-10-30'
published: '1989-12-01'
url: 'https://ntrs.nasa.gov/citations/19920001076'
first_author: 'Flynn'
keywords:
- 'sparse distributed memory'
- 'associative memory'
- 'best-match problem'
- 'critical distance'
- 'autoassociative'
- 'heteroassociative'
- 'folds'
- 'hardware prototype'
implementations: []
summary: >-
  Flynn, Kanerva & Bhadkamkar (1989), RIACS TR 89.53 / Stanford
  CSL-TR-89-400. A non-mathematical account of sparse distributed memory
  and the design of a Stanford prototype (256-bit words, 8,192 hard
  locations, up to 16 folds, 50 reads or writes a second). A word is
  written to every hard location within a Hamming radius of its address
  and read by summing and thresholding the counters of the locations near
  a cue. Used autoassociatively, a cue within a critical distance of a
  stored pattern converges on it in about ten iterated reads; beyond it
  the reads wander and may settle on another pattern. The critical
  distance falls as the memory fills and, in a sparsely filled memory, is
  below the sum of the write and read radii. The mathematics is referred
  to Kanerva's book.
---
<!-- inactive-ok-file: CLAIM-180 — Proposed; the claim this reading was filed for, cited as open -->
<!-- inactive-ok-file: NOTE-tmpwldwu — Skimmed; this entry's reading, which says what was read -->
<!-- inactive-ok-file: LIT-928 — Unavailable; Kanerva's book, unread, named as where the report sends its mathematics -->

# LIT-tmp4sulg: Sparse Distributed Memory: Principles and Operation

Flynn, M. J., Kanerva, P. & Bhadkamkar, N. (1989). *Sparse Distributed
Memory: Principles and Operation*. RIACS Technical Report 89.53, NASA Ames
Research Center; Stanford CSL-TR-89-400. NTRS 19920001076.

## Key takeaways

*From the reading, NOTE-tmpwldwu (Skimmed: chapter 1 in full).*

- **The memory.** Words are both addresses and data. A write adds the
  word, bit by bit as +1 or −1, into the counters of every hard location
  within Hamming radius d of its address; a read sums the counters of the
  locations within radius d′ of the cue and thresholds each sum (§1.4.4,
  pp. 11–14).
- **The critical distance.** "If Z is closer than a certain critical
  distance to P(1), then summing and thresholding ... results in a vector
  Z(1) that is closer to P(1) than Z was", so iterated reads converge on
  P(1). "The greater the population of the memory, the smaller the
  critical distance." A cue beyond it gives "a diverging sequence that
  will wander through address space" and may fall into another pattern's
  "attracting zone" (§1.5, pp. 15–16).
- **Divergence is visible for patterns, not for sequences.** Convergence
  takes about ten iterations and divergence many, so "the two situations
  are easy to distinguish in practice" (p. 16); for stored sequences "the
  difference is unfortunately hard to tell" (p. 18).
- **Not derived here.** The convergence claim is "shown mathematically"
  in Kanerva's book; the report gives neither the derivation nor data.

## Standing in the record

Filed on 2026-10-30 for CLAIM-180, whose statement of the critical
distance rests on NOTE-242's reading of LIT-269 while the book it comes
from, LIT-928, is unread. This report is Kanerva's own short statement of
the property, and confirms the claim's description of it, but it defers
the mathematics to the book. Most of the report describes the hardware.
