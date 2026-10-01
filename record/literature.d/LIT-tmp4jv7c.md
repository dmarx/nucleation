---
status: Active
status_note: 'read in full 2026-10-01 ([NOTE-tmp6hixb](../notes.d/NOTE-tmp6hixb.md)); worth reading as the earliest of Minsky''s own papers in this record to state the society-of-agents view, then called "The Society of Minds" (Note 1), and as its first worked mechanism: agents communicate by fixed-location channels ("c-lines") instead of messages. It is openly speculative ("a model of scientific irresponsibility", p. 1085), with no data and no program. Read it for the communication scheme, the "specificity gradient", the case-shift mechanism and the conjecture that cognitive cases precede and shape linguistic ones; do not read it as evidence for any of them. That it is the first published statement of the idea is the usual attribution, and this reading could not confirm it (see [NOTE-tmp6hixb](../notes.d/NOTE-tmp6hixb.md)).'
title: 'Plain Talk About Neurodevelopmental Epistemology'
version: 1
history:
- version: 1
  date: '2026-10-01'
  note: >-
    Read in full: the IJCAI-77 text (Proceedings of the Fifth International
    Joint Conference on Artificial Intelligence, Cambridge, Mass., August
    1977, vol. 2, pp. 1083–1092; PDF from ijcai.org,
    Proceedings/77-2/Papers/098.pdf, with a text layer). I also OCR'd the
    MIT AI Memo 430 scan on DSpace (https://hdl.handle.net/1721.1/5763,
    June 1977, 23 pp.) and compared it word by word with the IJCAI text:
    apart from the memo's cover, abstract page and diagram residue the two
    agree (difflib word-sequence ratio 0.98), so they are one text. The
    memo's cover says the paper "will be presented" at IJCAI-77 in August
    1977, so the memo is the first appearance and `published:` is its
    month. Citation verified on DSpace (title, AIM-430, 1977-06-01; DSpace
    misspells the author as "Minksy") and on the IJCAI proceedings index
    (invited paper, M. Minsky, p. 1083). A condensed version in Winston and
    Brown (eds.), Artificial Intelligence: An MIT Perspective, vol. 1 (MIT
    Press, 1979), is cited by Minsky in AIM-516 and was not seen. Not held
    in the Anthology of the SOTA.
tags:
- cognition
- mereology
- agency
- complex-systems
- linguistics
date: '2026-10-01'
published: '1977-06-01'
url: 'https://hdl.handle.net/1721.1/5763'
first_author: 'Minsky'
keywords:
- 'society of minds'
- 'agents'
- 'c-lines'
- 'short term memory'
- 'specificity gradient'
- 'laminar hypothesis'
- 'case-shift'
- 'cognitive cases'
- 'language acquisition'
implementations: []
extends:
- LIT-tmpf92fs
extended_by:
- LIT-tmp84goj
summary: >-
  Minsky (1977), MIT AI Memo 430, also IJCAI-77 pp. 1083–1092. Takes the
  mind as an organised society of simple "agents", a theory credited to
  joint work with Papert, and asks how such agents could communicate
  without language. The proposal: no messages at all, since each argument
  lives at a fixed location on shared channels ("c-lines") that the agents
  themselves constitute as short-term memory. A specificity gradient
  confines low-level agents to local sub-societies, and a case-shift moves
  an object of attention into a better-described slot. The paper
  conjectures that these internal cases precede, and shape, the cases of
  natural language. Openly speculative.
---
<!-- inactive-ok-file: LIT-046 — Proposed; named as a neighbouring account of collective intelligence, not leaned on -->

# LIT-tmp4jv7c: Plain Talk About Neurodevelopmental Epistemology

Marvin Minsky (1977), *MIT Artificial Intelligence Laboratory, A.I. Memo No.
430*, June 1977, 23 pp. — https://hdl.handle.net/1721.1/5763. Also an invited
paper in *Proceedings of the Fifth International Joint Conference on
Artificial Intelligence (IJCAI-77)*, Cambridge, Mass., August 1977, vol. 2,
pp. 1083–1092.

## Key takeaways

- The mind is "an organized society of intercommunicating 'agents'", each
  "by itself, very simple". The opening example is a child's play with
  blocks, in which WRECKER, BUILDER, PUT and GRASP serve
  PLAY-WITH-BLOCKS, and PLAY loses out to I'M-GETTING-HUNGRY.
- Agents too simple for language communicate by sending **nothing**: "Each
  of an agent's data sources is a FIXED location in (short term) memory."
  In effect these are global variables, and "the agents are the STM".
- Connectivity follows a **specificity gradient**: few, brain-wide top-level
  channels, and progressively local sub-societies that can talk only
  through the levels above them.
- **Persistence-memory** and a **transient case-shift** let a young mind
  survive interruptions without a recursive stack. Recursion in adults is
  "probably an illusion" of description (Note 7).
- The "cognitive cases" an infant's agents use internally would later be
  "relatively easy to encode into external symbols". On this view learning
  language is "learning to translate between languages", and linguistic
  universals reflect early internal uniformities.

## Standing in the record

Filed on 2026-10-01 at the owner's request, as part of Minsky's Society of
Mind programme. Of the four memos filed in this pass, it is the first to
state the society-of-agents view, and it names the theory "The Society of
Minds" (Note 1). There it is described as "a theory being developed in
collaboration with Seymour Papert", which "we hope to publish … within the
next year or so". Whether this is the first published statement anywhere is
the usual attribution, and I could not confirm it: Minsky's AIM-516 credits
a principle of the theory to Minsky and Papert's 1974 University of Oregon
lectures, which I did not see.

The paper says how it builds on the frame memo ([LIT-tmpf92fs](LIT-tmpf92fs.md)). It is "in
part a sequel" to it. Its fixed data locations are "an extension of the
'common terminal' idea in my paper on frame-systems". Its two-way memory
addressing revisits that memo's two-level frame matching. In turn, K-lines
([LIT-tmp84goj](LIT-tmp84goj.md)) says its own K→P connections correspond roughly to this
paper's c-lines, and offers itself as a complement. The book-length *Society
of Mind* (1986), filed alongside by another pass, is the publication this
paper promises.

[NOTE-tmp6hixb](../notes.d/NOTE-tmp6hixb.md) is the close reading of 2026-10-01, and it placed the work:
**Active**. It is worth reading as the earliest mechanism-level statement of
the programme. It is not evidence for it. The neurological parts (c-lines as
white matter, the laminar hypothesis) are offered "with no pretense that
there is any solid evidence".

Neighbours in this record:

- **Collective intelligence.** The computational account of collective
  intelligence ([LIT-046](LIT-046.md)) asks what a collective computes that its members
  cannot. This paper runs the analogy the other way. A mind is a society, but
  one whose members are "all equally mindless", so the social analogy is
  "poor" (Note 9).
- **Group minds.** Schwitzgebel's argument that a nation could be conscious
  ([LIT-159](LIT-159.md)) needs collectives of minded members. Minsky's society needs
  none.
- **Extended mind.** The extended-mind thesis ([LIT-097](LIT-097.md)) moves cognition
  outward from the head. This paper moves it downward into parts.

These pairings are mine. The paper carries no instruction for
machine-learning practice, and no anthology topic holds it.
