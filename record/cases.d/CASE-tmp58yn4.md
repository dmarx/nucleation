---
status: Active
title: 'FactBank''s source-relative factuality labels and Kiesling et al.''s stance-triangle annotation: one stance construct annotated reliably, the interpersonal ones not'
version: 1
standing: documented
tags:
- psychometrics
- pragmatics
- linguistics
date: '2026-10-10'
line: pragmatic-transport
summary: >-
  FactBank labels one event's factuality separately for each source that
  reports it, so a proposition held fixed gets different commitment
  labels by source, and trained annotators agree at κ = 0.82. Kiesling
  et al. annotate Du Bois's stance triangle in Reddit threads, including
  an investment dimension defined as the split of animator from
  principal, and reach only α = 0.40 to 0.57, with investment and
  alignment below 0.4 outside one community. Together they bracket an
  answer to [QUESTION-tmpt0ou9](../questions.d/QUESTION-tmpt0ou9.md): commitment relative to a source is
  annotatable when defined by tests, interpersonal stance only moderately.
---
<!-- inactive-ok-file: LIT-780 — Deferred; Goffman, unread here, named as the source of the footing construct and not leaned on -->

# CASE-tmp58yn4: FactBank's source-relative factuality labels and Kiesling et al.'s stance-triangle annotation: one stance construct annotated reliably, the interpersonal ones not

Found on 2026-10-10 by a search the owner asked for: annotation studies in
which several judges label stance or footing on the same material and an
agreement statistic is reported, the evidence [QUESTION-tmpt0ou9](../questions.d/QUESTION-tmpt0ou9.md) asks for.

## The case

**FactBank (Saurí and Pustejovsky).** Every event in a corpus of news text
is labelled with a factuality value relative to each source that bears on
it. Sources are nested, after Wiebe et al.'s MPQA: what the text reports
Izvestiya as saying is Izvestiya-according-to-the-author. The values run
from certainly true (CT+) through probable and possible to uncommitted (Uu).
The LDC readme: "Event factuality is not an inherent feature of events but a
matter of perspective."

The paper's example (25), "Izvestiya said that the G-7 leaders pretended
everything was OK in Russia's economy." The event "everything was OK" is
"assessed as being a fact (CT+) according to the G-7 leaders ... but as
being false (CT−) according to Izvestiya ... The text author, on the other
hand, remains uncommitted (Uu)" (Saurí and Pustejovsky 2008, §3.1). One
proposition, three sources, three labels.

Agreement, Cohen's κ, by task (2008, §6): identifying source-introducing
predicates 0.88; identifying the sources 0.95; assigning the factuality
value to each event for each source 0.82, "over the 30% of the corpus". In
an analysis of disagreements on 10% of the corpus, "around two thirds of
them are cases of true ambiguity", most often the scope of a reporting
predicate. The paper compares Rubin (2007) on five-way certainty, κ = 0.15,
rising to 0.41 under stricter instructions. The LDC readme gives κ = 0.81
overall, and credits the design: "a battery of discriminatory tests for
distinguishing between factuality values", and a procedure "divided into
basic, sequential annotation tasks".

**Kiesling, Pavalanathan, Fitzpatrick, Han and Eisenstein (Computational
Linguistics 2018).** Stance utterances in 68 Reddit threads are rated on
three dimensions from Du Bois's stance triangle ([LIT-779](../literature.d/LIT-779.md)), each on a scale
of 1 to 5: affect, investment and alignment with the interlocutor.
Investment is a footing construct by the authors' definition. Recasting "I
love that game" as "That game is all right" removes the speaking subject,
which "moves the evaluation away from being the responsibility of the
animator (more technically, it separates the animator and principal)" (§2).

Agreement, Krippendorff's α with squared-difference distance against a
within-thread permutation baseline, on 33 threads (§3.2): "moderate
agreement was attained for all three stance dimensions, with a maximum of
α = 0.57 for AFFECT, and a minimum of α = 0.40 for ALIGNMENT." It depends on
the community. In r/explainlikeimfive, affect α = 0.41 and investment 0.55.
In the other subreddits, affect α = 0.63, "with α < 0.4 for INVESTMENT and
ALIGNMENT". The authors' explanation: affect depends on "decontextualized
cues such as word meaning", and alignment "is the most dependent on
sequential context". In the first phase "each thread introduced new
challenges and causes for disagreement", and they "hypothesized a speech
activity effect", then narrowed the material to two subreddits. Comparing
linguists with computer scientists, and undergraduates with experienced
researchers, found no significant difference.

## What it bears on

[QUESTION-tmpt0ou9](../questions.d/QUESTION-tmpt0ou9.md) asks whether readers can judge footing and stance
reliably and validly in the categories the designs use. The case answers
part of it, in two directions.

- **A stance label separable from the proposition can be annotated
  reliably.** FactBank holds the proposition fixed and varies the source,
  and trained annotators agree on the source-relative label at κ = 0.82.
  Commitment of a source is close to Goffman's principal, the one who stands
  behind what is said ([LIT-780](../literature.d/LIT-780.md), unread). This is an existence proof for the
  question's "fixed definition and a fixed response format": defined by
  discriminating tests and decomposed into sequential tasks, a
  source-relative stance can be labelled consistently.
