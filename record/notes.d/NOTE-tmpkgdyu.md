---
status: Read
paper: 'LIT-tmpnmv4q'
title: 'Luppi — Convergent controllers of information integration and its anaesthetic breakdown'
version: 1
history:
- version: 1
  date: '2026-10-22'
  note: >-
    Read in full on 2026-10-22 from the publisher's open-access PDF (CC BY
    4.0), fetched from www.nature.com/articles/s41562-025-02381-5.pdf: the
    typeset version of record, 37 PDF pages, journal pages 777–802 followed
    by Extended Data Figs. 1–4 and the Reporting Summary. Text extracted
    with pdftotext. Read: abstract, introduction, every Results section,
    the Discussion, Methods, data and code availability, author
    contributions, the captions of Figs. 1–8 and Extended Data Figs. 1–4.
    The reference list was skimmed. The figures were not viewed, so what
    they show is taken from their captions and the text. Not read: the
    Supplementary Information (Supplementary Methods, Figs. 1–25, Tables
    1–32 and the Supplementary Discussion), the Source Data, the Reporting
    Summary and the peer-review file. Every dataset description, the
    preprocessing, and most robustness results (motion, debiasing, doses,
    parcellations) are in the Supplementary Information and are reported
    here only as the main text describes them. Page numbers are the
    journal's.
date: '2026-10-22'
summary: >-
  Pairwise integrated information ΦR, computed from resting-state fMRI by
  integrated information decomposition, falls under anaesthesia in humans
  (sevoflurane), macaques, marmosets and mice, with one mouse regimen
  the exception, and returns on recovery: spontaneously in humans, and
  under central thalamic stimulation in two macaques. Network control
  energy rises with it. Regional loss follows cortical PVALB expression in
  three species, and species-specific models reproduce both the PVALB
  effect and the advantage of central over ventrolateral thalamic
  stimulation. The state measured is behavioural responsiveness, which
  the authors call "presumably consciousness".
---
<!-- inactive-ok-file: THEORY-240 THEORY-063 THEORY-091 THEORY-497 — Proposed; accounts this reading bears on, named in prose, nothing here rests on them -->
<!-- inactive-ok-file: CLAIM-tmpdga80 CLAIM-tmp1lvwf — Proposed; the batch's claims, cited as open -->
<!-- inactive-ok-file: TERM-tmpgqmop — Proposed; the batch's term, cited as open -->
<!-- inactive-ok-file: THEORY-tmpvpggv — Proposed; filed from this reading, named -->

# NOTE-tmpkgdyu: Luppi — Convergent controllers of information integration and its anaesthetic breakdown

## Contribution

The paper takes the revised whole-minus-sum measure of integrated
information, ΦR, and applies it to fMRI from four mammalian species under
six anaesthetic regimes. In the main analysis ΦR falls under every regime
but one. It rises again on recovery, and in the macaque it rises again when
central thalamic stimulation restores arousal while the anaesthetic is
still running. The same group's 2024 paper (LIT-949) had shown this
for human propofol and disorders of consciousness. This paper adds three
more species, five more drugs, a causal reversal, and a mechanistic story
from transcriptomics, connectomes and models. What it measures is the
state of being responsive, at rest, with no contents and no report.

## Key insight

Different anaesthetics have different molecular targets, and different
species have different brains. If one change in brain dynamics appears
under all of them whenever the animal stops responding, and goes away
whenever it responds again, that change is a candidate for what the drugs
have in common. The authors offer whole-brain pairwise ΦR as that change.
They use thalamic stimulation to separate it from the mere presence of the
drug: ΦR "co-varies with the consciousness-suppressing effect of
anaesthetics, not with their mere presence in the system" (p. 781).

## Assumptions

- **Responsiveness stands in for consciousness.** The target is
  "breakdown of interaction with the environment" (p. 781). The paper says
  the drugs suppress "responsiveness and presumably consciousness"
  (p. 781). It grants that "Behavioural unresponsiveness is an imperfect
  marker of unconsciousness since it can also occur as a result of sensory
  disconnection or motor impairment, neither of which is the same as
  unconsciousness" (p. 792).
- **Linear-Gaussian dynamics.** The decomposition uses the minimum mutual
  information (MMI) redundancy for Gaussian variables, on the ground that
  "linear-Gaussian models are sufficiently good descriptors" of fMRI
  (p. 795). MMI makes one source's unique information zero by definition,
  and in the dynamical decomposition it "can thus lead to negative-signed
  atoms" (p. 795).
