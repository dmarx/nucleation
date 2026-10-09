---
status: Proposed
promote_when: >-
  Two kinds of result settle it. For the account of the field: a reading of
  Liu, Zhang and Poor's framework (ISIT 2021; IEEE Trans. Commun. 2022) and
  of one further semantic rate–distortion framework not by these authors,
  each found either to treat meaning as a latent variable with a known
  joint law with the observation, coded through the observation, or not.
  A framework whose limit depends on a property of the meaning beyond that
  joint law and the distortion would refute the general statement. For
  the two identities: an independent check (a published statement, or a
  second reader's derivation) that under Zhao et al.'s definitions the
  expected KL posterior distortion equals I(S;X) − I(S;Y) and the expected
  TV posterior distortion bounds the excess Bayes risk of bounded losses.
  Agreement among papers by the same groups does not count for the first.
title: 'In the semantic rate–distortion frameworks of 2021–2025, meaning is a latent variable with a known joint law with the observation, so their limits are indirect source-coding limits; a posterior-matching semantic distortion is, with KL divergence, exactly the information bottleneck, and with total variation a uniform bound on lost decision value'
version: 1
tags:
- information-theory
- mathematical-statistics
date: '2026-10-09'
source:
- LIT-tmp2w545
- LIT-tmpfnpwq
- LIT-tmpmigxa
- LIT-338
summary: >-
  From the readings of Zhao et al. (2025), LIT-tmp2w545, Chai et al.
  (2023), LIT-tmpfnpwq, and the survey of Xin, Fan and Letaief (2024),
  LIT-tmpmigxa. These frameworks fix meaning as a hidden S with a known
  p(S, X); their theorems are indirect rate–distortion results that do not
  depend on what S is. Zhao et al.'s posterior distortion reduces, for KL,
  to I(S;X) − I(S;Y), making the function the information bottleneck
  (LIT-338), and for TV bounds the extra Bayes risk of every bounded loss.
  The two identities are this record's derivations, not the papers'.
---

<!-- inactive-ok-file: THEORY-156 — Proposed; cited for the qualitative comparison this account's TV bound quantifies -->

# THEORY-tmp3ijnj: In the semantic rate–distortion frameworks of 2021–2025, meaning is a latent variable with a known joint law with the observation, so their limits are indirect source-coding limits; a posterior-matching semantic distortion is, with KL divergence, exactly the information bottleneck, and with total variation a uniform bound on lost decision value

## Source

Zhao, Ma, Li, Yuan, Ye and Zhou (2025), LIT-tmp2w545 (NOTE-tmpsmtp6);
Chai, Xiao, Shi and Saad (2023), LIT-tmpfnpwq (NOTE-tmp5zbie); Xin, Fan and
Letaief (2024), LIT-tmpmigxa (NOTE-tmpcfnb5), for Liu, Zhang and Poor's
framework, which it reports; Tishby, Pereira and Bialek (1999), LIT-338,
for the bottleneck.

## What was actually shown

- **The common form.** In the framework the survey reports (Liu et al.,
  Eqs. 21–22 there), in Chai et al. and in Zhao et al., a source emits
  pairs (S, X) with a joint law known to the designer; the encoder sees X
  only; fidelity is measured on S (directly, by its marginal law, or by
  its posterior) and optionally on X. The theorems are coding theorems for
  that problem: rate I(X; ·) minimised under expected-distortion
  constraints, proved by the standard random-coding or functional-
  representation arguments. Nothing in any of them uses a property of S
  other than its joint law with X and the distortion chosen. Each paper
  could have shown otherwise, by a limit that changes when S is given
  logical, compositional or contextual structure with the joint law held
  fixed; none does.
- **The KL identity.** Zhao et al. measure semantic distortion as
  d_p(p(S|x), p(S|y)), with p(S|y) the posterior under the code and S–X–Y
  Markov. For d_p = KL, E[D(p(S|X) ‖ p(S|Y))] = E log p(S|X)/p(S|Y) =
  H(S|Y) − H(S|X) = I(S;X) − I(S;Y). Their function with no symbolic
  constraint is therefore min{I(X;Y) : I(S;Y) ≥ I(S;X) − D_p}, the
  information bottleneck with the reconstruction as bottleneck variable.
  This is a two-line derivation from their definitions; the paper names
  KL as an admissible d_p and does not draw it.
- **The TV bound.** For d_p = TV and any loss L(a, s) of range at most 1,
  the receiver acting on p(S|Y) has Bayes risk at most E[d_TV(p(S|X),
  p(S|Y))] above one acting on p(S|X), since for each pair
  |min_a E_{p(S|y)}L − min_a E_{p(S|x)}L| ≤ sup_a |E_{p(S|y)}L −
  E_{p(S|x)}L| ≤ d_TV. A bound D_p therefore limits the loss of
  informativeness about S uniformly over every bounded decision problem,
  for the given prior. Also a short derivation; not in the paper.

## What this does not say

- **Not that semantic communication is "only" classical theory.** The
  frameworks may be the right formalisation; the claim is about what they
  formalise. The modelling questions the survey lists as open (what S
  is, where p(S, X) comes from, how knowledge bases enter) are exactly the
  ones these theorems take as given.
- **Not that the survey's other strands reduce.** Logical-probability
  semantic entropy (Carnap and Bar-Hillel, Bao et al.) and the semantic
  capacity definitions are not latent-variable rate–distortion and are
  outside this account. The account covers the rate–distortion strand
  only, in the three readings above plus the framework the survey reports
  second-hand.
- **Not a Blackwell comparison.** The TV bound fixes the prior on S and
  bounds risk for one prior; the Blackwell order (THEORY-156) compares
  experiments for every prior and is qualitative. The bound is a
  prior-dependent, quantitative relative of that order, not the order
  itself, and D_p = 0 gives Bayes sufficiency of Y for S at this prior,
  which for a Markov chain S–X–Y is the same as I(S;Y) = I(S;X).
- **Not about Chai et al.'s perception constraint.** A constraint on the
  marginal law of the reconstruction (Chai et al.) is not
  decision-relative: two reconstructions with the same law can differ
  completely in what they say about S. Only the posterior form carries
  the TV bound.
- **Not about Zhao et al.'s theorems as stated.** Their sequence
  distortion is written as an expected maximum while their proofs use
  maxima of per-letter expectations (NOTE-tmpsmtp6); the identities here
  are single-letter and unaffected, but the coding theorems hold for the
  per-letter form.
