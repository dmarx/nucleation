---
number: 79
status: Read
formerly:
- NOTE-tmpwli33
paper: LIT-036
title: 'Ouazan-Reboul et al. 2023, non-reciprocal metabolic cycles'
version: 2
history:
- version: 2
  date: '2026-09-25'
  note: >-
    Read in full (Full text of the published version, Nature Communications
    14:4496 (2023), 9 pp. incl. Methods, Table 1 and references
    (raw4/c33_nc.pdf → c33_nc.txt). Also read in full: the Supplementary
    Information (4 pp.: Supplementary Notes 1–2, Supplementary Figs. 1–5;
    raw4/c33_S1), the description of the ten Supplementary Movies
    (raw4/c33_S3), and the Peer Review File (10 pp.: two referees' reports
    and two rounds of author replies; raw4/c33_S2). I compared all of these
    against arXiv:2303.09832v1 (8 pp., the only arXiv version;
    raw4/2303.09832.txt). Text was extracted with PyMuPDF because pdftotext
    is not installed. I did not watch the movies. Figures came through only
    as labels, so for them I relied on captions and the surrounding prose.).
    Upgraded from `Skimmed` to `Read`: the claims table, assumptions and
    results are new, and the skim is corrected where the full text
    disagreed.
date: '2026-09-25'
summary: >-
  For M chemotactic catalyst species in a closed cycle, where species m
  converts chemical m into chemical m+1, the linearised long-wavelength
  interaction matrix is circulant, so its eigenvalues are Re λ_ℓ =
  −(αρ0/D)(μ(p)−μ(s))[1−cos(2πℓ/M)] and Im λ_ℓ = (αρ0/D)(μ(s)+μ(p))
  sin(2πℓ/M) (Eq. 5). The homogeneous state is unstable exactly when the
  species are self-attracting, μ(p) − μ(s) < 0 (Eq. 6). For even M the
  leading mode is real, with stoichiometry (1,−1,1,…), so same-parity
  species co-aggregate. For odd M the leading mode is a complex pair, and
  with chasing interactions this gives persistent "invasion–explosion"
  oscillations. The nonlinear phases were checked by Brownian dynamics at
  M = 5 and M = 6 only.
---

# NOTE-079: Ouazan-Reboul et al. 2023, non-reciprocal metabolic cycles

## Contribution

The paper gives a closed-form linear stability analysis of a minimal model. It has M species of catalytically active, chemotactic particles in a cyclic reaction network, all with equal parameters. Each species consumes its own substrate and produces the next species' substrate. Because each species responds to two chemicals, one made by its predecessor and one it shares with its successor, nearest neighbours in the cycle interact non-reciprocally. The resulting interaction matrix is circulant (Eq. 4), which makes the full spectrum explicit (Eq. 5) for any M. The new, checkable result is a parity dichotomy:
- **Even M:** a real leading eigenvalue λ_K = −2(αρ0/D)(μ(p)−μ(s)) (Eq. 7, M = 2K), and static aggregation by parity.
- **Odd M:** a complex-conjugate leading pair (Eq. 9), and, when chasing dominates, persistent oscillations.

Brownian dynamics at M = 5 and M = 6 bear out the linear predictions in the nonlinear regime.

## Key insight

Put the species on a ring with nearest-neighbour coupling that is not symmetric, and the stability matrix becomes a circulant. The Fourier mode with wavenumber π (alternating signs) exists only when M is even. On an even ring, the fastest-growing pattern splits the ring into two anti-correlated sublattices, which gives static "clusters of clusters". On an odd ring the alternating pattern frustrates: "if two clusters attempt to come together, a third will systematically come to break them apart" (p. 4). The best available mode is then a rotating complex pair, and the symmetric part of the coupling (chasing, μ(s) + μ(p)) sets its frequency.

## Assumptions

- All M species share one activity α and one pair of mobilities μ(s) (to own substrate) and μ(p) (to own product), and start at equal homogeneous density ρ0 (p. 3). The authors assert this "will not limit the range of validity of the predictions", citing their own follow-up preprints (refs 54–55), which are not reproduced here.
- Catalysis is substrate-saturated, so α is constant (Methods).
- The chemical fields are quasi-static (∂_t c ≃ 0), justified because substrates are small and diffuse fast (Methods). The chemicals are not degraded; the cycle has no net production.
- Only the long-wavelength mode q = 0 is analysed. The Dp q² term makes it the fastest-growing mode (Methods, after Eq. 13).
- Brownian dynamics set-up:
  - 3D periodic box with a minimum-image convention and no Ewald summation, even though the pair velocities decay only as 1/r² (Eq. 18). The authors note Ewald sums "would be relevant" only for larger systems;
  - volume fraction φ = 0.005, noise D̃p = 0.02, α̃ = 1;
  - N/M = 333 particles per species for M = 5 and 400 for M = 6;
  - forward Euler with hard-core overlap correction;
  - τ_tot ≈ 10²–10³ (Table 1 lists 900–8000).
