---
status: Read
paper: 'LIT-tmplg4lb'
title: 'Majikes et al. — The blocked state as a limit on single-fold yield in DNA origami'
version: 1
history:
- version: 1
  date: '2026-11-05'
  note: >-
    Read on 2026-11-05 from the PubMed Central author manuscript
    (https://pmc.ncbi.nlm.nih.gov/articles/PMC11005093/, NIST author
    manuscript, NIHMS1729042); text converted from the HTML. Read in full:
    the abstract, the introduction, the sections on thermodynamics of
    formation, the model system, the equilibrium model and its
    origami-relevant approximation, methods, affine transformation and
    uncertainty, confirmation of the blocked state, yield against
    staple:scaffold ratio and fold distance, the blocked state in whole
    origami and tiles, the conclusions, all figure captions and Tables 1
    and 2. Not read: the figure images, so no yield value is read off a
    plot; the reference list (scanned); equations 1–14, which came through
    garbled in layout and are paraphrased; and the supplement (Tm data,
    the low-temperature solution, the slower-anneal figure S4), which PMC
    served behind a challenge page, where the reader stopped.
date: '2026-11-05'
summary: >-
  A single-fold origami assay with a topology reporter finds that the
  folded fraction after annealing rises with staple excess to a turnover
  near 1–5× and then falls below 50 %, because each of a staple's two
  scaffold domains can be taken by a separate staple (the blocked state),
  as an equilibrium model with folded/blocked = j_fold/[staple] predicts;
  motif does not matter and a twofold slower anneal gives the same trend.
  The whole-origami escape by cooperativity and strand displacement is
  proposed, not tested; the supplement unread.
---
<!-- inactive-ok-file: CLAIM-184 CLAIM-478 CLAIM-557 CLAIM-566 CLAIM-567 CLAIM-569 CLAIM-570 CLAIM-571 CLAIM-574 CLAIM-581 CLAIM-583 CLAIM-591 CLAIM-592 CLAIM-tmp7y162 THEORY-1398 THEORY-tmpynb4z THEORY-tmpzb4hv THEORY-tmpzi9gz NOTE-tmpwxm2p — Proposed, Unavailable, Skimmed or new; cited from the reading of Majikes et al. (2021) as open -->

# NOTE-tmpetbc9: Majikes et al. — The blocked state as a limit on single-fold yield in DNA origami

## Contribution

The same NIST group's single-fold system (an M13mp18 scaffold with about
200 oligos removing secondary structure, one two-domain folding staple,
and a fluorophore–quencher reporter that reads topology, a circle against
a figure-eight) is used to measure how much of the scaffold ends folded
after an anneal, across a 400-fold range of staple:scaffold ratio, at
fold distances of 131, 1187 and 3407 bases, and for three staple motifs.
The paper reports the first experimental sight of the blocked state,
"previously computationally observed" in oxDNA by Snodin et al. (its
reference 12), gives an analytic rule for single-fold yield in staple
excess, and proposes why whole origami escapes it.

## Key insight

A staple that closes a fold must bind two scaffold domains. If two staple
molecules each take one, neither can close the fold: the scaffold is
blocked. Closing is unimolecular, blocking bimolecular, so excess staple
favours blocking. At equilibrium and large excess the folded-to-blocked
ratio is the fold's j-factor over the free staple concentration, and
yield falls as excess rises: a feasible target lost to a competitor that
more resource feeds.

## Assumptions

- **The low-temperature end state is equilibrium**, folded and blocked
  only, "provided that the quench is not too rapid"; checked by one
  twofold slower anneal (in the unread supplement).
- **Strand displacement is neglected in the model**, though invoked as
  the escape in whole origami.
- **The reporter is fully quenched**, else rescaled: the fitted scale
  factors of 0.75–0.89 amount to assuming a leaky reporter.
- **Concentrations corrected** for underestimation by UV-vis, up to 20 %.
- **Staples PAGE-purified** for the single fold; not for whole origami.

## Key results

- **The end state (Model System; Fig. 2a).** "the final state will consist
  entirely of the folded or blocked states to the extent possible given
  the initial concentrations of scaffold and staple, and provided that the
  quench is not too rapid."
- **The yield rule (Origami-relevant approximation; Eqs. 10–11).** At
  tenfold excess or more, folded/blocked = j_fold/[S] and yield tends to
  j_fold/S0. The text's gloss, "absent cooperative effects, the yield of a
  single fold in an origami is proportional to the ratio of the initial
  staple concentration and the j-factor", has the ratio inverted relative
  to the formula. Below stoichiometry, yield is the staple:scaffold ratio.
