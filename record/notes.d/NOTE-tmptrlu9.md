---
status: Read
paper: LIT-tmpm09g4
title: 'Signaling cascades and the importance of moonlight in coral broadcast mass spawning'
version: 1
history:
- version: 1
  date: '2026-10-04'
  note: >-
    Read in full from PMC4721961 (Europe PMC JATS XML, CC BY 4.0): every
    section, all of Materials and methods, all figure and figure-supplement
    captions, the decision letter and author response. Figure images,
    Supplementary files 1–3 and the Dryad and SRA data were not viewed.
    Numbers below are the text's and the captions'.
date: '2026-10-04'
summary: >-
  Two experiments at Heron Island on Acropora millepora. In 2011, colonies
  under ambient night light (N = 6) spawned with the reef, while colonies
  lit after sunset (N = 5) or kept dark (N = 5) did not spawn that night.
  184 transcripts selected by variance changed around gamete release only
  in ambient colonies. In 2006, 90 colonies under blue, green or white
  nocturnal light spawned 6–8 h or two nights late, and under red light on
  time. The GPCR and melanopsin cascade is a model built from correlated
  expression.
---
<!-- inactive-ok-file: THEORY-tmpezkoq THEORY-126 THEORY-069 — Proposed; the theory filed from this reading, and the record's account of collective emotion as synchrony from a shared cause, and the coupled-oscillator account, named for a parallel and a contrast with no relation claimed -->

# NOTE-tmptrlu9: Signaling cascades and the importance of moonlight in coral broadcast mass spawning

## Contribution

The first transcriptome time course across a coral's spawning night,
combined with light manipulations that stop or shift spawning. Before it,
moonlight was known from field correlation and older manipulations (Babcock
et al. 1986; Willis et al. 1985) to time mass spawning, but the molecular
events of the night were not described. It adds three things: a set of
genes whose expression changes only on the spawning night, evidence that
added light or darkness at night abolishes both that programme's normal
timing and the spawning, and a proposed GPCR signalling model for gamete
release.

## Key insight

The cue does not only set a date. On the night itself, light conditions
after sunset decide whether and when a mature colony releases gametes, and
a week of altered nights is enough to break it. The transcript programme
that accompanies release starts early under light and does not start under
darkness. So the timing runs through a light-sensitive process on the
night itself, not only through an entrainment set months before. The
authors contrast this with Willis et al. 1985, which suggested months.

## Assumptions

- **Species and site.** One species, Acropora millepora, from the Heron
  Island reef flat (23°33′S, 151°54′E), at the Heron Island Research
  Station, kept dark at night against stray light.
- **Maturity.** Colonies were checked for pink eggs before use.
- **Tank conditions stand in for the reef.** Outdoor flow-through tanks
  with reef-flat water and natural sun and moon. Ambient colonies spawned
  when the reef did, which the authors take as validation.
- **Transcript selection by variance.** The 184 "spawning" genes are those
  in the top 10% of Poisson-normalised variance on the spawning day and not
  in the top quartile on earlier days or in the August full and new moon
  samples, with more than 100 reads in some condition. Other cut-offs
  (top 5–25% versus not top 25–50%) "produced similar results". The
  up-regulated and down-regulated sets require a twofold difference against
  both the previous days and the August samples.
- **Library design.** 12 libraries (full and new moon, August) on one lane,
  each sequenced twice as technical duplicates. 24 libraries from the
  spawning experiment on two lanes. The paper does not say how 16
  colonies, three treatments and up to seven time points map onto 24
  libraries, so biological replication per time point is not stated.

## Key results

- **2011 manipulation (Figure 2A, Methods).** Twenty colonies were collected
  on 9 November 2011. Four were left on the reef flat (treatment F, not
  analysed further in the text), and 16 went to tanks: ambient (A, N = 6),
  light (L, N = 5, about 5 µmol quanta m⁻² s⁻¹ PAR from 18:15 to 24:00,
  then dark) and dark (D, N = 5, shaded 18:15 to sunrise). Sampling was at
  noon and at moonrise on 10, 12, 14 and 15 November. On the spawning night
  of 16 November, samples were taken at noon, 18:15, 19:30, 21:00, 22:00,
  22:30 and 00:20. Ambient colonies began "setting" at 19:30 and released
  gametes between 21:30 and 22:30. "No sign of spawning behavior occurred
  in either the light or dark treatments." Whether L and D colonies spawned
  on later nights is not reported.
