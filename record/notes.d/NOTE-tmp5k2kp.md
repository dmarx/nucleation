---
status: Read
paper: 'LIT-tmpb96vr'
title: 'Chalmers — Does a rock implement every finite-state automaton?'
version: 1
history:
- version: 1
  date: '2026-10-02'
  note: >-
    Read in full (the author's HTML copy at consc.net/papers/rock.html,
    headed "Published in Synthese 108:309-33, 1996"). Every section
    (§§1–9), the two footnotes (O'Rourke; Maudlin) and the references were
    read, and the clock-and-dial and input-memory constructions were
    checked step by step. The Springer typeset text was not seen, as the
    site returned a bot challenge, so no page numbers are given and
    differences from print are unknown. Putnam's appendix is quoted as
    Chalmers quotes it.
date: '2026-10-02'
summary: >-
  Implementation needs strong, counterfactual-supporting conditionals for
  every transition in the table, not one run, so Putnam's rock does not
  implement every FSA. Repaired, the triviality result survives for weak
  formalisms. A clock plus a dial implements every inputless FSA. The right
  input–output dependencies plus an input memory and a dial implement
  every FSA with those dependencies. Combinatorial-state automata, with
  independently varying components in distinct physical regions, demand
  fine-grained causal structure, and a blind implementation must grow
  exponentially. Logically possible false implementations and an overstrict
  independence condition are left open. Minds attach to (system, CSA)
  pairs, so the Chinese room holds two.
---
<!-- inactive-ok-file: THEORY-tmp31lxe — Proposed; this reading says how the paper bears on that account, and does not lean on it -->

# NOTE-tmp5k2kp: Chalmers — Does a rock implement every finite-state automaton?

## Contribution

Before this paper, Putnam's 1988 "theorem" and Searle's wall-runs-Wordstar
claim stood as reasons to think implementation is trivial and
computational functionalism vacuous. Chalmers shows where Putnam's proof
fails (it satisfies material, not strong, conditionals, and only for one
trace). He shows how much of it can be rescued (all of it, for formalisms
without combinatorial state), and which formalism resists it: the
combinatorial-state automaton, with an explicit definition of
implementation. That definition became the reference point for later work
on computational individuation.

## Key insight

An automaton is a structure of *possible* transitions, not a sequence of
states. Implementing it means that the causal structure of the system
mirrors that whole structure, counterfactually. When the formal states are
monadic, that structure is thin enough to be faked by a clock, a dial and
a record of inputs. When the states are vectors of independently varying
components, every recombination of component values must also transit
correctly. That constraint cannot be faked by bookkeeping in any system
that fits in the universe.

## Assumptions

- **Putnam's principles, accepted for the argument** (§2): noncyclical
  behaviour (every ordinary system is in a different maximal state at each
  time) and physical continuity.
- **Implementation conditionals are strong** (§3): "if the system were to
  be in state p, then it would transit into state q", however it came to
  be in p. Chalmers says this is not a Lewis similarity counterfactual but
  a lawfulness requirement.
- **Discrete time** (§4), "nothing will depend on this".
- **Computational sufficiency** (§1): there is a class of automata any
  implementation of which has a mind. It is the thesis being protected,
  not argued for. Its defence is deferred to Chalmers 1994b (§9).
- **One region per component** (§6): each component of a CSA state vector
  corresponds to a distinct physical region. This is stipulated, and §7
  questions it.
- **Physical possibility as the standard** (§7): the CSA account is said to
  give satisfactory results "within the class of physically possible
  systems". Logical possibility is conceded to remain a problem.

## Key results

- **Implementation of an inputless FSA** (§3, revised): a mapping f from
  physical states *onto* formal states such that, for every formal
  transition P → Q, a physical state p with f(p) = P causes a transition to
  some q with f(q) = Q.
- **Putnam's construction fails twice** (§3). The actual transitions are
  not reliable, since an open system could have been buffeted elsewhere.
  Putnam's appeal to boundary conditions "at subsequent times" is
  illegitimate. And unmanifested transitions are not reflected at all:
  read materially they are satisfied vacuously, read modally they are not.
- **Clock-and-dial theorem** (§4). Every physical system containing a clock
  (a subsystem reliably stepping through states) and a dial (a subsystem
  that stays in whatever state it is set to) implements every inputless
  FSA. States [i, j] are assigned run by run, with an infinite clock to
  handle the end of the run. Moral: inputless FSAs are trivial, a single
  unbranching sequence ending in a cycle.
- **FSAs with input and output** (§5). Implementation is defined with
  mappings for inputs and outputs and a strong conditional for every
  transition (I, S) → (S′, O). Putnam's construction fails it, since a
  system whose internal sequence is reliable in itself behaves the same
  for any input. But a system with an **input memory** (a distinct state
  for every input sequence) and a dial implements every FSA with the right
  input–output dependencies. So a zero-outputter with a recorder
  implements a primality tester, and FSA-functionalism "still almost
  reduces to behaviorism". A parenthetical gives a second route there,
  from FSA minimisation and principle (++).
- **CSA implementation** (§6). A system implements a CSA if its internal
  state decomposes into substates [s¹, …, sⁿ], each in a distinct region,
  mapped onto the CSA's substates, so that every formal transition over
  the vectors (with local dependencies where the CSA has them) holds as a
  strong conditional. Finite CSAs are no more powerful than FSAs, but
  their implementation conditions are far more constrained.
- **Blind implementations explode** (§7). To fake a CSA, each component
  must record all previous components, [a, b, c] + I → [abcI, abcI, abcI].
  The size then grows by a factor of n per step. For three components and
  100 steps the factor is 3¹⁰⁰, about 5·10⁴⁷. Systems of brain-like n hit
  the size of the universe "in a fraction of a second". So "the only
  physically possible systems that implement a non-trivial CSA will do so
  in virtue of having the right sort of fine-grained causal structure".
- **The independence condition is needed** (§7). Without distinct regions,
  any implementation of the collapsed FSA implements the CSA under a
  disjunctive mapping, and the CSA's structure is lost.
- **Searle answered, and two minds allowed** (§8). Every system implements
  a trivial 1-state CSA, most a 2-state one, so descriptions are
  "observer-relative" only in the harmless sense of choice among true
  ones. A system can implement two independent mind-sufficient CSAs, so
  mental properties attach to (system, CSA) pairs. The Chinese room holds
  two CSAs, the human brain's and the marks on paper's, and "we should
  expect two distinct minds".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Implementation requires strong, counterfactual-supporting conditionals for every formal transition, not only those exhibited | strong as an analysis; it is a definition, argued from what "implements" must mean | §3, with the trace/structure distinction credited to O'Rourke |
| C2 | Putnam's construction does not satisfy these conditionals | strong | §3, two independent failures |
| C3 | Every system with a clock and a dial implements every inputless FSA | strong, given the definitions (with an infinite clock for the end-of-run states) | constructive proof §4 |
| C4 | Every system with the right input–output dependencies, an input memory and a dial implements every FSA with those dependencies | strong, given the definitions | constructive proof §5 |
| C5 | So FSAs (with or without I/O) are the wrong formalism for computational sufficiency; FSA-functionalism nearly collapses into behaviourism | moderate | follows from C3–C4; the (++) route is an aside |
| C6 | Physically possible implementations of a non-trivial CSA must have the right fine-grained causal structure | moderate | the blow-up argument §7 is a sketch: it shows the obvious blind construction explodes and asserts that "any" will |
| C7 | The CSA account still admits logically possible false implementations and may be too strict about independence | author's concession | §7, left open |
| C8 | Implementation is objective; Searle's observer-relativity threatens no vacuity | moderate | follows from C1 and C6 within physical possibility |
| C9 | One system can host two minds, so minds attach to (system, CSA) pairs, and the Chinese room has two | weak–moderate | analogy to a computer running two programs; presupposes computational sufficiency |
| C10 | Computation can therefore serve as a foundation for the theory of mind | conditional | "only half the story, … the easy half"; whether causal organisation fixes mentality is deferred (§9) |

## Concepts

- **Strong conditional** — a counterfactual "if the system were in p it
  would transit to q", holding however p came about (§3). Distinct from a
  material conditional over the actual run.
- **Trace** — the sequence of states an automaton passes through on one run
  (§3). Putnam implements a trace, not an automaton.
- **Clock** — a subsystem that reliably steps through a sequence of states
  regardless of environment (§4).
- **Dial** — a subsystem with arbitrarily many states that stays in
  whichever one it is put in (§4).
- **Input memory** — a subsystem that goes into a distinct state for every
  possible input sequence (§5).
- **Combinatorial-state automaton (CSA)** — an automaton whose internal
  state is a vector of finitely valued components, with a transition
  function per component (§6).
- **Computational sufficiency** — the thesis that some class of automata is
  such that any implementation has a mind, or a given mental property (§1).
- **(System, CSA) pair** — the bearer of mental properties on §8's
  proposal.

## Connections

Putnam's appendix to *Representation and Reality* is the target, and
Searle's "Is the brain a digital computer?" (1990) the secondary one.
Block's "Psychologism and behaviorism" (1981) supplies the giant lookup
table that a recorder-equipped FSA resembles (§5). Maudlin's "Computation
and consciousness" (1989) is flagged in a footnote as a challenge to the
role of counterfactuals in experience, and set aside. Chalmers's own "On
implementing a computation" (1994a) and "A computational foundation for the
study of cognition" (1994b) are the companion pieces: the second is where
he argues that causal organisation fixes mentality.

In the record, Block's "Troubles with Functionalism" ([LIT-tmpc6np5](../literature.d/LIT-tmpc6np5.md),
[NOTE-tmpxt8ou](NOTE-tmpxt8ou.md)) is the case this paper most directly calibrates, though it
does not cite it. Block's homunculi each execute one quadruple of a
machine table, with the machine state displayed centrally. That is an FSA
with input and output, the formalism §5 shows to be nearly trivial. Block's
n. 17 variant, a billion people each simulating a neuron, is a CSA
implementation, with each person as one region. Schwitzgebel ([LIT-159](../literature.d/LIT-159.md),
[NOTE-131](NOTE-131.md)) does not cite this paper. The extended-mind paper ([LIT-097](../literature.d/LIT-097.md),
[NOTE-180](NOTE-180.md)), two years later, rests on role-functionalism about belief, and
this paper's implementation conditions are compatible with components
outside the skull. Whether the extended-mind programme filed alongside this
reading draws that link is for that reading to say. Dennett's "Real Patterns" ([LIT-220](../literature.d/LIT-220.md))
is a near neighbour on the objectivity of one description among many.

