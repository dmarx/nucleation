---
status: Read
paper: 'LIT-tmpqgb1s'
title: 'Floridi — Distributed morality in an information society'
version: 1
history:
- version: 1
  date: '2026-10-10'
  note: >-
    Read in full from the published version (Science and Engineering
    Ethics 19(3):727–743, the Springer PDF of 17 pages), which the owner
    supplied. I read the abstract and keywords, the introduction, all six
    sections and the conclusion, the acknowledgements, footnotes 1–10,
    Figures 1–4 and the 47 references. The text was extracted with
    `pdftotext -layout`. It reported syntax errors in some drawing
    operators, so I rendered pp. 729, 730, 732, 733 and 737 with `pdftoppm`
    and read Figures 1–4, and the logical symbols (∨, ¬, →, ◇) that the
    extraction garbles, from the images. Page numbers are the journal's.
    The first NOTE on this paper.
date: '2026-10-10'
summary: >-
  Distributed morality (DM) is the case where morally loaded actions of a
  multiagent system result from interactions among its members that are
  each morally neutral or negligible. The model is distributed knowledge:
  A knows P∨Q, B knows ¬P, and only the "supra-agent" AB knows Q. The paper
  models neutrality with two moral thresholds, which make environments
  fault-tolerant to small evils and inert to small goods, and it names the
  task of aggregating potential goods and fragmenting potential evils. It
  introduces "infraethics", the first-order framework of moral enablers
  (trust, privacy, transparency …) that is not morally good in itself. The
  analogy is not exact. Distributed knowledge combines different contents
  logically, while every example of DM sums contributions of one kind past
  a threshold, so what separates DM from a sum of actions is the threshold
  on moral evaluation, a parameter the paper leaves unspecified. No
  criterion of agency is applied to the supra-agent, and responsibility for
  DM, which Floridi & Sanders 2004 promised, is still not given.
---
<!-- inactive-ok-file: QUESTION-009 — Deferred; set aside, and cited to say what this paper does and does not supply for it -->
<!-- inactive-ok-file: CLAIM-010 — Rejected; the permissiveness objection, cited as history the paper's usage bears on -->
<!-- inactive-ok-file: THEORY-127 THEORY-tmpixb78 — Proposed; open, and cited as open, not leaned on -->
<!-- inactive-ok-file: LIT-391 LIT-737 — Deferred, unread; named as the group-agency and commons works this paper's cases touch, not leaned on -->

# NOTE-tmpiz7db: Floridi — Distributed morality in an information society

## Contribution

Floridi & Sanders 2004 ([LIT-tmpdg6qq](../literature.d/LIT-tmpdg6qq.md), [NOTE-tmpr4vy8](NOTE-tmpr4vy8.md)) named distributed
morality and said nothing more about it. This paper gives the term a
narrower scope and a model. DM covers only "cases of moral actions that are
the result of otherwise morally-neutral or at least morally-negligible …
interactions among agents constituting a multiagent system, which might be
human, artificial, or hybrid" (p. 729). The cases are kept apart from
collective responsibility so far as that "might" reduce to "the sum of
(some) human, individual, and already morally-loaded actions" (p. 729). The
model has two moral thresholds, which make neutrality an "attractor"
(p. 733). It names a programme of policy and design, aggregating potential
goods and fragmenting potential evils (p. 736). And it coins *infraethics*
for the morally non-good "ensemble of moral enablers" that make good or evil
more or less likely (pp. 738–740). What is new after it is a vocabulary
(moral threshold, moral inertia, fault-tolerance, moral enabler,
infraethics) and a statement of the phenomenon. It contains no result about
the phenomenon.

## Key insight

Below a threshold, an action makes no moral difference. So a whole can do
good or evil that none of its members does, without anyone's acts being
more than negligible. "Can 'big' morally-loaded actions … be the result of
many, 'small' morally-neutral or morally-negligible interactions? I hold
the answer to be yes" (p. 729). The same thresholds make environments
forgiving: a speeder's possible evil fails to happen "thanks to the
resilience of the overall environment" (p. 732). They also make
environments inert: small goods stay neutral unless something adds them up.
The ethical work is therefore partly the design of what does the adding up.
"Big issues call for big agents" (p. 742).