- **Pairwise and averaged.** ΦR is computed for each pair of regions and
  averaged over all pairs. The authors call this "perhaps best viewed as a
  lower bound" (p. 793). A check with 2,000 random sets of six regions,
  split three against three, is the only beyond-pairwise analysis
  (pp. 790–791).
- **Intrinsic information.** ΦR is the information the past of the system
  carries about its own future, "in the absence of any explicit tasks"
  (p. 778). No stimulus is presented.
- **Not a test of IIT.** The intention is "'not' to test integrated
  information theory (in any of its versions: 2.0, 3.0 or 4.0)" (p. 796).
- **Linear control.** Control energy uses the linear time-invariant
  model ẋ = Ax(t) + Bu(t) on each species' structural connectome, with
  time horizon T = 1, between successive fMRI volumes (p. 797).

## Key results

- **The measure (pp. 778–779; Methods pp. 795–796).** In integrated
  information decomposition the time-delayed mutual information of two
  regions splits into 16 atoms. Φ2008 = I(X_past, Y_past; X_future,
  Y_future) − I(X_past; X_future) − I(Y_past; Y_future). The sum of the
  parts counts the persistent redundancy Red→Red twice, so Φ2008 can be
  negative. ΦR = Φ2008 + Red→Red: the synergy-containing atoms plus the two
  pure-transfer atoms. In supplementary simulations, not read here, ΦR is
  higher for network motifs with recurrent connections, and highest for the
  empirical human connectome against rewired nulls (p. 796).
- **The data (pp. 779–781).** Humans: N = 15, awake, deep sevoflurane, and
  spontaneous recovery. Macaques: N = 5, scanned awake and under
  sevoflurane, propofol or ketamine. Marmosets: N = 4, 12 scans each, under
  sevoflurane, propofol or isoflurane. Mice: N = 43, awake (10),
  medetomidine–isoflurane (14) or halothane (19), between animals.
- **ΦR falls under anaesthesia (pp. 780–781, Fig. 2).** Whole-brain mean
  ΦR is lower under anaesthesia in every species and drug, "except for
  medetomidine–isoflurane in the mouse" (p. 781). Human ΦR rises again on
  recovery. In the six-region check both mouse regimens show a significant
  fall (p. 791, Extended Data Fig. 4).
- **Thalamic stimulation restores it (pp. 781–782, Fig. 3).** An
  independent macaque dataset (Tasserie et al.) had deep-brain stimulation
  in "N = 2 anaesthetized macaques" under propofol (p. 781). Central
  (centro-median) thalamic stimulation at 5 V and at 3 V raised ΦR against
  propofol alone. High-intensity stimulation of the ventrolateral
  thalamus, the control site, did not. Low-intensity ventrolateral
  stimulation gave "a smaller but significant increase" without restoring
  arousal (p. 781). Each ventrolateral condition comes from one animal.
- **ΦR tracks arousal best (pp. 781–782, Fig. 3c; p. 791).** A dominance
  analysis predicts the macaque arousal score (0 to 11) from ΦR, Φ2008,
  causal density and net information flow. ΦR carries 51% of the
  explained variance (R² = 0.57, P < 0.001 by permutation). With
  functional connectivity added, ΦR carries 46% and connectivity 15%
  (p. 791). Φ2008 is unchanged under anaesthesia in humans and macaques,
  rises in mice and marmosets, and goes negative in several datasets.
  Causal density misses recovery in humans and changes in neither primate.
  Net information flow behaves like ΦR and is the second-best predictor
  (pp. 790–791).
- **Control energy rises (pp. 782–784, Fig. 4).** The energy needed to move
  between successive brain states is higher under anaesthesia across
  species and drugs, "except for halothane in the mouse" (p. 782). It falls
  again on recovery and under central thalamic stimulation, and also
  partly under low-intensity ventrolateral stimulation. Across individuals
  it correlates negatively with ΦR in each dataset (Fig. 4g). The
  authors' gloss: "the brain's capacity to integrate information is
  systematically diminished when brain dynamics are less controllable"
  (p. 784).
