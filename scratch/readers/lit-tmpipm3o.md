# Reader notes: LIT-tmpipm3o (Baik, Ben Arous & Péché, arXiv math/0403022)

Reader: Claude (subagent), 2026-11-21. No email address sent to any service.

## Provenance and copies located

| work | address | kind | outcome (2026-11-21) |
|---|---|---|---|
| BBP, the work | https://arxiv.org/pdf/math/0403022 (v2, 21 Oct 2004) | arXiv preprint, authors' | read, PDF, 200 OK |
| Baik & Silverstein 2006 (neighbour) | https://arxiv.org/pdf/math/0408165 (v1, 12 Aug 2004) | arXiv preprint, authors' | read §1 (pp. 1–5), 200 OK |
| Paul 2007 (neighbour) | https://www3.stat.sinica.edu.tw/statistica/oldpdf/A17n418.pdf | publisher's own open site (Statistica Sinica 17(2007) 1617–1642) | read §1, §2.1–2.4 statements, 200 OK |
| Benaych-Georges & Nadakuditi 2012 (neighbour) | https://arxiv.org/pdf/1103.2221 (v2, 26 Jan 2012) | arXiv preprint, authors' | read §3.1 (pp. 9–10) and abstract, 200 OK |

No obstacle met. The published BBP (Ann. Probab. 33(5), 2005, doi
10.1214/009117905000000233) was not fetched; the arXiv v2 was read. The v2
acknowledges Paul "for finding a typographical error in the main theorem in
an earlier draft", so v2 postdates that fix.

What was read of BBP: §1 in full (Introduction, §1.1 known results, §1.2
definitions, §1.3 main results incl. Theorem 1.1, Corollary 1.1,
Proposition 1.1, the Conjecture, §1.4 Theorem 1.2), §2.1 (eigenvalue
density, and why the method fails for real samples), §6 (last-passage
heuristic for the threshold). Skipped: the steepest-descent proofs of
§§3–5 (pp. 14–48).

## Summary

For M i.i.d. **complex Gaussian** samples of N variables, with population
covariance Σ whose eigenvalues are all 1 except finitely many (r fixed),
and M/N = γ² ≥ 1 (their γ; samples at least as many as variables), the
paper gives the limiting law of the **largest** sample eigenvalue λ₁. The
critical spike is ℓ = 1 + γ⁻¹. Below it λ₁ sits at the edge (1 + γ⁻¹)²
with GUE Tracy–Widom fluctuations of order M^(−2/3); at it, new laws F_k;
above it, λ₁ → ℓ₁(1 + γ⁻²/(ℓ₁ − 1)) with Gaussian-type (k × k GUE)
fluctuations of order M^(−1/2). Theorem 1.2 gives interpolating laws in a
window of width M^(−1/3) about the threshold. The real case is stated as
a conjecture.

## Contribution

The first proof that the spiked threshold is sharp and the first limiting
laws across it (the "BBP transition"), via a Fredholm-determinant formula
for λ₁ available only for complex samples (HCIZ integral over U(N)).

## Key results

- **Setting (§1.1, p. 3).** "We assume that the samples ~y are complex
  Gaussian with mean ~µ and covariance Σ." The sample matrix is centred by
  the sample mean: "X = [~y1 − Y, · · · , ~yM − Y] to be the (centered)
  N × M sample matrix" (p. 2). The density used, (59), is
  e^{−M tr(Σ⁻¹S)}(det S)^{M−N}, i.e. M degrees of freedom.
- **Theorem 1.1 (p. 8).** "As M, N → ∞ while M/N = γ² is in a compact
  subset of [1, ∞) ... (a) When ... ℓ1 = · · · = ℓk = 1 + γ⁻¹ ...
  P((λ1 − (1 + γ⁻¹)²) · γ/(1+γ)^{4/3} M^{2/3} ≤ x) → Fk(x). (b) When ...
  ℓ1 = · · · = ℓk is in a compact set of (1 + γ⁻¹, ∞) ... → Gk(x)" with
  centring ℓ1 + ℓ1γ⁻²/(ℓ1 − 1) and scale √M.
- **Corollary 1.1 (pp. 9–10).** (a) "λ1 → (1 + γ⁻¹)² in probability";
  (b) "λ1 → ℓ1(1 + γ⁻²/(ℓ1 − 1)) in probability." And (p. 10): "λ1 is
  separated from the rest of eigenvalues if and only if at least one
  eigenvalue of Σ is greater than 1 + γ⁻¹."
- **Origin of the threshold (p. 10).** "Here the critical value 1 + γ⁻¹
  comes from a detail of computations and we do not have an intuitive
  reason yet." §6 (p. 49) gives a last-passage-percolation heuristic,
  max_x f(x) with f(x) = π₁⁻¹x + (√(1−x) + γ⁻¹)².