## Assumptions

- **A three-valued moral classification of actions.** Every action a is
  E(a), G(a) or N(a), "following common practice" (p. 729). The →-arrows
  that move actions between classes "are not formulae but mere
  abbreviations", and a deontic-logic treatment "would be cumbersome and
  provide no further insights" (fn. 2, p. 729).
- **Moral thresholds exist, and their value can be left open.** "Once we
  model the applications of (iii) and (iv) as being constrained by some
  thresholds the value of which can be left unspecified here, we obtain …
  moral inertia" (p. 731). How actions become morally significant is "a
  serious difficulty … Luckily, all this need not concern us here" (p. 731).
- **A receiver-side evaluation at a minimal LoA.** Because the multiagent
  systems "might be totally mindless", the paper adopts "a uniform,
  minimalistic level of abstraction (Floridi 2008b) such that even human
  individuals might be treatable as mindless agents". Actions are then
  assessed "not from a sender but rather from a receiver perspective … on
  the basis of their impact on the well-being of the environment at large
  and its inhabitants" (p. 732).
- **Good and evil are given.** The inquiry into infraethics "does not seek
  to uncover the morally good and evil, but rather presupposes a
  satisfactory understanding of both" (p. 739).
- **Morally good values and their infraethics can be separated**, though
  only as "an abstraction that never occurs in reality but that facilitates
  our analysis here" (p. 739).

## Key results

The paper proves nothing and reports no data beyond illustrative figures.
It offers a model drawn in Figures 1–3, four examples, a policy programme
and a definition.

### The analogy (p. 729)

A knows only P∨Q ("the car is in the garage or Jill got it"), and B knows
only ¬P. "Neither A nor B knows that Q, only the supra-agent (with 'supra'
as in 'supranational') C = AB knows that Q" (p. 729). Footnote 1 qualifies
this: "C is the agent that is perceived to know that Q at the level of
abstraction at which we do not have A and B as observables". The moral
counterpart is stated in one sentence. A causes {a₁, …, aₙ} and B causes
{b₁, …, bₙ} "to the effect that the supra-agent C causes a set of actions
{c₁, …, cₙ}" (p. 729). No aggregation rule for actions corresponds to the
pooling of information. The sources cited are Halpern & Moses 1990 and
Fagin et al. 1995.

### The old scenario (pp. 729–731, Figs. 1–2)

- The *deontologist* demotes G→N, since good done from heteronomous motives
  loses its moral value (i). The *intentionalist* demotes G→N and E→N
  ("great, but was not meant"; "sad, but was not meant"), (i) and (ii). The
  *consequentialist* promotes N→G and N→E, (iii) and (iv), because "all
  actions have consequences" (p. 730).
- Left unchecked, (iii) and (iv) leave no neutral actions. Floridi calls
  that "too implausible to be acceptable" (p. 730). The fix is the *morally
  negligible*, effects "too small to be morally significant or [that]
  mutually cancel each other" (p. 731). It is modelled as two thresholds,
  which turn the C-arrows into "vectors … [with] a strength, which needs to
  be sufficiently high" (p. 731, Fig. 2).
- *Moral inertia*: "most actions are morally neutral and tend to stay that
  way", because of the thresholds, the I-tendency or the D-tendency,
  according to the theory one holds (p. 731).

### The new scenario (pp. 731–734, Fig. 3)

- Inside N sit ◇Evil (possibly evil) and ◇Good (possibly good). Possible
  evils that stay below threshold show that environments are "morally
  resilient", that "goodness … is fault-tolerant" (p. 732). Possible goods
  that stay below threshold show that environments are "morally inert …
  potential goodness can be too weak to become actual goodness" (p. 733).
- An action is neutral because it is (a) "morally-unloaded", (b)
  "insufficiently morally-loaded (have some moral value, but still fail to
  overcome the threshold)", or (c) because such actions "mutually off-set
  each other" (p. 733).
