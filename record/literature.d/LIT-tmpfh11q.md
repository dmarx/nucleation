---
status: Active
status_note: 'read in full 2026-10-02 ([NOTE-tmp7cyl2](../notes.d/NOTE-tmp7cyl2.md)), from arXiv v3 (the Boston Review text), with v1''s conclusions compared; worth reading as the clearest short statement of the case for and against consciousness in LLMs, and as the origin of the "theory-balanced" credence approach that Butlin et al. built on. Its method is a regimented request for a feature X, and its verdicts are credences offered "for illustrative purposes": under 10% for current LLMs, 25% or more for conscious LLM+ systems within a decade, on "mainstream assumptions". It does not break the deadlock [THEORY-023](../theory.d/THEORY-023.md) describes. It is an instance of it: mimicry undercuts self-report, the main obstacles are theory-derived, and biology is set aside rather than answered.'
title: 'Could a Large Language Model be Conscious?'
version: 1
history:
- version: 1
  date: '2026-10-02'
  note: >-
    Read in full (arXiv:2303.07103 v3, 18 Aug 2024, 17 pp., headed
    "Published in the Boston Review, August 9, 2023 (published
    version)"; text extracted with PyMuPDF). I read every section, all 33
    footnotes and the Afterword (July 2023). I also read v1 (4 Mar 2023,
    "Draft!", an edited transcript with slides) for its conclusions and
    notes, to record how the numbers changed; v1's slides were not read
    one by one. The Boston Review page refused automated requests, so the
    venue and date are from the paper's own header and arXiv's
    journal-ref ("Boston Review, August 9, 2023"). arXiv lists v1 4 Mar
    2023, v2 29 Apr 2023 and v3 18 Aug 2024, with the comment "Invited
    lecture at NeurIPS, November 28, 2022". The DataCite DOI is
    10.48550/arXiv.2303.07103; there is no Crossref DOI. The brief's
    citation is right. `published:` is the arXiv v1 date. Not held in the
    Anthology of the SOTA: a grep of its literature.d for the arXiv id, the
    title, "Chalmers" and "consciou" found nothing, so ADR-013 does not
    apply.
tags:
- consciousness
- cognition
- epistemology
- agency
- representation-learning
- ethics
date: '2026-10-02'
published: '2023-03-04'
arxiv: '2303.07103'
first_author: 'Chalmers'
keywords:
- 'large language models'
- 'AI consciousness'
- 'sentience'
- 'LLM+'
- 'global workspace'
- 'recurrent processing'
- 'unified agency'
- 'theory-balanced approach'
implementations: []
summary: >-
  Chalmers (2023), arXiv:2303.07103; Boston Review, 9 August 2023; from a
  NeurIPS 2022 invited talk. Asks for a feature X that LLMs have (or lack)
  and that indicates consciousness (or its absence). Self-report,
  seeming-conscious, conversation and general intelligence give at most
  weak evidence for it. Biology, senses and embodiment, world and self
  models, recurrent processing, a global workspace and unified agency are
  the evidence against. All but biology are temporary. On mainstream
  assumptions: under 10% credence for current LLMs, 25% or more for
  conscious LLM+ systems within a decade. Twelve challenges are offered as
  roadmap or red flags.
---
<!-- inactive-ok-file: THEORY-023 THEORY-tmp31lxe — Proposed; this note says how the paper bears on those accounts, and does not lean on them -->

# LIT-tmpfh11q: Could a Large Language Model be Conscious?

David J. Chalmers (2023), arXiv:2303.07103 (v1 4 March 2023, v3 18 August
2024). Published in *Boston Review*, 9 August 2023. An edited version of
his invited talk at NeurIPS, 28 November 2022.

## Key takeaways

- **Method** (§§2–3). A claim for or against LLM consciousness should name
  a feature X, give reasons that LLMs have or lack it, and give reasons
  that having or lacking it makes consciousness probable or improbable.
- **For** (§2). Self-report is fragile and trained on human talk about
  consciousness. Seeming conscious is cheap, as ELIZA showed.
  Conversational ability matters only as a sign of general intelligence.
  General intelligence gives "some limited reason to take the hypothesis
  seriously".
- **Against** (§3). Six X's: biology, senses and embodiment, world models
  and self models, recurrent processing, a global workspace, unified
  agency. The strongest are recurrence, workspace and agency. All but
  biology are "temporary rather than permanent": each names a research
  programme, and LLM+ systems (multimodal, tool-using, embodied) may meet
  them "within the next decade or two".
- **Numbers** (§4), "for illustrative purposes". Give at least 1/3
  credence to each of the six requirements. If they were independent, a
  system lacking all six would have under a 1/10 chance of consciousness,
  hence "somewhere under 10 percent" for current paradigmatic LLMs. For
  sophisticated LLM+ systems within a decade: over 50% that they will be
  built, times 50% that they would be conscious, gives "25 percent or
  more".
- **The theory-balanced approach** (fn 30). Weigh several theories'
  verdicts by credences, perhaps taken from expert surveys. Chalmers
  presents this as distinct from Birch's theory-heavy, theory-neutral and
  theory-light approaches.
