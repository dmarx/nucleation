# LEAD-129 — matched comparison of institutions with/without effective means to revise their governing standards

Carries out LEAD-129, which advances CLAIM-685 (the reflexive accountability
hypothesis). CLAIM-685: institutions able to recognize, authorize and carry out
revisions of their own governing standards avoid persistent normatively
significant failures better than institutions that only monitor outcomes against
fixed standards, where the inherited standards are inadequate, and not on
routine work. The study is filed as CASE-tmp3pe1j (executed-study, documented).

## Selection rule

Public standards bodies, from open lawful sources (their own published
procedures and change histories), each governing a technical standard that
(a) was found inadequate to problems it had to represent, and (b) whose body
either has or lacks a *standing, resourced procedure* to recognize, authorize
and execute revisions of the governing standard. Pairs are matched *within a
domain* so that resources and the arrival/independence of defect evidence
(CLAIM-342) are as similar as the public record allows. This is a small,
purposively chosen set, not a sample — illustrative, not a powered test.

## Measure

`persistence_years` = years a recognized, normatively significant inadequacy of
the governing standard stood uncorrected, from the earliest dated recognition to
the correction (or to supersession of the regime). Data in `pairs.json`;
tally and direction check in `summarize.py`; tests in `test_summarize.py`.

## Result (see summarize.py output)

| pair | revising arm (persistence) | fixed arm (persistence) | gap |
|------|----------------------------|-------------------------|-----|
| P1 web markup, same era | WHATWG 2 yr | W3C HTML/XHTML track 8 yr | +6 |
| P2 same institution, before/after | W3C after 2019 ~0 yr | W3C 1999-2011 12 yr | +12 |
| P3 character encoding | Unicode Consortium 2 yr | ISO 8859 code-page regime 20 yr | +18 |
| X1 unmatched extreme | — | Julian calendar 857 yr (no revision organ) | — |

All three matched gaps are positive (fixed arm left the recognized inadequacy
standing longer), in the direction CLAIM-685 predicts. In P1 the fixed arm is
the *better-resourced* body, and P2 holds the institution and its evidence
constant — both cut against the rival explanation (CLAIM-685's defeater) that
the difference is really better evidence or more resources, not the revision
means. Unicode's stability policy (encoded characters, names, normalization
never revised) is selective non-revision, matching CLAIM-665's routine-work
limit rather than contradicting the hypothesis.

## Why illustrative, not powered

- N = 3 matched pairs + 1 unmatched extreme, chosen not sampled.
- "Fixed" was sometimes a deliberate governance bet (W3C's XHTML2) rather than
  absence of capacity; the operative variable is the *operative standard's*
  revision regime, not the body's latent capacity.
- `persistence_years` depends on when "recognition" is dated — a judgement
  (the calendar extreme spans 857 or ~1257 years by that choice).
- Independence of evidence is matched only roughly; P1 and P2 are the strongest
  controls.
- Survivorship/publication bias toward famous standards.

It does not meet CLAIM-685's defeater (it finds a difference, not none; and the
resource-reversed and same-institution pairs argue the difference is not only
evidence). So the case *illustrates* CLAIM-685; it does not establish it.

## Sources (public, lawful; fetched 2026-11-22)

- WHATWG FAQ (founding 2004; living-standard model; GitHub-issue intake):
  https://whatwg.org/faq
- W3C–WHATWG MOU, 28 May 2019 (HTML/DOM a single Living Standard at WHATWG;
  W3C endorses Review Drafts): https://www.w3.org/2019/04/WHATWG-W3C-MOU.html
  and the W3C blog announcement (2019).
- Unicode stability policy (what is frozen):
  https://www.unicode.org/policies/stability_policy.html ; Unicode error
  reporting / errata: https://www.unicode.org/reporting.html
- Gregorian reform: Britannica, "Ten Days That Vanished"
  (https://www.britannica.com/story/ten-days-that-vanished-the-switch-to-the-gregorian-calendar);
  Council of Nicaea (325) equinox reference; Bede (8th c.); Roger Bacon
  (c.1200-1267); bull *Inter gravissimas* (24 Feb 1582).

Facts above the matched-pair dates are well-established encyclopedic history;
the load-bearing procedural facts (WHATWG founding and model, the 2019 MOU,
the Unicode stability policy and error-reporting mechanism, the Gregorian
reform interval) were checked against the public pages listed on 2026-11-22. No
bot check, captcha, 403/429 or paywall was hit.

## To rerun

    cd scratch/studies/lead-129
    python3 -I summarize.py
    python3 -I -m pytest test_summarize.py -q
