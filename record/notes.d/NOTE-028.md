---
number: 28
status: Skimmed
formerly:
- NOTE-tmp0zirq
paper: LIT-083
title: 'Disinformation incidents as cyber threat intelligence (DISINFOX)'
version: 1
date: '2026-09-25'
summary: >-
  Disinformation incidents can be carried in existing cyber-threat-intelligence infrastructure: DISARM TTP labels mapped to STIX 2.1 objects and served by an open-source exchange platform (DISINFOX). The authors validate this end to end with more than 100 real incidents ingested into OpenCTI.
---

<!-- inactive-ok-file: LIT-083 — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-25 -->

# NOTE-028: Disinformation incidents as cyber threat intelligence (DISINFOX)

## Contribution

Cybersecurity has mature, standardised ways to model and exchange threat intelligence between organisations, but disinformation campaigns have no equivalent interoperable sharing. The authors propose an open-source framework with three parts. Incidents are modelled with DISARM, a MITRE ATT&CK-style taxonomy of disinformation tactics, techniques and procedures (TTPs). A custom mapping encodes DISARM-modelled incidents as STIX2 objects. A microservice exchange architecture, DISINFOX, stores the incidents centrally and serves them to CTI clients. The implementation is validated on more than 100 real-world incidents, and the authors claim it is the first academic and technical effort to bring disinformation into the CTI ecosystem.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- The paper compares five disinformation-modelling frameworks (DISARM, SCOTCH, BEND, ABCDE, ALERT; §3.1, Table 1). It picks DISARM because it is the only one that combines TTPs, STIX2 codification and cybersecurity analogies (kill chain, ATT&CK). DISARM has no explicit actor analysis, and BEND is the only framework with quantitative analysis (§3.1.2–3.2).
- The DISARM matrix is organised as phases → tactics → techniques, illustrated on a Russia–Ukraine case, the "Ukraine Re-sold French Howitzers" incident (URFH) (§3.3, Table 2).
- The STIX2 mapping (§4, Tables 3–4): disinformation entities become STIX Domain Objects (incident, threat actor, attack pattern, location, and so on), and their relations become STIX Relationship Objects. Fig. 1 shows the URFH incident as a STIX bundle graph.
- The DISINFOX architecture (§5, Figs. 2–6) is containerised. It has a web frontend with knowledge graphs and export, a public API, and a custom OpenCTI connector. The incident lifecycle runs report → upload → STIX transform → retrieval → OpenCTI ingestion (Fig. 4).
- Limitations (§6): only 118 incidents, all labelled by hand; a "minimal" STIX mapping; no TAXII support in the API. Future work proposes LLMs to automate DISARM labelling and alignment with DAD-CDM. The authors note that the stack (DISARM + STIX2.1 + OpenCTI) matches the approach the EU and US agreed at the fourth Trade and Technology Council ministerial.

## Open questions

- It is a data-standards and systems paper, not an empirical study of disinformation. The validation shows that the pipeline works, not that sharing improves detection or response.
- It pairs naturally with c02: the EEAS reports also encode FIMI incidents in STIX. Worth checking how closely DISINFOX's mapping matches the EEAS/DISARM practice.
- The future-work proposal (LLM-assisted TTP labelling) is the only ML hook, and it is unevaluated.
- Tagging gap: `society-and-governance` covers information operations, but the vocabulary has no security or cyber-threat topic for the CTI half of the paper.
