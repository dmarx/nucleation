---
number: 106
status: Read
formerly:
- NOTE-tmp822h0
paper: LIT-153
title: 'Angius et al. — Making sense of transformer success'
version: 2
history:
- version: 2
  date: '2026-09-26'
  note: >-
    Read in full (full text of the open-access Frontiers HTML (Frontiers in
    AI vol. 8, 2025, article 1509338, CC BY), read end to end: abstract,
    §§1–7, footnotes 1–4, and statements. The displayed equations (Eqs.
    1–12: word-embedding arithmetic, the attention computation, the OV/QK
    circuits, the composition scores, the sparse-autoencoder objective, the
    brain-score correlation) did not survive text extraction; their
    surrounding prose was read. The reference list was skimmed rather than
    read.). Upgraded from `Skimmed` to `Read`: the claims table, assumptions
    and results are new, and the skim is corrected where the full text
    disagreed.
date: '2026-09-26'
summary: >-
  Current attempts to explain transformer language models' competence fall
  into three kinds, and the paper maps each onto an explanatory form from
  philosophy of cognitive science: machine psychology is Cummins-style
  functional analysis, induction-head work is Machamer–Darden–Craver
  mechanistic explanation, and NLM–fMRI brain-score studies are a
  bidirectional "co-simulation". Its only thesis is that these do not
  differ from how cognitive science explains humans. Functional analyses
  are to be reduced to mechanisms as "mechanism sketches". The paper rests
  on existing literature and adds no new analysis or data.
---

# NOTE-106: Angius et al. — Making sense of transformer success

## Contribution

The paper recasts the question in philosophy of AI from "can machines think?" to "how can machines think?". It then classifies existing explanations of NLM competence by explanatory form:

- functional analysis (§4);
- mechanistic explanation (§5);
- simulative explanation, which it calls **co-simulation** (§6).

It argues that these are the same forms cognitive science uses for humans. It adds the claim that NLM–brain comparisons invert the traditional synthetic method: the brain is used to understand the artificial system as well as the reverse.

## Key insight

The "explanatory gap" for NLMs is not a new kind of problem. It is a question about how a simple architecture produces behaviour, answered by decomposing capacities into sub-functions and then filling those sub-functions with mechanisms. Where both the model and the brain are opaque, each is used as a simulation of the other.

## Assumptions

- **Premise (asserted, §3):** NLMs have empirically passed the imitation game. The metaphysical question of whether machines can think can be bracketed in favour of a posteriori possibility.
- **Authorities on explanation:**
  - Cummins 1975/1983 on functional analysis;
  - Machamer, Darden & Craver 2000 and Craver 2016 on mechanisms and levels;
  - Piccinini & Craver 2011 on functional explanations as mechanism sketches;
  - Woodward 2003 on interventionism;
  - Winsberg, Durán and Primiero on simulation, verification and validation;
  - Newell & Simon 1972 for the synthetic method.
- **Scope:** decoder- and encoder-style transformer NLMs (GPT-2/3/3.5/4, BERT, FLAN-T5). Mechanistic evidence comes from attention-only toy models of one and two layers (Elhage et al. 2021) and from Bietti et al.'s further simplifications.

## Key results

This is an argumentative and survey paper. What it argues, with the evidence it reports from others:

- **§4, functional analysis.** Machine-psychology studies decompose linguistic competence into sub-capacities. Three are examined:
  - ToM: Kosinski 2023 as reported, GPT-3.5 at about a 3-year-old's level and GPT-4 at about a 7-year-old's, with no ToM below 100B parameters.
  - Discourse-entity tracking: Kim & Schuster 2023 as reported, GPT-3.5 accuracy falling from more than 90% after one operation to "more than 25%" after seven.
  - Property induction: Han et al. 2024 as reported, GPT-4 humanlike except on non-monotonicity.

  This decomposition is Cummins-style functional analysis. By Cummins's own standard it is incomplete until each sub-function has a causal role filler, which NLM opacity blocks.
- **§5, mechanisms.**
  - The paper sorts interpretability tools into four kinds: circuit discovery (ACDC), localisation (sparse probing), visualisation (AttentionViz), and conversion (RASP, Transformer Programs).
  - It judges most ICL "mechanism" work to be mathematical equivalence rather than mechanism.
  - In Elhage et al. 2021, the one-layer copying algorithm and the two-layer induction head (built from prefix matching via K-composition) count as a multi-level mechanism in Craver's sense.
  - Olsson et al.'s co-occurrence evidence and smeared-key intervention are read as Woodwardian interventionism.
  - ICL is treated as a mechanism sketch.
  - Sparse autoencoders sit between functional and mechanistic analysis.
