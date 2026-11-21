# Delegated reading: First Contact (Reddy, Levine, Dragan 2022), arXiv 2205.12381

## 2026-11-21 Step 1: located and fetched
- https://arxiv.org/abs/2205.12381 (abs page, HTTP 200): v2 is latest, "last revised 15 Sep 2022 (this version, v2)"; v1 24 May 2022.
- https://arxiv.org/pdf/2205.12381 (HTTP 200, application/pdf, 18 pp.); stamp "arXiv:2205.12381v2 [cs.LG] 15 Sep 2022". Extracted with pdftotext; pp. 7-8 rendered to images to read Fig. 2 and Fig. 3 values.
- Read in full: main text (secs 1-6), appendix A.1-A.3, figure captions; reference list scanned.
- Other copies named in the paper, not fetched: project site https://sites.google.com/view/coadaptation; code https://github.com/rddy/mimi. NeurIPS 2022 proceedings copy not looked up.

## Step 2: findings (pointers)
- Fig. 2 panel rhos: X2T 0.45, ASHA switch 0.50, ISQL 0.11, SAvDRL (Delta=max ep. length 10^3) 0.43, ASHA bottle 0.69. Mean of the five = 0.436, so the reported "average rho = 0.43" averages all five, SAvDRL included at Delta = 10^3. Unpredictive domain per figure: ISQL (0.11), not stated in text.
- SAvDRL Delta sweep (Fig. 2d): rho about -0.45 at Delta=1, crosses zero near 10^2, ~0.4 at 10^3. Offline state = 1D horizontal position of lander (A.3).
- Delta limit, sec 5.1 p.7 and sec 6.1 p.10, quotes taken.
- Cursor study: interface = single rotation angle; policy ignores state (A.2); targets random each episode; rho=0.87 over user-interface points (Fig 3c), not 12 points.
- theta converges near 0 or pi; authors: 180 "tends to be easy for users to understand and invert".
- User adaptation: assumed (Fig 1, sec 4); Fig 7 shows within-10-episode adaptation to fixed interface; Likert "I improved" p>.05. No unassisted or transfer test.
- Sec 6.2: user may observe state the interface cannot.

## Step 3: record recheck done (see report).
