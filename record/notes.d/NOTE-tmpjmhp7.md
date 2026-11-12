---
status: Read
paper: LIT-tmpj8nbo
title: 'Zhu and others 2026 — What Does Multi-Turn Reinforcement Learning Really Improve in LLM Agents?'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Read on 2026-11-12 for the reading pass the owner asked for ("read the
    works you can reach"), from a reader's draft the filer verified against
    the downloaded text. Copy and extent: - Read:
    https://arxiv.org/pdf/2611.06483 (PDF, v1, "arXiv:2611.06483v1 [cs.LG] 4
    Nov 2026", 26 pp.), fetched 2026-11-12, pdftotext. Read: abstract, §1–§7
    (preliminaries and Pass@(K,T), trajectory-level results §3.1–3.2,
    step-level action quality §3.3, risks §3.4, likelihood and
    training-dynamics analyses §4, process supervision and BudgetMix §5,
    conclusion §7), AI use statement. Skipped: appendices A–E
    (implementation, structural upper bounds B.3, extra results), related
    work, references (checked only the Zhai et al. entry). Outcome as the
    reader gave it: **Read** (main text in full; appendices skimmed only
    where the main text points to them).
date: '2026-11-12'
summary: >-
  The paper asks what multi-turn agentic RL (GRPO mainly, also PPO and
  GiGPO, on Qwen3-4B/8B) improves over its base model, on four interactive
  benchmarks (DeepCoder-MT, BFCL v3, InterCode-SQL, FrozenLake), using the
  two-dimensional metric Pass@(K, T) of Zhai et al. (2026; arXiv 2604.14877,
  held as LIT-tmpt7avk). Across sampling breadth K, the RL model beats the
  base model at every k, so in multi-turn settings RL pushes success beyond
  the base model's empirical Pass@K boundary (unlike single-turn results).
  Across interaction depth T (k fixed at 8), the RL advantage needs a
  sufficient turn budget and shrinks, vanishes or reverses under tight
  budgets, even where headroom remains. At matched states, RL does not
  choose better single-step actions (better on only 46.8% of DeepCoder-MT
  and 42.8% of FrozenLake states), but it does after injected errors
  (65.7%/67.3%) and later in trajectories. Likelihood analysis: RL's actions
  are locally plausible under the base policy, but whole RL trajectories are
  far more likely under the RL policy (cumulative LLR ~228 vs 26), so RL
  improves how reliably plausible steps are composed. During training the
  trajectory reward rises while a step-quality reward falls. Mitigation:
  oracle process rewards help where available (FrozenLake) but not on BFCL;
  BudgetMix RL, training with budgets sampled at 10% intervals and stated in
  the prompt, beats full-budget RL at 25/50/75% of T_max (by 7.5, 5.3, 4.0
  pp on average) and keeps parity at 100%.
---
<!-- inactive-ok-file: ARG-tmpid47d CLAIM-tmpff0cq CLAIM-tmpyc5md THEORY-tmps74c5 — Proposed; filed from the same exchange -->

# NOTE-tmpjmhp7: Zhu and others 2026 — What Does Multi-Turn Reinforcement Learning Really Improve in LLM Agents?

## Contribution

An evaluation showing that trajectory-level gains from multi-turn agentic RL are budget-conditional and come from error recovery and long-horizon composition rather than better per-step decisions, with a simple budget-randomized training remedy.

## Key results

- Abstract: "trajectory-level RL advantages depend on sufficient turn budgets, diminishing significantly when budgets tighten."
- Abstract: "agentic RL does not uniformly elevate single-step decision quality; rather, its strength concentrates in error recovery and long-horizon resilience."
- §3.1, Takeaway 3.1: "multi-turn agentic RL can push trajectory-level performance beyond the empirical Pass@K capability boundary of the base model."
- §3.2: "under tight budgets (small T ), this advantage diminishes, and can even reverse on certain tasks."
- §3.3: "RL achieves better step-level decision quality on only 46.8% of DeepCoder-MT states and 42.8% of FrozenLake states"; on error states, "the RL model selecting the superior action in 65.7% of cases on FrozenLake and 67.3% on DeepCoder-MT"; continuation success from identical error states 51.3% vs 38.6% (FrozenLake), 38.5% vs 22.9% (DeepCoder-MT).
- §4.1: cumulative LLR of successful RL trajectories "reaching approximately 228, compared with 26 for successful base trajectories"; "even if the conditional probability per-step is reasonably high, the overall probability of entire trajectory can be extremely low."
- §4.2: "On DeepCoder-MT, Rmulti rises by 0.331 while Rsingle drops by 0.097."
- §5: BudgetMix: "During training, the total and remaining budget are provided within the prompt"; "the interaction budget changes the conditions under which the same reward can be obtained."
- §5.2, Table 1: BudgetMix gains over full-budget RL of 7.5, 5.3 and 4.0 pp at 25%, 50%, 75% of T_max.

## Assumptions

- "Empirical capability boundary" is Pass@K at finite K (up to 128), not a true reachability set.
- Step quality measured only where reliable: FrozenLake exact Q* via DP (γ = 0.95), DeepCoder-MT unit-test pass rates.
- Budget is announced to the model in the prompt at evaluation, so the policy may condition on T and remaining budget.
- Small open models (Qwen3-4B/8B); four benchmarks.

## Concepts

Pass@(K, T); sampling breadth vs interaction depth; empirical capability boundary; step-level action quality; error states; long-horizon resilience; trajectory composition (cumulative log-likelihood ratio); process supervision (GiGPO, oracle Q rewards); BudgetMix RL.

## Bearing on the record

**On the LIT's and the exchange's characterization.** A's account (gains depend on sufficient turn budgets, concentrate in error recovery and long-horizon resilience; proposes BudgetMix RL) is accurate and nearly verbatim from the abstract. It omits that the paper also confirms RL expands the empirical Pass@K boundary in multi-turn settings, and that per-step quality can decline during training.

- **CLAIM-tmpyc5md** (Pass@(k,T)'s capability boundary = reachability by a process under a budget; efficiency = reliable attainment; T = resource index): **supports, with the claim's qualification sharpened**. Zhu et al. use the same metric and find (a) boundary expansion along K and (b) that the ordering of two policies' success is not stable across T: an advantage at large T can vanish or reverse at small T. That is the record's distinction in action (what is reachable under a resource vs reached), and it shows the resource index matters to which process "can do more". Its finding that RL improves composition of locally plausible steps, not per-step choice, is a third distinction the CLAIM does not draw: reliability of a long path vs quality of each move.
- **CLAIM-tmpff0cq** (not named in the LIT; same exchange): **supports** its premise case. In Zhu et al. the policy is told "the total and remaining budget" in the prompt, so its choices depend on the remaining budget; Pass@T for such a policy need not be monotone in T, and BudgetMix deliberately trains that dependence.
- **ARG-tmpid47d** (qualification 1: the boundary is relative to a stochastic policy, not a move rule; estimates can fall with T): **supports**: a second paper's evidence that budget-conditional behaviour is real and trainable.
- **THEORY-tmps74c5** (Zhai et al.'s account): **extends**: an independent group confirms boundary expansion along K for multi-turn RL and adds that the depth axis decides whether the gain appears.

Searched origin/main and the batch ref for: arXiv id, BudgetMix, "agentic RL", "error recovery", Pass@/PASS@, 2604.14877.
- **Duplicate check**: not held under another LIT.
- Missed by the first search: **CLAIM-tmpff0cq** (budget-dependent processes, above), **THEORY-tmps74c5**, **ARG-tmpid47d**, **CLAIM-560/CLAIM-567** (resource-indexed reachability; reached via CLAIM-tmpyc5md). Pass@ also appears in NOTE-637 and NOTE-869 (test-time compute), unrelated to this result.
- Note per CLAIM.md boundary: BudgetMix as a training recipe is an instruction for ML practice and belongs to the anthology; the record's use is the conceptual finding. A candidate for the `anthology-candidate` flag.

## Limitations

Preprint, v1; small models, four benchmarks; empirical boundary at finite K; step-quality analysis on only two tasks; appendices (incl. the structural upper bounds used to rule out unsolvability) not read.
