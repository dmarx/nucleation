---
number: 71
status: Read
formerly:
- NOTE-tmpr57rx
paper: LIT-094
title: 'Shabrina, Arcaute & Batty 2021, Airbnb and London housing'
version: 2
history:
- version: 2
  date: '2026-09-25'
  note: >-
    Read in full (full text of the published article (Urban Studies, "1–25"
    online-first pagination; the UCL Discovery deposit of the SAGE PDF,
    rawC4/c42.pdf → c42.txt). I read the abstract (English; the Chinese
    abstract only as present), introduction, "The complexity of the London
    housing market", "The growth of the private rented sector", "Airbnb: An
    additional contributor", data list, "Possible misuse", the entropy and
    correlation section, the rental-change regression (Eq. 4, Tables 1–2,
    residual diagnostics), discussion and conclusion, note 1 and the
    references. Figures 1–7 came through as captions only. Their map values
    are known only where the text states them, and the Fig. 4 correlation
    matrix only for the coefficients quoted in the text and the Fig. 5
    captions. I did not read arXiv:1903.11205.). Upgraded from `Skimmed` to
    `Read`: the claims table, assumptions and results are new, and the skim
    is corrected where the full text disagreed.
date: '2026-09-25'
summary: >-
  Using Inside Airbnb data, "possible misuse" is defined as entire-home
  listings available for more than 180 days a year whose host has 2 or
  more listings. On that definition, about 0.16% of London's housing stock
  (≈5,300 homes) was possibly misused in 2018, rising to 3.5–7% in a few
  central LSOAs. Across LSOAs, misuse correlates weakly with purpose-built
  flats (r = +0.28), private renting (+0.33) and low dwelling-type entropy
  (−0.14). In a 33-borough OLS with 4 predictors, logged 2015 misuse has β
  = 0.084 (p = 0.001) on a min–max-normalised 2015–17 rent change. The
  paper translates this as "a 100% increase … up to 8%" in rent, which is
  £90 a year.
---

# NOTE-071: Shabrina, Arcaute & Batty 2021, Airbnb and London housing

## Contribution

The paper gives a London-wide, LSOA-level estimate of Airbnb supply that is possibly non-compliant with the 90-night short-let rule (Deregulation Act 2015, s. 44). It relates that supply to dwelling-type diversity, measured as Shannon entropy over 7 Census dwelling types, and to tenure. It reports a borough-level association between 2015 misuse and 2015–17 asking-rent change. The authors call it "the first to model the association between rental price, and specifically Airbnb misuse, as opposed to overall Airbnb activities" (Discussion).

## Key insight

Airbnb's share of the London housing stock is small citywide (about 2% listed and about 0.16% possibly misused), but it is spatially concentrated. It reaches up to 23% listed and 3.5–7% possibly misused in some LSOAs in Camden, Westminster, the City and Hackney. The concentration falls in low-diversity, flat-dominated, privately rented areas, which is where displacement pressure on long-term renting would bite.

## Assumptions

- **Misuse proxy** ("Possible misuse" section, note 1): an entire property, available more than 180 days a year, whose host has 2 or more listings. This assumes 50% occupancy.
- **Activity proxy.** A listing with at least one review is taken as active (about 50,000 of more than 69,000 listings in 2018, 72%).
- **Housing stock.** VOA dwelling counts (≈3.4 million, 2015) as the denominator. Dwelling types come from the 2011 Census, and tenure from Census 2011 (LSOA) and ONS 2015 (borough).
- **Rent.** Zoopla asking rents per bedroom per week, about 1.3 million listings, aggregated to borough level and min–max normalised.
- **Regression (Eq. 4).** ΔRent2015–17 = b1 Misuse2015 + b2 AddHousing2015–16 + b3 DistToCentre + b4 PropOwnedRented2015, estimated by OLS. Misuse and the tenure ratio are logged. Assumed: independence, linearity, normality and homoscedasticity. No spatial dependence is modelled.
- **Setting.** Greater London, 2015–2019 listings with 2018 the focal year. The rent model covers only 2015–2017, and misuse is measured in 2015 when total Airbnb supply was 0.75% of the stock.

## Key results

