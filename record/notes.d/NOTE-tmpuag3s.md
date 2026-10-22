---
status: Read
paper: 'LIT-1388'
title: 'Acharya, Blackwell & Sen — The political legacy of American slavery'
version: 1
history:
- version: 1
  date: '2026-10-22'
  note: >-
    Read in full on 2026-10-22 from the journal's typeset PDF of The
    Journal of Politics 78(3): 621–641 (published online 19 May 2016),
    posted by the second author on his own site
    (mattblackwell.org/files/papers/slavery.pdf), text extracted with
    pdftotext. Unpaywall and OpenAlex report the article closed; Unpaywall
    lists the SSRN working paper (2014) as an open accepted version, not
    used. Read: the abstract, every section, Tables 1–6 with their notes,
    the captions of Figures 1–6 and the 30 footnotes. The images of the
    figures were not viewed; what they show is taken from the text and
    captions. The reference list was skimmed. The online appendix (tables
    A.1–A.18, sections A, B.2 and D), where many robustness checks sit, was
    not read, and claims that rest on it are marked. In the extracted text
    the minus sign of every negative coefficient renders as "2", so
    coefficients below are quoted from the prose, not the tables.
date: '2026-10-22'
summary: >-
  Among Southern whites today, those in counties where a larger share of the
  1860 population was enslaved are more Republican, more opposed to
  affirmative action, more racially resentful and colder toward blacks; the
  association survives 1860 controls and a cotton-suitability instrument,
  and is not accounted for by today's black share, by 1935–40 migration or
  by income inequality. The divergence in voting appears after
  Reconstruction, not before the war, and is smaller where agriculture
  mechanized early, which the authors read as a post-emancipation
  amplification of attitudes then passed down locally.
---
<!-- inactive-ok-file: CLAIM-420 CLAIM-329 CLAIM-417 CLAIM-423 CLAIM-327 THEORY-tmpp1wwg — Proposed; the claims this reading bears on, named in prose, not leaned on -->
<!-- inactive-ok-file: LIT-1380 LIT-1381 — Unavailable or Deferred; works of the same exchange, named -->

# NOTE-tmpuag3s: Acharya, Blackwell & Sen — The political legacy of American slavery

## Contribution

It shows a county-level association between the local prevalence of
slavery in 1860 and the political and racial attitudes of white Southerners
150 years later, argues that the association is causal, and tests the
contemporary explanations offered for Black Belt conservatism (chiefly
racial threat) against it. It proposes and gives partial evidence for a
historical-persistence mechanism: emancipation gave Black Belt whites
incentives to intensify racial repression, which widened local differences
in attitudes that were then transmitted across generations.

## Key insight

The legacy is not slavery's attitudes carried forward unchanged. Before the
war, high- and low-slave counties voted alike; "the data show that regional
differences emerged after the end of Reconstruction" (p. 634). On the
authors' account the shock of emancipation, with the political and labor
threat it posed to planters, produced the divergence, and family and local
institutions then reproduced it. What persists is an attitude, not a party:
"it is sociopolitical attitudes, rather than partisanship, that are passed
down from parent to children" (fn. 23), so the same counties were more
Democratic until mid-century and are more Republican now.

## Assumptions

- **Treatment and units.** The share of each county's 1860 population that
  was enslaved, mapped onto 2000 county boundaries by area weighting
  (fn. 4), across the former Confederate states plus Kentucky and Missouri.
  Outcomes are pooled CCES surveys (2006–2011, over 40,000 white
  respondents in 1,329 counties) and ANES thermometer scores (1984–1998,
  3,123 respondents in 64 counties).
- **Selection on 1860 observables** for the baseline WLS: population, farm
  size, land inequality, farm value, improved acreage, free black share,
  rail and water access, area, ruggedness, latitude and longitude, with
  state fixed effects.
- **The instrument's exclusion restriction.** Cotton suitability (FAO,
  1961–1990 climate) affects attitudes only through slavery, "a strong
  assumption" (p. 628), probed by a falsification test outside the South
  (appendix B.2, not read).
- **Sequential g-estimation's assumptions** for the controlled direct
  effect: no omitted confounders of slavery–outcome or black share–outcome,
  and no interaction between slavery and black share (fn. 14).
- **County as the level of persistence.** Individuals are attributed the
  1860 slavery of the county where they live now, not where their families
  lived.

## Key results

- **Baseline (Table 1).** "a 20 percentage point increase in the slave
  proportion (roughly a one standard deviation change) is associated with a
  2.3 percentage point decrease in the share of whites who currently
  identify as Democrats", a 3 point fall in support for affirmative action,
  a 0.08 rise in racial resentment and a 7 point rise in the white–black
  thermometer gap. "These represent approximately a 0.09–0.13 standard
  deviation change in the CCES outcomes and roughly a 0.32 standard
  deviation change in the thermometer score difference" (p. 626). Small
  effects, consistently signed.
