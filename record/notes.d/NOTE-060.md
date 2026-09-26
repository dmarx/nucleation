---
number: 60
status: Read
formerly:
- NOTE-tmpj7uks
paper: LIT-084
title: '3rd EEAS report on FIMI threats (2025)'
version: 2
history:
- version: 2
  date: '2026-09-25'
  note: >-
    Read in full (full text of the 43-page PDF
    (EEAS-3nd-ThreatReport-March-2025-05-Digital-HD.pdf, downloaded
    2026-09-26 to raw4/c02.pdf, extracted with pypdf because pdftotext is
    not installed). That covers the foreword (HR/VP Kallas), glossary,
    executive summary, disclaimer, introduction, ch. 1 on trends (with the
    Russia and China actor profiles), ch. 2 on the Exposure Matrix (Figs.
    3–4, Table 1, the criteria page), ch. 3 on network analysis (Figs. 5–6,
    the Doppelgänger, False Façade, Portal Kombat and African Initiative
    profiles), all three case studies (Moldova, Africa, Chinese
    influence-for-hire), the conclusions and all 58 reference notes. The
    network graphs (the pp. 22–23 spread and Figs. 7–9) are images; only
    their labels and captions were read. Page numbers below are the report's
    printed numbers. After the two-page graph spread they run one ahead of
    the PDF page index, so the conclusions are printed p. 38 (PDF p. 37).).
    Upgraded from `Skimmed` to `Read`: the claims table, assumptions and
    results are new, and the skim is corrected where the full text
    disagreed.
date: '2026-09-25'
summary: >-
  The EEAS classifies channels in foreign information manipulation and
  interference (FIMI) into four tiers by their tie to a state: official,
  state-controlled, state-linked (covert, attributed) and state-aligned
  (non-attributed). It applies the scheme to 505 incidents it detected
  between 4 Nov 2023 and 4 Nov 2024, involving about 38,000 channels. In a
  filtered co-involvement graph of 2,055 recurrent channels, 20% are
  Russian-attributed, 3.5% Chinese-attributed and 76.5% non-attributed.
  The report states that the sample is illustrative and should not be used
  to infer general trends.
---

<!-- inactive-ok-file: LIT-083 — Proposed; DISINFOX, named in Connections as the encoding the EEAS scheme could feed -->

# NOTE-060: 3rd EEAS report on FIMI threats (2025)

## Contribution

This is the third in an annual series. The 1st report (Feb 2023) set out a FIMI analysis methodology and the 2nd (2024) a response framework; this one adds an attribution taxonomy, the FIMI Exposure Matrix. The Matrix sorts any channel, whatever the actor, into four categories by the strength and kind of evidence tying it to a state. It lists technical and behavioural indicators, grades them by confidence and by access (open, proprietary or classified), and gives criteria per category. The report then applies the Matrix to the EEAS's 2024 monitoring sample, draws a co-involvement network of Russian and Chinese FIMI infrastructure, and profiles named covert operations and three regional cases. Its stated purpose is to underpin attribution and so enable costs such as exposure and sanctions (pp. 5, 38).

## Key insight

The overt state voice (ministries, RT, CGTN) is a small, identifiable core. Most of the channels that carry FIMI cannot be formally attributed. The report's position is that they should still be classified, as "state-aligned", on repeated technical and behavioural patterns, and should be reclassifiable as evidence accrues. It is equally explicit that narrative alignment alone is not enough and that over-attribution is to be avoided (p. 14). Attribution is thus treated as graded and revisable. The final public attribution is, in the report's words, "often political" (p. 19; glossary p. 4).

## Assumptions

Premises and authorities the report rests on:

