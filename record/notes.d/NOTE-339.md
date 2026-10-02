---
number: 339
status: Read
formerly:
- NOTE-tmp262x5
paper: LIT-444
title: 'Examining the Society of Mind'
version: 1
history:
- version: 1
  date: '2026-10-01'
  note: >-
    Read in full: the journal's open-access PDF (cai.sk, article 467),
    23 pp., text extracted with PyMuPDF. I read the abstract, §§1–5, the
    acknowledgements, all 34 references and the author note. I checked the
    paper's citations of Minsky's 1991 reply against Crossref's records of
    that issue, and its forward references to *The Emotion Machine*
    against the 2005 draft of that book. I could not check its quotations
    of *The Society of Mind* or of the 1976 "Brazil" drafts: the first is
    unread in this record, and the second is unpublished.
date: '2026-10-01'
summary: >-
  An exposition, read in full. Singh dates the Society of Mind to Minsky
  and Papert's early-1970s robot work, finds its agent in the
  procedure-bearing frame of 1974, and quotes the unpublished 1976 book
  drafts. He sorts the 1986 book's mechanisms into agents, simplest agents,
  agency construction, problem solving, communication and growth. Agents
  need no shared code: K-lines, randomly wired buses and paranomes stand in
  for messages. He finds near-relatives in Bayes nets, case-based
  reasoning, blackboards, Cyc and Soar, and concludes that the theory has
  never been implemented. Its claims of lineage are asserted, not shown.
---
<!-- inactive-ok-file: LIT-046 — Proposed; named as a neighbouring account of collective intelligence, not leaned on -->
<!-- inactive-ok-file: LIT-418 — Deferred, closed access; named as Minsky's reply to the reviews of the book, not leaned on -->
<!-- inactive-ok-file: LIT-429 — Deferred, no lawful full text; named as the book this work belongs to or answers, not leaned on for its content -->

# NOTE-339: Examining the Society of Mind

## Contribution

A compact, mechanism-by-mechanism guide to *The Society of Mind*
([LIT-429](../literature.d/LIT-429.md)), aimed at "those interested in implementing Societies of
Mind" (§3). Minsky presents those mechanisms "in fragments and at a variety
of levels". Singh gathers them into one catalogue. He adds the theory's
early history, including quotations from unpublished 1976 drafts that he
had from Minsky and Papert. He also places the theory against the AI of
1986–2003 and says where each neighbour falls short of it.

## Key insight

The Society of Mind is a theory of organisation, not of a mechanism. Its
claim is that intelligence comes from the diversity of many specialised
processes and from how they are managed, not from one principle. Singh
quotes §30.8: "The trick is that there is no trick." So the hard problems
are the ones a uniform architecture hides. They are how agents that cannot
understand each other's representations still cooperate, and how
managerial knowledge chooses among them. That is the test Singh puts to
every later system.

## Assumptions

- **Exposition, not argument.** The paper describes the theory as Minsky
  stated it and does not defend it against its critics. The four 1991
  reviews (in the issue [LIT-418](../literature.d/LIT-418.md) closes) appear only through Dyer's
  connectionist alternatives (§4.1).
- **The author's position.** Singh was Minsky's doctoral student,
  "presently collaborating with Marvin Minsky to develop an architecture for
  commonsense thinking" (author note). The paper is openly sympathetic: "we
  predict that The Society of Mind will still be read decades from now".
- **Scope.** "In this article we could only examine a small fraction of the
  full Society of Mind theory" (§5).

## Key results

- **History (§2).**
  - The copy-demo robot of the late 1960s: "no single method ever worked well
    by itself" (quoting the book's Postscript).
  - Newell's 1962 "single personality, wandering over a goal net" is the
    view the theory opposed.
  - Frames (1974) included Fahlman's essay on frames as "a packet of related
    facts and agencies". Hewitt's Actors (1976) was a message-passing
    contemporary that Minsky and Papert's agents differed from.
  - The 1976 "Brazil" drafts: "The mind is a community of 'agents'. Each has
    limited powers and can communicate only with certain others."
  - The 1977 IJCAI paper names the theory "The Society of Minds" and says
    mental abilities "both 'intellectual' and 'affective' (and we ultimately
    reject the distinction)" emerge from "quasi-political hierarchies" of
    agents, critics and censors. The 1980 K-lines paper describes "Divisions"
    of agents.
- **Agents (§§3.1–3.2).** An agent is "any component of a cognitive process
  that is simple enough to understand". An agency is a society of agents
  that does more. Mental activity "ultimately reduces to turning individual
  agents on and off", and a "partial state of mind" is a subset of agent
  states.
  - K-lines are "the most common agent". They chunk a problem-solving
    episode, false starts included, so that its configuration can be
    re-entered.
  - Nemes (polynemes, micronemes) represent. Nomes (isonomes, pronomes,
    paranomes) control.