- **Real case open (p. 11).** "The real question is the real sample
  covariance ... Conjecture. For real sample covariance, the Theorem 1.1
  still holds true for different limiting distributions but with the same
  scaling. In particular, the critical value ... is again expected to be
  1 + γ⁻¹." And p. 13: "the techniques below ... [are] not applicable to
  real sample matrices."
- **Window (Theorem 1.2, p. 12).** ℓj = 1 + γ⁻¹ − (1+γ)^{2/3}wj/(γM^{1/3})
  gives interpolating laws Fk(x; w1, …, wk).
- **Fixed-N contrast (Prop. 1.1, p. 10).** With N = k fixed the top
  eigenvalue concentrates at ℓ1; in case (b) "the contribution to λ1
  comes from both ℓ1 = · · · = ℓk and infinitely many unit eigenvalues."

## Normalization: translating to the record's notation

BBP: N variables (record: D), M samples (record: N), γ_BBP² = M/N.
So γ_BBP⁻¹ = √(D/N) = √γ_rec, and ℓ = 1 + β.

- Threshold ℓ > 1 + γ_BBP⁻¹ ⇔ **β > √γ_rec**. Matches the record.
- Outlier ℓ(1 + γ_BBP⁻²/(ℓ − 1)) = (1+β)(1 + γ_rec/β). Matches
  CASE-tmp59xy5 and CLAIM-tmpqbo50 ((1 + ℓ)(1 + γ/ℓ) there with ℓ the
  relative spike; times σ²).
- Edge (1 + γ_BBP⁻¹)² = (1 + √γ_rec)². Matches.
- **Range:** BBP requires M ≥ N, i.e. **γ_rec ≤ 1** (D ≤ N). Rows with
  γ_rec > 1 (CLAIM-tmpqbo50's γ = 4 row) are outside BBP; Baik–Silverstein
  Thm 1.2 (c > 1) covers them, same threshold 1 + √c and location.
- **Only λ₁.** BBP gives the law of the largest eigenvalue only, and says
  nothing about eigenvectors.

## Neighbours (all read; each a work in its own right, not stand-ins — BBP itself was read)

**Baik & Silverstein, "Eigenvalues of large sample covariance matrices of
spiked population models" (arXiv math/0408165; J. Multivariate Anal. 97,
2006).** Real **or** complex, **non-Gaussian** i.i.d. Z with E Z = 0,
E|Z|² = 1, E|Z|⁴ < ∞, samples T^{1/2}Z, B_p = (1/n)T^{1/2}ZZ′T^{1/2}
(uncentred, mean-zero model), p/n → c, all c > 0 (Thms 1.1–1.3). All
spikes, not only the top: (1.10) "s → αj + cαj/(αj − 1), 1 ≤ i ≤ kj.
almost surely" for each αj > 1 + √c; (1.14) for r = 1, s₁ → (1+√c)² if
σ1 ≤ 1 + √c, else σ1 + cσ1/(σ1 − 1). Intro p. 2: "The purpose of this paper
is a complete study of the spiked model for both real and complex samples
which are not necessarily Gaussian. We obtain almost sure limits." Covers
the real case BBP left open, for a.s. limits (not fluctuations: "a
complete study of limiting distributions is still an open question").
Finite r fixed.

**Paul, "Asymptotics of sample eigenstructure for a large dimensional
spiked covariance model" (Statistica Sinica 17, 2007, 1617–1642).** Real
Gaussian, mean zero, S = (1/n)XXᵀ, N/n → γ ∈ (0, 1) (p. 1619). Theorem 4
(p. 1622): if ℓν > 1 + √γ, simple, "|⟨pν, eν⟩| → √((1 − γ/(ℓν − 1)²) /
(1 + γ/(ℓν − 1)))" a.s.; (b) if ℓν ≤ 1 + √γ, "⟨pν, eν⟩ → 0". With β = ℓ − 1
this is the squared overlap (1 − γ/β²)/(1 + γ/β) of CASE-tmp59xy5. Credits
the phenomenon physically to Hoyle and Rattray (2004), "retarded
learning".

