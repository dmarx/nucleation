# scratch/readers/lit-tmpa7f10.md

Running notes (ADR-108). Reader: sweep batch E, 2026-11-22.

## Step 1: copy located and fetched (2026-11-22)

- **Fetched once**: https://osf.io/29jeb/download, 2026-11-22 ~11:34 UTC, one
  GET with curl (generic user agent, no email or other identifier sent).
  Redirect chain: osf.io/29jeb/download -> 301 osf.io/download/29jeb -> 308
  .../29jeb/ -> 302 files.osf.io/v1/resources/29jeb_v1/providers/osfstorage/64f8b4716c0f5a31cad05897
  -> 302 to OSF's object storage (signed URL) -> 200. **No bot check, no
  challenge.** Saved at scratchpad/downloads/sweep-e/LIT-tmpa7f10/law2023-preprint.docx
  (123 KB, Word 2007+). Text extracted with python3 -I (zipfile + XML).
- **File name served**: "CFC, FSC & RFG Manuscript 5-21-24 - Preprint.docx".
  So the file now behind the DOI is a manuscript dated **21 May 2024**, not
  necessarily the text first posted on 6 September 2023 (`published:`).
  The filer should record that the version read is the 2024-05-21 file.
- **Kind (step 5)**: the authors' own preprint on PsyArXiv/OSF (CC BY per the
  LIT's status note). Lawful.
- **Identity check: matches, with an author-order correction.** Title "A
  Future Beyond Ourselves: Can Self-Oriented Prospection Motivate
  Intergenerational Beneficence?" Authors on the file: "*Stylianos
  Syropoulos, *Kyle F. Law, Matthew Coleman, & Liane Young", "* Denotes joint
  first-authorship" (Boston College; University at Albany; Northeastern).
  The LIT (from Europe PMC) lists Law first; this version lists Syropoulos
  first, as joint first author. Abstract matches the LIT's quotation (ten
  studies, N = 11,261 US participants). No page numbers in the docx; sections
  are cited below by heading and study.

## Step 2: read (2026-11-22)

### Provenance
The whole manuscript text read: abstract; introduction (other-oriented
drivers; adaptive function of self-oriented prospection; can it cultivate
concern; potential mechanisms; current research); Table 1 (all ten studies);
Table 2 (measures); Supplementary Studies S1-S3 and Study 1; Study 2 (with
Table 3 and the mediation); S4 summary; Studies 3a and 3b (with Table 4);
internal meta-analysis (Table 5); General Discussion; Implications,
Limitations and Future Directions; Conclusion. References scanned for the
works named below. Not available in the file: the SOM (supplementary
studies' tables S1-S5, pilots S5-S6), Figures 1-2 (path model, bar graph; only
captions), the OSF data. No page numbers exist in the docx.

### Summary
Ten US online studies (MTurk, CloudResearch, Prolific; N = 11,261 by the
abstract) ask whether self-oriented prospection -- Future Self-Continuity
(FSC, Hershfield) and Consideration of Future Consequences (CFC, Strathman) --
goes with concern for future generations: Responsibility for Future
Generations (RFG, Syropoulos et al. 2020) and moral value of future
generations (MFG). Correlational studies (S1, 1, S2, S3, 2, S4) find positive
links; Study 2 adds two proposed mediators, efficacy toward future
generations and "identification with future generations". Two pre-registered
writing-task experiments (3a, N = 1,598; 3b, N = 2,674) manipulate FSC and CFC
(and in 3b efficacy and identification). An internal meta-analysis pools the
correlations.

### Contribution
First joint study of self- and other-oriented prospection; positions FSC as a
possible route to concern for future people through an "expansive sense of
identity that transcends the self and includes future others in one's
self-concept" (Potential Mechanisms), after Wade-Benzoni & Tost 2009.

### Key results
1. Internal meta-analysis (Table 5): CFC-RFG r = .54 (N = 8,608); **FSC-RFG
   r = .21** (N = 7,212); **FSC-identification r = .42**; CFC-identification
   .40; CFC-efficacy .52; FSC-efficacy .16; identification-RFG .54;
   efficacy-RFG .58; FSC-CFC .24.
2. Study 1 (pre-registered, N = 289): CFC r = .49 and FSC r = .30 with RFG;
   both unique in regression (FSC beta = 0.16).
3. Study 2 (N = 345, cross-sectional): "FSC had a non-significant indirect
   effect via efficacy ... but a significant indirect effect via
   identification (b = .11 ...)". The authors add: "no arguments for a causal
   mechanism can be drawn".
4. Study 3a: the FSC writing task raised FSC (d = 0.39) and RFG/MFG (d = 0.24)
   but **not identification with future generations** (d = 0.09, p = .133);
   CFC task likewise raised RFG (d = 0.16) but not the mediators.
