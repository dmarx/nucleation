---
status: Read
paper: LIT-2363
title: 'Caliari (2026) — Behavioural welfare analysis and revealed preference'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Read on 2026-11-22 in the sweep of the Unfetched works (batch B), from
    a reader's draft the filer checked against the downloaded text. Copy:
    the publisher's open-access PDF,
    https://link.springer.com/content/pdf/10.1007/s11238-026-10164-1.pdf
    (CC BY 4.0, open access funded through WZB and Projekt DEAL), version
    of record, online first with no volume or pages yet, which answered
    one GET on 2026-11-22 with HTTP 200, application/pdf, 32 pages (on
    2026-11-12 the same host gave a "Client Challenge" page). Checked:
    title, sole author Daniele Caliari (WZB Berlin), Theory and Decision,
    received 9 September 2024, accepted 2 September 2026. Read §§1–5 and
    Appendix D; Appendix A skimmed; the proofs (Appendices B and C) and the
    references skipped; the data and code repository named in the paper
    not opened. Status Read rather than Skimmed because the argument and
    the experiment were read in full and only the proofs were not. The
    EconStor copies were not needed. The filer rechecked every quote below.
date: '2026-11-22'
summary: >-
  A researcher wants welfare preferences from the choices of people who are
  not utility maximizers, without knowing their behavioural model. Bernheim
  and Rangel's Pareto relation avoids false positives but is coarse.
  Caliari proposes an axiom, Informational Responsiveness: one more choice
  of x with y available breaks an indifference toward x. With neutrality,
  choice non-negativeness and an independence axiom, it characterizes
  weighted choice-count refinements of the Pareto relation that recover the
  true preference for all preference-monotonic choice models. In an
  experiment with 145 students most violate WARP, and such methods cut
  expected false positives against stated rankings.
---
<!-- inactive-ok-file: THEORY-1693 — Proposed; Freer and Nosratabadi's reading, set beside this one -->

# NOTE-tmphq6zm: Caliari (2026) — Behavioural welfare analysis and revealed preference

## Contribution

An axiomatic middle way between model-based welfare analysis and Bernheim
and Rangel's "model-less" approach: properties of a welfare method fix the
family of behavioural models under which it is correct. Plus an experimental
test against stated rankings, with a coarseness against false-positive
trade-off.

## Key results

1. **The trade-off (§1).** The researcher "faces a trade-off between the
   uncertainty of a coarse welfare preference and the mistakes of an
   incorrectly elicited one".
2. **"Model-less" is a misnomer (§1).** "a better description of this
   approach is "implicitly model-based," as each welfare method, being an
   inverse mapping, naturally imposes constraints on the models of
   decision-making".
3. **Informational Responsiveness (§2.1, Axiom 1).** "an indifference should
   always be broken by welfare-relevant choices"; first introduced by
   Goodin and List as "One Vote Responsiveness" (footnote 1).
4. **Proposition 1 (§2.2).** On single-menu data, a method satisfies IR,
   neutrality and choice non-negativeness exactly when it elicits correctly
   for the preference-monotonic models. The Bernheim–Rangel method "fails to
   elicit the underlying welfare preference more and more often as" data
   grow.
5. **Proposition 2.** On homogeneous datasets these axioms with
   transitivity guarantee much less: "in most cases a negative answer to
   whether IR can generalize the Pareto relation" (Remark 2).
6. **Proposition 3.** Adding Connection, an independence axiom, gives
   exactly the weighted counting refinements of the Pareto relation with
   positive menu weights, correct for all preference-monotonic models on
   any dataset.
7. **The threshold is the researcher's (§2.3.1).** The number of
   observations needed to break an indifference "is a decision variable for
   the researcher"; "the BR method, violating IR, is equivalent to
   unanimity. This implies, in our choice setting, giving veto power to
   irrationalities."
8. **Attention-type models fall outside (footnote 8).** Models based on
   attention, salience, perception, reference points or context "violate IR
   and CNN because they induce a misalignment between choice probabilities
   and the underlying deterministic preference".
9. **Aligned data assumed (§2.3.2).** "If we allow for sampling variation …
   our proofs do not follow through."
