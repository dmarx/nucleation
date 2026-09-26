---
number: 161
status: Read
formerly:
- NOTE-tmprj4h0
paper: LIT-213
title: 'Cartwright — Rigour vs evidential diversity'
version: 2
history:
- version: 2
  date: '2026-09-26'
  note: >-
    Read in full (full text of the open-access (CC BY) publisher PDF,
    Synthese 199:13095–13119 (2021), 25 pp. (via rd.springer.com), read in
    full: §§1–5, footnotes 1–30, Fig. 1 caption and the partial key given in
    the text, acknowledgements and references. Fig. 1 itself is an image,
    and the paper says its full key is only in Cartwright et al. (2020),
    which I did not read.). Upgraded from `Skimmed` to `Read`: the claims
    table, assumptions and results are new, and the skim is corrected where
    the full text disagreed.
date: '2026-09-26'
summary: >-
  Cartwright offers a characterisation of "rigour": a method is rigorous
  when a valid argument shows its results are evidence for the conclusion
  and its premises are well established or secured by design. On that
  definition even well-run RCTs often fail to rigorously establish a
  study-population ATE, because orthogonality holds only at assignment and
  the potential-outcomes premise carries heavy metaphysics, and they
  seldom answer singular questions. Her alternative is a
  causal-process-tracing theory of change (pToC) with five elements
  (steps, causal principles, support factors, derailers, safeguards). It
  catalogues the diverse and mostly non-rigorous evidence that singular
  causal predictions need.
---

# NOTE-161: Cartwright — Rigour vs evidential diversity

## Contribution

The paper lists six contributions (§1). The two that are new are (i) a proposed explication of what "rigour" means in the evidence-based-policy and credibility-revolution sense, which is used to show that RCTs often fail their own standard, and (ii) a re-framing of mixed methods. The usual argument uses different methods, triangulating on one overall causal claim. Cartwright argues instead that a singular causal claim decomposes into many subsidiary claims about a causal process, and each needs a different kind of evidence. The pToC template catalogues those kinds. She concludes that rigour is "an overvalued virtue in evaluating evidence for causal claims" (§1, p. 13097). Rigour should be used where available but should not "dictate what methods can be used" (§5).

## Key insight

Betting that C will cause E *here* is betting that a particular causal process will carry through, step by step, in this setting. Each step needs a causal principle that holds and is triggered, its support factors present, and its derailers absent or blocked. Those are facts about this place, and no single method, least of all an RCT run on another population, can warrant them all. So good singular causal prediction takes a weave of diverse, mostly non-rigorous evidence: the Jacana bird's nest rather than a pile of sturdy sticks (§5).

## Assumptions

For the RCT analysis (§3):

- (i) A potential-outcomes equation holds in study population P: y(u) = β(u)·x(u) + w(u). Here β(u) is the individual treatment effect, which also carries the net effect of interactive factors, and w(u) collects all other causes. On this equation ATE_P = Exp(β).
- (ii) Orthogonality: Exp(w | x) = Exp(w) and Exp(β | x) = Exp(β), which is her reading of "controlling for statistical bias".
- Under (i) and (ii), Exp(y | x=1) − Exp(y | x=0) = Exp(β), so the difference in arm means is an unbiased estimate of the study-population ATE.
- The metaphysics she says (i) builds in: every singular causal fact falls under some principle (Davidson 1992); causes are INUS conditions (Mackie 1974), with Mackie's form converted to the POE by "or → +, and → ×" (fn. 11); and there is a probability distribution over y and its causes in P.

For the pToC (§4, the three "fundamental assumptions", pp. 13116–7):

- Where C contributes to E at another place and time, a causal process with intermediate steps connects them. It may be continuous or discrete, and where this fails, as perhaps in wave-packet reduction, the pToC is simply not useful.
- Each step's cause is an INUS-type contributor that needs support factors and the absence of derailers.
- The most controversial assumption: each step proceeds according to some general causal principle, governing or merely descriptive. Her Rube Goldberg example shows that the C–E pair need not fall under a principle even when each step does. Where a step falls under no principle, the tool loses its guide to what evidence to gather.

