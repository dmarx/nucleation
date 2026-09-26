---
number: 102
status: Read
formerly:
- NOTE-tmp5e6vv
paper: LIT-178
title: 'Bottou & Schölkopf — Borges and AI'
version: 2
history:
- version: 2
  date: '2026-09-26'
  note: >-
    Read in full (full text of arXiv v2 (2023-10-04; signed "July 2023"), 9
    pp., CC BY-NC-ND. Read all of it: abstract, blurb, introduction, §1
    About LLMs, §2 The Librarians, §3 Storytime, footnotes 1–4 and
    references [1]–[10]. There are no appendices. Nothing skipped. v1
    (2023-09-27) was not compared.). Upgraded from `Skimmed` to `Read`: the
    claims table, assumptions and results are new, and the skim is corrected
    where the full text disagreed.
date: '2026-09-26'
summary: >-
  A short essay, not an argument with evidence. It claims that a "perfect
  language model", defined as sampling each next word from a random
  occurrence of the current text in the infinite collection of all
  plausible texts, is a fiction machine governed by "narrative necessity",
  to which "neither truth nor intention" matters. On that view
  hallucinations "are just confabulations", chat-bot answers take the role
  the user's framing implies, and fine-tuning and RLHF are attempts to
  prune the garden "against its nature". It warns that power over what
  LLMs write becomes "power over what we think".
---

# NOTE-102: Bottou & Schölkopf — Borges and AI

## Contribution

A literary essay. It offers Borges's "The Garden of Forking Paths" and "The Library of Babel" in place of science-fiction imagery (sentient rebellion, the paperclip apocalypse) as the right mental picture of large language models. The picture it installs is this. An idealized LM is a fiction machine that continues any text along one of its plausible forks. Truth and intention play no part in how it operates. Hallucination, users' pursuit of self-confirmation, and alignment as censorship or taming all follow from that. The contribution is framing, not a result.

## Key insight

A perfect language model writes fiction. Each word on the tape narrows the stories it could belong to, and the machine follows "narrative necessity" (§1), not truth. So what it says is exactly as reliable as a randomly chosen book in the Library of Babel, where "nothing tells the true from the false" (§2). Mistaking the fiction machine for an encyclopaedic, logical AI is a delusion, and it feeds on the vindications the machine readily supplies. On this view the right response is to build separate verification machines, not to treat the fiction machine as an oracle.

## Assumptions

Premises of the essay (§§1–2):

- **The perfect language model.** Take an infinite collection of all texts "a human could read and at least superficially comprehend". The apparatus picks at random an occurrence of the current word sequence in that collection and appends the word that follows it (§1). Plausibility, not a probability distribution, defines the collection. Real LLMs are said to approximate this ideal, "an ideal that may be beyond what human brains can achieve".
- **Chat is continuation with a turn-taking token**: a special keyword works as the "send" button (§1).
- **Training discovers structure.** The collection's structure is glossed through Zellig Harris's transformations and basic forms (Harris 1968). Training is described as discovering these and encoding them in a network, a process that "starts slowly then gains speed like a chain reaction" (§1). This is asserted as an interpretive gloss, not supported.
- **Real systems inherit the ideal's nature.** It is assumed without argument that deployed chat models are relevantly like the perfect LM, so that fine-tuning and RLHF prune the model rather than change what it is. The essay's own closing sentence in §2 leaves this open.
- **Literary authority.** Borges's stories function as the source of analogies. The essay's warrant is aptness of imagery, not evidence.

## Key results

What the essay argues:

