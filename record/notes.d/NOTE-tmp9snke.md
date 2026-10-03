---
status: Read
paper: LIT-tmpumhsc
title: 'The Markov blanket trick: On the scope of the free energy principle and active inference'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read in full: the PhilSci-Archive preprint (eprint 18831), §§1–5,
    Figures 1–3 by caption, footnotes 1–20 and references. Equations
    (1)–(20) were followed in the text layer; the derivation is a summary
    of Friston 2019, Friston et al. 2020 and Ramstead et al. 2020a, which
    were not read. Page numbers are the preprint's. The journal version was
    not seen.
date: '2026-10-03'
summary: >-
  The FEP is true of things defined its way, but its scope is limited: a
  Markov blanket fits only some things, is placed where the model needs it,
  and cannot represent relational properties or a boundary the system
  makes. Its real job is to give any system the partition variational Bayes
  requires. Active-inference models smuggle perception and action into
  hand-built generative models. A conceptual critique; no new formal result
  and no data.
---
<!-- inactive-ok-file: THEORY-tmpnd5gh — Proposed; named as the THEORY filed for this note's candidate, nothing here rests on it -->
<!-- inactive-ok-file: LIT-536 — Deferred, unread; named for the autonomy tradition it systematises, not leaned on -->
<!-- inactive-ok-file: LIT-tmpghan1 LIT-tmpp3m1q — Deferred; cited by this paper for coupled oscillators measured by relative phase, not leaned on -->

# NOTE-tmp9snke: The Markov blanket trick: On the scope of the free energy principle and active inference

## Contribution

A scope argument, distinct from the unfalsifiability and map–territory
critiques. It accepts the FEP's derivation, then asks what the derivation
needs: a NESS and a blanket. It argues that the blanket, not the dynamics,
does the work, that it is chosen rather than found, and that it is chosen
because it is what makes Bayesian inference applicable. It adds a separate
argument against active inference as a process theory of perception and
action.

## Key insight

Variational inference needs three kinds of variable: hidden, observed, and
the system's own. A Markov blanket partition delivers exactly those three
for any system you apply it to. So applying it turns any system into a
Bayesian inferrer by construction; that is a modelling move, not a
discovery about the system.

## Assumptions

- **The FEP as currently formulated** (Friston 2019; Friston et al. 2020):
  ẋ = f(x) + ω (Eq. 1); Fokker–Planck with NESS solution f = (Q − Γ)·∇ℑ,
  ℑ = −ln p (Eqs. 2–3); blanket partition (Eqs. 4–5); flows of autonomous
  states as gradients on particular surprisal (Eqs. 6–7); internal states
  parametrising q_μ(η) (Eqs. 8–11); F = D_KL + ℑ(π) ≥ ℑ(π) (Eqs. 12–17);
  flows on F (Eq. 18).
- **Empirical evidence for the FEP is out of scope** and called "at best,
  scarce" (§1).
- **No "Hegelian argument":** the authors do not argue against the FEP as a
  research programme.

## Key results

- **FEP holds given its commitments (§2, p. 17).** Three commitments: a
  NESS; a blanket making internal states conditionally independent of
  external ones; and, combining them, surprisal minimisation readable as
  variational inference under a generative model "provided by the NESS of
  the thing".
- **§3.1 Every thing.** Candle flames have no stable states to be blanket
  states (Friston 2013, 2019), though they are things; blankets whose states
  "wander away" (Friston 2019, p. 50) are not handled; so clouds and groups
  are doubtful. The FEP is "not a principle for a theory of everything".
- **§3.2 Placement.** Brain (receptors as blanket), bacillus (membrane and
  cytoskeleton), coupled pendulums (beam as blanket; velocity sensory,
  position active, after Kirchhoff et al. 2019): "the Markov blanket
  partition is stipulated as being located exactly wherever happens to be
  convenient". Formally the system x includes η, so the "thing" is
  organism-plus-environment; nested blankets do not help the pendulums,
  already explained by relative phase.
- **§3.3 Outside the blanket.** Relational properties: taller-than, heading
  (Fajen & Warren), affordances (step height to leg length, Warren 1984);
  redefining affordances as action-selection preferences is "a good
  demonstration of FEP's inability to capture relational properties".
  Constitutive self-organization: membranes are produced by cells; receptors
  are not produced by brains, nor beams by pendulums; footnote 17 on
  Friston 2013's particles.
- **§3.4 Fundamentality.** Deriving physics from the FEP is matched by
  Jaynes's MaxEnt and Wolfram's hypergraphs, which share the lack of
  empirical yield.
