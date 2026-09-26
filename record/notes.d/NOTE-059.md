---
number: 59
status: Read
formerly:
- NOTE-tmpj57st
paper: LIT-035
title: 'Peters & Adamou 2022, the ergodicity solution of cooperation'
version: 2
history:
- version: 2
  date: '2026-09-25'
  note: >-
    Read in full (full text of the open-access version of record, Phil.
    Trans. R. Soc. A 380:20200425, from the Europe PMC XML (PMC9125229,
    saved as rawC4/c34.xml). The flattened rawC4/c34.txt drops every display
    equation and loses the √ in inline formulas, so I re-extracted all 31
    numbered equations (2.1–2.8, 3.1–3.9, 4.1–4.3, 5.1–5.13) and the key
    inline formulas directly from the MathML. I read everything: abstract,
    §1 Introduction, §2 Noisy multiplicative growth, §3 Cooperation
    protocol, §4 Ergodicity solution (including 4a, group selection), §5
    Generalizations (5a idiosyncratic entities, 5b correlated fluctuations,
    5c other), §6 Discussion, and the back matter. I did not read the ESI
    (the code cooperate.py, which generates Fig. 2) or view the Fig. 1–2
    images; their captions were read. The reference list is not in the XML
    body I had, so I cite references by number only.). Upgraded from
    `Skimmed` to `Read`: the claims table, assumptions and results are new,
    and the skim is corrected where the full text disagreed.
date: '2026-09-25'
summary: >-
  If N entities' resources follow GBM (drift μ, volatility σ, independent
  noise), then pooling and sharing equally every step leaves the drift at
  μ, cuts the volatility to σ/√N (Eq. 3.9), and raises each member's
  time-average growth rate from μ − σ²/2 to μ − σ²/(2N) (Eq. 4.1). The
  premium is (σ²/2)(1 − 1/N) (Eq. 4.2). With pairwise correlation ρ the
  effective volatility is σ√((1 + (N−1)ρ)/N), and the large-N limit is μ −
  σ²ρ/2 (Eqs. 5.12–5.13).
---

<!-- inactive-ok-file: LIT-047 — Proposed by its close reading; named in Connections -->

# NOTE-059: Peters & Adamou 2022, the ergodicity solution of cooperation

## Contribution

- A minimal model in which sharing is advantageous with no complementarity, no threshold, no relatedness and no reciprocity, only multiplicative noise. N identical GBM entities grow, pool, and split equally each step (Eqs. 3.3–3.4, Fig. 1). The shared process is again a GBM with the same drift and volatility σ/√N (Eq. 3.9).
- Closed-form time-average growth rates for three cases:
  - identical members (Eq. 4.1);
  - heterogeneous members (Eq. 5.5), with join and admit conditions (Eqs. 5.6–5.7);
  - equicorrelated noise (Eqs. 5.12–5.13).
- An argument that, because the ensemble-average rate μ is unchanged by sharing, analyses built on expectations see no reason to cooperate, while the time-average rate μ − σ²/2 that a single trajectory achieves does see one (§4).

## Key insight

Under multiplicative noise, fluctuations cost growth: a single trajectory grows at μ − σ²/2, not μ. Averaging resources across independent trajectories every period removes variance without removing drift. So sharing converts variance into long-run growth for every participant, and the pooled members out-grow even the arithmetic mean of an equal number of non-sharers ("cooperation and averaging are not equivalent operations", §4).

## Assumptions

- **Dynamics.** Resources follow GBM, dx_i = x_i(μ dt + σ dW_i), with independent Wiener increments. This is unconstrained self-reproduction: the authors state that growth limited by resources, space or predation "would be poorly described" by it (§2).
- **GBM as an attractor.** Justified by the CLT on log-increments over many steps (§2). This requires finite-variance, weakly dependent log-increments.
- **Pooling.** Complete and equal pooling at every step Δt, with Δt → 0 in the continuous-time result. There is no cost of sharing and no benefit beyond variance reduction (§3).
- **Pacts cannot be broken** in the main result. Cheating and walk-away are set aside, with "ignore-for-tat" enforcement only sketched (§4a).
- **The criterion is the time-average growth rate** ḡ = lim_{T→∞} (1/T) ln(x(T)/x(0)). The claim that the entity with the highest ḡ comes to dominate is the paper's selection criterion (§2).
- **Correlated case.** Equal pairwise correlation ρ ≥ −1/(N−1) (Eq. 5.8).

## Key results

