---
number: 708
status: Read
formerly:
- NOTE-tmpmm4u0
paper: 'LIT-919'
title: 'Vekilov — Nucleation'
version: 1
history:
- version: 1
  date: '2026-10-11'
  note: >-
    Read in full from the PubMed Central copy, PMC2995260, fetched as NLM
    XML and converted to text by script. PMC labels it an NIHPA Author
    Manuscript (NIHMS252864, PMID 21132117), in the "NIHPA Author
    Manuscripts" collection. Unpaywall calls it the submittedVersion; the
    PMC record says only that it is an author manuscript, and nothing in
    the file says whether it is the text before or after peer review. I
    read the abstract, every section, the acknowledgement, all eight
    figure captions, all seven display equations (from their MathML, so
    the fraction structure is exact) and the 109 references, which I
    skimmed. The figures themselves are images only (nihms252864f1–f8.jpg)
    and I did not see them, so the plots of Figs. 4 and 5, the phase
    diagram of Fig. 6 and the micrographs of Figs. 7 and 8 are known
    here only from their captions and the text. The PMC copy has no
    journal page numbers, so locations below are section headings, with
    equation and figure numbers. I did not see the published version
    (Crystal Growth & Design 10(12):5007–5019), so I cannot say whether
    the slips listed under Limitations were corrected in it.
date: '2026-10-11'
summary: >-
  For lysozyme, measured homogeneous nucleation rates of crystals from
  solution are about ten orders of magnitude below the classical
  prediction, level off as supersaturation rises, and pass through a
  maximum as temperature falls. The paper explains these by two things
  classical theory lacks. A solution–crystal spinodal, defined
  kinetically as where the nucleus shrinks to one molecule, so the barrier
  vanishes. And a two-step mechanism, in which crystals nucleate inside
  metastable clusters of dense liquid that form fast; ordering inside the
  clusters is the slow step. For metastable clusters the two-step
  mechanism is inferred from a kinetic model fitted to one protein's
  data, not observed. The evidence for other systems is weaker and the
  author grades it so. The paper also argues that near the spinodal the
  barrier is negligible, so heterogeneous substrates must act on the
  prefactor, not the barrier.
---
<!-- inactive-ok-file: LIT-926 LIT-924 — Unavailable, unread; named as companions and as works this reading bears on, not leaned on -->
<!-- inactive-ok-file: CLAIM-176 CLAIM-186 CLAIM-181 — Proposed; open, and cited as open: the theses and objections of the nucleating-argument line are under test, not settled -->

# NOTE-708: Vekilov — Nucleation

## Contribution

The paper is a perspective, built mostly on the author's group's own work
on lysozyme and other proteins. It sets classical nucleation theory (CNT)
against measured rates of homogeneous nucleation of lysozyme crystals and
lists four features CNT cannot explain. It explains them with two ideas.
The first is a solution–crystal spinodal: a line in the phase diagram past
which the nucleus is one molecule and there is no barrier. The second is
the two-step mechanism: a crystalline nucleus forms inside a pre-existing
metastable cluster of dense liquid, and that second step is the slow one.
It then surveys evidence that the two-step mechanism operates in other
proteins, small molecules, colloids, biominerals and polymers. It draws one
further conclusion: near the spinodal, heterogeneous substrates must speed
nucleation by helping clusters order, not by lowering the barrier.

## Key insight

Forming a crystal from a dilute solution needs two changes: the molecules
must get denser and they must get ordered. CNT assumes both happen at once,
in one fluctuation. The paper argues they happen in sequence. Dense
disordered clusters form first, quickly and in large numbers. Ordering
inside a cluster comes second, slowly, and only that step sets the rate.
Because clusters fill only about 10⁻⁷–10⁻⁶ of the volume and are about 100
times more viscous than the solution, most of the solution never hosts a
nucleus, and the rate is far below the classical estimate. At the high
supersaturations used in practice, the barrier to the second step is
negligible. What limits nucleation is then the kinetics of ordering, not a
threshold.

## Assumptions

- **CNT's barrier (Eqs. 1–2).** A three-dimensional nucleus with a
  macroscopic surface free energy α; the paper takes a cube of side a,
  Ω = a³, and notes that other shapes change the coefficient but keep the
  n^{2/3} scaling (The classical nucleation theory: Thermodynamics). The
  paper does not discuss whether a macroscopic α holds for nuclei of 1–10
  molecules, which is the size it then measures.
