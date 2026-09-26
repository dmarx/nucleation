---
number: 156
status: Read
formerly:
- NOTE-tmpqazja
paper: LIT-182
title: 'Towards ethical evolution: responsible AI autonomy'
version: 2
history:
- version: 2
  date: '2026-09-26'
  note: >-
    Read in full (The full text of the published version (CC BY 4.0), from
    the self-archived copy at the University of Jyväskylä (JYX). Seeding
    downloaded it to rawP5/p101.pdf; it was copied to rawA/terziyan.pdf and
    extracted with PyMuPDF, since pdftotext is not installed. It is 27 PDF
    pages: a JYX cover sheet, the article on pp. 1–21, and 169 references on
    pp. 21–26. The read covers the abstract and §§1–8, including every
    subsection, Tables 1–3 and the back matter. The reference list was
    scanned for alignment literature, not read entry by entry. Figs. 1 (a
    history timeline) and 2 (the GA paradigm diagram) were seen only as
    captions. Springer was not retried, because the JYX file is the
    published version. Pages below are the article's own (PDF page − 1); the
    journal pagination is 5165–5190.). Upgraded from `Skimmed` to `Read`:
    the claims table, assumptions and results are new, and the skim is
    corrected where the full text disagreed.
date: '2026-09-26'
summary: >-
  The paper proposes, without implementation, formalism or experiment,
  that an AI system which designs further AI systems should pass on one
  "immutable" principle. The principle is: do not directly harm humanity
  or violate fundamental human values; monitor and mitigate misuse of your
  outputs; and make every derivative inherit this principle (p. 12). The
  mechanisms are a genetic-algorithm analogy, with immutable and mutable
  "genes", constrained crossover and filtered mutation, together with
  "temporal cloning". The paper is inconsistent about its central notion.
  The principle is enforced once by a penalty F = Q − α·P (p. 9) and once
  by "unbreachable" hard constraints (p. 13). And it is "immutable" only
  in its architecture, while its ethical content stays "adaptable" (p.
  14).
---

<!-- inactive-ok-file: LIT-182 — Deferred: the paper is placed by this reading; the directive lapses when its status changes; the directive lapses when its status changes -->

# NOTE-156: Towards ethical evolution: responsible AI autonomy

## Contribution

The paper names a problem: keeping ethical constraints intact when AI systems design, clone or spawn successor AI systems. It gives the problem a vocabulary: "meta-responsibility", "responsibility inheritance", "responsibility decay", "recursive accountability" and "temporal genetic responsibility". It proposes one candidate principle, with a heritability clause built in, as the invariant to preserve (p. 12). It adds nothing that is established after reading it. The mechanisms are named, not specified:
- crossover restricted to mutable genes;
- post-mutation ethical validation;
- cryptographic inheritance, a "blockchain-like" lineage and tamper-proof hardware with self-deactivation (§6.3, p. 18);
- "future clones".

No algorithm is stated beyond a five-line "Generic TGR Algorithm" (p. 17). No threat model, formal guarantee or implementation is given.

## Key insight

The paper's intended insight is that a heritability clause belongs inside the protected principle itself: "Any derivative products of AI must inherit this principle as an immutable safeguard" (p. 12). The clause makes the principle self-propagating across generations of AI designers. The rest of the paper maps that idea onto genetic-algorithm operators. Its own later concession undercuts the insight. If only the structure is immutable and the content of "harm" and "values" can be updated (p. 14), then the clause preserves a label, not a constraint.

## Assumptions