- "Unless A and B interact properly, their distributed action remains below
  the threshold of the morally negligible … neutrality works as a powerful
  attractor … it is only by aggregating and merging individual courses of
  action that a moral difference is made" (p. 733).
- Aggregation "is not one-way". Evils reached through DM can be aggregated
  further into good, and goods into evil (pp. 733–734). Floridi credits the
  point to Durante (fn. 4).

### Examples (pp. 734–736)

The tragedy of the commons is called "a classic and well-known example of
negative DM", and it is not discussed, with a reference to Greco & Floridi
2004 (p. 734). There are four positive cases, "all based on quantitative
analyses, in terms of moral benefits that can easily be quantified
economically" (p. 734). They are (RED) cause-marketing, the Co-operative
Bank's charity credit cards (£3 million to Oxfam, 1994–2007), JustGiving,
and peer-to-peer lending (marketplace and community models). The
conclusion adds fourth-generation bikesharing: "no component of the system
in itself would make any difference, and if only a few users were to take
advantage of it, the environmental benefits would be virtually null"
(p. 741).

### Harnessing DM (pp. 736–738)

The opportunity is to strengthen "environmental resilience and
fault-tolerance, while weakening inertia" (p. 736). That needs ethical
policies of (a) *aggregation* of possibly good actions and (b)
*fragmentation* of possibly evil ones, "isolated, parcelled and
neutralised". These are furthered by (c) incentives and disincentives,
which are not expanded on, and (d) "technological mechanisms that work as
'moral enablers'" (p. 736). ICTs are "a most influential enabling factor
behind the emergence of DM", which is why DM is witnessed "really only in
advanced information societies" (p. 736). But ICTs "are not (at least not
yet) designed in such a way as to meet the serious challenge" (p. 737).
Peer-to-peer technology can push neutral actions over either threshold.
The remedies proposed are a better understanding of "the logical dynamics
of DM", civil education, better design of "technological moral
aggregators", and improved incentives (pp. 737–738).

### Infraethics (pp. 738–740)

- It is introduced by analogy with a failed state. Such a state has lost
  "an implicit 'socio-behavioural infrastructure'" (p. 738) as well as its
  structures. Correspondingly, "the morally good behaviour of a whole
  population of agents is also a matter of 'ethical infrastructure' or
  infraethics" (p. 738).
- **Definition** (p. 738): "not as a kind of second-order ethical discourse
  or metaethics, but as a first-order framework of implicit expectations,
  attitudes, and practices that can facilitate and promote morally good
  decisions and actions. Examples include trust, respect, reliability,
  privacy, transparency, freedom of expression, openness, fair competition,
  and so forth." Footnote 9 separates the term from Jonsen & Butler's 1975
  "infraethics", a level of inquiry into public ethics.
- **Not good in itself** (p. 739): "Even a society in which the entire
  population consisted of angels … needs norms for collaboration", and "a
  society in which the entire population consisted of Nazi fanatics could
  rely on high levels of trust, respect, reliability, privacy, transparency,
  and even freedom of expression". "The best pipes may improve the flow but
  they do not improve the quality of the water" (p. 739).
- **The question** (p. 739): "given a dynamic, moral system in which DM
  plays a significant role, what is the right infraethics that can foster
  it?"