- **CNT's rate (Eq. 3).** "A major assumption in the derivation of Eq. (3)
  is that the solute molecules exchange directly with the crystalline
  embryo" (The rate of crystal nucleation). The replacement partition
  function of the nucleus is set to one, which the paper says is reasonable
  in a viscous solution but not in the gas phase.
- **The rate data are homogeneous.** This rests on the measurement method
  of refs. 36–37, which separates homogeneous from heterogeneous nuclei, and
  on the rates being several orders below less careful measurements
  (Experimental data on the rate of nucleation of crystals).
- **The CNT estimate.** ν* ≈ 300 s⁻¹ is taken from step velocities on
  large lysozyme crystals (~1 µm s⁻¹). The paper calls it "approximate".
  Z = 0.01–0.1 is assumed for any protein condensed phase, and
  n = 2 × 10¹⁸ cm⁻³. ΔG* ≈ 10⁻¹⁹ J is taken from the data, not from theory
  (The classical theory overestimates the crystal nucleation rate by 10
  orders of magnitude).
- **The two-step rate law (Eq. 5)** assumes step one is fast and step two
  is rate-determining, that the clusters are in equilibrium with the
  solution, and that the cluster number is steady (The rate determining
  step in the two-step nucleation mechanism). It also assumes the
  concentration inside the clusters, C1, rises as temperature falls, "in
  agreement with the phase diagram in Fig. 6 and the likely similarity
  between the dense liquid in the clusters and the stable [dense] liquid"
  (The rate law for the two-step mechanism).
- **The setting is narrower than the title.** "Nucleation" here is the
  nucleation of crystals from solution. Melts and vapour are set aside in
  the Introduction. The detailed case is one protein, lysozyme, at one
  buffer and pH.

## Key results

### Classical nucleation theory (Eqs. 1–4)

- **Free energy of a cubic cluster of n molecules** (Eq. 1):
  ΔG(n) = −nΔμ + 6a²n^{2/3}α, with Δμ = μ_solute − μ_crystal > 0.
- **Critical size and barrier** (Eq. 2):
  n* = 64Ω²α³/Δμ³ and ΔG* = 32Ω²α³/Δμ² = ½ n*Δμ, with Ω = a³.
  Both fall as supersaturation rises; n* as Δμ⁻³, ΔG* as Δμ⁻².
- **Rate** (Volmer): J = J₀ exp(−ΔG*/k_BT). In the statistical-mechanical
  form (Eq. 3): J = ν* Z n exp(−ΔG*/k_BT), with ν* the attachment rate to
  the nucleus, Z the Zeldovich factor and n the number density of solute.
  (The manuscript prints the exponent as −G*/k_BT, without the Δ.)
  External parameters act "mostly through ΔG*"; effects on J₀ are "weaker".
- **Nucleation theorem** (Eq. 4): n* − n₀ = k_BT ∂lnJ/∂Δμ + α₁, with
  0 ≤ α₁ ≤ 1 and n₀ < 1. It is called "a universal, model-independent
  nucleation law".

### The lysozyme data (Figs. 4–5)

Homogeneous nucleation rates against σ ≡ Δμ/k_BT at 12.6 °C and NaCl at
2.5, 3 and 4 %. J rises exponentially with σ, as Eq. 3 expects, with four
"peculiarities" (Experimental data on the rate of nucleation of crystals):

- (i) at 4 % NaCl, J(σ) breaks at σ = 3.1 and is "practically steady"
  above it;
- (ii) above σ = 3.45 the scatter grows;
- (iii) J is 0.1–1 cm⁻³ s⁻¹, "about ten orders of magnitude less than the
  prediction of the classical nucleation theory";
- (iv) as T is lowered, J rises exponentially, passes "a sharp maximum" and
  then falls.

### The solution–crystal spinodal

- Nucleus sizes from Eq. 4, read off the four linear segments of Fig. 4b,
  are 10, 4, 5 and 1 molecules. At 4 % NaCl the size drops from five to one
  at σ = 3.1, C = 33.5 mg/ml (The nucleus size and solution-crystal
  spinodal).