- **Ethical content can be encoded as an enforceable invariant.** The example is "do no harm" written as "if action(a) → outcome(o), ensure o ≠ harm" (p. 9). The conclusion concedes that the framework "assumes that ethical principles can be universally agreed upon and encoded without ambiguity" (p. 21).
- **Successor design can be modelled as GA-style evolution.** Designing a successor is treated as recombination and mutation of "genes" over a population, evaluated by a fitness function (§4). This fits evolutionary search. The paper also claims to cover LLM agents that "design, spawn, or reconfigure other agents via prompt chaining, code synthesis, or memory transfer" (p. 6), and it never shows how those map onto genes.
- **The designer can verify the successor.** Pre-deployment compliance checks, sandbox simulations and "AI-driven auditing" are assumed to detect violations (§6.1, §6.3, pp. 17–18). How a system verifies an arbitrary successor's future behaviour is not discussed.
- **Constrained systems are viable.** §7.1 raises this assumption as an open challenge (pp. 18–19) and does not resolve it.

## Key results

(Nothing is proven or measured. This is what the paper proposes.)

- **The candidate immutable principle** (p. 12): "AI must not act in ways that directly harm humanity or violate fundamental human values. AI must proactively monitor and mitigate potential misuse of its outcomes to prevent indirect harm. Any derivative products of AI must inherit this principle as an immutable safeguard." It has three components: direct harm prevention, indirect harm mitigation and principle inheritance (pp. 12–13).
- **Meta-responsibility** (§3, pp. 7–9):
  - inheritance, which should be "explicitly defined", "adaptively mutable" and "traceable";
  - decay, from environmental drift, mutation, incomplete accountability and optimisation bias, answered by audits, mutation screening and contextual adaptation;
  - recursive accountability, through self-regulation, external oversight, meta-learning and time-travel abstractions.
- **The ethical GA** (§4, pp. 9–15): immutable principles as hard-coded genes; crossover "only among mutable components"; mutation followed by validation; fitness F = Q − α·P as the "simplified" form (p. 9).
- **Temporal genetic responsibility** (§5, p. 17). There are five steps: initialise immutable and mutable genes; generate future clones; retrieve their feedback; adjust mutable genes; iterate. The section adds parallel "temporal multiverse" exploration and recursive correction of version t−1 by version t.
- **The inheritance mechanism** (§6.3, p. 18): cryptographic safeguards, ethical blueprints in software and hardware, pre-deployment compliance verification, a blockchain-like lineage, counterfactual simulation, tamper-proof hardware and self-deactivation. All are listed, and none is designed.
- **Open challenges** (§7.1, pp. 18–19): decentralised enforcement; survival of constrained AI against unconstrained competitors; safeguards for agents with indefinite lifespans; and unchecked accumulation of power.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Ethical principles can be preserved across AI generations by encoding them as immutable genes with constrained crossover and mutation. | assertion | §4, pp. 9–15; no implementation or example run |
| C2 | The proposed principle "is resilient to ethical dilemmas" and "prevents 'loophole' exploitation". | assertion | pp. 12–13 |
| C3 | The principle "aligns with" deontology, utilitarianism and virtue ethics, "ensuring robustness against philosophical critiques". | assertion | p. 12; one citation per theory, no argument |
| C4 | Immutable principles act as unbreachable hard constraints, not penalty terms. | contradicted within the paper | pp. 13–14 vs. F = Q − α·P on p. 9 and "heavily penalized … weighted" on p. 18 |
| C5 | The principle's core is immutable while its interpretation evolves with prevailing norms. | assertion; in tension with C1 and C4 | pp. 12, 14; §7.4 |
| C6 | Ethically constrained AI may be at a competitive disadvantage against unconstrained systems. | informal argument (conceded as an open challenge) | §7.1, pp. 18–19 |
| C7 | "Proposed framework demonstrates that autonomous systems can evolve responsibly." | unsupported; contradicted by the paper's own limitations paragraph | p. 21 vs. "require further empirical validation", p. 20 |
| C8 | Industry practice already shows retention of ethics across transfer, e.g. "BERT/RoBERTa: transfer learning on platforms like HireVue demonstrates the retention of ethical principles". | assertion (bulk citation) | Table 3, p. 6 |

## Method

