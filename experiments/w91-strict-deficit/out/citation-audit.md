# Citation and attribution audit for W90/W91 (sec:flip, sec:strict)

Date: 10 November 2026. Scope: `output/paper/superpatterns-notes.md` (sections sec:flip, sec:strict and the
introduction lines that feed them), `output/paper/references.bib`, `experiments/w90-layered-deficit/proof.md`,
`experiments/w91-strict-deficit/proof.md`, `experiments/w91-strict-deficit/proof-c21.md`, `memory/priority-check.md`.
No existing file was edited; section (iv) lists the edits to apply.

Provenance labels: **[read]** = I read the source text itself (arXiv PDF text, or the book copy);
**[meta]** = publisher/Crossref/zbMATH/arXiv metadata only; **[2nd]** = taken from another paper's citation;
**[agent]** = found by a search sub-agent and not re-read by me. Anything not labelled [read] should not be
quoted with a theorem number without a second look.

Headline findings

1. **B1 (Jelínek–Karpilovskij): the mathematics is right, the attribution is not.** Theorem 26 does follow from
   the known case k = 2 of the skew shape conjecture, but that case is *not* a theorem of JK21. JK21 quote it as
   their Theorem 2.5 and credit it to Jelínek's 2008 thesis and, independently, to Burstein–Pantone. JK21's own
   theorems are about D-free shapes and about non-transversal 01-fillings. See B1 for the replacement wording.
2. **A preprint the paper does not cite changes two sentences.** Chen and Wang, arXiv:2610.13530 (v1 9 Oct 2026,
   v2 5 Nov 2026) [read], announce that a random permutation of length 32k² is k-universal w.h.p. The paper says
   that the best bound "remains 2000k² log log k" and lists universality at Ck² as open (lines 434 and 535).
3. **"This is the argument of Alexander" (line 422) could not be confirmed.** The result is attributed correctly;
   the claim about the method is not supported by anything I could read. See B7.
4. `Arratia99` is the right first printed source for Alon's conjecture, but the paper never cites it (the entry
   is unused), and the conjecture is stated at line 13 with no citation at all.

--------------------------------------------------------------------------------------------------
## (i) Part A — bibliographic data

| Key | Status | Corrected / added fields | Source |
|:--|:--|:--|:--|
| JK21 | corrected | Paper no. 8 (23 pp.) of vol. 22 no. 2 (Permutation Patterns 2019 special issue), 2021; add `doi = 10.46298/dmtcs.6171`. Authors, title, year, arXiv id correct. The URL `dmtcs.episciences.org/7594` resolves to the paper (7594 is a document id, not the article number) | PDF header of arXiv v3 [read]; https://api.crossref.org/works/10.46298/dmtcs.6171 ; zbMATH 7524070 [meta] |
| BP15 | corrected | It is published: *Journal of Combinatorics* **6** (2015), no. 1–2, 55–67, `doi = 10.4310/JOC.2015.v6.n1.a4`. Change `@misc` to `@article`, year 2014 to 2015, keep arXiv:1402.3842 in `note` | https://api.crossref.org/works/10.4310/JOC.2015.v6.n1.a4 ; zbMATH 6437911 [meta]; JK21 ref. [4] [read] |
| BWX07 | confirmed | add `doi = 10.1016/j.aam.2004.11.006` | Crossref record of that DOI [meta] |
| HK20 | confirmed | none | Crossref record of 10.1112/blms.12345 [meta]; arXiv:1911.12878v2 [read] |
| BDJ99 | confirmed | add `doi = 10.1090/S0894-0347-99-00307-0`; optional `note = {arXiv:math/9810105}` | Crossref [meta]; arXiv PDF [read] |
| LS77 | confirmed | add `doi = 10.1016/0001-8708(77)90030-5` | Crossref; zbMATH 3565993 [meta]. Full first names as in Romik's book, p. 7 [read] |
| VK77 | confirmed | none. English title has "limiting form". Sov. Math., Dokl. 18, 527–531 (1977); original Dokl. Akad. Nauk SSSR 233, 1024–1027 (1977). No DOI exists. Issue number of the translation: could not confirm | zbMATH 3630761 [meta] |
| AD95 | confirmed | add `doi = 10.1007/BF01204214` | Crossref; zbMATH 810864 [meta] |
| Talagrand95 | confirmed | add `doi = 10.1007/BF02699376` (vol. 81, no issue number, pp. 73–205, 1995) | Crossref [meta] |
| Alexander94 | confirmed | none | Crossref; zbMATH 731965 [meta] |
| Rhee95 | confirmed | add `doi = 10.1214/aoap/1177004827`. Title wording is right ("First Passage Time", no hyphen) | Crossref; zbMATH 780979 [meta] |
| AlonSpencer16 | confirmed | add `series = {Wiley Series in Discrete Mathematics and Optimization}`, `address = {Hoboken, NJ}`, `isbn = {978-1-119-06195-3}`. Fourth edition, © 2016 | front matter of the book copy [read] |
| LastPenrose17 | corrected | Published book, not a manuscript: Cambridge University Press, Cambridge, 2018 ("First published 2018" on the copyright page; Crossref gives an online date of 26 Oct 2017), IMS Textbooks vol. 7, xx+293 pp., ISBN 978-1-107-08801-6 (hbk), 978-1-107-45843-7 (pbk), `doi = 10.1017/9781316104477`. **Theorem 4.4 is "Multivariate Mecke equation", on p. 30** (Chapter 4, "The Mecke Equation and Factorial Measures") — re-confirmed | book copy [read]; zbMATH 6796875 [meta] |
| ADT26 | confirmed | none. arXiv:2608.19050v1, 19 Aug 2026, primary math.PR; authors and title as in the entry | arXiv PDF header [read]; https://arxiv.org/abs/2608.19050 [meta] |
| CKS21 | confirmed | none | Crossref record of 10.1016/j.jcta.2021.105467 [meta] |
| EV21 | confirmed | journal name is "The American Mathematical Monthly" (cosmetic) | Crossref [meta] |
| Arratia99 | confirmed | add `number = {1}`; "N1" is a Note of 4 pp.; journal name "The Electronic Journal of Combinatorics" | PDF [read]; Crossref record of 10.37236/1477 [meta] |