- "Nucleus size n* − n0 = 1 means that every molecule in the solution can
  be an embryo of the crystalline phase, and the growth to dimer and larger
  clusters occurs with a free energy gain." ΔG* is then below k_BT.
- The spinodal is defined kinetically, as the transition to a nucleus of
  one molecule, because "a thermodynamic definition of the solution-crystal
  spinodal is impossible": no mean-field free energy covers a solution and
  a solid.
- Past the spinodal ΔG* ≈ 0 and J does not rise with supersaturation, which
  explains (i). At the transition J has a sharp maximum and is very
  sensitive to conditions, which explains (ii).

### CNT overestimates the rate by ten orders

With ν* ≈ 300 s⁻¹, Z = 0.01–0.1 and n = 2 × 10¹⁸ cm⁻³, the prefactor is
10¹⁹–10²⁰ cm⁻³ s⁻¹. ΔG* ≈ 10⁻¹⁹ J from the slopes of Fig. 4b gives, by
Eq. 2 with Ω ≅ 3 × 10⁻²⁰ cm³, α = 0.5–0.6 erg cm⁻², close to other protein
crystals. Eq. 3 then predicts J ≈ 10⁸–10⁹ cm⁻³ s⁻¹. Because ΔG* came from
the data, "the difference between the experimentally determined J and the
prediction of the classical nucleation theory is due to an overestimate of
the pre-exponential factor by the classical theory." *Holds for:* this one
system, at the stated conditions, with an order-of-magnitude ν*.

### Metastable dense liquid clusters

Seen by dynamic light scattering in solutions of lysozyme, three hemoglobin
variants and lumazine synthase, and by AFM for lumazine synthase (Dense
liquid clusters in the homogenous region of the phase diagram):

- they appear within seconds of preparing the solution and the population
  is then steady for hours;
- they occupy ϕ ≈ 10⁻⁶–10⁻³ of the volume, at 10⁵–10¹⁰ cm⁻³, and hold up
  to 10⁶ molecules;
- lifetimes are > 15 ms for lysozyme and Hb (a lower bound, from
  Γ₂ = Γ₀ + D₂q² with Γ₀ ≪ 70 s⁻¹) and ~10 s for lumazine synthase. Both
  are far longer than the ~10⁻⁵ s equilibration time at sub-micrometre
  scales, so "the compact clusters represent a metastable phase separated
  from the bulk dilute solution by a free energy barrier";
- their size is not explained by short-range attraction with screened
  repulsion, which needs charges proteins do not carry. A cited study
  (ref. 67) puts it down to long-lived but unstable protein complexes.

### The two-step rate law (Eqs. 5–7)

From a phenomenological theory (ref. 50):

- **Eq. 5:** J = k₂ C₁ T exp(−ΔG₂*/k_BT) / { η(C₁,T) [1 + (U₁/U₀) exp(ΔG°_C/k_BT)] },
  with C₁ ≈ 300 mg ml⁻¹ the concentration inside the clusters, ΔG₂* the
  barrier to a crystal nucleus inside a cluster, η the viscosity inside the
  clusters, U₁ and U₀ the effective rates of cluster decay and formation,
  and ΔG°_C ≈ 10 k_BT the excess standard free energy of a molecule in a
  cluster. The bracket is about ϕ₂⁻¹.
- **Eq. 6** (after Kashchiev, ref. 79), near the spinodal:
  ΔG₂*(T) = E*/(T_e − T)² · [1 − (T_e − T)²/(T_e − T_sp)²], which vanishes at
  T = T_sp.
- **Eq. 7:** η = η₀ {1 + [η]C₁ exp(k_η[η]C₁)} exp(−E_η/k_BT).
- Fitted with "literature values or independently determined parameters",
  Eqs. 5–7 reproduce Figs. 4 and 5 "with high fidelity". The maximum in
  J(T) falls at T = T_sp. The fall below T_sp comes from smaller cluster
  volume and higher viscosity inside the clusters. A one-step mechanism
  would give a fall of only ~16 % over the 5–6 K probed. The paper calls
  the steep fall "a crucial part in the proof of the validity of the
  two-step mechanism".
- Comparing Eq. 5 with Eq. 3, k₂ϕ₂C₁T/η replaces ν*Zn. With ϕ₂ ≈
  10⁻⁷–10⁻⁶ and η ≈ 100 cP, "the nucleation rate should be ~ 10⁹× lower
  than the prediction of the classical theory". That accounts for about
  nine of the ten orders.

