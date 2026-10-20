---
number: 726
status: Read
formerly:
- NOTE-tmp6pxon
paper: LIT-1038
title: 'Hoel, Albantakis & Tononi — Quantifying causal emergence shows that macro can beat micro'
version: 1
history:
- version: 1
  date: '2026-10-13'
  note: >-
    Read in full from the PubMed Central PDF of the published article
    (PMC3856819, pnas.201314922.pdf, 6 pp., the PNAS typeset pages
    19790–19795), fetched through the Internet Archive's capture of
    2022-11-13 because PMC now answers scripted requests with a
    reCAPTCHA page and pnas.org returned 403. The paper is free on both
    sites (bronze open access, per OpenAlex). An earlier capture of the
    pnas.org PDF (2021-12-06) was truncated at 1 MiB and was not used.
    Text extracted with pdftotext; the extraction is clean except that
    the display equations lose their layout, so the formulas below were
    rebuilt from the surrounding text and the definitions. Read: the
    whole main text, the Significance box, all six figure captions and
    the reference list. Not read: the online Supporting Information
    (derivations, Figs. S1–S2, the network-motif section), which the
    main text cites for proofs of the bounds and for one example of
    causal reduction. Every quotation below was checked against the
    extracted text by script, with whitespace and line-end hyphenation
    normalised.
date: '2026-10-13'
summary: >-
  Effective information (EI), the mutual information between uniformly
  imposed interventions on a system's states and their effects, can be
  higher for a coarse-grained macro description than for the micro
  description it supervenes on. This happens when coarse-graining makes
  the mechanisms more deterministic or less degenerate by more than the
  smaller state space costs. Four toy systems of binary logic gates
  give gains of 0.40 to 2.92 bits. Causal emergence is defined as that
  gain. The examples are computed exactly; the reading of the EI peak as
  the level where causation happens rests on the choice of a uniform
  intervention distribution at each level, which the paper adopts and
  does not test.
---
<!-- inactive-ok-file: THEORY-071 — Proposed; compared, nothing here rests on them -->
<!-- inactive-ok-file: THEORY-222 — Proposed; named in the dated note of 2026-10-16 as citing this paper, nothing in the reading rests on it -->

# NOTE-726: Hoel, Albantakis & Tononi — Quantifying causal emergence shows that macro can beat micro

## Contribution

A causal, quantitative criterion for emergence. Earlier arguments for
emergence were qualitative, and the few quantitative ones (Bar-Yam's
multiscale variety, Seth's Granger emergence) were not based on causal
models. The paper fixes a micro mechanism completely, defines macro
descriptions by coarse-graining it in space or time, measures effective
information at each level under interventions, and shows by worked
examples that the macro can score higher. It names the difference in
bits "causal emergence".

## Key insight

EI is effectiveness times size. A finer description has more states, so
more room for information, but its mechanisms may be noisy or degenerate.
A coarser description has fewer states, but grouping can average out noise
and merge states that lead to the same place. When the second effect beats
the first, the coarse description is the more informative causal model of
the same system, even though every fact about it is fixed by the micro.

## Assumptions

- **Discrete, finite, time-invariant systems** of binary elements, each
  implementing a logical function of its inputs. The transition
  probability matrix (TPM) is known exactly. There are no data and no
  estimation.
- **Uniform interventions at each level.** The TPM is obtained by setting
  the system "into all possible n initial states with equal probability
  1/n", Pearl's do-operator applied to every state. At a macro level the
  uniform distribution is imposed on macro states, so each macro state's
  effect is the average over its micro realizers ("macro perturbation").
  This is the step that lets the macro win. The authors say so: the
  "modified distribution of micro perturbations … makes EI sensitive to
  the causal structure at each level, ultimately allowing the supervening
  macro EI to exceed the micro EI".
- **Admissible coarse-grainings.** The mapping must be exhaustive and
  disjoint over micro elements, and "no micro-level information is
  available at the macro level": a macro state may not depend on which
  micro element is in which state. So [00, 01, 10] = off, [11] = on is
  allowed, and [[00, 01], [10, 11]] is not.
- **Supervenience and exclusion are both accepted.** No causal ingredient
  is added at the macro level, and causation is counted at one level only.
- The search over coarse-grainings is exhaustive, done "with a
  custom-made Python program", and is said to be infeasible for real
  systems.

## Key results

- **Definitions.** For a current state s₀, cause information is
  D_KL(cause repertoire ‖ U_C) and effect information is
  D_KL(effect repertoire ‖ U_E). Both are bounded by log₂ n. EI(S) is the
  expected effect information over uniformly imposed states, which equals
  the mutual information between the intervention distribution and the
  resulting effects, MI(U_C; U_E).
- **Effectiveness.** Eff(S) = EI(S)/log₂ n, and Eff = ⟨determinism
  coefficient⟩ − ⟨degeneracy coefficient⟩. Determinism is 1 when each
  state leads to one future state with certainty and 0 when every future
  is equally likely. Degeneracy measures "deterministic convergence (not
  due to noise)" of different states onto the same future.
