---
status: Read
paper: 'LIT-tmplkm3o'
title: 'Floridi — Faultless responsibility'
version: 1
history:
- version: 1
  date: '2026-10-10'
  note: >-
    Read in full from the published version (Phil. Trans. R. Soc. A
    374: 20160112, 13 pp., the Royal Society's typeset PDF), supplied by
    the owner; no open copy had been reachable when the work was
    registered. I read the abstract, §§1–6, all 23 footnotes, the
    acknowledgements, the competing-interests and funding statements and
    the 33 references. Text was extracted twice with `pdftotext`, once in
    reading order and once with `-layout`, because the footnotes and the
    margin column interleave with the body in the reading-order text;
    every quotation below was placed on its page from the layout text.
    Pages 5 and 7 were rendered with `pdftoppm` to read Figures 1–3 (the
    finite-state automaton's transition table and graph, and the
    neural-network picture of a society). Page numbers are the article's
    own, 1–13. The first NOTE on this paper.
date: '2026-10-10'
summary: >-
  When a morally loaded outcome C emerges from morally neutral
  interactions in a network of agents, nobody intends C, so an ethics
  that makes intention necessary assigns no responsibility for it.
  Floridi proposes to allocate it anyway: identify C and the network
  causally accountable for it, then make every node "prima facie equally
  and maximally responsible" (p. 7), overridable by showing no
  involvement, with the rule made common knowledge so that agents
  restrain one another. Back propagation, strict liability and common
  knowledge are borrowed as inspiration, and the paper says so. Two Dutch
  Supreme Court cases illustrate it. The argument is by design, not
  derivation. "Responsibility" here is causal accountability turned
  into a forward-looking corrective signal, which is what Floridi &
  Sanders 2004 called accountability and kept apart from responsibility.
  The paper never addresses that distinction, and in one of its own two
  examples the default is overridden by ease of rectification, which is
  a control criterion, not a causal one.
---
<!-- inactive-ok-file: QUESTION-009 — Deferred; set aside, and cited as the question this paper sidesteps -->
<!-- inactive-ok-file: CLAIM-010 — Rejected; the permissiveness objection, cited because the paper's causal criterion meets its form again -->
<!-- inactive-ok-file: LIT-742 LIT-391 LIT-698 — Deferred, unread; named as group-agency and collective-responsibility work the record holds but has not read -->
<!-- inactive-ok-file: THEORY-131 THEORY-139 THEORY-147 THEORY-118 THEORY-122 — Proposed; named as the record's corporate-responsibility and responsibility accounts this one is set beside -->
<!-- inactive-ok-file: THEORY-tmpixb78 THEORY-tmphi5o9 — Proposed; the line's agency account, and the record's statement of this paper's account, filed from this reading -->

# NOTE-tmpkq4jw: Floridi — Faultless responsibility

## Contribution

The paper gives a rule for allocating responsibility for a distributed moral action (DMA). A DMA is a morally good or evil outcome brought about by interactions that are each morally neutral, in a network whose agents may be human, artificial or hybrid. Before it, Floridi's line had the phenomenon, named in Floridi & Sanders 2004 ([LIT-tmpdg6qq](../literature.d/LIT-tmpdg6qq.md)) and analysed in Floridi 2013 ([LIT-tmpqgb1s](../literature.d/LIT-tmpqgb1s.md)), and no account of who answers for it. The rule is this. Identify the outcome and the network causally accountable for it. Then hold every node in it fully responsible by default, regardless of fault or intention. A node can override the default by showing it was not involved. The rule is publicised so that agents restrain one another before the outcome occurs. The paper proposes this rule and shows that law already uses something like it. It does not show that what it allocates is moral responsibility in any sense its predecessor would recognise.

## Key insight

Responsibility here is a training signal, not a verdict. The paper's own picture is a neural network (Figure 3, p. 7). Society maps history to an outcome by forward propagation, and responsibility is propagated backward to every node so that the output improves on the next pass. The one thing the nodes must be is learners: "The only assumption required is that the agents causally accountable can learn from, and modify, their behaviour" (p. 6). Once responsibility is a corrective signal sent to learners, intention drops out, because a signal works whatever its receiver meant. Fairness drops out too, which is why the first objection has to be met by biting a bullet. The paper says so: the attribution "is meant to play a significant role in preventing evil and fostering good, not in blaming or punishing agents for their morally unsuccessful actions" (p. 10).

## Assumptions

- **Moral neutrality is a threshold.** "By morally neutral, I mean here either not morally charged at all or below a threshold of moral relevance (virtually amoral)" (fn 11, p. 3). The local interactions in a DMA are below that threshold, and the outcome is above it.
- **An axiology is given.** "All we need to assume is that, according to an axiological analysis, some states of the system are morally better than others" (p. 6). In the sandbox it is stipulated: S1 is evil, S2 and S3 are neutral, S4 is good (p. 6). Floridi's own axiology is in The Ethics of Information (2013), which the record does not hold, and it is not used here (fn 14, p. 6).
- **Causal accountability can be fixed.** Steps (a) and (b), identifying the DMA and the network causally accountable for it, "are conceptually uncontroversial, although their implementation may be challenging in practice, and perhaps sometimes just impossible" (p. 7). The theory of causation is left "to a future work" (fn 15, p. 6). There Floridi inclines to causation as "sufficientization" at a level of abstraction chosen for a purpose, the approach of Floridi 2008 ([LIT-tmpqbvu8](../literature.d/LIT-tmpqbvu8.md)), and close to Hart & Honoré's "purpose of the inquiry" (fn 15).
- **The nodes are agents in Floridi & Sanders's sense, and learners.** They must be autonomous, interactive and able to "learn from their interactions (can change the rules according to which they behave …)". These are given as "three necessary and sufficient conditions", with Floridi 2013 (the book) and Floridi & Sanders 2004 cited for "a detailed analysis" (p. 7). The paper adds that agents so described "give rise to a multi-layered neural network that can learn its appropriate internal representations and hence any arbitrary mapping of input … to output (DMA)" (p. 7). That is a universal-approximation claim made of societies, and it is asserted, not argued.
- **Society's error correction exists.** The social counterpart of weight updates is "hard and soft legislation, rules and codes of conducts, nudging, incentives and disincentives; in other words, through social pushes and pulls" (p. 7).

## Key results

The paper has no formal result. It offers an argument against the received view, a five-step procedure, two legal cases, and replies to two objections and two challenges.

### Why standard ethics misses DMR (§2, pp. 3–4)

- **Neutral actions can combine into loaded ones.** Ethics usually treats moral value as monotonic: "if actions a and b are morally neutral, then their combination C = a + b not only does not but cannot acquire a negative or positive moral value" (p. 3). The tragedy of the commons is the counterexample (p. 3).
- **Intention is not closed under causal implication** (p. 4). Directly: ¬[[[A means to cause a] ∧ [a causes b]] → [A means to cause b]]. Distributively: ¬[[[A means to cause a] ∧ [B means to cause b] ∧ [a ∧ b cause C]] → [AB means to cause C]].
- **The seven steps** (p. 4). Classic ethics allocates individual punishments and rewards (1), so it attributes individual responsibility (2), so it needs individual intention, since otherwise allocation would be "indistinguishable from a mere random allocation" (3). But C is not intended (4), so no one is responsible for C (5) or can be fairly punished or rewarded for it (6), so standard ethics "either ignores DMAs and responsibilities or seeks to reduce both to non-distributed versions of individual morality of intentional actions" (p. 4).
- **The diagnosis.** The mistaken premise "is that the ethical discourse should focus entirely and only on the intentional nature of actions" (p. 3). It is to be complemented, not abandoned: intention "may still be very relevant, but it is no longer a necessary condition" (p. 4).

### The sandbox (§3, pp. 4–6)

A four-state finite automaton with three inputs (Figures 1–2, p. 5). The text calls it "not a model …, a blueprint … or a thought experiment" but "a simplified environment to test some ideas" (p. 5). It separates three foci of ethics: the agent (virtue ethics), the action (deontology and consequentialism) and the patient, meaning the state of the system (environmental ethics). "With an analogy, the ethical discourse may focus on the cook, on the cooking or on the cooked" (p. 6). The conclusion drawn is that "an ethics of state transitions, independent of the intentions of the agents involved, can provide a full account of DMR" (p. 6). After this the automaton is used only once, for the remark that the mechanism could as well move the system from S4 to S1 (p. 9). Its work is to show that states can carry value whatever anyone intended, and it shows no more than that.

### The mechanism (§4, pp. 6–9)

The procedure (p. 7):

- (a) identification of the DMA Cₙ;
- (b) identification of the network N causally accountable for Cₙ (forward propagation);
- (c) back propagation of moral responsibility to make each agent in N prima facie equally and maximally responsible for Cₙ;
- (d) correction of Cₙ into Cₙ₊₁; and
- (e) repetition of (a)–(d) until Cₙ₊₁ is axiologically satisfactory.

Three glosses carry the rest:

- **Responsibility in the aetiological sense.** Allocating it "means focusing on which agents are causally accountable for (i.e. contributed genetically to bring about) a morally distributed action C, rather than whether agents are fairly commendable or punishable for C". It is talking about "'responsibility' in the aetiological sense of being the source of (causally accountable for) a state of the system, and therefore, as a consequence, of being morally answerable (blameable/praisable) for its state" (p. 6). It "may lead to, but it is independent of, legal liability" (p. 6).
- **Default and override.** Step (c) "is the mechanism of 'responsible by default' or poena sine culpa" (p. 8). "Step (d) may require an overridability clause. Some nodes may share different degrees of responsibility, including none at all, if an agent is able to show no involvement in the interactions leading to C" (p. 8). The override is attached to (d) in the text, though it qualifies (c).
- **Prevention by common knowledge.** Step (e) may be unnecessary "if the presence of back propagation of DMR is known to all the agents involved" (p. 8). Common knowledge of p in a group is the infinite hierarchy of everyone knowing that everyone knows that p. It is reached by public announcement (p. 8). Floridi takes this to be "the substantive aspect in which DMR is very different from collective responsibility" (p. 8).

**Responsibility stays with the nodes.** Strict liability in criminal law gave rise to corporate liability, and Floridi declines that route: "I intend to keep the same scope of applicability (all individual agents involved), not shift it (the network). Here, faultless responsibility remains 'theirs' (agents') not 'its' (network's)" (p. 8). On the same page as the procedure, the network is treated "as accountable for it", and responsibility is back-propagated "to all its nodes/agents" (p. 7).

### The two examples (pp. 8–9)

Both come from Dutch case law. Radboud Winkels supplied them at JURIX 2015 (acknowledgements, p. 12).

- **Three cyclists.** Dutch traffic rules allow two cyclists abreast. When a third joins, the Supreme Court ruled "that each of them is to be held entirely responsible, because it is very easy for each of them to rectify the situation (HR 9 March 1948, NJ 1948, 370)" (p. 9).
- **Four boats.** Up to three boats may moor abreast on the Merwede. When a fourth moored, the Court ruled "that only the fourth ship was responsible, because it was much more difficult for the other three to rectify the situation than for the fourth that joined them (HR 19 January 1931, NJ 1931, 1455)" (p. 9). Here "the back propagation identified only one agent as responsible, even if the DMA required all four of them to occur" (p. 9).

The lesson drawn: "understanding and insight will need to be exercised when back propagating strict forms of DMR" (p. 9). A third, hybrid example, Wikipedia's bots (about 15% of edits in 2014), is named and deferred: "It will be the topic of another article" (fn 20, p. 9).

### Features, objections, challenges (§5, pp. 9–11)

- **Feature 1: uncommitted.** The mechanism is neutral about axiology. "It can work even to 'invert' a good outcome" (p. 9).
- **Feature 2: infraethics.** The mechanism is part of a society's infraethics, "the ethical infrastructure that, although not morally good or evil in itself, can facilitate or hinder actions that lead to good or evil states" (p. 9).
- **Objection 1: unfair.** "It is reasonable" (p. 10). The reply has two parts. Sometimes the allocation "is tragic, that is, it is indeed unfair". This is the bullet, softened by Honoré's "outcome responsibility" (p. 10). Otherwise the lack of intention is "(at least partially) counterbalanced by the presence of common knowledge" of the rule (p. 10). Footnote 22 concedes that this ignores the different costs agents bear for defecting from the network.
- **Objection 2: unrealistic.** "We already apply a blunt version of back propagation of strict DMR" when we blame leaders for what their subordinates do. The proposal only spreads this more finely, and "the more people who are going to be deemed responsible for some evil, the more likely it is that some of them will call for more caution to be exercised" (p. 10).
- **Challenge 1: uneven risk aversion.** Prudent agents adapt and imprudent ones free-ride on them, as reckless drivers do on careful ones (p. 10). There are three remedies (p. 11). Individual responsibility for conduct already loaded, such as reckless driving, remains. Incentives can be graded between the boats and the cyclists, "by identifying circumstances in which DMR is back propagated proportionally to the ability of the agents to avoid the negative outcome". And prudent nodes can bring social pressure on the rest.
- **Challenge 2: chilling.** If every node is fully responsible, "nobody would use the commons, just in case using it even once led to full responsibility for its depletion" (p. 11). The remedies offered are insurance-like incentives and, in ethics, "moral hedging" through "proactive care of the system affected" (p. 11).

### Conclusion (p. 11)

"Too often 'distributed' turns into 'diffused': everybody's problem becomes nobody's responsibility." The proposal back-propagates all responsibility to each causally relevant agent "independently of the degrees of intentionality, informed-ness and risk aversion of such agents (faultless responsibility)". It shifts ethics "from an agent's interest to a patient's harm": "Our world may not need an ethics for Paradise and individual sins, but it definitely needs an ethics for Eden and environmental risks" (p. 11).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Morally loaded outcomes can arise from morally neutral interactions | strong | the tragedy of the commons and the cyclists (pp. 3, 9); given the threshold definition of neutrality (fn 11), it is close to definitional |
| C2 | Intention is not closed under direct or distributed causal implication | strong | stated with two schemata (p. 4); uncontroversial |
| C3 | An ethics that makes intention necessary cannot allocate responsibility for DMAs | weak | the seven steps (p. 4) go from "C is not intended" to "no one is responsible for C". They skip the standard grounds that need no intention to cause the outcome: negligence, recklessness and knowing participation. The paper names "unintended consequences" only as a familiar phenomenon (p. 2) |
| C4 | Moral evaluation of states needs no information about agents' intentions | moderate | the sandbox and the three foci (pp. 5–6); it needs a given axiology, which is stipulated |
| C5 | Responsibility for a DMA should go by default, equally and maximally, to every causally accountable node, overridably | proposal | a design argued by analogy (p. 7) and by legal precedent (pp. 8–9); "more an inspiration than a template" (p. 3) |
| C6 | Common knowledge of the rule prevents DMAs and partly answers the unfairness | weak | asserted (pp. 8, 10). No evidence, and no account of why common knowledge rather than knowledge of the rule is needed |
| C7 | The mechanism is more realistic than the practice of blaming leaders, and allocating more widely raises caution | assertion | p. 10. An empirical claim with no evidence offered |
| C8 | Law already back-propagates strict responsibility | moderate | the two Dutch cases (p. 9) and strict liability for animals, products and nuclear plants (p. 8, fn 18). In the boats case the allocation goes by ease of rectification, which is not causal |
| C9 | The paper's "responsibility" is moral and not merely legal liability | assertion | "morally answerable (blameable/praisable)" is said to follow "as a consequence" from causal accountability (p. 6). Nothing is given for the step |

## Method

Conceptual design in information ethics. A received view is reconstructed as an argument (§2). A toy formal environment shows what a non-intentional ethics would assess (§3). A mechanism is assembled by analogy from three fields (§4), illustrated by case law, and defended against objections (§5). The paper calls this "a design perspective" (p. 11). Nothing is computed with the automaton or the network. Both are illustrations.

## Concepts

- **Distributed moral action (DMA)**: a morally loaded (good or evil) action caused by local interactions that are morally neutral, among agents that may be human, artificial or hybrid (abstract; p. 2). Defined in Floridi 2013, which this paper does not rehearse (p. 2).
- **Distributed moral responsibility (DMR)**: responsibility for a DMA (p. 2). It differs from collective responsibility, "a whole group of people … held responsible for some of its members' morally loaded … actions" (p. 2), in two ways: the nodes' actions are neutral, and the rule is publicly announced (p. 8).
- **Faultless responsibility (strict moral responsibility)**: full responsibility allocated by default to each causally relevant node, whatever its intention. A reviewer suggested the name, and the text mostly keeps "strict" (fn 8, p. 3).
- **Responsibility, aetiological sense**: being the causal source of a state of the system, and "as a consequence" morally answerable for it. It is distinguished from legal liability and from responsibility as being in charge (p. 6).
- **Back propagation**: here, assigning responsibility from the outcome back to every node in the network that produced it. In the paper's own description of real networks, weights are adjusted "by finding the derivative of error with respect to each weight" (p. 7). The social version has no derivative. Every node gets the same full share.
- **Strict liability**: "the legal responsibility of one or more agents for the damage or loss caused by their acts or omissions, regardless of their culpability", defined "in terms of intentionality of the action, possibility to control it and lack of excuse" (p. 8). Floridi uses it in the causal sense, not the risk-allocation sense (fn 9, p. 3).
- **Common knowledge, public announcement**: as in epistemic logic, p known by all, known by all to be known by all, and so on. It is reached by an announcement perceivable by all (p. 8). It is distinguished from knowledge of the law (fn 19, p. 8).
- **Infraethics**: ethical infrastructure, neither good nor evil itself, that makes good or evil states easier or harder to reach (p. 9).
- **Agent-, action- and patient-oriented ethics**: the three "points of 'pressure'" (p. 6).

## Connections

**Within the line.** The paper describes itself and Floridi 2013 ([LIT-tmpqgb1s](../literature.d/LIT-tmpqgb1s.md), [NOTE-tmpiz7db](NOTE-tmpiz7db.md)) as "a diptych, but they do not presuppose knowledge of each other" (fn 4, p. 2). This paper takes DMAs from the 2013 paper and adds the allocation of responsibility for them, the gap [NOTE-tmpiz7db](NOTE-tmpiz7db.md) found that paper left open. It keeps the 2013 threshold of moral neutrality (fn 11) and infraethics (p. 9). It drops two things. The 2013 model was distributed knowledge, with a "supra-agent" AB that alone knows Q. Neither distributed knowledge nor the supra-agent appears here. Responsibility goes to the nodes and not to any supra-agent (p. 8). The epistemic operator now used is common knowledge, at the other end of the group-knowledge hierarchy, and it does a different job. In 2013 it modelled how a DMA arises. Here it serves prevention, by making the rule known. This answers [NOTE-tmpiz7db](NOTE-tmpiz7db.md)'s open question: the change is substantive, and the paper does not remark on it. The 2013 speeder, who relies on others' fault-tolerance, comes back as the reckless motorway driver who free-rides on careful ones (p. 10). From Floridi & Sanders 2004 ([LIT-tmpdg6qq](../literature.d/LIT-tmpdg6qq.md), [NOTE-tmpr4vy8](NOTE-tmpr4vy8.md)) it takes the agent conditions (interactive, autonomous, adaptive; p. 7, citing [24]) and the programme of "mindless morality" (pp. 4, 8; the phrase is credited to the 2013 book). Its single reference to levels of abstraction (p. 6, citing Floridi 2008, [LIT-tmpqbvu8](../literature.d/LIT-tmpqbvu8.md), [NOTE-tmpnwh69](NOTE-tmpnwh69.md)) is to a scenario in which nothing about agents is observable, and fn 15 relativises causation to an LoA. It does not cite the 2004 paper's distinction between accountability and responsibility, and it does not use it. See Limitations.

**Borrowings, and whether each carries its weight.**

- *Back propagation (network theory).* What it contributes is a picture: outcome forward, correction backward, iterated until satisfactory. That picture explains why the nodes must be learners. It does not supply the method that makes back propagation back propagation, which is credit assignment in proportion to each weight's contribution to the error. Step (c) gives every node an equal and maximal share, which is close to the opposite. The proportional allocation that the paper reaches only as a remedy for risk aversion ("proportionally to the ability of the agents to avoid the negative outcome", p. 11) is the part nearest the borrowed idea. The borrowing works as an organising metaphor, and it tells against the paper's own default.
- *Strict liability (jurisprudence).* What it contributes is a precedent for liability without proof of fault, and with it a reply to the charge that faultless responsibility is incoherent. Floridi limits the borrowing himself: strict liability is "only … a source, and not … an importable concept" (fn 7, p. 3). It carries less than the text suggests. Legal strict liability attaches to a designated party: a keeper, a manufacturer, a plant operator (p. 8, fn 18). Its standard justification is that this party took on or controls a risk, which is the risk-allocation sense fn 9 sets aside. It does not attach to everyone causally involved. Footnote 18 also contradicts its own first sentence: "In cases of strict liability, the defendant is allowed to prove that he or she is innocent, which then leads to an exemption of liability." Both Dutch rulings give their reason in terms of how easily each party could rectify the situation (p. 9). That is a control criterion. The cyclists get full and equal shares because each had easy control, not because each was a cause.
- *Common knowledge (epistemic logic).* What it contributes is the prevention step and half of the reply on fairness. Prevention needs agents to know the rule, and coordinated restraint might need each to expect the others to know it. The infinite hierarchy is more than either requires, and the paper does not say why it is needed. The concept also cuts against the paper's own label. An agent who joins an interaction knowing that it will be held fully responsible for the outcome has foreseen the risk, so publication reintroduces a knowing-participation ground of fault. That is how it answers the unfairness objection. When the rule is common knowledge, responsibility is no longer quite faultless. Without it, the allocation is the "tragic" case. Either way, common knowledge does the fairness work only by bringing back what the label "faultless" excludes. The paper says it is "at least partially" a counterbalance (p. 10), and fn 22 concedes the unequal costs of defection.

**Outside the line.** Honoré's outcome responsibility (Responsibility and Fault, 1999) is cited as the closest philosophical relative (p. 10), and the record does not hold it. Of the collective-responsibility works cited (French & Wettstein, French, May, May & Hoffman, Olson), the record holds none of these titles. It holds French's "The Corporation as a Moral Person" ([LIT-727](../literature.d/LIT-727.md), [NOTE-568](NOTE-568.md)), which the paper does not cite. It also holds, unread, List & Pettit's Group Agency ([LIT-391](../literature.d/LIT-391.md)), Pettit's Responsibility Incorporated ([LIT-742](../literature.d/LIT-742.md)) and Isaacs on collective guilt ([LIT-698](../literature.d/LIT-698.md)), the collective-responsibility literature the paper's DMR is set against (p. 2). The tragedy of the commons comes from Hardin 1968 and 1998, and from Greco & Floridi 2004 on the digital commons.

## Bearing on the record

- **[QUESTION-009](../questions.d/QUESTION-009.md) (when a pattern of coordination is an additional agent).** The paper sidesteps the question. A society is "correctly interpreted as being equivalent to a multi-layered neural network" (p. 2), and the network is "accountable" for the DMA (p. 7). But responsibility is allocated to the nodes, explicitly not to the network (p. 8). The network is therefore treated as the source of an output without being made an agent or a bearer of responsibility. In Floridi & Sanders 2004's own terms, if the network met the three conditions as a whole it would be an agent at some LoA, and nothing here asks whether it does. Floridi 2013 had named a "supra-agent" as the bearer of distributed knowledge ([NOTE-tmpiz7db](NOTE-tmpiz7db.md)). This paper drops it, and so retreats from the nearest the line came to treating the pattern as an additional agent. The paper gives no evidence for or against an answer to [QUESTION-009](../questions.d/QUESTION-009.md). It shows only that one line of responsibility practice can proceed without one.
- **The distributed-agency line, [CLAIM-030](../claims.d/CLAIM-030.md) (a whole's operative intention is not the expectation of its members' intentions).** The paper's premise agrees with [CLAIM-030](../claims.d/CLAIM-030.md): a DMA is what the network outputs, not what any member intended, and "it no longer matters which agent does what or why" (p. 7). It then draws the allocation the other way from the record's corporate-responsibility readings. French ([LIT-727](../literature.d/LIT-727.md), [THEORY-131](../theory.d/THEORY-131.md)) and Pettit ([LIT-718](../literature.d/LIT-718.md), [NOTE-569](NOTE-569.md), [THEORY-139](../theory.d/THEORY-139.md)) make the organised whole a bearer of responsibility because it has a decision structure or a mind of its own. Floridi keeps responsibility with the members because the whole has no intention. The two can both stand: Pettit says the corporation and its members can be responsible in their own domains. They answer different questions. Pettit asks whether the whole is fit to be held responsible; Floridi asks what the parts answer for when nothing is anyone's fault. One shared assumption is worth recording: both treat holding responsible as regulative, Pettit's "regulative practice" ([NOTE-569](NOTE-569.md)) and Floridi's corrective signal.
- **What responsibility requires.** Against [THEORY-121](../theory.d/THEORY-121.md) (Fischer and Ravizza: moral responsibility requires guidance control), the paper denies nothing. Its responsibility is a different thing, allocated without asking about the agent's mechanism. Its closest neighbour in the record is Wolf's distinction ([THEORY-147](../theory.d/THEORY-147.md), [LIT-747](../literature.d/LIT-747.md)) between attributability and accountability as independent kinds of responsibility. Floridi's faultless responsibility is a third kind, causal answerability used to correct. It needs neither attributability nor fitness for the reactive attitudes. The record should not cite this paper as an argument about moral responsibility in the sense [THEORY-118](../theory.d/THEORY-118.md) to [THEORY-122](../theory.d/THEORY-122.md) discuss.
- **Graduated sanctions ([THEORY-149](../theory.d/THEORY-149.md), Ostrom).** The paper's chilling challenge (p. 11) is the commons case. The record's Active account of durable commons governance ([LIT-719](../literature.d/LIT-719.md)) singles out user-monitored rules and graduated sanctions. That is evidence that the institutions which last sit between the boats and the cyclists, nearer the proportional remedy than the full-and-equal default. It bears on the promote_when of the THEORY filed from this reading.
- **[CLAIM-010](../claims.d/CLAIM-010.md) (permissiveness).** The causal criterion invites the same objection as the 2004 agent criteria. Footnote 11 grants that "Alice scratching her left foot may cause unspeakable evil if one can imagine the right chain of causes" (p. 3). The override clause, together with the causal theory deferred in fn 15, has to keep the causally relevant network from taking in everyone. The paper does not say how.
- **[ADR-024](../decisions.d/ADR-024.md).** The nodes are agents in the 2004 sense (interactive, autonomous, adaptive, and learners). Nothing here makes them persons or selves, and responsibility is allocated without personhood. A document citing this paper should not read "responsible agent" as "person".
- **The line's agency account ([THEORY-tmpixb78](../theory.d/THEORY-tmpixb78.md)).** The paper offers nothing on agency itself. It assumes the 2004 conditions, adding that the nodes learn, and it says nothing about intelligence. What it gives Floridi 2025 ([LIT-tmp6juhh](../literature.d/LIT-tmp6juhh.md)) is a way to allocate responsibility for outcomes of human–AI networks without first settling whether the artificial nodes intend anything.
- **A THEORY is filed** ([THEORY-tmphi5o9](../theory.d/THEORY-tmphi5o9.md)), Proposed, as the record did for the comparable corporate-responsibility readings ([THEORY-131](../theory.d/THEORY-131.md) from French, [THEORY-139](../theory.d/THEORY-139.md) from Pettit). It states the allocation rule and what the paper actually supports, and leaves open whether the result is moral responsibility.
- No instruction for machine-learning practice. "Back propagation" is a metaphor for society, and nothing here is about training networks.

## Limitations

- **"Responsibility without fault or intention" is not shown to be moral responsibility.** The paper defines its responsibility as causal accountability "and therefore, as a consequence, … morally answerable (blameable/praisable)" (p. 6). Nothing supports the "therefore". It then says the attribution is for prevention, "not … blaming or punishing" (p. 10). So the blame and praise asserted on p. 6 are disowned on p. 10, and what is left is a forward-looking corrective assignment. That is legitimate, and it is what the paper argues for. It is liability or role-assignment in a moral setting, and calling it "full moral responsibility" (abstract) is a choice of name the paper does not defend.
- **It collapses Floridi & Sanders 2004's distinction without saying so.** The 2004 paper made accountability the property of being the source of a morally qualifiable action, and responsibility the further property that needs "the right intentional states" ([NOTE-tmpr4vy8](NOTE-tmpr4vy8.md), C6). The 2016 paper's "responsibility in the aetiological sense of being the source of (causally accountable for)" (p. 6) is the 2004 paper's accountability, almost word for word. It goes under the other name and comes with the praise and blame that 2004 reserved for responsibility. Either the 2016 paper revises 2004 or it equivocates on "responsibility". It never mentions the distinction, although it cites the 2004 paper on the same page (p. 7). Read through 2004, faultless responsibility is distributed accountability, plus a publicised rule that makes accountable learners correct.
- **The default does not survive its own examples.** The cyclists case has the default and the boats case has it overridden. The override does not go by involvement, which is the only override clause stated (p. 8), since all four boats were involved. It goes by ease of rectification. The criterion actually decisive in both cases is control, and the paper's later remedy, allocation in proportion to "the ability of the agents to avoid the negative outcome" (p. 11), makes it the general rule. On that rule, responsibility is no longer "equally and maximally" distributed, and it is no longer independent of what the agents could do.
- **"Causally accountable" is left unfixed.** Steps (a) and (b) are called "conceptually uncontroversial" (p. 7), while the theory of causation is deferred (fn 15). Which nodes are in N is the whole question for a default that gives each of them everything.
- **The case against standard ethics is too quick** (C3). Negligence, recklessness and foreseen side effects already hold agents responsible for what they did not intend, and the seven steps pass over them. A weaker conclusion follows: intention-of-the-outcome is not necessary. Most standard accounts already grant that.
- **Empirical claims are not evidenced.** Wider allocation raises caution (p. 10), common knowledge prevents DMAs (p. 8), and the equilibrium between prudent and imprudent agents can be corrected (p. 11). The paper offers no evidence for any of these, and the chilling challenge (p. 11) is raised against them and not answered.
- **The hybrid case is deferred.** Wikipedia bots are named and postponed (fn 20). The artificial and hybrid nodes in the abstract appear nowhere in the argument. Both examples involve only humans.
- **Slips.** The roadmap numbers the sections §1–§4 (p. 2), but the headings run §2–§5. "Prevents an evil DMR from being outputted" (p. 8) should read DMA. "Pubic announcement" appears in fn 19. Footnote 18 contradicts itself (see Connections). The FSA's set of acceptable states F is defined and never used (p. 5).

## Open questions

- What does "moral" add to faultless responsibility once the paper disowns blame and punishment (p. 10)? An answer would name one thing that moral faultless responsibility licenses and that publicised strict liability with an override for non-involvement does not. This is [NOTE-tmpr4vy8](NOTE-tmpr4vy8.md)'s open question about accountability, asked again of the later paper.
- Is the 2004 distinction between accountability and responsibility revised or abandoned? Neither later paper says. Floridi 2013 uses none of the 2004 machinery ([NOTE-tmpiz7db](NOTE-tmpiz7db.md)), and the 2016 paper uses the 2004 accountability under the name of responsibility without mentioning the split.
- What criterion fixes the network N and the override? A stated criterion would put the boats and the cyclists on the sides the Dutch court did, and would do so before the cases are known. A criterion that turns out to be control or ease of rectification would show that "faultless" responsibility is, in practice, allocation by capacity to prevent.
- Does full and equal allocation under common knowledge reduce harm more than graduated allocation does? [THEORY-149](../theory.d/THEORY-149.md)'s evidence on graduated sanctions is the nearest the record has. Floridi's challenges predict that full allocation leads to free-riding and chilling. A comparison of regimes, joint and several liability against proportionate liability for example, would settle which.
