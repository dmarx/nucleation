---
number: 352
status: Read
formerly:
- NOTE-tmpex347
paper: LIT-402
title: 'K-Lines: A Theory of Memory'
version: 1
history:
- version: 1
  date: '2026-10-01'
  note: >-
    Read in full from MIT AI Memo 516 (June 1979), the DSpace scan (hdl
    1721.1/5739), OCR'd with Tesseract: cover and abstract, body (pp. 2–17
    of the memo's numbering), Notes 1–12 and the twelve references. The
    ASCII figures (the P-pyramid, the level band, the K-pyramid against
    the P-pyramid, the G–K–P example) survive only as fragments; their
    content is restated in the surrounding prose. The Cognitive Science
    version (4(2):117–133, 1980) was not reachable (Wiley and the Elsevier
    DOI both returned 403 behind a bot check), so differences between memo
    and journal text, if any, are unknown.
date: '2026-10-01'
summary: >-
  Memory as reinstatement: a K-line, attached on a memorable event to the
  agents then active, later re-imposes that partial mental state. The
  level-band principle limits it to an intermediate band of levels, so the
  present is seen as an instance of the past without re-imposing the old
  answer. K-lines build on earlier K-lines into a K-pyramid against the
  perceptual P-pyramid; cross-exclusion makes conflicting details cancel
  into abstraction; learning needs a third, goal-holding net. A programme
  statement: no simulation, and the P→K link is left unspecified.
---
<!-- inactive-ok-file: LIT-385 — Deferred; Damasio's retroactivation proposal, named as a parallel the reader drew, not leaned on -->

# NOTE-352: K-Lines: A Theory of Memory

## Contribution

The memo replaces the store-and-retrieve picture of memory with
reinstatement. To remember is to reactivate some of the agents that were
active when something worked. It adds the three constraints that make this
more than a slogan:

- **Level band.** Reactivate only an intermediate band of levels.
- **Recursion.** Attach mainly to earlier memories.
- **Control.** Let a third agency decide what is memorable.

It also offers a distributed reading of frames.

## Key insight

A memory should make you *approach* the present the way you approached a
past success. It should not make you *see* the past again, and it should not
hand you the old conclusion. A K-line therefore sets the middle of the
processing hierarchy. Low levels stay free to report what is actually there,
and high levels stay free to pursue the current goal. Partial
reinstatement in that band is what turns recall into analogy.

## Assumptions

- **Society of Mind.** The mind is many partially autonomous agents in large
  "Divisions". In the simplest version each agent is active or quiet, a
  total mental state is the set of active agents, and a partial state fixes
  only some of them.
- **Mostly upward flow.** Agents take inputs from below or the side and send
  outputs up or sideways, so information moves "only upwards, on the whole".
  Seen from any agent, this gives a "P-pyramid", which is "an illusion of an
  agent's perspective".
- **Cross-exclusion groups.** Mutual inhibition within small groups means
  that forcing one member on resets the group, and a forced state persists.
  This is built-in short-term memory, seen from outside as "dispositions".
- **Neocortex only.** The theory is meant to cover the common properties of
  neocortex, not the brain at large (Note 6).
- **No neurological detail is claimed.** It is "just another form of
  information processing theory, emphasizing control structure and data
  flow" (Note 4).

## Key results

These are proposals, stated as principles. There are no proofs and no
simulations.

- **K-node assignment and K-line attachment.** When a part G declares a
  mental event in P memorable, a new K-node is made. Its K-line makes
  excitatory attachments to every currently active P-agent. No negative
  connections are needed, because cross-exclusion suppresses the rivals
  (Note 7).
- **Level-band principle.**
  - Lower limit: the K-line must not reach far below its level.
  - Upper limit: it must not reach close to its own level.
  - So it spans "only a band of levels somewhere below that of PK". The
    author concedes the upper limit is "much less clear" (Note 9).
- **K-recursion principle.** "Attach the new K-line … to just the
  currently-active K-nodes." K-agents lie near P-agents of the same level,
  and over development the preference shifts from P to K.
- **Crossbar problem.**
  - The answer is sought in the Society of Mind, not in clever coding: if
    most agents need not talk to each other, local crossbars suffice.
  - The scale is a few thousand P-nets of a few thousand agents each
    (Note 10).
  - Sparse random subset codes on shared "M-lines" are offered as a wiring
    economy (Note 10). For example, 10-line subsets of a 100-line bundle,
    after Mooers's Zatocoding and Willshaw, Buneman and Longuet-Higgins.
- **K-knowledge.**
  - Logical: K-lines at the same level combine disjunctively. With "drop
    out" cross-exclusion, conflicts default upward, which the memo credits to
    Papert's theory of Piagetian conservation.
  - Abstract: accumulated instances plus the cancelling of conflicts yield
    "the extraction of common, non-conflicting properties".
  - Procedural: K-lines interacting across levels could partly instantiate
    one frame with others.
- **Learning and reinforcement.** No "simplistic, centralized reward
  mechanism" can suffice, because deciding what is memorable "requires too
  much intelligence". Credit assignment across strategy and tactic time
  scales defeats recency. Minimal learning needs three nets, G, K and P, "in
  which the first controls how the second learns to operate the third".
