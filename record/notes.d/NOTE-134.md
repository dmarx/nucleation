---
number: 134
status: Read
formerly:
- NOTE-tmpi3hhh
paper: LIT-123
title: 'Carroll — Reality as a vector in Hilbert space'
version: 2
history:
- version: 2
  date: '2026-09-26'
  note: >-
    Read in full (full text of arXiv:2103.09780v1 (16 pp., downloaded
    2026-09-26 to rawM/carroll.pdf, extracted with pypdf because pdftotext
    is not installed; eq. (4) and the finiteness figure on p. 5 were checked
    against a rendered image of the page). That covers the abstract (p. 1),
    the unsectioned essay (pp. 2–12), the acknowledgements and all
    references (pp. 12–16). Nothing was skipped. The sections are
    unnumbered, so locations are PDF pages. The companion papers that carry
    the technical results were not opened: Carroll & Singh 2019 and 2021,
    Cotler, Penington & Ranard 2019, Cao, Carroll & Michalakis 2017, and Cao
    & Carroll 2018. The arXiv abs page (checked 2026-09-26) lists only v1.
    It has the comment "Invited contribution to the volume Quantum Mechanics
    and Fundamentality…, Valia Allori (ed.)". The book chapter's DOI was not
    checked.). Upgraded from `Skimmed` to `Read`: the claims table,
    assumptions and results are new, and the skim is corrected where the
    full text disagreed.
date: '2026-09-26'
summary: >-
  A programmatic essay, not a result paper. Carroll argues that a quantum
  theory is fixed, up to unitary equivalence, by the Hamiltonian's
  eigenvalue list {E_n} on a finite-dimensional factor (he assumes a
  non-degenerate spectrum), and that parts are not given. Subsystems
  (tensor factorisations H = H_S ⊗ H_E or ⨂_α H_α), classicality and space
  are to be selected afterwards as rare structure that suits the dynamics.
  The only uniqueness he reports is for local factorisations, and it rests
  on a cited theorem (Cotler et al. 2019). The system/environment
  criterion rests on "simple numerical examples" in a companion paper, the
  metric and Einstein's equation on "optimistic assumptions", and emergent
  fields on a hope.
---
<!-- inactive-ok-file: LIT-204 — Deferred: a related seed named by a 2026-09-26 close reading on the mereology tag; lapses when the cited work is read -->
<!-- inactive-ok-file: LIT-177 — Deferred: a related seed named by a 2026-09-26 close reading on the mereology tag; lapses when the cited work is read -->
<!-- inactive-ok-file: LIT-164 — Deferred: a related seed named by a 2026-09-26 close reading on the mereology tag; lapses when the cited work is read -->
<!-- inactive-ok-file: LIT-150 — Deferred: a related seed named by a 2026-09-26 close reading on the mereology tag; lapses when the cited work is read -->
<!-- inactive-ok-file: LIT-121 — Deferred: a related seed named by a 2026-09-26 close reading on the mereology tag; lapses when the cited work is read -->
<!-- inactive-ok-file: LIT-100 — Deferred: a related seed named by a 2026-09-26 close reading on the mereology tag; lapses when the cited work is read -->
<!-- inactive-ok-file: LIT-005 — Proposed: read in full and unproven as a formal criterion; cited as a related account, not as an established result -->
<!-- inactive-ok-file: LIT-049 — Proposed: read in full and unproven as a formal criterion; cited as a related account, not as an established result -->

# NOTE-134: Carroll — Reality as a vector in Hilbert space

## Contribution

The essay collects Carroll's programme into one short argument. First, Hilbert space is featureless, so an Everettian quantum theory is fully specified by the dimension and the Hamiltonian's spectrum {E_n}. Second, the finite dimension is motivated by gravitational entropy bounds. Third, everything else has to come out as emergent structure: subsystems, classical objects, space, spacetime and fields. The route is "quantum mereology", which means choosing a tensor-product factorisation of H that the dynamics favours. The essay derives nothing new. What is new is the explicit claim that parthood is not in the fundamental ontology at all, only a description chosen for how rare it is and how well it fits the dynamics.

## Key insight