- **Challenges** (§4): four foundational (benchmarks, theory,
  interpretability, ethics), seven engineering, and a twelfth: "If that's
  not enough for conscious AI: What's missing?". He offers them as a
  roadmap or as red flags. He is "not asserting that we should pursue
  this research program".

## Standing in the record

Filed on 2026-10-02 at the owner's request, as one of the Chalmers works
he asked for. [NOTE-tmp7cyl2](../notes.d/NOTE-tmp7cyl2.md) is the close reading. **Active**: it is the
paper the AI-consciousness works in this record react to. Butlin et al.
([LIT-056](LIT-056.md)) build on it ([NOTE-052](../notes.d/NOTE-052.md)), and Schwitzgebel ([LIT-191](LIT-191.md), [NOTE-104](../notes.d/NOTE-104.md))
reports its 25% figure.

**How it sits against [THEORY-023](../theory.d/THEORY-023.md).** [THEORY-023](../theory.d/THEORY-023.md) says current evidence
cannot settle whether an AI system is conscious. Mimicry undercuts
behavioural evidence, and architectural indicators presuppose the disputed
computational functionalism. This paper agrees on the first half, is an
example of the second, and adds one more voice to the contested prior.

- *Behaviour: agrees, independently and earlier.* Self-reports are
  "fragile" and the model "has learned to imitate those claims" from a
  corpus of people talking about consciousness, so "the evidence is much
  weaker". That is the undercutting move of Birch's gaming problem
  ([LIT-111](LIT-111.md)) and Schwitzgebel's Mimicry Argument ([LIT-191](LIT-191.md)), made in 2022.
  Chalmers's third challenge, an LLM that describes features of
  consciousness it was not trained on (after Schneider and Turner), is a
  candidate for the "theory-neutral marker … immune to training on human
  output" that [THEORY-023](../theory.d/THEORY-023.md) names as a refuter. He proposes it; he does not
  supply it.
- *Architecture: an instance of the Janus problem, not a way out.*
  Recurrence, workspace, self models and unified agency are all
  theory-derived requirements, and he treats building them into LLM+
  systems as progress toward consciousness. That is the functionalist face
  of Birch's Janus problem. The biological naturalist's face, Seth's
  ([LIT-135](LIT-135.md)), is set aside: Chalmers says he has "argued that these views
  involve a sort of biological chauvinism", that "silicon is just as apt
  as carbon", and then "I'll set this issue aside". He does give biology
  at least 1/3 credence and multiplies it in. So the numbers are not
  conditional on functionalism alone. But the multiplication is a credence
  under assumed theories, which [THEORY-023](../theory.d/THEORY-023.md)'s `promote_when` says "cannot
  settle it". The twelfth challenge, asking a doubter to name a missing X
  "and could that X be built into an AI system?", frames the burden as a
  functionalist would. For Seth the missing X is being alive, which is not
  an engineering item.
- *Priors: a fifth position.* [THEORY-023](../theory.d/THEORY-023.md) lists Seth (unlikely), Birch
  (cannot rule out), Butlin et al. (no strong current candidate) and
  Schwitzgebel (we will not know). Chalmers is low for current LLMs (under
  10%) and significant for LLM+ systems within a decade (25% or more). In
  fn 29 he says his own views "lean somewhat more to consciousness being
  widespread", so he would go higher. His own term for the stance is
  "theory-balanced".
- *Where it falls short of the account's bar.* Nothing here is evidence
  that both parties accepted in advance. It is a structured credence
  exercise, and Chalmers says so ("specious precision").

**On [THEORY-tmp31lxe](../theory.d/THEORY-tmp31lxe.md).** Two points only. First, a global workspace
"gathering information from numerous non-conscious modules" is offered as
a possible requirement. That is the subsystem-driven architecture
Schwitzgebel used to answer Chalmers's correspondence objection ([NOTE-131](../notes.d/NOTE-131.md)),
and here Chalmers does not press that objection against it. Second,
Chalmers suggests that one LLM "can support an ecosystem of multiple
agents". That is the multiplicity of minds in one system that his 1996
implementation paper ([LIT-tmpb96vr](LIT-tmpb96vr.md)) allowed, here offered as a reply to
the disunity objection. It is a passing remark, not an argument.

**[NOTE-131](../notes.d/NOTE-131.md)'s correspondence principle is not stated here.**

**Not the extended mind.** "LLM+" and "extended large language models"
mean models with added modalities, actions and tools. They are not the
extended mind of [LIT-097](LIT-097.md). Tool use (database queries, code execution) is
the natural place where the two would meet, and the paper does not make
the link. Among the core consciousness works filed alongside this one,
the hard problem is named here only as the second foundational challenge
("we don't understand consciousness. That's a hard problem, as they say").

**Boundary.** Not held in the anthology, so [ADR-013](../decisions.d/ADR-013.md) does not apply. Its
engineering challenges ("build LLM+s with a global workspace") are a
research map offered equally as red flags, not an instruction for
machine-learning practice, and no anthology topic holds AI consciousness.
So it stays here and is not tagged `anthology-candidate`.
