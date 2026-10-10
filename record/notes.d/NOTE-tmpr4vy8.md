---
status: Read
paper: 'LIT-tmpdg6qq'
title: 'Floridi & Sanders — On the morality of artificial agents'
version: 1
history:
- version: 1
  date: '2026-10-10'
  note: >-
    Read in full from the authors' preprint in the University of
    Hertfordshire repository (uhra.herts.ac.uk/id/eprint/2235, 29 pp.,
    self-numbered 1–29, digitally signed by Floridi on 2004-01-30, and
    post-review, since it thanks the Minds and Machines referees). The
    PDF's fonts are Type 3 with no text layer, so I read the text from
    rendered page images, all 29 pages: the abstract, §§1–5, the
    acknowledgements, footnotes 1–7, Figures 1–3 and the 37 references.
    The preprint does not show the published pagination (Minds and
    Machines 14(3):349–379). I did not see the published text beyond the
    Springer landing page, whose abstract matches the preprint's. Page
    numbers below are the preprint's.
date: '2026-10-10'
summary: >-
  Agenthood is fixed only at a level of abstraction (LoA). At the LoA the
  paper proposes, an agent is interactive, autonomous and adaptable, and a
  moral agent is any agent that can cause moral good or evil. Accountability
  (being the source of the action) needs no mental states; responsibility
  (praise and blame) needs intentional states. So artificial agents and
  organisations can be accountable moral agents without being responsible.
  The case is made by examples and by rebutting four objections. Its own
  MENACE example shows that agenthood vanishes when the LoA is lowered to
  include the code. The paper leaves that LoA-relativity unbounded, says
  only that "for most entities there is no LoA at which they can be
  considered an agent" (p. 26), and promises a payoff for distributed
  morality that it does not deliver.
---
<!-- inactive-ok-file: LIT-tmpqgb1s — Floridi 2013, distributed morality, filed unread in the same contribution; named as the paper that takes up what this one promises -->
<!-- inactive-ok-file: QUESTION-009 — Deferred; the open question this paper offers an answer to -->
<!-- inactive-ok-file: CLAIM-010 — Rejected; the permissiveness objection, cited as the objection this paper's criteria meet -->
<!-- inactive-ok-file: LIT-126 — Rejected on its close reading; cited for the sentientist premise this paper is the standard alternative to -->
<!-- inactive-ok-file: LIT-742 — Deferred, unread; Pettit's case for corporate responsibility, named as the contrast -->

# NOTE-tmpr4vy8: Floridi & Sanders — On the morality of artificial agents

## Contribution

The paper gives a criterion for agenthood that mentions no mental states, together with a method for saying where the criterion applies. Agenthood is judged at an explicit level of abstraction, a chosen set of observables. At the LoA the paper proposes, an agent is a transition system that is interactive, autonomous and adaptable. It then separates being a moral agent from being morally responsible. On this account artificial agents, animals and organisations can be accountable sources of moral good and evil without being responsible. Before it, the artificial-moral-agent debate mostly asked whether machines could have the mental states responsibility needs. The paper declines that question and calls its subject "mind-less morality" (p. 1).

## Key insight

"Is X an agent?" is not well posed until you say what you are observing. Fix the observables and the question gets an answer. Change them and the answer can change: MENACE, which learns noughts and crosses, is an agent when you watch a tournament of its games, and it is not one when you can see its matchboxes (pp. 11–12). The paper treats this as a feature. Moral agency is then a further question about the same observed system: can its actions cause good or evil? Whether it can be blamed is a third question, and the only one that needs a mind.

## Assumptions

