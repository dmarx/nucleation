---
number: 165
status: Read
formerly:
- NOTE-tmps1tct
paper: LIT-149
title: 'Martínez — information-processing view of representation'
version: 2
history:
- version: 2
  date: '2026-09-26'
  note: >-
    Read in full (full text, publisher's PDF (Philosophy and the Mind
    Sciences vol. 6, 2025, CC BY 4.0), 24 pp. — §§1–7, all six figures'
    captions, all footnotes (1–14) and the reference list; nothing
    skipped.). Upgraded from `Skimmed` to `Read`: the claims table,
    assumptions and results are new, and the skim is corrected where the
    full text disagreed.
date: '2026-09-26'
summary: >-
  A position paper, not an argument to a conclusion. It proposes that
  representations are signals adapted to transmit information for its own
  sake (Transmission), and that the evidence for this is efficiency in
  trading off rate, distortion and coder complexity (RDC Trade-Off). It
  supports the proposal by showing that cognitive scientists already
  attribute representational status on those grounds: compression, error
  protection, and explicitness understood as ease of decoding. It proves
  no theorem and reports no data of its own.
---

# NOTE-165: Martínez — information-processing view of representation

## Contribution

The paper sets out a framework for "representation" in cognitive science built on two theses (p. 1). **Transmission:** representations are, primarily, vehicles of information transmission for its own sake. **RDC Trade-Off:** representations aim at efficiently trading off (1) the rate of signals (transmission and storage costs), (2) the distortion of signals (faithfulness), and (3) the computational complexity of coders.

What is new is the empirical criterion that joins the two. Correlation or nonzero mutual information is cheap. What shows that something is *for* transmission is that it looks engineered for it: near-optimal compression, error protection, and low-complexity coders. The paper also names the resulting Pareto frontier the **representational surface** (p. 4).

## Key insight

Nonzero mutual information between two variables is a byproduct of almost any causal connection. Information flow that sits near a rate–distortion optimum, or coders near a complexity–distortion optimum, is "excellent evidence of design or adaptation for the transmission of information for its own sake" (p. 10). Representational status is therefore read off from efficiency, not from correlation.

## Assumptions

- **Main Model of cognition (p. 7).** Cognitive tasks are the transformation of a circumstance variable C into a behaviour variable B that minimises a distortion measure d: C × B → ℝ⁺. d is what ML and computational neuroscience call the loss, and what decision theory calls the utility function (p. 6). "Minimises" may be read as satisficing (fn. 5).
- **Shannon's point-to-point model (Figs. 1–2, p. 9).** A source emits a message M, it is encoded, it crosses a channel characterised by its capacity (the maximum mutual information between X and Y), and it is decoded into a destination variable M̂. Transmission explicitly includes processing and transformation (p. 2).
- **Teleofunctions fix the distortion measure (fn. 7, p. 11).** Without them, any system is efficient relative to some d. The account is avowedly teleosemantic.
- **An informal notion of complexity (p. 14).** Complexity rises with the number of free parameters, with nonlinearity, and with recurrence as opposed to feed-forward structure (Bassett et al. 2018). The paper states that classical complexity theory and Kolmogorov complexity are both unsuitable for practical use (fn. 9).
- **Scope.** The paper assumes that cognition is at least partly the production of adaptive behaviour, and that transmission is necessary but not sufficient for cognition (fn. 3). It considers evolved systems only; engineered systems are not treated.

## Key results

This is a position paper, so its results are theses supported by examples and by invoking standard theorems. It proves nothing new.

- **Lossy source coding (§4, p. 10).** The paper cites Shannon's rate–distortion function R(D) for the claim that lower expected distortion requires more rate, with a one-to-one optimal trade-off. Fig. 4 shows R(D) for a fair coin under Hamming distortion.
- **Source coding as a mark of representation (§4.1).**
  - Palmer et al. 2015: ganglion cells are credited with representing the future because they compress the past efficiently for predicting it.
  - Rosch's "cognitive economy" principle is read as a source-coding goal. That prototype theory corresponds to optimal compression of highly correlated stimuli is cited to Martínez 2024.
  - Further examples are listed without discussion: the efficient-coding hypothesis, predictive coding, Kirby's compressibility of languages, and Gibson et al. 2019.