- **Tacit and explicit knowledge.** In a society theory the puzzle is how
  any knowledge becomes explicit. "Most knowledge stays more or less where it
  was formed, and does its work there." "Self-awareness is a complex,
  constructed illusion."

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The function of a memory is to re-create a partial mental state, not to retrieve a stored description | assertion, framed as a thesis | stated and illustrated (the concert novice and professional); no evidence |
| C2 | Re-activating only an intermediate level band yields analogy: the present seen as an instance of the past | moderate as a design argument | the lower-limit argument is clear; the upper limit is admitted to be "much less clear" (Note 9) |
| C3 | With cross-exclusion, accumulating instances on one K-node produces abstraction by cancelling conflicts | moderate as a mechanism sketch | follows from the stated drop-out rule; not simulated |
| C4 | K-lines with weak lower fringes implement frames with default assignments | moderate | Note 9 gives the correspondence; the upper-fringe half is speculative |
| C5 | Global recency-based reinforcement cannot solve human credit assignment; at least three nets are needed | weak to moderate | argued from multi-time-scale strategies; no model |
| C6 | The crossbar problem needs no general solution, because most agents need not communicate | assertion | follows from the Society of Mind premise, which is assumed |
| C7 | Attitudes and feelings precede propositions in development, and concrete recollection needs the most expertise | assertion | analogy (the concert); no developmental data |

## Concepts

- **Agent.** A unit that recognises configurations of a few associates and
  changes state. In the simplest model it is active or quiet.
- **Partial mental state.** A specification of the states of some agents.
  Compatible partial states can be held at once.
- **P-pyramid.** The hierarchy below a given agent, from its perspective.
- **K-node, K-line.** A memory unit, and its "wire having potential
  connections to every Agent in the P-pyramid".
- **Level band.** The intermediate span of levels a K-line may reach.
- **Cross-exclusion.** Mutual inhibition within small agent groups.
- **K-pyramid.** The K-nodes' structure, mirroring the P-pyramid with
  activity flowing downward. Together they make a local "counterclockwise
  spiral" of computation.
- **Disposition.** "A momentary range of possible behaviors" (Note 2).
- **M-lines.** A shared bundle on which K-lines are simulated by sparse
  random subsets (Note 10).

## Connections

- **Plain Talk.** It extends Plain Talk ([LIT-399](../literature.d/LIT-399.md)), its reference [1].
  It "complements" that paper, maps its c-lines onto K→P connections, and
  cites it for P-net internals and the claim that not all P-nets need to
  communicate.
- **Frames.** It extends the frame memo ([LIT-410](../literature.d/LIT-410.md)), its reference [3],
  with K-nodes as distributed frames and weak lower fringes as defaults
  (Note 9).
- **Named sources.** Papert, for the basic idea and the conservation
  principle. Winston's near-miss learning, whose emphasis links are
  "identified with K-lines to members of cross-exclusion groups", while its
  prevention pointers have no easy equivalent (Note 11). Doyle's
  truth-maintenance in and out flags. Hebb and Marr. Mountcastle on
  excitatory cortical inputs. Miller, for the resemblance to the older
  notion of "redintegration".
- **Jokes memo.** The jokes memo ([LIT-408](../literature.d/LIT-408.md)) cites this paper for partial
  mental states and for the claim that memories are not all "made of the
  same stuff".

## Bearing on the record

- **Re-enactment accounts of memory.**
  - Damasio's convergence zones ([LIT-385](../literature.d/LIT-385.md), Deferred) make recall the
    reconstruction of fragments under feedback from convergence zones.
  - The somatic-marker hypothesis ([LIT-384](../literature.d/LIT-384.md)) re-enacts learned body states to
    bias decisions.

  Both share this memo's re-enactment shape and its dispositions-first
  emphasis. Neither is a K-line theory, and the pairing is mine. A reading of
  [LIT-385](../literature.d/LIT-385.md) should check whether Damasio cites Minsky.
- **Sparse distributed memory.** Note 10's sparse random-subset coding comes
  from the associative-memory line (Willshaw et al. 1969) that sparse
  distributed memory belongs to. The record reads SDM through Bricken and
  Pehlevan ([LIT-269](../literature.d/LIT-269.md), [NOTE-242](NOTE-242.md)). There retrieval is reconstruction by
  similarity of address. Here it is reinstatement of the agents that were
  active. These are different mechanisms with a common coding trick.
- **Consciousness.** "Self-awareness is a complex, constructed illusion" sits
  on the illusionist side of the record's consciousness readings. The memo
  asserts it in one paragraph and does not argue it.
- **Boundary.** No THEORY in the record should rest on this memo. It carries
  no machine-learning practice instruction, and no anthology topic holds it.

## Limitations

- **Half-built, by its author's account.** "This ends the constructive part
  of this essay." The P→K association, how events in P get tied to goals, is
  never specified.
- **Not simulated.** Nothing shows that level-band reinstatement produces
  useful analogy, or that cross-exclusion cancelling produces sensible
  abstraction, rather than mush.
- **Memory only grows.** Connections are only added, never removed. Note 12
  lists possible remedies and settles on none.
- **Neocortex only.** The scope is limited to neocortex (Note 6).
- **No sequence.** Sequential activity is "suppressed" throughout (Note 11).

## Open questions

- What is the P→K connection that relates perceptual events to goals?
- Does reinstating a middle band of a processing hierarchy, in any built
  system, give transfer to new cases without copying old answers? This would
  test C2.
- How are K-lines pruned or revised (Note 12)?

## Corrections

- none to a seeded skim (there was no seed).
- **Citation.** The brief is right that the article is in Cognitive Science
  4(2):117–133 (1980), and right on the memo, AIM-516, June 1979. Crossref
  holds **two** DOIs for the article: the Wiley DOI
  10.1207/s15516709cog0402_1, issued April 1980, and an Elsevier-era DOI
  10.1016/s0364-0213(80)80014-0, issued June 1980. The filing uses the Wiley
  one, the brief's "likely" DOI, which resolves. The DSpace title is
  "K-Lines: A Theory of Memory".
- **Which text was read.** The memo, not the journal article. The journal
  version was not reachable.
