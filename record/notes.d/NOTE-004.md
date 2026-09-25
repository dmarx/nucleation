---
number: 4
status: Read
formerly:
- NOTE-tmp6i7lb
paper: LIT-006
title: 'US v. Google remedies opinion'
version: 2
history:
- version: 2
  date: '2026-09-25'
  note: >-
    Read in full (full text, 230 PDF pp. (caption, TOC pp. i–iii, opinion
    pp. 1–223, witness Appendix pp. 224–226), ECF No. 1436 in No.
    1:20-cv-03010-APM, filed 09/02/25. Downloaded from CourtListener RECAP
    and text extracted with PyMuPDF (pdftotext unavailable). Every page
    read. Two images carried no text and were not seen: the AI-taxonomy
    slide (FOF ¶4, PXRD003 at 6) and the AI Overviews and Gemini screenshots
    (FOF ¶¶9, 16), plus the sample SQR image (op. p. 194). This is the
    public, redacted version. Several figures are blanked in the text: the
    Docjoins corpus size (FOF ¶29), the share of U.S. queries that trigger
    AI Overviews (FOF ¶64), the share of 70 days of logs used for RankEmbed
    (op. p. 154), and all contract dollar and percentage terms (FOF
    ¶¶79–93). Page references below are the opinion's own page numbers ("op.
    p."); PDF page = op. p. + 4. "FOF ¶" = the numbered Findings of Fact.).
    Upgraded from `Skimmed` to `Read`: the claims table, assumptions and
    results are new, and the skim is corrected where the full text
    disagreed.
date: '2026-09-25'
summary: >-
  Remedies opinion after the 2024 §2 liability ruling. The court (Mehta,
  J.) bars exclusive distribution deals for Search, Chrome, Assistant and
  the Gemini app, with a one-year exit right on all payment deals. It does
  not ban payments, and it rejects the Chrome and Android divestitures and
  choice screens. It orders (i) a one-time snapshot of six Search Index
  fields per document, (ii) Glue and RankEmbed user-interaction training
  data "at least twice", capped and privacy-treated, and (iii) five-year
  search and text-ads syndication on ordinary commercial terms (search
  capped at 40% of queries in year one). "Qualified Competitors" is
  rewritten so it can include GenAI firms. The term is six years (five
  plus one of ramp-up). On GenAI, the court finds that grounded chatbots
  perform an information-retrieval function similar to general search
  engines, enough to bring GenAI inside the decree. It also finds that
  plaintiffs "did not establish that Google's scale advantage in Search
  translates into a quality advantage in GenAI search-assisted responses"
  (op. p. 156). For that reason it refuses to order sharing of Gemini
  training data.
---

# NOTE-004: US v. Google remedies opinion

## Contribution

The opinion is the remedial decree's reasoning in *United States v. Google LLC* and *Colorado v. Google LLC* (consolidated). It adds three things that did not exist before.

1. It makes findings of fact, on a contested evidentiary record (evidentiary hearing Apr. 22–May 9, 2025; ~50 witnesses), about what LLMs are, why they need grounding in a search index, and who competes in GenAI.
2. It holds that GenAI products and firms fall within an antitrust remedy for a general-search monopoly. The basis is that grounded chatbots perform an information-retrieval function similar to general search engines, although not identical to it (COL §IV).
3. It orders a forced-data-sharing remedy tied to "scale", the user-interaction data found to be a fruit of the violation. Its tailoring distinguishes raw user-interaction data (shareable) from engineered ranking signals, models, and data not derived from user scale (not shareable).

## Key insight

The court treats data scale as the "fruit" of exclusive distribution and remedies it with raw data rather than with structure. It shares the inputs that scale produced: Glue click-and-query logs, RankEmbed training data, and index metadata. It does not share the engineered outputs (ranking signals, models, the Knowledge Graph) or the proceeds of scale (ads, publisher content). It brings GenAI in by function: a chatbot grounded in search does something similar to a search engine, so rivals with a "plan to invest and compete in or with" search may qualify for the remedies. But the court finds no proof that Google's search scale gives its GenAI models a quality edge. So nothing specific to GenAI model training is shared.

## Assumptions

The legal standards the court applies:

- **Remedial objectives** (*Microsoft III*, 253 F.3d at 103): unfetter the market, deny the defendant the fruits of the violation, and ensure no practices likely to result in future monopolization. The fourth objective, "terminate the illegal monopoly", is expressly not decided and not relied on (fn. 3, op. p. 58).
- **Tailoring**: the remedy must be "tailored to fit the wrong" (*Microsoft III* at 107). It may reach practices "of the same type or class" (*Zenith*), may impose affirmative obligations (*Massachusetts v. Microsoft*, 373 F.3d at 1215), and is valid if it is a "reasonable method of eliminating the consequences of the illegal conduct" (*NSPE*, 435 U.S. at 698).
- **Limits**: no punishment, no enjoining "all future violations", no aid to a particular competitor (*Brooke Group*), and care about innovation incentives and consumer welfare (*Massachusetts* at 1219). "Judicial humility" and "caution is key" (*NCAA v. Alston*, 594 U.S. at 106–07). No compelled product redesign (*New York I*, 224 F. Supp. 2d at 158). Decree terms must be specific enough to satisfy Fed. R. Civ. P. 65(d).
- **Causation, sliding scale** (op. pp. 63–74): "significant causal connection" is **not** but-for causation. The court rejects Google's reading of *Microsoft III* at length. Following *New York I* (at 102), "[t]he more drastic the remedy, the greater the causal connection required" (op. p. 73). Structural relief needs "a clearer indication of a significant causal connection" (*Microsoft III* at 106).
- **Strength of the liability-phase inference** (op. pp. 74–82): the court may revisit the liability record to grade its causal inference. It finds the inference stronger than in *Microsoft*, because the exclusion was aimed at "established substitutes" rather than nascent threats and the agreements "froze" the ecosystem. That is enough for "at least some" behavioral remedies, but not structural ones.
- **Fruits** need not be quantified (op. pp. 97–98). The fruits identified are freedom from threats, scale, and revenue (op. pp. 82–97).
- **Extending the remedy to new technologies**: *New York I* (at 128–29) asked whether a technology "has the capacity to function in a manner similar to" the protected category and has "a reasonable possibility of 'dissipating the restraints'". The court applies that test to GenAI (op. pp. 101–102).
- **Network-effects markets** may need "more aggressive means" than prohibition (3 Areeda & Hovenkamp ¶653a; *In re Google Play Store*, 9th Cir. July 31, 2025) (op. pp. 108–110).
- Setting: the relevant geographic market is the United States. Liability rests only on exclusive distribution agreements (browser agreements, MADAs, RSAs), not on product design, Chrome ownership or self-preferencing (op. pp. 9–11, 115, 190, 216).

## Key results

**Holdings and remedy ordered** (joint revised final judgment due Sept. 10, 2025; op. pp. 222–223):

- **Prohibitory injunction**. Google's proposal is accepted with modifications (op. pp. 104–111). The following are barred:
  - exclusive contracts for Search, Chrome, Google Assistant and the Gemini app;
  - conditioning Play Store or other app licensing on their placement;
  - cross-conditioning revenue share across these apps;
  - conditioning payments on placement for more than one year;
  - barring partners from distributing rival search engines, browsers or GenAI products.

  The court's modifications: a one-year renegotiation option now covers OEM and carrier deals, not only browsers. Browser developers may promote any "GenAI Product", and no exclusive GenAI deal with Apple is allowed. The definition of "Gemini Assistant Application" must cover future GenAI products.
- **Rejected**: Chrome divestiture (op. pp. 112–118), contingent Android divestiture (op. pp. 118–119), payment ban (op. pp. 119–128; the court is "prepared to revisit" it), choice screens (op. pp. 187–191), Knowledge Graph sharing, ads-data sharing, search-query-report, exact-match and data-export remedies, contingent marginal-cost ads syndication, public education fund, publisher exclusivity and opt-out remedies, anti-retaliation and anti-circumvention clauses (Rule 65(d)), investment notification, and self-preferencing bans.
- **Search Index data** (op. pp. 136–148). A one-time snapshot, at marginal cost, delivered at certification. It is limited to databases "crawled from the web" and contains DocID with duplicate notation, DocID→URL map, first-seen time, last-crawl time, spam score and device-type flag.
- **User-side data** (op. pp. 151–164). The data used to build or operate Glue and to train RankEmbed, disclosed "at least twice", with a cap to be set after consulting the Technical Committee. Privacy-enhancing techniques are applied first.
- **Search syndication** (op. pp. 168–180). Five-year license. Ranked organic web results from crawling, plus features, on terms "no less favorable than a current licensee". Priced at "financial terms no worse than those offered to any other user". First-year cap of 40% of annual queries, then a Technical-Committee taper. Ordinary use restrictions (no scraping, indexing or crawling) are allowed. No synthetic queries and no FastSearch. Google may not refuse a Qualified Competitor's request.
- **Search text ads syndication** (op. pp. 180–186). Five-year license with MFN pricing and non-discriminatory latency. No minimum-CPC right, no "all Ads Data", and ordinary restrictions allowed.
- **Ad-auction transparency** (op. pp. 199–201). Google must publicly disclose material auction changes, under parameters Plaintiffs and the Technical Committee develop, aimed at "ad launches" above a price-increase threshold.
- **Technical Committee** (op. pp. 210–213). Five members. The required expertise is "software engineering, information retrieval, artificial intelligence, economics, and behavioral science", to which the court adds "data privacy and data security". Its provisions take effect immediately.
- **Qualified Competitor** is redefined (op. pp. 103–104). "Competitor" now includes a provider of "a GenAI Product in the United States". An eligible firm must have a "plan to invest and compete in *or with* the GSE and/or Search Text Ads markets".
- **Term** (op. pp. 219–221). Six years (five plus one for ramp-up), effective 60 days after entry.

**GenAI Findings of Fact** (op. pp. 17–46). These are the court's findings. The witness each rests on is in brackets.

- **Definitions (FOF ¶¶1–5).**
  - GenAI "uses machine-learning techniques to generate new data" [Durrett, Collins, Hitt; PXR0102].
  - Machine learning "blends computer science with statistics" [Durrett].
  - LLMs take inputs and generate outputs "based on predictions". Language modeling is "the task of predicting the most likely next token in a sequence given a prior sequence of tokens" [Durrett].
  - Most LLMs are transformers: "a neural model—a computational model that attempts to mimic the way the human brain works—that uses billions of parameters to predict the probability of the next token" [Durrett]. Google's 2017 transformer paper is "the backbone of modern LLMs" [Collins, Pichai].
- **AI in Search (FOF ¶¶6–11).**
  - AI Overviews (2024) uses "a custom Gemini-based model" [Pichai] to summarize search results atop the results page [Durrett]. It is not triggered for every query [Reid; Parakh dep.].
  - U.S. Google queries have risen 1.5–2% since AI Overviews launched [Reid].
  - "Some evidence" suggests such features reduce clicks on organic results [Parakh dep.; PXR0158].
  - AI Mode users ask longer questions [Pichai].
- **Chatbots (FOF ¶¶12–17).**
  - Examples: ChatGPT, Claude, Grok, Copilot, Gemini [Hitt].
  - Chatbots and search are a partially overlapping "Venn diagram" [Turley, Reid, N. Fox].
  - A chatbot "makes a prediction about the answer, drawing upon the data used to train the model". A search engine retrieves and ranks from an index.
  - "Thus, chatbots perform an information-retrieval function like that performed by GSEs." This is the court's inference from Turley, Pichai and Hsiao, and from the Gemini and Perplexity demonstratives.
  - Chatbots also do things search does not: code, images, video [Pichai]; homework help, companionship, brainstorming [Reid].
- **Assistants and on-device AI (FOF ¶¶18–26).**
  - "Super assistant" ambitions, for which "Search is a necessary component" [Turley].
  - Gemini Nano runs on-device through AICore. AICore currently supports only Gemini Nano [Mickens, Samat, Collins dep.] but does not block other models from TPUs or NPUs [Samat].
  - Samsung phones ship both Gemini Nano and Samsung's Gauss.
- **How LLMs work (FOF ¶¶27–31).**
  - Pre-training on large data produces a base or foundation model. Post-training or fine-tuning imparts capabilities such as question answering or code [Durrett, Collins, Hitt].
  - Pre-training data is "primarily from public web pages", along with licensed and human-evaluation data [Hitt RDXD-32.009; Durrett].
  - Google pre-trains Gemini on its "Google Common Corpus", drawn from the Docjoins repository of web documents "visited at least once by Googlebot in the last few months". Its size is redacted; PXR0185 contrasts it with Common Crawl's "only a bit over 3 B" [Durrett; PXR0185].
  - Filtering matters. One corpus was filtered to ".14% of open-source data", and filtering improves performance [Durrett]. Deduplication and removal of spam are "common business practice" [Hitt].
- **Limitations (FOF ¶¶32–35)** [Durrett, Turley, Schechter].
  - An LLM cannot give a factual answer about information absent from its training data.
  - It is accurate on frequently seen facts and weak on rare ones.
  - It cannot store information "in a 'lossless way'".
  - It has a knowledge cutoff. Retraining "takes weeks or months" and is costly.
  - It hallucinates, producing statements "that are maybe probable to be true but not actually true".
  - The court calls these "factuality" and "recency" issues.
- **Grounding (FOF ¶¶36–46).**
  - Grounding or RAG "provide[s] a solution" to factuality and recency problems [Durrett, Allan, Collins].
  - Definition: "anchoring the output of a model on factual information or [an] external database" [Collins]. RAG is "[t]he process of accessing additional knowledge through a kind of information retrieval" [Durrett]. The terms are "sometimes used interchangeably".
  - Grounding "reduces an LLM's hallucinations and improves its factuality" [Collins, Reid, Durrett; PXR0040, PXR0105].
  - PXR0105: "Gemini model treats Google Search like a corpus for [RAG]".
  - Products turn prompts into search queries and read the results [Turley, Schechter, Cue].
  - Successful grounding "requires a high-quality search application program interface". Turley testified that quality problems with third-party search providers pushed OpenAI to build its own index. Schechter said GenAI products treat search results as fact.
  - Google grounds Gemini with **FastSearch**. It is based on RankEmbed signals, is faster because it retrieves fewer documents, and is lower in quality than full Search [Reid].
  - FastSearch is not offered through an API. Third parties get grounding through Vertex AI, and "only the information from those results", not the ranked results, "to protect its intellectual property" [Reid].
  - The Gemini app receives Knowledge Graph portions through Vertex that are unavailable to third parties [Reid; PXR0153].
- **Market (FOF ¶¶47–62).**
  - Firms that pre-train their own foundation models: Google, Anthropic, OpenAI, Meta, xAI, DeepSeek. Perplexity post-trains others' models (Meta, DeepSeek) [Shevelenko].
  - Google has invested in Anthropic [Reid; Anthropic amicus].
  - Google provides a Search API to Meta for grounding [Pancholi, N. Fox deps.].
  - OpenAI sought a grounding partnership with Google; Google declined [Turley; PXR0181].
  - "The GenAI space is highly competitive" [Turley, Collins, Hsiao]. Capital is "plentiful" [Hitt]; OpenAI raised $40B at a $300B valuation [Turley].
  - "Today, Google's models do not have a distinct advantage over others in factuality or other technical benchmarks" [Hitt; Durrett declined to opine].
  - OpenAI's own December 2024 estimate of U.S. share: ChatGPT ~85%, Gemini 7%, Claude 3% [Turley; RDX0355].
  - Google's estimate of daily queries as of Mar. 28, 2025: ChatGPT 1.2B, Meta AI >200M, Gemini ~140M, Grok 75M, DeepSeek 50M, Perplexity 30M [Hsiao; RDXD-04.008].
- **Impact on search (FOF ¶¶63–71).**
  - Safari's Google query volume declined "for the first time in 22 years perhaps due to" GenAI [Cue]. But GenAI "ha[s] not eliminated the need for GSEs".
  - The Gemini app is not diverting queries from Search to a significant degree [Hsiao].
  - AI Overviews "has potentially strengthened Google's position".
  - Navigational and commercial queries are not yet GenAI use cases [Shevelenko, Hsiao, Cue]. Firms expect to move into commercial queries [Pichai, Cue, Reid].
  - Answering commercial queries would need grounding in a search index or retailer databases [Hsiao].
  - The Gemini app "does not drive much, if any, meaningful traffic to Search" [Hsiao, Hitt].

**Other technical findings in the remedy sections** (from the Remedy-Specific Conclusions of Law):

- **Scale** (op. pp. 89–95).
  - These points come from the liability opinion. Google receives 9× the queries of all rivals combined (19× on mobile). NavBoost's 13 months of data ≈ 17.5 years of Bing's. Of 3.7M unique phrases over 7 days, 93% were seen only by Google and 4.8% only by Bing [Whinston].
  - Long-tail queries are ~⅓ of volume and 90% of distinct queries [UPX1079].
  - Turley: "a bit more than half of what our users want to do in ChatGPT relies on long-tail queries."
- **Ranking and index** (op. pp. 137–144).
  - Signals range from raw counts (Navboost) to deep-learning models (RankEmbedBERT) [Allan].
  - Quality signals are mostly page-derived. PageRank is "a single signal relating to distance from a known good source" [Allan; PXR0356].
  - The popularity signal P\* "uses Chrome data" and anchors. How far it rests on user data was not proved.
  - De-duplication cuts 1 trillion extracted links to ~100 billion processed [RDX0062].
  - The "80–20 problem": an index that answers 80% of queries is attainable; the long-tail 20% is hard [Weinberg, Turley].
- **Glue, RankEmbed, MAGIT** (op. pp. 153–155).
  - Glue is a "super query log" (query, SERP composition, clicks, hovers, dwell time, query interpretation) [Allan]. Navboost is a "memorization system", "just a giant table" [Lehman, liability trial].
  - RankEmbed/RankEmbedBERT is trained on a redacted % of 70 days of search logs plus human-rater scores [Nayak, liability trial]. It is "trained on 1/100th of the data used to train earlier ranking models yet provides higher quality search results" [Lehman, liability trial]. It helped especially with long-tail queries [Nayak].
  - **Google does not use click-and-query data to pre-train base Gemini models**. It considered doing so and judged the benefit not worth the cost [Collins]. Microsoft and OpenAI witnesses said the same of their own base models (as cited in Google's proposed findings ¶985).
  - The Search team post-trains Gemini. MAGIT is a generator model fine-tuned for AI Overviews formatting and trained on unspecified "Search data" [Durrett citing Parakh dep.].
- **Privacy** (op. pp. 161–164). Both privacy experts agreed that raw query logs can re-identify users without explicit personal identifiers [Evans, Culnane]. Both also agreed that noise, generalization and k-anonymity can protect privacy while keeping some utility. Evans cited Google's disclosures under the EU Digital Markets Act, where privacy filtering excluded 99% of queries.
- **Publishers** (op. pp. 203–205). Google-Extended lets publishers opt out of training Google's foundation models and of grounding for the Gemini app and Vertex AI. It does not let them opt out of fine-tuning of Search models or of display in AI Overviews, except by blocking crawling altogether [Reid].

## Claims

Strength rates the record behind each finding. The categories are: testimony (fact witness), expert evidence, documents (party exhibits), concession, liability-phase finding (carried forward from the 2024 opinion), or the court's own inference.

| id | claim | strength | support |
|---|---|---|---|
| C1 | Language modeling is next-token prediction, and most LLMs are transformers with billions of parameters. | expert evidence (single expert, lay-level) | FOF ¶¶3, 5, 27 (Durrett, plaintiffs' expert; Collins and Pichai on the 2017 origin) |
| C2 | LLMs cannot answer factually about data absent from training, are weaker on rare facts, cannot store information losslessly, have knowledge cutoffs (retraining "weeks or months"), and hallucinate. | expert evidence and testimony | FOF ¶¶32–35 (Durrett; Turley and Schechter on hallucination) |
| C3 | Grounding/RAG reduces hallucination, improves factuality and solves recency, though it "does not fully eliminate the problem of hallucinations". | expert evidence, testimony and documents | FOF ¶¶36–40 (Durrett, Allan, Collins, Reid; PXR0040, PXR0105); caveat at op. p. 139 |
| C4 | Grounding quality depends on the quality of the search index and API. | testimony | FOF ¶43 (Turley, Schechter, Cromwell dep.) |
| C5 | Chatbots "perform an information-retrieval function like that performed by GSEs", which brings GenAI within the remedy. | court's inference from testimony and demonstratives | FOF ¶14; COL §IV (op. pp. 99–103) |
| C6 | GenAI chatbots have not replaced search. Their functionality only partially overlaps. | testimony and documents, plus a concession by plaintiffs' counsel | FOF ¶¶13, 17, 63, 65 (Pichai, Reid, Hsiao; PXR0176; Rem. Tr. 21:2-5) |
| C7 | GenAI "may be having some impact" on search usage. Safari's Google queries fell for the first time in 22 years. | testimony (single witness; causation hedged "perhaps" in FOF ¶63 and "likely" at op. p. 100) | FOF ¶63; op. p. 100 (Cue) |
| C8 | The GenAI market is "highly competitive", with frequent entry and leapfrogging, and Google's models have no distinct advantage in factuality or benchmarks. | testimony and expert evidence (largely Google's own witnesses and expert) | FOF ¶¶56–59 (Turley, Collins, Hsiao, Hitt RDXD-32.015–.016) |
| C9 | U.S. share in Dec. 2024: ChatGPT ~85%, Gemini 7%, Claude 3%. Daily queries on Mar. 28, 2025: ChatGPT 1.2B, Gemini ~140M. | documents (each party's internal estimate) | FOF ¶60 (RDX0355, OpenAI; RDXD-04.008, Google) |
| C10 | Google declined OpenAI's request for a grounding partnership. Third parties can ground only through Vertex AI, without the ranked results. | testimony and documents | FOF ¶¶45, 52 (Turley, PXR0181; Reid, PXR0153) |
| C11 | Google does not pre-train base Gemini models on click-and-query data. | testimony (single Google witness) | op. pp. 154–155 (Collins) |
| C12 | Plaintiffs did not establish that Google's search scale gives its GenAI products a quality advantage, so GenAI training data is not shared. | court's finding that the evidence fell short (the "logical implication" testimony was held insufficient) | op. p. 156 (Durrett 216–218; FOF ¶¶56–62) |
| C13 | Exclusive distribution produced a scale advantage (9×/19× queries; 93% vs 4.8% unique phrases; 13 months ≈ 17.5 Bing-years) that is a "fruit" of the violation. | liability-phase findings plus the court's inference | COL §III.B (op. pp. 89–95) |
| C14 | RankEmbed(BERT) was trained on 1/100th the data of earlier ranking models, gave higher quality, and helped especially on the long tail. | testimony (liability-phase, Google witnesses) | op. pp. 154, 158 (Lehman, Nayak) |
| C15 | Most of Google's quality signal comes from the page itself (e.g., PageRank). The extent of user-data input into popularity and spam signals is unproven. | expert evidence, with gaps the court acknowledges | op. pp. 143–144, fn. 17 (Allan; PXR0171, PXR0356) |
| C16 | Sharing raw Glue and RankEmbed data will not let rivals clone Google Search. Allan's "mimic" opinion concerned improvement, not parity. | expert evidence (Google's expert, qualified on cross-examination) plus the court's inference | op. pp. 159–163 (Allan 2946–2952) |
| C17 | User logs can be de-identified with noise, generalization and k-anonymity, at a cost to utility (the DMA example lost 99% of queries). | expert evidence (both sides agree) | op. pp. 161–164 (Evans, Culnane) |
| C18 | An index answering ~80% of queries is attainable quickly. The long tail is the hard part. The 40% first-year syndication cap follows Allcott et al.'s finding that 38.7% of Bing desktop searches are rare. | testimony plus an academic study; the court concedes the long-tail cutoff is unclear | op. pp. 139–140, 176–177 (Weinberg, Turley, Shevelenko; Allcott et al., NBER WP 33410) |
| C19 | Default bias and choice friction hold users to Google. Of users paid to switch to Bing for 14 days, 33% kept Bing and 64% found it better than expected. | liability findings plus an academic field experiment | op. pp. 83–85 (Allcott et al.; Luca, Rangel) |
| C20 | A payment ban would harm distributors and consumers. With Google data, Bing desktop CTR would rise only from 23.5% to 24.8%, a ~1% share shift that the authors call "more speculative". | testimony, economic expert evidence and an academic model | op. pp. 121–127, fn. 15 (Cue, Kim, Laflamme, Muhlheim, Murphy, Chipty; Allcott et al.) |
| C21 | Plaintiffs' expert's 31% share-shift estimate for a payment ban is "too speculative". | the court's own assessment of expert evidence | fn. 11, op. p. 120 (Chipty) |
| C22 | Choice screens barely move share: <1% [Whinston]; EU 0.5–1.5% [study cited by Rangel]; −1.3 pp and +$0.07 consumer surplus in the Allcott model. | expert evidence plus an academic study | op. pp. 190–191 |
| C23 | GenAI firms are "in a better position, both financially and technologically, to compete with Google than any traditional search company has been in decades (except perhaps Microsoft)". | court's inference | op. p. 128 (from FOF ¶¶56–66) |
| C24 | "AI has unquestionably improved general search, but it has not yet fundamentally altered market dynamics." | court's inference from market evidence (Bing gained no share after AI integration; Neeva's exit) | op. pp. 109–110 |

## Concepts

- **Grounding** — "anchoring the output of a model on factual information or [an] external database" (Collins, FOF ¶37). The court treats it as the mechanism that makes a search index an input to GenAI.
- **RAG** — "[t]he process of accessing additional knowledge through a kind of information retrieval" (Durrett). A grounding technique, and "sometimes used interchangeably" with grounding (FOF ¶37).
- **FastSearch** — Google's grounding retrieval. Abbreviated ranked web results based on RankEmbed signals (FOF ¶44; op. p. 179 says "derived primarily from the RankEmbed model"). Faster and lower in quality than Search. Offered to others only through Vertex AI.
- **Scale** — "[g]reater query volume" that translates to "more user data" (op. p. 150, quoting the liability opinion). This is the fruit the data remedies target.
- **User-side Data** — data obtained from users "directly through a search engine's interaction with the user's Device", explicitly including data used to train ranking, retrieval and GenAI models "at all stages of training including pre-training and filtering, post-training, fine-tuning" (plaintiffs' definition, op. pp. 151–152). In practice this means click-and-query data.
- **Glue** — "super query log" of query, SERP and interaction data. **Navboost** — a "memorization system" over click-and-query data (op. p. 153).
- **Qualified Competitor** — a Competitor, now including a provider of "a GenAI Product in the United States". It must meet data-security standards, accept audits, show "a plan to invest and compete in or with the GSE and/or Search Text Ads markets", and pose no national-security risk (op. pp. 103–104).
- **80–20 problem** — industry term used in testimony. An index covering 80% of queries is quick to build; the long-tail 20% is hard (op. p. 139).
- **Fruits** — market advantages produced by the violation. They need not be quantified or be "attributable entirely" to it (op. pp. 97–98).

## Connections

The opinion builds on the court's liability opinion, *United States v. Google LLC*, 747 F. Supp. 3d 1 (D.D.C. 2024). Many of its scale and default findings are carried forward from there. Its legal spine is the Microsoft line:

- *Microsoft III* (D.C. Cir. 2001 en banc);
- *New York v. Microsoft* (D.D.C. 2002), for sliding-scale causation and for extending remedies to "new technologies";
- *Massachusetts v. Microsoft* (D.C. Cir. 2004), which upheld compelled API disclosure and rejected the open-source Internet Explorer remedy.

The court distinguishes Google's data remedy from that rejected open-source IE remedy on three grounds: it is tied to the liability theory, it benefits competition rather than particular competitors, and it is not a de facto divestiture. For data or catalog sharing as a remedy in network-effects markets, it leans on *In re Google Play Store Antitrust Litigation* (9th Cir. July 31, 2025) and on the Areeda & Hovenkamp treatise's "pooling" discussion (¶653i2). Its empirical anchors outside the record are Allcott et al., "Sources of Market Power in Web Search: Evidence from a Field Experiment" (NBER WP 33410, 2025), and Hovenkamp's articles on platform remedies.

## Bearing on the record

Nothing here is an instruction for ML practice, and nothing belongs in the Anthology of the SOTA as a practice. The LLM findings (FOF ¶¶27–46) restate expert testimony at an introductory level. The court's own heading is "Greatly Simplified". They add no evidence on any technique beyond what the cited witnesses asserted.

What the record could usefully cite from this opinion is a small set of sworn industry statements, each resting on one or two witnesses, and each marked in the opinion as testimony rather than as a finding established by measurement:

- Google does not pre-train base Gemini models on click-and-query data (Collins).
- RankEmbed reached higher quality on 1/100th of the training data (Lehman, 2023 liability trial).
- Frontier labs build their own search indexes because third-party search APIs were inadequate for grounding (Turley).
- The "80–20" index-coverage heuristic (Weinberg, Turley).

It is also a documented instance of a court finding **no proof** that search-log scale confers an LLM quality advantage (op. p. 156). Anyone citing it for "search data is a moat for LLMs" would be citing it for the opposite of what it holds. Any THEORY on grounding/RAG as a remedy for hallucination and recency could cite FOF ¶¶36–40 only as a description of the testimony, not as support.

## Limitations

- **Technical findings are thin by design.** The court says the Findings of Fact "are therefore far less extensive and detailed" than the liability findings (op. p. 16). It disclaims expertise: it "has no expertise in ... the engineering of GenAI technologies" (op. p. 2). Several characterizations are loose. The clearest is the transformer described as a model that "attempts to mimic the way the human brain works" (FOF ¶5). Another is "without human supervision", used about next-token completion (FOF ¶27).
- **Single-source findings.** Many GenAI findings rest on one witness. The benchmark-parity finding (FOF ¶59) rests on Google's own expert (Hitt), and plaintiffs' expert declined to opine. The share numbers (FOF ¶60) are each party's internal estimates.
- **Redactions** hide load-bearing numbers: Docjoins' size relative to Common Crawl, the share of queries triggering AI Overviews, and RankEmbed's share of the logs.
- **Hedging inconsistency.** Cue's Safari decline is attributed to GenAI "perhaps" (FOF ¶63) and "likely" (op. p. 100).
- **Plaintiffs' proof gaps shaped the remedy.** The court repeatedly declined remedies for want of evidence rather than on the merits. Examples are popularity signals (op. pp. 143–144), GenAI training data (op. p. 156), synthetic queries (op. pp. 178–179), publisher opt-out (op. pp. 205–206), and a Vertex-access remedy that plaintiffs never requested (op. p. 179). None of these is a finding that such sharing would be ineffective.
- **Key parameters are left open.** The disclosure cap, the privacy treatment, the syndication taper and Qualified Competitor criteria are delegated to the Technical Committee and the final judgment. So the actual scope of data sharing cannot be read from this opinion. The final judgment and any appeal are unverified here.
- It is a district-court opinion, not appellate precedent. The court says it is "prepared to revisit a payment ban" (op. p. 128).

## Open questions

- Does Google's search scale translate into better grounded GenAI answers? The court found the record silent. Closing the question would take a comparison of RAG quality holding the model fixed and varying the index or log scale. The only testimony on the point is Durrett's untested "logical implication" (op. p. 156).
- How much utility survives privacy treatment of Glue and RankEmbed data? The Digital Markets Act precedent suggests heavy loss (99% of queries excluded). The answer is left to the Technical Committee.
- Will GenAI firms qualify as "Qualified Competitors" and use the index snapshot and syndication? Cue testified that GenAI firms are "very good at their LLMs" and "have to get better at the search index part" (op. p. 140). Whether the remedy speeds that up is the test of its design.
- Grounding access through Vertex AI or FastSearch was left outside the decree because plaintiffs did not request it. Whether denial of grounding access to rivals becomes a live issue is open.

## Corrections to the seeded skim

- Date: the dossier gives `published: 2025-09-01`. The opinion is dated and filed September 2, 2025 (signature block op. p. 223; ECF header "Filed 09/02/25").
- The dossier summary leaves out the scope and limits of the data remedy, which the full text makes central. Search Index sharing is a one-time snapshot of six fields: DocID with a duplicates notation, DocID→URL map, first-seen time, last-crawl time, spam score and device-type flag (op. p. 144). The popularity (Navboost/Glue) and quality/authoritativeness signals the plaintiffs asked for were refused, and so was the Knowledge Graph (op. pp. 142–151). User-side data covers only the data underlying Glue and RankEmbed (not models, signals, salient terms or human-rater scores). It is disclosed "at least twice", under a cap to be set with the Technical Committee (op. pp. 157–158). Sharing of GenAI/Gemini training data was expressly rejected (op. p. 156). Ads data was rejected (op. pp. 164–168).
- Syndication is not simply "on largely ordinary commercial terms". The court cut plaintiffs' 10-year marginal-cost license to 5 years, at "financial terms no worse than those offered to any other user". It capped first-year use at 40% of annual queries, with a Technical-Committee taper to follow. It struck synthetic queries and FastSearch results, the latter being Google's LLM-grounding feed (op. pp. 171–179).
- The Cue "22 years" point is hedged differently in two places. In FOF ¶63 the court says Safari query volume fell "perhaps due to" GenAI chatbots. In COL §IV (op. p. 100) it says "likely due to". The dossier reports only the second form.
- The GenAI findings run from op. p. 17 to p. 46 (through "GenAI's Impact on GSE Usage"), not pp. 17–36. The grounding findings are FOF ¶¶36–46 (op. pp. 32–36). The market findings are FOF ¶¶47–66 (op. pp. 36–46).
- The dossier's framing that the grounding findings are "directly relevant to ML practice" goes further than the text. The court's own heading is "How LLMs Work (Greatly Simplified)". The findings restate expert and executive testimony at a lay level, and the court decides nothing about technical questions (see Limitations).
