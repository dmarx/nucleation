---
number: 359
status: Read
formerly:
- NOTE-tmprnrsd
paper: 'LIT-414'
title: 'High-level perception, representation, and analogy: A critique of artificial intelligence methodology'
version: 1
history:
- version: 1
  date: '2026-10-01'
  note: >-
    Read in full, from the authors' preprint posted by Chalmers
    (https://consc.net/papers/highlevel.pdf; CRCC Technical Report 49,
    Indiana University, March 1991; 36 pp.; text extracted with PyMuPDF).
    I read the abstract, §1 (the problem of perception), §2 (AI and the
    problem of representation, including the BACON case study), §3
    (models of analogical thought, SME and ACME, and the two arguments
    against a representation module), §4 (Copycat), §5 (conclusion) and
    the 36 references. Figure 1 was read from its extracted labels;
    Figures 2–3 survived only as labels. The published JETAI text
    (4(3):185–211, 1992) was not seen. Page numbers below are the
    preprint's own (1–34, after the title and abstract pages). Two
    references were checked against Crossref.
date: '2026-10-01'
summary: >-
  Traditional AI models of discovery and analogy (BACON, the
  Structure-Mapping Engine, ACME) start from representations built by
  people who already know the answer, and so skip high-level perception,
  where most of the difficulty lies. Two informal arguments say the gap
  cannot be closed later by a separate representation module: analogy
  shapes perception, and the right representation depends on the task.
  Copycat is described as an architecture that builds representations and
  mappings together. Argued well; nothing is measured in the paper.
---
<!-- inactive-ok-file: LIT-416 — Deferred, unreachable full text; Hofstadter's "Is there an 'I' in AI?", named as a neighbour, not leaned on -->
<!-- inactive-ok-file: LIT-435 — Deferred, closed access; Mitchell & Hofstadter's Copycat paper, named as the program's primary description, not leaned on -->
<!-- inactive-ok-file: THEORY-023 — Proposed; named as the account a behavioural criterion for thought runs into, not leaned on -->

# NOTE-359: High-level perception, representation, and analogy: A critique of artificial intelligence methodology

## Contribution

