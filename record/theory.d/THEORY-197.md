---
number: 197
status: Active
formerly:
- THEORY-tmp1hbbz
title: 'Mehta and Schwab''s correspondence between Kadanoff''s variational renormalization group and restricted Boltzmann machines is an identity of parametrizations, under which an exact RG step is a perfect fit of the data distribution; away from that point it does not make training by distribution fitting a renormalization'
version: 4
history:
- version: 2
  date: '2026-10-09'
  note: >-
    Corrected: the free-energy point was called the reader's alone. Lin,
    Tegmark & Rolnick's v2 appendix (LIT-887, read in NOTE-688)
    makes it in substance, and Mehta & Schwab conceded Eq. 8's "iff" as a
    typo in their comment (arXiv 1609.03541). LIT-887 joins the
    sources. The claim is unchanged.
- version: 3
  date: '2026-10-09'
  note: >-
    Schwab & Mehta's comment (LIT-891, read in NOTE-694) joins
    the sources: the mapping's own authors put its content at the trace
    condition and withdraw Eq. 8's converse. The claim is unchanged.
- version: 4
  date: '2026-10-19'
  note: >-
    Promoted, carrying out the promotion audit's decision for THEORY-197
    (batch 038, ADR-047 v2). The promote_when asked for a second,
    independent derivation stating the scope as here. The record already
    held two sources that state it, added in versions 2 and 3: LIT-887's
    v2 appendix makes the normalization point, and LIT-891, the mapping's
    own authors, places its content at the trace condition and withdraws
    Eq. 8's converse. The identity, the exactness condition and the
    free-energy point were also re-derived step by step, in the dated
    note below. The claim is unchanged.
tags:
- natural-sciences
- representation-learning
date: '2026-10-09'
source:
- LIT-882
- LIT-873
- LIT-887
- LIT-891
summary: >-
  Mehta and Schwab (2014), [LIT-882](../literature.d/LIT-882.md), Eqs. 18–22: setting the RG
  kernel T = −E + H makes the RG coarse Hamiltonian equal the RBM's
  hidden-marginal Hamiltonian for every parameter value, and Kadanoff's
  exactness condition equal to zero KL divergence. Short of exactness the
  paper itself says the two use different variational schemes, and
  Koch-Janusz and Ringel ([LIT-873](../literature.d/LIT-873.md)) give a case where distribution fitting
  keeps the wrong variables. The free-energy part of the argument was
  derived independently here; Lin, Tegmark and Rolnick's v2 appendix makes
  it in substance (LIT-887).
answers:
- QUESTION-060
---
<!-- inactive-ok-file: THEORY-194 — Proposed; cited as the empirical counterpart from LIT-873 -->

# THEORY-197: Mehta and Schwab's correspondence between Kadanoff's variational renormalization group and restricted Boltzmann machines is an identity of parametrizations, under which an exact RG step is a perfect fit of the data distribution; away from that point it does not make training by distribution fitting a renormalization

## Source

Mehta and Schwab (2014), [LIT-882](../literature.d/LIT-882.md): Sections I and III, Eqs. 1–22,
and the closing paragraph of Section III; as read in [NOTE-683](../notes.d/NOTE-683.md).
Koch-Janusz and Ringel (2017; Nature Physics 2018), [LIT-873](../literature.d/LIT-873.md): main text
p. 4 and the supplement's comparison with contrastive-divergence RBMs, as
read in [NOTE-674](../notes.d/NOTE-674.md).

## What was actually shown

**The identity.** Kadanoff's variational RG couples hidden spins h to
physical spins v by a kernel T(v, h) and defines the coarse Hamiltonian by
e^{−H^RG(h)} = Tr_v e^{T(v,h) − H(v)}. An RBM has a joint energy E(v, h).
With T = −E + H, H^RG equals the Hamiltonian of the RBM's hidden marginal,
for every parameter value and for any Boltzmann machine (Eq. 21). And
e^T = p(h|v) e^{H − H^RBM}, so the exactness condition Tr_h e^T = 1 for
every v holds exactly when the RBM's visible marginal is the data
distribution (Eq. 22). Both are short, checked derivations.

**The concession.** The paper states that short of exactness RG works on
free energies and the RBM on the KL divergence, and that the two "employ
distinct variational approximation schemes".

