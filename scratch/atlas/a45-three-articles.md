<!-- scratch/atlas/a45-three-articles.md -->

# The three articles of A45 (verbatim)

ChatGPT's A45 in the exchange "Hyper article interpretation" (2026-11-25), answering the owner's U21: "let's maybe break this up into separate articles: 1. presenting Nucleation's broader theory of inquiry in the abstract, 2. presenting Nucleation as a demonstration of how this theory can be operationalized via luria, 3. presenting the argument for Hyperarticles and presenting Nucleation as a reference implementation." Kept verbatim as the text the works conditions-of-correction, luria-beyond-software and hyperarticles are defined on (ADR-tmp85hdc). Its words are ChatGPT's; its codes are as at the time of the exchange.

---

I think these should be three **independently publishable articles**, not three installments of one essay. They have different theses, audiences, and standards of evidence.

The first develops Nucleation's philosophical account of inquiry, with its formal constructions and recorded cases. The second examines Nucleation as a concrete implementation of that account using Luria, including what worked, what failed, and what remains untested. The third derives the scholarly publishing proposal and uses Nucleation as a reference implementation of the underlying *research-record-and-view* architecture—not a completed hyperarticle publishing platform.

I've drafted them as companion papers. The Nucleation references remain parenthetical, and the extensions beyond the existing record are identified as such.

---

## Article 1 — The theory

<WritingBlock id="62948" variant="document"># Inquiry as a Governed Process
### Representation, legibility, learning, and the conditions of correction

*David Marx*

### Abstract

Inquiry is commonly described as a process of obtaining answers to questions. I develop a broader account in which inquiry can also revise the distinctions that make questions and answers possible. An inquiry is characterized by its language, answer space, available observations and interventions, evaluative criteria, and resources. These components constrain not only what an investigator can discover but what the investigator can formulate as a question. Representations that preserve the results of earlier inquiry can expand these capacities, although they can also entrench inadequate distinctions.

This account connects inquiry to three further problems: representation, legibility, and governance. A representation determines which distinctions can become operationally available. Legibility depends on whether a particular observer can recover and use those distinctions for a task. Governance determines whether recognized discrepancies can affect decisions and whether the rules governing those decisions can themselves be revised. Learning, on this account, cannot be reduced to accumulating information; it may involve developing maintained capacities that transfer beyond the circumstances that produced them.

I develop these relationships using claims and formal cases from the Nucleation inquiry, while distinguishing demonstrated separations from interpretive hypotheses and open questions.

## 1. Inquiry does more than answer questions

An inquiry ordinarily begins with a question.

But a question already assumes quite a bit.

It presupposes a language in which the problem can be stated, some distinction between possible answers, and some account of what would count as evidence for preferring one answer over another.

Often these assumptions are unproblematic. If I want to know whether a particular program terminates for a given input, I have a reasonably well-defined question and methods for investigating it.

Other questions are less cooperative.

Suppose I'm asking whether an organization has learned something, whether a translation preserves the meaning of an utterance, or whether two apparently different theoretical descriptions refer to the same phenomenon.

Part of the inquiry may involve figuring out what would even count as an answer.

This is the starting point for Nucleation's account of inquiry.

An inquiry is characterized by its language, answer space, interventions, observations, evaluative criteria, and resources. It becomes *reflexive* when some part of that specification becomes an object of inquiry itself (TERM-095).

The central claim is that inquiry is a form of specification, with an important difference from ordinary specification: inquiry can revise what an answer could be (CLAIM-470).

That distinction separates two kinds of progress.

One consists in making better selections among alternatives already recognized by the inquiry.

The other consists in revising the alternatives, or the standards used to evaluate them.

The second can be more consequential than the first. Discovering that two apparently distinct problems share a common structure can change what questions are worth asking. Discovering that an established category combines several importantly different phenomena can make a previously invisible disagreement tractable.

These aren't merely improvements in our answers.

They're changes in the machinery used to formulate and evaluate answers.

The account is developed across several entries, including the thematic synthesis of inquiry as specification (SYNTHESIS-114, Proposed).

## 2. The questions we can ask depend on what we can afford to distinguish

There's a resource implication here that I find particularly useful.

We usually think of research resources in terms of what it costs to answer a question: experimental equipment, computation, time, access to evidence, and so on.

But formulating the question also costs something.

You need concepts capable of expressing the distinction. You need enough background knowledge to recognize that the distinction might matter. You may need a mathematical apparatus before the question can be made precise enough to investigate.

Nucleation calls the set of questions an agent can practically formulate, given its available resources, its *inquiry frontier* (TERM-092).

This frontier isn't identical to the set of sentences expressible in the agent's language. Nor is it the set of questions the agent can successfully answer.

A question may be expressible without being practically formulable as a determinate research problem. It may be formulable without being answerable using available methods.

A stabilized specification can therefore function as stored work. It preserves distinctions that earlier inquiry made expensive to develop, allowing later investigations to use them without repeating the original process (CLAIM-475).

This explains part of the value of mathematical notation, experimental methods, and established theoretical frameworks.

A good abstraction doesn't merely summarize earlier findings.

It changes which subsequent investigations are feasible under a given resource budget.

But storing a specification can also have a cost. The same framework that makes one family of questions easy to formulate may make alternatives less apparent. A classification can become entrenched because the tools, procedures, and institutions built around it all presuppose its distinctions.

So expanding an inquiry's practical capabilities isn't necessarily equivalent to monotonically refining a fixed classification.

The inquiry frontier can change shape, not simply grow.

## 3. A representation makes some differences consequential

This brings us to representation.

It's tempting to treat a representation as a passive description of something that exists independently of it.

Sometimes that's a useful approximation. But for a system actually conducting an inquiry, the organization of a representation affects which distinctions can be recovered and used.

