---
number: 355
status: Read
formerly:
- NOTE-tmpjsht2
paper: 'LIT-394'
title: 'Turing — Computing Machinery and Intelligence'
version: 1
history:
- version: 1
  date: '2026-10-02'
  note: >-
    Read in full (the off-print from Mind LIX, No. 236, Oct. 1950, pp.
    433–460, scanned in the Turing Digital Archive, King's College
    Cambridge, AMT/B/19; OCR by Tesseract). I read §§1–7 and the
    bibliography. The storage figures on pp. 441, 442 and 455 were
    checked against the page images, since OCR loses exponents. The
    typescript AMT/B/9 and the Mind's I reprint were not compared.
date: '2026-10-02'
summary: >-
  Turing replaces "Can machines think?" by whether a digital computer can
  play the imitation game, predicts that by about 2000 a 10^9-bit machine
  will hold an average interrogator to 70 per cent right identifications
  after five minutes, and answers nine objections. The answer to the
  argument from consciousness is that its extreme form is solipsism. The
  positive case is admitted to be weak ("recitations tending to produce
  belief"); the programme is to educate a child-machine.
---
<!-- inactive-ok-file: THEORY-023 — Proposed: named as the account this reading bears on, not as support -->
<!-- inactive-ok-file: THEORY-043 — Proposed: named as the account this reading bears on, not as support -->
<!-- inactive-ok-file: LIT-413 — Deferred: the anthology that reprints this paper; named, not leaned on -->

# NOTE-355: Turing — Computing Machinery and Intelligence

## Contribution

The paper turns a question about the meaning of "think" into a question
about performance that could be settled by experiment, and fixes the
setting precisely: teleprinter, interrogator, a human competitor, a
digital computer. It is also the first systematic catalogue of objections
to machine thought, and it sketches a learning programme for meeting them.

## Key insight

Do not define thinking; replace the question. If a machine can stand in
for a man in a conversation game as well as a man stands in for a woman,
the reasons for withholding "thinks" from it are the same reasons that
would withhold it from other people, and nobody accepts those.

## Assumptions

- **Machines are digital computers** (§3). Engineering in general is
  excluded because it would let biological techniques "rear a complete
  individual" count as a machine.
- **Universality** (§5): a digital computer with adequate storage and
  speed mimics any discrete-state machine, "considerations of speed apart".
  The discrete-state machines are idealised; Turing says "strictly
  speaking there are no such machines".
- **The best strategy is imitation** (§2): "it will be assumed that the
  best strategy is to try to provide answers that would naturally be given
  by a man". He calls the alternative "unlikely" to matter, and does not
  argue it.
- **Questions only, by teleprinter** (§§1–2): no sight, touch, voice or
  practical demonstration.
- **Telepathy-proof room** (§6.9), needed only if E.S.P. is admitted.

## Key results

- **The game** (§1). A man (A), a woman (B) and an interrogator (C) in
  another room; C must say "X is A and Y is B" or the reverse; A tries to
  mislead. "What will happen when a machine takes the part of A in this
  game?"
- **Storage capacity** (§5). Capacity is log₂ of the number of states.
  The Manchester machine has about 2^165,000 ≈ 10^50,000 states, a
  capacity of about 165,000 (174,380 itemised); the three-state wheel has
  about 1.6. Capacities add when machines are combined.
- **The reduction** (§5). By universality, "Can machines think?" becomes:
  can one computer C, given adequate storage, speed and programme, "play
  satisfactorily the part of A in the imitation game, the part of B being
  taken by a man?"
- **The prediction** (§6). In about fifty years, at storage about 10^9,
  "an average interrogator will not have more than 70 per cent. chance of
  making the right identification after five minutes of questioning". And
  by the end of the century "one will be able to speak of machines thinking
  without expecting to be contradicted".
- **The nine objections** (§6):
  1. *Theological*: answered in theological terms (God could give a
     machine a soul), then set aside.
  2. *Heads in the sand*: needs "consolation", not refutation.
  3. *Mathematical*: any one machine has questions it cannot answer, but
     "it has only been stated, without any sort of proof, that no such
     limitations apply to the human intellect".
  4. *Consciousness* (Jefferson): the extreme form is solipsism; most
     holders would accept the game, as a viva voce, rather than that.
  5. *Various disabilities*: induction from the small machines people have
     seen; "errors of functioning" are distinguished from "errors of
     conclusion"; a machine can be its own subject matter.
  6. *Lady Lovelace*: "machines take me by surprise with great frequency";
     the objection assumes all consequences of a fact are present to a
     mind at once.
  7. *Continuity of the nervous system*: a digital computer can give the
     right sort of answer a differential analyser gives (π as a weighted
     guess among 3.12–3.16).
  8. *Informality of behaviour*: confuses rules of conduct with laws of
     behaviour; a 1000-unit Manchester programme already defeats
     prediction from its replies.
  9. *E.S.P.*: "quite a strong one", answered only by a telepathy-proof
     room.
- **Learning machines** (§7). Brain storage is estimated at 10^10 to
  10^15 binary digits; no more than 10^9 should be needed for the game,
  and 10^7 is practicable now. Sixty programmers for fifty years could do
  it by hand, so instead build a child-machine and educate it. Reward and
  punishment signals alone carry too little information, so add
  "unemotional" channels and a symbolic language. A random element helps
  the search for behaviour that satisfies the teacher. The teacher "will
  often be very largely ignorant of quite what is going on inside".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | "Can machines think?" is too meaningless to discuss and should be replaced by the imitation game | assertion | §§1, 6; the "Gallup poll" argument against reading it off usage |
| C2 | Restricting to digital computers loses nothing, because they are universal for discrete-state machines | strong, given idealisation and adequate store and speed | §5; Turing's 1937 result, cited |
| C3 | By about 2000, at 10^9 bits, an average interrogator gets at most 70 % right after five minutes | prediction | §6, stated as a belief and a conjecture |
| C4 | The mathematical objection shows limits on each machine, not a human advantage | moderate | §6.3: no proof is offered that humans lack such limits |
| C5 | The argument from consciousness, pressed fully, is solipsism, and its holders would accept the game instead | moderate | §6.4: the viva voce example; an argument about what objectors would accept, not about consciousness |
| C6 | Machines can surprise, make errors of conclusion, and be their own subject matter | moderate | §6.5–6.6; examples, and the programme-modification remark |
| C7 | The informality of behaviour does not show we are not machines | moderate | §6.8: the rules/laws distinction and the unpredictable 1000-unit programme |
| C8 | Telepathy, if real, is a strong objection | assertion | §6.9: "the statistical evidence, at least for telepathy, is overwhelming" |
| C9 | A child-machine plus education is the practicable route | weak | §7; "I have done some experiments with one such child-machine … too unorthodox … to be considered really successful" |
| C10 | The positive case is not argued | Turing's own | §7: "I have no very convincing arguments of a positive nature"; the onion and atomic-pile passages are "recitations tending to produce belief" |

## Concepts

- **Imitation game** — the three-party game of §1, with a machine in A's
  place. Turing never calls it a test of thinking; it replaces the
  question.
- **Digital computer** — store, executive unit and control, run from a
  table of instructions (§4). With a random element, it is sometimes said
  to have free will, "though I would not use this phrase myself".
- **Discrete-state machine** — one that moves "by sudden jumps or clicks"
  between definite states, given by a state table (§5).
- **Universal machine** — one that can mimic any discrete-state machine
  when programmed for it (§5).
- **Storage capacity** — log₂ of the number of states (§5).
- **Errors of functioning / errors of conclusion** — mechanical faults,
  which abstract machines cannot have, versus false outputs under an
  interpretation, which any machine can produce (§6.5).
- **Rules of conduct / laws of behaviour** — precepts one can act on and
  be conscious of, versus laws of nature applied to a body (§6.8).
- **Sub-critical / super-critical minds** — whether an idea injected
  produces on average fewer or more than one idea in reply (§7).

## Connections

- **Searle** ([LIT-400](../literature.d/LIT-400.md), read in [NOTE-349](NOTE-349.md)) attacks the adequacy of
  the test directly: two systems could both pass it, and only one
  understands. He calls the Turing test "unashamedly behavioristic and
  operationalistic". Turing's C5 is the answer Searle's "other minds
  reply" section dismisses as "only worth a short reply".
- **Block** ([LIT-407](../literature.d/LIT-407.md)) is the record's other early critic of judging
  mind by input–output equivalence; his China brain would pass a
  Turing-style test by construction.
- **Nagel** ([LIT-096](../literature.d/LIT-096.md)) holds that functional analyses are compatible with the
  absence of experience. Turing's C5 does not engage that claim; it is
  about what we would be entitled to say, not what is there.
- **Hofstadter.** The selection that follows this paper in *The Mind's I*
  ([LIT-413](../literature.d/LIT-413.md)) is Hofstadter's coffeehouse dialogue on it; not filed.
  [NOTE-136](NOTE-136.md) reports his later view that a consistent-understanding
  Turing test suffices to attribute thinking.
- **Not filed.** Jefferson's Lister Oration (BMJ 1949) and Lovelace's
  notes are cited here and are not in the record.

## Bearing on the record

- **[THEORY-023](../theory.d/THEORY-023.md) (Proposed): consistent, and it sharpens the account.** The
  account says mimicry undercuts behavioural evidence for AI
  consciousness. Turing's test is a test of thinking, not of
  consciousness. His defence of it against the consciousness objection is
  an other-minds parity argument, which assumes the behaviour is produced
  the way a human's is, not by imitation of human output (his §2
  assumption). Birch's and Schwitzgebel's mimicry worry ([LIT-111](../literature.d/LIT-111.md),
  [LIT-191](../literature.d/LIT-191.md)) is aimed exactly at that assumption, which Turing states and
  does not defend.