Not confirmed anywhere: a DOI for the 4th edition of Alon–Spencer; the issue number of the English translation
of VK77; whether JK21 had an earlier extended abstract.

--------------------------------------------------------------------------------------------------
## (ii) Part B — attributed statements

### B1. Jelínek–Karpilovskij — verdict: **needs rewording** (implication correct, attribution wrong in part)

Source read: arXiv:2002.12308v3 = DMTCS 22:2 (2021) #8, in full for §§1–2 and §5 [read].

What the paper contains.

* Objects: a *skew shape* is the difference of two top-left justified Ferrers shapes with a common top-left
  cell (so the missing corners are top-left and bottom-right). Fillings are by non-negative integers; a
  *transversal* has exactly one 1 in each row and column. ι_k is the increasing (NE) chain and δ_k the decreasing
  (SE) chain of size k; an occurrence must have its whole k×k sub-shape inside the shape.
* **Conjecture 1.1 = Conjecture 2.4 (skew shape conjecture):** for every skew shape S and k ≥ 1,
  Tr(S, ι_k) ≥ Tr(S, δ_k), where Tr counts avoiding transversals. Stated to be trivial for k = 1, true for
  k = 2, and "so far only verified for k ≤ 2".
* **Theorem 2.5, credited to Jelínek's thesis (Lemmas 29 and 30) and independently to Burstein–Pantone
  (Lemmas 1.4 and 1.5):** a skew shape that admits a transversal has exactly one δ_2-avoiding transversal, and
  exactly one transversal avoiding both ι_2 and a fixed three-cell filling φ_D of the "dented" 3×3 shape D.
