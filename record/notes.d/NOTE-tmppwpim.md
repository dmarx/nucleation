---
status: Read
paper: 'LIT-tmpvyqe9'
title: 'Combining contextuality and causality'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from the published version of record (Phil. Trans. R.
    Soc. A 382:20230002), as the Europe PMC full-text JATS XML for
    PMC10822710 with its MathML rendered to text, and the two table
    images (the GHZ support table of §3b and the Kahn–Plotkin terminology
    table of §4e) from the PMC page: abstract, §§1–9, footnotes and the
    reference list. Propositions 4.1, 4.4, 7.1 and 8.1 followed;
    Examples 7.2 and 7.3 worked through by hand; the GHZ parities and the
    Anders–Browne choice C_{a⊕b} checked against the table. The arXiv
    versions were not compared with it. The extended version and the
    sequel it promises, and the cited works [10]–[13] on simulations
    between empirical models, were not read.
date: '2026-10-09'
summary: >-
  Extends sheaf-theoretic contextuality to causal scenarios by an
  enabling relation on measurements and a game reading: Nature's
  deterministic strategies, which may depend on causal history, replace
  the event sheaf, and the Abramsky–Brandenburger definitions then go
  through. Recovers flat contextuality and causal Bell scenarios, and
  expresses adaptive MBQC by Experimenter strategies. The strategy
  presheaf is not a sheaf: compatible deterministic local strategies can
  have no gluing or several.
---

<!-- inactive-ok-file: LIT-813 — Superseded; the withdrawn causal sheaf paper this one builds on and claims to recover -->
<!-- inactive-ok-file: THEORY-171 — Proposed; cited for the result this reading gives a second instance of -->
<!-- inactive-ok-file: CLAIM-037 CLAIM-038 CLAIM-100 — Proposed; open, and cited as open: the claims this reading bears on -->

# NOTE-tmppwpim: Combining contextuality and causality

## Contribution

The paper gives one framework for contextuality under three kinds of
causal structure: a causal order in the physical background, an order in
which an experiment's measurements are made, and adaptive choice of
measurement in measurement-based computation. Earlier causal refinements
(Mansfield's ordered measurements, Gogioso and Pinzani's ordered Bell
sites, [LIT-813](../literature.d/LIT-813.md)) handled one order at a time over Bell or Leggett–Garg
scenarios. Here the enabling relation can depend on outcomes, the
scenario need not be Bell-type, and the roles of Nature (causal
background) and Experimenter (adaptivity) are separated. It also shows
that once causality enters, the deterministic layer is no longer a
sheaf.

## Key insight

Change only the sheaf of events. Replace "a section assigns each
measurement an outcome" with "a strategy assigns each measurement an
outcome given the history in which it is performed". Every later
definition (empirical model as a compatible family of distributions,
noncontextuality as a global section, the classical polytope) is then
the old one applied to the new presheaf. Signalling from the causal past
becomes part of what a classical model may do, so it no longer counts as
contextuality.

## Assumptions

- Finite sets of measurements and outcomes for the polytope and the
  fixed-point description of histories.
- Each measurement occurs at most once in a history (histories are
  consistent event sets).
- Nature's strategies are deterministic and total; probabilities enter
  only by composing with the distribution monad D_R over a semiring R
  (non-negative reals for probability).
- The cover still decides which measurements can be performed together;
  causal structure decides in what order and on what condition (§6a).

## Key results

- **Histories** H(M): the least set of consistent event sets containing
  ∅ and closed under s ⊳ x (x not yet performed, some t ⊆ s with t ⊢ x),
  for every outcome of x. For finite X it is reached at a finite stage.
- **Proposition 4.1 (monotonicity).** A strategy's outcome for x is
  fixed at the minimal histories enabling x, and so the same along any
  chain above them. It may still differ between incomparable causal
  pasts.
- **Proposition 4.2.** Strategies are maximal: σ ⊆ τ implies σ = τ.
- **Propositions 4.3–4.5.** Restriction σ|_U = σ ∩ H(M_U) is a strategy,
  and strategies form a presheaf Γ on P(X).
- **§5.** An empirical model is a compatible family in D_R Γ over a cover;
  it is causally noncontextual when it extends to a global distribution
  on Γ(X). Noncontextual models are the convex hull of deterministic
  strategies, so classicality is a linear program, and a causal
  contextual fraction is suggested, not defined.
