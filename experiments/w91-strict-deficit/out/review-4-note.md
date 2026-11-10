# Referee report 4 — `output/paper/layered-refutation.md` (revised 16-page note)

Date: 2026-11-10. Cold read: only `output/paper/layered-refutation.md` (350 lines, timestamp 16:31) and
its PDF `output/pdf/layered-refutation.pdf` (16 pages, same timestamp) were opened; no other file of the
repository. Line numbers below are lines of the Markdown source. The reviewer is an AI system (Claude);
this report is not a substitute for a specialist's reading.

## 0. Verdict

**No invalidating error found.** Every statement of Sections 2–7 was re-derived line by line; the
parts that changed in substance (new (O5)/(O6), Lemmas 3.2, 3.4, 3.5, 2.9, 7.1, 7.2, Section 6, the
proofs of Theorem 1.2 and of Corollary 1.3 in both directions) are correct as written, and all
constants were recomputed. Lemmas 3.1(ii),(iii), 3.2, 3.3, 3.4, 3.5 and 2.9 were also tested by
brute-force programs written from the definitions in the note (Section 5 of this report): 0 failures.

What remains is (a) five small mathematical loose ends, none of which affects a result, (b) one
wrong lemma number and a handful of imprecise pointers, (c) a list of notation collisions that the
renaming did not remove (two of them involve the anchors `e`, `f`), and (d) presentation points in
the abstract, the AI declaration and the verification record. With (b), the `e`/`f` collisions and
the points of Section 4 below repaired, the note is fit to send to a specialist.

| Task item | Verdict |
|:--|:--|
| 1 Cross-references | All numbered references resolve to the intended statement, except one (X1). Slips X1–X9. |
| 1 Symbols | All defined before use. Collisions N1–N16 (N1, N2 touch the anchors `e`, `f`). |
| 2(a) (O5),(O6); Lemmas 3.2, 3.4, 3.5 | Correct. Proof of 3.4 is complete; brute force 0 violations, negative controls fire. |
| 2(b) Lemma 2.9 (i),(ii) | Correct. |
| 2(c) Lemma 7.1, Lemma 7.2 | Correct; constants 12, 17, 80, 40, 22, 45, 171, 200 check. Loose ends G1, G2. |
| 2(d) Theorem 1.2, Corollary 1.3 | Correct in both directions; odd/even k sentence correct. Slip X2. |
| 2(e) Section 6 | Bookkeeping, pigeonhole, three probabilities correct; constant recomputed (4.8e-84 ≥ 1e-84). |
| 3 Rest | Re-derived by reading (not machine-tested): see Section 3 of this report. Nothing broken. |
| 4 Presentation | Abstract: first sentence over-precise (P1). Declaration vs record: three clarifications (P3–P5). |

## 1. Errors and gaps, by severity

### 1.1 Invalidating errors

None.

### 1.2 Mathematical loose ends (no result affected)

**G1. Lemma 7.1(i), degenerate medians (line 280, 287).** "$\Pr(Y_n\le m_n-u)\le2\exp(-u^2/(8m_n))$" is
undefined if $m_n=0$, and "integers $b\ge1$" fails for $b=m_n+\lceil u\rceil$ when $m_n=0$, $u=0$.
Both are vacuous cases. Repair: add "for $n\ge n_0$ we have $m_n\ge1$ (e.g. by Lemma 5.3 or
directly), and the bounds are trivial for $u=0$".

**G2. Lemma 7.2, meaning of "for large $T$" (line 302).** "$\mathbb EM\le a+1\le\Lambda_{21}(T)+22\sqrt{T\ln T}$
for large $T$" needs $18\sqrt T+2\le2\sqrt{T\ln T}$, i.e. $\ln T\ge81$ ($T\gtrsim10^{35}$). True as
stated, but a reader checking with moderate $T$ will stumble. Repair: say so, or replace 22, 45, 171,
200 by constants valid from a small $T$ (e.g. $a+1\le\Lambda_{21}(T)+40\sqrt{T\ln T}$ for $T\ge3$).

**G3. (F3), order of the argument (line 275).** Fekete's lemma is invoked and
"$\Lambda_{21}(T)\le c_{21}T$" is concluded before it is shown that the supremum is finite; finiteness
of $c_{21}$ needs $\Lambda_{21}\le\Lambda\le2T$, which is derived two sentences later in the same item
("It is finite, being at most $\Lambda$" only says $\Lambda_{21}(T)<\infty$ for each $T$). Repair:
move the bound $\Lambda(T)\le2T$ before the definition of $c_{21}$, and note that monotonicity of
$\Lambda_{21}$ is what allows Fekete's lemma for real $T$.

**G4. Section 6, (A1) (line 259).** "$\Pr(N\ge t)\ge\Pr(2L_{21}(P_T)\ge t)$ by Corollary 2.6" uses, besides
Corollary 2.6 with $S\subset\mathbb N$, that $W_{\mathbb N}[1..t]$ is contained in
$21^{\oplus\lceil t/2\rceil}$ and that $2L_{21}\ge t$ forces $L_{21}\ge\lceil t/2\rceil$. Repair: one
clause.

**G5. Unproved assertions presented as facts.** Remark (i) of Section 6 (line 263): "With a second
planted pattern, 1 4 5 2 7 8 3 6, ... the bound improves to $c\,T/\ln T$". This is plausible
(14527836 $=1\oplus3416725$, so the extra point shifts the lens by one level and every step of the
window becomes usable, giving a per-stage cost of order 1 instead of $1/K$), but it needs analogues
of Lemmas 3.3–3.5 and 4.1 for eight points, which are not given. Repair: "we expect" / "one can
check", or delete. Same for line 318 ("which would follow from the skew shape conjecture").

### 1.3 Things checked that are *not* errors (for the record)

* Lemma 3.2 with the simplified (O5), (O6): every quantity entering (O1)–(O6) is $\ell(e)$, $h(f)$,
  $\ell(r)$ for $r<f$, $h(r)$ for $r>e$, or $\ell,h$ of a lateral point, and none of these sees $R$.
  The quantities that *do* depend on the content of $R$ ($h(e)$, $\ell(f)$, $h$ of lower points,
  $\ell$ of upper points) appear in no condition. Correct.