- **Spawning-day genes (Figures 1C, 2B).** 184 transcripts. In A they
  changed (mostly induced) just before and at release. In D they did not
  change. In L they changed early, around 18:15 and 19:30. GO enrichment
  (FDR < 0.1): cell cycle, GTPase activity, signal transduction.
- **Up and down sets (Figure 2—figure supplement 1, Figure 3B–C).** 177
  up-regulated (54 also in the 184) and 29 down-regulated (none in the 184).
  Up: G-protein-coupled processes, signal transduction, respiration. Down:
  rhythmic processes including circadian clock-related genes. Induced genes
  include two opn4b (melanopsin)-like homologs, many GPCRs, a synaptotagmin
  7 homolog and a Trp-related protein 4. Expression did not correlate with
  the released gametes' own transcriptome (mean Pearson r 0.22, and 0.05
  for the spawning-day genes), so the signal is from the colony tissue, not
  from gametes.
- **qPCR check (Figure 2—figure supplement 2).** Twelve genes, ambient
  colonies at 22:00 against 19:30: r² = 0.92 with RNA-seq log₂ fold
  change, p < 0.0001.
- **Lunar transcription (Figure 1—figure supplement 1).** August, N = 4
  colonies at 2 m depth, at 12:00, 18:00 and 24:00 on new and full moon
  days. Differences between full and new moon were tested against Poisson
  noise with a Bonferroni correction. Genes higher at full-moon midnight
  include cry1, cry2 and thyrotroph embryonic factor.
- **2006 light-quality experiment (Figure 2—figure supplement 3).** 90
  colonies in tanks shaded by day to simulate 3 m depth, unshaded at night.
  For six hours after sunset (18:00–24:00) they received high (100), medium
  (50) or low-dim (0.75–1 µmol quanta m⁻² s⁻¹) white light, or blue, green
  or red light at 1 µmol quanta m⁻² s⁻¹, from 31 October to 15 November
  2006. Full moon was 5 November. The reef and the controls spawned on 13
  November, eight nights after full moon. Red and ambient colonies spawned
  at 21:30. Blue, green and all white intensities delayed spawning 6–8 h or
  to two nights later. One-way ANOVA with Tamhane post hoc, p < 0.01, for
  the phase shift.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Altering nocturnal light for the week before spawning (added light after sunset, or darkness) prevents A. millepora colonies from spawning on the spawning night | moderate: clear all-or-none outcome, but N = 5–6 per arm, one night, one site, later nights not reported | Results; Methods (2011) |
| C2 | Blue, green and white nocturnal light delay spawning by hours or nights, and red light does not | moderate: 90 colonies, but the result is shown in a supplementary figure, with treatment numbers that do not add up as written (see Limitations) | Figure 2—figure supplement 3 |
| C3 | A set of transcripts changes only on the spawning night, around gamete release, and its timing follows the light treatment | moderate as description; selection by variance ranking, replication per time point unstated | Figures 1C, 2B |
| C4 | Spawning-night up-regulated genes are enriched for GPCR signalling and include melanopsin-like homologs | moderate (GO enrichment, qPCR-validated fold changes for 12 genes) | Figure 3; Figure 2—figure supplement 2 |
| C5 | Gamete release is triggered by a melanopsin-like photoreceptor and/or neuropeptides acting through GPCR cascades | weak: a model from co-expression; the authors say the photopigment role is not shown | Figure 4; Discussion |
| C6 | Coral transcription varies with lunar phase, including cryptochromes | weak to moderate: N = 4, apparently one library per condition with technical duplicates | Figure 1—figure supplement 1 |
| C7 | Disruption by altered night light takes effect within 7 days, faster than the months of entrainment earlier work proposed | moderate, from C1 and C2 | Discussion; author response |