Nucleation adopts an operational notion of *apparatus*: an organization that selectively couples differences in one system to distinguishable outcomes in another. Such an apparatus may differentiate, retain, enforce, or revise distinctions. These functions are separable (TERM-089).

An apparatus can therefore make a difference operationally significant without establishing that its way of classifying the world is correct.

Consider a research community that maintains an impeccable record of its reasoning.

Every conclusion is linked to evidence. Every objection is documented. Every revision is attributable.

Unfortunately, the community's theoretical vocabulary excludes the correct explanation.

A less accountable community using better experimental interventions discovers what the first community cannot formulate within its existing scheme.

This is a formal illustrative case from Nucleation (CASE-084).

The point isn't that accountability is useless. Once the missing possibility becomes available, the first community's record might help it discover exactly where its assumptions failed.

The point is that **representational accountability and epistemic correctness are different properties**.

We should not infer that a coherent, fully traceable representation is a correct one simply because its own internal standards find no problems.

The same issue appears when an inquiry needs to revise its conclusions.

Two investigators can assign the same current probability to a hypothesis while maintaining different relationships between that hypothesis and a background condition.

When the condition is subsequently established, their probabilities should be updated differently.

The construction in Nucleation makes this exact: two joint distributions share a marginal probability of 0.9 for a hypothesis, but conditioning on the same observation changes the result to 1.0 in one and 0.8 in the other (CASE-093; CLAIM-294).

The current marginal doesn't preserve enough information for that revision.

But this doesn't establish that every inquiry should retain its entire history. Keeping the relevant joint distribution would suffice.

A complementary construction exhibits an agent whose current posterior is already sufficient for the decisions it needs to make, even though it cannot reconstruct how it arrived there (CASE-082).

Taken together, these examples establish an important limit.

**The usefulness of a representation depends on the decisions and revisions it must support.**

Historical accountability, correctness, and decision sufficiency can come apart (CLAIM-299; SYNTHESIS-017, Proposed).

## 4. Legibility isn't an intrinsic property of information

The same task-relative structure appears in Nucleation's account of legibility.

A distinction is legible to an observer when that observer, using its actual categories, rules, and resources, can recover the distinction from a representation and bring it to bear on a task (TERM-064).

The observer matters.

The task matters.

And the distinction between information being present and information being usable matters.

There's a particularly simple organizational case.

Suppose a worker reports an unsafe practice.

The event can be correctly classified by the equipment involved or by the obligations imposed on workers. Both descriptions are accurate.

But the organization's intake procedure requires one primary classification.

If the report is classified as an equipment problem, it goes to maintenance. If it's classified as a workplace-rights issue, it reaches a body authorized to reconsider working conditions.

Even indexing the report under both categories doesn't necessarily solve the problem. One classification may make it searchable without giving it a route to the relevant authority (CASE-132).

This is a constructed example, but it isolates a real distinction.

Compatible descriptions can produce different consequences because the institution's procedures act on the classifications.

The question isn't simply which description is true. It's which distinctions the institution can use to make the decisions available to it.

The formal account gives a corresponding condition.

An organization acting on its observations can select an acceptable action in every circumstance only if circumstances indistinguishable under the observation admit at least one acceptable action in common (CLAIM-535).

This means the distinctions an observer needs to make depend on what the observer must do.

A representation adequate for one decision can be inadequate for another.

Maximizing information isn't therefore a complete design objective.

We need to specify which distinctions matter, to whom, for which tasks, under which constraints.

## 5. Recognition is not correction

There's another step that can't be skipped.

Making a discrepancy legible doesn't establish that an organization can respond to it.

Nucleation distinguishes three achievements needed for a normatively relevant discrepancy to change an organization's behavior: recognition of the discrepancy, its capacity to influence action, and the practical availability of an appropriate correction (CLAIM-523).

These can fail independently.

An organization might recognize a problem and lack the authority to change anything.

It might have the authority but lack the resources.

Or its procedures might systematically prevent the relevant evidence from reaching the people who could respond.

A broader account distinguishes admission, recognition, credibility, uptake, and participation in revising the standards of uptake as separate stages (CLAIM-403; SYNTHESIS-111, Proposed).

This is not merely an information problem.

An organization can also become dependent on an apparently successful interpretation because that interpretation controls which evidence is subsequently admitted or how new evidence is scored.

Nucleation contains computational constructions in which an inferior perspective retains authority through feedback involving evidence selection and evaluation (CASE-162).

Correcting selective admission and correcting biased scoring are different problems. An intervention that addresses one need not address the other (CLAIM-466).

The implication is that a system's apparent ability to process information does not establish its ability to correct its own commitments.

Nor does responsiveness under existing rules establish responsiveness to reasons for changing those rules.

The stronger question is whether the organization can revise the procedures through which it recognizes and evaluates discrepancies.

## 6. Learning requires more than retaining information

This suggests another distinction.

A system can retain information without acquiring a new capability. It can also perform better on an immediate task without maintaining the improvement.

Nucleation's account of *self-formation* isolates one route by which a system acquires a durable new capacity.

An unresolved discrepancy can occasion the development of a new distinction or action channel that persists beyond the initial problem and transfers to later problems of the same class (CLAIM-532).

A formal construction makes the idea precise.

An agent initially has one shared output and cannot satisfy two demands that require different responses in different contexts.

Its activity in response to that discrepancy produces a sensing capacity and a differentiated action channel.

Those capacities subsequently maintain one another. The original conflict disappears, but the agent retains the new organization and can handle later discrepancies of the same class (CASE-191).

The construction shows that a persistent capability can be distinguished from a temporary response.

It doesn't establish that every instance of learning has this form, or that discrepancies automatically produce self-formation. The broader relationship remains qualified (SYNTHESIS-116, Proposed).