### The rate-determining step

- Step one is fast: clusters appear within seconds. Stable dense-liquid
  droplets nucleate at ~10⁸ cm⁻³ s⁻¹, "about ten orders of magnitude faster"
  than crystals, and the paper uses that as a proxy for the unstable
  clusters (The rate determining step in the two-step nucleation
  mechanism).
- So the nucleation theorem applied to the macroscopic J measures the
  crystalline nucleus inside the clusters, and the spinodal corresponds to
  ΔG₂* = 0.
- The two-step path is chosen because it is faster. The surface free
  energy between crystal and solution "is likely significantly higher" than
  between crystal and dense liquid, so direct nucleation would be slower.

### Heterogeneous substrates

Of the four parameters J₀₁, J₀₂, ΔG₁*, ΔG₂*, the answer lies between J₀₂
and ΔG₂*, and since ΔG₂* is very small near the spinodal, "the most
important parameter is J02" (The role of heterogeneous nucleation
substrates). Hence, "in contrast to the generally accepted viewpoint
heterogeneous nucleation centers assist nucleation not by lowering ΔG2*,
but by assisting the growth of the ordered clusters". Suggested mechanisms
are templating, stabilizing an intermediate structure, and catalysing bond
formation. Polarized-light nucleation of α- and γ-glycine is offered as
structuring of the dense liquid by a field.

### Other systems

The paper grades its own evidence (Other systems for which the two-step
nucleation mechanism applies). Lysozyme allows "a rather confident
conclusion". For other proteins the evidence "is less direct". Colloids
are where the evidence "is the strongest", from particle tracking by
confocal microscopy. It also cites HbS polymers, amyloid (with a molten
globule as the intermediate), urea and glycine (inferred from laser-induced
nucleation), calcium carbonate prenucleation clusters, and one block
copolymer system (theory only). For organic "oils" it says the two-step
route "has not been tested".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | In CNT, n* = 64Ω²α³/Δμ³ and ΔG* = 32Ω²α³/Δμ² for a cubic nucleus, so both fall steeply with supersaturation | strong | textbook derivation from Eq. 1 (The classical nucleation theory: Thermodynamics) |
| C2 | Homogeneous nucleation of lysozyme crystals is about ten orders of magnitude slower than CNT predicts, and the error is in the prefactor, not the barrier | moderate | one system; ν* is an order-of-magnitude estimate and Z is assumed; ΔG* is taken from the data, so the barrier cannot be wrong by construction (The classical theory overestimates …) |
| C3 | The lysozyme nucleus is 1–10 molecules, and at 4 % NaCl it drops from five molecules to one at σ = 3.1 | moderate | nucleation theorem (Eq. 4) applied to slopes in Fig. 4b, with n₀ "roughly estimated as less than 1" |
| C4 | A solution–crystal spinodal exists, past which there is no barrier, and it explains the plateau, the scatter and the maximum in J | moderate | the spinodal is defined kinetically by C3; the explanation of the scatter and the maximum leans on refs. 34, 50 |
| C5 | Metastable clusters of dense liquid, long-lived and mesoscopic, exist in homogeneous protein solutions | moderate | DLS for five proteins, AFM for one; networks excluded by a viscosity argument; the lysozyme lifetime is a lower bound |
| C6 | Lysozyme crystals nucleate inside those clusters | moderate | inferred, not observed: direct imaging exists "only for the case of stable dense protein liquid" (Fig. 7); rests on C5 and on fitting Eqs. 5–7 to Figs. 4–5, chiefly the steep fall below T_sp |
| C7 | The two-step mechanism accounts for ~10⁹ of the ~10¹⁰ shortfall | weak | order-of-magnitude arithmetic with ϕ₂ and η inside the clusters |
| C8 | Cluster formation is fast and ordering inside clusters is the rate-determining step | moderate | clusters appear within seconds; stable-droplet nucleation rates used as a proxy for unstable clusters |
| C9 | Near the spinodal, heterogeneous substrates speed nucleation through the prefactor, not by lowering the barrier | weak | inference from C4 and C8; no substrate data are presented, and it runs against the accepted view, as the paper says |
| C10 | The two-step mechanism operates in many systems beyond lysozyme | weak to moderate, by system | the paper's own grading: strongest for colloids, "less direct" for other proteins, untested for organic oils, theory only for the copolymer |
| C11 | Systems take the two-step route because it is faster | weak | rests on a surface energy that "is likely significantly higher"; Lutsko and Nicolis (ref. 107) are cited in support |
| C12 | Most industrial and laboratory crystallization runs at or near the spinodal, with nuclei of a few molecules | assertion | stated in the Conclusions as "more straightforward"; no data beyond lysozyme |