- **§6a.** If ∅ enables everything, Γ is in bijection with the event sheaf
  E and the theory is [LIT-016](../literature.d/LIT-016.md)'s.
- **§6b.** For the two-site chain ω₁ < ω₂ with the Bell cover, a strategy
  is a pair of functions I_A → O_A and I_A × I_B → O_B, matching
  Gogioso and Pinzani's sheaf of sections. The general GP case is
  asserted, with proof deferred.
- **Proposition 7.1.** The union of a compatible family of strategies is
  deterministic.
- **Example 7.2 (no gluing).** X = {x, y, z}, ∅ ⊢ x, ∅ ⊢ y,
  {(x,0)} ⊢ z, {(y,0)} ⊢ z, cover {x, z}, {y, z}. The strategies
  answering z = 0 after x = 0 and z = 1 after y = 0 are compatible (z is
  never enabled within {z}) and each is total, but any global strategy
  must contain {(x,0),(y,0)} and then answer z both ways.
- **Example 7.3 (non-unique gluing).** With {(x,0),(y,0)} ⊢ z, z is
  enabled in neither member of the cover, and the gluing leaves its
  value free. The authors call this pathological.
- **Note added in proof.** For covers of causally secured sets the
  sheaf property holds; details are deferred to a sequel.
- **Proposition 8.1 and E-strategies.** Maximal histories are those with
  no accessible measurement. An Experimenter strategy is down-closed and
  co-total, accepting every outcome of each measurement it allows, and
  ⟨σ | τ⟩ = σ ∩ τ plays it against a Nature strategy. The Anders–Browne
  OR gate is the E-strategy that measures C_{a⊕b} after A_a and B_b on
  GHZ; the GHZ parities XXX = +1 and XYY = YXY = YYX = −1 make the XOR
  of the three outcomes equal a OR b. Chaining two gates needs a choice
  of measurement that depends on outcomes, which is full adaptivity.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Replacing the event sheaf by the presheaf of Nature's strategies extends sheaf-theoretic contextuality to causal scenarios without changing its definitions | strong (construction) | §§4–5, Propositions 4.3–4.5 |
| C2 | The flat theory is the case where everything is initially enabled | strong (proof sketch) | §6a |
| C3 | Gogioso and Pinzani's causal Bell theory is a special case | moderate | §6b: two-party case worked; the general case deferred |
| C4 | Compatible deterministic strategies need not glue, and need not glue uniquely | strong (counterexamples) | Examples 7.2, 7.3, checked here |
| C5 | On causally secured covers the strategy presheaf is a sheaf | not supported here | note added in proof; deferred to a sequel |
| C6 | Adaptive MBQC is an Experimenter strategy played against a flat model | strong for the one-gate case | §§3b, 8a |
| C7 | The framework also covers Leggett–Garg and classical causal networks | not supported here | §9: deferred to an extended version |

## Concepts

- **causal measurement scenario** M = (X, O, ⊢): measurements, outcomes,
  and an enabling relation from consistent event sets to measurements.
- **history**: a consistent set of events reachable from ∅ by performing
  enabled measurements; a play of the game.
- **N-strategy**: a down-closed, deterministic and total set of
  histories; a hidden variable that may depend on the causal past.
- **E-strategy**: a down-closed, co-total set of histories; an adaptive
  measurement protocol.
- **causally secured context**: one that can occur on its own, its
  measurements' causal prerequisites included (used informally in §3a and
  the note added in proof).
- **causal contextuality**: an empirical model on D_R Γ with no global
  section.

## Connections

The base is Abramsky and Brandenburger ([LIT-016](../literature.d/LIT-016.md)). The Bell-scenario
special case is Gogioso and Pinzani 2021 ([LIT-813](../literature.d/LIT-813.md)), cited as [24]; that
paper was withdrawn by its authors in April 2024, after this one
appeared, and replaced by their trilogy ([LIT-800](../literature.d/LIT-800.md), [LIT-808](../literature.d/LIT-808.md), [LIT-788](../literature.d/LIT-788.md)). This
paper's claimed equivalence with "the sheaf of sections" of [24] stands
on the two-party example only, and the withdrawal concerns [24]'s
locale of inputs, not that example. The trilogy's corrected treatment
([LIT-808](../literature.d/LIT-808.md)) also finds that causal functions are not always a sheaf. The
contextual fraction it proposes to generalise is [LIT-265](../literature.d/LIT-265.md); the cohomology
it lists among the framework's tools is [LIT-277](../literature.d/LIT-277.md) and [LIT-278](../literature.d/LIT-278.md).
Contextuality-by-Default ([LIT-777](../literature.d/LIT-777.md)) is contrasted, not used: CbD treats
signalling as uncharacterised, while this paper declares the causal
background and allows signalling only from the causal past.

