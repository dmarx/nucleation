---
status: Active
status_note: 'read in full 2026-10-01 from the MIT AI Memo 516 text ([NOTE-tmpex347](../notes.d/NOTE-tmpex347.md)), not the Cognitive Science version, which was not reachable; worth reading as the society-of-mind programme''s theory of memory and the first place Minsky''s own text uses the phrase "Society of Mind". The idea to take away is that a memory re-creates a partial mental state rather than retrieving a stored description, and its level-band principle: re-enact only an intermediate band of the original state, so the present problem is seen as an instance of the remembered one. The second half is, by its author''s account, not constructive ("from this point, the reader can assume that difficulties in understanding are my fault"), and nothing is simulated or measured.'
title: 'K-Lines: A Theory of Memory'
version: 1
history:
- version: 1
  date: '2026-10-01'
  note: >-
    Read in full: MIT AI Memo 516, June 1979, 23 pp., the scan on MIT
    DSpace (https://hdl.handle.net/1721.1/5739), OCR'd page by page with
    Tesseract because the scan has no text layer; the ASCII diagrams (P-
    and K-pyramids, level band) came through only as fragments. The
    journal version, Cognitive Science 4(2):117–133 (1980), was not
    reachable: Wiley's PDF and the Elsevier DOI landing page both returned
    HTTP 403 behind a bot check, and Semantic Scholar lists only that
    Wiley URL as open access. Citation verified on Crossref, which carries
    two DOIs for the article: 10.1207/s15516709cog0402_1 (Wiley, issued
    April 1980, pp. 117–133) and 10.1016/s0364-0213(80)80014-0 (the
    Elsevier-era DOI, issued June 1980); the Wiley DOI is used. The memo is
    the first appearance (cover date June 1979; "Cambridge, Massachusetts,
    January - June, 1979" at the end of the text), so `published:` is its
    month; Minsky's own AIM-603 cites the journal as "Vol. 4, No. 2 (April
    1980), 117-133". Not held in the Anthology of the SOTA.
tags:
- cognition
- mereology
- complex-systems
date: '2026-10-01'
published: '1979-06-01'
doi: '10.1207/s15516709cog0402_1'
first_author: 'Minsky'
keywords:
- 'K-lines'
- 'K-nodes'
- 'partial mental states'
- 'society of mind'
- 'dispositions'
- 'level-band principle'
- 'cross-exclusion'
- 'crossbar problem'
- 'memory'
implementations: []
extends:
- LIT-tmp4jv7c
- LIT-tmpf92fs
summary: >-
  Minsky (1979/1980), MIT AI Memo 516; Cognitive Science 4(2):117–133.
  "The function of a memory is to re-create a state of mind." On a
  memorable event a K-node is made, and its K-line attaches to the agents
  then active. Reactivated, it re-imposes that partial mental state, but by
  the level-band principle only on an intermediate band of levels, so the
  present is seen as an instance of the past without hallucinating the old
  answer. K-lines attach mainly to earlier K-nodes, forming a K-pyramid
  against the perceptual P-pyramid, and cross-exclusion lets conflicting
  details cancel into abstraction. Read from the memo; a programme
  statement, with no simulation.
---
<!-- inactive-ok-file: LIT-385 — Deferred; Damasio's retroactivation proposal, named as a parallel the reader drew, not leaned on -->

# LIT-tmp84goj: K-Lines: A Theory of Memory

Marvin Minsky (1980), *Cognitive Science* 4(2):117–133 —
DOI-10.1207/s15516709cog0402_1. First issued as *MIT Artificial Intelligence
Laboratory, A.I. Memo No. 516*, June 1979, 23 pp. —
https://hdl.handle.net/1721.1/5739. This filing was read from the memo.

## Key takeaways

- **Memory re-creates a state.** "The function of a memory is to re-create a
  state of mind." A K-line is attached to the agents active during a
  memorable event, and reactivating it re-imposes that **partial mental
  state**, a subset of the agents' states.
- **Dispositions before propositions.** Feelings, attitudes and "ways of
  seeing things" may be the simpler elements, and facts the harder ones. So
  memory is first a predisposition, not a stored description.
- **Level-band principle.** A K-line should reach only a band of levels
  below its own. Reaching too low imposes false perceptions; reaching too
  high makes one "hallucinate the present problem as already solved". The
  memo calls this "probably the most important idea of this theory".
- **K-recursion.** New K-lines attach mainly to K-nodes already active, so
  "new memories are composed mainly of ingredients from earlier memories".
- **Abstraction for free.** With cross-exclusion groups, conflicting details
  cancel out, so an "accumulating" K-node extracts what its instances share.
- **Learning needs three nets.** A goal net G must control how K learns to
  drive P. Global, recency-based reinforcement cannot solve human credit
  assignment.

## Standing in the record

Filed on 2026-10-01 at the owner's request, as part of Minsky's Society of
Mind programme. It is the programme's theory of memory. It is also the first
of Minsky's texts filed here to use the phrase "Society of Mind", in its
section "MENTAL STATES and the SOCIETY of MIND". Its Note 1 calls the theory
one "I have been evolving jointly with S. Papert", and the acknowledgement
says "the basic idea came in conversations with him".

It builds on two works in this filing, and says so.

- **Plain Talk.** It extends Plain Talk ([LIT-tmp4jv7c](LIT-tmp4jv7c.md)), "which the present
  paper complements in several areas". That paper's c-lines "correspond
  roughly to the K-->P connections here". It recasts their "confusingly
  bidirectional" structure as a K–P duality.
- **Frames.** It extends the frame memo ([LIT-tmpf92fs](LIT-tmpf92fs.md)) by offering a
  distributed implementation of frames (Note 9). "A K-node acts like a
  'frame'": the agents it activates in its level band are the frame's
  obligatory terminals, and weak connections at the band's lower fringe give
  "the loosely bound 'default assignments'".

The jokes memo ([LIT-tmpcmegc](LIT-tmpcmegc.md)) takes over its partial mental states. The 1986
book, filed alongside by another pass, makes K-lines one of its central
mechanisms.

[NOTE-tmpex347](../notes.d/NOTE-tmpex347.md) is the close reading of 2026-10-01, from the memo, and it
placed the work: **Active**. It is a clear, compact statement of memory as
state reinstatement with a principled limit on how much to reinstate. It is
not evidence. The constructive part stops halfway: the P→K connection, which
relates perceptual events to goals, is left "somehow".

It belongs with three works already in this record, which the memo does not
cite.

- **Convergence zones.** Damasio's proposal ([LIT-385](LIT-385.md), Deferred) has recall
  as the time-locked re-activation of feature fragments in early cortices,
  directed by convergence zones. That is the same shape as a K-line
  re-activating agents.
- **Somatic markers.** The somatic-marker hypothesis ([LIT-384](LIT-384.md)) has learned
  situation–body-state links "re-enacted" to bias choice. That is a
  disposition-first memory of the kind this memo argues for.
- **Sparse codes.** For its crossbar problem the memo's Note 10 proposes
  sparse random subset codes on a shared bundle of lines, after Mooers and
  Willshaw et al. That is the family of codes behind sparse distributed
  memory, which this record reads in [LIT-269](LIT-269.md) and [NOTE-242](../notes.d/NOTE-242.md).

All three pairings are mine. The memo carries no instruction for
machine-learning practice, and no anthology topic holds it.