The state vector has no parts until something chooses a factorisation, and the choice can in principle be made by the dynamics. Among all ways of writing H as a tensor product, a generic Hamiltonian makes none of them look like quasi-classical subsystems or local regions (pp. 8–9, 11). When one does, its rarity is what lets it be defined uniquely from bare ingredients, and on this view that uniqueness is what makes the parts "real, though not fundamental" (pp. 7, 11–12, following Dennett 1991 and Wallace 2012).

## Assumptions

- **Everettian minimalism.** The ontology is |Ψ⟩ ∈ H evolving by Ĥ|Ψ⟩ = iℏ∂_t|Ψ⟩ (eq. 1), with no hidden variables or collapse (p. 3). This is a methodological choice, "to see how far we can get from a minimal starting point".
- **No preferred basis.** Changes of basis, such as position to momentum, have "no physical importance whatsoever" (p. 4).
- **A non-degenerate spectrum.** The energy eigenbasis is unique, "for simplicity" (p. 4).
- **Finite dimension.** The analysis works in a finite-dimensional factor H_R, the observable universe or another finite region (p. 5). This is justified by black-hole entropy bounds, with citations to Banks, Bao et al., Bekenstein, Bousso and Jacobson. H_E interactions are neglected "for practical purposes". Mixed states are handled by purification with a finite auxiliary factor.
- **Non-separable spaces are set aside.** In that case extra data would be needed, typically an algebra of observables, because of Haag 1955 (p. 5).
- **Time is fundamental** (p. 11). For Wheeler–DeWitt (Ĥ|Ψ⟩ = 0) the paper supposes an effective split Ĥ = Ĥ_eff − i d/dτ (eq. 14) and uses Ĥ_eff's spectrum.
- **Criteria for a natural ontology.** A subsystem ontology is natural when (a) its internal dynamics are simple and (b) it is what external observation "sees", following Zanardi et al. 2004 (pp. 6–7). This premise drives the mereology.
- **The mereology programme's own inputs** (p. 8). Factor dimensions are fixed. dim H_E ≫ dim H_S, and the environment's internal dynamics are "largely irrelevant". Test states start localised and unentangled.
- **The spacetime programme's own inputs** (p. 10). The state is near the vacuum. Mutual information falls monotonically with distance. A best-fit smooth geometry exists. For Einstein's equation, approximate Lorentz invariance emerges.

## Key results

The paper states these results but does not prove them. Each is reported from a cited source.

- **A theory equals its spectrum** (pp. 4–5). Given only d and Ĥ as an abstract operator, all the information in the Hamiltonian is its eigenvalue list {E_n}. The eigenvectors are just an orthonormal set. Evolution in that basis is trivial: |Ψ(t)⟩ = Σ_n ψ_n e^{−iE_n t}|n⟩ (eq. 5, p. 6).
- **Finiteness** (p. 5). dim H_R ≤ exp(e^{πr²/G}) as printed (eq. 4), and "approximately" e^{e^{123}} for the observable universe. See corrections: the premise supports dim H_R ≤ exp(πr²/G).
- **Factorisations and splitting the Hamiltonian** (pp. 7–8). Once the factor dimensions are fixed, the factorisations H = H_S ⊗ H_E (eq. 6) are related by unitaries that mix the factors. Each one induces Ĥ = Ĥ_S ⊗ I_E + I_S ⊗ Ĥ_E + Ĥ_int (eq. 7).
- **Quasi-classical selection criterion** (pp. 8–9, from Carroll & Singh 2021).
  - For each factorisation, take the candidate pointer observable Q̂_S = Σ|φ_n⟩⟨φ_n| that comes closest to Zurek's commutativity condition [Ĥ_int, Q̂_S ⊗ I_E] ≈ 0 (eq. 8).
  - From an initially localised, unentangled system state, compute how fast delocalisation and entanglement grow.
  - "The correct factorization is the one that minimizes both."
  - The support offered is that "simple numerical examples verify" it recovers the standard split. The behaviour does not occur for random Hamiltonians or for random factorisations.
- **Local factorisation** (p. 9, from Cotler et al. 2019).
  - Write H = ⨂_α H_α (eq. 9), and expand Ĥ as self, 2-point, 3-point and higher terms (eq. 10). A necessary condition for "space" is that eq. 10 terminates, with only few-body, nearest-neighbour terms.
  - Generic Hamiltonians admit no local factorisation. When one exists, it is unique up to irrelevant internal transformations.
  - Carroll adds that the necessary condition is "also essentially sufficient". That step is his gloss, not part of the cited theorem.
