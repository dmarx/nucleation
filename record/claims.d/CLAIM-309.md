---
number: 309
status: Active
formerly:
- CLAIM-tmpd7v8w
title: 'How good a mixture is and how discriminable it is from its diluent come
  apart: under linear mixing a smoothie''s distance from milk only shrinks as milk
  is added, so a preference that rises and then falls with milk is over the ratio
  and cannot be a d′, and the signal-detection reading of the owner''s smoothie
  line reverses one of its directions'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  A model of taste in which adding the diluent first increases the mixture's discriminability
  from the diluent alone, with the other ingredients fixed: that is, the distance
  from milk first grows as milk is added. Linear mixing rules it out. A nonlinear
  perceptual map could allow it, and would have to be shown.
tags:
- probabilistic-modeling
- cognition
date: '2026-10-15'
line: formal-apparatus
grounds:
- CASE-096
complements:
- CLAIM-307
summary: >-
  The smoothie note in the owner's LEGO monograph reads the owner's line ([CASE-096](../cases.d/CASE-096.md))
  as signal detection. Milk is the noise, "Less Good" is d′ falling as the mixture
  approaches milk, and "More Good" is d′ rising as a little milk is added. Under
  linear mixing the mixture's taste is (1 − f)s + f·m, and its distance from milk
  is (1 − f)|s − m|. That falls monotonically from the first drop, so discriminability
  from milk cannot rise and then fall. The note's own first model is right: goodness
  is a single-peaked function of the ratio, which is a preference, not a discriminability.
  [MOM-CLM-166](https://github.com/dmarx/mathematics-of-meaning/blob/main/record/claims.d/CLM-166.md) found the same kind of reversal in the formal reading of the LEGO
  parable. MOM's record never mentions the smoothie note.
illustrated_by:
- CASE-096
---

# CLAIM-309: How good a mixture is and how discriminable it is from its diluent come apart: under linear mixing a smoothie's distance from milk only shrinks as milk is added, so a preference that rises and then falls with milk is over the ratio and cannot be a d′, and the signal-detection reading of the owner's smoothie line reverses one of its directions

## The claim

The note's second half, "Smoothies, Milk, and Signal Detection Theory":
"Adding *a little* milk: increases creaminess, boosts the perceptual
distinctiveness of the smoothie relative to milk (higher μ₁ − μ₀), so d′
improves — **More Good**." And: "Your smoothie only tastes like a smoothie
so long as its distribution is discriminable from milk."

**Discriminability from milk only falls as milk is added.** Let taste be a
point in some perceptual space, s for the other ingredients and m for milk.
Under linear mixing the blend at milk fraction f tastes
t(f) = (1 − f)s + f·m, and its distance from milk is
|t(f) − m| = (1 − f)|s − m|. That is strictly decreasing in f, from the
first drop. With equal noise, d′ against milk is proportional to it, so
it never rises. It was checked numerically: for s = (1, 0.3) and
m = (0, 1), the distance at f = 0, 0.2, …, 1 is 1.221, 0.977, 0.732,
0.488, 0.244 and 0. "Less Good" as milk dominates is consistent with
falling d′. "More Good" at first is not.

**What the line is about.** The note's first model already has it:
goodness U = I(V)·Q(f), with Q single-peaked at a preferred fraction f*.
That is a preference over composition. It is a value, and the taster can
find it only because the blends at different f are discriminable. The
two come apart in both directions: two blends can be easy to tell apart
and equally good, or nearly indistinguishable and on opposite sides of the
peak. The ridge f = f* that "more of all the other stuff" stays on is a
ridge of preference. That it is also a ridge of constant d′ against milk
is a coincidence of linear mixing, not the reason the smoothie stays good.

**The pattern.** [MOM-CLM-166](https://github.com/dmarx/mathematics-of-meaning/blob/main/record/claims.d/CLM-166.md) found the formal reading of the owner's LEGO
parable stated with its sign inverted. A criterion for detection was
substituted for one about retrieval, so that the parable's rule (set an
item aside when it does not stand out) was written as its opposite ([CLAIM-307](CLAIM-307.md)). Here a
criterion for discrimination is substituted for one about value, and the
rising half of the owner's *More Good, then Less Good* is reversed. In
both, a signal-detection quantity is put in place of the owner's
quantity, and the owner's own words, kept beside the formal reading (in
the same file here, a link away there), contradict it.

## Why it is Active

The monotonicity is one line under the stated mixing model and was
checked numerically. That the note asserts the rising half is a matter of
its text, quoted above.

## What it does not say

- That signal detection has nothing to say about smoothies. Whether the
  taster can find f* depends on telling nearby blends apart, which is a
  question of d′ between blends, not against milk.
- That perception mixes linearly. A nonlinear map could break
  monotonicity, and the defeat condition says what would have to be shown.
