---
number: 235
status: Read
formerly:
- NOTE-tmp01mls
paper: LIT-264
title: 'Dzhafarov, Zhang & Kujala, contextuality in behaviour'
version: 2
history:
- version: 2
  date: '2026-10-09'
  note: >-
    Read in full from the arXiv v5 PDF (23 August 2015, 23 pp., including
    supplementary files S1–S3; comment: "text with supplementary files is
    not the journal's format"), text extracted with pdftotext. Read: the
    abstract, §§1–8, the acknowledgments, the references, the S1 table (73
    question-order pairs), the S2 table (23 word combinations) and S3 (the
    psychophysical experiments). The rank-2 worked examples of §3 were
    recomputed from Wang & Busemeyer's Table 1 proportions, all 23 S2 ΔC
    values from their components, and the pooled χ² from S1. The figures
    were read from their captions. Eq. 7 is quoted from refs. [14, 16,
    17]; its proof is not in this paper and was not read. The typeset
    Royal Society version was not compared. Upgraded from `Skimmed` to
    `Read`: assumptions, results and the claims table are new, and the
    skim is corrected where the full text and the tables disagree with it.
date: '2026-09-27'
summary: >-
  Under Contextuality-by-Default, which separates context-dependent
  marginals ("inconsistent connectedness") from contextuality, no
  behavioural or social data set re-analysed is contextual: 73 poll
  question-order pairs, Schröder staircases, conjoint choices, 23 primed
  word combinations and psychophysical matching. The quantum question
  model's QQ equality implies noncontextuality, so a quantum model here
  predicts its absence. The worked Rose–Jackson example mislabels two
  marginals; its conclusion stands.
---

<!-- inactive-ok-file: THEORY-013 — Proposed; this reading is its source and bears on it without settling its promote_when -->
<!-- inactive-ok-file: THEORY-tmp9wyar — Proposed; this reading is one of its sources -->
<!-- inactive-ok-file: LIT-263 — Deferred: filed and skimmed on 2026-09-27 while bringing the contextuality threads together -->

# NOTE-235: Dzhafarov, Zhang & Kujala, contextuality in behaviour

## Contribution

Behavioural "contextuality" had been claimed from order effects, priming
and violations of CHSH-type inequalities computed as if each measurement
had one distribution in every context. The paper applies a criterion that
holds when distributions do vary with context, the Contextuality-by-Default
cyclic-system criterion, to five kinds of behavioural data, two of them
previously published as contextual. None is contextual. It also shows that
the quantum question-order model predicts the absence of contextuality.

## Key insight

Two things are called "context effects" and only one of them is
contextuality. An answer's distribution depending on what came before is
inconsistent connectedness: ordinary, ubiquitous and, in the authors'
words, "a trivial sense of contextuality". Contextuality is the further
fact that no joint model can make each question's answers across contexts
as similar as their own distributions allow. Behavioural data have
plenty of the first and, so far, none of the second.

## Assumptions

- **Binary measurements**, ±1, arranged as a cyclic system: each object
  is measured in exactly two contexts, and successive objects form the
  contexts (§2).
- **Bunches from different contexts are stochastically unrelated**. A
  coupling imposes a joint distribution on them. Noncontextuality is the
  existence of a coupling in which each connection attains its own
  maximal coincidence probability.
- **Participants as replicants** in §§3–6: probabilities are proportions
  across people, between-subjects (§§3–4) or within-subjects (§§5–6).
  §7 uses repeated trials from very few participants.
- **The criterion is quoted**: Eq. 7 is proved in refs. [14, 16, 17].

## Key results

- **Eq. 7**: noncontextual iff ΔC = s₁(⟨V₁W₂⟩, …, ⟨VₙW₁⟩) − (n − 2) −
  Σᵢ|⟨Vᵢ⟩ − ⟨Wᵢ⟩| ≤ 0, s₁ being the maximum over sign patterns with an
  odd number of minuses. For consistent marginals and n = 3, 4, 5 this is
  Suppes–Zanotti–Leggett–Garg, CHSH and (with a constraint) KCBS.
- **Rank 2, question order** (Eq. 10): ΔC = |⟨V₁W₂⟩ − ⟨V₂W₁⟩| −
  (|⟨V₁⟩ − ⟨W₁⟩| + |⟨V₂⟩ − ⟨W₂⟩|). The white–black poll gives ΔC = −0.406;
  I reproduced this from Wang & Busemeyer's Table 1.
- **The QQ equality from the model** (§3): for projectors P, Q,
  (1 + ⟨V₁W₂⟩)/2 = ⟨(P Q P + (I − P)(I − Q)(I − P))ψ|ψ⟩, and
  P Q P + (I − P)(I − Q)(I − P) = I − (P + Q) + (P Q + Q P) is symmetric
  in P and Q, so ⟨V₁W₂⟩ = ⟨V₂W₁⟩ for any state. The empirical equality
  then needs the same mixture of states in the two groups. QQ ⇒ ΔC ≤ 0.
- **S1**: 73 pairs (66 Pew, four Gallup from Moore, three others). ΔC > 0
  in six Pew pairs, all ≤ 0.063. In five the QQ equality survives
  (p 0.06–0.47); in the sixth p = 0.008 and ΔC = 0.063, discounted for
  multiplicity (P(at least one rejection at 0.01 in 73) ≈ 0.52). Pooled
  χ² for QQ over the 72 non-Rose–Jackson pairs: the text says p > 0.35;
  the S1 values sum to 76.04 on 72 df, p ≈ 0.350.
- **Rose–Jackson** violates QQ (p < 10⁻⁷) yet is noncontextual: QQ is
  sufficient, not necessary.
- **§4**, Schröder staircases (Asano et al.), rank 3: ΔC = −1.233.
- **§5**, animals and sounds (Aerts, Gabora & Sozzo), rank 4: ΔC = −3.357.
  The published CHSH violation (s₁ − 2 > 0) presupposes consistent
  connectedness, which the data violate.
- **§6**, Bruza et al.'s primed ambiguous word pairs, rank 4: all 23 ΔC
  negative, −2.882 to −0.418 ("apple chip" −1.640). I recomputed all 23
  from S2's s₁ and marginal differences; they agree. Bruza et al.'s
  "compositionality" is, in these terms, consistent connectedness plus
  noncontextuality.
- **§7 and S3**, psychophysical matching, seven experiments: between 3,024
  and 11,663,568 dichotomisations per 2 × 2 design, and not one positive
  ΔC.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | A binary cyclic system is noncontextual iff ΔC ≤ 0 | strong, but proved elsewhere | Eq. 7, refs. [14, 16, 17] |
| C2 | The QQ equality implies noncontextuality for question-order systems | strong (proof) | §3 |
| C3 | Question-order data (73 pairs) show no contextuality | strong for these data | §3, S1 |
| C4 | The CHSH violation reported for conjoint choices is an artefact of assuming equal marginals | strong | §5 |
| C5 | Primed word combinations and psychophysical matching show no contextuality | strong for these data | §§6–7, S2, S3 |
| C6 | Behavioural and social systems are noncontextual in general | weak: a working hypothesis from five paradigms | §8 |

## Concepts

- **bunch**: the measurements recorded jointly in one context.
- **connection**: the measurements of one object across contexts.
- **consistent connectedness**: every connection's measurements have the
  same distribution (marginal selectivity). Inconsistent connectedness is
  its failure, and the paper's name for most "context effects".
- **contextuality (CbD)**: no coupling of the bunches attains, on every
  connection, that connection's own maximal coincidence probability.
- **cyclic system of rank n**: n objects, n contexts, each object in two
  consecutive contexts.

## Connections

The question-order data and model are Wang & Busemeyer's ([LIT-tmptn5dr](../literature.d/LIT-tmptn5dr.md))
and Wang, Solloway, Shiffrin & Busemeyer's ([LIT-tmp56yt5](../literature.d/LIT-tmp56yt5.md)); the data were
supplied by the authors. The general theory is Contextuality-by-Default
([LIT-777](../literature.d/LIT-777.md) in this record, read 2026-10-09). The same criterion applied to
physics is reviewed in [LIT-263](../literature.d/LIT-263.md).

## Bearing on the record

- **[THEORY-013](../theory.d/THEORY-013.md) is sourced here**, and the full reading supports what it
  states. Two refinements. First, its "73 poll question-order pairs"
  includes three non-poll studies (S1 rows 70–72; two are laboratory
  experiments). Second, "apart from one poll pair the authors discount
  for multiple comparisons" is right: that pair is a Pew pair with
  ΔC = 0.063. Its first promote_when condition, a close reading of the
  proof of the criterion, is not met by this reading: the proof is not in
  this paper.
- **[THEORY-tmp9wyar](../theory.d/THEORY-tmp9wyar.md)** takes from this paper the re-derivation of the QQ
  equality and its implication of noncontextuality.
- **Corrections to the skim of 2026-09-27.** The skim said "72 of 73
  pairs fit the QQ equality". The paper says so, but by its own S1
  flags the QQ equality is rejected at 0.05 for two pairs besides
  Rose–Jackson (a Pew pair at p = 0.008 and one of the three non-Gallup,
  non-Pew studies at χ² = 5.48, p ≈ 0.02). That is about what 72 tests
  produce by chance, and the pooled test holds.
- **An error in §3, not affecting the conclusion.** The Rose–Jackson
  diagram swaps ⟨W₁⟩ and ⟨V₂⟩, and the two product expectations, against
  the variable definitions of Eq. 9. Recomputed from Wang & Busemeyer's
  Table 1: ⟨V₁⟩ = .324, ⟨W₂⟩ = −.289, ⟨V₂⟩ = −.035, ⟨W₁⟩ = .078,
  ⟨V₁W₂⟩ = .316, ⟨V₂W₁⟩ = .619, so ΔC = −0.197, not −0.422. S1's row for
  the same pair lists different marginals again and ΔC = −0.851. All
  three are negative, so the pair is noncontextual on any reading.
- No instruction for machine-learning practice; nothing for the
  anthology.

## Limitations

- The criterion's proof is cited, not given.
- Five paradigms, mostly re-analyses of others' data; the general
  conclusion is offered as a working hypothesis.
- §§3–4 compare different groups of people across contexts, so the
  "random variables" are population proportions, not one system measured
  repeatedly.
- Only cyclic systems with binary outcomes are treated.

## Open questions

- Is there any behavioural paradigm with ΔC robustly above zero? Later
  Contextuality-by-Default work (e.g. Cervantes & Dzhafarov 2018) is
  reported to find one; not held or read here.
- Where does the Rose–Jackson row of S1 come from? It matches neither
  the §3 diagram nor the published proportions.
