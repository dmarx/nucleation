---
status: Read
paper: LIT-tmpx4cpq
title: 'Schram and Ule — Regulatory independence may limit electoral holdup but entrench capture'
version: 1
history:
- version: 1
  date: '2026-10-21'
  note: >-
    Read in full from the publisher's open-access PDF (Springer, CC BY
    4.0), link.springer.com/content/pdf/10.1007/s11127-023-01136-y.pdf,
    which Unpaywall lists as the published version; text extracted with
    pdftotext. Read: §§1–5, Tables 1–7, Figure 1 from its caption and
    text, and the footnotes. Not read: the online supplementary appendices
    (A, the model and its perfect Bayesian equilibria; B, the instructions;
    C, the payoff tables; D, the treatment pooling; E, the formal
    hypotheses; F, the analyses excluding period-1 investors), so the
    equilibrium predictions of Table 2 are taken as stated. Table 2's cells
    were partly scrambled by extraction and are read with the text.
date: '2026-10-21'
summary: >-
  In a laboratory game of one infrastructure operator, two policymakers and
  three voters (59 groups), letting the first elected policymaker fix the
  price for all nine periods, the paper's "regulatory independence",
  moved prices toward the efficient level when policymakers' payoffs were
  aligned with consumers', and raised prices further above it when they
  were aligned with the operator, "capture entrenchment". Voters' pressure
  under flexible regulation lowered prices under capture but did not
  remove the effect.
---
<!-- inactive-ok-file: CLAIM-tmpjo2zr CLAIM-342 CLAIM-tmpyxupb TERM-tmpe6jtq THEORY-tmpvj1mm — Proposed; open entries this reading bears on and the account filed from it, nothing here rests on their being settled -->
# NOTE-tmpze6la: Schram and Ule — Regulatory independence may limit electoral holdup but entrench capture

## Contribution

It studies holdup and capture together. The usual argument for an
independent regulator is that it protects investors from electorally
driven price cuts. The paper shows, in a model and in the lab, that the
same commitment locks in whatever the designing policymaker wanted, so
independence helps when the designer serves consumers and harms them when
the designer serves the regulated firm. It names the second case
"entrenched institutional capture, the institutionalization of regulatory
capture in an independent regulator."

## Key insight

"Independence" here is independence from future elections, not from the
industry. Whoever sets up the independent regime still sets it. If that
person is captured, independence removes the one force that was pushing
prices down, electoral pressure, and keeps the captured price in place.
"The intuition underlying this effect is that flexible regulation allows
electoral pressure to reduce the price, but independence does not.
Instead, it offers the policymakers an opportunity to ensure lax regulation
in the long run."

## Assumptions

- **The game.** Per period: the operator (IO) decides whether to invest
  (irreversible, costly, relieves a capacity constraint as demand grows);
  the IO and the two policymakers (PMs) announce prices (cheap talk); three
  consumer-voters elect one PM by majority; the elected PM sets the price
  in {0, …, 5}; the IO charges it. Nine periods, each group played once.
