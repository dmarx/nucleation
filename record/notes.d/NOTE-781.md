---
number: 781
status: Read
formerly:
- NOTE-tmpe5owc
paper: LIT-977
title: 'Torii, Maeda and Hidaka — Distributional hypothesis as isomorphism'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the publisher's open-access PDF (CC BY), fetched
    from journals.plos.org (article/file?id=10.1371/journal.pone.0312151
    &type=printable) and extracted with pdftotext: all 25 pages, §§1–7
    with Theorem 1 and its proof, and the S1 Appendix (one page, fetched
    from the article's supplementary file s001). The matrices of the
    proof (Eqs. 8, 10, 12, 13, 16) came through the extraction scrambled.
    The necessity step below was checked by the reader's own argument
    rather than read off them. Figures 1–8 were read through their
    captions and the text.
date: '2026-10-14'
summary: >-
  An SVD of log raw co-occurrence counts solves 61% of Google analogies
  over a 1,487-word vocabulary, against 75% for full word2vec. In a
  24-sentence toy corpus whose eight subjects carry every combination of
  three binary aspects, the subjects' raw co-occurrence rows form a
  parallelepiped exactly when, for each object, its four sentences are
  equally probable. The attributes are independent, so the concept
  lattice is Boolean.
---
<!-- inactive-ok-file: THEORY-185 THEORY-183 THEORY-271 — Proposed; the accounts this reading bears on, and the one filed from it -->

# NOTE-781: Torii, Maeda and Hidaka — Distributional hypothesis as isomorphism

## Contribution

The paper argues that analogy parallelograms are in the co-occurrence
data, not made by word2vec's training. It gives two kinds of evidence.
On Wikipedia, linear decompositions of log co-occurrence counts solve
the Google analogy set about as well as word2vec on the same restricted
vocabulary, and without negative sampling. In a toy corpus, it proves a
necessary and sufficient condition on sentence probabilities for raw
co-occurrence rows to form a parallelepiped. The condition is a local
uniformity, which the authors call "local unigram".

## Key insight

In the toy corpus each sentence expresses one aspect of its subject, so
a subject's co-occurrence row is a *sum* of one contribution per aspect.
If, for each object, the probability is the same across the subjects
that take it, each contribution depends only on the aspect's value.
The rows are then affine in the subject's ±1 aspect vector, which is
what a parallelepiped is. Any departure from that uniformity puts a
subject-specific term in a column, and the shape breaks.

## Assumptions

- **Real-text analysis (§3).**
  - English Wikipedia dump of 1 October 2017: about 2.9 billion words,
    7.6 million unique, window k = 5, lowercased.
  - Only square sub-matrices are used: the Google set's 905 words plus
    the top 1,000 (or 10,000) words by co-occurrence with them. That
    gives vocabularies n = 1,487 and n = 10,072.
  - d = 300 dimensions, with word vectors U_d S_d^(1/2).
- **The restricted word2vec baseline (S1 Appendix).** word2vec-NS-topn
  is trained by Gensim CBOW with negative sampling on a dummy corpus of
  500 million "sentences". Each has length 2k + 1, a centre word drawn
  from U(w), and the other 2k words drawn independently from P(c | w).
- **Toy corpus (§5.3, Figs. 5, 8).**
  - 8 subjects, 3 verbs and 6 objects form 24 sentences out of 8 × 3 × 6
    = 144 possible.
  - Each verb carries one aspect through two hidden states: Sex (M/F,
    tie/dress), Royalty (R/C, palace/house) and Number (S/P).
  - Every subject occurs with every verb, and its object is fixed by its
    value on that verb's aspect.
  - The eight subjects are all 2³ combinations of the three aspects.
  - Window 5, so every pair within a sentence co-occurs.
- **Definition 1 (Eq. 4).** Eight rows form a parallelepiped if, for
  some permutation π, the three edge vectors are each repeated four
  times. For example, c_π(1) − c_π(2) = c_π(3) − c_π(4) = c_π(5) −
  c_π(6) = c_π(7) − c_π(8), and likewise for the other two edges.
- **Raw counts.** Theorem 1 is about the raw co-occurrence rows. It does
  not cover their logarithm, a PMI or an SVD.

## Key results

- **Analogy accuracy (§3.2, Fig. 1).** Percent correct on the Google
  set (19,544 questions, 14 categories), for the 1,487-choice task, with
  the 10,072-choice task in brackets.

  | model | accuracy |
  |---|---|
  | raw rows (freq) | < 6% (< 5%) |
  | logfreq | about +40 points over freq; 41% in §6 |
  | logfreq-SVD | above 61% (50%); "60%" in §6 |
  | ppmi | about 54% (54%) |
  | ppmi-SVD | 55% (51%) |
  | word2vec-NS-topn | 38% (40%) |
  | word2vec-NS-full (about 0.32M words) | 75% (69%) |

- **Without negative sampling (§4).** word2vec trained by full-softmax
  cross-entropy on P(c | w), with centre words drawn ∝ U(w)^α, reaches:

  | n | α | words seen | accuracy |
  |---|---|---|---|
  | 1,487 | 1 | 50M | about 56% |
  | 1,487 | 1/2 | 3.6M | about 60% |
  | 10,072 | 1/2 | 10M | about 59% |

- **Uniform toy corpus (§5.3.1).**
  - With p_i = 1/24, the 8 × 9 subject block has rank 4 and lies in a 3D
    affine space.
  - Its coordinates C′B(BᵀB)⁻¹, with C′ = C(I₉ − (1/9)1₉,₉), form a
    parallelepiped (Fig. 7a).
  - With a ±1 basis per aspect, the three axes are Sex, Royalty and
    Number (Fig. 7b).
- **Non-uniform toy corpus (§5.3.2).** With p_i drawn uniformly from
  [0, 1], the eight rows form "neither a parallelepiped nor
  parallelograms" (Fig. 7c, one draw shown).
- **Natural text (§5.4).**
  - One "parallelepiped-like" object is shown among Family-category words
    in a 2D PCA of logfreq-SVD vectors (Fig. 7d).
  - "It merely demonstrates the 'existence' of a parallelopiped."
- **Theorem 1 (§5.5).** For the toy corpus, the 8 × 17 subject block
  forms a parallelepiped if and only if
  p01 = p02 = p03 = p04, p05 = … = p08, …, p21 = … = p24 (Eq. 5).
  Each group of four is the four sentences that end in one object.
  - **Necessity.** For a fixed labelling, Eq. 6 is N C = 0 with N a 9 × 8
    matrix whose kernel is spanned by the constant vector and the three
    aspect indicators k₁, k₂, k₃ (Eq. 10). So every column of C must be
    affine in the aspects.
  - The reader's check: an object's column is zero on the four subjects
    that do not take it. An affine function of three ±1 variables that
    vanishes on a face of the cube is a multiple of the opposite face's
    indicator. So the four non-zero entries are equal, which is Eq. 5.
  - The paper extends this to all permutations through a case analysis
    of the rank of B (§5.5, cases 1–4).
  - **Sufficiency** is asserted from the uniform case and the
    permutation classes.
- **The symmetry (§5.6).** The 48 permutations that solve case 1 are
  called "the dihedral group". 48 is the order of the symmetry group of
  the cube, the hyperoctahedral group, not a dihedral group of the
  square.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | SVD of log raw co-occurrence counts solves most Google analogies over a restricted vocabulary | moderate | Fig. 1; one corpus, two vocabularies, consistent with Tian et al. |
| C2 | Negative sampling is not needed for word2vec to solve analogies at small vocabularies | moderate | §4, full-softmax training at n = 1,487 and 10,072 |
| C3 | ppmi-SVD beating word2vec-NS-topn shows that negative sampling is not mostly PPMI | weak | §3.2; the baseline is trained on a dummy corpus with independent context words |
| C4 | In the toy corpus, raw co-occurrence rows form a parallelepiped if and only if each object's four sentences are equally probable | moderate | Theorem 1; necessity is sound, the permutation case analysis is loosely written |
| C5 | Parallelograms in word vectors reflect a symmetry, local uniformity, in sentence probabilities in natural text | weak | one toy theorem and one PCA picture |

## Concepts

- **Parallelepiped.** Eight vectors whose differences along three edges
  each repeat four times (Definition 1). It is the 3D form of the
  analogy parallelogram.
- **Local unigram.** The condition of Eq. 5: within a class of sentences,
  the next word's probability does not depend on which earlier word
  occurred.
- **Distributional hypothesis, refined.** An isomorphism between a
  symmetry (exchangeability) in the word generator and a geometric shape
  of word vectors.

## Connections

The paper sets itself against Levy, Goldberg and Dagan's account of
negative sampling as implicit PPMI factorisation. It takes up Chiang et
al.'s finding that analogies survive the removal of within-sentence
pairs. It agrees with Tian et al.'s ln-SVD analogy result on the British
National Corpus, which covered only about 55% of the Google set. It does
not cite Arora et al.'s or Allen and Hospedales's ratio conditions
beyond listing them. It does not cite any model in which attributes act
multiplicatively.

**The reader's remark: sum against product.** [THEORY-185](../theory.d/THEORY-185.md) (from [LIT-863](../literature.d/LIT-863.md))
gets linear attribute directions in the *PMI*, because there each
attribute multiplies co-occurrence and the logarithm turns the product
into a sum. Here the aspects combine as a mixture: each sentence carries
one aspect, so counts add across aspects. Raw counts are then linear,
and the logarithm would break the shape: log of a sum is not a sum, and
zero cells go to −∞. The two models agree that parallelograms are in the
data. They disagree about which transform of the data shows them,
because they assume different ways for attributes to combine.

## Bearing on the record

- **[QUESTION-025](../questions.d/QUESTION-025.md).**
  - The toy corpus is the full hypercube: every subject is one of the 2³
    combinations of independent aspects. Its concept lattice is Boolean.
    So Theorem 1 is "a further demonstration that independent attributes
    give parallelograms", which the question says does not settle it.
  - Its non-uniform result does touch the question's third case,
    attributes that "interact in co-occurrence". With the incidence held
    Boolean, any departure from local uniformity breaks the *exact*
    parallelepiped in raw counts.
  - It gives no measure of how far the shape degrades. It says nothing on
    implication or exclusion between attributes.
- **[LIT-977](../literature.d/LIT-977.md)'s registration.**
  - [LIT-977](../literature.d/LIT-977.md) calls this "a derivation of why linear analogy structure
    follows from co-occurrence statistics" and "a second account of the
    premise that [THEORY-185](../theory.d/THEORY-185.md) derives". Two corrections.
  - The derivation covers one 8-subject toy corpus and raw counts only.
  - Its premise is not [THEORY-185](../theory.d/THEORY-185.md)'s. Aspects combine additively (a
    mixture over sentences), not multiplicatively. So the condition for
    linearity sits in a different transform of the data: raw counts here,
    PMI there.
  - It is a rival account for a different generative structure, not a
    second derivation of the same one.
  - The real-text evidence that "the data" suffice uses log counts and an
    SVD, and raw rows score under 6%.