- **Channel coding as vehicle realism (§4.2).** Error correction surrounds each code word with a "safety bubble" of unused values. It is a syntactic, not a semantic, operation. The paper proposes that representational vehicles (Shea 2018) are channel-coding safety bubbles. Examples are sparse coding (Perez-Orive et al. 2002) and synchronised assemblies (Buzsáki 2010).
- **Complexity management as explicitness (§5).**
  - In neuroscience, "explicit" representation means decodable in one step, or linearly decodable (Kriegeskorte & Diedrichsen 2019; Hong et al. 2016). Marr's decimal/binary example is read the same way.
  - By the data-processing inequality, information about a car/no-car decision can only fall from the retina to IT. A mutual-information heuristic would therefore locate the decision at the earliest stage, which is wrong.
  - The paper reads the ventral stream as trading rising distortion for falling decoder complexity until the decision is linearly decodable (pp. 16–17).
- **The representational surface (§6).** Classical and 4E cognitive science are recast as disagreeing about the *shape* of the surface. On the 4E view complexity "saturates" early and distortion is dominated by rate (Fig. 6). Which shape holds is "a thoroughly empirical question" about multiobjective optimisation (p. 19).
- **Mapping to representational properties (§7).** Noise protection corresponds to vehicles, compression to cognitive economy, and complexity management to explicitness. MDL codes "sit on the representational surface", but MDL is lossless and "no mechanical" way to find the best model exists. The Free Energy Principle is described as compatible with the framework but going beyond it.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Representations are primarily signals adapted for information transmission for its own sake | weak | informal argument plus illustrative examples (§§1, 4, 5); defended elsewhere (Martínez 2019b, 2024) by the author's own admission (p. 5) |
| C2 | Transmission that operates near an R(D) optimum is excellent evidence of adaptation for transmission | moderate | Shannon's lossy source coding theorem plus an inference to best explanation (p. 10); the inference is not defended against alternatives |
| C3 | Cognitive scientists already attribute representational status on grounds of compression, error protection and ease of decoding | moderate | a survey of cited practice (Palmer 2015, Rosch, Barlow, Perez-Orive, Buzsáki, DiCarlo, Kriegeskorte) (§§4–5); the examples are selected, not systematically sampled |
| C4 | A mutual-information heuristic mislocates the car/no-car decision in the ventral stream | strong | the data-processing inequality (pp. 16–17) |
| C5 | Representational vehicles are channel-coding safety bubbles | weak | conceptual proposal (p. 13) with two neural examples |
| C6 | The classical-vs-4E debate is a disagreement about the shape of the representational surface | weak | reinterpretation of Chemero 2011, ch. 6 (§6); fn. 14 concedes that part of it is terminological |
| C7 | Without teleofunctions, any system is RD-efficient relative to some distortion measure | moderate | informal argument (fn. 7), attributed to a reviewer |
| C8 | The kinds of properties cognitive scientists associate with paradigmatic representations are generated by RDC adaptations (abstract) | weak | three mappings in §7; the abstract states as a finding what the body offers as a framework, and the paper says other connections are "matter for another time" |

## Method

Conceptual analysis. Standard information-theoretic results (lossy source coding, channel capacity, the data-processing inequality) are paired with case studies of how cognitive scientists and neuroscientists justify calling states representations. There is no formal model of the surface beyond the idealised Figs. 5–6, and no new data.

## Concepts

- **Transmission for its own sake** — having adaptations (compression, error protection, complexity management) that further the transmission of information "to a significant extent independently from whatever that information is about" (p. 2). This is stronger than Dretskean correlation.
- **Distortion measure d** — a score over (circumstance, behaviour) pairs; lower is better. It is the same object as the loss or the utility.
- **Rate** — the expected number of bits the encoder uses per source value, or the richness of the signal repertoire. It is "dynamic" economy.
- **Complexity** — the computational cost of the coders. It is "static" economy, estimated heuristically.
- **Coder / codec** — coder covers both encoders and decoders; a codec is an encoder–decoder pair (fn. 2).
- **Representational surface** — the Pareto frontier of jointly minimising rate, distortion and complexity: a 2-D surface in the 3-D budget space.
- **Explicit representation** — information that a simple (typically linear, single-step) decoder can extract.
- **Safety bubble** — the set of unused channel inputs around each code word that error correction reserves.

## Connections

The paper places itself against the correlational, Dretskean use of information in philosophy of mind (Dretske 1981/1988, Neander 2017, Skyrms 2010, Shea 2018). It sides with Mann 2023 in finding Shannon theory relevant to semantics, and with teleosemantics (fn. 7). It extends the author's own "Representations are rate-distortion sweet spots" (2019b) by adding the complexity budget. It engages 4E and ecological cognition (Chemero, Wilson & Golonka) by reinterpreting it rather than rejecting it.

