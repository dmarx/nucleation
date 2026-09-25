---
number: 7
status: Read
formerly:
- NOTE-tmp79sp8
paper: LIT-021
title: 'From the origin of life to pandemics'
version: 2
history:
- version: 2
  date: '2026-09-25'
  note: >-
    Read in full (full text of arXiv 2205.11595v1 (23 May 2022), 20 pp. I
    read the abstract, §§1–6 (including §5, the per-paper summary of the
    theme issue, which the skim had skipped), the Fig. 1 caption and the end
    matter. Extraction was with PyMuPDF (no pdftotext on this host). I did
    not read the 188-item reference list in full. I consulted individual
    entries: [11], [54], [160], [161], [165], [166], [188]. I did not
    compare the published Phil. Trans. A version (DOI
    10.1098/rsta.2020.0410). The preprint is still typeset on the Proc. R.
    Soc. A template ("rspa", subject and keyword fields "TBCompleted").).
    Upgraded from `Skimmed` to `Read`: the claims table, assumptions and
    results are new, and the skim is corrected where the full text
    disagreed.
date: '2026-09-25'
summary: >-
  An editorial review with no new result. Its one formal item (§4, Eq.
  4.1: x(t+1) = f[x(t)], x(0) = x₀) sorts phenomena three ways.
  Non-emergent: local rules plus initial conditions let you deduce the
  "expected" high-level pattern. Weakly emergent: they let you deduce an
  "unexpected" one by computation. Strongly emergent: no deduction is
  possible even in principle. "Unexpected" is never defined. The rest is a
  cross-domain survey (§3), a 16-paper map of the theme issue (§5), and an
  outlook (§6).
---

# NOTE-007: From the origin of life to pandemics

## Contribution

This is the introduction to the Phil. Trans. A theme issue "Emergent phenomena in complex physical and socio-technical systems: from cells to societies". It adds no result. After it, a reader has three things:
- a short history of the concept (§2: Aristotle, Gestalt psychology, the British emergentists, cybernetics, Anderson's "More is different", Prigogine, Wolfram's Rule 110);
- a broad catalogue of claimed emergent phenomena, from quantum to urban scales (§3);
- a one-paragraph synopsis of each of the issue's 16 papers (§5).

Its own proposal is an operational framing (§4). A system has units, local mechanistic rules f and an initial condition x₀. Emergence is classified by whether the high-level pattern the dynamics produces can be deduced from those, and whether it is "expected".

## Key insight