- **Turnover (Confirmation of the blocked state; Fig. 3).** "the yield of
  the folded state increases as a function of staple concentration up to
  about 5× the scaffold concentration", then falls, "a result of the
  blocked state becoming increasingly favored". Theory puts the peak at
  1:1; "the observed offset provides some evidence of the interplay of
  kinetic and quench effects", but "it is difficult to determine the exact
  process".
- **All fold distances (Fig. 4a).** "All three folding distances have the
  expected turnover in yield between 1× to 10× staple concentration and all
  fall below 50 % yield at high staple:scaffold ratios."
- **Not kinetic at this scale.** "We do not anticipate this to be a kinetic
  effect as anneals performed two times slower replicated the trend (SI Fig
  S4)." The standard anneal steps down at 0.75 °C per minute from 80 °C.
- **j-factors (Table 2).** The 3407-base fold yields more than the 1187:
  "it is difficult to say whether one, the other, or both are anomalous";
  the authors "make the assumption that the 3407 base fold is anomalous".
- **Motif does not matter (Fig. 5).** The 15-15, 25-25 and 10-40 staples
  "had the same yield of the folded state", "consistent with the notion
  that the energetic difference between the blocked and folded states is
  independent of the size of staple domains". For 25-25, "numerous samples
  of moderate scaffold:staple ratio failed to collapse".
- **Whole origami escapes (Fig. 6).** The notched rectangle "still forms at
  high fidelity even at 100x staple excess", even when "taken from the
  thermocycler at 95 °C and immediately imaged", which the authors find
  "somewhat surprising". Truncated staples "could poison a binding site
  until removed by a correct copy via strand displacement".
- **The proposed escape.** Folding shortens fold distances and raises j;
  but "cooperativity can go both ways – stiffer structures due to
  partially assembled regions can disfavor certain folds and thus favor
  blocked states." Release of a blocking strand is driven by "the 3/2R
  gain in entropy as a blocking strand is released into solution".
  Origami "would nucleate in areas having short fold distances, giving
  rise to a growth front"; the corrections "can be slow and are only
  favorable along a ‘nucleation front’".
- **Tiles (Fig. 7).** In tile growth an overabundant strand's relative
  excess "increases geometrically as the reaction progresses", blocking
  perimeter sites and "ultimately terminating growth".
- **Barrier type left open (Conclusions).** "The degree to which the
  blocked state will act as a barrier, either thermodynamic or kinetic,
  will depend heavily on the distribution of fold j-factors, initial
  concentrations, and on the annealing regime."
- **What the measurement can tell apart.** "our reporter cannot
  distinguish between the blocked state and a scaffold without a staple";
  blocked is told from unbound by regime, "whereas at high excess that
  fraction is linked to the blocked state". Gels "failed to identify any
  conditions that could distinguish the circular and figure-eight states".
  Resolving more: "a typical staple with three domains would require at
  least five reporting channels."

## Concepts

- **Blocked state**: each fold domain taken by a separate staple.
- **j-factor**: a fold as an effective local concentration; the ratio
  j/[S].
- **Staple:scaffold ratio as a non-monotone control.**
- **Unimolecular against bimolecular binding**; intra- and inter-fold
  cooperativity.
- **Strand displacement as repair**; **nucleation front**.
- **Topology reporter** against hybridization reporter; affine collapse,
  with failure to collapse as a rejection test.
- **Off-stoichiometry in tile growth** as blocked growth.

## Connections

It extends Majikes et al. 2020 (LIT-tmp0hqya, NOTE-tmperio5,
THEORY-tmpynb4z) from the holding side of one fold (melting temperature
against fold distance, recorded on the melt) to the reaching side (the
population folded after an anneal), reuses its j-factors as the a priori
model, and adds a second mechanism to the same nucleation-and-growth
inference. Rothemund (LIT-tmp5gf89, NOTE-tmp8kyp2, THEORY-tmpzb4hv) found
9:1 and 100:1 excess indistinguishable for whole rectangles and proposed
strand invasion; this paper shows the single fold is hurt by such excess
and supplies the mechanism by which the whole rectangle may not be. The
blocked state is the elementary competitor a domain-level model such as
Dannenberg et al.'s (LIT-tmpdyrnb, NOTE-tmpyo994) must carry. The
nucleation-front hypothesis sits beside the measured pathways of Dunn et
al. (LIT-tmpqku12), Schneider et al. (LIT-tmp7v945) and Lee Tin Wah et al.
2016 (LIT-tmps9gx3), whose own mass-action model has the same blocking
by a second copy, and beside Sobczak's isothermal folding (LIT-tmpwddcn,
NOTE-tmpwxm2p); it tests none of them. Like Wagenbauer et al.
(LIT-tmpduceb), it finds the cheap probe hides differences; strand
displacement, designed actuation in Marras et al. (LIT-tmp11aw1), is here
the proposed repair of a misfold. Against the held simulation, LIT-2081
(NOTE-1561, THEORY-1398): complementary, a local, per-fold,
concentration-driven trap beside global topological ones, both pointing
to long or interior folds as the hard ones.

