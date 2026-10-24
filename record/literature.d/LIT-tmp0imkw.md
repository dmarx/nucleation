---
status: Unavailable
status_note: >-
  filed 2026-10-24 for the owner's question how the record stands on
  multi-agent reinforcement learning; a reading was attempted the same day
  and failed on access. The ACM Digital Library (doi:10.1145/860575.860687)
  answered every request from this client with a Cloudflare challenge
  (403). Unpaywall and OpenAlex list no open copy. The repository records
  OpenAlex names hold no file this client could reach: the VUB repository
  (biblio.vub.ac.be) page is a script-only catalogue entry, ULB's DI-fusion
  record shows no attached full text, the Hasselt document server returned
  503 and a search result describes its record as "No Fulltext", and
  CiteSeerX reset the connection. Web searches found no author copy. The
  model the paper derives is read instead through Kaisers & Tuyls 2010
  (LIT-tmpgfdwc, NOTE-tmp43vkx), which restates its equation and shows that
  it describes frequency-adjusted, not plain, Q-learning. It stays
  Unavailable until a copy is supplied. No NOTE is filed.
title: 'A selection-mutation model for Q-learning in multi-agent systems'
version: 1
history:
- version: 1
  date: '2026-10-24'
  note: >-
    Filed 2026-10-24, not read. Citation checked against Crossref
    (doi:10.1145/860575.860687): Karl Tuyls, Katja Verbeeck and Tom
    Lenaerts, Proceedings of the Second International Joint Conference on
    Autonomous Agents and Multiagent Systems (AAMAS '03), pp. 693–700, ACM,
    14 July 2003; Crossref's title has a lower-case "q", and the title here
    capitalizes it as the paper's later citations do. Status Unavailable
    under ADR-041: searched the same day, as the status note records.
    `published:` is Crossref's date. A grep of record/literature.d for the
    DOI, "Tuyls" and the title found nothing.
tags:
- game-theory
- learning-theory
- anthology-candidate
date: '2026-10-24'
published: '2003-07-14'
doi: '10.1145/860575.860687'
first_author: 'Tuyls'
keywords:
- 'Q-learning'
- 'replicator dynamics'
- 'selection-mutation'
- 'Boltzmann exploration'
- 'multi-agent systems'
- 'evolutionary game theory'
implementations: []
summary: >-
  Tuyls, Verbeeck & Lenaerts (2003). Derives the continuous-time dynamics of
  Boltzmann Q-learning in two-player stateless matrix games, as later
  restated by Kaisers & Tuyls: ẋ_i = x_i α(τ⁻¹[(Ay)_i − x·Ay] − log x_i +
  Σ_k x_k log x_k), a replicator (selection) term plus an entropy
  (mutation) term, linking exploration in reinforcement learning to
  mutation in evolutionary game theory. Summary drawn from the abstract and
  from Kaisers & Tuyls 2010, not from the paper.
---
<!-- inactive-ok-file: NOTE-tmp43vkx — filed in the same batch; the substitute reading, named -->

# LIT-tmp0imkw: A selection-mutation model for Q-learning in multi-agent systems

Tuyls, K., Verbeeck, K. & Lenaerts, T. (2003). A selection-mutation model
for Q-learning in multi-agent systems. In *Proceedings of the Second
International Joint Conference on Autonomous Agents and Multiagent Systems
(AAMAS '03)*, 693–700. ACM. doi:10.1145/860575.860687.

Not read. The summary is drawn from the abstract and from Kaisers & Tuyls
(2010), LIT-tmpgfdwc, which restates the paper's equation. A reading should
check it first.

## Why this is here

Filed 2026-10-24 when the owner asked how the record stands on multi-agent
reinforcement learning, as the source of "Q-learning is replicator dynamics
plus an exploration term that removes absorbing states". The later paper by
one of its authors, read in its place, says the model describes Q-learning
only after a frequency adjustment (NOTE-tmp43vkx).