- **Supply growth (Fig. 2).** Airbnb supply was 0.75% of stock (≈25,000) in 2015 and 2.38% (≈80,000) in 2019.
- **2018 spatial extent (Fig. 3).**
  - 82% of LSOAs (3,982 of 4,835) have at least one active listing.
  - At LSOA maxima, more than 23% of dwellings are listed, 16% as entire homes; private and shared rooms are about 11% and 2%.
  - Entire homes available for more than 180 days: 0.25% (≈8,200). Possible misuse: 0.16% (≈5,300).
  - Possible misuse reaches 3.5–7% in some LSOAs in Camden, Westminster, the City and Hackney.
  - By borough: City of London up to 1.5%; Westminster and Kensington & Chelsea up to 0.9%; Tower Hamlets, Islington, Hackney and Southwark up to 0.4%.
- **LSOA correlations with misuse share (Fig. 4/5).**

  | variable | r |
  |---|---|
  | purpose-built flats | +0.28 |
  | flats in commercial buildings | +0.27 |
  | privately rented | +0.33 |
  | dwelling-type entropy | −0.14 |
  | detached houses | −0.25 |
  | semi-detached houses | −0.20 |
  | owned | −0.31 |

  No significance tests or spatial-autocorrelation adjustment are reported. Entropy ranges from 0 to ln 7 ≈ 1.94, with inner-London cores at 0.05–0.62.
- **Borough regression (Table 2, n = 33).**

  | term | coefficient | SE | p |
  |---|---|---|---|
  | intercept | 0.911 | – | – |
  | Misuse2015 | 0.0838 | 0.022 | 0.001 |
  | AddHousing | −0.0095 | – | 0.856 |
  | DistToCentre | −0.0071 | – | 0.390 |
  | PropOwnedRented | 0.1623 | 0.063 | 0.015 |

  R² = 0.62, adjusted R² = 0.56, VIF ≤ 3.54, Jarque–Bera p = 0.8, BP p = 0.41.

  The authors translate the coefficients as follows: a 100% increase in misuse means ≈8% higher rent per bedroom per week over two years, "a £90 difference in rents annually". Doubling the owned/rented ratio means ≈16%, or ≈£180 a year. (See corrections on these translations.)

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | About 0.16% of London's stock (≈5,300) was possibly misused via Airbnb in 2018, up to 3.5–7% in some LSOAs | moderate as a descriptive estimate under the stated proxy | Inside Airbnb and VOA counts. Depends on the untested 50%-occupancy assumption and on availability ≠ bookings |
| C2 | "More than 2% of all properties … are being misused" (abstract) | contradicted by the body | The body gives more than 2% *listed* and about 0.16% possibly misused |
| C3 | Misuse concentrates in low-diversity, flat-dominated, privately rented LSOAs | weak–moderate | Pairwise LSOA correlations with abs(r) ≤ 0.33. No inference or spatial adjustment |
| C4 | 2015 misuse is positively associated with 2015–17 borough rent change | weak–moderate | OLS, n = 33, p = 0.001. Cross-sectional, with no control for initial rent level, tourism demand or gentrification trend. Ecological |
| C5 | Doubling misuse ≈ +8% rent per bedroom-week (≈£90/yr) | weak (a translation error) | Mixes a normalised dependent variable with a log-unit coefficient (see corrections) |
| C6 | "It is plausible that our speculation that Airbnb disrupts the provision of housing for permanent residents is well-grounded" | informal argument | Discussion. The data are associational throughout; the paper itself earlier calls causality "a challenging research question" |
| C7 | Results are "comparable" with Barcelona (up to +7%), Boston (+0.4% per SD, up to 3.1%), US (+0.018% per 1% listings) and NYC (+6–9% per doubling) | assertion | Numbers quoted from other studies. Different estimands and designs |

## Concepts

- **Possible (potential) misuse.** An entire-home listing offered for more than 180 days a year by a multi-listing host. "Possible" because occupancy is assumed (note 1).
- **Dwelling-type entropy.** H = −Σ_i P_i ln P_i over K = 7 Census dwelling types per LSOA. H_max = ln K ≈ 1.94 (Eqs 1–3).
- **LSOA.** Lower Super Output Area, averaging about 1,500 residents in London. There are 4,835 of them.
- **Min–max-normalised rent change.** The borough 2015–17 change rescaled to [0, 1] across boroughs.

## Connections

