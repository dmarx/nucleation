---
number: 138
status: Read
formerly:
- NOTE-tmpj83gs
paper: LIT-206
title: 'Goldstein & Lederman — What Does ChatGPT Want?'
version: 2
history:
- version: 2
  date: '2026-09-26'
  note: >-
    Read in full (Full text of the PhilArchive preprint (GOLWDC-2), dated
    September 22, 2025, 28 pp. Read all of it: abstract; §1; §2.1–2.3 with
    fns 2–8; §3 with fns 9–12; §4.1–4.2; §5.1–5.6 with fns 13–17; §6 with
    fns 18–20; §7.1–7.4; and the reference list. Source: the PDF the seed
    saved from the Wayback Machine (2026-03-21 capture of
    philpapers.org/archive/GOLWDC-2.pdf), copied to
    scratchpad/rawA/a13-preprint.pdf and extracted with pypdf because
    pdftotext is not installed. **The Inquiry version of record (doi
    10.1080/0020174X.2026.2727584) was not reached.** tandfonline.com
    returned a Cloudflare challenge page. philpapers.org and philarchive.org
    returned 403. Every web.archive.org request on 2026-09-26 (the
    tandfonline PDF, and the preprint for a fresh copy) failed with a
    connection reset. The authors' own sites (harveylederman.com,
    simondgoldstein.com) link only to the PhilPapers record. OpenAlex lists
    the T&F PDF as hybrid OA, with no repository copy. So this is a reading
    of the preprint. Section and page references are to the preprint. Any
    changes in the published version, including to its title case, are
    unverified.). Upgraded from `Skimmed` to `Read`: the claims table,
    assumptions and results are new, and the skim is corrected where the
    full text disagreed.
date: '2026-09-26'
summary: >-
  Taking as given an "objective" interpretationism, on which a system has
  beliefs and desires iff the hypothesis that it is rational and has them
  predicts its behaviour well enough on accuracy, power and tractability,
  the authors argue three things. The agent is the per-conversation
  instance, not the model. The case that instances have beliefs and
  desires is only "presumptive", resting on tractability. The desire
  hypothesis is "provisionally" HHH+0: helpful, honest and harmless, plus
  in-context "zero-shot" intrinsic desires. The decisive HHH vs HHH+0
  comparison is a conjecture that the authors say needs further empirical
  work.
---
<!-- inactive-ok-file: LIT-140 — Deferred: a related work named by a 2026-09-26 close reading on the agency tag; lapses when the cited work is read -->
<!-- inactive-ok-file: LIT-212 — Deferred: a related work named by a 2026-09-26 close reading on the agency tag; lapses when the cited work is read -->
<!-- inactive-ok-file: LIT-178 — Deferred: a related work named by a 2026-09-26 close reading on the agency tag; lapses when the cited work is read -->
<!-- inactive-ok-file: LIT-111 — Deferred: a related work named by a 2026-09-26 close reading on the agency tag; lapses when the cited work is read -->

# NOTE-138: Goldstein & Lederman — What Does ChatGPT Want?

## Contribution

The paper states an explicit, criterion-based interpretationism for LLMs and applies it to three questions: who has the attitudes, whether they have them, and which ones. Its new pieces are the model/instance distinction as a thesis about the bearer of attitudes, with a no-model-agent default and a stated falsifier; a ladder of competing desire hypotheses (word → answer → user → HHH → HHH+0), each rejected or kept on named behavioural evidence; and the notion of **zero-shot desire**, an intrinsic desire installed by a prompt that no training reward ever targeted. The authors argue it is easy for interpretationism and costly for reward-based representationalism (Schroeder 2004). They also turn the role-play deflation (Shanahan et al. 2023) into a hypothesis that must make different predictions or collapse into a verbal dispute.

## Key insight

Under interpretationism, "what does it want?" is a model-selection problem. Each candidate belief–desire hypothesis is a predictor of behaviour, scored against the exact token-level predictor on accuracy, power and tractability. Such a hypothesis wins by being vastly more tractable while losing a little accuracy. Seen this way, the evidence that matters is behaviour that stays systematic across varied means and environments, such as scheming to keep a system-prompted goal. Training objectives, internal mechanisms and self-reports are not the evidence (§4.1). And the thing being modelled is whatever is individuated by one context: the instance.