Still, this provides a useful account of why merely accumulating records is not the same as learning.

A record is valuable when it contributes to maintained capacities for discrimination, investigation, judgment, or action.

That may involve storing an answer.

But it may also involve developing a new question, changing a classification, improving a method, or revising the criteria used to decide whether an answer is acceptable.

## 7. Inquiry has to be able to reconsider its own apparatus

The argument now comes back to its starting point.

If inquiry can revise its specification, and representations help determine which distinctions become operationally available, then the machinery of inquiry is itself a legitimate object of inquiry.

That doesn't mean every system capable of modifying its rules governs itself.

A programmable system can change its behavior according to externally supplied criteria. A system can also modify its own criteria badly.

The capacity to revise a standard and the capacity to revise it appropriately are distinct (CLAIM-424).

Nucleation therefore leaves open important questions about what distinguishes adaptation, reflexive inquiry, and self-governance (QUESTION-388; SYNTHESIS-114, Proposed).

But the distinction gives us a useful standard for evaluating systems intended to support inquiry.

We should ask whether they can preserve consequential distinctions, make relevant discrepancies legible, and support justified revision when their existing representations or procedures fail.

And we should assess these capabilities against external tasks, not merely against the system's ability to reproduce its own records.

A coherent record of an incorrect theory is still an incorrect theory.

A documented objection that never reaches a relevant decision is not an effective correction.

A growing collection of propositions is not necessarily evidence that anyone has learned.

The broader proposal is that inquiry should be understood as the development and maintenance of capacities for asking, distinguishing, evaluating, and revising—not simply the accumulation of answers.

That has implications for how we design knowledge systems.

It also has implications for scientific institutions, including the ways we represent and evaluate the work of research.

Those applications require additional arguments and tests. The account of inquiry by itself does not establish any particular software architecture or publishing model.

But it gives us a better set of questions to ask of them.

### Record and scope note

This article is a proposed thematic view over Nucleation's accounts of inquiry, representation, legibility, governance, and learning. Its central components are recorded in SYNTHESIS-114, SYNTHESIS-012, SYNTHESIS-017, SYNTHESIS-111, and SYNTHESIS-116. Those syntheses are Proposed and inherit the limitations of their component claims.

The cited cases are persisted Nucleation records. Formal constructions establish the separations they were designed to exhibit; they should not be read as empirical generalizations to all scientific or institutional inquiries.