- **Metric from entanglement** (p. 10, from Cao et al. 2017). Define a distance that decreases with I(α:β) = S_α + S_β − S_αβ (eq. 11). If a smooth best-fit geometry exists, classical multidimensional scaling determines it uniquely. This holds only "if that state is near to the vacuum". The metric comes out on space, not spacetime (p. 11).
- **Einstein's equation** (p. 10, from Cao & Carroll 2018, after Jacobson). Assume δA ∝ δS (eq. 12) and emergent Lorentz symmetry. Perturbations of the vacuum then obey δG_μν ∝ δT_μν (eq. 13) in the weak-field limit. Carroll adds his own caveat: the result "shouldn't be over-interpreted", and "we haven't shown that it is *the* emergent metric" that test particles follow.
- **Approximate Lorentz invariance** (p. 11). Non-compact groups have no nontrivial finite-dimensional representations, so in a finite-dimensional factor Lorentz invariance can only be approximate. The paper says this could be an experimental signature.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | A finite-dimensional quantum theory (H, Ĥ) is determined up to unitary equivalence by its energy spectrum. | strong as mathematics; the ontological reading ("the laws of physics are determined solely by" it, abstract) is argued, not shown | informal argument, pp. 4–5; standard spectral theorem; assumes non-degeneracy and finiteness |
| C2 | The Hilbert space of the observable universe is finite-dimensional. | weak–moderate | argument from cited black-hole entropy bounds, p. 5; eq. 4 as printed does not follow from its stated premise (see corrections); gauge theories do not factorise by region (fn. 1) |
| C3 | Parts and subsystems are not fundamental. The emergent descriptions to look for are tensor-product factorisations, and direct sums "for certain situations". | assertion (a programme choice) | pp. 6–7, motivated by Zanardi et al. 2004 and the N-particle and fluid examples |
| C4 | Generic Hamiltonians admit no factorisation with quasi-classical system dynamics and slow system–environment entanglement. | weak here | "It was argued by Carroll & Singh (2019)", p. 8; cited argument, not reproduced |
| C5 | Minimising delocalisation and entanglement growth over factorisations selects the standard system/environment split. | weak here | "simple numerical examples verify", pp. 8–9, from Carroll & Singh 2021; no examples shown; needs fixed dimensions and a test state as inputs |
| C6 | Generic Hamiltonians admit no local factorisation, and one that exists is unique up to irrelevant transformations. | strong (by citation) | theorem of Cotler et al. 2019, p. 9, with "some technicalities that we won't go into" |
| C7 | A local factorisation is "essentially sufficient" for an emergent structure recognisable as space. | assertion | p. 9; nothing is argued beyond C6 |
| C8 | The dimension and geometry of space can be read off the mutual information of a near-vacuum state. | moderate, conditional | Cao et al. 2017, p. 10; holds only if a best-fit smooth geometry exists |
| C9 | The emergent geometry obeys Einstein's equation in the weak-field limit. | weak–moderate, conditional | Cao & Carroll 2018, p. 10; needs "optimistic assumptions", above all emergent Lorentz invariance, and δA ∝ δS is posited; the author warns against over-interpreting it |
| C10 | Quantum fields can be reconstructed from the spectrum. | conjecture | "not unreasonable to hope", p. 11; string-net condensates are cited as a possible route |
| C11 | Emergent spacetime and fields are "equally real as tables and chairs". | philosophical argument | p. 12; real-patterns reasoning (Dennett, Wallace, p. 7) plus non-genericity (p. 11) |
| C12 | The spectrum "seems to provide the requisite information" to pinpoint a classical description when one exists. | weak | p. 9; inferred from C4–C5 and hedged by the author |

## Method

A philosophical argument that surveys results. The pattern is: remove the structure that quantisation brings in (pp. 2–4), reduce what is given to (d, {E_n}) plus the state (pp. 4–5), then for each familiar structure name the companion paper that recovers it and the conditions that paper needs (pp. 7–11). The essay contains no new derivations, figures or numerics.

## Concepts