**Benaych-Georges & Nadakuditi, "The singular values and vectors of low
rank perturbations of large rectangular random matrices" (arXiv
1103.2221; J. Multivariate Anal. 111, 2012).** §3.1 "Gaussian rectangular
random matrices with non-zero mean" (p. 9): Xn n×m, i.i.d. N(0, 1/m),
n/m → c ∈ (0, 1], plus deterministic Pn of rank r with singular values θi:
(9) σi(Xn + Pn) → √((1+θi²)(c+θi²)/θi²) "if i ≤ r and θi > c^{1/4}", else
1 + √c; (10) |⟨ũ, u⟩|² → 1 − c(1 + θ²)/(θ²(θ² + c)) for θ ≥ c^{1/4}, else
0. With n = D, m = N, β = θ²: threshold β > √γ, top eigenvalue of the
uncentred second moment (1+β)(1+γ/β), overlap (1 − γ/β²)/(1 + γ/β) —
the same three formulas, for an **additive mean shift / information-plus-
noise** model. Already cited by NOTE-666 (Thm 2.9) and LIT-862; the
record holds no LIT for it.

## Verdict on the exchange's characterization

Correct in its formulas and threshold, after the change of notation;
loose in its attribution. (1) BBP proves the threshold for **complex
Gaussian, centred** sample covariance and only for the **top eigenvalue**;
the real case is a conjecture there. (2) Eigenvector claims ("only then does
its eigenvector carry information", the overlap formula) are not BBP's —
they are Paul 2007 (real Gaussian, γ < 1) and Benaych-Georges–Nadakuditi.
(3) The exchange's γ = D/N is BBP's γ⁻², and its threshold √γ is BBP's γ⁻¹.
(4) The exchange's models are real-valued, and two of them (CASE's ±1
mixture; CLAIM-tmpk33au's mean shift in the uncentred second moment) are
not spiked-covariance samples Σ^{1/2}z at all, but rank-one additive
perturbations: covered by Benaych-Georges–Nadakuditi §3.1, which gives the
identical formulas, not by BBP.

## Bearing on each code

- **CLAIM-tmp5y856** — *qualifies* (supports the threshold). BBP Cor. 1.1
  gives β > √γ and the location; the "opening as (β − √γ)²/β" follows by
  algebra from (46) [(1+β)(1+γ/β) − (1+√γ)² = (β − √γ)²/β]. The eigenvector
  sentence needs Paul 2007 Thm 4 / BGN (10), not BBP. Real-valued data:
  Baik–Silverstein. Also: BBP's own "phase transition" is in the law of λ₁
  (fluctuation order M^(2/3) → M^(1/2)), which fits the claim's
  "detectability, not a thermodynamic transition" reading.
- **CASE-tmp59xy5** — *qualifies*. Formulas exact (BBP (46) translated;
  overlap from Paul Thm 4). But z = √β·s·v + ε with s = ±1 is a real,
  non-Gaussian mixture, not complex Gaussian (BBP) nor T^{1/2}Z with i.i.d.
  Z (Baik–Silverstein needs identically distributed entries; the v-coordinate
  differs). It is exactly BGN's additive rank-one model: data matrix √β·v sᵀ + E,
  i.e. after scaling by 1/√N a perturbation of singular value θ = √β; cite BGN §3.1 for it. Also the "Deferred: registered, not
  read" parentheticals should be updated once filed.
- **CLAIM-tmpk33au** — *qualifies*. "PCA ... sees a mean shift c along μ as
  a spike β = c² in the uncentred second moment" is not a BBP statement:
  BBP centres by the sample mean (p. 2), which would remove the shift.
  The uncentred second moment of N(cμ, I) samples is the additive rank-one
  model of BGN §3.1 (θ = c), threshold θ > γ^{1/4}, i.e. c = γ^{1/4}:
  **the claim's κ_BBP = √D·(D/N)^(1/4) stands, on BGN**. The mean-field
  precursor (θ² = γ(K/D)/(1 − K/D) along a random direction) is a
  covariance spike and uses the Baik–Silverstein real-case threshold.
- **CLAIM-tmp8mvx8** — *qualifies*. BBP gives only λ₁; counting K_det
  outliers needs Baik–Silverstein (1.10): each spike above 1 + √c gives its
  own outlier, for r fixed. K growing with D is outside both, as the
  claim's row 5 already shows; the paper supports the "sparse regime only"
  correction. "Which N": BBP's M is the number of samples of the
  covariance estimate, supporting the claim's correction.
- **CLAIM-tmpqbo50** — *supports (formulas), qualifies (range)*. Outlier
  σ²(1+ℓ)(1+γ/ℓ) and edge σ²(1+√γ)² are BBP (46)/(44) rescaled. The
  table's γ = 4 row lies outside BBP (M ≥ N) and needs Baik–Silverstein
  Thm 1.2. With φ independent of ξ, h = bφu + σξ is again BGN's additive
  model. The "invisible within ~N^(−2/3) of the edge" remark (CLAIM-tmp8mvx8
  too) is BBP Theorem 1.1(a)/1.2: edge fluctuations of order M^(−2/3) and
  a critical window of width M^(−1/3) in ℓ.

## Assumptions (BBP)

Complex Gaussian samples; all but r (fixed) population eigenvalues equal
1; M/N = γ² in a compact subset of [1, ∞); spikes in compact sets away
from the threshold except in Theorem 1.2; centred sample covariance
(asymptotically the same as uncentred for mean-zero data).

## Concepts

Spiked population model (Johnstone); BBP transition; Tracy–Widom F_GUE,
F_GOE; new laws F_k and finite-GUE G_k; HCIZ integral; Laguerre unitary
ensemble; last passage percolation / queueing link; retarded learning
(Hoyle–Rattray, via Paul).

## Limitations

The real case is conjectured, not proved, in BBP; only λ₁; Gaussian only;
γ_rec ≤ 1 only; the threshold has "no intuitive reason" given beyond the
percolation heuristic; finitely many spikes.

## Candidate THEORY

Sentence: "For complex Gaussian samples whose population covariance is
the identity except for finitely many eigenvalues, with M samples of N
variables and M/N → γ² ≥ 1, the largest sample eigenvalue separates from
the Marchenko–Pastur edge (1 + γ⁻¹)² if and only if some population
eigenvalue exceeds 1 + γ⁻¹, converging then to ℓ₁(1 + γ⁻²/(ℓ₁ − 1)) with
fluctuations of order M^(−1/2) instead of the edge's Tracy–Widom M^(−2/3)."

promote_when: "A second proof or a published restatement confirms, for
complex Gaussian spiked sample covariance with M/N → γ² ≥ 1, the threshold
1 + γ⁻¹, the limit ℓ₁(1 + γ⁻²/(ℓ₁ − 1)) above it, and the change of
fluctuation order from M^(2/3) to M^(1/2)." (Baik–Silverstein 2006 Thm 1.1
already confirms the threshold and limit, a.s., for general samples; the
fluctuation part rests on BBP.)

