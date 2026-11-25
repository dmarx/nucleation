---
number: 1269
status: Proposed
formerly:
- CLAIM-tmpei0cf
title: 'Relative to a separately justified standard, many cognitive biases are spurious sensitivity, a response that varies under a transformation of the situation that the standard treats as irrelevant, or spurious invariance, a response that does not vary under one the standard treats as relevant, so a family of response contrasts under controlled transformations is a candidate signature of a perspective, not yet a character in the representation-theoretic sense'
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  A set of well-established biases each of which, with its transformations
  and its normative standard declared, shows no mismatch between the
  response's contrasts and the standard's, so that the two classes cover few
  of them; or a showing that the classification depends on no declared
  standard, so that the same response is spurious sensitivity under every
  standard.
tags:
- cognition
- epistemology
date: '2026-11-24'
line:
- pragmatic-transport
- nucleating-argument
works:
- governance-of-becoming
complements:
- CLAIM-085
- CLAIM-298
uses:
- TERM-026
summary: >-
  A11 §§4 and 5 of the exchange "Memes, Contracts, and Systemic Normativity"
  (2026-11-24), answering the owner's U10. A bias is read as a mismatch
  between how a perspective's response changes under a controlled
  transformation of a situation and how a separately justified standard
  says it should change: changing where the standard does not
  (framing, irrelevant anchors, source weighting), or not changing where
  it does (stereotyping, base-rate neglect). For a transformation that is
  its own inverse A11 splits a response into parts that transform by the
  trivial and the sign representation of C₂. The assistant's note of
  2026-11-24 below shows both classes are one quantity and that a bias
  uniform across the transformations escapes both. The wording is A's
  (ChatGPT, in the exchange 'Memes, Contracts, and Systemic Normativity');
  adopting it is the owner's call.
---

<!-- inactive-ok-file: CLAIM-298 LIT-3238 — Proposed or Deferred; the held frame claim and the unread work A11 cites -->

# CLAIM-1269: Relative to a separately justified standard, many cognitive biases are spurious sensitivity, a response that varies under a transformation of the situation that the standard treats as irrelevant, or spurious invariance, a response that does not vary under one the standard treats as relevant, so a family of response contrasts under controlled transformations is a candidate signature of a perspective, not yet a character in the representation-theoretic sense

## The claim

A11 §4 defines, for a perspective P's response R_P(x) to a situation x and a
transformation g of "its presentation, source, temporal order, social
implications or relationship to existing commitments", the response
contrast Δ_P(g,x) = R_P(gx) − R_P(x), and "A family of such contrasts
provides a candidate signature of perspectival organization." Its table
pairs transformations with the biases they would reveal: an irrelevant
numerical starting point with anchoring, gain against loss framing with the
framing effect, the source's identity with authority or ingroup bias,
repetition without evidence with the illusory truth effect, ownership with
the endowment effect. "This is not yet a mathematical character in the
strict representation-theoretic sense."

A11 §5: "Some cognitive biases involve distinguishing situations that ought
to be treated equivalently. Others involve treating situations equivalently
that ought to be distinguished." So: "**Spurious sensitivity:**
responsiveness to differences irrelevant to the task. **Spurious
invariance:** insensitivity to differences relevant to the task. Many
familiar cognitive biases can be investigated through combinations of these
properties. Their classification as biases, however, remains relative to an
independently specified task, environment or normative standard."

For an "independently anchored binary transformation g, such that applying
it twice returns the original situation", A11 writes R⁺(x) = (R(x) +
R(gx))/2 and R⁻(x) = (R(x) − R(gx))/2: "These transform according to the
trivial and sign representations of C₂", and "where two situations are
equivalent under an independently justified decision criterion, the
antisymmetric component measures the response's sensitivity to their
framing difference." The decomposition is textbook and was checked
(`python3 -I`): R = R⁺ + R⁻, R⁺(gx) = R⁺(x), R⁻(gx) = −R⁻(x).

## Where the record stands

- [CLAIM-085](CLAIM-085.md) holds the standard-relativity for one case: a framing effect in
  a model is a property of the model, and what ought to be preserved "is a
  normative question that model response distributions, being descriptive,
  cannot settle". This claim generalizes the form and keeps that point.
- [CLAIM-298](CLAIM-298.md) and [TERM-026](../terms.d/TERM-026.md) hold a frame as an operation on an interpretive
  state, and [CLAIM-041](CLAIM-041.md) holds that noncommuting framing operations do not by
  themselves show nonclassical probability.
- [CLAIM-249](CLAIM-249.md) and [CLAIM-132](CLAIM-132.md) are the qualification A11 repeats: comparing
  characters needs one group identified on both sides, and "establishing
  the relevant equivalence and correspondence is substantive, not merely
  mathematical".
- Klayman and Ha ([LIT-3238](../literature.d/LIT-3238.md)), as A11 reports them, are why the standard
  matters: a positive test strategy is a bias in some environments and not
  in others.

## What it does not say

That every bias is one of the two, that the signature Φ(P) is a group
character, or that the standard can be read off the responses.

## Standing

Proposed, in A's voice.

## Note of 2026-11-24: both classes are one quantity, and a uniform bias escapes both

The assistant's gap fill ([ADR-137](../decisions.d/ADR-137.md)) for A11 §§4 and 5, which state the two
classes and the C₂ decomposition but do not relate them, and do not say
which biases the contrasts cannot see.

**One quantity.** Let R_* be the standard's response, and g an involution.
Then Δ_P(g,x) = R_P(gx) − R_P(x) = −2R⁻_P(x), and likewise for R_*. So the
mismatch of contrasts is Δ_P − Δ_* = −2(R⁻_P − R⁻_*). Spurious sensitivity
is R⁻_* = 0 with R⁻_P ≠ 0; spurious invariance is R⁻_* ≠ 0 with R⁻_P = 0
(or smaller in magnitude). Both are the one difference R⁻_P − R⁻_*, read
where the standard's antisymmetric part vanishes or does not.

**What escapes.** A response that departs from the standard by an offset
that does not change under the transformations considered, R_P = R_* + c,
has Δ_P(g,x) = Δ_*(g,x) for every g in the family, so no response contrast
shows it. Its measure is the symmetric part's mismatch R⁺_P − R⁺_*, the
level, which a profile of contrasts discards. Overconfidence measured as an
excess of confidence over accuracy that is the same across the item sets
compared is such a bias. So the duality covers biases of sensitivity, and
the signature Φ(P) misses biases of level unless the family includes a
comparison with the standard's own value. Checked by hand; the algebra is
two lines.

The wording is the assistant's (Claude, in this session); adopting it is
the owner's call.