## Bearing on the record

- **[THEORY-tmp31lxe](../theory.d/THEORY-tmp31lxe.md): supports its premise, not its seam.** The account
  takes organisation to be what makes a mind. This paper gives
  "organisation" an implementation-level content, the CSA. That content is
  indifferent to whether a component is a neuron, a module or a person,
  and §8 lets one system host two minds. So it sides with the account's
  diagnosis that nothing in functionalism itself forbids nesting, and it
  offers no anti-nesting principle and no architectural criterion that
  would separate a modular mind from a nation. Neither route of the
  account is strengthened.
- **[LIT-tmpc6np5](../literature.d/LIT-tmpc6np5.md) (Block): a formalism point the record did not have.** The
  machine-table China system implements only an FSA. On this paper's
  analysis FSA-sufficiency is nearly behaviourism, so the China system is
  not the strongest functionalist target. The strong target is the
  neuron-level version Block mentions in n. 17 and where, he reports,
  "intuition seems to founder". That pairing is mine.
- **[NOTE-131](NOTE-131.md)'s correspondence principle is not stated here.** The CSA
  condition requires causal interaction among separate components. It does
  not require that a system's capacities arise mainly from the relations
  among its subsystems rather than from their capacities. The closest the
  paper comes is §5's lesson that a recorder doing all the work trivialises
  implementation. That is about implementation, not about where capacities
  come from.
