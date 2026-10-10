---
status: Active
title: 'Two satisfaction questions in German and in a back-translated Chinese version: an order effect that reverses across a rendering, with the Clinton–Gore poll as the scale of the 2ε bound'
version: 1
standing: documented
tags:
- probabilistic-modeling
- pragmatics
- translation
- social-science
date: '2026-10-10'
line: pragmatic-transport
summary: >-
  Haberstroh, Oyserman, Schwarz, Kühnen and Ji (2002), Experiment 2,
  asked German and Chinese students the same two satisfaction questions,
  in a back-translated Chinese version, in both orders. The part–whole
  correlation depends on order in the German administration and reverses
  in the Chinese one, and the authors explain it by a pragmatic mechanism.
  Only correlations are reported, so the case shows the bound's
  contrapositive in kind, not in number. Moore's Clinton–Gore poll, held
  through [LIT-834](../literature.d/LIT-834.md), supplies the number: an order effect of total variation
  about 0.095, against a sampling floor of about 0.03 per order at poll
  sizes, so 2ε is about as large as the effect it would certify.
illustrates:
- CLAIM-tmpfzcik
---
<!-- inactive-ok-file: CLAIM-tmpeqvy4 — Proposed; the procedure-level measure that fixes the kernel across items, cited as open -->

# CASE-tmpkhubu: Two satisfaction questions in German and in a back-translated Chinese version: an order effect that reverses across a rendering, with the Clinton–Gore poll as the scale of the 2ε bound

Found on 2026-10-10 by a search the owner asked for: a documented order
effect measured in both orders on a source item and a rendering of it, to
give [CLAIM-tmpfzcik](../claims.d/CLAIM-tmpfzcik.md)'s bound a case and a scale.

## The case

**The rendering.** Haberstroh, Oyserman, Schwarz, Kühnen and Ji (2002),
*Journal of Experimental Social Psychology* 38: 323–329,
doi:10.1006/jesp.2001.1513, Experiment 2. Students at the University of
Heidelberg (N = 58) and Beijing University (N = 109) answered "How
satisfied are you with your studies?" and "How satisfied are you with your
life as a whole?" on 1–7 scales. Method: "These questions were translated
into Chinese and back-translated to ensure comparability." Participants
"were randomly assigned to one of two order conditions, resulting in a 2
(Culture) × 2 (Question Order) factorial design."

Table 2 gives the Pearson correlation between the two answers, N in
parentheses:

| order | Germany | China |
|---|---|---|
| academic, then life | .78 (30) | .36 (55) |
| life, then academic | .53 (28) | .50 (54) |

The German order effect on the correlation is about +.25; the Chinese one
is about −.14. In the life-first order the two administrations "showed
nearly identical correlations, z = .17, ns". The interaction: "the observed
differences in correlation between countries are significantly larger in
the academic–life than in the life–academic order, z = 1.93, p = .053".

The authors' account is pragmatic. A respondent who attends to the common
ground reads the general question, after the specific one, as asking for
*new* information, and leaves out what was just reported, so the
part–whole correlation falls. Abstract: "participants' differential
attentiveness to the common ground resulted in differential question order
effects, raising important methodological issues for cross-cultural
research." Experiment 1 produced the same mechanism within Germans by
priming. The study builds on Schwarz, Strack and Mai (1991), who, as
Haberstroh et al. report them, found marital and life satisfaction
correlating .32 or .67 by order, and .20 when the general question was
reworded "Aside from your marriage, which you already told us about, how
satisfied are you with other aspects of your life?". That is an
intralingual rewording that removes an order effect; its primary was not
read.

**The scale.** Moore (2002), *Public Opinion Quarterly* 66(1): 80–91,
doi:10.1086/338631, as reproduced in Wang and Busemeyer (2013), [LIT-834](../literature.d/LIT-834.md),
p. 691 and Table 1. A Gallup split ballot (6–7 September 1997) asked whether
Bill Clinton, and Al Gore, is "honest and trustworthy", in the two orders:
"In the non-comparative context, Clinton received a 50% agreement rate and
Gore received 68% … in the comparative context, the agreement rate for
Clinton increased to 57% while for Gore, it decreased to 60%". Table 1
gives the joint yes/no tables. Clinton first, N = 447: .4899, .0447, .1767,
.2886 (CyGy, CyGn, CnGy, CnGn). Gore first, N = 432: GyCy .5625, GyCn .1991,
GnCy .0255, GnCn .2130.

Computed here, not by the authors. On the common outcome set (Clinton,
Gore) the observed order effect is TV(p_CG, p_GC) =
½(.0726 + .0192 + .0224 + .0756) ≈ 0.095. A simulation of samples of 447
from the Clinton-first table gives a total variation from the true table
with median about 0.027 and 95th percentile about 0.054; between two
independent samples of that size, median about 0.038.

## What it can show

