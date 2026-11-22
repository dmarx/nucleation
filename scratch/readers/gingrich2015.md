# Reader notes: gingrich2015 (LIT-2981)

Gingrich, Horowitz, Perunov & England, "Dissipation bounds all steady-state
current fluctuations", arXiv 1512.02212v3 (4 Feb 2016), Phys. Rev. Lett. 116,
120601 (2016), doi:10.1103/PhysRevLett.116.120601 (journal ref and DOI from the
arXiv API, 2026-11-22, no email sent).

## Provenance and copies located

- https://arxiv.org/pdf/1512.02212 : arXiv PDF, v3, 5 pages. Fetched
  2026-11-22, no obstacle. Kind: arXiv (author's manuscript of the published
  letter). Used to confirm the version stamp and page count.
- https://arxiv.org/e-print/1512.02212 : arXiv LaTeX source (bound.tex,
  bound.bbl, three figure PDFs), v3. Fetched 2026-11-22, no obstacle. **Read
  in full**: abstract, main text, all three figure captions, the Derivation
  section, acknowledgments. Skipped: the bibliography beyond the entries cited
  in the text; figures viewed only through their captions.
- Published PRL version (doi above): not sought; the arXiv v3 postdates
  acceptance-era corrections (acknowledgment thanks Chetrite and a referee
  "for identifying an error in an earlier draft"). No paywalled copy was used.
- Downloads at /tmp/claude-0/-home-user-nucleation/63921577-b6c0-500a-97b6-9cee22fffb6e/scratchpad/downloads/gingrich2015/arxiv/ (not committed).

Status outcome: read in full. No neighbour needed.

## Summary

For an ergodic continuous-time Markov jump process with reversible edges and
local detailed balance, in its steady state, the authors prove that the
large-deviation rate function of the vector of empirical edge currents lies
below a quadratic "linear-response" form weighted by each edge's entropy
production. Contracting to any scalar linear combination of currents (a
generalized current j_d) gives a weaker bound in terms of the total
dissipation rate Σ^π alone. Since both bounds share the minimum of I, the
curvature at the minimum gives the variance, and the thermodynamic
uncertainty relation conjectured by Barato and Seifert follows: ε²_d Σ^π ≥ 2.
The proof is short: level-2.5 large deviations, contraction evaluated at the
steady-state density, then an edgewise quadratic upper bound on the level-2.5
function. Illustrated numerically on a 4-state multicyclic graph and on an
open-boundary ASEP with L = 15.

## Contribution

The first general proof of the thermodynamic uncertainty relation for
steady-state currents in Markov jump processes, including multicyclic
networks far from equilibrium, which Barato and Seifert (LIT-1885) had shown
only within linear response and for unicyclic networks and had otherwise
conjectured. More than the TUR: a bound on the whole rate function, so on
rare as well as typical fluctuations.

## Key results (section references are to the arXiv v3 text)

1. **Edgewise bound on the current rate function** (main text, eq. 3):
   "I(j) ≤ I_LR(j) = Σ_{y<z} (j(y,z) − j^π(y,z))² / (4 j^π(y,z)²) · σ^π(y,z)".
   Saturated at j = j^π and at j = −j^π, "as our bound also satisfies the
   fluctuation theorem for currents".
2. **Generalized-current bound** (eq. 4): "I(j_d) ≤ I_WLR(j_d) =
   (j_d − j^π_d)² / (4 (j^π_d)²) · Σ^π"; "this bound is tightest, and indeed
   as strong as the linear-response bound, when d = F", giving for the
   dissipation itself I(Σ) ≤ (Σ − Σ^π)²/(4Σ^π) (eq. 5).
3. **The TUR as corollary** (eq. 8): "we have a general proof of the
   conjectured thermodynamic uncertainty relation [Barato2015]. Namely, the
   relative uncertainty in a generalized current ε²_d = Var(j_d)/(j^π_d)² ...
   verifies the inequality ε²_d Σ^π ≥ 2." Var here is the long-time scaled
   variance, from I''(j^π_d) = 1/Var(j_d). Also an edgewise TUR,
   Var(j(y,z)) ≥ 2 j^π(y,z)²/σ^π(y,z), tighter than the generalized one.
4. **Direction of the deviation from linear response** (abstract; main
   text): "nonequilibrium current fluctuations are always more likely than
   what is expected from a linear-response analysis". The bounds "are not
   quadratic truncations of I for small currents, but originate in a
   linear-response expansion about small force or entropy production".
   Expansion (eq. 13): the first-order term in F is the linear-response
   Gaussian; "All higher order corrections must have a negative sum."
