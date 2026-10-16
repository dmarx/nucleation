---
number: 466
status: Active
formerly:
- THEORY-tmp8lv8d
title: "Among contestants of equal prowess with dangerous weapons, individual selection can favour conventional fighting backed by retaliation: an escalating Hawk is not evolutionarily stable, Retaliator is at most neutrally stable because Mouse ties it, and in a contest settled by persistence alone no fixed persistence is stable while an exponential mixture is"
version: 1
tags:
- natural-sciences
- game-theory
date: '2026-10-16'
source:
- LIT-505
summary: >-
  Maynard Smith & Price (1973), [LIT-505](../literature.d/LIT-505.md), read in full in [NOTE-404](../notes.d/NOTE-404.md). A
  simulation of five strategies, 2,000 contests per pairing, shows that
  "limited war" can be favoured by individual selection, without benefit to
  the species. The paper calls Retaliator an ESS "though Mouse does equally
  well", which fails its own second condition. There is no Hawk–Dove game,
  no "dove", no difference in prowess and no ownership, so it is not the
  source of display, deference or owner–intruder conventions.
---

<!-- inactive-ok-file: LIT-503 — Proposed: Curry 2016, the statement of morality-as-cooperation; cited for the hawk-dove contests it credits to Maynard Smith & Price -->

# THEORY-466: Among contestants of equal prowess with dangerous weapons, individual selection can favour conventional fighting backed by retaliation: an escalating Hawk is not evolutionarily stable, Retaliator is at most neutrally stable because Mouse ties it, and in a contest settled by persistence alone no fixed persistence is stable while an exponential mixture is

## Source

Maynard Smith & Price (1973), "The Logic of Animal Conflict", [LIT-505](../literature.d/LIT-505.md)
(*Nature* 246: 15–18), read in full in [NOTE-404](../notes.d/NOTE-404.md). Table 1 digits misread by
OCR were checked against values the prose quotes.

## What was actually shown

**The ESS (p. 17).** A strategy I is evolutionarily stable if, for all J,
E_I(I) > E_I(J); or if E_I(I) = E_I(J), then E_J(I) > E_J(J).

**The contest model.** Contestants have "identical fighting prowess" and no
memory across contests. Moves are conventional, dangerous or retreat. One
dangerous blow injures seriously with probability 0.10. Payoffs: +60 for a
win, −100 for serious injury, −2 per non-injuring blow received, up to +20
for a short contest. Losing uninjured scores 0, so future breeding remains.

**Table 1.** Mouse and Bully each beat Hawk in a Hawk population, so Hawk
is not an ESS. Mouse scores 29.0 against Retaliator, as Retaliator does
against itself, and Retaliator scores 29.0 against Mouse, as Mouse does
against itself. The paper: "Retaliator is an ESS since no other strategy
does better, though Mouse does equally well." By its own second condition
that tie makes Retaliator at most neutrally stable. Prober-Retaliator "is
almost an ESS".

**Sensitivity.** Hawk becomes the ESS if a dangerous blow injures with
probability 0.90, or if retreating uninjured costs as much as serious
injury. The qualitative result is said to survive "moderate changes"; those
runs are not shown.

**War of attrition (p. 17).** If the contestant willing to pay more wins
and both pay the smaller cost, no pure strategy is stable: a little more
persistence beats any fixed m. The mixture p(x) = (1/v)exp(−x/v) is an ESS.
The derivation is deferred to later work.

**What could have come out otherwise.** Escalation could have paid in a
population of retaliators. It does not under the stated payoffs, though it
does under the high-injury and costly-retreat variants.

## What this does not say

- **That Retaliator is strictly stable.** Mouse can drift in. Gale & Eaves
  (1975) commented on the analysis; that comment was not read.
- **A Hawk–Dove game.** The word "dove" does not occur, and the strategies
  are Mouse, Hawk, Bully, Retaliator and Prober-Retaliator. The record holds
  no source for the two-strategy game.
- **Display and deference.** Contestants are identical, so assessment of a
  superior opponent appears only in the informal "Real Animals" section, as
  argument ([NOTE-404](../notes.d/NOTE-404.md), C6).
- **Ownership or division.** There is no owner–intruder asymmetry, and the
  war of attrition is about who takes the whole prize.
- **That the strategy space was searched.** Five strategies were chosen by
  hand, and only means of the simulated contests are reported.

## Connections

- Hamilton's Part II ([LIT-506](../literature.d/LIT-506.md), [THEORY-655](THEORY-655.md)) explains restraint between
  relatives by relatedness. This explains it between non-relatives by
  retaliation.
- Axelrod & Hamilton ([LIT-498](../literature.d/LIT-498.md), [THEORY-672](THEORY-672.md)) take the ESS concept from
  here. Their TIT FOR TAT is neutrally stable in the same way Retaliator is.
- Morality-as-cooperation ([LIT-503](../literature.d/LIT-503.md)) and [NOTE-034](../notes.d/NOTE-034.md) credit this paper with
  "hawk–dove contests". [NOTE-404](../notes.d/NOTE-404.md) corrects that: it grounds restraint backed
  by retaliation, and only informally the retreat from a superior and the
  honest signal.