[CLAIM-tmpfzcik](../claims.d/CLAIM-tmpfzcik.md) bounds the change in an order effect by 2ε, where ε bounds
each order's observational distortion. Its contrapositive is: if the
rendering's order effect differs from the source's, some order-context
was distorted. Haberstroh et al. document that in kind. The two-question
item, rendered into Chinese, has an order effect opposite in sign on the
correlation. So under the identity kernel on the 1–7 scale, the rendering
did not keep both orders' joint response distributions at the source's.
The table also localises the distortion, as the bound's per-context
hypothesis invites: the life-first order is nearly kept (.53 against .50),
the academic-first order is not (.78 against .36). ε is small in one
order-context and large in the other.

The mechanism is the line's own. The first question frames the second, and
what it does depends on the interpreter population's attention to common
ground: a pragmatic order effect, not a perceptual one.

The Clinton–Gore numbers give the bound its practical resolution. A real
attitudinal order effect is about 0.095 in the bound's metric. At poll
sizes, sampling alone puts about 0.03 to 0.04 into each estimated ε, so 2ε
is about 0.05 to 0.08 before any distortion. A rendering fielded at
n ≈ 450 per order could not be certified by the bound to have kept a
Clinton–Gore-sized order effect. To make 2ε a fifth of the effect, ε must
be under about 0.01, which by the usual 1/√n scaling needs roughly ten
times the respondents per order and language. This belongs to the claim's
"What it does not say": estimation error is not in the bound.

## What it cannot show

- **It gives no ε.** Haberstroh et al. report correlations, not joint
  response distributions. A correlation is a functional of the joint
  distribution, but without bounds on the variances a change in it gives
  no lower bound on total variation. So the bound cannot be checked on
  these numbers, only its contrapositive illustrated. It is why the case
  illustrates and does not support.
- **The rendering and the readership change together.** Chinese students
  read the Chinese version; German students read the German. The paper
  quotes the items in English and does not say in so many words that the
  German administration was in German; that is the natural inference for
  Heidelberg students, not a quotation, and is **unverified**. The case
  shows that the order effect, transported to a new language and readership,
  changed. It does not show that the translation changed it.
- **The strongest reply.** A defender of the rendering would say it is
  faithful: back-translation checked it, and the change is the readers'
  self-construal, which the authors themselves predicted from culture. The
  reply is right about cause and beside the bound's point, since the bound
  is stated on the target readers' responses whatever their source. But it
  means the case cannot speak to fidelity of the *text*, and the kernel K
  is assumed, not tested: whether "5" on a Chinese 1–7 satisfaction scale
  corresponds to "5" on a German one is not established ([CLAIM-tmpeqvy4](../claims.d/CLAIM-tmpeqvy4.md)
  asks that K be fixed across items).
- **The cells are small.** 28 to 55 per cell make each correlation
  uncertain by about ±.2, and the interaction is marginal (p = .053).
- **The Clinton–Gore poll has no rendering.** It calibrates; it is not an
  instance.
- **What would close the gap.** The design that would test the bound
  itself: the same two questions, source and rendering, crossed with
  readership (for instance bilingual Chinese students given both versions
  on separate occasions, beside monolingual groups), both orders in each
  cell, the full 7 × 7 joint tables reported, and n per order and
  version an order of magnitude above 450. Such items could sit in the
  discriminating study ([CASE-tmp1uzfn](CASE-tmp1uzfn.md)) as an order-effect arm.

## Sources

Held in the record:

- Wang, Z. and Busemeyer, J. R. (2013), [LIT-834](../literature.d/LIT-834.md), doi:10.1111/tops.12040.
  Read directly in the author copy
  (https://jbusemey.pages.iu.edu/quantum/QuestOrdEff.pdf) for p. 691 and
  Table 1. Moore's data are known here through it.
- Wang, Solloway, Shiffrin and Busemeyer (2014), [LIT-795](../literature.d/LIT-795.md),
  doi:10.1073/pnas.1407756111, which reports the same poll's order effect
  (χ²(3) = 10.14, as the search report gives it; not re-checked here).

Not held, cited by identifier:

- Haberstroh, S., Oyserman, D., Schwarz, N., Kühnen, U. and Ji, L.-J.
  (2002), "Is the Interdependent Self More Sensitive to Question Context
  Than the Independent Self? Self-Construal and the Observation of
  Conversational Norms", *J. Exp. Soc. Psychol.* 38(3): 323–329,
  doi:10.1006/jesp.2001.1513. Read directly in the author copy,
  https://dornsife.usc.edu/daphna-oyserman/wp-content/uploads/sites/232/2023/11/02_jesp_haberstroh_et_al_self___question_context.pdf.
- Moore, D. W. (2002), "Measuring New Types of Question-Order Effects",
  *Public Opinion Quarterly* 66(1): 80–91, doi:10.1086/338631. Not read;
  known only through [LIT-834](../literature.d/LIT-834.md).
- Schwarz, N., Strack, F. and Mai, H.-P. (1991), *Public Opinion Quarterly*
  55(1): 3–23. Not read (the fetch was blocked); its figures are as
  Haberstroh et al. report them, and **unverified**. DOI not checked.
