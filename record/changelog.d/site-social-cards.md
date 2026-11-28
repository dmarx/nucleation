### Changed

- The published site no longer renders a social-card image for every page
  (`site.social_cards: false`, luria 1.13.0). A link to any page now previews
  with one site-wide image. Turning the cards off cut the site build from
  1,709 s to 754 s and the deploy from 444 MB to 145 MB. The three deploys
  that timed out at 10 minutes were all 360–440 MB.
- CI pins luria 1.13.0 everywhere, up from 1.12.0. 1.13.0 is 1.12.0 plus the
  social-cards switch, so nothing else changes.
- A manual run of the Pages workflow can time the build: check `timings`, and
  the run uploads a `site-perf` report and writes it to the job summary.
