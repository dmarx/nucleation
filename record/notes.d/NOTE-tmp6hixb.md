---
status: Read
paper: LIT-tmp4jv7c
title: 'Plain Talk About Neurodevelopmental Epistemology'
version: 1
history:
- version: 1
  date: '2026-10-01'
  note: >-
    Read in full from the IJCAI-77 proceedings text (vol. 2, pp.
    1083–1092, ijcai.org PDF with a text layer): body, Minitheories 1–3,
    Notes 1–9 and references. The c-line and case-ordering diagrams survive
    only as fragments in the text layer. I also OCR'd the MIT AI Memo 430
    scan (DSpace hdl 1721.1/5763, June 1977) and compared the two word by
    word. They are the same text, apart from the memo's cover page, which
    dates it June 1977 and says the paper will be presented at IJCAI-77.
    The 1979 condensed version in Winston and Brown was not seen.
date: '2026-10-01'
summary: >-
  The first worked mechanism of the society-of-agents view, then "The
  Society of Minds". Agents too simple for language exchange no messages:
  each argument sits at a fixed location on shared channels (c-lines),
  and the agents themselves are short-term memory. A specificity gradient
  makes low-level communities local, persistence-memory and a case-shift
  handle interruptions without a stack, and the infant's internal
  "cognitive cases" are conjectured to precede and shape linguistic
  cases. Speculation throughout; the author says so.
---
<!-- inactive-ok-file: LIT-031 — Proposed; named as a neighbour, not leaned on -->
<!-- inactive-ok-file: LIT-046 — Proposed; named as a neighbouring account of collective intelligence, not leaned on -->

# NOTE-tmp6hixb: Plain Talk About Neurodevelopmental Epistemology

## Contribution

The paper takes the society-of-agents view as given, credits it to joint
work with Papert (Note 1), and asks one engineering question of it: how
could very simple agents in one mind communicate? Its answer is that they do
not send messages. Arguments live at fixed locations that the agents share.
From that one constraint it derives a developmental story about how agents
differentiate, how a young mind handles interruption, and how internal
"cases" could seed the cases of natural language.

## Key insight

If the parts of a mind are too stupid to parse, they cannot talk; they can
only share wires. A shared wire works like a shared convention, where water
comes from faucets and mail from mailboxes. Conventions are cheap to keep if
every new agent is born as a slight variant of an old one, already attached
to the same wires. So the constraint that looks crippling, rigid fixed
locations, is what development would produce anyway.

## Assumptions

- **Agents are very simple.** They are "just intelligent enough to
  accomplish their own specialized purposes", and lack syntax and shared
  symbol definitions.
- **Brain as parallel machine.** The scheme is meant to work without the
  ordering conventions a serial computer would allow.
- **Development by splitting.** New agents arise "by splitting off from old
  ones, with only small changes", so they inherit their data connections. Radically
  novel agents are assumed rare in infancy, by analogy with organic
  evolution.
- **Method.** The paper favours developmental over performance theory: "Only
  a good theory of the principles of the mind's development can yield a
  manageable theory of how it finally comes to work." It calls its own
  speculations a possible "model of scientific irresponsibility".
- **Neurology is offered without evidence.** c-lines are white matter and
  agents are cortex. The "laminar hypothesis" has redundant parallel layers
  that differentiate as crosstalk is reduced, "with no pretense that there
  is any solid evidence for it".

## Key results

There are no theorems, data or programs. The results are proposals.

- **Five ways to pass arguments.**
  1. attribute-value pairs;
  2. an ordered list of values;
  3. an ordered list of pointers;
  4. a parsed linear message;
  5. "Send nothing!"

  The paper adopts a variant of (5): fixed short-term-memory locations,
  "global variables, with all the convenience and dangerous side-effects".
- **STM is the agents.** STM is "an extensive, branching structure, whose
  parts are not interchangeable". The classic limited-capacity results are
  reinterpreted as different groups of agents blocking one another's
  external communication.
- **Specificity gradient.** A few high-level channels span much of the brain;
  lower agents are segregated into sub-societies that "communicate within,
  but not between, those divisions".
- **Temporary storage.** Persistence-memory restores a recent sustained
  state after a transient disturbance. Transient case-shift moves patterns
  "upward" between c-line levels. The author distrusts the case-shift: it
  "seems physiologically unnatural to me" and is offered "more as an
  exercise than as a strong conjecture".
- **Minitheories 1–3 for descriptions.**
  1. A distinct c-line per property. Fine for infants, "extravagant" for
     adults.
  2. A GETPROP-like noun-agent. Rejected, because it loses "homogeneity of
     symbol-type".
  3. Several noun-cases with graded property structures and a case-shifter
     that moves the focus of attention into a better-described case.

  Minitheory 3 predicts a preferred ordering of cases in early language: when
  OBJECT shifts into SUBJECT, a "third" case replaces OBJECT by default.
- **Language.** Children already use something like syntactic structure
  internally. The puzzle is why grammatical speech comes so late, and the
  conjecture is a computational step, "learning to translate between
  languages". On "innate vs. acquired", internal uniformities in infancy may
  "compel society, in subtle ways, to certain conformities".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The mind is a society of simple agents whose interactions produce intellect and affect alike | assertion | stated as the background theory (Note 1); not argued in this paper |