- **Where ΦR falls (p. 784, Fig. 5).** By network-based statistic, most
  significant edge changes are decreases, "overwhelmingly so" in human and
  macaque. Most cross functional systems. "The highest prevalence of
  significant reductions in integrated information involves unimodal
  visual and somatomotor cortices" (p. 784). Default-mode and other
  association regions also fall, so the finding "does not contradict the
  importance of the default mode network (DMN) and association cortex in
  supporting consciousness" (p. 784). The pattern is called "widespread
  but unimodal dominated" (p. 792).
- **PVALB (pp. 784–786, Fig. 5).** Of 81 conserved receptor and cell-type
  genes, PVALB/Pvalb, a marker of fast-spiking inhibitory interneurons, has
  the most consistent spatial relation to regional ΦR loss. Against
  spatial-autocorrelation nulls: human rho(98) = −0.40, P = 0.01; macaque
  rho(80) = −0.61, P < 0.001; mouse, over regions that lose ΦR, rho(24) =
  −0.28, P = 0.008, 95% CI [−0.60, 0.13], and over regions that gain it,
  rho(44) = 0.48. Larger loss goes with more PVALB. SST is positive in
  humans (rho = 0.27, P = 0.045) and null in macaque and mouse. The
  restoration under central thalamic stimulation follows the same PVALB
  map (Extended Data Fig. 2). Subcortically there is no PVALB relation,
  so the link "may be a primarily cortical phenomenon" (p. 786).
- **Thalamic core and matrix (pp. 786–787).** In humans, ΦR loss is
  stronger in thalamic nuclei rich in matrix cells. Mouse data show no such
  relation, by mRNA or by protein.