- **Causal emergence.** CE = EI(S_M) − EI(S_m), in bits. CE > 0 is
  emergence; CE < 0 at every macro level is causal reduction. The gain
  splits exactly as CE = ΔI_Eff + ΔI_Size, with ΔI_Eff = (Eff(S_M) −
  Eff(S_m))·log₂ n_M and ΔI_Size = Eff(S_m)·(log₂ n_M − log₂ n_m), which
  is always negative. Emergence requires ΔI_Eff > −ΔI_Size.
- **Four examples.**
  - Spatial, noise. Four noisy AND gates. EI(S_m) = 1.15 bits
    (Eff 0.29); grouping into two macro elements gives EI(S_M) = 1.55
    bits (Eff 0.78). CE = 0.40 bits, 91% of the effectiveness gain from
    determinism.
  - Spatial, degeneracy. Six deterministic AND gates wired for high
    degeneracy (degeneracy coefficient 0.6), EI(S_m) = 2.43 bits; three
    macro COPY gates give EI(S_M) = 3 bits, Eff 1. CE = 0.57 bits.
  - Temporal. Second-order Markov elements that answer a two-spike burst
    with a two-spike burst. One micro step: EI 0.16 bits; two micro steps:
    1.38 bits; one macro step over two micro steps: 2 bits, Eff 1.
    CE = 0.62 bits.
  - Spatiotemporal. Nine fully connected, heterogeneous, spontaneously
    active elements in three groups, read as "minicolumns" with states
    inhibited, receptive and bursting. EI(S_m) = 0.59 bits, EI(S_M) =
    3.51 bits, CE = 2.92 bits, from a rise in determinism that outweighs
    a slight rise in degeneracy.
- **Rules of thumb (Applicability).** If Eff(S_m) ≥ Eff(S_M), emergence
  is impossible. If EI(S_m) > log₂ n_M, reduction holds. A drastic rise in
  Eff under some coarse-graining makes emergence likely. Systems already
  near maximal effectiveness at the micro level reduce.
- **Interpretive claims (Discussion).** The EI-maximising level is called
  "an intrinsic property of the system". Exclusion is turned around: "to
  avoid double-counting causes, optimal macro causation must exclude
  micro causation". The maximal level is "optimal to characterize,
  predict, and retrodict the behavior of the system", and emergence is
  said to imply causal "self-definition" at that level.
- **Conclusions.** Brains are likely to work at a macro level
  because selection must cope with noise and produces degeneracy, and the
  hierarchy of the sciences "may not just be a matter of convenience".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | EI decomposes into effectiveness (determinism minus degeneracy) times log₂ of the state-space size | strong | derivation, with details in the SI (not read) |
