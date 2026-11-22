<!-- scratch/studies/lead-124/README.md: the materials of LEAD-124's refit -->
# LEAD-124: decay by task type, refit from Tatel & Ackerman's posted data

Run on 2026-11-22 for LEAD-124. The article (doi:10.1037/bul0000481) could not be fetched: APA answered with an Imperva WAF challenge. Its OSF project, https://osf.io/bgfyp/ (linked from the DOI by OpenAlex), holds the coded data and the authors' R script but no manuscript. This refit uses that data.

- Data (not committed; download it again): "Study Data Independent Samples Effect Size Formula.xlsx", https://osf.io/download/8hw6u/ (version of 2025-04-09, 1,273 rows). This is the file the authors' script (`R Script for Analyses_For Submission.R`, https://osf.io/download/zq35p/) reads as `df_is`.
- `metareg.py`: a random-effects meta-regression (REML) with cluster-robust standard errors (CR1; the authors use clubSandwich's CR2, so the robust SEs are close to theirs but not identical). `test_metareg.py`: two tests (`python3 -m pytest -q test_metareg.py`).
- `by_task_type.py <xlsx> [out.json]`: the authors' specification. vi = (n1+n2)/(n1·n2) + d²/(2(n1+n2)); intervals of 60 months or more dropped for accuracy and speed; clusters are source × study × group. It fits the main slope for each measure, then the retention interval × `task_realism` and × `task_domain` interaction models, giving each level's implied slope and intercept, and then the same models with intervals capped at 1, 3, 6 and 14 months, as a check for curvature.
- `results.json`: the output.

Rerun: `python3 -I by_task_type.py <path to the xlsx> results.json`.

Checks: the main slopes reproduce the article's abstract (accuracy −0.076, speed −0.063, mixed −0.061 SD a month, against 0.08, 0.06 and 0.06). The accuracy task-domain interactions reproduce the dissertation's Appendix D (0.121, 0.155, 0.132 and 0.178, against 0.12, 0.16, 0.13 and 0.18). The mixed task-domain model is singular because laboratory mixed measures reach only 0.93 months. Not done: the practice moderator by task type, half-loss times by type, and a non-linear model.
