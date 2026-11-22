# Reader notes: mermin1966 (LIT-2985)

Mermin and Wagner (1966), "Absence of Ferromagnetism or Antiferromagnetism
in One- or Two-Dimensional Isotropic Heisenberg Models", PRL 17, 1133,
doi:10.1103/PhysRevLett.17.1133. Read on 2026-11-22.

## Outcome

**The original was not read: Unavailable** (ADR-041). No lawful copy was
found; the only copy located is the publisher's, which is paywalled and sat
behind a Cloudflare challenge. **Two neighbours read in full**, one course
note read in full; everything below about the 1966 paper is what these
neighbours say of it, not a reading of it. Nothing is written from memory.

## Copies located (2026-11-22)

| Address | Kind | Outcome |
|---|---|---|
| https://journals.aps.org/prl/pdf/10.1103/PhysRevLett.17.1133 | publisher PDF (paywalled) | HTTP 403, Cloudflare "Just a moment..." challenge. Stopped, not retried. |
| https://link.aps.org/abstract/PRL/v17/p1133, https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.17.1133 | publisher abstract | HTTP 403 (same challenge). Stopped. |
| OpenAlex `works/doi:10.1103/PhysRevLett.17.1133` | catalogue | `oa_status: closed`, one location (doi.org), no repository copy. |
| Unpaywall (email=noreply@anthropic.com) | catalogue | `is_oa: false`, no OA location. |
| Semantic Scholar API | catalogue | `openAccessPdf.status: CLOSED`. |
| bibsonomy.org/bibtex/1be5adaba7290786b97f942735a67c3e2 | bibliography entry naming a "Mermin1966.pdf" attachment | not a reachable copy; not pursued. |
| Web searches (three) for a course or reading-list copy | — | none found. |

So the status for LIT-2985 is **Unavailable** (only a paywalled copy), not
Unfetched: the Cloudflare challenge was on the paywalled publisher copy,
which is not a lawful-copy route anyway.

Neighbour copies located:

| Address | Kind | Outcome |
|---|---|---|
| https://arxiv.org/pdf/1812.00220 (v2, 14 Dec 2018) | arXiv, author's paper | **read in full** (5 pp.) |
| https://arxiv.org/pdf/cond-mat/0106090 (v1, 5 Jun 2001) | arXiv, authors' accepted manuscript (J. Phys.: Condens. Matter 2001) | **read**: §§1–2.3, §3 intro to §3.2, §3.4, §4 opening, §5; skipped §2.4 generalized inequalities, §§3.1, 3.3 detail (films, Hubbard, PAM), most of §4 |
| https://www.math.ucdavis.edu/~bxn/mermin-wagner.pdf | course notes (MAT266, UC Davis, Winter 2006), faculty page | **read in full** (6 pp.) |
| https://www.weizmann.ac.il/condmat/oreg/sites/condmat.oreg/files/uploads/2021/mermin_wagner_tutorial.pdf | course tutorial | not read: curl (52) empty reply from server, 2026-11-22 (Unfetched-type; neighbour only) |
| https://www.soft-matter.uni-tuebingen.de/teaching/vorlesung_atcoma_ws24/14.%20Mermin-Wagner%20theorem.pdf | lecture slides | not read: curl (35) connection reset by peer, 2026-11-22 |

None of the three neighbours is held in record/literature.d (grep for
1812.00220, 0106090, Halperin, Gelfert, Nachtergaele: no hit).

## Neighbour 1: Halperin, "On the Hohenberg-Mermin-Wagner theorem and its limitations", arXiv:1812.00220

**How far it stands in.** Best stand-in for the paper's *scope*: it states
what Mermin–Wagner proved, on what model, under what condition, and what
the theorem does not imply. It does not reproduce the MW proof; it gives
the inequality used and runs the same argument for itinerant electrons.

**Summary.** A short retrospective by a contemporary: the history of the
Hohenberg and Mermin–Wagner proofs, the limits of the rigorous theorem
(quasi-long-range order, long-range interactions, orientational order,
tethered membranes, T = 0), and an extension ruling out ferromagnetism in
2D itinerant electron systems with SU(2) symmetry.

**Key results, with passages.**
- *What MW proved* (§I): "a similar proof of the absence of long-range
  order in one and two dimensions for a Heisenberg ferromagnet or
  antiferromagnet, with SU(2) symmetry, or a magnetic system with U(1)
  symmetry and an order parameter perpendicular to the symmetry axis."
