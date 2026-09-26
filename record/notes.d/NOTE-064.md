---
number: 64
status: Read
formerly:
- NOTE-tmplcpv6
paper: LIT-049
title: 'Bourrat 2023, a coarse-graining account of individuality'
version: 2
history:
- version: 2
  date: '2026-09-25'
  note: >-
    Read in full (full text of the published open-access (CC BY 4.0)
    version, Biol. Philos. 38:33 (2023), 23 pp. I read every page: the
    Introduction; the six unnumbered sections, which the paper cross-refers
    to as "Sect. 2" and so on; Eqs. 1–2; Figs. 1–2 (captions and the text
    describing them); footnotes 1–17; and the reference list.
    Link.springer.com was not needed, because the PDF came through the
    rd.springer.com mirror and is saved as raw4/c30.pdf. I extracted it with
    PyMuPDF to raw4/c30.txt. (`file` reports "11 page(s)" but the PDF has
    23; the extraction has all 23 page headers.) I did not view the figure
    images themselves, so what I say about Fig. 1 comes from the numbers in
    the text and the caption. Nothing else was skipped.). Upgraded from
    `Skimmed` to `Read`: the claims table, assumptions and results are new,
    and the skim is corrected where the full text disagreed.
date: '2026-09-25'
summary: >-
  Bourrat proposes that a partition of particles into collectives defines
  individuals when the "projected" prediction (coarse-grain at t1, then
  evolve the coarse-grained state) differs from the "truthful" one (evolve
  at the fine grain, then coarse-grain at t2) by δC = C_T − C_P < θ,
  across many traits (Eqs. 1–2). He argues that, because measurement and
  computation are finite, coarse-graining can be the only way to predict
  at all: in his example, 100 operations predict 10 entities for 10
  timesteps or 2 collectives for 50. That indispensability is his whole
  case for the "quasi-ontological" status of collectives at Godfrey-Smith
  and Kerr's fifth stage. Nothing is computed on any model.
---

<!-- inactive-ok-file: LIT-049 — Deferred: the paper is placed by this reading; the directive lapses when its status changes -->

<!-- inactive-ok-file: LIT-005 — Proposed; this reading is of the paper LIT-005 cites, read against it -->

# NOTE-064: Bourrat 2023, a coarse-graining account of individuality

## Contribution

- A generic, informal criterion for when a partition of lower-level entities ("particles") defines higher-level individuals ("collectives"). Compare the error between two routes to the coarse-grained state at t2:
  - the *truthful* route: evolve the fine-grained state, then coarse-grain;
  - the *projected* route: coarse-grain at t1, then evolve the coarse-grained state.

  Accept the partition if the error is below a threshold θ across many traits, and, where environmental common causes might fake coherence, conditional on the environment (pp. 11–14, Eqs. 1–2, Fig. 2).
- A pragmatic argument that finite measurement and computation make the coarse description not just convenient but, beyond some horizon, the only available one (pp. 15–17). The paper calls the status this confers "quasi-ontological".
- An application of both to Godfrey-Smith & Kerr's (2013) five-stage model of ETIs. The fifth stage introduces a collective fitness parameter with no map to particle fitness. Bourrat reads that as forced by the map being "fundamentally unknown", either not measured or too costly to measure, rather than as a modeller's free choice or a factual change in the level of selection (pp. 18–20).

## Key insight

A higher level is a level of *description*: "There is nothing that exists at the higher level that could not be described or predicted, in principle, for the lower level" (p. 15). What makes collectives look ontologically real is that, for a fixed budget of measurement and computation, predicting them lets you see further ahead than predicting their parts. An ETI is where that trade-off tips: "the breaking point where a pragmatic but indispensable shift in description must occur" (p. 17).

## Assumptions

- **Physicalism / supervenience.** A change at the particle level necessarily changes the collective level (p. 5). Coarse descriptions carry at most as much information as fine ones "if both descriptions refer to the same substrate" (fn. 13).
- **A functional map from fine to coarse state exists**, so that the projected route is defined. Footnote 11 concedes this may not exist, in which case "the vertical white arrow of Fig. 2 would be assumed rather than represent a functional mapping".
- **The lower-level entities are bona fide individuals** (fn. 6), or are themselves coarse-grainings (fn. 11).
- **Proximity as a prior on partitions.** Nearby cells interact more (p. 9), which prunes the 2ⁿ − 2 bipartitions. There is a network version in fn. 8: maximise within-group edges and minimise between-group edges.
- **Coarse-graining by averaging** a property within each part (p. 9).
- **Discrete, synchronous generations** at both levels in the evolutionary case, so every offspring particle belongs to an offspring collective (p. 14). The author calls this unrealistic and adopts it for simplicity.
- **The cost model for the pragmatic argument:**
  - one operation per entity per timestep;
  - no interactions;
  - no group-level operations (fn. 14).
