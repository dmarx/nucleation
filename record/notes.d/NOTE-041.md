---
number: 41
status: Read
formerly:
- NOTE-tmp9kcii
paper: LIT-033
title: 'Doctorow, "Disenshittify or die!" (DEF CON 32)'
version: 2
history:
- version: 2
  date: '2026-09-25'
  note: >-
    Read in full (Full text of the author's own "lightly edited version of
    my speech crib". It was posted on Pluralistic on 17 Aug 2024 as
    "Disenshittify or Die" (pluralistic.net/2024/08/17/hack-the-planet/,
    about 8,200 words, every paragraph from "What the fuck happened to the
    old, good internet?" to the closing line). I skipped the unrelated
    sections of that day's newsletter ("Hey look at this", "This day in
    history", appearances, books, colophon). I did not watch the delivered
    talk. The YouTube video (4EmstuO0Em8) returned HTTP 429 to the seed, and
    I did not retry it. Doctorow says the video "hasn't yet been posted", so
    he published the crib in its place. Everything below describes his text,
    and the delivered talk may differ from it. Under the brief's rule for
    talks this counts as a read, because the text is the speaker's own.
    Legal and factual assertions that I checked, or that I could date from
    general knowledge, are marked as such. The rest are the author's
    assertions and are unverified.). Upgraded from `Skimmed` to `Read`: the
    claims table, assumptions and results are new, and the skim is corrected
    where the full text disagreed.
date: '2026-09-25'
summary: >-
  Doctorow argues that platforms follow a three-stage decay cycle: good to
  users while locking them in, then good to business customers at users'
  expense, then taking all the value for themselves. The mechanism is
  "twiddling". It became possible when four disciplining forces weakened:
  competition, regulation, interoperability and tech-worker power. A "new,
  good internet" needs all four restored, with interop
  (reverse-engineering rights) and unionisation as the hacker-specific
  levers. The argument is assertion and anecdote throughout. It carries
  several checkable factual slips, notably about EU law and the court in
  United States v. Google.
---

# NOTE-041: Doctorow, "Disenshittify or die!" (DEF CON 32)

## Contribution

This is a talk, not research. It adds a causal story to Doctorow's earlier description of enshittification (his 2023 DEF CON talk, which the text links). The story is that tech bosses "were always that guy", and what changed was the environment that kept "the enshittification lever" from moving. He names four forces that used to discipline firms and says why each weakened. The talk then says how an audience of hackers can help restore each one.

## Key insight

The talk puts the cause of platform decay in lost constraints, not in any change in managers' character. In the text's words: "Not because they used to be better people, but because they used to be subjected to discipline." Because the problem is structural, it is also reversible. "We can make good services out of imperfect people" if competition, regulation, interoperability and worker power are "durably installed".

## Assumptions

These are premises, not formal conditions.
- Firms maximise extraction subject to constraints. "The point of the business was to charge the most, and deliver the least". The author asserts this as a description of all tech bosses.
- Digital platforms can be re-priced and re-ranked at near-zero cost ("a twiddler's utopia"). This is what makes the cycle fast.
- General-purpose computers make any "enshittificatory alteration" reversible by another program, unless the law forbids it. Doctorow grounds interop in Turing-completeness. The legal barriers he treats as decisive are DMCA §1201, the CFAA, tortious interference, and trademark, copyright and patent.
- Worker leverage came from scarcity, not from organisation. Once layoffs arrived, only a union is a durable source of power.
- Authorities invoked: Veena Dubal ("algorithmic wage discrimination"); Emily Baker-White in Forbes (the TikTok "heating tool"); Fobazi Ettarh ("vocational awe"); Jay Freeman ("Felony Contempt of Business Model"); Judge Amit Mehta's opinion in United States v. Google.

## Key results

What the talk argues:
- **The cycle.** Stage 1 is being good to end users and locking them in (Stage "1a"). Lock-in mechanisms: network effects and the collective-action problem; prepayment (Prime, Audible); DRM (HP ink); and Apple's "grab bag" of parts pairing and engraved-logo customs seizures. Stage 2 shifts value to business customers (Google ad labelling, Amazon search ads, the Facebook feed). Stage 3 is "screw everybody".
- **Against "you're the product".** Paying business customers are squeezed too. His examples: Amazon sellers paying "between 45 and 51%" of revenue, and the "most favored nation" clause pushing prices up everywhere; Apple's ATT opt-out alongside its own ad targeting; John Deere repair unlock codes.
- **Twiddling** is "when someone alters the back end of a service to change how its business operates". Examples: Plexure payday pricing, Norwegian e-ink shelf tags changing "2,000 times per day", Uber per-driver pay, YouTube downranking, and TikTok's "heating tool", which he likens to a carnival's "giant teddy bear".
- **Four forces, each removed.** (1) Competition: 40 years of permissive antitrust; Facebook–Instagram; Google's default payments ("more than 20 billion per year to Apple alone"). (2) Regulation: regulatory capture by cartels; "we do it with an app"; the Video Privacy Protection Act (1988) as the last federal consumer privacy law. (3) Interoperability: blocked by DMCA §1201 ("5-year prison sentence and a $500k fine for a first offense"), the CFAA and IP law. Hence "no one's ever installed a tracker-blocker for an app", and his product-meeting parable (web ads 20% worse vs app ads 100% worse). (4) Tech workers: "Tech laid off 260,000 of us last year, and another 100,000 in the first half of this year."
- **Remedies.** An antitrust revival ("more antitrust action over the past four years than over the preceding forty years", across the US, UK, EU, Australia, Canada, Japan, South Korea and China). The DMA's interop mandate. A federal privacy law with a private right of action. State right-to-repair bills. A tech-worker union.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Platforms decay in three stages (users → business customers → shareholders), each preceded by lock-in | assertion with anecdote | illustrative company examples; no systematic evidence |
| C2 | The decay is caused by weakened constraints (competition, regulation, interop, worker power), not by changed management | informal argument | historical narrative (Myspace, Yahoo, LiveJournal "died"); no comparison across firms or periods |
| C3 | Amazon's first search result is on average 29% more expensive than the best match; the best match averages 17 places down; ad revenue is $38b/yr | assertion (figures stated without citation in the text) | none given in the text; unverified here |
| C4 | Independent Amazon sellers pay 45–51% of each dollar to Amazon | assertion | none given; unverified |
| C5 | DMCA §1201 carries a 5-year sentence and a $500k fine for a first offence | assertion; broadly consistent with 17 U.S.C. §1204's criminal penalties for wilful violations for commercial gain, which is narrower than "reverse engineering an app" | statute not quoted; the qualifier is missing |
| C6 | Judge Mehta, "ruling for the DC Circuit", found Google a monopolist in docket 20-3010 | the quote is accurate, but the court is misstated | Mehta sits on the US District Court for D.C. (No. 1:20-cv-03010), not the D.C. Circuit |
| C7 | The DMA is an "Act", not a "Regulation", so it bypasses national transposition and Irish enforcement, unlike the GDPR | wrong on the law (see Limitations) | assertion |
| C8 | Wiz turning down Google's $23b was "the largest acquisition offer in history" | assertion; overstated (it would have been Google's largest acquisition, but far larger acquisitions exist, e.g. Microsoft–Activision) | none |
| C9 | More antitrust action worldwide in 2020–24 than in the preceding 40 years | assertion | none given |
| C10 | Only a union gives tech workers durable power | informal argument | analogy to Amazon warehouse workers |