## Concepts

- **Nucleus**: a cluster of size n*, with "equal probabilities of growth and
  decay". "[B]y this definition all nuclei are critical and the term
  'critical nuclei' is redundant" (Thermodynamics). A nucleus is the point
  of even odds, not a guaranteed crystal.
- **Supersaturation**: σ ≡ Δμ/k_BT, the excess chemical potential of the
  solute over the crystal, in units of k_BT.
- **Order parameters**: concentration (dilute solution against dense
  liquid) and structure (dense liquid against crystal). The dilute solution
  and the crystal differ in both. Crystallization from solution is a
  transition along both.
- **Dense liquid**: a liquid phase much denser in solute than the solution.
  It can be stable, forming macroscopic droplets, or unstable, in which case
  it exists only as metastable mesoscopic clusters. The paper says the two
  have distinct causes and occur independently (Conclusions and
  perspectives).
- **Two-step mechanism**: a dense liquid cluster forms (step one); a
  crystalline nucleus forms inside it (step two). Fig. 3c gives the two
  barriers, ΔG₁* and ΔG₂*.
- **Solution–crystal spinodal**: the line at which n* − n₀ = 1 and the
  barrier vanishes. It is kinetic by definition, not thermodynamic.
- **Spinodal regime**: past that line, where "the rate of generation of the
  new phase is only limited by the kinetics of growth of its clusters".
- **Nucleation theorem**: Eq. 4, which gives the nucleus size from the
  slope of ln J against Δμ without a model of the nucleus.
- **Zeldovich factor**: Z, which accounts for the width of ΔG(n) around its
  maximum.

## Connections

The thermodynamics is Gibbs's, adapted to a cubic crystal; the rate law is
Volmer's, in the form of Kashchiev's *Nucleation* (2000, ref. 18). The
two-step idea was "first suggested by simulations and analytical theory":
ten Wolde and Frenkel 1997, Talanquer and Oxtoby 1998, Soga et al. 1999
(refs. 27–29). The paper reports that this theory predicted the density
and structure fluctuations "are only separated near the critical point for
liquid-liquid (L-L) separation", and coincide away from it. The experiments
the paper reviews are claimed to show two steps "under a broad range of
conditions". So the paper's claim goes beyond the simulations it credits.
The paper does not say the author proposed the mechanism.

The cluster and rate-law results come from the author's group: Pan,
Kolomeisky and Vekilov 2005 for Eqs. 5–7 (ref. 50); Filobelo, Galkin and
Vekilov 2005 for the spinodal (ref. 81); Pan et al. 2007 and 2010 and Gliko
et al. 2005 and 2007 for the clusters (refs. 66–69). The author's own 2004
paper on a dense liquid precursor (ref. 33) is cited. The Nanoscale paper
of the same year, [LIT-926](../literature.d/LIT-926.md), is not cited, and neither is De Yoreo and
Vekilov 2003, [LIT-924](../literature.d/LIT-924.md), although De Yoreo is thanked in the
acknowledgement. Lutsko and Nicolis 2006 (ref. 107) and Sear 2009
(ref. 106) are the theory offered for why the two-step route is general.
The calcium carbonate prenucleation clusters of Gebauer et al. 2008
(ref. 104) are cited as a biomineral case.

The paper does not cite Ostwald's rule of stages ([LIT-920](../literature.d/LIT-920.md)), though
the two-step route, through a metastable intermediate before the stable
crystal, is close to it in spirit.

## Bearing on the record

The paper is physical chemistry. Nothing in it is about arguments, records
or recognition. What follows is what the physics says about the analogies
the record draws, not evidence for them.

