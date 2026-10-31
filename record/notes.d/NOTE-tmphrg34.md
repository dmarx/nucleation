---
status: Read
paper: 'LIT-tmpkp8vh'
title: 'Vellela & Qian — Schlögl model, stochastic and thermodynamic'
version: 1
history:
- version: 1
  date: '2026-10-31'
  note: >-
    Read in full from the PubMed Central copy of the version of record
    (PMC2838355, J. R. Soc. Interface 6, 925–940), fetched 2026-10-31 as
    HTML. The PMC PDF and the Royal Society PDF were refused to this
    client (a bot check and a 403); the HTML carries the full text, with
    every displayed equation as an image, and I read the equations
    (2.1)–(4.11), (A1)–(A12) and the figures from those images. Read:
    abstract, §§1–5, appendix A, footnotes 1–5, Table 1, the captions and
    curves of Figs. 1–12. Section numbers are the paper's; it has no
    page numbers in this copy. I checked numerically (my scripts, numpy
    and scipy): the fixed points and barrier heights of eq. (4.4); the
    slow eigenvalue λ₁ of the truncated master equation for V = 5–80
    against a Kramers-type sum; the asymptotic rates (3.29)–(3.30) and
    ratio (3.37)–(3.38); the volume-driven exchange of stability at
    a = 1, b = 2; and the Fokker–Planck counterexample of footnote 5.
date: '2026-10-31'
summary: >-
  The Schlögl model A + 2X ⇌ 3X, B ⇌ X, treated by rate equation, chemical
  master equation and nonequilibrium thermodynamics. Bistability needs the
  chemostats out of equilibrium; the master equation has one stationary
  distribution with two peaks, so in the long run which state the system
  occupies does not depend on where it started; the slow eigenvalue,
  exponentially small in volume, is the sum of the two escape rates; the
  more stable state can have the higher or the lower entropy production.
  The paper's asymptotic rate formula carries a spurious factor 1/V, so the
  "breakdown" of asymptotics it reports at small volume is mostly that
  factor.
---
<!-- inactive-ok-file: THEORY-671 LIT-1664 QUESTION-281 — Proposed, Unavailable or Open; the entries this reading bears on, cited as open -->

# NOTE-tmphrg34: Vellela & Qian — Schlögl model, stochastic and thermodynamic

## Contribution

A worked, integrated treatment of the canonical bistable chemical system
in three registers at once: the deterministic rate equation, the chemical
master equation (CME) and the nonequilibrium thermodynamics of the open
system. It adds four things to the older literature: the result that the
bistability requires a nonzero chemical potential difference between the
two chemostats; a stochastic entropy production rate that, unlike the
deterministic one, is single-valued, and its relation to the three
deterministic rates; a two-state reduction whose rate sum is the CME's slow
eigenvalue; and numerics comparing that eigenvalue with Monte Carlo and
with published large-volume asymptotics. Little of it is new as
mathematics; its value is the clean side-by-side.

## Key insight

