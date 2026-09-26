---
number: 58
status: Read
formerly:
- NOTE-tmphwo5s
paper: LIT-072
title: 'Iranian NEWSCASTER social-media espionage (SecurityWeek, 2014)'
version: 2
history:
- version: 2
  date: '2026-09-25'
  note: >-
    Read in full (Full text of the SecurityWeek article by Mike Lennon (29
    May 2014; article:published_time 2014-05-29T12:58:23Z), about 1,000
    words, read end to end. The article's embedded image listing "some of
    the accounts/fake personas" did not come through as text, and the linked
    podcast was not heard. I also read, as a check on the article's
    sourcing, iSIGHT Partners' own public disclosure: "NEWSCASTER – An
    Iranian Threat Inside Social Media", a blog FAQ by Stephen Ward dated 28
    May 2014, reached as a PDF capture at cyber-peace.org, 7 pp. I did not
    reach the full iSIGHT report. The blog says it was "available upon
    request by registering".). Upgraded from `Skimmed` to `Read`: the claims
    table, assumptions and results are new, and the skim is corrected where
    the full text disagreed.
date: '2026-09-25'
summary: >-
  SecurityWeek relays iSIGHT Partners' claim that more than a dozen fake
  personas, supported by a fake news site (NewsOnAir.org), ran a
  social-media espionage campaign from 2011 aimed at US military,
  diplomatic, congressional, press, think-tank and defence targets. The
  purpose was credential phishing and reconnaissance. Iranian origin is
  inferred from targeting, "technical indicators" and a Tehran working-day
  schedule, and iSIGHT says it has "no information implicating the
  ultimate sponsor". The article's figure of "over 2,000" is connections
  to the personas, not confirmed victims. iSIGHT itself says it is "not
  clear ... how many credentials the attack has captured".
---

# NOTE-058: Iranian NEWSCASTER social-media espionage (SecurityWeek, 2014)

## Contribution

It is a trade-press news report, published the day after iSIGHT's disclosure. That disclosure named NEWSCASTER, a persona-based social-engineering espionage campaign. The article's own additions are an interview with iSIGHT's Stephen Ward, three industry comments (Michael Sutton of Zscaler, Anup Ghosh of Invincea, James C. Foster of ZeroFOX) and a link to a FireEye report from the same month. Everything factual about the campaign comes from iSIGHT.

## Key insight

The campaign made up for weak technical capability with patience and credibility on social platforms. The personas built trust by connecting with targets and their contacts ("connected, linked, followed, and 'friended'"), then turned that trust into credential phishing and reconnaissance. Ward likens the approach to improvised explosive devices: "low cost ... but is very effective".

## Assumptions

These are premises and authorities.
- The sole authority for the campaign's existence, scope and attribution is iSIGHT Partners, a commercial threat-intelligence vendor. Its methods are undisclosed ("We are protective of sources and methods").
- Attribution rests on three kinds of evidence: (a) an activity schedule matching Tehran working hours, "a lengthy lunch break", half-day Thursdays and little Friday activity; (b) target selection; (c) unspecified "additional technical indicators".
- iSIGHT coordinated with the FBI and notified Facebook, LinkedIn and others. Ward says the personas were removed from Facebook and LinkedIn. Neither platform is quoted.

## Key results

What the article reports, attributed:
- (iSIGHT) Active "since 2011". More than a dozen fake personas on Facebook, Twitter, LinkedIn, Google+, YouTube and Blogger, including "at least two (falsified) legitimate identities from leading news organizations" and "young, attractive women", supported by the fictitious outlet NewsOnAir.org. The source blog adds that the site "plagiarizes news content from other legitimate media outlets", and that newsonair.com (a legitimate Indian outlet) is unrelated.
- (iSIGHT) Targets: senior US military and diplomatic personnel, congressional staff, DC journalists, US think tanks, and defence contractors in the US and Israel. Others were in the UK, Saudi Arabia and Iraq, plus vocal supporters of Israel.
- (Ward) "Largely this campaign was about credential harvesting and recon". Connections were used as "springboards" to corporate and personal email.
- (iSIGHT) Malware was used. It was "not particularly sophisticated" but capable of exfiltration.
- (iSIGHT) There is "no direct information" that the Iranian government is the sponsor. The operators are believed to be in Iran.
- (Sutton, Ghosh, Foster) General commentary: social media is outside organisational control; password reuse; "every major foreign adversary is leveraging social media".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | A persona-based espionage campaign ran across six platforms from 2011 | vendor assertion, relayed | iSIGHT disclosure; no independent confirmation in the article; the personas' removal is reported by iSIGHT, not by the platforms |
| C2 | Over 2,000 individuals were "connected or victimized" | vendor assertion; the article's wording overstates the source | the source says ≥2,000 connected to personas; the number of credentials captured is unknown |
| C3 | The operators are located in Iran | vendor inference from circumstantial evidence | working-hours pattern, targeting, undisclosed "technical indicators" |
| C4 | The Iranian government sponsored it | not claimed | iSIGHT: "no direct information"; the headline implies more than the body |
| C5 | Its purpose was credential harvesting and reconnaissance | vendor assertion plus a spokesperson interview | Ward, quoted |
| C6 | The approach is effective despite low sophistication | assertion | iSIGHT and commentators; no measure of success given |

## Concepts

- **NEWSCASTER**: iSIGHT's name for the campaign, taken from its fake-news-site cover.
- **persona**: a fabricated or misappropriated social-network identity (fake journalist, government or defence employee, or "attractive women") used to build trust networks with targets.
- **credential harvesting**: sending links to fake login pages to capture passwords, which are then reused against other accounts.

## Connections

The article is secondary to iSIGHT's disclosure of 28 May 2014, from which the quoted material is taken. It links a FireEye report from about two weeks earlier on the maturing of Iranian APT methods. Later reporting and industry naming (e.g., the Wikipedia entry "Operation Newscaster", surfaced by search; not read) connect the campaign to Iranian threat groups tracked under other names. I have not verified that link. The technique is an early, well-documented case of the fake-persona social engineering that later reporting describes being scaled with generative models.

## Bearing on the record

It carries nothing for ML practice. There are no models, data or methods in it. It could serve as historical background for a document on influence or espionage operations that use synthetic personas. For that, the iSIGHT disclosure is the better citation, with the caveat that it is a vendor's unaudited account. It carries no instruction for the Anthology of the SOTA.

## Limitations

- It has a single source: a commercial vendor that had a report to promote. Its closing section advertises its own services, and it gave a spokesperson who is its marketing director (Ward's title in the article: "Senior Director of Marketing").
- The attribution evidence is circumstantial, and partly undisclosed.
- The effectiveness claims are unquantified. Neither the number of compromised credentials nor the data taken is known ("We are unable to say with complete visibility").
- The headline states as fact what the body gives as an inference.

## Open questions

- How many accounts were actually compromised, and what was taken? Only the full iSIGHT report, or a government or platform account, could say.
- Did later government or academic work confirm the attribution and the actor's identity? Unverified here.

## Corrections to the seeded skim

- The dossier says the personas "befriended more than 2,000 people". The article says the operation was "successful in connecting or victimizing over 2,000 individuals". The source says "At least 2,000 people/targets are, or have been, caught in the snare and are connected to the false personas", and separately "It is not clear at this time how many credentials the attack has captured to date." The 2,000 counts connections. Neither the article nor the dossier should be read as 2,000 compromises.
- The dossier (and the article: "the closely held report said") present the quoted passages as coming from a closely held report. Every iSIGHT passage the article quotes appears verbatim in iSIGHT's public blog FAQ of 28 May 2014, including the working-hours attribution, "brazen, complex multi-year cyber-espionage", and "We are protective of sources and methods". The article prints that last one without attribution. So the article's sourcing is reachable, and the dossier's note that the primary report was "not reached" overstates the gap.
- Missing from the dossier: the article adds targets in the UK, Saudi Arabia and Iraq, and "vocal supporters of Israel", and places the report two weeks after a FireEye report on Iranian APT development. Both points are in the text.
- The dossier's summary says iSIGHT "believes [it was] run from Iran". That is accurate, but the headline ("Iranian Hackers Targeted US Officials") and the lede ("Iranian threat actors") state the attribution without hedging. The body's own hedge ("no direct information showing that the Iranian government is the ultimate sponsor") appears only under "Attribution to Iran".
