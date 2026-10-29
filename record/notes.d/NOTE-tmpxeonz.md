---
status: Read
paper: 'LIT-1234'
title: 'Bunin — Ecological communities with Lotka-Volterra dynamics'
version: 1
history:
- version: 1
  date: '2026-10-29'
  note: >-
    Read in full on 2026-10-29 from the published version on the
    author's own Technion page
    (https://phsites.technion.ac.il/bunin/wp-content/uploads/sites/37/2018/08/PhysRevE.95.042414_LV_communities.pdf,
    8 pages, Physical Review E 95, 042414), text extracted with
    pdftotext. Read: the abstract, the introduction, §§I–VI, Appendices A
    and B, the captions of Figs. 1–7 and the 40 references. No number was
    taken from a chart. The UFP–MA boundary σ_c = √2/(1 + γ) for σ_K = 0
    was re-derived from the self-consistency relations (10)–(11) and the
    divergence condition (13) at Δ = 0 (record arithmetic, 2026-10-29),
    and agrees with Fig. 5(b)'s analytic mark σ = 1/√2 at γ = 1. Bunin's
    arXiv:1607.04734 ("Interaction patterns and diversity in assembled
    ecological communities", 2016) was also downloaded and its abstract
    and headings checked: it is a companion paper on the same model, not
    a preprint of this one, as the LIT's version-1 history says.
date: '2026-10-29'
summary: >-
  For generalized Lotka–Volterra dynamics of a community assembled from a
  pool of S species with random interactions of mean μ/S, variance σ²/S
  and symmetry γ, the cavity method gives exact large-S results in the
  phase with a unique uninvadable fixed point: a Gaussian truncated at
  zero for abundances, the fraction of surviving species, and a loss of
  stability at σ = √2/(1 + γ) for equal carrying capacities, independent
  of μ. Beyond it lies a multiple-attractor phase in which the outcome
  depends on history; that phase is located, not solved, and its history
  dependence is shown numerically.
---

# NOTE-tmpxeonz: Bunin — Ecological communities with Lotka-Volterra dynamics

## Contribution

A self-contained cavity calculation for the random generalized
Lotka–Volterra model of a single community fed by migration from a
species pool, without assuming symmetric interactions. It gives the
phase diagram (unique fixed point, multiple attractors, unbounded
growth), the diversity and the abundance distribution in closed form in
the first phase, and a change of variables that shows the fixed points
depend on the parameters only through three combinations, which explains
why the unique-fixed-point boundary is independent of the mean
interaction strength.

## Key insight

Once abundances are normalized by their mean, the fixed-point problem
depends only on u ≈ 1/σ, the symmetry γ and the scaled spread of
carrying capacities σ_λ. Adding one more species to a large community
perturbs the others only by linear response, so the new species sees a
Gaussian field and its abundance is that field divided by a renormalized
self-interaction u − γv, truncated at zero. The unique fixed point stops
being stable when its response to small perturbations diverges; past
that line the community has more than one possible outcome, and which it
reaches depends on its assembly history.

## Assumptions

- Dynamics (1): dN_i/dt = (r_i/K_i) N_i (K_i − N_i − Σ_{j≠i} α_ij N_j),
  noise neglected.
- α_ij = μ/S + σ a_ij with ⟨a_ij⟩ = 0, ⟨a_ij²⟩ = 1/S, ⟨a_ij a_ji⟩ = γ/S;
  otherwise independent, any distribution. K_i independent of α, mean 1,
  Gaussian with variance σ_K² when not identical.
- Large S with μ, σ, γ fixed ("individually weak interactions"). The
  calculation assumes an uninvadable fixed point exists and checks the
  assumption self-consistently; it uses feasibility and uninvadability,
  not dynamical stability, which the author checks numerically
  (Mij* = α*_ij r*_i N*_i / K*_i positive definite in the UFP phase for
  several distributions of r).
- Migration acts on time scales long enough for the community to relax
  between invasions.

## Key results

- **Symmetry (§III).** Fixed points satisfy 0 = n_i(λ_i − u n_i −
  Σ a_ij n_j + h), with n_i normalized abundances, u = (1 − μ/S)/σ,
  λ_i = (K_i − 1)/(σ⟨N⟩) and h = (1/⟨N⟩ − μ)/σ. For equal K_i the
  normalized properties do not depend on μ. These fixed points are those
  of a replicator equation, though the full dynamics differ.
- **Abundance distribution (9).** n = max(0, (h + √(q + σ_λ²) z)/(u − γv)),
  z standard normal: a truncated Gaussian. Self-consistency (10)–(11)
  fixes q = ⟨n²⟩, v, h and the surviving fraction φ. ⟨N⟩ = 1/(σh + μ),
  and unbounded growth begins where σh + μ = 0.
- **Loss of stability (13).** ⟨(δn)²⟩/⟨ξ²⟩ = φ/((u − γv)² − φ), which
  diverges at φ = (u − γv)², equivalently u = (1 + γ)v. For σ_K = 0 this
  is σ_c = √2/(1 + γ) for all μ > 0 (Appendix A). Lower symmetry and more
  variable carrying capacities both move the transition to larger σ.
- **Simulations.** S = 15, 100, 200, 400, 800; the predictions for φ and
  the moments hold at S = 200 in the UFP phase and approximately into
  the MA phase; at S = 15 with communities of about six species the fit
  is still good. The fraction of systems with more than one final
  community jumps at σ_c for large S and is broadened at finite S, with
  unique fixed points found "well inside" the MA phase even at S = 100.
- **MA phase.** For γ = 0 the dynamics may reach non-fixed-point
  attractors and, with an extinction cutoff, may never become
  uninvadable; invasions can switch the community between alternatives.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | In the UFP phase the large-S abundance distribution is a Gaussian truncated at zero | strong | cavity derivation §IV; simulations Figs. 3–4 |
| C2 | The UFP–MA transition is at φ = (u − γv)², i.e. σ_c = √2/(1 + γ) for equal carrying capacities, independent of μ | strong | (13), Appendix A; re-derived; Fig. 5(b) |
| C3 | Past the transition the community outcome depends on assembly history | moderate | numerical: repeated runs from different initial conditions, Fig. 5(b); not derived |
| C4 | In the UFP phase every feasible uninvadable fixed point is also dynamically stable | moderate | numerical check over several r distributions, §V |
| C5 | Feasibility, uninvadability and stability all fail together at one transition | moderate | §VI, interpretive summary of C2–C4 |

## Method

The cavity method: add species 0 with fresh interactions; treat its
effect on the others by linear response with susceptibilities
v_ij = ∂n_i/∂ξ_j; the diagonal sum gives the self-interaction
correction γv and the off-diagonal terms vanish at large S. The
stability calculation perturbs every λ_i by independent noise and
asks when the variance of the response diverges.

## Concepts

- **UFP phase**: a unique, stable, uninvadable fixed point for every
  realization.
- **MA phase**: multiple dynamical attractors, fixed or not; composition
  depends on initial conditions or invasion order.
- **Persistent species**: N_i > 0 at the fixed point; φ is their
  fraction of the pool.

## Connections

The equations match those of the random replicator model of Diederich and
Opper and Opper and Diederich (refs. 4, 6) for σ_λ = 0, and the
transition is of the same kind as theirs. Rieger (ref. 5) treated the
Lotka–Volterra case under assumptions that hide the MA phase. The
companion arXiv paper (Bunin 2016, 1607.04734) uses the same model for
the structure of assembled interaction networks. Blumenthal, Rocks and
Mehta (LIT-1236) apply the same cavity stability test to a
consumer–resource model with non-reciprocal interactions and identify
its transition with this paper's MA transition. CLAIM-369 is the
symmetric case of a related model, where dynamics are gradient flow.

## Bearing on the record

- **QUESTION-083.** The LIT files this as the phase in which outcomes
  depend on history. The reading supports that, with a qualification:
  what is derived is where the unique outcome ends; that the alternative
  outcomes then depend on order of arrival is shown by simulation only,
  and for γ = 0 the dynamics may not settle at all. "Entrenchment of
  whatever gained influence early" (the synthesis's reading) is a
  reading of the MA phase that the paper does not test: it does not
  study which of several attractors early arrivals select.
- **CLAIM-369.** For γ = 1 (symmetric interactions) this model has
  MacArthur's Lyapunov function V = Σ K_i N_i − ½ Σ α_ij N_i N_j (a
  standard fact for positive r_i/K_i, checked here, not stated in the
  paper), and the MA phase
  still exists (σ_c = 1/√2). So
  symmetry and an optimization principle do not by themselves give a
  unique outcome; multiplicity of minima does the work. This is
  consistent with CLAIM-369, which concerns the A = UᵀU case, positive
  semidefinite and so convex.

No instruction for machine-learning practice.

## Limitations

- The MA phase is located but not analysed; the author says it "may
  require more powerful and involved theoretical tools".
- No noise, no spatial structure, a single trophic level, unstructured
  random interactions. The truncated-Gaussian abundances differ from the
  lognormal or power-law forms commonly observed, which the author
  attributes to omitted processes.
- **Errors and slips.** Typographical only: "posses", "at at large S",
  "is not longer consistent", "resistent". None in the derivations
  checked.

## Open questions

- In the MA phase, how many attractors are there and how do their basins
  depend on invasion order? The paper points to later work.