The paper follows Schäfer & Braun (2016) on Berlin misuse (0.30% of stock, 5,555 units) for its definition. It follows the Batty-school use of entropy as urban heterogeneity (Batty et al. 2014; Wilson 2013), and extends Quattrone et al. (2016) on Airbnb and socio-economic attributes. For magnitudes it compares with Barron et al. (2018), Horn & Merante (2017), Garcia-López et al. (2019) and Sheppard & Udell (2018). Those studies use panel or instrumental designs that this paper does not replicate. Its policy context is Ferreri & Sanyal (2018) on London's "regulated deregulation". No other work in this record bears on it.

## Bearing on the record

- It is a social-science background item on platform effects on housing. The descriptive misuse map is its durable part.
- If the record ever cites an Airbnb rent effect, this paper's 8% figure should not be the source: see C5. The panel and IV studies it cites are better sources for effect sizes, though I have not read them.
- Nothing here bears on ML practice. No ANTH- document is implicated.

## Limitations

- Headline inconsistency between the abstract and the body on the misuse share (C2).
- A 33-observation cross-section with 4 regressors. There is no spatial-dependence test, although boroughs are contiguous and rents are spatially autocorrelated. There is no control for pre-period rent level or trend, tourism or employment.
- Misuse is measured in 2015, when total supply was 0.75% of stock. The rent outcome uses asking rents from Zoopla, which the authors say are "geographically uneven" and noisy in prime boroughs.
- The misuse proxy uses availability, not bookings, and relies on a 50% occupancy assumption borrowed from hotel data. It excludes single-listing hosts who breach 90 nights and includes multi-listing hosts who do not.
- The effect-size translation is unsupported (see corrections), and there are reporting errors in Table 2 significance stars and in the name of the diagnostic test.
- LSOA correlations come without tests, and the explained variance is small (r² ≤ 0.11).

## Open questions

- Does the misuse–rent association survive panel variation (boroughs or LSOAs over 2015–2019, with fixed effects) or an instrument, as in Barron et al. or Garcia-López et al.?
- What are actual booked nights, for example from AirDNA-type occupancy data? That would show how many "possible misuse" listings exceed 90 nights.
- How sensitive is the 0.16% figure to the 180-day and 2-or-more-listings thresholds?

## Corrections to the seeded skim

- **The abstract's headline figure is not the body's misuse figure.** The abstract says "more than 2% of all properties in London … are being misused through Airbnb". The body says more than 2% of the stock is *advertised* on Airbnb at all (2.38%, ≈80,000, in 2019; "More than 2% … advertised … in 2018", Discussion). Possible misuse is "around 0.16% (5300 properties)" in 2018 ("Possible misuse" section), and "almost 0.15%" in the Discussion. The dossier's summary repeats the abstract's ">2% … misused". The dossier's Skim section does note the 0.15% figure, but the two are never reconciled.
- **The "8%" translation does not follow from Table 2.** This is my analysis; the paper gives no derivation.
  - The dependent variable is described as "standardised rental change values after applying the min–max normalisation method" (Table 1: mean 0.473, SD 0.194). A unit of it is a fraction of the range across boroughs, not a percentage rent change.
  - Misuse2015 is log-transformed after a Shapiro–Wilk test, but the paper does not state the base. The coefficient 0.0838 is therefore the change per one unit of log misuse. A doubling is 0.0838 × ln 2 ≈ 0.058 in natural logs, or × log10 2 ≈ 0.025 in base 10, not 0.08.
  - So "a 100% increase … approximately 0.08 unit … equivalent to 8% unit rental price-per-week increase" conflates three things: a log-unit change with a doubling, a normalised unit with a percentage, and a two-year change with an annual £90.
- **The regression's sample size, which the dossier left unchecked, is n = 33** (32 boroughs plus the City; Table 1). The model has 4 predictors and an intercept. R² = 0.62, adjusted 0.56.
- **The misuse definition rests on availability, not bookings.** An entire-home listing counts if it is *offered* for more than 180 days a year. Note 1 derives the threshold by assuming 50% occupancy, from Visit Britain hotel bed-space occupancy of 53–55%, so that 180 days offered corresponds to more than 90 booked nights, the legal cap. The occupancy assumption is not tested on Airbnb data.
- **Reporting errors in the diagnostics.**
  - Table 2 marks Prop:owned:rented2015 as *** ("99% level") at p = 0.015.
  - The Breusch–Pagan(–Godfrey) test is described as testing "no serial correlation of the error". Breusch–Pagan tests heteroscedasticity (as the preceding sentence says), and Godfrey's test is for serial correlation. It is unclear which was run.
