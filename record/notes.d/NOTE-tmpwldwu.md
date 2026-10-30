---
status: Skimmed
paper: LIT-tmp4sulg
title: 'Flynn, Kanerva & Bhadkamkar — SDM principles and operation'
version: 1
history:
- version: 1
  date: '2026-10-30'
  note: >-
    Read from NASA's public-domain NTRS copy
    (ntrs.nasa.gov/api/citations/19920001076/downloads/19920001076.pdf,
    60 scanned pages with an OCR layer), text extracted with pdftotext.
    Read in full: the abstract, the contents, and chapter 1 (pp. 1–28),
    which is the report's account of how the memory works, including
    §1.5 on autoassociative dynamics and the critical distance and §1.6
    on sequences and folds. Looked over, not read closely: chapter 2 on
    the hardware modules (pp. 29–42) and chapter 3 on the programmer's
    interface (pp. 43–49); the bibliography (p. 50) was read. The figures
    were seen only through their captions and OCR fragments. Page
    numbers are the report's. Kanerva's book, to which the report refers
    its mathematics, is not read (LIT-928). Hence Skimmed.
date: '2026-10-30'
summary: >-
  Kanerva and co-authors state SDM's critical distance in words and do
  not derive it: a cue within it converges on the stored pattern under
  iterated reads, a cue beyond it wanders and may settle on another
  pattern, the distance shrinks as the memory fills, and in a sparsely
  filled memory it is below the sum of the write and read radii. For
  single patterns convergence and divergence are "easy to distinguish in
  practice"; for stored sequences they are not. The rest of the report
  is a hardware design.
---
<!-- inactive-ok-file: CLAIM-180 — Proposed; the claim this reading bears on, cited as open -->
<!-- inactive-ok-file: LIT-928 — Unavailable; Kanerva's book, unread, where the report sends its mathematics -->

# NOTE-tmpwldwu: Flynn, Kanerva & Bhadkamkar — SDM principles and operation

## Contribution

A non-mathematical introduction to sparse distributed memory written
around a hardware prototype built at Stanford with RIACS. Chapter 1
explains the memory from a one-dimensional toy example up to the real
model, then its use as an autoassociative memory, as a store of sequences,
and with folds of several orders for prediction. Chapters 2 and 3 describe
the prototype's four modules and its programming interface. Nothing is
proved: "Readers desiring a mathematical description of these concepts
should consult the book by Kanerva [4]" (p. 3).

## Key insight

Retrieval by content works because every word is spread over many
locations and read back as a vote of many locations. A cue near a stored
pattern draws a majority of that pattern from the locations it reaches,
so its read-out is nearer still and the reads converge. A cue too far
away draws mostly other patterns, and its reads wander. The critical
distance is where the one behaviour turns into the other.

## Assumptions

- **Long binary words.** The properties appear only when "the memory
  addresses [are] at least 100 bits and preferably several hundred, and
  any read or write operation [manipulates] many memory locations" (p. 2).
  The prototype uses N = M = 256.
- **Hard locations sparse and random.** 8,192 hard addresses "scattered
  randomly with uniform probability through the address space" (p. 11),
  on the assumption that the patterns of interest are "sparsely scattered
  throughout the input space" (p. 4).
- **Distance is Hamming distance**, chosen for convenience; "other
  measures could equally well be used" (p. 4).
- **Counters saturate.** ±127 in §1.4.4 and Fig. 1.18; Table 1.2 and §2.3
  give 16-bit counters instead (see Limitations).

## Key results

- **Write and read (§1.4.4, pp. 11–14).** To write, "draw an
  N-dimensional sphere of Hamming radius d around the address" and add
  the word into the 256 counters of every hard location inside it. To
  read, draw a sphere of radius d′ around the cue, "which need not equal
  the radius d used for storing", sum the counters of the locations
  inside it bit by bit, and threshold each sum.
- **The best-match example (§§1.4.1–1.4.3, pp. 5–11).** Storing each
  input only in its nearest location fails to retrieve the closest stored
  item; spreading it over all locations within ±25 and reading from all
  within ±25 of the cue returns it.
- **Signal and noise (p. 15).** The locations a cue Z activates hold a
  mixture of the target P(1) ("signal") and other patterns ("noise",
  after Keeler). "The signal-to-noise ratio is higher (a) the closer Z is
  to P(1), and (b) the less densely populated the memory is."
- **The critical distance (pp. 15–16).** "It can be shown mathematically
  [4] that if Z is closer than a certain critical distance to P(1), then
  summing and thresholding the contents of the locations activated by Z
  results in a vector Z(1) that is closer to P(1) than Z was. The
  critical distance is a function of how densely populated the memory
  is. The greater the population of the memory, the smaller the critical
  distance." Iterating gives a sequence "that converges rapidly to either
  P(1) or a minimally noisy version of P(1)".
- **Beyond it (pp. 15–16).** "If the cue vector Z is beyond the critical
  distance from P(1), i.e., if it is too contaminated or incomplete, the
  sequence of vectors Z(1), Z(2), ... will not converge to P(1). Instead,
  it will be a diverging sequence that will wander through address
  space. It may eventually wander, by chance, into the attracting zone of
  some other stored pattern, say, P(k), and thereby converge onto P(k)."
- **Telling the two apart (p. 16).** "Experimentally, convergence to the
  correct value P(1) occurs rapidly (~10 iterations), whereas the
  diverging sequence, if it eventually converges to some other pattern,
  takes a large number of iterations. The two situations are easy to
  distinguish in practice." No experiment is reported.