- The pair interactions are far-field (point-source) velocities between spheres of radius R (Eqs. 14–18).

## Key results

- **Spectrum (Eq. 5).** Re λ_ℓ = −(αρ0/D)(μ(p)−μ(s))[1−cos(2πℓ/M)] and Im λ_ℓ = (αρ0/D)(μ(s)+μ(p)) sin(2πℓ/M), for ℓ = 1…M. There are M−1 nonzero eigenvalues in conjugate pairs, except λ_{M/2} when M is even. The non-cyclic comparison, where all species act on one chemical, has the single eigenvalue λ = −Mαμρ0/D and reduces to Keller–Segel (p. 3).
- **Instability condition (Eq. 6):** μ(p) − μ(s) < 0, i.e. the species must be self-attracting. It is independent of M and of the chasing strength.
- **Even M = 2K (Eqs. 7–8).** The leading eigenvalue λ_K = −2(αρ0/D)(μ(p)−μ(s)) is real, with eigenvector (1,−1,1,…,−1).
  - In Brownian dynamics (Fig. 3a, Movie 3, M = 6), M single-species clusters form first. They then assemble into two "clusters of clusters", one per parity, and the mean cluster size saturates at N/2 (Fig. 1e).
  - With chasing comparable to self-attraction, hybrid clusters chase each other (Supplementary Fig. 4a).
  - With strong chasing, two fully mixed same-parity clusters form (Movie 5).
  - With negligible self-attraction, transient oscillations come before clustering (Supplementary Fig. 4b).
- **Odd M = 2K+1 (Eqs. 9–10).** The leading pair is λ = −(αρ0/D)(μ(p)−μ(s))[1+cos(π/(2K+1))] ∓ i(αρ0/D)(μ(s)+μ(p)) sin(π/(2K+1)). Its eigenvector components are (−1)^{m−1}[cos((m−1)π/(2K+1)) ± i sin((m−1)π/(2K+1))], so second-nearest neighbours are out of phase by 2π/(2K+1).
  - Cross-repelling case: M single-species clusters, and cluster size saturates at N/M (Fig. 3b, Fig. 1e).
  - Chasing case, when growth is slower than oscillation (Eq. 11, stated to be "only... an order of magnitude" criterion): a periodic sequence in which a cluster of species m is invaded by species m+1 and "explodes" (Fig. 4, Movie 8). Supplementary Note 2 quantifies this at M = 5. Formation and explosion events are regularly spaced in the order 5→4→3→2→1→5, and the peak clusters hold 20–30 % of all particles (Supplementary Fig. 2).
  - Even weaker self-attraction gives "self-stirring" density waves with no clusters (Movie 9).
  - When growth beats oscillation, the result is non-oscillating chasing hybrid clusters (Supplementary Fig. 5, Movie 10).
- **Coarsening (p. 3):** N(t) = N0 exp[(μα/D)∫0^t ρ dt₁] ≃ N0 exp[(μα/D)ρt], contrasted with Lifshitz–Slyozov ~t^{1/3} coarsening.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The homogeneous state of the cycle is linearly unstable iff μ(p) − μ(s) < 0, for any M | strong | exact circulant eigenvalues, Eqs. 4–6 and Methods Eq. 13 (derivation, q = 0 mode) |
| C2 | For even M the leading mode is real with alternating stoichiometry, so same-parity species co-aggregate | strong (linear), moderate (nonlinear) | Eqs. 7–8 analytic; the final state is checked by Brownian dynamics at M = 6 only (Fig. 3a, Fig. 1e) |
| C3 | For odd M the leading mode is a complex pair, so oscillatory dynamics are possible | strong (linear) | Eq. 9; spectra plotted for M = 3–8 (Supplementary Fig. 1) |
| C4 | Odd cycles with chasing interactions reach a persistent oscillatory "invasion–explosion" steady state | moderate | Brownian dynamics at M = 5, one parameter set (Movie 8; Supplementary Note 2, 5 cycles shown); the onset criterion Eq. 11 is order-of-magnitude only |
| C5 | Cluster formation is exponential (even super-exponential), far faster than power-law coarsening | weak–moderate | scaling argument with an unspecified cluster density ρ(t); ensemble growth curves described as "qualitative" (Methods), Fig. 1e |
| C6 | The same long-range phoretic mechanism offers a route to metabolically active protocells at the origin of life | weak | informal argument (Discussion). The referees flagged the gap; the authors conceded in the review file that the μ values of prebiotic catalysts are unknown |
| C7 | Odd-membered metabolic cycles "may have an advantage", possibly connected to the 11-member citric acid cycle | assertion | Discussion sentence added during review; no fitness or efficiency measure is defined or computed |
| C8 | Unequal parameters across species would not change the conclusions | assertion (here) | cites the authors' own follow-up preprints (refs 54–55), not shown in this paper |

