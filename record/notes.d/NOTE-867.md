---
number: 867
status: Read
formerly:
- NOTE-tmpav8gn
paper: LIT-1066
title: Hutchins — How a cockpit remembers its speeds
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Read in full 2026-10-15 from the copy Hutchins posts on his own UCSD page (pages.ucsd.edu/~ehutchins/documents/CockpitSpeeds.pdf):
    a 24-page scan of the published article as typeset in Cognitive Science 19(3),
    pp. 265–288, with the journal's running heads and page numbers, made searchable
    by Acrobat Capture (OCR) in 2002. An earlier reader had downloaded it the same
    day; it was fetched again from the same URL on 2026-10-15 (HTTP 200, application/pdf)
    and the two files are byte-identical (SHA-256 3db8ebb3…8e31e16). Unpaywall also
    lists the article as free on the publisher's site (bronze, onlinelibrary.wiley.com/doi/pdfdirect/10.1207/s15516709cog1903_1);
    that copy was not fetched. The printed first page confirms pages 265–288. Text
    extracted with pdftotext, with and without -layout; the OCR garbles the abstract's
    line order in the plain extraction and some words ("tokes" for "takes", "AS1"
    for "ASI", "Vrer" for "Vref"), so the abstract was read from the layout extraction
    and Table 1 (p. 270, an image only) and Figure 4 (p. 282) were read from page
    images. Read: abstract, introduction, "Applying the cognitive frame", the flight-mechanics
    and crew-role background, all three descriptions of memory for speeds (procedural;
    outside the pilots; inside the pilots), "Cognitive properties of the cockpit
    system", the Discussion, footnotes, the references and the glossary. Nothing
    skipped. Cognition in the Wild (LIT-1060), which the paper cites as Hutchins
    1995, was not read, so what this paper says it argues is not checked. Every
    quotation below was checked against the extracted text by script, with whitespace
    normalised and the OCR's errors in the quoted passages corrected to the page
    image ("ASI" for "AS1", "Vref" for "Vrer"); all 71 quotations of the paper matched.
    The six quoted phrases not from the paper are from the record's own entries
    (QUESTION-101, CASE-085, LIT-1066).
date: '2026-10-15'
summary: >-
  In an MD-80 approach, the correspondence between airspeeds and wing configurations
  for the day's landing weight is computed once, 25 to 30 minutes before landing,
  by selecting a printed speed card with the displayed gross weight, and is stored
  in the positions of movable bugs on both airspeed indicators; when the plane slows
  10 to 15 minutes later, the needle's approach to a bug cues each flap call by
  a judgment of spatial proximity. Hutchins argues that this memory belongs to the
  cockpit as a functional system and that speed bugs do not improve any pilot's
  memory but replace a recall-and-scale-reading task with a perceptual one. The
  account is a stylized description of mandated procedure, informed by more than
  100 observer flights and simulator recordings, with no measured performance, no
  comparison of crews with and without bugs, and no failure cases; the claim that
  the arrangement changes what the system can do is established by analysis of the
  tasks, not by data.
---
<!-- inactive-ok-file: CLAIM-296 — Proposed; open claims and accounts cited as open, nothing here rests on their being settled -->
<!-- inactive-ok-file: LIT-1060 — Unavailable; held without a reading, cited as such -->

# NOTE-867: Hutchins — How a cockpit remembers its speeds

## Contribution

The paper applies the cognitive-science frame of representations and the processes that transform them to a unit larger than a person, the cockpit of a commercial airliner, and argues that "the classical cognitive science approach can be applied with little modification to a unit of analysis that is larger than a person". Its worked example is one task performed on every approach: remembering which wing configuration goes with which airspeed for the airplane's current weight, and the landing speed (Vref). It gives three descriptions of the same activity, procedural, then the representations outside the pilots, then the tasks this leaves to the pilots inside, and draws the conclusion that "The cockpit system remembers its speeds, and the memory process emerges from the activity of the pilots. The memory of the cockpit, however, is not made primarily of pilot memory."

## Key insight