5. **Design principle** (closing discussion): "for fixed average
   dissipation and current, the fluctuations are most suppressed in a
   near-equilibrium process ... with a fixed energy budget, it is impossible
   to surpass the linear-response bound, no matter how complex the design."
6. **Derivation** (Derivation section): level-2.5 rate function (eqs.
   9–10), contraction I(j) = inf_p I(p,j) bounded by evaluating at p = π
   (eq. 11), then Ψ(j, j̄, a) ≤ (j − j̄)²/(4j̄²) · 2j̄ arcsinh(j̄/a) (eq. 12),
   with σ^π = 2j^π arcsinh(j^π/a^π). The WLR bound evaluates I_LR at the
   trial current j* = (j_d/j^π_d) j^π, which is conservative because it is
   proportional to the steady current. The exact contracted LR bound is
   (j_d − j^π_d)² B⁻¹₀₀/4 (eq. 16), with B⁻¹₀₀ = 1/Σ^π when d ∝ F.
7. **Priority note**: "we became aware of the preprint by Pietzonka,
   Barato, and Seifert [arXiv 1512.01221], which conjectures (4) as a
   universal bound."

## Assumptions

- Finite state space, continuous-time Markov jump process, ergodic, unique
  steady state π.
- Every transition reversible: r(z,y) > 0 whenever r(y,z) > 0.
- Local detailed balance, so F(y,z) = ln[π(y)r(y,z)/(π(z)r(z,y))] is the
  dissipation of a jump.
- Steady state and the long-time (large-deviation) limit; currents that are
  linear combinations of edge currents (antisymmetric increments). Not
  occupation/density observables, not finite time, not time-dependent
  driving, not overdamped diffusions or underdamped dynamics as such.
- k_B = 1.

## Concepts

Thermodynamic uncertainty relation; empirical (integrated) current; large
deviation principle and rate function; level-2.5 large deviations;
contraction principle; scaled cumulant generating function via tilted
generator; local detailed balance; generalized current j_d = ⟨d, j⟩;
edgewise entropy production σ^π; linear-response bound I_LR and its weakening
I_WLR; fluctuation theorem for currents (symmetry at −j^π); ASEP.

## My check

Script at /tmp/claude-0/-home-user-nucleation/63921577-b6c0-500a-97b6-9cee22fffb6e/scratchpad/scripts/ging.py.
With the Fig. 2 rates: Σ^π = 6.271. Over the dissipation current and 299
random generalized currents d(y,z) ∈ [−1, 1), min ε²_d Σ^π = 2.340, attained
at d = F (tightest, as the paper says); I_WLR − I ≥ −2×10⁻⁶ at the six
sampled points per current (Legendre transform on z ∈ [−4, 4]), and for d = F
the gap at j = −Σ^π is −2×10⁻⁶, i.e. saturation to numerical precision. The
grid-limited Legendre transform can only underestimate I, so the bound check
is weaker than the TUR check.

## Verdict on the exchange's characterization

