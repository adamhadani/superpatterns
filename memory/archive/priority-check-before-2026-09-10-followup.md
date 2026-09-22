# Historical record — superseded by current ledger

This file includes obsolete claims and execution state. Do not treat it as current instructions or proof status.

# Priority / novelty check — superpattern lower bound 1.0003125·k²/e² and sp(7) ≤ 23, sp(8) ≤ 32

Compiled 2026-08-29. Scope: any published or preprint work 2020–Aug 2026 that (a) improves the
Chroman–Kwan–Singhal (CKS) lower-bound constant for k-superpatterns (permutations, unrestricted
alphabet), or (b) exhibits a 7-superpattern shorter than 25 or an 8-superpattern shorter than 33.

## Verdict

1. **Lower bound constant.** No work found that improves the CKS constant 1.000076. Every source
   examined that states the best known lower bound (Wikipedia, last edited 30 Jan 2026; OEIS
   A342474, last revised 26 Mar 2021; Hunter 2021/2023; Manjunath–Dsouza Feb 2026; Bóna 3rd ed. 2022)
   still gives k²/e² or 1.000076·k²/e². **sp(k) ≥ (1.0003125 − o(1))·k²/e² is new** as far as
   the record shows. (Caveat: the improvement is by exactly the two avenues CKS themselves flag
   in their concluding remarks — see quote below — so a referee will regard it as "optimising CKS"
   rather than a new idea; CKS say explicitly they did not do this optimisation.)