- **[THEORY-183](../theory.d/THEORY-183.md).** That account gets Fourier modes from a translation
  symmetry of co-occurrence. Theorem 1 gets a parallelepiped from a
  symmetry of the sentence distribution, the cube's 48 symmetries. Both
  read geometry as a symmetry of the statistics. The paper does not
  connect the two.
- **Filed from this reading:** [THEORY-271](../theory.d/THEORY-271.md).
- **The anthology.** The analogy benchmarks of §§3–4, and the remark on
  when negative sampling helps, are about building word embeddings. They
  are ML practice and belong to the Anthology of the SOTA, so the LIT
  keeps its `anthology-candidate` flag. Theorem 1 and the
  distributional-hypothesis argument are linguistics, and stay here.

## Limitations

- **Theorem 1 covers one corpus.** It applies to a single 24-sentence
  design with 8 subjects, and to exact shapes. The authors note that
  "there is no solution for Eq (6) with noisy word vectors", and they propose, without
  doing it, to minimise an error instead.
- **The real-text comparison is confounded.** word2vec-NS-topn was
  trained on a dummy corpus whose context words are independent given
  the centre. In CBOW every word in turn is a centre, so context–context
  pairs enter training with no real co-occurrence behind them. That may
  explain part of its 38–40%. The full-corpus word2vec still beats every
  count model.
- **The two reports of logfreq-SVD differ.** §3.2 gives "above 61%" and
  §6 gives "60%".
- **The natural-text parallelepiped is one example in a 2D projection.**
- **The proof is loose.** Its permutation case analysis is hard to
  follow: Eq. 15 is numbered twice, and the closing sentence of the case
  list reads "class 4 with Eq (5) is the necessary condition".

## Open questions

- What, in the toy corpus, keeps a parallelepiped under the logarithm or
  PMI? For instance, a condition under which sentence probabilities
  factorise across aspects. Answering this would join this account to
  [THEORY-185](../theory.d/THEORY-185.md).
- A graded version is needed: how far rows depart from a parallelepiped
  as a function of how far Eq. 5 fails.
- A toy corpus with implication would show what Theorem 1's method
  gives. For example, Royalty defined only for adults, or a subject set
  that is not the full cube. The method of the proof (the kernel of the
  constraint matrix) applies to any target shape, and the paper says
  so.