**The free energy under the identity** (the reader's derivation from
Eqs. 4, 6, 7 and 18, in [NOTE-683](../notes.d/NOTE-683.md)): F^h = −log Z_λ, so
ΔF = log Z − log Z_λ, which a constant shift of E sets to zero for any
parameters. The criterion variational RG minimizes therefore measures only
normalization once the kernel is the RBM's, and the paper's Eq. 8, which
equates ΔF = 0 with the pointwise exactness condition, is too strong:
ΔF = 0 says only that the condition holds on average under the data. Mehta
and Schwab conceded the "⟺" as a typo in their comment on Lin and Tegmark
(arXiv 1609.03541), and Lin and Tegmark's v2 appendix makes the
normalization point in substance ([LIT-887](../literature.d/LIT-887.md), [NOTE-688](../notes.d/NOTE-688.md)).

**The counterexample.** [LIT-873](../literature.d/LIT-873.md) trains an RBM by contrastive divergence
on fully packed dimers with added decoupled spin pairs; it spends its
hidden units on the noise, then on columnar textures, not on the
staggered patterns that carry the RG-relevant electric fields.

What could have come out otherwise: the identity could have required
conditions on E or on training; it does not. The counterexample's RBM
could have found the fields.

## What this does not say

- **Not that the correspondence is wrong.** Eqs. 18–22 hold, and nothing
  in [LIT-873](../literature.d/LIT-873.md) disputes them.
- **Not that distribution-fitting networks never perform RG.** One
  counterexample shows they need not; when they do is open. The stacked,
  L1-penalized network of [LIT-882](../literature.d/LIT-882.md) was not tested on [LIT-873](../literature.d/LIT-873.md)'s noisy
  dimers.
- **Not that variational RG in Kadanoff's own practice has no
  approximate criterion.** The claim is about the criterion as the
  mapping paper states it (minimize ΔF), under the mapping's kernel.
  Kadanoff's lower-bound schemes, as usually described, keep the trace
  condition exactly and approximate elsewhere; how they fare under the RBM parametrization is
  not worked out in either paper.
- **Not a claim about deep networks other than Boltzmann machines**, nor
  an instruction for machine learning.
- **Nothing about attribute hierarchies or embeddings.** The levels are
  nested spatial blocks.

## Connections

It is the formal counterpart of [THEORY-194](THEORY-194.md), the empirical account from
[LIT-873](../literature.d/LIT-873.md) that the coarse-graining informative about the far environment is
the RG-relevant one while a distribution-fitting one is not. Together they
say: the formalisms correspond exactly, and which variables are kept is
fixed by the objective, not by the correspondence.

## Note of 2026-10-19: the correspondence, re-derived

Write p(v) = e^{−H(v)}/Z for the data. The RBM has joint energy E(v, h)
and marginal energies e^{−H^RBM(h)} = Tr_v e^{−E} and
e^{−H^RBM(v)} = Tr_h e^{−E}, with partition function Z_λ.

- **The identity.** With T = −E + H, Tr_v e^{T − H} = Tr_v e^{−E} =
  e^{−H^RBM(h)}. So H^RG = H^RBM for every parameter value. Nothing about
  training or the form of E is used.
- **Exactness.** Tr_h e^T = e^{H(v) − H^RBM(v)}, which is 1 for every v iff
  H^RBM = H. Then Z_λ = Z and p_λ = p, so an exact step is a perfect fit.
  The converse holds only up to a constant. A perfect fit gives
  H^RBM = H + log(Z_λ/Z), and the trace condition holds once E is shifted
  by that constant, which leaves p_λ unchanged.
- **Short of exactness.** F^h = −log Tr_{h,v} e^{−E} = −log Z_λ, so
  ΔF = log Z − log Z_λ. A constant shift of E sets ΔF to zero for any
  parameters. Under the mapping's kernel, the criterion variational RG
  minimizes measures only normalization, while the RBM minimizes the KL
  divergence. ΔF = 0 is the trace condition only on average under the
  data, which is why Eq. 8's converse fails.
- **The negative half.** It is a non-implication, so one counterexample
  suffices. [LIT-873](../literature.d/LIT-873.md)'s contrastive-divergence RBM fits the distribution of
  dimers with decoupled spin pairs and keeps the wrong variables.

