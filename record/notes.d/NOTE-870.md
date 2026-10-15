---
number: 870
status: Read
formerly:
- NOTE-tmph7b4n
paper: LIT-1055
title: Geisler — Contributions of ideal observer theory to vision research
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Read in full on 2026-10-15 from the NIH author manuscript in PubMed Central
    (PMC3062724, NIHMS252298; accepted manuscript, "unedited manuscript that has
    been accepted for publication", not the typeset Vision Research 51(7), 771–781
    version). The PMC article page (pmc.ncbi.nlm.nih.gov/articles/PMC3062724/) returned
    a reCAPTCHA page to this environment, so the text was taken from the same manuscript
    as NCBI serves it to machines: the JATS XML from E-utilities (eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=3062724),
    which carries the citations and both display equations as MathML, cross-checked
    against the BioC JSON of the same record (ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_json/PMC3062724/unicode),
    which drops citations and equations. Text extracted by script (tags stripped,
    MathML read directly). Read: abstract, all eight sections (Introduction; Ideal
    observers; Pattern detection, discrimination and identification; Pattern estimation;
    Contour and region grouping; Shape, depth and cue integration; Motion; Optimal
    features; Overt and covert attention; Future; Conclusion), all seven figure
    captions and the reference list. The figures themselves were not seen, so numbers
    read off plots are not reported; only numbers stated in the text are. None of
    the cited primary studies was read, so what the review says they found is its
    account of them. Pagination of the printed version could not be checked: the
    Elsevier PDF (sciencedirect.com/science/article/pii/S0042698910004724/pdf, open
    archive per Unpaywall) returned 403, and the Internet Archive's capture of the
    article page could not be reached. Every quotation below was checked against
    the extracted XML text by script, with whitespace normalised.
date: '2026-10-15'
summary: >-
  A short review, not a methods paper. It defines the ideal observer as the device
  that "performs a given task at the optimal level possible, given the available
  information and any specified constraints", writes the Bayesian ideal as an argmax
  of expected utility over the posterior given either the stimulus S or a constrained
  neural representation Z = g(S;θ) (eq. 1), and surveys applications from photon-noise
  detection to eye-movement search. It gives no formula for efficiency and no procedure
  for locating information loss beyond saying that constraints are added to the
  ideal one at a time (optics, receptor sampling, receptor noise, ganglion-cell
  summation) and that models are built by "degrading the ideal observer with hypothesized
  neural noise or with hypothesized heuristic computations". Its constraints restrict
  the information available to an optimal decoder; it has no notion of an optimum
  over a restricted class of computations, though its attention examples compare
  the ideal with specific suboptimal rules (a one-location "serial" mechanism, a
  MAP searcher, a random searcher).
---

# NOTE-870: Geisler — Contributions of ideal observer theory to vision research

## Contribution

A 25th-anniversary review for Vision Research. It sets out the logic of
Bayesian ideal observer analysis in about a page and a half, then surveys
applications in seven areas, mostly behavioural: detection, discrimination
and identification; estimation; contour grouping; shape, depth and cue
integration; motion; optimal features; and overt and covert attention. Its
argument is that the ideal observer is useful for four things: identifying
the task-relevant stimulus properties, describing one sufficient
computation, serving as a benchmark, and generating principled models of
real observers.

## Key insight

The ideal observer is defined relative to what it is given. Geisler: "An
ideal observer is a hypothetical device that performs a given task at the
optimal level possible, given the available information and any specified
constraints." Constraints enter as a mapping from the stimulus to a neural
representation, and the ideal is then optimal on that representation. So
there is not one ideal observer for a task but a family, one for each
stage of the visual system at which the input is taken, and the
comparison of a real observer with ideals at different stages is what lets
the analysis say where performance is lost. The review states this logic
only through examples; it does not formalise it.

## Assumptions

- **Bayesian statistical decision theory.** "Most of the ideal observers
  described here fall within the framework of Bayesian statistical decision
  theory." The ideal knows the prior over world states, the likelihood of
  the (constrained) signal and the utility function.
- **Equation (1).** The ideal response is
  r_opt(Z) = argmax_r Σ_ω γ(r, ω) p(ω | Z), where p(ω | Z) is the posterior
  and γ(r, ω) the utility of response r when the world is in state ω. "If
  there is no constraint function, then Z in equation (1) is replaced by S."
- **Constraint function.** Z = g(S; θ), "the constraint function that
  specifies the mapping of the stimulus into a neural representation"; the
  example is photons absorbed in each photoreceptor. θ allows unknown
  parameters in the mapping, and in the optimal-features section θ is
  the receptive fields being learned.
- **Performance by calculation or simulation.** It "can sometimes be
  determined by direct calculation, but often can be determined only by
  Monte Carlo simulation (i.e., applying equation (1) to random samples of
  the signal Z)."