2. **sp(7) ≤ 23, sp(8) ≤ 32.** No source states any value for sp(7) or sp(8) other than the
   general bound ⌈(k²+1)/2⌉ (= 25 and 33). OEIS A342474 still ends at a(6)=17 with keyword
   "more"; Engen–Vatter's survey says sp(6)=17 was found ad hoc (Arnarson) and gives nothing for
   k ≥ 7; the Feb 2026 circular-superpattern paper lists no linear values beyond the ⌈(k²+1)/2⌉
   formula. **Both values are new** on the record. (Note the previous-best for k=7 is 25 by
   Engen–Vatter, and for k=8 it is 33; Miller's (k²+k)/2 gives 28 and 36.)

3. **Hunter's claimed (15/32)k² upper bound** remains unpublished: arXiv 2108.05474 has only v1
   (Aug 2021); Hunter's arXiv author page (42 papers through Jul 2026) contains no superpattern
   upper-bound paper; his homepage lists only 2108.05474. It does not bear on the lower bound or
   on k = 7, 8 anyway (15/32·49 ≈ 23 only "+O(k)").

## Previous best results — exact statements

### Lower bound: Chroman–Kwan–Singhal
Z. Chroman, M. Kwan, M. Singhal, *Lower bounds for superpatterns and universal sequences*,
J. Combin. Theory Ser. A 182 (2021) 105467; arXiv:2004.02375.

Theorem 1.1 (p. 2 of arXiv version, lit/2004.02375.txt lines 79–80):
> "Theorem 1.1. Suppose that n < (1.000076/e²)k². Then every σ ∈ S_n contains only o(k!)
> different patterns π ∈ S_k. In particular, there is no k-superpattern of length less than
> (1.000076/e²)k²."

Immediately following (lines 81–84):
> "We have made some effort to optimize the constant in Theorem 1.1, where it would not
> negatively affect the readability of the proof. However, it would be quite complicated to
> fully squeeze the utmost out of our proof idea (see Section 6 for further discussion). In any
> case, obtaining a constant that is substantially larger than 1/e² seems quite out of reach."

Section 6 concluding remarks (lines 756–764) — the two avenues the new proof uses:
> "It should be clear from the proof of Theorem 1.1 that it is possible to make various small
> improvements to our lower bound: for example, it was convenient to restrict our attention to
> widths t_{i+1} − t_{i−1} only for even i, but with a more sophisticated argument one could take
> both even and odd i into account. Also, the bounds in Lemma 2.1 were rather crude, and
> presumably one could prove exact large deviation bounds for the number of widths above a given
> threshold. However, it would be very complicated to fully optimize all aspects of our argument,
> and it seems unlikely that one could prove a lower bound much larger than k²/e² without
> substantial new ideas. At present, we do not have a strong conjecture for the true minimal
> length of a k-superpattern."

Parameters used in their proof (line 287): c = 0.00075, d = 8.180.

### Upper bound / small values: Engen–Vatter
M. Engen, V. Vatter, *Containing all permutations*, Amer. Math. Monthly 128 (2021) 4–24;
arXiv:1810.08252 (v4, 28 Mar 2020), Section 6.

lit/1810.08252.txt lines 992–999:
> "Theorem 6.4. There is a word over P of length ⌈(n²+1)/2⌉ containing subsequences
> order-isomorphic to every permutation of length n.
> A computer search reveals that the bound in Theorem 6.4 is best possible for n ≤ 5. Alas, for
> n = 6 the bound in the Theorem 6.4 is 19, but Arnar Arnarson [private communication] has found
> that the permutation 6 14 10 2 13 17 5 8 3 12 9 16 1 7 11 4 15 of length 17 is universal for
> the permutations of length 6. Computations have shown that no shorter permutation is universal
> for the permutations of length 6. The best lower bound in this case is still the one given by
> Arratia [4] in his initial work on the problem."

Nothing is said about n = 7 or 8; ⌈(49+1)/2⌉ = 25 and ⌈(64+1)/2⌉ = 33 are the implied bests.

### OEIS A342474 (fetched 2026-08-29; entry #15, last modified 26 Mar 2021, author V. Vatter)
> %S 1,3,5,9,13,17
> %C A upper bound is ceiling((n^2+1)/2), see Engen and Vatter. A simple lower bound is n^2/e^2,
> which has been improved to 1.000076 n^2/e^2 by Chroman, Kwan, and Singhal.
> %K nonn,more

### Bóna, Combinatorics of Permutations, 3rd ed. (2022)
Grep of the full text: "superpattern" occurs in Ch. 5 Exercises 19–21 (sp(3)=5; sp(4) ≤ 10;
sp(k) ≤ k²; "sp(4) > 7"), Problems Plus 14–17 (4-superpattern of length 9 = 519472683, R. Smith;
"computer data proves that there is no 4-superpattern of length 8"; (2/3)k² EELW; weak
superpattern; Miller (k+1 choose 2); Engen–Vatter ⌈n²/2⌉), and the preface ("Records have fallen
in just about every version of the superpattern problem"). CKS is reference [117] in the
bibliography but the text states no lower-bound constant beyond the k²/e² counting bound; no
value for sp(7) or sp(8).

### Wikipedia "Superpattern" (last edited 30 Jan 2026)
States lower bound n ≥ k²/e² "with a slight improvement to 1.000076 k²/e²", upper bound
⌈(k²+1)/2⌉; no table of small values.

## Every relevant item found in the citation / listing sweep

Citation indices queried: Semantic Scholar citations API for arXiv:2004.02375 (8 citers),
arXiv:2108.05474 (1), arXiv:1810.08252 (21); Google Scholar "Cited by 10" for CKS (only 3
rendered: Altschuler–Dubroff–Tikhomirov 2026, Mitchell–Wild 2026, Engen thesis 2021); OpenAlex
(cited_by lists empty); zbMATH title search "superpattern"; arXiv full-text search for
"superpattern" (13 hits, all listed below where relevant) and "universal permutation"; arXiv
author listing for Zach Hunter (42 papers); StackExchange API search on MathOverflow and MSE.

| Paper | What it proves | Relevance |
|---|---|---|
| Chroman–Kwan–Singhal, JCTA 182 (2021), arXiv 2004.02375 | sp(k) ≥ (1.000076/e²)k² (Thm 1.1); also universal sequences bound (Thm 1.2, n < (1+e^{−600})k²/e over alphabet (1+e^{−1000})k) | Previous best lower bound |
| Engen–Vatter, AMM 128 (2021), arXiv 1810.08252 | sp(k) ≤ ⌈(k²+1)/2⌉; sp(6)=17; exact for k ≤ 5 | Previous best upper bounds 25 / 33 for k=7,8 |
| Z. Hunter, arXiv 2108.05474 (v1 only), Combinatorial Theory 3(2) (2023) | f(k;(1+o(1))k) = (1/2+o(1))k² for words over small alphabets; refutes Gupta's rosary conjecture. Claims "in forthcoming work [9], the author will show that f(k) ≤ (15/32)k² + O(k)"; [9] = "A new upper bound for superpatterns, in preparation" — never appeared | No lower-bound content for permutations |
| H. Manjunath, R. Dsouza, *Circular Super patterns and Zigzag constructions*, arXiv 2602.09072 (Feb 2026) | Upper bounds for circular k-superpatterns (Table 1); simplified EV score function | Intro cites only "An improved lower bound for L_k was given by Chroman et al [3]"; no linear small values, no new lower bound |
| Altschuler–Dubroff–Tikhomirov, *Online Permutation Embedding*, arXiv 2608.19050 (Aug 2026) | Optimal online embedding time of a fixed k-pattern into an iid stream | Cites CKS; not about superpattern length |
| Mitchell–Wild, *Weight-constrained cut-down de Bruijn sequences*, arXiv 2607.22350 (2026) | de Bruijn-type sequences | Cites CKS for universal sequences; irrelevant |
| Eppstein–Lincoln? (Semantic Scholar entry) *Quasipolynomiality of the Smallest Missing Induced Subgraph*, arXiv 2306.11185 (2023) | Graph complexity | Cites CKS for universality; irrelevant |
| Dagstuhl Seminar 23121 report (2023), talk by C. Defant "Three Topics in Pattern Avoidance" | Survey talk; cites CKS [6], EV [9], Hunter [11] | No new bounds |
| M. Engen, *Universal Combinatorial Structures*, PhD thesis, U. Florida 2021 (advisor Vatter) | Not accessible online in text form; contemporaneous with the survey (v4 Mar 2020) | Presumably restates sp(6)=17; no indication of k=7 computations anywhere in Vatter's later OEIS entry (Mar 2021) |
| He–Kwan, *Universality of random permutations*, BLMS 52 (2020), arXiv 1911.12878 | Random permutation of length 2000k² log log k is k-universal whp | Upper-bound side only |
| Defant–Kravitz–Sah, *Supertrees*, EJC 27 (2020), arXiv 1908.03197 | Supertrees | Irrelevant |
| Biers-Ariel–Zhang–Godbole 2016; Bannister et al 2013/14; Godbole–Liendo 2013 | Earlier restricted-class superpattern results | Pre-2020, irrelevant to the constant |
| "Skip Letters for Short Supersequence of All Permutations", arXiv 2201.06306 (2022) | Supersequences (words containing all permutations of a set as subsequences — a different problem) | Irrelevant |
| OpenAlex 2026 "Superpatterns of Spectrally Arbitrary Sign Patterns" | Matrix sign patterns | Name collision only |
| MSE 2559477 (2017) "Permutation superpatterns…" | Unanswered question about length-n² superpatterns | Irrelevant |

MathOverflow: the StackExchange API returns zero questions containing "superpattern"; searches
for "universal permutation", "contains all patterns of length", "Arratia conjecture" return no
relevant thread.

Matthew Kwan's publication page (mkwn.github.io/publications.html) lists only CKS and He–Kwan on
this topic. Zach Hunter's homepage (zachhunter.xyz) lists only 2108.05474.

## Sources consulted (URLs)
- https://arxiv.org/abs/2004.02375 ; https://www.sciencedirect.com/science/article/pii/S0097316521000662
- https://arxiv.org/abs/1810.08252 ; https://doi.org/10.1080/00029890.2021.1835384
- https://arxiv.org/abs/2108.05474 ; https://escholarship.org/uc/combinatorial_theory/3/2
- https://arxiv.org/abs/2602.09072 ; https://arxiv.org/abs/2608.19050 ; https://arxiv.org/abs/2607.22350
- https://oeis.org/search?q=id:A342474&fmt=text
- https://en.wikipedia.org/wiki/Superpattern
- https://api.semanticscholar.org/graph/v1/paper/arXiv:2004.02375/citations (and 2108.05474, 1810.08252)
- https://scholar.google.com/scholar?cites=4441707694311431980
- https://api.openalex.org/works?filter=cites:W3014226464 ; https://api.zbmath.org/v1/document/_search?search_string=superpattern
- https://arxiv.org/search/?query=superpattern&searchtype=all ; https://arxiv.org/search/?query=Hunter%2C+Zach&searchtype=author
- https://zachhunter.xyz ; https://mkwn.github.io/publications.html
- https://drops.dagstuhl.de/entities/document/10.4230/DagRep.13.3.49
- https://api.stackexchange.com/2.3/search/advanced?q=superpattern&site=mathoverflow (and math.stackexchange)
- Bóna, Combinatorics of Permutations 3rd ed. (local text, scratchpad/BonaCombinatoricsofPermutation.txt)
