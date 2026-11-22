# Reader notes: martinez2024 (LIT-2965)

Martínez-Sánchez, Arranz & Lozano-Durán (2024), "Decomposing causality into
its synergistic, unique, and redundant components", arXiv:2405.12411;
Nat Commun 15, 9296 (2024), doi:10.1038/s41467-024-53373-4.

## Step 1: copies located (2026-11-22)

- https://arxiv.org/pdf/2405.12411 — arXiv preprint (latest version, updated
  2024-08-21 per the arXiv API), PDF, 30 MB. Fetched 2026-11-22, HTTP 200,
  no obstacle. Lawful (arXiv, step 5 first route).
- arXiv API (https://export.arxiv.org/api/query?id_list=2405.12411) gives
  journal_ref "Nat Commun 15, 9296 (2024)" and doi 10.1038/s41467-024-53373-4.
  No email sent.

## Step 2: read (2026-11-22)

Read the arXiv v3 PDF (58 pp.: main text 21 pp., Supplementary Materials
after it), via pdftotext. Read in full: main text (Introduction, Results,
Discussion, Methods incl. "Assumptions for causal discovery", the SURD
definition, the turbulence data descriptions, transport maps); SI §S1
(formulation, the nine-step definition, properties), §S5 (non-separability),
§S6 (predictive modelling). Skimmed only: SI §S2 (descriptions of CGC, CCM,
PCMCI, CTE), §S3 (further validation cases), §S4 (sensitivity), figures
(bar values not legible in text extraction). Not read against the Nat Commun
version of record; page numbers below are arXiv v3's.

## Report

### Provenance
- Read: https://arxiv.org/pdf/2405.12411 (arXiv v3, 21 Aug 2024; PDF;
  fetched 2026-11-22, no obstacle). Version of record: Nat Commun 15, 9296
  (2024), doi:10.1038/s41467-024-53373-4, not fetched (not needed; arXiv
  copy read). Coverage as in Step 2. No other work was read or quoted.
- Copies located: the arXiv PDF above (arXiv, lawful, read). No others
  sought, since a lawful full text was read.

### Summary
SURD (Synergistic-Unique-Redundant Decomposition) is an observational,
information-theoretic measure of "causality" among time series. The entropy
of a target's future, H(Q_j⁺), is split into redundant, unique and
synergistic parts of I(Q_j⁺; Q), plus a "causality leak" H(Q_j⁺ | Q) for
what the observed variables do not account for. The split is made per state
of the target, using specific mutual information, and then averaged. It is
benchmarked against conditional Granger causality, conditional transfer
entropy, convergent cross-mapping and PCMCI on toy systems (mediator,
confounder, synergistic and redundant colliders and others). It is then
applied to two turbulent flows: the interscale energy flux in a DNS of
isotropic turbulence, and inner/outer-layer velocities in a boundary-layer
experiment.

### Contribution
A partial-information-style decomposition of the predictive information
about a target's future. It has 2^N-ish terms, all nonnegative, and they add
up exactly (Eq. 1), with a bounded leak term. The authors present it as
handling redundancy, synergy, self-causation and unobserved drivers together,
which no single earlier method does.

### Key results (arXiv v3)
1. Decomposition, p.3, Eq. (1): H(Q⁺_j) = Σ ΔI^R + Σ ΔI^U + Σ ΔI^S +
   ΔI_leak→j, where the leak "is the causality from unobserved variables,
   referred to as the causality leak". Properties, p.4: the terms "are
   non-negative and such that the sum of redundant, unique, and synergistic
   causalities equals the information shared between Q⁺_j and Q", and
   I(Q⁺_j; Q_i) is the sum of the unique and redundant terms involving Q_i.
2. Construction, Methods p.13 and SI §S1.2 steps 1–8. For each target state
   the specific informations ĩ of every subset are sorted in ascending order.
   The redundancy among a set is the increment shared by all of its
   singletons, the unique term is the top singleton's excess over the next,
   and synergy is a higher-order ĩ's excess over max{G̃^{M−1}}. All are then
   averaged over p(q⁺_j). SI §S1.2: "one of the most referenced
   decompositions by Williams & Beer [114] results in a number of terms that
   grows as the Dedekind numbers. In the case of 9 variables, this
   decomposition yields over 10[^]23 terms, whereas SURD produces only 512
   terms." (The text extraction gives "1023". It is presumably 10^23, which
   would understate the Dedekind count; the filer should check the figure
   against the PDF or the version of record before quoting it.)
3. Invariance, SI §S1.4: "The redundant, unique, and synergistic causalities
   are invariant under invertible transformations of Q. This property follows
   from the invariance of the mutual information."