- **Two-category accuracy case.** With γ = 1 for r = ω and 0 otherwise,
  equation (1) reduces to choosing the category with the higher posterior.
- **Sources of variability** limiting all performance: the stimulus
  (photon noise, category heterogeneity, illumination, 3D-to-2D
  projection), the sensory representation, and the decoding circuits
  (decision and motor noise).
- Elaborations named but not developed: influence graphs (Bayesian
  networks), learning of posteriors, utilities or decision rules, and
  biophysical costs of computation or fitness.

## Key results

These are the review's statements; the numbers come from the cited studies.

**Definition and uses.**
- Benchmark: "The performance of the ideal observer is a precise
  ‘information measure’ that describes how the task-relevant information
  varies across stimulus conditions." If a real observer uses the same
  stimulus properties as the ideal, "its performance should parallel that
  of the ideal observer". "When human performance approaches ideal
  performance, then the implications for neural processing can become
  particularly powerful; specifically, all hypotheses (model observers)
  that cannot approach ideal performance can be rejected. When human
  performance is far below ideal, there are generally a greater number of
  models than could explain human performance."
- Model building: "This is often done by degrading the ideal observer with
  hypothesized neural noise or with hypothesized heuristic computations
  that approximate ideal computations. Models generated this way are
  principled and often have very few free parameters."

**Efficiency.** The review uses the word without defining it. Humans are
"substantially less efficient than the ideal observer" in increment
detection; adding external noise moves performance "closer to that of the
ideal observer (i.e., efficiency increases)"; "Although efficiency is
higher with moderate to high levels of external Gaussian or Poisson noise,
performance is still generally well below ideal." No formula appears, in
terms of d′, thresholds or anything else. Burgess et al. (1981),
"Efficiency of human visual signal discrimination", is cited but its
definition is not reproduced.

**Locating losses: constrained ideals, stage by stage.**
- Photon-noise ideal: threshold for an increment or decrement "increases
  in proportion to the square root of the background (baseline)
  intensity". Humans sometimes parallel it but are far less efficient.