Putting a representation into the right medium changes the task that the people in the system have to do, not how well they do the old one. Once the speeds are set as bugs on the airspeed indicator, "What was accomplished without speed bugs by remembering speed values, reading the ASI needle values, and comparing the two values is accomplished with the use of speed bugs by judgments of spatial proximity. Individual pilot memory has not been enhanced; rather, the memory function has now become a property of a larger system in which the individual engages in a different sort of cognitive behavior." So calling a bug a memory aid "is to mistake the cognitive properties of the reorganized functional system for the cognitive properties of one of its human components. Speed bugs do not help pilots remember speeds; rather, they are part of the process by which the cockpit system remembers speeds."

## Assumptions

- **The unit of analysis is the cockpit, and in particular a functional system.** The paper borrows Luria's term: "a constellation of structures, some of them internal to the human actors, some external, involved in the performance of some invariant task." The functional system of interest "is the one that controls the coordination of airspeeds with wing configurations."
- **Memory, for a system, means a saved representational state that later organizes activity.** "I call this entire process a cockpit system's 'memory' because it consists of the creation, inside the system, of a representational state that is then saved and used to organize subsequent activities."
- **The task is invariant, anticipated and mandated.** "Virtually all of the practices described in this paper are mandated by federal regulations and airline policy or both", and "nearly all" crews do them "on every flight". The speeds needed are known in advance, few (four bugs) and needed in a fixed order.
- **A stylized account, not observations.** "I will not present extended examples from actual observations ... Instead, I will present a somewhat stylized account". The procedures come from one major airline's MD-80 operations manual (proprietary, not named), informed by more than 100 observer flights, video and audio recordings of crews in high-fidelity simulators, and interviews (footnote 6).
- **The pilots' internal representations are inferred.** The pilots' memories are treated as "media that are not directly observable", of "unknown persistence". The third description reasons from what the external representations demand of the pilots to what they must do inside, and says "Lacking additional evidence, we cannot know the duration or quality of these memories."
- **Success is the norm.** "In all of my observations, never have I seen a crew fail to compute and set the approach speeds." Failure is mentioned only as possible ("sometimes crews do miss these procedures"); none is analysed.

## Key results

