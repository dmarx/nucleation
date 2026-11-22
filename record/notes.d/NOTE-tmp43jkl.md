---
status: Skimmed
paper: LIT-2235
title: 'Schultz and Spivak — Temporal Type Theory: A topos-theoretic approach to systems and behavior'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Skimmed on 2026-11-22 for LEAD-023 from the arXiv copy (1710.10258v3,
    23 December 2017, a 224-page book): the overview (§1.1) and §8.4
    (systems, components and behavior contracts) read; the construction of
    the topos B (Chapters 2–3), the type theory and its axioms (Chapters
    4–5), the semantics and soundness proofs (Chapters 6–7) and the
    remaining applications of Chapter 8 not read. Quotations checked by
    script.
date: '2026-11-22'
summary: >-
  Behavior types as sheaves on a translation-invariant topos of time
  intervals, with an internal constructive higher-order temporal logic for
  proving behavior contracts of interconnected systems. The overview gives
  behavior types whose compliant pieces do not compose and one, roughly
  monotonic curves, that is the solution set of no differential equation;
  §8.4 composes components' contracts by conjunction with the shared
  latent variables existentially quantified out. The logic is undecidable.
---

# NOTE-tmp43jkl: Schultz and Spivak — Temporal Type Theory: A topos-theoretic approach to systems and behavior

## Contribution

A book: a topos B of behavior types over continuous time, and a temporal
type theory, sound for B, in which properties of interconnected systems are
proved from their components' contracts.

## Key results (parts read)

1. **Behavior types (§1.1).** A behavior type assigns to each time window
   the set of behaviors that can occur over it, with restriction to
   subwindows; it "has composable sections when, for any two overlapping
   time window, behaviors over the first that match behaviors over the
   second can be glued".
2. **Not all compose (§1.1).** For "roughly monotonic" behaviors (f
   increasing between samples at least 5 apart), "Any behavior— if tested
   over a very short time window—will comply with this property, but if one
   glues two compliant behaviors that agree along an overlap, the result may
   not be compliant"; "functions of bounded difference" have no composability
   at all. All are still sheaves "in an appropriate setting".
3. **Beyond differential equations (§1.1).** "there is no differential
   equation whose solution set is the roughly-monotonic curves from Eq.
   (1.1), because two such trajectories f can "cross", but these
   trajectories constitute a perfectly good behavior type in B."
4. **Composing contracts (§8.4.2).** A system of components with contracts
   φᵢ satisfies an outer contract when the conjunction implies it for all
   values of the latent (internal) variables; "The strongest contract Φ′
   satisfied by the system" is the conjunction with the latent variables
   existentially quantified.
5. **Undecidable (§1.1).** "our logic is wildly undecidable".

## Assumptions

Continuous time; a translation-invariant topos built from the interval
domain; constructive (non-Boolean) internal logic.

## Concepts

Behavior type; composable sections; topos B; subobject classifier
("compliant when" truth values); temporal type theory and modalities;
interface, port map, machine, behavior contract; latent variables.

## Bearing on the record

- **QUESTION-379.** Two points. A family of behaviors can be coherent, a
  perfectly good behavior type, and still be the solution set of no system
  in a given class (ODEs): a representability gap of the kind the question
  asks about, relative to a class of realizers. And compliance checked on
  short windows does not compose, the question's local-to-global gap in
  time. Neither touches resources.
- **CLAIM-480** (a parallel). The strongest contract of a composite is
  the components' conjunction with the latent variables existentially
  eliminated, the logical form of this claim's interior elimination.
- **QUESTION-143** (no bearing on its iff). Sheaves over time windows, not
  over causal input histories.

## Limitations

Skimmed: under a tenth of the book read, none of the proofs. Its claim to
be a "big tent" for other temporal logics is stated as belief, not proved.