- **The system is a transition system** at the chosen LoA: a non-empty set S of states, with transitions that may take input and give output (external) or neither (internal) (p. 8). "With the explicit assumption that the system under consideration forms a transition system, we are now ready to apply the Method of Abstraction" (p. 8).
- **The LoA is chosen, and chosen well.** "Since human beings count as standard moral agents, the right LoA for the analysis of moral agenthood must accommodate this fact" (p. 9). The LoA is calibrated so that humans pass, and it is then applied to everything else. The paper does not say what makes an LoA adequate beyond this and a list of modelling virtues (p. 7).
- **LoA-relativity is pluralism, not relativism**, because LoAs "are mutually comparable and assessable" (p. 7). The defence is deferred to the authors' 2003 chapter on the Method of Abstraction, reference [18], which the record does not hold.
- **Moral good and evil are given.** Criterion (O) and the threshold function both take as given what counts as moral good or evil. The tolerance "is identified by human agents exercising ethical judgements" (p. 20).
- **Freedom means nondeterminism plus the practical counterfactual.** "The AAs are already free in the sense of being non-deterministic systems", and that "is also sufficient for our purposes" (p. 17).

## Key results

The paper proves nothing and contains no formal result. What it offers are definitions, a table of cases and arguments.

### Definitions (§§2.2–2.5)

- **LoA**: "a finite but non-empty set of observables" (p. 7). An observable is a typed variable together with a statement of the feature it represents (p. 6). An **interface** is a collection of LoAs, called a "gradient of abstractions" in [18] (p. 7). A lower LoA includes a higher one's observables. The translation relations of the gradient-of-abstractions formalism (see [NOTE-099](NOTE-099.md)) are not used here.
- **Agent at LoA₁**: a system, situated in and part of an environment, that initiates a transformation in it. At this LoA "there is no difference between Jan and an earthquake" (p. 9).
- **The three criteria** (p. 9). (a) *Interactivity*: the agent and its environment "(can) act upon each other". (b) *Autonomy*: it can "change state without direct response to interaction", by internal transitions. (c) *Adaptability*: "the agent's interactions (can) change the transition rules by which it changes state". The source given for the three is Allen, Varner & Zinser (2000).
- **Criterion (O)** (p. 15): "An action is said to be morally qualifiable if and only if it can cause moral good or evil. An agent is said to be a moral agent if and only if it is capable of morally qualifiable action."
- **Accountability and responsibility** (p. 21): "An agent is morally accountable for x if the agent is the source of x and x is morally qualifiable … To be also morally responsible for x, the agent needs to show the right intentional states (recall the case of Oedipus)."
- **Threshold** (p. 20): a function of the observables at an LoA. An agent is morally good if it keeps the function within a pre-agreed tolerance at all times. Examples: distance from the patients' desired well-being, for the thermostat; the count of misfiled emails, for the webbot; T(M) ≤ T₀(M), games until MENACE never loses, for MENACE.

### Cases (§2.6, Figure 2)

All eight combinations of the three criteria are given at one LoA, a video camera running for 30 seconds: rock (none); pendulum (autonomous only); closed ecosystem and solar system (autonomous and adaptable); postbox and mill (interactive only); thermostat (interactive and adaptable); "juggernaut" (interactive and autonomous); human (all three). No example is given for adaptable only. After MENACE come a spam-filtering webbot, a "futuristic" hospital thermostat, SmartPaint and organisations. Each is an agent at some LoA and not at another.

### MENACE at three LoAs (pp. 11–13)

At the *single-game LoA* it is interactive and autonomous but not adaptive. At the *tournament LoA* it is adaptive, "and hence an agent". At the *system LoA*, where the boxes are observed, the apparent change of rule is "a simple deterministic update of the program state", and "MENACE fails to be an agent". Hence: "if a transition rule is observed to be a consequence of program state then the program is not adaptive" (p. 12). The paper ties this to software practice. Closed, downloaded code calls for the LoA at which the software is an agent, and "only since the advent of applets … has the issue of moral accountability of AAs become critical" (p. 13).

### Four objections (§3.2)

