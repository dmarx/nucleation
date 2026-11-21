# Reader notes: LIT-tmpsqbr9

Gutenkunst, Waterfall, Casey, Brown, Myers & Sethna (2007), "Universally Sloppy
Parameter Sensitivities in Systems Biology Models", PLoS Comput Biol 3(10):
e189, DOI 10.1371/journal.pcbi.0030189. Read 2026-11-21.

## Provenance

- **Read: the full text** through Europe PMC's documented REST interface,
  `https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2000971/fullTextXML`
  (PMCID PMC2000971, PMID 17922568; Europe PMC search lists it isOpenAccess=Y).
  HTTP 200, JATS XML, 2026-11-21. It was the first route tried, not a fallback
  (ADR-101 names this route). Everything was read: abstract, author summary,
  Introduction, Results (three subsections), Discussion, Methods, the captions
  of Figs. 1–4, supporting-information list, accession numbers, references.
- **Equations.** The PMC XML has Eqs. 1–3 and six inline formulas only as
  images. Eqs. 1–3 were read from the MathML comments in the publisher's own
  article XML,
  `https://journals.plos.org/ploscompbiol/article/file?id=10.1371/journal.pcbi.0030189&type=manuscript`
  (HTTP 200, text/xml, 2026-11-21). Inline formulas ex001–ex004 were read as
  images from
  `https://journals.plos.org/ploscompbiol/article/file?type=thumbnail&id=10.1371/journal.pcbi.0030189.ex00N`.
- **Figure 1** read as an image,
  `https://journals.plos.org/ploscompbiol/article/figure/image?size=large&id=10.1371/journal.pcbi.0030189.g001`.
- **Dataset S1** (the paper's supplementary zip: SBML, SloppyCell scripts and
  the Hessian H_χ² of each model),
  `https://journals.plos.org/ploscompbiol/article/file?type=supplementary&id=10.1371/journal.pcbi.0030189.sd001`,
  HTTP 200, 2026-11-21. Only `hessian.dat` (plain-text matrices),
  `Common.py` and `Fig1B_spectra_plot.py` were extracted and read as text;
  nothing from it was executed or unpickled. Eigenvalues were computed with
  `python3 -I` from a script kept outside the download directory. These
  numbers are the reader's computation, flagged as such below.
- **Skipped:** Texts S1–S5 (stiffest eigenvectors; other poorly determined
  parameters; fragility of other predictions; rescaled Brown model;
  Brodersen binding data). Figs. 2–4 read from captions only.
- All hosts are the publisher (PLOS, CC-BY) or Europe PMC. No bot check,
  paywall or refusal met. No email address sent anywhere.

## Copies located

| Address | Kind | Outcome |
|---|---|---|
| Europe PMC REST fullTextXML, PMC2000971 | repository API, open access | read |
| journals.plos.org manuscript XML | publisher, open access | read (equations) |
| journals.plos.org figure g001, formulas ex001–ex004 | publisher | read |
| journals.plos.org supplementary sd001 (Dataset S1) | publisher supplement | read in part |

## Summary

The authors took 17 ODE models of systems-biology processes from the
literature (mostly BioModels/SBML), 9 to 234 parameters each, and for each
computed the Hessian, in log parameters, of a least-squares measure of how
far all species' time courses move from those at the published parameters.
Every spectrum spans many decades, roughly evenly in log, with no cutoff
between important and unimportant combinations, and the eigenvectors are
skewed from the bare-parameter axes. Treating that Hessian as the Fisher
information of an idealized fit (100 data points per parameter, 10% error),
most models leave many parameters with more than 100% uncertainty. In the
48-parameter PC12 growth-factor model of Brown et al. (2004), a prediction
that a collective fit to 14 experiments constrained tightly would need all
24 relevant parameters measured to ±25% to be matched by direct measurement,
and leaving one of them known only to a factor-1000 range destroys it.
Conclusion: focus on predictions, not parameters.

## Contribution

