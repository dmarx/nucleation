---
number: 2
status: Read
formerly:
- NOTE-tmp5k01m
paper: LIT-009
title: 'Eulalia impact shower'
version: 2
history:
- version: 2
  date: '2026-09-25'
  note: >-
    Read in full (Full text of arXiv:2606.05036v1 (3 Jun 2026; the title
    page says "Draft version June 4, 2026", "Submitted to The Planetary
    Science Journal"), 42 pp. I read the abstract, §1–§8, the
    acknowledgements, the reference list and Appendix A.1–A.3. Text came
    from raw4/2606.05036.pdf via PyMuPDF (no pdftotext on this host).
    Figures 2–21 are plots, so I read their captions and the prose around
    them, not the images; any number that appears only in a figure (e.g. the
    J3:1 influx-versus-time curves in Figs. 7–11) is unverified. I did not
    compare against the typeset PSJ version (DOI 10.3847/PSJ/ae74cc, vol. 7
    art. 171), whose title shortens "800-Million-Year-Old" to "800
    Myr-old".). Upgraded from `Skimmed` to `Read`: the claims table,
    assumptions and results are new, and the skim is corrected where the
    full text disagreed.
date: '2026-09-25'
summary: >-
  The paper builds a collisional-plus-dynamical source model. In its
  preferred Solution 5, the Eulalia parent body breaks up T = 865 Myr ago
  at a_c = 2.48 au next to the Jupiter 3:1 resonance. The model sends
  6,995 D ≥ 2 km and 833 D ≥ 5 km fragments into the J3:1 (Table 1, before
  a ≈1.5× collisional correction). With impact probabilities per resonance
  entrant of 5.4×10⁻³ (Venus), 4.2×10⁻³ (Earth) and 0.6×10⁻³ (Mars), and
  the Moon at 1/20 of Earth, the expected largest impactor is D ≈ 8 km on
  Earth and Venus, 4.5 km on Mars and ">3 km" on the Moon. A Monte Carlo
  of 7 lunar projectiles puts the seven lunar craters dated 760–820 Ma
  "generally … within the 1σ" envelope. The authors conclude the breakup
  "can plausibly account for" the ~800 Ma lunar crater cluster, although
  on average the model's projectiles are too small to make Copernicus.
---

<!-- inactive-ok-file: LIT-009 — Deferred: the paper is placed by this reading; the directive lapses when its status changes -->

# NOTE-002: Eulalia impact shower

## Contribution

The paper gives the first quantitative source model for the proposed ~800 Ma lunar impact spike. It re-identifies the Eulalia asteroid family against the overlapping New Polana and Nysa/Hertha families, using 777,353 proper-element orbits, 134,314 albedos and 306,856 SDSS colour records (§3.2.1). It fits a Yarkovsky/YORP chronology model under three choices of family centre (§3.3–§4). For the first time in this model line, it records the flux of synthetic fragments crossing into the J3:1 (§3.3, "This kind of calculation was not attempted in our previous works"). It then corrects for WISE incompleteness (F1 ≈ 2.3, §5) and for collisional loss (≈1.5× for 3 < D < 10 km, §6.2), and converts resonance entrants into planetary impacts using 61,065 J3:1 test particles from Nesvorný et al. 2023 (§6.3). The result is an expected impactor size-frequency distribution for Venus, Earth, Mars and the Moon (Fig. 16), compared against the lunar crater cluster (Figs. 17–18).

## Key insight

A breakup matters to the terrestrial planets less for its size than for where it happens. A C-type parent of D ≥ 100–200 km sitting on the inner edge of the J3:1 injects part of its debris straight into a fast delivery resonance. It then feeds more over 10⁸-year timescales as Yarkovsky drift carries outward-drifting fragments into the resonance. That produces a delayed, prolonged shower of multi-km bodies. The same collisional physics explains why such showers can hide in the small-crater "clock": small fragments grind down within a few Myr, while multi-km ones survive for hundreds of Myr. A family can therefore raise the flux of large impactors without visibly changing the small-crater production rate used for dating (App. A.2).

## Assumptions

- **Lunar crater ages are N(1)-scaled from one calibration point.** Ages for 45 of Terada et al.'s 59 D ≥ 20 km craters come from their N(1) superposed-crater densities. This assumes a constant small-crater production rate over 3 Gyr (App. A.2) and anchors the scale on Copernicus = 800 Ma from Apollo 12 ray samples (§2.1). The check is two craters: Aristillus, model 1510 ± 140 vs sample 1400 ± 60 Ma, and Autolycus, 1930 ± 190 vs 1940 ± 10 Ma. The seven "~800 Ma" craters are therefore *defined* as craters whose N(1) matches Copernicus's, so their absolute date is Copernicus's by construction.
- **Background flux varies slowly.** Between 650 and 750 Ma it is taken to be as low as between 300 and 650 Ma, so the 800 Ma event "should stand out" (§2.2). This rests on Mazrouei et al. 2019a and Fig. 2.
- **Family membership.** The E0 box is 0.125 ≤ e ≤ 0.167 and 0.037 ≤ sin I ≤ 0.063, restricted to dark objects (p_V ≤ 0.125). The border is the C★ isoline from the contrast function r(C, a_c; ΔC) = N(C−ΔC, C; a_c)/N(C, C+ΔC; a_c) with ΔC = 1.5×10⁻⁵ au (Eq. 3). Only the a ≤ a_c half of the "V" is usable, because the resonance has removed the other half. The contrast maximum is at a_c ≃ 2.456 au (r_max ≃ 7.2), but the authors test a_c = 2.47, 2.475 and 2.48 au, following prior arguments that (495) Eulalia diffused from 2.475–2.48 au to its current ~2.486 au. The correlation line is C★(a_c) = −[7.08 + 53(a_c − 2.455)]×10⁻⁵ au (Eq. 4).
- **Chronology model.** H(C, a; a_c) = 5 log₁₀((a − a_c)/C) (Eq. 1). Ejection is isotropic with v_ej(D) = v5·(5 km/D). Rotation periods are Maxwellian, peaking at 6 h, and obliquities are isotropic. Stochastic YORP uses τ_YORP = τ0·√D, with τ0 from 0.5 to 10 Myr. Bulk density ρ = 1.2–1.5 g cm⁻³ is Bennu-motivated, as is thermal inertia Γ = 100–300 SI. Only members with H ≤ 17.5 are used, in 19 bins of ΔC = 5×10⁻⁶ au, with σ = √dN inflated by a factor of 1–2 in the first six bins. Fit parameters are p = (v5, T, c_YORP), obtained by minimising χ² (Eq. 5). ρ, Γ and τ0 are gridded, not fitted, so "we cannot evaluate their correlation with the three internal parameters" (§3.3). The J3:1 border is taken as a = 2.487 au.
- **Scalings stated, not derived.** T ∝ ρ, T ∝ Γ and T ∝ τ0^α with α ≃ 1/3 (§3.3). Solution 3 (T = 965 Myr) is noted to break the ρ–Γ scaling, "suggest[ing] … a rather flat minimum" in χ².
- **Incompleteness.** Dark and bright objects are taken as complete in WISE W3 at H ≤ 17.6 and H ≤ 16.0 respectively (both ≈1.7 km), using NEATM with η = 1.08. The Nesvorný et al. 2024a proper-element catalogue is assumed complete to H = 17.6. F2 = 10^(γ_MB·ΔH) = 10^(0.3×1.6) ≈ 3.02. F1 is "a knob" tuned by eye to 2.3 in Eq. 6, N = F1[(1 − f)N_dark + F2 f N_bright] (§5).
- **Collisional evolution.** CoDDEM (a 1-D code) uses the Bottke et al. 2020 main-belt SFD and neglects intra-family collisions. The initial remnant SFD at small sizes extrapolates the 3 < D < 10 km power law (§6.2).
- **Delivery.** Impact probabilities come from Nesvorný et al. 2023 J3:1 particles with osculating I ≤ 7.5° (61,065 of 100,000; 257 hit Earth). The Moon is taken as 1/20 of Earth by gravitational cross-section, not simulated (§6.3). Crater scaling is Shoemaker et al. 1990 per Stuart & Binzel 2004, with impact velocity 19.2 km s⁻¹ and equal projectile and target densities (App. A.3).
- **Only Solution 5 is propagated.** "If Solution 5 cannot produce an adequate impact shower, the results from Solutions 1–4 are unlikely to be relevant" (§6.2). The impact numbers are therefore an upper-yield case among the five, not a central estimate.

## Key results

- **Lunar crater cluster (§2.1, Fig. 2).** Seven craters have mean model ages of 760–820 Ma: Al-Khwarizmi 22.5, Stefan 26, Saha 29.4, Godin 35.1, Das 36.6, Lowell 65.5 and Copernicus 93.1 km. Three more (54S 19.7, Klute 30.2, Stevinus 70.3 km) date to 900–930 Ma and are conservatively excluded from the comparison (§6.4).
- **Glasses (§2.3, Fig. 3b).** The summed Gaussian age profile of 118 Apollo impact glasses (Ghent et al. 2021) shows an ~800 Ma peak, like the crater profile. The authors concede the glasses probably record 1–5 km craters, not D ≥ 20 km ones, and that gardening and Ar-diffusion survival biases affect the young end.
- **Meteorite shock ages (§2.4).** There are ~800 Ma ⁴⁰Ar/³⁹Ar ages in H chondrites (LAP 031308, Travis County; Dimmett less certain), L chondrites (~700–800 Ma: Cat Mountain, Y 74445, NWA 091) and one of eight Chelyabinsk LL ages. Attributing them to Eulalia projectiles hitting parent bodies is a favoured interpretation, and the paper says "Additional modeling work will be needed".
- **Family fit (§3.2, Fig. 6).** Canonical a_c = 2.475 au, C★ = −8.14×10⁻⁵ au, mean p_V = 0.055. SFD power-law slopes for 4–11 km are −2.95 (all members) and −3.42 (excluding possible Polana H < 14 bodies). A slope change at ≃4 km is attributed to collisions and one at ≃2.8 km to incompleteness. A zeroth-order age of 0.8–1 Gyr (ρ ≈ 1.3, p_V ≈ 0.055) uses Nesvorný et al. 2015a's Eq. 1. The cluster offsets imply ≈120 m s⁻¹ ejection and an anisotropic breakup (§3.2.2).
- **Solutions (§4).**
  - Sol. 1: a_c 2.475, ρ 1.3, Γ 200, τ0 1 → T = 785 Myr, v5 = 32 m s⁻¹.
  - Sol. 2: Γ 230 → T = 855 Myr, v5 = 14.
  - Sol. 3: ρ 1.5, Γ 200 → T = 965 Myr, v5 = 14.
  - Sol. 4: a_c 2.47, ρ 1.5, Γ 200 → T = 920 Myr, v5 = 20.
  - Sol. 5: a_c 2.48, ρ 1.3, Γ 230 → T = 865 Myr, v5 = 30.
  - The flux of 2 km bodies is ≈5× that of 4 km bodies and peaks in the first ~100 Myr.
- **Table 1 (J3:1 yields after F1 recalibration, before the collisional factor):**

  | Solution | D ≥ 2 km | D ≥ 3 km | D ≥ 4 km | D ≥ 5 km |
  |---|---|---|---|---|
  | 1 | 6090 | 2932 | 1464 | 750 |
  | 2 | 4510 | 2158 | 1100 | 529 |
  | 3 | 4554 | 2198 | 1132 | 533 |
  | 4 | 4400 | 2120 | 1074 | 531 |
  | 5 | 6995 | 3326 | 1645 | 833 |

  Across solutions the yields differ by at most a factor of ≈1.6.
- **Incompleteness (§5).** 3,322 WISE objects fall in the zone, and 2,386 fall within C★ at a ≤ 2.475 (2,064 dark, median p_V 0.057; 322 bright, median 0.26). The size-matched sample is 1,784 dark and 244 bright. Bright interlopers are ≈12% overall, ≈5% for |C| > 5×10⁻⁵ au and ≈25% for |C| < 4×10⁻⁵ au. F1 ≈ 2.3 and F2 ≈ 3.02.
- **Collisions (§6.2, Fig. 14).** The remnant family loses a factor of ≈1.5 for 3 < D < 10 km (the Fig. 14 caption says 3 < D < 8 km), with modestly more below 3 km. The modelled remnant matches the observed SFD for 3 < D < 15 km.
- **Delivery (§6.3, Fig. 15).** Impact probability per J3:1 entrant is 5.4×10⁻³ (Venus), 4.2×10⁻³ (Earth) and 0.6×10⁻³ (Mars). Median delay from resonance entry to impact is 6.4, 7.5 and 15.7 Myr for Mars, Earth and Venus. "The majority of the Eulalia impact shower … would take place within the ~700–850 Ma time window."
- **Impacts (§6.4, Fig. 16).** The largest impactor on average is D ≈ 8 km on Earth and Venus (versus ~10 km for Chicxulub), with "the order of 5" D > 5 km impactors, each making a crater ≥ Popigai (~100 km). The largest on Mars is 4.5 km and on the Moon > 3 km. Only D = 2–5 km is modelled; larger and smaller sizes are extrapolated (dashed curves) and called "modestly conceptual".
- **Monte Carlo (§6.4, Fig. 18).** 10,000 trials each draw 7 lunar projectiles with D > 1 km. The observed crater-projectile sizes "generally fall within the 1σ envelope".
- **Small-crater clock (App. A.2).** A tenfold small-body flux lasting 5 Myr adds the equivalent of 50 Myr of impacts, a ~6% change in small-crater density on an ~800 Myr-old surface. The argument: family showers enhance large-impactor flux for 10⁸ years, but small-impactor flux for only a few Myr.
- **Venus surface age (§7.3).** Earth has 38 D ≥ 20 km craters younger than 650 Myr on cratons covering 10.7 ± 3.1% of its surface, which scales to 355 (+145/−80) global. Venus, with the NEOMOD3 SFD fitted to craters ≥ 25 km, yields ~380. The Venus surface age comes out ≈650 Myr, "give or take the order of 100 Myr".
- **Mars calderas (§7.2, Fig. 19).** The summed ages of 36 calderas from Robbins et al. 2011 (with R_b = 2.8) show sharp peaks near 140, 220 and 800 Ma and subdued ones near 480 and 1090 Ma.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Seven D ≥ 20 km lunar craters have model ages of 760–820 Ma, pointing to a spike near 800 Ma | moderate | N(1) data from Terada et al. 2020 scaled to Copernicus = 800 Ma, checked on 2 sample-dated craters (§2.1). The absolute date is inherited from one calibration crater |
| C2 | Lunar glass ages and meteorite shock ages independently show ~800 Ma events | weak | Summed-Gaussian profile of 118 glasses (Fig. 3b) with admitted size and survival biases. A handful of meteorite ages, some flagged uncertain (§2.3–2.4) |
| C3 | Background impact flux was low enough around 650–750 Ma for an 800 Ma shower to stand out | weak | Reading of Fig. 2 plus Mazrouei et al. 2019a. "Assuming the background flux changes slowly" (§2.2) |
| C4 | The Eulalia family formed ~800–900 Ma | moderate | χ² Yarkovsky/YORP fits give T = 785–965 Myr across 5 solutions (not the stated 800–900). No formal errors. ρ, Γ and τ0 gridded, not marginalised (§3.3–§4) |
| C5 | About three-quarters of the family entered the J3:1 over ~150 Myr | weak | Geometric first approximation (§3.1). The simulation outputs (Table 1, Figs. 7–11) are absolute yields, and the fraction is not reported |
| C6 | Solution 5 delivers ≈7,000 D ≥ 2 km and ≈830 D ≥ 5 km fragments to the J3:1 | moderate | Table 1, calibrated with F1 ≈ 2.3, where F1 was tuned by eye (§5) |
| C7 | The remnant family lost ≈1.5× of its 3 < D < 10 km population to collisions | moderate | CoDDEM run for Solution 5 only, matched to the observed SFD over 3–15 km (Fig. 14) |
| C8 | J3:1 entrants hit Venus, Earth and Mars with probabilities 5.4, 4.2 and 0.6 ×10⁻³ | strong | Direct impacts counted in 61,065 test particles (§6.3). The Moon's value is a 1/20 cross-section assumption |
| C9 | The largest expected Eulalia impactor was ≈8 km on Earth and Venus, 4.5 km on Mars and > 3 km on the Moon | moderate | Product of C6 × C7 × C8 for Solution 5 (Fig. 16). The most favourable solution; sizes above 5 km extrapolated |
| C10 | The modelled shower is consistent with the seven ~800 Ma lunar craters, Copernicus included | weak | Monte Carlo of 7 projectiles "generally" within 1σ (Fig. 18). On average the projectiles are too small for Copernicus (§6.4). The 7-projectile count is taken from the observed craters |
| C11 | The Eulalia shower may have caused or contributed to the Bitter Springs Anomaly, Snowball Earth onset and eukaryote diversification | assertion | Analogy with Chicxulub and the 466 Ma L-chondrite breakup. The authors call it "necessarily speculative" (§7, §7.1.2) |
| C12 | Eulalia impacts may have triggered a pulse of Martian volcanism ~800 Ma via seismic shaking | assertion | Coincidence of the 800 Ma peak in 36 caldera ages (Fig. 19) and a Zunil/Cerberus Fossae analogy. The paper concedes it "could be considered a fluke" (§7.2) |
| C13 | The Venus surface age is ≈650 ± ~100 Myr; any link to Eulalia needs a predisposed Venus | informal argument | Earth-craton crater scaling compared with the Venus crater SFD (§7.3). Called "highly speculative" |
| C14 | Family showers enhance large-impactor flux for 10⁸ yr without disturbing the small-crater dating clock | informal argument | Collisional-lifetime reasoning and a back-of-envelope 6% estimate (App. A.2) |

## Method

The pipeline is a chain of multiplications (§3–§6):

1. **Catalogue assembly (§3.2.1).** Proper elements, MP3C albedos and SDSS colours, with a★ = 0.89(g−r) + 0.45(r−i) − 0.57 (Eq. 2).
2. **Membership (§3.2.2).** Dark objects in the E0 box, then the V-shape border C★(a_c) from the contrast function (Eqs. 3–4). The large, high-inclination bodies that may be Polana are included in one SFD variant and excluded in the other.
3. **Chronology and resonance flux (§3.3).** A synthetic family is evolved in (a, H) with Yarkovsky drift and stochastic YORP (dt = 0.2 Myr, mapped every 2 Myr). χ² is fitted on dN(C), and crossings of a = 2.487 au are counted as J3:1 influx.
4. **Bias correction (§5).** WISE W3 completeness limits, a bright-interloper fraction f per C-bin, and F1 and F2 (Eq. 6).
5. **Collisional correction (§6.2).** CoDDEM applied to the remnant family SFD over T.
6. **Delivery (§6.3).** Empirical impact probabilities and delay distributions from Nesvorný et al. 2023 J3:1 particles.
7. **Comparison (§6.4).** Shoemaker scaling converts impactors to crater sizes, and a 7-projectile Monte Carlo is set against the lunar crater list.

## Concepts

- **Asteroid shower** — a temporary rise in the terrestrial-planet impact flux caused by a main-belt breakup whose fragments reach a delivery resonance, either by direct injection or by Yarkovsky drift (§1).
- **N(1)** — cumulative number of D ≥ 1 km craters per km² superposed on a large crater's floor and ejecta. Used as a relative age (§2.1).
- **C-parameter / V-shape** — the family-specific Yarkovsky isoline label defined by Eq. 1. C★ is the family border isoline, found at maximum pile-up contrast (Eq. 3).
- **Remnant Eulalia family** — the part of the family that did not escape through the J3:1 (§6.2).
- **E0** — the (e, sin I) box enclosing the Eulalia family (§3.2.2).
- **F1, F2** — the WISE sky-coverage incompleteness factor (≈2.3) and the bright-population magnitude-extension factor (≈3.02) (§5).
- **Variable (stochastic) YORP** — YORP strength re-randomised on timescale τ_YORP = τ0√D, which decouples the evolution of obliquity from that of spin rate (§3.3).
- **R_b** — Mars/Moon impactor rate per unit area per unit time, taken as 2.8 (§7.2).

## Connections

This paper extends Walsh et al. 2013 (the Eulalia/New Polana split) and Bottke et al. 2015b (both families as sources of Bennu and Ryugu; Eulalia age 830 +370/−100 Ma), using the chronology method of Vokrouhlický et al. 2006a. The shower hypothesis it tests comes from Zellner et al. 2009a (impact glasses) and Terada et al. 2020 (crater ages); the background-flux picture is Mazrouei et al. 2019a. It rules out the Flora family as the source because Vokrouhlický et al. 2017 date Flora to 1.3 ± 0.3 Ga. Its template event is the 465.8 ± 0.3 Ma L-chondrite breakup (Schmitz et al.; Liao et al. 2020), whose source family (Gefion or Massalia) it leaves open. It departs from Lagain et al. 2022 on Mars crater ages (App. A.1), arguing that automated counting is biased and that Lagain et al. were wrong to dismiss a ~300 Ma rise.

## Bearing on the record

This paper carries nothing for ML practice. It is planetary dynamics and chronology, it produces no instruction for the Anthology of the SOTA, and it neither supports nor contradicts any THEORY document. The one transferable methodological observation is generic: a pipeline of multiplied factors, where the most favourable branch is propagated and one factor (F1) is tuned by eye, gives an existence argument, not an estimate. Nothing in the anthology needs that pointed out through this paper. It belongs in the catch-all record as an astronomy reading.

## Limitations

- **The headline claims more than the body shows.** The abstract says the breakup "can plausibly account for the observed lunar craters formed near 800 Ma". The body shows that the *most favourable* of five solutions gives an average largest lunar impactor too small for Copernicus. Consistency then rests on a Monte Carlo that "generally" falls within 1σ (C10).
- **The date is inherited.** The 800 Ma in "800 Ma cluster" comes from the Copernicus calibration. The cluster itself is a cluster in N(1). If Copernicus's ray-sample age were not its formation age, every date in Fig. 2 would shift together.
- **The age spread is understated.** The text says 800–900 Ma, but the fits give 785–965 Myr, with no formal uncertainties and degenerate ρ–Γ–τ0 trade-offs (§3.3).
- **Only Solution 5 goes forward.** The collision and impact stages were run for Solution 5 alone. The paper says Solutions 1–4 were "analyzed" but reports none of their impact numbers.
- **Several inputs are hand-set.** F1 is set by visual match, the SFD is extrapolated at both ends, the Moon's impact probability is a cross-section ratio rather than a simulation, and the crater scaling law is validated only for the Moon (App. A.3).
- **§7 is speculative, by the authors' own account.** The Bitter Springs Anomaly, Snowball Earth, eukaryote diversification, Martian caldera volcanism and Venus resurfacing are all correlations or analogies, flagged "necessarily speculative". §7.1.3 cites Fig. 11 as showing that the Sturtian and Marinoan glaciations coincide with heightened flux, but Fig. 11 plots J3:1 influx, not Earth impacts. Adding the 7.5 Myr median delay does not change that much, but the figure does not show the claimed coincidence directly.
- **There are small internal inconsistencies.** §6.2 says 3 < D < 10 km loses ≈1.5×, while the Fig. 14 caption says 3 < D < 8 km, and §8 repeats 3 < D < 8. Fig. 14's caption says 870 Myr of evolution against 865 in the text. §6.3 cites "Figs. 3 and 3)". §2.2 and §8 phrase the background-flux bound differently.
- **The possible second, lower-(e, I) half of the family is out of scope.** It could raise the flux "potentially by a factor of two" (§3.2.2), so the modelled shower may be an underestimate, not only an optimistic one.

## Open questions

- Do sample ages for any of the other six ~800 Ma craters confirm their N(1)-scaled dates? That is the test that turns the shower from "putative" into observed.
- Does a CI-like projectile signature appear at Copernicus beyond Morgan et al. 1973's trace-element hints, or at other members of the cluster?
- How robust is the shower's timing if Solutions 1–4 are carried through §6? Would Solution 1 (T = 785 Myr) push the shower's end to ~600 Ma, as §6.1 suggests?
- Did Eulalia's direct injection of dust produce an L-chondrite-like micrometeorite spike near 800 Ma, detectable as extraterrestrial chromite in Tonian sediments? (This is implied by §7.1.2 but not stated as a test.)
- Does an ensemble analysis of Earth, Moon and Mars crater ages (App. A.1) make the ~300 Ma flux rise and the 800 Ma feature statistically significant?

## Corrections to the seeded skim

- The dossier says "five candidate solutions give ages of 800–900 Ma". That repeats §4's opening sentence ("estimated to be within the range of 800–900 Ma"), which the paper's own figures contradict. The best-fit ages are 785 Myr (Sol. 1, Fig. 7), 855 Myr (Sol. 2, Fig. 8), 965 Myr (Sol. 3, Fig. 9), 920 Myr (Sol. 4, Fig. 10) and 865 Myr (Sol. 5, Fig. 11). Only two of the five fall inside 800–900 Ma, and the full spread is 785–965 Myr. No formal uncertainty is given on any T; §6.1 says the ages "could be adjusted" through density or thermal parameters.
- The dossier's summary and the abstract say "Our simulations indicate that approximately three-quarters of the family's fragments eventually entered the J3:1 over a ~150-million-year interval". The three-quarters figure is first derived in §3.1 as a geometric first approximation: up to half injected directly if ejection is isotropic, plus half of the remainder drifting outward by Yarkovsky. The simulations never report the fraction itself. Table 1 gives absolute yields calibrated to the observed family, and the synthetic population is simply initialised at twice the current a < a_c population (§3.3). The timescale is not a single number either. Fig. 7 (Sol. 1) puts later influx at "≃50–150 Myr", Fig. 11 (Sol. 5) says "more than twice as many fragments drift to the J3:1 over the next ≃200 My", and §8 says "over a timescale of 150 Ma".
- The dossier's summary says the breakup "can plausibly explain the spike in large lunar craters (including Copernicus)". The paper is more guarded about Copernicus. The average largest lunar projectile is ">3 km", enough for Lowell (65.5 km), but "the formation of Copernicus crater, however, would require a larger projectile" (§6.4). Copernicus falls within the model only through Monte Carlo stochasticity (Fig. 18), and the conclusions call it "reasonably plausible".
- The dossier says Eulalia "is also named as a plausible source of Bennu and Ryugu". True, but it omits that the paper's own prior work favoured the *other* family: "New Polana was modestly favored over Eulalia as a source of Bennu and Ryugu by 70% to 30%" (§3.1, citing Bottke et al. 2015b). The Copernicus-impactor composition link rests on trace-element enrichments (Ir, Re, Sb, Se, Zn relative to Au) found by Morgan et al. 1973 in Apollo 12 KREEP. The paper calls this "compelling albeit circumstantial".
- The dossier says the background flux was "≤ half of today's (§2.2, §8)". §8 says the background production of large craters was "at least two times lower than present-day levels", which is the same thing. But §2.2's quantitative support is Mazrouei et al. 2019a's factor 2.6 (95% CI 1.7–4.7) rise at ~290 Ma, plus a qualitative reading of Fig. 2 for 650–750 Ma. The paper does not estimate the flux at 800 Ma independently.
- The dossier's §-map is otherwise accurate. One addition: an Appendix A (Mars crater ages from Lagain et al. 2022; the small-impactor flux argument; the Shoemaker crater-scaling check) carries an argument the main text depends on (A.2, below).