- **[CLAIM-176](../claims.d/CLAIM-176.md)** (recurrence is the nucleation threshold). The paper
  **complicates** the analogy. It does not undercut it.
  - In the physics the threshold is a size, n* = 64Ω²α³/Δμ³, and it moves
    with the driving force as Δμ⁻³. A fixed count of two has no counterpart.
    If the analogy is taken seriously, the threshold count should depend on
    how "supersaturated" the exchange is. [CLAIM-176](../claims.d/CLAIM-176.md) already leaves
    "whether 'second' is the right number" untested, and this is a reason to
    expect it is not fixed.
  - At high supersaturation the threshold disappears. Past the spinodal
    "every molecule in the solution can be an embryo", and the paper says
    most practical crystallization runs at or near that regime. Read
    across, a fast, prolific exchange (the high-supersaturation case of
    [CLAIM-186](../claims.d/CLAIM-186.md)) would be one where coding at first occurrence is the
    natural rule. That fits the claim's own exceptions ("a decision, or a
    source") but makes them the regime, not the exception. This is an
    inference from the analogy, not from anything the paper says.
  - A nucleus is a point of even odds of growth and decay, not a settled
    crystal. Coding at the threshold, on this picture, gives a thing an even
    chance of persisting, no more.
  - The claim's second job, keeping capture from flooding the record, has a
    counterpart only in the Introduction. Fast nucleation gives many
    crystals of similar size; nucleation hindered "everywhere in the growth
    container but at a few selected spots" gives few crystals that "grow
    large before the solution is depleted of nutrient". This is stated
    qualitatively, with no data.
  - The code as nucleation site: the paper argues (C9, weak) that near the
    spinodal a site works by helping clusters order, through templating or
    stabilizing an intermediate, and not by lowering a barrier. If that
    transfers, a code helps by giving structure to material already
    gathered, which is closer to [CLAIM-181](../claims.d/CLAIM-181.md)'s lattice reading than to
    a threshold reading.
- **The two-step reading** of [LIT-926](../literature.d/LIT-926.md) and [LIT-919](../literature.d/LIT-919.md) (an idea first
  recurs as a loose cluster; the threshold is when the cluster is
  recognized). The paper **supports the shape** of this reading and
  **qualifies its details**.
  - Separability. The [LIT-926](../literature.d/LIT-926.md) standing asks whether the two steps are
    separable in the physics. The paper's answer is: in the order-parameter
    plane and in rate, yes, for lysozyme. Cluster formation is ~10 orders
    faster than crystal nucleation, and the clusters persist for
    milliseconds to seconds. But the early theory separated the steps only
    near a liquid–liquid critical point, and the Lutsko–Nicolis result,
    which the paper calls "an intriguing hypothesis", has the intermediate
    "just a well developed density fluctuation", so "the two-step mechanism
    may in fact operate in systems where no intermediate is independently
    found". The first step need not leave a lasting object.
  - What transfers: step one is fast and common; step two, ordering inside
    the cluster, is slow and sets the rate. That matches the reading's picture, in which loose recurrence is common and
    recognizing it as one thing is the bottleneck. Most of
    the volume never hosts nucleation (ϕ₂ ≈ 10⁻⁷–10⁻⁶), which matches most
    loose recurrence never being coded.
  - What does not transfer: the ordering step is a spontaneous fluctuation
    inside the cluster. Nothing in the physics corresponds to an outside
    agent recognizing the cluster. And in the two-step picture the
    threshold is still a critical nucleus, ΔG₂*, inside the cluster, which
    near the spinodal is negligible. The rate is then set by the
    prefactor: how much clustered material there is (ϕ₂) and how mobile it
    is (η inside the cluster). Read across, the limit would be how much
    loosely gathered material exists and how easily it can be rearranged,
    not a moment of recognition.
  - One detail transfers as a caution. Denser clusters are more viscous and
    order more slowly, and some organic "oils" are "so viscous that no
    crystals can form in it". An idea accreted into a dense tangle might be
    harder to order, not easier. This is a suggestion from the analogy only.
- **[QUESTION-037](../questions.d/QUESTION-037.md).** The question's framing says a supersaturated
  solution may not crystallize "because crystals need a site to form on".
  The paper's own data are homogeneous rates: crystals do form without
  sites, at 0.1–1 cm⁻³ s⁻¹. What holds them back is the barrier and, more
  so, the slow ordering kinetics. Fig. 1's caption also shows that a
  supersaturated solution can yield amorphous precipitate or dense liquid
  droplets instead of crystals, and Fig. 6 has a gelation line; the paper
  does not discuss these outcomes.