This is conceptual design by analogy. Biological inheritance and genetic-algorithm operators are mapped onto ethical constraints for self-designing AI, and the mapping is illustrated with Asimov's Three Laws and his stories (pp. 10–11). The paper runs no simulation or experiment and gives no formal model. The five-step TGR algorithm (p. 17) and the three-step "ethically filtered mutation algorithm" (p. 15) are the only procedures, and both are at the level of named steps.

## Concepts

- **Meta-responsibility.** A recursive design imperative: agents must ensure their successors "retain ethical alignment" (p. 7).
- **Responsibility inheritance.** The transmission of core ethical principles to offspring or clones, which must be explicitly defined, adaptively mutable and traceable (p. 7). The paper itself calls it "a vague concept somehow related to genetic responsibility" (p. 7).
- **Responsibility decay.** The erosion of ethical behaviour across generations, likened to concept drift (pp. 7–8).
- **Recursive accountability.** Internal oversight: self-audit, peer or parent review, meta-learning of accountability criteria, and clone probes (pp. 8–9).
- **Immutable / mutable principles.** Hard-coded ethical "genes" versus adaptive secondary guidelines (§§4.1–4.2).
- **Structural immutability with semantic adaptability.** The p. 14 restatement: the architecture is fixed and the ethical content can be updated.
- **Temporal genetic responsibility (TGR) and temporal cloning.** Feedback from "future clones" to current agents (§5.1, p. 17).
- **AI-as-a-designer-of-AI.** Any architecture in which AI participates in the recursive design, refinement or instantiation of other AI systems, "potentially including themselves" (p. 6).

## Connections

The motivating case is LLM-agent systems that design agents, with Hu, Lu & Clune's *Automated Design of Agentic Systems* as ref. 1, and self-evolving LLMs (ref. 2). Neither is held in either record. The authors build on their own earlier work: responsible cognitive digital clones [35], "AI as a user of AI" [37], and 3D-printed intelligent entities [36]. The problem is the one the alignment literature treats as preservation of goal content under self-modification and successor design. The paper does not engage that literature beyond bulk citations (see corrections). It also does not engage the corrigibility tradition, which cuts against the paper's own "immutable, self-inherited" design.

**Account of agency.** The paper presupposes a thin, engineering account. An agent is an optimiser with a fitness function, operating autonomously and able to design, clone and audit other agents. Autonomy means designing successors "with minimal human intervention" (p. 2). The paper assigns responsibility to AI agents themselves: agents "must ensure that their successors … retain ethical alignment" (p. 7), and act as "both designer and auditor" (p. 18). Whether an AI system can bear responsibility is listed as a research direction in Table 1 and Table 2 ("The problem of AI agents' ability to bear responsibility", p. 5). It is then assumed rather than addressed. No account is given of goals, intention or moral agency.

**Agency tag: justified, weakly.** The title's subject is "responsible autonomy", and the paper is about the autonomy and control of machine agents across generations, which falls within the tag's blurb ("autonomy, control … in machines"). Someone browsing agency would not be wrong to expect it. The paper presupposes an account of agency rather than offering one, so agency should stay behind ethics, as it now is.

## Bearing on the record

- **Anthology-candidate: the flag should be removed.** The work carries no ML practice (see corrections). The alignment problem it names, preserving values across AI-designed successors, is real. If the anthology ever wants a source for practice on recursive self-improvement or agent-spawning safety, this paper would not serve as that source, because it establishes nothing.
- The record has no THEORY documents for it to support or contradict. No other held document cites [LIT-182](../literature.d/LIT-182.md); a grep of literature.d and notes.d on 2026-09-26 found only its own LIT and NOTE.
- The dossier's "home: anthology" judgement should not be carried forward as a reason for anything.

## Limitations