| C2 | Simple agents can communicate without messages by reading and writing fixed shared locations | moderate as a design argument | §"Communication"; the computational point (global variables) is sound, and the brain mapping is unargued |
| C3 | Short-term memory is the extensive, non-interchangeable structure of c-lines, and span limits reflect blocking between agent groups | weak | reinterpretation of "well-known experiments", none cited or analysed |
| C4 | Agents differentiate by splitting from common ancestors, which explains how they come to share connections | weak | analogy with organic evolution; Notes 5–6 conjecture cross-inhibition and "concept-leaf" splitting |
| C5 | A transient case-shift lets young minds handle subproblems without a recursive stack | weak, by the author's own account | "something about it bothers me" |
| C6 | Early cognitive cases precede, and shape, the cases of natural language, and may give a preferred case ordering in early speech | weak, testable | conjecture; the paper proposes looking at early language development and reports no look |
| C7 | Grammatical speech arrives late because of an added computational facility, not because internal structure is missing | assertion | analogy with the theory of computation |

## Concepts

- **Agent.** A very simple specialist. "Each such agent is, by itself, very
  simple."
- **c-line.** A communication channel. Each agent reads and writes a few
  nearby ones, on two or three adjacent levels.
- **Specificity gradient.** The gradual decentralisation from a few global
  channels to many local ones.
- **Laminae.** Redundant parallel layers that act as one unit early and
  differentiate later.
- **Persistence-memory.** The tendency of c-lines to restore a recent
  sustained state.
- **Case-shift.** A shift of c-line contents into a "more principal" case.
- **Cognitive case.** A conceptual focus, such as ORIGIN, DESTINATION or
  INSTRUMENT, with its own property lines. It is the internal analogue of a
  linguistic case.
- **The Society of Minds.** The name, in 1977, of the theory pursued with
  Papert (Note 1).

## Connections

- **Frames.** The paper builds on the frame memo ([LIT-tmpf92fs](../literature.d/LIT-tmpf92fs.md)). It is "in
  part a sequel" to it (Note 1). Its fixed locations extend the frame memo's
  "common terminal". Its adjacent-level memory addressing revisits the frame
  memo's two-way frame matching ("I still don't understand the issues very
  well"). Families of agents sharing terminals "would usually constitute a
  'frame-system'".
- **K-lines.** K-lines ([LIT-tmp84goj](../literature.d/LIT-tmp84goj.md)) is Minsky's next step. It recasts
  these c-lines as K→P connections and says the earlier scheme was
  "confusingly bidirectional".
- **Named sources.** Tinbergen's hierarchical instinct model, used for
  coordination and the "consummatory act". Winston's near-miss learning.
  Newell, Shaw and Simon on reading as matching. Halliday's *Learning How to
  Mean*. Hewitt's antecedent and consequent reasoning.
- **Perceptrons, "on tap, not on top".** Local perceptron-like detectors are
  proposed for learning symbol patterns. Minsky's own book limited what
  simple perceptrons can do, and he answers that limit here: inputs are
  already meaningful symbols (Note 8).

## Bearing on the record

- **Collectives and wholes.** For the record's work on collectives, notably
  [LIT-046](../literature.d/LIT-046.md)'s computational account of collective intelligence, this paper
  supplies the inverse case. It is a collective whose members are mindless
  and cannot know more than their superiors (Note 9).
- **Group minds.** The society analogy here does not license treating a
  group of minded people as a mind, which is the move Schwitzgebel's
  argument needs ([LIT-159](../literature.d/LIT-159.md)). The pairing is mine.
- **Language.** C6 bears on the lexicalism and morphology papers in the
  record ([LIT-031](../literature.d/LIT-031.md), [LIT-071](../literature.d/LIT-071.md)) only remotely. It is a claim about acquisition
  order, not structure, and no THEORY here rests on it.
- **Boundary.** No machine-learning practice instruction; no anthology
  topic holds it.

## Limitations

- No evidence of any kind: no experiment, no program, no citation for the
  STM claims.
- The neuroanatomy is explicitly unsupported.
- The paper leaves "conflict and control in the Society of Minds" aside. It
  treats only communication, so the theory it names is not stated here,
  only presupposed.
- Its strongest mechanism, the case-shift, is the one its author trusts
  least.

## Open questions

- Is there a preferred case ordering in early language development, of the
  kind C6 predicts? The paper asks this and does not look.
- Do STM span limits behave like blocking between agent groups, differing by
  context, as C3 needs? Or do they behave like a fixed number of shared
  slots?
- Can fixed-location communication scale beyond infancy without the
  case-shift, or some other way to rebind roles?

## Corrections

- none to a seeded skim (there was no seed).
- **Citation.** The brief is right on number, year and venue, but it
  understates the first appearance. MIT AI Memo 430 is dated **June 1977**.
  The IJCAI-77 text appeared in August 1977 (vol. 2, pp. 1083–1092) and is
  the same text.
- **Attribution.** "Generally taken as the first published statement" of the
  society idea is not something the paper claims. It presents the theory as
  unpublished and in progress, under the name "The Society of Minds",
  plural. Minsky's 1979 K-lines memo credits a principle of the theory to
  Minsky and Papert's 1974 Oregon lectures, which were not checked, so
  priority is left open here.
