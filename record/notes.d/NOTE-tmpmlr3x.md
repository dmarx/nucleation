---
status: Skimmed
paper: LIT-tmpjtw0k
title: 'Baik and Silverstein, Eigenvalues of large sample covariance matrices of spiked population models, read for real samples, more variables than samples, and several outliers'
version: 1
history:
- version: 1
  date: '2026-11-21'
  note: >-
    Read on 2026-11-21 by a delegated reader, as a supplement to the BBP
    paper (NOTE-tmpggv08), from arXiv math/0408165v1 (12 Aug 2004), the
    authors' PDF: §1 (pp. 1–5), with Theorems 1.1–1.3 and the limits
    (1.10)–(1.14) as stated. The proofs (§§2–4) were not read, hence
    Skimmed. Running notes on the branch claude/readers/lit-tmpipm3o. The
    quotations below rechecked by the filer by script against the
    downloaded text.
date: '2026-11-21'
summary: >-
  For real or complex samples T^(1/2)Z with i.i.d. standardized entries of
  finite fourth moment and finitely many spikes, at any c = p/n > 0, each
  spike α above 1 + √c gives a sample eigenvalue converging almost surely
  to α + cα/(α − 1); at or below it the top eigenvalue sits at the edge
  (1 + √c)². Limits only: the fluctuations are left open.
---
<!-- inactive-ok-file: THEORY-tmp0zr7o THEORY-tmp0covn CLAIM-tmp5y856 CLAIM-tmp8mvx8 CLAIM-tmpqbo50 CLAIM-tmpk33au CASE-tmp59xy5 ARG-tmpvalfs — Proposed; the reading and the entries it bears on -->

# NOTE-tmpmlr3x: Baik and Silverstein, Eigenvalues of large sample covariance matrices of spiked population models, read for real samples, more variables than samples, and several outliers

## Contribution

The almost-sure limits of every sample eigenvalue of a spiked population
model, for real and complex samples that need not be Gaussian, at any ratio
of variables to samples. It settles for limits the real case that BBP left
as a conjecture. The reading is THEORY-tmp0zr7o.

## Key results

- **Aim** (§1, p. 2): "The purpose of this paper is a complete study of
  the spiked model for both real and complex samples which are not
  necessarily Gaussian. We obtain almost sure limit results."
- **Model.** Samples T^(1/2)Z with Z having i.i.d. entries, E Z = 0,
  E|Z|² = 1, E|Z|⁴ < ∞; B_p = (1/n)T^(1/2)ZZ*T^(1/2), uncentred; p/n → c,
  any c > 0; T has finitely many eigenvalues other than 1, fixed.
- **Each spike its own outlier** (1.10): for each α_j > 1 + √c, the k_j
  sample eigenvalues belonging to it tend almost surely to
  α_j + cα_j/(α_j − 1).
- **One spike** (1.14): the top eigenvalue tends to (1 + √c)² if the
  spike is at most 1 + √c, and to σ_1 + cσ_1/(σ_1 − 1) otherwise.
- **Spikes below 1** give outliers below the lower edge when c < 1
  (1.12)–(1.13).
- **Fluctuations open**: a complete study of the limiting distributions
  "is still an open question".

## Assumptions

Independent, identically distributed standardized entries with a finite
fourth moment; the population covariance acts as T^(1/2) on such a vector;
finitely many spikes, fixed as p, n grow; an uncentred sample covariance of
mean-zero data.

## Concepts

Spiked population model; almost-sure limits of extreme and intermediate
sample eigenvalues; the outlier map α ↦ α + cα/(α − 1).

## Connections

Restates BBP's threshold and location (THEORY-tmp0covn) in the almost-sure
sense and widens them to real and non-Gaussian samples, to c > 1, and to
every spike. It does not restate BBP's fluctuation laws. It notes that Paul
(LIT-tmpxru3g) obtained the same limits for real Gaussian samples with
c < 1. In the record's notation (c = D/N = γ, α = 1 + β): threshold β > √γ
and outlier (1 + β)(1 + γ/β), the same formulas the entries use.

## Bearing on the record

- **CLAIM-tmp5y856** (grounds its threshold for real data). The claim's
  setting is real-valued; this is the theorem that covers it.
  ARG-tmpvalfs.
- **CLAIM-tmp8mvx8** (grounds the count). Counting K_det outliers needs
  (1.10), one outlier per spike above threshold, for a fixed number of
  spikes; a hierarchy whose rank grows with D is outside it, which the
  claim's row 5 shows. ARG-tmpvalfs.
- **CLAIM-tmpqbo50** (grounds its γ = 4 row). D > N is outside BBP and
  inside this theorem, with the same threshold and location. ARG-tmpvalfs.
- **CLAIM-tmpk33au** (grounds the precursor's threshold). The mean-field
  precursor treats the ordering mode as a covariance spike in real data.
  ARG-tmpvalfs.
- **CASE-tmp59xy5** (does not cover it). Its ±1 mixture has a coordinate
  along v that is not distributed like the others, so it is not T^(1/2)Z
  with i.i.d. Z; it falls under Benaych-Georges and Nadakuditi
  (LIT-tmp1q78e) instead.

## Limitations

Limits only, no fluctuations; finitely many fixed spikes; identically
distributed entries, which excludes mixtures like the record's ±1 case;
nothing on eigenvectors.
