---
number: 194
status: Active
formerly:
- THEORY-tmpsylqv
title: 'On Monte Carlo samples of the 2D Ising model and of the 2D dimer model with added noise spins, a block coarse-graining trained to maximize mutual information with the system beyond a buffer recovered the variables renormalization already uses (Kadanoff block spins; the dimers'' low-momentum electric fields, with no weight on the noise), and iterated on 128 × 128 Ising samples gave the flow away from the critical point, locating it to about 1% and giving ν ≈ 1.0 ± 0.15, while a restricted Boltzmann machine trained by contrastive divergence on the noisy dimer data coupled to the noise and to columnar patterns instead'
version: 4
history:
- version: 2
  date: '2026-10-09'
  note: >-
    The authors' two sequels join the sources: Lenggenhager et al. 2020
    (LIT-881, read in NOTE-682), which proves that a
    coarse-graining keeping all of a block's information about its
    environment adds no range to the Hamiltonian, though the optimised
    coarse-grainings fall short of that condition; and Gökmen et al. 2021
    (LIT-878, read in NOTE-681), which extends the evidence to the
    interacting dimer model across a BKT transition, with operators already
    known from field theory. Neither meets promote_when. The claim is
    unchanged.
- version: 3
  date: '2026-10-09'
  note: >-
    Two further sources: Gordon, Banerjee, Koch-Janusz & Ringel 2021
    (LIT-885, read in NOTE-690), which proves that near the
    first information-bottleneck transition the optimal encoder of a slab
    follows the leading transfer-matrix mode, the relevant operator at
    criticality, though not for a block in a buffer shell nor for the RSMI
    optimum; and Gökmen et al. 2021 (LIT-889, read in NOTE-692),
    the 2D Ising results and the ensemble of optimal filters. Neither meets
    promote_when. The claim is unchanged.
- version: 4
  date: '2026-10-20'
  note: >-
    Narrowed and promoted, carrying out the promotion audit's decision for
    THEORY-194 (batch 061, ADR-047 v3). The title moves from "the
    renormalization-group relevant one" for the 1D and 2D Ising and 2D
    dimer models to what LIT-873, read in full in NOTE-674, measured on
    the two 2D models, with the figures checked against the arXiv PDF. The
    1D filter comparison is among three candidate filters, so it stays in
    the body. The closing gloss, that which variables a compression keeps
    is set by what it must stay informative about, is the record's
    reading and moves to a dated note. The promote_when moves unchanged to
    QUESTION-tmpjpe7s.
tags:
- natural-sciences
- information-theory
- representation-learning
date: '2026-10-09'
source:
- LIT-873
- LIT-881
- LIT-878
- LIT-885
- LIT-889
summary: >-
  Koch-Janusz and Ringel (2017), [LIT-873](../literature.d/LIT-873.md): shown numerically on two
  2D lattice models whose relevant variables were known (Ising block
  spins, dimer electric fields), with an iterated Ising flow giving T_c to
  about 1% and ν ≈ 1.0 ± 0.15, and analytically only for 1D and quasi-1D
  chains. The general equivalence of the objective with a short-ranged
  effective Hamiltonian is argued, not proved, and no system with unknown
  relevant variables was tried.
supports:
- CLAIM-152
---
<!-- inactive-ok-file: THEORY-036 THEORY-017 QUESTION-025 — Proposed or open; cited as accounts this one bears on and the question it does not answer -->

# THEORY-194: On Monte Carlo samples of the 2D Ising model and of the 2D dimer model with added noise spins, a block coarse-graining trained to maximize mutual information with the system beyond a buffer recovered the variables renormalization already uses (Kadanoff block spins; the dimers' low-momentum electric fields, with no weight on the noise), and iterated on 128 × 128 Ising samples gave the flow away from the critical point, locating it to about 1% and giving ν ≈ 1.0 ± 0.15, while a restricted Boltzmann machine trained by contrastive divergence on the noisy dimer data coupled to the noise and to columnar patterns instead

## Source

Koch-Janusz and Ringel (2017; Nature Physics 2018), [LIT-873](../literature.d/LIT-873.md): main
text Figs. 2, 4 and 5; supplement Eqs. 5–15 (the estimator), Eqs. 20–40
(1D Ising), Eqs. 41–44 (saturation), Figs. 8–11; as read in [NOTE-674](../notes.d/NOTE-674.md).

The sequels: Lenggenhager, Gökmen, Ringel, Huber & Koch-Janusz (2020),
[LIT-881](../literature.d/LIT-881.md), Appendix B's theorems, as read in [NOTE-682](../notes.d/NOTE-682.md); and Gökmen,
Ringel, Huber & Koch-Janusz (2021), [LIT-878](../literature.d/LIT-878.md), the interacting dimer
model, as read in [NOTE-681](../notes.d/NOTE-681.md). The formal counterpart, on why a fitted
coarse-graining is not one, is [THEORY-197](THEORY-197.md) from Mehta & Schwab's
mapping ([LIT-882](../literature.d/LIT-882.md)).

