---
status: Unavailable
status_note: >-
  not read; no lawful copy reached as of 2026-11-05. Looked at: OpenAlex,
  which marks it closed access with no repository copy; the Ruina lab
  papers page at Cornell,
  https://ruina.tam.cornell.edu/research/topics/locomotion_and_robotics/papers.htm,
  where the connection was reset twice; a UCSB course copy,
  https://courses.ece.ucsb.edu/ECE594/594D_F13Byl/papers/McGeer90.pdf, and a
  Penn course-wiki copy said in search listings to be the 1988 technical
  report, not the journal text,
  https://alliance.seas.upenn.edu/~medesign/wiki/uploads/Courses/McGeer90-IJRR-Passive.pdf,
  both failing TLS verification (a certificate chain the client does not
  trust; verification was not disabled) and answering HTTP 503 to a second
  fetcher; CORE, https://core.ac.uk/download/4419055.pdf, HTTP 403 with a
  Cloudflare challenge. The publisher, SAGE, not tried, since it is
  closed access. Unpaywall not used, since it requires an email address.
  Two neighbours stand in for it, as later restatements and not as its own
  text: Asano (2012), [LIT-tmpckrd7](LIT-tmpckrd7.md), for the rimless wheel as the simplest
  passive walker and the stability of its gravity-powered gait; and
  Obayashi, Aoi, Tsuchiya and Kokubu (2016), [LIT-tmpw9g80](LIT-tmpw9g80.md), for the idea of
  passive dynamic walking and what later work found about the stability of
  such gaits. Neither gives McGeer's derivations, his two-legged walkers,
  his machine, his stability eigenvalues or his parameter studies.
title: 'Passive Dynamic Walking'
version: 1
history:
- version: 1
  date: '2026-11-05'
  note: >-
    Registered on 2026-11-05 from the owner's pasted synthesis on FACT,
    rigidity, compliant mechanisms and origami (the pasted synthesis on
    constraint architectures, written by another assistant, A, in the same
    exchange as the emergency-readiness bibliography, pasted 2026-11-04),
    which cites it as M10, McGeer 1990, IJRR,
    doi:10.1177/027836499000900206, for "stable gait cycles driven by
    gravity and their own dynamics." Citation checked against Crossref: Tad
    McGeer, The International Journal of Robotics Research 9(2), 62–82,
    April 1990, journal article. Crossref gives 1990-04-01, the issue date,
    which is `published:` (its record was created in 2007 by SAGE's
    back-file deposit). A's citation is correct. Not held before: the
    record's other McGeer, LIT-736, is a different work. Searched for a
    lawful copy and found none (see the status note). At the owner's
    request two neighbouring works were read in its place: Asano (2012),
    LIT-tmpckrd7, and Obayashi, Aoi, Tsuchiya and Kokubu (2016),
    LIT-tmpw9g80.
tags:
- control-theory
- complex-systems
date: '2026-11-05'
published: '1990-04-01'
doi: '10.1177/027836499000900206'
first_author: 'McGeer'
keywords:
- 'passive dynamic walking'
- 'bipedal locomotion'
implementations: []
summary: >-
  McGeer (1990). Unverified until read: no copy and no abstract were
  reached. The neighbours credit it with proposing passive dynamic walking:
  Obayashi et al. (2016), [LIT-tmpw9g80](LIT-tmpw9g80.md), say that such a system "walks down
  a shallow slope without an actuator or controller", balancing the energy
  lost at foot contact against the gravitational energy gained, and Asano
  (2012), [LIT-tmpckrd7](LIT-tmpckrd7.md), cites it for the rimless wheel as the simplest model
  of passive dynamic walking. The pasted synthesis on constraint
  architectures cites it for stable gait cycles driven by gravity and the
  walker's own dynamics.
---
<!-- inactive-ok-file: THEORY-tmpbbt2m THEORY-tmpabuss — Proposed and new; the accounts filed from the neighbours read in place of McGeer (1990), cited as open -->

# LIT-tmpv6ctd: Passive Dynamic Walking

McGeer, T. (1990). Passive Dynamic Walking. *The International Journal of Robotics Research* 9(2): 62–82. doi:10.1177/027836499000900206.

## Key takeaways

*Not read. What follows is what later works say of it, unverified against
the original.*

- **The idea.** Obayashi et al. (2016), [LIT-tmpw9g80](LIT-tmpw9g80.md): "Passive dynamic
  walking, a popular dynamic system that is based on the inverted pendulum
  mechanism, was proposed by McGeer [13,14]." (§1, p. 2).
- **The rimless wheel.** Asano (2012), [LIT-tmpckrd7](LIT-tmpckrd7.md), cites it as the work in
  which the rimless wheel "has been investigated as the simplest model of
  passive dynamic walking [1]." (§I, p. 1).

## Standing in the record

Registered from the pasted synthesis on constraint architectures, which
glosses it as "stable gait cycles driven by gravity and their own
dynamics." That cannot be checked against McGeer's text. As a description
of the idea the neighbours credit to him it is right. What the neighbours
add, and A's use leaves out, is that such gaits are stable only within a
small, thin basin of attraction and only within a window of slope, beyond
which walking gives way to running or the attractor is destroyed: stability
with narrow viability.

**The neighbours.** Asano (2012), [LIT-tmpckrd7](LIT-tmpckrd7.md), read in [NOTE-tmpbpr6m](../notes.d/NOTE-tmpbpr6m.md),
stands in for the rimless-wheel model and the stability of its gait, as
Asano restates and analyses it 22 years later. Obayashi, Aoi, Tsuchiya and
Kokubu (2016), [LIT-tmpw9g80](LIT-tmpw9g80.md), read in [NOTE-tmpescek](../notes.d/NOTE-tmpescek.md), stand in for the
general idea and for later findings on the basin of attraction of a
descendant of McGeer's compass walker. Neither restates any specific result
of McGeer's: his derivations, his two-legged walkers with or without knees,
his physical machine, his stability eigenvalues or his parameter studies.
The accounts filed from them, [THEORY-tmpbbt2m](../theory.d/THEORY-tmpbbt2m.md) and [THEORY-tmpabuss](../theory.d/THEORY-tmpabuss.md), are the
neighbours' own, not McGeer's.
