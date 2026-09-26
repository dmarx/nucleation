---
number: 28
status: Read
formerly:
- NOTE-tmp0zirq
paper: LIT-083
title: 'Disinformation incidents as cyber threat intelligence (DISINFOX)'
version: 2
history:
- version: 2
  date: '2026-09-25'
  note: >-
    Read in full (full text of arXiv 2502.20997v1 (36 pp., downloaded
    2026-09-26 to raw4/c01.pdf, extracted with pypdf because pdftotext is
    not installed). That covers the abstract, §1 Introduction, §2 State of
    the Art, §3 Modeling (framework comparison, Table 1; DISARM selection;
    DISARM matrix with the URFH case, Table 2), §4 STIX2 codification
    (Tables 3–4, Listings 1–8, Fig. 1), §5 DISINFOX architecture (Figs.
    2–6), §6 Conclusion and future work, acknowledgements, and all 55
    references. Figs. 5 and 6 are screenshots and were read through their
    captions only. The GitHub repository, the incident dataset CSV and the
    DISARM master data it points to were not opened. The arXiv abs page
    (checked 2026-09-26) still lists only v1, and a Crossref bibliographic
    search on the same day found no journal version.). Upgraded from
    `Skimmed` to `Read`: the claims table, assumptions and results are new,
    and the skim is corrected where the full text disagreed.
date: '2026-09-25'
summary: >-
  The paper shows that a DISARM-labelled disinformation incident can be
  encoded in plain STIX 2.1 with four object types (IntrusionSet for the
  incident, ThreatActor, AttackPattern, Location) and three relationships
  (uses, attributed-to, targets), then served by an open-source
  microservice platform (DISINFOX) to OpenCTI through a custom connector.
  Its validation is a demonstration that 118 hand-labelled incidents
  passed through the pipeline; it reports no measurement of fidelity,
  usefulness or scale.
---

<!-- inactive-ok-file: LIT-083 — Deferred: the paper is placed by this reading; the directive lapses when its status changes -->

# NOTE-028: Disinformation incidents as cyber threat intelligence (DISINFOX)

## Contribution

The paper assembles existing parts into an end-to-end pipeline for sharing disinformation incidents as cyber threat intelligence. DISARM supplies the technique labels, STIX 2.1 the data format, and OpenCTI the consuming platform. The authors add three things: a small mapping from an incident's actor, techniques and targeted countries to standard STIX objects (§4); an open-source containerised exchange platform, DISINFOX, with a web frontend, a public API and a document store (§5); and a custom OpenCTI connector that pulls incidents from that API (§5.2). After the paper there is a public, working reference implementation of disinformation-as-CTI exchange, not only a proposal for one.

## Key insight

A disinformation incident can be treated as a cyber intrusion set without extending STIX. Once the techniques come from a MITRE ATT&CK-style matrix (DISARM), the analyst's knowledge of an incident reduces to "who (ThreatActor) used which techniques (AttackPattern) against where (Location)". That is already a shape CTI tooling ingests, correlates and visualises. The price is that everything outside that triple is dropped: content, narratives, channels, evidence and confidence.

## Assumptions

Premises and design commitments:

- **Disinformation is a cybersecurity concern.** It is justified by analogy (both depend on the Internet and erode trust) and by authority (ENISA lists it among main threats; §1, refs [10], [13], [14]). The paper does not argue that CTI's detection or response practices transfer to it.
- **DISARM is the right labelling scheme.** It is chosen by a qualitative seven-feature comparison against SCOTCH, BEND, ABCDE and ALERT (Table 1, §3.1.2). The decisive features are STIX2 codification, a staged methodology and the ATT&CK/kill-chain analogy, which only DISARM has. Endorsements by the EEAS, ENISA, Hybrid CoE and FIMI-ISAC are cited as supporting evidence (§3.2).
- **Attribution is a single edge.** An incident is `attributed-to` one ThreatActor, and in the worked case that actor is a country ("Russia", typed `nation-state`, Listing 2). The model has no field for attribution confidence, evidence or intermediate actors.
- **Manual labelling is the input.** Reporters submit DISARM techniques by hand (§5.3, Step 2), and the pipeline trusts them. §6 names this as the bottleneck.
- **Centralised exchange.** One DISINFOX server feeds many organisations' OpenCTI instances (Fig. 3). Transport is plain HTTP carrying STIX objects; TAXII, the CTI transport standard, is not supported (§6).

