---
number: 718
status: Read
formerly:
- NOTE-tmp7i51r
paper: LIT-1023
title: 'Gallego & Orús — Language Design as Information Renormalization'
version: 1
history:
- version: 1
  date: '2026-10-13'
  note: >-
    Read in full from arXiv v5 (6 February 2022, the latest of five
    versions; 25 pp.), downloaded from arxiv.org. v5 carries the funding
    and conflict-of-interest statements of the SN Computer Science
    submission; the published version and v1 to v4 were not compared.
    Text extracted with pdftotext. Read: the whole text, Appendix A, all
    footnotes, the figure captions and Table I; the reference list was
    checked only for what the text cites it for. The figures are tree and
    tensor-network diagrams and were read from their captions; the
    equations extracted legibly. Every quotation below was checked
    against the extracted text by script, with whitespace and line-end
    hyphenation normalised. Lin and Tegmark's "Critical Behavior in
    Physics and Probabilistic Formal Languages", which the anthology says
    this must be read against, was not read.
date: '2026-10-13'
summary: >-
  Reads Chomsky's MERGE as a coarse-graining and builds sentence
  probabilities as mostly loop-free tensor networks of 3-index MERGE
  tensors, one per node of a given parse. Because MERGE's output is fixed
  by its input, a parsed sentence's probability is a product of local
  coefficients. Tree-shaped parses make correlations decay with tree
  distance, about log |j − i|, so polynomially in word separation. The
  averaging step that turns this into a claim about languages is
  asserted, and nothing is tested on data. Syntax only: semantics and
  context are set aside by the authors.
---
<!-- inactive-ok-file: CLAIM-098 CLAIM-061 CLAIM-163 — Proposed; open claims this reading tests or compares, cited as open -->
<!-- inactive-ok-file: THEORY-197 THEORY-036 — Proposed; readings this one is set beside, not leaned on -->

# NOTE-718: Gallego & Orús — Language Design as Information Renormalization

## Contribution

A physicist and a syntactician propose that MERGE, the Minimalist
Program's binary structure-building operation, is a coarse-graining in the
sense of the renormalization group, with time as the coarse-grained
variable. They make the analogy concrete for probabilistic language models.
A MERGE becomes a 3-index probability tensor, and a parse becomes a tensor
network whose contraction gives the sentence's probability. From that they
derive the decay of word-to-word correlations, define a quantum state whose
amplitudes are square roots of the model's probabilities, and bound
perplexity by the state's entanglement. The paper is mainly an analogy
followed through, not an empirical study. No treebank or model is
evaluated.

## Key insight

A parse tree is a renormalization diagram. Each node discards its
children's identities and keeps one coarser label for the next level up.
Correlations in a sentence therefore run through the tree, not along the
string. Two words far apart in the string can be close in the tree, so
their correlation decays with tree distance rather than with word
distance.

## Assumptions

- **Syntax only.** "here we did not consider any semantic unit of
  information, but rather focus only on the syntaxis." Agreement features
  are also dropped: the authors "assume here that no other information is
  carried by MERGE (such as genre, number, case, etc)".
- **MERGE is a function.** "given two objects being merged, there is only
  one possible output, no matter the context." Footnote 5 adds "Notice
  that the converse is not true", so the map is many-to-one. From this the
  authors conclude that "MERGE tensors are diagonal". In the reader's
  terms, each tensor is supported on the graph of a function from input
  pairs to outputs.
- **A known parse.** Every result is for a sentence with a given syntax
  tree T_n. The language-model probability is the sum over valid trees,
  and the quantum state of Eq. 22 is defined one tree at a time.
- **Phrase-structure grammar, few loops.** Movement and chains add an
  index and a loop. The authors say the loops can be fused back into a
  tree, and that "the number of loops in the TN is always quite small, as
  long as the syntax tree is based on a Phrase-Structure (Constituency)
  Grammar". Dependency grammars are deferred to a MERA-like sketch
  (Fig. 20).
- **Joint normalisation.** Eq. 5 normalises each MERGE tensor over all
  three indices, so it is a joint distribution, not a conditional kernel.
  The sentence probability of Eq. 8 is a product of such entries. The
  normalisation is restored by the partition function Z(T_n) of Eq. 23.
