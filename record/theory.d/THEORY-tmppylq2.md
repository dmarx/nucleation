---
status: Active
title: "When implementing an automaton requires reliable, counterfactual-supporting transitions for every formal state, Putnam's construction fails, but any system with a clock and a dial still implements every inputless finite-state automaton, and any system with the right input–output dependencies, an input memory and a dial implements every finite-state automaton with those dependencies, so finite-state automata cannot carry computational sufficiency; combinatorial-state automata are argued, not proved, to escape"
version: 1
tags:
- cognition
- metaphysics
date: '2026-10-16'
source:
- LIT-404
summary: >-
  Chalmers (1996), [LIT-404](../literature.d/LIT-404.md), read in [NOTE-342](../notes.d/NOTE-342.md) from the author's HTML copy.
  The failure of Putnam's construction and the clock-and-dial and
  input-memory theorems are constructive proofs given the definitions, so
  FSA-functionalism "still almost reduces to behaviorism". That a
  combinatorial-state automaton can be implemented only by the right
  fine-grained causal structure is a sketch: the obvious blind construction
  grows by a factor of n per step, and that every construction does is
  asserted. Logically possible false implementations and the
  one-region-per-component condition are left open by the author.
---
<!-- inactive-ok-file: THEORY-043 THEORY-092 THEORY-252 THEORY-tmp4k9ec THEORY-tmpted1p — Proposed; named as related or rival accounts in Connections and prose, not leaned on as settled -->

# THEORY-tmppylq2: When implementing an automaton requires reliable, counterfactual-supporting transitions for every formal state, Putnam's construction fails, but any system with a clock and a dial still implements every inputless finite-state automaton, and any system with the right input–output dependencies, an input memory and a dial implements every finite-state automaton with those dependencies, so finite-state automata cannot carry computational sufficiency; combinatorial-state automata are argued, not proved, to escape

## Source

Chalmers (1996), *Does a rock implement every finite-state automaton?*,
[LIT-404](../literature.d/LIT-404.md) (*Synthese*), read in full in [NOTE-342](../notes.d/NOTE-342.md) from the author's HTML copy;
the typeset text and its page numbers were not checked.

## What was actually shown

**The definition (§3).** A system implements an inputless FSA if there is a
mapping f from physical states onto formal states such that, for every
formal transition P → Q, a physical state p with f(p) = P would cause a
transition to some q with f(q) = Q. The conditionals are strong: they hold
however the system came to be in p. An automaton is a structure of possible
transitions, not a trace of one run.

**Putnam's construction fails (§3).** It fails twice. The actual
transitions are not reliable, since an open system could have been
buffeted elsewhere. And unmanifested transitions are satisfied only
vacuously, read materially; read modally they fail.

**But FSAs are still trivial.**

- *Clock and dial (§4).* Every physical system containing a clock (a
  subsystem that reliably steps through states) and a dial (one that stays
  in whatever state it is set to) implements every inputless FSA. Such an
  automaton is a single unbranching sequence ending in a cycle.
- *Input memory (§5).* With inputs and outputs, Putnam's construction fails,
  since its internal sequence ignores input. But a system with the right
  input–output dependencies, an input memory (a distinct state for every
  input sequence) and a dial implements every FSA with those dependencies.
  A zero-outputter with a recorder implements a primality tester. So
  FSA-functionalism "still almost reduces to behaviorism".

**The escape that is argued (§§6–7).** A combinatorial-state automaton
(CSA) has a vector of components, each in a distinct physical region, and
every recombination of component values must transit correctly. To fake one
blindly, each component must record all the others, so the system grows by
a factor of n per step: for three components and 100 steps, 3^100, about
5·10^47. Brain-sized n reaches the size of the universe "in a fraction of a
second". So "the only physically possible systems that implement a
non-trivial CSA will do so in virtue of having the right sort of
fine-grained causal structure". Without the distinct-region condition the
CSA collapses into its FSA under a disjunctive mapping.

**Searle (§8).** Every system implements a one-state CSA and most a
two-state one, so description is "observer-relative" only in the harmless
sense of choosing among true descriptions. One system can implement two
mind-sufficient CSAs, so mental properties attach to (system, CSA) pairs,
and the Chinese room should have two minds.

**What could have come out otherwise.** The FSA results are theorems given
the definitions and could not. The CSA claim could: a cleverer encoding
that fakes a CSA without the blow-up would refute it.

## What this does not say

- **That CSA implementation is non-trivial for every construction.** §7
  shows the natural blind construction explodes and asserts that any will;
  no proof rules out a cleverer one.
- **That the account is complete.** Chalmers leaves open logically possible
  false implementations and an independence condition that may be too
  strict (one region per component, against pointers or distributed codes).
- **How much counterfactual robustness is required.** "In all (or perhaps
  most) situations" (§3) is semi-formal.
- **That implementing the right CSA suffices for a mind.** That is
  computational sufficiency, which the paper protects and does not argue
  ("only half the story, … the easy half", §9). The two-minds verdict on
  the Chinese room depends on it.
- **That the result is about experience.** Maudlin's challenge to the role
  of counterfactuals in experience is set aside in a footnote.

## Connections

- **The functionalist hypothesis it disciplines.** Putnam's clause that
  every organism is a probabilistic automaton "under some Description" is
  empty by his own admission ([THEORY-tmp4k9ec](THEORY-tmp4k9ec.md)). This result says why an
  FSA-level Description cannot make it bite.
- **The clamp.** [THEORY-252](THEORY-252.md) takes this criterion as given: a voltage clamp
  that removes unexercised branches removes the counterfactuals, and
  dropping counterfactuals would reopen the rock problem.
- **The China brain.** [NOTE-342](../notes.d/NOTE-342.md) observes that Block's machine-table China
  system ([LIT-407](../literature.d/LIT-407.md)) is an FSA with input and output, the formalism shown here
  to be nearly trivial; the neuron-level variant is a CSA. That pairing is
  the reader's.
- **Composition.** [THEORY-043](THEORY-043.md) cites the implementation conditions as
  indifferent to whether a component is a neuron or a person, so nothing in
  functionalism itself forbids nesting.
- **Psychologism.** A recorder-equipped FSA resembles Block's lookup table
  ([THEORY-092](THEORY-092.md)); both make the point that matching input–output behaviour
  fixes little.
- **Searle ([THEORY-tmpted1p](THEORY-tmpted1p.md))** is the secondary target, answered by §8.