## Key results

- **Framework comparison (Table 1, §3.1).** Across seven features, only DISARM offers STIX2 codification, defined stages (Plan, Prepare, Execute, Assess) and a cyber analogy. DISARM lacks actor analysis and quantitative analysis. BEND is the only framework with quantitative analysis, and has TSV codification for ORA-PRO. SCOTCH lacks countermeasures. ABCDE and ALERT are judged conceptual.
- **DISARM matrix (§3.3).** It has 4 phases. PLAN has 3 tactics, PREPARE 6, EXECUTE 6 and ASSESS 1, with techniques and sub-techniques under the tactics. The URFH case is encoded as 10 techniques across 5 tactics in 3 phases (Table 2), and ASSESS is "not intuitively interpretable by the analyst".
- **STIX mapping (§4, Tables 3–4).**
  - Incident maps to IntrusionSet (name, description, first_seen, labels ["incident","disinformation"]).
  - Actor maps to ThreatActor (threat_actor_types e.g. ["nation-state"]).
  - Technique maps to AttackPattern. DISARM's own pre-generated objects are reused, which is why their timestamps predate the others by more than a year (Listing 3).
  - Country maps to Location.
  - The relationships are Incident `uses` Technique, Incident `attributed-to` Actor and Incident `targets` Country. The objects are packaged as a STIX Bundle (Listing 8, Fig. 1).
- **Architecture (§5.1–5.2, Figs. 2–3).** The system has four services: a frontend (manual and bulk upload, maps, knowledge graphs, export to STIX bundle, Word and PDF), a backend (validation, transformation, document database), a public API and an OpenCTI connector. It is deployed with Docker (§6).
- **Validation (§5.3, §6).** 118 incidents were "modeled, stored, shared, and consumed successfully" and were pushed into OpenCTI by a proof-of-concept connector. Figures 5–6 show the URFH incident in the DISINFOX frontend and in OpenCTI's Knowledge tab. No other quantity is reported: no error rate, round-trip fidelity check, throughput, user study or correlation result.
- **Policy alignment (§6).** The stack of DISARM, STIX 2.1 and OpenCTI is said to match the approach agreed by the EU and US at the fourth Trade and Technology Council ministerial (ref [55]).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | DISARM-labelled incidents can be represented with standard STIX 2.1 objects and relationships, without extensions | strong (as a demonstration) | explicit mapping (Tables 3–4) and worked listings; the objects shown are valid STIX shapes |
| C2 | DISARM is the most suitable framework for CTI-oriented modelling of disinformation | moderate | qualitative feature comparison adapted from the authors' prior paper (Table 1); the criteria (codification, cyber analogy) favour DISARM by construction for a CTI goal |
| C3 | The DISINFOX pipeline works end to end, from upload to OpenCTI ingestion, on more than 100 real incidents | moderate | implementation and screenshots; count of 118; no fidelity or error measurement |
| C4 | The work is the first academic and technical effort to integrate disinformation threats into the CTI ecosystem | weak | assertion ("to the best of our knowledge"); §2 itself describes DAD-CDM (2023) and an existing OpenCTI DISARM connector |
| C5 | CTI-style sharing of disinformation could enhance global collaboration and the detection and mitigation of campaigns | assertion | stated as motivation (§1); not tested |
| C6 | Large language models could significantly reduce the time and expertise needed to map incidents to DISARM TTPs | assertion | future work (§6); no experiment |
| C7 | The DISARM + STIX 2.1 + OpenCTI stack matches the EU–US TTC approach to FIMI | moderate | citation of the TTC fourth-ministerial annex ([55]); alignment asserted, not detailed |