- **[CLAIM-186](../claims.d/CLAIM-186.md)** (growth rate). The paper is about nucleation and
  says nothing about morphological instability or dendrites. Its only
  growth content is that crystals growing from solution have smooth
  surfaces and molecules attach only at steps covering 10⁻³–10⁻² of the
  surface. It neither supports nor tests the claim.
- **[CLAIM-181](../claims.d/CLAIM-181.md).** C9 is the only point of contact: substrates act by
  structuring, through templating, consistent with the objection's view
  that a seed passes on its lattice. The paper's evidence for C9 is
  inference, not measurement.
- No THEORY should be filed from this reading. No instruction for
  machine-learning practice; the paper does not belong in the Anthology of
  the SOTA.

## Limitations

- **One system carries the argument.** Every quantitative result is for
  lysozyme in 0.05 M Na acetate, pH 4.5, at 2.5–4 % NaCl. The other systems
  are cited, not analysed, and the paper grades their evidence as weaker.
- **The two-step mechanism is inferred for the common case.** For
  metastable clusters the evidence is that clusters exist plus a fit of a
  phenomenological model with several fitted or imported parameters
  (k₂, E*, the viscosity constants, U₁/U₀). The fit's quality is shown
  only in Fig. 5, which I could not see.
- **The CNT estimate is order-of-magnitude.** ν* is borrowed from step
  growth on large crystals and Z is assumed. The size of the discrepancy,
  and so how much of it the two-step model explains, carries that
  uncertainty. The two-step estimate leaves about one order unexplained,
  which the paper does not mention.
- **CNT's barrier formula is used on nuclei of 1–10 molecules** to extract
  α, without comment on whether a macroscopic surface free energy applies
  at that size.
- **The substrate conclusion (C9) is argued, not shown.** No measurement of
  substrate action is presented.
- **The spinodal is a definition.** It is defined by nucleus size one, so
  the statement that the nucleus is one molecule past the spinodal is true
  by construction.
  The content is that this happens at a definite line, measured for one
  system (ref. 81).
- **Slips in the manuscript.** Eq. 3 prints the exponent as −G*/k_BT,
  without the Δ. ΔG°_C is defined twice in the text after Eq. 5, once as
  "the barrier for nucleation of crystals inside the clusters" (which is
  ΔG₂*) and once as the excess free energy of a molecule in a cluster.
  E* is said to be found by "fitting Eq. (7)", but Eq. 6 is meant. The
  maxima in J(T) are put "in Fig. 4", but they are in Fig. 5. The calcite
  free energy landscape is "in Fig. 2c", but there is no Fig. 2c; Fig. 3c
  is meant. "Fig. 4c" is cited and does not exist. Eq. 7's last factor,
  exp(−E_η/k_BT), would make viscosity fall as temperature falls, which
  contradicts the text around it; the sign is probably a slip. α is
  described as the surface free energy "between the dense liquid and the
  solution", though Eq. 2 is applied to a crystal nucleus. I did not check
  whether the published version corrects these.
- **Some evidence is unpublished.** The point about viscous organic oils
  rests on "unpublished evidence from the pharmaceutical industry".

## Open questions

- Is two-step nucleation general, or limited to systems with suitable
  clusters? The paper says both: "not all solutions would support the
  existence of such clusters", yet the mechanism "may in fact operate in
  systems where no intermediate is independently found". Direct imaging of
  a crystalline nucleus forming inside a metastable cluster, as Fig. 7 does
  for a stable droplet, would settle it for one system.
- How do heterogeneous substrates act near the spinodal? C9 predicts that
  substrates change J₀₂ and leave ΔG₂* alone. Rates measured on substrates
  of varied structure, analysed with the nucleation theorem, would test it.
- What sets the size of the clusters? The paper rules out one class of
  explanation and cites a mechanism based on long-lived complexes (ref. 67)
  without settling it.
- For the record: does the threshold count depend on the pace of an
  exchange, as the physics would suggest? A comparison of drift in fast and
  slow exchanges under first- and second-occurrence rules would test the
  analogy, but that test belongs to [CLAIM-176](../claims.d/CLAIM-176.md) and [CLAIM-186](../claims.d/CLAIM-186.md), not
  to this paper.
