---
status: Deferred
status_note: 'filed 2026-10-11 from its bibliographic record, not read. Registered at the owner''s request for the nucleating-argument line, on what it is standardly cited for. No NOTE is filed, and it stays Deferred until it is read, not on merit.'
title: 'Neural networks and physical systems with emergent collective computational abilities'
version: 1
history:
- version: 1
  date: '2026-10-11'
  note: >-
    Filed, not read. J. J. Hopfield, Proceedings of the National Academy
    of Sciences 79(8), pp. 2554–2558, April 1982, which is the
    `published:` date (Crossref gives the month only). A free full text
    is in PubMed Central, PMC346238. Not held in the Anthology of the
    SOTA: a grep of its record/ (clone at commit d8b5ba5) for Hopfield
    and the DOI found no LIT for this paper. An anthology topic could
    hold it, as the anthology's Kanerva entries cover the same family,
    so it carries the anthology-candidate flag (ADR-005).
tags:
- complex-systems
- neuroscience
- anthology-candidate
date: '2026-10-11'
published: '1982-04-01'
doi: '10.1073/pnas.79.8.2554'
first_author: 'Hopfield'
keywords:
- 'Hopfield network'
- 'associative memory'
- 'content-addressable memory'
- 'attractor'
- 'energy function'
implementations: []
summary: >-
  Hopfield (1982), PNAS 79, 2554. A network of simple threshold units
  with symmetric connections stores memories as stable states of an
  energy function, so a partial or noisy cue settles into the nearest
  stored memory: content-addressable memory as an emergent collective
  property. Not read; a free full text is in PMC.
supports:
- CLAIM-tmp7vmnc
---
<!-- inactive-ok-file: CLAIM-tmp6b44r CLAIM-tmp7vmnc — Proposed; open, and cited as open: the theses and objections of the nucleating-argument line are under test, not settled -->
<!-- inactive-ok-file: LIT-tmpcc2ij LIT-tmpgwyow LIT-tmpz8twi — Deferred, unread; named as a related work in this batch, not for a reading here -->

# LIT-tmp64dfb: Neural networks and physical systems with emergent collective computational abilities

J. J. Hopfield (1982), *Proceedings of the National Academy of Sciences* 79(8), 2554–2558

## Key takeaways

*Filed, not read.* Known here by what it is standardly cited for.

- With symmetric connections, the network's dynamics descend an energy
  function, and stored memories are its local minima.
- A cue that is part of a memory, or a corrupted version of it, settles
  into the stored memory: memory addressed by content.
- Capacity is limited. Beyond a load of roughly 0.15 memories per unit,
  retrieval errors become severe and spurious states appear.
- Memories are stored by a Hebbian outer-product rule.

## Standing in the record

Filed on 2026-10-11 at the owner's request, with Hebb ([LIT-tmpgwyow](LIT-tmpgwyow.md)) and
Kanerva ([LIT-tmpz8twi](LIT-tmpz8twi.md), [LIT-tmpcc2ij](LIT-tmpcc2ij.md)). Its basins of attraction are the
dynamical form of SDM's critical distance: a cue inside a basin is
retrieved, a cue outside settles elsewhere, possibly into a spurious
state. That bears on [CLAIM-tmp7vmnc](../claims.d/CLAIM-tmp7vmnc.md). Its capacity limit bears on flooding
([CLAIM-tmp6b44r](../claims.d/CLAIM-tmp6b44r.md)): past a load, stored items interfere and spurious ones
appear. Flagged anthology-candidate. A full text is in PMC, so it can be
read here next.