- **Sample.** The incidents are those "detected and analysed" by EEAS strategic monitoring, which "does not cover all regions or languages". The report says they reflect "known outlets related to overt FIMI or independently attributed operations by selected actors and on priority issues of the EEAS", and that they are illustrative and "should not be used to draw conclusions about general trends" (p. 6; p. 9 notes i–ii). Platform coverage depends on data access and on whether automated collection was feasible (p. 10 n. iv). Romanian election activity is excluded (n. iii).
- **Definition.** FIMI is "a mostly non-illegal pattern of behaviour" that is manipulative, intentional and coordinated, by state or non-state actors (glossary p. 4, from the EEAS 2021 activity report).
- **Framework lineage.** The Matrix builds on the Actor dimension of Pamment's ABCDE framework (p. 14, n. 26). It also draws on attribution work by the NATO StratCom COE and Hybrid CoE (Pamment & Smith 2022), Adac.io and cyber-attribution literature (nn. 27–35). It adopts STIX encoding and TTP vocabulary from CTI.
- **Evidence access.** The strongest indicators (financial records; shared infrastructure seen in proprietary or classified data) are often unavailable to outside researchers (p. 18). Category 3 assignments therefore partly rest on evidence the report does not show.
- **Institutional stance.** The report is the EU diplomatic service's own publication, with a political foreword that frames FIMI as "a major security threat" and cites the EU's first FIMI sanctions (December 2024). It is a policy document as much as an analysis.

## Key results

Counts (all from the 2024 sample, attributed to the EEAS):

- **Scale (p. 9, Fig. 1).** 505 incidents; about 38,000 unique channels; 25 platforms; more than 68,000 observables; 90 countries and 322 organisations targeted. Organisations were targeted in 85% of incidents and individuals in 53% (p. 10).
- **Targets (pp. 9–10).** Ukraine 257 incidents ("almost half"), France 152, Germany 73 and Moldova 45. Sahel states are frequent targets. There were 42 Russian FIMI cases around the June 2024 European elections, peaking 6–9 June, with "no severe incidents" detected (p. 10).
- **TTPs (p. 11).** At least 349 incidents localised content; 28 used online ads. Disposable bot and CIB accounts made up 73% of channels (28,000 of 38,000). There were 124 inauthentic news sites, 127 impersonations of established entities and 13 impersonations of political figures or celebrities. About 41 incidents involved AI.
- **Exposure Matrix (pp. 14–19).**
  1. *Official state channels* (overt; self-attributed government accounts).
  2. *State-controlled outlets* (overt; owned, funded and editorially controlled; RT, Sputnik, CGTN, and mirrors that share infrastructure).
  3. *State-linked channels* (covert but attributed; high-confidence indicators, mostly proprietary or classified, combined with open-source indicators).
  4. *State-aligned channels* (non-attributed; combinations of medium-level, mostly open-source indicators showing "strong, repetitive patterns of alignment").

  Indicators are grouped as technical (public affiliation, financial records, shared infrastructure such as IPs, hosting, domain ownership, ad networks and ASNs) or behavioural (systematic amplification, coordinated messaging, reuse of inauthentic assets, historical consistency). They run from higher to medium confidence (Table 1, p. 17). Classification is "not static" (pp. 14, 16).
- **Network (p. 20).** Nodes are channels, and an edge means "shared involvement in FIMI incidents". Only channels in more than one incident with at least two connections are kept, giving 2,055 nodes and 8,056 edges. By attribution: Russia 20%, China 3.5%, non-attributed 76.5%. China's infrastructure is described as "highly centralised and synchronised" and Russia's as "more decentralised" (p. 20). Node roles are high-influence hubs, boosters and bridges (p. 21).
- **Operations profiled (pp. 26–28).**
  - *Doppelgänger*: attributed to Russia, via the firms Struktura and SDA; 228 domains; "25,000 CIB networks"; 9 languages; 60 incidents; a "self-contained cluster" with no direct interaction with official or state-controlled sources.
  - *False Façade / Storm-1516 / CopyCop*: 230 sites; 47 incidents; bi-directional laundering; pre-created backup domains on bulletproof hosting.
  - *Portal Kombat / Pravda*: 200 outlets in 35 languages; 73 incidents; automated republication; traced by VIGINUM to a Crimea-based firm.
  - *African Initiative*: 16 sites and channels in 6 languages; 18 incidents; EU-sanctioned; described as run by people linked to the FSB and GRU.
