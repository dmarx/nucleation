# Reader notes: takeuchi2010 (LIT-2982)

Takeuchi and Sano (2010), "Universal Fluctuations of Growing Interfaces:
Evidence in Turbulent Liquid Crystals", arXiv:1001.5121v3, PRL 104, 230601,
doi:10.1103/PhysRevLett.104.230601.

## Step 1: copies located (2026-11-22)

- https://arxiv.org/e-print/1001.5121v3 : arXiv author source (LaTeX, v3,
  14 Jun 2010, "minor changes made; note added"). Fetched, HTTP 200.
- https://arxiv.org/pdf/1001.5121 : arXiv PDF of v3, 4 pages. Fetched,
  HTTP 200; used for page numbers.
- arXiv API (export.arxiv.org) metadata: journal ref and DOI confirmed.
- Publisher version (APS, doi above): not sought; arXiv v3 is the author's
  final with note added in proof.

## Step 2: read (2026-11-22)

### Provenance

- Read: the arXiv v3 LaTeX source in full (abstract, all body text, five
  figure captions, note added in proof, bibliography), checked against
  the arXiv v3 PDF (https://arxiv.org/pdf/1001.5121, 4 pp.) for page
  numbers. Format: LaTeX + PDF. Skipped: the figures themselves (EPS),
  read through their captions and the text; the APS version (paywalled,
  not sought; v3 is the authors' final with the note added in proof).
- Copies located: arXiv e-print (https://arxiv.org/e-print/1001.5121v3,
  author's manuscript, read), arXiv PDF (https://arxiv.org/pdf/1001.5121,
  author's manuscript, read for pagination). No obstacle at either.
- Catalogue lookup only, not read: arXiv API search returned the
  authors' directed-percolation papers in the same system, cited here as
  ref. [13]: arXiv:0706.4151 (PRL 99, 234503, 2007, "Directed percolation
  criticality in turbulent liquid crystals") and arXiv:0907.4297 (PRE 80,
  051116, 2009). Titles only; neither is held in record/.

### Summary

An experiment on electroconvection in a thin homeotropic nematic layer
(MBBA, 12 µm, 26 V at 250 Hz, above the DSM1-DSM2 threshold of 20.7 V).
A laser pulse nucleates a DSM2 cluster (a turbulent state dense in
disclinations) inside DSM1; it grows as a circular droplet whose edge
roughens. Repeating the run 563 times, the authors measure the local
radius R(x, t) and find (1) the KPZ scaling exponents in 1+1 dimensions,
(2) the cumulants, skewness, kurtosis and full histogram of R matching the
GUE Tracy-Widom distribution predicted by Prähofer and Spohn for curved
interfaces, with no fitting parameter once λ and A are measured, and
(3) the two-point correlation matching the Airy₂ process.

### Contribution

The first quantitative experimental test of the KPZ fluctuation
predictions beyond exponents: the one earlier test (paper combustion,
Miettinen et al. 2005) had to shift and rescale the distribution and
discard avalanche data. Also among very few experiments to find the KPZ
exponents directly at all.

### Key results (page of the v3 PDF; quotes verbatim)

- Experiments rarely find KPZ (p. 1): "experimentally measured values of
  the exponents are widely diverse and mostly far from the KPZ values for
  both α and β [1]. To our knowledge, only two experiments among dozens
  directly found the KPZ exponents".
- Exponents (p. 2): "α = 0.50(5)"; W(t) and C_pl(t)^{1/2} "show a very
  clear power law t^β with β = 0.336(11) [Fig. 2(c)] in remarkable
  agreement with the KPZ growth exponent β^KPZ = 1/3"; Family-Vicsek
  collapse with KPZ exponents; "We therefore safely conclude that the
  DSM2 interfacial growth belongs to the (1+1)-dimensional KPZ class."
  This also "rules out the logarithmic temporal scaling claimed by
  Escudero for the droplet geometry".
- Parameters (p. 3): λ = 35.40(23) µm/s from dR/dt against t^{-2/3}; A
  only roughly, "A ≈ 10 µm", by direct estimates that "increase slowly
  with time and do not agree with each other".
- Distribution (p. 3): skewness and kurtosis, "which do not depend on the
  parameter estimates", "asymptotically converge to the values of the GUE
  TW distribution, about 0.2241 for the skewness and 0.09345 for the
  kurtosis [6], and clearly rules out the GOE TW and Gaussian
  distributions." Assuming GUE TW, A = 9.98(7) µm, consistent with the
  direct estimate. Histograms of q = (R − λt)/(A²λt/2)^{1/3} "show
  remarkable agreement with the GUE TW one without any fitting, apart from
  a slight horizontal translation"; the mean approaches the GUE value
  with "a power close to −1/3"; conclusion "at least up to the fourth
  order cumulants".
- Geometry fixes the ensemble (p. 3): GUE and GOE "for curved and flat
  interfaces, respectively"; conclusion (p. 4): "the geometry-dependent
  universality of the (1+1)-dimensional KPZ class".
- Correlation (p. 4): C₂(l, t) agrees with the Airy₂ covariance g₂(u)
  "with an algebraic finite-time correction consistent with the power
  −1/3".
- Why this system shows KPZ when others do not (p. 4): "(a) The growth of
  DSM2 results from strictly local processes ... (b) The stochasticity of
  the process stems from intrinsic turbulent fluctuations ... [not]
  overwhelming quenched disorder. (c) Good controllability and fast
  response ... allowed us to repeat hundreds of experiments".
  Reproducibility "confirmed with different voltages and spatial
  resolutions" (not shown).
- Note added in proof (p. 4): Sasamoto and Spohn's exact solution of the
  1+1 KPZ equation "offers a clear theoretical ground of our experimental
  results."

### Assumptions

The DSM2 front is a 1+1D KPZ interface (local growth, white noise, no
quenched disorder: argued, not derived); Prähofer-Spohn's conjecture
carries over from solvable models to the KPZ class; the asymptotic
Krug-Meakin-Halpin-Healy relations for λ and A hold for a circular front;
finite-time corrections are t^{-1/3}. Times are short (to 28.4 s); higher
cumulants "statistically more demanding and hence provide less conclusive
results".

### Concepts

KPZ equation and class (1+1D, α = 1/2, β = 1/3, z = 3/2); Family-Vicsek
scaling; width w(l, t), height-difference correlation C(l, t); Tracy-Widom
GUE/GOE; Prähofer-Spohn ansatz h ≃ v∞t + (A²λt/2)^{1/3}χ; Airy₂ process,
Dyson Brownian motion; DSM1/DSM2, disclinations, Carr-Helfrich
instability; quenched disorder; finite-time corrections.

### Verdict on the exchange's characterization

LIT-2982's summary ("Growing turbulent domains in liquid-crystal
convection show KPZ exponents and Tracy-Widom height fluctuations, the
first experimental evidence of the latter") is accurate with two
refinements: it is GUE TW specifically, for a curved (circular) front,
with GOE and Gaussian ruled out; and "first" should be "first
quantitative", since Miettinen et al. (2005) had reported "an apparent
agreement" for flat fronts after shifting and rescaling. CLAIM-841's row
"W(L, t) = L^α F(t/L^z), α = ½, z = 3/2 in 1D, generically" is the form
the paper tests (as w(l, t) ∼ t^β F(l t^{-1/z})). "Generically" is right
for the theory and for numerical models (p. 1, "universal as widely
confirmed in numerical models") but not for experiment: the paper's own
starting point is that experiments mostly do not find KPZ.

### Bearing on the named codes

- **CLAIM-841** (KPZ row of the routes table): **supports, with a
  qualification.** Supports: scale-invariant roughening with KPZ
  exponents is found in a driven state well above a threshold ("26 V ...
  sufficiently larger than the DSM1-DSM2 threshold at 20.7 V", p. 2) and
  is reported robust across voltages (p. 4), so no parameter is tuned to
  a transition. The paper never uses "criticality" or discusses tuning;
  this reading is the record's, from those two passages. Qualifies:
  untuned is not the same as generic. KPZ needs locality and the absence
  of quenched disorder (p. 4, factors (a), (b)), which most experiments
  lack (p. 1). So the KPZ route removes the scale without tuning but only
  where those conditions hold. Also bears on A24 §9 ("a KPZ interface has
  universal scaling without power-law tails"): the universal object is a
  Tracy-Widom distribution, which the paper characterizes by cumulants,
  not tails; consistent, not addressed.
- **QUESTION-508**: **supports one partial answer; leaves the question
  open.** The case is a scale-invariant state reached without tuning by
  nonequilibrium local growth. The paper's three factors are a local,
  system-level answer to "what a system must have" for KPZ (local growth,
  intrinsic noise, no quenched disorder), but not a general one. A
  contrast the record could use: the same liquid-crystal system shows
  directed-percolation criticality at the DSM1-DSM2 coexistence
  ("spatiotemporal intermittency", p. 2, ref. [13]), a tuned
  absorbing-state transition, and untuned KPZ above it. The DP character
  comes from ref. [13]'s title only, not read here.

### Limitations

One system, one (curved) geometry; flat interfaces "in progress".
Short times (≤ 28.4 s) and finite-time corrections in the mean and the
correlation; A is fixed by assuming GUE TW, though skewness and kurtosis
are parameter-free and the direct estimate agrees roughly. Cumulants
beyond the fourth not established. The three factors are argued, not
tested. Robustness across voltages not shown.

### Candidate THEORY

Sentence: "Takeuchi and Sano find that turbulent DSM2 clusters growing in
nematic electroconvection, driven well above threshold, roughen with the
1+1-dimensional KPZ exponents (α = 0.50(5), β = 0.336(11)) and that their
local-radius fluctuations follow the GUE Tracy-Widom distribution, with
GOE and Gaussian ruled out by skewness and kurtosis, and Airy₂
correlations, the first quantitative experimental test of the KPZ
fluctuation predictions."

promote_when: "An independent experiment or a reanalysis confirms GUE
Tracy-Widom fluctuations for curved KPZ fronts (with skewness and
kurtosis near 0.224 and 0.093), or the authors' later flat-interface
measurements find the GOE counterpart in the same system."

## Step 3: recheck (2026-11-22)

Searched record/ for KPZ, Kardar, Tracy-Widom, Family-Vicsek, Airy,
Sasamoto, Spohn, Prähofer, Miettinen, electroconvection, liquid crystal,
nematic, directed percolation, growing interface, self-affine,
Edwards-Wilkinson, universality class, random matrix, and the arXiv ids
0706.4151 and 0907.4297. Not held: the DP papers in the same system,
Prähofer-Spohn, Sasamoto-Spohn, Miettinen. Entries the first search
(which reached CLAIM-841, QUESTION-508, LIT-2978) missed:

- **LEAD-209** (Open; protocol for telling mechanisms apart), "Growth
  (KPZ)" column: **supports and qualifies.** Its cells "W ∝ L^α" and
  "z = 3/2 in 1D" are what the paper measures (α = 0.50(5), β =
  0.336(11), Family-Vicsek collapse). Its cell "odd-order statistics of
  increments: nonzero skewness" is near but not what the paper shows: the
  paper's nonzero skewness (≈ 0.2241, GUE TW) is of the height (local
  radius) itself, not of increments. The paper also supplies a sharper
  row for that column: the parameter-free skewness and kurtosis that
  discriminate GUE TW from GOE TW and Gaussian, and so read geometry
  (curved vs flat). Its trial's "1D KPZ discretization" could be scored
  against these numbers.
- **CLAIM-803** (Proposed; a shared power law does not show a shared
  mechanism or universality class): **supports, as parallel.** The paper
  goes "beyond the scaling laws" (p. 1): it identifies the class by the
  full fluctuation distribution and correlation, not exponents alone,
  and the distribution distinguishes sub-classes (GUE vs GOE) that share
  exponents.
- **SYNTHESIS-119** (Proposed; a power law does not identify its
  mechanism): background; the paper is an instance of identifying a
  mechanism from more than the exponent, through TW and Airy₂.
- **QUESTION-505** (Open; what fixes the exponent: geometry, dimension
  ...): **parallel/contrast.** In KPZ geometry does not fix the exponents
  (same α, β for curved and flat) but fixes the distribution (GUE curved,
  GOE flat; "geometry-dependent universality", p. 4).
- **THEORY-2148** (Baik, Ben Arous and Péché; Tracy-Widom fluctuations of
  the largest sample eigenvalue): background; the same GUE TW law, here
  reached by a growing interface.
- **TERM-139** (relevant/irrelevant/marginal at an RG fixed point):
  background; the paper cites "the renormalization group approach" for
  the exact 1+1D exponents (p. 1).

No held entry contradicts the reading.

## Step 4: report (2026-11-22)

Status for LIT-2982: **read** (lawful arXiv copy, full text). No
neighbour needed. Candidate registrations for the filer, catalogue
metadata only, not read: Takeuchi, Kuroda, Chaté and Sano, arXiv:0706.4151
and arXiv:0907.4297 (directed percolation in the same system), useful as
the tuned counterpart for QUESTION-508; Sasamoto and Spohn, PRL 104,
230602 (2010), cited in the note added in proof. No email address sent
to any service.