A26 (exchange_full.txt lines ~6803–6811) gives the TUR as
Var(J_T)/⟨J_T⟩² ≥ 2/⟨Σ_T⟩ for "a suitable integrated current", with Σ_T
the total entropy production over the interval in units of k_B, and says it
"applies under specified assumptions, particularly for steady-state currents
in continuous-time Markov jump processes; other dynamics require modified
bounds". **Accurate.** It is the paper's eq. 8 written for integrated
quantities (Var(J_T) = T·Var(j), ⟨Σ_T⟩ = TΣ^π, asymptotically in T). Two
qualifications: "suitable" means any linear combination of edge currents
(the paper's point is that it holds for all of them); and the relation is
asymptotic in T here (the paper's variance is the large-T scaled one;
finite-time versions came later and are not in this paper). The exchange's
gloss, "a smaller relative variance requires a sufficiently large entropy
budget", is the paper's "reducing current fluctuations carries a
fundamental energetic cost". LIT-2981's summary ("A proof that entropy
production bounds the fluctuations of every current in a nonequilibrium
steady state, the general form of the TUR") is right; its date in prose
says 2016 (PRL), arXiv posting 2015-12-07 is correct in `published`. It
omits that the result is a bound on the full rate function, not only the
variance, and that it covers Markov jump processes only.

## Bearing on codes

- **LIT-2981** (this work): read; can move from Deferred. Add
  `doi: 10.1103/PhysRevLett.116.120601` beside the arXiv id if the scheme
  allows.
- **THEORY-1268** (Barato & Seifert, Active): **supports and completes**.
  THEORY-1268's "What this does not say" reads "That the general case is
  proved here. Proofs for general networks came later and are not held."
  This paper is that proof: "we have a general proof of the conjectured
  thermodynamic uncertainty relation" (eq. 8), for any network and any
  current, with "these uncertainty relations are tightest in linear response
  and when d ∝ F, as predicted by Barato and Seifert". THEORY-1268 should get
  a dated note pointing here; its title's "states it as a conjecture" stays
  true of the 2015 letter.
- **LIT-1885** (Barato & Seifert): background/parallel; the conjecture this
  paper proves.
- **QUESTION-452** (Open; precision of maintained organization vs
  dissipation): **qualifies / leaves open**. It sharpens the first item of
  "what would count as an answer": the bound holds for any linear
  combination of edge currents of a Markov jump network, far from
  equilibrium, and for rare fluctuations too, so if maintenance is such a
  current the price applies. It does not settle whether maintenance is a
  current, and it says nothing about occupations (how exactly a state is
  held), which is the question's second worry. The design-principle passage
  ("impossible to surpass the linear-response bound, no matter how complex
  the design") rules out buying precision cheaply by adding metabolic
  cycles, a point the question can use.
- **THEORY-1830 / LIT-2547** (Tu, energy–speed–accuracy): contrast. Tu
  prices adaptation accuracy logarithmically; this paper prices current
  precision as 1/ε². Different observables; no conflict, as the note on
  THEORY-1268 already says.
- **THEORY-431** (fluctuation theorems): parallel. The bound respects the
  current fluctuation theorem: saturation at j = −j^π.
- **TERM-062** (causal state), which the curation entry names as holding
  this work's ideas: **no bearing**. That pairing looks like a mix-up with
  Shalizi 2003 (LIT-2996); the Gingrich ideas are held in THEORY-1268, as
  the curation line also says.
- **Exchange-batch claims (CLAIM-795 to CLAIM-850)**: none uses the TUR; the
  A26 "precision versus energetic cost" passage was not filed as a claim
  (curation entry line 163: "cited by no filed entry").

## Recheck (second search of record/)

Searched: 1512.02212, Pietzonka, "level 2.5", "large deviation", "rate
function", "contraction principle", "current fluctuation", "fluctuation
theorem", ASEP/"exclusion process", Barato, Horowitz, "energy–accuracy",
"speed–accuracy", "cost of precision".

- Not held: Pietzonka, Barato & Seifert 2015/16 (arXiv 1512.01221), the
  companion conjecture of eq. 4; nothing on level-2.5 large deviations.
- Missed by the first search and bearing: **QUESTION-452** (named above);
  **THEORY-1830 / LIT-2547** (contrast); **THEORY-431** (parallel).
- Large-deviation entries found (THEORY-1366 Freidlin–Wentzell, CLAIM-815,
  LIT-1892 macroscopic stochastic thermodynamics, contraction-principle
  hits in QUESTION-046, CLAIM-165, CLAIM-355): background only; same
  apparatus, different objects. LIT-1892 (Macroscopic stochastic
  thermodynamics) is the nearest held neighbour in method.
- "speed–accuracy" hits LIT-569/576 (decision models) and procedural-skill
  meta-analyses: unrelated.

## Limitations

- Markov jump processes with reversible transitions only; one-way
  transitions make F infinite and the bound vacuous (as THEORY-1268 notes).
- Long-time, steady-state currents only; not finite-time, not periodically
  driven, not occupation observables, not underdamped dynamics.
- The bound is tight only near equilibrium and for d ∝ F; far from
  equilibrium generic currents sit well inside it (Fig. 2 inset).
- Bounds dissipation from below given precision; says nothing about which
  state a system selects (not an extremum principle).
- The numerical illustrations are two models; the result itself is proved.

## Candidate THEORY sentence

For an ergodic Markov jump network with reversible transitions obeying local
detailed balance, in its nonequilibrium steady state, the large-deviation
rate function of any current that is a linear combination of edge currents is
bounded above by the quadratic (j_d − j^π_d)²Σ^π/(4(j^π_d)²), so current
fluctuations far from equilibrium are always at least as likely as linear
response predicts, and as a corollary every such current obeys the
thermodynamic uncertainty relation ε²_d Σ^π ≥ 2, the bound being tightest
for the dissipation current itself and in linear response.

`promote_when`: the proof in the Derivation section (level-2.5 rate function,
contraction at p = π, the edgewise quadratic bound on Ψ, and the trial
current j*) has been checked step by step, and the inequality ε²_d Σ^π ≥ 2
with saturation of I(Σ) at Σ = ±Σ^π has been reproduced numerically on at
least one multicyclic network. (The filer's check above does the numerical
half on the Fig. 2 network; the step-by-step proof check remains.)

Other works read: none beyond this paper.