## Method

Continuum model (Eqs. 1–2). Each species density obeys ∂_t ρ_m = ∇·[Dp∇ρ_m + (μ(s)∇c(m) + μ(p)∇c(m+1))ρ_m]. Each chemical obeys ∂_t c(m) = D∇²c(m) + α(ρ_{m−1} − ρ_m). Linearising about the homogeneous state with quasi-static chemicals gives (λ + Dp q²)δρ_m = −(αρ0/D)[μ(s)δρ_{m−1} + (μ(p)−μ(s))δρ_m − μ(p)δρ_{m+1}] (Eq. 13). The q = 0 mode gives the circulant Λ (Eq. 4).

Particle simulations use far-field pair velocities, derived from point sources and sinks of strength α/(4πD):
- v = αμ(s)r/(4πDr³) for n = m+1;
- v = −αμ(p)r/(4πDr³) for n = m−1;
- v = α(μ(p)−μ(s))r/(4πDr³) for self (Eq. 18).

These are summed pairwise with Gaussian noise (Eq. 19) and integrated by forward Euler with hard-sphere overlap correction, in custom Julia code. Clusters are identified by a 1.1σ distance linkage.

## Concepts

- **Non-reciprocal interaction.** Here v_{m,m−1} ≠ −v_{m−1,m}. Species m moves toward m−1 because m−1 makes m's substrate (∝ αμ(s)). Species m−1 moves toward or away from m because m consumes m−1's product (∝ −αμ(p)).
- **Self-attraction strength |μ(p) − μ(s)|.** The coefficient of the self-interaction (Λ_mm). Instability requires μ(p) − μ(s) < 0.
- **Chasing strength |μ(s) + μ(p)|.** The antisymmetric part of the neighbour coupling. It sets Im λ; "chasing" means one neighbour attracts while the other repels.
- **Interaction motif.** One of six sign patterns of (μ(s), μ(p), μ(p)−μ(s)) that decide which interaction dominates (Fig. 1d).
- **Cluster of clusters.** The even-M steady state: single-species clusters grouped into two parity super-clusters.
- **Self-stirring.** The oscillating, cluster-free state at very weak self-attraction, which the authors suggest speeds mixing beyond passive diffusion. This is asserted and not measured.

## Connections

The paper extends the authors' earlier active phase separation in mixtures of chemically interacting particles (Agudo-Canalejo & Golestanian, PRL 2019; Ouazan-Reboul et al., EPJE 2021) from a single shared chemical to a cyclic network. It sits beside non-reciprocal Cahn–Hilliard models (Saha et al. 2020; You et al. 2020) and non-reciprocal phase transitions (Fruchart et al., Nature 2021). It is contrasted with Keller–Segel (the non-cyclic limit) and with Turing reaction–diffusion patterning (added in review). The authors distinguish their model by noting that each catalyst species is individually conserved, so "it is truly the catalysts and not the reactants that self-organize". Follow-ups by the same group (refs 54–55: self-repelling catalysts; motif-based classification) generalise to unequal parameters. For origin-of-life context, added in review, it cites Kauffman/RAF autocatalytic sets and RNA-network experiments. The model does not engage with them beyond citation.

## Bearing on the record

This is physics of active matter and origin-of-life theory. It carries **no instruction for machine-learning practice** and nothing for the Anthology of the SOTA. The dossier notes that non-Hermitian (here circulant, non-symmetric) interaction matrices also arise in learning dynamics. That is a mathematical kinship only: the paper makes no such link, and nothing in it transfers as a practice or a theory about training. Within this record it is a clean worked example of a spectral parity effect of cyclic non-reciprocal coupling, alongside other non-reciprocal and delay-induced oscillation papers. c36, delay-induced Hopf oscillations in random Lotka–Volterra, is the nearest in this batch.

## Limitations

