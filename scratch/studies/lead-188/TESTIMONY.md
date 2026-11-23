# LEAD-188 testimony findings

Coded under CODING.md (written before reading). All pages read on
2026-11-23 through the session's web fetch tool, which returns a model's
extract of the page, not the raw text; quotes below are as that extract
gave them, and are flagged for the owner's recheck in the report.

## Findings

| id | source (URL) | outlet, date published | speaker | quote | V | R | E | T |
|---|---|---|---|---|---|---|---|---|
| F1 | https://looper.com/233945/how-vinnie-jones-really-feels-about-his-role-in-x-men-exclusive | Looper (David L. Lebovitz), 2020-08-06 | Vinnie Jones (Juggernaut) | called it "Brett's line"; Ratner "found that on the internet and wanted to do that" | V1 | R1 | E1 | T0 |
| F2 | https://sg.news.yahoo.com/vinnie-jones-lock-stock-x-men-gentlemen-080039142.html | Yahoo (Roxy Simons), 2024-03-06 | Vinnie Jones | "We did the movie in Vancouver and then Brett Ratner phoned me and he said, 'oh, I want you to do this line'." / "He'd seen it online, I think, and so he said, 'I want you to do it'" / "so we had to go to Elstree for the day and we did that one line." | V1 | R1 | E2 | T1 |
| F3 | https://comicbookmovie.com/x_men/x_men-3-the-last-stand/x-men-the-last-stand-writer-reveals-infamous-juggernaut-btch-line-was-not-in-his-shooting-script-a205434 | ComicBookMovie (Mark Cassidy), 2023-09-04, citing Polygon | Simon Kinberg (co-writer), via Polygon | "The real [story] on that is that was a reshoot Ratner line." Not in the shooting script he submitted with Zak Penn. | V2 | R0 | E1 | T1 |
| F4 | same as F3 | same | Cassidy (writer) | "The line was inspired by a parody dub video of the '90s X-Men: The Animated series" | V4 | R0 (origin, no route) | E1 | T0 |
| F5 | https://www.cbr.com/x-men-the-last-stand-simon-kinberg-juggernaut-line/ | CBR (Leon Miller), 2023-09-04 | Kinberg via Polygon | repeat of F3 (same quote); line "meme-inspired" (writer) | repeat | | | |
| F6 | https://heroichollywood.com/x-men-the-last-stand-writer-juggernaut-line-origins | Heroic Hollywood (Anthony Singletary), 2023-09-05 | writer, paraphrasing Kinberg via Polygon | line not in the script made with Matthew Vaughn; added by Ratner after Vaughn left | V4 | R0 | E1 | T0 (ambiguous: "after Vaughn left" is compatible with T1 and T2) |
| F7 | https://www.cinemablend.com/news/2551639/x-men-the-last-stands-brett-ratner-responds-to-vinnie-jones-recent-juggernaut-comments | CinemaBlend (Erik Swann), 2020-08-02 | Brett Ratner (Instagram, excerpted) | "I shot the script I was given and I was not able to expand the role of Juggernaut as per Vinnie's request" | V1 | R0 (silent on the line) | | T0 |
| F8 | https://www.darkhorizons.com/?p=16733 | Dark Horizons, 2006-05-24 | Ratner interview | nothing on the line, the video, reshoots | null | | | |
| F9 | https://movieweb.com/director-brett-ratner-breaks-down-x-men-the-last-stand/ | MovieWeb, 2006-05-23 | Ratner interview | nothing on the line or the video | null | | | |
| F10 | https://comicbookmovie.com/x_men/x-men_3_the_last_stand/vinnie-jones-finally-sets-the-record-straight-on-x-men-the-last-stand-role-i-got-mugged-off-exclusive-a177141 | ComicBookMovie (Josh Wilding), 2020-07-27 | Vinnie Jones | nothing on the line | null | | | |
| F11 | https://uk.style.yahoo.com/m-juggernaut-b-loud-improbable-053357107.html | The Independent via Yahoo (Kevin E G Perry), 2021-06-07 | writer | nothing on how the line came in | null | | | |

Held already, not re-coded (read 2026-10-29, NOTE-1272 of LIT-1142):
Siegel's oral history (V4 "likely a fan", R1, E2), Nazario's recollection
of a pre-release TV segment ("Word got around that the line was being
added": V3, R0, E3), and Kinberg via Polygon (= F3).

## Not reached

- https://www.polygon.com/23846994/invasion-season-2-simon-kinberg-interview-x-men-star-wars
  (Polygon's Kinberg interview, the original of F3): the session's fetch
  tool refused the host ("unable to fetch from www.polygon.com"),
  2026-11-23. Not worked around.
- https://theplaylist.net/x-men-last-stand-vinnie-jones-disappointed-20200729/
  (The Playlist on Jones, 2020-07-29): HTTP 403, 2026-11-23. Not retried.
- Searched and not found: any statement by Ratner on why the line was
  added; any editor's, producer's or studio account; the TV segment
  Nazario recalls.

## Result under the decision rules

- **Production testimony on the route: one voice, two occasions (F1,
  F2).** Vinnie Jones, first-hand as to the call and the Elstree pickup
  day, says Ratner had seen the line "online" / "found that on the
  internet". Jones's knowledge of where Ratner saw it is what Ratner told
  him or what Jones supposes ("I think" in F2): coded V1 because Jones is
  on the production, but it is first-hand only as to the request, and
  second-hand as to Ratner's exposure.
- **Reported production testimony (V2): Kinberg (F3)**, dating the line
  to a reshoot under Ratner, no route.
- **Route coded: R1 in every production finding that gives one.** A
  named decision-maker saw it online and asked for the line. No finding
  codes R2 (line reached the production through crew or cast quoting it),
  R3 (test screenings, marketing) or R4 (independent origin).
- **Timing: T1.** The line was shot after principal photography, on one
  day at Elstree (F2), consistent with Kinberg (F3).
- What R1 leaves open is exactly CLAIM-332's question: "online" is
  where the circulation was. The testimony fixes the last link (one
  director, his own viewing) and is silent on how the video came to his
  screen. That is what the model in `model.py` prices.