- **Instrument (Table 2).** Second-stage estimates are larger than the
  baseline; the first-stage F is about 80.
- **Racial threat.** "the correlation between percent slave in 1860 and
  percent black in 2000 is 0.77" (p. 628). With black share in 2000 held
  fixed by sequential g-estimation (Table 3), the direct effect of slavery
  is about the baseline's, and once slavery is accounted for, black
  concentrations "appear to have the opposite effect that racial threat
  theory would predict" (p. 630).
- **Sorting.** In the 1940 census's 1935–39 migration data, migrants differ
  from stayers alike in high- and low-slave counties (Figure 3). The
  authors call this "suggestive evidence that the differences we are seeing
  are not due to geographic sorting alone" for one five-year window
  (p. 631); 2000 mobility is in appendix D (not read).
- **Inequality.** Black–white income inequality in 2014 predicts attitudes
  weakly and, if anything, in the wrong direction (Table 4).
- **Timing (Figures 4 and 5).** Little difference in Democratic presidential
  vote between high- and low-slave counties before the war; in Georgia's and
  Mississippi's 1851 governor's races, which turned on slavery and secession,
  "there is little evidence of a strong relationship between slavery and
  vote choice" (p. 635). The effect grows as disenfranchisement proceeds,
  peaks when poll taxes and literacy tests are in place, weakens around 1950,
  and by 2008 runs the other way (more Republican). Black voters are in the
  historical vote data, which the authors handle by stopping at 1968
  (fn. 24).
- **Violence.** A 10 point rise in 1860 slave share goes with 1.89 more
  black lynchings per 100,000 (1882–1930), conditional on controls (Table 5).
- **Mechanization.** Where tractors spread fastest in 1930–40, slavery's
  effect on present partisanship nearly vanishes (from 1.8 to 0.2 points per
  10 points of slave share, Table 5). Appendix tables A.16 and A.18 (not
  read) are offered against racial-threat and self-selection readings.
- **Transmission.** In the Youth–Parent Socialization Panel, Southern
  parents' 1965 white–black thermometer gap correlates with their children's
  in 1965, 1973, 1982 and 1997 (Figure 6; n = 241 Southern students), and
  "the effect of slavery on these younger whites is just as strong and
  statistically significant as it is for older whites" among those born after
  1965 (Table 6, p. 638).
- **The authors' summary of mechanism.** The evidence "provides some
  support that political culture, rather than exclusively institutions,
  plays an important role in explaining the persistent effects of American
  slavery" (p. 638), and "we do not rule out that Southern institutions may
  have also played an important role" (p. 639).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Southern whites in counties with more slavery in 1860 are today less Democratic, less supportive of affirmative action, more racially resentful and colder toward blacks | strong as an association; moderate as a causal effect | Tables 1–2; CCES and ANES; IV with a strong exclusion restriction |
| C2 | Contemporary black population share does not account for it; racial threat is not the explanation | moderate | Table 3, sequential g-estimation under no-unmeasured-confounding assumptions |
| C3 | Sorting and income inequality do not account for it | weak to moderate | Figure 3 (one five-year window), Table 4; appendix D not read |
| C4 | The county differences emerged after emancipation and Reconstruction, not before the war | moderate | Figures 4–5; presidential and 1851 gubernatorial vote, including black voters after 1867 |
| C5 | The divergence was driven by post-emancipation incentives to control black labor and votes, and decays where those incentives fell earlier | weak to moderate | lynching (Table 5), 1925 farm tenancy (appendix), mechanization interaction (Table 5) |
| C6 | The attitudes are transmitted across generations, through families as well as institutions | weak | parent–child correlation in a national panel's Southern subsample (n = 241, not tied to county slavery); equal effects among those born after 1965 |
| C7 | What is transmitted is sociopolitical attitude, not party; so the legacy is compatible with the 1960s realignment | interpretive | fn. 23; the reversal of sign in Figure 4 |

## Concepts

- **Historical persistence of political attitudes**: the authors' name for
  local attitude differences that originate in a historical shock and are
  reproduced across generations, as against explanations from present
  conditions.
- **Racial threat**: the theory, after Key and Blalock, that whites become
  more conservative where black populations are large now.
- **Controlled direct effect**: the effect of 1860 slavery if present black
  share were fixed at one level for all counties; estimated by sequential
  g-estimation (Vansteelandt 2009).
- **Black Belt**: the crescent of plantation counties that held most of the
  enslaved population.

## Connections