- *Teleological*: an AA has no goals. Dismissed, since LoA₂ "could readily be … upgraded to include goal-oriented behaviour". It is left out on purpose, because a non-teleological level helps with distributed morality (p. 16).
- *Intentional*: dismissed, since intentional states are "a nice but unnecessary condition" for moral agenthood, and access to them presupposes "a God's eye perspective". Agents should be judged moral "if they do play the 'moral game'" (p. 16).
- *Freedom*: met by nondeterminism and the practical counterfactual (p. 17).
- *Responsibility*: "the only one with real strength" (p. 17). The reply is that the objection reduces "all prescriptive discourse to responsibility analysis", which the paper calls "a juridical fallacy" (p. 19). Parents morally evaluate children who are not yet responsible. Search-and-rescue dogs are moral agents that are not responsible. "Oedipus is a moral agent without responsibility" (p. 19).

A fifth objection, "does this enlargement … bring any real advantage?", is answered in the conclusion (p. 26). Its benefits: "We can stop the regress of looking for the *responsible* individual when something evil happens", and "Promoting normative action is perfectly reasonable even when there is no responsibility but only moral accountability".

### Computer ethics (§4)

The "traditional" view, that only human programmers are accountable, is said to meet "insurmountable difficulties": team construction, off-the-shelf components, maintenance, automated tools, probabilistic and adaptive code (p. 22). All 16 imperatives of the ACM Code except "improve public understanding" make sense for AAs (p. 22). Censure maps the human ladder (social censure, isolation, death) onto maintenance, "removal to a disconnected component of Cyberspace" and "annihilation from Cyberspace (deletion without backup)" (p. 24). The paper compares this ladder with Norton AntiVirus, and ends by suggesting "agencies for the policing of AAs".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Agenthood can be settled only relative to an explicit LoA | moderate | argued from the general point that definitions are LoA-relative (Turing's test as the model, p. 5), with the MENACE case as illustration; the method itself is deferred to [18] |
| C2 | At the right LoA, agenthood is interactivity, autonomy and adaptability | weak | proposed as "guidelines" and "an effective characterisation", not a definition (pp. 3, 9); calibrated so that humans pass, and justified by the table of cases. No argument excludes rival criteria |
| C3 | Humans, learning software, webbots and organisations are agents at a suitable LoA | moderate | follows from C2 once the LoA is granted; the organisation case is one paragraph (p. 14) |
| C4 | Whether software is an agent depends on whether its code is observed | strong, on the paper's terms | the MENACE analysis (pp. 11–13), which is the most careful argument in the paper |
| C5 | Moral agency does not require intentional states, free will or responsibility | moderate | the replies to the intentional, freedom and responsibility objections (§3.2), resting on the dogs, children and Oedipus cases |
| C6 | Accountability (source of a morally qualifiable action) is necessary but not sufficient for responsibility, which needs intentional states | moderate | stipulated as a distinction (p. 21), motivated by the Oedipus case (p. 19) |
| C7 | An H/W pair indistinguishable at LoA₂ shows that the class of moral agents must include AAs | weak | "So can you tell the difference? If you cannot, you will agree with us" (p. 15). An imitation-game argument at an LoA chosen to leave out what the objector says matters |
| C8 | Morality at an LoA is a threshold function on the observables | weak | definitional. The tolerance is set by human judgement (p. 20), so the formalism names where the values go but supplies none |
| C9 | The approach makes distributed morality intelligible | assertion | promised at pp. 3 and 16 ("This will become clearer in the conclusion") and only named at p. 27 |
| C10 | For most entities there is no LoA at which they are agents | assertion | "Of course. Otherwise one might be reduced to the absurdity of considering the moral accountability of the magnetic strip that holds a knife to the kitchen wall" (p. 26). No argument limits which LoAs are admissible |

## Method

Conceptual analysis in computer ethics. The formal vocabulary of observables, LoAs and transition systems comes from Formal Methods ("for the purposes of this paper no mathematics is required", p. 6). It is applied to constructed and real examples (MENACE, a webbot, SmartPaint), and the conclusions are defended against objections.

## Concepts

- **Level of abstraction (LoA)**: a finite non-empty set of observables at which a system is analysed. The result of the analysis is a *model* (pp. 6–7).
- **Interface**: a collection of LoAs (p. 7). In this paper it is not the gradient-of-abstractions structure with translation relations.
- **Transition system; external and internal transitions**: an external transition takes input or gives output, and an internal one does neither. Which is which depends on the LoA: "At a lower LoA an internal transition may become external" (p. 8).
- **Autonomy**: change of state without stimulus, by internal transition. It needs at least two states (p. 9). This is not the Kantian sense of autonomy, and not self-governance.
- **Adaptability**: change of the transition rules through interaction. At a given LoA it is distinguished from change of state (§2.6.2).
- **Moral agent**: an agent capable of morally qualifiable action (O). "Moral agent" here does not imply person, self or responsible party.
- **Accountability and responsibility**: accountability belongs to the source of a morally qualifiable action. Responsibility adds intentional states, and with them makes praise and blame appropriate.
- **Mind-less morality**: the study of moral agency that sets aside mental states (p. 1).
- **Distributed morality**: "global moral actions and collective responsibilities resulting from the 'invisible hand' of systemic interactions among several agents at a local level" (p. 3). The term is named here and defined no further.

## Connections

The three criteria are taken from Allen, Varner & Zinser (2000), and the method from the authors' 2003 chapter. Neither is held. Turing ([LIT-394](../literature.d/LIT-394.md)) is the paper's model for fixing an LoA before asking a question (p. 5), and the "can you tell the difference" argument (p. 15) is an imitation game at LoA₂. The appeal to playing "the moral game", judged from observables and not from inner states, is close in spirit to Dennett's intentional stance ([LIT-440](../literature.d/LIT-440.md)), but the paper cites Dennett only for "When HAL kills, who's to blame?" (p. 26), and its criteria are behavioural-structural, not interpretive: no rationality is ascribed.

On organisations it differs from Pettit ([LIT-718](../literature.d/LIT-718.md), [NOTE-569](NOTE-569.md); [LIT-742](../literature.d/LIT-742.md)). Pettit makes corporations fit to be held responsible because they are conversable. Floridi & Sanders make organisations agents at an LoA and accountable, and keep responsibility for agents with intentional states. The paper is also the standard alternative to the sentientist premise that [LIT-126](../literature.d/LIT-126.md) asserts without argument ([NOTE-128](NOTE-128.md), its P1), namely that moral agency needs phenomenal consciousness.

Within Floridi's own work, the LoA method here is the same one used in informational structural realism ([LIT-152](../literature.d/LIT-152.md), [NOTE-099](NOTE-099.md)) and in the account of personal identity ([LIT-136](../literature.d/LIT-136.md), [NOTE-130](NOTE-130.md)), stated here informally and with fewer of the formal parts. The line's later papers build on two things in this one. The first is the separation of agency from intelligence and mind: "AAs, though not intelligent and fully responsible, can be fully accountable sources of moral action" (p. 3). That is the move the 2023 paper's title, "AI as Agency Without Intelligence", names ([LIT-tmp0pyws](../literature.d/LIT-tmp0pyws.md)). The second is the promised account of distributed morality, which Floridi 2013 takes up ([LIT-tmpqgb1s](../literature.d/LIT-tmpqgb1s.md)). The method of levels of abstraction in Floridi 2008 ([LIT-tmpqbvu8](../literature.d/LIT-tmpqbvu8.md)) generalises the 2003 chapter this paper defers to. This paper uses the method; it does not develop it.

## Bearing on the record

- **[QUESTION-009](../questions.d/QUESTION-009.md)** (when a pattern of coordination is an additional agent). The paper's answer: when, at some admissible LoA, the pattern is interactive, autonomous and adaptable. Organisations qualify (§2.6.6). The answer moves the question rather than settling it, because everything turns on which LoAs are admissible, and the paper offers only "for most entities there is no LoA" (p. 26). Its own Figure 2 shows how cheap the criteria are. The closed ecosystem and the solar system are already autonomous and adaptable at the video LoA, and fail only interactivity, which is an artefact of the 30-second window. Add their inputs to the LoA and they become agents.
- **[CLAIM-010](../claims.d/CLAIM-010.md)** (the permissiveness objection). The paper meets this objection's form, and its reply, that we choose an LoA, does not answer it. The record's own answer, agent-indexing ([CLAIM-080](../claims.d/CLAIM-080.md)), is different: it supposes the agent and asks how its efficacy is organised. Floridi & Sanders try to derive the agent from observables, which is the approach the record's paper set aside.
- **[ADR-024](../decisions.d/ADR-024.md)** (agent, individual, self, person). The paper keeps these apart in the way [ADR-024](../decisions.d/ADR-024.md) asks. Its agents are neither persons nor selves, and its "autonomy" is not self-governance. A document that cites it should not read "moral agent" as "person".
- **Distributed agency.** The organisation case is compatible with [CLAIM-030](../claims.d/CLAIM-030.md) and offers no evidence for it. The paper says nothing about how an organisation's direction relates to its members' intentions.
- **No THEORY is filed from this reading alone.** If the record later states a THEORY that agency, or moral agency, is LoA-relative, this paper is its source and C4 is the strongest support in it. Any such THEORY should carry C10 as an open liability.
- No instruction for ML practice. The "machine learning" in the paper (MENACE, Mitchell 1997) is an illustration of adaptability.

## Limitations

- **There is no bound on admissible LoAs.** Every verdict is "at a given LoA". The only check on choosing an LoA is that humans must come out as agents (p. 9). The paper gives no reason to prefer the tournament LoA, at which MENACE is an agent, over the system LoA, at which it is not. It says the commercial and open-source views "are at variance" (p. 13) and leaves them so.
- **The MENACE argument reaches humans too, and the paper does not apply it to them.** If adaptability fails whenever the rule is seen to follow from state, then a sufficiently low LoA on a human (the "Hobbesian" model the paper mentions at p. 20) would remove human agenthood by the same reasoning. The paper notes the Hobbesian dispute only for thresholds and does not ask whether its criterion survives it.
- **The text is inconsistent about adaptability.** p. 9: "if an agent's transition rules are stored as part of its internal state, discernible at this LoA, then adaptability follows from the other two conditions." p. 12: "if a transition rule is observed to be a consequence of program state then the program is not adaptive." These read in opposite directions, and the paper does not reconcile them.
- **Criterion (O) is very wide.** Any agent whose actions can cause good or evil is a moral agent. The MENACE ethics example ("The software behaves unethically if and only if it loses a game after a sufficient learning period", because the game might fail on the market, p. 20) shows that moral evil reduces to any outcome somebody disvalues.
- **The threshold adds structure, not content.** The tolerance is set by human judgement or consensus (p. 20). The claim that thresholds let responsibility "be separated and formalised" (p. 26) has not been made good: responsibility is separated by stipulation (p. 21), not by the threshold.
- **Distributed morality is promised and not delivered** (C9).
- **There are slips in the preprint.** The roadmap (pp. 3–4) describes six sections (examples in §4, threshold in §5, computer ethics in §6), but the body has five, with the examples in §2.6, the threshold in §3.3 and computer ethics in §4. The cases table is called "Figure 1" in the text (p. 10), but it is Figure 2. The ACM table is called "Figure 2" (p. 22), but it is Figure 3. Whether the published text corrects these was not checked.

## Open questions

- What makes an LoA admissible for attributing agency? An answer would need a principled constraint on observables, stronger than "humans must pass", that rules out the knife-strip magnet and the solar system while keeping MENACE at the tournament level. A constraint of that kind would turn C10 from an assertion into a result.
- Does accountability without responsibility do any normative work that causal role does not already do? The censure ladder (maintenance, disconnection, deletion) is also what we do to faulty tools. The paper admits as much: "We are not punishing them, anymore than one punishes a river when building higher banks" (p. 18). So it remains open whether calling the AA a moral agent adds anything.
- Can an organisation's agenthood at an LoA be squared with its members' agenthood at a lower LoA without double-counting? This is [QUESTION-009](../questions.d/QUESTION-009.md) again, and the paper does not raise it.
