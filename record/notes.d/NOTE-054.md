---
number: 54
status: Read
formerly:
- NOTE-tmpgajrb
paper: LIT-080
title: 'Brain states across spacetime via whole-brain models'
version: 2
history:
- version: 2
  date: '2026-09-25'
  note: >-
    Read in full (full text of the open-access (CC BY) review, from the
    Europe PMC full-text XML of PMC9125224 (rawC4/c68.xml → c68.txt; the PMC
    HTML page was also saved, as c68.html). I read the abstract and
    keywords, §1–7 (Introduction; Insights from neuroimaging; Insights from
    whole-brain modelling; Spacetime of psychedelic and depressive brain
    states; Theoretical descriptions; Empirical findings (a)–(c);
    Conclusion), all six figure captions, the declarations and references
    1–102. The figures themselves are adapted panels from cited studies and
    carry no new data. I did not compare against the Royal Society typeset
    version (403 at seeding).). Upgraded from `Skimmed` to `Read`: the
    claims table, assumptions and results are new, and the skim is corrected
    where the full text disagreed.
date: '2026-09-25'
summary: >-
  This is a narrative review with no new data, model or quantitative
  synthesis. It argues that healthy waking brain dynamics sit in a
  metastable regime near criticality, which whole-brain models
  (connectome-coupled Hopf oscillators, weakly coupled, at the edge of
  instability) reproduce. On its "activity landscape" picture, depression
  deepens particular attractors and psychedelics flatten the landscape.
  The depression side rests on three cited fMRI studies, one of them in
  remitted patients, and the review itself says "further studies will be
  required".
---

# NOTE-054: Brain states across spacetime via whole-brain models

## Contribution

The review assembles three strands into one framing: dynamic functional connectivity and connectome harmonics (§2), whole-brain computational models (§3), and theoretical accounts of psychedelic and depressive states, the entropic brain and REBUS (§5). The framing is that brain states are characterized by spatio-temporal dynamics on a landscape of weakly coupled substates constrained by the structural connectome (§6c, Fig. 6). It proposes that causal whole-brain models, enriched with receptor maps and other regional heterogeneity, be used to find perturbations that move between states. The review adds no data or model of its own.

## Key insight

A brain state is best described by *how it moves*: its fractional occupancy, dwell time and transition probabilities among substates. That is a better description than static connectivity. Health is a metastable balance: stable enough to visit substates meaningfully, flexible enough not to get trapped. Depression and psychedelics are placed at opposite ends, as over-deep attractors versus a flattened landscape (Fig. 6, Conclusion).

## Assumptions

These are premises of the argument:
- The brain operates near criticality, where dynamic range and information capacity are maximal and metastability is hypothesised maximal (§1). The support is power-law observations across scales, cited, not re-examined.
- Brain structure (the diffusion-MRI connectome) "constrains the space on which dynamics emerge" (§2). The slowest graph-Laplacian eigenmodes reproduce resting-state networks [47].
- Whole-brain models are validated by fit to empirical FC and FCD. The best fits need small-world topology balancing modularity and efficiency [61], weak coupling [55], and local nonlinear (supercritical Hopf) nodes at the edge of instability with noise [57, 68, 70] (§3).
- Structured noise plus structural connectivity explains static FC but not non-stationary FCD [66, 67]. This is the stated reason for the nonlinear local dynamics.
- Resting-state networks are "weakly emergent" from neuronal activity (§1).

## Key results

These are what the review reports from the literature. None are its own findings.
- **Perturbation.** TMS evokes a distributed, differentiated response when awake and a local stereotyped one in deep sleep [18, 19]. Perturbational complexity separates vegetative, minimally conscious and anaesthetised states [20] (§1).
- **Psychedelics, spatial (§6a).**
  - Broader connectome-harmonic repertoire under LSD and psilocybin [46, 49]. Enhanced repertoire of dynamic-connectivity substates under psilocybin [84].
  - Decreased mPFC–PCC connectivity [75]. Increased between-network connectivity [86]. LSD increases global FC density in DMN/salience/FPN [81] and decreases within-DMN connectivity [78].
  - The review's summary: "within-network disintegration coupled with increased between-network cohesion".
- **Psychedelics, temporal (§6a).**
  - Increased MEG signal diversity (LZ) under LSD, psilocybin and ketamine [82].
  - Ayahuasca reduces alpha and raises gamma [89]. DMT reduces alpha and beta [80].
  - Broadband MEG power decrease under LSD and psilocybin [78, 90].
  - The review reads this as "inhibition of long-range synchronization".
- **Depression (§6b).**
  - Remitted-MDD patients show less recruitment and shorter duration of a frontoparietal/default-mode/salience/striatum network and more time in a global pattern. Sad-mood induction raises global-pattern occupancy in both groups [93].
  - More within-DMN connectivity, and more global synchrony and temporal stability, in MDD [94, 95].