## Method

1. **Select a model.** Compare five frameworks on seven features and choose DISARM (§3).
2. **Label.** A reporter identifies an incident and assigns DISARM techniques, plus an actor name and targeted countries (Fig. 4, Steps 1–2).
3. **Transform.** The backend creates the SDOs (IntrusionSet, ThreatActor, Location). It looks up the pre-existing DISARM AttackPattern objects by ID rather than minting new ones, then creates the three kinds of SRO (Fig. 4, Step 3).
4. **Store and serve.** Bundles are stored in a document-oriented database and exposed through the frontend and a public HTTP API (Step 4).
5. **Consume.** A custom OpenCTI connector polls the API and imports the bundles. OpenCTI renders the techniques against the DISARM matrix using the `kill_chain_phases` field (Step 5; Listing 3).

## Concepts

- **Disinformation incident** — as modelled here: a named, dated event with a description, attributed to an actor, using DISARM techniques and targeting countries. It is encoded as a STIX IntrusionSet, not as STIX 2.1's `incident` object.
- **DISARM** — Disinformation Analysis and Risk Management: an ATT&CK-style matrix of disinformation phases, tactics (TA-codes) and techniques (T-codes), with countermeasure mappings and a STIX2 generator for its techniques (§3.1.1, §3.2, ref [47]).
- **CTX (Cyber Threat Exchange)** — a platform that shares indicators, reports and TTPs among collaborators, e.g. AlienVault OTX (§1).
- **URFH** — "Ukraine Re-sold French Howitzers", the July 2022 incident, sourced to a DFRLab write-up ([53]), used as the running example.
- **DAD-CDM** — the OASIS "Defending Against Deception Common Data Model" (2023), a STIX-based data model for disinformation; named as related work and as a future alignment target.

## Connections

- **The 3rd EEAS FIMI report (c02, [LIT-084](../literature.d/LIT-084.md)).** Both documents put FIMI or disinformation incidents into STIX. The EEAS says all 505 of its 2024 incidents "have been encoded in STIX" and calls for FIMI analysis to be integrated with CTI (c02 pp. 6, 9, 38). This paper supplies a public mapping and exchange path of the kind the EEAS calls for; the EEAS report does not publish its own encoding, so how closely the two match cannot be checked from these texts. The paper cites the 1st and 2nd EEAS reports, not the 3rd, which appeared three weeks after it ([7], [8]).
- **The two documents are complementary on attribution.** This paper picks DISARM partly because the frameworks with actor analysis lack codification, and it notes that DISARM "does not explicitly offer actor-focused analysis" (§3.1.2). It then models attribution as one `attributed-to` edge to a nation-state. The EEAS Exposure Matrix is built on "the A or the Actor in the ABCDE Framework" (c02 p. 14), the framework this paper sets aside as "less actionable". It grades each channel's tie to a state into four categories with evidence tiers. The paper's schema has no place for that gradation.
- **The EEAS anticipates attribution "based on recurring attack patterns and combinations of STIX objects", "much like in cybersecurity with Advanced Persistent Threats" (c02 p. 19).** That is the use the paper's IntrusionSet mapping would support, although the paper does not attempt correlation or attribution.
- **Prior work in the paper.** DISARM (Terp & Breuer 2022), Misinfosec (Walker et al. 2019), the authors' own framework review ([22]) and their influence-operations survey ([21], arXiv 2502.11827). The paper describes the OpenCTI DISARM connector and DAD-CDM as the nearest prior art.

## Bearing on the record

It carries no instruction for machine-learning practice. The only ML content is a one-sentence future-work suggestion that LLMs could automate DISARM labelling (§6), which the paper does not evaluate; nothing in the anthology should cite it for that. No THEORY document is affected. The skim's tagging note stands: the paper is half about information operations and half about cyber-threat-intelligence data standards. If the record's topic vocabulary has no security or threat-intelligence topic, that gap is real and is not answered by `society-and-governance` alone.