- **Hilbert space fundamentalism / "Mad-Dog Everettianism"** — the fundamental ontology is completely and exactly a vector in abstract Hilbert space evolving unitarily. Everything else is emergent (p. 2).
- **Quantum mereology** — "how to decompose the whole of Hilbert space into parts such that individual subsystems have simple internal dynamics, and those dynamics are readily observed via interactions with other subsystems, given nothing but the spectrum of the Hamiltonian" (p. 7). A part is a tensor factor, and parthood is relative to a chosen factorisation.
- **Factorisation** — a tensor-product decomposition of H into factors of fixed dimensions. Factorisations with the same dimensions differ by a unitary (p. 7).
- **Pointer observable / pointer states** — Q̂_S = Σ|φ_n⟩⟨φ_n|, built from the basis in which the system's density operator diagonalises under monitoring by the environment. These are the states that look classical (p. 8, Zurek).
- **Quantum Measurement Limit** — the regime where Ĥ_int dominates Ĥ_S, in which eq. (8) holds (p. 8).
- **Local factorisation** — a factorisation ⨂_α H_α in which Ĥ has only few-body, neighbour interactions (p. 9).
- **Non-generic** — the paper's term for how rare useful structure is. Most Hamiltonians and most factorisations lack it, and that rarity is what allows a unique definition (pp. 8, 11–12).

## Connections

The essay sits among the wave-function ontology positions the record holds. Against Albert's configuration-space wave-function realism, it sides with Wallace (2017): configuration space is one representation among many (p. 3). For the field this is surveyed in [LIT-204](../literature.d/LIT-204.md) (Chen) and [LIT-121](../literature.d/LIT-121.md) (Gao), and it bears on [LIT-164](../literature.d/LIT-164.md). It is the opposite pole to relational and epistemic readings, [LIT-177](../literature.d/LIT-177.md) (Rovelli) and [LIT-090](../literature.d/LIT-090.md). Where [LIT-100](../literature.d/LIT-100.md) (Belot) asks what category the quantum state belongs to, Carroll answers that the state is the only category. It takes ψ-ontology for granted and does not engage [LIT-062](../literature.d/LIT-062.md) (Pusey–Barrett–Rudolph).

For the mereology tag, the contrast with [LIT-124](../literature.d/LIT-124.md) (Varzi, SEP *Mereology*) is sharp. Carroll offers no parthood relation, no axioms and no account of composition, overlap or sums. There is only a whole, and a family of ways to split it. Parts exist relative to a factorisation, and one factorisation is preferred on dynamical and epistemic grounds (simple internal dynamics, observability), not metaphysical ones. That puts the essay closer to the individuality literature than to classical mereology. Bourrat's coarse-graining account, [LIT-049](../literature.d/LIT-049.md), also treats individuals as summaries a lower level licenses, and [LIT-005](../literature.d/LIT-005.md) adds causal criteria to information-theoretic individuality. The formal settings differ entirely: evolutionary populations there, Hilbert-space factors here. The analogy is mine and is not in the paper. The essay also belongs to the emergence cluster, [LIT-150](../literature.d/LIT-150.md) and [LIT-025](../literature.d/LIT-025.md), through its real-patterns account of emergent reality (p. 7).

## Bearing on the record

- For the mereology topic, this is the record's clearest example of a whole-first ontology in which parts are chosen descriptions, not constituents. Any document that cites it for a *uniqueness* result about subsystems should cite the local-factorisation theorem (Cotler et al.), not the quasi-classical criterion, which is supported only by numerical examples in a companion paper. It should not cite this essay as proof of either.
- NOTE-134's summary overstates what is recovered: fields are hoped for, not recovered. The finiteness figure should not be quoted from this paper as printed.
- No THEORY document is known to depend on it; none was checked beyond the grep of literature.d.
- For ML practice it carries nothing. There is no instruction for the Anthology of the SOTA.

## Limitations

- Nothing in the paper is proved. Every technical claim is delegated to cited work, most of it the author's own. The author calls it "an overly concise discussion of an ambitious research program (and one that may ultimately fail)" (p. 12).
- The mereology is not purely spectral. Factor dimensions, a test state, the regime dim H_E ≫ dim H_S, and the region/rest split behind H_R (eq. 3, "somewhat cheating", fn. 1) all enter from outside the spectrum.
- Gauge theories do not factorise by region (fn. 1), yet the Standard Model is a gauge theory. The problem is noted and not addressed.
- The treatment covers only a single bipartite split and a single local multipartite split. Nested, hierarchical or overlapping parts are not discussed, nor whether several good factorisations can coexist for different subsystems. Direct sums get one bracketed sentence (p. 7).
- The spacetime results are conditional on proximity to the vacuum, the existence of a smooth geometry and emergent Lorentz invariance. They yield a spatial metric, not the metric test particles follow.
- Eq. (4) and the e^{e^{123}} figure appear inconsistent with the stated entropy premise (see corrections).
- The essay does not engage objections that spectrum-only structure underdetermines physics. Whether such objections defeat C1's ontological reading is outside the text, and unverified here.

