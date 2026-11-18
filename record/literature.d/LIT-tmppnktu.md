---
status: Active
status_note: >-
  read 2026-11-15 ([NOTE-tmpkleq4](../notes.d/NOTE-tmpkleq4.md)) from the arXiv preprint, v3: §§1–7,
  Tables 1–2, Appendix B.1–B.2 opening and D.1–D.5; the later tables by
  caption. Worth reading here as the work A cites for interference
  "visible in Fourier transforms" of weights, and as a caution: its
  frequencies are taken over the arbitrary order of a weight matrix's
  rows and columns, so they change when hidden units are permuted, which
  leaves the network's function unchanged. It is a signal-processing
  heuristic on weight arrays that works empirically within one start, not
  wave mathematics in a physical sense.
title: 'FREE-Merging: Fourier Transform for Efficient Model Merging'
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Registered and read on 2026-11-15 from the owner's pasted
    continuation of the ChatGPT exchange "Explain String Theory", in A's
    turn on model merging and task arithmetic as an instance of
    superposition in weight space, where A cites it for frequency-domain
    filtering. Citation checked against the arXiv API (authors, title, v1
    date 2024-11-25, which is `published:`) and Crossref, queried without
    mailto (2025 IEEE/CVF ICCV, issued 2025-10-19,
    doi:10.1109/iccv51701.2025.00368, title cased "Free-Merging"). The
    IEEE and CVF open-access copies were not fetched. No email address
    was sent to any service. Quotes rechecked by the filer against the
    downloaded text.
tags:
- loss-landscapes
- mathematics
- anthology-candidate
date: '2026-11-15'
published: '2024-11-25'
arxiv: '2411.16815'
doi: '10.1109/iccv51701.2025.00368'
first_author: 'Zheng'
keywords:
- 'model merging'
- 'Fourier transform'
- 'frequency domain'
- 'high-pass filtering'
- 'task interference'
- 'task experts'
implementations:
- 'https://github.com/Zhengsh123/FREE-Merging'
compared_against:
- LIT-tmpmqgjz
- LIT-675
summary: >-
  Zheng & Wang (2025, ICCV). Each weight matrix's task vector is treated
  as a 2D signal and Fourier transformed. Different tasks' spectra differ
  most in amplitude at low frequencies, and that variance correlates with
  worse merges. High-pass filtering each task vector before adding them
  (FR-Merging) beats task arithmetic and TIES on CLIP ViT-B/32, and
  routed 1% "experts" bring FREE-Merging near the specialised models.
  The frequencies run over the arbitrary order of rows and columns and are
  not invariant to permuting hidden units, which [THEORY-112](../theory.d/THEORY-112.md) treats as a
  symmetry. A rival diagnosis to TIES ([THEORY-107](../theory.d/THEORY-107.md)).
---
<!-- inactive-ok-file: THEORY-107 — new tmp codes, or Proposed; this work's reading and neighbours, not leaned on -->

# LIT-tmppnktu: FREE-Merging: Fourier Transform for Efficient Model Merging

Zheng, S. & Wang, H. (2025). FREE-Merging: Fourier Transform for Efficient Model Merging. In *2025 IEEE/CVF International Conference on Computer Vision (ICCV)*. doi:10.1109/iccv51701.2025.00368. arXiv:2411.16815.

## Key takeaways

*From the reading, [NOTE-tmpkleq4](../notes.d/NOTE-tmpkleq4.md).*

- **The diagnosis** (§4, Fig. 2a): "task vectors from different
  fine-tuned models also exhibit great misalignment in the frequency
  domain", and so, the authors infer, "task interference in the
  low-frequency part are severe."
- **The correlation** (§4, Fig. 2b): "a clear negative correlation between
  the variance of amplitude power among models and the normalized merging
  performance".
- **The merge** (Table 2, ViT-B/32, 8 tasks): task arithmetic 70.1, TIES
  73.6, FR-Merging 78.1, FREE-Merging (with routed experts) 89.7, against
  90.5 for the individual models.
- **The ablation** (§6.6): low-pass filtering degrades performance badly,
  and band-pass is worse than high-pass.

## Standing in the record

Filed with the merging batch from the same turn, as the work A cites for
Fourier analysis of weights.

A's characterization: "The authors report interference visible in
Fourier transforms of model parameters and propose frequency-domain
filtering." The reader's verdict: it holds as a report, with three
precisions. The transform is of task vectors (fine-tuned minus
pretrained), not of the parameters themselves. The filter is high-pass.
The full method adds experts and a router that are not Fourier at all.

**The frequencies are not a property of the computation.** They are
taken over the index grid of a weight matrix, the arbitrary order of its
rows and columns. Permuting a layer's hidden units leaves the network's
function unchanged and changes this spectrum, so the quantity is not
invariant to permutations, the symmetry [THEORY-112](../theory.d/THEORY-112.md) factors out. Low
frequencies near the centre mostly carry row and column means and other
smooth trends of the storage layout. The paper's reading that
"low-frequency parts capture the global structure" is an analogy from
images, not shown for weights, and the text never mentions permutation
except in citing Git Re-Basin. Within one pretrained start the layout is
shared across models, which may be why the filter still helps. Across
independently trained models the method would not be well defined
without alignment. The singular-value quantities of [LIT-tmpbknaa](LIT-tmpbknaa.md) and
[LIT-tmpzk5vb](LIT-tmpzk5vb.md) are unchanged by such permutations; this work's are not. So
the batch is "spectral" in two senses, and only the SVD sense is
invariant to relabelling units. Neither is wave mathematics in a
physical sense.

The causal step is also weak: interference is defined as amplitude
variance across models, its evidence is a correlation, and the merge that
reduces it most (Table 1) filters that very quantity by construction.