- **Renormalization in a thin sense.** Footnote 1 sets aside critical
  exponents, fixed points, RG flows and scaling: "we do not assume
  necessarily the existence of any of these in the case of language". The
  rescaling half of an RG step "has not been discussed in this paper"
  (Appendix A).

## Key results

- **Correlated factorization (§III.C.2).** For a parsed sentence, "no
  tensor contraction is needed at all". The probability is a product of
  one coefficient per MERGE (Eq. 8), and a word's marginal given the rest
  is read off one tensor that encodes "both the immediate neighborhood of
  the word, as well as about the overall syntactic neighborhood". The
  cost is O(n) once the tree is known. *Holds when:* MERGE is a function
  and the parse is given.
- **Counting (§III.C.1).** A loop-free parse of n words has exactly n − 1
  merged objects, so "one requires on the whole 2n − 1 units of syntactic
  information".
- **Correlations (§III.C.3, Eqs. 13–15).** The two-point function decays
  as C(i, j) ≈ e^(−d(i,j)/τ) in tree distance d. In a purely sequential
  parse (an MPS) d = |j − i| and the decay is exponential. In a balanced
  binary tree d ≈ log₂|j − i| and the decay is polynomial,
  1/|j − i|^(1/τ). *Holds when:* the network has finite bond dimension and
  few loops, so the standard tensor-network results apply. In the reader's
  check, e^(−log₂ x/τ) is x^(−1/(τ ln 2)), not x^(−1/τ); the difference is
  only in the exponent's constant.
- **Language-level power law (§IV, Eqs. 18–21).** The average tree
  distance over a language's sentences is taken to be about log₂|j − i|.
  This "must be the case, simply because most of the syntactic structures
  are trees as in Fig.13". The average correlation then decays as a power
  of separation, and mutual information as at least a power, through
  I ≥ a·C². The authors say "we obtained these expressions exactly". The
  averaging step is asserted, not shown, and the reader notes that the
  average of e^(−d/τ) is not e^(−(average d)/τ).
- **Universal decay, language-specific exponent (§IV).** The polynomial
  form is said to be universal and τ language-dependent, so τ "provides a
  quantitative way to classify different texts and different languages",
  and perhaps to place isolates such as Basque. No τ is measured.
- **Quantum state and circuit (§V).** Taking square roots of every MERGE
  coefficient gives a tree tensor-network state (Eq. 24). Successive QR
  decompositions make it isometric, and so preparable by two-body gates;
  the norm of the top state is the total probability of the tree.
- **Perplexity bound (§VI, Eq. 39).** For a block of n′ contiguous words,
  the reduced density matrix has rank at most the number of lexical
  categories N_l. Its eigenvalues are λ_α = p(n′)_α p(n − n′)_α, and a
  majorization step gives P ≥ min_α 1/(p(n′)_α p(n − n′)_α). The authors
  note it "is a fully classical result". The scaling P ≈ (1/p_max)^(n−1)
  (Eq. 40) is offered as rough.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | A probabilistic phrase-structure model of a parsed sentence is a mostly loop-free stochastic tensor network of MERGE tensors | strong, as a restatement | Eqs. 4–8; a PCFG written in tensor notation |
| C2 | If MERGE's output is a function of its input, a parsed sentence's probability factorizes into local coefficients and costs O(n) | strong, given the assumption | §III.C.2, Eq. 8; the assumption is an empirical claim about grammar, footnoted as one-directional |
| C3 | Correlations decay exponentially in tree distance, so polynomially in word distance for balanced trees | moderate | standard TTN/MPS results cited [18, 23, 24]; the log₂ distance is "correct in average" (fn. 7) |
| C4 | Languages on average show power-law correlations because of tree-like syntax | weak | the averaging step is asserted; matched to published observations [30], not to new data |
| C5 | The perplexity of a block of words is bounded below by its entanglement in the language-model state | moderate | majorization argument, §VI; one step left as "One can check" |
| C6 | Tree-structured networks (deep convolutional ones) suit language and recurrent networks and HMMs do not, because only the first have the right renormalization structure | weak | correlation decay of the corresponding tensor networks, via Levine et al. [45]; no training or benchmark |
| C7 | MERGE's irreversibility matches RG irreversibility, and phase impenetrability is its linguistic form | analogy | Appendix A, Table I; qualified by §VIII.D |
| C8 | The brain is "a biological information-renormalization machine", and language, mathematics and perhaps music are one ability | speculative | §VIII.F; the authors call it a hypothesis taken "somehow phylosophically" |

