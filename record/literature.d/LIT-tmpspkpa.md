---
status: Active
status_note: >-
  read 2026-11-15 ([NOTE-tmpy669h](../notes.d/NOTE-tmpy669h.md)) from the arXiv preprint, v2 (§§1–6,
  Tables 1–4, Figs. 2–4; appendices skipped), with v1 searched for
  "logarithm" and "exponential" (no match). Published at ICML 2026, PMLR
  306, per the v2 footer and the arXiv comment; the PMLR page was not
  checked. Worth reading here as a second account of merge interference
  as cancellation, coordinate-free: rotations from orthogonal finetuning
  are mapped to so(d) by the inverse Cayley transform, not the matrix
  logarithm the exchange names, averaged there, and rescaled to restore
  the norm that conflicting directions cancel. Its ablation finds that
  rescaling is what matters (41.01 without it, 46.25 with it), which
  bears on [THEORY-107](../theory.d/THEORY-107.md). Its "orthogonal" is the adaptation itself, not a
  function-preserving symmetry as in [THEORY-112](../theory.d/THEORY-112.md).
title: 'Orthogonal Model Merging'
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Registered and read on 2026-11-15 from the owner's pasted
    continuation of the ChatGPT exchange "Explain String Theory", in A's
    turn on how model merging fails (merging on the orthogonal group).
    Citation checked against the arXiv API: Sihan Yang, Kexuan Shi and
    Weiyang Liu (CUHK, SphereLab), v1 2026-02-05, which is `published:`,
    v2 2026-11-04, comment "ICML 2026"; the v2 PDF footer gives
    Proceedings of the 43rd International Conference on Machine Learning,
    Seoul, PMLR 306, 2026. A says the method "uses the matrix logarithm";
    neither version mentions a logarithm or an exponential map, and the
    map is the inverse Cayley transform (Eq. 5). No email address was
    sent to any service.
tags:
- loss-landscapes
- mathematics
- anthology-candidate
date: '2026-11-15'
published: '2026-02-05'
arxiv: '2602.05943'
first_author: 'Yang'
keywords:
- 'model merging'
- 'orthogonal finetuning'
- 'orthogonal group'
- 'Lie algebra'
- 'Cayley transform'
- 'magnitude collapse'
- 'orthogonal-residual decoupling'
- 'hyperspherical energy'
implementations: []
compared_against:
- LIT-675
summary: >-
  Yang, Shi & Liu (2026), ICML. Merges models fine-tuned by orthogonal
  finetuning by averaging their rotations' skew-symmetric generators in
  so(d), reached by the inverse Cayley transform, and rescaling the mean
  by Σ‖Q_i‖/‖ΣQ_i‖ to undo "magnitude collapse", the cancelling of
  conflicting directions. For LoRA and fully fine-tuned models it splits
  each update into a Procrustes rotation and a residual merged by an
  ordinary method. On five Llama-3.1-8B OFT experts the corrected merge
  scores 46.25 against 41.01 without the correction and 44.71 for the
  experts; gains on non-OFT models are small and mixed. Bears on
  [THEORY-107](../theory.d/THEORY-107.md) (magnitude handling matters most) and is a sense of
  "orthogonal" distinct from [THEORY-112](../theory.d/THEORY-112.md)'s.
---
<!-- inactive-ok-file: THEORY-107 — Proposed; the coordinate account of merge interference this reading bears on -->

# LIT-tmpspkpa: Orthogonal Model Merging

Yang, S., Shi, K. & Liu, W. (2026). Orthogonal Model Merging. *Proceedings
of the 43rd International Conference on Machine Learning*, PMLR 306.
arXiv:2602.05943v2.

## Key takeaways

*From the reading, [NOTE-tmpy669h](../notes.d/NOTE-tmpy669h.md).*

- **The diagnosis** (abstract): Euclidean addition of task vectors
  "destroys the intrinsic geometric properties of pretrained weights, such
  as hyperspherical energy".
- **Magnitude collapse** (§3.2, Eq. 6): a plain mean of generators "can
  suffer from magnitude collapse due to destructive interference:
  conflicting components cancel out, yielding a merged update with a
  smaller norm".
- **The chart** (Eqs. 2, 5): R = (I + Q)(I − Q)⁻¹ and
  Q = (R − I)(R + I)⁻¹, the Cayley transform and its inverse.
- **The ablation** (Table 4): Simple Average R 39.53, Sequential Product R
  40.76, Simple Average Q 41.01, OrthoMerge 46.25: "our magnitude-corrected
  averaging scheme is essential".
- **Non-OFT models** (Table 2, MergeBench Llama-3.2-3B): "+OrthoMerge-G
  improves TA by 1.32%", "+OrthoMerge-C ... boosts TIES by 2.41%", but
  TSV-M with OrthoMerge-G falls by 1.49.

## Standing in the record

A, in the exchange, says the paper "investigates merging on the manifold
of orthogonal matrices ... uses the matrix logarithm to work with
orthogonal transformations in a Lie algebra, with additional handling for
nonorthogonal residual components". The reader found the manifold, the Lie
algebra and the residual handling right, and the matrix logarithm wrong:
the map to so(d) is the inverse Cayley transform, a different chart that
also lands in so(d). A also leaves out the magnitude correction, which is
the ingredient the ablation finds essential.

Two of its results bear on held entries. The ablation is a second case,
independent of TIES ([LIT-675](LIT-675.md)), in which handling the merged update's
magnitude matters more than other merge choices, so it bears on
[THEORY-107](../theory.d/THEORY-107.md)'s note that rescaling is TIES's largest step; it does not test
sign. And its orthogonal transformations change the function, whereas
[THEORY-112](../theory.d/THEORY-112.md)'s orthogonal map on the residual stream preserves it, so the
two uses of "orthogonal" must not be read as one.
