<!-- scratch/studies/lead-101/README.md: what is here and how to rerun it -->
# LEAD-101: sanction lifted, harm still weighed?

- `CODING.md`: the coding rules, written before the table.
- `cases.csv`: three firm-sanction cases (Purdue, Siemens, Wells Fargo), coded
  for arm, outcome during and after the sanction, timing, source standing,
  reputation and benefit.
- `events.csv`: the dated events behind each code, with source and locator.
- `studies.csv`: the coefficients read from Gallo, Lynch and Tomy (2023),
  Table 5.
- `summarize.py`: converts the log-count coefficients to percent changes,
  marks 5% significance, and checks each case against the standard in
  `CODING.md`; writes `results.json`.
- `test_summarize.py`: 11 pytest tests.

Rerun from this directory:

    python3 -m pytest -q -p no:cacheprovider test_summarize.py
    python3 -I summarize.py

Source keys in the CSVs: `gallo2023` (J. Accounting Research,
doi:10.1111/1475-679X.12502, read from knowledge.uchicago.edu), `cia_purdue`
(the 2007 CIA, from the UNT end-of-term web archive of oig.hhs.gov),
`indiana_complaint` (State of Indiana v. Richard Sackler et al., Marion
Superior Court, filed 2019-05-21, redacted version, from
content.govdelivery.com), `norway_council` (Council on Ethics of the
Norwegian Government Pension Fund Global, recommendation of 15 June 2012,
unofficial English translation, from regjeringen.no), `reporters100`
(Ben Knight, 100Reporters, July 2021, co-published with the Associated
Press), `fed_2025` (Federal Reserve press release of 3 June 2025). No
downloaded text is committed.
