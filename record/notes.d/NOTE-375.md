---
number: 375
status: Read
formerly:
- NOTE-tmpb651q
paper: LIT-457
title: 'Burns — Fluid Concepts and Creative Analogies: A Review'
version: 1
history:
- version: 1
  date: '2026-10-02'
  note: >-
    Read in full (AAAI's PDF of AI Magazine 16(3), pp. 81–83, the same file
    the AAAI OJS page links; text extracted with PyMuPDF, whose column order
    on these three-column pages is scrambled, so passages were re-ordered by
    sense before reading). Read: the whole review, its two references and
    the reviewer's note. The book itself (LIT-428) was not read, so where
    the review describes the book this note reports the review. Page
    references to the book (p. 187, p. 515) are Burns's.
date: '2026-10-02'
summary: >-
  A three-page review of Hofstadter and FARG's collection. It explains the
  parallel terraced scan and "cognition is recognition" clearly, then asks
  why the work has had little impact on AI: microdomains with possibly
  hidden assumptions, and critiques of rivals that rest on analogy and
  intuition and are not turned on Copycat. Its sharpest point is that the
  symbol-grounding charge against SME applies to Copycat too.
---
<!-- inactive-ok-file: LIT-428 — Deferred, no lawful full text; the book this review is of, cited for what the review says about it, not leaned on for its content -->

# NOTE-375: Burns — Fluid Concepts and Creative Analogies: A Review

## Contribution

