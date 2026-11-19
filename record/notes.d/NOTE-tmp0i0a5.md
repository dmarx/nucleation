---
status: Read
paper: LIT-tmpa8gus
title: 'Lu and Kankanhalli 2026 — Agentic-TTT: Training Test-time Policy for Test-time Training'
version: 1
history:
- version: 1
  date: '2026-11-19'
  note: >-
    URL: https://arxiv.org/pdf/2610.12002 (HTTP 200, 2026-11-19; arXiv v1, 8
    Oct 2026, 26 pages). Kind of copy: arXiv preprint posted by the authors
    (step 5: arXiv). Date: 2026-11-19. Nothing stopped the fetch. Text
    extracted with pdftotext to dl/text.txt. Read: abstract, §1–§5 in full
    (formulation, two-stage policy learning, main results, compute trade-
    off, unseen domains, model families, ablations, conclusion), appendix
    B.2 (benchmark scope) and appendix E (limitations). Skipped: references;
    appendices A, B.1, C, D (data sources, harness and prompts, optimization
    details), seen only where the main text cites them.
date: '2026-11-19'
---
<!-- inactive-ok-file: CASE-tmphsr99 CLAIM-697 — Proposed; cited in this filing of 2026-11-19 -->

# NOTE-tmp0i0a5: Lu and Kankanhalli 2026 — Agentic-TTT: Training Test-time Policy for Test-time Training

## Contribution

Treats test-time training as a decision rather than a fixed procedure. Five TTT methods become tools; each use produces a LoRA adapter over a frozen backbone, stored with a description in a persistent skill library. A policy, trained first by hint-guided distillation and then by GRPO on utility gain over direct answering minus a compute penalty, decides per query whether to answer directly, load an existing skill, pool material, or build a new skill with a chosen method. On a deliberately enriched benchmark the policy roughly doubles a 7B model's utility, trades utility against compute under the penalty, and transfers to held-out domains.

## Key results

- **The problem (abstract).** "TTT is not universally beneficial: each TTT algorithm works in different settings", and an ill-suited method wastes test-time compute "or even damage model performance".
- **Return (§2.1).** The base-relative return subtracts λ times the extra computation, so "An agentic trajectory is therefore beneficial only when its utility improvement justifies its additional cost."
- **Main result (§3.1, Table 1).** "Agentic-TTT increases overall utility from 0.256 to 0.510, with positive gains in all eight domains"; fixed methods help some domains and hurt others: Always-SEAL "improves Passage QA but degrades mathematics and code generation".
- **Help against harm (§3.1).** Across three runs it "converts 141 incorrect direct answers into correct ones, while reversing only 7 correct direct answers".
- **Reuse amortizes construction (§3.1, Fig. 2b).** 100 queries are answered with previously built skills, helping on 61 and harming one; "Loading these skills requires no additional adaptation, allowing their construction cost to be amortized across subsequent queries."
- **Compute penalty (§3.2, Fig. 3).** Raising λcomp from 0 to 0.4 raises the direct-answer rate "from 11.8% to 39.8%" and cuts normalized adaptation compute by 35.5%; moderate penalties "reduce compute by approximately 30% while achieving higher mean utility than λcomp = 0". Training data keep a TTT trajectory only "when its empirical utility gain amortized over expected future reuse, justifies its compute cost".
- **Selective reallocation (§3.2, Fig. 4).** Under penalty, costly low-gain TTRL use "nearly halves, decreasing from 21.3 to 11.7 invocations".
- **Unseen domains (§3.3, Fig. 5).** Gains on held-out domains are "broadly comparable to those on domains seen during training".
- **Other backbones (§3.4, Table 2).** Gains of 0.136 on Llama-8B and 0.142 on GLM-9B, with losses in some domains; Qwen-14B rises from 0.432 to 0.621.

## Assumptions

- A benchmark enriched for queries where TTT helps: about 65% of it, against 7.0% of MATH-500 under the paper's high-gain criterion (B.2).
- Isolated LoRA skills over a frozen backbone; verifiers giving a binary score; a FLOPs-based cost normalized by one direct answer and entered as λcomp log10(1 + cm).
- RL on query-level returns, with the training stream advanced by gold actions rather than the policy's own (E).

## Concepts

- **Agentic TTT**: a learned policy over when and how to adapt parameters at test time.
- **Skill library**: persistent, described LoRA adapters built by TTT and reusable on later queries.
- **Adaptation pool**: queries held until enough compatible material exists for a multi-query TTT method.
- **Base-relative return**: utility gain over direct answering minus λ times extra compute.

## Bearing on the record

- **QUESTION-095**: supports, directly. The paper's decision rule is the question's trade: build a skill (precompute) when its gain "amortized over expected future reuse" covers its compute, and reuse it at no adaptation cost. It is a working cost model of precompute, reuse and retrieval for parameter skills, though storage, upkeep and staleness are not costed.
- **CLAIM-303**: corroborates, in another domain. Filing pays now against reconstruction later, worth it when expected reuse covers it; here a skill pays adaptation compute now and is worth it when expected reuse covers it, and the trained policy learns where that holds.
- **CLAIM-118**: qualifies. A skill built on one query and loaded on later ones carries earlier contexts into new ones, so by the claim's test it is interpreter, not signal, although the backbone never changes and the skill can be unloaded. The interpreter here is a backbone plus a library, and the policy chooses per query which interpreter answers.
- **CASE-tmphsr99**: supports two arms. The λcomp sweep is an operational utility–compute exchange rate of the kind the exchange-rate arm wants, and the policy's decision to adapt or not is a learned version of the active-acquisition arm. The enriched benchmark is a warning for the case: selecting tasks where adaptation helps inflates the measured gain.
- **CLAIM-697**: supports. Success here is a function of the composition of operations chosen under a budget, and the frozen model's direct answer is one point on that curve.

## Limitations

By the authors' account, gains "characterize this curated setting and should not be interpreted as expected gains under the original source distributions"; a stream of 176 scored queries; three training runs; RL trained on oracle-advanced streams (exposure bias); negative gains in some domains on other backbones; the cost model counts FLOPs, not latency or storage.