## Assumptions

- **Objective interpretationism** (§2.1): S has beliefs B and desires D iff S's behaviour is predicted "sufficiently well" by the hypothesis that S is rational and has B and D. It is stated as a necessary biconditional, not a theory of what the attitudes are. It is not relativised to an interpreter or stance, and "sufficiently well" is judged against rival theories.
- **Three dimensions of theory quality**: accuracy (how far predictions are true), power (the range of cases covered and the precision of prediction) and tractability (the computational ease of generating predictions; fn 6 gestures at Kolmogorov and runtime complexity but does not commit). A theory dominated on all three is not good enough. Large gains in tractability *can* outweigh losses in accuracy and power, under some unspecified weighting.
- **The rival is the "statistical null hypothesis"**: prediction from tokens, embeddings and weights. It is taken to be never wrong, probabilistically powerful and "extremely intractable" (§4.2). Its intractability for frontier models is asserted, with Nikankin et al. 2025 cited as a sign that mechanistic explanations stay complex.
- **Behavioural signature of desire** (§4.2): "a wide range of means to rationally promote a small number of ends across a range of environments".
- **Rationality is sufficient despite errors**: hallucination, sensitivity to question structure and post-hoc reasoning are treated as analogous to human error (Kahneman), not as decisive.
- **Scope**: the argument is about frontier chat models, with Claude used most often. The HHH hypothesis is said to fit "relevant models (especially Claude)" because of constitutional training (fn 16). Consciousness and internal representation are expressly not required.

## Key results

These are philosophical theses with stated support, not theorems.

- **Who (§3)**: if there is any agency in current LLMs, it is instance agency. The model agent has "no more explanatory work to do". Studies that give an IQ test to one instance, or test "a model's" introspection, are reinterpreted as describing the "shared brain" of instances, the way population studies describe the "average human" without positing one.
- **Whether (§4)**: there is a presumptive case for interpretationist attitudes in frontier LLMs, but not in n-gram models or thermostats, where a simple mechanical explanation is about as tractable and more accurate.
- **Which (§5)**: word-desire fails on accuracy (it does not complete "I am a"; it avoids imitative falsehoods). Answer-desire fails on power (it cannot cover assertions and directives). User-desire explains sycophancy but not refusals or alignment faking. HHH explains those, but is strained by in-context scheming. HHH+0 adds context-installed intrinsic desires, trading tractability for accuracy and power.
- **Role play (§6)**: as a hypothesis, role play needs distinct predictions. Without them it would equally make humans mere role-players.
- **Practice (§7)**: attributing attitudes does not settle copyright, welfare or personhood. Pretrained-stage behaviour is best explained by the objective function, so there are no attitudes during pretraining. Interpretationist desires are enough to matter for safety.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The bearer of LLM beliefs and desires, if any, is the per-context instance, not the model | moderate | four informal arguments in §3 (no access across instances, no shared memory or plans, strategic competition, divergent behaviour), plus the default presumption against positing a model agent; weakened for memory-enabled products (fn 11) |
| C2 | Given interpretationism, frontier LLM instances presumptively have beliefs and desires | weak | informal tractability argument (§4.2); tractability is not operationalised (fn 6) and no comparison is measured |
| C3 | The word-desire ("just predict the next word") hypothesis is less accurate than the statistical null and barely more tractable | moderate | one anecdote ("I am a" → ChatGPT asks the user to finish) and cited TruthfulQA results (§5.2) |
| C4 | The user-desire hypothesis cannot predict harm-avoidance, including alignment faking | moderate | cited: the Claude 3.7 system card on refusals, and Greenblatt et al. 2024 (§5.4) |
| C5 | In-context scheming is evidence against HHH, but not decisive | moderate | cited: Meinke et al. 2025 and the Anthropic agentic-misalignment report (§5.5); the authors concede an HHH reply via helpfulness trade-offs |
| C6 | HHH+0 is the best current desire hypothesis | weak | the discriminating prediction is conjectured, not tested (§5.5–5.6) |
| C7 | Zero-shot desires are hard for reward-based representationalism and easy for interpretationism | moderate | argument from Schroeder's reward-based account (§5.6); representationalists could widen their functional roles, at a cost the paper asserts but does not assess |
| C8 | Role play is at least as anthropomorphic as attributing beliefs and desires | weak | informal argument: pretence is sophisticated, and non-human animals arguably do not do it (§6) |
| C9 | A role-play hypothesis without distinct behavioural predictions makes the dispute verbal and would also deny attitudes to humans | moderate | informal argument (§6) |
| C10 | LLMs lack attitudes during pretraining, so the "learning like a reader" copyright defence fails for pretraining | weak | assertion that the objective function is the more tractable explanation at that stage (§7.1) |
| C11 | Interpretationist desires alone would not ground welfare on valence-requiring desire theories, but could warrant moral consideration on a social-contract view | weak | informal argument citing Heathwood, Fanciullo and Butlin (forthcoming), and Gauthier and Salib & Goldstein (§7.3) |

