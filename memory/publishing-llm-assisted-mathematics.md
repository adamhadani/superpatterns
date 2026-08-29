# Publishing LLM-Assisted Mathematics

## A practical guide to verification, peer review, and publication

LLMs can be powerful discovery tools, but a publishable mathematical result must ultimately stand on ordinary mathematical evidence. The safest workflow is:

> **Explicit result or witness → independent verification → expert scrutiny → public preprint → journal peer review**

The central principle is simple: treat the LLM as part of the discovery process, not as a source of authority. Every theorem, construction, computation, proof, and citation should be understandable, reproducible, and owned by the human authors.

## 1. Establish exactly what has improved

Write the claim in a form that leaves no room for ambiguity. For the standard, nonconsecutive permutation-superpattern problem, the previously discussed bounds were

\[
19 \leq sp(7) \leq 25, \qquad 21 \leq sp(8) \leq 33.
\]

Consequently:

- A valid 7-superpattern of length at most 24 improves the upper bound on \(sp(7)\).
- A proof that no length-19 through length-24 example exists, together with the known construction of length 25, would settle \(sp(7)=25\). More generally, an exact-value claim needs matching lower and upper bounds.
- A valid 8-superpattern of length at most 32 improves the upper bound on \(sp(8)\).
- A claimed value below the known lower bounds of 19 and 21 should first be treated as a likely definition or verification error.

Before presenting the result, classify it accurately:

- an explicit permutation witnessing a new upper bound;
- a search algorithm that finds such witnesses;
- a general construction that works for infinitely many \(k\);
- a lower-bound or nonexistence proof;
- or a combination of these.

This distinction affects both the proof burden and the appropriate publication venue.

## 2. Verify an explicit superpattern independently

For an upper-bound witness, verification is finite and conceptually straightforward. Given a permutation \(w\) of length \(m\), a checker should:

1. Confirm that \(w\) is a valid permutation of \(1,\ldots,m\).
2. Enumerate every \(k\)-element subset of positions.
3. Extract the corresponding subsequence.
4. Standardize that subsequence to its relative-order pattern in \(S_k\).
5. Confirm that all \(k!\) patterns occur.

The relevant raw enumeration sizes are manageable:

- \(\binom{24}{7}=346{,}104\) subsequences for a length-24 candidate at \(k=7\).
- \(\binom{32}{8}=10{,}518{,}300\) subsequences for a length-32 candidate at \(k=8\).

### Recommended verification standard

Use at least two independently written checkers, preferably in different languages or by different people. They should not share the same standardization or indexing implementation. Agreement between two genuinely independent implementations greatly reduces the risk of a common coding mistake.

Also test the checkers on:

- established small cases, including \(sp(5)=13\) and \(sp(6)=17\);
- deliberately damaged witnesses that should fail;
- boundary cases involving the first and last positions;
- hand-constructed subsequences whose standardized patterns are known.

Archive the following materials:

- the witness permutations in a plain-text file;
- the complete source code for both checkers;
- dependency and compiler/interpreter versions;
- tests and expected outputs;
- the number of distinct patterns found;
- cryptographic hashes of the released witness and code files;
- a short README containing one-command reproduction instructions.

An explicit upper-bound witness normally does not require a formal proof assistant, because the exhaustive check is small and transparent. Formal verification becomes more attractive for lower bounds, complicated reductions, SAT/CSP encodings, or proofs that depend heavily on a large search. In those cases, release independently checkable proof certificates or solver logs rather than asking readers to trust the search program itself.

## 3. Audit novelty before announcing the result

Computational discoveries are especially vulnerable to rediscovering an old construction in different notation. Search broadly under neighboring terminology, including:

- permutation superpatterns;
- universal permutations and \(k\)-universal permutations;
- complete or universal sequences for permutation patterns;
- dense packing of permutation patterns;
- zigzag constructions;
- theses, conference proceedings, OEIS entries, and research-code repositories.

Compare candidate witnesses under natural symmetries such as reverse, complement, inverse, and any cyclic transformations relevant to the precise definition. A numerically different permutation may be mathematically equivalent to a known example.

Recent experience with AI-assisted work reinforces this point. In one study of Gemini's attempts on 700 Erdős problems, 13 problems were selected as apparently addressed, but eight of those solutions were later found to have prior solutions. The authors emphasize the importance of literature identification and the possibility of unrecognized overlap with training data or earlier work. See [*AI-Assisted Mathematical Research: A Case Study on Erdős Problems*](https://arxiv.org/abs/2601.22401).