## Recheck (grep of record/ after reading)

Searched: Benaych, Nadakuditi, c^{1/4}, spiked, Tracy–Widom, Johnstone,
Wishart, outlier eigenvalue, retarded learning, Hoyle, Silverstein, Paul,
0408165, 1103.2221. Entries the first search (arXiv id, title, Baik,
"spiked" in literature.d) missed:

- **NOTE-666** (Saxe et al., semantic development) — *parallel*: its C6,
  "recoverable only above coherence C = 1", is the BGN θ > c^{1/4}
  threshold (Thm 2.9), and l. 231 calls it "the BBP transition (Baik, Ben
  Arous and Péché)". Same rectangular additive model the exchange's
  CASE/CLAIM-tmpk33au need.
- **LIT-862** — *parallel*: "a coherence threshold (a BBP transition, from
  Benaych-Georges and Nadakuditi)".
- **NOTE-659** (Small Singular Values Matter) — *background*: "The upper
  outlier is the BBP transition (Baik, Ben Arous and Péché;
  Benaych-Georges and Nadakuditi)"; lower outlier read as the same at the
  lower edge (spike below 1, which Baik–Silverstein (1.12)–(1.13) give for
  c < 1).
- **NOTE-660 / LIT-855** (word2vec closed-form dynamics) — *background*:
  analogy vectors fitted as a spiked random matrix, "borrows the spiked
  covariance model of Baik, Ben Arous and Péché (2005)".
- **NOTE-689** (scaling laws from language statistics) — *parallel*:
  resolvability threshold P^(−1/2) "compared to the spiked-matrix (BBP)
  detectability threshold".
- **NOTE-805** (Defilippis et al.) — *parallel*: "BBP-type weak-recovery
  transitions" in multi-index learning.
- **QUESTION-tmp7d1ws** — *background*: cites the threshold β = √γ as a
  proportional-limit result; BBP's M/N → γ² regime is that limit.
- **CLAIM-tmpp83vc**, **SYNTHESIS-tmpsejrp**, **LEAD-tmpp88ld**,
  **CLAIM-tmpqqngq** — cite BBP via the claims above; no separate bearing.
- THEORY-078, THEORY-420, CLAIM-164 already named in CLAIM-tmp5y856.

Not held: no LIT for Baik–Silverstein, Paul 2007, Benaych-Georges–
Nadakuditi, Johnstone 2001, or Hoyle–Rattray 2004.

## For the filer

- Status: read (arXiv v2). The three neighbours are supplements the
  filing would quote/rely on (ADR-114): Benaych-Georges–Nadakuditi
  especially, since it, not BBP, warrants CASE-tmp59xy5's and
  CLAIM-tmpk33au's real, uncentred, mean-shift setting; Paul for the
  overlap; Baik–Silverstein for real data, γ > 1 and multiple outliers.