**Account of mind held.** A representationalist, information-processing account of cognition. Representations are teleofunctional signals within a Shannon-style source–coder–channel–decoder architecture that maps circumstances to behaviour under a task loss. It is naturalistic and teleosemantic about content, and it is neutral on phenomenal matters. The **cognition** tag is plainly justified: this is a theory of mental representation and of how cognitive science should attribute it.

In the nucleation record it sits beside [LIT-220](../literature.d/LIT-220.md) (Dennett, "Real Patterns") and [LIT-005](../literature.d/LIT-005.md) (Bourrat, on the information-theoretic perspective on individuality) as information-theoretic philosophy. It has no direct citation link to either.

## Bearing on the record

This is philosophy of cognitive science. It carries no instruction for ML practice. It has a real conceptual kinship with the information-bottleneck line of deep-learning theory held in the anthology, [ANTH-LIT-531](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-531.md) (Tishby & Zaslavsky), [ANTH-LIT-508](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-508.md) and [ANTH-LIT-509](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-509.md). On that kinship, linear decodability (probing) is an explicitness criterion, and representation learning is an RDC trade-off. The paper does not draw that connection itself, and nothing in it tests or informs a training practice. Should a THEORY document in the anthology ever argue that "linearly probeable = represented", this paper's §5 and footnote 13 (citing Ritchie et al. 2020 against inferring representation from decodability) would be relevant on both sides.

## Limitations

- By its own account a position paper, "comparatively light" on objections and on critiques of rival accounts (p. 5).
- Complexity has no operational measure (fn. 9). The complexity leg, and so the surface, cannot currently be computed for any real system.
- Misrepresentation, content determination (what a given representation is *about*), and the status of engineered systems are not addressed. Footnote 7 hands content-fixing to teleofunctions without developing that.
- The examples are chosen to fit the thesis. There is no attempt to find paradigm representations that are not RDC-efficient, or RDC-efficient systems that nobody would call representational.
- The abstract's claim that representational properties "are generated by" RDC adaptations (C8) outruns three illustrative mappings.

## Open questions

- Can a usable complexity measure be supplied so that a representational surface can actually be estimated for some neural or artificial system? That would turn §6 into a test.
- Does the criterion classify engineered, efficiently coded signals (a JPEG pipeline, a trained autoencoder's latent code) as representations? If not, what excludes them besides teleofunction?
- Where on the surface do concepts sit relative to percepts? The paper conjectures they are lower in both rate and complexity (p. 21) but does not test it.

## Corrections to the seeded skim

- The dossier says the Transmission thesis is "explicitly stronger than the Dretskean claim". That is right, but the full text adds a commitment the skim missed. Footnote 7 (p. 11) makes the account "a version of teleosemantics". Without teleofunctions, distortion becomes a free parameter, and "any information processing system can be seen as rate-distortion efficient … with respect to some … distortion function". This is the paper's only answer to the question the dossier asks, how it avoids counting every efficiently coded engineered signal. It does not discuss misrepresentation anywhere.
- The dossier asks whether Martínez discusses learned networks directly. He does not. Bengio et al. 2013 appears once (p. 12), in a list of illustrations "presented without discussion". The only other ML contact is that the distortion measure d is what ML calls the loss (p. 6), and that linear decodability serves as the criterion of explicitness (p. 15).
- The dossier says §4–5 should say what empirical signatures count as adaptations. The signatures are qualitative: operating near an R(D) optimum (p. 10), and having coders near a complexity–distortion optimum, the "best prima facie explanation" of which is adaptation (p. 15). The paper admits (p. 14, fn. 9) that it has no workable formal measure of complexity. It falls back on heuristics (free parameters, nonlinearity, recurrence) and gives no test that could be run.
- The dossier places "no system can enrich the source" in §5. The argument there is the data-processing inequality, applied to the ventral stream (pp. 16–17). Its use against 4E "cognitive enrichment" comes in §6 (pp. 18–19), and footnote 14 concedes that the point is "to a large extent terminological".
- The representational surface is presented as the 2-D Pareto frontier in rate × distortion × complexity space, first in §1 (p. 4) and again in §6. It is not introduced only in §6.
- The Transmission thesis says representations are *primarily* signals. The skim missed the qualifier. Structural representations (cognitive maps, memories, generative models) are subordinated to it as parts of or identical with the coders (p. 17).
- cognition tag: justified. This is a theory of mental representation in cognitive science.
- tags: neuroscience would be justifiably appropriate as an additional (non-primary) tag. Most of the evidence is neural: retinal ganglion cells, sparse coding in the mushroom body, synchronised assemblies, and the ventral stream from V1 to IT and V4 colour.