- The nonlinear phase behaviour rests on simulations at two cycle lengths (M = 5, 6) and ten parameter sets (Table 1). "Odd vs even" is general at linear order only. The M = 5 oscillation is shown for one trajectory, with no ensemble statistics.
- The coarsening claim is stated three ways (exponential in the text, super-exponential in the Fig. 1e caption and in the authors' review reply) and is backed by a scaling argument plus qualitatively fitted curves.
- The periodic 3D simulations use minimum-image truncation of 1/r² interactions without Ewald summation, at φ = 0.005.
- All species have identical parameters. The authors cite their own later work for robustness but show none here.
- **The origin-of-life relevance is not tested.** The paper defines no metabolic output, efficiency or selection measure, so "advantage" (C7) is undefined. The most important hedge is not in the paper at all. Referee 2's final objection was that they knew of no nucleic acids or enzymes showing chemophoretic effects. The authors listed experimental chemotaxis reports and then wrote that "there isn't sufficient information about the µ's for specific catalysts in specific metabolic cycles relevant to pre-biotic chemistry for us to make quantitative claims" (Peer Review File, p. 9). That sentence decides how much of the abstract's framing is supported, and it lives only in the review file.
- The model has no chemical degradation or external supply, and no hydrodynamics. The far-field approximation ignores near-field phoretic corrections.

## Open questions

- Does the odd-cycle oscillatory steady state persist for larger odd M, e.g. M = 7 or the 11 of the citric acid cycle? The leading pair's Re/Im ratio changes with K (Eq. 11). Simulating M = 7, 9, 11 across the Eq. 11 boundary would settle it.
- Does the parity dichotomy survive heterogeneous α, μ(s), μ(p) and unequal densities? The authors defer this to refs 54–55.
- Do real catalysts have mobilities in the unstable region (μ(p) < μ(s)) at prebiotic concentrations? Measuring μ(s) and μ(p) for a two- or three-enzyme cascade (cf. Zhao et al., Nat. Chem. 2018) would test the premise directly.
- Does clustering actually increase cycle throughput? The paper cites enzyme co-clustering work (refs 15, 69) but computes no flux.

## Corrections to the seeded skim

- **The dossier describes an earlier text than the published one.** arXiv v1 (17 Mar 2023) is a shorter letter. The Nature Communications version adds a good deal, mostly in response to the referees:
  - the citric-acid-cycle remark;
  - the "glassy condensates" and Lifshitz–Slyozov argument in the introduction;
  - the Turing/reaction–diffusion comparison;
  - the full Methods section: the derivation of Eq. 13, the far-field pair velocities (Eqs. 14–18) and the Brownian dynamics set-up;
  - the simulation-parameter table (Table 1);
  - the "odd cycles may have an advantage" sentence.

  The v1 abstract is also different. It states the physics only (parity decides the outcome) and makes no origin-of-life claim. Equation numbers differ between versions: the even-M result is Eqs. 6–7 in v1 and Eqs. 7–8 in the journal. The dossier's numbering matches the journal.
- **Metabolic partners are not what cluster together.** The dossier's summary says the interactions "make metabolically linked partners cluster together". In the demonstrated cross-repelling case, direct metabolic partners (m, m±1) repel and separate. What co-aggregates is species of the same parity, i.e. second neighbours m and m±2 (Fig. 3a, Eq. 8). The odd cross-repelling case goes to M single-species clusters (Fig. 3b). Hybrid clusters of all same-parity species form only in the chasing regime (Supplementary Movie 5). The sentence the dossier echoes is the paper's own closing line ("molecules that are metabolically connected to each other will preferentially and efficiently form active clusters together", Discussion). The results support it only in the weak sense that the grouping is set by the reaction network.
- **The "molecule" phases are in the stable region.** The dossier lists "self-propelled or rotating molecules" among the phases that depend on chasing versus self-attraction strength. The paper places them in the *linearly stable*, self-repelling region (μ(p) − μ(s) > 0), as transient or long-lived small molecules in an otherwise homogeneous state (p. 4; Supplementary Fig. 3; Movies 1–2). They are not outcomes of the instability.
- **The coarsening rate is inconsistent.** The dossier says clustering is "exponentially fast". The paper says "exponential" in the text and abstract but "super-exponential" in the Fig. 1e caption. Its scaling argument, N(t) = N0 exp[(μα/D)∫ρ dt], yields exponential growth at constant ρ and super-exponential growth only if the density rises. Methods calls the growth-law determination "qualitative", from 100 runs per case at τ_tot = 400.
- **Fig. 1e and the growth-law Methods paragraph cross-reference the wrong panels and movies.** Fig. 1e says M = 5 is "see Fig. 3a and Supplementary Movie 7" and M = 6 is "see Fig. 3b and Movie 3". Fig. 3a is the even case (M = 6) and Fig. 3b the odd case. The Methods paragraph ("Cluster growth law determination") swaps the movies instead: it pairs "even" with Movie 7, but Table 1 and S3 make Movie 7 the M = 5 case. This is a labelling slip only; the saturation values (N/2 for M = 6, N/5 for M = 5) are consistent with the text. Ref. 55 is printed as "arXiv:22305.05472"; it is presumably 2305.05472 (unverified).
- **The citric-acid-cycle remark was added under review.** The dossier cites it (the cycle has 11 members) as part of the paper's argument. It entered in revision, in reply to Referee 1's question whether odd or even cycles would be favoured. The authors' reply calls it "speculated". The paper itself says only "It remains to be seen whether…".