Scope: singular claims, meaning ex ante predictions or post hoc evaluations about a specific individual or population at a specific time and place. This can include averages, such as attainment across a school district (p. 13108).

## Key results

What the paper argues:

- **What "rigour" means (§3, p. 13105).** A valid argument from the method's results to the conclusion, plus credible premises, where credible means well established or secured by design. RCTs' claim rests on the valid proof above and on the design (randomisation plus blinding) being thought to secure premise (ii). Her source for this is the credibility revolution (Angrist & Pischke 2010; Leamer 1983).
- **RCTs often fail that standard even for the study-population ATE (§3; fn. 1).** Randomisation secures orthogonality only *at assignment*. Blinding removes only bias "in the sense of prejudice". Post-assignment differences between arms arising from the specifics of C, E, P and the setting need further, non-design evidence. Premise (i)'s metaphysics cannot be made credible by rigorous methods. "Unbiased" means that the expectation over endless repetitions on the same population equals the true ATE.
- **"External validity" is a misnomer (fn. 13).** Nothing about the result or the method makes it evidence about another population Q. The exception is random sampling of P from Q.
- **Other methods can be as rigorous in the right epistemic circumstances (p. 13106).** For example, stratification in an observational study yields orthogonality, and then the same proof applies. Which methods are usable depends on what local knowledge is available as premises: "choose our methods to fit our local knowledge".
- **Evidence-based-policy case (p. 13107).** The UK What Works crime toolkit's alley-gating review is rigorous about whether gating *has reduced* crime, but it says contextual factors "could not be tested". Those factors are the bulk of what one needs to predict success in Headington Quarry.
- **pToC (§4).** Five elements and three evidence demands (see corrections), illustrated with World Vision Indonesia's 2013 mHealth growth-monitoring programme. Local knowledge matters: community health workers were largely untrained volunteers, so an ability-to-use support factor becomes salient. The pToC supplies evidence only if the pToC is itself right; "facts don't come labelled as evidence" (p. 13113).
- **Three things pToC-based evidence can do that RCTs cannot (p. 13109).** (1) evidence about individual units, ex ante or post hoc; (2) predictions for an unstudied setting without transport assumptions from studied populations; (3) supply the mechanistic evidence that Russo & Williamson argue should accompany difference-making evidence.
- **Cautions (pp. 13113–5).** (a) Build support factors from concrete, low-level principles and refine recursively. (b) A pToC traces one pathway, so masking or dual capacities (Hesslow) and other causes in w can still defeat E; and establishing that C caused a bad E does not show that removing C prevents it (Munro's systems view). (c) There is no method here for aggregating evidence. (d) A pToC does not directly represent evidence against rival hypotheses. (e) Little to offer on transport; she suggests abstracting to a middle-level pToC and then re-concretising. (f) Effect size could in principle be computed as the probability mass of sufficient support/derailer combinations, if one had a probability measure over that space.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Under (i) POE and (ii) orthogonality, the difference in arm means is an unbiased estimate of the study-population ATE | strong | standard derivation, sketched in §3 (full treatment in Deaton & Cartwright 2018) |
| C2 | "Rigorous", as used of RCTs, means valid argument plus premises that are well established or secured by design | moderate | conceptual reconstruction from the credibility-revolution literature. She notes she failed to find an explicit definition |
| C3 | Even well-conducted RCTs often cannot rigorously establish the study-population ATE, because post-assignment confounding and premise (i) are not secured by design | moderate | informal argument (§3). No empirical estimate of how "often" |
| C4 | RCT results are not, by the method, evidence about other populations or individuals (except under random sampling from the target) | strong | follows from the formal set-up (fn. 13), and agrees with the standard transportability literature |
| C5 | No single method, or handful of methods, can warrant a singular causal claim | moderate | argument from the diversity of the facts a pToC requires (§4–5), plus an illustrative case. No proof and no survey |
| C6 | A well-done pToC "can yield reliable predictions about programme success" even though none of its pieces is rigorously supported | weak | assertion (p. 13110). No track record of pToC-based predictions is reported |
| C7 | Rigour is overvalued, and emphasising it is counterproductive because it narrows admissible methods and questions | moderate | follows from C3–C5 given her definition of rigour; illustrated by the What Works toolkit and Campbell Collaboration standards |
| C8 | The pToC's assumptions about causation are compatible with essentially all standard accounts of causality | moderate | informal argument (pp. 13116–7), conceding that the third assumption (steps fall under principles) is controversial |

## Method

The **causal-process-tracing theory of change (pToC)**, from Cartwright et al. (2020):

1. For cause C, effect E and setting S, lay out the significant intermediate steps from C to E.
2. For each step, state the causal principle, as a low-level, concrete tendency principle, by which it produces the next, with reasons it can operate and be triggered in S.
3. For each step, list the support factors needed with it (Mackie-style), the derailers that could stop or diminish it, and the safeguards against those derailers.
4. Gather whatever evidence is possible, by whatever method suits each item, that each support factor and needed safeguard is or was in place, and that each unguarded derailer is or was absent. Common knowledge counts as a method.
5. Weigh the evidence, with no method given here; she points to process-tracing tests such as van Evera's hoop and smoking-gun tests, and to Bayesian evaluation (Befani). Refine the pToC recursively as local information arrives.

## Concepts

- **singular causal claim** — a claim about what a cause will contribute or has contributed in a specific setting (an individual or a specific population at a time and place). The contrast is with universal or widespread claims.
- **rigour** — valid argument from method results to conclusion, with premises well established or secured by design (§3).
- **statistical bias** — confounding of C with other causes of E, operationalised as failure of the orthogonality conditions. Distinguished from bias "in the sense of prejudice".
- **support factor** — an INUS co-factor that must be present for a step's cause to produce its effect.
- **derailer** — anything that can intervene to stop or diminish a process once in train.
- **safeguard** — a "wall" preventing a derailer from intruding.
- **middle/low-level causal principle** — a generic tendency principle (after Mill) that is neither universal nor case-specific and needs the right setting to be triggered. Elster calls these "mechanisms".
- **pToC** — a theory of change augmented with principles, support factors, derailers and safeguards at each step.

## Connections

The paper condenses Deaton & Cartwright (2018) on RCTs and builds on Cartwright et al. (2020, CEDIL) for the pToC. It is part of the Synthese topical collection *Evidential Diversity in the Social Sciences* (eds. Shan & Williamson). Its philosophical sources are Salmon's process theory, Mackie's INUS conditions, Davidson on causal principles, Mill's tendency laws, Elster's mechanisms and Anscombe on perceiving causation. Methodologically it draws on process tracing, case-study methods and realist evaluation (Pawson & Tilley), and it aligns with EBM+ and the Russo–Williamson thesis on mechanistic evidence. In this record the natural companions are Worrall's *Evidence in Medicine and Evidence-Based Medicine* ([LIT-175](../literature.d/LIT-175.md)) on evidence hierarchies and Reiss's *A Pragmatist Theory of Evidence* ([LIT-118](../literature.d/LIT-118.md)). Both are Deferred, and I have not checked their content against this paper. Garg et al. ([LIT-079](../literature.d/LIT-079.md)) document the rise of RCT/DiD/IV-backed causal claims in economics working papers (7.7% of edges in 1990 to 31.7% in 2020) and a publication premium for them. That is quantitative evidence of the methodological narrowing Cartwright describes in §2, though neither work cites the other.

## Bearing on the record

**Epistemology.** The paper is about *evidence and warrant*: what makes a fact evidence for a causal hypothesis, and what "rigorous" support is. Its positions are these. Evidential relevance is always relative to background assumptions ("facts don't come labelled as evidence"). Warrant for singular claims comes from the joint support of many subsidiary claims, not from any single privileged method. Rigour, understood as valid argument plus design-secured premises, is one epistemic virtue among several and is overvalued. The closing Neurath image signals a coherentist/fallibilist view of knowledge claims. The `epistemology` tag is justified. `philosophy-of-science` stays primary, since the tag's blurb explicitly covers "causation and evidence". `social-science` is justified by the policy and economics setting.

**ML practice.** The paper carries no instruction for ML practice. The transferable idea, flagged in the seed, is still a conceptual analogy. A benchmark gain is like an RCT's study-population average: at best rigorous about *that* population, and not by itself evidence that a method will work in a given deployment. Predicting deployment success would mean evidencing the steps, support factors and derailers in the deployment setting. That might justify an Anthology *theory* or evaluation note citing it as a philosophical gloss, but it is not a `source:` for a practice. I found no Anthology document on external validity or deployment evidence to attach it to.

## Limitations

- Its own disclaimers: there is no method for aggregating diverse evidence into a verdict (caution c), little on transporting a pToC to new settings (caution e), and a pToC traces one pathway, so masking and other causes are not handled without a fuller local causal model (caution b).
- The claim that well-supported pToCs yield reliable predictions (C6) is asserted. No evaluation of pToC predictive success is reported, and the mHealth example is illustrative, not a test.
- The critique of RCT rigour depends on her reconstructed definition of rigour. Advocates who mean something weaker, such as "best available protection against selection bias", are not directly answered.
- "Often" (RCTs often fail to secure even the ATE) is not quantified.
- The full worked template (Fig. 1 key) is outside this paper.

## Open questions

- How should the heterogeneous evidence a pToC calls for be weighed? Would the Bayesian process-tracing work she mentions (Befani) close the gap, and does it reintroduce a kind of rigour?
- Do pToC-based predictions actually outperform RCT-transport predictions? A prospective comparison on programme roll-outs would settle it.
- What is the relation between this "rigour vs diversity" view and Worrall ([LIT-175](../literature.d/LIT-175.md)) and Reiss ([LIT-118](../literature.d/LIT-118.md))? Both are still unread here.

## Corrections to the seeded skim

- The skim lists the pToC contents as steps, support factors and derailers. The template has **five** element types (§4, p. 13110): (1) the significant steps; (2) the causal principles by which each step leads to the next ("not actually pictured in the figure but ... listed alongside"); (3) support (interactive) factors; (4) derailers; (5) safeguards. From these follow three evidence demands: that the principles operate and are triggered at each step, that support factors take appropriate values, and that derailers are absent or guarded against.
- The dossier and LIT ask for the "full pToC template (§4 and its figures)" and an explicit checklist. This paper has one figure, an image reproduced from Cartwright et al. (2020, CEDIL Methods Working Paper 1). The text gives the key only for the first two steps of the Indonesian mHealth example (principle "health workers tend to do what they can in their clients' best interest", support factors on capacity, agreement and clinic attendance, derailer "external pressure ..."; principle "mHealth technology does accurate calculations", support factors "well designed", "correct data input", derailer "technology fails"). The paper refers readers elsewhere for the rest. The five-element list plus the three evidence demands is the checklist this paper contains.
- The paper's own definition of rigour is missing from the dossier and the skim. It is §3, p. 13105: a method is rigorous when "a) there is, if not a deductive, at least an argument otherwise warranting the label 'valid', why results produced following the method count as evidence ... and b) where the premises ... are credible in the sense that they are, or follow from, well-established knowledge or are secured by the design". Her critique of RCTs is internal to this definition.
- The seed summary says evidential diversity "requires evidencing every step". Cartwright's wording is weaker and graded: gather "whatever evidence is possible" for each support factor and derailer, and "to the extent that any have no evidence in their favor, to that extent our case ... is weakened" (p. 13112).
- The paper openly disclaims two things a reader might expect from it. It offers no method for aggregating the evidence into a verdict (§4 caution c, which points to van Evera's tests and Befani's Bayesian work), and "I don't have much to offer" on transporting a setting-specific pToC to other settings (caution e).
- primary topic: philosophy-of-science is right, since the tag's blurb names "causation and evidence". The epistemology tag is justified (see Bearing on the record).