## Concepts

- **enshittification**: the three-stage platform-decay cycle above. The name covers what it "looks like from the outside".
- **twiddling**: altering a service's back end ("prices, costs, search ranking, recommendation criteria") at low cost and high frequency. The talk calls it the "pathological mechanism" inside the firm.
- **giant teddy bear**: a platform subsidy given to a few visible winners (the TikTok heating tool, early high-earning Uber drivers, Substackers, Rogan's Spotify deal) to recruit many unpaid imitators.
- **interop / adversarial interoperability**: third-party modification or compatible products (ad-blockers, refill kits, battery jailbreaks, Facebook's Myspace scraper bot). The talk treats it as a check on enshittification that IP law has disabled.
- **"we do it with an app"**: the talk's name for the regulatory-capture gambit of claiming that an illegal practice is new because it is software-mediated.

## Connections

It follows directly from Doctorow's 2023 DEF CON 31 talk "An Audacious Plan to Halt the Internet's Enshittification", which the text links. It draws on Dubal's work on algorithmic wage discrimination and on Ettarh's "vocational awe". The fullest later statement of the thesis is presumably Doctorow's 2025 book *Enshittification*. I have not read it, and its relation to this talk is unverified.

## Bearing on the record

Nothing here bears on ML practice. The talk mentions AI only in passing ("AI-generated covers", "AI slop", "AI cameras", "AI deepfake porn"), and nothing in it is a claim about training, evaluation or deployment of models. It carries no instruction for the Anthology of the SOTA. If this record later holds a document on platform governance or interoperability law, this talk is a statement of one advocate's position to be cited as such. It is not evidence for the figures it quotes.

## Limitations

- **The medium.** This is a speech crib, not the talk as delivered, and not an argued essay. Almost every number (C3, C4, the 2,000/day shelf-tag figure, the layoff totals, "96% of users", "at least ten billion dollars") comes without a source in the text. The newsletter form normally links sources, but this crib carries only two links (the DEF CON event page and the 2023 talk).
- **EU law is misdescribed (C7).** The DMA is Regulation (EU) 2022/1925. EU regulations, the GDPR included, are directly applicable and are not "transposed"; directives are. The real difference the talk is gesturing at is enforcement. The GDPR's one-stop-shop mechanism routes cross-border cases through the lead national authority, often Ireland's. The DMA is enforced centrally by the European Commission, with review by the EU courts. There are no "EU federal courts". The talk also expands GDPR as "General Data Privacy Regulation"; it is the General Data Protection Regulation.
- **Court misnamed (C6).** United States v. Google was decided in the District Court, not the D.C. Circuit.
- **Time-sensitivity.** Several "wins" the talk counts were later reversed or narrowed. I know this from general knowledge and did not check it in this reading. The FTC noncompete rule was set aside by a federal court in Texas later in August 2024. The Google remedies decision (2025) did not break the company up. The talk's optimism about antitrust describes August 2024.
- **Unfalsifiable framing.** The causal claim (C2) is never set against a counterfactual. Nothing in the text could show that a firm facing all four forces still decayed.

## Open questions

- Is there systematic evidence (across platforms and over time) that lock-in plus weakened constraint predicts decline in service quality? The talk relies on examples chosen after the fact.
- Which of the four forces carries the most weight? The talk treats them as jointly necessary but gives no way to tell them apart.
- Did the delivered talk differ from the crib? That would take the DEF CON video or a transcript, neither of which was reached.

## Corrections to the seeded skim

- The dossier gives the final line as "restore competition, regulation, interop and tech worker power". That phrase is in the penultimate paragraph, and in full it continues "…so that we can create the new, good internet we'll need to fight fascism, the climate emergency, and genocide". The actual last line is "To build a digital nervous system for a 21st century in which our children can thrive and prosper."
- Missing from the dossier: the prescriptive half of the talk is concrete, not only "fight for interop and unionise". It names the Google search ruling, the FTC noncompete rule, the FTC/DOJ merger guidelines, the EU Digital Markets Act, a US federal privacy law with a private right of action (via EFF's list), state right-to-repair bills (Oregon's 2024 parts-pairing ban, repair.org, iFixit), and the Tech Workers Coalition and Tech Solidarity.
- Missing from the dossier: the text contains factual errors that a skim would not catch (see Limitations). These are errors in the source, not in the dossier. Filing should not repeat them.
- The dossier dates the talk to 2024-08-10 by inference. This is consistent with the text ("Last weekend, I traveled to Las Vegas for Defcon 32", posted Saturday 17 Aug). The text itself gives no date.