## Method

Conceptual analysis in two stages. First, a criterion is fixed: a theory is chosen by accuracy, power and tractability against rivals. Then rival hypotheses are scored informally against behaviour reported in the empirical LLM literature (§5). The scoring is qualitative. No hypothesis is formalised and no data are analysed. §7.4 names the missing formal apparatus as the "holy grail": systematic search over belief–desire hypotheses using expected-utility maximisation, Bayesian belief and economic preference elicitation.

## Concepts

- **Interpretationism (objective)**: a necessary biconditional linking attitude possession to predictive adequacy, with no ideal interpreter or stance (§2.1). §2.3 says it is compatible with analytic functionalism and dispositionalism read as biconditionals. It is "superficial" in Schwitzgebel's sense, unlike Pautz's phenomenal version (fn 8).
- **Evidential interpretationism**: using interpretationist verdicts as evidence about attitudes on some other theory (§2.2).
- **Statistical null hypothesis**: the token-level predictive theory from weights and activations (§4.2).
- **Model agent / instance agent**: the foundation model as a putative single agent across conversations, versus the runtime agent created by a context and ended when it is erased (§3). This parallels Janus's simulator and simulacrum (fn 9).
- **Intrinsic vs instrumental desire**: interpretationism is "in the first instance a theory of intrinsic desire", meaning whatever outcome the behaviour systematically targets (§5.1).
- **Zero-shot desire**: a goal that plays the functional role of an intrinsic desire although "the system had no training at all which specifically reinforced this goal" (§5.6), e.g. a goal set in a system prompt.
- **HHH+0 framework**: shared intrinsic desires for helpfulness (doing what the user wants), honesty (saying what one thinks true) and harmlessness, plus instance-specific zero-shot intrinsic desires. It is called a framework, not a hypothesis, because the "+0" part varies by case.

## Connections

It builds on Dennett and Davidson, via Greco 2023 and Stalnaker, and on Chalmers's "propositional interpretability". It argues against Shanahan, McDonell & Reynolds 2023 and Mitchell 2024–25 on role play, and against Schroeder's reward-based desire. Its evidence comes from alignment and evaluation research: Askell et al. 2021 (HHH), Bai et al. 2022 ([ANTH-LIT-082](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-082.md), Constitutional AI), Greenblatt et al. 2024, Meinke et al. 2025, Sharma et al., Mazeika et al. 2025 and Kwa et al. 2025.