- **Eq. 2.4**: g(x_i, T) ~ N(μ − σ²/2, σ²/T). **Eq. 2.8**: ḡ(x_i) = μ − σ²/2. **Eq. 2.7**: the ensemble rate is g(⟨x⟩) = μ.
- **Eq. 3.9**: dy^(N) = y^(N)(μ dt + (σ/√N) dW^(N)).
- **Eq. 4.1**: ḡ(y^(N)) = μ − σ²/(2N). **Eq. 4.2**: premium = (σ²/2)(1 − 1/N). **Eq. 4.3**: → μ as N → ∞.
- **Eqs. 5.3, 5.5 (heterogeneous)**: μ^(N) = (1/N)Σμ_i and σ^(N) = (1/N)√(Σσ_i²), giving ḡ = (1/N)Σ(μ_i − σ_i²/(2N)).
- **Eqs. 5.9, 5.12, 5.13 (correlated)**: Σξ_i ~ N(0, N + N(N−1)ρ); σ_corr = σ√((1 + (N−1)ρ)/N); and ḡ → μ − σ²ρ/2 as N → ∞.
- **Fig. 2** (simulation; μ = 0.15, σ² = 0.2, Δt = 0.1): one pair of cooperators vs two non-cooperators and their mean. The implied rates are 0.05 for a non-cooperator and 0.10 for a pair member (my arithmetic from Eq. 4.1).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Equal pooling among N independent GBMs leaves drift μ and reduces volatility to σ/√N | strong | derivation, Eqs. 3.6–3.9 |
| C2 | Each cooperator's time-average growth rate rises to μ − σ²/(2N), premium (σ²/2)(1 − 1/N), with the largest marginal gains at small N | strong | Eqs. 4.1–4.2 (within the model) |
| C3 | Cooperators out-grow the arithmetic average of the same number of non-cooperators | strong (as a long-time statement) | Fig. 2 simulation; follows from C2, since a finite sum of independent GBMs grows at μ − σ²/2 almost surely |
| C4 | With equicorrelated noise, a benefit exists iff ρ < 1, and the many-member limit is μ − σ²ρ/2 | strong | Eqs. 5.9–5.13 |
| C5 | Heterogeneous entities benefit from joining iff Eq. 5.6 holds, so highly skilled members may do better alone | strong | Eqs. 5.5–5.7 |
| C6 | This is a candidate explanation for cooperation in rudimentary settings (for example unicellular to multicellular) | weak | informal argument (§1, §6); no biological model or data |
| C7 | Cooperation is the behavioural baseline, and its absence needs special explanation | weak | follows only under the model's zero-cost, no-defection, unconstrained-growth assumptions (§6) |
| C8 | An "ignore-for-tat" policy suffices to protect the cooperative from pact-breakers, even with imperfect detection | weak | informal argument (§4a); no invasion or stability analysis |
| C9 | The growth benefit is an overlooked rationale for insurance, pensions and taxation | weak | assertion (§6) |

## Method

1. Non-cooperators: discrete GBM, Δx_i = x_i(μΔt + σξ_i√Δt) with ξ_i ~ N(0,1) (Eqs. 3.1–3.2).
2. Cooperators: each grows from the common per-capita level y^(N), then the pool is split equally (Eqs. 3.3–3.4).
3. Replace the sum of the N normals by one equivalent standard normal, ξ^(N) = Σξ_i/√N (Eq. 3.7). Take Δt → 0 to get a GBM with volatility σ/√N.
4. Apply the GBM time-average formula μ − σ²/2 to each case. Generalize to (μ_i, σ_i) (Eqs. 5.1–5.5) and to equicorrelated ξ (Eqs. 5.8–5.12).

## Concepts

- **ensemble-average growth rate** g(⟨x⟩) — the growth rate of the population mean in the infinite-population limit, equal to μ (Eq. 2.7).
- **time-average growth rate** ḡ(x_i) — the long-time growth rate of a single trajectory, μ − σ²/2 (Eq. 2.8). Their inequality is what the paper calls non-ergodicity.
- **cooperation** — repeated pooling and equal sharing of resources, and nothing more (§1, §3).
- **ignore-for-tat** — refusing future interaction with past pact-breakers (§4a).
- **σ_corr** — the effective volatility of a cooperative with pairwise noise correlation ρ (Eq. 5.12).

## Connections

- **Geometric-mean fitness and bet-hedging.** The paper sits squarely in this literature (refs 8–17 as cited in §1): Starrfelt & Kokko, Schreiber, and Kennedy et al., for whom this is a special case. It chooses "growth rates, not fitness" as its language.
- **Earlier derivations of the same variance.** McCloskey (the medieval field-scattering literature) and Winterhalder (forager food sharing) derive the same pooled-variance expression, per §5b. Uitdehaag's anticorrelated-specialist mutualism is the N = 2, ρ = −1 extreme.
- **Extensions by others.** §5c points to partial pooling (Berman et al.), network pooling (Stojkoski et al.) and binary-outcome processes (Yaari & Solomon).
- **Programme.** The paper presents itself as part of ergodicity economics (ref. 4, Peters 2019).
- **In this record.** It pairs with [LIT-047](../literature.d/LIT-047.md) (Curry et al.) as a quite different explanation of cooperation: a game-theoretic "solutions to cooperation problems" account on the one hand, a variance-reduction account on the other. It also relates to the individuality and major-transitions cluster through its unicellular-to-multicellular remark.