## Concepts

- **mass spawning** — the annual release of gametes by many coral species
  over a few nights, a few days after a full moon in the spawning season on
  the Great Barrier Reef (November in both experiments here).
- **setting** — gamete bundles appearing in the polyp mouths before
  release.
- **light pollution** — here, artificial PAR light after sunset.
- **phase shift (of spawning)** — the delay, in hours or nights, relative
  to ambient colonies. Unrelated to the ecological "phase shift" of
  [LIT-tmpr2ulq](../literature.d/LIT-tmpr2ulq.md).

## Connections

- **Hughes et al. ([LIT-tmpr2ulq](../literature.d/LIT-tmpr2ulq.md))** share an author (Hoegh-Guldberg) and the
  Great Barrier Reef. This paper says reproduction is "one of the most
  important processes for the persistence of reefs"; Hughes et al. show
  recovery after bleaching running through recruitment. Neither cites the
  other.
- **Collective emotion ([LIT-696](../literature.d/LIT-696.md), [THEORY-126](../theory.d/THEORY-126.md)).** Von Scheve and Ismer's
  minimal collective emotion is "synchronous convergence" across
  individuals produced by a shared event with no mutual awareness. Mass
  spawning, on this paper's evidence, is synchrony of that minimal kind in
  a non-cognitive system. The parallel is the record's; no relation is
  claimed.
- **Coupled-oscillator synchrony ([THEORY-069](../theory.d/THEORY-069.md), [LIT-091](../literature.d/LIT-091.md)).** The record's
  synchronisation material is about units that pull on each other. Nothing
  here is coupling, which keeps this case apart from that material.

## Bearing on the record

- Source of the theory that in A. millepora the nocturnal light regime is
  necessary for spawning on the expected night, with a spawning-night GPCR
  programme whose timing follows the light ([THEORY-tmpezkoq](../theory.d/THEORY-tmpezkoq.md)). That theory
  takes C1–C4 and C7. It holds C5 as a proposal and C6 as background.
- No ML instruction; nothing for the anthology.

## Limitations

- **Single species, single site, single spawning night** for the
  transcriptome (2011), and single season for the light-quality test
  (2006).
- **Small N** in 2011 (5–6 colonies per arm), and the fate of the L and D
  colonies after 16 November is not reported. "Prevented" may be
  "delayed", which is what the 2006 experiment found.
- **Replication of the RNA-seq is unclear.** 24 libraries cannot cover
  every colony at every time point and treatment, and the text does not
  say how samples were pooled. The spawning-gene list comes from a variance
  filter, not a test against biological replicates.
- **Inconsistent numbers in the 2006 design.** "Five colonies were placed
  into each aquarium", "three aquaria for each of the seven treatments" and
  intensity (n = 15) and spectra (n = 10) groups do not reconcile with 90
  colonies. A control group is also mentioned. The treatment sizes are
  therefore uncertain.
- **No mechanism test.** No inhibitor, knockdown or receptor assay. The
  melanopsin-like genes' photopigment function is untested, as the authors
  say.
- **The cue is not isolated.** Both added light and darkness abolished
  spawning, so the experiment shows that the natural night-light pattern is
  needed, not which feature of it (moonlight intensity, the dark interval
  after sunset, moonrise time). The 2006 experiment only adds light, and
  shows its spectrum matters.
- **No test of inter-colony coordination.**
- **Timeline.** The text says treatments began "8 days prior to the
  spawning night". The methods give collection on 9 November and spawning
  on 16 November, which is seven days.

## Open questions

- Do colonies kept dark or lit spawn later, and is the delay a fixed number
  of nights (as in 2006) or abolition for the season?
- Which feature of the night is the cue: irradiance after moonrise, the
  dark interval after sunset, or the timing between them? A design that
  shifts artificial "moonrise" while keeping the dark interval would
  separate them.
- Are the melanopsin-like homologs photopigments, and does blocking GPCR
  signalling block release?
- Does a coral species that spawns on a different night use the same
  programme with a different trigger? The reviewers proposed this and the
  digest names it as future work.