The empirical generalization of sloppiness from one model (Brown et al.
2004) to a collection, plus the converse argument that direct parameter
measurement is an inefficient route to predictivity.

## The 17 models (Fig. 1 caption; Np from Dataset S1 Hessians)

a Tyson 1991 eukaryotic cell cycle (9); b Zwolak 2005 Xenopus egg cell cycle
(11); c Goldbeter 1991 mitosis (13); d Vilar 2002 generic circadian (15);
e Edelstein 1996 nicotinic acetylcholine receptor (17); f Kholodenko 2000
kinase cascade (21); g Lee 2003 Xenopus Wnt (22); h Leloup 1999 Drosophila
circadian (38); i Brown 2004 rat growth-factor signalling, PC12 (48);
j von Dassow 2000 Drosophila segment polarity (49); k Ueda 2001 Drosophila
circadian (49); l Locke 2005 Arabidopsis circadian (61); m Zak 2003 in-silico
regulatory network (97); n Curto 1998 human purine metabolism (105);
o Chassagnole 2002 E. coli carbon metabolism (119); p Chen 2004 budding-yeast
cell cycle (131); q Sasagawa 2005 rat growth-factor signalling (234).
Text: "they range from having about ten to more than 200 parameters. In most
cases, these parameters were not systematically fit or measured in the
original publication" (Results, first subsection).

## Key results, with place and quote

1. **Cost function (Eq. 1).** χ²(θ) = 1/(2 N_c N_s) Σ_{s,c} (1/T_c) ∫₀^{T_c}
   [(y_{s,c}(θ,t) − y_{s,c}(θ*,t))/σ_s]² dt; "a kind of continuous
   least-squares fit of parameters θ to data simulated from published
   parameters θ*". Normalization: "We took the species normalization σ_s to
   be equal to the maximum value of species s across the conditions
   considered; other consistent normalizations yield the same qualitative
   conclusions." The sum runs over all species and (where feasible) all
   conditions of the original paper, "an attempt to neutrally measure system
   behavior under conditions deemed significant by the original authors."
2. **Parametrization: log parameters (Eq. 2).** H_jk = d²χ²/d log θ_j d log θ_k;
   "We took derivatives with respect to log θ to consider relative changes in
   parameter values, because biochemical parameters can have different units
   and widely varying scales."
3. **Computation (Methods, Eq. 3).** H = (1/N_c N_s) Σ (1/T_c σ_s²) ∫ (dy/dlogθ_j)
   (dy/dlogθ_k) dt, i.e. JᵀJ; second-derivative terms "vanish because we
   evaluate H_χ² at θ*". Sensitivities by integrating sensitivity equations,
   avoiding "finite-difference derivatives, which are troublesome in sloppy
   systems." H "is the corresponding Fisher information matrix" (Parameter
   Values from Collective Fits). SloppyCell 0.81.
4. **Span (Results).** "In every case, the eigenvalues span many decades. All
   but one span more than 10⁶, indicating that the sloppiest axes ... are
   generally more than 1,000 times as long as the stiffest axes. In each
   spectrum the eigenvalues are also approximately evenly spaced in their
   logarithm; there is no well-defined cutoff between 'important' and
   'unimportant' parameter combinations." Fig. 1B is normalized by λ₁ and
   clipped at 5×10⁻⁷ ("Not all values are visible for all models"). The text
   does not say which model is the exception.
5. **The criterion: span and skew together.** "These characteristic parameter
   sensitivities that evenly span many decades and are skewed from bare
   parameter axes define a 'sloppy' model [20]." Skew is measured by I/P per
   parameter (intersection over projection of the ellipsoid on each axis,
   ∝ 1/√H_ii and √(H⁻¹)_ii): "very few axes have I/P ≈ 1". No numerical
   threshold for either.
6. **Eigenvectors.** They "often tend to involve significant components of
   many different parameters", hence "may not be useful in guiding model
   reduction"; analogy to random-matrix eigenvectors.
