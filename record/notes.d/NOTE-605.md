---
number: 605
status: Read
formerly:
- NOTE-tmp5zbie
paper: 'LIT-812'
title: 'Rate-Distortion-Perception Theory for Semantic Communication'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from arXiv v1 (9 December 2023, 6 pages, text extracted
    with pdftotext): Sections I–VI, Appendices A and B, the reference
    list. Figures 1–2 were not seen; their captions and the text's
    observations about them were. The proofs were followed as far as the
    paper gives them: Appendix A is a sketch, and Appendix B states the
    reduction and omits the solution ("The detailed proof is omitted").
    The binary relation d(S, Ŝ) = (1 − 2q) d(X, Ŝ) + q was rederived.
date: '2026-10-09'
summary: >-
  Formulates semantic communication as indirect source coding of a hidden
  source S, observed by the encoder only through X, with decoder side
  information, common randomness, an expected-distortion constraint on S
  and a total-variation constraint on the law of the reconstruction.
  States a rate region (proof sketched) and a binary closed form, showing
  that perfect recovery of X does not recover S and that side information
  alone can meet loose constraints at zero rate.
---

<!-- inactive-ok-file: THEORY-161 — Proposed; filed from this batch's readings, under test -->
<!-- inactive-ok-file: LIT-767 — Deferred; cited as the classical Wyner–Ziv result this paper builds on -->
<!-- inactive-ok-file: CLAIM-050 — Proposed; named as a manuscript claim this reading bears on -->

# NOTE-605: Rate-Distortion-Perception Theory for Semantic Communication

## Contribution

It joins two existing lines: the rate–distortion theory of a semantic
source that the encoder sees only indirectly (Liu, Zhang and Poor; Xiao et
al.), and the rate–distortion–perception trade-off (Blau and Michaeli;
Theis and Wagner), in a model with Wyner–Ziv side information and common
randomness. The result is a stated rate region and a binary-source closed
form. The paper is a workshop paper; its theorems are given with sketched
or omitted proofs.

## Key insight

If meaning is a hidden variable S behind what the sender observes, then a
good reconstruction of the observation is not a good reconstruction of the
meaning: in the binary case, the error on S is an affine function of the
error on X with intercept q, the observation noise. And if the receiver
already has side information correlated with S, there is a level of
tolerated error at which it needs nothing from the sender.

## Assumptions

- S i.i.d.; the encoder receives k indirect observations X via p(X|S); the
  channel carries m symbols; the reconstruction Ŝ lives in S's alphabet.
- Side information: Wyner–Ziv variables Y′ (encoder) and Y″ (decoder),
  defined separately, but the region uses a single Y; common randomness U
  shared by encoder and decoder.
- Perception measured by total variation between p_S and p_Ŝ, per block
  (strong) or in expectation over empirical distributions (empirical).
- Binary closed form: S ~ Ber(π), doubly symmetric binary p(X|S) with
  crossover q, symmetric side-information channels (u* = v*, a* = b*).

## Key results

- **Definition 3 / Theorem 1.** R^(s) = {(R, D, P): ∃Z, p_SXYZ = p_S
  p_XY|S p_Z|X, R ≥ I(X; Z|Y), I(S, X; Z|Y) ≤ (k/m) I(M; M̂),
  E d(Sⁿ, Ŝⁿ) ≤ D, D_TV(p_Sⁿ, p_Ŝⁿ) ≤ P}; R^(e) replaces the block TV by the
  single-letter one. (R, D, P) is achievable iff it lies in the closure.
  *Holds when:* as stated; the proof (Appendix A) is a binning sketch for
  achievability and a pointer to Merhav and Shamai for the converse.
- **Theorem 2.** For the doubly symmetric binary case,
  R(D, P) = R_{πx}(D_x) for D ∈ [q, π′_x) when P ≥ π_x; for 0 < P < π′_x
  it is R_{πx}(D_x) on [q, D′), R_{πx}(D_x, P) on [D′, π′_x), and 0
  beyond, with D_x = (D − q)/(1 − 2q), π′_x = (1 − 2q)π_x + q. The proof
  reduces to a Lagrangian problem and omits its solution.
- **Observation 3.** d(S, Ŝ) = (1 − 2q) d(X, Ŝ) + q, so d(S, Ŝ) ≥ q, with
  equality when Ŝ reproduces X exactly.
- **Observation 5.** With side information, the rate reaches zero at
  D = π_x, not at D = 1/2: the decoder outputs Ŝ = Y.
- **Experiment.** MNIST, x = s + noise, side information y = f_Y(x) a
  learned feature of the observation, uniform quantisation (L = 8),
  loss MSE + λ·Wasserstein (by a GAN critic). Curves: R_S|Y below R_S;
  R_S|Y above R_X|Y.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The stated region characterises achievable (rate, distortion, perception) for an indirectly observed source with side information and common randomness | weak: proof sketched; the region's printed form is incomplete (see Bearing) | Theorem 1, Appendix A |