- **An upper bound (p. 16).** "In a sparsely populated memory in which
  there is little or no overlap between the locations in which patterns
  have been stored, the critical distance is necessarily less than the
  sum of the Hamming radii used during storage and retrieval", since a
  cue farther away activates no location holding a copy of P(1).
- **Hopfield (p. 16).** The behaviour "is similar to the dynamic behavior
  of the Hopfield net used in its autoassociative mode", where "stored
  patterns act like attractors for input cues within a certain critical
  distance"; Hopfield's is driven by energy minimisation.
- **Sequences (pp. 16–18).** Writing P(i + 1) at address P(i) stores a
  sequence; a cue near one element recovers the rest by iterated reads.
  But "unlike the autoassociative case where convergence can be easily
  distinguished from divergence, in the case of sequences the difference
  is unfortunately hard to tell by looking at the retrieved patterns."
- **Folds (pp. 19–21).** A kth-order fold stores P(i + k) at address
  P(i); summing the reads of several folds, each cued with a different
  recent pattern, disambiguates sequences that share elements.

## Claims

Only a Read note may fill this in; this reading is Skimmed, since the
hardware chapters were not read closely. The claims of chapter 1 are
graded in prose above: the critical-distance statements are asserted with
a citation to the book, and the "~10 iterations" figure is asserted
without data.

## Concepts

- **Hard location** — one of the implemented physical locations, with a
  fixed N-bit hard address and M counters (p. 4).
- **Critical distance** — the cue-to-pattern distance within which one
  read moves the cue closer to the pattern, so that iterated reads
  converge on it; it decreases with the number of stored patterns (p. 15).
- **Attracting zone** — the region of cues that iterated reads carry to a
  given stored pattern (p. 16).
- **Fold** — a full set of locations storing P(i + k) at address P(i), for
  one order k (p. 19).

## Connections

It is a companion to Kanerva's book (ref. 4, [LIT-928](../literature.d/LIT-928.md)) and cites Keeler's
and Chou's comparisons with the Hopfield network. Kanerva's 1992 report
([LIT-921](../literature.d/LIT-921.md), read in [NOTE-779](NOTE-779.md)) gives the signal-to-noise analysis in matrix
form but, as [NOTE-779](NOTE-779.md) records, not the critical distance; this report
names the critical distance but gives no analysis. The definition
[NOTE-242](NOTE-242.md) reads from Bricken and Pehlevan ([LIT-269](../literature.d/LIT-269.md), App. B.5), "the
largest query–target distance from which iterated reads still converge to
the target", matches this report's description. Hopfield's network itself
is [LIT-918](../literature.d/LIT-918.md) ([NOTE-819](NOTE-819.md)).

## Bearing on the record

- **[CLAIM-180](../claims.d/CLAIM-180.md): partly.** The claim needs the critical distance and cites
  Kanerva's book for it, unread. This report, by Kanerva and two
  co-authors, states the property in the claim's own terms: a cue within
  the critical distance converges on the stored pattern, and one beyond it
  does not and "will wander through address space", possibly into another
  pattern's attracting zone (pp. 15–16). That supports the claim's
  description first-hand. It does not meet the want, because the report
  only asserts the property and sends its derivation to the book, so
  where the critical distance comes from still waits on [LIT-928](../literature.d/LIT-928.md).
- **[CLAIM-180](../claims.d/CLAIM-180.md), "taken for new".** The claim says "taken for new" has no
  Hopfield analogue, since the network never treats a cue as new. In SDM
  the report gives one: for a single pattern, divergence takes many
  iterations and convergence about ten, so "the two situations are easy to
  distinguish in practice" (p. 16). Failure to retrieve is then visible to
  the memory. For stored sequences it is "hard to tell" (p. 18). A
  restated idea read as a step in a chain of reasoning is closer to the
  sequence case, where a failed retrieval passes unnoticed.
- **[CLAIM-180](../claims.d/CLAIM-180.md), capacity.** "The greater the population of the memory, the
  smaller the critical distance" (p. 15). A fuller record retrieves only
  closer restatements. That is the claim's capacity point in SDM's own
  terms, and it is consistent with the correction of 2026-10-14 that
  Hopfield overload loses memories rather than merging them: here load
  narrows the distance from which a pattern is reached.
- **No instruction for machine-learning practice.** Nothing for the
  anthology.

## Limitations

- **No derivation and no data.** The critical distance, its dependence on
  load and the convergence speed are asserted; the report cites the book
  for the first and gives no simulation for the third, though it says the
  theory "has been verified by computer simulation" (p. 1).
- **No numbers.** No value of the critical distance is given for any
  memory size, radius or load.
- **Internal inconsistencies.** Counters are 8-bit (±127) in §1.4.4 and
  Fig. 1.18 but 16-bit in Table 1.2 and §2.3; Fig. 1.18 indexes a
  location's counters from Tag × 256 while §1.8 gives 512 bytes per
  location. These concern the hardware, not the principles.
- **OCR.** The copy is a scan; some figure labels did not survive
  extraction, and quotations were checked against the extracted text.

## Open questions

- What the book derives for the critical distance as a function of N, the
  radii and the number of stored patterns, and whether the iterates beyond
  it are shown to wander or only not to converge.
- Whether the easy detection of divergence holds near capacity, where the
  report gives no figures.
