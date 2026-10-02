---
number: 404
status: Read
formerly:
- NOTE-tmpjvb5a
paper: 'LIT-505'
title: 'The Logic of Animal Conflict'
version: 1
history:
- version: 1
  date: '2026-10-02'
  note: >-
    Read in full (Nature 246: 15–18, from the course-library copy at
    public.ek-cer.hu/~szabo/EGT20/library/maynard_n73.pdf; text extracted
    with PyMuPDF). Whole article, Table 1 and references read. Table 1
    digits partly misread by OCR ("SO.O", "-lS.l"); the entries used here
    were checked against values the prose quotes (Mouse v. Hawk 19.5 and
    80.0) and against the row/column logic of the text.
date: '2026-10-02'
summary: >-
  Five strategies for contests with dangerous weapons, simulated 2,000
  times per pairing with payoffs +60 win, −100 serious injury, −2 per
  scratch, up to +20 for brevity. Hawk is not an ESS; Retaliator is
  called one though Mouse ties it, so by the paper's own second
  condition it is only neutrally stable. In a war of attrition no pure
  strategy is stable; the exponential mixture p(x) = (1/v)e^(−x/v) is.
  Individual selection can explain limited war. No Hawk–Dove game, no
  ownership.
---

<!-- inactive-ok-file: LIT-503 — Proposed: Curry 2016, the statement of morality-as-cooperation filed in the same batch; cited for which sources it credits for each domain -->

# NOTE-404: The Logic of Animal Conflict

## Contribution

- The concept of an evolutionarily stable strategy, defined informally on
  p. 15 and formally on p. 17, and used to analyse animal contests.
- A computer simulation showing that "limited war" strategies beat "total
  war" under individual selection, against the received explanation by
  benefit to the species.
- An analytic war-of-attrition result: no pure ESS, a mixed exponential ESS.

## Key insight

Restraint is stable if it is backed by retaliation. An escalator facing
retaliators risks injury for a prize it could have won or lost again
later, while retreating uninjured costs little when there are future
mating chances; so in a population of retaliators escalation does not
pay. Where weapons are harmless and persistence decides, stability needs
unpredictability: any fixed persistence can be beaten by a little more.

## Assumptions

- **Symmetric contestants**: "identical fighting prowess", differing only in strategy (p. 16).
- **No memory across contests** with the same or other opponents (p. 16).
- **Moves**: conventional C, dangerous D, retreat R, alternating; a seriously injured contestant always retreats; P(serious injury | one D) = 0.10.
- **Payoffs**: +60 win; −100 serious injury; −2 per non-injuring D received; 0 to +20 for saving time. Losing uninjured scores 0, so future breeding chances exist.
- **Probabilities**: Prober-Retaliator probes with 0.05; retaliation against a probe is certain.
- **War of attrition**: prize v; a contestant chooses a maximum cost m; the one prepared to pay more wins and both pay the smaller m.

## Key results