- **A threshold θ** set by "context and measurement errors" (p. 11). It is never specified.

## Key results

There are no theorems, simulations or data. The formal content, in full:

- **Eq. 1.** δC = C_T − C_P: the difference between the truthful prediction C_T and the projected coarse-grained prediction C_P, for the change in a trait between two times (p. 11–12).
- **Eq. 2.** A coarse-graining is acceptable if δC < θ and unacceptable if δC ≥ θ. δ*C is the minimal δC below θ, and it marks "the best candidate for defining a level of individuality" (p. 12).
- **Multi-trait version.** Bold **δC** is a vector over n traits. A coarse-graining is taken to define individuals only if **δC*** exists for the *same* coarse-graining across many traits, following functional integration (p. 13).
- **Tie-breaking and horizon.** Tied coarse-grainings are separated by testing longer and shorter timesteps. Individuality may be timescale-relative (p. 13; fn. 4).
- **Environment-conditioned version.** Low δC can come purely from ecology. In the example, chemotaxis toward resources at four corners aligns neighbouring cells. For such cases the paper proposes **δC|E**, checked to "remain consistently below the threshold θ in all the states of the environment (with the probability to be in a particular state chosen from the actual probability of the system)". It offers two operationalisations: a multidimensional distance, or the maximum element (p. 14).
- **Fig. 1 toy.** A coherent triplet (240°, 220°, 200° → 220°) has max error 20°. An incoherent one (350°, 240°, 80°) gives "≈223°" with max error 143°, which is arithmetically averaged (see corrections: circular mean ≈355°, max error ≈115°).
- **Evolutionary toy (p. 14–15).** If particles reproduce only when interacting with at least three others, a partition that captures this gives a small δC. A partition into pairs shows unexplained stochastic collective reproduction and a larger δC.
- **Computation toy (p. 16).**
  - A budget of 100 operations covers 10 entities for 10 timesteps, or 2 collectives for 50.
  - Predicting the fine grain to 50 steps would need 500 operations.
  - The loss in accuracy is therefore "a counterfactual one".
- **Measurement argument (p. 16).** In Hammerschmidt et al. (2014)-type experiments, colony-level measurement is the only affordable one. Measuring the parts of highly integrated collectives alters them.
- **Reading of Godfrey-Smith & Kerr (2013), pp. 18–20:**
  - In stages 1–3 both levels "contain the same quantity of information" (gestalt switching is possible, no coarse-graining).
  - Stage 4 may lose the information needed to recover collectives from particles. There, the collective phase may even have *higher* dimensionality, in a temporal rather than mereological sense.
  - Stage 5 drops the particle–collective fitness map, because it is unknown or too costly.
  - Conclusion: "there is no factual change of the level at which selection occurs during an ETI … for pragmatic reasons, it becomes useful to pretend as if this were the case" (p. 19).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Okasha's factual MLS1→MLS2 (fitness-decoupling) account fails because the two levels' fitnesses are commensurable once measured in the same environment | citation of own prior work | §2, pp. 4–5, citing Bourrat 2015a,b; 2021; Bourrat et al. 2022; in press |
