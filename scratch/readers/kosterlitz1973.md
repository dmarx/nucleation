# Reader notes: kosterlitz1973 (LIT-2969)

Kosterlitz and Thouless (1973), "Ordering, metastability and phase transitions
in two-dimensional systems", J. Phys. C 6, 1181, doi:10.1088/0022-3719/6/7/010.

## Step 1: copies located (2026-11-22)

- OpenAlex (api.openalex.org, no email sent): oa_status bronze, one location,
  the publisher PDF https://iopscience.iop.org/article/10.1088/0022-3719/6/7/010/pdf
  (publishedVersion, is_oa true); any_repository_has_fulltext false.
- Fetched 2026-11-22: HTTP 403, Cloudflare "Just a moment..." challenge. Stopped;
  not retried. Kind: publisher's own free (bronze) copy. Outcome: Unfetched.

## Step 2: neighbours located and read (2026-11-22)

The original was not read (Cloudflare at its only located copy). Two neighbours read:

**N1. Kosterlitz, Nobel Lecture "Topological Defects and Phase Transitions"**, 8 Dec 2016,
in Les Prix Nobel / The Nobel Prizes 2016, pp. 85-99.
https://www.nobelprize.org/uploads/2018/06/kosterlitz-lecture.pdf (PDF, 15 pp., HTTP 200),
linked from https://www.nobelprize.org/prizes/physics/2016/kosterlitz/lecture/ . Kind: the
rights holder's own copy: the page states "Copyright © The Nobel Foundation 2016" beside
"Read the Nobel Lecture", and the host is the Nobel Foundation's site (ADR-102). Read in full
(text layer; figures seen only as captions). Also published as Rev. Mod. Phys. 89, 040501
(2017), doi:10.1103/RevModPhys.89.040501, not fetched. The slides PDF
(https://www.nobelprize.org/uploads/2018/06/kosterlitz-lecture-slides.pdf, "Copyright © J.
Michael Kosterlitz") located, not read.
Stands in for: the 1973 paper's physical argument (defect free energy, Coulomb-gas mapping,
dielectric screening, crystal/superfluid/magnet/superconductor cases, metastable topological
sectors), told by its first author 43 years on, with its errors named. Does not stand in for
the paper's equations, its own wording, or what it did and did not derive (e.g. η(T)).

**N2. Drouin-Touchette (2022), "The Kosterlitz-Thouless phase transition: an introduction for
the intrepid student"**, arXiv:2207.13748v1 (SciPost Physics Lecture Notes submission),
https://arxiv.org/pdf/2207.13748v1 (PDF, 43 pp., HTTP 200). Kind: arXiv. Read §1-3 (pp. 2-14)
and the passages on 2D melting and superfluids (§5); skimmed §4 (Monte Carlo) and §6.
Not held (grep for 2207.13748 / Drouin: no hit). Stands in for: the spin-wave algebraic
correlations, the vortex free-energy argument "from Kosterlitz and Thouless", the Coulomb-gas
mapping and the RG flow; but it attributes the RG equations to Kosterlitz 1974 and José et
al. 1977, not to the 1973 paper.

## Step 3: report

### Outcome for LIT-2969
**Unfetched** (ADR-053). A lawful copy was located at
https://iopscience.iop.org/article/10.1088/0022-3719/6/7/010/pdf. It is the publisher's free
(bronze) copy, listed by OpenAlex and Semantic Scholar. Fetching it on 2026-11-22 returned
HTTP 403 with a Cloudflare "Just a moment..." challenge, so I stopped. arXiv has nothing
(1973). There is no repository copy (OpenAlex any_repository_has_fulltext: false). I read the
neighbours N1 and N2 instead. Each is a work of its own (ADR-114) and must not be filed under
LIT-2969.

### N1 (Nobel lecture): Summary
Kosterlitz tells how he and Thouless came to 2D defect-driven transitions, then sets out the
physics:
- Mermin-Wagner and Peierls forbid long-range order in 2D, yet experiments showed abrupt
  transitions.
- The way out is "topological order". Vortices interact logarithmically, so the system is a
  2D Coulomb gas, and the sign of a free vortex's free energy changes at a temperature.
- The RG equations (Kosterlitz 1974) give a universal jump in the superfluid density.
  Bishop and Reppy (1978) confirmed it.
- It then covers 2D melting (KTHNY, the hexatic phase) and superconducting films.