## Bearing on the record

- **A's characterization.** That the authors found a "previously
  unobserved blocked state" in a single-fold assay: supported (abstract).
  That obstacles to correct assembly can arise at the level of one
  staple-mediated fold: supported in substance, A's paraphrase. A's
  framing of it as a precedent for kinetic trapping, a malformed state
  that the system is slow to escape although the target is lower in free
  energy, is not what the paper found for the single fold: its blocked
  state is an "equilibrium blocked state", favoured at high excess, and
  the trend survived a slower anneal. Kinetic-trap language appears only
  as a hypothesis for whole origami, and the authors leave the barrier
  type open. A's reading-list entry, "Kinetic blocking and failure
  mechanisms at the level of a single fold", is A's paraphrase; "kinetic"
  is not supported for the single fold.
- **CLAIM-567 (feasible, reachable, reliably reached): supports,
  directly.** The folded state is feasible and reached, and at high excess
  reached by under half the molecules through an equilibrium competitor;
  reliability is set by S0/j. CLAIM-357's separation of infeasibility from
  realized shortfall fits: here the shortfall is realized with the target
  feasible.
- **CLAIM-tmp7y162 (non-monotone resource, window): a parallel case on
  another resource.** Staple excess has a window, but at a single fold it
  is equilibrium, not a time budget, and heat is not what drives it.
- **CLAIM-569: qualifies.** The constructing resource is non-monotone for
  one fold and behaves otherwise for a whole origami, where Rothemund
  found excess harmless.
- **CLAIM-583: qualifies.** A changed motif joining the same scaffold sites
  left yield unchanged; a changed fold distance changed it.
- **CLAIM-571: supports, as hypothesis.** Leaving the blocked state needs
  a whole staple displaced, possible only once neighbouring folds raise j;
  holding the fold needs no such thing.
- **CLAIM-591: weak, inferred**: repair is favourable only along a front,
  a one-way order, unmeasured. **CLAIM-184: supports locally**, as an
  equilibrium share at one fold, not lock-in.
- **CLAIM-557 and CLAIM-574 (observing refines): supports.** One topology
  channel lumps blocked with unbound, gels lump circle with figure-eight,
  and more states need more channels. CLAIM-570 and CLAIM-592: a weak
  illustration, the dearer probe proposed, not built.
- **QUESTION-380 (small compatible nucleus): directly relevant, as a
  hypothesis.** Nucleate where fold distances are short; each fold raises
  its neighbours' j and lets blockers be displaced; tiles lack these
  cooperativities and stall.
- **QUESTION-tmpg0j9y**: a window on the amount of one staple, not an
  allocation among staples.
- **CLAIM-581, CLAIM-566, CLAIM-478, CLAIM-025, QUESTION-388, TERM-070:
  nothing.**
- Filed: THEORY-tmpzi9gz. No instruction for machine-learning practice.

## Limitations

- **One fold at a time**, three fold distances, and a single test of
  motif at one distance; points sparse around the turnover.
- **One reporter channel** cannot tell blocked from unbound; the
  identification rests on regime and model.
- **The 1187/3407 inversion** is unexplained and one fold is declared
  anomalous by assumption; the fitted scale factors imply a leaky
  reporter or a concentration error.
- **The slower-anneal control and the low-temperature solution** are in
  the supplement, unread.
- **Whole-origami claims** rest on qualitative AFM of one design and on
  reasoning, with no yields; strand displacement is neglected in the
  model yet invoked as the escape.
- **Text quirks**: the short fold is 131 bases in Fig. 4 and Table 2 and
  138 once in the text; the turnover is "between 5 × and 1×" in Results and
  between 1 and 10 in the Conclusions.
