---
status: Read
paper: 'LIT-tmptmm0j'
title: 'Banerjee, Hanna, Kreindler and Olken — Cash transfers and the labour supply of the poor in seven randomized evaluations'
version: 1
history:
- version: 1
  date: '2026-11-05'
  note: >-
    Read in full on 2026-11-05 from the published journal version (PDF
    wbro_32_2_155.pdf) in the World Bank Open Knowledge Repository, handle
    10986/31221, item "Published by Oxford University Press on behalf of
    the World Bank": 30 pages, pp. 155–184, carrying OUP's stamp that it
    was downloaded by the Joint Bank-Fund library on 20 September 2017.
    OUP's own article page returned a Cloudflare check and was not
    retried. Text extracted by pdftotext, which rendered every minus sign
    as a control byte, so a first pass printed negative table entries as
    positive; the text was regenerated with the minus signs restored, and
    negative numbers were checked against the prose (the text calls
    Honduras's −0.0295 a "3 percentage point decrease" and the pooled
    −0.004 "a decrease of 0.4 percentage points"). Read: the abstract,
    introduction, theory and prior literature with Table 1, data and
    method, results with Tables 2–6 and Figures 1–4, the tax-rate section,
    the comparison with asset programmes, the conclusion, notes and
    references. Not read: the online appendices (the excluded-studies
    list, balance tables, the split by type of work and gender, and the
    hierarchical model's details), so attrition is unverified; the
    article's text does not report it. The pooled intervals of Table 6
    are the posterior 5th and 95th percentiles, 90% credible intervals,
    and the text's "with 95 percent probability" is one-sided. Page
    numbers below are the journal's.
date: '2026-11-05'
summary: >-
  A harmonized re-analysis of seven randomized evaluations of government
  cash transfer programmes in six countries finds no programme that
  changes adults' weekly hours and one, the least generous, that changes
  participation at the 10% level. Pooled with a Bayesian hierarchical
  model and scaled to a transfer worth 13.6% of consumption, participation
  moves −0.4 points (90% interval −2.3 to +1.4) and hours about five
  minutes a week (−1.7 to +1.4 hours); men's moderate reductions are
  excluded and women's interval is wide. The authors trace the null partly
  to low implicit tax rates. Support continued throughout; nothing is
  measured after withdrawal.
---
<!-- inactive-ok-file: THEORY-tmp7qas0 CLAIM-tmpc3x0c CLAIM-tmpqa0qu CLAIM-tmpoh07b CLAIM-tmpw4ai2 CLAIM-597 THEORY-tmph35ra THEORY-tmpkkhou THEORY-tmp0qrm2 THEORY-tmp02gkd THEORY-470 LIT-1493 — Proposed, Unavailable or new; cited from the reading of Banerjee, Hanna, Kreindler and Olken (2017) as open -->

# NOTE-tmpy2r15: Banerjee, Hanna, Kreindler and Olken — Cash transfers and the labour supply of the poor in seven randomized evaluations

## Contribution

Earlier studies of cash transfers and adult work were programme by
programme, on differing definitions; most found nothing (Table 1, p. 162).
This paper re-analyses the household micro-data of seven randomized
evaluations on one definition of work, pools them while letting effects
differ across programmes, and so turns a scatter of insignificant results
into a bounded null: a quantified zero, not an absence of
significance. It also measures the implicit benefit-withdrawal rate in two
programmes, which ties the null to how the programmes are targeted.

## Key insight

Whether a transfer lowers work depends less on the help being assured than
on whether working more takes it away. The programmes studied paid for two
to nine years whatever the household earned, or nearly so, and work did
not fall: "the targeting rules of these programs, coupled with the size of
the transfers, provides one reason why we do not observe systematic
negative effects" (p. 175).

## Assumptions

- **Selection (pp. 157, 163).** Inclusion required a government-run
  programme in a low-income country with a pure control group, micro-data
  for both adult men and women, and "at least 40 clusters" (p. 157). Of 18
  trials identified, 11 were excluded (missing labour data by sex, not
  government-run, baseline imbalance, or no obtainable data).
- **Unit and window.** Adults aged 16–65 in eligible households, excluding
  domestic workers, surveyed one to two years after rollout, with
  transfers still being paid. Endline comparison for two programmes,
  difference-in-differences for five (Table 3).
- **Work coded alike.** Self-reported work in the last week (Morocco's
  30-day recall rescaled); non-workers count as zero hours, so hours carry
  both margins (p. 165). Indonesia's PKH has no hours data.
- **Pooling.** Each programme's effect is scaled linearly by its transfer
  size to a transfer worth 13.6% of consumption, the average, and
  programme effects are drawn from a normal parent distribution (pp. 167–168,
  172).
- **Transfer size and duration (p. 164).** Transfers run from 4% (PRAF II)
  to about 20% (Progresa) of household consumption, "intended to
  supplement other sources of income"; once a household is eligible the
  benefit "lasts at least a period between two and nine years".
- **The tax calculation is an upper bound** (p. 175 and n. 24): working more
  is valued at the loss of the full present value of benefits, assuming
  households know when they will be reassessed.

## Key results

- **Headline** (abstract, p. 155): the authors "find no systematic
  evidence that cash transfer programs discourage work".
- **Programme by programme** (Table 3, p. 170; p. 169). Participation:
  Honduras −0.0295* (s.e. 0.0164), Morocco −0.0097, Philippines +0.0096,
  PAL +0.0135, PKH −0.0043, Nicaragua −0.0202, Progresa −0.0089. Hours a
  week: −0.51, −0.48, +0.37, +1.15, none for PKH, −1.17, −0.34, none
  significant. Of Honduras: "this is roughly what we may expect by pure
  chance" (p. 169).
- **Type of work** (Table 4, p. 171): "No clear systematic patterns
  emerge." Progresa shifts work out of the household, Nicaragua's RPS
  into it.
- **By sex** (Table 5, p. 172): participation changes for men only in the
  Philippines (+0.0301*), for women only in Honduras (−0.0535*); hours
  change significantly in no programme for either.
- **Pooled** (Table 6, p. 173; 90% credible intervals):

  | Outcome | Group | Base | Effect | Elasticity |
  |---|---|---|---|---|
  | Worked last week | All | 0.56 | −0.004 (−0.023, +0.014) | −0.06 (−0.30, +0.18) |
  | Worked last week | Men | 0.84 | +0.001 (−0.020, +0.026) | +0.01 (−0.17, +0.23) |
  | Worked last week | Women | 0.29 | −0.008 (−0.039, +0.024) | −0.21 (−0.99, +0.60) |
  | Hours per week | All | 21.1 | −0.077 (−1.734, +1.356) | −0.03 (−0.60, +0.47) |
  | Hours per week | Men | 34.2 | +0.470 (−1.702, +2.965) | +0.10 (−0.37, +0.64) |
  | Hours per week | Women | 8.7 | −0.430 (−2.588, +1.611) | −0.36 (−2.18, +1.36) |

  "the point estimate corresponds to a decrease of five minutes of work per
  week", and a new programme will not cut hours "by more than 1 hour and 42
  minutes per week" (one-sided); the effects "are broadly symmetric around
  zero" (p. 173). For men "we can reject moderate negative effects with a
  high probability"; for women there is "significant uncertainty in the
  impact of a new cash transfer program for women" (p. 174).
- **The implicit tax** (pp. 174–175). Morocco and PAL are targeted purely
  by geography, Honduras by geography and household make-up, Nicaragua
  with a light asset test; for about half the programmes "eligibility is
  not directly related to current employment or income, effectively
  implying no tax". In PKH, Rp. 1,000 more annual consumption per head
  costs Rp. 40 of expected transfers over six years; for Progresa "the
  implied tax rate is 15 percent", and if households do not know when they
  will be assessed the rates are "6 and 3-9 times smaller" (n. 24).
- **Asset programmes** (pp. 176–178, cited, not re-analysed). BRAC's
  graduation programme: total labour supply up 218 hours a year, 19%,
  after four years; the six-country graduation trial: up 10% of the
  control mean two years on; women in northern Uganda given $150, training
  and supervision: hours "go up by a stunning 10 hours" a week; Uganda's
  YOP grants: 17% more hours after four years. But "the evidence is not
  yet available as to whether supervision is needed" or the asset alone
  would do (p. 178).
- **Temptation goods** (p. 178), from Evans and Popova (2014), cited: no
  evidence "that the transfers induce increases in spending on temptation
  goods"; transfers "do not induce the “bad” behaviors that are often
  attributed to them".
- **Prior literature** (Table 1, p. 162): of 21 studies of 17 programmes,
  14 report overall work, and "Overall, these studies suggest little to no
  effects on overall labor supply".
- **Beliefs** (Figure 1, p. 156): across countries, spending on cash
  transfers as a share of GDP falls with the share answering "Poor because
  of laziness" in the World Values Survey. A correlation only.

## Concepts

- **Income effect** and **implicit tax** (benefit-withdrawal rate): the two
  routes by which a transfer can lower work (p. 158).
- **Routes to more work** (p. 158): escape from a Dasgupta–Ray poverty
  trap, eased credit constraints, financed migration, local spillovers.
  Named, none tested.
- **Extensive and intensive margins**; work inside and outside the
  household.
- **Bayesian hierarchical pooling**: a site effect for a hypothetical new
  programme, drawn from the distribution of programme effects.
- **Proxy-means and geographic targeting.**
- **Graduation model**: an asset, training and a stipend of no more than
  six months for the poorest households (p. 176).

## Connections

The household counterpart, and counterweight, to the aid batch's
state-level dependency accounts: THEORY-tmph35ra (Ostrom et al., the
Samaritan's dilemma in aid), THEORY-tmpkkhou (Azam et al., tax capacity
lost under gap-filling aid), THEORY-tmp0qrm2 (Moss et al.) and
THEORY-tmp02gkd (Moore, revenue source and capacity). Figure 1, beliefs
about the lazy poor going with smaller programmes, is a policy-feedback
observation of the kind LIT-1493 (Pierson) is about. THEORY-470's
structural-not-character account of platform decay is a distant parallel
to the paper's explanation by programme design rather than by recipients'
character.

## Bearing on the record

- **CLAIM-tmpc3x0c** (safe withdrawal of transient support). Contradicts
  its "slack effort" route as a general mechanism: help assured for two to
  nine years, and for about half the programmes not withdrawn as earnings
  rose, did not lower effort, pooled or for men. Supports, second-hand, its
  condition that the party do the work: support that needs the party's
  labour, a productive asset, raised work by 10–19%. Silent on what happens
  after withdrawal.
- **CLAIM-tmpqa0qu** (the Black Queen and the Samaritan's logic).
  Contradicts the step from the dilemma's logic to an observed fall in
  effort among households: one-way transfers set from outside did not
  produce it within the observed horizon. It does not test loss of skill
  over decades.
- **CLAIM-tmpoh07b** (supply that does the work crowds out capacity).
  Consistent, and qualifies its reach: transfers of 4–20% of consumption
  supplement the household's work rather than doing it, so by the claim's
  own distinction no crowd-out is expected, and none is seen. The claim
  should not be cited for welfare transfers. The paper's design point, that
  effort falls when benefits are withdrawn as one's own effort rises, not
  because support is assured, sharpens the claim's ordering condition.
- **CLAIM-tmpw4ai2** (thresholds). Little: the poverty trap is named as a
  route to more work, but no threshold is estimated; that lump-sum assets
  outperform small flows is suggestive and second-hand.
- **CLAIM-597** (supplied upkeep and decay on withdrawal). None directly;
  there are no data after withdrawal.
- **THEORY-tmph35ra**. Qualifies it, and contradicts it if read as being
  about households: the theory's "best response is to expend a low level of
  effort" should be held as a construction about the upkeep of donor-built
  assets, not as a fact about recipients in general.
- **QUESTION-398**. None directly: effort is measured under continuing
  support. The graduation results, gains four years on after a stipend of
  at most six months, are the nearest analogue to a nucleus that keeps
  growing once support ends, and they are second-hand.
- **The level distinction.** The findings are about households receiving
  small, income-supplementing, weakly means-tested cash; the record's aid
  evidence is about states, where aid substitutes for tax effort or
  upkeep. The finding does not refute state-level substitution, but it does
  refute carrying the dependency story from states down to households.

Filed from it: THEORY-tmp7qas0.

## Limitations

- **Short horizon, support never withdrawn.** It tests effort while support
  continues, one to two years in, not dependence after it ends.
- **Small transfers.** 4–20% of consumption; transfers large enough to
  live on are not covered (p. 164).
- **Narrow geography.** No African or South Asian trial qualified (n. 4);
  seven of 18 trials were kept.
- **Women's effects are imprecise**: the participation elasticity's
  interval runs from −0.99 to +0.60.
- **90% intervals.** The "95 percent" statements in the text are one-sided.
- **Self-reported work; mostly conditional programmes** whose conditions
  are enforced unevenly.
- **Attrition is not reported in the article**; it may be in the online
  appendices, not read.
- **Second-hand evidence** on temptation goods and asset programmes.
- **No reverse mechanism tested**: scarcity and stress are absent; the
  routes to more work are theoretical.

## Open questions

Whether work holds up after a transfer stops, and whether a transfer large
enough to replace earnings, or one withdrawn steeply as earnings rise,
lowers it: the paper's own account predicts that the second would.