### N1: Key results (page numbers are the volume's)
- No LRO in 2D (p. 87): low-energy phonons give "a mean square deviation of atoms ...
  increasing logarithmically with the size of the system, L".
- The way out (p. 89): "there can be a more subtle type of order called topological order in
  some two dimensional systems."
- Metastability, the word in the title (p. 90): the winding numbers n_x, n_y "are numbers
  defining a particular metastable state. Transitions can take place from one metastable state
  to another only if a vortex-antivortex pair is formed ... there is an energy barrier
  proportional to the logarithm of the system size". For the 2D Heisenberg model the barrier
  "is of order unity ... which implies that there is no ordered state" (p. 90).
- Defect free energy (p. 92): "∆F = ∆E − T∆S = kBT(πK0(T) − 2) ln(L/a)". For 2kBT < πJ a
  free vortex has probability → 0; above it there is "a finite concentration of free
  vortices". The lecture places this argument in the 1972 letter [15] (J. Phys. C 5 L124),
  not in the 1973 paper.
- Self-consistent screening (pp. 92-93): a scale-dependent dielectric function ε(r).
  "Kosterlitz and Thouless [15] derived this self consistent integral equation for the
  effective interaction energy [16]" ([16] is the 1973 paper). Its error: "KT made an
  unnecessary approximation by replacing U(r) by K(r) ... but this led to incorrect results. A
  proper treatment has been given by Young [21] who showed that this is equivalent to the
  renormalization group equations of Kosterlitz [17]" (Kosterlitz 1974).
- Transition criterion (p. 93): "a transition between a phase of bound dipoles and a phase of
  free charges will happen when πK(∞) = 2". Fig. 2 caption: "for T ≤ Tc, y(∞) = 0".
- Universal jump (p. 94): ρs(Tc−)/Tc = 2m²kB/πħ² = 3.491×10⁻⁸ g cm⁻² K⁻¹, "an exact,
  inescapable prediction". The data were "obtained and plotted before the authors were aware
  of our theoretical prediction".
- Melting error (p. 95): "In our paper, we ignored the second term ... which was an
  unfortunate error ... We assumed that dislocation unbinding led directly to an isotropic
  fluid which is now known to be wrong". The hexatic phase has "algebraic orientational order"
  (pp. 95-96). The 2D crystal has "no δ-function Bragg peaks ... but algebraic peaks",
  S(q) ∼ |q − G|^(−2+ηG(T)) (p. 96).
- Superconducting films (p. 98): "In our original paper, we stated that true
  superconductivity in a 2D superconducting film could not exist because of the finite
  penetration depth λ(T) which limits the range of the logarithmic interaction ... the
  vortices are always free at any T > 0".

### N2 (Drouin-Touchette notes): Key results
- Spin waves alone (§2.2, eq. 18, p. 5): g(r) ≈ (πr/a)^(−kBT/2πJ) = (πr/a)^(−η(T)). "the
  correlation function falls off algebraically at all finite temperatures ... the XY model has
  an infinite correlation length ξ = ∞, and η is temperature dependent. This means that, at
  all low-temperatures, the system is critical."
- Magnetization (§2.1, eqs. 8-9, p. 4): ⟨Sx⟩ = exp(−(T/2J) ln(L/a)) → 0, "directly the
  statement of the Mermin-Wagner theorem".
- Vortex argument (§2.3, eq. 24, p. 7): ∆F = (πJn² − 2kBT) ln(L/a), so kBTc = πJ/2. "This
  remarkably simple argument from Kosterlitz and Thouless is not too far from the truth".
- Spin waves have no transition (§3.1, p. 10): "ZS.W. is perfectly analytic ... we expect all
  of the phase transition properties to come from the topological term".
- Line of fixed points (§3.3, p. 12): the flows "terminate on a line of fixed points at which
  y0 = 0 and K_eff^−1 ≤ π/2. In this regime, the fugacity becomes irrelevant." The notes credit
  the RG equations (eq. 44) to "José, Kirkpatrick, Kadanoff and Nelson in 1977". Their ref [5]
  is Kosterlitz 1974.
- Not a power-law transition (§3.4, eq. 50, p. 14): ξ ≈ a exp(π²/(8b) √(T_KT/(T−T_KT))),
  which diverges "not in the same way as usual second-order phase transitions". The free energy
  "only has an essential singularity". §1 (p. 3) calls it "an infinite-order phase transition".
- §5 (pp. 26-27): "These settings were pointed out in the first paper by Kosterlitz and
  Thouless as potential realizations". In the hexatic phase ⟨ψ*(r)ψ(0)⟩ ∼ r^(−η(T)).