- **§6, co-simulation.** Brain-score studies (Caucheteux & King 2022; Caucheteux et al. 2022, 2023; Kumar et al. 2023) are reported as follows:
  - middle GPT-2 layers score highest;
  - brain score correlates with subjects' comprehension;
  - adding long-range (up to 10-word, peak at 8) predictions raises scores;
  - the layer–cortex hierarchies align;
  - similarity scales logarithmically from 125M to 30B parameters (Antonello et al. 2023).

  Because the metric is symmetric, and cortical hierarchy is used to hypothesise model structure, the paper calls the practice reciprocal co-simulation. It departs from the classic synthetic method because NLMs were not built to implement hypothesised brain mechanisms.
- **§7, conclusion.** Success came from "more elegant mathematics", not brain mimicry. There is "no mystery about what a Transformer does" but there is opacity about how particular outputs arise. NLMs are "typical creatures of cognitive science" yet a different kind of intelligence.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Explanations of NLMs use the same explanatory forms as cognitive science uses for humans | moderate | informal argument that maps published studies onto Cummins, Machamer–Darden–Craver and the synthetic method (§§4–6); no counter-cases considered |
| C2 | Machine psychology amounts to (possibly failing) functional analysis | moderate | conceptual mapping (§4) |
| C3 | Induction heads provide a mechanistic explanation of in-context learning | weak | the abstract states it; the body calls the link "speculated" and rests it on Olsson et al. 2022's evidence as reported (§5) |
| C4 | Functional explanations of NLMs are mechanism sketches, reducible to mechanisms | weak | endorsement of Piccinini & Craver 2011 (§5), not argued for NLMs specifically |
| C5 | NLM–brain studies are a co-simulation in which each system models the other | weak | the symmetry of the brain-score formula, plus a reading of Caucheteux et al. (§6); the directional claim that the cortex is used as a model of the NLM rests on one study series |
| C6 | Passing the imitation game is empirically established | assertion | BIG-bench and Jannai et al. 2023 cited (§3) |
| C7 | Most ICL-mechanism papers give mathematical equivalences, not mechanisms | moderate | brief critical survey (§5) |
| C8 | Transformer success came from mathematics, not brain inspiration | assertion | §7, with the historical sketch of §2 |

## Method

*(Omitted: philosophical analysis of published literature. The paper has no method of its own.)*

## Concepts

- **Explanatory gap (for NLMs)** — the distance between the known, simple algorithmic components and the linguistic competence they produce.
- **"Can comes first" objection** — that one must settle whether machines think before asking how they do. It is bracketed by a posteriori possibility.
- **Functional analysis** (Cummins) — explaining a capacity by sub-capacities of components and their organisation. It halts at an explanatory level or at mechanism.
- **Mechanism sketch / schema** (Machamer et al.) — a mechanism description with unfilled or abstract parts.
- **Co-simulation** — the authors' term (from Angius et al. 2024) for mutual use of NLM and brain as simulative models of each other, grounded in the symmetry of the brain score.
- **Brain score** — the mean Pearson correlation between a neuroid's actual response and a linear prediction of it from the other system's activations (Schrimpf et al.).

## Connections

The paper builds on Cummins, Machamer–Darden–Craver and Piccinini & Craver for explanation, and on Winsberg and Primiero for simulation. The ML results it takes over are Elhage et al. 2021, Olsson et al. 2022, Bietti et al. 2023, the sparse-autoencoder and dictionary-learning line (Bricken et al. 2023; Templeton et al. 2024), and the Caucheteux/King brain-alignment programme.

**Account of mind held.** A computationalist, functionalist account. Cognition is computation over quantitatively represented information (§7). Minds are "a consistent set of computational architectures", of which human and machine minds are variants (§3). Intelligence is multiply realisable, like flight across birds and aircraft. The authors decline to settle whether NLMs "really" think, but they take their competence as genuine for the argument. The **cognition** tag is justified: the paper is about explaining cognitive capacities, and the explanatory forms it analyses are those of cognitive science.

In the nucleation record it pairs naturally with [LIT-148](../literature.d/LIT-148.md) (López-Rubio, computational functionalism for deep learning) and [LIT-131](../literature.d/LIT-131.md) (Freeborn, a model of understanding in deep-learning systems). On the ML side, [ANTH-LIT-533](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-533.md) (von Oswald et al., "Transformers learn in-context by gradient descent") is cited in §5. It belongs to the family of ICL results the paper calls mathematical descriptions rather than mechanisms.

## Bearing on the record