It places itself in the persistence literature in economics (Dell 2010;
Nunn and Wantchekon 2011; Acemoglu et al. 2012; Voigtländer and Voth 2012)
and cites Pierson 2000 ([LIT-1372](../literature.d/LIT-1372.md)) for "the path dependence of historical
institutions over time" (p. 623). Its foil is the racial-threat literature
from Key (1949). Its transmission claim rests on the socialization
literature (Jennings and Niemi 1968; Bisin and Verdier 2000; Boyd and
Richerson 1988). It acknowledges Eric Schickler among those who commented,
but does not cite *Racial Realignment* ([LIT-1380](../literature.d/LIT-1380.md)), which postdates it. The
authors expanded it into a book, *Deep Roots* (2018), not in the record.

## Bearing on the record

- **[CLAIM-420](../claims.d/CLAIM-420.md) (story, perspective and descent kept apart).** The claim
  calls this paper "the hard case, where association has to be told from
  transmission". The reading supports that framing, and sharpens it in a
  way the claim does not anticipate.
  - **Association to transmission.** The paper does more than show
    association: an instrument, a direct-effect estimate and tests of
    rivals. But its evidence for transmission itself is thin (C6): a
    parent–child correlation in 241 Southern respondents that is not
    linked to county slavery, and equal effects in a younger cohort. So the
    record should hold the association as strong and the transmission as
    argued and weakly evidenced.
  - **Not inheritance from the source.** The attitudes that persist did not
    descend unchanged from slavery. On the paper's own timing they diverged
    after emancipation, as a reaction to its loss. That is descent from
    slavery in [CLAIM-420](../claims.d/CLAIM-420.md)'s third sense, by way of its abolition, followed by
    perspectival transmission of what the reaction produced. It is a case of
    the claim's distinction at a collective scale: causal descent from an
    institution, with the transmitted perspective formed later. The
    claim's line "slavery's political legacy ... is the hard case" is fair;
    a dated note there could add the post-Reconstruction timing.
- **[CASE-133](../cases.d/CASE-133.md) (party realignment).** The case says "That attitudes in the
  South today are transmitted from slavery rather than associated with it.
  Acharya et al. argue for transmission; the record has not read them."
  Accurate. The reading adds the case's strongest evidence that carrier
  and character come apart: "it is sociopolitical attitudes, rather than
  partisanship, that are passed down" (fn. 23), and the same counties that
  were more Democratic when "the Democratic Party was the racially
  conservative party" (p. 634) are more Republican now (Figure 4). The
  attitude stayed with the place and changed party. That is the case's
  "An orientation can acquire a new carrier", shown in vote data, though
  the paper does not use that language. It also gives a date the case
  lacks: the slavery effect on the Democratic vote "weakens" around 1950,
  partly from "the move of national Democratic candidates toward a civil
  rights platform" (p. 634). That fits the case's timeline, which puts the
  national parties' move late.
- **[CLAIM-329](../claims.d/CLAIM-329.md) (persistence by causal transmission, not resemblance).** The
  paper is a test of that kind of claim for an attitude: it rules out
  rivals that would make the persistence resemblance (similar present
  conditions producing similar attitudes) rather than transmission. Racial
  threat is the rival it tests most carefully.
- **[CLAIM-327](../claims.d/CLAIM-327.md) (a slow collective variable read and regenerated).** The
  paper's mechanism includes norms enforced locally and elite opinion
  diffusing to the public (p. 633), which is that loop, but it tests none of
  it directly.
- **[CLAIM-423](../claims.d/CLAIM-423.md) (timescales and authority).** Only indirectly: a local
  attitude persisted across generations while parties and national
  coalitions changed over it, which is a slow component outlasting faster
  ones. It says nothing about authority.
- **THEORY warranted?** One, Proposed: [THEORY-tmpp1wwg](../theory.d/THEORY-tmpp1wwg.md), C1 with C4 and C5.
  The record holds no account of the persistence of attitudes from a
  historical institution.
- No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- The effects are small (about a tenth of a standard deviation on the CCES
  measures). The paper is about a systematic difference, not about most
  Black Belt whites.
- Residence today stands in for descent: the design cannot tell whether a
  respondent's family lived in the county.
- The instrument's exclusion restriction is untestable; the falsification
  test outside the South is in the appendix, not read here.
- The sorting test covers one five-year window, 1935–40.
- Historical vote shares include black voters before disenfranchisement,
  so the timing in Figure 4 mixes changes in who voted with changes in how
  whites voted.
- The transmission evidence is not county-linked, and family and
  institutional channels are not separated. The authors say so.
- Spatial correlation among neighbouring counties is not discussed in the
  main text.

## Open questions

- Does the effect hold for individuals whose families were in the county in
  1860, as against present residents? Linked genealogical or census data
  would answer it.
- How much of the transmission runs through families and how much through
  local institutions (churches, schools, local party organizations)? A
  design that varies one while holding the other, such as movers raised
  elsewhere, would separate them.
- If what persists is attitude and not party, what carried it through the
  realignment years county by county, and how quickly did party
  identification follow?