- **What an enabler is** (p. 740). Enablers are not meta-values ("values
  qualifying other values") and not infra-values ("values that underpin
  other values"). They are "intra-components of the moral system,
  metaphorically comparable to the lubricant of the moral machinery. They
  work at the same level as moral values, neither below nor above them …
  even if they themselves are not moral values." Logically, they may be
  represented in modal semantics "as agents in themselves, which operate
  between possible worlds", blocking transitions to morally worse worlds
  and fostering transitions to better ones (p. 740).
- **Conclusion** (p. 741): "an information society is a better society if
  it can implement an array of moral enablers … Agents (including, most
  importantly, the State) are better agents insofar as they … foster the
  right kind of moral facilitation".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Morally loaded actions of a multiagent system can result from interactions that are each morally neutral or negligible | moderate, given thresholds | it follows from the threshold model once thresholds are granted (p. 733). The examples (pp. 734–736) illustrate it |
| C2 | DM is the moral counterpart of distributed knowledge | weak | one example of distributed knowledge, and one sentence stating the moral counterpart without an aggregation rule (p. 729). See Limitations |
| C3 | DM is not the sum of individual morally loaded actions | weak | stipulated by the definition (p. 729). Category (b), "have some moral value, but still fail to overcome the threshold" (p. 733), lets in sums of slightly loaded actions, so the line between DM and the excluded cases is the threshold, whose value is left unspecified (p. 731) |
| C4 | Moral thresholds make environments fault-tolerant to small evils and inert to small goods | moderate, as a model | the speeding and charity cases (pp. 732–733). This restates the thresholds and adds no independent evidence |
| C5 | Managing DM requires aggregating possible goods, fragmenting possible evils, incentives, and moral enablers | weak | proposed as a programme (p. 736). Fragmentation is never illustrated |
| C6 | ICTs are what make DM common and salient, so it characterises advanced information societies | weak | asserted (pp. 736, 741), supported by one Eurostat series (Fig. 4) and the four cases |
| C7 | There is a first-order infraethics of moral enablers that are not morally good in themselves | moderate as a distinction, weak as a thesis | the failed-state analogy and the Nazi and angels thought experiments (pp. 738–739). The paper concedes that the separation "never occurs in reality" |
| C8 | Moral enablers sit at the same level as moral values without being values | assertion | p. 740, the "lubricant" metaphor. Several listed enablers (privacy, transparency, freedom of expression, fair competition) are ordinarily counted as values, and the conclusion says conflicts among them (privacy against transparency) need priority-ordering (p. 741). The paper does not say how that is non-moral |
| C9 | Enablers can be modelled as agents operating between possible worlds | assertion | one paragraph (p. 740); no semantics is given |

## Concepts

- **Distributed morality (DM)**: moral actions of a multiagent system that
  result from interactions among its members that are morally neutral or
  negligible (p. 729). In the introduction it is "the macroscopic and
  growing phenomenon of global moral actions and non-individual
  responsibilities, resulting from the 'invisible hand' of systemic
  interactions among multiagent systems … at a local level" (p. 728). This
  is the 2004 wording, with "collective" changed to "non-individual".
- **Supra-agent**: the agent C = AB to which the aggregate is attributed,
  at the LoA where A and B are not observables (p. 729, fn. 1).
- **Multiagent system (MAS)**: any human, artificial or hybrid system
  treated as a source of morally loaded action. The examples are "you and
  I, … webbots …, a corporation, an individual driving a car with the help
  of a GPS, or a drone-network-pilot-command system" (pp. 731–732).
- **Morally negligible; moral threshold; moral inertia**: the three
  concepts from the old scenario (p. 731).
- **Moral resilience / fault-tolerance; moral inertia of environments**:
  potential evil and potential good, respectively, staying below threshold
  (pp. 732–733).
- **Aggregation; fragmentation**: the two policies (p. 736).
- **Moral enabler**: a non-moral factor that facilitates morality and
  hinders immorality (p. 738). A **moral hinderer** is its opposite (p. 741).
- **Infraethics**: the first-order framework, or ensemble, of moral enablers
  (pp. 738–739).
- **Universalization** (fn. 3, pp. 732–733): "the normative coordination of
  the possibly good, distributed actions of a multiagent system", which
  agents "ought to implement, optimise and coordinate … so as to make them
  converge on the achievement of a morally good output".

## Connections

**Floridi & Sanders 2004 ([LIT-tmpdg6qq](../literature.d/LIT-tmpdg6qq.md), [NOTE-tmpr4vy8](NOTE-tmpr4vy8.md)).** "I introduced the
concept of distributed morality (DM) in (Floridi and Sanders 2004)"
(p. 728). Three things come from that paper: mind-less moral agency, the
receiver-side LoA at which humans too are "mindless agents" (p. 732), and
the threshold idea. In 2004 the threshold was a function on observables
held within a tolerance ([NOTE-tmpr4vy8](NOTE-tmpr4vy8.md), p. 20 of the preprint); here it is
a boundary between moral classes, and it is not formalised. The `extends`
on the LIT holds: the paper's subject is that paper's named but undeveloped
concept, and its agents are that paper's mind-less agents. **Does it
deliver what 2004 promised?** In part. [NOTE-tmpr4vy8](NOTE-tmpr4vy8.md)'s C9 was that the
approach "makes distributed morality intelligible", and that it was
"promised … and only named". This paper does make the phenomenon
intelligible: it gives a definition, a mechanism (thresholds and
aggregation) and examples. The 2004 conclusion, though, sold the
enlargement as a way to "stop the regress of looking for the *responsible*
individual". On that the paper says nothing. Responsibility appears in the
definition ("non-individual responsibilities", p. 728) and in one verdict,
on the speeder. None of the 2004 machinery is used: interactivity, autonomy
and adaptability, criterion (O), the split between accountability and
responsibility. The allocation of responsibility for DM is left to Floridi
2016 ([LIT-tmplkm3o](../literature.d/LIT-tmplkm3o.md), Deferred), whose title, "moral responsibility for
distributed moral actions", names the gap. A reading of that paper should
start from here.

**The method of abstraction ([LIT-tmpqbvu8](../literature.d/LIT-tmpqbvu8.md), [NOTE-tmpnwh69](NOTE-tmpnwh69.md)).** Cited twice, in
fn. 1 for the supra-agent's knowledge and at p. 732 for the minimal LoA. As
in Floridi 2025 ([NOTE-tmpu5qjn](NOTE-tmpu5qjn.md)), the LoA is the analyst's, not the system's.
No observables are named and no relation between LoAs is used. The paper
would read the same without the citation, so no `extends` to Floridi 2008
is written.

**Floridi 2025 ([LIT-tmp6juhh](../literature.d/LIT-tmp6juhh.md), [NOTE-tmpu5qjn](NOTE-tmpu5qjn.md)).** That paper cites this one in a
single sentence, as part of Floridi's answer to responsibility gaps.
Read now, this paper does not answer responsibility gaps; it describes how
outcomes without culpable parts arise. The 2025 citation therefore points
to the 2016 paper's work more than to this one's.

**Social ontology and group agency.** The distributed-knowledge example is
the epistemic face of List & Pettit's supervenience result ([THEORY-127](../theory.d/THEORY-127.md);
*Group Agency*, [LIT-391](../literature.d/LIT-391.md), unread). The group's attitude to Q is fixed by its
members' attitudes to *other* propositions (P∨Q, ¬P), and no member holds
it on Q itself. Floridi does not cite List & Pettit and does not take the
step their result forces: once a group's attitudes are formed from its
members' whole sets, which aggregation is used matters, and it can make the
group depart from what every member holds. In DM the aggregation function
is never specified (see Limitations). List 2016 ([LIT-401](../literature.d/LIT-401.md), [NOTE-340](NOTE-340.md))
grants group agency only to organised groups with an attitude-forming
structure. Floridi's "supra-agent" is any pair at an LoA that hides its
members, a much thinner notion.