This is philosophy of science about interpretability. It carries no instruction for ML practice. It could inform how the anthology classifies interpretability evidence, by distinguishing behavioural evals (functional analysis), circuit and intervention work (mechanism) and brain alignment (similarity or co-simulation). The criticism in §5, that ICL "mechanism" papers often provide equivalence results rather than mechanisms, is a fair caution for any anthology THEORY that cites such a result as *the* mechanism of in-context learning. The paper does not argue this with any rigour, however, and should not be a source for such a document; the primary papers are the sources. It does not belong in the anthology.

## Limitations

- It adds no new analysis. All empirical content is reported from others, sometimes loosely (C3, the Kosinski thresholds, the GPT-4 parameter figure).
- The §2 primer misdescribes transformer training as autoencoding, reproducing the input.
- Co-simulation is argued from the formal symmetry of a correlation metric. In the studies described, the metric is used directionally (model → brain encoding), so the symmetry is thinner than claimed.
- Whether behavioural psychological tests validly transfer to NLMs is explicitly set aside (§4), yet the functional-analysis reading depends on those tests measuring the named sub-functions.
- No counterexample or alternative taxonomy is considered. The thesis that NLM explanation "does not differ" from human-cognition explanation is established by assimilation, not by testing for differences.

## Open questions

- Would an interventionist NLM–brain study, which the paper notes does not yet exist, turn co-simulation into explanation?
- Can the functional-to-mechanistic reduction be completed for any linguistic sub-capacity beyond induction-head copying in toy models? That would test C4.
- Do the sub-functions probed by machine psychology (ToM tasks) correspond to any identifiable circuits at all? If not, the Cummins-style analysis may be decomposing along the wrong joints.

## Corrections to the seeded skim

- The dossier asks whether any strategy is privileged. The full text does privilege one, which the skim missed. §5 (end) endorses Piccinini & Craver 2011: functional explanations are "mechanism sketches", to be reduced to full mechanisms by supplying the bottoming-out causal role fillers. Cummins's own demand that each sub-function be tied to a component (§4) is what makes functional analysis alone insufficient for NLMs. The paper's position is therefore a reductive functional-to-mechanistic hierarchy, not three parallel strategies.
- The dossier says co-simulation "answers the worry" about prediction versus explanation. It does not. Co-simulation is defined (§6) through the "perfect symmetry" of the brain-score formula (Pearson r between a target neuroid and a linear prediction from a source neuroid). The paper claims that Caucheteux et al. use cortical hierarchy to generate hypotheses about the layer organisation of GPT-2, "the cortex is used as a model of the NLM". It never addresses whether correlation is explanatory. It says only that such similarity "may–at least in part–justify" transformer success, and notes that no interventionist NLM–brain studies exist.
- The skim casts §3 as "the Turing test no longer seems a real obstacle". The paper goes further. It asserts that "the passing of Turing's Imitation Game can now be considered empirically established" and brackets the "can comes first" objection by appeal to a posteriori possibility (ab esse ad posse). That is an assumption, not a finding.
- The skim omits §5's criticism that most in-context-learning "mechanism" papers give mathematical equivalences (sparse linear regression, ridge, Bayesian model averaging) "rather than mechanisms in the proper sense".
- The skim also omits that §5 treats sparse autoencoders as "halfway between functional and mechanistic analysis".
- The skim also omits that the abstract's "shown to provide a mechanist explanation of in-context learning" is softened in the body. There the induction-head→ICL link is "speculated", supported by Olsson et al.'s co-occurrence and smeared-key evidence, and ICL is treated as a mechanism sketch.
- The Transformer primer in §2 contains an error that the dossier did not note. It says the Transformer bypasses supervised learning through the autoencoder concept, "the task assigned to the ANN is to reproduce its own input". Next-token prediction in decoder-only NLMs is not input reconstruction, and the original Transformer was trained on supervised translation.
- Some figures in §4 are unverified. "GPT-4 with over 1 trillion parameters" is an undisclosed, unverified figure. The ToM-by-scale thresholds are reported from Kosinski 2023 without their subsequent contestation, beyond a list of citations.
- The sparse-autoencoder work is cited as "Huben et al. (2023)". Whether that is the right first author for the SAE paper is unverified.
- cognition tag: justified. The paper applies explanation in cognitive science (functional analysis, mechanism, simulative method) to machine cognitive capacities (ToM, entity tracking, property induction), and presupposes the computational theory of mind.
- tags: neuroscience would be justifiably appropriate (§6 is entirely about fMRI brain-score studies). linguistics is weak under its blurb ("not as models encode them"). The paper is about how models attain linguistic competence, not about language as linguists pose it. Primary topic philosophy-of-science is right.