- **Interpersonal stance is only moderately reliable, even for trained
  judges.** Kiesling et al. use the record's own construct, Du Bois's
  triangle, with a footing dimension. Agreement is α = 0.40 to 0.57, below
  0.4 for investment and alignment in most of the material, and it changes
  with the community. That supports the question's worry that "a defeat
  test run on those categories tests the categories as much as the
  thesis".

The two studies differ in what makes the difference. FactBank's construct
is tied to explicit linguistic structure (reporting predicates, nested
sources), and the source is identified before the value is assigned.
Kiesling et al.'s alignment depends on sequential context, which is where
footing lives.

The case is not offered in support of a claim. It is evidence on an open
question, and points two ways.

## What it cannot show

**Reliability between passes.** The question asks for agreement between
judges and between two passes of one judge. Both studies report agreement
between judges only. [CASE-012](CASE-012.md)'s failure was the analyst's own labels
drifting between passes; neither study tests that.

**Known-groups validity.** The question's validity test is renderings built
to differ only in the attributed speaker, which judges should separate, and
renderings built to differ only in wording, which they should not. FactBank
varies the source within one sentence by its grammar; nobody built
contrasts and checked that judgements track them. Kiesling et al. annotate
naturally occurring threads, with no constructed contrast.

**The construct the designs use.** FactBank's construct is epistemic
commitment, not teasing against reproach. Kiesling et al.'s is nearer but
is rated on 1-to-5 scales, not in [CASE-021](CASE-021.md)'s categories ("condemnation,
solidarity, amusement and irony") or [CASE-040](CASE-040.md)'s. Neither labels Goffman's
participation roles as such.

**Lay readers.** FactBank's annotators were trained, with guidelines and
adjudication; Kiesling et al.'s were authors and research assistants, and
in the first phase the authors discussed their disagreements (without
changing labels). The designs' receivers are lay readers.

**The defender's reply.** A defender of the designs' categories would say
that Kiesling et al.'s low α reflects their material, not the construct:
short Reddit posts with inside jokes and jargon, in threads of mixed speech
activity, where the authors themselves found every thread brought new
causes of disagreement. Give judges whole scenes with a known relation
between the speakers, as [CASE-018](CASE-018.md) does, and footing would be judged as
reliably as FactBank's commitment. The data cannot rule this out.
Agreement on investment was higher in the one focused community (0.55) than
in the rest (below 0.4), and FactBank shows how much a decomposed task with
tests helps. The reply turns the question into a design requirement, not
an answer.

**What would close the gap.** Stage 0 of the discriminating study,
[CASE-tmp1uzfn](CASE-tmp1uzfn.md): written definitions of stance and footing, a fixed response
format, agreement between judges and between passes against a target fixed
in advance, and known-groups validation with [CASE-018](CASE-018.md)'s reattributions as
stimuli. FactBank's design suggests how to write it: decompose the judgement
(first who the speaker is taken to be, then whom they address, then the
footing), and give a discriminating test for each category. Kiesling et
al.'s α against a permutation baseline is a usable statistic, and their
note, citing Craggs and Wood (2004), that Krippendorff's α "does not have a
cut-off score" points to the source on coefficients the question says it
lacks.

## Sources

Every URL below was retrieved on 2026-10-10. None of these works is held in
this record or, on a check of the anthology clone, in the anthology. They
are NLP corpus papers, and whether an anthology topic could hold them has
not been decided; none is filed here.

- **R. Saurí and J. Pustejovsky**, "From structure to interpretation: a
  double-layered annotation for event factuality", LREC 2008 workshop paper,
  https://www.cs.brandeis.edu/~roser/pubs/sauriPustejovsky_lrec08_2.pdf.
  Read directly and in full.
- **R. Saurí and J. Pustejovsky**, "FactBank: a corpus annotated with event
  factuality", *Language Resources and Evaluation* 43(3) (2009), 227–268,
  DOI 10.1007/s10579-009-9089-9. Not read; cited for the corpus.
- **FactBank 1.0**, LDC2009T23, readme,
  https://catalog.ldc.upenn.edu/docs/LDC2009T23/readme.pdf. Read directly.
- **S. F. Kiesling, U. Pavalanathan, J. Fitzpatrick, X. Han and J.
  Eisenstein**, "Interactional stancetaking in online forums",
  *Computational Linguistics* 44(4) (2018), 683–718, DOI
  10.1162/coli_a_00334, https://aclanthology.org/J18-4007. Read directly
  and in full.
- **J. Wiebe, T. Wilson and C. Cardie**, "Annotating expressions of opinions
  and emotions in language", *Language Resources and Evaluation* 39(2–3)
  (2005), 165–210, DOI 10.1007/s10579-005-7880-9, the source of FactBank's
  nested sources. Not read here; the research report gives its average
  pairwise κ of 0.81 for objective against subjective speech events.
  **Unverified here.**
- **V. L. Rubin** (2007) and **A. Craggs and M. M. Wood** (2004), cited only
  as FactBank and Kiesling et al. cite them. Not read.
- **J. W. Du Bois**, "The stance triangle" (2007), held as [LIT-779](../literature.d/LIT-779.md).
- **E. Goffman**, *Forms of Talk* (1981), held as [LIT-780](../literature.d/LIT-780.md) (Deferred,
  unread).