- **Laundering (p. 24, Fig. 5).** A worked example traces a false Zelenskyy villa story from a new YouTube channel (31 Mar 2024), through a False Façade site, Telegram and aligned outlets, and Sputnik and Ukraina.ru, to a Russian MFA account citing "British media" (5 Apr). Laundering is said to run in both directions.
- **Cases.**
  - *Moldova (pp. 29–31)*: infrastructure previously aimed at Ukraine was redeployed; new assets appeared, including Portal Kombat Moldova domains and Moldova24 (at least 14 sites, with an IP associated with RT-affiliated sites, blocked by Moldova's SIS). Reported methods include a deepfake, forged letters and a Telegram chatbot paying for anti-EU content.
  - *Africa (pp. 32–34)*: state media expanded after the 2022 EU suspension of RT and Sputnik; African Initiative took over from Wagner's media activities; two-way laundering through Sputnik Afrique.
  - *China (pp. 35–37)*: HaiEnergy (Mandiant: at least 72 sites; the EEAS now counts at least 316, 140 of them in the graph), Paperwall (Citizen Lab: at least 123 sites) and a newly labelled "VN" network (at least 142 sites). They are tied together by IPs, AdSense and Analytics codes and shared intermediaries. The PR firms are placed in category 4 (state-aligned).
- **Conclusions (p. 38).** Covert and non-attributed channels will "very likely" remain central. FIMI analysis must be integrated with CTI. FIMI is "a strategic instrument embedded in the foreign policy toolbox of threat actors".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The Exposure Matrix gives a systematic, actor-agnostic way to classify channels and support attribution | moderate (as a proposal) | explicit categories, criteria and indicator list (pp. 15–18); no inter-rater test, no worked classification of individual channels with evidence |
| C2 | Official and attributed channels are "the tip of the iceberg"; non-attributed channels are 76.5% of the architecture | moderate for the graph share; weak as stated in the conclusions | network count on 2,055 filtered channels (p. 20); the conclusions (p. 38) extend it to "channels investigated" |
| C3 | Ukraine was the main target (257 incidents), followed by France (152), Germany (73) and Moldova (45) | moderate as sample counts | EEAS incident data; the report itself disclaims generalisation (p. 6) |
| C4 | X accounts for 88% of detected activity | weak | stated without denominator; the platform counts in Fig. 2 do not reconcile with the 38,000 total |
| C5 | Russian and Chinese networks cross-amplify, but opportunistically, not systematically | moderate | network observation (p. 25), named bridging outlets; no quantification of cross-edges |
| C6 | China's FIMI infrastructure is centralised and synchronised; Russia's is decentralised and adaptive | weak–moderate | qualitative reading of the graph (p. 20); no metric reported |
| C7 | Doppelgänger, False Façade, Portal Kombat and African Initiative are Russian-linked operations with the stated sizes | moderate | EEAS data plus third-party exposures (VIGINUM, DFRLab, Clemson, Microsoft, Recorded Future, Citizen Lab, Mandiant; nn. 36–57) and EU/UK/US sanctions; proprietary evidence referred to but not shown |
| C8 | HaiEnergy, Paperwall and VN are linked through shared intermediaries to Chinese PR firms that partner with state media | moderate | technical indicators named (IP, AdSense, Analytics codes) and third-party reports (Mandiant, Citizen Lab, Korean NCSC); raw evidence not shown |
| C9 | AI use in FIMI is increasing, but its use does not necessarily increase impact | weak | about 41 incidents counted; the impact claim is asserted |
| C10 | In future, operations may be attributable from recurring combinations of STIX objects, as with APTs | assertion | forward-looking statement (p. 19) |
| C11 | FIMI is a strategic foreign-policy instrument and a security threat requiring a whole-of-society response | assertion / institutional position | conclusions and foreword |

## Concepts

- **FIMI** — "a mostly non-illegal pattern of behaviour that threatens or has the potential to negatively impact values, procedures and political processes", manipulative, intentional and coordinated, by state or non-state actors and their proxies (p. 4).
- **Exposure** vs **attribution** — making hidden FIMI activity public, as against identifying the responsible actor. The report calls attribution's final decision political (p. 4).
- **FIMI Exposure Matrix** — the four-category, evidence-graded classification of channels described under Key results (pp. 14–19).
- **State-aligned channel** — non-attributed, but showing "systematic signs of alignment with a state entity"; held in this category "until more evidence emerges" (p. 15).
- **Booster node** / **bridge** — channels that systematically repost content from core actors, or connect clusters across platforms or regions (p. 21).
- **Information laundering** — moving content between attributed and non-attributed layers so that its origin is obscured; described as bi-directional (p. 24).
- **Information confrontation (информационное противоборство)** — named as "central to Russian doctrine, where information is both the weapon and the environment" (p. 12). The report asserts this and cites no Russian doctrinal text for it.

## Connections

- **DISINFOX (c01, [LIT-083](../literature.d/LIT-083.md)).** Both documents encode FIMI or disinformation incidents in STIX and call for integration with CTI. The EEAS counts "Attack Patterns" under TTPs "encoded in STIX objects" (p. 14) and expects APT-style attribution from recurring STIX combinations (p. 19). DISINFOX supplies a public mapping and exchange path of that kind, but models attribution as a single edge. The Exposure Matrix, which grows out of ABCDE's Actor dimension, is exactly the actor-graded layer that DISINFOX's chosen framework (DISARM) lacks. The EEAS does not publish its own STIX encoding, so the two cannot be compared field by field.
- **Fridman (c11, [LIT-088](../literature.d/LIT-088.md)).** The EEAS names "information confrontation" as central to Russian doctrine (p. 12). Fridman's article traces the Russian theories that frame the West as waging information war on Russia, and cites Russian work on informatsionnoe protivoborstvo (c11 n. 2). The two describe the same field from opposite ends: the EEAS catalogues Russian practice, and Fridman describes the Russian self-account of being the target.
- **Clark, "Russian Hybrid Warfare" ([LIT-023](../literature.d/LIT-023.md)).** The foreword's statement that FIMI is "an integral part of military operations used by foreign states to lay the way for kinetic action" (p. 2) parallels Clark's reading that in Russian hybrid war kinetic action is subordinate to information campaigns. The report does not cite Clark, and it does not develop the military link beyond the foreword.
- **Series and sources.** It builds on the 1st report (Feb 2023, methodology) and the 2nd (Jan/Feb 2024, response framework; the body calls it "(2023)" on pp. 10 and 38). It relies heavily on the Pamment and ABCDE attribution literature, and on external exposures by VIGINUM, DFRLab, Clemson's Media Forensics Hub, Citizen Lab, Mandiant and Recorded Future.

## Bearing on the record

It carries no instruction for machine-learning practice, and no THEORY document is affected. The generative-AI passages (p. 11) are counts and assertions: about 41 AI-involving incidents; AI text "probably" used but hard to detect; no evidence of greater impact. They are not a finding about detection methods, and the anthology should not cite the report for any claim about AI-text detectability. The network-science tag from the skim is justified only lightly. The network is a descriptive co-involvement graph with filtering thresholds; no network-science method is reported.

## Limitations

- The sample is non-representative by the report's own account (p. 6; p. 9 n. ii). Every count is a count of what the EEAS monitored, and the report says so.
- The network construction is described only in outline. The edge definition is co-involvement in an incident, and edge weight is "more frequent interactions". Layout, weighting and the software used are not given, nor are centrality or cluster metrics. "Centralised" and "decentralised" are read off the picture.
- The headline 76.5% belongs to a filtered graph that excludes 28,000 CIB accounts and all single-incident channels. The conclusions generalise it to all channels investigated.
- The figures do not reconcile. The platform counts sum to more than the 38,000 total. The foreword (more than 80 countries, more than 200 organisations) differs from the body (90 countries, 322 organisations). The 88% for X has no stated base.
- Category 3 attributions rest partly on proprietary or classified evidence that is not shown. Fig. 4's placement of named entities is "indicative" only (p. 16 n. v).
- There is an internal tension on hosting. "Bulletproof hosting" is defined as services that "ignore or evade law enforcement requests" (p. 27), yet on p. 36 Amazon services are given as an example of bulletproof hosting for the VN network. The report does not reconcile the two.
- The report does not measure impact. It says the "true reach and impact" of CIB networks "remains unclear" (p. 11) and assumes the Chinese networks aim mainly at search results (p. 37).
- The Matrix has not been validated. The report gives no reliability test and no worked example showing how the indicators were weighed for a particular channel.

## Open questions

- Would independent analysts using the Matrix's criteria assign the same channels to the same categories? An inter-rater study on a shared channel set would settle it.
- How much of the "state-aligned" 76.5% is later attributed, or cleared? Follow-up reports tracking reclassification would test whether the category is predictive or residual.
- How do the co-involvement graph's properties, such as the Russian and Chinese structural contrast and cross-amplification, hold up under stated metrics and alternative filtering thresholds?
- What exactly is the EEAS STIX encoding, and is it compatible with DISARM-based and DAD-CDM-based schemas (c01)?

## Corrections to the seeded skim

- The skim says "non-attributed channels are 76.5% of those investigated". The report's conclusions (p. 38) do say "a sizeable majority (76.5%) of the channels investigated". However, the body defines the figure on the network graph (p. 20): 2,055 channels "that appeared in multiple incidents and are connected to at least two other nodes", after about 28,000 disposable CIB assets were removed. The 20% Russian, 3.5% Chinese and 76.5% non-attributed shares add to 100% of that graph. They are not shares of the 38,000 channels. The conclusions restate a graph share as a share of all channels investigated.
- The skim puts the conclusions at p. 37. They are on printed p. 38 (PDF p. 37). The Exposure Matrix chapter runs pp. 14–19, not 14–18, and the network chapter, including the four operation profiles, runs pp. 20–28, not 20–23.
- The skim says the report finds "occasional cross-amplification between Russian and Chinese channels". That is accurate. The report characterises it as "ad hoc", "mostly an opportunistic behaviour, rather than systematic" (p. 25; also p. 13).
- The skim did not read what the report says about generative AI. The report says about 41 incidents in 2024 involved AI, mainly deepfake audio or video and automated dissemination through bot networks. It says AI-generated text is "probably" used but hard to detect, and that AI's use "does not necessarily translate into a greater impact" (p. 11). "Systematic use of AI tools to generate content" is also one of the Matrix's behavioural indicators (p. 17). Case-level AI mentions are a deepfake mimicking President Sandu's voice (p. 31) and AI translation of False Façade articles (p. 27).
- The skim did not note a discrepancy between the foreword and the body. The foreword says "over eighty countries and over two hundred organisations" were targeted (p. 2). The body gives 90 countries and 322 organisations (pp. 5, 9–10).
- The skim did not note that the per-platform channel counts in Fig. 2 (p. 11: X 33,000; Facebook 15,000; websites 14,000; Telegram 759; VK 183; TikTok 160; YouTube 94) add to about 63,000, well above the "38,000 unique channels". The report does not explain the difference. The 88% "of the activity" attributed to X (pp. 5, 10) has no stated denominator.
