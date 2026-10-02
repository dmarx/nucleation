---
status: Active
status_note: 'read in full 2026-10-01 ([NOTE-tmp0yhbo](../notes.d/NOTE-tmp0yhbo.md)); worth reading as the source of the frame idea and of the critique of "logistic" representation that later motivated non-monotonic reasoning. It is a proposal, not a result: no program is described as built, nothing is measured, and the author says so ("Apology!", p. 2). The parts to take away are the frame with weakly bound default assignments (§1.11), frame-systems sharing terminals across viewpoints (§1), terminals read as questions (§2.8), the similarity network with cluster "capitols" as an account of family resemblance (§§3.4–3.5), and the appendix on monotonicity and consistency (§6). It contains no society-of-agents idea; that arrives in Plain Talk ([LIT-tmp4jv7c](LIT-tmp4jv7c.md)), which calls itself in part a sequel to this memo.'
title: 'A Framework for Representing Knowledge'
version: 1
history:
- version: 1
  date: '2026-10-01'
  note: >-
    Read in full: MIT AI Memo 306, June 1974, the 82-page scan on MIT
    DSpace (https://hdl.handle.net/1721.1/6089, file AIM-306.pdf). The
    scan has no text layer; I rendered each page and ran Tesseract OCR, then
    read the OCR text of the cover, §§1–5, the Appendix (§6) and the
    bibliography. Figures and diagrams did not survive OCR and were not
    read. Citation verified against DSpace: title, author, date
    1974-06-01, series AIM-306, 82 p. The memo's cover says it "will be
    available in the early part of 1975 as a part of the book The
    Psychology of Computer Vision" (Winston, ed., McGraw-Hill); a later
    Minsky memo (AIM-603) calls that version "condensed". The 1975 text and
    the reprints that carry DOIs (Frame Conceptions and Text
    Understanding, de Gruyter 1979, DOI 10.1515/9783110858778-003;
    Readings in Cognitive Science, 1988, DOI
    10.1016/b978-1-4832-1446-7.50018-2; Mind Design II, MIT Press 1997,
    DOI 10.7551/mitpress/4626.003.0005) were not seen, so `url:` is the
    memo's handle and not a reprint's DOI. Not held in the Anthology of the
    SOTA: a grep of its record for "Minsky" and the title found nothing.
tags:
- cognition
- linguistics
- logic
date: '2026-10-01'
published: '1974-06-01'
url: 'https://hdl.handle.net/1721.1/6089'
first_author: 'Minsky'
keywords:
- 'frames'
- 'frame-systems'
- 'default assignment'
- 'terminals'
- 'similarity network'
- 'scenarios'
- 'knowledge representation'
- 'criticism of logistic'
implementations: []
extended_by:
- LIT-tmp4jv7c
- LIT-tmp84goj
- LIT-tmpcmegc
summary: >-
  Minsky (1974), MIT AI Memo 306. A self-declared partial theory of
  thinking: on meeting a situation one retrieves a frame, a stereotyped
  structure whose terminals carry conditions and weakly bound default
  assignments, and adapts it by replacing details. Frames that share
  terminals form frame-systems whose transformations stand for moves,
  actions or changes of viewpoint, and failed matches are routed through a
  learned similarity network. The memo applies this to vision, imagery,
  language, memory and problem solving, and ends by arguing that
  consistency-seeking logical systems cannot represent commonsense
  knowledge, because they are monotonic. Nothing is implemented or tested.
---
<!-- inactive-ok-file: LIT-334 — Deferred; named as a neighbouring account of concepts, not leaned on -->

# LIT-tmpf92fs: A Framework for Representing Knowledge

Marvin Minsky (1974), *MIT Artificial Intelligence Laboratory, A.I. Memo
No. 306*, June 1974, 82 pp. — https://hdl.handle.net/1721.1/6089. A condensed
version appeared in P. H. Winston (ed.), *The Psychology of Computer Vision*,
McGraw-Hill, 1975.

## Key takeaways

- A **frame** is a data-structure for a stereotyped situation. Its top levels
  are fixed, and its lower **terminals** ("slots") carry markers that say
  what may fill them. Frames are stored with **weakly bound default
  assignments** at every terminal, never empty, and new evidence displaces
  them easily (§1.11).
- Frames that share terminals form a **frame-system**. Moving round a cube
  or a room, a change of emphasis in a sentence, and a before-and-after
  event pair are all transformations between frames of one system. Shared
  terminals are what keep what is already known when the viewpoint changes
  (§§1.4–1.8, 2.2).
- Terminals can be read as **the questions a situation raises** (§2.8). On
  this reading a scenario frame such as a child's birthday party
  pre-compiles its typical problems.
- A frame that fails to match is replaced through a learned **similarity
  network** of difference-labelled pointers, after Winston. Its clusters
  and "capitols" account for Wittgenstein's family resemblance without a
  definition (§§3.4–3.5).
- The **appendix** argues that "logistic" systems fail for commonsense,
  because they are monotonic, keep facts apart from advice on using them,
  and pursue consistency, which "is not necessary or even desirable" (§6).

## Standing in the record

Filed on 2026-10-01 at the owner's request, as the first of four of
Minsky's MIT memos that lead up to the Society of Mind programme. It is a
precursor, not part of that programme: the memo never uses "society" or
"agent" in that sense. It is the representational ground the later papers
stand on. Plain Talk ([LIT-tmp4jv7c](LIT-tmp4jv7c.md)) calls itself "in part a sequel" to this
memo, and its fixed-location data lines are "an extension of the 'common
terminal' idea" here. K-lines ([LIT-tmp84goj](LIT-tmp84goj.md)) says a K-node "acts like a
frame": the agents it activates in its level band are the frame's obligatory
terminals, and its weak lower fringe gives the effect of default
assignments. The jokes memo ([LIT-tmpcmegc](LIT-tmpcmegc.md)) rests its account of humour on
the frame-shift and default machinery set out here. The book-length Society
of Mind and its 2006 sequel, filed alongside by another pass, take frames
over as one kind of agency among many.

[NOTE-tmp0yhbo](../notes.d/NOTE-tmp0yhbo.md) is the close reading of 2026-10-01, and it placed the work:
**Active**. It is the original statement of the frame idea and an early,
sharp statement of why monotonic logic is a poor model of commonsense. As
evidence it is nothing: it is a programme statement, careful to say which
parts it has not worked out.

Within this record it sits beside the work on concepts and their contexts.
Aerts and Gabora's "pet" experiment ([LIT-340](LIT-340.md)) measures exactly the effect
this memo builds into its defaults: an exemplar's typicality shifts with
context, as the default chair under a seated person becomes a park bench in
a park. Gärdenfors's conceptual spaces ([LIT-334](LIT-334.md), Deferred) is the geometric
alternative to symbolic structures like these. The pairings are mine, not
the memo's. The memo's "MATCHING" request, to find the frame sharing the most
terminals with a partial description (§3.2), is the best-match retrieval
problem that the record's reading of sparse distributed memory ([LIT-269](LIT-269.md))
traces to Minsky and Papert.

It carries no instruction for machine-learning practice, and no anthology
topic holds symbolic knowledge representation, so it is filed here only.