### Contribution (as the neighbours report it)
A finite-temperature transition in 2D with no symmetry breaking and no order parameter. It
separates a disordered phase from a low-temperature phase whose correlations follow a power
law over a whole range of T. Its driver is the unbinding of topological defects bound by a
logarithmic interaction. The same mechanism covers XY magnets, superfluid films and 2D
crystals.

### Assumptions (neighbours)
- Short-range interactions with U(1) (or translational) symmetry, in exactly 2D.
- A logarithmic interaction between defects across the whole system. This fails for charged
  superconductors beyond the penetration depth λ.
- Dilute vortices: small fugacity, unit charges only.
- Equilibrium statistical mechanics.
- For melting, the angular term of the dislocation energy is neglected (corrected later).

### Concepts
BKT transition; topological defect (vortex, dislocation, disclination); winding number and
topological sector; 2D Coulomb gas; vortex fugacity; dielectric screening; spin stiffness
(helicity modulus); quasi-long-range order; line of fixed points; the Nelson-Kosterlitz
universal jump; infinite-order transition and essential singularity; hexatic phase; KTHNY
melting.

### Verdict on how the exchange characterized the work
- LIT-2969's summary says "A phase transition without symmetry breaking ... driven by the
  unbinding of vortex pairs, with quasi-long-range order below it". **Supported** by N1
  (pp. 89-93) and N2 (§2-3), but only for the BKT line of work as a whole. I could not check
  which parts the 1973 paper itself states, as against the 1972 letter or Kosterlitz 1974.
- "evades the Mermin-Wagner theorem" is **loose**. Nothing evades the theorem: there is still
  no LRO (N1 p. 87; N2 §2.1). The work reconciles a transition with the theorem through a
  different kind of order ("topological order", N1 p. 89). Better wording: "a transition
  consistent with Mermin-Wagner".
- "topological order through vortex unbinding" is the lecture's own phrase (p. 89). It is the
  1970s sense (winding-number sectors), not Wen's later quantum sense. Say so if filed.
- CLAIM-841's row "Line of fixed points (2D XY), C(r) ∝ r^(−η(T)), η = T/2πρ_s; LIT-2969":
  **the attribution is qualified**.
  - Both neighbours place the RG and the "line of fixed points" in Kosterlitz 1974 (J. Phys.
    C 7, 1046) and José et al. 1977.
  - The lecture says the 1973 self-consistent treatment's approximation "led to incorrect
    results" near Tc.
  - So the 1973 paper should ground the row together with Kosterlitz 1974. The record does
    not hold Kosterlitz 1974: record/literature.d has no "Kosterlitz" hit besides LIT-2969.
  - Whether the 1973 paper states η(T) is unchecked.
  - The spin-wave exponent is T/2πJ in N2 eq. 18 (J the stiffness). This matches the row's
    T/2πρ_s, with ρ_s the renormalized stiffness.

### Bearing on named codes
- **CLAIM-841: supports, with qualifications on the attribution and on the word
  "criticality".**
  - The row is supported. N2 §3.3: the flows "terminate on a line of fixed points at which
    y0 = 0 ... the fugacity becomes irrelevant" for all T < T_KT, so T needs no tuning.
  - But N2 calls that phase "critical" (§2.2, §3.4: "The XY model is critical in its
    low-temperature phase"). The claim's narrow sense of "criticality" (a tuned transition;
    see its "What it does not say") is not universal usage. A NOTE should flag that a source
    calling the XY phase critical does not contradict the claim.
  - The transition itself is not a power-law critical point either: ξ diverges as an
    essential singularity (N2 eq. 50).
- **QUESTION-508: narrows it, a partial answer for one class.**
  - The neighbours give the mechanism that A's "line of fixed points" only names. The one
    candidate relevant perturbation, the vortex fugacity y, is irrelevant (dy/dl = (2 − πK)y
    < 0) throughout πK > 2. In 2D a free defect's energy (πK ln L) and its entropy (2 ln L)
    scale alike (N1 p. 92, N2 eq. 24). K is marginal and is only renormalized.
  - So the relevant direction is held at zero by symmetry (U(1), which gives the winding
    number) together with dimension (the logarithmic interaction), over a range of stiffness.
    "Symmetry removes θ²" alone does not account for it.
  - A finite interaction range destroys the phase: in a charged superconducting film λ frees
    vortices at any T > 0 (N1 p. 98). This has the shape of the question's counterexample: an
    introduced length scale ends the untuned phase.