7. **Collective fits.** With 100×Np data points at 10% error (H scaled by
   N_d/f², σ²_logθi = (f²/N_d)(H⁻¹)_ii, Σ_i = exp(4σ) − 1): "For most of the
   models, Figure 3 indicates that such fitting leaves many parameters with
   greater than 100% uncertainty (Σ > 1)." Sloppiness "predicts that it will
   be true even for fitting to complete data that the model can fit
   perfectly."
8. **Fits vs measurement (Fig. 4).** Brown et al.'s fit: "Not a single
   parameter was constrained to better than a factor of 50", yet the ERK
   prediction is tight. Direct measurement: "all 24 involved parameters must
   be measured to within a factor of plus or minus 25%"; with one (Mek
   activation by Raf1) bounded only within a range of 1,000, "The resulting
   prediction ... would likely be useless", though every parameter is then
   tighter than after the fit. "Uncertainty for this prediction is large if
   any one of about 18 of the 24 involved parameters is unmeasured."
9. **Causes (Discussion).** "(1) ... an extraordinarily singular coordinate
   transformation ... between the bare parameters ... and the eigenparameters
   ... this parameterization is fundamental to the system, not an artifact
   of the modeling process. (2) Sloppiness depends not just upon the model,
   but also on the data it is fit to; exhaustive experiments designed to
   decouple the system and separately measure each parameter will naturally
   not yield sloppy parameter sensitivities." Rescaled Brown model (all
   concentrations and rates set to 1) "remains sloppy, with eigenvalues
   roughly uniformly spanning five decades (Text S4)".
10. **"Universal".** "the term 'universal' has a technical meaning from
    statistical physics, denoting a shared common property with a deep
    underlying cause; see [23]. Universality in this sense does not imply
    that all models must necessarily share the property." (Introduction)

## Reader's computation from Dataset S1 (not the paper's statements)

Eigenvalues of each `hessian.dat`, normalized by λ₁. Several Hessians have
small negative eigenvalues, which mark a numerical floor (relative 10⁻¹⁸ to
4×10⁻⁷); counted below are eigenvalues above that floor.

| Model | Np | resolved | decades spanned | median gap (dec) | per decade |
|---|---|---|---|---|---|
| a | 9 | 9 | 9.6 | 0.82 | 0.9 |
| b | 11 | 11 | 10.3 | 0.37 | 1.1 |
| c | 13 | 10 | 7.6 | 0.69 | 1.3 |
| d | 15 | 15 | 8.8 | 0.60 | 1.7 |
| e | 17 | 11 | 6.4 | 0.45 | 1.7 |
| f | 21 | 21 | **5.2** | 0.17 | 4.1 |
| g | 22 | 21 | **5.7** (+1 at ~10⁻¹⁸) | 0.17 | 3.7 |
| h | 38 | 38 | 10.0 | 0.21 | 3.8 |
| i | 48 | 34 | 6.5 | 0.15 | 5.2 |
| j | 49 | — | file has 957 non-finite entries; unreliable | | |
| k | 49 | 48 | 8.7 | 0.12 | 5.5 |
| l | 61 | 51 | 6.8 | 0.10 | 7.5 |
| m | 97 | 74 | 7.5 | 0.06 | 9.9 |
| n | 105 | 18 | 6.4 | 0.28 | 2.8 |
| o | 119 | 47 | 7.2 | 0.11 | 6.5 |
| p | 131 | 102 | 6.7 | 0.04 | 15.1 |
| q | 234 | 183 | 8.3 | 0.03 | 22.1 |

- The exception to "more than 10⁶" is f (Kholodenko kinase cascade, 5.2
  decades, all 21 eigenvalues positive). g resolves 5.7 decades plus one
  eigenvalue at numerical zero, so "more than 10⁶" holds for it only by
  counting that one.
- The figure's clip at 5×10⁻⁷ hides the lower tails: the small models look
  short in Fig. 1B (b visibly ends near 2.4×10⁻⁴) but span 8–10 decades in
  the data.