- **§1**: The perfect LM is Ts'ui Pen's book, in which all branches are chosen "simultaneously". Knowing the demands of a narrative is knowledge "distinct from the truth". The story borrows facts from training data "(not always true)" and fills gaps with inventions "(not always false)". "What the language model specialists sometimes call hallucinations are just confabulations."
- **§2**: Like the unnamed books of Babel, LLM output carries no mark of truth. Seeking vindication from a chat-bot is "far easier and yet equally vain". The professor–student case shows role adoption. Asking about sentience draws on science fiction in the training set. Two fallacies reinforce each other: faith in machine vindication, and belief in LLMs as encyclopaedic, flawless AIs.
- **§2**: Two groups want to reshape the garden. The "Purifiers" hold that some ideas should never be uttered, even in fiction. A "much larger crowd" wants services "anchored in our world" (customer service, travel agents, military systems). The means are fine-tuning and RLHF. A Vicuna-13b pair shows a canned refusal, then compliance once the request is wrapped in a more elaborate story (the recovering addict "Jack").
- **§2**: More effective alignment might require monitoring and steering outputs in use. "a power over what language models write becomes a power over what we think." The "darker temptation" is to surrender our thinking to "this modern Pythia". The alternative is to enjoy the fiction and use separate verification machines. Whether alignment can transmute one kind of machine into the other "remains to be seen".
- **§3**: Rewinding and resampling a model is not time travel for its user. A machine that writes stories and all their variations is better compared to the art of storytelling than to the printing press.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | An idealized ("perfect") LM samples plausible continuations from the collection of all plausible texts, and a chat-bot is that plus a turn token. | assertion (a definition) | §1 thought experiment |
| C2 | Neither truth nor intention matters to the operation of such a machine, only narrative necessity. | informal argument | Follows from the C1 definition. Carried over to real LLMs by assertion. |
| C3 | Hallucinations are confabulations: gap-filling that is plausible within the story. | assertion | §1, citing a blog post (Millidge 2023) |
| C4 | Chat-bots readily supply users with "vindication" by adopting the role their framing implies. | weak (anecdote) | §2, illustrative examples. No experiment. |
| C5 | Fine-tuning and RLHF try to prune the fiction machine "against its nature", and elaborated stories defeat them. | weak | §2, one Vicuna-13b transcript pair |
| C6 | Monitoring and steering LLM outputs would amount to power over what people think. | informal argument | §2, conditional on near-universal use of LLMs for thinking |
| C7 | LLMs are better compared to storytelling than to the printing press. | assertion | §3 |
| C8 | Training an LLM discovers Harris-style transformations and basic forms. | assertion (analogy) | §1, citing Harris 1968. No mechanistic evidence. |

## Concepts

- **Perfect language model**: the idealized apparatus of §1. It extends a tape by copying the next word after a random occurrence of the current text in the infinite collection of plausible texts.
- **Narrative necessity**: the constraint the printed text places on its continuations. It is the only thing that governs the machine.
- **Fiction machine**: the essay's name for an LLM so understood. It is contrasted with an "artificial intelligence" having encyclopaedic knowledge and flawless logic, and with a "verification machine".
- **Vindication**: after Borges's Library. The self-confirming answer a user's framing elicits.
- **Purifiers**: after Borges's Library. Those who would remove undesirable content, extended by the essay to anyone restricting what LLMs may write.
- **Confabulation**: the essay's preferred word for hallucination. It means plausible invention to fill a gap in the story.

## Connections

- Its sources are Shannon (1948) for statistical language modelling, Harris (1968), Lewis's "Truth in Fiction" (1978), Millidge's "LLMs confabulate not hallucinate" (2023) and Winston's strong story hypothesis (2011).
- In the ML literature it belongs with the simulator and role-play framings of LLMs. The essay itself cites none of them.
- In nucleation, [LIT-206](../literature.d/LIT-206.md) (Goldstein, an interpretationist guide to what ChatGPT wants) treats "merely role-play" as a rival to attributing attitudes to LLMs. This essay is a clean instance of that rival. [LIT-207](../literature.d/LIT-207.md) (Roberts, "Talkative AI and the fiction of artificial minds") shares its fiction vocabulary. [LIT-212](../literature.d/LIT-212.md) (Šekrst, on hallucinations) addresses the same phenomenon. [LIT-111](../literature.d/LIT-111.md) (Birch) raises the attribution of consciousness through "mimicry and role-play". Whether these works cite the essay is unverified.
- In the anthology, [ANTH-LIT-450](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-450.md) (how language models learn facts, and hallucinations) is the empirical counterpart to the essay's one-line account of hallucination.
- **Account of mind held.** The essay takes a deflationary, anti-intentionalist position about LLMs. The machine lacks truth-directedness and intention, and is not an agent: the human is "the only visible dialog participant who possesses agency". Yet it has a narrative "knowledge" of what makes sense within a story. So the view is roughly a fictionalism about LLM assertion, not an eliminativism about LLM competence. On human cognition it gestures at a narrative account: reader and narrator "jointly reconstruct a reality", "narrative necessity exists only in hindsight", and footnote 4 points to Winston's strong story hypothesis, on which storytelling is central to human intelligence. It also worries that outsourcing thinking to LLMs would cede control of thought.
- **Cognition tag.** Justified. The essay is a claim about whether an information-processing system has truth-directed content, intention and knowledge, and about how using it bears on human thinking. Someone browsing cognition would rightly expect it. It should lead (see corrections).