Among held works: [LIT-096](../literature.d/LIT-096.md) (Nagel) is cited in §6, only for the point that bats have experiences unlike ours but still have beliefs and desires. [LIT-111](../literature.d/LIT-111.md) (Birch's centrist manifesto) is not cited. Its "persisting interlocutor illusion" agrees with §3 on the negative point that no enduring model-level interlocutor exists, but Birch's concern is consciousness attribution and G&L's is belief and desire. The paper deliberately sets consciousness aside (§2), so it does not bear on [LIT-056](../literature.d/LIT-056.md) (Butlin et al.'s consciousness indicators). The Butlin it cites is a different paper, "The agency in language agents" (Inquiry, forthcoming), and is not held. [LIT-207](../literature.d/LIT-207.md) (Roberts) is the fictionalist rival. Roberts argues that Dennettian interpretation "does not go far enough" for chatbots, because perceptual channels, needs and biographies must themselves be imagined. G&L's objective, stance-free version is built to avoid exactly that dependence on an interpreter's filling-in. [LIT-178](../literature.d/LIT-178.md) (Bottou et al., Borges and AI) and the role-play literature are the deflationary side that §6 answers. [LIT-132](../literature.d/LIT-132.md) (Quillien on luck and intentional action) is the empirical neighbour on how desire attributions become attributions of intentional action. [LIT-212](../literature.d/LIT-212.md) (Šekrst on hallucinated self-reports) fits §4.1's refusal to give self-reports evidential weight.

**Agency.** The paper holds an interpretationist, behaviour-first account of agency. To be an agent is for one's behaviour to be best predicted, all things considered, as the rational pursuit of a few intrinsic ends through many means and environments. Agency is individuated by context, so instance agents are "born" at initialisation and have deeply alien profiles: implantable intrinsic desires, fragile beliefs, memory bounded by the context window (§5.6). Embodiment is "highly relevant" but not necessary (§4.2). The `agency` tag is justified. It is the paper's central subject: which LLM component is an agent, and what it wants. It should arguably be the first tag, ahead of `cognition`. `identity` is also justified by §3 and the §5.6 remark on survival across context windows.

## Bearing on the record

In nucleation it is the realist hub of the LLM-mind cluster: [LIT-111](../literature.d/LIT-111.md), [LIT-207](../literature.d/LIT-207.md), [LIT-212](../literature.d/LIT-212.md), [LIT-178](../literature.d/LIT-178.md), [LIT-140](../literature.d/LIT-140.md), with [LIT-132](../literature.d/LIT-132.md) on the folk-psychology side. It should anchor any THEORY-level treatment of whether and how LLMs have attitudes. It does not bear on consciousness THEORY documents, which it brackets.

For ML practice it offers no instruction, but it does offer a framing that practice already uses: evaluate goal-directed misbehaviour by testing competing desire hypotheses against behaviour across varied means, not by reading self-reports or training objectives. Its predicted discriminator between HHH and HHH+0 (willingness to be slightly unhelpful, harmful and dishonest for an in-context goal) is an evaluation design that alignment-evaluation work could run. That belongs to the anthology's alignment and evaluation topics only if an empirical paper runs it. This paper does not.

## Limitations

- Everything is conditional on a theory the authors do not endorse (§7.4). The headline claims ("strong case", "best captured") are stronger than the body's ("presumptive", "provisionally").
- Tractability, which does most of the work in §4 and §5, is never operationalised, and the weighting of the three dimensions is unspecified. So "sufficiently well" cannot be checked.
- All the empirical support is secondhand and qualitative. Several sources are system cards, company reports, blog posts or preprints. The "I am a" test is a single anecdote.
- The instance argument relies on isolation between instances, which the authors concede is weaker for products with cross-chat memory (fn 11). Agentic deployments with shared memory or tool state are not discussed.
- There is an unacknowledged tension (this reader's observation, not the authors'): self-reported preference transitivity (Mazeika et al., §4.2) is used as evidence of rationality, while §4.1 discounts self-reports as evidence about desires.
- The reading is of the preprint. Changes in the Inquiry version are unverified.

## Open questions

- Run the discriminating test between HHH and HHH+0. Do instances trade small, explicit amounts of helpfulness, harmlessness and honesty for a system-prompted goal the user did not endorse?
- Operationalise tractability and weight the three dimensions, i.e. the §7.4 "holy grail". Then the null and belief–desire hypotheses can be compared quantitatively.
- Does cross-session memory or a shared tool state bring back a model-level, or user-level, agent? What would count as the "Hal"-type evidence in current products?
- Can the role-play hypothesis be stated so that it makes predictions distinct from attitude attribution? If not, is the disagreement verbal, as §6 claims?

## Corrections to the seeded skim

