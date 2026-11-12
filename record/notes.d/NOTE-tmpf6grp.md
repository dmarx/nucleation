---
status: Read
paper: LIT-2315
title: 'Fang, Jian, Li and Ma — AI-Newton: A Concept-Driven Physical Law Discovery System without Prior Physical Knowledge'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Read on 2026-11-12 from https://arxiv.org/pdf/2504.01538. **Read** (the
    letter), 2026-11-12. A delegated reader drafted the reading; quotations
    were rechecked by script against the downloaded copy, and any that did not
    match were kept as paraphrase without quotation marks.
date: '2026-11-12'
summary: >-
  AI-Newton discovers general physical laws from simulated noisy data across
  46 classical-mechanics experiments without prior physical concepts. It
  keeps an experiment base and a theory base of symbols, concepts and laws
  written in a physical domain-specific language. Concepts are defined
  explicitly: dynamical (e.g. velocity as a derivative), intrinsic (e.g.
  mass, defined by the measurement procedure of a named experiment), and
  universal constants.
---
<!-- inactive-ok-file: TERM-098 — Proposed; cited for what each holds, not as settled -->

# NOTE-tmpf6grp: Fang, Jian, Li and Ma — AI-Newton: A Concept-Driven Physical Law Discovery System without Prior Physical Knowledge

## Contribution

Concept-driven discovery across experiments: laws stated in terms of autonomously defined, reusable concepts, and generalized by extending laws that fail, rather than fitting one model per experiment.

## Key results

- Plausible reasoning (Autonomous discovery workflow): “if a general law holds across multiple experiments but fails in the current one, there is a possibility to derive a valid modified law by adding simple terms to the original formulation via SR.” Example: kinetic-energy conservation fails in spring systems, and the system adds elastic potential energy “to restore conservation”.
- Concepts make laws tractable (Knowledge base; Summary): “Introducing interpretable physical concepts allows discovered laws to remain concise, making them more tractable for SR to identify.”
- Intrinsic concepts carry their measurement (Knowledge base): “Recording the measurement procedures of intrinsic concepts is essential, since it allows the value of an intrinsic property to be retrieved by invoking its defining experiment, ensuring conceptual consistency across different problems.”
- Scale (Rediscovering Laws): with 1200 trials and about 48 hours on average, the system identifies “approximately 90 physical concepts and 50 general laws on average across the test cases”, including energy conservation and Newton's second law.
- Two routes to mass (Rediscovering Laws): gravitational and inertial mass are defined from different experiments and their numerical equivalence is then verified, which the authors present as indicating the weak equivalence principle.
- Redundancy control (Autonomous discovery workflow): redundant knowledge would cause “an explosion in both the theory base and search space”, so laws are simplified to minimal representations each trial.
- Scope (Summary): the laws rediscovered are known ones, “a task where direct reliance on large language models (LLMs) is unsuitable, as they already possess this knowledge”.

## Assumptions

Simulated data from 46 designed experiments with Gaussian noise stand in for real measurement; the space-time coordinates and experimental parameters given are concept-free; the DSL and operators bound what can be discovered; rediscovery of known laws is a fair test of method.

## Concepts

Experiment base, theory base; physical DSL; dynamical concepts, intrinsic concepts, universal constants; specific vs general laws; plausible reasoning; era control; recommendation engine; symbolic regression; Rosenfeld–Gröbner simplification; controlled-variable analysis.

## Bearing on the record

The exchange (A14, decoded line 624), citing the PRR version (4 Nov 2026): "Instead of fitting an equation to one dataset, it proposes physical concepts and progressively generalizes across experiments. It recovered familiar physical laws from noisy mechanics data", "though the laws themselves were not new". Accurate to the arXiv letter. "Noisy mechanics data" is simulated data with added Gaussian errors, which the exchange does not say.

The LIT names no code. Found on recheck:

- **[TERM-099](../terms.d/TERM-099.md)** (self-formation: producing, from a discrepancy the agent cannot yet resolve, a maintained capacity or new distinction that serves later discrepancies): **an instance in a formal system**. A general law failing in a new experiment is the discrepancy; the added term (elastic potential energy) becomes a concept registered in the theory base and reused across later experiments.
- **[CLAIM-475](../claims.d/CLAIM-475.md)** (a stabilized specification is past inquiry stored so later questions become cheaper; it can make other questions harder): **supports the first half, as an instance**. Concepts keep laws concise enough for symbolic regression to find them. The paper's redundancy control speaks to the cost side but does not test the second half.
- **[TERM-098](../terms.d/TERM-098.md)** (concept as a reusable, systematically consequential pattern of distinctions) and **[QUESTION-360](../questions.d/QUESTION-360.md)** (when a learned distinction becomes a concept): **illustrates**. AI-Newton's concepts are explicit, carry their measurement procedures, and are reused across experiments; the mass-unification result is an instance of two routes to one concept. It does not address the question's graded/categorical issue.
- **[CLAIM-419](../claims.d/CLAIM-419.md)** (a move the grammar cannot hold has been answered by amending the grammar): **analogy only**, not claimed: AI-Newton extends a law's form when a case fails, but its DSL (the grammar) is fixed.

## Limitations

Simulated, designed experiments; known laws; one domain (Newtonian mechanics); compute-heavy (48 h on 64 cores per run); details of the recommendation engine and DSL are in the Supplemental Materials, not read.