- Adding biological constraints to that ideal: the studies "evaluated the
  additional effects on ideal observer performance of biological
  constraints such as the optics of the eye, the spatial and chromatic
  sampling by the photoreceptors, photoreceptor noise, and ganglion cell
  spatial summation." Finding: human performance "often parallels ideal
  observer performance qualitatively (and sometimes quantitatively)", so
  "the variation in human performance across conditions is often predicted
  by the information available in the retinal responses". "Nonetheless,
  the suboptimal performance of human observers implies substantial
  contributions of central factors." This is the review's only explicit
  statement of where a loss is placed: whatever an ideal observer at the
  retinal output does not lose is attributed to later stages. The method
  behind it (Geisler 1989, "Sequential ideal-observer analysis of visual
  discriminations") is in the reference list but not described.
- External noise (Barlow 1978): high external noise bypasses photon noise
  and retinal factors to "isolate the effects of some of the central
  factors". In white Gaussian or Poisson pixel noise the ideal for
  detection is a template matching the target compared with a criterion.
  For that ideal "the square of contrast detection (or identification)
  threshold increases linearly with the square of the root-mean-squared
  (rms) contrast of the external noise"; human thresholds follow this
  approximately above some noise level, in the fovea and near periphery.
  The intercept gives "an equivalent internal noise", the combined effect
  of the low-level factors the external noise swamps. No equation is
  given.
- Named causes of the remaining loss: internal uncertainty (spatial or
  "channel"), which the review counts as "forms of internal noise that
  necessarily limit performance"; contrast nonlinearities such as gain
  control; and inefficient pooling, measured by classification images.
  Uncertainty and nonlinearities "can only blur (or sharpen) the
  classification image; whereas measured classification images frequently
  reveal missing target features and sometimes added illusory features".

**Examples with numbers.**
- Chromatic estimation from individual cone mosaics (Brainard et al.
  2008): Bayesian optimal colour names for 0.6 min spots at 500, 550 and
  600 nm, nine labels, five subjects; ideal predictions correlate with
  subjects' colour names at r = 0.83.
- Peripheral sampling (Geisler & Perry, under review at the time): at
  2.5 deg eccentricity midget ganglion-cell sampling is about half the
  foveal rate in each direction, "a factor of four fewer samples per unit
  area". A Bayesian decoder using natural-image statistics gives 40%
  smaller mean squared error than linear interpolation on the example
  image and 42% on average over 1000 natural images.
- Contour occlusion (Geisler & Perry 2009): the ideal rule is a lookup
  table from natural-image contour pair statistics. Across 7 subjects,
  without feedback, the ideal observer predicted "approximately 99%" of
  the variance in human responses, with "essentially no part of the
  stimulus space where humans systematically deviate from the ideal
  decision rule".
- Cue combination: for independent Gaussian cues the ideal estimate is
  ω̂ = σ₂²/(σ₁² + σ₂²)·ω̂₁ + σ₁²/(σ₁² + σ₂²)·ω̂₂ (eq. 2). Knill & Saunders
  (2003, texture and stereo slant) and Ernst & Banks (2002, visual and
  haptic height) fit its parameter-free predictions approximately. The
  review notes these designs make the linear rule ideal by construction,
  and that with dependent cues or a choice among generative models the
  ideal is nonlinear.
- Single-fixation search (Eckstein 1998): set size 2 to 12, 2AFC. The
  ideal ("parallel") mechanism with independent noise at each location
  falls with set size "because of the greater chance that some noise
  features will be mistaken for target features"; a "serial" mechanism
  that "can only select one location independent of set size" is the
  suboptimal comparison; one optimal mechanism predicts both feature and
  conjunction displays.
- Multiple-fixation search (Najemnik & Geisler 2005, 2008): an ideal
  searcher limited only by the measured human d′ map across the retina,
  updating the posterior after each fixation and choosing the fixation
  that maximises the probability of locating the target. Human fixation
  counts and accuracy were similar to the ideal and MAP searchers and much
  better than random; the spatial distribution of human fixations was
  closer to the ideal than to MAP. No numbers are given in the text.
- Pattern estimation (Brainard & Freeman 1997): a maximum-local-mass
  estimate outperforms MAP for the illuminant.

## Bearing on the record

**[QUESTION-103](../questions.d/QUESTION-103.md).** The question attributes to this work the statement
that efficiency is "the squared ratio of human to ideal d′". The review
does not say this. It uses "efficiency" informally and gives no formula.
The squared-d′-ratio definition is the standard one in the literature it
cites (Burgess et al. 1981; Pelli and Farell 1999 are in its reference
list), but the record should either cite one of those or say the formula
is the record's, not Geisler's. [LIT-1055](../literature.d/LIT-1055.md)'s summary ("the comparison of
human with ideal performance, as efficiency, to locate where information
is lost") is fair as a description of the field, but this paper states
the location-of-loss logic in one paragraph (the retinal-constraints
work) and the efficiency comparison only in passing.

The bounded-observer bridge is narrower here than the question needs.
Geisler's constrained ideal observer restricts the *input*: it is optimal
on Z = g(S; θ), a garbling of the stimulus. Losses are located by moving
the point where the ideal takes its input (stimulus, retinal image,
receptor absorptions, ganglion-cell output) and seeing how much
performance each stage costs. That is a data-processing argument:
each constrained ideal is still unrestricted in computation. The
computational-indistinguishability side of the question ([CLAIM-302](../claims.d/CLAIM-302.md))
restricts the *test class* and leaves the input intact, and the gap it
exhibits, near-total variation with no feasible test above chance, is not
produced by any garbling of the input, since a garbling that left total
variation near one would leave the ideal's ROC near perfect. So the two
frameworks share the benchmark (the likelihood-ratio ideal of [THEORY-031](../theory.d/THEORY-031.md))
and the form of the comparison (real or restricted performance against
ideal), but Geisler's degraded ideal is not a bounded-observer optimum
in the record's sense. The nearest thing in the review to a class-restricted
observer is "degrading the ideal observer with ... hypothesized heuristic
computations", and the attention examples, which compare the ideal with
single named suboptimal rules (serial one-location selection, MAP fixation
choice, random fixation), not with the best rule in a class. The review
also notes the asymmetry the question would need: near-ideal human
performance rejects every model that cannot approach ideal, while
far-below-ideal performance leaves many models standing. That is the
empirical analogue of the point that a gap below the ideal does not
identify which restriction produced it.

What the review does supply for the question: a precise definition of the
ideal relative to information and constraints (eq. 1), the template-matcher
ideal in white noise, the linear threshold-squared versus noise-variance law
with its equivalent internal noise, and the named sources of residual loss
(uncertainty, nonlinearity, pooling). Uncertainty is the closest bridge:
an observer uncertain about location or channel must combine many
irrelevant template outputs, which is a loss from the decision rule, not
from the input, and the review counts it as internal noise.

**[THEORY-031](../theory.d/THEORY-031.md).** Consistent with it and adds nothing to it formally. The
two-category accuracy case of eq. (1) is the posterior-maximising
likelihood-ratio rule at threshold set by the priors. The review uses d′
only for the search experiments.

**[CLAIM-302](../claims.d/CLAIM-302.md).** No bearing on the claim itself, which is a theorem
about ensembles. The review does not discuss computational limits on the
observer except as noise, heuristics, or biophysical cost of computation,
which it names as an elaboration without development.