| C2 | Godfrey-Smith & Kerr's purely modelling-choice account leaves the stage-5 collective fitness "mysterious" | informal argument | §2, p. 5; §6, p. 18 |
| C3 | A multiply realisable property is "simply the philosophical equivalent" of a universal property under renormalisation-group coarse-graining | assertion, attributed to Batterman 2000 | §3, p. 7 |
| C4 | A partition defines individuals when δC = C_T − C_P < θ across many traits, and δ*C (minimal δC below θ) marks the best candidate | definition/proposal; **degenerate as stated** | Eqs. 1–2, pp. 11–13. The identity partition (every particle its own collective) gives C_P = C_T, so δC = 0. Fn. 12 concedes zero error when there is no within-group variation. Minimising δC therefore selects the finest grain unless a cost term or a minimum group size is added, and the criterion includes neither. δC is also signed, so "δC < θ" accepts any negative error; a norm is needed. |
| C5 | Single-trait coarse-grainings can be spurious, so individuality requires one partition to be good for many traits | informal argument + toy (chemotaxis vs phototaxis) | p. 13 |
| C6 | Environment-driven coherence can be excluded by requiring δC\|E < θ in all environmental states | proposal, not shown to work | p. 14. In the paper's own chemotaxis example, cells are still coherent *given* each fixed resource state, so conditioning alone does not remove the ecological case. What would remove it is variation in E, i.e. states such as uniform resources that break the alignment. The proposal is really an invariance-across-environments test, and "all states" sits awkwardly with weighting by "the actual probability". |
| C7 | Under a fixed operations budget, coarse-graining extends the prediction horizon (10 → 50 timesteps at 100 ops) | arithmetic under stated toy assumptions (correct as arithmetic) | p. 16, fn. 14 |
| C8 | Fine-grained descriptions have primacy because coarse ones never contain more information | assertion (true for a deterministic coarse-graining map, by data processing) | p. 15, fn. 13 |
| C9 | Collectives acquire "quasi-ontological" status because they are sine qua non for prediction or explanation, and "this property is sufficient to see them as having an ontology" | informal argument | pp. 16–17 |
| C10 | The stage-5 collective fitness parameter is introduced because the particle–collective map is "fundamentally unknown" (not measured or too costly) | assertion about scientific practice | p. 19; no case examined |
| C11 | In Godfrey-Smith & Kerr stages 1–3 both levels contain equal information | textual reading of GS&K; unverified by me | p. 18 |
| C12 | Abstract: the change of parameters "is necessary and cannot be dismissed as merely epistemic" | **headline claim exceeds the body** | The body says there is "no factual change" in the level of selection and that one "pretend[s] as if" there were (p. 19). The Conclusion says individuals are "ultimately epistemic tools" (p. 20). What is shown is pragmatic indispensability under resource limits, which is still an epistemic ground. |
| C13 | Conclusion: the account "supposes the existence of a map between the terms at different levels" | in tension with the body | Fn. 11 allows that the map may only be assumed. Stage 5 is characterised by the particle–collective fitness map being absent (p. 19). |

## Method

1. Choose a trait, or better a vector of traits, and candidate partitions of particles into collectives, pruned by proximity or interaction-network modularity (fn. 8).
2. For each partition:
   - compute the truthful prediction C_T (evolve fine, then coarse-grain at t2);
   - compute the projected prediction C_P (coarse-grain at t1 by averaging, then evolve the coarse state);
   - form δC.
3. Accept partitions with δC < θ for many traits. Prefer the minimal one, δ*C. Break ties by varying the horizon. Where ecological common causes are suspected, require δC|E < θ across environmental states.
4. For evolving populations, add rules mapping particle births and deaths to collective births and deaths.

My note: step 2 needs C_T, a full fine-grained prediction. Yet the pragmatic section's case for quasi-ontology is precisely the regime where fine-grained prediction is unaffordable or unmeasurable (pp. 16–17, 19). So the criterion that certifies a collective cannot be evaluated where the certification matters most, except by validating on shorter horizons or subsamples. The paper does not propose that.

## Concepts

- **Particle / collective**: lower-level entities, and the coarse-grained entities formed from them (p. 2).
- **Coarse-graining**: discarding information by mapping a fine description to a coarser one, such as rounding, 2×2 pixel averaging, decimation or RG. Here it means partitioning particles and averaging a property within each part (pp. 5–9).
- **Truthful vs projected prediction**: fine-evolve-then-coarse-grain vs coarse-grain-then-evolve (Fig. 2, p. 11). Their agreement is what a coarse-graining is judged by.
- **δC, δ*C, δC (vector), δC|E**: prediction error, its minimum below θ, the multi-trait vector, and the environment-conditioned version (pp. 11–14).
- **Quasi-ontological individuality**: treating collectives as if they were independent of their parts, warranted when doing so is indispensable for prediction under finite resources (pp. 5, 17, 19).
- **MLS1 / MLS2**: collective fitness counted in particles produced (aggregative) vs in collectives produced (Damuth & Heisler 1988), p. 4.
- **Gestalt switching**: re-describing an MLS1 process at either level with no fact of the matter (fn. 16).
- **Level (of individuality)**: a level of description, not of being (p. 15).

## Connections

**Against [LIT-005](../literature.d/LIT-005.md)** ("Adding causality…", reads/73). This paper is the earlier one, and [LIT-005](../literature.d/LIT-005.md) cites it. So the question for each of [LIT-005](../literature.d/LIT-005.md)'s three defects is whether it was already present here, not whether it was repaired here.

