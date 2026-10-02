---
status: Active
status_note: 'read in full 2026-10-02 ([NOTE-tmp5k2kp](../notes.d/NOTE-tmp5k2kp.md)), from the author''s HTML copy, not the Synthese typeset text; worth reading as the standard reply to Putnam''s and Searle''s triviality arguments and as the source of the combinatorial-state automaton (CSA). Its result is real but partial: implementation needs counterfactual-supporting transitions over all formal states, inputless FSAs are trivially implemented by any clock plus dial, FSAs with input are implemented by any system with the right input–output dependencies plus an input memory and a dial, and CSAs escape only because a blind implementation must grow by a factor of n per step. Chalmers leaves two open problems (logically possible false implementations, and an overstrict one-region-per-component condition). For this record it decides which formalism a China-brain argument has to be stated in, and it lets one physical system host two minds.'
title: 'Does a rock implement every finite-state automaton?'
version: 1
history:
- version: 1
  date: '2026-10-02'
  note: >-
    Read in full (the author's HTML copy at consc.net/papers/rock.html,
    headed "Published in Synthese 108:309-33, 1996"; §§1–9, both
    footnotes and the references). Page numbers are not given, because
    the HTML carries none and the Springer text refused automated requests
    with a bot challenge, so the typeset version was not compared.
    Citation checked against Crossref: Synthese 108(3):309–333, September
    1996, DOI 10.1007/BF00413692, sole author David J. Chalmers. The
    brief's citation is right in every detail. `published:` is the first
    of the month: Crossref gives September 1996 and no day. Not held in
    the Anthology of the SOTA: a grep of its literature.d for the DOI, the
    title and "Chalmers" found nothing.
tags:
- cognition
- metaphysics
- mereology
- consciousness
date: '2026-10-02'
published: '1996-09-01'
doi: '10.1007/BF00413692'
first_author: 'Chalmers'
keywords:
- 'implementation'
- 'computational functionalism'
- 'finite-state automata'
- 'combinatorial-state automata'
- 'Putnam triviality argument'
- 'counterfactuals'
- 'Chinese room'
implementations: []
summary: >-
  Chalmers (1996), Synthese 108(3):309–333. Putnam's proof that every open
  system implements every finite-state automaton fails, because
  implementation needs reliable, counterfactual-supporting transitions for
  every formal state. Repaired, it survives only for weak formalisms: a
  clock and a dial implement every inputless FSA, and an input memory and a
  dial upgrade any system with the right input–output dependencies to
  every FSA with them. Combinatorial-state automata, whose states are
  vectors of independently varying components in distinct physical
  regions, put a strong constraint on implementation. That keeps
  computation available as a foundation for the theory of mind.
---
<!-- inactive-ok-file: THEORY-tmp31lxe — Proposed; this note says how the paper bears on that account, and does not lean on it -->

# LIT-tmpb96vr: Does a rock implement every finite-state automaton?

David J. Chalmers (1996), *Synthese* 108(3):309–333. DOI 10.1007/BF00413692.
Author's copy at https://consc.net/papers/rock.html.

## Key takeaways

- **Putnam's argument** (Representation and Reality, 1988, appendix):
  every ordinary open system realises every inputless FSA, by mapping
  disjunctions of its successive maximal states onto the formal states.
- **What it gets wrong** (§3). Implementation needs *strong* conditionals:
  if the system were in a state mapped to P, it would go to one mapped to
  Q, however it got there. That has to hold for *every* transition in the
  table, including those not run. Putnam's construction captures one
  trace, not the automaton.
- **What survives** (§§4–5).
  - Any system with a *clock* and a *dial* implements every inputless FSA.
    So inputless FSAs are the wrong formalism for a mind.
  - Any system with the right input–output dependencies, an *input
    memory* and a dial implements every FSA with those dependencies. A
    zero-outputter so equipped implements a primality tester. With FSAs as
    the formalism, functionalism "still almost reduces to behaviorism".
- **Combinatorial-state automata** (§6). A state is a vector of
  substates. Each component must be realised in a distinct physical
  region, and each transition rule must hold as a strong conditional over
  the components. That demands fine-grained causal structure few systems
  have. A blind Putnam-style implementation must grow by a factor of n per
  step and outruns the universe within a fraction of a second of brain
  time (§7). FSAs, Turing machines, cellular automata and programs all
  translate into CSAs.
- **Open problems** (§7). Astronomically large false implementations remain
  logically possible, and a uniformity or causal-relevance clause is left
  as a challenge. The one-region-per-component condition may be too
  strict, for instance for virtual memory.
- **Searle** (§8). Computational descriptions are not observer-relative in
  any way that threatens vacuity. A system implements many automata, and
  whether it implements a given complex CSA is objective. A system running
  two AI programs would host two minds, so minds belong to (system, CSA)
  pairs. In the Chinese room there are two CSAs and "we should expect two
  distinct minds".