## Open questions

- Does the Carroll–Singh criterion single out one factorisation in any setting that is not a toy? What would settle it is a uniqueness theorem analogous to Cotler et al. for quasi-classical splits, not numerical examples.
- Can the inputs outside the spectrum (factor dimensions, test states, the region split behind finiteness) be eliminated or derived? If not, "given nothing but the spectrum" (p. 7) is too strong.
- How does a factorisation-relative notion of part relate to classical mereological axioms ([LIT-124](../literature.d/LIT-124.md))? Is entanglement, where the whole is not fixed by its parts' states, a counterexample to supplementation or composition principles? The paper is silent.
- Do the objections that spectrum-only structure underdetermines physics, which the skim attributes to Stoica, defeat C1? Reading those works would settle whether C1 is a fact about representation or an ontology.
- Does "equally real" amount to a substantive metaphysics of emergence? The text gives only the real-patterns criterion (p. 7) plus non-genericity (pp. 11–12). It is a pragmatic–structural view, not a worked-out account.

## Corrections to the seeded skim

- Uniqueness is misattributed. The skim's open question checks "the uniqueness claims for the quasi-classical factorisation (Carroll & Singh 2019)". The paper makes no uniqueness claim for the quasi-classical system/environment factorisation. It cites Carroll & Singh (2019, "Mad-Dog Everettianism") only for the argument that generic Hamiltonians show quasi-classical behaviour in no factorisation (p. 8). The selection criterion comes from Carroll & Singh (2021, Phys. Rev. A 103, 022213), and all the paper says of it is that "simple numerical examples verify" it picks the usual split (pp. 8–9). The one uniqueness claim is for a *local* factorisation, "unique up to irrelevant internal transformations (and some technicalities…)", and it is credited to Cotler, Penington & Ranard (2019) (p. 9).
- The finiteness figure was copied unchecked. The skim reports "dim ≲ e^(e^123)" as the paper's result. The page image confirms the paper prints eq. (4) as dim H_R ≤ exp(e^{πr²/G}) and the figure as e^{e^{123}} (p. 5). The premise it states, maximum entropy S_BH = πr²/G, gives dim H_R ≤ exp(πr²/G), a single exponential, so the extra exponential in eq. (4) looks like a typo. The paper does not state its entropy value. On the commonly quoted S ≈ 10^122 the bound would be ≈ e^{10^122} ≈ e^{e^{281}}, not e^{e^{123}}. That arithmetic is mine: treat the printed number as unverified and cite the order of magnitude, not the figure. The bound also covers only the factor H_R. Whether the full H is finite is left open, with an indirect Boltzmann-brain consideration (p. 5).
- Fields are not recovered. NOTE-134's summary says subsystems, classicality, space "and fields" are "recovered". On fields the paper says "less explicit progress has been made" and that "it's not unreasonable to hope" the task is easier, pointing to string-net condensates (p. 11). Space is recovered only conditionally: only the spatial metric, near vacuum, under stated assumptions.
- The quasi-classical factorisation is not picked out from the spectrum alone. The criterion fixes dim H_S and dim H_E in advance (p. 7) and assumes dim H_E ≫ dim H_S (p. 8). It evaluates each candidate from "an initially localized and unentangled system state" (p. 8). The finite factor H_R is itself introduced through a split into a region of space and the rest (eq. 3), which footnote 1 concedes is "somewhat cheating". The skim's gloss hides these inputs.
- Minor locations. The non-separable caveat is on p. 5, not p. 4. The local factorisation, the mutual-information metric and Einstein's equation are on pp. 9–10. Time and fields are on p. 11. "Equally real as tables and chairs" is on p. 12. Stoica, named in the skim's open questions, is not cited or discussed in the paper; that pointer is the skimmer's own.