5. Study 3b (direct replication): FSC raised (d = 0.41), **RFG not**
   (d = 0.06, p = .288); CFC raised, RFG not (d = 0.0003). The identification
   manipulation (generations "remain the same over time") moved nothing
   (identification d = 0.09, ns). The efficacy manipulation (recalling a
   sacrifice for future people) raised identification (d = 0.14), CFC and RFG
   (d = 0.15) but not efficacy.
6. Authors' summary: "we cannot confidently claim that experimentally
   manipulating any of the target predictors will result in increases in
   responsibility for protecting future people" (3b Discussion); the reverse
   direction "is equally plausible" (Limitations).

### Measures that matter for the record (Table 2, Study 2 Materials)
- **FSC**: Study 1, six items on how "connected" and "similar" one feels to
  oneself 1/5/10 years on; from Study 2 on, the single overlapping-circles
  item (Hershfield et al. 2009), "your connection to your future self, 25 years
  from now".
- **Identification with future generations**: three items: "To what extent do
  you feel connected to future generations of people?"; "It is easy for me to
  put myself in the shoes of future generations of people."; and the same
  overlapping-circles item with "future generations of people" in place of
  the future self (alpha = .89). In 3b only the circles item was used. Table 2
  glosses the construct as: "Does a person living in the present feel
  **empathy** towards future generations of people? Does this person find
  things in common with future generations?"
- **RFG**: four items, e.g. "People living today have an obligation to protect
  future generations, even if it means tightening our belts now"; plus an MFG
  item valuing far-future lives "equally with the lives of people today".

### Assumptions
- Construal Level Theory: temporal and social distance share one cognitive
  architecture, so self-oriented prospection can transfer to others.
- Self-report scales capture the constructs; a writing task can induce them.
- Identification with future generations is a form of self-extension
  ("includes future others in one's self-concept").

### Concepts
self-oriented vs other-oriented prospection; future self-continuity (FSC);
consideration of future consequences (CFC); responsibility for future
generations (RFG); moral value of future generations (MFG); intergenerational
identification; intergenerational efficacy; impartial intergenerational
beneficence (IIBI); construal level theory; present bias / delay discounting;
social generativity; legacy motives (cited, not measured).

### Verdict on the record's characterization
**The abstract-based summary is accurate as far as it goes, but it overstates
the evidence by omission.** (a) The "consistent connection" is correlational;
the two pre-registered experiments give mixed and then null effects of FSC on
RFG (3a d = .24, 3b d = .06 ns), and FSC manipulation never moved
identification. (b) The LIT's open point is answered: **identification with
future generations is not separated from caring** -- its items include
perspective-taking ("put myself in the shoes") and its stated focus is
"empathy towards future generations". Only the overlapping-circles item is a
self-extent measure in form, and its link to FSC (r = .42) may be inflated by
the identical item format. (c) Author order: this version lists Syropoulos and
Law as joint first authors, Syropoulos first. (d) The file is the
2024-05-21 manuscript. (e) Sample totals disagree inside the text (11,261 in
the abstract; "NTotal = 9570" in Limitations; Table 1 sums to 11,261).

### Bearing on codes
- **LEAD-062 / CASE-tmp413kq** (a study measuring the self's extent apart from
  caring, testing whether concern follows): **not the test.** Its "self's
  extent" toward future people (identification) mixes connection, empathy
  and overlap; no caring measure is held apart from it; nothing varies whether
  anyone will know. It does supply (i) an off-the-shelf overlapping-circles
  item for "future generations of people" that CASE-tmp413kq could use as its
  continuity measure (as the authors did alone in 3b), and (ii) two
  manipulations that failed as identification inductions -- a warning for the
  case's salience arm.
- **CLAIM-492** (the self thesis needs a criterion of the self's extent that
  can come apart from caring): consistent with it, and an instance of the
  problem: the paper operationalizes self-extension partly *by* empathy, so
  its identification-RFG link (r = .54) cannot test the thesis. The cleanest
  datum for the claim is experimental: raising continuity with one's own
  future self (FSC d about .4) did not reliably raise concern for future people
  (3b null), nor identification with them (3a, 3b null).