## Bearing on the record

- **[THEORY-171](../theory.d/THEORY-171.md)** (context-dependent causal constraints make deterministic
  causal assignments fail to glue). Example 7.2 is a second, independent
  instance in a different formalism: the measurement z has two
  incomparable causal pasts, as event B does in [LIT-808](../literature.d/LIT-808.md)'s Θ₃, and two
  locally causal answers cannot be joined. It also adds a case
  [THEORY-171](../theory.d/THEORY-171.md) does not state, non-unique gluing (Example 7.3), which
  [LIT-808](../literature.d/LIT-808.md)'s causal functions cannot show, being separated. The two
  remedies differ: Gogioso and Pinzani restrict the space (tightness),
  this paper the cover (causally secured sets, unproved here). [THEORY-171](../theory.d/THEORY-171.md)
  could cite it as further support.
- **[CLAIM-038](../claims.d/CLAIM-038.md)** ("a further kind of non-gluing"). The same point: here
  the obstruction is in the causal structure of the contexts, with no
  probabilities involved.
- **[CLAIM-037](../claims.d/CLAIM-037.md)** (formal contextuality needs Contextuality-by-Default when
  marginals shift with context). This paper is a second route. When the
  shift can be attributed to a declared causal order, signalling from the
  causal past is part of the classical model, and the sheaf criterion
  applies to the relaxed no-signalling conditions. CbD is needed when the
  signalling cannot be so characterised, which is the paper's own
  description of the difference. For language, the subject-to-verb
  influence that makes Wang et al.'s corpus models signalling
  ([LIT-tmp9rgb4](../literature.d/LIT-tmp9rgb4.md)) is the kind of thing a declared order could absorb.
  Wang and Sadrzadeh's causal analysis of ambiguous phrases (EPTCS 394,
  not held) takes the Gogioso–Pinzani route.
- **[CLAIM-100](../claims.d/CLAIM-100.md)** (extending sheaf contextuality to directed transport
  between scenarios whose covers change is the open problem). Partial
  prior art, like [LIT-808](../literature.d/LIT-808.md)'s: an E-strategy makes which context is
  measured depend on earlier outcomes, and playing it against a model
  yields a model. But both stay inside one scenario; the paper builds no
  map between empirical models on different scenarios. The works it
  lists on simulations between contextual systems (Karvonen 2019,
  Abramsky, Barbosa, Karvonen and Mansfield 2019, Barbosa, Karvonen and
  Mansfield 2021) define maps between empirical models on different
  scenarios. They are the nearer test of [CLAIM-100](../claims.d/CLAIM-100.md)'s `defeated_if`, and
  are not held.
- No instruction for machine-learning practice; nothing for the
  anthology.

## Limitations

- A short paper: the general equivalence with Gogioso and Pinzani's
  theory, the Leggett–Garg and causal-network cases, the sheaf property
  for good covers and a Vorob'ev-type theorem are all deferred.
- No new quantum example of causal contextuality is computed; the
  examples illustrate the definitions.
- The causal contextual fraction and a logical characterisation of the
  polytope's facets are posed, not given.
- "Causally secured" is used without a formal definition.
- Its cited Bell-scenario predecessor ([LIT-813](../literature.d/LIT-813.md)) was later withdrawn, so
  the special-case claim of §6b now points at a superseded paper.

## Open questions

- Question 7.3: which covers make Γ a sheaf? The authors report a
  positive answer for causally secured covers, unpublished here.
- How the cover condition relates to Gogioso and Pinzani's tightness
  ([LIT-800](../literature.d/LIT-800.md), [LIT-808](../literature.d/LIT-808.md)): whether one implies the other.
- Whether Experimenter adaptivity can ever create contextuality that the
  flat model lacks. In the Anders–Browne case the model Nature plays is
  the ordinary GHZ model.
