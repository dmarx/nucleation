---
number: 128
status: Read
formerly:
- NOTE-tmpgcb40
paper: LIT-126
title: 'Category error in AI safety: non-sentient moral machines'
version: 2
history:
- version: 2
  date: '2026-09-26'
  note: >-
    Read in full (full text of the author-deposited PhilArchive PDF, 10 pp.
    The PDF was rendered from Google Docs and carries no author name, date
    or affiliation; its embedded title uses a colon ("…Discourse: Why
    Non-Sentient Systems…"). Read all of it: abstract and keywords; §1
    Introduction; §2 The Category Error Thesis; §3 Moral Zombies; §4 The
    "Moral Machines" Misnomer; §5 Moral Status Without Sentience; §6
    Implications for AI Safety with §§6.1–6.4; §7 Objections and Replies
    with §§7.1–7.4; §8 Conclusion; and the 23-entry reference list. Nothing
    was skipped. Source: the Wayback Machine capture of
    philpapers.org/archive/VIETCE.pdf (March 2026), fetched in an earlier
    session. A fresh Wayback fetch on 2026-09-26 failed with connection
    resets, and philarchive.org and philpapers.org returned 403. The
    PhilArchive record page came from its Wayback capture of 2026-03-22.
    Text was extracted with pypdf because pdftotext is not installed.
    **Venue check (2026-09-26):** the record lists "AI and Society
    (forthcoming)" and gives the author's affiliation as the University of
    Tartu. Three searches found no such article. Crossref returned no match
    for a bibliographic query on the title, or for an author query
    restricted to AI & Society's ISSNs (0951-5666 and 1435-5655). An
    exact-phrase Springer Link search returned "No results". OpenAlex could
    not be checked (HTTP 429). The venue is therefore still the author's own
    unverified claim; nothing shows it is false, but no version of record
    exists to compare.). Upgraded from `Skimmed` to `Read`: the claims
    table, assumptions and results are new, and the skim is corrected where
    the full text disagreed.
date: '2026-09-26'
summary: >-
  A ten-page position paper. Its one explicit argument is "P1: moral
  status requires phenomenal consciousness; P2: current and foreseeable AI
  lacks it; C: such AI lacks moral status" (§3, p. 3). P1 rests on
  Swanepoel 2020, and P2 is asserted without argument. From this Vieira
  recommends that AI-safety frameworks measure only effects on sentient
  beings (§6.4). His replies retreat from C to a weaker norm, "we should
  not attribute moral status absent positive evidence of phenomenal
  consciousness" (§6, p. 6; §7.1), and he never says what that evidence
  would be.
---

<!-- inactive-ok-file: LIT-126 — Deferred: the paper is placed by this reading; the directive lapses when its status changes; the directive lapses when its status changes -->

# NOTE-128: Category error in AI safety: non-sentient moral machines

## Contribution

Little that is new. It restates the sentientist position on AI moral status (Swanepoel 2020) and borrows the label "moral zombies" from Véliz (2021). What it adds is a policy corollary: AI-safety frameworks and metrics should be "explicitly structured around impact on sentient beings rather than around properties of AI systems themselves", measuring "human autonomy, wellbeing, fairness, and flourishing, not anthropomorphized notions of AI 'welfare'" (§6.4, p. 6).

## Key insight

Separate three senses in which a system can be called "moral" (§4, p. 4). It can be *morally relevant*, meaning its operations affect sentient beings. It can be *morally programmed*, meaning it is built to follow moral rules or optimise for moral outcomes. It can be *morally minded*, with understanding "grounded in phenomenal consciousness and subjective valuation". Vieira holds that current AI is clearly the first and often the second, but not the third, and that "moral machines" talk slides from the first two to the third. The distinction is the one durable piece of the paper. Everything else depends on the unargued claim that the third is absent.

## Assumptions

Premises and authorities the argument rests on:

- **P1, sentientism about moral status, for agents and patients alike** (§3). Support: an appeal to Swanepoel 2020, who "defends sentience as the key criterion" (§2), and to "a long philosophical tradition". Nothing argues for extending the requirement to moral *agency*.
- **P2: current and foreseeable AI lacks phenomenal consciousness** (§3). This is asserted. §7.1 cites "significant theoretical reasons to doubt" it but names none. "Foreseeable" gets no argument at all.
- **A burden-of-proof rule.** Without positive evidence of consciousness, moral status should not be attributed (§6, §7.1, §7.2, §8). What would count as positive evidence is never specified.
- **The Rylean frame.** Attributing phenomenal properties to computation is a *category* error (§2), a mistake about logical type. This sits badly with Vieira's concession that the question is open to evidence (§6), because a category error cannot be corrected by evidence.
- **The p-zombie frame.** Chalmers' zombie is physically and functionally identical to a conscious human (§3). Current AI systems are neither, so the zombie is used here as an illustration, not as a conceivability argument.
- **A picture of the target discourse.** "Much contemporary AI safety discourse focuses on scenarios where advanced AI systems might themselves become objects of moral concern" (§6, citing Bostrom 2014). This is asserted with no survey, and it is doubtful as a description of AI-safety work in general.

## Key results

What it argues:

- **Category-error thesis (§2).** The discourse conflates (1) functional capacity with phenomenal consciousness, (2) behavioural simulation with moral understanding, and (3) instrumental value with intrinsic moral status.
- **Moral-zombie argument (§3, p. 3).** P1 and P2 give C, that current and foreseeable AI lacks moral status. Vieira says this "does not depend on skepticism about strong AI".
- **Three senses of "moral" (§4).** Relevant, programmed and minded, as set out under Key insight. The chess-queen sacrifice illustrates the second without the third.
- **Opportunity-cost claim (§4, end).** Resources spent on the "welfare" of non-sentient systems are diverted from sentient beings.
- **Non-sentient moral status (§5).** Ecosystems can be valued but not harmed "because there is no subject of experience", and "the same logic applies to AI systems".
- **Four safety implications (§6.1–6.4).** Clarify priorities, avoid anthropomorphic errors, keep responsibility with human designers and deployers, and build safety metrics on effects on sentient beings.
- **Four replies (§7).** Uncertainty does not warrant precaution toward AI, and precaution means making AI safe for "known sentient beings" (7.1). Functionalism supplies conditions, not evidence, and the burden of proof lies on whoever claims consciousness (7.2). Graded status still needs a baseline of sentience (7.3). Relational ethics explains why humans feel concern, not what grounds status, and confusing the two is "a second category error" (7.4).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Attributing moral status to AI conflates functional sophistication with phenomenal consciousness, a Rylean category error | weak | informal argument (§2); the "category" label is not defended against the paper's own concession that the question is empirical (§6) |
| C2 | Moral status, of agent or patient, requires phenomenal consciousness (P1) | weak | appeal to authority (Swanepoel 2020) and to "a long philosophical tradition" (§§2–3); nothing specific to agency |
| C3 | Current and foreseeable AI lacks phenomenal consciousness (P2) | assertion | §3; §7.1's "significant theoretical reasons to doubt" are not given |
| C4 | Current AI is morally relevant and often morally programmed, but not morally minded | weak | conceptual distinction (§4) plus C3 |
| C5 | Attention to AI welfare has real opportunity costs for sentient beings | assertion | §4 and §6.1; no evidence of how resources are actually allocated |
| C6 | AI-safety metrics should measure effects on human autonomy, wellbeing, fairness and flourishing, not AI "welfare" | weak | normative corollary of C2 and C3 (§6.4) |
| C7 | Uncertainty about AI consciousness does not warrant precautionary moral consideration | weak | informal reply (§7.1), which does not engage any stated precautionary principle |
| C8 | Functionalism supplies conditions, not evidence, and the burden of proof lies on those who claim consciousness | moderate | informal argument (§7.2); the first half is a fair point |
| C9 | Relational ethics explains moral concern, not moral status | weak | analogy to a child's doll (§7.4) |
| C10 | The paper answers objections from empirical human–AI interaction studies and from global perspectives on moral status | unsupported | claimed in the abstract only; absent from the body |

## Concepts

- **Category error** — attributing to one logical type the predicates proper to another (Ryle 1949). Here, treating computational processes as bearers of phenomenal properties (§2).
- **Moral zombie** — a system with "all the functional hallmarks of moral agency or patiency" but no phenomenal consciousness (§3). The term is Véliz's (2021).
- **Morally relevant / morally programmed / morally minded** — the three senses of "moral" in §4.
- **Moral patiency** — having interests that can be thwarted or fulfilled, which Vieira holds requires "a subject of experience for whom things go well or poorly" (§5).

## Connections

**The account of consciousness it holds.** Consciousness is phenomenal: "no 'what it is like' to be that system" (§2), and "nothing it is like to be them" (§5). This is Nagel's criterion, [LIT-096](../literature.d/LIT-096.md), used without citing Nagel. Paired with sentientism, it is the only thing that grounds moral status. On AI the paper is presumptively denialist but agnostic in principle: P2 is asserted for "current and foreseeable" systems, and §6 grants that machine consciousness is not impossible. It holds no theory of which physical or functional systems are conscious, and so has no way to say what "positive evidence" it wants. That gap is exactly what the indicator method of [LIT-056](../literature.d/LIT-056.md) (Butlin et al.) tries to fill. [LIT-056](../literature.d/LIT-056.md) is the obvious work to engage, and the paper does not cite it.

**Against held works.**

- *[LIT-166](../literature.d/LIT-166.md)* (Schwitzgebel & Sinnott-Armstrong's review of Birch, Sebo and Keane). Its §2 sets out Birch's Framework Principle 2, "sentience candidature can warrant precautions", and the definition of a sentience candidate, which counts AI systems with computational markers of sentience (Birch p. 321). Vieira's §7.1 rejects precaution toward AI without engaging that principle.
- *[LIT-111](../literature.d/LIT-111.md)* (Birch's centrist manifesto). It holds both errors, over-attribution and missed alien consciousness, in view at once. Vieira addresses only the first.
- *[LIT-207](../literature.d/LIT-207.md)* (Roberts). It reaches a similar deflationary verdict on chatbot self-ascriptions from a stated conditional premise, that many states depend on an animate body. It is a much better-argued route to part of P2.
- *[LIT-206](../literature.d/LIT-206.md)* (Goldstein & Lederman). It shows how beliefs and desires can be attributed to LLM instances on interpretationist grounds without any phenomenal claim. That is the separation of agency from phenomenality that Vieira's P1 ("either as agent or patient") denies without argument.
- *[LIT-135](../literature.d/LIT-135.md)* (Seth). It gives substantive biological-naturalist reasons to doubt AI consciousness, the kind of "theoretical reasons" §7.1 invokes but never states.

## Bearing on the record

- **consciousness tag: justified.** The paper's criterion of moral status is phenomenal consciousness, and its central factual premise is about attributing consciousness to machines. That falls squarely under the tag's blurb. Consciousness is still not what the paper is *mostly* about, so `ethics` should stay primary.
- It would oppose any THEORY document built on precautionary or indicator-based attribution of moral patienthood to AI (the [LIT-111](../literature.d/LIT-111.md) and [LIT-166](../literature.d/LIT-166.md) cluster), but it supplies no argument such a document would need to answer.
- **ML practice: nothing.** The recommendation in §6.4, to measure safety by effects on sentient beings, is a slogan, not a method. It names no metric, benchmark or procedure. Nothing here belongs in the Anthology of the SOTA.

## Limitations

- P2, which the whole conclusion needs, is asserted. The "theoretical reasons" of §7.1 are never stated.
- The argument's conclusion shifts. C in §3 is ontic ("lack genuine moral status"). The defended claim in §6 and §§7.1–7.2 is epistemic ("should not attribute absent positive evidence"). The paper does not say what would count as positive evidence, so the second claim cannot be tested.
- The Rylean framing does not fit the concession. If machine consciousness is an open empirical question (§6), attributing it is at worst a false belief, not a category error.
- The abstract overclaims: two of the three promised sources of counterargument are absent.
- Half the bibliography is uncited, and the cited survey (Danaher et al. 2017) is not a survey of AI moral status.
- The description of AI-safety discourse as focused on AI systems' own moral standing is unsupported. Bostrom (2014) is cited for it, and that book's main concern is risk to humans.
- It is a preprint. The venue claim cannot be verified.

## Open questions

- What would count as the "positive evidence of phenomenal consciousness" that the paper's burden-of-proof rule requires? Until that is specified, the rule gives the same verdict whatever systems are built.
- Is P1 plausible for moral *agency* (responsibility), as opposed to patiency? The paper runs the two together.
- Would it still be right to exclude AI "welfare" from safety metrics under a non-zero credence in AI sentience, the case [LIT-166](../literature.d/LIT-166.md) and [LIT-111](../literature.d/LIT-111.md) are about? That needs an explicit decision-theoretic comparison, which the paper does not attempt.

## Corrections to the seeded skim

- **Venue (dossier: "forthcoming in AI & Society; unverified").** It is still unverified after a direct check. Crossref and Springer Link hold no AI & Society article with this title, by this author or under these ISSNs, as of 2026-09-26. Keep it as a PhilArchive preprint (archived 2026-01-08) and do not cite it as AI & Society. The record gives the author's affiliation as the University of Tartu. The PDF's own title uses a colon where the record has "and".
- **Dossier: "§8 (p. 8) concedes that the question should be revisited if positive evidence of machine consciousness appears."** The concession is made first, and more fully, at the end of §6 (p. 6), where Vieira says the thesis "does not claim that machine consciousness is impossible in principle". §8 repeats it. The concession also changes the argument, which the dossier does not note. It turns the conclusion of §3 ("lack genuine moral status") into an evidential norm ("should not attribute moral status absent positive evidence"). These are different claims, and only the second is defended.
- **Dossier: "Check §7 to see whether the objections section actually engages the model-welfare literature."** It does not. §7 has four objections: Uncertainty (7.1), Functionalist (7.2), Gradient (7.3) and Relational Ethics (7.4). None cites the model-welfare or AI-sentience-indicator literature, and each reply is a paragraph long. The abstract promises counterarguments "from … empirical studies of human–AI interaction, and global perspectives on moral status". **Neither appears in the body.**
- **Reference list.** 12 of the 23 references are never cited in the text: Bryson 2018, Bryson et al. 2017, DeGrazia 2020, Dung 2022, Harris & Anthis 2021, Hildt 2019, Königs 2025, Long 2022, Metzinger 2021, Mosakas 2020, Schwitzgebel & Garza 2015 and Schwitzgebel 2023. These are the works that would have engaged the other side.
- **Miscited authority.** §5 says "Danaher et al. (2017) survey the landscape of positions on AI moral consideration". The listed Danaher et al. (2017) is "Algorithmic governance: Developing a research agenda through the power of collective intelligence" (Big Data & Society), not such a survey. The uncited Harris & Anthis (2021) is the survey. The quoted phrase attributed to Formosa (2021), "artificial moral agents are infeasible with foreseeable technologies" (§3), comes from a paper on robot autonomy; the quotation was not located and is unverified.
- **Dossier: "§§4–5 (pp. 3–5)"; "§6 (pp. 5–6)".** Correct. The dossier's P1/P2 paraphrase is also exact, including "(either as agent or patient)" in P1, which matters: P1 applies the sentience requirement to moral *agency* too, and nothing argues for that.
- primary topic: ethics (unchanged, correct). A secondary `agency` tag is justified, because §§4, 6.3 and 7 are about artificial moral agency and where responsibility lies.