| C2 | EI can be higher at a coarse-grained macro level than at the micro level it supervenes on | strong as an existence result | four exactly computed toy systems |
| C3 | The gain arises when coarse-graining raises determinism or lowers degeneracy more than the state space shrinks | strong | the exact decomposition CE = ΔI_Eff + ΔI_Size |
| C4 | The EI-maximising level is intrinsic to the system and is where its causal work is done | weak | argued, given the uniform intervention distribution, which is a choice the paper does not test |
| C5 | Macro causation, when it wins, excludes micro causation | weak | an application of Kim's exclusion principle to C4, not argued separately |
| C6 | Brains and other selected systems are likely to work at a macro level | speculative | an argument from noise and degeneracy in selected systems; no measurement |

## Concepts

- **Effective information (EI).** Mutual information between a uniform
  distribution of interventions over a system's states and the resulting
  next states. A property of the TPM, not of observed data.
- **Effectiveness (Eff).** EI divided by log₂ n; 1 for a deterministic,
  non-degenerate (reversible) system, 0 for a fully noisy or fully
  degenerate one.
- **Determinism.** How reliably a state leads to one future state.
- **Degeneracy.** How far different states deterministically lead to the
  same future state.
- **Macro perturbation.** Setting a macro state by setting each of its
  micro realizers with equal probability and averaging the effects.
- **Causal emergence (CE).** EI(S_M) − EI(S_m) at the optimal macro level;
  positive means the macro supersedes the micro.
- **Supervenience versus supersedence.** The macro is fixed by the micro
  (supervenience) but may carry more EI (supersedence).

## Connections

Built on Tononi & Sporns (2003) for EI, Pearl (2000) for interventions,
Tononi, Sporns & Edelman (1999) for degeneracy, and Kim (1993, 2000) for
the exclusion argument it turns around. It names channel capacity as the
parallel: both search over input distributions, but here the system is its
own channel and the distributions must come from admissible coarse-grainings.
It names Markov-chain lumpability and ε-machines as future work.

In the record, later work in the same line is Varley & Hoel ([LIT-027](../literature.d/LIT-027.md)),
which re-describes EI through a partial information decomposition, and
the ΦID account reviewed in [LIT-025](../literature.d/LIT-025.md), which cites this paper as a "not too
dissimilar" approach ([NOTE-010](NOTE-010.md)). Levin ([LIT-439](../literature.d/LIT-439.md), [NOTE-341](NOTE-341.md)) and Rizi
([NOTE-153](NOTE-153.md)) name it as the way to compare levels without using it.

## Bearing on the record

**On [QUESTION-093](../questions.d/QUESTION-093.md): an interventional criterion, met without closure or
self-individuation.**

- EI is defined by interventions, not by prediction from observed
  statistics. So CE > 0 is a measure of what the question calls
  interventional autonomy: higher-level variables that support more
  informative predictions about the effects of interventions. The paper
  does claim the EI-optimal level is also best "to characterize, predict,
  and retrodict", so it bundles predictive autonomy in, but only for
  predictions from imposed uniform states, not from the system's own
  history.
- None of the paper's systems maintains itself. They are logic gates with
  a fixed TPM. Positive CE therefore does not need organisational closure.
- The coarse-graining is chosen by an exhaustive search the analyst runs.
  The paper calls the optimum "intrinsic", meaning that the EI maximum is
  fixed by the TPM once the admissible mappings and the uniform
  intervention distribution are fixed. That is not self-individuation in
  [THEORY-071](../theory.d/THEORY-071.md)'s sense, where the system distinguishes itself from its
  environment. The paper's "self-definition" is a figure of speech for the
  EI maximum.
- So the paper is evidence that the first criteria can be had without the
  last two, which is half of what the question asks. It is not evidence
  about whether closure or self-individuation can be had without them.

**On the reification rule ([CLAIM-154](../claims.d/CLAIM-154.md)) and [QUESTION-040](../questions.d/QUESTION-040.md): the same shape of
trade-off, for a different question.**