| C2 | For the binary case the rate–distortion–perception function has the stated closed form | weak: solution omitted | Theorem 2, Appendix B |
| C3 | Reproducing the observation exactly does not reproduce the semantic source; semantic distortion is at least the observation noise | strong (for the binary model) | Observation 3, rederived |
| C4 | With side information, loose enough constraints are met at zero rate | strong, and standard for Wyner–Ziv problems | Observation 5 |
| C5 | Side information lowers, and indirect observation raises, the achievable rate on images | weak: learned operating points, not the function; no error bars | Fig. 2 |

## Concepts

- **semantic information source**: a random variable S carrying "rich
  intrinsic knowledge" that the encoder cannot observe directly.
- **indirect observation**: X, a noisy or partial view of S, the only
  input of the encoder.
- **Wyner–Ziv side information**: a variable correlated with the source
  available at the decoder (and here possibly the encoder), described as
  the user's background, language or preference.
- **perception-based semantic distance**: a divergence between the laws
  of S and Ŝ (total variation in the theory, Wasserstein in the
  experiment).
- **strong / empirical perception constraint**: TV between n-block laws,
  or expected TV between empirical distributions.

## Connections

It applies Blau and Michaeli's rate–distortion–perception function and
Theis and Wagner's coding theorem to the indirect semantic source of Liu,
Zhang and Poor and of Xiao et al. (its reference [9], by two of the same
authors). Its side-information treatment follows Hamdi and Gündüz and Niu
et al. The underlying problem, coding a source seen through noise, is the
remote or indirect rate–distortion problem of classical information
theory; the paper does not use that name. Wyner and Ziv's rate–distortion
function with decoder side information is held here as [LIT-767](../literature.d/LIT-767.md). Zhao et
al. ([LIT-793](../literature.d/LIT-793.md)) cite this paper as a semantic RDP framework and replace
its perception constraint, on the marginal law of Ŝ, by a constraint on
posteriors p(S|x) and p(S|y).

## Bearing on the record

- **[CLAIM-088](../claims.d/CLAIM-088.md).** The claim's description is accurate in substance:
  this is "a formal rate–distortion–perception treatment of semantic
  communication with encoder/decoder side information". Two precisions.
  The side information is defined at both ends, but the region and the
  binary result use one variable Y, available to both. And what is
  preserved is a single hidden variable S under one distortion and the
  marginal law of Ŝ; the paper does not consider several tasks or decision
  problems, or the conditional distribution of S given the message. So it
  establishes task-sensitive preservation for one task fixed in advance.
- **[CLAIM-050](../claims.d/CLAIM-050.md)** (fidelity relative to the receiver's decisions,
  made precise by Blackwell's order). The perception constraint here is
  not decision-relative: two reconstructions with the same marginal law
  can carry very different information about S. The distortion
  constraint is decision-relative for one loss only. Nothing in the paper
  compares experiments.
- **The region as printed** does not define Ŝ in terms of Z and Y (the
  distortion and perception constraints refer to an Ŝ the region never
  constructs), and it mixes a source-coding rate with a joint
  source–channel condition. A reader should take the binary Theorem 2,
  whose constraints are explicit, as the paper's usable result.
- **Observation 5** is presented as a finding about semantic
  communication; it is the general fact that a Wyner–Ziv rate is zero once
  the allowed distortion is what the decoder's side information achieves
  alone. Its interpretation, that a receiver can infer the meaning from
  shared background without any message when tolerances are loose, is the
  paper's gloss.
- A typo with content: Section III calls both H(X|S) and H(S|X) "the
  semantic redundancy"; from the surrounding text the second is meant as
  the semantic ambiguity induced by indirect observation.
- One of three sources of [THEORY-161](../theory.d/THEORY-161.md). Not machine-learning
  practice; no anthology flag.

## Limitations

- Six pages: the coding theorem's proof is a sketch, and the binary
  solution is omitted.
- The experiment trains networks at chosen operating points; it shows
  achievable points, not the function, and uses Wasserstein distance where
  the theory uses total variation.
- In the experiment the side information is a function of the encoder's
  observation, f_Y(x), given to the decoder: an unusual source of side
  information, since in a Wyner–Ziv problem the decoder's variable is not
  computed from what the encoder sees.

## Open questions

- A complete proof of Theorem 1 with Ŝ defined, and a check against the
  known indirect rate–distortion–perception results it should reduce to
  when Y is trivial.
- Whether the perception constraint should be on the marginal of Ŝ, or,
  as Zhao et al. propose, on the conditional law of S given what is
  received; the paper does not discuss the choice.