## What was actually shown

**The objective.** For a block V, a buffer B and the environment E beyond
it, choose the coarse variables H, drawn from an RBM-form P_Λ(H|V), to
maximize I_Λ(H : E). Only Monte Carlo samples are used.

**Numerically, in 2D.** For the Ising model the maximizer on a 2 × 2 block
is Kadanoff's block spin, and on larger blocks it weights the boundary. For
the fully packed dimer model it reads the low-momentum electric fields of
the height-field description, and it gives zero weight to decoupled,
regularly patterned noise spins. Iterated four times on 128 × 128 Ising
samples, it produces the flow away from T_c on both sides, locates T_c to
about 1%, and gives ν ≈ 1.0 ± 0.15. An RBM trained by contrastive
divergence to fit the noisy dimer data instead spends its hidden units on
the noise, then on columnar patterns that carry no field. Each could have
come out otherwise: the maximizer could have coupled to the noise, the
flow could have failed to separate, or the fitted RBM could have found the
fields too.

**Analytically, in 1D.** Among decimation, boundary-majority and uniform
majority filters for the 1D Ising chain, decimation, the known optimal RG,
carries twice the boundary filter's information and the uniform filter's
vanishes with block size. For 1D and quasi-1D systems with short-range
interactions, if adding hiddens no longer increases the information, the
effective Hamiltonian has no coupling across the block.

## What this does not say

- **Not that the objective finds relevant variables in general.** Every 2D
  case had a known answer. The account is that, on these models, the
  objective and RG agree; whether they agree where RG's variables are
  unknown is what [QUESTION-tmpjpe7s](../questions.d/QUESTION-tmpjpe7s.md) asks.
- **Not a proof of equivalence with RG in two or more dimensions.** The
  equivalence with a compact, short-ranged effective Hamiltonian is proved
  only for 1D and quasi-1D chains, and the 1D comparison is among three
  filters, not over all.
- **Not that distribution-fitting networks never coarse-grain correctly.**
  One dataset shows that they need not; when the two objectives coincide is
  open.
- **Not that the variables are intrinsic to the data.** The block, buffer
  and environment are a spatial partition supplied before anything is
  learned, and the buffer's width is a choice. Mutual information is
  invariant under bijections of the variables, but the partition is not;
  so, consistently with [THEORY-017](THEORY-017.md), the parts the method compresses are
  given to it.
- **Not a hierarchy of attributes.** The levels are nested spatial blocks.
  Nothing here concerns attributes implying one another, linear attribute
  directions in embeddings or concept lattices, so it leaves [QUESTION-025](../questions.d/QUESTION-025.md)
  as it was.
- **Not an instruction for machine learning.** It says which objective
  coincides with RG on these models, not how to train anything.

## Connections

It gives an operational criterion for the scale-relative, lossy
description that [THEORY-036](THEORY-036.md) and Ladyman's real patterns ([LIT-219](../literature.d/LIT-219.md)) take RG
as their example of: the compression that counts is the one that keeps
information about the far field. The objective is a variant of the
information bottleneck ([LIT-338](../literature.d/LIT-338.md)) with the environment as the relevance
variable.

## Note of 2026-10-20: scope at promotion

Promoted on one study read in full ([ADR-047](../decisions.d/ADR-047.md) v3). [NOTE-674](../notes.d/NOTE-674.md) read the
figures from their captions. For the promotion they were checked against
the arXiv PDF of [LIT-873](../literature.d/LIT-873.md) (18 pp.). Fig. 2(A) shows a single hidden unit
weighting a 2 × 2 block uniformly. Fig. 4 shows 8 × 8 filters with the
staggered E_y and E_x ± E_y patterns. Fig. 5 shows effective temperature
against RG step for starting T/T_c from 0.98 to 1.03: the curve from 0.99
flows down and the one from 1.002 flows up. Fig. 11 shows the
contrastive-divergence filters coupling to the noise pairs, then to
columnar textures. The 1% and ν ≈ 1.0 ± 0.15 are stated in the text,
together with the method (finite-size data collapse over four RG steps,
5000 samples per temperature). The supplement's Fig. 9 says only that
the slope is "consistent with" ν = 1.

Three things are left out of the title. First, the 1D result: it compares
three filters on the paper's proxy for mutual information, to leading
order in block size, and decimation scores twice the boundary filter.
That does not show decimation maximizes the objective over all filters.
Second, the general equivalence with renormalization, which
[QUESTION-tmpjpe7s](../questions.d/QUESTION-tmpjpe7s.md) now carries. Third, the former title's closing
gloss, that which variables a compression keeps is set by what it must
stay informative about. That is the record's reading of these results,
and [THEORY-202](THEORY-202.md) cites this account for it. The results are consistent
with it but do not test it apart from the choice of environment.