Source: [Nucleation at revision aa259663](https://github.com/dmarx/nucleation/tree/aa2596632e4949c3fe3dd64b4870a92f04a0547f).</WritingBlock>

---

## Article 2 — The operational demonstration

<WritingBlock id="24861" variant="document"># Governing an Inquiry
### Nucleation as a case study in applying Luria beyond software development

*David Marx*

### Abstract

A persistent record of a research conversation is not necessarily a usable record of the argument developed in that conversation. Claims can be silently reformulated, objections rediscovered, and earlier decisions forgotten despite the availability of complete transcripts. I developed Luria to address similar continuity problems in LLM-assisted software development, then applied its governance machinery to Nucleation, an ongoing philosophical inquiry.

This article examines that application as a case study in operationalizing distinctions among inquiry, representation, legibility, and governance. It describes the record's source-and-view architecture, the separation of claim identity from epistemic standing, and the procedures used to revise the representational grammar. Recorded cases show both successful correction of representational misfits and limitations that the machinery cannot resolve. I distinguish these observations from the empirical claim that governed records improve inquiry relative to less structured alternatives, which remains to be tested.

## 1. Why a transcript isn't enough

I initially developed Luria because I was having trouble maintaining continuity in an LLM-assisted pair-programming collaboration.

We were building a web application.

The assistant could help investigate implementation approaches, compare alternatives, and produce code. But continuity across sessions was unreliable.

An earlier decision might still exist somewhere in the transcript without being used when a later decision depended on it.

A rejected design might be proposed again. A requirement could change without the consequences being traced through the implementation.

The problem wasn't always missing information.

It was missing structure around what that information meant and how it was supposed to remain consequential.

So I developed a process for recording decisions, their status, their justifications, and their relationships to other parts of the project.

I eventually extracted that process into [Luria](https://github.com/dmarx/luria).

The aim was to make the governance machinery reusable, rather than build a custom memory system for each project.

Nucleation was the first project outside the original webapp and Luria itself to use that machinery.

That matters because Nucleation isn't a software-development project. It's an ongoing philosophical inquiry, conducted extensively through collaboration with LLMs.

The question was whether the same general approach could maintain the structure of an evolving argument.

## 2. What Luria maintains

Luria's core objects are identifiable records with declared relationships and standing.

A record can remain identifiable while its standing changes. A decision can be proposed, adopted, and eventually superseded.

The distinction between identity and standing is important because historical existence and current authority are not the same property.

Luria also treats references as more than strings that happen to name files.

An implementation can depend on a decision. A decision can supersede another decision. A design can extend an earlier design without retiring it.

Those relationships have different semantics.

When a referenced decision changes standing, Luria can identify dependent records that may require reconsideration.

That doesn't mean the machinery determines what the new decision should be. It makes the maintenance obligation available for review.

The distinction also applies to corrections.

If the reason for a decision was mistaken but the choice remains valid, the appropriate action is not necessarily to supersede the choice. Luria's decision doctrine permits a versioned correction of the justification while preserving the decision's identity (Luria ADR-019).

And not every suspicious dependency needs to be prohibited. The consequences of a finding depend on the project's rules and use of the relevant object (Luria ADR-035).

These are relatively modest mechanisms.

But they distinguish a record that merely remembers what was written from one capable of governing the consequences of changes to what was written.

## 3. Nucleation required a different grammar

Nucleation couldn't simply inherit the original software project's record types.

A philosophical inquiry needs to distinguish questions, claims, definitions, examples, arguments, literature, and the relationships among them.

Some objects represent positions the inquiry currently adopts.

Others record objections, suppositions, unresolved questions, or alternative interpretations.

Nucleation therefore introduced separate schemes for those intellectual objects, along with relationships for grounding, contesting, refining, and revising them (ADR-032).

The separation emerged from examination of actual research exchanges.

Those exchanges exhibited repeated failures of argumentative identity: concepts were silently redefined, objections were re-derived, and later accounts omitted earlier commitments without identifying what had changed (CLAIM-177).

A second coding exercise found similar identity failures in another exchange, although the study's limited scope and coding procedure leave the wider generalization open (CASE-306, Proposed).

This motivates an important difference between a conversation archive and a maintained argument.

The archive records turns.

The argument record identifies the intellectual moves made in those turns and maintains their standing and relationships.

Consider the distinction between a claim's status, role, and warrant.

An argument can contain a counterclaim without adopting it. A claim can be actively entertained without being demonstrated. A formal consequence can hold under stated assumptions without establishing the assumptions.

Nucleation separates these properties rather than asking a single status field to do all the work (ADR-043).

The result is a record whose structure corresponds more closely to the distinctions the inquiry needs to maintain.

Not perfectly, as it turns out.

## 4. The graph that invented a dependency

One of the most instructive examples is a failure of Nucleation's own machinery.

During the development of a line of inquiry, a claim was recorded as providing support for an earlier claim.

The relation-fixing machinery wrote a converse dependency indicating that the earlier claim *rested on* the new one.

But the earlier claim had already been argued independently. The new material corroborated it without being a necessary premise.

The record had generated an inference nobody made.

The corrective action was not merely to fix the affected entry. The record's representational grammar needed another relation capable of expressing corroboration without dependency.

The false dependency was removed and the vocabulary revised (CASE-131).

This is a useful test of the general account developed in the companion theory paper.

The record's grammar made a distinction operationally available, but the distinction was wrong for the intended argumentative relationship.

The system was functioning according to its rules and nevertheless misrepresenting the inquiry.

The correction required revising those rules.

This also identifies a limitation.

The false relation was noticed partly because it produced an identifiable inconsistency with the history of the argument.

A different representational mistake might have been accepted without producing anything obviously wrong.

The example establishes that a recognized misfit can motivate grammar revision.

It doesn't establish that every important misfit is recognized (CLAIM-181, Proposed; CLAIM-419, Active).

## 5. The record has a history of revising its own representation

We can examine how exceptional that kind of change was.

Nucleation includes a census of its governance decisions through November 20, 2026.

Of the first 114 decisions examined, 88 changed the record's grammar. Sixty-two were classified as refinements, 25 as revisions, and one as a restraint on a proposed change.

The coding distinguished changes that added detail within existing categories from changes affecting what counted as a category, an answer, or a unit of inquiry.

The review also examined which problems motivated changes and who recognized, proposed, and authorized them (CASE-300).

This is not an experiment showing that Luria outperforms an alternative system.

It's a descriptive study of what happened within one project.

But it establishes that the record's grammar wasn't simply designed once and held fixed.

The inquiry encountered representational requirements and changed its infrastructure in response.

The distinction between refining the record and revising its categories was itself part of what the study attempted to measure.

That makes Nucleation an interesting example of an inquiry in which the machinery used to represent the inquiry can become an object of inquiry.

There is an additional complication: the categories used to code the history are themselves choices made by investigators.

A record's own measurements cannot certify that its representation is correct merely because they report coherent patterns within it.

The census needs to be interpreted under that limitation.

## 6. The source record and its views are different objects

Luria distinguishes the maintained source from projections generated over it.

This is a design principle motivated by software-maintenance failures: manually maintained representations of the same underlying information tend to drift apart (Luria DP-003).

For example, if a set of records declares relationships in local fields, a higher-level lineage can be derived by traversing those relationships.

That is preferable to repeating the lineage in prose across several files and maintaining all those descriptions independently (Luria ADR-083).

Nucleation uses generated indexes, line views, status views, and syntheses to help readers navigate its material.

These are different organizations of the same underlying source records.

The distinction also reveals a problem with manuscript production.

In one documented reconstruction of a research exchange, a manuscript drafted directly from the conversation changed the apparent thesis without an intervening argumentative move and omitted 24 items from the reconstructed argument (CLAIM-324).

The broader inference—that maintaining an argument record provides a more reliable basis for drafting manuscripts—remains Proposed (CLAIM-178).

There are at least two things we shouldn't infer from that result.

First, an omission isn't necessarily an error. A good exposition often excludes material that doesn't belong in the presentation.

Second, the record can expose only omissions relative to what it successfully captured.

But the finding identifies a useful capability.

If the manuscript is one view over a separately maintained argument, we can ask which commitments it includes, which it excludes, and whether substantive changes have been introduced without being justified.

That's more informative than treating the finished manuscript as the only surviving version of the argument.

## 7. What does the additional structure cost?

There's an obvious danger in this approach.

I started building the tooling partly because reconstructing intellectual context was expensive.

If the solution requires more work to maintain than it saves, I haven't solved the problem.

Nucleation contains an illustrative cost model addressing exactly this issue.

In one construction, a recurring objection becomes worth filing after enough later uses make retrieval cheaper than re-derivation.

In another, an argument that will never be reused costs more to file than it would have cost to reconstruct. The storage succeeds, but the investment doesn't pay for itself (CASE-088).

That isn't empirical evidence for a particular break-even point in actual research.

It's a reminder that the value of structure depends on reuse, retrieval costs, and the consequences of failing to maintain it.

Luria's own principles reflect the same concern.

Important information should be captured while its context is available rather than reconstructed later. But the filing process has to be cheap enough that this remains worthwhile (Luria DP-008).

LLMs may help reduce the cost of identifying candidate claims, relations, and revisions.

That creates another governance problem, though.

An assistant can generate a plausible argument without establishing that the argument should be adopted.

Nucleation's dialectic procedures allow an assistant to file developing material while reserving consequential decisions—such as changes of standing and governance—for the owner (ADR-127).

This separates assistance in maintaining the record from authority over its epistemic commitments.

It doesn't make the record infallible. It makes the allocation of responsibility more explicit.

## 8. What Nucleation demonstrates

I think Nucleation supports a fairly specific conclusion.

The same underlying governance machinery can be used to maintain a software project and a philosophical inquiry with substantially different record types.

Within the inquiry, explicit identities, statuses, and relations make certain argumentative and representational changes available for inspection.

The record has also encountered failures in its own representational grammar and revised that grammar in response.

These are observable properties of the system.

What remains open is whether this produces better inquiry at acceptable cost.

Nucleation includes proposed experimental designs for evaluating that question.

One compares forms of persistent memory on revision tasks where the correct answers are known (CASE-091).

Another compares conversational coordination, summaries, shared notes, typed records, and governed records on tasks requiring distributed evidence integration (CASE-252, Proposed).

A third tests whether explicit governance improves the benefits of modifiable schemas when the original categories are inadequate, while including controls where no schema change is warranted (CASE-253, Proposed; CLAIM-667, Proposed).

These are the kinds of tests that would let us move beyond demonstrating that the system can maintain a structured record.

The more interesting question is whether researchers using the system become better able to resume, revise, and extend their inquiries.

That is not settled by the fact that Nucleation exists.

But Nucleation gives us a concrete implementation against which the question can be asked.

### Record and scope note

This paper treats Nucleation as an operational case study, not a controlled evaluation of Luria's benefits.

Its principal sources are the project's governance decisions (ADR-032, ADR-043, ADR-127), evidence about argumentative continuity (CLAIM-177, CLAIM-324), and persisted cases concerning representational misfit, grammar revision, and maintenance cost (CASE-131, CASE-300, CASE-088).

The claims about general usefulness and comparative research performance remain hypotheses for further testing.

Sources: [Nucleation](https://github.com/dmarx/nucleation/tree/aa2596632e4949c3fe3dd64b4870a92f04a0547f) and [Luria](https://github.com/dmarx/luria/tree/863ebbed27cb5f2bda58f4f49b54fbf180c64ca3).</WritingBlock>

---

## Article 3 — The publishing proposal

<WritingBlock id="24862" variant="document"># One Inquiry, Many Articles
### Hyperarticles, editorial feeds, and scientific publishing over governed research records

*David Marx*

### Abstract

The conventional scientific paper combines several functions that need not be performed by the same object: communicating an argument, identifying scholarly contributions, preserving the research record, receiving editorial evaluation, and providing a unit for academic assessment. I propose separating these functions.

A *hyperarticle* is a coherent narrative view over a maintained collection of versioned research objects. The underlying record preserves the identities, relationships, standing, and revision histories of claims, arguments, evidence, and other contributions. Different articles can present different selections of the same research to different audiences without requiring independently maintained copies of the underlying work.

I develop this proposal from the source-and-view architecture of Luria and the Nucleation inquiry, which serves as a reference implementation of the governed research substrate. Extending the separation to editorial evaluation suggests journals as feeds over independently attributable editorial judgments, with publishing and preservation treated as infrastructure services. I consider consequences for academic incentives and AI-assisted education, while distinguishing the implemented record from the proposed scholarly publishing network.

## 1. Why am I writing another paper about the same research?

I have a practical problem with academic publishing.

I like developing theories. I enjoy pursuing their implications, finding objections, and revising the argument when something doesn't work.

I have a much harder time stopping that process to manufacture a self-contained manuscript.

Part of this is a consequence of my ADHD. The activity that keeps me engaged is developing the inquiry, not reconstructing it into a publication.

But there's a more general problem.

Suppose a theory has implications for machine learning, statistics, philosophy, and organizational behavior.

Each community has different interests. Each expects a different explanation of why the work matters.

The obvious publishing strategy is to produce several papers.

One presents the formal result. Another develops the philosophical implications. Another describes an application. Another introduces the general framework.

Each paper repeats some of the same background, definitions, and arguments.

And each becomes another independently maintained representation of the theory.

If the theory changes, I have to determine which papers depend on the revised material.

This seems unnecessarily expensive.

Why should the intellectual structure of one inquiry be divided according to the document boundaries required to communicate it to different audiences?

I'd rather maintain the research itself and provide as many presentations of it as are useful.

## 2. An article is already a view

An article is a selection from a larger body of intellectual activity.

The author chooses which questions to introduce, which claims to defend, which examples to include, and which qualifications need to be explained.

A good article doesn't reproduce everything that happened during the inquiry.

It constructs a useful path through the material.

That sounds a lot like a view over a database.

The view selects and organizes information from an underlying source according to some purpose.

The problem with conventional scholarly publishing is that the view often becomes the canonical object.

The research record may consist of notebooks, code, correspondence, experimental logs, drafts, and private notes. But the thing that receives a stable scholarly identity is the finished paper.

Nucleation suggests a different arrangement.

The source record maintains identifiable questions, claims, arguments, terms, cases, and syntheses.

Their relationships and standing are explicit.

A narrative can then select from those records without becoming the sole authority over what they say.

Luria already uses a similar separation. Its generated indexes and lineage views are derived from authoritative records rather than separately maintained copies (Luria DP-003; Luria ADR-083).

Nucleation also includes a specific proposed argument for treating manuscripts as views over separately maintained arguments (CLAIM-178, Proposed).

The argument was motivated partly by an observed failure during manuscript drafting. A draft produced from a research exchange introduced a change of thesis that hadn't been argued for and omitted material from the reconstructed argument without identifying what had changed (CLAIM-324).

A good article may legitimately omit material. The problem is not omission itself.

The problem is losing the ability to distinguish deliberate selection from an unnoticed change in the underlying argument.

A maintained record gives us something against which to check the presentation.

## 3. What I mean by a hyperarticle

I'm calling the proposed publication object a *hyperarticle*.

The name isn't meant to imply that adding hyperlinks to a PDF constitutes a new publishing paradigm.

The important change is the relationship between the article and its source.

A hyperarticle is a readable narrative whose substantive components can refer to independently maintained research objects.

Those objects have stable identities and version semantics.

A claim can be cited independently of the article that introduces it.

An objection can identify which claim it challenges.

A reader can inspect the evidence and argument supporting a conclusion.

And a later revision need not silently overwrite the state of the work that an earlier reader or reviewer encountered.

This doesn't require every sentence to become a separately identified object.

Nor does it require articles to be written automatically.

The article remains an authored narrative.

The difference is that the intellectual objects it presents don't exist exclusively inside that narrative.

Consider a research result that matters to several communities.

A statistician may need to inspect its assumptions and derivation.

A philosopher may want the argument's interpretation and its relationship to competing theories.

An applied researcher may care about implementation details and performance under particular conditions.

These can be different presentations of the same underlying result.

They don't have to become different canonical results merely because the audiences differ.

Nucleation contains a useful case about audience-relative evaluation, although it concerns literary translation rather than scientific publishing. Different critical communities evaluated the same translation against different tasks and reached different judgments about its success (CASE-067).

The case doesn't prove that hyperarticles are useful.

It illustrates why there need not be one privileged presentation or evaluation of a complex object.

What matters to one audience may not be the distinction another audience needs.

A hyperarticle supports different paths through the research while keeping the underlying objects and their histories connected.

## 4. Nucleation as a reference implementation

I think Nucleation is useful here because it isn't merely an imagined example.

It's a working inquiry maintained through Luria.

Its record contains source objects with stable identities and declared relationships. Claims have distinct statuses, roles, and warrants (ADR-032; ADR-043).

Its generated documentation supports different ways of navigating the same material.

And its own philosophical arguments concern precisely the problems that this publishing model is intended to address: representation, revision, legibility, and governance.

For example, the record distinguishes historical accountability from epistemic correctness and from decision sufficiency (CLAIM-299).

Its supporting constructions show why current conclusions may fail to preserve enough information for certain revisions, while also showing why preserving the entire history is not always necessary (CASE-082; CASE-093).

A hyperarticle drawing on those results can present the conclusions in a readable sequence while leaving readers access to the constructions and their limitations.

That's already the pattern this article is trying to demonstrate.

But I want to be precise about the word *implementation*.

Nucleation is a reference implementation of the underlying **governed research record** and of generating different navigational views over that record.

It is not yet a complete implementation of hyperarticle publishing.

In particular, the present system doesn't automatically compose publication-ready prose, manage a distributed editorial network, or provide all the identifier, archival, and version-resolution guarantees scholarly publication would require.

This article is manually composed.

The source records already exist separately, and the references permit inspection.

That's a partial implementation of the proposed relationship, not proof that the whole publishing architecture works.

The distinction matters because the entire argument is about refusing to confuse an attractive representation with the thing it's supposed to represent.

## 5. One body of research, as many views as we need

There's a direct consequence for scholarly productivity.

A complicated research program often generates a flood of interrelated papers.

The papers may share definitions, assumptions, results, or substantial portions of the same argument.

The author is encouraged to present each as a sufficiently independent contribution to merit publication.

But those publication boundaries need not correspond to independent intellectual work.

With hyperarticles, the underlying theory can remain one maintained, interconnected body of research.

Different expositions can draw from it.

Different reviewers can evaluate different parts of it.

Different communities can cite different contributions without requiring those contributions to be packaged into separate canonical manuscripts.

This doesn't mean researchers should never write more than one article about a body of work.

Separate expositions can be genuinely valuable.

The point is that exposition becomes a choice about communication rather than a requirement for establishing the identity of the contribution.

I should be able to present an argument to a philosophical audience, explain its formal apparatus to mathematicians, and discuss its engineering implications with software developers without pretending that these are three unrelated bodies of research.

**One body of work. Multiple audiences. Multiple presentations. A shared intellectual history.**

## 6. A journal is a feed over editors

Once the research can be published independently of the journal that evaluates it, the role of editorial institutions becomes more interesting.

I've been looking at the [AT Protocol](https://atproto.com/) as a possible architectural precedent.

The relevant feature isn't social media. It's the separation of hosting, identity, independent labeling, and feed generation.

Different services can produce views over content that they don't own.

A scholarly system could use a similar separation.

Suppose an editor evaluates a particular version of a research result.

The editor records what was assessed, the judgment reached, and the grounds for that judgment.

Another editor might evaluate the same result for a different purpose.

One may judge its formal derivation sound. Another may consider its interpretation overstated. A third may find it particularly useful to a different field.

These are different assessments.

We shouldn't collapse them into a single undifferentiated endorsement.

Nucleation already distinguishes a claim's standing, argumentative role, and warrant because those properties cannot safely be treated as equivalent (ADR-043).

Editorial judgments need at least comparable specificity.

A recommendation isn't a replication.

A methodological criticism isn't necessarily a refutation.

An interesting conjecture isn't a demonstrated result.

Now suppose a journal maintains an editorial board and a policy for aggregating those assessments.

The journal can produce a feed of the research its editors recommend, review, or otherwise judge relevant.

**A journal is a feed over editors.**

The journal need not own the underlying work.

The same research object can appear in multiple journals for different reasons.

Editors can contribute to multiple journals without recreating their assessments.

Readers can follow journals, individual editors, or feeds assembled from several editorial sources.

A journal becomes a maintained editorial perspective rather than an exclusive gatekeeper to the scientific record.

There's a further distinction that I think deserves to be treated as part of the architecture:

**A feed is a view with a memory over data.**

A view selects and organizes records.

Its memory preserves the history of those selections, the policies applied, and the decisions that caused them to change.

A journal issue could be a snapshot of that feed at a particular time.

The journal itself would remain an ongoing, inspectable editorial process.

This is a proposal. Bluesky's existing moderation labels are not sufficient scholarly review records.

We would need a more expressive model for assessment scope, versioning, evidence, conflicts of interest, and editorial governance.

And decentralization doesn't automatically produce independent or reliable evaluations.

Nucleation contains computational cases illustrating how evidence selection and self-scoring can create reinforcing authority loops, even when the preferred interpretation is inferior (CASE-162; CLAIM-466).

A decentralized journal system needs to take those risks seriously rather than assume that removing a centralized publisher removes editorial capture.

## 7. The publisher doesn't need to own the judgment

If authors maintain their research and editors independently assess it, what remains for the publisher?

Hosting, preservation, versioning, identifiers, metadata, and accessibility.

Those are substantial responsibilities.

But they're infrastructure responsibilities.

A scholarly research object should retain its identity when its hosting arrangement changes.

A citation should identify the object and version relevant to the citation, rather than depending entirely on a particular server continuing to exist.

And an editorial assessment should remain attributable to its editor even if that editor or the journal changes organizations.

Different services could meet different parts of the publishing requirement.

One might host the current state of a research project. Another might archive immutable versions. Another might register persistent identifiers. Another might specialize in interactive rendering.

This architecture doesn't eliminate publishers.

It separates publishing infrastructure from editorial authority.

That makes the functions easier to evaluate independently.

A hosting provider should be accountable for access and preservation.

An editor should be accountable for the quality and scope of an assessment.

A journal should be accountable for its editorial policy and the judgments of its contributors.

There's no compelling reason these must all be functions of one institution.

## 8. What happens to publish-or-perish?

There's a broader incentive problem here.

Suppose I spend a year improving a theory.

I discover that an earlier formulation was too strong. I establish a narrower result, incorporate neglected literature, and revise a conceptual framework so that a new family of questions becomes tractable.

I've improved the research.

But perhaps I haven't produced another paper.

Now suppose I divide the same work into five manuscripts.

Suddenly I have five countable outputs.

Did I produce five times as much knowledge?

Obviously not.

I produced five documents.

The distinction matters because academic evaluation often uses publication output as a proxy for contribution.

That gives researchers an incentive to organize their work into publishable units even when the resulting divisions complicate maintenance or duplicate explanation.

A governed research record could make other contributions independently attributable.

Originating a theory, demonstrating a result, finding a counterexample, repairing an argument, and maintaining a synthesis are different kinds of intellectual work.

All can be valuable.

And sometimes maintenance means removing something rather than adding another contribution.

Retiring an unsupported claim can improve a research program.

Correcting a misleading classification can improve future inquiry.

An academic evaluation system should be able to recognize those accomplishments without requiring each one to become another paper.

But I don't want to replace publication count with claim count.

If institutions reward the number of maintained records, we'll encourage researchers to manufacture records.

The same problem can recur under any convenient proxy.

Nucleation's account of institutionally operative categories warns that a classification system can help produce the regularities later taken as evidence of its validity (CLAIM-402).

A better approach is to make substantive contributions more legible to evaluators, without pretending the record itself computes their intellectual value.

A research portfolio could be a view over a maintained body of work.

A committee could inspect the important claims, evidence, corrections, independent assessments, and the researcher's specific contributions.

The portfolio provides evidence for evaluation.

It doesn't replace the evaluator's judgment.

## 9. There's an educational version of this problem

The title has another intended meaning.

We've been telling students to show their work for a long time.

The reason is straightforward: a correct final answer doesn't necessarily demonstrate understanding.

LLMs make that distinction more important.

A student can use an LLM to generate a plausible solution without understanding it.

But they can also use an LLM to explore an approach, identify a faulty assumption, construct a counterexample, and develop a correction.

Those are very different performances.

A structured collaboration record could make them easier to distinguish.

Luria was originally developed to govern precisely this kind of human–LLM work.

Its principles require important project knowledge to be available in a shared record rather than remaining in private agent memory (Luria DP-007).

Nucleation's governance procedures distinguish assistant-generated contributions from consequential decisions reserved for the inquiry's owner (ADR-127).

That distinction doesn't establish who understands what.

The record itself explicitly distinguishes publicly inspectable epistemic commitments from the private beliefs and knowledge of the participants (TERM-119; CLAIM-668, both Proposed).

But it creates an opportunity for better assessment.

Instead of trying to determine whether a student used an LLM, an instructor could evaluate how the student used it.

What did the model contribute?

Which proposals did the student adopt?

Which did they reject, and why?

Can they defend the resulting argument or solve a related problem independently?

A provenance record wouldn't replace examinations or other independent tests of understanding.

It could give those evaluations a more informative starting point.

The educational proposal also raises serious privacy, authenticity, and maintenance-cost concerns.

I wouldn't want every student compelled to record every thought or interaction.

Still, the principle is worth investigating.

Use the tools.

Keep track of what they contributed.

Show what you did with the results.

## 10. What would establish that hyperarticles are better?

The architecture is attractive to me partly because it responds directly to problems I've encountered maintaining research.

That isn't sufficient evidence that it's a better publishing system.

We'd need to test the specific benefits.

Can readers reconstruct the standing and justification of a result more accurately when given a hyperarticle and its source record?

Can authors identify the consequences of a revision across multiple presentations?

Does a shared underlying corpus reduce contradictory definitions and duplicated maintenance?

Can reviewers produce more precise evaluations when the objects under review have stable identities and explicit version references?

And does the additional machinery cost less than it saves?

Nucleation already contains experimental proposals relevant to some of these questions, including comparisons among different kinds of persistent memory and governance arrangements (CASE-091; CASE-252 and CASE-253, Proposed).

A publishing-specific research program would need to extend those designs.

The relevant dependent variable isn't the number of claims successfully converted into structured records.

It's whether the resulting system improves communication, correction, attribution, and subsequent inquiry at an acceptable cost.

A perfectly maintained research graph can still contain an incorrect theory (CASE-084).

A complete history can be unnecessary for decisions whose current state is already sufficient (CASE-082).

A citation graph alone cannot determine how an argument should change when evidence is withdrawn (CASE-089).

These aren't reasons to avoid governed research records.

They're reasons to evaluate the proposal against the tasks it's actually intended to support.

## Conclusion: publish the research

Nucleation is currently an ongoing inquiry maintained through Luria's governance machinery.

Its claims, arguments, cases, and syntheses have identities and standing independent of the essays that might be written about them.

Its generated documentation already provides multiple ways of navigating the work.

And it contains examples of its own representational machinery being revised when the inquiry exposed a weakness in that machinery.

That makes it a useful reference implementation for the underlying record-and-view approach.

A complete hyperarticle publishing ecosystem would extend this arrangement with durable scholarly identifiers, versioned narrative views, independently attributable editorial assessments, and interoperable hosting and preservation.

The broader proposal is to stop asking the paper to serve simultaneously as the presentation, source of truth, unit of attribution, and object of editorial control.

Maintain the research.

Let articles present different views of it.

Let editors assess identifiable contributions.

Let journals curate those assessments.

Let publishers provide the infrastructure.

And let institutions evaluate the substance of scholarly work rather than relying so heavily on the number of documents produced.

I'm not claiming the entire system already exists.

I'm arguing that the distinction between the research and its presentations is useful enough to take seriously, and that Nucleation provides a concrete starting point for investigating it.

The paper is a view over the argument.

The argument is the thing we're maintaining.

**Just show your work.**

### Record and scope note

This article is a proposed publishing argument using Nucleation as a reference implementation of the underlying governed research record, not of the complete hyperarticle ecosystem.

Its principal Nucleation dependencies concern manuscript views (CLAIM-178), source-record accountability (CLAIM-299 and SYNTHESIS-017), task-relative legibility (TERM-064), representations as operational apparatuses (CLAIM-469), and the governance of correction (CLAIM-523).

The hyperarticle publication contract, editorial-feed architecture, portable publishing arrangements, and proposed educational applications would require additional CLAIMs, ARGs, and evaluation cases if adopted into Nucleation.

Sources: [Nucleation](https://github.com/dmarx/nucleation/tree/aa2596632e4949c3fe3dd64b4870a92f04a0547f) and [Luria](https://github.com/dmarx/luria/tree/863ebbed27cb5f2bda58f4f49b54fbf180c64ca3).</WritingBlock>

---

## How these should fit together in Nucleation

I'd treat the three articles as **separate governed works with overlapping dependencies**, not as three versions of the same argument.

<box border radius="xl" padding={3} gap={2}>
  <box background="surface-secondary" padding={3} radius="lg" gap={1}>
    <text color="secondary" weight="medium" size="xs">ARTICLE 1 · THEORY</text>
    **Inquiry as a Governed Process**

    <text size="sm">What is inquiry, and what does it require for representation, learning, legibility, and correction?</text>
    <caption>Primary source: Nucleation's CLAIMs, TERMs, ARGs, CASEs and SYNTHESISes</caption>
  </box>
  <row justify="center" align="center" gap={2}>
    <icon name="arrow-down" color="secondary"/>
    <text color="secondary" size="xs">Provides the theoretical distinctions</text>
  </row>
  <box padding={3} border radius="lg" gap={1}>
    <text color="secondary" weight="medium" size="xs">ARTICLE 2 · CASE STUDY</text>
    **Governing an Inquiry**

    <text size="sm">How were those distinctions operationalized through Luria, and what does Nucleation's history actually demonstrate?</text>
    <caption>Primary source: implementation decisions, recorded failures, revisions and evaluation designs</caption>
  </box>
  <row justify="center" align="center" gap={2}>
    <icon name="arrow-down" color="secondary"/>
    <text color="secondary" size="xs">Supplies the technical reference implementation</text>
  </row>
  <box background="surface-secondary" padding={3} radius="lg" gap={1}>
    <text color="secondary" weight="medium" size="xs">ARTICLE 3 · PROPOSAL</text>
    **One Inquiry, Many Articles**

    <text size="sm">What follows for scholarly publishing if research can be maintained independently of its presentations?</text>
    <caption>Primary contribution: hyperarticles, editorial feeds, and a separable publishing architecture</caption>
  </box>
</box>

The most important editorial consequence is that **Article 1 no longer needs to argue for hyperarticles**, and **Article 2 no longer needs to defend a proposed publishing ecosystem**. Each can stand or fall on its own claims. Article 3 can then cite both without needing to reproduce their full arguments.

Before persisting these as Nucleation works, I would also give the new claims in Article 3 their own record identities. In particular, the source/view publishing contract, the feed-with-memory abstraction, and the journal-as-feed proposal are currently extensions of the inquiry. Recording them explicitly would make the third article a much stronger demonstration of the system it proposes.

