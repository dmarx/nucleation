---
status: Active
status_note: 'read in full 2026-10-13 ([NOTE-tmp6pxon](../notes.d/NOTE-tmp6pxon.md)) from the PubMed Central PDF of the published article (PMC3856819, pmc.ncbi.nlm.nih.gov/articles/PMC3856819/pdf/pnas.201314922.pdf), fetched through the Internet Archive capture of 2022-11-13 because PMC answered scripted requests with a reCAPTCHA page and pnas.org returned 403; the online Supporting Information was not read. Worth reading as the source of effective information as a measure of causal emergence: it shows exactly when a coarse-grained description of a known mechanism can carry more EI than the micro, and its macro advantage rests on imposing a uniform intervention distribution at each level. For [QUESTION-tmpuz3py](../questions.d/QUESTION-tmpuz3py.md) it is an interventional criterion met with no closure and no self-individuation; it complements [CLAIM-154](../claims.d/CLAIM-154.md) and [THEORY-133](../theory.d/THEORY-133.md) and is neither a case nor a rival of them; it measures a different object from the information-decomposition account of [LIT-025](LIT-025.md).'
title: 'Quantifying causal emergence shows that macro can beat micro'
version: 1
history:
- version: 1
  date: '2026-10-13'
  note: >-
    Filed, not read. Citation checked against Crossref on 2026-10-13: Crossref gives the online date 2013-11-18.
    Not held in the Anthology of the SOTA: a grep of its record/ (clone of 2026-10-13, commit d1573d2) for the authors, the title and the DOI found nothing.
    Read the same day (NOTE-tmp6pxon).
tags:
- causality
- complex-systems
- information-theory
date: '2026-10-13'
published: '2013-11-18'
doi: '10.1073/pnas.1314922110'
first_author: 'Hoel'
keywords:
- 'causal emergence'
- 'effective information'
- 'coarse-graining'
- 'macro scale'
implementations: []
summary: >-
  Hoel, Albantakis and Tononi (2013), PNAS 110(49). Effective information,
  the mutual information between uniformly imposed interventions and their
  effects, equals effectiveness (determinism minus degeneracy) times the log
  of the state-space size. Coarse-graining always loses size and can gain
  effectiveness, so in four toy systems of logic gates a macro description
  carries 0.40 to 2.92 bits more than the micro it supervenes on. The
  claim that the EI peak is where causation happens rests on the uniform
  intervention distribution imposed at each level.
---
<!-- inactive-ok-file: THEORY-133 THEORY-tmpuumxo — Proposed; accounts this reading bears on, not leaned on -->

# LIT-tmptmcvs: Quantifying causal emergence shows that macro can beat micro

Hoel, E. P., Albantakis, L., & Tononi, G. (2013). Quantifying causal emergence shows that macro can beat micro. *PNAS* 110(49), 19790–19795. DOI 10.1073/pnas.1314922110

## Key takeaways

Read in full ([NOTE-tmp6pxon](../notes.d/NOTE-tmp6pxon.md)), main text only; the Supporting Information
was not read.

- **EI is effectiveness times size.** Effective information is the mutual
  information between a uniform distribution of interventions on a
  system's states and the resulting next states. Divided by log₂ n it is
  effectiveness, which is average determinism minus average degeneracy.
- **Causal emergence is a difference in EI.** CE = EI(macro) − EI(micro),
  and it splits exactly into a gain in effectiveness and a loss in size.
  The size term is always negative, so the macro wins only when
  coarse-graining makes the mechanism much more deterministic or much less
  degenerate.
- **Four constructed examples** (noise, degeneracy, time, space and time)
  give 0.40, 0.57, 0.62 and 2.92 bits. Systems already near maximal
  effectiveness at the micro level cannot show emergence.
- **The macro is scored under its own uniform interventions**, each macro
  state set by averaging over its micro realizers. The authors say this is
  what lets the macro win. It is a choice, and the paper does not try
  another.
- **Interpretation.** The EI-optimal level is called intrinsic, and the
  macro, when it wins, is said to exclude the micro, turning Kim's
  exclusion argument around. The claims about brains and the sciences are
  conjecture.

## Why this is here

A7 and A11 cited it for when a coalition deserves a higher-level operator
description. The filing's summary was right about the result. It left out
the condition that carries it, the uniform intervention distribution
imposed separately at each level, and it said "causally privileged" where
the paper shows only that EI is higher.

What the reading found, for the codes it was filed for:

- **[QUESTION-tmpuz3py](../questions.d/QUESTION-tmpuz3py.md).** EI is defined by interventions, so CE measures
  interventional autonomy, with predictive autonomy only for predictions
  from imposed states. The paper's systems are fixed logic gates with no
  self-maintenance, and the coarse-graining is an analyst's search, so the
  first criteria can be met with neither closure nor self-individuation.
  The paper's "self-definition" is a figure of speech for the EI maximum.
- **[CLAIM-154](../claims.d/CLAIM-154.md) and [QUESTION-040](../questions.d/QUESTION-040.md).** The same shape of trade-off, a gain
  against a size cost always paid, but for a known mechanism, with no data,
  prior or posterior. It complements the reification rule and is not a
  case of it. With an estimated mechanism, the maximum over many
  coarse-grainings would be biased upward, which is [QUESTION-040](../questions.d/QUESTION-040.md)'s worry,
  and the paper does not discuss it.
- **[THEORY-133](../theory.d/THEORY-133.md).** A complement. Both reach downward exclusion system by
  system; degeneracy reduction is realization insensitivity in information
  terms. Neither paper cites the other.
- **[LIT-025](LIT-025.md).** A different formal object under the same name:
  interventional and comparing two models here, observational and asking
  what a macro feature predicts beyond the parts there.

[THEORY-tmpuumxo](../theory.d/THEORY-tmpuumxo.md) records the result as Proposed.
