---
status: Active
status_note: >-
  read in full 2026-11-04 ([NOTE-tmpnn27v](../notes.d/NOTE-tmpnn27v.md)) from the open-access text in
  Europe PMC (PMC4237059); worth reading as the reference statement of the
  Hierarchical Gaussian Filter: n levels of coupled Gaussian random walks,
  updates that are precision-weighted prediction errors at every level
  (value prediction errors at the first, volatility prediction errors
  above), a perceptual model joined to a response model for per-subject
  MAP estimation, and a first simulation study of parameter recovery.
  Its empirical content is one subject and simulations; recovery was
  tested for two parameters of one model on one input sequence; κ and
  the prior on x3 are confounded unless one is fixed; and the scheme
  still assumes near-quadratic variational energies.
title: 'Uncertainty in perception and the Hierarchical Gaussian Filter'
version: 1
history:
- version: 1
  date: '2026-11-04'
  note: >-
    Registered and read on 2026-11-04 from the owner's pasted synthesis
    on hierarchical probabilistic models in cognitive science, written by
    another assistant, which cites it in §3 as the hierarchical Gaussian
    filter of "Mathys and collaborators", with no year or title.
    Citation checked against Crossref and OpenAlex, which agree with the
    article's front matter: Christoph D. Mathys, Ekaterina I. Lomakina,
    Jean Daunizeau, Sandra Iglesias, Kay H. Brodersen, Karl J. Friston
    and Klaas E. Stephan, Frontiers in Human Neuroscience 8, article 825,
    doi:10.3389/fnhum.2014.00825, PMCID PMC4237059, PMID 25477800.
    `published:` is 19 November 2014, Crossref's online date and the
    Frontiers publication date. The Frontiers page also carries an online
    date of 27 September 2014, probably acceptance or a provisional
    version; what it marks was not confirmed, so it is not used. Read in
    full (NOTE-tmpnn27v) from the Europe PMC full-text XML,
    https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4237059/fullTextXML;
    the Frontiers page was fetched for metadata only.
tags:
- probabilistic-modeling
- learning-and-conditioning
- model-comparison
date: '2026-11-04'
published: '2014-11-19'
doi: '10.3389/fnhum.2014.00825'
first_author: 'Mathys'
keywords:
- 'hierarchical Gaussian filter'
- 'volatility'
- 'sensory uncertainty'
- 'precision-weighted prediction error'
- 'observing the observer'
- 'variational Bayes'
- 'parameter recovery'
extends:
- LIT-tmpld7ct
implementations:
- 'http://www.translationalneuromodeling.org/tapas/'
summary: >-
  Mathys, Lomakina, Daunizeau, Iglesias, Brodersen, Friston & Stephan
  (2014). Generalizes the model of [LIT-tmpld7ct](LIT-tmpld7ct.md) to any number of levels
  and names it the Hierarchical Gaussian Filter: each level a Gaussian
  random walk with variance exp(κ x + ω) of the level above, scaled by
  the time between inputs. Variational inversion gives updates of one
  form at every level above the first, each mean update a prediction
  error weighted by a ratio of precisions: a value prediction error at
  level 1, a volatility prediction error above. Joined to a response
  model, it gives per-subject MAP estimates in transformed parameter
  spaces. Shown on two simulated agents differing in sensory
  uncertainty, one subject from Iglesias et al. (2013) with two response
  models compared by free energy, and a simulation study comparing four
  estimation methods at recovering κ and decision noise ζ.
---
<!-- inactive-ok-file: THEORY-tmph6x8h — Proposed or new; cited from the reading of Mathys et al. (2014) as open -->

# LIT-tmpkft30: Uncertainty in perception and the Hierarchical Gaussian Filter

Mathys, C. D., Lomakina, E. I., Daunizeau, J., Iglesias, S., Brodersen, K. H., Friston, K. J. & Stephan, K. E. (2014). Uncertainty in perception and the Hierarchical Gaussian Filter. *Frontiers in Human Neuroscience* 8: 825. doi:10.3389/fnhum.2014.00825.

## Key takeaways

*From the reading, [NOTE-tmpnn27v](../notes.d/NOTE-tmpnn27v.md).*

- **n levels, one update form.** "here, we extend the HGF explicitly to
  any number of levels" (Introduction); "the updates of the means are
  precision-weighted prediction errors" (Discussion), with "value
  prediction errors (VAPEs) at the first level, volatility (i.e.,
  variance) prediction errors (VOPEs) at all higher levels" (Inversion).
- **Optimal for the agent, not for the world.** "it provides learning
  rates that are optimal given a particular agent's parameter setting"
  (Discussion).
- **Recovery, within limits.** "All optimization methods could reliably
  distinguish different values of κ at low or moderate decision noise
  (Figure 7)"; at high noise κ is underestimated or pulled to mid-range.
- **An identifiability caveat.** "there is a fundamental ambiguity
  between individual differences in coupling (i.e., κ) and individual
  differences in priors for x3 (i.e., μ(0)3)" (Appendix F).

## Standing in the record

The owner's pasted synthesis of 2026-11-04 placed the hierarchical
Gaussian filter beside HDDM ([LIT-563](LIT-563.md)) as hierarchical estimation of
parameters across participants. Here, too, the hierarchy is over states
in one agent's model, and parameters are estimated per subject by MAP
with fixed priors and no group-level pooling; pooling HGF parameters in
the HDDM manner would be an extension this paper does not make. The
synthesis's table row "Hierarchical Bayesian filtering" is the right
placement. This is the paper the record's anxiety-and-uncertainty
entries ([QUESTION-325](../questions.d/QUESTION-325.md), [QUESTION-329](../questions.d/QUESTION-329.md)) rely on for the machinery, not for
evidence about anxiety. Filed from it: [THEORY-tmph6x8h](../theory.d/THEORY-tmph6x8h.md). The paper's
parameter-recovery result is a separable claim, noted in [NOTE-tmpnn27v](../notes.d/NOTE-tmpnn27v.md)
and not filed.