## Concepts

- **MERGE.** Binary set formation, K = {X, Y}, applied recursively.
  External MERGE takes two distinct objects; internal MERGE takes one
  contained in the other, which yields a chain (Appendix A).
- **MERGE tensor.** M_αβγ, the probability that α and β merge into γ,
  normalised jointly over all three indices.
- **Syntactic tensor network.** The tensor network whose shape is a
  sentence's parse, with one MERGE tensor per node.
- **Correlated factorization.** The paper's name for the fact that fixing
  the words fixes every internal index, so no sum over internal indices
  is needed.
- **Refinement levels.** One MERGE tensor for the whole plane (a PCFG);
  one per scale z; one per position (z, t); one per position and tree.
  They correspond to dropping "scale invariance", "translation
  invariance" and tree independence.
- **Language model quantum state.** |Ψ(T_n)⟩, with amplitudes the square
  roots of the model's probabilities for a fixed tree.
- **Phase / phase impenetrability.** A derivational stage whose interior
  later operations cannot reach. The paper maps it to an RG scale and to
  RG irreversibility.

## Connections

- The paper places itself among physics approaches to language
  (Piattelli-Palmarini and Vitiello; complex networks after Ferrer i
  Cancho and Solé) and says its own is "radically different" from
  network analyses of language.
- For long-range correlations it cites the empirical studies of
  Alvarez-Lacalle et al. and Altmann et al., together with Lin and
  Tegmark's "Critical Behavior in Physics and Probabilistic Formal
  Languages" ([30]). It cites Lin and Tegmark only as an observation and
  does not engage its argument. As that paper is standardly cited, it
  derives power-law mutual information from recursive grammars and
  exponential decay from Markov processes. That is close to this paper's
  §IV, and was posted on arXiv fourteen months earlier
  (arXiv:1606.06737, v1 21 June 2016, there titled "Criticality in Formal
  Languages and Statistical Physics"; the date was checked on its arXiv
  record). Lin and Tegmark is
  not read here. This record does not hold it.
- The neural-network claims rest on Levine et al. ([45]) for the tensor
  structure of networks and on Lin, Tegmark and Rolnick ([46], held here
  as [LIT-887](../literature.d/LIT-887.md)) for the network–renormalization link.
- The authors' Matrix Syntax programme ([40]) is named as where the
  rescaling step of RG appears concretely.

## Bearing on the record

The LIT's standing section lists three checks. Each is answered here.

**1. Composition and [QUESTION-026](../questions.d/QUESTION-026.md).** [QUESTION-026](../questions.d/QUESTION-026.md) asks whether how a whole
utterance's observables are carried is fixed by how its parts' are. The
paper does give a result of that shape, for one observable. A parsed
sentence's probability is a product of local MERGE coefficients (Eq. 8),
and a word's conditional distribution is fixed by one tensor and its
syntactic environment. That is a result of the form the question asks
about: the whole fixed by its parts and their mode of combination. Appendix A states compositionality the same way: an
object's "interpretation is fixed by the elements it contains and the way
in which they are combined". But the observable is the syntactic
probability of a well-formed string, not a meaning, and not an empirical
model indexed by context. The paper sets semantics aside explicitly, and
context of use never enters. So it offers neither the construction nor
the separation that [QUESTION-026](../questions.d/QUESTION-026.md) says would settle it. If it leans either
way, it leans by omission to the question's second branch. Its
composition stops before propositional content, not past it, so it says
nothing about footing or force ([CLAIM-061](../claims.d/CLAIM-061.md)). As a source for [QUESTION-026](../questions.d/QUESTION-026.md)
it is weaker than the record's DisCoCat readings ([NOTE-245](NOTE-245.md), [NOTE-246](NOTE-246.md)),
which at least compose meanings.

**2. Irreversibility and [CLAIM-098](../claims.d/CLAIM-098.md).** The LIT's inference was that a
coarse-graining is not invertible, and that this is [CLAIM-098](../claims.d/CLAIM-098.md)'s point about
translations. The paper supports the premise and not the step. The premise
is there: MERGE is many-to-one (footnote 5), the coarse label keeps "a
priori" nothing of the constituents, and Appendix A ties strict
cyclicity and phase impenetrability to "the idea of irreversibility of RG
flows". Three things block the step.
- The irreversible map runs from a sentence's parts to its whole inside
  one structure. [CLAIM-098](../claims.d/CLAIM-098.md) is about maps between media or languages. The
  paper has no transport, and nothing in it carries irreversibility from
  the first kind of map to the second.
