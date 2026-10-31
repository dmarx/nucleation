---
status: Read
paper: 'LIT-tmpj1wfs'
title: 'Rao & Esposito — Thermodynamics of open chemical reaction networks'
version: 1
history:
- version: 1
  date: '2026-10-31'
  note: >-
    Read in full from the arXiv preprint 1602.07257v3 (11 January 2017,
    the version the authors mark as published in PRX 6, 041064), 22 pp.,
    fetched 2026-10-31. The journal version was not compared. Text
    extracted with plain `pdftotext`; the two-column equations came out
    scrambled in places and were reassembled from context; section and
    equation numbers are the paper's. I read the abstract, §§I–VI,
    Appendices A–D, the captions of Figs. 1–4 and the reference list.
    I checked (numpy and sympy, my own script) the bookkeeping
    |S_y| = |λ_b| + |ε| and the deficiency of a mass-action, reversible
    rewriting of CASE-tmpwxags's first construction; that its dissipation
    at steady state equals the emergent-cycle form (eq. 61); and its
    fixed points as the emergent affinity varies.
date: '2026-10-31'
summary: >-
  Builds the nonequilibrium thermodynamics of open, deterministic,
  mass-action networks of reversible elementary reactions on top of the
  rate equations, as stochastic thermodynamics is built on master
  equations. Chemostatting a species either breaks a conservation law or
  opens an emergent cycle; a network with no emergent affinity relaxes to
  a unique equilibrium, and a steady state dissipates the sum of emergent
  currents times emergent affinities. The minimal chemical work to hold a
  network away from equilibrium is a relative entropy of concentrations,
  a nonequilibrium Landauer principle. For complex-balanced networks the
  dissipation splits into a non-negative steady and a non-negative
  transient part.
---
<!-- inactive-ok-file: LIT-tmpkp8vh LIT-tmpejle0 — Deferred; registered from the same exchange, unread, named as neighbours -->

# NOTE-tmp3zcaf: Rao & Esposito — Thermodynamics of open chemical reaction networks

## Contribution

Before this paper the thermodynamics of chemical reaction networks (CRNs)
was either stochastic (master equations, small numbers) or restricted to
steady states. It gives a complete deterministic account for open networks
driven by chemostats whose concentrations may change in time: first and
second laws (eqs. 65, 67–68), a nonequilibrium Gibbs free energy (eq. 70),
the chemical work done by the chemostats (eq. 69), and a bound on the work
needed to create or hold a nonequilibrium concentration distribution
(eq. 83). It ties these to the topology of the network through
conservation laws, emergent cycles and deficiency, which Chemical Reaction
Network Theory had studied as dynamics without thermodynamics.

## Key insight

A chemical network can be held away from equilibrium only by a pathway
that carries chemicals from one reservoir to another while leaving the
network itself unchanged: an **emergent cycle**. Its affinity depends only
on the chemostatted concentrations (eq. 28), and every nonequilibrium
steady state dissipates exactly current times affinity summed over those
cycles (eq. 61). So "something is being produced" is not yet a
thermodynamic fact. What is thermodynamic is which fuel-to-waste
conversions the network catalyses, and how far from equilibrium the
reservoirs are held.

## Assumptions

- **Homogeneous ideal dilute solution** at constant T, p and V; the solvent
  is the heat bath (§II, §III A).
- **Deterministic mass-action rate equations**, J^{±ρ} = k^{±ρ} Π Z^σ^{∇σ±ρ}
  (eq. 4). Species abundances large enough to ignore discreteness.
- **Elementary reactions only, every one reversible**: "all reacting species
  and reactions must be resolved (none can be hidden), and all reactions must
  be reversible" (p. 2). Effective enzymatic kinetics are outside the theory;
  the authors say metabolic networks "require some care" (p. 15).
- **Local detailed balance** k^{+ρ}/k^{−ρ} = exp(−Δ_r G°_ρ/RT) (eq. 50),
  imposed as "a universal property of elementary reactions which holds
  regardless of the network state" (p. 5). "Closed CRNs must be
  detailed-balanced. This statement can be seen as the zeroth law for CRNs"
  (p. 5).
- **Local equilibrium**: equilibration after each reaction event is faster
  than any reaction (§III A).
- **Finite networks.** Infinite-dimensional CRNs "can exhibit long-time
  behaviors different from equilibrium even in absence of emergent cycles"
  (p. 6, citing their ref. 63).

## Key results

- **Broken conservation laws and emergent cycles (§II C–D).** Chemostatting
  turns some conservation laws ℓ of the closed network into broken ones and
  makes some right-null vectors of the internal stoichiometric matrix ∇_X
  emergent cycles c_ε, with |S_y| = |λ_b| + |ε| by rank–nullity (p. 5). This
  is "a topological feature": it depends on which species are chemostatted,
  not on their concentrations.