- **CLAIM-842: qualifies.**
  - N2 §2.1-2.2 confirms the d = 2 logarithm: ⟨Sx⟩ = (L/a)^(−T/2J).
  - But at d_s = 2 exactly, what survives is algebraic order, not no order. The Gaussian
    elastic energy alone has no transition at all (N2 p. 10, "ZS.W. is perfectly analytic").
    Whether the algebraic phase survives is set by defects (vortices), which no Gaussian
    elastic energy contains.
  - So "whether conventional order survives is set by the spectral dimension" holds for
    conventional LRO. At d_s = 2 the claim's Gaussian premise leaves the phase's fate open,
    and a learned-manifold analogue would need its defects identified.

### Recheck
After reading I grepped record/ again for: topological sector, metastable, winding, Coulomb
gas, hexatic, KTHNY, essential singularity, infinite-order, universal jump, Goldstone, spin
wave, Peierls, penetration depth. Held entries the first search missed:
- **CLAIM-694** (a conserved topological charge fixes the sector): **supports/parallel**.
  N1 p. 90: the winding numbers define "a particular metastable state", with a barrier ∝ ln L
  between states. The 2D Heisenberg model has an invariant N too, but its barrier is O(1), so
  that sector protects nothing. This is a clean case of a topological invariant that protects
  only when its energy barrier grows with system size.
- **CLAIM-606** (persistence by topological charge): parallel, from the same passage. It adds
  the barrier condition.
- **TERM-139** (relevant, irrelevant, marginal): used. The BKT flow is its textbook case: y is
  irrelevant below T_KT and relevant above, and K is marginal along the fixed line.
- **THEORY-1095** (Toner-Tu LRO in 2D flocks): contrast. The equilibrium 2D XY model gets
  only QLRO (N2 §2.2); Toner-Tu's true LRO is what nonequilibrium adds.
- **CLAIM-846** (Gaussian spin-wave field): parallel. N2 §2.2 is that Gaussian computation.
- **LEAD-209** (response to a symmetry-breaking field): the λ cutoff (N1 p. 98) is a second
  kind of scale-introducing perturbation. The protocol could list it beside a field.
- **NOTE-124 / LIT-141** (McKenzie, emergence): background. It already cites BKT and the
  hexatic as phases predicted before they were found. N1 bears this out: the jump data were
  plotted "before the authors were aware" (p. 94), and Young's modulus was measured "several
  decades" later (p. 97).
- LIT-878 / NOTE-681 (dimer model, BKT), THEORY-2032 (topology in active matter) and
  QUESTION-490: background only.

### Limitations
- The 1973 paper was not read. Its equations, its own claims, what it got wrong in its own
  words, and whether it states η(T) or a fixed-point picture are all unchecked.
- N1 is a retrospective by the first author and partly autobiographical. Its equations came
  out garbled in text extraction; I checked them against N2 where the two overlap.
- N2 is an unrefereed, student-level submission. It has an unresolved cross-reference
  ("Appendix ??") and some typos. Its figure on p. 13 was not seen.

### Candidate THEORY (for N1, the Nobel lecture; not for LIT-2969)
"Kosterlitz's Nobel lecture holds that the two-dimensional planar rotor and superfluid film
have a finite-temperature topologically ordered phase without long-range order, in which
winding-number sectors are separated by barriers growing as ln L, ended when vortex-
antivortex pairs unbind at πK = 2, and that the renormalization-group equations predict a
universal jump ρs(Tc−)/Tc = 2m²kB/πħ² confirmed in helium-4 films."
promote_when: the primary papers it summarizes (Kosterlitz and Thouless 1972/1973; Nelson and
Kosterlitz 1977) are read and state the free-vortex criterion and the jump, and the
Bishop-Reppy 1978 measurement is read and agrees with the stated value.

If N2 is filed: "Drouin-Touchette's notes derive that the 2D XY model's spin waves give
correlations falling as r^(−T/2πJ) at every low temperature, and that vortex fugacity flows to
a line of fixed points for K^−1 ≤ π/2, so the whole low-temperature phase has infinite
correlation length." promote_when: the derivation is checked against Kosterlitz 1974 or
José et al. 1977.

### Other works read or quoted
None beyond N1 and N2. Catalogue pages only: the OpenAlex and Semantic Scholar records for the
DOI, and the nobelprize.org lecture page (for the copyright statement).
