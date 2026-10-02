---
status: Read
paper: LIT-tmpsfrs2
title: 'Intelligence without representation'
version: 1
history:
- version: 1
  date: '2026-10-02'
  note: >-
    Read in full from the copy the author posts
    (people.csail.mit.edu/brooks/papers/representation.pdf, 12 pp.),
    text extracted with PyMuPDF: the abstract, §§1–8, the acknowledgement
    and all 15 references. The two figures did not extract; their captions
    did, and §6.2 describes Fig. 2's three layers in prose. The Elsevier
    typeset version was not seen. Cited works (Brooks 1986 on the layered
    control system, Agre & Chapman's memo, Minsky 1986) were not read
    here; where the paper leans on them, that is said.
date: '2026-10-02'
summary: >-
  A methodological manifesto with working robots behind it. Brooks argues
  that AI should build complete autonomous Creatures incrementally and
  test them in the real world, and that intelligence should be decomposed
  into parallel activity-producing layers, each running from sensing to
  action, not into perception, central reasoning and action. His robots
  have no central representation or control, and their coherence exists
  "in the eye of an observer", as in Minsky's account of human behaviour.
  The evidence is three layers on one robot, described, not measured, and
  the broad hypothesis about representation is flagged as a hypothesis.
---
<!-- inactive-ok-file: LIT-tmpqepho — Deferred, no lawful full text; named because this paper cites it, not leaned on for its content -->

# NOTE-tmpcsgpq: Intelligence without representation

## Contribution

The paper gives an engineering argument, with robots that run, for building
intelligence out of parallel competences instead of around a central model
of the world. Its two new things are a decomposition and a methodology.
The decomposition slices a system "in the orthogonal direction", into
layers that each produce an activity, instead of into perception, a
central reasoner and action. The methodology requires a complete,
real-world-tested system at every step, with one new layer added and
debugged at a time. The architecture itself (subsumption) was published
in 1986 and is summarised here, not introduced.

## Key insight

If every part of a system connects sensing to action by itself, the system
needs no shared description of the world. Each layer reads what it needs
straight off its sensors, "projections of a representation into a simple
subspace, if you like", and acts. A newer layer steers an older one only by
overriding its signals for a while. So nothing in the system holds a world
model, a goal list or a controller, and yet the robot avoids people,
wanders and heads for distant places. The unity an onlooker sees is, on
Brooks's account, the onlooker's: the robot "is a collection of competing
behaviors".

## Assumptions

- **The goal is engineering, not explanation.** "I have no particular
  interest in demonstrating how human beings work … I have no particular
  interest in the philosophical implications of Creatures." The
  requirements are timely response, graceful degradation, multiple goals
  that can be switched, and "some purpose in being" (§4).
- **Evolutionary argument.** Evolution spent most of its time on "the
  ability to move around in a dynamic environment". Problem solving,
  language and reason are "pretty simple once the essence of being and
  reacting are available" (§2). This is argued from the timeline, not
  shown.
- **Insect-level first.** The working target is "simple insect level
  intelligence within two years" (§8), not human-level.
- **Careful engineering of interactions.** "We are not claiming that chaos
  is a necessary ingredient"; interactions are to be carefully engineered
  (§5.1).

## Key results

- **The critique of abstraction (§3).** AI "succeeds" by defining away the
  unsolved parts. The researcher does the abstraction, producing atoms
  like PERSON, CHAIR and BANANAS, "leaving little for the AI programs to do
  but search". The human-supplied "Merkwelt" (after von Uexküll) is both
  the wrong one for robots with other sensors and possibly not the one
  humans really use. MYCIN, told of a ruptured aorta, looks for a
  bacterial cause.
- **Decomposition by function vs. by activity (§4).** Functional
  decomposition needs "a long chain of modules to connect perception to
  action", and none can be tested until all are built, so interfaces are
  chosen by the module's own researchers and "subject to intellectual
  abuse". Activity decomposition gives "an incremental path from very
  simple systems to complex autonomous intelligent systems".
- **Who has the representations? (§5).** "Not by design, but rather by
  observation", the layered robots have no central representation.
  - Low layers react quickly because they maintain no representations.
  - Changes in the world disable some layers, not all.
  - Each layer has "its own implicit purpose (or goal if you insist)",
    checked continuously against the world, which is "its own model".
  - "There need be no explicit representation of goals that some central
    (or distributed) process selects from."
  - §5.1: "Just as there is no central representation there is not even a
    central system." Coherence emerges "in the eye of an observer", and
    "Minsky [10] gives a similar account of how human behavior is
    generated."
  - Even locally, "we never use tokens which have any semantics that can be
    attached to them". A number passed between processes can be
    interpreted only "by looking at the state of both the first and second
    processes". Brooks grants that "an extremist might say that we really
    do have representations, but that they are just implicit", and
    declines the word.
  - Following Simon's ant and Agre & Chapman, "much of even human level
    activity is similarly a reflection of the world through very simple
    mechanisms" (a hypothesis).
- **Methodological maxims (§6.1).** Test in the real world, never a
  simplified one, since a simplified world infects the interfaces. Debug
  each layer extensively before adding the next, so that only the new
  layer can be varied.
- **The instantiation (§6.2).** Four robots of three designs: Allen with an
  off-board Lisp machine, Tom and Jerry with single PALs, and Herbert with
  a 24-node CMOS parallel processor. Layers are fixed networks of
  finite-state machines, with "a handful of states, one or two internal
  registers, one or two internal timers", passing 1-bit or 24-bit
  messages. "All finite state machines are equal, yet at the same time
  they are prisoners of their fixed topology connections." The three
  layers on Allen are:
  1. avoid: twelve sonars, collide, feelforce, runaway, turn, forward;
  2. wander: a random heading every ten seconds or so, summed with
     repulsion;
  3. explore: whenlook, stereo, pathplan and integrate, steering around
     the obstacles the lower layer avoids.
- **What it is not (§7).** It is not connectionism, whose nodes are uniform
  and which hopes for distributed representations: "we believe
  representations are not necessary and appear only in the eye or mind of
  the observer". It is not neural networks, and "no biological
  significance" is claimed. It is not production rules, since there are no
  variables and no matching. It is not a blackboard, since connections are
  hard-wired. It is not Heideggerian, since it was "based purely on
  engineering considerations".
- **Limits to growth (§8).** Three layers ran on a robot and six in
  simulation. A fourteen-layer soda-can robot is planned, with behaviours
  that "index off of the state of the world" instead of being centrally
  coordinated. Learning works only "as an isolated subsystem", which is
  "the very position we lambasted most AI workers for earlier in this
  paper".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | At simple levels of intelligence, explicit world models get in the way; the world is its own best model | moderate for the robots built; untested beyond them | three-layer robot run "for well over a year"; described, no measurements or comparisons |
| C2 | Representation is the wrong unit of abstraction for the bulk of intelligent systems | hypothesis, labelled (H) | the robots, plus the evolutionary timeline argument |
| C3 | Decomposing by activity gives an incremental path to complex autonomous intelligence | weak–moderate | argued against functional decomposition; demonstrated to three layers |
| C4 | The Creature has no central representation, no central control and no explicit goals; its coherence is imputed by an observer | strong for the architecture (true by construction: no global data, no global control); assertion for the interpretive claim about coherence | §§5.1, 6.2 |
| C5 | Much of human-level activity reflects the world through simple mechanisms, without detailed representations | hypothesis | Simon's ant, Agre & Chapman's unpublished memo; Minsky cited as "similar" |
| C6 | As of mid-1987 these are "the most reactive real-time mobile robots in existence" | the author's report | no comparison given |
| C7 | Testing in simplified worlds produces systems that must be rebuilt for the real one | moderate as experience; not shown | argued from how interfaces absorb a simplified world's properties |

## Concepts

- **Creature** — a "completely autonomous mobile agent" that coexists with
  humans and is seen by them "as intelligent beings in their own right".
- **Layer / activity** — a behaviour-producing subsystem that connects
  sensing to action by itself and "must decide when to act for
  [itself]", not a subroutine.
- **Subsumption architecture** — layers of fixed-topology finite-state
  machine networks, combined by suppression (a new wire replaces an input
  for a set time) and inhibition (a new wire blocks an output for a set
  time).
- **Merkwelt** — the perceptual world of an animal or robot species (after
  von Uexküll), which AI programs are handed ready-made by their
  designers.
- **The world as its own model** — reading the state of the world afresh
  through sensors instead of maintaining an internal copy.

## Connections

- **Minsky ([LIT-tmpqepho](../literature.d/LIT-tmpqepho.md)).** Cited directly, and for the point that matters
  here: "Minsky [10] gives a similar account of how human behavior is
  generated", meaning coherent behaviour from competing parts with no
  central locus. The two differ in what the parts are. Minsky's agents
  include memory and representational machinery (K-lines, frames, nemes;
  [LIT-tmp84goj](../literature.d/LIT-tmp84goj.md), [LIT-tmpxp9b8](../literature.d/LIT-tmpxp9b8.md)). Brooks's layers have "no variables" and pass
  uninterpreted numbers. Brooks is the more austere decomposition.
- **Selfridge and the homunculi.** Brooks does not cite Selfridge's
  Pandemonium or homuncular functionalism. His competing behaviours with no
  arbiter sit in the same family, but the lineage is not one he claims.
- **Levin ([LIT-tmpsygq0](../literature.d/LIT-tmpsygq0.md)).** Levin cites a 1986 paper from the same programme
  (Cudhea & Brooks, "Coordinating multiple goals for a mobile robot") as
  evidence that "modular designs with sub-goals" help. He then complains
  that robots are built from "reliable but very dumb parts". Brooks's
  layers are dumb parts by design, and each has its own "implicit
  purpose". The two agree that purpose can be distributed over parts.
  They disagree on whether the parts must be competent agents.
- **IIT 3.0 ([LIT-tmpzhi2q](../literature.d/LIT-tmpzhi2q.md)).** Not connected by either author. The bearing
  is through IIT's rule that elements outside a candidate set are only
  background conditions. Brooks's layers "interface directly to the world
  through perception and action, rather than interface to each other
  particularly much". Coordination that runs through the world would not
  integrate them on IIT. Whether a subsumption network is one complex,
  several, or none would depend on its internal wiring, which IIT treats
  as decisive and Brooks treats as an engineering detail.
- **Schwitzgebel ([LIT-159](../literature.d/LIT-159.md), [NOTE-131](NOTE-131.md)).** Not connected by either author.
  Brooks's observer-imputed coherence is the deflationary reading of what
  Schwitzgebel's telescopic view treats as real. The "Brooks" [NOTE-131](NOTE-131.md)
  lists in the group-mind tradition is a different author, very likely
  D.H.M. Brooks on group minds (unverified).

## Bearing on the record

For the Minsky–Schwitzgebel bridge this is the **decomposition side**, made
concrete. It shows that a whole can pursue several goals, switch between
them and degrade gracefully, with no part holding a model, a goal list or
control. That is an existence proof at insect scale for Minsky's thesis
that mind-like behaviour needs no mind-like part.

Against [NOTE-131](NOTE-131.md)'s numbering it is **neutral on C3, C4 and C5**. It makes
no claim about experience in parts or wholes, and its parts are not minded
at all. Two of its results are still useful to a THEORY on the seam:

- **Goal-directedness without self-representation.** Schwitzgebel counts
  goal-directed responsiveness, self-monitoring and self-representation
  among the materialist marks the United States has. Brooks's Creatures
  have the first with "no explicit representation of goals" and none of
  the others. So the marks come apart, and a criterion for consciousness
  that counts them separately will treat a subsumption robot as a partial
  case.
- **Observer-imputed unity.** Brooks says the unity of the Creature exists
  "in the eye of an observer". A THEORY that treats a composite's unity as
  real, as Schwitzgebel's "entityhood-enough" does, should acknowledge
  this deflationary reading of the same kind of architecture.

**Boundary.** The methodological maxims are an instruction for AI and
robotics practice, so the LIT is flagged `anthology-candidate`. The
anthology's `agents-and-environments` topic could hold it. They are not an
instruction for machine-learning practice as such: the paper predates
learning in these systems, and its learning module is "isolated".

## Limitations

- **Thin evidence.** Three layers on one physical robot and six in
  simulation. Performance is described, never measured or compared, and
  the most ambitious system (fourteen layers) is a plan.
- **Scaling is open by the author's own account.** "How many layers …
  before the interactions between layers become too complex", "how
  complex can the behaviors be" and whether learning is possible are
  posed in §8 and not answered.
- **The no-representation claim depends on a narrow definition.**
  Representations are refused the name because they lack variables, rule
  matching and choice. Brooks concedes that the system's numbers and
  topology could be mapped to a representation. So the claim is about
  *explicit, central, symbolic* representation, which is what the title
  overstates.
- **The evolutionary argument is a timeline.** That evolution spent longer
  on mobility than on reasoning does not show that reasoning is "pretty
  simple" once mobility is solved.
- **Unread sources.** The 1986 architecture paper and Agre & Chapman's memo,
  on which §§5–6 lean, were not read here.

## Open questions

- Does activity decomposition scale past a handful of layers without an
  arbiter? The later behaviour-based robotics literature would answer it.
  None of it is held in the record.
- Is "coherence in the eye of an observer" compatible with the system
  being a real agent in Levin's sense ([LIT-tmpsygq0](../literature.d/LIT-tmpsygq0.md)), or with its being a
  real subject in Schwitzgebel's? The paper gives the deflationary answer
  without arguing against the others.
- Under IIT 3.0, what are the complexes of a subsumption network? The
  answer would test whether the architecture that most closely realises
  the society of mind is, on that theory, one subject, several, or none.