- **The speed card booklet is the system's long-term memory.** "The speed card booklet is a long-term memory in the cockpit system." It holds weight-to-speed correspondences, one card per weight interval (usually 2,000 lb), "functionally durable" for the life of the airplane and "nonvolatile", and is "not changed by any crew actions", with the operating manual's table as backup. Table 1 gives the same speeds for weights from 86,000 to 150,000 lb.
- **Retrieval by the booklet is done by filtering with a cue the environment supplies.** The gross weight, continuously displayed on the fuel quantity indicator, "is used as a filter on this written memory, making one set of speeds much more accessible than any other." Because weight and speeds are printed on the same card, "selecting the correct weight can't help but select the correct speeds." The open booklet then is a memory "for both the projected gross weight and the appropriate speeds", and "Once performed, the filtering need not be done again during the flight."
- **Posting the card distributes access.** Posting it where both pilots can see it "creates a distribution (across social space) of access to information", supports "redundant storage of the information and redundant processing", gives a new path by which speeds reach the pilot flying, and "provides a temporally enduring resource for checking and cross checking speeds, so that these tasks can be done (or redone) any time." Because the card carries the weight, it can be checked against the displayed weight a few inches away, a check on whether "the wrong weight, and therefore, the wrong speeds, may have been selected."
- **The same values are re-represented across media with different properties.** Printed card (permanent); the pilot not flying's spoken values ("ephemeral ... If it is to be processed, it must be attended to at the time it is created"), which also signal that bug-setting should begin; the pilot flying's readback; bug positions on two airspeed indicators, which are redundant and "a memory that is malleable, and that fits a particular period of time (this approach)", "quite resistant to disruption by other activities"; and the pilots' own memories. "The memory is stored ultimately for use in the physical state of the speed bugs. It is represented temporarily in the spoken interchanges, and represented with unknown persistence in the memories of the individual pilots."
- **Using the bugs, the regions of the dial carry meaning.** The bugs "segment the face of the ASI into regions", each associated with a flap/slat setting name; "Once the bugs are set, it is not necessary actually to read the scale values where they are placed. It is necessary, however, to remember the meanings of each of the bugs with respect to names for flap/slat configurations." As the needle nears a bug the pilot flying calls the setting, the pilot not flying moves the flap handle to the matching label, and "The speed bugs contribute to this process by providing the bridge between the indicated airspeed and the name of the appropriate flap/slat configuration".
- **Two task transformations on final approach.** With the salmon (command) bug, "a memory and scale reading task is transformed into a judgment of spatial adjacency." The pilot not flying can tell whether speed is within 5 knots of target by whether the needle points at the roughly ten-knot-wide base of the salmon bug, which "permits a conceptual task to be implemented by perceptual processes"; the base width was not specified for this purpose, an "opportunistic use of structure in the environment". The pilot not flying's callout then turns the pilot flying's visual task into "monitoring a particular aural cue". Each change "results in a change in the nature of the cognitive task facing the pilot" and changes "the kinds of internal knowledge structures that must be brought into play".
- **Redistribution across time.** "Speed bugs permit a shift in the distribution of cognitive effort across time. They enable the crew to calculate correspondences between speeds and configurations during a low workload phase of flight, and save the results of that computation for later use." Landing data are prepared "about 25 to 30 minutes prior to landing", because "crew workload is relatively light" then and "Later in the approach, the crew workload increases dramatically"; the bugs are used "ten to fifteen minutes later". "a properly set speed bug is much less likely than a pilot's memory to 'forget' its value", which lets the computation "be moved arbitrarily far in time from the moment of their use" and makes it "relatively insensitive to the interruptions, the distractions, and the delays that may disrupt internal memories."
- **Time available sets how much checking is done.** At the mandated slat-extension cross-check, "The depth of the processing engaged in here, that is, how many of these other checks are performed, may depend on the time available and the pilots' sense about whether or not things are going well." Tasks on final approach must be "as simple as possible because there are many other things the pilot must do". These are the paper's only statements about time pressure; none is measured.
- **Distribution across people.** The division of labour in which the pilot flying calls flaps and the pilot not flying sets them was likely justified by aircraft control, but "also has a very attractive system-level cognitive side effect" of redundant checking. On final approach, the pilot not flying watches airspeed and converts it to speech so the pilot flying can keep eyes outside.
- **Pilots' memory as reconstruction.** "The memory observed in the cockpit is a continual interaction with a world of meaningful structure." It is "not just the retrieval of something from an internal storehouse", but "a combination of recognition, recall, pattern matching, cross modality consistency checking, construction, and reconstruction" with representations "many of which permit, but do not demand, the reconstruction of some internal representation that we would normally call the 'memory' for the speed."
- **Media properties shape the system's properties.** "Such factors as the endurance of a representation, the sensory modality via which it is accessed, its vulnerability to disruption, and the competition for modality specific resources may all influence the cognitive properties of such a system." Of individual memory theory: "what the theory of individual human memory explains is not how this system works, but why this system must contain so many components that are functionally implicated in cockpit memory, yet are external to the pilots themselves."
- **On external memory.** "structure in the environment can provide much more than external memory (Norman, 1993)": the card selects as well as stores, and the bugs turn reading into seeing.

## Bearing on the record

**On [QUESTION-101](../questions.d/QUESTION-101.md): a worked answer for one class of tasks, of the form the question asks for, but argued and not measured, and for anticipated retrieval rather than search.**

- The question wants, for a stated class of tasks, when availability is a property of the system rather than any member, and "a case where changing the arrangement alone changes it." Hutchins's speed bugs are that case argued in principle: "Adding speed bugs to the system does nothing to alter the memory of the pilots, but it does permit a different set of processes to be assembled into a functional system that achieves the same results". The comparison is to an imagined functional system without bugs; no crews are compared and nothing is timed. The paper also says the bug system "achieves the same results" as the system without them; the gain it claims is lower demand on "scarce cognitive resources" and robustness to interruption and delay, not a different outcome. The record would need to say that a lower demand at the moment of use is what raises the chance of deployment in time.
- The class of tasks is narrow: a known, mandated, invariant task with a few values needed in a fixed order, prepared ahead in a quiet phase. Hutchins's answer is that the system remembers when the task's structure was anticipated and built into artifacts (card indexed by a displayed weight; bugs on the instrument where the value is used). [CASE-085](../cases.d/CASE-085.md) is the opposite class: one of many stocked items, needed unpredictably, located by a person's search on a spoken request. The paper says nothing about search through a store under a deadline, so it does not answer the question for the case the record is about. It does name what the ambulance lacked relative to the cockpit: the retrieval had not been prepared in advance, and nothing in the environment indexed location by the cue given.

