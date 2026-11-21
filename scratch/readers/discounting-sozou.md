# Reader notes: discounting-sozou (LIT-tmpk0e2v, Sozou 1998)

## Step 1: copies located (2026-11-21)

- Europe PMC REST search: PMCID PMC1689473, isOpenAccess N, inEPMC Y.
- Europe PMC REST fullTextXML PMC1689473: HTTP 500 (no XML; likely a scan).
- https://europepmc.org/articles/PMC1689473?pdf=render: Cloudflare "Just a moment..." challenge (403). Stopped.
- https://pmc.ncbi.nlm.nih.gov/articles/PMC1689473/: Google reCAPTCHA challenge page. Stopped; www.ncbi.nlm.nih.gov PMC links not tried (same service).
- https://royalsocietypublishing.org/doi/pdf/10.1098/rspb.1998.0534: Cloudflare challenge (403). Stopped.
- http://www.dklevine.com/users/levucla/hyperbolic.pdf (OpenAlex, submittedVersion, a reading-list page): HTTP 401, authorisation required. Stopped.
- IDEAS RePEc page cla/levarc/618897000000000775: no file, no abstract.
- CiteSeerX summary 10.1.1.983.4791: connection failed.
- Semantic Scholar API: abstract elided by publisher; OA pdf points to Europe PMC (blocked).
Result: Unfetched (copies exist, all behind bot checks or auth). Going to neighbours.

## Step 2: neighbour read (2026-11-21)

- Fedus, Gelada, Bengio, Bellemare, Larochelle (2019), "Hyperbolic Discounting and Learning over Multiple Horizons", arXiv:1902.06865v3, PDF via arxiv.org. Read: abstract, sections 1-3 (intro, related work, "Belief of risk implies a discount function"), appendix B.2-B.3. Restates Sozou: s(t)=∫p(λ)e^{-λt}dλ; exponential prior p(λ)=(1/k)exp(-λ/k) gives 1/(1+kt); uniform on [0,k] gives (1-e^{-kt})/(kt); gamma prior gives 1/(1+bt)^c; delta prior gives e^{-λt}. Fig 2 reproduces two of Sozou's figures.
