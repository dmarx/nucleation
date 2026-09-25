---
status: Deferred
status_note: seeded from the abstract and a skim on 2026-09-25; not read in full
title: 'The Work Capacity of Channels with Memory: Maximum Extractable Work in Percept-Action Loops'
version: 1
tags:
- information-theory
- agency
- natural-sciences
date: '2026-09-25'
published: '2025-04-08'
arxiv: '2504.06209'
doi: 'unverified (see access)'
first_author: 'Fiderer'
keywords:
- 'work capacity'
- 'percept-action loops'
- 'stochastic thermodynamics'
- 'hidden Markov channels'
- 'predictive agents'
implementations: []
summary: >-
  Fiderer et al. (2025), [ARXIV-2504.06209](https://arxiv.org/abs/2504.06209). When an agent's actions change what it later perceives, the maximum rate at which it can extract work from its environment (the environment channel's "work capacity") is in general reached neither by a maximally predictive agent nor by one that randomizes its actions and forgets them. Prediction and forgetting have to be traded off.
---

# LIT-tmp6pfj4: The Work Capacity of Channels with Memory: Maximum Extractable Work in Percept-Action Loops

Lukas J. Fiderer, Paul C. Barth, Isaac D. Smith, Hans J. Briegel (2025), *arXiv preprint* — [ARXIV-2504.06209](https://arxiv.org/abs/2504.06209)

## Key takeaways

- When an agent's actions change what it later perceives, the maximum rate at which it can extract work from its environment (the environment channel's "work capacity") is in general reached neither by a maximally predictive agent nor by one that randomizes its actions and forgets them. Prediction and forgetting have to be traded off.

*Seeded from the abstract and a skim, not a reading. What follows is what the work says about itself.*

Prediction is widely treated as the organizing principle for adaptive systems, and earlier thermodynamic work on agents reading a fixed tape found that maximal prediction is required to reach the energetic limit. Real agents also act on their environment. The authors model agent and environment as coupled hidden-Markov (finite-state) channels forming a percept-action loop and analyse its stochastic thermodynamics. They define the work capacity of an environment channel as the maximum expected work per round that any agent can extract. They show that the two earlier design principles for work-efficient agents (maximize predictive power, and randomize and forget your own actions) stop being optimal once actions have observable consequences: remembering past actions improves prediction but lowers the free energy available. They conclude that prediction and energy efficiency can conflict in active learning systems.

## Standing in the record

Filed from the survey of 2026-09-25 of work the anthology set aside as out of scope (tier A): 120 seconds of active reading over 8 sessions in the papers-feed tracker. `Deferred` because nobody has read it closely here yet, not on merit.

**Priority for a deeper reading: high — It is the journal's named scope decline, so the filing decision depends on it. The owner's reading time is low (t=120 s over 8 sessions, i.e. revisited often), and the DOI or published version still needs confirming before a note is filed. The skim covers the argument but not the proofs.**

What a deeper reading should check:

- The anthology's journal names this as its one scope decline by title. The skim supports the decline: this is information-thermodynamics theory. There are no ML experiments, no training recommendation and no evaluation method, and the cs.LG listing and LLM mentions are motivation only. It is not `analysis-and-evaluation` material. It fits a reading-list note under information-theory, with agency as a secondary tag.
- A deeper reading should check whether the PRX version (if 10.1103/7nds-tjr8 is it) changed any results or framing, and pin the DOI before filing.
- Check how strong the "prediction vs. efficiency" claim really is. The counterexample (Thm 5) is a small hand-built binary environment. It is worth asking whether the trade-off is generic or an edge case, and how it relates to the free-energy principle, which the abstract invokes but the paper never engages formally.

Access when seeded: I read the arXiv abstract page and the full v1 PDF (42 pp.: 10 pp. main text plus 32 pp. supplement). I read §I–VI of the main text in full, plus Table I and the theorem statements; I did not work through the supplement's proofs. arXiv lists cs.LG as the primary category, with cond-mat.stat-mech, cs.IT, nlin.AO, nlin.CD and quant-ph. Crossref has a Physical Review X DOI, 10.1103/7nds-tjr8, dated 2026-08-10, under a different title: "Information thermodynamics of agents: The work capacity of channels with memory". Its metadata is a placeholder (author "Anonymous"), and the APS landing page returned 403 (Cloudflare challenge). That makes it very likely the journal version, but I have not confirmed it, so the doi field is left unverified.