- **PVALB as control input (p. 787, Fig. 6).** Down-weighting each region's
  control input by its PVALB expression raises transition energy more than
  autocorrelation-matched surrogate maps do, in all four datasets tested
  (Hedges' g from 0.54 to 9.82).
- **Models (pp. 788–789, Figs. 7–8).** Dynamic mean-field models were fitted
  to each species' awake dynamics on its own connectome. Raising regional
  inhibition by PVALB expression lowers simulated ΦR more than null maps
  do, in human, macaque and mouse (g = 1.00, 1.52 and 0.70). The model is
  "not directly fitted to match the anaesthesia data" (p. 788). A macaque
  model fitted to the anaesthetized state, with thalamic nuclei that differ
  only in their tractography, gains more ΦR from simulated central than
  from ventrolateral thalamic stimulation (g = 1.07). The authors grant
  that ventrolateral stimulation "achieves greater success in our model
  than in real data" (p. 793).
- **Robustness (pp. 790–791).** Debiasing against surrogates, doses,
  another parcellation, three motion strategies and protein-based PV
  densities are reported to leave the results qualitatively unchanged.
  Some individual results lose significance with motion as a covariate.
- **Discussion (pp. 791–794).** Anaesthesia and brain lesions causing
  disorders of consciousness "may have functionally equivalent effects"
  (p. 791). ΦR is called "unequivocally the most consistent
  information-theoretic marker of anaesthesia and its reversal" (p. 792).
  The authors propose that anaesthesia acts on output modulation (PV)
  rather than input modulation (SST). They concede that "the consistency
  was not perfect" (p. 793). The weaker mouse effects are put down to
  lighter anaesthesia and different drugs.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Whole-brain mean pairwise ΦR from resting fMRI is lower under anaesthesia than in wakefulness, across four species and five of six regimes | strong as a measured contrast | Fig. 2; pp. 780–781; six-region check, Extended Data Fig. 4 |
| C2 | ΦR returns on recovery, spontaneously in humans and under central thalamic stimulation in anaesthetized macaques | moderate: humans n = 15; stimulation in two macaques, controls from one | Figs. 2c, 3b; p. 781 |
| C3 | ΦR tracks the macaque arousal score better than Φ2008, causal density, net information flow and functional connectivity | moderate: one dataset's behavioural scale, dominance analysis | Fig. 3c; p. 791 |
| C4 | Control energy between successive fMRI states rises under anaesthesia and correlates negatively with ΦR | moderate: linear model, uniform control, one mouse exception | Fig. 4; pp. 782–784 |
| C5 | Regional ΦR loss follows cortical PVALB expression in human, macaque and mouse | moderate: spatial correlations against autocorrelation nulls; cortical only | Fig. 5; pp. 784–786 |
| C6 | PVALB-weighted inhibition is especially suited to lowering controllability and ΦR | weak to moderate: linear-control and mean-field models, not fitted to anaesthesia data | Figs. 6–7; pp. 787–788 |
| C7 | The connectivity of the central thalamus suffices to make it a better stimulation target than the ventrolateral thalamus | weak: one model, which overstates ventrolateral success | Fig. 8; pp. 788–789, 793 |
| C8 | Anaesthesia and DOC-inducing lesions may have functionally equivalent effects | speculative | prior DOC results by the same group; p. 791 |

## Concepts

- **Integrated information decomposition (ΦID)**: the extension of
  partial information decomposition to the information a pair of
  variables' past carries about their joint future, giving 4 × 4 = 16
  atoms grouped as persistence, copy, transfer, erasure, upward and
  downward causation (p. 795).
- **ΦR**: whole-minus-sum integrated information that subtracts the
  "proper" sum of the parts, so persistent redundancy is not counted
  twice; equal to Φ2008 + Red→Red (pp. 779, 796).
- **Φ2008**: Balduzzi and Tononi's whole-minus-sum measure, here read as
  the balance between ΦR and persistent redundancy.
- **Transition (control) energy**: the minimum summed squared input that
  drives the linear network model from one fMRI volume to the next,
  averaged over a scan (p. 797). Higher energy means less controllable
  dynamics.
- **Responsiveness**: interaction with the environment, scored behaviourally
  in macaques on a 0–11 arousal scale (p. 782); the paper's operational
  target.

## Connections

The measure is Mediano et al.'s revised integrated information. The
workspace paper by the same group, LIT-949 (NOTE-799), is the paper's
ref. 45, cited for propofol and disorders of consciousness reducing ΦR
between a shared set of cortical regions, "among those" that fall in the
present human sevoflurane data (p. 791). The macaque stimulation data are
Tasserie et al. (2022); the central-thalamus literature includes
Redinbaugh et al. Integration–segregation difference (Jiang et al.) is
cited as converging on the same unimodal-dominated topography. Network
control follows Gu, Bassett and colleagues, and the pharmacological
flattening of the energy landscape under 5HT2A agonists is the authors'
earlier work. The closure notions of LIT-1306, with Luppi and Mediano
among its authors, are not used.

## Bearing on the record

- **THEORY-240 (Proposed; LIT-949).** That THEORY's `promote_when`
  names this paper's design: it is strengthened "if restoring
  consciousness by intervention (central thalamic stimulation, for
  example) restores gateway ΦR".
  - **Half met.** Central thalamic stimulation restores ΦR in the macaque.
    But the paper has no gateways or broadcasters. Its whole-brain ΦR is
    an average over all pairs, and its regional maps put the largest losses
    in unimodal visual and somatomotor cortex, not in default-mode
    gateways. So it does not show what THEORY-240's claim is about, that
    the change is on the gateway side.
  - **Its refutation clause.** THEORY-240 is in trouble "if it tracks
    sedation or responsiveness rather than consciousness". This paper
    defines its target as responsiveness. It cannot tell the two apart and
    says so (p. 792).
  - **The sample.** The human anaesthetic here is sevoflurane, not
    propofol. The stimulated macaques number two.
  - **Proposed change (proposal only).** THEORY-240's `promote_when` could
    add that the restored ΦR must be shown regionally on the gateway side.
    The status stays Proposed.
- **QUESTION-048 (deficit and recovery evidence).** This is the
  kind of deficit-and-recovery evidence the question asks about, extended
  to four species and to a causal reversal. It confirms THEORY-091's
  limit, as LIT-965 did. Its marker of consciousness is responsiveness,
  which is a marker of access, and the authors say that animals "cannot
  provide subjective reports" (p. 792). The cross-species reach is real,
  but it reaches responsiveness. Nothing in it separates access from
  experience.
- **CLAIM-tmpdga80 (experience constituted by interpretive
  organization).** The exchange cited this paper for integration breaking
  down under anaesthesia. It does show that. But ΦR is a content-free
  statistic of how much information the past of a pair of regions carries
  about their joint future beyond what each carries alone. It is not a
  measure of interpretation in TERM-tmpgqmop's sense: there is no
  distinction, context or consequence for the system in it. So the finding
  bears on the claim only if "interpretive organization" requires such
  integration, which the claim does not say. At most it shows that some
  integration of this kind goes with responsiveness. That is a necessary-
  condition reading of production views as much as of constitution.
- **CLAIM-tmp1lvwf (most interpretation is unconscious).**
  Integration, as A3 named it, was one of the candidate conditions. Here it
  falls with responsiveness, which fits a candidate. But the paper gives no
  case of rich integration without responsiveness, and ΦR has not been
  measured here between conscious and unconscious processing within a
  waking brain. It does not meet the claim's defeater, which needs the
  unconscious cases to fall outside a stated organization.
- **CLAIM-tmpn2xr4 (four facts that come apart).** The stimulation
  design is an intervention that separates what the ordinary trajectory
  cannot: low-intensity ventrolateral stimulation partly restored ΦR and
  controllability without restoring behaviour. That is an empirical case
  of a measure and its supposed behavioural effect coming apart under
  intervention, in the spirit of that claim. The connection is mine.
- **QUESTION-tmpc4j7p.** Integration is on the question's list of
  candidates. This paper gives the candidate a measured form in four
  species. It does not say what the measure would give for a firm or a
  language model, and pairwise ΦR could be computed for either. Applying
  it there is a test the question could ask for, and the paper does not
  attempt it.
- **THEORY-063 (unity as one functional cluster).** Its promotion test
  asks for "a measure of integration in the brain ... computed and not
  asserted" that tracks unity "across waking, dreaming, anaesthesia".
  This is a computed integration measure that tracks anaesthesia, but it
  measures the amount of pairwise integration, not whether there is one
  dominant cluster. It does not meet that test.
- **THEORY-497 (synergy and macro features).** ΦR is mostly
  synergy-containing atoms, so the fall under anaesthesia is a fall in the
  synergistic information about the system's own future that THEORY-497
  describes, relative to the same Gaussian MMI choice.
- **THEORY warranted.** One. THEORY-tmpvpggv states C1–C3: ΦR falls
  with responsiveness across species and returns with it, including under
  thalamic stimulation. The PVALB and model results (C5–C7) bear on no
  record question and are left in this note.
- No instruction for machine-learning practice.

## Limitations

- **Responsiveness, not experience.** The authors say so (p. 792). Sensory
  disconnection or motor impairment would give the same marker.
- **Resting state, no contents.** No stimulus or task was used, so nothing
  here concerns what is experienced or reported, only the state.
- **Pairwise, linear-Gaussian, MMI.** Pairwise ΦR averaged over pairs is a
  lower bound by the authors' account. The six-region check uses random
  bipartitions, not a minimum-information partition. Results may depend on
  the redundancy function; other functions are said to agree, with
  citations.
- **Small causal sample.** The stimulation result rests on two macaques for
  central thalamus and one for each ventrolateral condition. Low-intensity
  ventrolateral stimulation raised ΦR without restoring arousal, which the
  authors explain as neural effects not yet large enough to show in
  behaviour (p. 793). That explanation is untested.
- **One human anaesthetic.** Humans had sevoflurane only. The other drugs
  were given to animals.
- **Mouse exceptions.** The main ΦR analysis misses medetomidine–isoflurane,
  control energy misses halothane, the PVALB correlation in the mouse runs
  both ways, and the thalamic result does not replicate. The authors
  attribute this to lighter anaesthesia; that too is untested.
- **Models.** The mean-field and linear-control models show that a PVALB-
  shaped inhibition or a central-thalamus-shaped input is sufficient in
  the model, not that anaesthetics act through them. The authors grant
  that the drugs' molecular targets are "not all of which are directly
  known to influence inhibition or PV+ interneurons" (p. 792).
- **Most robustness is supplementary.** It was not read.
- **Data access.** Raw data are available from the authors "through
  academic collaboration" for most datasets.

## Open questions

- Does ΦR fall in disconnected but conscious states, such as ketamine
  dreaming or covert awareness in unresponsive patients? That would
  separate integration from responsiveness, which this design cannot.
- Is the restored ΦR under central thalamic stimulation on the side of the
  default-mode gateways of LIT-949, or spread as the anaesthetic loss is?
- What does ΦR do within a waking brain between conscious and unconscious
  processing of the same content, the contrast CLAIM-tmp1lvwf turns on?
- Does a beyond-pairwise or partition-minimizing ΦR give the same
  topography as the pairwise average?