- **Â never computed.** *Neither repaired nor repeated. The same pattern appears one step earlier.* There is no Â, no mutual information and no DAG in this paper. Its own measure, δC, is likewise never computed on any model. The only numbers are the Fig. 1 angles (arithmetically mis-averaged) and the 100-operation arithmetic. "My account will be presented mostly informally with the help of toy examples" (p. 8). So the no-worked-example habit carries straight through from this paper to [LIT-005](../literature.d/LIT-005.md).
- **Â = A identity (fails on S′ = S ⊕ E).** *Absent.* The paper states no information-theoretic identity at all, and declines to summarise Krakauer et al.'s measures (p. 8). The nearest thing is δC|E (p. 14). It is the observational, stratify-on-E ancestor of [LIT-005](../literature.d/LIT-005.md)'s A = I(S′; S | E): score within each environmental state and weight by "the actual probability of the system". So the stratification idea that [LIT-005](../literature.d/LIT-005.md) later equates, wrongly, with the interventional Â originates here, as a fix for the ecological confound. The XOR counterexample has an analogue here. A system whose coherence given E holds in every E-stratum but vanishes when E is marginalised would pass δC|E. Whether that is the right verdict is exactly the question [LIT-005](../literature.d/LIT-005.md) got wrong. This paper does not raise it.
- **Fig. 3 backdoor left open.** *Absent*, since there is no causal graph. The chemotaxis example (p. 13–14) is the confounding case that [LIT-005](../literature.d/LIT-005.md) formalises as its Fig. 2: environment E as a common cause of neighbouring cells' coherence. Here it is handled by conditioning on the current environment only. If resource distributions persist or feed back (cells deplete resources), conditioning on E_t alone would have the same lagged-environment gap as [LIT-005](../literature.d/LIT-005.md)'s Fig. 3. The paper has no temporal structure fine enough to show this, so I record it as a latent, not an actual, error.
- **Shared unsolved problem: scale selection.** [LIT-005](../literature.d/LIT-005.md) §7 concedes Â cannot tell an individual from a part of one, and proposes "the coarsest grain in which Â is maximal". Here the same problem appears more sharply. Minimal δC is attained by the identity partition (C4), so the accuracy criterion prefers parts over wholes. The cost argument of pp. 15–17 is the intended counterweight, but it is never made part of the criterion. Neither paper closes this.

**Other connections:**

- **δC = 0 is the commuting-diagram condition**: exact lumpability of the coarse-graining, "consistency" in Wolpert et al.'s state-space compression (cited, via Libby et al. 2016), and computational or causal closure in the emergence literature. Bourrat cites only Libby/Wolpert.
- **Accuracy-plus-cost selection of a macroscale** is Libby et al.'s framing. Scale selection by an information criterion is the move of the causal-emergence work in [LIT-027](../literature.d/LIT-027.md) and [LIT-025](../literature.d/LIT-025.md) (reads/22, reads/21). Those papers do write down a selection objective, which is what this one lacks (my observation; none is cited here).
- **Philosophical lineage:**
  - Batterman 2000/2001 (RG and multiple realisability);
  - Dennett's "real patterns" and Goodman's projectibility, flagged in fn. 10 as links "worth investigating further";
  - Godfrey-Smith 2006 (model-based science, "imagined concrete things");
  - Griesemer 2008 on the "dual character" of individuality concepts.

## Bearing on the record

- **[LIT-049](../literature.d/LIT-049.md)'s seeded summary is accurate in substance and should be tightened in three ways:**
  - the formal criterion is δC < θ (truthful vs projected prediction), not a cost-aware objective;
  - the cost argument is a separate, verbal justification;
  - nothing is computed.
- **The abstract's "cannot be dismissed as merely epistemic" is stronger than the body** (C12). A citation of [LIT-049](../literature.d/LIT-049.md) for an ontological claim about individuals would overstate it. The paper's own conclusion is pragmatic indispensability.
- **[LIT-005](../literature.d/LIT-005.md)'s reading (reads/73) should note** that the confounding worry it formalises, and the stratify-on-E response it gets wrong, both first appear here in δC|E (p. 14).
- **No bearing on the Anthology of the SOTA.** The paper carries no instruction for ML practice and supports or contradicts no THEORY document. The truthful/projected criterion is structurally the latent-consistency / model-irrelevance condition used in state abstraction and learned world models. The accuracy-vs-compute trade-off is familiar there too. But the paper makes no ML connection, and the analogy is the reader's. Nothing here warrants an ANTH- document.