## Bearing on the record

There is no instruction for ML practice. The underlying mathematics (log-growth, the μ − σ²/2 volatility drag, Kelly-style time-average criteria) is standard and has no specific bearing on any anthology practice. If a THEORY document in this record makes a variance-reduction or "time-average vs ensemble-average" argument about cooperation or individuality, this paper supports the mathematics but not the evolutionary claim.

## Limitations

- **Zero-cost, perfect, continuous pooling.** The authors acknowledge that coordination costs "may … make cooperation disadvantageous" (§3), but no cost term is analysed, so the paper cannot say when cooperation stops paying.
- **Defection and invasion** are explicitly out of scope ("we refrain from further development", §4a). Yet the "baseline" claim depends on cooperation being stable against pact-breakers.
- **Unconstrained growth.** GBM is the authors' stated limitation. Under carrying-capacity limits the premium's form is not derived.
- **Time average as the criterion.** Selection on the time-average rate is asserted as what matters for dominance over long times. Finite horizons and population structure are not treated.
- **The unicellular-to-multicellular application** is a suggestion without a model.
- **The title** ("The ergodicity solution of the cooperation puzzle") claims more than the body: the body shows a sufficient mechanism in an idealized model, which the abstract more modestly calls a "candidate explanation".

## Open questions

- With a per-step sharing cost c, or partial pooling fraction f, what is the break-even? Presumably σ²(1 − 1/N)/2 > c, but that is not derived here.
- Is full pooling evolutionarily stable against a mutant that shares only when it has lost, in the same GBM setting? That calls for an invasion analysis.
- Does any empirical system (for example early multicellular aggregates or microbial public-goods sharing) show the predicted 1 − 1/N scaling of the growth benefit?

## Corrections to the seeded skim

- Volatility. The dossier says the text "renders the volatility as 'σ/N'" but that the stated rate implies variance σ²/N. The version of record has σ/√N throughout: Eq. 3.7 defines ξ^(N) = (1/√N)Σξ_i; Eqs. 3.8–3.9 have σ/√N; the prose says "amplitude is 1/√N times" (§3); and "σ_corr → σ/√N as ρ → 0" (§5b). The "σ/N" in the flattened text is an extraction artefact (the √ was dropped), not a typo in the paper. The dossier's summary line ("variance from σ² to σ²/N") is correct.
- Correlated case. The dossier asks whether the premium vanishes as ρ → 1. It does, exactly and only there: 0 ≤ σ_corr ≤ σ, with σ_corr = σ iff ρ = 1 (§5b). Also:
  - Validity requires ρ ≥ −1/(N−1). Perfect anticorrelation is possible only for N = 2, which gives σ_corr = 0 and the full ensemble rate μ.
  - With many members, the benefit caps at μ − σ²ρ/2 (Eq. 5.13).
  - The paper calls ρ a "covariance". With unit-variance ξ it equals the correlation.
- Unequal members. The dossier asks "when leaders should share with laggards" without the answer, which is given in closed form:
  - The cooperative's rate is (1/N)Σ(μ_i − σ_i²/(2N)) (Eq. 5.5).
  - Entity j gains by joining iff that exceeds μ_j − σ_j²/2 (Eq. 5.6).
  - The group gains by admitting j iff that exceeds the (N−1)-member rate (Eq. 5.7).
  - So a sufficiently superior member does better alone, and the paper names "skill differences" as a reason cooperation can be absent (§6).
- Framing vs the known literature. The dossier notes that ergodicity economics is contested. More to the point, the paper itself says:
  - McCloskey (land scattering) and Winterhalder (forager food sharing) "obtain the same expression for the variance" (§5b).
  - Uitdehaag studied "a model similar to ours".
  - Kennedy et al. treat it as a special case of a general cooperation model with relatedness (§1).
  The novelty is the time-average framing and the "baseline" claim, not the result.
- Dates. Received 30 Apr 2021, accepted 20 Oct 2021, issue date 11 Jul 2022, 380(2227). The dossier's 2022-05-23 online date is from Crossref and was not contradicted. Whether arXiv:1506.03414 is an earlier form remains unverified; this text does not cite it.