- No ML instruction; nothing for the anthology.

## Limitations

- **Two problems left open by the author** (C7): logically possible false
  implementations, and an independence condition that may be too strict.
- **The blow-up argument (§7) is a sketch.** It shows that the natural
  blind construction explodes and asserts that "any Putnam-style
  implementation" will. It does not prove that no cleverer encoding avoids
  the explosion.
- **Strong conditionals are left semi-formal.** "In all (or perhaps most)
  situations", "perhaps with some restriction ruling out extraordinary
  environmental circumstances" (§3): how much counterfactual robustness is
  required is not fixed.
- **Only half the story.** Whether implementing the right CSA suffices for a
  mind, or for experience, is not argued here (§9).
- **Read from the author's HTML.** Typos in it ("that" for "than", "area
  therefor", "impleented") suggest it is not the typeset text. Page
  numbers and any print revisions are unchecked.

## Open questions

- What uniformity or causal-relevance clause rules out the logically
  possible false implementations (§7)?
- How far can the one-region-per-component condition be relaxed (pointers,
  virtual memory, distributed codes) without letting in disjunctive fakes?
- Does a neuron-level nation, which on this account implements the brain's
  CSA, have the brain's mental properties? The paper's own §9 says this is
  "the harder part".

## Corrections

- No seeded skim to correct. The brief's citation is right in every detail.
- **A slip in the copy read** (§3): "while failing to be in state b at all
  times between t_n and t_{n-1}" should be t_n and t_{n+1}.