## Limitations

- **No worked model or data.** Eqs. 1–2 are never evaluated beyond hand toys, by the author's own description (p. 8).
- **The criterion is degenerate as written** (C4). Finer partitions minimise δC, and the trivial partition achieves 0. The cost term needed to prevent this is argued for (pp. 15–17) but never formalised. θ and the trait set are unspecified.
- **δC is signed** (Eq. 1). It needs a norm or distance, which p. 14 gestures at only for the vector δC|E.
- **C_T is required**, which contradicts the regime in which the account says collectives matter: fine-grained prediction unaffordable or impossible.
- **δC|E does not, as described, exclude the paper's own chemotaxis case** (C6).
- **Angle averaging in Fig. 1 is not circular** (see corrections). This does not change the qualitative point.
- **The cost toy assumes non-interacting entities.** Interactions, which are what makes collectives cohesive, change the scaling. The effect on the 10-vs-50 comparison is not discussed.
- **Headline vs body.** "Not merely epistemic" (abstract) against "pretend as if" and "ultimately epistemic tools" (pp. 19–20). "Supposes the existence of a map" (Conclusion) against the stage-5 map being absent (p. 19).
- **Typographical slips:**
  - fn. 3 reverses the containment ("each micro-variable contains at least one macro-variable");
  - p. 12 labels a difference "(θ)";
  - p. 13 "difference between truthful and predicted prediction";
  - p. 20 "MSL1".

## Open questions

- Can the account be stated as one objective, prediction error plus measurement and computation cost, as in state-space compression? Evaluated on an explicit ETI model (for example ecological scaffolding, or Hammerschmidt-type life cycles), does it select the collective partition, and does the selected grain shift as the transition proceeds?
- How can a collective be certified when C_T is unaffordable? Is short-horizon validation enough to license long-horizon use?
- Should the ecological confound be handled by conditioning (δC|E, later A in [LIT-005](../literature.d/LIT-005.md)), by invariance across environmental states, or by intervention ([LIT-005](../literature.d/LIT-005.md)'s Â)? This paper's chemotaxis example suggests conditioning alone is insufficient.
- Does the stage-5 fitness parameter become indispensable in the cost sense at a point that can be located empirically, rather than by the modeller's choice?

## Corrections to the seeded skim

- Title. The published title is "…how the emergence of individuals represents a *summary* of lower-level evolutionary processes" (p. 1), which matches the dossier and [LIT-049](../literature.d/LIT-049.md). The title in this task's instructions ("represents a *change* in lower-level evolutionary processes") is wrong.
- Cost in the algorithm. The dossier says Bourrat "keeps the cost term" from Libby et al. and gives an algorithm. In the text, the algorithm (pp. 9–14, Eqs. 1–2) is accuracy-only: "a particular δC … that is both minimal and inferior to θ … would be the best candidate for defining a level of individuality" (p. 12). Cost enters only afterwards, in the pragmatic section (pp. 15–17), as a verbal justification. It is never combined with δC into one criterion. The dossier's summary line implies more integration than the paper has.
- Details the dossier did not capture:
  - the truthful/projected construction (Fig. 2), which is the paper's only formal apparatus;
  - the vector version **δC** over n traits (p. 13);
  - the environment-conditioned **δC|E**, meant to exclude cases where low error is "driven purely by ecological factors" (chemotaxis example, pp. 13–14);
  - the birth–death mapping rules for the evolutionary case, with discrete synchronous generations assumed (p. 14).
- The Fig. 1 numbers do not check out. The paper averages directions 350°, 240° and 80° arithmetically to "approximately 223°", with maximal error 143° (p. 9–10). Direction is a circular variable. The circular mean is ≈355° (resultant length 0.22), with maximal error ≈115° (my computation). The qualitative point that this coarse-graining is poor survives. The 240°/220°/200° case (mean 220°, error 20°) is correct either way.
- The dossier says Krakauer et al.'s measures are "built on". In fact the paper explicitly declines to state them: "which I will not summarize here" (p. 8). It reads Krakauer et al. as a predictive-accuracy account only.
- Chronology, which affects the comparison asked for. This paper (received 15 Jul 2022, published 14 Aug 2023) predates [LIT-005](../literature.d/LIT-005.md) (received 2 Jul 2023, published Feb 2024) and is cited by it. So it cannot "repair" [LIT-005](../literature.d/LIT-005.md)'s defects. See Connections.