## Limitations

- The authors state that the dataset is small (118 incidents), that labelling is manual, that the STIX mapping is "minimal" and that the API does not support TAXII (§6).
- There is no evaluation beyond successful ingestion. Round-trip fidelity, labelling consistency between analysts, query usefulness, correlation value and performance are all unmeasured.
- The schema drops the evidence, content, channels, narratives, dates beyond `first_seen`, confidence in attribution and countermeasures. DISARM's countermeasure mapping, cited in §3.1.2 as a reason to choose it, is not carried into the STIX model.
- Attribution is represented without confidence or provenance. In the worked example "Russia" is a nation-state ThreatActor on the strength of one DFRLab write-up.
- The DISARM AttackPattern objects that are reused carry `source_name: "mitre-attack"` and `kill_chain_name: "mitre-attack"` (Listing 3). This is DISARM's generator output, not a choice by the authors. The paper does not discuss whether the labels could collide with genuine MITRE ATT&CK objects in a shared OpenCTI instance; this reading notes it and has not verified it against OpenCTI.
- The framework comparison is qualitative and adapted from the authors' own earlier work.
- The small inconsistencies noted under corrections (date, technique name) are harmless in a demonstration, but they are the kind of error a hand-labelling pipeline propagates.
- It is a preprint that says it was submitted to *Computers & Security*; no published version was found as of 2026-09-26.

## Open questions

- Does sharing incidents in this form improve anything downstream, for example correlation across organisations, faster exposure or reuse of labels? A deployment study with consuming analysts would settle it.
- How do the DISINFOX mapping and DAD-CDM differ, and could one be translated into the other without loss?
- Can attribution confidence, of the kind in the EEAS Exposure Matrix's four tiers, be expressed in STIX here, for example through `confidence` or opinion objects, without leaving the standard?
- Would LLM-assisted DISARM labelling match human inter-annotator agreement? It is proposed, not tested.

## Corrections to the seeded skim

- The skim says disinformation entities become STIX Domain Objects "(incident, threat actor, attack pattern, location, and so on)". There is no "and so on". The mapping has exactly four SDO types (Table 3, §4.1), and a disinformation incident is mapped to an `IntrusionSet`, not to STIX 2.1's own (stub) `incident` object; the paper does not mention that object. The paper justifies this by the IntrusionSet's "shared objectives" semantics. There are exactly three SRO types (Table 4, §4.2).
- The skim says the validation was on "more than 100 real incidents" and implies all were the authors' own. The dataset combines three sources (§5.3, fn. 5–6): Fulde-Hardy's working-paper dataset (81 election campaigns, §2), entries from the official DISARM master data, and "cases modeled by this work". The paper does not say how many of the 118 (§6) the authors labelled themselves.
- The skim says the paper claims it is "the first academic and technical effort". It does, in the abstract, but §2 itself describes two prior efforts in the same direction: OASIS's DAD-CDM (2023), a STIX-based common data model for disinformation that builds on DISARM, and an existing OpenCTI DISARM connector. The paper distinguishes itself from the connector as "basic, primarily aimed at generating reports", and does not compare itself with DAD-CDM beyond naming alignment as future work. The priority claim is therefore narrower than the abstract suggests: it is a claim about an ingestion and exchange pipeline.
- The skim cites §3.1.2–3.2 for the framework comparison. The comparison is adapted from the authors' own earlier paper ([22], JNIC 2024), per the Table 1 caption, and is qualitative. It has no scoring procedure.
- Minor internal inconsistencies the skim did not note. The URFH narrative dates the claims to July 2022 (§3.3), while the encoded `first_seen` is 2022-06-20 (Fig. 1, Listing 8). Table 2 lists T0019.001 "Create fake research", while the Fig. 1 bundle shows an AttackPattern named "Create Fake Experts". Neither affects the argument.