**The commons.** The tragedy of the commons is Floridi's paradigm of
negative DM (p. 734), on Hardin's model. The record's reading of Ostrom
([LIT-719](../literature.d/LIT-719.md), [NOTE-563](NOTE-563.md); *Governing the Commons*, [LIT-737](../literature.d/LIT-737.md), unread) argues
against Hardin's tragedy as a general model. On that evidence, local
institutions of monitoring, sanction and communication avert it. In
Floridi's terms these are infraethics and fragmentation policies. The
paper does not cite Ostrom. Her design principles are the kind of empirical
content about moral enablers that the paper says is missing ("The lack of
similar studies about … an infraethics is understandable", p. 739).

## Bearing on the record

- **[QUESTION-009](../questions.d/QUESTION-009.md)** (when is coordination an additional agent?). The
  paper treats the question as already answered. It calls C = AB a
  "supra-agent" by fiat, and fn. 1 makes C's knowledge an artefact of an LoA
  that hides A and B. It also calls a corporation, a GPS-assisted driver,
  the State and even moral enablers "agents" (pp. 731–732, 740–741). No
  criterion from Floridi & Sanders is applied, so the paper does not bear on
  the question beyond showing how freely the line uses the word. The
  enablers-as-agents passage (p. 740) is the most permissive use of "agent"
  in the line so far. It is the permissiveness objection
  ([CLAIM-010](../claims.d/CLAIM-010.md)) accepted rather than met.
- **The distributed-agency line ([CLAIM-030](../claims.d/CLAIM-030.md), [CLAIM-045](../claims.d/CLAIM-045.md), [CLAIM-060](../claims.d/CLAIM-060.md)).** DM
  is a claim about the moral *value* of a whole's actions, not about the
  whole's direction or intention. It is compatible with [CLAIM-030](../claims.d/CLAIM-030.md) and
  provides no evidence for it. The thresholds are not "systemic mechanisms
  that may evolve … divorced from the intentions of lower level agents".
  They are features of the evaluation. Two points touch [CLAIM-060](../claims.d/CLAIM-060.md). The
  receiver perspective assesses actions by "impact on the well-being of the
  environment at large and its inhabitants" (p. 732), so the members are
  among the patients. And the remark that aggregation "is not one-way"
  (pp. 733–734), that goods reached through DM can be aggregated into
  evil, is close to [CLAIM-060](../claims.d/CLAIM-060.md)'s point that an organisation's success and
  its constituents' good come apart. It is stated in one sentence and not
  developed.
- **[ADR-024](../decisions.d/ADR-024.md)** (agent, individual, self, person). The paper's "agent"
  carries no implication of individual, self or person, and "supra-agent"
  carries none of individuality. A document that cites it should not take
  "big agents" (p. 742) to mean unified individuals.
- **[THEORY-tmpixb78](../theory.d/THEORY-tmpixb78.md)** (agency is multiply realisable without mental
  states). This paper gives that theory no support beyond Floridi & Sanders.
  It assumes mind-less agents from the start ("any talk of beliefs, desires,
  intentions and motivations would be merely metaphoric", p. 732) and
  argues nothing about them.
- **No THEORY is filed from this reading.** The record's practice for the
  comparable conceptual readings in this line is not to file one: none for
  Floridi & Sanders 2004 ([NOTE-tmpr4vy8](NOTE-tmpr4vy8.md)), none for Floridi 2008 ([NOTE-tmpnwh69](NOTE-tmpnwh69.md)),
  none for ISR ([NOTE-099](NOTE-099.md)). The paper offers a model and a coinage, not a
  claim about the world with evidence that a THEORY could carry. If the
  record later states a theory of moral thresholds or of infraethics, this
  paper is its source, C1 and C7 are its support, and C3 is its liability.
- No instruction for machine-learning practice. Its "artificial agents" are
  webbots, and its technologies are P2P and Web 2.0.

## Limitations

- **The analogy is not exact, at three points.**
  1. *What is combined.* Distributed knowledge combines *different*
     contents (P∨Q and ¬P), and the result follows from them logically.
     Neither member knows Q to any degree. Every DM example combines
     contributions *of one kind* (pounds, purchases, loans, bike rides) that
     are summed until a threshold is crossed. Each contribution already has
     a little of the aggregate's value: category (b), "some moral value". So
     the examples are sums, and what makes them DM rather than a sum of
     actions is only that the moral evaluation is a step function of the
     summed impact. The non-additivity is in the evaluation, not in the
     actions. A case closer to the analogy would be one where heterogeneous
     neutral acts are jointly sufficient for a harm that no sum of them, act
     by act, approaches. The paper offers none.
  2. *Whether interaction is needed.* In the cited semantics (Halpern &
     Moses; Fagin et al.), distributed knowledge is a property of the
     group's state. It is what someone would know who combined the members'
     knowledge, and it holds whether or not they communicate. The paper
     says instead that "unless A and B interact properly, their distributed
     knowledge cannot emerge" (p. 733), and its fn. 1 makes C's knowledge
     what is "perceived" at an LoA. This matters for the moral side. On the
     standard reading DM would be present wherever neutral acts are jointly
     sufficient. On Floridi's it needs an aggregator, and indeed all four
     positive examples are aggregators somebody designed (a brand
     programme, a card scheme, a platform, a marketplace). The definition's
     "invisible hand" (p. 728) fits the commons case and none of the
     examples.
  3. *No operator for actions.* Distributed knowledge has a definition (the
     intersection of the members' accessibility relations). "To the effect
     that the supra-agent C causes {c₁, …, cₙ}" (p. 729) has none, and fn. 2
     declines to give one.
- **DM's boundary is a free parameter.** Whether a case is DM or a sum of
  morally loaded acts (excluded, p. 729) depends on where the threshold
  lies, and that "can be left unspecified" (p. 731). A thousand £100
  donations, each above threshold, are not DM. A million 25p contributions,
  each below it, are. Nothing else separates them.
- **The receiver perspective is not kept.** Actions are to be assessed by
  impact on the patient, not by the agent's state (p. 732). Yet the speeder
  is "morally irresponsible not because of the effects of his action … but
  because of his unwarranted reliance on the fault-tolerance of the rest of
  the system" (p. 732). That is a verdict about the sender.
- **Fragmentation is named and never shown.** All the examples are of
  aggregation, the negative case is set aside, and no example is given of a
  possible evil "isolated, parcelled and neutralised" (p. 736).
- **The neutrality of enablers is weaker than the abstract says.** The
  abstract calls them "morally neutral per se". The body says only that
  infraethics "is not necessarily morally good in itself" (p. 739). It
  concedes that the separation from values "never occurs in reality"
  (p. 739), and it lists as enablers things ordinarily called values. It
  also cites Taddeo's treatment of trust "as a second order relation (and
  hence an enabler)" (p. 740) in the paragraph that warns against reading
  enablers as meta-values. Whether a given enabler's neutrality survives
  once its effects are known is not asked.
- **No account of responsibility or accountability for DM** (see
  Connections).
- **Small slips in print.** EndNote placeholders survive in the citations
  "Hildebrandt 2008, 2011, [#93](https://github.com/dmarx/nucleation/issues/93)" (p. 727) and "Pagallo (2012, [#92](https://github.com/dmarx/nucleation/issues/92))" (p. 738).
  The text gives "in 2011, 20.7 %" for laptop internet access away from
  home or work (p. 737), but Fig. 4 plots 2007–2010 only and ends at about
  17.5 %, with a chart title ("via wireless") narrower than its caption. In
  Fig. 3 the "threshold of fault-tolerance" is drawn on the Good side, while
  the text makes fault-tolerance the failure of possible *evil* (p. 732).
  None of this affects the argument.

## Open questions

- Is there a case of DM in the strict sense the analogy suggests, where
  heterogeneous, individually neutral acts combine non-additively into a
  morally loaded one, as P∨Q and ¬P combine into Q? If there is, DM is more
  than threshold-relative summation. If there is not, the analogy with
  distributed knowledge is decorative.
- What sets the threshold? Until something does, "morally negligible" and
  so "DM" are relative to an evaluator's choice, as Floridi & Sanders' LoAs
  are.
- Does the 2016 paper ([LIT-tmplkm3o](../literature.d/LIT-tmplkm3o.md)) keep distributed knowledge, or switch
  to common knowledge, as its abstract suggests? The two are at opposite
  ends of the group-knowledge hierarchy. Distributed knowledge is what the
  pooled group would know; common knowledge is what everyone knows that
  everyone knows, and so on. A rule that makes every causally relevant node
  responsible looks like it needs the second, so the change would be
  substantive.
- Is the supra-agent an agent by Floridi & Sanders' criteria (interactive,
  autonomous, adaptable at a stated LoA), or only a locus to which outcomes
  are attributed? This is [QUESTION-009](../questions.d/QUESTION-009.md) asked of this line's own central
  case.