- *Priority* (§I): Hohenberg's paper was received 24 October 1966; MW was
  submitted "a week before" and appeared "some six months before Pierre's";
  the proofs "should be properly referred to collectively as the
  'Hohenberg-Mermin-Wagner theorem'". MW "clearly state ... that their own
  work was, in fact, inspired by discussions with Pierre."
- *The range condition* (§II, "Long-range interactions"): with second
  moments K_αβ ≡ Σ_r r_α r_β J(r), "The argument for the non-existence of
  long-range order, as given in the Mermin-Wagner paper requires that these
  second moments be finite." For ferromagnetic J falling "slower than
  1/r^4", "we expect that long-range ferromagnetic order should indeed be
  possible in two dimensions".
- *What it does not say* (§II): "The HMW theorem sheds no light on the
  question of whether quasi-long-range order can exist in any particular
  system." And "It has sometimes been suggested that the HMW theorem ...
  rule[s] out the possibility of long-range order at T ≠ 0 in any
  two-dimensional system where the order parameter would break a
  continuous symmetry. However, this is not completely correct": bond
  orientational order in a 2D crystal can be long-range, because "the
  generator of these rotations cannot be written as an unweighted sum of
  local operators".
- *T = 0* (§II): "The HMW theorem has nothing to say about the existence or
  non-existence of long-range order in a quantum mechanical system at T = 0."
- *The heuristic behind it* (§II): ρ_s/2 ∫|∇θ|² gives phase variance
  ∝ T/(ρ_s k²), ⟨[θ(r) − θ(0)]²⟩ ∼ (T/πρ_s) log r, and
  ⟨a(r)a*(0)⟩ ∼ r^(−T/(2πρ_s)) (eqs. 2–3); for Heisenberg, correlations
  "decay exponentially with distance at any non-zero temperature".
- *The inequality* (§III, eq. 12): "{A, A†} ≥ T χ_{A,A}", which "follows
  directly from the quantum version of the fluctuation dissipation theorem."
- *Membranes* (§II): Gaussian fluctuations of the normal diverge, but
  nonlinear coupling renormalizes κ, which "diverges for k → 0", so
  long-range orientational order is predicted to survive.

## Neighbour 2: Gelfert and Nolting, "The absence of finite-temperature phase transitions in low-dimensional many-body models: a survey and new results", arXiv:cond-mat/0106090

**How far it stands in.** Closest stand-in for the *proof*: §3 "briefly
outline[s] the paradigmatic procedure" of Mermin and Wagner step by step,
with the operators, bounds and integral; the bounds (47)–(48) are stated
"as has been shown by Mermin and Wagner", not re-derived.

**Key results, with passages.**
- *Bogoliubov inequality* (§2.3, eq. 9): |⟨[C, A]⟩|² ≤ (β/2) ⟨{A, A†}⟩
  ⟨[[C, H], C†]⟩, proved by a Schwarz inequality on an energy-weighted
  scalar product.
- *MW's procedure* (§3, eqs. 41–52): Heisenberg model with field b coupling
  to e^(−iK·R_i) S_i^z (K handles antiferromagnetism); A = S⁻(−k − K),
  C = S⁺(k); the double commutator is bounded by ξ₂N|B₀M| + ξ₃k²; in 2D
  the k-integral gives M² ≤ ξ₄β / ln(1 + ξ₃k₀²/|B₀M|). "As B0 → 0, the
  denominator diverges logarithmically, thus forcing the magnetization to
  vanish. This result is independent of the original choice of the
  auxiliary wave vector K ..., so that both ferromagnetic and
  antiferromagnetic order is ruled out in the two-dimensional Heisenberg
  model." 1D is "a similar divergence".
- *The integral it rests on* (§3.2, eq. 63): the scheme "ultimately rests
  on the divergence of the integral ∫_{k≤k0} d^Dk / k² in one or two
  dimensions".
- *Classical case* (§3): "Mermin showed that a classical Bogoliubov-type
  inequality holds" (J. Math. Phys. 8, 1061, 1967), ruling out order in
  the infinite-spin limit for short-range interactions.
- *Graphs and fractals* (§3.4): Hattori, Hattori and Watanabe (Prog. Theor.
  Phys. Suppl. 92, 1987) ask "Why do the spins on the lattice 'know' this
  natural embedding into Euclidean space ...?", since "the only geometrical
  structure that spins can feel is ... the 'network structure of the
  interaction'"; they define the spectral dimension of general networks.
  Cassi (Physica A 191, 1992) shows that "on fractal and disordered
  lattices whose spectral dimension is less or equal to 2 ... at finite
  temperature no spontaneous magnetization can exist for the classical
  O(n) and the ferromagnetic (quantum) Heisenberg model. This is due to the
  infrared divergencies displayed by the corresponding Gaussian models".