- **Table 1** (row's mean payoff against column), among the values the prose relies on: Mouse v. Hawk 19.5, Hawk v. Mouse 80.0; Mouse and Bully each beat Hawk in a Hawk population, so Hawk is not an ESS; Hawk, Bully and Prober-Retaliator beat Mouse in a Mouse population; Bully is not an ESS.
- **Retaliator.** "Retaliator is an ESS since no other strategy does better, though Mouse does equally well." Mouse scores 29.0 against Retaliator, as Retaliator does against itself, and Retaliator scores 29.0 against Mouse, as Mouse does against itself.
- **Prober-Retaliator** "is almost an ESS"; it replaces Retaliator as the predominant type if Mouse exceeds 7% of the population.
- **Sensitivity.** Hawk becomes the ESS if P(injury per D) is 0.90, or if retreating uninjured costs as much as serious injury (+60/−100/−100); cautious strategies gain if retreat is costless relative to a large injury cost (+60/0/−500).
- **ESS definition (p. 17).** I is an ESS if for all J, E_I(I) > E_I(J); or if E_I(I) = E_I(J), then E_J(I) > E_J(J).
- **War of attrition (p. 17).** No pure strategy m is an ESS (m + ε beats m; if m > v, zero beats m). The mixed strategy p(x) = (1/v)exp(−x/v) is an ESS.
- **Real animals (pp. 16–17).** Category distinctions between conventional and dangerous tactics are easier to program than intensity limits; C-level fighting carries information about D-level prowess, so animals should probe inferiors and retreat from clear superiors; simulated "insane rage" pays until bluff-calling evolves, which favours unfakeable signals such as musth.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Individual selection can account for limited war | strong for the model; the qualitative result is robust to "moderate changes" | Table 1 plus stated sensitivity runs (not shown) |
| C2 | Hawk is not an ESS under the stated payoffs | strong | Table 1 column comparison |
| C3 | Retaliator is an ESS | weak as stated | it ties with Mouse, which fails the paper's own second ESS condition; it is at most neutrally stable |
| C4 | A stable strategy requires retaliation against escalation | moderate | follows from C1–C2; Mouse cannot hold the population against Hawk |
| C5 | In a war of attrition the ESS is the exponential mixture | strong | stated with "it can be shown"; derivation not given ("a more detailed analysis will be published elsewhere") |
| C6 | Animals use conventional fighting to assess opponents and retreat from superiors; unfakeable signals like musth pay | assertion | informal argument in "Real Animals" |

## Concepts

- **Evolutionarily stable strategy** — a strategy which, if most of a population adopt it, admits no mutant strategy of higher fitness (p. 15), made exact by the two conditions on p. 17.
- **Probe / escalate / retaliate** — playing D first or after C; replying to D with D.
- **Limited war / total war** — conventional, rarely injurious fighting versus escalation to injury.

## Connections

- **Hamilton** ([LIT-506](../literature.d/LIT-506.md), §6) explains restraint between relatives; this paper explains it among non-relatives and names kin selection only as a brake on very dangerous weapons. Hamilton is thanked, and Hamilton (1967) on sex ratio is cited as a source of the ESS idea.
- **Axelrod & Hamilton** ([LIT-498](../literature.d/LIT-498.md)) adopt the ESS for the iterated Prisoner's Dilemma and cite this paper and Maynard Smith & Parker (1976).
- **Morality-as-cooperation.** Curry 2016 ([LIT-503](../literature.d/LIT-503.md)) and [NOTE-034](NOTE-034.md) cite it for hawk–dove contests; see Corrections.

## Bearing on the record

- **Contest domains (hawk, dove).** Grounded only in part. The paper supplies (i) the ESS logic, (ii) restraint backed by retaliation, and (iii) in prose, assessment of prowess and retreat from superiors, with honest signals of formidability. It does not model display followed by deference, since contestants are identical, and it has no "dove".
- **Possession.** Not grounded: no owner–intruder asymmetry.
- **Division.** Not grounded: the war of attrition is about who gets the whole prize.
- **No THEORY is indicated.** No instruction for ML practice.

## Limitations

- Five hand-picked strategies; the space is not searched.
- Only the means of 2,000 simulated contests are given; no variance.
- Symmetric contestants, no memory, no asymmetries of size or ownership.
- The attrition result is asserted, with the derivation deferred.

## Open questions

- With assessment of an opponent's prowess and asymmetries such as ownership added, which strategies are stable? The paper says actual animals "may combine Prober-Retaliator and Mouse capabilities" but does not model it.
- Is Retaliator stable once the tie with Mouse is broken, for example by small costs of retaliating or by Mouse's loss to probers?

## Corrections

- none to a seeded skim (there was no seed)
- **No Hawk–Dove game.** [NOTE-034](NOTE-034.md) credits "hawk–dove contests (Maynard Smith & Price)" and glosses hawkish and dovish traits with this citation, and Curry 2016 ([LIT-503](../literature.d/LIT-503.md)) says conflicts are "modelled … as nonzero-sum hawk–dove games … (Maynard Smith & Price, 1973)". The paper's strategies are Mouse, Hawk, Bully, Retaliator and Prober-Retaliator, and "dove" does not occur. The two-strategy Hawk–Dove game is later work; the record holds no source for it.
- **Retaliator's stability.** The paper calls Retaliator an ESS while noting that Mouse does equally well. Under the paper's own second condition (p. 17) that tie makes it at most neutrally stable. Gale & Eaves (1975, DOI-10.1038/254463b0) commented on the paper in Nature; not read here.