- "Evenly spaced" is density, not a step per rank: successive gaps have
  medians of 0.03 to 0.8 decades, and the number per decade rises with Np
  (about 1 for a–b, 15–22 for p–q), while the resolved span stays at 5–10
  decades from 9 to 234 parameters. Large models' spans are lower bounds,
  their tails sitting under the numerical floor.
- Rescaled Brown model: 23 eigenvalues over 4.4 decades (the paper says five).

## Assumptions

Local quadratic approximation at θ* (defended by Monte Carlo in Brown &
Sethna 2003 for one model); perfect, continuous, noise-free-in-mean data on
every species under every condition; σ_s = max of the species; log
parameters; model structure taken as correct.

## Concepts

Stiff/sloppy directions; the χ² Hessian as Fisher information; I/P alignment;
parameter-set ensembles; relative confidence-interval size Σ; collective fit
vs direct measurement; "universal" in the statistical-physics sense.

## Verdict on how the record characterizes it

- LIT summary ("sensitivities span many decades in a roughly geometric
  spectrum, so most parameter combinations barely affect predictions"):
  correct in gist. "Geometric" is the record's word; the paper says
  "approximately evenly spaced in their logarithm" / "span many decades
  roughly evenly".
- NOTE-tmphbpab ("seventeen systems-biology models"): correct.
- CLAIM-tmpficzj's attribution of breadth to this survey: correct; the paper
  says every model is sloppy and that collective fits give tight predictions
  with loose parameters (shown in one model, Fig. 4).
- TERM-tmptiim0 ("The literature's examples span six decades or more"):
  essentially right; the paper's count is "All but one span more than 10⁶".

## Bearing on the named codes

- **TERM-tmptiim0 — qualifies, and corrects in three places.**
  (1) *The criterion is two-part.* The paper defines a sloppy model by
  spectra that "evenly span many decades **and are skewed from bare parameter
  axes**" (Results). The TERM's definition has the spread and the no-gap
  condition (which matches "there is no well-defined cutoff") but not the
  skew. The skew is chart-relative too (bare axes in log units); the TERM may
  add it or say why it leaves it out.
  (2) *"each typically a decade or more below the last" is wrong for most of
  the collection.* By the Dataset S1 Hessians, median successive gaps are
  0.03–0.8 decades; only the smallest models (Np ≤ 13) have about one
  eigenvalue per decade. "Evenly spaced in log" in this paper means roughly
  uniform density over the log range.
  (3) *The power-law contrast.* The TERM says a sloppy spectrum "covers
  decades in proportion to the number of parameters". Across these 17 models
  (reader's computation, with the floor caveat) the resolved span stays at
  5–10 decades from 9 to 234 parameters while the density per decade grows;
  the paper itself says nothing on scaling with Np. The geometric-per-rank
  reading fits the single-model examples of the later papers, not this
  collection.
  Also: the "unread" mark and "six to eight decades" can now cite this
  paper's "All but one span more than 10⁶"; the exception is the Kholodenko
  model at about 5.2 decades (reader's computation). **Relative to a design**
  is supported verbatim (Discussion, cause 2). **Relative to a chart**: the
  paper uses log parameters and argues the bare parametrization "is
  fundamental to the system, not an artifact". It is a 2007 paper and
  predates the 2011 observation that the metric can be reparametrized to
  anything.
- **TERM-tmp5z2du (hyperribbon) — background.** The paper has no model
  manifold, no widths and no hyperribbon; its ellipsoids are in parameter
  space, widths ∝ 1/√λ (Fig. 1A). It is the empirical base only.
- **CLAIM-tmpficzj — supports consequence 1, in one model.** "The prevalence
  of sloppiness highlights the power of collective fits and suggests that
  modelers should focus on predictions rather than on parameters"
  (Abstract); Fig. 4 shows it for the ERK prediction in the PC12 model only.
  Sloppiness across the 17 is shown; tight predictions from loose parameters
  are not tested across them (Fig. 3 tests only loose parameters). On
  defeated_if's second clause, the paper answers with the bare parameters
  being "fundamental to the system", not with invariance. It also supports
  "relative to the observables fitted" (cause 2). Rescaling all rates and
  concentrations to 1 leaves the model sloppy (five decades), which is
  against the spread being merely an artefact of scales.
- **NOTE-tmpamhd2 (2010 letter) — parallel.** The letter cites this paper
  for ubiquity; what it is cited for holds.
- **NOTE-tmphbpab (2015 review) — parallel; corroborated.** The review's
  "seventeen" and its use as the empirical base are accurate. The review's
  practical cut (eigenvalues below 1 in units of measurement error) has an
  antecedent here in the scaling of H by N_d/f² (Methods) but no cut is
  stated.

## Limitations

The data are simulated from the published parameters, with every species
observed continuously, so the spectra are of an idealized design, not of
the experiments the models were fitted to. Local (Hessian) analysis only.
No threshold for "many decades" or "evenly"; "evenly" is judged by eye from
Fig. 1B. The fit/measurement comparison is one prediction in one model (with
others in Text S3, unread). The figure's clipping at 5×10⁻⁷ hides tails, and
the provided Hessians have numerical floors near 10⁻⁷ in several models.

## Candidate THEORY

"In seventeen ODE models from the systems-biology literature, with 9 to 234
parameters, the eigenvalues of the Hessian of a species-normalized
least-squares deviation of all time courses, taken in log parameters at the
published values, span many decades (all but one more than 10⁶), roughly
evenly in log with no cutoff between important and unimportant combinations,
along eigenvectors skewed from the bare-parameter axes; and in one of them,
a 48-parameter signalling model, a collective fit to 14 experiments
constrains a prediction that direct parameter measurement would match only
if every one of 24 relevant parameters were measured to about ±25%."

promote_when: the 17 spectra and the PC12 comparison are confirmed from the
paper's Fig. 1B, Fig. 4 and Dataset S1, and the description of the cost
function and parametrization from Eqs. 1–2 (done in this reading); a filer
checks the quotes against the PMC text.

## Recheck (search of record/ after reading)

Searched: Gutenkunst, Waterfall, Vandermonde, SloppyCell, PC12, Brown and
Sethna, collective fit, BioModels/SBML, Brodersen, skewed/bare parameter,
evenly spaced, parameter uncertainty, systems biology, random matrix,
experimental design, universality class.

- **NOTE-1018** (Machta, Chachra, Transtrum & Sethna, "Parameter space
  compression", LIT-1299) names "Gutenkunst et al. 2007" in Connections
  without the code. Background; it could cite LIT-tmpsqbr9. Missed by the
  first search, which looked only at the named codes.
- **Waterfall et al. 2006**, "Sloppy-model universality class and the
  Vandermonde matrix" (PRL 97:150601), the paper's ref. [23] for the
  technical sense of "universal" and for the cause "redundancy between the
  effects of different parameter combinations", is named in NOTE-1018 but
  not held as a LIT. Candidate for registration.
- **Brown & Sethna 2003** (PRE 68:021904), ref. [20], the source of the
  word "sloppy" and of the two-part definition, and **Brown et al. 2004**
  (Phys Biol 1:184), ref. [21], the PC12 model: neither is held.
- **PC12** hits (THEORY-tmpkoje5, THEORY-tmpgsgka, NOTE-tmpzxtnv,
  ARG-tmpj0r42, CLAIM-tmpcg4uu) refer to the same Brown et al. model as
  studied in the 2010/2011 geometry papers. Parallel.
- No entry other than those named holds the Fig. 4 result (precise and
  complete measurement) or the I/P skew criterion. "Brodersen" hits are a
  different Brodersen (THEORY-1362, LIT-2015). "Collective fit" hits are
  about collective fitness (NOTE-064, THEORY-607). Irrelevant.

## Neighbours

None needed; the work itself was read.