- *Approximations* (§4): mean-field-type methods "consistently predict
  finite-temperature phase transitions in one or two dimensions" for models
  that obey the theorem.

## Neighbour 3: Nachtergaele, "The Mermin-Wagner Theorem", UCD MAT266 notes (2006)

**How far it stands in.** A different, operator-algebraic proof
(energy-entropy balance on KMS states), more general than MW's; it does not
use the Bogoliubov inequality or present MW's argument. Stands in only for
the statement. Quotes: "The original theorem, a special case of what we will
prove here, says that no spontaneaous breaking of any continuous symmetry
occurs at finite temperatures (β < ∞) in dimensions d ≤ 2" (p. 1).
Proposition 2.2 (p. 5) needs "sup_x Σ_y |x − y|² |J(x, y)| < +∞", and
"Translation invariance is not required; in fact the argument works for
inhomogeneous systems with spins of different magnitudes at different
sites." The mechanism: a rotation can be interpolated to zero at infinity
"in such a way that there is a uniform bound on the energy involved", using
|φ_m(x) − φ_m(y)| ≤ |φ|/m against |Λ_m| ∼ m² in d = 2 (p. 6).

## Summary of the work (as the neighbours report it)

MW prove, for quantum Heisenberg ferro- and antiferromagnets on 1D and 2D
lattices (and U(1) magnets with in-plane order), that the spontaneous
magnetization vanishes at every T > 0, provided the exchange has a finite
second moment. The tool is Bogoliubov's inequality with operators chosen to
put the order parameter on the left; the bound reduces to ∫d^Dk/k², which
diverges in D ≤ 2 as the symmetry-breaking field goes to zero.

**Contribution.** The first rigorous exclusion of magnetic order in low
dimensions, for lattice spins (Hohenberg's parallel proof was for
continuum bosons and fermions); the template for a family of later proofs.

**Assumptions.** Isotropic (SU(2)) or U(1) symmetry of H; finite-range in
the second-moment sense; thermal equilibrium (Gibbs state); T > 0; order
parameter a sum of local operators generated by a sum of local generators.

**Concepts.** Bogoliubov inequality; quasi-average (field B₀ → 0 after the
thermodynamic limit); second moment of J; infrared divergence ∫d^Dk/k²;
lower critical dimension 2; Hohenberg–Mermin–Wagner naming.

## Verdict on how the exchange characterized the work

- LIT-2985 summary: "isotropic Heisenberg models with short-range
  interactions in one or two dimensions have no spontaneous magnetization
  at finite temperature". **Accurate**, with two refinements: "short-range"
  means a finite second moment Σ r²|J(r)| (Halperin; Nachtergaele), so
  power-law couplings falling faster than 1/r⁴ are covered; and it covers
  antiferromagnetic order too (title; Gelfert eq. 52).
