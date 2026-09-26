---
number: 118
status: Read
formerly:
- NOTE-tmpd9gwh
paper: LIT-122
title: 'Belot — Time and change in mechanics'
version: 2
history:
- version: 2
  date: '2026-09-26'
  note: >-
    Read in full (full text of the published chapter (Handbook of the
    Philosophy of Science: Philosophy of Physics, Part A, eds. Butterfield &
    Earman, Elsevier/North-Holland 2007, pp. 133–227; 95 PDF pp.), from the
    public mirror copy (isidore.co) the dossier used. It was already
    downloaded in this sweep and extracted with PyMuPDF. That covers §§1–7
    including all remarks, examples and footnotes (pp. 133–221), the
    acknowledgements, and the bibliography (pp. 221–227; scanned, not
    checked entry by entry). The PhilSci-Archive preprint (#2549) was not
    compared. Displayed equations were read in their text-extracted form,
    and several matrices and integrals are garbled by the extraction, but
    the surrounding prose states each result.). Upgraded from `Skimmed` to
    `Read`: the claims table, assumptions and results are new, and the skim
    is corrected where the full text disagreed.
date: '2026-09-26'
summary: >-
  For theories with ideal existence, uniqueness and a dynamical
  time-translation group, time is three intertwined ℝ-actions (on
  spacetime, on the symplectic space of solutions, and on the isomorphic
  space of initial data), and change is a slicing-indexed family of
  functions on those spaces. Singular dynamics, gauge freedom and
  time-dependence each damage this picture in a repairable way. Spatially
  compact vacuum GR breaks it, because the reduced Hamiltonian vanishes (h
  ≡ 0) and there is only one canonical isomorphism between the reduced
  spaces. That is the problem of time. It is not an artefact of the 3+1
  split, it does not show change to be illusory, and it is absent from
  asymptotically flat GR and from artificially generally covariant
  theories. A parameterized "geometric time", such as CMC, restores change
  and, in the CMC case, a time-dependent Hamiltonian flow.
---
<!-- inactive-ok-file: LIT-180 — Deferred: a related work named by a 2026-09-26 close reading on the metaphysics tag; lapses when the cited work is read -->

# NOTE-118: Belot — Time and change in mechanics

## Contribution

It pins the "problem of time" to a precise structural failure. In every well-behaved classical theory, time appears as a flow (ℝ-action) on a symplectic space, and change is represented by functions on that space or a slicing-indexed family of them. Spatially compact GR is the case where neither holds. The chapter derives this by building the covariant (space-of-solutions) Lagrangian picture alongside the Hamiltonian one, so that the problem cannot be blamed on the 3+1 split. It also separates the problem from general covariance as such, using asymptotically flat GR and artificially covariant theories as contrasts.

## Key insight

Keep the space of solutions and the space of initial data apart. In a well-behaved theory, a slicing gives a *one-parameter family* of symplectic isomorphisms T_Σt : S → I. That family is what lets initial data represent states that recur at different times, and what lets functions on S represent changeable quantities. In cosmological GR, after reduction, there is only *one* canonical isomorphism between the reduced spaces. So both spaces represent whole worlds, not instants. Nothing in the formalism then represents change, although many of the worlds represented contain change.

## Assumptions

- The level of rigour is formal differential geometry. Spaces may be non-Hausdorff, infinite-dimensional (Banach) and Whitney-stratified, with mild singularities, and "functional analytic details are held in abeyance" (p. 138; §3.1).
- Field theories are (K, Δ) or (K, L) on a spacetime V ≅ M × ℝ, with W a finite-dimensional vector space and K a space of sections of a trivial bundle (§4). From §5 on, equations of motion are second-order.
- **§5 ideal conditions:** (a) global existence of solutions; (b) uniqueness given initial data on an instant; (c) V has a time-translation group τ̄ whose induced τ is a Noether group of L (a "dynamical time translation group").
- **§6** drops (a), (b) and (c) one at a time, keeping enough spacetime structure to support slicings.
- **§7:** vacuum GR, zero cosmological constant, globally hyperbolic solutions with compact orientable Cauchy surfaces. §7.3 uses (3+1) dimensions and "well-behaved" solutions, i.e. those admitting a CMC foliation. Example 54 needs S of Yamabe type −1 with no metrics having positive-dimensional isometry groups.
- Possible-worlds talk is heuristic only (Remark 2, p. 139).

## Key results

- **Symplectic structure of solutions (§4.2, fn. 61).** A Lagrangian L induces a closed two-form Ω on S, obtained by integrating Z := ∂M over any instant and independent of the instant. Ω is symplectic iff solutions are determined by initial data (believed; fn. 63), and presymplectic under gauge symmetry. Nontrivially different Lagrangians for the same Δ can induce different Ω and so different quantizations (the spherical-potential example, fn. 66).
- **Noether (§4.3).** A Noether group ξ has a current J_ξ whose charge Q_ξ(Φ) = ∫_Σ J_ξ(Φ) is independent of Σ, and Q_ξ is the (pre)symplectic generator of ξ on S (Remark 22). Charges of gauge groups are identically zero (fn. 107).
- **Well-behaved theories (§5.5).** (S, Ω) and (I, ω) are symplectic, and each T_Σ is a symplectic isomorphism with h = H ∘ T_Σ⁻¹. T_Σ intertwines time translation on S with time evolution on I: t ·_I T_Σ(Φ) = T_Σ(t ·_S Φ). A solution is changeless iff it is invariant under some time-translation group (§5.4, fn. 84). A changeable quantity f on I yields f_t := f ∘ T_Σt on S.
- **Singular dynamics (§6.1).** The Hamiltonian vector field is incomplete, so time evolution on I is only a local flow, and each T_Σ is a partial symplectic isomorphism. The planar Kepler problem with H < 0 has a non-Hausdorff space of solutions, assembled from copies of X^{3,∞}_1, while I = T*Q is Hausdorff (Example 32). Which space one quantizes is then a real choice (Remark 34).
- **Gauge freedom (§6.2).** S and I are presymplectic and not isomorphic, even locally. H generates a gauge-equivalence class of flows, and only gauge-invariant quantities evolve deterministically. Reduction gives isomorphic symplectic reduced spaces, "when all goes well". Example 36 (L = ½ e^y ẋ²) is a counterexample: the reduced solution space is ℝ, odd-dimensional, and the reduced data space is a point. Examples 37 (Newtonian, Leibnizean and semi-Leibnizean two-body theories) and 38 (Maxwell) show reduction removing otiose variables. On R³ × S¹ the Maxwell reduced space needs a holonomy, which is non-local and at odds with Humean supervenience (fn. 122).
- **Reduction and determinism (Remark 35).** Maudlin's objection to making theories deterministic by identifying futures does not transfer to gauge reduction. The indeterminism removed is "unphysical", and in known cases reduction yields a well-behaved symplectic space.
- **Time-dependent systems (§6.3).** S ≅ I symplectically, but there is no time-translation group on S. On I there is a family of one-parameter groups g^{t₀}_s, indexed by the instant of posing data, that are symplectic but do not preserve h.
- **General covariance (§7.1).** Weak general covariance means D(V) is a symmetry of Δ. Strong general covariance means D(V) is a gauge group of L, which holds cleanly for compactly supported D_c(V). Spatially compact vacuum GR has no nontrivial Noether quantities, and its reduced space S′ of "geometries" [g] is symplectic with mild singularities at solutions with Killing fields.
- **Vanishing Hamiltonian (p. 202).** For spatially compact GR, h ≡ 0. Dynamical trajectories are curves within gauge orbits, and on the reduced data space I′ they are constant. It is "presumed" that I′ ≅ S′ canonically. There is no ℝ-action implementing time on S, S′ or I′.
- **Asymptotically flat contrast (pp. 204–206).** D^∞(V) is D^∞_0(V) ⋊ Poincaré, and the reduced spaces carry a Poincaré representation with a non-zero Hamiltonian for each time translation at infinity. Change is represented in the familiar way.
- **Artificial general covariance (Examples 43–44).** Any Lagrangian theory on a fixed background can be made strongly generally covariant (Lee & Wald; Torre). Its Hamiltonians vanish too, but the background theory T₀ can be reconstructed and S′ ≅ S₀, so the problem of time is avoidable there. The residual worry is that the reconstructed metric is fixed only up to conformal class.
- **Problem of time (§7.2, p. 209).** "time is not represented in general relativity by a flow on a symplectic space and change is not represented by functions on a space of instantaneous or global states." Its sources: not the 3+1 split; not lack of a preferred slicing, slicing freedom or diffeomorphism invariance alone; but full dynamism of geometry in a diffeomorphism-invariant theory (p. 210). It is urgent for quantization, because quantum dynamics and semiclassical methods need a Hamiltonian (p. 211, fn. 174).
- **Geometric time (§7.3, Defs 45–50).** A geometric time assigns foliations to solutions equivariantly under D(V). Such times are always absolute (Remark 51), so Minkowski spacetime and time-symmetric solutions fall outside every parameterized geometric time. Examples: dust-orthogonal and isometry-orbit foliations (small domains), CMC time (Example 52) and cosmological time (Example 53). With a parameterized geometric time, a changeable quantity f on instantaneous geometries gives f_t[g] on S′.
- **CMC Hamiltonianization (Example 54).** For S of Yamabe type −1, I* = T*M/D(S), with M the metrics of scalar curvature −1. For each t < 0, solving the Lichnerowicz equation gives a symplectic isomorphism I* ≅ S′, and the resulting trajectories are generated by a time-dependent Hamiltonian that is "a simple function of t and of spatial volume" (pp. 218–219; Fischer–Moncrief). Time-independent Hamiltonianizations are known for special cases: the T² spatial topology in (2+1), and GR with perfect fluid, where baryon number drives the dynamics (fn. 199).
- **Quantum worry (pp. 220–221).** Distinct geometric times are not expected to give unitarily equivalent quantizations (fn. 201; Gotay & Demaret). The hopes are "long shots", and "Far more plausibly, the solution … will come from some other direction entirely".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | For well-behaved theories (§5 conditions), (S, Ω) ≅ (I, ω) via each T_Σ, and T_Σ intertwines time translation on S with time evolution on I | strong | derivation in §§5.1–5.3, standard results cited (Woodhouse, Zuckerman, Deligne–Freed) at the formal level |
| C2 | Theories with gauge symmetries have presymplectic S and I, trivial gauge Noether charges, and (when all goes well) isomorphic symplectic reduced spaces | strong for the general facts; moderate for "when all goes well" | proof sketches with cited results; Example 36 shows the proviso is needed |
| C3 | The planar Kepler problem's space of solutions is non-Hausdorff, so S ≇ I there | strong | explicit construction (Example 32) |
| C4 | For spatially compact vacuum GR, h ≡ 0, and there is no ℝ-action implementing time on S, S′ or I′ | strong | standard canonical GR (Wald App. E; Beig), stated with citations |
| C5 | The reduced space of initial data and the reduced space of solutions of spatially compact GR are canonically symplectically isomorphic | moderate | "it is presumed" (p. 202), citing Fischer & Moncrief |
| C6 | The problem of time does not show change to be an illusion | moderate–strong | argument (pp. 209–210): I′ ≅ S′, and S′ contains changing worlds (Big Bang solutions) and changeless ones (Einstein static) |
| C7 | The problem of time is not an artefact of the 3+1 decomposition | strong | the problem is derived in the covariant Lagrangian picture |
| C8 | Diffeomorphism invariance, absence of a preferred slicing, and slicing freedom are not sufficient for the problem of time | moderate | contrast cases: asymptotically flat GR (cited results) and artificial covariance (Example 44, "I think") |
| C9 | Gauge reduction is not open to Maudlin's objection to identifying indeterministic futures | moderate | informal argument (Remark 35) |
| C10 | Gauge freedom may be prevalent because non-physical variables let an intrinsically non-local theory be cast in local form | weak | "it seems plausible" (p. 191), citing Belot 2003 §13 |
| C11 | A parameterized geometric time lets changeable quantities be represented as one-parameter families on S′, and CMC time yields a time-dependent Hamiltonianization | strong for the construction; moderate for its scope | Defs 45–50; Example 54 cites Fischer–Moncrief; the scope depends on open CMC-foliation conjectures (pp. 214–215) |
| C12 | The content of GR is "exhausted by the set of all Hamiltonianizations" | weak | stated as what "seems entirely in the spirit" of GR (p. 220); not argued |
| C13 | Distinct geometric times are not expected to yield unitarily equivalent quantizations | moderate | expectation grounded in Stone–von Neumann's failure for infinite-dimensional and nonlinear phase spaces, with a minisuperspace example (fn. 201) |

## Method

Conceptual analysis on top of a technical exposition. The chapter sets up the covariant phase space (space-of-solutions) formalism for Lagrangian field theories following Zuckerman and Deligne–Freed. It sets beside it the Hamiltonian formalism relative to a slicing, and tracks what represents time (ℝ-actions) and change (functions or families of functions) in each. Assumptions are relaxed one at a time (§6), each with worked examples (Kepler, n-body, a pathological gauge example, the two-body Newtonian/Leibnizean/semi-Leibnizean theories, Maxwell). The results are then applied to GR in two sectors (spatially compact and asymptotically flat) and to an artificially covariant theory.

## Concepts

- **Space of solutions S / space of initial data I** — heuristically, possible worlds vs possible instantaneous states. The distinction is grounded by the slicing-indexed family of isomorphisms T_Σt.
- **Dynamical time translation group τ** — the Noether group on K induced by a time-translation group τ̄ of V.
- **Slicing** — a diffeomorphism σ : ℝ × S → V whose leaves are instants and whose curves are possible worldlines (Def. 27). It is *adapted* to τ̄ if its curves are τ̄-orbits.
- **Change** — "a single object having a given property at a given time and a distinct and incompatible property at a different time" (p. 169). A changeless solution is one invariant under some time-translation group.
- **Presymplectic form, gauge orbit, reduction** — as in §3.3. Reduction is the passage to the space of gauge orbits.
- **Weak / strong general covariance** — D(V) a symmetry of Δ, or a gauge group of L (after Earman 2006).
- **Geometry / instantaneous geometry** — a D(V)-orbit in S, and a D(S)-orbit in I. An instantaneous geometry is *not* a point of the reduced data space (fn. 175).
- **Geometric time; Hamiltonianization** — an equivariant assignment of foliations to solutions, and a (possibly time-dependent) Hamiltonian system on a symplectic I* whose flow reproduces the trajectories that the geometric time assigns.

## Connections

The chapter is the application counterpart of Butterfield's symplectic-reduction chapter in the same volume, and it is closest to the canonical treatments of the problem of time by Kuchař (1992) and Isham (1993). It positions itself against readings on which GR shows change to be illusory: Earman's "Thoroughly modern McTaggart" (2002) and Belot & Earman (2001) are cited. It also answers Maudlin's (2002) and Kuchař's resistance to applying reduction in GR (fn. 117, Remark 35). It draws on its own author's "Symmetry and gauge freedom" (2003) and "Dust, time, and symmetry" (2005).

Its distinction between symmetries of laws and symmetries of solutions (§1) is the modern, variational form of Wigner's distinction between geometric and dynamical invariance ([LIT-180](../literature.d/LIT-180.md)). Its treatment of gauge reduction as eliminating "physically otiose" variables is the same move whose analogue for dualities Le Bihan & Read ([LIT-113](../literature.d/LIT-113.md)) consider and De Haro & Butterfield ([LIT-199](../literature.d/LIT-199.md)) develop as the common core. Belot's Leibnizean vs semi-Leibnizean contrast (Example 37) is a clean small case of a "bare theory" obtained by quotienting.

The metaphysical thesis it presupposes is realism about change in a world described by GR, along with a modest view of theory content: what a theory says about time is read from the structure of its laws "qua dynamical theory", not from particular solutions (p. 134). It explicitly denies that GR entails that change is illusory. Its remarks on holonomies (fnn. 45, 122) put pressure on Humean supervenience for gauge theories. The metaphysics tag is justified, with philosophy-of-science leading.

## Bearing on the record

It would anchor any THEORY-style entry in the record on time, change or gauge in physics, and it is the reading to cite against "GR shows time is unreal" claims. It supports distinguishing solution-space and state-space representations, a distinction other seeded works in this sweep invoke loosely. Nothing in it is an instruction for ML practice, and it belongs in neither the Anthology of the SOTA nor any ML-facing summary.

## Limitations

- Formal rather than rigorous. Functional-analytic issues are deferred, and several key facts are "believed" or "presumed" (C5; the CMC foliation conjectures, pp. 214–215; "when all goes well" throughout §6.2).
- The GR analysis is restricted to vacuum, zero cosmological constant, globally hyperbolic, spatially compact solutions, and in §7.3 to (3+1) with CMC-foliable solutions. Example 54 needs special spatial topologies.
- Classical only. Quantum conclusions are stated as expectations (C13) and "long shots".
- The claim that the problem of time does not afflict the artificial covariant theory is hedged ("I think", p. 210), and the conformal-class worry about reconstructing T₀ is answered only partly.
- The chapter's literature and the status of the CMC conjectures date from 2005–2007.

## Open questions

- Is there a geometric time of wide scope that yields a *time-independent* Hamiltonianization of GR with non-trivial dynamics (p. 220)? Its construction would single out a "correct" time.
- Do distinct Hamiltonianizations lead to physically inequivalent quantizations in a realistic, not minisuperspace, setting?
- Does the reduced Maxwell or Yang–Mills solution space admit a local Lagrangian description (Remark 39)? A negative answer would support C10.
- Which spatial topologies admit global CMC foliations (Rendall's conjectures, fn. 183)? This fixes the domain of the CMC route.

## Corrections to the seeded skim

- The dossier leaves out the chapter's main diagnostic result (§7.2, p. 210). The problem of time does not arise for asymptotically flat GR, where the Poincaré group at spatial infinity supplies a non-zero Hamiltonian, nor for field theories on fixed backgrounds, nor ("I think") for the artificially strongly generally covariant Klein–Gordon theory of Examples 43–44. So "the lack of a preferred slicing; the jiggleability of admissible slicings; the invariance of the theory under a group of spacetime diffeomorphisms" are not sufficient conditions. It appears when a diffeomorphism-invariant theory models geometry as "fully dynamical", with no background structure "at spatial infinity or elsewhere".
- The dossier summary calls geometric time "the natural but costly way around it". Belot says §7.3 is offered "by way of further clarification of the problem of time, rather than as a suggested resolution" (p. 196). The cost he names is narrower: privileging *one* geometric time violates the spirit of GR, while taking the theory's content to be "exhausted by the set of all Hamiltonianizations" seems "entirely in the spirit" of it (pp. 219–220). That second sentence is a stated view, not an argued result, so the dossier's "argues" is too strong.
- The core technical fact behind the problem, missing from the dossier, is that for spatially compact vacuum GR the Hamiltonian obtained by the usual rule is h ≡ 0. Dynamical trajectories therefore stay inside gauge orbits, and on the reduced space of initial data they are constant curves (p. 202).
- Section boundaries: §7.2 is pp. 209–211 and §7.3 is pp. 212–221 (the dossier gives "~211–221"). The problem of time "only arises in those versions of general relativity most appropriate to the cosmological setting" (fn. 7, p. 137). The dossier's first bullet hints at this but does not state it.
- The dossier's `published: 2005-12-06` is the PhilSci deposit date. The chapter as read is the 2007 Elsevier printing, © 2007.
- metaphysics tag: justified. Time and change are the subject, the chapter rejects the thesis that GR shows "change is an illusion" (pp. 209–210), and it bears on Humean supervenience (fnn. 45, 122).
- primary topic: philosophy-of-science (keep as listed). The chapter is about how physical theories represent time and change, and metaphysics is the right second tag.