4. Energy cascade, pp.8–9, Fig. 6. The data are a 1024³ DNS of forced
   isotropic turbulence, Gaussian-filtered at Δ̄ = 163η, 81η, 42η and 21η
   (all in the inertial range). The variables are "the time signals of the
   volume-averaged energy transfer, denoted by Σi" (Σ̃ = τ_ij S̄_ij, p.14).
   Results: "The dominant contributions come from redundant and unique
   causalities, whereas synergistic causalities play a minor role. The unique
   causalities … vividly capture the forward energy cascade of causality from
   large to smaller scales, inferred from the non-zero terms ΔI^U_1→2,
   ΔI^U_2→3, and ΔI^U_3→4. Curiously, no unique causality is observed from
   smaller to larger scales, and any causality from the backward cascade
   arises solely through redundant relationships." The reading given: "no new
   information is conveyed from the smaller scales to the larger scales". It
   "justifies the success of subgrid-scale modeling in large-eddy simulation",
   and supports Taylor's dissipation surrogate and the dissipation anomaly.
5. Leak in the cascade, p.9: "The largest causality leak occurs for Σ2, where
   approximately 47% of the causality is carried by variables not included
   within [Σ1, Σ2, Σ3, Σ4]". Σ1 has the "smallest leak of 14%", because of a
   high self-unique term: "the future of the largest scales is mostly
   determined by its own past."
6. Comparison, p.9: "CGC and CCM do not support the hypothesis of a forward
   energy cascade … CTE and PCMCI are consistent with the forward propagation
   of energy, but the strength of the causal links detected is extremely
   weak."
7. Boundary layer, p.10, Fig. 7. Melbourne wind tunnel, Re_τ = 14,750, two
   hot-wire signals. "The results distinctly support the prevalence of
   top-down interactions" (outer to inner, consistent with Townsend's
   outer-layer similarity). But "The causality leak … is 99% for both uI and
   uO."
8. Lag choice, p.15: for each target Σ_j, the lag ΔT_j "was determined as the
   time required for maximum ΔI^U_i→j with j ≠ i". In the boundary layer,
   ΔT* ≈ 756 is "the time lag for maximum cross-induced unique causality".
9. Non-separability, SI §S5: SURD keeps the Q1↔Q2 coupling in Sugihara's
   logistic system when lags are added, where nonlinear CGC loses it. Lags
   raise the redundant terms instead.

### Assumptions (p.12, "Assumptions for causal discovery")
- Causality is read as information: the "forward-in-time propagation of
  information", with transitional probabilities between states.
- "The method also assumes that the time signals are stationary".
- The leak "alleviates the need for the assumption of causal sufficiency".
- Probabilities are estimated by binning (50–100 bins per variable) or by
  transport maps (sixth-order polynomials). Results depend on the partition
  (SI §S4).
- Success in Table 1 is judged by whether results "are consistent with the
  functional dependencies of the system, rather than on the concrete value
  of the causal strength" (p.4).

### Concepts
Redundant, unique and synergistic causality. Causality leak. Specific mutual
information (ref. 124). Forward propagation of information. Interscale
energy flux Σ̃ = τ_ij S̄_ij. Forward and backward cascade. Transport maps.
The Williams–Beer lattice, as the rival decomposition.