- LIT-2985 status note: "no continuous symmetry breaking in two dimensions
  at finite temperature". **Overbroad as an attribution to this paper.**
  MW is about Heisenberg (and U(1)) magnets; the general statement is the
  later family (Nachtergaele's "The original theorem ... says ... any
  continuous symmetry" is a gloss), and even the family has exceptions:
  orientational order in a 2D crystal (Halperin §II).
- CLAIM-841: "the 2D infrared integral ∫k^(d−3) dk diverges logarithmically
  (Mermin–Wagner)". **Consistent**: ∫d^Dk/k² = ∫k^(D−3)dk is the integral
  the proof rests on (Gelfert eq. 63). But MW's proof gets there through the
  Bogoliubov bound, not through a Gaussian spin-wave integral; the spin-wave
  argument is the older non-rigorous one (Halperin §II, eqs. 2–3).
- CLAIM-842: d_s ≤ 2 as "the lower critical dimension of the Mermin–Wagner
  theorem read on a learned manifold". **The graph generalization exists in
  the literature**: Cassi 1992 via Hattori et al. 1987 (Gelfert §3.4), for
  O(n) and ferromagnetic Heisenberg models. Not MW's own result.

## Bearing on the named codes

- **CLAIM-842: supports the mechanism and qualifies the reach.** Supports:
  Cassi's theorem (reported in Gelfert §3.4) is exactly "spectral dimension
  ≤ 2 forbids spontaneous magnetization", from "the infrared divergencies
  displayed by the corresponding Gaussian models", and Hattori et al.'s
  framing ("the only geometrical structure that spins can feel is ... the
  network structure of the interaction") is A29's point that the governing
  dimension is that of the interaction graph, not the embedding. Qualifies:
  (i) the rigorous results need a continuous symmetry of the Hamiltonian
  whose generator is a sum of local generators (Halperin §II on
  orientational order); CLAIM-842's own first caveat (no identified
  symmetry) is the gap; (ii) a Gaussian divergence is not always the
  answer: in tethered membranes nonlinear coupling makes κ diverge and
  "removes the divergence" (Halperin §II), a worked case where the
  Gaussian criterion predicts disorder and order survives; (iii) the
  theorem needs finite second moments; long-range couplings (on a graph,
  long edges) can restore order (Halperin §II); (iv) it is an equilibrium
  theorem (Halperin eq. 12 rests on the fluctuation-dissipation theorem),
  which sharpens CLAIM-842's equilibrium caveat.
- **CLAIM-841: supports the Goldstone and XY rows and the "no tuning"
  point, with one qualification.** The divergence that kills order in
  d ≤ 2 holds at every T > 0, with no tuned parameter (Gelfert eq. 52).
  Halperin's eqs. 2–3 give the XY-row exponent the claim rechecked,
  r^(−T/2πρ_s). Qualification: "The HMW theorem sheds no light on ...
  quasi-long-range order" (Halperin §II), so the "line of fixed points"
  row rests on LIT-2969 (Kosterlitz–Thouless), not on LIT-2985; LIT-2985
  grounds only the absence of true long-range order.

## Limitations

The 1966 text itself was not seen: its exact hypotheses, constants, the
erratum (p. 1307, per the search result for MathWorld; not checked), and
MW's own wording are unverified. The Gelfert outline is a secondary
paraphrase; Cassi and Hattori et al. are known here only through Gelfert's
summary.

## Candidate THEORY sentence (for the neighbour, Gelfert and Nolting)

"Gelfert and Nolting show that Mermin and Wagner's exclusion of
ferromagnetic and antiferromagnetic order in the 1D and 2D Heisenberg model
rests on Bogoliubov's inequality reducing the order parameter's bound to
the infrared divergence of ∫d^Dk/k² in D ≤ 2, and report that Cassi
extended the exclusion to graphs of spectral dimension at most 2."
`promote_when`: a reading of Mermin and Wagner (1966) confirms the
operator choice and the logarithmic bound as Gelfert outline them, and a
reading of Cassi (1992) confirms the spectral-dimension statement.

For Halperin (alternative): "Halperin shows that the Hohenberg–Mermin–Wagner
theorem excludes true long-range order breaking a continuous symmetry
generated by a sum of local operators at T > 0 in d ≤ 2 for finite
second-moment interactions, and says nothing about quasi-long-range order,
T = 0, or orientational order." `promote_when`: a second source confirms the
orientational-order exception and the second-moment condition.

## Recheck (search of record/ after reading)

- **LIT-2969** (Kosterlitz and Thouless, Deferred): the record of BKT; per
  Halperin, QLRO is outside HMW, so the XY row of CLAIM-841 rests here.
  Bearing: contrast/complement.
- **LIT-1670 / NOTE-1228 / THEORY-1085** (Toner and Tu): NOTE-1228 cites
  "Mermin and Wagner (ref. [5])" as "the equilibrium results the flock
  evades". Consistent with Halperin's equilibrium framing (eq. 12).
  Bearing: parallel; the exception that MW's equilibrium premise permits.
- **TERM-136** (spectral dimension) and **QUESTION-515**, **SYNTHESIS-120**:
  carry CLAIM-842's d_s criterion; the first search missed that the record
  holds **no LIT for Cassi 1992 or Hattori et al. 1987**, the literature
  that actually proves the graph version. Recommend registering both.
- **THEORY-1272** (spectral dimension of SGD drift): a different object, as
  CLAIM-842 says; no bearing.
- **CLAIM-846** (Gaussian spin-wave route checked numerically): parallel to
  Halperin eqs. 2–3.
- Grep for Bogoliubov, Hohenberg, Halperin, Cassi, Hattori, "lower critical
  dimension", "tethered membrane", "hexatic", "orientational order" found
  nothing else on this topic (Bogoliubov hits are Bogoliubov–de Gennes and
  Krylov–Bogoliubov; Hohenberg hits are Cross–Hohenberg, LIT-527).

## Every other work read and quoted

Only the three neighbours above. Cassi (1992), Hattori et al. (1987),
Mermin (1967, J. Math. Phys.) and Hohenberg (1967) are known only through
Gelfert and Halperin; not read.