- **Capture is exogenous and reduced-form.** "In the case of capture,
  [PMs'] interests coincide perfectly with those of the industry"; without
  capture they are aligned with consumers. Alignment is common knowledge.
  "A detailed modeling of the nature of regulatory capture is beyond the
  scope of this paper." No influence is exercised in the game. Capture is a
  treatment.
- **Regulatory independence is commitment.** In [RegInd] "only the PME
  elected in period 1 can choose the price which then holds for all
  periods." In [RegFlex] the elected PM sets the price each period.
- **Information.** Consumers know their own payoffs and that higher prices
  are better for the investor, not the IO's payoff table.
- **Design.** 2 × 2 between subjects (capture × independence), 351
  subjects at CREED, Amsterdam, 59 groups of six; 41 groups without
  capture, 18 with. Fisher–Pitman permutation tests, two-sided.
- **Outcomes.** P6, the mean price over periods 1–6; I5, investment by
  period 5; ΔEP, the mean absolute deviation from the efficient no-loss
  price (1 after investment).

## Key results

- **Equilibria (Table 2, two boundary cases of voting).** With no
  electoral pressure, capture gives high prices (4–5) and early enough
  investment; without capture, flexible regulation gives price 0 and no
  investment, the holdup. Independence without capture fixes price 1 and
  investment in period 4. With strong electoral pressure, capture does not
  matter in theory.
- **Period-1 investment.** 45.8% of IOs invested in period 1, a dominated
  choice, independent of treatment (p = 0.869, p > 0.999). Kept in the main
  analysis; Appendix F excludes them.
- **Capture (§4.2).** P6 significantly higher with capture (p < 0.001).
  All IOs invest by period 5 under capture; without capture 50% do, and 32%
  of groups never invest (p = 0.025). ΔEP 1.93 with capture, 0.77 without
  (p < 0.001).
- **Table 4.** Without capture: flexible P6 = 0.16, I5 = 63%,
  ΔEP = 0.98; independent P6 = 0.47, I5 = 84%, ΔEP = 0.53. With capture:
  flexible P6 = 1.78, I5 = 100%, ΔEP = 1.56; independent P6 = 3.19,
  I5 = 100%, ΔEP = 2.31.
- **Independence without capture (§4.4).** Prices rise toward 1
  (p = 0.015), closer to efficient (p < 0.001). The investment effect is
  not significant (p = 0.255).
- **Independence with capture (§4.5).** Prices rise further from 1
  (p = 0.001; p < 0.10 in the restricted sample). ΔEP higher, marginally
  by permutation test (p = 0.066), significantly by the Tobit regression of
  Table 5 (F = 8.80, significant at 1%; p = 0.07 in the restricted sample).
- **Electoral pressure.** Observed capture prices lie between the two
  equilibria: "Electoral pressure is stronger than assumed in the
  no-pressure equilibrium but weaker than in the pressure equilibrium."
- **Voting (Tables 6–7).** Voters punish higher past prices (−23
  percentage points for a higher last price) and weigh promises (−34 points
  per unit in period 1, −12 later). Promises count for more when PMs are not
  captured.
- **Tacit collusion.** Under capture with flexible regulation, only 36% of
  newly elected PMs lowered the predecessor's price and 24% raised it.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | In this game, policymakers aligned with the operator set higher prices and the operator invests earlier | strong | §4.2, p < 0.001 and p = 0.025, 59 groups |
| C2 | Without such alignment, fixing the price at period 1 moves prices toward the efficient level and reduces deviation from it | strong for prices, not significant for investment | §4.4, p = 0.015, p < 0.001; investment p = 0.255 |
| C3 | With such alignment, fixing the price raises prices further above the efficient level ("capture entrenchment") | moderate | §4.5, p = 0.001 for P6 on 18 groups; ΔEP marginal by permutation, significant by regression |
| C4 | Voters' electoral pressure is too weak to remove the effect of aligned policymakers, partly through tacit collusion between them | moderate | prices between the two equilibria; 36% / 24% of new PMs; three voters per group |
| C5 | Regulatory independence benefits consumers only when policymakers designing it serve consumers or electoral pressure is strong | moderate as a reading of C2–C3; a generalization beyond the lab | §5 |
| C6 | The electoral pressure in the lab is probably an upper bound for real elections | weak | asserted: three voters, one issue |

## Concepts

- **Holdup**: delayed investment because electorally driven future price
  cuts may expropriate its return.
- **Regulatory capture**: here, policymakers whose payoffs equal the
  operator's, "a reduced form approach ... sufficiently general to allow
  for various underlying models".
- **Regulatory independence**: a price fixed by the first elected
  policymaker that later ones cannot change.
- **Capture entrenchment**: an inefficient price set by captured
  policymakers that "cannot be corrected at later points in time".

## Connections

It cites Stigler (1971) and Peltzman (2022) for capture, Posner (1974) for
dispersed voters and colluding politicians, and Martimort (1999) for
agencies that drift toward industry as public attention declines, which its
conclusion says it "complements". Its experimental antecedents include Cox,
Offerman, Olson and Schram (2002) on railways and Engel and Heine (2017) on
price caps.

## Bearing on the record

- **[THEORY-tmpqzjvn](../theory.d/THEORY-tmpqzjvn.md)** (Active) states C1–C4 as measured.
  **[THEORY-tmpvj1mm](../theory.d/THEORY-tmpvj1mm.md)** (Proposed) carries the authors' general conclusion,
  C5.
- **[CLAIM-tmpjo2zr](../claims.d/CLAIM-tmpjo2zr.md).** A25 cited the paper for "independence from one source
  of authority does not imply independence from every other source." The
  paper supports a sharper form. Its independence is from voters, and
  capture enters through the designer. Making the regime independent of
  elections removed the only corrective channel left, the voters' pressure,
  and so held the captured price in place. That is the claim's last clause,
  that formal independence of a procedure does not make it independent, by
  a route the claim does not name: independence installed by a captured
  designer insulates the capture from correction. In [CLAIM-342](../claims.d/CLAIM-342.md)'s terms the
  voters were the evidence-bearing check outside the loop, and
  independence cut it. The paper's capture is not informational or
  evaluative. It is an alignment of the decision maker's own payoffs, so it
  does not bear on the claim's two routes, which the LIT's "complicates"
  overstated.
- **[TERM-tmpe6jtq](../terms.d/TERM-tmpe6jtq.md).** The paper's capture is the conventional
  interest-alignment sense, not the TERM's fidelity-relative one, and it
  has no loop. It is a clean instance of what the TERM sets aside as the
  institutional sense, without the OECD's intent condition: alignment is
  simply given.
- **[CLAIM-tmpyxupb](../claims.d/CLAIM-tmpyxupb.md).** The two treatments are two governance profiles with
  the same price-setting authority at period 1 and different holders of
  revision after it: the electorate in [RegFlex], nobody in [RegInd]. That
  difference, not the number of rules, decides the outcome. It is an
  experimental instance of the claim's point that authority over revision
  is a separate component.
- **[CASE-tmp3uarw](../cases.d/CASE-tmp3uarw.md)** is stipulated. This paper is a laboratory measurement,
  not a documented episode of real regulation, so it does not supply the
  documented variant the case waits for.

No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- **Capture is assigned, not produced.** The study measures what
  independence does given captured policymakers. It says nothing about how
  capture arises, or whether independence makes it more likely, which the
  paper's introduction cites as a further risk (Mitchener, 2007; "Rajam &
  Ramcharan, 2016", as the paper spells it).
- **Independence is commitment by the first policymaker.** Real independent
  regulators have mandates, appointments and budgets that this does not
  model.
- **Small groups.** Three voters, two candidates, one issue. The capture
  cells have 18 groups. Some effects weaken in the restricted sample.
- **45.8% dominated period-1 investment.** Treated as error and kept. The
  authors report that conclusions are mostly unaffected.
- **An internal inconsistency.** §4.2 says that without capture "only 50%
  of the IOs invest by period 5", but Table 4 gives I5 = 63% and 84% for
  the two no-capture cells, so the pooled figure should lie between them.
  The text does not explain the difference.
- **Appendices not read.** The equilibrium derivations and the treatment
  pooling (Appendix D) were taken as stated.

## Open questions

- Would independence also entrench capture that operates through the
  evidence a regulator receives rather than through its payoffs? The paper
  does not model that route.
- Does an intermediate design, such as fixed terms with periodic review,
  keep the holdup benefit without the entrenchment? The paper studies only
  the two boundary cases.