- **One chemostat never drives (Example 6, p. 6).** "Any CRN with one
  chemostatted species only (|S_y| = 1) is unconditionally detailed-balanced",
  because the first chemostat always breaks the total-mass law.
- **Detailed balance iff every emergent affinity vanishes (p. 6)**, which is
  Wegscheider's condition. A detailed-balanced network relaxes to an
  equilibrium that is "globally stable" and, for given kinetics and
  chemostatting, "unique and depends on the unbroken components only" (p. 5).
- **Entropy production (eqs. 55, 59–61).** T Ṡ_i = RT Σ_ρ (J^{+ρ} − J^{−ρ})
  ln(J^{+ρ}/J^{−ρ}) ≥ 0; at a nonequilibrium steady state T Ṡ_i = Ī^{σy} μ_{σy}
  = J̄^ε A_ε, "which clearly emphasizes the crucial role of emergent cycles in
  steady state dissipation".
- **Nonequilibrium Gibbs free energy (eqs. 74, 77).** G = G_eq + RT L(Z|Z_eq),
  with L the relative entropy of non-normalised concentrations (eq. 75); in a
  closed network d_t G = −T Ṡ_i ≤ 0, so G is a Lyapunov function.
- **Work (eqs. 78–83).** T Ṡ_i = Ẇ_c − d_t G ≥ 0. Integrated,
  W_c − ΔG_eq = RT ΔL + T Δ_i S, so the irreversible chemical work satisfies
  W_c^{irr} ≥ RT ΔL: what the chemostats must supply "to create a
  nonequilibrium distribution from an equilibrium one" (p. 12), a
  nonequilibrium Landauer principle. This holds for any CRN.
- **Complex-balanced networks (§IV, App. C).** For unconditionally
  complex-balanced networks (deficiency zero, App. D) the entropy production
  splits into an adiabatic part (dissipation of the steady state) and a
  nonadiabatic part (relaxation and driving), both non-negative (eqs. 84–87).
  Without driving, L(Z|Z̄) to the complex-balanced steady state is a Lyapunov
  function (eq. 87), and the complex-balanced steady state is "always
  globally stable" (p. 7, citing Craciun's proof of the global attractor
  conjecture). A complex-balanced network therefore has a unique, globally
  attracting steady state however far from equilibrium it is driven.
- **Open detailed-balanced networks (§V).** A transformed Gibbs free energy,
  G minus the energy of the broken components (eq. 90), is the Lyapunov
  function (eq. 93), and a driving-work Landauer bound holds (eq. 103).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Each chemostatted species breaks a conservation law or creates an emergent cycle, |S_y| = |λ_b| + |ε| | strong | rank–nullity, p. 5; checked on Example 5 and on my rewriting of CASE-tmpwxags |
| C2 | A network with one chemostat, or with all emergent affinities zero, relaxes to a unique equilibrium | strong | Example 6; Wegscheider and cited global stability |
| C3 | Steady-state dissipation is Σ_ε J_ε A_ε | strong | eqs. 60–61; checked numerically |
| C4 | The irreversible chemical work to reach a nonequilibrium distribution is at least RT times a relative entropy | strong | eqs. 78–83, derived |
| C5 | Complex-balanced networks have non-negative adiabatic and nonadiabatic entropy production | strong | App. C |
| C6 | The deterministic entropy (eq. 63) is the large-number limit of the stochastic entropy | moderate | App. B, assuming the distribution narrows to a delta |

## Concepts

- **Chemostat** — a reservoir that fixes the concentration of a species;
  "via external reactions ... or via abundant species whose concentrations
  are negligibly affected by the CRN reactions within relevant time scales"
  (p. 3). The second reading is what Remlein, Esposito and Avanzini later
  derive (LIT-tmpgm18n, NOTE-tmp658wp).
- **Emergent cycle** — a reaction combination leaving the internal species
  unchanged and moving chemicals between chemostats (eq. 20); its affinity
  A_ε (eq. 49) is the external force.
- **Moiety** — a part of molecules conserved across reactions; conservation
  laws are often moieties (p. 4).
- **Deficiency** — dim ker ∇_X − dim ker ∂_C (App. D); zero deficiency implies
  unconditional complex balance.

## Connections

The cycle and conservation-law bookkeeping is Polettini and Esposito 2014
(their ref. 56), not held here. Its geometry for hypergraphs is Dal Cengio,
Lecomte and Polettini (LIT-tmpw6f74, NOTE-tmpif2g2); its bounds on what a
given driving can sustain are Liang, De Los Rios and Busiello (LIT-tmpfq9vf,
NOTE-tmp3di1n); the derivation of chemostats inside closed systems is
LIT-tmpgm18n (NOTE-tmp658wp). The stochastic precursor is Seifert's review,
LIT-523, read in NOTE-420; Prigogine's linear-regime thermodynamics, which
the paper "embeds", is THEORY-692. Vellela and Qian (LIT-tmpkp8vh) and
Barato and Seifert (LIT-tmpejle0), registered from the same exchange, are its
neighbours.