### Verdict on the exchange's characterization
CLAIM-810 ("What it does not say") and LIT-2965 attribute to it "a 2024
study decomposing [turbulence's interscale causation] into unique, shared
and synergistic parts", with the decomposition "applied to energy transfer
between scales in turbulence". This is accurate. "Shared" is the paper's
"redundant". The LIT summary is also accurate. What the exchange did not
carry: the measure is computed on four volume-averaged scalar flux signals,
not on fields; the finding is forward unique causality with backward
influence only redundant; and Σ2's leak is 47%.

### Bearing on codes
- **CLAIM-810: qualifies, and supports in part.**
  - Supports: the paper keeps transfer and dependence apart in its own
    construction. The energy transfer Σ̃ is a physical flux, defined
    dynamically (p.14). SURD then measures the predictive information among
    the time series of those fluxes (p.3). These are two different objects:
    a measure of the second, not a measure of the first.
  - Bears on CLAIM-810's remark that A23 §6's transfer entropy needs the
    decomposition into scales fixed. The paper fixes it, with Gaussian
    filters at four widths and volume averaging, so it is an instance of
    what the claim asks for.
  - Qualifies the line "That turbulence's interscale causation is settled":
    the paper's result is directed, forward and mostly unique and redundant.
    That fits the claim's turbulence row (all three properties present). It
    does not test the separations the claim argues for.
  - The invariance under invertible maps (result 3) means SURD has no
    reflection blindness when it is applied to the flux signals. The sign of
    the flux is in the variable, unlike THEORY-748's block entropies on the
    velocity.
- **CLAIM-335 (recheck hit): supports, parallel.** CLAIM-335 says transfer
  entropy is unique information plus synergy with the target's past, and is
  predictive, not flow. The paper's "causality" is likewise predictive
  information about Q_j⁺ (p.12: "causal relationships emerge as a result of
  transitional probabilities between states"). It also notes that
  multivariate CTE can be negative (p.11). Its language of "causality",
  information "flow" and "energy cascade of causality" is the slide
  CLAIM-335 warns against.
- **CLAIM-343 (recheck hit): leaves open, contrast.** CLAIM-343 says that on
  the Williams–Beer lattice, from three sources up, the identity axiom and
  nonnegative atoms are inconsistent. SURD gets nonnegativity by not using
  the lattice, with fewer terms (result 2). Its redundancy, taken per target
  state from the sorted singleton specific informations, has the shape of
  Williams–Beer's I_min. That is the reader's reading of SI step 3; the paper
  does not name I_min or discuss the identity axiom. If the reading holds,
  SURD drops the identity axiom, which is CLAIM-343's "name the axiom" point.
  The paper does not state which axiom it gives up.
- **LIT-1172 (Williams & Beer, "Nonnegative Decomposition of Multivariate
  Information"; recheck hit): background.** The paper cites it as ref. 114
  and names it the main rival decomposition (SI §S1.2).
- **SYNTHESIS-073, TERM-057, TERM-058 (recheck hits): background and
  support.** These hold Granger causality and transfer entropy as predictive
  quantities relative to an information set. SURD belongs to the same
  family, with the leak as an explicit measure of what the information set
  lacks. The leak does not supply an interventional reading.
- **CLAIM-407 (recheck hit): contrast.** CLAIM-407 says informational closure
  need not preserve responses to an intervention. SURD is purely
  observational (p.12), and its leak and its redundancy cannot speak to
  interventional responses.
- **THEORY-748 (grounds CLAIM-810): parallel.** See the invariance point
  above.
- **THEORY-747 and THEORY-754 (subgrid and large-eddy, cascade flux):
  background.** The paper claims that its forward-only unique causality
  "justifies the success of subgrid-scale modeling". That is a claim the
  record could set against THEORY-747's memory closures.
- **CLAIM-846, CLAIM-850, TERM-142, SYNTHESIS-119:** no direct bearing. The
  paper says nothing about scale invariance or power laws.

### Limitations
- The cascade finding rests on four volume-averaged scalars from one DNS
  (165 T_ε at Δt = 0.0076 T_ε, about 2×10⁴ snapshots by the reader's
  arithmetic). Spatial structure and local backscatter are averaged out. A
  backward cascade that is local and cancels in the volume average cannot
  show up.
- Each lag is chosen to maximize cross unique causality (result 8). That is a
  selection which favours finding cross-scale unique terms.
- The leaks are 47% for Σ2 and 99% in the boundary layer. The authors' own
  discussion (p.11) says a link "would still be deemed insignificant if the
  causality leak … is 99%". They nonetheless call the boundary-layer result
  distinct.
- "Causality" is predictive information under stationarity, with no
  interventions. Success is judged by agreement with known dependencies or
  the field's consensus, not by strength.
- The decomposition is one of many. Its redundancy definition is not
  defended axiomatically: it is "motivated by their consistency with the
  properties presented … along with the ease of interpretability" (SI §S1.2).
- Results depend on the estimator: bins or transport maps (SI §S4).

### Candidate THEORY sentence
"Decomposing the predictive information that the volume-averaged interscale
energy fluxes at four inertial-range filter widths carry about each other's
futures (SURD), in a DNS of forced isotropic turbulence, gives nonzero
unique terms only from larger to the next smaller scale (Σ1→Σ2→Σ3→Σ4). Any
small-to-large dependence is redundant, and synergy is minor;
Martínez-Sánchez, Arranz and Lozano-Durán read this as directed causality of
the forward cascade."
promote_when: an independent analysis of a different turbulence dataset, or
of local rather than volume-averaged fluxes, with a lag not chosen to
maximize cross unique terms, finds the same pattern: forward unique terms
and no small-to-large unique term. Or a second decomposition (a different
redundancy function) applied to the same signals does.

## Step 3: recheck (2026-11-22)
Searched record/ (excluding notes.d) for: Williams–Beer / partial
information decomposition / PID, transfer entropy, Granger, convergent cross
mapping / Sugihara, PCMCI / Runge, Lozano, energy cascade / backward cascade
/ backscatter, information flow / Liang, causality leak / causal
sufficiency, synergy, O-information / Rosas, large-eddy / subgrid, Townsend
/ boundary layer, Takens, I_min / identity axiom / specific information.
Entries the first search missed: CLAIM-335, CLAIM-343, LIT-1172,
SYNTHESIS-073, TERM-057, TERM-058, CLAIM-407, THEORY-747, THEORY-754 (all
above). LIT-1162 ("Quantifying unique information") and LIT-042 ("Shannon
invariants") are rival decompositions, background only. Not held: no LIT
for SURD's code or for the Melbourne boundary-layer data. No "Takens" hit.