- **§3.5 The trick.** Why blankets and not, say, causal blankets (Rosas et
  al. 2020)? Because blankets give the variational-inference structure.
  Historically F came first (Helmholtz machine, Hinton & van Camp, Dayan &
  Abbott 2001), the FEP after; the real logic runs from "model it as an
  autoencoder" to "therefore FEP holds".
- **§4 Active inference.** With a T-maze generative model (Eqs. 19–20, after
  Friston et al. 2017 and Hesp et al. 2021), the A, B, C matrices, and even
  their dimensions, encode the experimenters' rationalisation of the task;
  the cue's perception and the movements' control are assumed. Deriving
  priors from the NESS makes "hidden" states not hidden in x.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Given its commitments the FEP is true | stated | the authors' own summary of the derivation (§2) |
| C2 | Markov blankets apply only to some things (not candle flames, doubtfully to clouds or groups) | moderate | FEP literature's own exclusions; argument §3.1 |
| C3 | Blanket placement follows modelling convenience, not the system | moderate | three examples compared (§3.2) |
| C4 | The blanket formalism cannot represent relational properties or constitutive self-organization | moderate | examples and argument §3.3; footnote 17 on Friston 2013 |
| C5 | Blankets are adopted because they supply variational inference's partition | moderate as an interpretation | historical priority of F; structural parallel (§3.5) |
| C6 | Active inference presupposes perception and action rather than explaining them | moderate | analysis of one generative-model example (§4.2) |

## Concepts

- **Thing.** In the FEP, a random dynamical system with a NESS and a Markov
  blanket; the authors italicise it to keep it apart from things in general.
- **Particular states.** Internal and blanket states; autonomous states are
  internal and active.
- **Markov blanket trick.** Using the blanket partition to make any system
  modellable as variational inference, by analogy with the
  reparameterization trick.
- **Constitutive self-organization.** A system producing the boundary that
  distinguishes it from its environment.

## Connections

Builds on Biehl, Pollock & Kanai (2021), Andrews (2020), van Es (2020),
Bruineberg et al. (2020; [LIT-tmpxq8pk](../literature.d/LIT-tmpxq8pk.md)), Chemero's radical embodied
cognitive science and ecological psychology (Gibson; Warren). Its foil
includes Kirchhoff et al. 2018, Ramstead et al. 2018–2020, Friston 2013
([LIT-526](../literature.d/LIT-526.md)) and 2019. It uses HKB ([LIT-tmpp3m1q](../literature.d/LIT-tmpp3m1q.md); read through [LIT-tmpw3fkg](../literature.d/LIT-tmpw3fkg.md))
as the explanation that makes a blanket idle for pendulums.

## Bearing on the record

- **[LIT-526](../literature.d/LIT-526.md).** C4 via footnote 17 is the basis of the LIT's narrow
  `corrects` (the autopoiesis claim). C2 accepts [LIT-526](../literature.d/LIT-526.md)'s flame claim and
  uses it against the FEP's scope.
- **Organisational closure ([LIT-tmpksq6n](../literature.d/LIT-tmpksq6n.md); [LIT-tmp9gfzl](../literature.d/LIT-tmp9gfzl.md); [LIT-536](../literature.d/LIT-536.md)).** The
  constitutive self-organization the paper says blankets miss is the
  organizational school's subject; the paper cites autopoiesis rather than
  closure of constraints.
- **THEORY filed** as [THEORY-tmpnd5gh](../theory.d/THEORY-tmpnd5gh.md) (shared with [LIT-tmpxq8pk](../literature.d/LIT-tmpxq8pk.md)): a Markov-blanket
  partition presupposes rather than discovers a system's boundary.
- **[LIT-tmpe0pw4](../literature.d/LIT-tmpe0pw4.md) (Sophisticated Inference)** is open to C6 as stated.
- No instruction for machine-learning practice.

## Limitations

- Conceptual throughout; no model is built to show a relational property or
  a self-produced boundary escaping a blanket description.
- The FEP's derivation is summarised from secondary formal sources; the
  formal problems of Biehl et al. are reported, not used.
- The active-inference critique rests on one family of discrete-state
  examples.

## Open questions

- Can a blanket formalism with time-varying blanket states (Ramstead et al.
  2020a, noted in footnote 14) represent a self-produced membrane?
- Would causal blankets (Rosas et al.) or closure of constraints serve the
  same modelling role without the inferential reading?