## Bearing on the record

- **A13's line "positive production term ⇏ physically realizable maintenance
  mechanism" is right, and the paper makes it exact** (THEORY-tmplh6oa). A
  production term is admissible only as a reversible elementary reaction,
  and sustained turnover needs an emergent cycle with nonzero affinity. I
  rewrote CASE-tmpwxags's first construction that way: fuel S and waste W
  chemostatted, c₂ catalysing S + 2c₂ ⇌ c₁ + 2c₂, c₁ catalysing the
  mirror reaction, and decay c_i ⇌ W, all rate constants 1, [S] = 3. The
  network has two chemostats, one broken conservation law, one emergent cycle
  S → W, and deficiency 2. Its emergent affinity is A = RT ln(3/[W]). At
  A = 0 it has one equilibrium, c = (3, 3), with no current and no extinct
  alternative. It is bistable only for A > 3.52 RT ([W] < 0.0887). As
  [W] → 0, so that A → ∞, its symmetric equilibria are exactly the case's,
  (3 ∓ √5)/2, because c(3 − c) = 1 and 3c/(1 + c²) = 1 are the same
  quadratic. At [W] = 0.01 the maintained state c = 2.620 dissipates
  29.77 (in units of RT times the rate unit), and Σ_ρ J_ρ ln(J⁺/J⁻) and
  J_ε A_ε agree to five figures. So in this rewriting the case's maintained
  organization, with its extinct alternative, exists only above a finite
  fuel-to-waste affinity, and it costs that dissipation per unit time.
- **CLAIM-tmpczfpk: its hypothesis is an infinite-affinity limit.** Local
  detailed balance makes decay reversible, c ⇌ W. With any waste present the
  back reaction is a basal production d′[W] > 0, which the claim excludes.
  Capacities in an acyclic production graph then relax to the level set by
  the waste reservoir, (d′/d)[W], and not to zero. The induction is untouched.
  What changes is its physical reading: "extinction" means relaxation to
  equilibrium with the waste, and the hypothesis holds only to the extent
  that waste is removed or its back reaction negligible. The claim's
  production graph is also not a stoichiometric object (THEORY-tmp05y8u).
- **THEORY-692: a far-from-equilibrium exception, and a topological
  necessary condition.** THEORY-692 follows Cross and Hohenberg in saying no
  Lyapunov potential exists in general "though there are notable
  exceptions". Complex-balanced networks are one: however hard they are
  driven, L(Z|Z̄) is a Lyapunov function and the steady state is unique and
  globally attracting (eq. 87, p. 7). So a chemical dissipative structure,
  order born of an instability, needs a network that is not complex-balanced
  under its driving, and in particular one of nonzero deficiency, since
  deficiency zero forces complex balance (App. D). That is a topological
  sharpening of Prigogine's "autocatalytic steps are necessary but not
  sufficient". It should be added to THEORY-692's connections.
- **CLAIM-273: what a thermodynamic quantity would need.** CLAIM-273 says
  no thermodynamic quantity is defined for r/place. This paper shows what
  defining one takes in chemistry: a stoichiometry, local detailed balance
  tying rates to free energies, and reservoirs. A canvas has none of the
  three, so the claim's restriction to the structural sense stands.
- **TERM-070.** In Montévil and Mossio's closure the paradigm constraint is
  an enzyme: it acts on a process without being consumed by it. A catalyst
  cancels from the net stoichiometric matrix (eq. 2), so the thermodynamic
  account here does not see closure at all. It sees only which fuel-to-waste
  cycles the network runs. Closure is a kinetic and organizational property
  layered on a thermodynamic budget that is indifferent to it
  (THEORY-tmp05y8u).
- **No instruction for machine-learning practice.**

## Limitations

- **Deterministic and well-mixed.** No fluctuations beyond App. B, no
  diffusion, so no patterns.
- **Elementary reversible reactions only.** Michaelis–Menten, Hill and other
  effective rate laws, the forms the record's toy models use, are not
  covered without being resolved into elementary steps.
- **Chemostats are postulated.** Where they come from is LIT-tmpgm18n.
- **Nothing on multistability, oscillation or selection.** Beyond the
  global stability of detailed- and complex-balanced networks, the paper is
  silent on what a driven network does.
- **Equations partly scrambled in extraction**; I checked those I rely on
  against their derivations.

## Open questions

- For the class of production models the record uses, what is the least
  emergent affinity at which a bistable maintained state exists? For the
  rewriting above it is 3.52 RT; a general bound would come from
  Liang et al.'s thermodynamic space (NOTE-tmp3di1n) combined with
  deficiency theory.
- Does the nonequilibrium Landauer bound (eq. 83) give a lower bound on the
  cost of maintaining an organization against a given damage rate?
