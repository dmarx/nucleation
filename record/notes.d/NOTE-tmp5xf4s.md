---
status: Skimmed
paper: LIT-tmpuy2kv
title: 'Neacsu and others 2026 — Reviewing Structure Learning in and Out of the Active Inference Framework'
version: 1
history:
- version: 1
  date: '2026-11-19'
  note: >-
    URL read:
    https://link.springer.com/content/pdf/10.1007/s11023-026-09787-8.pdf
    (publisher's open-access version, "© The Author(s) 2026", Minds and
    Machines (2026) 36:33; located through OpenAlex, which lists it as
    hybrid OA, publishedVersion). Kind: publisher open-access copy. Date
    2026-11-19. HTTP 200, no obstacle. Also located, not read: Cambridge
    repository submitted version,
    https://www.repository.cam.ac.uk/handle/1810/404807 (bitstream https://w
    ww.repository.cam.ac.uk/bitstreams/8cb124db-a297-40a5-848a-
    5e8eeb194e8d/download). Not needed once the published version was read.
    Read: abstract, §1 Introduction, §2.2.1 (graphical models), §2.3 Summary
    (the general definition), §3.3 Structure Learning and Bayesian Model
    Reduction, §3.4 Summary (the AIF definition), §4.1.1 (information gain
    and Structure Learning), §4.2 Overarching Discussion. Skimmed: §2.1
    (human studies), §2.2.2-2.2.3 (RL, replay), §3.1-3.2 (inference and
    parametric learning), §4.1.2-4.1.6. Skipped: references. Authors as
    printed: Neacsu, So, Rutar, da Costa, Adams, Friston. Received 16 Jan
    2025, accepted 28 May 2026, published 15 June 2026.
date: '2026-11-19'
---
<!-- inactive-ok-file: THEORY-564 — Proposed; cited in this filing of 2026-11-19 -->

# NOTE-tmp5xf4s: Neacsu and others 2026 — Reviewing Structure Learning in and Out of the Active Inference Framework

## Contribution

A conceptual review. It first surveys what "structure learning" names across infant statistical learning, adaptive generalisation, meta-learning, insight, concept learning, replay, graphical models and RL. It then offers a generic definition, and a narrower active-inference definition ("Structure Learning", capitalised): Bayesian model selection by model evidence, either by refitting under alternative priors or by Bayesian model reduction or expansion of accumulated posteriors. Finally it maps the general phenomena onto the framework's three levels: inference, parametric learning and structure learning. The paper argues for the framework's unifying power and advises integrating it with other accounts. It reports no new results.

## Key results

- §2.3, p. 11, the general definition: "structure learning is the ability to internalise models of contingencies (i.e., conditional [in] dependencies) among different elements in space and time, that can be leveraged with ease across new contexts".
- §3.4, p. 17, the AIF definition: "Structure Learning involves selecting between (alternative) models using a measure called model evidence." It is offline: "Structure Learning happens in the absence of novel evidence (i.e., it occurs offline)".
- §3.3, pp. 15–16, two flavours: refitting under alternative priors (used for phenotyping), and Bayesian model reduction or expansion (used in synthetic agents), the latter "a more expedited method by circumventing the necessity of reinversion".
- §4.1.1, p. 18: an information gain between parametric and structure learning "informs forward-looking implementations (i.e., planning actions based on employing BMR or not), rather than backward-looking".
- §4.2, p. 23, the open problem: "The challenge (which remains an open question) lies in defining the alternative explanations (i.e., models, hypotheses) in the first place." The authors' own earlier work specified "twelve alternative hypotheses" a priori.
- §4.2, p. 24, on model growth: "Showing that one can add a variable to a model is, in principle, as trivial as my ability to add another alternative hypothesis to the model (manually)."
- Abstract: the single objective "should not be confounded with the exclusivity of this framework. The integration with other computational accounts is advised."

## Assumptions

- Structure learning in active inference is model selection over a hypothesis space that must be supplied. The review takes ecological validity, not speed, as the aim (§4.2, against Erdmann and Mathys 2021).
- Its mapping of phenomena onto the three levels is interpretive. No study is re-analysed.

## Concepts

- structure learning (general) versus Structure Learning (in active inference), used as a capitonym.
- Bayesian model selection, reduction and expansion. Offline structure learning, linked to sleep and synaptic homeostasis.
- The two open problems it quotes: infinite alternative explanations, and "How do we grow a model?".

## Bearing on the record

- THEORY-564: qualifies, and agrees with its framing. The review classes Smith, Schwartenbeck et al. 2020 (LIT-615, THEORY-564's source) among the reduction/expansion approaches. Its remark that adding a variable is "in principle, as trivial" as adding a hypothesis matches THEORY-564's view that expansion was never in doubt and reduction is the open part. The review adds a different gap: the hypothesis space is supplied by hand. It reports no recovery rates and does not move the promote_when.
- CASE-153: leaves open. The review places structure learning offline and has nothing on structure learning under a process that blocks inspection. For the case it offers vocabulary only.
- QUESTION-tmprj00l: leaves open. Variational model evidence only, with no physical cost.
- Verdict on the LIT's source (A69 called it the most useful single paper for what the free-energy literature covers): fair as a map of definitions and open problems. But it is a conceptual review with no quantitative results, and it defines Structure Learning as offline. Active, data-choosing structure learning is in LIT-tmpg7w4q, not here.

## Limitations

- No new data or simulation. The breadth of phenomena is covered by illustrative example, not systematically.
- Written mainly by the framework's proponents. The comparison with other accounts is brief (hierarchical Bayesian nonparametrics are mentioned, not compared).
- Skimmed in part (§2.1, §2.2.2–2.2.3, §3.1–3.2, §4.1.2–4.1.6).