- **QUESTION-301** (legacy as self-interest on a temporally extended self;
  Hershfield's offspring bridge, NOTE-1259): weak support at most. FSC goes
  with RFG at r = .21 cross-study; causally, mixed to null. Neither legacy,
  offspring nor being remembered is measured (legacy is cited only as prior
  work: Zaval et al. 2015, Bang et al. 2017). With LIT-tmpre45d's reported
  ordering (concern before continuity), the prudence-to-legacy bridge is not
  shown.
- **QUESTION-299** (what is owed to far-future people, and on what ground):
  descriptive only; the RFG and MFG items measure felt obligation and
  impartial valuation, not its ground. The note's line "links future-self
  continuity to responsibility" stands, qualified as correlational.
- **QUESTION-300** (motivation aimed at another's good and no self's): no
  direct bearing; the paper treats identification as a mechanism but cannot
  say whether concern for future people is self-interested; efficacy, a
  non-self route, predicts RFG as strongly (r = .58) as identification.

### Limitations and gaps
- All but two studies cross-sectional; mediation (Study 2) is cross-sectional
  and the authors disclaim causal inference.
- Shared method: identification's circles item copies the FSC item's format.
- Construct overlap: identification measured partly by empathy and
  perspective-taking; RFG and MFG averaged in 3a "given the strong
  correlation" (r = .64).
- Writing-task manipulations are weak (d about .1-.4); 3a's effects did not
  replicate in 3b.
- US online samples only; no behaviour measured, only attitudes.
- Manuscript inconsistencies: studies cited by stale numbers ("Study 4",
  "Study 5", "Study 3's cross-sectional findings"), Study 1 sample source
  (MTurk in text, CloudResearch in Table 1), total N. A filer should treat
  section-level citations, not study numbers, as stable.
- Gap: the step from FSC to "an expansive sense of identity that transcends
  self-boundaries" is proposed, not shown: FSC manipulations did not move
  identification.

### Candidate THEORY sentence
"Across ten US studies, Syropoulos, Law, Coleman and Young find that continuity
with one's own future self and consideration of one's own future
consequences correlate with felt responsibility for future generations
(meta-analytic r = .21 and .54), partly through identification with and
efficacy toward future generations, but writing tasks that raised
future-self continuity raised responsibility in one pre-registered
experiment and not in its replication, and never raised identification, so
the self-to-others route is shown as association, not cause."
- promote_when: a study manipulates or measures continuity with future
  people apart from empathy or caring and finds concern follows it; or the
  longitudinal follow-up (LIT-tmpre45d) is read and confirms or reverses the
  direction.

## Step 3: recheck of the record (2026-11-22, worktree at staging)

Searched record/ for: future self-continuity / self-continuity; Hershfield;
consideration of future consequences; Syropoulos; Wade-Benzoni; construal
level; inclusion of other in self / IOS / overlapping circles; longtermism;
generativity; Zaval / "How Will I Be Remembered"; impartial
intergenerational beneficence; Parfit.

- **Held, missed by the first search** (the LIT and LEAD-062 note name none):
  - **LIT-1713 / NOTE-1293 / THEORY-1579** (Syropoulos et al. 2023,
    "Responsibility to Future Generations: A Moral Reframing Strategy";
    Active): the same group's RFG work; THEORY-1579 reports RFG widely
    endorsed and nearly unrelated to ideology. The RFG scale used here is
    Syropoulos et al. 2020 (check whether that is LIT-1741 or another).
  - **LIT-1741** (Syropoulos & Markowitz 2021, perceived responsibility
    towards future generations; Unavailable): S1 reanalyses this group's
    earlier data (Syropoulos et al. 2020; Syropoulos & Markowitz 2021).
  - **LIT-1702 / NOTE-1259** (Hershfield 2011, FSC; Active): the source of the
    FSC construct and measure, and of the offspring guess QUESTION-301 cites.
  - **LIT-1724** (Zaval et al. 2015, legacy; Unavailable) and **LIT-1750 /
    NOTE-1316** (place and legacy framing): the legacy literature this paper
    cites but does not test.
  - **NOTE-1274** ("Empirical Approaches to Altruism"): doubts what the IOS
    scale measures ("It is far from clear what the other two tests [IOS and
    use of 'we'] are measuring", l. 55-56). Directly relevant: this paper's
    identification item in 3b is an IOS-style circles item.
  - LIT-tmpmox49 / NOTE-tmpirf1e (Simić et al.) already linked by LEAD-062.
- **Not held**: Strathman et al. 1994 (CFC scale); Wade-Benzoni & Tost 2009
  (the identification/efficacy theory); Trope & Liberman 2010 (construal
  level); Syropoulos & Law et al. 2023a/b (longtermism / IIBI).
- No "not held" verdict overturned. LEAD-062's "no study separates
  continuity with future people from caring" stands after reading this one.

## Copies located (summary table)

| address | kind | outcome, date |
|---|---|---|
| https://osf.io/29jeb/download (-> files.osf.io ... 29jeb_v1 ... 64f8b4716c0f5a31cad05897) | authors' CC BY preprint, PsyArXiv/OSF | read; fetched once 2026-11-22, no check; served file "CFC, FSC & RFG Manuscript 5-21-24 - Preprint.docx" |
| Europe PMC PPR721445 | abstract record | abstract only (LEAD-062 run, 2026-11-22) |

Status implied: read (preprint, 2024-05-21 version); ready to move from
Unfetched to Active. Supplementary materials and OSF data not read.