The paper names a methodological error and gives it a mechanism. The error is
modelling cognition on hand-built representations. Chalmers, French and
Hofstadter call the work those representations hide *high-level
perception*: deciding which of the available data are relevant (the
"problem of relevance") and organising them into structure (the "problem of
organization", p. 4–5). They show the error at work in two celebrated
programs. Then they argue it cannot be excused as a postponement, because
perception cannot be split off from the task that uses it. Finally they
present Copycat as an existence proof that the two can be run together. The
first two parts are new as a sustained critique; the third summarises work
published elsewhere ([LIT-435](../literature.d/LIT-435.md)).

## Key insight

Representations are the product of perception, and perception is shaped by
what the representation is for. A model handed its representation has
therefore been handed most of its answer. Analogy-making is the clearest
case: the analogy decides which aspects of a situation matter (DNA as a
zipper, or DNA as source code, pp. 11, 18), and analogies in turn shape how
situations are perceived ("Nicaragua as another Vietnam", p. 11). So
analogy is "not separate from perception: analogy-making itself is a
perceptual process" (p. 17).

## Assumptions

(Premises of an argument, since the paper proves nothing formally.)

- **High-level perception begins "where concepts begin to play an important
  role"** (p. 2). Low-level perception is set aside throughout, and the
  authors concede a complete model must include it (pp. 2, 30).
- **Human high-level perception is flexible**: shaped by belief, goals and
  external context, and capable of radical restructuring (pp. 3–4). The
  support is examples and older experiments (Bruner's New Look, Maier's
  two-string problem), not new data.
- **Representations are short-term, active, working-memory structures**,
  as distinct from long-term knowledge (p. 4); the argument is about the
  former.
- **Fodor's and Pylyshyn's encapsulation arguments apply mostly to
  low-level perception** (p. 4). Asserted in one sentence ("Few would
  dispute"), and load-bearing: the argument needs top-down influence at the
  conceptual level.
- **Microdomains are a legitimate route to the real world** (pp. 20–21).
  The authors argue that "real world" programs like BACON and SME are
  themselves "stripped-down domains of certain highly idealized logical
  forms" with English labels attached.

## Key results

(What it argues and reports.)

- **BACON (pp. 8–10).** Its "discovery" of Kepler's third law used only mean
  distances and periods, "precisely the data required to derive the law",
  plus a bias toward algebraic laws. Kepler took thirteen years among
  Platonic solids, circles and theology. Qin and Simon's finding that
  students given BACON's data rediscover the laws within an hour is read as
  a "reductio ad absurdum of the BACON methodology", not as support for it
  (p. 10). Similar remarks are said to apply to STAHL and GLAUBER.
- **SME (pp. 13–15).** In the atom/solar-system example the
  representations contain almost exactly the relations the analogy needs:
  "attracts", "revolves around", "gravity", "opposite-sign", "greater" and
  "cause" (p. 14). The object/attribute/relation split and SME's arity
  matching (a 3-place predicate maps only to a 3-place predicate) force
  arbitrary choices to which the program is "highly sensitive" (p. 15).
  The authors credit SME's mapping work and note its authors made no
  claims of insight.
- **ACME (p. 16)** uses a connectionist network for soft-constraint
  mapping, but on "preordained, frozen structures of predicate logic".
- **Argument 1 against a representation module (p. 17).** Perception
  depends on analogy (the Satanic Verses and Last Temptation of Christ
  analogy; Saddam Hussein as Hitler or as Robin Hood), so analogy-making
  cannot be split into "first perception, then mapping".
- **Argument 2 (pp. 18–19).** A module would have to supply one
  context-independent representation. Either it is too narrow for some
  tasks (zipper vs. source code), or it is all-encompassing, and then
  selecting from it is "tantamount to high-level perception all over
  again". Claimed to apply to "almost any area within artificial
  intelligence".
- **Copycat (pp. 21–29).** Letter-string analogies in a non-circular
  alphabet. Codelets, chosen nondeterministically from a pool, build bonds,
  groups, descriptions and correspondences; the Slipnet's activations spawn
  and favour codelets (top-down over bottom-up); perception and mapping
  codelets share the pool; computational temperature, a measure of the
  amount and coherence of structure, sets the randomness ("parallel
  terraced scan", likened to Holland's two-armed bandit). On "abc → abd,
  xyz → ?" a snag at z raises temperature, breaker codelets destroy
  structure, attention floods to Z, and the program can re-perceive xyz as
  a predecessor group to answer wyz, though "xyd is actually given more
  often than wyz" (p. 29).
- **What Copycat does not do (pp. 29–30).** It does not learn; its
  mechanisms are fixed and hand-coded, which the authors distinguish from
  BACON's and SME's fixed representations. It has no low-level perception;
  Tabletop, Chapman's Sonja and Shrager's laser program move a little
  toward it.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Most AI models of cognition skip high-level perception by starting from hand-coded representations | moderate | case studies of BACON, SME, ACME; the general claim ("endemic in traditional AI", p. 20) is asserted from them |
| C2 | BACON's success at Kepler's third law is an artefact of pre-selected data and biases, not a model of Kepler's discovery | strong as a critique of the claim made for it | §2; the authors' own reading of Qin & Simon (1990) |
| C3 | SME's representations were built with its target analogies in mind | moderate | Figure 1's relations; "difficult to avoid the conclusion" (p. 15); no alternative encoding is run |
| C4 | Analogy shapes perception, so perception and mapping cannot be temporally separated | informal argument | anecdotes (pp. 11, 17); no experiment |
| C5 | No context-independent "representation module" can serve all tasks | informal argument, the paper's strongest | the narrow-or-overloaded dilemma (pp. 18–19) |
| C6 | Copycat builds its own context-dependent representations and integrates perception with mapping | description of an architecture | §4; one worked problem; details cited to Mitchell & Hofstadter (1990) |
| C7 | Copycat's answer distributions are qualitatively similar to people's | reported, not shown here | one sentence (p. 28) citing Mitchell (1990) and Hofstadter & Mitchell (1992) |
| C8 | Copycat's re-perception of xyz is a stripped-down model of a Kuhnian paradigm shift | analogy | p. 29 |

## Concepts

- **High-level perception.** Perception from the level where concepts
  matter: object recognition, relations, and whole situations; "semantic",
  "drawing meaning out of situations" (pp. 2–3).
- **Problem of relevance / problem of organization.** Which data enter the
  representation; how they are put into its form (pp. 4–5).
- **Meaning barrier.** The gap, "rarely crossed by work in AI", between
  low-level programs whose representations are not yet meaningful and
  high-level programs whose meaning is built in (p. 5).
- **Representation module.** The hypothetical front end that would supply
  ready-made representations to task processes (p. 7).
- **20–20 hindsight.** Representations designed with the answer known.
- **Codelet, Slipnet, computational temperature, parallel terraced scan.**
  Copycat's agents, concept network, randomness control and search
  strategy (pp. 23–28).

## Connections

The paper is the methodological companion to the Copycat paper
([LIT-435](../literature.d/LIT-435.md)), which it cites for details; this record holds that paper
unread. Its targets are named exactly: Langley, Simon, Bradshaw and
Zytkow's BACON; Falkenhainer, Forbus and Gentner's SME, built on Gentner's
structure-mapping theory; Holyoak and Thagard's ACME. It sides with
connectionist context-dependent representations (Rumelhart & McClelland,
Elman) and Holland's classifier systems as "a step in the right direction"
(p. 7), and cites Marr, James and Lakoff against objectivist representation.
Among the formats it lists, frames come from Minsky ([LIT-410](../literature.d/LIT-410.md), filed in
the same session); the paper does not cite Minsky, but its target, a
representation format whose slots someone else fills, is the frame
tradition's open question. It cites Evans's ANALOGY from Minsky's edited
*Semantic Information Processing* as the early analogy program that did
build its own representations.

## Bearing on the record

- **No THEORY document** in the record makes a claim this paper supports
  or contradicts. [THEORY-023](../theory.d/THEORY-023.md) is about evidence for machine consciousness,
  which the paper does not discuss.
- **Emergence.** Its Copycat section is an engineered case of "higher-level
  understanding emerges" from local parallel processes with top-down
  modulation (p. 21), which the record's emergence surveys ([LIT-141](../literature.d/LIT-141.md),
  [LIT-150](../literature.d/LIT-150.md)) could use as an example; the paper offers no account of
  emergence beyond the phrase.
- **Machine understanding.** The "meaning barrier" frames the question
  that [LIT-131](../literature.d/LIT-131.md) (understanding in deep networks) and Hofstadter's 2026 essay
  ([LIT-416](../literature.d/LIT-416.md)) ask of learned systems. A THEORY could be drawn, but only
  with those readings in hand.
- **ML practice.** It carries an instruction for AI modelling (build
  representation-forming into the model; do not hand-code it), addressed to
  symbolic cognitive modelling of 1990. No anthology topic holds it well;
  the closest is the anthology's `analysis-and-evaluation`, for the charge
  that a program's success can be an artefact of its inputs.

## Limitations

- **Nothing is measured.** The Copycat evidence is architectural
  description and one problem; the human comparison is one sentence citing
  other work.
- **The case studies are few.** BACON and SME are typical, the authors say,
  and ACME and four other programs get a sentence each; "endemic" is
  inferred from them.
- **The Copycat defence is quick.** Against the charge that codelets and
  the Slipnet are themselves hand-coded hindsight, the reply is that
  mechanisms, unlike representations, are fixed in people too, and their
  origin is "a question about learning" (pp. 29–30). The Slipnet's concepts
  (successor, sameness, leftmost) are the domain's relevant relations, so
  the hindsight charge is moved, not answered.
- **Argument 2 assumes working memory is small** and that selecting from a
  large representation is as hard as perceiving afresh; both are asserted.
- **Preprint only.** The published text may differ.

## Open questions

- Does Copycat's architecture scale to domains whose relevant concepts were
  not chosen by its designers? The paper names Tabletop as a step and
  leaves it there.
- Where would learned representations from end-to-end training fall in the
  critique: as the flexible, context-dependent representations it asks
  for, or as another fixed representation module? The paper's only
  evidence on connectionism is its approval of context-sensitivity.

## Corrections

- The brief's citation (authors, journal, 4(3):185–211, DOI) is correct.
- The paper's reference for Maier (1931) gives the journal as *Cognitive
  Psychology*, 12:181–194. It is *Journal of Comparative Psychology*
  12:181–194 (Crossref, DOI 10.1037/h0071361); *Cognitive Psychology* did
  not exist in 1931.
- The Kant quotation "Concepts without percepts are empty; percepts without
  concepts are blind" (p. 31) is a paraphrase. Kant's sentence (*Critique
  of Pure Reason*, A51/B75) is usually rendered "Thoughts without content
  are empty, intuitions without concepts are blind."
