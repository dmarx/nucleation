---
status: Read
paper: LIT-tmpf92fs
title: 'A Framework for Representing Knowledge'
version: 1
history:
- version: 1
  date: '2026-10-01'
  note: >-
    Read in full from MIT AI Memo 306 (June 1974), the 82-page scan on MIT
    DSpace (https://hdl.handle.net/1721.1/6089). The PDF has no text layer;
    I rendered each page at 200 dpi and read Tesseract's OCR of the cover,
    §§1–5, the Appendix (§6) and the bibliography. The OCR is good on
    running text but lost every figure (the cube and room diagrams, the
    river-flow frames, the similarity-network figure 3.1), so where an
    argument leans on a figure, this note relies on the prose around it.
    Pages 2 and 3 of the scan are blank or a cover verso. The 1975
    condensed version in The Psychology of Computer Vision was not seen.
date: '2026-10-01'
summary: >-
  The frame memo. A frame is a stereotyped situation-structure whose
  terminals carry conditions and weakly bound defaults. Frames sharing
  terminals form systems whose transformations encode moves, actions and
  shifts of viewpoint, and mismatches are routed through a learned
  similarity network. Applied to vision, imagery, language, memory, search
  and control, with an appendix arguing that monotonic, consistency-seeking
  logic cannot carry commonsense knowledge. A programme statement:
  nothing is built or measured, and the author says what is missing.
---

# NOTE-tmp0yhbo: A Framework for Representing Knowledge

## Contribution

The memo proposes that the units of perception, language understanding and
reasoning are large structured chunks, called frames, not small facts. It
makes three new moves, by its own account. The frame idea itself it places in
the tradition of Bartlett's schema and Kuhn's paradigms, and calls "not
particularly original"; the frame-*system* "is probably more novel" (p. 3).

- **Defaults.** Frames come with weakly bound default fillers that new
  evidence displaces.
- **Frame-systems.** Frames share terminals, so a change of viewpoint keeps
  what has already been seen.
- **Retrieval.** A frame that fails is replaced through difference-labelled
  pointers between frames.

It ends with a sustained case against representing commonsense in logistic,
monotonic, consistency-seeking systems.

## Key insight

Understanding is retrieval followed by repair. One does not build a
description of a scene or a story from parts. One pulls a whole remembered
stereotype from memory, with every slot already filled by a default, and
spends one's effort only where reality disagrees with it. Speed, the sense
that one sees a whole room at a glance, and the stubbornness of stereotypes
all come from the same source: most of what one "sees" or "understands" was
assumed.

## Assumptions

- **No boundary between psychology and AI.** "I draw no boundary between a
  theory of human thinking and a scheme for making an intelligent machine"
  (§1.3).
- **Sufficiency over parsimony.** The memo aims at mechanisms that could work
  quickly enough, not at the fewest mechanisms, and says parsimony is
  "inappropriate at this stage" (§1.3).
- **Serial symbolic processing.** Parallelism is useful at the level of
  feature detection, and the memo doubts its usefulness at "higher" levels
  (§1.2).
- **Incompleteness, stated.** Representations are often proposed "without
  specifying the processes that will use them" (p. 2, "Apology!").
- **Development.** Direct frame use is identified with Piaget's concrete
  operations (§1.12). Reasoning *about* transformations is left to a later
  stage the memo does not model.

## Key results

There are no theorems and no experiments. The results are proposals with
worked examples.

- **Frame anatomy (§1, pp. 1–2).**
  - Top levels are fixed.
  - Terminals have markers, which are conditions on their assignments.
  - Assignments are usually sub-frames.
  - Frames that share terminals form frame-systems, linked in turn by an
    information-retrieval network.
- **Vision (§§1.4–1.9).**
  - The cube is a frame-system whose MOVE-RIGHT and MOVE-LEFT
    transformations keep face descriptions in shared and "invisible"
    terminals.
  - Rooms, perspective and occlusion are handled the same way. The memo
    flags a "serious bug": one motion name passed down to subframes
    mispredicts near and far walls (§1.8).
- **Seeing and imagining (§1.10).** Both end in terminal assignments. Seeing
  feels more vivid because its assignments resist change, not because
  something is lost from memory, which was Hume's view.
- **Defaults (§1.11).**
  - Frames are never stored with unassigned terminals.
  - Defaults yield "pseudo-syllogisms": "Most A's are B's and most B's are
    C's, so most A's are C's" is believed, though sometimes false (§1.12).
- **Language (§2).**
  - Grammaticality and meaning are two ends of a continuum (§2.1). If the
    top frame fits but low terminals do not, the sentence is meaningless; if
    low fragments fit but the top is weak, it is ungrammatical but meaningful.
  - Discourse builds a growing scene- or story-frame, and the verb-centred
    case frame is a transient stage (§2.3).
  - Scenario frames are the subject of §§2.6–2.7, which use Charniak's
    birthday-party and kite stories.
  - Terminals are reinterpreted as questions (§2.8): "A Frame is a
    collection of questions to be asked about a hypothetical situation."
  - The memo names four levels of frames: surface syntactic, surface
    semantic, thematic and narrative (p. 39).
- **Memory (§3).**
  - It poses five problems: expectation, elaboration, alteration, novelty
    and learning.
  - It proposes four responses to a frame in trouble: matching, excuses,
    advice and summary.
  - Winston's similarity network supplies the advice. The memo argues that
    its cost of K·N² pointers is no obstacle, and that the real problem is
    "too few connections" (§3.4).
  - The geographic analogy of blocks, towns and capitols explains short
    retrieval paths. Family resemblance falls out of local
    difference-pointers (§3.5).
- **Problem solving (§§3.6–3.8).**
  - The car-generator example works in two frame-systems at once,
    mechanical and electrical, with a visual one as well.
  - A new paradigm for search: "the purpose of search is to get information
    for this reformulation, not … to find solutions" (§3.7, p. 56). A
    minimax score is a number that cannot say why a position is weak, so
    recursive frame-summaries should replace it.
  - New frames are built by debugging old ones, after Sussman and Goldstein
    (§3.8).
- **Control (§4).** Neither top-down nor lateral filling, and neither central
  nor demon control, is uniformly right. The section includes Scott
  Fahlman's "Frame Verification" text, which proposes packets of facts and
  demons, recognition by exemplars with excuses, and frame hierarchies with
  "parasitic" frames such as statue-of.
- **Spatial imagery (§5).**
  - A Global Space Frame of typical locations is proposed, which the author
    says he does "not like … very much".
  - Arguments follow on evolution, and against quantitative models: a
    number "is an evaluation -- and not a summary" (p. 73).
- **Appendix (§6).** Logistic systems fail on five counts:
  - relevancy;
  - **monotonicity**: "each added axiom means more theorems, none can
    disappear";
  - procedure-controlling knowledge (illustrated by the transitivity of
    "near");
  - combinatorial explosion;
  - consistency, which "is not necessary or even desirable in a developing
    intelligent system".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Much of perception and understanding consists of retrieving a stored frame and adapting it, with weakly bound defaults filling everything not observed | weak | argued from introspection and worked examples (cube, room, kite story); no program or experiment |
| C2 | Shared terminals across a frame-system let a viewpoint change reuse prior analysis without recomputation | moderate as a design argument | the cube construction (§1.4) shows it works for a convex object; §1.8 admits it fails as stated for rooms |
| C3 | Seeing feels more vivid than imagining because seen assignments resist change, not because of loss in storage | weak | asserted against Hume (§1.10); no evidence offered |
| C4 | Grammaticality and meaningfulness are two ends of one continuum of frame-fit | weak | one worked example (Chomsky's sentence pair, §2.1) |
| C5 | Family resemblance needs no definition: it follows from local difference-pointers and cluster capitols | moderate as an existence argument | §3.5 shows how such a structure could yield crisscross resemblances; nothing shows people have it |
| C6 | In problem solving, search is for information to reformulate the problem space, not for solutions | assertion | §3.7; offered as a paradigm, with the summary-divergence problem noted |
| C7 | Logistic systems cannot represent commonsense knowledge, because they are monotonic and separate facts from advice on their use | moderate | §6; the monotonicity point is a correct observation about classical logic; that no repair is possible is asserted ("I think such attempts will continue to fail") |
| C8 | Consistency is neither necessary nor desirable in a developing intelligent system | assertion | §6; argued by analogy with human inconsistency and the mathematician who "shall not take that step" |

## Concepts

- **Frame.** "A data-structure for representing a stereotyped situation"
  (p. 1), with fixed top levels and terminals. It is later reinterpreted as
  "a collection of questions to be asked about a hypothetical situation"
  (§2.8).
- **Terminal / slot.** A place for an assignment, usually a sub-frame,
  governed by **markers** (conditions).
- **Default assignment.** A filler attached "loosely" to a terminal, which
  serves as a variable, an example or a stereotype until displaced (§1.11).
- **Frame-system.** Frames sharing terminals, linked by transformations that
  stand for actions or changes of viewpoint.
- **Similarity network.** Winston's pointers between frames, each labelled
  with a difference, used to propose a better candidate after a mismatch
  (§3.4).
- **Capitol.** A focal frame of a cluster under some difference, so that
  retrieval routes through a few centres (§3.5).
- **Excuse.** An explanation that saves a failing match, such as occlusion,
  a functional variant, breakage or a parasitic context (§3.3).
- **Logistic system.** One that separates propositions from general laws of
  inference completely (§6).

## Connections

- **Sources the memo names.** Bartlett's schema and Kuhn's paradigms for the
  frame idea. Winston's similarity networks for retrieval. Charniak's
  demons, Schank's conceptual dependency, Wilks's preference semantics,
  Abelson's scripts and Fillmore's case grammar for language. Piaget for
  development. Sussman and Goldstein for debugging. McCarthy's Airport
  problem as the target of the appendix.
- **Within this filing.**
  - Plain Talk ([LIT-tmp4jv7c](../literature.d/LIT-tmp4jv7c.md)) builds directly on it: its fixed-location
    channels extend the common terminal, and it calls itself "in part a
    sequel".
  - K-lines ([LIT-tmp84goj](../literature.d/LIT-tmp84goj.md)) reimplements a frame as a K-node over a level
    band of agents (its Note 9).
  - The jokes memo ([LIT-tmpcmegc](../literature.d/LIT-tmpcmegc.md)) uses frame-shift as the core of humour.
- **Later books.** The 1986 *Society of Mind*, filed alongside by another
  pass, keeps frames as one representation among the agencies, as do the
  later books in that line.

## Bearing on the record

- **Concepts and contexts.** Aerts and Gabora ([LIT-340](../literature.d/LIT-340.md)) measure, in their
  "pet" data, the context-shift of exemplar typicality that §1.11 and §3.3
  build into displaceable defaults. The memo predicts the direction of such
  effects and nothing quantitative. The pairing is mine.
- **Retrieval.** The "find a frame with as many terminals in common … as
  possible" request (§3.2) is a best-match retrieval. The record's reading
  of sparse distributed memory ([NOTE-242](NOTE-242.md)) names this problem after Minsky
  and Papert.
- **THEORY.** No THEORY document in the record cites or should cite this
  memo as evidence. It is a source of hypotheses, not of support.
- **Boundary.** It carries no instruction for machine-learning practice, and
  no anthology topic holds it.

## Limitations

- **Unbuilt, by its author's account.** The memo proposes structures
  "without specifying the processes that will use them" (p. 2), so no
  claim in it is tested.
- **No arithmetic of matching.** It never says how strongly a default is
  bound, how much "strain" a match can bear, or when a frame should be given
  up. The memo itself says these depend on goals and context. Fahlman's
  section sketches a numerical satisfaction score; the memo's own text
  argues against such scores (§5.5).
- **Mostly vision and stories.** The worked domains are visual scenes and
  short stories. Its claims for reasoning and problem solving rest on two
  examples, the car generator and chess summaries.
- **One-sided appendix.** It attacks "logistic" in general but engages one
  target, McCarthy's Airport problem. It offers no alternative formalism, and
  says so.

## Open questions

- Can frame-system transformations be made to work for concave scenes and
  partial motions? The memo's own "serious bug" (§1.8) is left open.
- What controls how far a default may be stretched before the frame is
  replaced? Only a mechanism with measurable consequences could test C1.
- What, beyond the frame machinery, is needed for reasoning *about*
  transformations, Piaget's formal operations? The memo says it has "no idea
  what role frame systems might play" there (§1.12).

## Corrections

- none to a seeded skim (there was no seed).
- **Citation.** The brief's details are right: MIT AI Memo 306, June 1974.
  DSpace records it as 82 pages. The 1975 McGraw-Hill chapter is a condensed
  version, not the same text; Minsky's own AIM-603 bibliography calls it
  "condensed".
- **What the memo is a precursor of.** It contains no society-of-agents
  idea. A reader who arrives from the Society of Mind should not expect one.
  The only "agents" in the memo are case roles (§§2.2, 2.8).
