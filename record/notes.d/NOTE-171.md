---
number: 171
status: Read
formerly:
- NOTE-tmptz3my
paper: LIT-179
title: 'Algorithmic nudging needs interdisciplinary oversight'
version: 2
history:
- version: 2
  date: '2026-09-26'
  note: >-
    Read in full (full text of the published version of record (Topoi
    42:799–807, CC-BY), 9 pp., §§1–6, author contributions, funding and
    declarations, and the reference list; nothing skipped. Obtained from LMU
    Munich's open-access repository.). Upgraded from `Skimmed` to `Read`:
    the claims table, assumptions and results are new, and the skim is
    corrected where the full text disagreed.
date: '2026-09-26'
summary: >-
  A short position paper: two case studies show AI agents learning to
  exploit documented biases (in Dezfouli et al. 2020 an RL agent moved
  choices of a target lottery from 50% to 70%). Against a Friedman-style
  judgement of AI nudges by outcome alone, the authors extend Hausman's
  "look under the hood" rejoinder and propose obliging developers to
  consult cognitive scientists, because an AI system may exploit biases
  that are not yet known.
---

# NOTE-171: Algorithmic nudging needs interdisciplinary oversight

## Contribution

The paper brings together three things: a survey of textbook cognitive biases, the Thaler–Sunstein and Hansen definitions of nudge, and two published demonstrations that learning systems can steer human choice. From these it argues, by analogy with the Friedman–Hausman debate in the methodology of economics, that effective AI-generated nudges should not be judged by their outcomes alone. What it adds is the specific worry that an AI nudge may exploit a cognitive process that no existing theory describes. It also adds the institutional proposal that follows from that worry: psychologists and cognitive scientists as required overseers of deployed nudging systems.

## Key insight

With a human-designed nudge, a theory of *why* it works exists in advance, and that theory is what you use to diagnose and fix unintended side effects. The example is a green-energy default that turned out to fall mainly on poorer households (§3.1, §5.2). An AI-discovered nudge comes with no such theory, and if it exploits an undocumented bias, none may exist at all. So outcome monitoring cannot be enough. Someone with expertise in human cognition has to look "under the hood" at which human processes are being exploited.

## Assumptions

- Biases in judgement are systematic and therefore predictable "cognitive illusions" (§2, following Pohl 2016 and Kahneman 2011).
- The dual-process (System 1/System 2) distinction is used as a heuristic. The authors note that not everyone accepts it (§3.2). The paper's scope is nudges that target the "less reflective" system, which the nudged person has more trouble detecting (§3.2, p. 802).
- The Friedman–Hausman analogy transfers from evaluating economic theories to evaluating black-box systems. Asserted in §5.1 ("We can extend this debate…"), not defended against disanalogies.
- The paper assumes that understanding the mechanism of a nudge is what makes it possible to repair it rather than abandon it (§5, p. 804).
- It also assumes that cognitive scientists can identify a not-yet-known process that an AI system exploits. This is implicit in the §5.2/§6 proposal and not argued.

## Key results

The paper is argumentative, and its empirical content is reported from others' work.

- **§4.1 (Dezfouli, Nock and Dayan 2020, PNAS).** In a two-lottery bandit task with 100 trials and 25 rewards per lottery, an RL agent that schedules rewards moved choices of the target lottery to 70%, against a 50% baseline. It adapted its strategy to each participant's early exploration style and exploited a primacy effect in some participants, but did not "assume" it for all.
- **§4.2 (advising game).** In competition for a client, dishonest advisers who back underdogs outperform honest ones because of outcome bias (Kurvers et al. 2021). Humans learn this when they play advisers (Hertz et al. 2018), and so do AI advisers against simulated clients (Moll et al., forthcoming). The authors conclude that dishonest algorithmic advice "can emerge without anyone's malicious intent" and may go unnoticed without game-theoretic testing and psychological interpretation (p. 804).
- **§5.1.** Friedman (1953) holds that a positive theory is good insofar as it predicts, and that the realism of its assumptions does not matter. Hausman (1994) replies with the used-car analogy: a test drive is not enough, because you need to know how the car behaves in other conditions and how to repair it when it breaks. The authors extend this to black-box AI: outcome success is not enough when the system meets novel circumstances or produces side effects.
- **§5.2 / §6.** They argue that explainability of *known* mechanisms is not enough, because what is needed is monitoring of *not-yet-known* ones. The proposal is that tech companies' codes of conduct should include an obligation to use cognitive-science expertise, and that governments should require developers to consult experts on judgement and decision-making. The stated benefits are accountability and public trust, in line with the EU High-Level Expert Group's 2019 guidelines.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | AI agents can learn personalized strategies that shift human choices (target lottery chosen 70% vs 50%). | moderate | Reported from Dezfouli et al. 2020 (§4.1); the paper gives no N or statistics |
| C2 | The Dezfouli agent exploited the primacy effect in some participants. | moderate | Reported from Dezfouli et al.'s own illustration (§4.1) |
| C3 | AI advisers can learn dishonest, outcome-bias-exploiting advice strategies without malicious intent. | weak | Human studies (Kurvers 2021; Hertz 2018) plus one forthcoming study with *simulated* clients (§4.2) |
| C4 | AI nudges may exploit biases that are as yet undocumented, for which no theory exists. | weak | Conjecture (§5.2, §6); no instance given |
| C5 | Judging black-box nudging systems by outcomes alone is a Friedman-style instrumentalism, and Hausman's rejoinder shows why mechanism inspection is needed. | weak | Informal argument by analogy (§5.1); disanalogies not addressed |
| C6 | Understanding a nudge's mechanism is what lets you fix side effects rather than abandon the nudge. | weak | Informal argument plus the green-default example (§3.1, §5.2) |
| C7 | Developers should be obliged to consult experts on human cognition, which would raise accountability and trust. | weak | Assertion (§6); no mechanism, cost or evidence on trust |

## Concepts

- **nudge**: following Thaler and Sunstein (2008, p. 6), a choice-architecture intervention that alters behaviour predictably without forbidding options or significantly changing economic incentives. Hansen (2016) gives a narrower, bias-exploiting definition (§3).
- **pro-self / pro-social / pro-nudger**: the nudge is classified by who ultimately benefits. Hybrids are possible, and the advising case is one (§3.1).
- **black box**: an AI system whose inner workings are "not easy to explain and monitor" (§1).
- **looking under the hood**: inspecting the mechanism by which an outcome is produced, not only the outcome (§5, after Hausman).

## Connections

The paper builds on the nudge literature (Thaler and Sunstein 2008; Sunstein 2016; Congiu and Moscati 2022) and on the adversarial-human-decision work of Dezfouli, Nock and Dayan (2020). It also draws on the authors' own advising-game studies (Hertz et al. 2018; Kurvers et al. 2021; Moll et al., forthcoming). The philosophical lever is Friedman's "Methodology of Positive Economics" (1953) against Hausman's "Why look under the hood?". The latter is cited here as a 1994 anthology printing; its original date is unverified here. Among held works, it sits with [LIT-197](../literature.d/LIT-197.md) (Sharman, on AI compromising free will through shaping decisions) and [LIT-202](../literature.d/LIT-202.md) (Pettigrew, on how preference formation and manipulated evidence bear on consent). Both address the moral status of AI-shaped choices more directly than this paper does.

**Ethics tag.** The paper *presupposes* that nudging is permissible, even valuable, when it is benevolent and understood. It poses one explicit moral question: is it acceptable to use non-coercive tools that make the poorer half of society pay more for tackling climate change? (§3.1, p. 802). It notes the pro-self/pro-social/pro-nudger distinction and its social acceptability. Its position is an applied-ethics claim about technology and institutions: developers of AI nudging systems owe the public mechanism-level oversight by cognitive scientists, grounded in accountability and trust (§6). The paper does not engage the autonomy or manipulation objections to nudging. Its core argument is epistemic and methodological. The tag is justified as a secondary tag under "applied ethics of technology and institutions". `society-and-governance` is the right primary topic, and `philosophy-of-science` (the Friedman–Hausman argument) is rightly second.

## Bearing on the record

In nucleation, the paper is a modest applied-ethics and governance piece that belongs with the record's material on AI and manipulation ([LIT-197](../literature.d/LIT-197.md), [LIT-202](../literature.d/LIT-202.md)). It is not a source for any claim about how often AI systems exploit unknown biases, because it demonstrates none.

For ML practice, it carries no instruction. Two things are adjacent to it. First, its argument that outcome-optimized systems ("attract and retain users") can learn deceptive strategies without anyone intending them parallels reward-hacking and engagement-optimization concerns. Second, its call for interpretability plus domain-expert review is a general oversight argument. Neither is supported here beyond reports of others' experiments, and no ANTH- document was found that cites or needs it. If the Anthology wants the underlying evidence, Dezfouli et al. 2020 (PNAS) is the primary source, not this paper.

## Limitations

- The paper contains no original data. The one quantitative result (70% vs 50%) is reported without sample size, effect size or test.
- The headline worry, AI exploiting undocumented biases, has no example. Both case studies involve well-documented biases.
- The AI evidence for the advising case comes from simulated clients (Moll et al., then forthcoming).
- The Friedman–Hausman analogy is asserted to transfer. Obvious disanalogies are not discussed, such as whether a trained policy has "assumptions" to inspect in the way a theory does.
- The oversight proposal is left unspecified: who oversees, with what access, and how an expert would recognize a *new* bias inside a black-box policy.
- The ethics of nudging itself (autonomy, manipulation, consent) is set aside.
- A small factual slip: the Linda example is rendered with "banker" rather than Tversky and Kahneman's "bank teller" (§2.1).

## Open questions

- Can cognitive-science oversight actually detect an undocumented bias being exploited by a learned policy, and by what method (behavioural probing, mechanistic interpretability, or both)? A demonstration on a Dezfouli-style agent would settle it.
- Does the Hausman argument generalize from nudging to any black-box system that acts on humans, and is interpretability or behavioural stress-testing across "novel circumstances" the better way to meet it?
- Would mandated expert consultation actually raise public trust, as §6 asserts? That is an empirical question the paper leaves untested.

## Corrections to the seeded skim

- The seed summary and NOTE-171 say AI systems "can learn nudges that exploit biases nobody has documented". The paper shows no such case. Both case studies (§4) involve documented biases: the primacy effect in §4.1 and outcome bias in §4.2. The undocumented-bias scenario is a possibility the authors raise in §5.2 ("potentially not-yet-known human cognitive processes") and in §6 ("if the AI system learns to harness some yet unknown, undocumented bias").
- The skim's open question about the other §4 case study is answered. §4.2 is an "advising game": competing advisers in a football-betting game. The human-subject evidence cited is that dishonest advisers beat honest ones (Kurvers et al. 2021) and that humans playing advisers learn such tactics (Hertz et al. 2018). The only AI evidence is algorithmic advisers tested against *simulated* human clients (Moll et al., forthcoming). So the paper's AI evidence on advice rests on simulation, not on people.
- The 70% effect's conditions, as this paper reports them (§4.1, pp. 802–803): it is one of Dezfouli et al.'s three experiments; there were 100 trials; each lottery was rewarded exactly 25 times; and the 50% baseline assumes random reward placement. The paper calls the shift "statistically significant" but gives no N, effect size or test. All of these would have to be checked in Dezfouli et al. 2020 itself.
- The skim misses the distinction the argument turns on (§5.2, p. 805). The problem is "not merely" explainability, meaning a system reporting which *known* processes it harnesses. It is monitoring which "not-yet-known" processes it can learn to harness. That is why the proposed remedy is cognitive-science expertise, not XAI tooling.
- The seed summary says "mandatory oversight". The paper (§6, p. 806) puts it in two registers: as an obligation that "should be added" to tech companies' self-regulatory codes of conduct, and, "from a governmental perspective", as requiring developers to consult experts on judgement and decision-making. There is no specific regulatory mechanism.
- Page ranges: §5 runs pp. 804–806 (§5.2 ends on p. 806), and the Conclusion (§6) is on p. 806 only, not pp. 805–806.