* **Theorem 2.2 / Corollary 2.3 (JK's first main result):** for D-free skew shapes there is a bijection on
  integer fillings exchanging δ_k-avoidance and ι_k-avoidance for all k; hence Tr(S, δ_k) = Tr(S, ι_k) there.
* **Theorem 2.6 (JK's second main result):** for every skew shape, the number of *binary* fillings avoiding δ_2
  equals the number avoiding both ι_2 and φ_D, by a bijection preserving the number of 1-cells in each row.
  This extends Theorem 2.5 from transversals to general 01-fillings.
* Permutations: the Introduction and §5 say that the conjecture for a given k would imply that α ⊖ δ_k ⊖ β is
  avoided by fewer permutations than α ⊖ ι_k ⊖ β (skew sums), referring to Jelínek's thesis, §3.2, for the
  reduction. JK add that their own results do not seem to give direct consequences for permutation enumeration.

So each of the three things our texts say is true in substance: the size-2 statement for skew shapes, the
conjecture for all k, and "known only for k ≤ 2". What is wrong is the phrase "the transversal case k = 2 **of
the theorem of Jelínek and Karpilovskij**". The transversal case k = 2 is prior work that JK21 quote; their
theorem is the non-transversal extension. The line in W90 `proof.md` and `priority-check.md`,
"#fillings avoiding δ₂ = #fillings avoiding ι₂ and φ_D", is Theorem 2.6 and is accurate if "fillings" is read as
"01-fillings".

Does it imply Theorem 26 (W90 Theorem 1)? **Yes for the inequality, given a reduction that JK21 do not prove.**

Correspondence (ours → JK):

1. Reverse every permutation. Direct sums become skew sums and 12 ↔ 21, so our α⊕12⊕β is JK's α′ ⊖ δ_2 ⊖ β′
   and our α⊕21⊕β is their α′ ⊖ ι_2 ⊖ β′.
2. For a fibre (O, X, Y), the board D = (X × Y) ∩ U ∩ S is a skew shape after this reflection: U is an up-set
   and S a down-set, so D contains every grid cell between two of its cells c ≤ c′, which is JK's
   Observation 2.1. Rows and columns of outside points are deleted.
3. The fibre is the set of transversals of D (W90 Lemmas 2 and 3). This is the reduction JK cite to the thesis;
   Burstein–Pantone carry it out only for α = β = 1 (left-to-right minima and right-to-left maxima).
4. An increasing pair p < q of inside points always spans a 2×2 sub-shape inside D, so "has an increasing pair"
   is "contains the reflected δ_2". A decreasing pair spans a sub-shape inside D exactly when a∧b ∈ U and
   a∨b ∈ S, so "has a D-inversion" is "contains the reflected ι_2".
5. Theorem 2.5 then says: exactly one valid filling has no increasing pair (our Lemma 4(i)), and at least one
   has no D-inversion (our Lemma 4(ii), a ≥ 1). Summing over fibres gives Theorem 26.
6. The exact formula Σ(a − 1) is the same sum written out: a = Tr(D, ι_2) and 1 = Tr(D, δ_2). JK do not state
   it. Theorem 2.5 gives more than we use: a − 1 is the number of D-inversion-free fillings that contain the
   reflected φ_D.
7. The shape D with Tr(D, ι_2) = 2 and Tr(D, δ_2) = 1 (stated after JK's Fig. 6) is the three-point lens of
   Proposition 28.

Closest statement in pattern language already in print: Burstein–Pantone, end of §3 [read], report as a private
communication that Jelínek proved {σ ⊕ 12 ⊕ τ} ∼ {σ ⊕ 21 ⊕ τ} ∪ B for a finite set B of permutations of length
at most 2|σ| + 2|τ| + 3. That contains the inequality of Theorem 26 verbatim (no proof is given there). They
also say that Jelínek's thesis already had 1234 ∼ {1324, 3416725}, unpublished.

Not checked: Jelínek's thesis itself (no PDF located; a catalogue record exists at
https://invenio.nusl.cz/record/482909). "Lemmas 29 and 30" and "§3.2" are as cited by JK21 [2nd].

Related sentence, line 358: "for layers of size at least three the inequality itself is the conjecture of
[@JK21]". The conjecture is about fillings; the permutation inequality is its consequence. Reword (see (iv)).

### B2. Burstein–Pantone — verdict: **attribution correct**; bibliography out of date

Theorem 1.1 [read]: {1324, 3416725} ∼ 1234. Lemma 1.4: unique filling of a "nice board" avoiding the board of
1234 (credited there to Bóna's Lemma 2). Lemma 1.5: unique filling avoiding the boards of 1324 and 3416725.
Published as J. Comb. 6 (2015), no. 1–2, 55–67. Our uses (the fibre of 3416725, the planted gadget, "which is
where the unbalanced Wilf-equivalence comes from") are accurate. The inequality |Av_n(1324)| > |Av_n(1234)| for
n ≥ 7 is cited by them to Bóna, Discrete Math. 175 (1997), 55–67 (DOI 10.1016/S0012-365X(96)00140-9 [meta]);
W90 `proof.md` names Bóna without a reference.

### B3. Backelin–West–Xin — verdict: **attribution correct**, add one clause

Abstract [meta]: a bijection between the permutations avoiding 12⋯t p_{t+1}⋯p_m and those avoiding
t⋯21 p_{t+1}⋯p_m, i.e. I_t ⊕ τ ∼ J_t ⊕ τ; the same abstract credits t = 2 to West's 1990 MIT thesis and t = 3 to
Babson–West. JK21 describe the filling form: Tr(F, δ_k) = Tr(F, ι_k) for Ferrers shapes F [read]. Reference:
Adv. Appl. Math. 38 (2007), no. 2, 133–148. The theorem number inside BWX07 could not be confirmed (full text
not read). Proposition 28 says "this is the case k = 2 of [@BWX07]": correct, but the case t = 2 is older, and
BWX put the monotone block first (our α empty); the case β empty follows by reverse-complement.

### B4. He–Kwan and the origin of Alon's conjecture — verdict: **attribution correct**; add the original source

* Conjecture 1.1 [read]: for fixed ε > 0, a random permutation of length (1+ε)k²/4 is w.h.p. k-universal. It is
  introduced as a conjecture made by Alon in 1999, with references to Alon's 2016 Oberwolfach abstract and to
  Arratia 1999.
* Theorem 1.2 [read]: length 2000 k² log log k suffices w.h.p. Theorem 1.3: length 20k² suffices for a family of
  (1 − o(1))k! patterns.
* Conjecture 5.3 [read]: the single-pattern weakening (every fixed π ∈ S_k is contained w.h.p. at
  (1+ε)k²/4). Corollary 36 concerns one explicit pattern, so it contradicts Conjecture 5.3 as well. The paper
  mentions only Conjecture 1.1.
* Journal data: Bull. Lond. Math. Soc. 52 (2020), no. 3, 515–529.
* **First appearance in print: Arratia 1999, Conjecture 3** [read], attributed there to Noga Alon: with t(k) the
  least n at which a random n-permutation contains all of S_k with probability at least 1/2, t(k) ∼ (k/2)².
  So `Arratia99` is the right citation. Its form is a median threshold, not the w.h.p. form of He–Kwan;
  Corollary 36 contradicts both. The same note has Arratia's own Conjecture 2 (shortest superpattern ∼ (k/e)²).
* Alon's own text: N. Alon, "When are random permutations k-universal?", in *Combinatorics and Probability*,
  Oberwolfach Rep. 13 (2016), no. 2. Workshop report pp. 1189–1257, DOI 10.4171/OWR/2016/22 [meta]; pp. 1218–1219
  for the abstract itself as cited by Chen–Wang [2nd]. Not read.

### B5. Baik–Deift–Johansson — verdict: **attribution correct**; cite the theorem numbers

Theorem 1.1 [read, arXiv math/9810105]: (l_N − 2√N)/N^{1/6} converges in distribution to the Tracy–Widom law.
Theorem 1.2: all moments converge; in particular eq. (1.10) gives (E l_N − 2√N)/N^{1/6} → ∫t dF(t), numerically
−1.7711. So E LIS(σ_n) = 2√n + O(n^{1/6}) is correct, with a negative coefficient. The statement in Corollary 30
about the identity (contained w.h.p. once n − k²/4 ≫ k^{4/3}) uses Theorem 1.1, not the moments. Theorem numbers
are those of the arXiv version; the journal numbering was not compared.

### B6. Logan–Shepp, Vershik–Kerov, and the Poissonised statement — verdict: **attribution correct**; one citation missing

* E LIS(σ_n)/√n → 2: Romik, Theorem 1.1 (p. 7) [read], credited there to Vershik–Kerov and independently
  Logan–Shepp (1977). Our citation [@LS77; @VK77] is the standard one. (Some surveys credit the upper bound to
  Vershik–Kerov alone; not checked here.)
* Poisson model and superadditivity: Romik §1.4. Theorem 1.6 (p. 10, "Hammersley's convergence theorem"): the
  limit Λ exists. The proof uses the Poisson process in the quadrant and the superadditivity of the diagonal
  variables (p. 12, around eqs. (1.5)–(1.6)), and identifies the limit with sup_m E Y_{0,m}/m. Theorem 1.23
  (p. 62): Λ = 2. Exercise 1.4 (p. 71) is the Fekete-lemma route. Together these give E LIS(P_T) ≤ 2T, which
  the paper asserts with "in the same way" and no citation, and which `proof-c21.md` (S3) derives correctly.
* Hammersley, "A few seedlings of research", Proc. 6th Berkeley Symp. Math. Statist. Probab., vol. 1, 345–394
  (1972): bibliographic data confirmed (zbMATH 3373691 [meta]); content not read.
* Aldous–Diaconis 1995: bibliographic data confirmed; the paper is paywalled and the theorem number for c = 2
  could not be confirmed.

### B7. Alexander 1994 and Rhee 1995 — verdict: result **correct**; the claim about the method **needs rewording**

* Alexander, abstract [meta]: γn ≥ E L_n ≥ γn − C(n log n)^{1/2} for the longest common subsequence of two
  i.i.d. sequences, with an explicit C independent of the letter distribution. This matches our text.
* Rhee, abstract [meta]: a unified simple proof of Alexander's results for common subsequences and for
  first-passage times.
* Method: neither full text could be read (Project Euclid refuses automated access). The only description I
  found is in Lember–Matzinger–Torres, arXiv:1011.2688 = Ann. Appl. Probab. 22 (2012), no. 3, 1046–1058 [read]:
  Alexander's main result is his Proposition 2.4, and his proof uses McDiarmid's inequality but rests mainly on
  first-passage-percolation techniques. Their own proof is the one that resembles Lemma 34: cut an optimal
  alignment into pieces whose two lengths sum to 2n, bound each piece by superadditivity and symmetry, then
  McDiarmid's inequality and a union bound over the cuts.
* So "This is the argument of Alexander" (paper, line 422), "the same argument" (`priority-check.md`) and the
  description in `proof-c21.md` ("cutting an optimal object in two plus concentration") are unconfirmed for
  Alexander and Rhee and confirmed for Lember–Matzinger–Torres. Cite the result to Alexander and the scheme to
  LMT, or have someone with access read Alexander §2 and Rhee.

### B8. Talagrand 1995 — verdict: **attribution correct**

Publ. Math. IHÉS 81 (1995), 73–205, DOI 10.1007/BF02699376 [meta]. The paper cites [@Talagrand95] in the proof
of Corollary 30 and [@AlonSpencer16, Thm 7.7.1] in Lemma 34 for the same inequality; cite both in both places.
I did not re-check Theorem 7.7.1. `priority-check.md` contradicts itself on this: the W91 row says the theorem
number was not checked, the W91 part 2 row says it was.

### B9. Altschuler–Dubroff–Tikhomirov — verdict: **attribution correct**; one presentation point

Read: arXiv:2608.19050v1, §1 [read].

* β(π) is the optimal expected time to embed π online into an i.i.d. uniform stream. Theorem 1.1: recursion.
  Theorem 1.3: an explicit optimal algorithm, with concentration of its stopping time at scale β(π)^{3/4},
  uniformly in π. Theorem 1.7: concentration and a central limit theorem for β of a uniform π.
* Theorem 1.5: with c−, c_typ, c+ the limits of min, mean and max of β(π)/k², one has c− < c_typ < 1/2 < c+ and
  1/4 ≤ c− ≤ 0.48867, 0.48934 ≤ c_typ ≤ 0.49967, 0.50547 ≤ c+ ≤ 0.50568. The identity has coefficient 1/2.
* After Theorem 1.5 they state the dichotomy: either online and offline embedding have fundamentally different
  extremisers, or Alon's conjecture and its weakening (He–Kwan Conjecture 5.3) do not hold. Our paraphrase in
  `priority-check.md` is accurate, and "the increasing permutation is known not to be extremal for online
  embedding" (line 360) is exactly their first negative result. No overstatement found.
* They do not name an offline counterexample, do not mention layered patterns in §1, and describe the online
  maximisers only as neither near-monotone nor near-random (Question 1.11). They attribute Alon's conjecture to
  "Alon (1999)" via Arratia's note.
* Presentation point: 0.50568 and 0.49967 are *online* constants (upper ends of the intervals for c+ and c_typ).
  The offline coefficients in line 15 and in the summary-table row "Typical target" are our deduction from
  Theorems 1.3 and 1.5. Line 15 says so; the table cell "0.49967+ε [@ADT26]" reads as if ADT stated an offline
  bound.

--------------------------------------------------------------------------------------------------
## (iii) Part C — prior art for the new claims

Searches were run by a sub-agent (about 20 web queries, arXiv listing search, Semantic Scholar citation lists
for arXiv:1911.12878, math/0505485 and 2608.19050); I re-read the two sources that matter most (Chen–Wang, ADT).
MathOverflow could not be searched natively (site search blocked); four web queries restricted to
mathoverflow.net and math.stackexchange.com returned nothing. Google Scholar and MathSciNet were not available.

(a) *A specific pattern with a strictly larger threshold than the identity.* **Nothing found.** He–Kwan give
only the heuristic that monotone patterns are believed hardest, and state Conjecture 5.3. ADT prove the online
analogue fails and state the dichotomy (B9). Queries: "pattern harder to contain than monotone pattern in random
permutation threshold layered 2143"; "random permutation contains every pattern monotone not hardest k^2/4
counterexample"; "random permutation 2143 containment threshold disjoint inversions Hammersley".

(b) *Alon's conjecture proved or disproved.* No proof or disproof of the sharp constant found. **New since
He–Kwan: Y. Chen and Y. Wang, "Quadratic-size Random Permutations are Universal", arXiv:2610.13530**
(https://arxiv.org/abs/2610.13530) [read]. Theorem 1.1: a uniform permutation of length 32n² is n-universal with
failure probability at most exp(−n/25) for large n. §4.1 sketches how to replace 32 by any constant above 1;
§4.2 calls the constant 1 a natural barrier for the method. The abstract says the proof was found by an AI
system; it is an unrefereed preprint. It is consistent with Corollary 36 (threshold near 1.0023·k²/4, far below
k²) and does not mention layered patterns. The six papers citing He–Kwan on Semantic Scholar [agent]:
2610.13530, 2608.19050, 2305.17933, 2108.05474, 2004.02375, 2001.05767; none settles the sharp constant.

(c) *The constant for 2143⋯.* **Nothing found for c₂₁.** Closest: Albert, arXiv:math/0505485 (already in the
bibliography as Albert05/Albert07) [agent]: Theorem 2 gives lim E L_A(σ_n)/√n = 2√(c_A) for sum- or
difference-closed classes A; Conjecture 1 says c_A equals the growth rate; §4 simulates the class
Av(231, 312, 321) of layered permutations with layers of size at most 2 and calls it a likely counterexample.
That is a different quantity: it allows singleton layers, so the longest such subsequence is at least
max(LIS, 2·L₂₁). Albert et al. 2003 (Albert03) is algorithmic only.

(d) *Asymptotics of |Av_n(21 ⊕ ⋯ ⊕ 21)|.* No source for the growth rate of this family was found. Related, in
the regime of fixed pattern length k and n → ∞: Bóna, "The limit of a Stanley–Wilf sequence is not always
rational, and layered patterns beat monotone patterns", arXiv:math/0403502 (abstract [meta]: for a layered
pattern q of length k, L(q) ≥ (k−1)²; published in J. Combin. Theory Ser. A 110 (2005), 223–235 [agent]);
Claesson–Jelínek–Steingrímsson, arXiv:1111.5736 [agent]. These say layered patterns are at least as easy to
avoid as monotone ones for fixed k, which is the fixed-k shadow of Theorem 26 and Corollary 27. Nobody was found
connecting them to Alon's conjecture. Worth one sentence of context in the paper; not prior art for c₂₁ < 1.

(e) *Jelínek's unpublished generalisation* (found while reading for B1, not by search): Burstein–Pantone §3
report {σ⊕12⊕τ} ∼ {σ⊕21⊕τ} ∪ B. This is prior art for Theorem 26 in exactly its pattern form, and a referee in
permutation patterns will know it.

Conclusion for Part C: no prior statement of (a), (c) or of c₂₁ < 1 was found. The searches remain shallow for a
claim of this size; the recommendation in `priority-check.md` to ask a specialist stands.

--------------------------------------------------------------------------------------------------
## (iv) Edits to apply

### references.bib — replace these entries

```bibtex
@article{JK21,
  author  = {Jel{\'\i}nek, V{\'\i}t and Karpilovskij, Mark},
  title   = {Fillings of skew shapes avoiding diagonal patterns},
  journal = {Discrete Mathematics \& Theoretical Computer Science},
  volume  = {22},
  number  = {2},
  year    = {2021},
  doi     = {10.46298/dmtcs.6171},
  note    = {Paper no. 8, 23 pp.; arXiv:2002.12308},
  url     = {https://dmtcs.episciences.org/7594}
}
@article{BP15,
  author  = {Burstein, Alexander and Pantone, Jay},
  title   = {Two examples of unbalanced {W}ilf-equivalence},
  journal = {Journal of Combinatorics},
  volume  = {6},
  number  = {1--2},
  pages   = {55--67},
  year    = {2015},
  doi     = {10.4310/JOC.2015.v6.n1.a4},
  note    = {arXiv:1402.3842}
}
@book{LastPenrose17,
  author    = {Last, G{\"u}nter and Penrose, Mathew},
  title     = {Lectures on the {P}oisson Process},
  series    = {Institute of Mathematical Statistics Textbooks},
  volume    = {7},
  publisher = {Cambridge University Press},
  address   = {Cambridge},
  year      = {2018},
  isbn      = {978-1-107-08801-6},
  doi       = {10.1017/9781316104477}
}
@book{AlonSpencer16,
  author    = {Alon, Noga and Spencer, Joel H.},
  title     = {The Probabilistic Method},
  edition   = {4},
  series    = {Wiley Series in Discrete Mathematics and Optimization},
  publisher = {Wiley},
  address   = {Hoboken, NJ},
  year      = {2016},
  isbn      = {978-1-119-06195-3}
}
```

The key `LastPenrose17` is kept so that no citation breaks. `priority-check.md` links the manuscript URL twice;
point those at the DOI.

### references.bib — add one field to existing entries

* `BWX07`: `doi = {10.1016/j.aam.2004.11.006}`
* `BDJ99`: `doi = {10.1090/S0894-0347-99-00307-0}`
* `LS77`: `doi = {10.1016/0001-8708(77)90030-5}`
* `AD95`: `doi = {10.1007/BF01204214}`
* `Talagrand95`: `doi = {10.1007/BF02699376}`
* `Rhee95`: `doi = {10.1214/aoap/1177004827}`
* `Arratia99`: `number = {1}`

### references.bib — new entries

```bibtex
@phdthesis{Jelinek08,
  author = {Jel{\'\i}nek, V{\'\i}t},
  title  = {Wilf-Type Classifications, Extremal and Enumerative Theory of Ordered Structures},
  school = {Charles University in Prague},
  year   = {2008}
}
@misc{ChenWang26,
  author = {Chen, Yu and Wang, Yiting},
  title  = {Quadratic-size Random Permutations are Universal},
  year   = {2026},
  note   = {arXiv:2610.13530},
  url    = {https://arxiv.org/abs/2610.13530}
}
@article{LMT12,
  author  = {Lember, J{\"u}ri and Matzinger, Heinrich and Torres, Felipe},
  title   = {The rate of the convergence of the mean score in random sequence comparison},
  journal = {The Annals of Applied Probability},
  volume  = {22},
  number  = {3},
  pages   = {1046--1058},
  year    = {2012},
  doi     = {10.1214/11-AAP778},
  note    = {arXiv:1011.2688}
}
@book{Romik15,
  author    = {Romik, Dan},
  title     = {The Surprising Mathematics of Longest Increasing Subsequences},
  series    = {Institute of Mathematical Statistics Textbooks},
  volume    = {4},
  publisher = {Cambridge University Press},
  address   = {Cambridge},
  year      = {2015},
  isbn      = {978-1-107-07583-2},
  doi       = {10.1017/CBO9781139872003}
}
@incollection{Hammersley72,
  author    = {Hammersley, John M.},
  title     = {A few seedlings of research},
  booktitle = {Proceedings of the Sixth Berkeley Symposium on Mathematical Statistics and Probability, Vol. 1},
  publisher = {University of California Press},
  address   = {Berkeley},
  pages     = {345--394},
  year      = {1972}
}
@article{Bona97,
  author  = {B{\'o}na, Mikl{\'o}s},
  title   = {Permutations avoiding certain patterns: the case of length 4 and some generalizations},
  journal = {Discrete Mathematics},
  volume  = {175},
  number  = {1--3},
  pages   = {55--67},
  year    = {1997},
  doi     = {10.1016/S0012-365X(96)00140-9}
}
```

Thesis title as cited by JK21 and by Burstein–Pantone; the thesis was not seen. Add an entry for Alon's
Oberwolfach abstract only after its pages have been checked against the report (B4).

### Paper `output/paper/superpatterns-notes.md`

1. Line 341, replace the paragraph "Theorem 26 is the transversal case $k=2$ of the theorem of Jelínek and
   Karpilovskij … included for completeness." by:

   > Theorem 26 is not new. After reversing permutations, which turns direct sums into skew sums and exchanges $12$ with $21$, each fibre is the set of transversal fillings of a skew shape, and the two sorting arguments say that exactly one transversal avoids the chain $\delta_2$ and at least one avoids $\iota_2$. This is the case $k=2$ of the skew shape conjecture, proved by Jelínek [@Jelinek08] and independently by Burstein and Pantone [@BP15, Lemmas 1.4 and 1.5]; see [@JK21, Theorem 2.5]. The conjecture for chains of every size is [@JK21, Conjecture 2.4], where it is noted to be known only for $k\le2$. Burstein and Pantone also report, as a communication from Jelínek, the equivalence $\{\sigma\oplus12\oplus\tau\}\sim\{\sigma\oplus21\oplus\tau\}\cup B$ for a finite set $B$ [@BP15, §3], which contains the inequality of Theorem 26. The short proof above is included for completeness.

2. Line 35, replace "is the size-two transversal case of a theorem on fillings of skew shapes [@JK21] and is not
   claimed as new" by:

   > is, after reversal, the case $k=2$ of the skew shape conjecture for transversal fillings, due to Jelínek and to Burstein and Pantone [@Jelinek08; @BP15; @JK21, Theorem 2.5], and is not claimed as new

3. Line 29 (summary table), prior-best cell: replace "Skew shapes [@JK21]; $1324$ vs $1234$ [@BP15]" by
   "Skew shapes, $k=2$ [@Jelinek08; @BP15; @JK21, Thm 2.5]".

4. Line 358, replace "for layers of size at least three the inequality itself is the conjecture of [@JK21]" by:

   > for layers of size at least three the inequality itself is open; it would follow from the skew shape conjecture [@JK21, Conjecture 2.4]

5. Line 337, replace "this is the case $k=2$ of [@BWX07]" by:

   > this is the case of a block of size two in the theorem of Backelin, West and Xin [@BWX07], which for that size goes back to West's thesis; they place the monotone block first, and the other case follows by reverse-complement

6. Line 13, replace the two sentences "Alon's conjecture asks … $2000k^2\log\log k$ [@HK20]." by:

   > Alon's conjecture [@Arratia99, Conjecture 3; @HK20, Conjecture 1.1] asks whether a uniform permutation of length $\lceil(1/4+\varepsilon)k^2\rceil$ simultaneously contains all of $S_k$, with probability tending to one, for every fixed $\varepsilon>0$. He and Kwan establish this with length $2000k^2\log\log k$ [@HK20]. A recent preprint of Chen and Wang announces it with length $32k^2$, and sketches any constant above $1$ in place of $32$ [@ChenWang26].

7. Line 434, replace "Corollary 36 contradicts the conjecture as stated in [@HK20, Conjecture 1.1] for small
   fixed $\varepsilon$. It leaves open what the true threshold constant is and whether a random permutation of
   length $Ck^2$ is a $k$-superpattern for some absolute $C$." by:

   > Corollary 36 contradicts the conjecture as stated in [@HK20, Conjecture 1.1], its weakening to a single pattern [@HK20, Conjecture 5.3] and the original form [@Arratia99, Conjecture 3], for small fixed $\varepsilon$. It leaves open what the true threshold constant is. Universality at length $Ck^2$ for an absolute constant $C$ is announced in [@ChenWang26]; this is consistent with Corollary 36.

8. Line 535, replace "and, independently of the constant, prove universality at $Ck^2$ for some absolute $C$,
   where the best bound remains $2000k^2\log\log k$ [@HK20]" by:

   > and determine the threshold constant; the best published upper bound is $2000k^2\log\log k$ [@HK20], and $32k^2$ is announced in [@ChenWang26]

9. Line 422, replace "This is the argument of Alexander for the longest common subsequence
   [@Alexander94; @Rhee95]." by:

   > Lemma 34 is the analogue for $L_{21}$ of Alexander's rate-of-convergence theorem for the longest common subsequence [@Alexander94]; see also [@Rhee95]. The scheme of the proof, cutting an optimal object along an antidiagonal and combining superadditivity with a concentration inequality, is that of [@LMT12].

10. Line 413: "[@Talagrand95]" → "[@Talagrand95; @AlonSpencer16, Thm 7.7.1]", and "[@BDJ99]" →
    "[@BDJ99, Theorem 1.2]". Line 371: "[@BDJ99]" → "[@BDJ99, Theorem 1.1]". Line 420: "[@AlonSpencer16, Thm 7.7.1]" →
    "[@Talagrand95; @AlonSpencer16, Thm 7.7.1]".

11. Paragraph "From a deficit to the constant" (before Lemma 34), replace "In the same way
    $\mathbb E\,\mathrm{LIS}(P_T)\le2T$." by:

    > In the same way $\mathbb E\,\mathrm{LIS}(P_T)\le2T$, since the limit of $\mathbb E\,\mathrm{LIS}(P_T)/T$ is $2$ [@Hammersley72; @LS77; @VK77; @Romik15, §1.4 and Theorem 1.23].

12. Line 24 (summary table, "Typical target" row): "$0.49967+\varepsilon$ [@ADT26]" →
    "$0.49967+\varepsilon$ (online bound of [@ADT26], transferred)". Optional.

13. Line 32 (summary table): "Conjectured threshold $(1+\varepsilon)k^2/4$ [@HK20]" →
    "Conjectured threshold $(1+\varepsilon)k^2/4$ [@Arratia99; @HK20]".

Run `make check` and re-render after applying; items 1, 6 and 7 lengthen paragraphs.

### `experiments/w90-layered-deficit/proof.md`, header paragraph "Prior art for the inequality"

Replace from "Jelínek–Karpilovskij, *Fillings of skew shapes …*" to "… gives the equality case." by:

> the case k = 2 of the skew shape conjecture for transversal fillings (every skew shape with a transversal has
> exactly one δ₂-avoiding transversal and exactly one avoiding ι₂ and φ_D), due to Jelínek (PhD thesis, Charles
> University, 2008) and independently Burstein–Pantone (Lemmas 1.4, 1.5); stated as Theorem 2.5 in
> Jelínek–Karpilovskij, *Fillings of skew shapes avoiding diagonal patterns*, DMTCS 22:2 (2021) #8,
> arXiv:2002.12308, who extend it to 01-fillings (Theorem 2.6), conjecture Tr(S, ι_k) ≥ Tr(S, δ_k) for every k
> (Conjecture 2.4) and note that it is known only for k ≤ 2. Burstein–Pantone §3 also report Jelínek's
> unpublished {σ⊕12⊕τ} ∼ {σ⊕21⊕τ} ∪ B. Theorem 1 is the k = 2 transversal case read in pattern language after
> reversal (skew sums ↔ direct sums, δ₂ ↔ ι₂); the short proof below is self-contained. Backelin–West–Xin
> (I_t ⊕ τ ∼ J_t ⊕ τ; t = 2 already in West's thesis) gives the equality case.

Also give Bóna's inequality its reference (Discrete Math. 175 (1997), 55–67) and the Burstein–Pantone journal
data (J. Comb. 6 (2015), 55–67).

### `experiments/w91-strict-deficit/proof-c21.md`, paragraph after the status table

Replace "The idea is the classical one for superadditive functionals (Alexander, … gives a short proof):" by:

> The statement is the analogue of the classical rate-of-convergence theorem for superadditive functionals
> (Alexander, Ann. Appl. Probab. 4 (1994) 1074–1082, proves γn − C√(n log n) ≤ E L_n ≤ γn for the longest common
> subsequence; Rhee, Ann. Appl. Probab. 5 (1995) 44–48, gives a short proof; neither proof was read). The scheme
> used here is that of Lember–Matzinger–Torres, Ann. Appl. Probab. 22 (2012) 1046–1058:

In (S3) add after "Vershik–Kerov": "; Romik, *The Surprising Mathematics of Longest Increasing Subsequences*,
Theorem 1.1, §1.4 and Theorem 1.23".

### `experiments/w91-strict-deficit/proof.md`

* Lemma 3.1, proof: "(Last–Penrose, *Lectures on the Poisson process*, Thm 4.4)" → "(Last–Penrose, *Lectures on
  the Poisson Process*, Cambridge University Press 2018, Theorem 4.4, p. 30)".
* Corollary C, proof: "(Baik–Deift–Johansson)" → "(Baik–Deift–Johansson, Theorems 1.1 and 1.2)".

### `memory/priority-check.md`

* W90 row "Block-flip inequality": the comparison should name Jelínek's thesis and Burstein–Pantone as the
  source of the k = 2 transversal case, JK21 Theorem 2.5 as where it is stated, and Burstein–Pantone §3 for the
  pattern form. Replace "the paper itself was not read line by line" by "JK21 §§1–2, 5 and Burstein–Pantone §1,
  §3 read on 10 Nov 2026 (`experiments/w91-strict-deficit/out/citation-audit.md`); Jelínek's thesis not seen".
* W91 part 2 row "Rate of convergence": replace "**Not new**: the same argument, adapted …" by "**Not new in
  kind**: analogue of Alexander's theorem; the proof scheme matches Lember–Matzinger–Torres 2012; Alexander's and
  Rhee's proofs were not read".
* W91 row "Tools": delete "the Alon–Spencer theorem number was not checked against the book and is cited by
  section only", which the part 2 row contradicts.
* Top table, row "General random universality": add Chen–Wang, arXiv:2610.13530 (32k², unrefereed).
* Both Last–Penrose links: use https://doi.org/10.1017/9781316104477.

### `output/paper/layered-refutation.md` (untracked standalone note, appeared during this audit; not in scope, grep only)

The same misattribution occurs twice and should get the same fix as items 1 and 2 above:

* Line 24: "This is the size-two transversal case of a theorem of Jelínek and Karpilovskij on fillings of skew
  shapes [@JK21]" → "This is, after reversal, the case $k=2$ of the skew shape conjecture for transversal
  fillings, due to Jelínek and to Burstein and Pantone [@Jelinek08; @BP15; @JK21, Theorem 2.5]".
* Line 64: "The inequality in Theorem 8 is the transversal case of the theorem of Jelínek and Karpilovskij for
  chains of size two [@JK21]" → "The inequality in Theorem 8 is the case $k=2$ of the skew shape conjecture for
  transversal fillings [@Jelinek08; @BP15; @JK21, Theorem 2.5]".

The rest of that file was not audited. Check there too: whether Alon's conjecture is cited to `Arratia99`,
whether Chen–Wang is mentioned where the state of the universality problem is described, and the page for
[@LastPenrose17, Theorem 4.4] (p. 30).

* Line 262 (open problems) lists "Universality at $Ck^2$ for some absolute $C$" as open and calls the
  size-three analogue "the transversal case of the conjecture of [@JK21]". The first is announced in
  [@ChenWang26] (unrefereed); the second should read "which would follow from the skew shape conjecture
  [@JK21, Conjecture 2.4]".