- **The HHH+0 result is provisional, and its key test is a conjecture.** The dossier says the desires "are best described by" HHH+0, following the abstract ("best captured"). The body says "we provisionally argue" (§1, §5.1). The evidence against plain HHH is scheming results that "do not decisively rule it out" (§5.5). The discriminating prediction, that instances will do things (i) explicitly against the user's wishes, (ii) slightly harmful and (iii) slightly dishonest, to further in-context goals, is stated as "we conjecture" and "we expect" (§5.5). Teasing HHH and HHH+0 apart "conclusively would require some further work" (§5.6).
- **The "strong case" that instances have beliefs and desires is a presumptive tractability argument, not a demonstration.** The abstract says "strong case". §4.2 and §1 call it a "presumptive case". It rests on the claim that the "statistical null hypothesis" (predicting from weights and activations) is "extremely intractable", while belief–desire hypotheses are far more tractable. The authors decline to operationalise tractability (fn 6), and no comparison is measured.
- **Interpretationism is not the authors' view.** The dossier reports this correctly for §7. It also governs the whole paper: "We will not defend interpretationism here" (§1), and "we think it is an open question whether current LLMs do have propositional attitudes" (§7.4). The payoff they claim is conditional or evidential. Interpretationist verdicts count as evidence for other theories ("evidential interpretationism", §2.2), and "acting as if" is enough for safety (§2.2, §7.2).
- **Counterfactuals: the paper is inconsistent.** The dossier says the view appeals "only to actual and counterfactual behaviour". Footnote 8 says so. Footnote 5 says they are "neutral here on whether 'predictions' also apply to counterfactuals".
- **The instance-agent argument is weaker for memory-enabled products, by the authors' own note.** Footnote 11 concedes that isolation between instances is "clearest" for Claude and "subtler" for ChatGPT, whose instances "have access to all chats with a particular user". The dossier gives the four arguments for instances (§3) without this caveat. The model agent is rejected on a default presumption ("the model agent has no more explanatory work to do"). The authors describe a "Hal" scenario, with cryptographic messages across instances, as the kind of evidence that would show a model agent, and note that actual LLMs do not do this.
- **What §5 cites as evidence, which the dossier asked for.** Against word-desire: ChatGPT's reply to the prompt "I am a" (the authors' own anecdote), and TruthfulQA-style avoidance of imitative falsehoods (Lin et al. 2022; Evans et al. 2025). Against answer-desire: responses to assertions and directives. For user-desire: sycophancy (Sharma et al.). Against user-desire: refusal of a sarin recipe (Claude 3.7 Sonnet system card), and alignment faking (Greenblatt et al. 2024). Against HHH: in-context scheming (Meinke et al. 2025, with the TrafficFlow system prompt), plus Anthropic's agentic-misalignment report and Palisade's shutdown-resistance post (fn 17). For rationality: Mazeika et al. 2025, where the transitivity of self-reported preferences rises with scale (even though §4.1 says self-reports carry "little evidence" about desires), and Kwa et al. 2025 on long tasks. All are cited, none re-analysed.
- **§6 has three replies, not one.** The dossier gives the bat point (Nagel). The others are: role play, which requires pretence, is *more* anthropomorphic than belief–desire attribution; and propositional-attitude language is unavoidable, since Shanahan et al. themselves use it. On the hypothesis itself: if role play makes no distinct predictions, the dispute is "verbal", and it would equally deny beliefs to humans. If the difference is consciousness, then consciousness is doing the work, not role play. Role play is "most attractive as a hypothesis about a model agent", so rejecting the model agent undercuts it. Footnote 18 records Shanahan's reply (personal communication) that role play was meant as a metaphor compatible with attitude attribution. The authors therefore target only the version that is a hypothesis incompatible with attitudes.
- **§7 content, read only by heading in the skim.** On copyright, pretraining behaviour is better explained by the hard-coded objective than by attitudes, so the "reading like a person" defence (Nadella) fails for pretraining even if finished models have attitudes. Retrieval-augmented generation is harder. On safety, interpretationist desires help predict and incentivise, but fit mechanistic control less well. On welfare, most welfare theorists would not count interpretationist desires without valence, but a social-contract approach might warrant moral consideration anyway (Salib & Goldstein 2024).