- CE = ΔI_Eff + ΔI_Size has the form of [CLAIM-154](../claims.d/CLAIM-154.md)'s ½(d'² − Occam): a
  gain set against a size cost that is always paid. The resemblance stops
  there. [CLAIM-154](../claims.d/CLAIM-154.md) asks whether data justify keeping a candidate
  structure, and its cost is the information the data add about it. Hoel
  et al. assume the mechanism known exactly. Their cost is the loss of
  states under coarse-graining, and there is no prior, no posterior and no
  sample. The two can be combined: [CLAIM-154](../claims.d/CLAIM-154.md) decides whether a coarse
  block is supported by data, and CE says whether, granted the mechanism,
  the coarse description is the more effective causal model. Neither
  implies the other. This is a complement, not a rival and not a case.
- [QUESTION-040](../questions.d/QUESTION-040.md) asks how far searching for a candidate inflates its score.
  The paper searches all admissible coarse-grainings and reports the
  maximum. With an exact TPM there is nothing to inflate. With an
  estimated TPM, which every application to a real system would need, the
  maximum over many coarse-grainings would be biased upward, and the paper
  does not discuss it. The question applies to this measure unchanged.

**On proportional causation ([THEORY-133](../theory.d/THEORY-133.md)): a complement that supplies a
number.**

- List & Menzies ([LIT-722](../literature.d/LIT-722.md)) hold that a higher-level property excludes its
  realizer as a cause when the effect would survive a change of realizer.
  Hoel et al. accept Kim's exclusion principle and turn it around: when
  the macro wins, it "must exclude micro causation". Both reach downward
  exclusion system by system, not a priori.
- They reach it differently. List & Menzies use counterfactuals over
  nearest worlds; Hoel et al. average effects over all micro realizers of
  a macro state and compare information. Degeneracy reduction, one of the
  two routes to CE, is the information-theoretic face of realization
  insensitivity: many micro states lead to the same macro effect.
- Neither paper cites the other. The comparison is the record's.

**On the information-decomposition account ([LIT-025](../literature.d/LIT-025.md)): a different formal
object under the same name.** EI is interventional and uses a uniform
distribution imposed on the states; ΦID emergence is a property of a
supervenient variable's unique information about the future under the
system's own dynamics. One compares a macro model against a micro model;
the other asks what a macro feature predicts that no part does. [NOTE-010](NOTE-010.md)
already records the review's claim that the two are compatible. They can
disagree on a given system, and the record holds no case that tests them
together. No rivalry is declared, since the record holds no THEORY for
either.

*Note of 2026-10-16:* [THEORY-222](../theory.d/THEORY-222.md) now cites [LIT-1038](../literature.d/LIT-1038.md) as a source.

## Limitations

- **The intervention distribution carries the result.** Uniform
  interventions are imposed independently at each level, so the macro is
  scored under a different distribution of micro states than the micro.
  The paper presents this as what makes the comparison fair. Whether a
  different choice, such as the system's stationary distribution, would
  keep the macro ahead is not tested.
- **Toy systems only.** Four hand-built examples, each designed to show
  emergence (Fig. S1, a case of reduction, is in the unread SI). No real
  system is measured.
- **Exhaustive search.** Infeasible beyond a few elements, by the
  authors' own account. The rules of thumb are offered instead.
- **EI rewards determinism.** A system can raise EI by being reversible.
  Whether more EI means more causation, rather than more invertibility,
  is assumed.
- **"Intrinsic" depends on two choices**: the admissible mappings and the
  intervention distribution.
- **The claims about brains and the sciences** in the Conclusions are
  conjecture.

## Open questions

- Does the macro advantage survive when the intervention distribution is
  the system's own stationary distribution, or when the TPM is estimated
  from data with a correction for the search?
- On a system that also has closure, such as a protocell model, does the
  EI-optimal coarse-graining coincide with the boundary the organisation
  maintains? That would bear on whether [QUESTION-093](../questions.d/QUESTION-093.md)'s criteria
  converge.
- Do EI, the ΦID criteria and [CLAIM-154](../claims.d/CLAIM-154.md)'s rule pick the same level on one
  shared model?