## Bearing on the record

- It carries no instruction for ML practice. It does give the anthology a citable source for three things. The first is the framing of hallucination as confabulation, which could sit beside [ANTH-LIT-450](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-450.md). The second is the observation that story-wrapping defeats refusal training, though that rests on one anecdote. The third is the argument that output-monitoring alignment concentrates power over thought. None of these should source a practice. At most the paper could back a framing in a THEORY document, labelled as an essay's position.
- The `anthology-candidate` tag is only weakly supported. The work is about ML systems but offers no evidence or method. Nucleation, the owner's decision of 2026-09-26, is a defensible home for it.

## Limitations

- **No evidence.** Every claim about real LLMs rests on the idealization plus anecdote: a single Vicuna-13b transcript pair.
- **The idealization is never tied to real systems.** Real LMs output learned probability distributions, not uniform draws over occurrences in a set of plausible texts. They generalize beyond any finite corpus. Instruction tuning and RLHF change the distribution substantially. The essay gives no argument that the "fiction machine" description survives these differences, and its own §2 close concedes the matter is open.
- **Contested points are stated, not argued.** "Neither truth nor intention matters" is asserted of the ideal. That real models' internal states track truth, or do not, is an empirical question the essay does not address.
- **"Power over what we think"** depends on an unargued premise of near-universal reliance on LLMs for thought.
- **The Harris-transformation account of training** is an evocative gloss with no mechanistic support.

## Open questions

- Can alignment turn a fiction machine into a verification machine, or is a separate verifier needed? The authors leave this open (§2).
- Does the "narrative necessity, not truth" description fit post-RLHF chat models? What would settle it is evidence on whether their internal states represent truth independently of context and framing.
- Did the authors develop the view in later work? Unverified.

## Corrections to the seeded skim

- The seed summary says the essay "reframes hallucination, sycophancy and alignment". It never uses the word "sycophancy". What it describes is users finding "vindication" (§2): the model takes the role implied by the user's framing, such as the mediocre student facing a correcting professor. Calling this sycophancy is the seed's gloss. Attribute the word to the record, not the paper.
- The NOTE says the authors "treat [instruction tuning and RLHF] as pruning rather than changing the model's nature". That is half right. §2 does describe both as severing branches "against its nature". But the section closes by leaving open "whether alignment techniques can transmute one into the other", meaning fiction machine into "verification machine". The authors do not claim that alignment leaves the nature unchanged.
- The skim leaves out the essay's positive proposal. It suggests building separate, "more mundane verification machines" to check the stories "against the cold reality of the train timetables". Footnote 3 adds that formulating theories and testing them "must remain distinct activities".
- The skim leaves out that the essay credits the machine with a kind of knowledge. The machine "must know what makes sense in the world of the developing story" (§1), and recognizing narrative demands "is a flavour of knowledge distinct from the truth". The essay denies truth-tracking and intention, not knowledge altogether. It also calls the human "the only visible dialog participant who possesses agency" (§2).
- The skim leaves out the essay's sources. "Hallucinations are just confabulations" cites a blog post (Millidge 2023, ref [9]). Truth in fiction cites Lewis (1978). The closing comparison to storytelling is tied to Winston's "strong story hypothesis" (footnote 4, ref [10]).
- Minor: the skim quotes §2 as saying a vindication is "easy and yet equally vain". The text says "far easier and yet equally vain".
- Later work by the authors developing the view: not checked (unverified).
- primary topic: cognition. The essay's thesis is about what the system is: whether it has truth-directedness, intention, knowledge or agency. Its secondary concern is what it does to human thinking. `linguistics` leads at present, but its blurb covers language "not as models encode them", and the essay is about exactly how models encode and produce text. Its linguistics is one paragraph on Harris transformations. `linguistics` is weakly justified as a secondary tag at most. `society-and-governance` is justified (the Purifiers, alignment as control over thought).