## Standing in the record

Filed on 2026-10-02 at the owner's request, with the other Chalmers works,
for its bearing on Block's China brain ([LIT-tmpc6np5](LIT-tmpc6np5.md)) and on
[THEORY-tmp31lxe](../theory.d/THEORY-tmp31lxe.md). [NOTE-tmp5k2kp](../notes.d/NOTE-tmp5k2kp.md) is the close reading. **Active**: it is the
reference account of implementation that later work on computational
individuation starts from. Its main limitations are ones Chalmers states
himself.

**Primary subject left unsaid by the vocabulary.** The paper is about
*computation*: what it is for a physical system to implement an abstract
automaton, and whether that relation is trivial. The vocabulary has no
word for it. `cognition` is justified, because the paper's stated aim is
to secure the computational foundation of cognitive science. `metaphysics`
fits the realisation question, and `mereology` the decomposition of a
system into independent components and the individuation of two minds in
one hunk of matter. But none of the four is the paper's subject.
`mathematics` would stretch a neighbour: the automata theory is used, not
studied. This is a gap to close by decision, not by these tags.

**On Block's China brain ([LIT-tmpc6np5](LIT-tmpc6np5.md)).** Chalmers does not discuss
Block's 1978 paper; he cites only Block's 1981 "Psychologism and
behaviorism", for the lookup table. But his account decides what the China
system implements, and the answer is sharper than "yes".

- Block's homunculi each execute one quadruple of a machine table, and
  the current machine state is shown on a card or by satellite
  ([NOTE-tmpxt8ou](../notes.d/NOTE-tmpxt8ou.md)). That system implements an FSA *with input and output*,
  whose states are monadic. Chalmers's §5 shows that this formalism is too
  weak to carry a mind. Anything with the right input–output dependencies,
  an input memory and a dial implements every FSA with those
  dependencies. So, on Chalmers's terms, Block's machine-table China
  system makes a weaker case against functionalism than it appears to: a
  thesis of computational sufficiency stated for FSAs is close to
  behaviourism already.
- The version Block sets aside in n. 17, a billion people each simulating
  one neuron, is the one that implements a *CSA*. Each person is a
  distinct physical region carrying one component. The radio links carry
  the strong conditionals, if they are reliable. On Chalmers's account a
  nation so organised implements the brain's CSA. Whether it has a mind
  then turns on computational sufficiency, which Chalmers here leaves to
  "the harder part" (§9). That pairing is mine, not the paper's.

**On [THEORY-tmp31lxe](../theory.d/THEORY-tmp31lxe.md).** The account's functionalist premise is that a
whole's mental properties come from how its parts are organised. This
paper is where "organised the right way" gets implementation conditions.

- *A CSA's components are positions, not minds.* The account requires
  only distinct physical regions and reliable dependencies, and is
  indifferent to whether a component is a neuron, a chip or a person. So it
  treats Minsky's mindless agents and Schwitzgebel's citizens alike. It
  supplies no anti-nesting principle.
- *It allows two minds in one system* (§8). Chalmers puts mental
  properties on (system, CSA) pairs. A human who facilitates another CSA's
  dynamics, as in the Chinese room, does not prevent a second mind. He
  expects two. That runs directly against Putnam's and IIT's exclusion
  postulates, and it is the 1996 statement of a nesting-permissive view.
  It is argued from the CSA account plus an analogy to a computer running
  two programs. It is not defended against an anti-nesting principle,
  which the paper does not mention.
- *It does not state [NOTE-131](../notes.d/NOTE-131.md)'s correspondence principle.* The CSA
  account requires complex causal interaction among separate parts. It
  says nothing about whether a system's capacities must come mainly from
  the relations among its subsystems rather than from their own
  capacities. A CSA whose components are humans each doing most of the
  work is still a CSA.

**On the extended mind ([LIT-097](LIT-097.md)).** The paper does not discuss extension.
But its implementation conditions ask only for distinct physical regions
with counterfactual-supporting dependencies, and they let the theorist
"move the boundary inward" (§4) by redescribing inputs. So nothing in them
ties a cognitive system to the skull. That is the computational side of the
parity claim Clark and Chalmers state two years later. The extended-mind
programme being filed alongside this note is where that link would be
tested. The connection is mine; the 1996 paper does not draw it.

**Neighbours.** Dennett's "Real Patterns" ([LIT-220](LIT-220.md)) makes a parallel move
about intentional descriptions: many descriptions of one system, each
objective. Chalmers, French and Hofstadter ([LIT-tmph3vnp](LIT-tmph3vnp.md)) is the earlier
Chalmers paper in the record on AI methodology; it argues for emergent
representation in Copycat and does not touch implementation. It carries no
instruction for machine-learning practice.