The paper takes Chalmers' and Bedau's position that only *weak* emergence is scientific. Weak emergence here means patterns that are unexpected given the micro-rules but derivable in principle by computation or simulation. It pairs this with an observer-relative, information-based notion of "organization" (§3, citing Ashby's "organization is partly in the eyes of the beholder"). On that view emergence is not a property of the dynamics alone. It is a relation between the dynamics, a pair of well-separated scales and an observer who finds a pattern at one scale and not at the other.

## Assumptions

- **Two well-separated scales and an external observer** who identifies patterns and "measure[s] them in terms of information" (§3, p. 3). The paper states these as necessary conditions for characterising any emergent phenomenon.
- **A finite system of many units** with local rules f[·] and an initial condition x₀. The dynamics can be deterministic or stochastic, open or closed, and discrete or continuous in time (§4, Eq. 4.1). Stochasticity and openness count as "additional external conditions".
- **Physicalism.** Strong emergence would "require new fundamental laws of nature" and is set aside as not scientifically relevant (§4, following Bedau [161]).
- **Shannon information is observer-relative.** The observer chooses the relevant degrees of freedom and the state count (§3, p. 5).

## Key results

This is a review, so there are no theorems or experiments. Its load-bearing statements:

- **§3, mass example.** Mass is additive (M = Σ mᵢ) at everyday scales. At the nuclear scale the binding-energy mass defect breaks additivity. Even so, mass is not treated as emergent, because it can be defined for a single unit. A property counts as emergent when it "cannot be defined at the level of a single unit".
- **§3, thermodynamics.** Self-organisation requires ΔS_S/Δt < 0 for a sufficient time. That is possible only if ΔS_E/Δt > 0, so that ΔS_U/Δt > 0 (a von Foerster-style open-system requirement).
- **§4, classification.**
  - Non-emergent: LLMR + IC ⇒ expected HLP.
  - Weakly emergent: LLMR + IC ⇒ unexpected HLP through computation.
  - Strongly emergent: LLMR + IC do not determine HLP even in principle.

  The same classification applies to emergent systems Σ and to emergent properties Π.
- **§6, open problems.**
  1. Whether a few generative rules underlie emergence across domains. The authors add that "it is still not granted that such a comprehensive picture exists or if it useful at all".
  2. What the paper calls the "inverse problem": predicting macroscopic outcomes from microscopic rules. By usual convention that is the forward problem. The paper suggests it "might lead to the discovery of a new kind of universality classes".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Characterising emergence requires at least two well-separated scales and an observer who identifies patterns at one scale and not the others | assertion | §3, p. 3; no argument beyond the mass example |
| C2 | Only weak emergence is scientifically relevant; strong emergence would need new fundamental laws | assertion (attributed) | §4, citing Bedau [161] and Chalmers [160] |
| C3 | Emergence can be classified as non / weak / strong by whether LLMR + IC allow deducing the expected / an unexpected (by computation) / no HLP | informal argument | §4, Eq. 4.1, Fig. 1; "expected" is undefined |
| C4 | Not every combination of LLMR and IC produces a high-level pattern | assertion | Fig. 1 caption |
| C5 | Self-organisation requires an open system, with environment entropy rising faster than system entropy falls | informal argument | §3, p. 6 (second law bookkeeping) |
| C6 | Emergence research remains without a widely accepted rigorous definition or an agreed account of the conditions that favour it | assertion | abstract, §6; this is the paper's framing premise |
| C7 | Swarm learning outperformed standard federated learning, and beats nodes learning separately | assertion (secondhand) | §6, one sentence citing [188]; no setting or numbers |
| C8 | Life is an emergent property of any random dynamical system with a Markov blanket, given a "heuristic theoretical and computational proof" | assertion (secondhand) | §3, citing Friston 2013 [54]; not assessed here |
| C9 | The issue's 16 papers can be ordered from theory to scale-specific phenomena, from quantum spins to epidemics | editorial organisation | §5 |

The abstract promises "a general overview … and … current and future challenges". The body delivers that. The one place where the text claims more than it shows is the heading of §4, "Defining emergence from a mathematical perspective". The section offers a classification, not a definition that could be checked.

## Concepts

- **Emergence** — "the apparition of system-wide properties or qualities that are not present individually in the units but have their origin precisely in the interactions" (§4).
- **LLMR / IC / LLEP / HLP** — low-level mechanistic rules f[·]; initial conditions x₀; the low-level evolution process; and the high-level phenomenon, a "stable or metastable emergent pattern" (§4).
- **Weak emergence** (Chalmers; Bedau) — high-level patterns that are unexpected given the lower-level laws but deducible in principle by computation.
- **Strong emergence** — not deducible even in principle.
- **Σ versus Π** — Σ is an emergent system or structure, such as a network backbone produced by an optimisation principle. Π is an emergent property of an existing system, such as superconductivity or network robustness (§3, §4).
- **Organization** — the formation of spatial and/or temporal structure that an external observer can measure in terms of information. It is observer-dependent (§3).
- **Self-organized criticality** — driven, out-of-equilibrium systems that reach a critical point as an attractor without any parameter being tuned (§3).

## Connections

- **The theme issue it introduces** contains the two emergence papers read in this batch. The first is Mediano, Rosas et al., "Greater than the parts" (item 21; [LIT-025](../literature.d/LIT-025.md)), which the editorial attributes to "Rosas and collaborators". The second is Varley & Hoel, "Emergence as the conversion of information" (item 22; [LIT-027](../literature.d/LIT-027.md)).
  - The editorial's gloss on item 21 ("accessible and rigorous review … case studies, both from empirical data and synthetic simulations") matches reads/21.
  - Its gloss on item 22 accepts that paper's "unifying theory" and "overcomes the … dichotomy between strong and weak emergence" framing, and says it was applied to "Boolean networks". reads/22 found the unification to be a framing only, shown for MI+PID and re-described for EI. It also found that the systems were small logic-gate networks and 3-node TPMs.
  - The editorial's weak/strong framework (§4) and item 22's claim to get past it are therefore not reconciled anywhere in the issue's front matter.
- **Items 21 and 22 against this paper's §4.** Both give *quantitative* criteria for emergence: Syn⁽ᵏ⁾ > 0 or Un⁽ᵏ⁾(V; X′|X) > 0 in item 21, and a rise in B_syn or EI at a macroscale in item 22. §4 here gives none. It also does not say how its "unexpected" relates to those information measures. §3's appeal to observer-relative Shannon information is the nearest point of contact, and it stays verbal.
- **Other theme-issue items** named in §5 that a reader of this record might follow:
  - Abrahão & Zenil, on algorithmic-information emergence, which is observer-independent if it grows unboundedly fast;
  - Adami & Nitash, on functional information from multivariate correlations;
  - Wolpert, on a strengthened second law for multipartite CTMCs;
  - Sokolov et al., on entanglement networks in XX spin chains.

  None of these is in the record.

## Bearing on the record

- In nucleation this is [LIT-021](../literature.d/LIT-021.md). Its summary is accurate as far as it goes. It should add two things: that §4 classifies rather than defines, since the criterion "unexpected" is informal; and that §5 is the issue's reading list, including [LIT-025](../literature.d/LIT-025.md) and [LIT-027](../literature.d/LIT-027.md).
- It supports and contradicts no THEORY document in the Anthology of the SOTA.
- **Not the ML sense of "emergent".** "Emergent capabilities" in ML ([ANTH-LIT-470](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-470.md), [ANTH-LIT-471](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-471.md), [ANTH-THEORY-040](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-040.md), [ANTH-SOTA-200](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/practices.d/SOTA-200.md)) means abrupt onset of a task ability as model scale grows. This paper's emergence is about system-wide patterns arising from local interactions. It never mentions model scale, training or capability onset.
- Its only ML statement is the secondhand swarm-learning sentence (C7). That sentence gives no setting, baseline or metric, so it cannot source anything. A practice about decentralised or federated training would need the primary paper [188], and the anthology's federated-learning source is [ANTH-LIT-307](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-307.md). The paper carries no instruction for ML practice.

## Limitations

- **No result of its own.** Every substantive scientific claim is cited, and the paper's own contribution is organisational.
- **The §4 classification depends on "expected" versus "unexpected", which is never formalised.** So whether something is weakly emergent or merely non-emergent depends on the observer's expectations. That is consistent with the §3 observer-relativity, but it makes the classification uncheckable.
- **Strong emergence may be empty under the formalism as stated.** This is my observation, not the paper's. §4 assumes f, x₀ and any external conditions are fully specified. Under that assumption, a computable f leaves no room for a pattern that cannot be deduced even in principle. For stochastic f, deduction is of a distribution. The paper does not address whether its "strongly emergent" category can be non-empty in its own setting.
- **The survey (§3) is broad and uncritical.** It lists claimed emergent phenomena without distinguishing established physics (BCS superconductivity, the Josephson effect) from contested proposals (life as an emergent property of Markov-blanketed systems, [54]).
- **The §6 applications paragraph is aspirational:** robot swarms, drones, "smarticles", swarm learning, cybersecurity and precision medicine. It closes with "there were no lasagne encoded in the Big Bang".

## Open questions

- Can "unexpected" in §4 be replaced by a quantitative criterion, such as one of the information measures of items 21 and 22? If so, would the weak/strong split survive, or collapse as item 22 claims?
- Is there a small set of generative rules shared across domains? The authors themselves doubt that such a picture exists or would be useful (§6).
- The "inverse problem" of §6 (macro outcomes from micro rules): does it yield new universality classes, as the paper suggests? No result is given or cited beyond programmable pattern formation [180].

## Corrections to the seeded skim

- The skim left §5 unread and called the paper's value "navigational". §5 has now been read. It summarises 16 contributions in scale order, from Abrahão & Zenil (algorithmic information and observers) to Khanjanianpak et al. (protective behaviour under heterogeneous risk perception). Two of those glosses disagree with the source papers as this record has read them. §5 attributes the causal-emergence review to "Rosas and collaborators", but ref. [165] lists Mediano as first author ([LIT-025](../literature.d/LIT-025.md)). It also says Varley & Hoel "overcomes the traditional dichotomy between strong and weak emergence", which repeats that paper's headline framing. The body of that paper does not support the framing (see reads/22: the "unifying theory" is a framing, not a result).
- The skim says §4 gives "a mathematical definition". The only mathematics is the generic update rule Eq. 4.1. The three-way classification rests on whether the high-level pattern is "expected" or "unexpected", and the paper never formalises that. §3 does say the pattern is identified by "an external observer" who measures it "in terms of information".
- The skim does not mention the second distinction §4 draws. Σ is a system that itself emerges from its constituents (e.g. a network backbone). Π is a property that emerges because a system exists (e.g. superconductivity, or robustness to random failure).
- The skim describes the swarm-learning remark (§6) accurately. Note, though, that it is one sentence citing a single paper, [188] (Warnat-Herresthal et al. 2021, Nature 594:265). The editorial gives no conditions, numbers or setting for "outperformed the standard federating learning".
