---
status: Proposed
promote_when: >-
  A result that derives, from the condition Zurek states (a mutual
  information I(S : F_f) that reaches a plateau near H_S for many disjoint
  fragments) or from a stated strengthening of it, that observers each
  measuring a different fragment obtain the same outcome for the pointer
  observable, in the same basis, without disturbing the system; together
  with the conditions under which the plateau holds and that inference
  fails. A further model in which mutual information plateaus does not
  settle it, since the gap is between the information measure and the
  structure of the joint state, and neither does an interpretive argument
  that redundancy is what objectivity means. A state with a high plateau
  whose fragments do not each determine the pointer outcome, if it is the
  generic case for decoherence dynamics, would defeat the identification.
title: 'In models of decoherence, the information a small fraction of the environment holds about a system rises steeply to a plateau at the system''s entropy H_S, so many disjoint fragments each carry nearly all of it, and this redundancy is high only for the pointer observable; Zurek identifies it with objective existence, many observers learning the pointer state independently and without disturbing the system, though the paper argues and does not prove that a plateau in mutual information gives each observer the same record'
version: 1
tags:
- quantum-foundations
- information-theory
date: '2026-10-27'
source:
- LIT-tmpb4amz
summary: >-
  Zurek (2009), LIT-tmpb4amz, section II and Figs. 2–3, read in
  NOTE-tmpvsoha. Redundancy R_δ = 1/f_δ, the number of disjoint fragments
  each holding (1 − δ)H_S of the information about S, is large for states
  made by decoherence and absent for random states, and peaks sharply at
  the pointer observable. Those are model results the review cites. The
  step from redundancy to objectivity ("Large redundancy implies
  objectivity") is an identification. The later caveat, that mutual
  information alone does not guarantee independently accessible records,
  is not in the paper. Proposed for that step.
---
<!-- inactive-ok-file: THEORY-621 THEORY-tmp08c0w — Proposed or new; neighbouring readings, cited as open -->

# THEORY-tmp0d0qe: In models of decoherence, the information a small fraction of the environment holds about a system rises steeply to a plateau at the system's entropy H_S, so many disjoint fragments each carry nearly all of it, and this redundancy is high only for the pointer observable; Zurek identifies it with objective existence, many observers learning the pointer state independently and without disturbing the system, though the paper argues and does not prove that a plateau in mutual information gives each observer the same record

## Source

Zurek (2009), LIT-tmpb4amz, section II (pp. 2–4), Figs. 2–3 and section III
(p. 5) of the arXiv preprint 0903.5082; read in NOTE-tmpvsoha.

## What was actually shown

**The measures.** ρ_SF = Tr_{E/F}|Ψ_SE⟩⟨Ψ_SE| (eq. 2) and
I(S : F) = H_S + H_F − H_{S,F} (eq. 3), for fragments F that are disjoint
collections of environment subsystems, each "individually accessible to
measurements" with commuting observables (Fig. 1). Redundancy is the number
of disjoint fragments supplying (1 − δ)H_S: R_δ = 1/f_δ (eq. 4, p. 3).

**What could have come out otherwise.** For Haar-random pure states of SE,
fragments smaller than half the environment hold almost nothing, and "such
random states … exhibit no redundancy" (Fig. 2). States produced by
decoherence instead rise "quickly" to H_S at small f_δ (Fig. 2, schematic).
In spin-environment models "the same number of spins suffices to reach the
plateau", so redundancy grows with the number of environment subsystems
interacting with S; in quantum Brownian motion R_δ ≈ s^{2δ} for squeeze
factor s (p. 3). These results are cited from refs. [12]–[16].

**Selectivity.** With Shannon entropies of a specific observable
σ(μ) = cos μ σ_z + sin μ σ_x in a spin model with N = 50, the whole
environment holds information about many observables, but R_{δ=0.1} "is
sharply peaked around the pointer observable: Redundancy is a very
selective criterion" (Fig. 3). A cited theorem [12, 24]: "only pointer
states can be discovered from fractions of E. Other observables … can be
deduced only to the extent they are correlated with the pointer
observable" (p. 5). THEORY-tmp08c0w gives the reason only orthogonal sets
can be copied at all.

**The identification.** "Large redundancy implies objectivity: The state of
the system can be found out indirectly and independently by many
observers, who will agree about their conclusions" (Fig. 2 caption).
Independence is argued from commuting observables: "Observables of
different F's commute – such measurements are independent. Yet, underlying
correlations mean that their outcomes imply the same state of the system,
as if S were classical" (p. 3).

## What this does not say

- **That a mutual-information plateau guarantees independently accessible
  classical records.** The paper infers redundancy from the plateau ("Rapid
  rise and gradual leveling of I(S : F_f), Fig. 2, implies redundancy",
  p. 3) and objectivity from redundancy. It gives no condition on the
  joint state of S and several fragments under which each fragment's record
  determines the same outcome. Its closest step is to note that von
  Neumann mutual information can exceed H_S through global correlations
  (up to 2H_S, Fig. 2; p. 4) and to switch to observable-specific Shannon
  quantities for Fig. 3 (p. 5). The caveat that mutual information alone
  is not enough is the later literature's, not this paper's.
- **That redundancy is derived in general.** It is shown in models cited
  from elsewhere; Fig. 2 is schematic; the mixed-environment claim rests on
  work "in preparation" (p. 4).
- **That the parts are found rather than chosen.** The system–environment
  split and the subdivision of E into accessible subsystems are assumed
  (Fig. 1). Redundancy is relative to that choice.
- **That decoherence suffices for records.** The paper says it does not: a
  completely mixed environment "can still induce decoherence" but is
  "useless" as a channel, and air molecules' records become "effectively
  undecipherable" (p. 4).
- **That objectivity here is the same as fact-hood across observers in a
  relational sense.** Agreement is for pointer observables read from a
  shared medium, with the Born rule assumed in computing the measures
  (p. 6). It is not a consistency result of the kind THEORY-621's
  promote_when asks for.
- **That the measurement problem is solved.** That is the author's verdict
  (p. 9); this finding is the redundancy result and its reading.