* Lemma 3.4: the proof is complete. It does **not** need $e=e'$ before treating $f,f'$: each of the two
  cases ($e\ne e'$; $f\ne f'$) ends in a contradiction on its own, using only that $q_1$ lies in both
  rectangles. "We may assume that $e'$ is north-west of $e$" is legitimate: the hypotheses are symmetric
  in the two pairs, two distinct incomparable points of a configuration are north-west/south-east of
  each other, and the two "we may assume" are two independent relabelings, one per case. The only
  facts left tacit are $e'\ne f$ (because $f>e$ and $e'$ is incomparable with $e$) and $f'\ne e$
  (because $f'>q_1>e$).
* Lemma 3.5, (O5)/(O6): a lower point of level $i$ is in $G_i$ (height $\ge h(f)+1$, equality by
  3.1(iii)), an upper point of height $N-i$ is in $G_{i+1}$; leftmost choice of $z_i$, $z_{i+1}$
  finishes. Correct.
* Lemma 2.9(i): the rightmost inside point of a lens at $(\alpha,b)$ has height exactly $b+1$, so for
  $b'>b$ at most two inside points remain; by symmetry of the roles of $b,b'$ this gives uniqueness.
  (ii): fillings 231, 312, 321; only 321 has a $D$-inversion; $\rho=1/3$. Correct (also enumerated).
* Lemma 7.1: Talagrand in the Alon–Spencer form for integer $b$ only (certificate $2b$ is valid only
  for integer levels: correct precaution); $b=m_n+\lceil u\rceil$ with integer median and monotonicity
  of $v^2/(m_n+v)$; both tails; $\sqrt{8\pi m_n}\le\sqrt{40\pi T}=11.21\sqrt T$;
  $\sqrt{16\pi m_n}+32\le15.86\sqrt T+32\le17\sqrt T$ for $T\ge779$; Poisson step; the three pieces of
  the integral in (iii) ($(80T/s)T^{-5}$, $10T\exp(-(\ln T)^2/3)$, $(\mathbb E\nu^2(e/5)^{10T})^{1/2}$).
  Correct.
* Lemma 7.2: $j^*=0$ (then $m-1\le M'$), $j^*=m$ (then $m\le M$), $m=0$; the grid covers $[0,2T]$
  and $|\tilde R_k|\le T^2+1$; reflection maps $R_x$ to $R'_{2T-x}$; $45=2\cdot22+1$;
  $\frac12\sum_i2^{-i/2}(1+\sqrt i)=3.7796<3.79$, $45\cdot3.7796=170.1\le171\le200$. Correct.
* Theorem 1.2 and Corollary 1.3: two-sided estimate
  $c_{21}\sqrt n-O(n^{1/4}\sqrt{\ln n})\le\mu_n\le c_{21}\sqrt n+O(\ln n)$ follows from 7.1(iii), (F3),
  7.2; $\eta\in(0,1)$ guarantees $u=\eta\sqrt n\le5T$ in the upper tail; the lower tail has no
  restriction on $u$; $21^{\oplus\lfloor k/2\rfloor}$ is itself of length $k$ for even $k$ and is
  contained in $21^{\oplus(k-1)/2}\oplus1$ for odd $k$. Correct.
* Section 6: $p=2i-2=t_0+2K+2\xi-2$; $p-1=\iota_0+2\xi-1$; the step $(z_{p-1},z_p)$ is step number
  $2\xi$ of the window $z_{\iota_0}<\dots<z_{\iota_0+2K}$; $\max p=\iota_0+2K$ so (A1) gives $N\ge p$;
  fewer than $K$ thin steps among $2K$ leaves $\ge K+1$ non-thin, and only $K$ steps are odd;
  failure probabilities $\exp(-10^{-4}(T-2))$, $T^{-2.21}$, $(2\log_2T+5)T^{-96.9}$;
  $0.015/45.1^2=7.37\cdot10^{-6}$, $A_1^7/(6\cdot7!^2)=6.56\cdot10^{-79}$, product
  $4.8\cdot10^{-84}\ge10^{-84}$. Correct.

## 2. Slips

### 2.1 Cross-references and pointers

Every "Lemma x.y", "Theorem x.y", "Corollary", "Proposition", "Definition", "(O1)–(O6)", "(A1)–(A3)",
"(F1)–(F4)", equation tag ((2.1), (6.1)), "Section" and "Table 1" was followed. All resolve to the
right statement except X1. Tables 2 and 3 are never referred to by number (fine).

| # | Line | Quote | Problem | Fix |
|:--|:--|:--|:--|:--|
| X1 | 88 | "By Lemmas 2.1 and 2.2, $P_\varphi\supseteq\alpha\oplus12\oplus\beta$ iff ..." | That the regions and the inside set of $P_\varphi$ are $\mathcal U_\alpha(O),\mathcal V_\beta(O),\Gamma_\varphi$ is Lemma 2.3, not 2.2 | "By Lemmas 2.1 and 2.3" |
| X2 | 308 | "By Lemma 7.1(iii) with $T=\sqrt n$, $\lvert\Lambda_{21}(\sqrt n)-\mu_n\rvert\le5\ln n+1$" | The lemma gives $5\ln\sqrt n+1$; the stated bound is weaker, hence true, but is not what the lemma says | "$\le5\ln\sqrt n+1$" or "$\le3\ln n$" |
| X3 | 40 | "Flipping blocks one at a time writes $\mathbb E\,\mathrm{LIS}-2\,\mathbb EL_{21}$ as a sum of non-negative stage costs" | Lemma 2.7 gives equality only for $\mathbb E\,\mathrm{LIS}-\mathbb EN_S$; for $2L_{21}$ it is a lower bound | "bounds ... below by a sum" |
| X4 | 153 | "(O5) and (O6) are tie-breaking rules, used only in Lemma 3.4" | They are also verified in Lemma 3.5 and are part of $\mathcal E$ in Lemma 4.1 | "needed only for Lemma 3.4" |
| X5 | 202, 212 | "Let $S$ be finite, $\Pi=W_S$, and $p\ge t_0+2$" | $t_0$ was defined "throughout this section" (Section 3, line 130) and is used in Section 4 without being recalled | add "$t_0=2\max S$" |
| X6 | 328 | "Theorem 2.5 → Lemmas 2.7, 2.9 → Lemmas 3.3–3.5 → ..." | Omits Corollary 2.6, Lemma 3.1 and Lemma 3.2, although 3.2 is named two lines later as the most delicate step | "Lemmas 3.1–3.5", add Cor. 2.6 |
| X7 | 332 | "brute-force computation from the definitions of Section 2" | The tested lemmas 3.2–3.5 use the definitions of Section 3 | "Sections 2 and 3" |
| X8 | 44 | "every window of $90\ln T$ consecutive steps" | Section 6 uses $2K=2\lceil45\ln T\rceil$ steps | "about $90\ln T$" |
| X9 | refs | [7] Chen–Wang 2026, [18] Altschuler–Dubroff–Tikhomirov 2026: no arXiv number; [4] Alon 2016 lacks "Oberwolfach Reports 13"; [10] "22:" lacks issue and article number | Reader cannot locate [7], [18]; I could not locate [7] by a web search | add identifiers |

### 2.2 Notation (one meaning per symbol)

No symbol is used before it is defined. The following collisions survive the renaming. N1 and N2
re-use the anchor letters and should be fixed; the others are local and cosmetic.

| # | Symbol | Meanings (lines) | Fix |
|:--|:--|:--|:--|
| N1 | $f$ | upper anchor (144–215); "$f$-certifiable with $f(s)=2s$" (287) | "certifiable with certificate size $\psi(s)=2s$" |
| N2 | $e$ | lower anchor (144–215); Euler's number in "$(e/5)^{10T}$", "$(eT/k)^{2k}$" (293), whereas the note writes $\exp$ elsewhere to avoid exactly this | "$(\mathrm e/5)^{10T}$" with $\mathrm e$ declared, or $\exp(-10T\ln(5/\mathrm e))$ |
| N3 | $b$ | length of the increasing tail $I_b$ (50, 104–215); Talagrand level "integers $b\ge1$" (287) | rename the Talagrand level ($\lambda$) |
| N4 | $S_m$, $S_r$ | sets $\{i_1,\dots,i_m\}$ (110–111); symmetric groups $S_n$, $S_k$, $S_7$ (15, 58, 88, 337) | $S^{(m)}$ |
| N5 | $G_i$ / $\mathcal G_p$ | antichain of an optimal copy (192–198) / set of planted pairs (186–215) | rename $G_i$ ($Z_i$) |
| N6 | $A_1$ / (A1) / $\mathcal A$ / $A$ | thin threshold (219, 229, 258–261) / condition (253) / event (251) / area $\lvert R\rvert$ (208) / copies $A,A'$ (68–76) | threshold $\to\theta$ or $a_0$ |
| N7 | $\eta$ | configuration in the Mecke formula (208, 210); increments $\eta_i$ (219–229); constant in Cor. 1.3 (312) | Mecke dummy $\to\chi$; constant $\to\theta$ |
| N8 | $\rho$ / $\varrho$ | $(F^\circ-1)/F$ (82, 85, 126) / integer scale in Lemma 5.2 (227–229): two glyphs of the same letter | $\varrho\to d$ |
| N9 | $k$ | pattern length (Sec. 1, 312); chain length (Sec. 5); $k=2K$ (254); grid index and $X_k$ (302); dummy (276, 293) | grid index $\to\kappa$ |
| N10 | $m$, $M$ | $21^{\oplus m}$ (24); max level (142); $L_{21}([0,2T]^2)$ (298); $\lfloor k/2\rfloor$ (312); median $m_n$ (278); $M=2k$ (227) vs $M=\sup$ (299) | Lemma 7.2: $m\to L$; Lemma 5.2: $M\to2k$ |
| N11 | $W$ | pattern $W_S$ (94); width $\sum\omega_i$ (227) | width $\to w$ |
| N12 | $I$, $O$, $F$, $X$, $Y$ | inside set $I$ vs pattern $I_b$; outside set $O$ vs (O1)–(O6) vs $O(\cdot)$ (312); $F$ vs (F1)–(F4); coordinate sets $X,Y$ (62) vs $X_k$, $Y_n$, $Y$, $Y'$ (Sec. 7) | at least rename (F1)–(F4) to (S1)–(S4)? optional |
| N13 | $\beta$, $c$, $a$ | pattern $\beta$ vs blocks $\beta_j$ (298; blocks are $B_i$ in Sec. 2); points $a,c$ (56–80) vs $a=M2^\varrho$, $c=2M2^{-\varrho}$ (227) vs real $a$ (302, 320) vs $c$ in "$c\,T/\ln T$" (263) vs corners $c_j$ (298) | Lemma 7.2 blocks $\to B_j$ |
| N14 | $D$-inversion | the letter $D$ is never explained (62) | one clause (shape $D$ of [JK21]?) or rename |
| N15 | $J_d$ | used in line 318, not in the Notation paragraph (which has only $I_b$) | define |
| N16 | $T_\ast$ | appears only in Theorem 1.4 (33); Section 6 says "for large $T$" three times and never fixes $T_\ast$ | end the proof with "this defines $T_\ast$" |

Checked and consistent: $q_1,q_2,q_3,u_1,u_2,v_1,v_2$ (159–190; Table 1 agrees with the order type
3416725 and with the list of comparable pairs); $p$ ($\ell(e)+1$ in 3.3, $\ell(e)=p-1$ in
$\mathcal G_p$, $2i-2$ in Section 6); $t_0$; $\mathcal U,\mathcal V,\mathcal U_t$ (always
calligraphic); $F,F^\circ$; $\varphi$ (fillings) vs $\Phi$ (indicator; no bare $\phi$ anywhere);
$N$ vs $\nu$; $\Lambda$ vs $\Lambda_{21}$; $\mu_n$, $m_n$; $K$, $J$, $i_j$, $\xi$, $\iota_0$ and
the index $\iota$ of the copy in Section 6 (distinct from the block index $i$);
lower/upper/lateral (a lateral point is indeed north-west or south-east of the whole rectangle).

## 3. Skim of the remaining sections (Task 3)

Read and re-derived on paper, **not** machine-tested by this referee: Lemmas 2.1–2.4, Theorem 2.5,
Corollary 2.6, Lemma 2.7 (telescoping; the index bijection $(t,i_m)\leftrightarrow(i,b)$ is right),
Lemma 3.1(i), Lemma 4.1, Proposition 4.2, Lemmas 5.1–5.3 (constants recomputed: $0.0697$,
$0.3144<1/3$, $4\mathrm e^{-4}=0.0733$, $0.063\lfloor T/2\rfloor\ge0.03T$ for $T\ge50$), (F1)–(F4).
Nothing was found broken by the rewrite. Machine-tested here: Lemmas 3.1(ii),(iii), 3.2, 3.3
(Table 1 and the lens), 3.4, 3.5, 2.9(i) on planted configurations, 2.9(ii).

External statements checked against the sources (web): [HK20] Conjecture 1.1, Conjecture 5.3, the
$2000k^2\log\log k$ theorem, the random-graph heuristic and the threshold question are quoted
accurately; [BP15] is the source of 3416725 and has Lemmas 1.4 and 1.5; [JK21] Conjecture 2.4 is
the skew shape conjecture and Theorem 2.5 is the size-two case with the attribution given in the
note; the DOIs of [HK20] and [JK21] resolve. Not checked: [ChenWang26] (not found), [ADT26],
[Alon16] page numbers; [LastPenrose17, Theorem 4.4] and [AlonSpencer16, Theorem 7.7.1] agree with my
recollection of those books but were not opened.

## 4. Presentation (Task 4)

**P1. Abstract, first sentence.** "contains the increasing pattern of length $k$ with high probability
if and only if $n$ exceeds $k^2/4$ by a lower-order term" is neither proved nor cited in the note
(which only uses $\mathrm{LIS}=(2+o(1))\sqrt n$), and as an "if and only if" it is imprecise: the
window is $n-k^2/4\gg k^{4/3}$ (Baik–Deift–Johansson). Repair: "the threshold for containing the
increasing pattern of length $k$ is $n=(1+o(1))k^2/4$". All other claims of the abstract follow from
Theorem 1.2 and Corollary 1.3 (the pattern $2\,1\,4\,3\cdots k\,(k-1)$ presupposes $k$ even: say so).

**P2. Introduction, points a specialist will stop at.**
* Line 36: "Simulations with $n$ up to $10^8$ give ... $\approx0.0023\sqrt n$, that is
  $c_{21}\approx0.99887$": five digits, no error bar, no sample size, no word on how $L_{21}$ is
  computed at $n=10^8$, no pointer to the data. Finite-size corrections of both terms are of order
  $n^{1/6}$ (about 38 for $\mathrm{LIS}$ at $n=10^8$, against a measured gap of 23); say why they
  cancel (line 342 suggests they nearly do) or quote the fitted correction.
* Theorem 1.4 is stated in $T$ (side of the square, about $T^2$ points) next to statements in $n$;
  add "so $P_T$ has about $T^2$ points and the deficit is of order $\sqrt n/(\ln n)^2$".
* "We show" (line 23) and "So Conjecture 1.1 fails" (line 31) are unhedged while the title page says
  "draft for independent verification" and line 36 says "would place". Use one register.
* [HK20] already records that the threshold of any single pattern is at most $(1+o(1))k^2$ (after
  their Conjecture 5.3); quoting it gives the reader the sanity bound $\varepsilon_0\le3$.
* Line 318: "the analogous quantity" for $J_d$-layers is not defined (which multiple of $L_{J_d}$ is
  subtracted from $\mathrm{LIS}$?).

**P3. Declaration vs verification record: which version was reviewed?** The declaration (line 11) and
the last row of Table 3 (line 343) say the proofs "have been re-derived by AI reviewers" / "by three
AI reviewers ... one of which read only this note". The text has since been renumbered and
(O5)/(O6), Lemma 3.4 and Corollary 1.3 changed. State for each review which version it read; as
written a reader will assume the present text. (The present report is a cold read of the present
text and can be cited as such.)

**P4. "Independent".** "independently written programs" (line 11), "independently written code"
(line 332), "reviewers that did not write them": independent of what? If programs and reviews were
produced by separate sessions of the same AI system, say so; a specialist will otherwise read
"independent" as "human or different system".

**P5. Coverage of Table 3.** No row for Lemma 2.9, Lemma 3.1, Proposition 4.2, Lemmas 5.1–5.3,
Lemma 7.1, Corollary 1.3; the last row covers only "Theorems 1.2, 1.4". Add a row "all other
statements: written proofs only". The entry for Lemma 4.1 ("exact at leading order in $T$ for the
seven-point plant") is not intelligible without the program. The declaration says "the deterministic
lemmas have been tested"; the record also lists Monte Carlo checks (4.1, 7.2) — consistent, but
Lemma 2.9 and 3.1 are deterministic and have no entry.

**P6.** The declaration says the proofs were "found and written ... on 10 November 2026"; the note is
dated the same day and reports simulations to $n=10^8$ and eight batteries of tests. If the
simulations or parts of the argument predate that day, say so.

The PDF renders cleanly (pages 8, 10, 15 inspected; no "??", no literal citations, tables within
margins; Table 2 sits at the foot of page 10 and its explanation begins on page 11).

## 5. Programs

All in `/private/tmp/claude-501/-Users-adamhadani-Development-math-proofs-superpatterns/0c33b450-b609-4fd6-9183-ef318e6a7155/scratchpad/ref4/`
(session scratch space; the sources are reproduced in the appendix so that they can be restored).
Pure Python 3, single process, each run under two minutes. Run from that directory.

| Command | What it does | Output |
|:--|:--|:--|
| `python3 t0_validate.py` | Cross-validates the containment routine (levels $\ell$, $N_S$) against generic brute-force pattern containment, $n\le9$, $S\in\{\emptyset,\{1\},\{2\},\{1,2\},\{1,3\}\}$ | 2000 (configuration, $S$) cases agree |
| `python3 t1_lemma35_33_32.py 7 400` and `... 20261110 500` | Random configurations of 15–30 points, same five $S$. Lemma 3.1(ii),(iii) at every point; Lemma 3.5 for every consecutive pair; then plants 3416725 at random real positions in one rectangle and checks Lemma 3.2 ($\ell(e)$, $h(f)$, $\mathcal E$ unchanged), Table 1, the lens of Definition 2.8 computed from the outside set, no lens at any other $b$ (Lemma 2.9(i)), and $\mathcal G_p=\{(e,f)\}$ by enumeration of all pairs | 900 configurations; 2,668 consecutive pairs; 740 plantings; 0 failures |
| `python3 t2_lemma34.py 11 1500` | Lemma 3.4, adversarial. Random part: plants into one or two *arbitrary* empty rectangles and adds twin anchors north-west/south-east of $e$ and $f$; enumerates all pairs with a planted rectangle. Exhaustive part: $e$, $f$, the seven points and two extra points in all relative positions ($S=\emptyset$ and $S=\{1\}$) | random: 1,120 configurations, 4,075 planted pairs, 530 with $\lvert\mathcal G_p\rvert=1$, **0 with $\lvert\mathcal G_p\rvert\ge2$**; exhaustive: 23,674 configurations, 0 violations. Negative controls: with (O5),(O6) dropped two pairs occur 665 + 650 times; with only (O6) dropped 394 + 284 times; with only (O5) dropped 380 + 298 times (so each rule is needed and both together suffice) |
| `python3 t3_constants.py` | Recomputes the constants of Lemmas 2.9(ii), 5.1–5.3, Section 6, Lemmas 7.1, 7.2, and the numbers of the introduction | as quoted in Section 1.3 |

Method note for the containment routine: $\mathcal U_{\Pi[1..t]}$ is computed on the grid of
locations from the definition of the direct sum only ($\gamma\oplus1$: a point above-right of a copy
of $\gamma$; $\gamma\oplus21$: an inversion whose lower corner is above-right of a copy of $\gamma$);
Lemma 3.1 is not used, it is tested. The lens test recomputes the board from the outside set $O$, as
in Definition 2.8, not from $P$.

Sources consulted on the web: arXiv:1911.12878 (He–Kwan), arXiv:1402.3842 (Burstein–Pantone),
arXiv:2002.12308 (Jelínek–Karpilovskij), Crossref records of 10.1112/blms.12345 and
10.46298/dmtcs.6171.

## Appendix: program sources

### `core.py`

```python
"""Referee 4: definitions of the note, coded directly (Sections 2-3).
A configuration is a list of (x,y) with integer coordinates in 1..n, distinct abscissae
and distinct ordinates (not necessarily all of 1..n used).  Pattern Pi = W_S, S finite.
Locations are grid corners (i,j), 0<=i,j<=n, standing for (i+1/2, j+1/2):
SW(i,j) = points with x<=i and y<=j."""
import itertools, random

PLANT = [3, 4, 1, 6, 7, 2, 5]          # ordinate ranks left to right: u1 q1 u2 q2 v1 q3 v2

def rerank(pts):
    xs = sorted(p[0] for p in pts); ys = sorted(p[1] for p in pts)
    rx = {v: i + 1 for i, v in enumerate(xs)}; ry = {v: i + 1 for i, v in enumerate(ys)}
    return [(rx[x], ry[y]) for x, y in pts]

def upclose(base, n):
    g = base
    for i in range(n + 1):
        gi = g[i]; gp = g[i - 1] if i else None
        for j in range(n + 1):
            if not gi[j] and ((i and gp[j]) or (j and gi[j - 1])):
                gi[j] = True
    return g

def cont_grids(pts, n, S):
    """cont[t][i][j] = [ SW(i,j) contains Pi[1..t] ], for t = 0.. until empty (definition of
    direct sum only: gamma+1, gamma+21)."""
    cont = [[[True] * (n + 1) for _ in range(n + 1)]]
    t = 0
    while True:
        t += 1
        base = [[False] * (n + 1) for _ in range(n + 1)]
        m = t // 2
        if t % 2 == 0 and m in S:                    # Pi[1..2m] = Pi[1..2m-2] (+) 21
            prev = cont[t - 2]
            for a in pts:
                for c in pts:
                    if a[0] < c[0] and a[1] > c[1] and prev[a[0] - 1][c[1] - 1]:
                        base[c[0]][a[1]] = True
        else:                                        # Pi[1..t] = Pi[1..t-1] (+) 1
            prev = cont[t - 1]
            for r in pts:
                if prev[r[0] - 1][r[1] - 1]:
                    base[r[0]][r[1]] = True
        g = upclose(base, n)
        if not g[n][n]:
            return cont                              # N = len(cont)-1
        cont.append(g)

def levels(pts, cont):
    L = {}
    for r in pts:
        t = len(cont) - 1
        while not cont[t][r[0] - 1][r[1] - 1]:
            t -= 1
        L[r] = t + 1
    return L

def heights(pts):
    H = {}
    for r in sorted(pts, key=lambda p: -p[0]):
        H[r] = 1 + max([H[s] for s in H if s[0] > r[0] and s[1] > r[1]], default=0)
    return H

def lis_len(pts):
    best = {}
    for r in sorted(pts):
        best[r] = 1 + max([best[s] for s in best if s[0] < r[0] and s[1] < r[1]], default=0)
    return max(best.values(), default=0)

def lt(a, b): return a[0] < b[0] and a[1] < b[1]
def nw(a, c): return a[0] < c[0] and a[1] > c[1]
def inR(r, e, f): return lt(e, r) and lt(r, f)

def classify(r, e, f):
    if lt(r, f): return 'lower'
    if lt(e, r): return 'upper'
    return 'lateral'

def conditions(pts, e, f, L, H, t0):
    """returns dict O1..O6 (booleans), straight from the list in Section 3."""
    o = dict(O1=L[e] >= t0 + 1, O2=True, O3=True, O4=True, O5=True, O6=True)
    for r in pts:
        if r == e or r == f or inR(r, e, f): continue
        k = classify(r, e, f)
        if k == 'lower':
            if L[r] > L[e]: o['O2'] = False
            if L[r] == L[e] and nw(r, e): o['O5'] = False
        elif k == 'upper':
            if H[r] > H[f]: o['O3'] = False
            if H[r] == H[f] and nw(r, f): o['O6'] = False
        else:
            if L[r] >= L[e] + 2 and H[r] >= H[f] + 2: o['O4'] = False
    return o

def has_plant(pts, e, f):
    Q = sorted(r for r in pts if inR(r, e, f))
    if len(Q) != 7: return None
    ys = sorted(q[1] for q in Q)
    return Q if [ys.index(q[1]) + 1 for q in Q] == PLANT else None

def lens_at(pts, n, S, p, b, cont=None, H=None):
    """Definition 2.8 for (alpha,beta) = (Pi[1..p], I_b). Returns sorted inside points or None."""
    cont = cont or cont_grids(pts, n, S); H = H or heights(pts)
    if p >= len(cont): return None
    inside = [r for r in pts if cont[p][r[0] - 1][r[1] - 1]
              and lis_len([s for s in pts if lt(r, s)]) >= b]
    if len(inside) != 3: return None
    O = [r for r in pts if r not in inside]
    contO = cont_grids(O, n, S)
    X = sorted(r[0] for r in inside); Y = sorted(r[1] for r in inside)
    for i, x in enumerate(X):
        for j, y in enumerate(Y):
            inU = p < len(contO) and contO[p][x - 1][y - 1]
            inV = lis_len([s for s in O if s[0] > x and s[1] > y]) >= b
            if (i, j) == (0, 0):
                if inU: return None
            elif (i, j) == (2, 2):
                if inV: return None
            elif not (inU and inV): return None
    return sorted(inside)

def plant_into(pts, e, f, rng):
    """7 new points in the open rectangle R(e,f), order type 3416725, at random real positions
    (so that their coordinates interleave at random with those of the other points)."""
    xs = sorted(rng.uniform(e[0], f[0]) for _ in range(7))
    ys = sorted(rng.uniform(e[1], f[1]) for _ in range(7))
    new = [(xs[i], ys[PLANT[i] - 1]) for i in range(7)]
    allp = pts + new
    rk = rerank(allp)
    mp = dict(zip(allp, rk))
    return rk, mp[e], mp[f], [mp[q] for q in new]

# generic brute force, for cross-validation only
def prefix_pattern(S, t):
    seq = []
    m = 1
    while len(seq) < t:
        seq += [2 * m, 2 * m - 1] if m in S else [2 * m - 1, 2 * m]
        m += 1
    seq = seq[:t]; s = sorted(seq)
    return [s.index(v) + 1 for v in seq]

def contains_bf(pts, pat):
    k = len(pat)
    P = sorted(pts)
    for comb in itertools.combinations(P, k):
        ys = [c[1] for c in comb]; s = sorted(ys)
        if [s.index(v) + 1 for v in ys] == pat: return True
    return k == 0
```

### `t0_validate.py`

```python
"""Cross-validate the direct-sum DP (cont_grids, levels, N) against generic brute-force containment."""
import random, sys
from core import *
rng = random.Random(1)
cnt = 0
for trial in range(400):
    n = rng.randint(5, 9)
    perm = list(range(1, n + 1)); rng.shuffle(perm)
    pts = [(i + 1, perm[i]) for i in range(n)]
    for S in [set(), {1}, {2}, {1, 2}, {1, 3}]:
        cont = cont_grids(pts, n, S)
        N = len(cont) - 1
        # N by brute force
        t = 0
        while contains_bf(pts, prefix_pattern(S, t + 1)): t += 1
        assert t == N, (pts, S, t, N)
        L = levels(pts, cont)
        for r in pts:
            sw = [s for s in pts if lt(s, r)]
            t = 0
            while contains_bf(sw, prefix_pattern(S, t + 1)): t += 1
            assert L[r] == t + 1, (pts, S, r)
        cnt += 1
print("validated", cnt, "(config,S) cases: DP levels and N agree with generic brute force")
```

### `t1_lemma35_33_32.py`

```python
"""Lemma 3.1 (ii),(iii); Lemma 3.5 (leftmost optimal copy; (O1)-(O6) for consecutive pairs);
Lemma 3.2 (conditions do not see the rectangle); Lemma 3.3 (table + lens);
Prop. 4.2 membership ((z_{p-1},z_p) plus plant lies in G_p) and |G_p| = 1 (Lemma 3.4)."""
import random, sys
from core import *
seed = int(sys.argv[1]) if len(sys.argv) > 1 else 7
trials = int(sys.argv[2]) if len(sys.argv) > 2 else 400
rng = random.Random(seed)
SS = [set(), {1}, {2}, {1, 2}, {1, 3}]
st = dict(configs=0, pairs35=0, plants=0, lens_ok=0, skipped_smallN=0, l31=0, uniq_b=0)
for trial in range(trials):
    n = rng.randint(15, 30)
    perm = list(range(1, n + 1)); rng.shuffle(perm)
    pts = [(i + 1, perm[i]) for i in range(n)]
    S = SS[trial % len(SS)]
    t0 = 2 * max(S) if S else 0
    cont = cont_grids(pts, n, S); N = len(cont) - 1
    L = levels(pts, cont); H = heights(pts)
    st['configs'] += 1
    # Lemma 3.1 (ii), (iii)
    for r in pts:
        if L[r] >= t0 + 1:
            below = [L[s] for s in pts if lt(s, r)]
            assert L[r] == 1 + max([t0] + below), ('3.1ii', pts, S, r)
            assert L[r] + H[r] - 1 <= N, ('3.1iii', pts, S, r)
            st['l31'] += 1
        for s in pts:
            if lt(s, r) and L[s] >= t0 + 1: assert L[r] >= L[s] + 1
    if N < t0 + 2:
        st['skipped_smallN'] += 1; continue
    z = {}
    for i in range(t0 + 1, N + 1):
        G = [r for r in pts if L[r] == i and H[r] == N - i + 1]
        assert G, ('G empty', pts, S, i)
        z[i] = min(G)
    cand = []
    for i in range(t0 + 1, N):
        e, f = z[i], z[i + 1]
        assert lt(e, f), ('not e<f', pts, S, i)
        assert not any(inR(r, e, f) for r in pts), ('R not empty', pts, S, i)
        o = conditions(pts, e, f, L, H, t0)
        assert all(o.values()), ('E fails', pts, S, i, o)
        st['pairs35'] += 1
        cand.append(i)
    # plant into one random consecutive pair
    i = rng.choice(cand); e, f = z[i], z[i + 1]
    pts2, e2, f2, new = plant_into(pts, e, f, rng)
    n2 = n + 7
    cont2 = cont_grids(pts2, n2, S); L2 = levels(pts2, cont2); H2 = heights(pts2)
    # Lemma 3.2
    assert L2[e2] == L[e] and H2[f2] == H[f], ('3.2 numbers', pts, S, i)
    o2 = conditions(pts2, e2, f2, L2, H2, t0)
    assert all(o2.values()), ('3.2 E', pts, S, i, o2)
    # Lemma 3.3: table
    p = L2[e2] + 1; b = H2[f2] + 1
    assert p == i + 1
    u1, q1, u2, q2, v1, q3, v2 = new
    assert [L2[x] - p for x in new] == [0, 1, 0, 2, 3, 1, 2], ('levels', pts, S, i)
    assert [H2[x] - b for x in new] == [3, 2, 2, 1, 0, 1, 0], ('heights', pts, S, i)
    ins = lens_at(pts2, n2, S, p, b, cont2, H2)
    assert ins == sorted([q1, q2, q3]), ('lens', pts, S, i, ins)
    st['lens_ok'] += 1
    # Lemma 2.9(i): no lens at (Pi[1..p], b') for b' != b
    for bb in range(0, b + 6):
        if bb != b: assert lens_at(pts2, n2, S, p, bb, cont2, H2) is None, ('second lens', pts, S, i, bb)
    st['uniq_b'] += 1
    # G_p by full enumeration over all pairs of the planted configuration
    Gp = []
    for a in pts2:
        for c in pts2:
            if lt(a, c) and L2[a] == p - 1 and has_plant(pts2, a, c) and all(conditions(pts2, a, c, L2, H2, t0).values()):
                Gp.append((a, c))
    assert Gp == [(e2, f2)], ('G_p', pts, S, i, Gp)
    st['plants'] += 1
print(st)
```

### `t2_lemma34.py`

```python
"""Lemma 3.4, adversarial.  (a) random: plant 3416725 into one or two arbitrary empty rectangles
R(e,f) (no condition imposed on (e,f) beyond level(e) >= t0+1), and optionally add 'twin' anchors
e' north-west of e / f' north-west or south-east of f that keep the rectangle content unchanged;
then enumerate ALL pairs of the final configuration and check, for every p,
   #{pairs with plant, level(e)=p-1, (O1)-(O6)} <= 1,  and a lens at (Pi[1..p], h(f)+1) if = 1.
Negative control: count configurations where two pairs satisfy (O1)-(O4) [(O5),(O6) dropped].
(b) exhaustive: e, f, the seven planted points and two extra points in all relative positions."""
import random, sys, itertools
from core import *
seed = int(sys.argv[1]) if len(sys.argv) > 1 else 11
trials = int(sys.argv[2]) if len(sys.argv) > 2 else 1500
rng = random.Random(seed)
SS = [set(), {1}, {2}, {1, 2}]
st = dict(configs=0, with_Gp=0, viol=0, neg_two_O1234=0, neg_two_O12345=0, neg_two_O12346=0, lens_checked=0,
          pairs_with_plant=0, twin_e=0, twin_f=0)

def analyse(pts, S, check_lens=True):
    n = len(pts)
    t0 = 2 * max(S) if S else 0
    cont = cont_grids(pts, n, S); L = levels(pts, cont); H = heights(pts)
    byp = {}
    for a in pts:
        for c in pts:
            if lt(a, c) and L[a] >= t0 + 1 and has_plant(pts, a, c):
                o = conditions(pts, a, c, L, H, t0)
                byp.setdefault(L[a] + 1, []).append((a, c, o))
                st['pairs_with_plant'] += 1
    st['configs'] += 1
    for p, lst in byp.items():
        full = [(a, c) for a, c, o in lst if all(o.values())]
        o4 = [(a, c) for a, c, o in lst if o['O1'] and o['O2'] and o['O3'] and o['O4']]
        o45 = [(a, c) for a, c, o in lst if o['O1'] and o['O2'] and o['O3'] and o['O4'] and o['O5']]
        o46 = [(a, c) for a, c, o in lst if o['O1'] and o['O2'] and o['O3'] and o['O4'] and o['O6']]
        if len(o4) >= 2:
            st['neg_two_O1234'] += 1
            if len({a for a, c in o4}) >= 2: st['twin_e'] += 1
            if len({c for a, c in o4}) >= 2: st['twin_f'] += 1
        if len(o45) >= 2: st['neg_two_O12345'] += 1
        if len(o46) >= 2: st['neg_two_O12346'] += 1
        if len(full) >= 2:
            st['viol'] += 1; print('VIOLATION', pts, S, p, full)
        if len(full) == 1:
            st['with_Gp'] += 1
            if check_lens:
                a, c = full[0]
                assert lens_at(pts, n, S, p, H[c] + 1, cont, H) is not None, ('no lens', pts, S, p)
                st['lens_checked'] += 1
        # every pair satisfying O1-O4 must give a lens (Lemma 3.3) - spot check
        if check_lens and len(o4) >= 2:
            for a, c in o4[:2]:
                assert lens_at(pts, n, S, p, H[c] + 1, cont, H) is not None, ('no lens O1-4', pts, S, p)

def empty_pairs(pts, L, t0):
    return [(a, c) for a in pts for c in pts if lt(a, c) and L[a] >= t0 + 1 and not any(inR(r, a, c) for r in pts)]

for trial in range(trials):
    n = rng.randint(8, 22)
    perm = list(range(1, n + 1)); rng.shuffle(perm)
    pts = [(float(i + 1), float(perm[i])) for i in range(n)]
    S = SS[trial % len(SS)]
    t0 = 2 * max(S) if S else 0
    ipts = rerank(pts)
    cont = cont_grids(ipts, n, S); L = levels(ipts, cont)
    back = dict(zip(ipts, pts))
    ep = [(back[a], back[c]) for a, c in empty_pairs(ipts, L, t0)]
    if not ep: continue
    for rep in range(rng.choice([1, 1, 2])):
        e, f = rng.choice(ep)
        if any(inR(r, e, f) for r in pts): continue
        xs = sorted(rng.uniform(e[0], f[0]) for _ in range(7)); ys = sorted(rng.uniform(e[1], f[1]) for _ in range(7))
        new = [(xs[i], ys[PLANT[i] - 1]) for i in range(7)]
        pts = pts + new
        mode = rng.randrange(4)
        lo_x, lo_y = min(xs), min(ys); hi_x, hi_y = max(xs), max(ys)
        if mode in (1, 3):      # twin anchor e' north-west of e, below the plant (keeps R(e',f) content)
            left = max([r[0] for r in pts if r[0] < e[0]], default=e[0] - 1)
            pts.append((rng.uniform(left, e[0]) if rng.random() < .7 else e[0] - rng.uniform(0, 3), rng.uniform(e[1], lo_y)))
        if mode in (2, 3):      # twin anchor f' north-west of f, right of the plant
            up = min([r[1] for r in pts if r[1] > f[1]], default=f[1] + 1)
            pts.append((rng.uniform(hi_x, f[0]), rng.uniform(f[1], up) if rng.random() < .7 else f[1] + rng.uniform(0, 3)))
        if rng.random() < .3:   # twin south-east of e / south-east of f
            pts.append((rng.uniform(e[0], lo_x), e[1] - rng.uniform(0, 2)))
        if rng.random() < .3:
            pts.append((f[0] + rng.uniform(0, 2), rng.uniform(hi_y, f[1])))
    if len({p[0] for p in pts}) < len(pts) or len({p[1] for p in pts}) < len(pts): continue
    analyse(rerank(pts), S)
print('random part:', st)

# (b) exhaustive: skeleton + two extra points in all relative positions
st2 = dict(st); 
for k in st: st[k] = 0
for S, pre in [(set(), []), ({1}, [(-3.0, -2.0), (-2.0, -3.0)])]:
    base = pre + [(0.0, 0.0)] + [(i + 1.0, float(PLANT[i])) for i in range(7)] + [(8.0, 8.0)]
    bx = sorted(p[0] for p in base); by = sorted(p[1] for p in base)
    gx = [bx[0] - 1] + [(bx[i] + bx[i + 1]) / 2 for i in range(len(bx) - 1)] + [bx[-1] + 1]
    gy = [by[0] - 1] + [(by[i] + by[i + 1]) / 2 for i in range(len(by) - 1)] + [by[-1] + 1]
    for x1 in gx:
        for y1 in gy:
            for x2 in gx:
                for y2 in gy:
                    # second point: same gap allowed on either side of the first
                    for dx in ((0,) if x1 != x2 else (-.1, .1)):
                        for dy in ((0,) if y1 != y2 else (-.1, .1)):
                            if (x2 + dx, y2 + dy) < (x1, y1) and x1 != x2 and y1 != y2: continue   # unordered
                            analyse(rerank(base + [(x1, y1), (x2 + dx, y2 + dy)]), S, check_lens=False)
print('exhaustive part (two extra points):', st)
```

### `t3_constants.py`

```python
"""Recompute every numerical constant of Sections 5-7 and of the introduction."""
from math import *
from itertools import permutations
print("== Lemma 2.9(ii): lens board ==")
fills = [p for p in permutations(range(3)) if p[0] != 0 and p[2] != 2]
def Dinv(p):
    for i in range(3):
        for j in range(i + 1, 3):
            if p[i] > p[j]:                       # a=(i,p[i]) NW of c=(j,p[j]); corners (i,p[j]) and (j,p[i])
                if (i, p[j]) != (0, 0) and (j, p[i]) != (2, 2): return True
    return False
print(" valid fillings", [''.join(str(v + 1) for v in p) for p in fills], " without D-inversion:",
      [''.join(str(v + 1) for v in p) for p in fills if not Dinv(p)], " rho =", (sum(not Dinv(p) for p in fills) - 1), "/", len(fills))
print("== Lemma 5.1 ==  2*0.132^2*2 =", 2 * 0.132**2 * 2, " 1-exp(-1) =", 1 - exp(-1))
A1 = 1e-10
print("== Lemma 5.2 ==  8*sqrt(A1/2) =", 8 * sqrt(A1 / 2), " 16 e^2 (A1/2)^(1/4) =", 16 * exp(2) * (A1 / 2) ** .25, " <1/3:", 16 * exp(2) * (A1 / 2) ** .25 < 1 / 3)
print("== Lemma 5.3 ==  4exp(-4) =", 4 * exp(-4), "; 0.063*floor(T/2) >= 0.03T for T>=50:",
      all(0.063 * floor(T / 2) >= 0.03 * T for T in [50 + 0.01 * i for i in range(200000)]))
print("== Section 6 ==")
print(" K<=45.1 lnT iff lnT>=10;  (A2) exponent 4-0.069*90 =", 4 - 0.069 * 90, "; (A3) exponent 2-90 ln3 =", 2 - 90 * log(3))
c1 = 0.015 / 45.1**2; c2 = A1**7 / (6 * factorial(7)**2)
print(" 0.015/45.1^2 =", c1, " A1^7/(6*7!^2) =", c2, " product with 7e-6:", 7e-6 * 6.5e-79, " exact product:", c1 * c2)
for d in (5, 9, 22, 44):                      # T = 10^d, exact integer arithmetic for the index check
    T = 10**d; lnT = d * log(10); K = ceil(45 * lnT); J = (15 * T) // (1000 * K)
    ok = 100 * (4 * K * J - 2) < 6 * T              # iota0+2K <= 4KJ-2 < 0.06 T
    lg = lambda x: x / log(10)                      # log10 of the three failure probabilities
    fails = [-1e-4 * (T - 2) / log(10) if d < 300 else float('-inf'), 4 * d - 0.069 * 2 * K / log(10), log10(2 * d * log2(10) + 5) + 2 * d - 2 * K * log10(3)]
    print("  T=1e%d: K=%d, (J/K)/(T/lnT^2) = %.4g ; iota0+2K <= 4KJ-2 < 0.06T: %s ; log10 P(A1,A2,A3 fail) <= %s" % (
        d, K, (J / K) * lnT**2 / T, ok, ['%.1f' % v for v in fails]))
print("== Lemma 7.1 ==")
print(" 3*sqrt(2) =", 3 * sqrt(2), "<=5;  sqrt(8*pi*5) =", sqrt(40 * pi), "<=12;  sqrt(16*pi*5) =", sqrt(80 * pi),
      "; +32 <= 17 sqrt(T) needs T >=", (32 / (17 - sqrt(80 * pi)))**2)
print(" s^2/(80T) with s=20 sqrt(T lnT): 400/80 =", 400 / 80, "(so exp(-5 lnT)=T^-5)")
print("== Lemma 7.2 ==")
s = 0.5 * sum(2**(-i / 2) * (1 + sqrt(i)) for i in range(0, 400))
print(" (1/2) sum 2^(-i/2)(1+sqrt i) =", s, "; 45*that =", 45 * s, "<= 171")
print(" 18 sqrtT + 2 <= 2 sqrt(T lnT) needs lnT >= about", [L for L in range(1, 200) if 18 + 2 * exp(-L / 2) <= 2 * sqrt(L)][0],
      "(so 'large T' in Lemma 7.2 means T >= e^82 with the constant 22)")
print("== Introduction ==  c21 = 0.99887: 2(1-c21) =", 2 * (1 - 0.99887), " eps0 =", 0.99887**-2 - 1)
print("== Theorem 1.2 == sign change of (1/2)1e-84/lnT^2 - 200 sqrt(lnT/T): lnT ~",
      [L for L in range(100, 2000) if 0.5e-84 / L**2 > 200 * sqrt(L) * exp(-L / 2)][0])
```