- **Nothing is implemented, formalised or tested.** The authors say the constructs "require further empirical validation in real-world settings" (p. 20). The conclusion nonetheless says the framework "demonstrates that autonomous systems can evolve responsibly" and "offers a robust solution" (p. 21).
- **The central notion is inconsistent**, as a penalty term versus a hard constraint, and as immutable versus semantically adaptable (see corrections).
- **The ethical content is deferred.** "The final choice of principles must therefore be left to domain experts" (p. 14; §7.4). The one candidate principle rests on undefined terms: "humanity", "fundamental human values", "harm". The paper concedes their meaning varies and will be interpreted "according to the understanding … at the moment in time when it is enacted" (p. 12).
- **No threat model.** Adversarial successors, deceptive compliance with audits, and a designer that is itself misaligned are not considered. Cryptographic and hardware safeguards are listed without saying what they would prevent or how.
- **The GA analogy covers little of the paper's own motivating case.** It fits population-based evolutionary search, but not an LLM agent writing code or prompts for a successor, which the paper names as its "primary application domain" (p. 6).
- **Some supporting examples are dubious.** Table 3's claim that HireVue's use of BERT/RoBERTa "demonstrates the retention of ethical principles during AI knowledge transfer" is one (p. 6).
- The acknowledgements note that AI tools were used for language editing (p. 21).

## Open questions

- Can a designer AI verify that a successor preserves a constraint whose content is itself allowed to change? This is the question the paper's p. 14 concession raises and leaves open.
- Is a self-inheriting, unoverridable principle compatible with human correction of flawed principles? That is the corrigibility tension, and the paper does not address it.
- Would any concrete instantiation show that constrained crossover and mutation keep a behavioural constraint across generations of agents that design agents, not only across GA populations? Such a demonstration is what would move the work from Rejected to Proposed.

## Corrections to the seeded skim

- The anthology-candidate flag does not hold. The dossier set the home to anthology because the subject is "how AI systems are designed". The paper, however, carries no ML practice. It has no method a practitioner could run, no training or evaluation procedure, and no empirical claim. The only formula is a generic penalised fitness F = Q − α·P (p. 9), and the "Data availability" statement says no datasets were generated or analysed (p. 21). It is AI-ethics and governance argument in *AI and Ethics*, and it belongs in nucleation under ethics and society-and-governance. Recommend removing `anthology-candidate`.
- The immutable principle is not inherited as content. The dossier's summary says systems "carry an immutable harm-prevention principle". The paper concedes that the immutability "refers to the architectural design", while "the ethical content instantiated within this structure may remain adaptable, allowing updates to the actual principles (e.g., interpretations of harm, fairness, or autonomy)" (p. 14). The same point appears as "ethical variables" (p. 12) and in §7.4 (p. 20). So what is immutable is the scaffold, and the ethical drift the paper sets out to prevent can re-enter by reinterpretation.
- Hard constraint vs. penalty is internally contradictory, and the dossier smooths it over. Three passages disagree:
  - §4.1 enforces the principle with a penalty term, F = Q − α·P, and says a solution may be preferred "even if their raw performance (Q) is slightly lower" (p. 9).
  - pp. 13–14 insist the principles are "not mere soft constraints … Unlike traditional penalty terms".
  - §6.2 says violations are "heavily penalized" in "a weighted multi-objective fitness function, where ethical constraints act as hard boundaries" (p. 18).

  The dossier reports only §6.2's hard-constraint version.
- The alignment engagement is thinner than "not cited", and differently so. The dossier says the paper cites IEEE and Turing guidelines, "not e.g. corrigibility or reflective stability". The reference list does include Bostrom [71], Russell, *Human Compatible* [76], and Hadfield-Menell et al.'s cooperative IRL [97]. They appear only as bulk citations in Table 2 (p. 5) and are never discussed. Corrigibility, goal-content integrity, reflective stability and Omohundro-style drives are indeed absent, from the text and from the references.
- The "time-travel abstraction" is two different things, and neither is time travel. §3.3 describes clones "deploy[ed] … in diverse environments" and "periodically recall[ed]" as probes (p. 8). §5.1 has "future clones" evaluate the current agent and "inform current agents" (p. 17). How a future clone is generated is never said, so "temporal cloning" amounts to forward simulation. §5.5 calls the whole a "speculative but grounded vision" (p. 17).