- MERGE here is a deterministic function. The paper's tensors are
  stochastic only as distributions over which merges occur, not as
  stochastic transformations of content. A many-to-one function failing to
  be invertible is the trivial case of [CLAIM-098](../claims.d/CLAIM-098.md)'s semigroup, and needs no
  paper.
- The authors qualify the irreversibility themselves (§VIII.D). In use,
  "our brain seems to organize the information according to different
  time scales, but does not seem to fully erase the information when
  going from one scale to the next". The "memory environment" is
  "non-Markovian". The coarse-graining is irreversible in the grammar and
  not, for a while, in the speaker.

So the resemblance the LIT recorded fails on inspection. The paper can be
cited for composition being many-to-one in syntax, and not for
translation.

**3. Lin and Tegmark.** The anthology's caution is borne out. The power-law
result of §IV is close to Lin and Tegmark's. This paper's version adds an
asserted averaging step and is no more rigorous. It neither engages that
paper nor improves on it. Lin and Tegmark was not read here (see
Connections).

**Two nearer bearings the LIT did not name.**
- **Target-relative coarse-graining ([CLAIM-152](../claims.d/CLAIM-152.md)).** The paper's RG step
  keeps "the most relevant information" for the next scale. In the worked
  example, what is relevant is that "the compound object is a verb phrase".
  Relevance is fixed by what the grammar needs next, which is a target in
  [CLAIM-152](../claims.d/CLAIM-152.md)'s sense. The paper does not say so. It illustrates [CLAIM-152](../claims.d/CLAIM-152.md)
  without arguing for it, and that bearing is the reader's.
- **Architecture against objective ([QUESTION-060](../questions.d/QUESTION-060.md)).** C6 is a pure
  architecture answer to [QUESTION-060](../questions.d/QUESTION-060.md): networks suit language when their
  tensor structure matches the parse. No training is considered.
  [THEORY-197](../theory.d/THEORY-197.md) found that the objective, not a formal match, fixes what a
  Boltzmann machine keeps. C6 is the kind of claim that finding warns
  against reading as an explanation. It is also an instruction for
  machine-learning practice, and so the anthology's reading, not this
  record's.

**On the analogy itself.** The paper keeps the name "renormalization" and
drops most of what makes RG more than coarse-graining: no rescaling, no
fixed points, no flow (footnote 1, Appendix A). That is the shape of the
objection [CLAIM-163](../claims.d/CLAIM-163.md) makes to "synchronization", an analogy whose
mechanism is missing. Read honestly, "MERGE = Coarse-graining" says that a
parse discards constituent identity level by level. The literature on
coarse-graining as lossy, scale-relative description that the record
already holds ([NOTE-674](NOTE-674.md), [THEORY-036](../theory.d/THEORY-036.md)) says more about that.

No THEORY should be produced from this reading.

## Limitations

- No data. The four refinement levels are described as "computable from a
  TreeBank", but none is computed, and no correlation exponent or
  perplexity is measured.
- The language-level power law rests on an unproved average over parse
  shapes.
- Everything is conditional on a known parse. Parsing, ambiguity and the
  sum over trees are named and not treated.
- MERGE as a function is assumed from grammar, and the authors say why
  it holds is "beyond the scope of this work".
- The neural-network verdict (C6) predates, and in v5 does not mention,
  attention-based models. It rests on correlation decay, not on
  performance.
- The authors' own scope statement: "we observed how correlations in
  human language get organized, explained this organization using the
  tools of physics, and exploited the consequences. And that is
  everything we did."

## Open questions

- Whether measured treebank parses have average tree distance near
  log₂|j − i|, and so whether τ can be estimated per language as §IV
  proposes.
- Whether the factorization survives semantics. The authors say it
  "would not be difficult" to add semantic information. If it did
  survive, it would bear on [QUESTION-026](../questions.d/QUESTION-026.md)'s first branch.
- What the non-Markovian retention of discarded detail (§VIII.D) does to
  the irreversibility claim, and whether a reader-side model of it would
  still be a coarse-graining.