A maintained state of a driven chemical system is a peak of a stationary
distribution, not a fixed point. The rate equation says the system stays
in whichever basin it starts in; the master equation says that it leaves
on a time exponentially long in the volume, and that in the long run the
fraction of time in each state is fixed by the parameters, "solely ...
(i.e. whether u(x₊)>u(x₋) or vice versa) and not on the initial condition"
(§3.4). The two descriptions agree for any fixed time as V → ∞ and
disagree when t → ∞ is taken first (Keizer's paradox, §3.4, appendix A).

## Assumptions

- **Well-mixed, one dynamical species.** Space is ignored (§1.2); A and B
  are chemostatted at fixed concentrations a, b (§2).
- **Mass-action propensities** λₙ = ak₁n(n − 1)/V + bk₃V,
  μₙ = nk₄ + k₂n(n − 1)(n − 2)/V² (eqs. 2.6–2.7), with concentrations and
  rate constants held fixed as V varies.
- **Every reaction reversible.** The thermodynamics needs it: the cycle
  free energy is ΔG = k_BT ln(k₁k₄a/(k₂k₃b)) (eq. 3.9), zero exactly at
  chemical detailed balance (eq. 3.10).
- **A one-dimensional birth–death chain**, so the stationary distribution
  is in closed form (eq. 2.8) and satisfies "mathematical detailed balance"
  even out of chemical equilibrium (§2, appendix A). Much of the paper's
  tractability rests on this; none of it transfers to two or more species.

## Key results

### Equilibrium and bistability (§3.1–3.2)

- At chemical detailed balance, k₁k₄a/(k₂k₃b) = 1, the stationary CME
  distribution is Poisson and the steady state unique (eqs. 3.3–3.5). With
  the paper's rates, a = 0.5 needs b = 29.5 (Fig. 1).
- Bistability (three steady states) occurs where the cubic's discriminant
  is negative (eq. 3.6, Fig. 2), which requires ΔG ≠ 0: "non-equilibrium
  conditions are shown to be necessary for bistability" (abstract). For
  k = (3, 0.6, 0.25, 2.95), a = b = 1 the steady states are 0.0935, 1.2041
  and 3.7024 (eq. 4.4; checked, the text prints "3.7024i"), and ΔG/k_BT =
  ln 59 ≈ 4.08. With a = 1 the bistable range is 0 < b < 3.278 (my scan).
- The deterministic entropy production rate at steady state i is
  ξᵢ = ΔG × J^ss_i (eq. 3.12), non-negative termwise (eqs. 3.13–3.14).

### Stochastic entropy production (§3.3)

- The CME's mean entropy production is ΔG times the stationary cycle flux
  (eq. 3.23), and ≈ V(ξ₊p₊ + ξ₋p₋) (eq. 3.27): the deterministic rates
  of the two stable states weighted by their probabilities. The middle
  (unstable) state's rate is not represented. As printed, eq. (3.26)–(3.27)
  weight by the single-site peak values p^ss at n±, which is O(V^{-1/2})
  of the well mass; the reading "weighted by their probabilities" needs the
  well masses. The qualitative conclusion is unaffected.
- **No extremum principle.** "The more stable of the two stable equilibria
  can have either a high or a low entropy production rate" (§3.3, Fig. 6);
  "the entropy production rate alone is unable to fully describe stability
  in the steady state" (§5). Fig. 7's negative slope of entropy production
  against barrier height, offered as support for least dissipation as a
  robustness principle, is one parameter sweep of one model.

### Two-state reduction and the slow eigenvalue (§§3.4, 4)

- Long-run dynamics: a two-state chain with rates r₋ (out of x₋) and r₊ (out
  of x₊), eq. (3.31); its nonzero eigenvalue −(r₊ + r₋) is the CME's
  second eigenvalue λ₁ (§4.1). Checked: λ₁ from the full tridiagonal
  generator matches the Kramers-type sum 1/(P₋P₊ Σₙ 1/(λₙpₙ)) to four
  digits for V = 40–80, and ln|λ₁| falls at slope ≈ −0.22 per unit V,
  the smaller barrier Δu₊ ≈ −0.222 (Fig. 12 gives −0.22 and −0.32;
  mine −0.2224 and −0.3185).
- Two slips in §3.4's prose, harmless downstream: the mean waiting time in
  a state is the inverse of the rate *out of* it, not "into that state";
  and the long-run probability of x₊ is r₋/(r₊ + r₋), as eq. (3.32)'s v₀
  correctly gives, not r₊/(r₊ + r₋) as the sentence before says.
- Eqs. (3.37)–(3.38) print the exponent as u(x₊) − u(x₋). With eq. (3.34)
  p ∝ e^{Vu}, the ratio P₋/P₊ has exponent V[u(x₋) − u(x₊)]; the exact CME
  confirms the latter (at V = 150, ln P₋/P₊ = 17.83, asymptote 17.32).

### The asymptotic rates are off by a factor of order V (my check)

- Eqs. (3.29)–(3.30) carry a prefactor ε = 1/V. Evaluated as printed they
  reproduce the dot-dashed "asymptotic" line of Fig. 11 exactly
  (ln λ₁ ≈ −12.2 at V = 40), and they fall below the exact λ₁ by a factor
  0.565V at V = 40 and 0.59V at V = 150: the gap grows without bound, so
  the claim that "eventually these lines should all converge as V increases
  further" (§4.3) fails for the formula as printed. Without the ε the
  formula stays within a constant factor ≈ 1.7 of λ₁ at every V checked.
  The paper attributes the gap to the asymptotics being "only valid for
  large volume systems" (§4.3) and the abstract reports "a breakdown of
  previously known asymptotic approximations on small volume scales".
  Most of that breakdown is the prefactor. Whether the ε is a
  transcription of Hinch & Chapman's time units, which I have not seen,
  I cannot say.

### Volume-driven exchange of stability (§3.1, Figs. 3–4, §5)

- At a = 1, b = 2 the dominant peak moves from x₋ to x₊ as V grows
  (Fig. 4). Checked: the lower well holds 73% of the mass at V = 10, 38% at
  V = 20 and 2% at V = 40. The paper says this "cannot be observed through
  studying the ODE model" and that "Asymptotic analysis ... predicts that
  one of the FCA will be more stable for all values of V" (§5). The second
  holds only if the O(1) prefactor is dropped: with it, ln P₋/P₊ ≈
  V[u(x₋) − u(x₊)] + ln C changes sign at V* ≈ 16.5, where the exact CME
  crosses between 10 and 20. The exchange is a finite-size competition
  between an O(1) curvature-and-rate prefactor and an O(V) barrier term,
  which footnote 2 itself describes in "enthalpic" and "entropic" terms.

### Fokker–Planck fails for the stationary state (appendix A)

- The exact CME gives ln P(k) ≈ V∫ ln(v/w) (eq. A3); the Fokker–Planck
  approximation gives −2V∫ (q − 1)/(q + 1) with q = w/v (eqs. A6–A8). They
  share extrema and curvatures there, but not the relative depth of the
  two wells (eq. A11). Checked footnote 5's counterexample (b = 1.305):
  ∫ ln q from x₋ to x₊ is +0.00166 and 2∫(q − 1)/(q + 1) is −0.00020, so as
  V → ∞ the CME concentrates on x₋ and the diffusion approximation on x₊.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Bistability of the Schlögl model requires a nonzero chemostat free-energy difference | strong | eqs. 3.3, 3.10 and the uniqueness of the Poisson equilibrium |
| C2 | For finite V the long-run occupation of the two states is independent of the initial condition; the deterministic dependence on it holds only for t ≪ 1/λ₁ | strong | eq. 2.8, §3.4; checked |
| C3 | λ₁ = −(r₊ + r₋), exponentially small in V | strong | §§3.4, 4; checked numerically |
| C4 | The more stable state may have the higher or the lower entropy production; neither minimum nor maximum EP selects it | moderate | Fig. 6, one model, one parameter sweep |
| C5 | Asymptotic rate formulas break down at small V | weak | the formula as printed has a spurious 1/V factor (my check) |
| C6 | Relative stability can exchange with V alone, which asymptotics cannot capture | moderate for the first half, wrong for the second | checked; asymptotics with the prefactor capture it |
| C7 | The diffusion approximation can select the wrong dominant state | strong | appendix A, footnote 5; checked |

## Concepts

- **Functional cellular attractor (FCA)** — a peak of the CME's stationary
  distribution, corresponding to a stable steady state of the rate
  equation (§1.2).
- **Chemical vs mathematical detailed balance** — every reaction balanced
  (equilibrium) versus only the total birth and death fluxes balanced at
  each n, which a one-dimensional chain always has (§3.1).
- **Keizer's paradox** — the V → ∞ and t → ∞ limits do not commute
  (§3.4, appendix A).

## Connections

- Hänggi et al. 1984 and Hinch & Chapman 2005 for the rates (cited);
  Keizer 1979; Horsthemke et al. 1977 on the Fokker–Planck failure.
- Falasco & Esposito's review ([LIT-tmpm46ks](../literature.d/LIT-tmpm46ks.md), §VII.A.1) redoes this model in
  the language of quasi-potentials and cites this paper for the two-state
  reduction and the diffusion failure; its eq. (243) is the closed form of
  this paper's u(x) with the opposite sign.
- Langer's decay of metastable states ([LIT-1664](../literature.d/LIT-1664.md), unread) is the
  equilibrium-nucleation counterpart.

## Bearing on the record

- **[CASE-tmpwxags](../cases.d/CASE-tmpwxags.md) and [CASE-111](../cases.d/CASE-111.md): what a fold becomes at finite size.** Both
  cases are deterministic, and in both a maintained regime "ends" at a
  saddle-node. This paper shows the stochastic reading of such a regime:
  it is a metastable state with a lifetime exponential in system size,
  lost by fluctuation long before the fold, and the barrier that sets the
  lifetime closes at the fold. In the Schlögl model I checked that it
  closes as (distance to fold)^{3/2} (barrier/(b* − b)^{3/2} = 0.064 for
  b* − b from 0.1 to 0.001). The cases' "regime ends at d ≈ 0.691" is the
  V → ∞ statement. Also: the cases use irreversible production and decay,
  which have no defined entropy production; a thermodynamic reading of
  them needs reverse reactions, as this paper's ΔG does.
- **[THEORY-671](../theory.d/THEORY-671.md) (maximum entropy production selects the steady state):
  a counterexample.** The more stable Schlögl state can carry either the
  higher or the lower entropy production ([THEORY-tmpshz26](../theory.d/THEORY-tmpshz26.md)).
- **[QUESTION-281](../questions.d/QUESTION-281.md)'s nucleation route**: a worked chemical example of
  passage across a finite barrier from a locally stable state, with the
  waiting time computed.
- Produces [THEORY-tmpwystk](../theory.d/THEORY-tmpwystk.md), [THEORY-tmpshz26](../theory.d/THEORY-tmpshz26.md) and, with the review,
  [THEORY-tmpkze5s](../theory.d/THEORY-tmpkze5s.md).

## Limitations

- One species; the closed-form stationary law is a one-dimensional
  accident.
- The numerical range (V ≤ 100) is small, and the asymptotic comparison is
  compromised by the prefactor.
- The entropy-production claims rest on one parameter sweep.

## Open questions

- Does the asymptotic formula without the ε factor, with the correct
  Kramers prefactor for a birth–death chain, close the remaining factor
  of ≈ 1.7? (A question about Hinch & Chapman, not held.)