A contemporary, sympathetic but critical review of [LIT-428](../literature.d/LIT-428.md) by a
psychologist who models analogy himself (a postdoctoral fellow in
psychology at UCLA, per the reviewer's note). It gives a compact account of
the book's architecture and thesis, and a diagnosis of why the work had
"surprisingly little impact on the field of AI".

## Key insight

Burns's frame is the Sagan analogy, used both ways: like Sagan, Hofstadter
explains ideas to a wide audience and inspires people in his field; like
Sagan among some astronomers, he is not taken seriously by many in his
field, partly for irrelevant reasons (a Pulitzer Prize and a newsgroup) and
partly for valid ones. The valid ones are about method: what a program in a
microdomain shows, and how one argues against rival programs.

## Assumptions

- That impact on AI is a fair measure to ask of the work, and that
  intuitions must be argued for if others are to build on them.
- That the same evaluative standard should be applied to one's own programs
  as to rivals'. The criticism of Copycat rests on it.
- No assumption about the book is checked against the book here; this note
  reads the review only.

## Key results

- **The book (as Burns describes it).** Basic Books, New York, 1995, 518
  pp., $30, ISBN 0-465-05154-5. A collection of articles, many already
  published, with "a coherent vision" given by Hofstadter's prefaces.
  Represented FARG members: Chalmers, Defays, French, McGraw, Mitchell.
  Quick tour: chapters 2, 4, 5; chapter 5 (Copycat) "perhaps the best
  description of an implementation".
- **Parallel terraced scan.** Representation starts as unrelated elements
  and is elaborated by codelets, some of which recognise possible
  structures and post codelets to build them, others build, and others
  destroy structures inconsistent with higher-level ones. Codelets wait on a
  coderack, each with nonzero probability of running; running one changes
  the probabilities of others. Lowering temperature as coherence grows
  makes destruction harder. Burns likens it to neural networks and genetic
  algorithms, and suggests codelets might be learned by genetic algorithms,
  which would answer the objection that they are hand-coded.
- **High-level perception.** "Cognition is recognition": extracting
  meaning from low-level perception by accessing concepts. Burns traces the
  idea to the Gestalt psychologists and, with Hofstadter, to Kant. Analogy
  is not a "heavy weapon wheeled out now and then to deal with especially
  tough problems" (p. 187, quoted). Slippage between related concepts
  explains fluidity, and so creativity. BACON is criticised for being given
  Kepler's data, when finding the data was the discovery.
- **Criticism 1: microdomains.** Letter strings, table settings, word
  puzzles, letter fonts. Hofstadter's defence, that real-world programs
  also restrict their domains, less honestly, is granted "a worthwhile
  point". But microdomains "can contain hidden assumptions", and it is
  "not clear to what extent the programs ... succeed because they avoid
  representational issues that are relegated to low-level perception".
- **Criticism 2: method of argument.** Analogy and rhetorical question in
  place of analysis of "what a program aims to achieve and how well it
  achieves its goals", sometimes straying "in the direction of ridicule".
  - The Eliza effect ("Preface 4") is real but "not an all-or-none
    proposition"; the analysis it calls for should be applied to
    Hofstadter's programs too.
  - Symbol grounding: SME is criticised because it would run the same with
    *water* and *ice* replaced by A and B; the same objection to Copycat is
    dismissed because an observer would work out that SIGMA means
    successor. Burns: "the symbol grounding problem is not so easily
    solved". An equally astute observer could infer that the symbol with
    *water* and *ice* means *melts*.
  - Evaluation ("Preface 5"): Hofstadter dismisses models for disagreeing
    with his intuitions (the index entry "SOAR program ... ambitiousness yet
    boringness of", p. 515) and says any project is "90 percent" intuition.
    Burns agrees AI models are hard to compare and validate, but calls the
    response "tantamount to withdrawal from the argument".
- **Verdict.** Recommended; the ideas "might be on the right track", but
  "Hofstadter makes his challenge too easy to ignore for those who should
  take the most notice of it."

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The book rests on two ideas, the parallel terraced scan and cognition as high-level perception | moderate | the reviewer's reading; consistent with the chapter titles in [LIT-428](../literature.d/LIT-428.md) |
| C2 | Hofstadter's work has had "surprisingly little impact" on AI | assertion | no citation or other measure is given |
| C3 | The microdomain programs may succeed by relegating representation to low-level perception | open question, posed as such | "It is not clear to what extent" |
| C4 | The symbol-grounding charge against SME applies equally to Copycat | moderate | a symmetric counter-example (SIGMA vs. *melts*), argued in the review |
| C5 | Hofstadter's response to the evaluation problem withdraws from argument and risks irrelevance | opinion, argued | the "90 percent intuition" passage and the SOAR index entry |

## Concepts

- **Parallel terraced scan.** Many possibilities explored in parallel at
  different levels of commitment, with resources shifted by probabilistic
  choice of codelets.
- **Codelet, coderack, temperature.** Small specialised pieces of code; the
  pool they wait in; a global measure of disorder that sets how readily
  structure is torn down.
- **High-level perception.** Making sense of perceived material at the
  level of concepts.
- **Eliza effect.** Crediting a program with understanding it does not
  have, because its outputs look meaningful.
- **Microdomain.** A deliberately small, constructed domain in which a
  cognitive phenomenon can be modelled.

## Connections

- **[LIT-428](../literature.d/LIT-428.md) (the book).** The work reviewed. The review agrees with
  [LIT-428](../literature.d/LIT-428.md)'s report of it on every point checked; see the LIT's standing.
- **[LIT-150](../literature.d/LIT-150.md) (Rizi, on emergence).** [LIT-428](../literature.d/LIT-428.md) pairs the book's "emergent" with
  it. Burns's description adds one thing to check there: the emergence he
  describes is the absence of "top-level control", a claim about
  architecture, not about coarse-graining or prediction.

## Bearing on the record

- It does not change [LIT-428](../literature.d/LIT-428.md)'s status. The book remains unread, and the
  review is one reader's account.
- It sharpens what a reading of [LIT-428](../literature.d/LIT-428.md) should test: whether Copycat's
  symbols are grounded in any sense SME's are not (C4), and whether its
  success depends on representation decided in advance (C3).

## Limitations

- A three-page review: the book's models are described, not assessed in
  detail, and no experiment or comparison is reported.
- The impact claim (C2) is unsupported.
- The preface numbering the review uses cannot be checked without the book
  (see Corrections).

## Open questions

- How does the book number its prefaces? Burns's "Preface 4" (Eliza effect)
  agrees with [LIT-428](../literature.d/LIT-428.md)'s contents note if prefaces take the number of the
  chapter they precede; his "Preface 5" (evaluation) does not, since the
  note places that preface before chapter 9.

## Corrections

- None to the record. [LIT-428](../literature.d/LIT-428.md)'s account of this review was checked against
  the full text and agrees with it.