**On [CLAIM-296](../claims.d/CLAIM-296.md): supports the relational reading and the separation of "has" from "can use", and adds that the cue can be engineered into the environment.**

- The claim's thesis, that deployability is a relation and not a property of any one element, is the paper's thesis for memory: the memory function is "a property of a larger system", and the paper's warning against crediting the bug to the pilot is the claim's warning, A17 §8, against treating a system failure as an individual's.
- The cue. The record adds the cue actually supplied (A19). In the cockpit the cue for both retrievals is supplied by the environment, not by a request: the displayed gross weight selects the card, and the moving needle approaching a bug prompts the flap call. Hutchins's design point is that a well-organized system does not leave the cue to a person's recall. That supports the claim's inclusion of the cue and adds that cue and store can be built together, which the claim does not say.
- The distinction between possessing information and deploying it. The paper shows it in the strong form A18 noted: what the pilots must hold in mind once the bugs are set is the meaning of each region, not the speeds, and the paper doubts bugs "contribute to the pilot's memory at all". The system deploys the speeds without either pilot needing to recall them. It does not show the converse case in the record, a resource possessed and known but not deployable, because it analyses no failure.
- The deadline. The paper has no deadline in the record's sense (a time τ by which retrieval must finish). Its time claims are about moving computation earlier ("arbitrarily far in time from the moment of their use") so that little remains at the moment of need, and about the time available setting how much cross-checking is done. That fits the claim's inclusion of the deadline and suggests a factor the claim does not list: when the work of retrieval is done relative to the deadline. The record's α as a probability of retrieval by τ treats retrieval as happening after the request; Hutchins's system does most of it beforehand.
- It does not contradict the claim. One difference of framing: the claim is about a physical resource, a drug; the paper is about information, speeds. Hutchins's memory is "a representational state", and the paper does not discuss locating objects.

**On [TERM-055](../terms.d/TERM-055.md): compatible; the paper locates the variable the term's supremum hides.**

- The term takes the supremum over procedures π available to the agent in the environment. Hutchins's analysis is about how the artifacts change which procedures exist ("permit a different set of processes to be assembled into a functional system") and so which cognitive task the person faces. That is consistent with the term, but the paper's interest is in the procedure actually assembled and its resource demands, which the supremum abstracts away. Two systems with the same α could differ in what Hutchins cares about: redundancy, cross-checking, and robustness to interruption.
- The paper's "redundant representation", "redundant processing" and the weight-against-card check address the term's fifth level from A17 §1, deploying the right thing (here, the right speeds for the right weight). It treats checking correctness as part of the same system, not a separate stage.
- The paper does not use or define any probability of deployment; it gives no rates, times or error frequencies beyond the remark that transposition errors are "probably" the most frequent in reading the card.

**On [CASE-085](../cases.d/CASE-085.md): an analogue that shows what an organized system adds, not evidence about the case.**

- The paper's counterfactual (the system without bugs) is of the kind A17's counterfactuals list: a change to the environment alone, the individual unchanged. The card-and-bug system is a worked version of A17's "labelled compartment" and "standard layout", with two additions: the index is driven by a cue the environment displays, and the result is posted where it will be used.
- It cannot say why retrieval failed in the ambulance, and its cockpit is a case of success. Its cross-checks and the depth of checking set by the time available are the nearest it comes to A17 §4's point that search spends what it needs.

**On [LIT-1066](../literature.d/LIT-1066.md)'s current summary.** The summary ("the memory for approach speeds ... is a property of the cockpit system ... not of either pilot alone") is fair. Hutchins also says the pilots' memories "clearly are involved" and the memory process "emerges from the activity of the pilots"; the claim is that the cockpit's memory "is not made primarily of pilot memory", not that pilots' memory plays no part. The paper's term "functional system" is taken from A. R. Luria (1979).

## Limitations

- No measurements: no timings, error rates, or comparison of procedures or crews. The system-level claims rest on task analysis of mandated procedure.
- One aircraft type (MD-80), one task, one airline's manual; the paper says similar procedures exist for every airliner.
- Only success is analysed. Missed speeds are said to be rare and dangerous ("killer" item) and are not examined.
- The pilots' internal memory is inferred from task demands; its duration and quality are explicitly left unknown.
- The task is anticipated and invariant; nothing on unanticipated retrieval or search among many items.