10. **Inconsistency is common (§4.1).** "In Time, 63% of the participants
    violate WARP at least once, while in Risk this percentage grows to 94%."
11. **Time (§4.2.1).** The Pareto relation uniquely identifies the top
    alternative for 55% of participants, the Proposition 3 methods for 87%;
    expected false positives for the top alternative 26% against 12%, for
    the whole preference 44% against 35%.
12. **Risk (§4.2.2).** The Pareto relation uniquely identifies the top
    alternative for 12% and set-identifies it for 88%; expected false
    positives for the top alternative 57% against 39%. The ranking of
    Proposition 3 over Proposition 2 methods "seems less clear" here.
13. **Completeness (§4.3).** The Proposition 3 family comes "surprisingly
    close" to an oracle method fitted to the stated rankings, which is
    "purely diagnostic"; the one menu type given negative weights,
    asymmetric dominance in Time, is "a potential source of false
    positives".
14. **The attention model's welfare relation is nearly empty in data
    (Appendix D).** The Masatlioglu et al. method "uniquely identifies the
    best alternative only for 1 out of 145 participants" in Time, and 14 in
    Risk.

## Assumptions

- Each decision-maker has a complete, transitive welfare preference that a
  stochastic choice model maps to choice probabilities.
- Datasets are aligned with the generating model, as if sampled many times;
  the experiment has one observation per menu, which "is therefore unlikely
  to satisfy the alignment property" (§4.3.1).
- The stated, non-incentivized ranking is the welfare preference against
  which methods are scored.
- Neutrality: no prior information about alternatives or models.

## Concepts

Welfare method; Pareto relation (Bernheim–Rangel); coarseness versus false
positives; implicitly model-based; Informational Responsiveness;
Connection; choice non-negativeness; neutrality; preference-monotonic
models; additive perturbed utility; counting revealed preference and its
weighted versions; aligned and homogeneous datasets; WARP violations; set
versus unique identification; expected false positives; completeness;
attention filter.

## Bearing on the record

- **On the LIT's characterization.** A's account ("recovering
  welfare-relevant preferences from inconsistent choices without knowing
  the behavioural model, with an informational-responsiveness criterion
  and experiments") is right in outline, with one correction: the methods
  need no explicit model but are "implicitly model-based" and guaranteed
  only for preference-monotonic models, so attention, salience and
  reference-point models are outside. "Recovering" is also stronger than
  shown: in Risk the expected false-positive rate for the top alternative
  is 39%.
- **[QUESTION-456](../questions.d/QUESTION-456.md)**, failure mode 2: supports and sharpens it (dated note
  there). Any rule from choices to preferences embeds a model of
  behaviour; the rule is reliable only when choice frequency is monotone in
  preference, which selective attention breaks; and the threshold for
  breaking an indifference is the analyst's normative choice.
- **[LIT-2458](../literature.d/LIT-2458.md)** (Caliari and Petri), the neighbour read in this work's place:
  superseded as a stand-in, since the target is now read. The two agree in
  theme at different levels.
- **[THEORY-1693](../theory.d/THEORY-1693.md)** (Freer and Nosratabadi): the same finding from the data
  side, that under the standard limited-attention model choices reveal
  almost nothing (result 14).
- **[CLAIM-482](../claims.d/CLAIM-482.md)**: a different notion of revealed preference, not a rival
  (dated note there).
- **[LEAD-158](../leads.d/LEAD-158.md)**: weak bearing (dated note there).
- **No instruction for machine-learning practice.**

## Limitations

- **The benchmark is stated, non-incentivized rankings**; a "false
  positive" is disagreement with what subjects say afterwards, which the
  paper assumes is welfare-relevant.
- **The theory assumes aligned data and the experiment has one
  observation per menu**, so the match between theorems and experiment is
  by analogy.
- **The oracle method is fitted to the reported rankings**, so
  completeness scores are relative to them.
- **Preference monotonicity is assumed, not tested directly**, and the Risk
  results leave it unclear.
- **Sample**: 145 students at the University of St Andrews in 2019, in two
  domains whose inconsistency barely correlates.
- Welfare-relevant preferences that differ from both choice and report are
  outside the framework.