- **Combining agents (§3.3).** Frames are built from bound pronomes.
  Frame-arrays share slots across viewpoints, and shared slots are "the
  ancestors of paranomes". Transframes represent events, with origin,
  destination, actor, motive and instrument.
- **Problem solving (§3.4).** Difference-engines, after GPS, are "elevated to
  a central principle". Censors and suppressors carry "negative expertise",
  which may be "the bulk of what we know, yet remain invisible". Humour is
  linked to it, citing the jokes memo. A B-brain watches the A-brain.
- **Communication (§3.5).**
  - Agents cannot share consistent symbol definitions. Minsky: "The fewer
    things an agent does, the less likely that what another agent does will
    correspond to any of those things."
  - So agents communicate by arousal through K-lines, and by randomly
    connected bus lines whose meanings both sides learn ("first invented by
    Calvin Mooers", with "low probability of collision").
  - They use an internal language of "grammar-tactics" and their inverses,
    from the 1991 reply.
  - Paranomes, "the most common method", work with "no active communication
    at all".
  - "Thoughts themselves are ambiguous!" (§20.1).
- **Growth (§3.6).** Protospecialists. Predestined learning. Accumulating,
  uniframing, transframing and reformulating. Learning goals from
  attachment figures ("goal learning" as against "skill learning"). Mental
  managers and Papert's Principle (§10.4). The Principle of Non-Compromise.
  Stages that teach each other.
- **Since 1986 (§4).**
  - Symbolic–connectionist hybrids: Dyer, Shastri's SHRUTI, Maes.
  - Graphical models resemble neme networks. Ring-closing is "similar in
    some ways" to Pearl's belief propagation. Graphical models lack nomes and
    procedural control knowledge.
  - Brooks's Behavior Language and Hearn's K-line Language are attempts at a
    Society of Mind programming language.
  - Case-based reasoning: derivational analogy "came directly from the
    K-line theory".
  - Blackboards fail to scale past a few agents "huddled around a
    blackboard".
  - Cyc's microtheories resemble agencies, but Cyc knows little about
    cognitive processes.
  - Soar is the "opposite" in philosophy but similar in mechanism, as
    Minsky's 1993 review of Newell found.
  - Multiagent systems lack the heterogeneous, reflective architecture the
    theory proposes.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The Society of Mind grew from Minsky and Papert's robot work and from frames, with agents descended from frames with attached procedures | moderate | quotations from Minsky's own retrospective passages and the frames memo; the frame-as-ancestor link is Singh's reading |
| C2 | Minsky and Papert drafted a society-of-mind book by 1976 and abandoned it | moderate | quoted from the book's Postscript; the "Brazil" drafts are cited as unpublished and were given to the author, so they cannot be checked |
| C3 | Agents in the theory communicate mainly without shared symbols: by K-line arousal, learned bus codes and paranomes | strong as a description of the book | §3.5 quotes the book and the 1991 reply; it describes, it does not evaluate |
| C4 | Derivational analogy in case-based reasoning "came directly from the K-line theory" | weak: asserted | cites Carbonell (1983) [24] but quotes nothing showing the lineage |
| C5 | Graphical models lack nomes and procedural control, and will need them to scale to commonsense | weak: a prediction | §4.2, argued from the theory, not from any experiment |
| C6 | No blackboard system has been built with hundreds of agents | weak: asserted | §4.5, no survey cited for the negative |
| C7 | The Society of Mind theory has not been implemented, unlike Soar | moderate | §4.7; consistent with §4.3's partial attempts (Brooks, Hearn) |
| C8 | The theory was "ahead of its time" and the field's fragmentation explains its neglect | weak: opinion | §5 |

## Concepts

- **Agent / agency.** An agent is simple enough to understand. An agency is
  a society of agents that, seen from outside, may act as one agent.
- **K-line.** An agent that turns on a set of agents. It is often formed by
  chunking a problem-solving episode.
- **Neme / nome.** K-lines for representing ("data") and for controlling
  ("control"), "analogous to the data and control lines in the design of a
  computer".
- **Polyneme / microneme.** Arouse partial states across agencies (an
  "apple-polyneme"), or broadcast diffuse context.
- **Pronome / isonome / paranome.** Short-term role-binding; uniform
  operations across agencies; linked pronomes that keep parallel
  representations in step.
- **Transframe.** A frame for an event, with before and after states and
  their causes.
- **Negative expertise.** Knowledge of what not to do, held by censors
  (which act before the thought) and suppressors (which act before the
  action).
- **Papert's Principle.** "Some of the most crucial steps in mental growth
  are based not simply on acquiring new skills, but on acquiring new
  administrative ways to use what one already knows."
- **Principle of Non-Compromise.** A conflict between agents is a sign to
  reformulate with a third view, not to average.

## Connections

- **The 1986 book ([LIT-429](../literature.d/LIT-429.md)).** This is the record's second-hand map of
  it. Singh quotes its §§2.5, 6.12, 10.4, 20.1 and 30.8 and its Postscript.
- **The 1991 reply ([LIT-418](../literature.d/LIT-418.md)).** Singh quotes it on "agent" and "agency"
  and takes its internal-language mechanism from it. He names Dyer's review
  from the same issue.
- **The Emotion Machine ([LIT-432](../literature.d/LIT-432.md)).** Singh's footnotes 2–4 describe
  three things before publication: selector K-lines for "cognitive-emotional
  states", panalogy, and the six levels (reactive, deliberative, reflective,
  self-reflective, self-conscious, self-ideals). The 2005 draft has all
  three. Its level names differ slightly ("instinctive" and "learned
  reactions"), and its sixth level is "self-conscious reflection". The
  draft cites this paper in its Introduction.
- **The earlier memos and papers**, filed at the same time by another
  reader: the 1974 frames memo, the 1977 "Plain Talk" paper (which Singh
  shows already calls the theory "The Society of Minds"), the 1980 K-lines
  paper and the 1980 jokes memo. Singh's reference [13] gives the jokes
  memo's title as "Jokes and the Cognitive Unconscious", MIT AI Lab Memo
  603. The memo (November 1980) is titled "Jokes and their Relation to the
  Cognitive Unconscious". The version Minsky posted is headed "Jokes and the
  Logic of the Cognitive Unconscious".
- **Superimposed coding and sparse memory.** The bus scheme Singh describes
  (§3.5) uses random subsets of wires so that many symbols share a small bus
  with "a low probability of collision". That is the regime of
  near-orthogonal sparse codes in which Kanerva's sparse distributed memory
  works. Bricken and Pehlevan ([LIT-269](../literature.d/LIT-269.md)) read SDM's intersections of Hamming
  balls as attention. [NOTE-242](NOTE-242.md) cites Minsky and Papert's "Best Match
  Problem" from *Perceptrons*, not this programme. The parallel is mine;
  Singh does not draw it.
- **Collective intelligence ([LIT-046](../literature.d/LIT-046.md)).** Singh warns that "the societies of
  The Society of Mind should not be regarded as very much like human
  communities, for individual humans are 'general purpose', and individual
  agents are quite specialized" (§1). Pilgrim et al.'s framework is built on
  capable individuals. On Singh's reading, the Society of Mind is not a case
  of it.

## Bearing on the record

- No THEORY document in the record bears on it.
- It is the source for this record's knowledge of *The Society of Mind*
  while that book is unread. Anything the record says about the book's
  mechanisms should name this paper as the source until the book is read.
- **Boundary.** No instruction for machine-learning practice. §4 compares
  the theory with AI architectures, including probabilistic graphical
  models and connectionist hybrids. That is history and design comparison,
  and no anthology topic holds it as practice. I did not tag it
  `anthology-candidate`.

## Limitations

- The paper is an exposition by an insider, and it is uncritical by design.
  It reports no implementation, and its mechanism catalogue inherits the
  book's vagueness. Its §4.3 says it has been hard to find "good 'higher
  level' abstractions for agencies".
- Its history depends partly on private documents (the 1976 drafts) that a
  reader cannot see.
- It surveys only work that resembles the theory. It does not discuss work
  that argues against it, beyond Dyer's alternatives.

## Open questions

- Did any later system implement enough of the theory (K-lines, nomes,
  Critics) to test it? Singh's own architecture work with Minsky would be
  the place to look. It is not in this record.
- Is the lineage from K-lines to derivational analogy documented by
  Carbonell, or only by the Minsky school?

## Corrections

- none to a seeded skim (there was no seed)
- **Reference titles.** Reference [13] names the jokes memo "Jokes and the
  Cognitive Unconscious". Its title is "Jokes and their Relation to the
  Cognitive Unconscious", per the header of Minsky's posted copy. Reference [14] names the 1991 article "A Response
  to Four Reviews of the Society of Mind". The published title, as Elsevier
  gives it, is "Society of mind: A response to four reviews" (Crossref
  gives only "Society of mind"). Reference [34] gives no title for Singh and
  Minsky (2003).
- **Keywords differ.** The PDF gives "multiagent systems" as a keyword. The
  journal's page gives "intelligent systems" in that place.
</content>
</invoke>
