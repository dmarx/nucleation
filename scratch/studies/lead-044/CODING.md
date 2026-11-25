# LEAD-044 coding, under CODING-RULES.md (unamended)

Coded on 2026-11-23. Each criterion with the passage it rests on.

## Search, as run

- Europe PMC REST search: `TITLE:"supply chain" AND TITLE:"essential" AND
  Zambia AND randomized`; `TITLE:"immunisation" AND "incentives" AND
  Rajasthan`; `"cost-equivalent" AND randomized AND "health system"` (the
  third returned nothing organizational).
- OpenAlex search (no email parameter) for the Zambia pilot's report and
  for the Andhra Pradesh Randomized Evaluation Study (AP RESt), which the
  filer knew of as a trial with arms calibrated to equal cost.
- Obstacles, not retried:
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC2871989/ : reCAPTCHA page
    (2026-11-23). Read instead through NCBI E-utilities efetch (db=pmc),
    the repository's documented interface (ADR-101).
  - Europe PMC fullTextXML for PMC2871989: HTTP 500, twice.
  - https://www.tandfonline.com/doi/full/10.1080/23288604.2019.1596050
    (Vledder et al. 2019, gold open access, CC BY): Cloudflare challenge,
    HTTP 403 (2026-11-23).
  - https://deepblue.lib.umich.edu/bitstreams/4fdb55ef-5b4f-4c64-86d3-d22feb6bfd09/download
    (the 2015 Ross School working paper): Cloudflare challenge, HTTP 403
    (2026-11-23).

## Case 1. AP RESt: inputs against incentives (Muralidharan and Sundararaman, NBER w15323, 2009)

Read: NBER working paper PDF, sections 1, 3, 6 (mechanism, as summarized in
section 1), 7 and 9, Table 9.

- **C1 yes.** 500 government-run rural primary schools in Andhra Pradesh,
  "2 out of the 10 project schools in each mandal were randomly allocated
  to each of 5 cells (four treatments and one control)".
- **C2 yes.** Four arms at four places in how a school produces learning:
  an extra contract teacher (staff), a block grant "for school materials"
  (materials), a group bonus and an individual bonus "conditional on
  average improvements in test scores" (the effort of teachers already
  there). "No school received more than one treatment".
- **C3 yes for three arms, partial for the fourth.** "The average annual
  spending on each of the input treatments was Rs. 10,000/school, while
  the group and individual incentives programs cost roughly Rs.
  6,000/school and Rs.10,000/school respectively." Contract teacher, block
  grant and individual bonus: equal. Group bonus: 10,000 / 6,000 = 1.67,
  above the 1.5 bound. The bonus slope "was set so that the expected
  incentive payment per school would be approximately equal to the
  additional spending in the input treatments".
- **C4 yes.** Normalized endline test scores, math and language.
- **C5 yes.** Randomized, mandal fixed effects, school-clustered errors.
- **C6 partial.** The paper names the contrast as inputs against
  incentives, not as location. Its mechanism finding is that the main
  channel "was not increased teacher attendance, but greater (and more
  effective) teaching effort conditional on being present"; reading that
  as "the binding constraint was effort, not staff or materials" is this
  filing's.
- **Result.** Individual bonus 0.27 SD after two years against 0.09 SD for
  the pooled input arms at the same spending ("three times larger"); group
  bonus 0.16 SD at Rs 6,000. Pooled incentives minus pooled inputs: 0.13
  SD, p = 0.002 (Table 9, column 7).
- **Limits.** The two input arms are pooled in this paper; their separate
  effects are in companion papers not read here. Location is confounded
  with conditionality: the arms acting on effort are also the only
  conditional ones. Costs exclude testing (about Rs 5,000 per school per
  year, which the paper says leaves the ranking unchanged).
- **Verdict: meets the lead's standard** (C1, C2, C4, C5 yes; C3 yes for
  the three equal-cost arms).
- **Adding can hurt:** not coded; no nested arms.

## Case 2. Seva Mandir immunisation camps with and without incentives (Banerjee, Duflo, Glennerster and Kothari, BMJ 2010)

Read: full text via E-utilities; the correction of 2016 (BMJ
2016;355:i6423) read, which swaps the abstract's two cost figures back.

- **C1 yes.** 134 villages in Seva Mandir's catchment, Udaipur.
- **C2 partial.** A: "regular availability of immunisation services"
  (supply side). B: "the same infrastructure as intervention A but in
  addition offered parents 1 kg of raw lentils" (A plus the demand side).
  Nested, not two arms at two places.
- **C3 partial.** Costs per fully immunised child only: "$27.94 ... in the
  reliable camp with incentives and $55.83 ... in the reliable camp
  without incentives". Totals per village not equalized.
- **C4 yes.** Full immunisation of children aged 1-3: 39 %, 18 %, 6 %.
- **C5 yes.** Clustered randomized.
- **C6 yes.** Supply alone "might not be enough"; drop-out after the first
  injections, which the incentive addresses: "the impact of the incentive
  was mainly to reduce the number of children dropping out after three
  injections."
- **Verdict: not a case** under the rules (C2 partial); filed as the
  closest of its kind, lacking separate arms of equal cost. The authors:
  "we could not introduce an incentive programme without simultaneously
  making the supply more reliable."
- **Adding can hurt:** the nested arm did better, not worse.

## Case 3. Zambia's 2009/10 supply chain pilot (Vledder et al. 2019, unread; read through Leung, Chen, Yadav and Gallien, PLoS One 2016)

Read: Leung et al. in full via E-utilities. Vledder et al. not reached.

- **C1 yes.** 16 districts of Zambia's public pharmaceutical supply chain.
- **C2 yes.** "Intervention A maintained intermediary stock with picking
  and packing activities in district stores; Intervention B converted
  district stores into cross-docking points for shipments pre-packaged for
  the clinics at the national warehouse."
- **C3 no** in what was read; Vledder et al.'s costs not reached.
- **C4 yes** in Vledder et al. as Leung et al. report it: "a substantial
  reduction of the average number of days without stock for these
  products in intervention B compared with intervention A and control
  facilities".
- **C5 partial.** Leung et al. call it "a quasi-randomized field
  experiment"; Vledder et al.'s title says randomized.
- **C6 partial.** Leung et al. attribute the later stock-outs to the
  max-min inventory policy, common to both arms, not to where picking sits.
- **Verdict: not a case** in what was read (C3 no); the closest of its
  kind, lacking costs, until Vledder et al. is read.