Terence Tao's community-maintained [AI contributions to Erdős problems tracker](https://github.com/teorth/erdosproblems/wiki/AI-contributions-to-Erd%C5%91s-problems) is also a useful model for careful classification: it distinguishes genuinely correct progress from partial results, variants, rediscoveries, and incorrect claims.

Before a public announcement, send a concise package—the theorem statement, witness, verification instructions, and comparison with prior bounds—to one or two specialists in permutation patterns. Ask specifically whether they know of prior art or a definitional mismatch.

## 4. Turn the discovery into a mathematical paper

A good paper should lead with the mathematics rather than the AI narrative. A descriptive title such as **“Short superpatterns for permutations of lengths seven and eight”** is usually stronger than a title centered on the model that helped find them.

A practical structure is:

1. **Introduction and prior bounds.** State the problem, known results, and exact improvement.
2. **Definitions.** Specify whether patterns are classical/nonconsecutive and state every convention.
3. **Main theorem.** Give the new upper bound, lower bound, construction, or exact value precisely.
4. **Explicit witnesses.** Print manageable witnesses in the paper and provide machine-readable copies.
5. **Correctness verification.** Explain standardization, exhaustive coverage, implementation independence, and computational complexity.
6. **Discovery method.** Report how the model and search procedure contributed, including model/version, dates, prompts or strategy, random seeds, and human interventions.
7. **Additional mathematics.** Analyze why the construction works, recurring structure, symmetries, families, or possible generalizations.
8. **Reproducibility and AI disclosure.** Link to the permanent archive and state human responsibility.
9. **Appendices.** Include pseudocode, extra witnesses, logs, and implementation details as needed.

A single finite witness is enough to prove an upper bound, but it can make a thin journal paper. The work becomes substantially stronger if it includes both \(k=7\) and \(k=8\), a reproducible search method, structural insight explaining the witnesses, or a construction that extends to other values of \(k\). An exact-value claim requires a separately rigorous lower-bound argument.

## 5. Be transparent about the role of the LLM

The LLM should not be listed as an author. The human authors must understand the argument, check every claim and citation, and accept full responsibility for the paper.

Preserve a research record containing:

- model name and version;
- access date and, where available, system configuration;
- prompts and visible model outputs relevant to the discovery;
- random seeds and sampling settings when meaningful;
- candidate-selection and rejection criteria;
- human edits, corrections, and verification steps;
- code and intermediate computational artifacts.

Do not assume that a model-generated citation exists or supports the stated claim. Check bibliographic metadata and the actual contents of every cited source.

### Sample disclosure

> **Declaration of AI-assisted research.** During the discovery phase, the authors used [model and version] to propose search strategies, generate candidate constructions, and/or assist with implementation. Every mathematical claim, witness, citation, and program used in this article was checked by the human authors. The superpattern property was verified independently by two implementations. The authors take full responsibility for the content. Relevant prompts, visible outputs, code, and computational artifacts are archived at [repository or DOI].

Adapt the disclosure to the target journal's current rules. Policies differ:

- [The Electronic Journal of Combinatorics](https://www.combinatorics.org/ojs/index.php/eljc/about/index) explicitly permits AI assistance while placing responsibility for proofs, prior work, and presentation on the authors.
- [Elsevier's generative-AI policies for journals](https://www.elsevier.com/en-au/about/policies-and-standards/generative-ai-policies-for-journals) require appropriate disclosure and do not permit an AI system to be an author.
- [INTEGERS submission guidance](https://math.colgate.edu/~integers/submit.html) currently takes a much more restrictive position on AI-produced mathematics, code, and bibliography. Check the live policy before submitting.

## 6. Use staged peer review

The recommended route is:

1. **Independent confirmation.** Have a collaborator or outside researcher rerun the verification from the archived files.
2. **Informal expert review.** Obtain feedback from specialists on novelty, definitions, and mathematical significance.
3. **Permanent archive.** Deposit code, witnesses, prompts, and logs in a service such as Zenodo and obtain a DOI.
4. **Public preprint.** Post a polished manuscript to arXiv, normally in `math.CO` for this topic. Remember that arXiv screening is not peer review.
5. **Research presentation.** Present the result in a combinatorics seminar or a permutation-patterns meeting; questions often reveal hidden assumptions quickly.
6. **Journal submission.** Submit to one journal at a time and include the reproducibility archive and AI disclosure.
7. **Revision.** Update the manuscript and preprint in response to referee reports.
8. **Post-publication updates.** Add the journal reference to arXiv and notify relevant survey or OEIS maintainers if appropriate.

## 7. Possible journals

Venue choice depends on how much mathematical structure accompanies the computation.

- **The Electronic Journal of Combinatorics** is a natural venue for a substantial permutation-pattern result. It is fully refereed, open access, and has an explicit policy on AI-assisted work. See its [journal information and policies](https://www.combinatorics.org/ojs/index.php/eljc/about/index).
- **The Australasian Journal of Combinatorics** publishes original research across combinatorics and is another plausible home. See its [journal site](https://ajc-new.maths.uq.edu.au/).
- **Discrete Mathematics** may suit a concise computational or structural note, subject to [Elsevier's current AI-disclosure policy](https://www.elsevier.com/en-au/about/policies-and-standards/generative-ai-policies-for-journals).
- **Combinatorial Theory** is more plausible if the work contains a broader theorem, general construction, or significant conceptual advance. See its [aims and scope](https://repositories.cdlib.org/uc/combinatorial_theory/aimScope).

Read several recent papers from a prospective journal before submission. Match the paper's length, level of structural explanation, and computational documentation to the journal's normal standards.

## 8. What recent AI-assisted mathematics examples teach

Several recent preprints illustrate useful review patterns:

- **Erdős Problem #728.** A GPT-5.2/Aristotle workflow produced a Lean-formalized proof, followed by a human-readable mathematical account connecting the formal statement to the intended problem. See [the preprint](https://arxiv.org/abs/2601.07421).
- **Erdős Problem #1196.** GPT-5.4 suggested a method involving Markov's inequality and the von Mangoldt function; human mathematicians checked, expanded, and developed the idea into a substantially broader paper. See [the preprint](https://arxiv.org/abs/2605.00301).
- **Unit-distance problem.** An AI-generated proof was converted into a human-readable digest and checked by multiple experts, showing the value of independent domain review even when a proof appears complete. See [the preprint](https://arxiv.org/abs/2605.20695).
- **Formal proof search for Erdős and OEIS problems.** Lean proofs provide machine-checked confidence in the formal statements, while still leaving humans responsible for matching those statements to the intended informal problems and establishing novelty. See [the preprint](https://arxiv.org/abs/2605.22763).

These examples suggest three complementary layers of validation:

1. **Computational or formal verification** checks the encoded claim.
2. **Expert mathematical review** checks that the encoded claim is the intended one and that the reasoning is meaningful.
3. **Journal peer review** evaluates correctness, originality, attribution, significance, and exposition.

Formalization does not replace literature review, and journal review does not replace reproducible computation.

## 9. Submission checklist

### Mathematical claim

- [ ] The definition of \(k\)-superpattern is explicit.
- [ ] The new bound or exact-value claim is stated precisely.
- [ ] The comparison with the best known bound uses the same conventions.
- [ ] Every witness is printed or linked in machine-readable form.

### Verification

- [ ] Two independent implementations reproduce the result.
- [ ] Checkers pass established positive and negative test cases.
- [ ] Counts, versions, seeds, and hashes are recorded.
- [ ] Lower-bound searches release certificates or independently checkable evidence where possible.

### Novelty

- [ ] The literature was searched under neighboring terminology.
- [ ] Symmetry-equivalent prior witnesses were considered.
- [ ] Specialists were asked about unnoticed prior art.
- [ ] Every citation was opened and checked by a human.

### Reproducibility

- [ ] Code, witnesses, tests, and instructions are publicly archived.
- [ ] The archive has a stable DOI or equivalent permanent identifier.
- [ ] A fresh machine can reproduce the principal result.

### Responsible AI disclosure

- [ ] Model/version, dates, and material uses are disclosed.
- [ ] Prompts and visible outputs relevant to the result are preserved.
- [ ] The LLM is not named as an author.
- [ ] Human authors understand and accept responsibility for every claim.
- [ ] The target journal's current AI policy has been checked.

### Publication

- [ ] The manuscript leads with the mathematical contribution.
- [ ] The paper explains more than the bare existence of a witness when possible.
- [ ] The preprint clearly identifies its non-peer-reviewed status.
- [ ] The manuscript is submitted to only one journal at a time.

## Bottom line

An LLM-assisted result should be reviewed and published like any other mathematical result, but with extra care around provenance, reproducibility, prior-art detection, and disclosure. For a new superpattern upper bound, the strongest package is an explicit witness, two independent exhaustive verifiers, a permanent artifact archive, a careful novelty audit, and a paper that adds structural mathematical insight. If those pieces are in place, AI assistance is a methodological fact to disclose—not a reason the theorem should receive either more or less mathematical trust.