- **[LIT-153](../literature.d/LIT-153.md) / [NOTE-106](NOTE-106.md):** a claim that the imitation game has been passed
  should be measured against §6's specification: an average interrogator,
  five minutes, at most 70 per cent right, with a human competitor in B's
  place. A study that drops the human competitor or the time limit is not
  Turing's game.
- **[THEORY-043](../theory.d/THEORY-043.md) (Proposed): neutral.** The onion-skin passage states
  the decomposition, but as rhetoric, and Turing draws no conclusion about
  wholes and parts.
- **No new THEORY is indicated.** No ML instruction strong enough for the
  anthology; §7 is a research programme, historically the first, and the
  LIT notes the boundary question.

## Limitations

- The positive case is not argued, by Turing's own account (C10).
- The §2 assumption that imitation of a man is the machine's best strategy
  is unargued, and the test's power to detect thinking depends on it.
- Sample size, the number of interrogators and the statistics are left
  open: §3 mentions that "statistics [could be] compiled" and stops.
- The E.S.P. objection rests on evidence Turing accepts without citing.
- The child-machine experiment is reported as not "really successful",
  with no details.

## Open questions

- What should replace the §2 assumption once machines are trained on human
  output, so that imitation is the training objective?
- What would a test of the question Turing set aside, whether there is
  "no mystery about consciousness", look like? He says the mystery need not
  be solved first; he does not say it never has to be.

## Corrections

- none to a seeded skim (there was no seed)
- **Stale cross-references in the printed text.** §6.5 says "Compare the
  parenthesis in Jefferson's statement quoted on p. 21", and §7 says "The
  reader should reconcile this with the point of view on pp. 24, 25". In
  the Mind pagination Jefferson is quoted on pp. 445–446, and the
  arithmetic-mistakes discussion is on p. 448. The numbers appear to be the
  typescript's (AMT/B/9 is paginated pp. 2–40), and were not updated in
  print. Inferred from the pagination, not checked against the typescript.
- **"Turing test" is not Turing's phrase.** The paper says "imitation
  game", "the game" and "our test" (§6.4); it never says "Turing test".