- **Transitions.** Whole-brain models have been used to predict which regions to stimulate to force wake ↔ deep-sleep transitions [70]. 5-HT2A receptor maps in a whole-brain model account for LSD effects [100, 101] (§6c).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Healthy waking dynamics are metastable, near criticality | informal argument (cited) | §1, citing power-law and criticality literature. Not evaluated against critiques |
| C2 | Whole-brain models fit empirical FC/FCD best with small-world topology, weak coupling and nodes at the edge of a Hopf bifurcation | moderate (cited modelling studies) | §3 [55, 57, 61, 68, 70]. Several are the authors' own |
| C3 | Psychedelics broaden the repertoire of brain substates and raise signal diversity | moderate (cited, small-sample studies) | §6a [46, 49, 82, 84]. Sample sizes not reported by the review |
| C4 | Depression is "characterized by excessively rigid, highly ordered states" (abstract) | weak | Three studies in §6b, one in remitted patients. The review itself calls for further studies |
| C5 | Depressed and psychedelic states lie at "opposite sides of a spectrum" of spatio-temporal dynamics | assertion / hypothesis | Conclusion and Fig. 6, adapted from [49]. No study measures both on a common scale |
| C6 | Causal whole-brain models with receptor and heterogeneity data can find perturbations that rebalance brain states and "inspire new treatments" | informal argument (programmatic) | §6c, citing [70, 99–101] |

## Concepts

- **Brain state.** A regime of whole-brain activity distinguished by its spatio-temporal dynamics and its response to perturbation (§1).
- **FCD (functional connectivity dynamics).** Time-varying FC summarised as a repertoire of substates, with fractional occupancy, dwell time and transition probability (§2, Fig. 2a).
- **Connectome harmonics.** Eigenvectors of the structural connectome's graph Laplacian, used as a basis for activity patterns (§2, Fig. 2b).
- **Metastability.** Dynamical flexibility, with transient visits to substates without locking into any (§1). The review gives no formal measure.
- **Whole-brain model.** Coupled differential equations per region (neural mass, Kuramoto or Hopf), wired by the structural connectome and fitted to empirical FC/FCD (§3).
- **Activity landscape.** An n-dimensional terrain of weakly coupled substates (basins of attraction) through which brain activity moves (§6c, Fig. 6).
- **Entropic brain / REBUS.** Brain-state entropy indexes the richness of states. Psychedelics relax the precision of high-level priors (§5; [72–74]).

## Connections

This is a programme review from the Deco/Kringelbach/Cabral group. Most modelling citations are the authors' own [53, 57, 59, 61, 70, 96, 99–101], and the theory is Carhart-Harris's [72–74]. In this record, [LIT-066](../literature.d/LIT-066.md) documents meditation-induced changes in sense of self and perception; the REBUS and entropic-brain framing here is the natural neural counterpart for such altered states, though neither paper cites the other (my link). [LIT-056](../literature.d/LIT-056.md), on consciousness science applied to AI, shares the perturbational-complexity and criticality vocabulary but is not cited.

## Bearing on the record

- It is useful as an entry point to whole-brain modelling, connectome harmonics and FCD, and as the source of the "landscape flattening" metaphor for psychedelics.
- Do not cite it as evidence that depression *is* rigid or ordered dynamics. Cite the primary studies [93–95], after checking them.
- Nothing here bears on ML practice. The "edge of instability" and criticality language has ML echoes (edge-of-chaos initialisation), but the review makes no such connection. No ANTH- document is implicated.

## Limitations

- A narrative review. There are no inclusion criteria, no effect sizes or sample sizes, and no discussion of replication or of criticisms of brain criticality and dynamic-FC methods (for example, sampling variability of sliding-window FC).
- It is heavily self-citing in the modelling section, and alternative accounts are not weighed.
- The abstract states the depression characterization more strongly than §6b supports (C4).
- The landscape picture (Fig. 6) is illustrative, adapted from [49]. No landscape is estimated from data.
- There are editorial errors: figure-panel cross-references in §6a, swapped DOIs for refs 59/60, and "flocks of startles".

## Open questions

- Can one estimated landscape (for example, an energy landscape [97, 98] or model-derived attractors) place healthy, depressed and psychedelic data on a common axis, so that the "opposite ends" claim is tested rather than drawn?
- Do the psychedelic "repertoire broadening" and depression "rigidity" findings replicate in larger, pre-registered samples?
- Can receptor-informed whole-brain models [100, 101] predict an intervention's effect out of sample? That is the step the "new treatments" claim needs.

## Corrections to the seeded skim

- **The dossier puts the depression evidence too strongly.** The one study it paraphrases ("reduced visits to a frontoparietal/default-mode/salience state") is Figueroa et al. 2019 [93] in *vulnerable remitted*-MDD patients, not currently depressed ones. That network also included the striatum. The only other depression evidence is Demirtas 2016 [94] and Kaiser 2016 [95], and the review closes §6b with "further studies will be required to further investigate FCD in the depressive state". Yet the abstract says flatly that "depression is characterized by excessively rigid, highly ordered states".
- **The dossier's §5 heading "Theory" misses that the depression claim there is also theoretical.** The entropic-brain hypothesis *posits* diminished entropy in depression (§5), and the review offers the DMN/FPN "coming to control most of cognition" as "one possibility".
- **Figure cross-references in §6a are mislabelled.** The text cites "figure 4c" for connectome-harmonic repertoire broadening and "figure 4b" for signal complexity. The caption has these the other way round: (b) repertoire, (c) LZ complexity. References [59] and [60] also carry each other's DOIs.
- **§4 is one paragraph stating a hypothesis.** That the psychedelic and depressive states "can be approached from a theoretical perspective combining" neuroimaging and whole-brain models is proposed there, and nothing later tests it.
