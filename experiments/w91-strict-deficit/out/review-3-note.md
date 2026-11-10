# Review 3 — cold referee report on `output/paper/layered-refutation.md`

Date: 2026-11-10. Reviewer: AI referee (cold read). Scope: the note only (13 pp., "A layered pattern and the
sharp form of Alon's conjecture on random superpatterns"). No other file of the repository was opened
(no `proof.md`, logs or earlier reviews); line numbers below (`L…`) refer to the Markdown source.

## 0. Verdict in one paragraph

I tried to break every statement and could not. **I found no error that invalidates any lemma, Theorem 3,
Theorem 1 or Corollary 2.** Every statement was re-derived by hand in order; the deterministic core
(Lemmas 4–7, Theorem 8, Lemma 11, Lemmas 12–16) was additionally re-implemented from the definitions and
checked by programs written for this review (Section 6, Appendix); every numerical constant was recomputed.
What I did find: about a dozen places where a step is missing or a sentence is literally imprecise (all
repairable in one or two lines, none affecting a conclusion), one optional simplification of the tie-break
rules, and a heavy load of overloaded notation that will slow a human referee considerably. **The note is fit
to be sent to a specialist after a notation pass.** Residual risk: this is one more non-specialist AI reading;
agreement between my derivation and my programs covers the combinatorial core well, the probabilistic part
(Mecke, Talagrand, Alexander-type rate) rests on hand derivation plus standard theorems whose statements I
could confirm only through secondary sources.

## 1. What was done

* Hand re-derivation of every statement in the order of the note (Section 2 below).
* Programs (Appendix; all outputs in Section 6): exhaustive check of Section 2 of the note on $S_n$, $n\le7$;
  random and adversarial tests of Lemmas 11–16 from the fibre definitions; Monte Carlo check of the
  structure of Lemma 17 with a one-point plant; recomputation of all constants.
* External facts: He–Kwan abstract (arXiv:1911.12878) confirms the form of Alon's conjecture
  ($n=(1+\varepsilon)k^2/4$, every fixed $\varepsilon>0$) and the bound $2000k^2\log\log k$. Alon–Spencer
  Thm 7.7.1 (form $\Pr[X\le b-tK\sqrt{f(b)}]\Pr[X\ge b]\le e^{-t^2/4}$) and Last–Penrose Thm 4.4
  (multivariate Mecke) were confirmed through papers that quote them, not from the books themselves.
  Not checked: the numbering "Conjecture 1.1" in [HK20]; the attributions to [JK21], [BWX07], [BP15],
  [Alexander94] (the note does not depend on them: Theorem 8 is proved in full, and Lemma 23 is proved in full).
* Not verifiable from the note and not verified: the simulation figures ($0.0023\sqrt n$, $c_{21}\approx0.99887$),
  the verification table of the last section, Remark (i) after Theorem 3 (eight-point pattern, $cT/\ln T$),
  and the novelty claim.

## 2. Verdict per statement

Legend: **C** correct as written; **C+** correct, a step is missing or a phrase is imprecise (item number in
Section 3); **W** wrong. There is no **W**.

| Statement | Verdict | Notes |
|:--|:--|:--|
| Lemma 4 | C | Both directions and the "then $p,q\in I$" clauses checked (weak monotonicity of $U$, $S$ is what is used for the corners). |
| Lemma 5 | C | The extremal copy avoids all of $P\cap U$, a fortiori $I$. Machine-checked on all cells and half-integer locations, $n\le7$. |
| Lemma 6 | C+ | G1: the converse inclusion ("exactly the $P_f$") needs "inside points of $P'$ lie on the board by Lemma 5 for $P'$". Class sizes $=F$ machine-checked. |
| Lemma 7 | C | (i) inversion count increases, (ii) decreases; new points stay on the board. |
| Theorem 8 | C+ | Identity (1) verified exactly on $S_n$, $n\le7$, 13 pairs $(\alpha,\beta)$. G2: the $P_T$ version needs one sentence. |
| Corollary 9 | C | Also valid for $S'=\mathbb N$ (finitely many blocks below $t$). |
| Lemma 10 | C | Telescoping and the re-indexing $t=2i+b$ checked; all terms $\ge0$ so rearrangement is free. |
| Lemma 11 | C+ | $F=3$, $a=2$ checked by hand for 231, 312, 321; uniqueness of $b$ correct. G3: uniqueness should be a numbered statement (it is cited later as "the last part of the proof"). |
| Lemma 12 | C+ | G4: in (b) the maximum over an empty set. |
| Lemma 13 | C | Checked (O1)–(O6) and $\{\ell(e)=p-1\}$ one by one; the key sentence is cryptic (R7). |
| Lemma 14 | C | All seven levels/heights and all nine cells recomputed (table in Section 4.3); 8,040 + 98,845 machine checks from the fibre definitions. |
| Lemma 15 | C+ | G5: the step $x=x'$ silently uses $e=e'$. Machine-checked on 54,649 adversarial cases, 26,395 of them with competing pairs. |
| Lemma 16 | C+ | G6: two silent steps (leftmost = topmost in an antichain; why the maximum in 12(b) is attained by a point). 30,888 pairs machine-checked. |
| Lemma 17 | C | Legitimate use of the bivariate Mecke equation; see Section 4.2. |
| Proposition 18 | C | $\Pr(\mathcal G_p\ne\emptyset)=\mathbb E|\mathcal G_p|$ by Lemma 15; the Lemma 16 pair is one term of a non-negative sum on $\{N\ge p\}$. |
| Lemma 19 | C | $2(0.132)^2\cdot2=0.0697$; domain of integration has volume $T^4/4$. |
| Lemma 20 | C | Covering, tilt bound, $16e^2(A_1/2)^{1/4}=0.31438$; all recomputed. |
| Lemma 21 | C | $4e^{-4}=0.07326$; $0.063\lfloor T/2\rfloor\ge0.03T$ iff $T\ge42$. |
| Theorem 3 | C | Index bookkeeping, pigeonhole, $\Pr(\mathcal A)$ and the constant ($4.59\cdot10^{-84}\ge10^{-84}$) all confirmed. |
| (F1) | C | |
| (F2) | C | "moved" = removed then added, each monotone and 1-Lipschitz. |
| (F3) | C+ | G8: Fekete for a real variable; "Poissonisation" is one line but is not written. $\lambda(T)\le2T$ is justified. |
| (F4) | C+ | G7: "Corollary 9 … conditioned on the number of points" is not a valid inference as worded; the statement is true. |
| Lemma 22 | C+ | G9: certificate size for non-integer level; G10: two implicit steps. All three pieces of the integral check. |
| Lemma 23 | C+ | G11: edge cases and the range of the grid index. Cutting, reflection, union bound in expectation, iteration, $3.7797<3.79$, $45\cdot3.79\le171$ all confirmed. |
| Theorem 1 | C | All inequalities point the right way; no circularity ($c_{21}$ is defined by Fekete before Theorem 3 is used). |
| Corollary 2 | C+ | G12: odd $k$; $u$ capped at $5\sqrt n$. |

## 3. Errors and gaps, by severity

### 3.1 Fatal or serious

None found.

### 3.2 Minor: literal imprecision or missing step (no conclusion changes)

**G7 — (F4), L209.** Quoted: "The first inequality is Corollary 9 with $S=\emptyset$, conditioned on the number
of points." Reason: Corollary 9 is stated for $P_T$; an inequality between expectations over a Poisson mixture
does not pass to each $n$ by conditioning. Repair: "Theorem 8 holds for $\sigma_n$, so the proof of Corollary 9
applies verbatim to $\sigma_n$; with $S=\emptyset\subset S'=\mathbb N$ it gives
$2\mu_n\le\mathbb EN_{\mathbb N}(\sigma_n)\le\mathbb E\,\mathrm{LIS}(\sigma_n)$." Better: state Corollary 9 for
both models.

**G9 — Lemma 22, L214.** Quoted: "$f$-certifiable with $f(s)=2s$ … for all $b,t\ge0$." Reason: for non-integer
$s$ the event $Y_n\ge s$ needs $2\lceil s\rceil>2s$ points, so the inequality is available as stated only for
integer $b$. Repair: choose an integer median $m_n$; for the lower tail $b=m_n$ is an integer; for the upper
tail apply the inequality with $b=m_n+\lceil u\rceil$ and use that $u\mapsto u^2/(m_n+u)$ is increasing, which
gives the displayed bound $2\exp(-u^2/(8(m_n+u)))$ unchanged. (Also exclude $m_n=0$, harmless for $n\ge n_0$.)

**G5 — Lemma 15, L147.** Quoted: "Then $x'$ is of class (b) for $(e,x)$, and
$(R(e,x')\setminus R(e,x))\cap P=Q'\setminus R(e,x)=\emptyset$." Reason: both claims use $e=e'$, proved in the
previous paragraph but not invoked ($x'>e$ because $x'>e'=e$; $P\cap R(e,x')=P\cap R(e',x')=Q'$). Repair: start
the paragraph with "By the previous step $e=e'$." Also say once why "exchanging the pairs" is legitimate:
everything used so far ($Q=Q'$, $h(x)=h(x')$, membership in $\mathcal G_p$) is symmetric in the two pairs.

**G2 — Theorem 8 / Lemma 11, L60 and L92.** Quoted: "The same holds with $P_T$ in place of $\sigma_n$" and (L34)
"every statement below about the probability that $\sigma_n$ contains a pattern holds for $P_T$". Reason: (1)
and Lemma 11 involve $F$, $a$ and the lens event, not only containment probabilities. Repair: add "$F$, $a$,
and the property of having a lens depend only on the order type of the configuration; given $|P_T|=n$ the
order type is uniform on $S_n$, so (1) and every consequence hold for $P_T$ by averaging over $n$."

**G3 — Lemma 11 / Lemma 15, L92 and L141.** Quoted (L141): "by the last part of the proof of Lemma 11 there is
only one such $b$". Reason: a fact used later is buried in a proof. Repair: make it Lemma 11(ii): "For fixed
$\alpha$, a configuration has a lens at $(\alpha,b)$ for at most one $b$; the inside set and $b$ are then
determined by $P$ and $\alpha$."

**G6 — Lemma 16, L151.** (a) Quoted: "so $z_i$ is its north-west-most point" and "the ordinate of … $w'$, which
is at most that of $z_{i+1}$". Missing: in an antichain the leftmost point is the topmost. (b) Quoted: "by
Lemma 12(b) some $r<q$ has $\ell(r)=i$". Missing: $\ell(q)=i+1\ge T_0+2$, so the maximum in Lemma 12(b) is
$i\ge T_0+1>T_0$ and is attained by a point, not by the term $T_0$. (c) "(O2): $r<x$ gives $\ell(r)\le i$ by
Lemma 12(b)": only if $\ell(r)\ge T_0+1$; otherwise $\ell(r)\le T_0\le i$ trivially.

**G1 — Lemma 6, L50–52.** Quoted: "Consequently the configurations with outside set $O$ and inside coordinate
sets $X,Y$ are exactly the $P_f$". Missing: if $P'$ is such a configuration, its inside points lie in
$U_\alpha(P')\cap S_\beta(P')=U_\alpha(O)\cap S_\beta(O)$ by Lemma 5 applied to $P'$, hence on the board, so
$P'=P_f$ for a valid $f$.

**G4 — Lemma 12(b), L105.** Quoted: "Let $m$ be the maximum of $\ell(r)$ over $r<q$." Undefined when no point
lies below $q$; say "$m=0$ if there is none".

**G8 — (F3), L208.** (a) Fekete's lemma is applied to a function of a real variable; it needs $\ell$ bounded on
bounded intervals (true: $\ell$ is non-decreasing and $\ell\le\lambda<\infty$). (b) "the limit being 2 by
[LS77; VK77] and Poissonisation": write the line ($\lambda(T)=\mathbb E\,g(N)$ with $g(n)=\mathbb E\,\mathrm{LIS}(\sigma_n)$
non-decreasing, $g(n)\le3\sqrt n$, $N$ concentrated at $T^2$), or cite the Poisson statement directly.
**Answer to the question asked: yes, $\lambda(T)\le2T$ is justified** — superadditivity gives
$\lambda(T)/T\le\sup=\lim=2$.

**G10 — Lemma 22, L214–218.** (a) "$m_n-\mu_n\le\int_0^\infty2e^{-u^2/(8m_n)}du$" uses
$m_n-\mu_n\le\mathbb E(m_n-Y_n)^+=\int_0^\infty\Pr(Y_n\le m_n-u)\,du$; say so. (b) The Poisson tail
$\Pr(|N-T^2|>T\ln T)\le2e^{-(\ln T)^2/3}$ is used without mention (Bernstein/Chernoff for Poisson, valid for
large $T$). (c) The integral is split as $\int_s^{5T}+\int_{5T}^\infty$ and the last piece is bounded by
$\mathbb E[Y;Y\ge5T]\le\mathbb E[N;\mathrm{LIS}\ge5T]$; "its contribution" should be written as this chain.

**G11 — Lemma 23, L223–227.** (a) Cases $j^*=0$ and $j^*=m$ (no $c_{j^*}$, resp. no $c_{j^*+1}$): the bound
$m\le1+M+M'$ still holds, say so. (b) "there are $\lceil4T^2\rceil$ values of $k$": true with closed intervals
$k\delta\le x\le(k+1)\delta$, $k=0,\dots,\lceil4T^2\rceil-1$. (c) $\tilde R_k$ can stick out of $[0,2T]^2$; this
is why $P$ lives on the quadrant — say so. (d) "$\ell(T')\le\ell(T)+1$ by (F2)" also uses that the expected
number of points of $[0,T']^2\setminus[0,T]^2$ is $1$. **Answers to the questions asked:** exactly one block
($\beta_{j^*+1}$) is lost; both rectangles have area $x(2T-x)\le T^2$; the reflection maps $R_x$ to $R'_{2T-x}$
and $21^{\oplus m}$ is invariant under reverse-complement; $\mathbb EM\le a+\sum_k\mathbb E(X_k-a)^+$ needs no
independence.

**G12 — Corollary 2, L237.** (a) For odd $k$ the pattern $21^{\oplus\lfloor k/2\rfloor}$ has length $k-1$; "not a
$k$-superpattern" follows because it is contained in a pattern of length $k$ — say so. (b) The tail bound is
stated for $0\le u\le5\sqrt n$ while the needed $u=\eta c_{21}\sqrt n-O(n^{1/4})$; use monotonicity in $u$ (or
note $\eta c_{21}<5$). (c) "fix $\varepsilon<\varepsilon_0$" should read "$0<\varepsilon<\varepsilon_0$" (or
$-1<\varepsilon$).

**G13 — Abstract, L6.** Quoted: "which gives $\mathbb E\,\mathrm{LIS}-2\,\mathbb EL_{21}\ge c\sqrt n/(\ln n)^2$".
Theorem 3 is proved for the Poisson process only; the statement for $\sigma_n$ needs
$|\lambda(\sqrt n)-\mathbb E\,\mathrm{LIS}(\sigma_n)|=O(\ln n)$ (same argument as for $\ell$), which the note
does not contain. Either say "in the Poissonised model" or add the line.

**G14 — Theorem 3 vs Section 3, L19 and L96/L190.** $T_0$ is the threshold in the statement of Theorem 3 and,
inside the proof of that same theorem, the number $2i_{j-1}$. Not a mathematical error, but it is a collision
inside one proof and must be fixed (see R1).

### 3.3 Optional simplification (found while testing; not an error)

**The emptiness clauses in (O5) and (O6) are not needed.** Define (O5′): "no $e'$ of class (a) with
$\ell(e')=\ell(e)$ and $e'$ north-west of $e$", and (O6′) likewise. Lemma 13 is unaffected; the proof of
Lemma 16 already proves (O5′), (O6′) (it never uses the clause); and in Lemma 15 the paragraph "Let $z\in P$
with $e'<z<x$ … Hence $(R(e',x)\setminus R(e,x))\cap P=\emptyset$" can be deleted, because $e'$ (class (a),
same level, north-west of $e$) violates (O5′) outright, and $x'$ violates (O6′) outright. Checked by
`simplified_tiebreak.py`: Lemma 16 on 6,714 pairs, and $\mathcal G_p=\{(z_{p-1},z_p)\}$ in 1,787 plantings.
The author should re-derive this before adopting it.

## 4. The points singled out for hostile reading

### 4.1 Lemma 11

* Fillings of a lens board: of the six bijections, 123, 132 use $(x_1,y_1)$ and 213 uses $(x_3,y_3)$; 231,
  312, 321 remain, $F=3$. In 321 the pair in columns $x_1,x_2$ has corners $(x_1,y_2)$, $(x_2,y_3)$, both on
  the board. In 231 the two inversions have lower corner $(x_1,y_1)$, resp. upper corner $(x_3,y_3)$; in 312
  likewise. So $a=2$.
* At most one $b$: correct. For the rightmost inside point $q$ of a lens at $(\alpha,b)$, $h(q)\ge b+2$ would
  produce an inside point $r>q$ to its right; so $h(q)=b+1$ and for $b'>b$ at most two inside points remain.
  (No lens exists for $b=0$ or empty $\alpha$, consistently with the definition.) Machine check: in 8,040
  planted configurations exactly one $b$ gives a lens at $(\Pi[1..p],b)$.
* Passage to $P_T$: correct, with the sentence of G2.

### 4.2 Lemma 13 and Lemma 17

Each condition was checked against the definition of the classes:

| Item | Quantities involved | Why they ignore $P\cap R$ |
|:--|:--|:--|
| $\ell(e)=p-1$, (O1) | $\mathrm{SW}(e)$ | $R$ lies above-right of $e$ |
| (O2) | $\ell(r)$, $r<x$, $r\notin R$; $\ell(e)$ | a point $q\in R$ with $q<r<x$ would force $r\in R$ |
| (O3) | $h(r)$, $r>e$, $r\notin R$; $h(x)$ | symmetric |
| (O4) | $\ell(r)$, $h(r)$ for $r$ of class (c) | $r$ is north-west or south-east of all of $R$ (checked: class (c) $\Leftrightarrow$ $x_r<x_e,\ y_r>y_x$ or $x_r>x_x,\ y_r<y_e$) |
| (O5) | class (a) points, their levels, $P\cap(R(e',x)\setminus R)$ | all outside $R$ |
| (O6) | class (b) points, their heights, $P\cap(R(e,x')\setminus R)$ | all outside $R$ |

The level $\ell(r)$ depends on $P$ only through $\mathrm{SW}(r)$ by its definition (not only via Lemma 12), so
no hypothesis on $T_0$ is needed here. The set of points of each class is the same for $P$ and $P'$.
Mecke: $f(e,x,\eta)=\mathbf 1\{e<x\}\,\Phi(e,x,\eta\setminus R(e,x))\,\mathbf 1\{\eta\cap R(e,x)\cong3416725\}$ is
a measurable function of finitely many order comparisons; it vanishes unless $e<x$; on the right-hand side it
is evaluated on $P_T\cup\{e,x\}$, the two added points lie outside the open rectangle, and
$P_T\cap R$, $P_T\setminus R$ are independent. Both sides equal
$\iint_{e<x}\mathbb E\Phi\cdot e^{-A}A^7/(7!)^2$. Correct. A Monte Carlo check of the same identity with a
one-point plant (same indicator, $|P\cap R|=1$ against $|R|$) agrees within one standard error for three
choices of $(S,p)$ (Section 6).

### 4.3 Lemma 14: the seven points

Recomputed by hand (levels via Lemma 12(b) and (O2); heights via (O3)); the note states only the entries it
needs, the others are mine.

| Point | value in 3416725 | points of $Q$ below | $\ell-p$ | points of $Q$ above | $h-b$ | inside? |
|:--|:--|:--|:--|:--|:--|:--|
| $u_1$ | 3 | — | 0 | $p_1,p_2,v_1,v_2$ | 3 | no (level) |
| $p_1$ | 4 | $u_1$ | 1 | $p_2,v_1,v_2$ | 2 | yes |
| $u_2$ | 1 | — | 0 | $p_2,p_3,v_1,v_2$ | 2 | no (level) |
| $p_2$ | 6 | $u_1,p_1,u_2$ | 2 | $v_1$ | 1 | yes |
| $v_1$ | 7 | $u_1,p_1,u_2,p_2$ | 3 | — | 0 | no (height) |
| $p_3$ | 2 | $u_2$ | 1 | $v_2$ | 1 | yes |
| $v_2$ | 5 | $u_1,p_1,u_2,p_3$ | 2 | — | 0 | no (height) |

Board (columns $x_1,x_2,x_3$ = positions 2, 4, 6; rows $y_1,y_2,y_3$ = values 2, 4, 6):

| Cell | in $U_p$? witness | in $S_{I_b}$? witness |
|:--|:--|:--|
| $(x_1,y_1)$ | **no**: $u_1$ is too high (3>2), $u_2$ is to the right; only $e$ and class (a), level $\le p-1$ | yes ($v_2$) |
| $(x_1,y_2)$ | yes ($u_1$) | yes ($v_2$) |
| $(x_1,y_3)$ | yes ($u_1$) | yes ($v_1$) |
| $(x_2,y_1)$ | yes ($u_2$) | yes ($v_2$) |
| $(x_2,y_2)$ | yes | yes ($v_1,v_2$) |
| $(x_2,y_3)$ | yes | yes ($v_1$) |
| $(x_3,y_1)$ | yes ($u_2$) | yes ($v_2$) |
| $(x_3,y_2)$ | yes | yes ($v_2$) |
| $(x_3,y_3)$ | yes | **no**: $v_2$ is too low (5<6), $v_1$ is to the left; only $x$ and class (b), height $\le b-1$ |

The inside points sit at $(x_1,y_2),(x_2,y_3),(x_3,y_1)$, the filling 231, as it must be. Negative controls:
dropping exactly one of (O2), (O3), (O4) makes the lens fail in 1,255 / 988 / 217 sampled instances, so each
hypothesis is used.

### 4.4 Lemma 15

* Same $b$, same inside set, same labels ($p_1<p_2$ is the only comparable pair among the three): correct.
* $Q=Q'$: the two descriptions $Q\cap\mathrm{SW}(p_2)=\{q<p_2:\ell(q)\ge p\}$ and
  $Q\cap\mathrm{NE}(p_1)=\{q>p_1:h(q)\ge b\}$ are right (points of $P\setminus Q$ below $p_2$ are $e$ or class (a);
  above $p_1$ they are $x$ or class (b)), and $\{u_1,u_2,p_1\}\cup\{p_2,v_1,v_2\}\cup\{p_3\}=Q$. So $Q=Q'$ does follow.
* $e=e'$: incomparability from equal levels $\ge T_0+1$; $e'<u_1<x$ gives class (a); the emptiness argument is
  correct ($z<x'$ would put $z$ in $Q'=Q$; $z=x'$ would give $h(x')>h(x)$; otherwise (O3) for $(e',x')$
  contradicts $z<x$). What is violated is exactly (O5) for $(e,x)$.
* $x=x'$: correct once $e=e'$ is invoked (G5); what is violated is exactly (O6) for $(e,x)$.
* Stress test: 7 planted points plus 2–9 points scattered around the rectangle; in 26,395 of 54,649 cases at
  least two pairs pass (O1)–(O4) for the same $p$, and never more than one passes (O1)–(O6).

### 4.5 Lemma 16, Proposition 18

All claims re-derived (see G6 for the silent steps). (O5), (O6) hold for the leftmost points even without
their emptiness clauses. In Proposition 18 the chain is:
$\sum_b[\cdot]\ \ge\ \tfrac13\Pr(\exists b\text{ lens})\ \ge\ \tfrac13\Pr(\mathcal G_p\ne\emptyset)\ =\ \tfrac13\mathbb E|\mathcal G_p|
\ =\ \tfrac13\mathbb E\sum(\cdots)\tfrac{|R|^7}{(7!)^2}\ \ge\ \tfrac1{3(7!)^2}\mathbb E[|R(z_{p-1},z_p)|^7;N\ge p]$,
using Lemma 11, Lemma 15, Lemma 15 again ($|\mathcal G_p|\le1$), Lemma 17, Lemma 16 with $i=p-1$
($T_0+1\le p-1<N$ on $\{N\ge p\}$). Correct.

### 4.6 Lemmas 19–21

All correct. Covering in Lemma 20: for $W/M\ge2^{-R_0}$, $r=\lceil\log_2(W/M)\rceil$ gives $W\le M2^r$,
$H\le M^2/W<2M2^{-r}$, $-R_0\le r\le\lceil\log_2T\rceil-1$ (as $M\ge2$); otherwise $r=-R_0$ and
$H\le T\le2^{R_0}\le2M2^{R_0}$. (200,000 random $(T,k,W,H)$: no failure.) Tilt: a free step contributes
$ab/k^2=8$; a thin step $8\Pr(E_1E_2<A_1/8)\le8\sqrt{A_1/2}$; with $2^k$ choices of the thin set and
$\lceil k/2\rceil\ge k/2$ the total is $\le T^2(16e^2(A_1/2)^{1/4})^k$.

### 4.7 Proof of Theorem 3

* Inequality (2): Lemma 10 holds for each realisation of $S$; $\mathrm{Cost}_S(i_j)$ is a deterministic
  function of $(i_1,\dots,i_j)$; taking expectation over $\xi$ is legitimate.
* $\alpha_i=\Pi[1..2i-2]$ for all $K$ candidates: yes, blocks $i_{j-1}+1,\dots,i-1$ are 12 in both.
* Indices: $p=2i-2=T_0+2K+2\xi-2\ge T_0+2K$; $2i-3=\iota_0+2\xi-1$; the usable steps are
  $(z_{\iota_0+2\xi-1},z_{\iota_0+2\xi})$, $\xi=1,\dots,K$, i.e. steps number $2,4,\dots,2K$ of the $2K$ steps of
  the window. On $\mathcal A$, $N\ge\iota_0+2K\ge2i-2$ for every candidate, and $\iota_0\ge T_0+1$ as $K\ge2$.
* Chains in the span have $\le2K-1$ points (levels $\iota_0<\ell(q_1)<\dots<\ell(q_m)<\iota_0+2K$), so by (b) the
  span has area $<4(2K)^2$, so by (c) fewer than $K$ steps are thin, so the $K$ designated steps are not all
  thin. Correct.
* $\Pr(\mathcal A)$: (a) $\iota_0+2K\le4Kj-2<4KJ\le0.06T$ and $\Pr(N\ge t)\ge\Pr(2L_{21}\ge t)$; (b)
  $T^{4-6.21}$; (c) $T^{2-98.9}$ times a logarithm. Correct.
* Constant: $0.015/45.1^2=7.37\cdot10^{-6}$, $A_1^7/(6(7!)^2)=6.56\cdot10^{-79}$, product with $7\cdot10^{-6}$ is
  $4.59\cdot10^{-84}$.

### 4.8 Theorem 1 and Corollary 2

$2c_{21}T-400\sqrt{T\ln T}\le2\ell(T)$ (Lemma 23), $2\ell(T)\le\lambda(T)-10^{-84}T/(\ln T)^2$ (Theorem 3),
$\lambda(T)\le2T$ (F3). No step uses $c_{21}<1$ or anything downstream. The inequality
$\tfrac12 10^{-84}(\ln T)^{-2}>200\sqrt{\ln T/T}$ first holds near $\ln T\approx430$; the theorem is purely
existential, as the note says. Corollary 2: correct with G12.

## 5. Readability

### 5.1 Overloaded symbols (most damaging first)

| # | Symbol | Meanings (location) | Proposed change |
|:--|:--|:--|:--|
| R1 | $T_0$ | threshold in Theorem 3 (L19); $2\max S$ (L96); both in the proof of Theorem 3 (L190–194) | threshold $T_*$; write $\tau=2\max S$ |
| R2 | $S$ | down-set $S_\beta(P)$ (L37, Lemma 4: "$q\in S$"); set of integers (L68 on); a real number in (F3) "$[0,S]^2$" (L208) | down-set $D_\beta$; keep $S$ for integer sets; "$[0,s]^2$" in (F3) |
| R3 | $x$ | abscissa and cell coordinate (L38, L87, L135, L223); the upper point of the pair $e<x$ (L107 on). In Lemma 14 both occur in one sentence: "the points above-right of $(x_3,y_3)$ are $x$ and points of class (b)" | call the pair $e<g$ |
| R4 | $p$ | a point (L42, L48, L56); the level $p$ (L125 on) next to the points $p_1,p_2,p_3$: "$\ell(p_1)=\ell(p_3)=p+1$" | rename the planted points $m_1,m_2,m_3$ ("middle") |
| R5 | $a$, $b$ | points of a decreasing pair (L38, L42, L56); $a$ = number of fillings without $D$-inversion (L60); $b$ = length of $I_b$ (L77 on); sides of a rectangle (L178); Talagrand's $b$ (L214); a real level $a$ (L227) | decreasing pair $(c,d)$; count $F_0$; rectangle sides $\rho,\rho'$; Talagrand level $s$; truncation level $\theta$ |
| R6 | (a), (b), (c) | parts of Lemma 12; classes of points; parts of the event $\mathcal A$. "(a) with $t=m-1$" (L105) and "(a) fails" (L194) sit next to "class (a)" | classes SW / NE / side (or I, II, III); events ($\mathcal A$1)–($\mathcal A$3) |
| R7 | $\ell$ | level $\ell(q)$ (L97); $\ell(T)=\mathbb EL_{21}$ (L202) | $m_{21}(T)$ and $m_{12}(T)$ for the two means |
| R8 | $h$, "height" | chain height $h(q)$ (L98); step increments $h_i$ (L170); "heights 3, 4, 1, 6, 7, 2, 5" = pattern values (L122), two lines before the paragraph "*Heights.*" | "values 3, 4, …"; increments $(w_i,w_i')$ |
| R9 | $e$ | the point $e$ and Euler's number in one display: "$\int\!\!\int\mathbb Ef(e,x,P_T)\,de\,dx$ … $e^{-A}A^7/(7!)^2$" (L159–161) | write $\exp(-A)$ |
| R10 | $k$ | pattern length (L13, Cor. 2); chain length (L172–180); in the proof of Lemma 23 both the grid index (L227) and the doubling exponent (L228) | grid index $\nu$; exponent $J$ |
| R11 | $N$ | $N_S(P)$ (L96); number of Poisson points (L216); $\mathbb N$ | number of points $|P_T|$ or $\mathsf n$ |
| R12 | $A$ | a copy of $\alpha$ (L44, L48, L105); area (L161); $A_1$ (L170); event $\mathcal A$ (L192) | area $|R|$ throughout; thinness threshold $\theta_1$ |
| R13 | $M$, $R$, $W$, $X$, $Y$, $I$, $U$, $f$, $G$ | $M=2k$ / $M=\sup$; $R(e,x)$ / $R_0$ / $R_x$; $W_S$ / $W=\sum w_i$; $X,Y$ coordinate sets / $X_k$, $Y$, $Y_n$, $Y'$; $I$ inside set / $I_b$; $U_\alpha$ / $U_t$; $f$ filling / Mecke integrand / certificate function; $G_i$ / $\mathcal G_p$ | at least: $U^{(t)}$ or $U_{\Pi[1..t]}$; $\mathrm{Id}_b$ for the increasing pattern; $G_i\to Z_i$ |
| R14 | $i$ vs $\iota$ | $i_0=0$ (L188) and $\iota_0=T_0+2K-2$ (L192) are different things one line apart | $\iota_0\to w_0$ ("window start") |

### 5.2 Notation used before or without definition

| # | Location | Problem | Fix |
|:--|:--|:--|:--|
| R15 | L59 and on | "$\sigma_n\supseteq\pi$" is never defined | "we write $P\supseteq\pi$ for '$P$ contains $\pi$'" in the Setting |
| R16 | L127–151 | "above", "below" mean the product order ($q>e$), never defined; a reader will read "below" as "smaller ordinate" (e.g. "being below $x$", L151; "a chain of $h(q)-1$ points above $q$", L105) | define once: "$q$ is *above* $r$, and $r$ *below* $q$, if $r<q$"; or write $r<q$ |
| R17 | L164, L191 | $\mathbb E[X;\,A]$ | define as $\mathbb E[X\mathbf 1_A]$ |
| R18 | L38 | "$D$-inversion": the letter is unexplained | "an inversion both of whose corners lie in the regions (a *$D$-inversion*, $D$ for 'detected')", or simply *board inversion* |
| R19 | L44 | "$\alpha\oplus B\oplus\beta$ … a copy $B'$ of $\beta$": $B$ is the middle block, $B'$ unrelated | name the copies $A_\alpha$, $A_\beta$ |
| R20 | L149, L163, L190 | "leftmost optimal copy" $(z_i)$ is only defined for $T_0+1\le i\le N$ and only when $N\ge T_0+2$; it is a chain, not a copy of $\Pi[1..N]$ | "the *leftmost optimal tail* $(z_i)_{T_0<i\le N}$, defined on $\{N\ge T_0+2\}$" |
| R21 | L182 | Lemma 21 has no title; Section 5 is called "three first-moment estimates" but Lemma 21 is a Hoeffding bound | "Lemma 21 (many disjoint inversions)"; "Three counting estimates" |
| R22 | L202 | $P$ is now a Poisson process on the quadrant, after being a deterministic configuration for four sections | $\mathcal P$ or $P_\infty$ |
| R23 | L116 | "(O5) and (O6) … used only in Lemma 15" — they are also verified in Lemma 16 | "used only in Lemma 15 (and verified in Lemma 16)" |

### 5.3 References to statements

No statement number is wrong. Imprecise references: (F4) "Corollary 9 with $S=\emptyset$" (G7); Lemma 15
"the last part of the proof of Lemma 11" (G3); Theorem 1 "as in the proof of Lemma 22" and Corollary 2 "by
the first step of the proof of Lemma 22" and "by the previous proof". Proposed: split Lemma 22 into
**22a** (fixed $n$: $\Pr(Y_n\ge\mu_n+12n^{1/4}+u)\le2\exp(-u^2/(80\sqrt n))$ for $0\le u\le5\sqrt n$, $n\ge n_0$),
**22b** ($|\ell(T)-\mu_{\lfloor T^2\rfloor}|\le5\ln T+1$ for large $T$) and **22c** (the present statement), and
cite 22a, 22b by number. The "logical order" line of the last section omits Corollary 9 and Lemmas 12–13.

### 5.4 Places where the reader has to reconstruct an argument (with proposed text)

* **Lemma 13, L120.** "which forces $r\in R$ or $q<e$" → "if $r<x$ then $e<q<r<x$, so $r\in R$; if $r=e$ then
  $q<e$, contradicting $q\in R$."
* **Lemma 14, L129–135.** Add the table of Section 4.3 and a figure: the seven points with $(\ell-p,h-b)$
  labels, $e$ and $x$ at the corners, and the $3\times3$ board with the two missing cells. This single figure
  would remove most of the effort of checking the note.
* **Outside conditions, L107–116.** Add a figure of the three classes and of the strips
  $R(e',x)\setminus R$, $R(e,x')\setminus R$; say in words what (O2)–(O4) achieve ("no outside point can
  become inside for $(\Pi[1..p],I_b)$, and the levels/heights seen from inside $R$ are those of $e$ and $x$").
* **Theorem 3, L190–192.** Replace "the $K$ odd offsets of the window" by: "the step $(z_{2i-3},z_{2i-2})$ is
  the step number $2\xi$ of the chain $z_{\iota_0}<\dots<z_{\iota_0+2K}$; as $\xi$ runs over $1,\dots,K$ these are
  the $K$ even-numbered of its $2K$ steps." Add "on $\mathcal A$, $N\ge\iota_0+2K\ge2i-2$ for every candidate
  $i$" before the display, and "fewer than $K$ thin steps among $2K$, so the $K$ designated steps are not all
  thin".
* **Theorem 3, L188–189.** After (2): "Here $\mathrm{Cost}_S(i)$ is, for each fixed $S$, a number (a sum of
  probabilities for $P_T$); the outer expectation is over $\xi_1,\dots,\xi_J$ only."
* **Lemma 20, L180.** State the union bound ("at least $k/2$ thin steps implies that some set of exactly
  $\lceil k/2\rceil$ steps is thin") and the step $(A_1/2)^{\lceil k/2\rceil/2}\le(A_1/2)^{k/4}$.
* **Lemma 10, L83.** "$W_S[1..t]=W_{S_r}[1..t]$" deserves "by the remark before Corollary 9 when $t$ is odd".
* **Stage costs, L70.** "$2L_{21}\le N_{\mathbb N}$" is used again in the proof of Theorem 3 as
  $\{2L_{21}\ge t\}\subset\{N_{\mathbb N}\ge t\}$; say it there.
* **Introduction.** State early, in one sentence, why a deficit of order $T/(\ln T)^2$ suffices: it beats the
  $O(\sqrt{T\ln T})$ error in $\ell(T)\approx c_{21}T$. The outline has this only implicitly.

## 6. Results of the programs written for this review

All in `/private/tmp/claude-501/-Users-adamhadani-Development-math-proofs-superpatterns/0c33b450-b609-4fd6-9183-ef318e6a7155/scratchpad/ref3/`
(a session scratch directory; the sources are reproduced verbatim in the Appendix so that the runs can be
repeated: save the six files in one directory, Python 3, no dependencies).

| Command | What it checks | Result |
|:--|:--|:--|
| `python3 exhaustive.py 7` (165 s) | Lemma 5 on all cells, Lemma 6 class sizes, Lemma 7, identity (1) and the per-class counts $F-1$, $F-a$, for all $\sigma\in S_n$, $n\le7$, 13 pairs $(\alpha,\beta)$; lens weight; uniqueness of $b$ for 6 patterns $\alpha$ | all pass. The only non-zero difference in the list is $(\alpha,\beta)=(1,1)$, $n=7$: $\#\{1234\}-\#\{1324\}=1=3$ lens permutations $\times\frac13$, matching $|Av_7(1324)|-|Av_7(1234)|=2762-2761$ |
| `python3 gadget.py --validate` | staircase recursion for levels and $N_S$ against brute-force containment, 400 configurations, $n\le9$ | agree |
| `python3 gadget.py 12000 101` | Lemma 12 (12,000 configurations, $12\le n\le34$, $S\subset\{1,2,3\}$); Lemma 16 (30,888 consecutive pairs); Lemmas 13, 14, uniqueness of $b$, Lemma 15 on 8,040 plantings (2,728 in steps of the leftmost optimal tail, 5,312 in other empty rectangles satisfying (O1)–(O6) or only (O1)–(O4)); negative controls | all pass; $|\mathcal G_p|=1$ in 7,096 and $0$ in 944 cases; lens fails without (O2)/(O3)/(O4) in 1,255/988/217 controls |
| `python3 stress15.py 100000 2` | Lemma 14 and Lemma 15 on adversarial small configurations | 98,845 lenses confirmed; 54,649 cases, 26,395 with $\ge2$ pairs passing (O1)–(O4); never more than one passes (O1)–(O6) |
| `python3 mecke_mc.py 200000 4 11` (100 s) | one-point-plant analogue of Lemma 17, $T=4$ | $(S,p)=(\emptyset,3)$: $0.4026$ vs $0.4039$, diff $-0.0013\pm0.0017$; $(\{1\},4)$: $0.3568$ vs $0.3566$, $+0.0002\pm0.0016$; $(\{1,2\},6)$: $0.1393$ vs $0.1399$, $-0.0007\pm0.0010$ |
| `python3 simplified_tiebreak.py 3000 3` | Section 3.3 (tie-break without emptiness clauses) | Lemma 16 on 6,714 pairs; $\mathcal G_p=\{(z_{p-1},z_p)\}$ in 1,787 plantings |
| `python3 constants.py` | every constant of Sections 5–7 | $1-e^{-1}=0.63212$; $0.069696$; $0.314377$; $4e^{-4}=0.073263$; $0.069\cdot90=6.21$; $90\ln3=98.875$; $7.3746\cdot10^{-6}$; $6.5613\cdot10^{-79}$; $4.593\cdot10^{-84}$; $\sqrt{40\pi}=11.21$; series $3.77963$, $\times45=170.08$ |

Remark on the note's own table: it says the tie-break "is needed in about a third" of cases. In my two
samplers the proportion of cases with competing pairs was 7.6% (plantings in random configurations) and 48%
(adversarial), so the figure depends on the sampling distribution; this is not a discrepancy, but the note
should say how its cases were generated.

## 7. Fitness for a specialist, and the three most valuable improvements

Fit to send, in my judgement, once the notation is cleaned: the argument is short, self-contained apart from
five standard tools, and I could not find a wrong step. A specialist's time is best spent on (i) Lemma 15 and
Lemma 17 (the only places where a new idea carries weight), and (ii) confirming novelty and the attribution of
Theorem 8.

1. **De-overload the notation and number the hidden facts.** Fix R1–R9 at least ($T_0$, $S$, $x$, $p$, $a/b$,
   class labels, $\ell$, "height", $e$); promote to numbered statements the uniqueness of $b$ (G3), the
   fixed-$n$ concentration bound and the comparison $|\ell(T)-\mu_{\lfloor T^2\rfloor}|\le5\ln T+1$ (Section 5.3);
   state Theorem 8 and Corollary 9 explicitly for both $\sigma_n$ and $P_T$ (G2, G7).
2. **Two figures and one table for the gadget.** The seven points with level/height offsets and the
   $3\times3$ board (Section 4.3); the classes (a), (b), (c) with the tie-break regions; an index table for the
   proof of Theorem 3 ($\xi\mapsto i\mapsto p=2i-2\mapsto$ step number $2\xi$).
3. **Close the small gaps and tighten the claims.** G5 (Lemma 15 uses $e=e'$), G9 (integer levels in
   Talagrand), G6, G8, G10–G12; say "Poissonised" in the abstract or add the de-Poissonisation of Theorem 3
   (G13); mark Remark (i) and the simulation figures as not proved here; consider the simplified tie-break of
   Section 3.3, which removes a paragraph from the proof the note itself flags as the most error-prone.

## Appendix. Sources of the programs

`stress15.py`, `mecke_mc.py` and `simplified_tiebreak.py` import `gadget.py`; keep all files in one directory.

### `exhaustive.py`

```python
#!/usr/bin/env python3
"""Exhaustive small-n checks of Section 2 of layered-refutation.md, straight from the definitions.
Checks, for all sigma in S_n (n <= NMAX) and a list of (alpha, beta):
  Lemma 5  : U_alpha(P) = U_alpha(O), S_beta(P) = S_beta(O) on all grid cells
  Lemma 6  : each class (O,X,Y) has exactly F members (F = number of valid fillings)
  Lemma 7  : decreasing bijection valid; a >= 1
  Theorem 8: Pr(12) - Pr(21) = E[(a-1)/F]  (exact rationals), and per-class counts F-1, F-a
  Lemma 11 : lens boards have F=3, a=2; for alpha fixed and beta=I_b a permutation has a lens for <= 1 value of b
usage: python3 exhaustive.py [NMAX]
"""
import sys
from itertools import permutations, combinations
from fractions import Fraction
from functools import lru_cache
from collections import defaultdict

NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 7

def std(seq):
    s = sorted(seq)
    return tuple(s.index(v) + 1 for v in seq)

@lru_cache(maxsize=None)
def contains_seq(seq, pat):
    k = len(pat)
    if k == 0:
        return True
    if len(seq) < k:
        return False
    for c in combinations(seq, k):
        if std(c) == pat:
            return True
    return False

def contains(points, pat):
    """points: iterable of (x,y) with distinct coords"""
    pts = sorted(points)
    return contains_seq(std(tuple(p[1] for p in pts)), pat)

def dsum(*pats):
    out = []
    for p in pats:
        m = len(out)
        out += [v + m for v in p]
    return tuple(out)

def inU(z, pts, alpha):
    return contains([p for p in pts if p[0] < z[0] and p[1] < z[1]], alpha)

def inS(z, pts, beta):
    return contains([p for p in pts if p[0] > z[0] and p[1] > z[1]], beta)

def analyse(P, alpha, beta):
    """returns (key, F, a, lens?, flags)"""
    I = [p for p in P if inU(p, P, alpha) and inS(p, P, beta)]
    O = [p for p in P if p not in I]
    X = sorted(p[0] for p in I)
    Y = sorted(p[1] for p in I)
    key = (tuple(sorted(O)), tuple(X), tuple(Y))
    # Lemma 5 on all cells of the full grid (shifted by 1/2 as well, to test non-point locations)
    n = len(P)
    for x2 in range(1, 2 * n + 2):
        for y2 in range(1, 2 * n + 2):
            z = (x2 / 2, y2 / 2)
            assert inU(z, P, alpha) == inU(z, O, alpha), ("Lemma5 U", P, alpha, z)
            assert inS(z, P, beta) == inS(z, O, beta), ("Lemma5 S", P, beta, z)
    UO = {(x, y): inU((x, y), O, alpha) for x in X for y in Y}
    SO = {(x, y): inS((x, y), O, beta) for x in X for y in Y}
    board = {c for c in UO if UO[c] and SO[c]}
    F = 0
    a = 0
    dec_valid = False
    fillings = []
    for perm in permutations(Y):
        g = list(zip(X, perm))
        if all(c in board for c in g):
            F += 1
            fillings.append(g)
            if list(perm) == sorted(Y, reverse=True):
                dec_valid = True
            dinv = False
            for i in range(len(g)):
                for j in range(i + 1, len(g)):
                    A, B = g[i], g[j]
                    if A[1] > B[1]:  # A north-west of B
                        if UO[(A[0], B[1])] and SO[(B[0], A[1])]:
                            dinv = True
            if not dinv:
                a += 1
    lens = False
    if len(I) == 3:
        full = {(x, y) for x in X for y in Y}
        if board == full - {(X[0], Y[0]), (X[2], Y[2])} and not UO[(X[0], Y[0])] and not SO[(X[2], Y[2])]:
            lens = True
    return key, F, a, lens, dec_valid, len(I)

def run(n, alpha, beta):
    P12 = dsum(alpha, (1, 2), beta)
    P21 = dsum(alpha, (2, 1), beta)
    classes = defaultdict(lambda: [0, 0, 0, None])
    lhs = 0
    rhs = Fraction(0)
    nl = 0
    for sig in permutations(range(1, n + 1)):
        P = [(i + 1, sig[i]) for i in range(n)]
        key, F, a, lens, dec_valid, nI = analyse(P, alpha, beta)
        c12 = contains_seq(sig, P12)
        c21 = contains_seq(sig, P21)
        lhs += int(c12) - int(c21)
        if nI > 0:
            assert F >= 1 and a >= 1 and dec_valid, ("Lemma 7", sig, alpha, beta)
            rhs += Fraction(a - 1, F)
            cl = classes[key]
            cl[0] += 1; cl[1] += int(c12); cl[2] += int(c21)
            if cl[3] is None:
                cl[3] = (F, a)
            assert cl[3] == (F, a)
        else:
            assert not c12 and not c21
        if lens:
            nl += 1
            assert (F, a) == (3, 2), ("lens weight", sig, alpha, beta, F, a)
    for key, (cnt, k12, k21, Fa) in classes.items():
        F, a = Fa
        assert cnt == F, ("Lemma 6 class size", key, cnt, F)
        assert k12 == F - 1 and k21 == F - a, ("Theorem 8 class counts", key)
    assert lhs == rhs, ("Theorem 8", n, alpha, beta, lhs, rhs)
    return lhs, nl

def lens_unique(n, alpha):
    worst = 0
    tot = 0
    for sig in permutations(range(1, n + 1)):
        P = [(i + 1, sig[i]) for i in range(n)]
        cnt = 0
        for b in range(0, n):
            beta = tuple(range(1, b + 1))
            # cheap precheck: exactly three inside points
            I = [p for p in P if inU(p, P, alpha) and inS(p, P, beta)]
            if len(I) != 3:
                continue
            if analyse(P, alpha, beta)[3]:
                cnt += 1
        worst = max(worst, cnt)
        tot += cnt
    return worst, tot

if __name__ == "__main__":
    pairs = [((), ()), ((1,), ()), ((), (1,)), ((1,), (1,)), ((1, 2), (1,)), ((2, 1), (1,)), ((1,), (2, 1)),
             ((1,), (1, 2)), ((2, 1), (1, 2)), ((2, 1), (2, 1)), ((1, 2), (1, 2)), ((2, 1, 3), (1,)), ((1,), (1, 3, 2))]
    for alpha, beta in pairs:
        for n in range(len(alpha) + len(beta) + 2, NMAX + 1):
            d, nl = run(n, alpha, beta)
            print(f"Thm8/L5/L6/L7 ok  n={n} alpha={alpha} beta={beta}  #(12)-#(21)={d}  lens perms={nl}")
    for alpha in [(1,), (1, 2), (2, 1), (2, 1, 3), (1, 2, 3), (2, 1, 4, 3)]:
        for n in range(len(alpha) + 4, NMAX + 1):
            w, tot = lens_unique(n, alpha)
            assert w <= 1
            print(f"Lemma 11 uniqueness ok  n={n} alpha={alpha}: max #b with a lens = {w}, perms with a lens = {tot}")
```

### `gadget.py`

```python
#!/usr/bin/env python3
"""Random tests of Section 3 of layered-refutation.md (Lemmas 12-16), written from the definitions.

Levels are computed by a staircase recursion for U_t (validated against brute-force pattern containment
with --validate).  The lens of Lemma 14 is then checked from the *fibre definitions* of Section 2
(inside set, outside set O, board computed in O), not from the level/height shortcut.

usage: python3 gadget.py --validate          (DP for levels vs brute force, n <= 9)
       python3 gadget.py [trials] [seed]     (Lemmas 12, 13, 14, 15, 16 on random configurations)
"""
import sys, random
from itertools import combinations, permutations

NEG = float("-inf")
PLANT = (3, 4, 1, 6, 7, 2, 5)

# ---------------------------------------------------------------- patterns W_S
def W_prefix(S, t):
    out = []
    i = 1
    while len(out) < t:
        base = 2 * (i - 1)
        out += [base + 2, base + 1] if i in S else [base + 1, base + 2]
        i += 1
    out = out[:t]
    s = sorted(out)
    return tuple(s.index(v) + 1 for v in out)

def std(seq):
    s = sorted(seq)
    return tuple(s.index(v) + 1 for v in seq)

def contains_bf(points, pat):
    pts = sorted(points)
    ys = [p[1] for p in pts]
    k = len(pat)
    if k == 0:
        return True
    return any(std(c) == pat for c in combinations(ys, k))

# ---------------------------------------------------------------- staircase recursion for U_t
def staircase(gens):
    """minimal elements of a set of generators (z in U iff some generator g < z strictly)"""
    gens = sorted(set(gens))
    out = []
    best = float("inf")
    for g in gens:
        if g[1] < best:
            out.append(g)
            best = g[1]
    return out

def member(z, st):
    return any(g[0] < z[0] and g[1] < z[1] for g in st)

def U_stairs(P, S, tmax):
    """list st[t], t=0..tmax, generators of U_t = {z : SW(z) contains W_S[1..t]}"""
    st = [[(NEG, NEG)]]
    for t in range(1, tmax + 1):
        if t % 2 == 1:
            gens = [q for q in P if member(q, st[t - 1])]
        else:
            blk = t // 2
            if blk in S:
                prev = st[t - 2]
                gens = []
                for a in P:
                    for b in P:
                        if a[0] < b[0] and a[1] > b[1] and member((a[0], b[1]), prev):
                            gens.append((b[0], a[1]))
            else:
                gens = [q for q in P if member(q, st[t - 1])]
        st.append(staircase(gens))
        if not st[-1]:
            for _ in range(t + 1, tmax + 1):
                st.append([])
            break
    return st

def levels(P, S):
    st = U_stairs(P, S, len(P) + 1)
    lev = {}
    for q in P:
        t = 0
        while t + 1 < len(st) and member(q, st[t + 1]):
            t += 1
        lev[q] = t + 1
    N = max(t for t in range(len(st)) if st[t])
    return lev, N, st

def heights(P):
    h = {}
    for q in sorted(P, reverse=True):
        h[q] = 1 + max([h[r] for r in h if r[0] > q[0] and r[1] > q[1]], default=0)
    return h

def lt(a, b):
    return a[0] < b[0] and a[1] < b[1]

# ---------------------------------------------------------------- outside conditions, literally
def classes(P, e, x):
    A, B, C = [], [], []
    for r in P:
        if r == e or r == x or (lt(e, r) and lt(r, x)):
            continue
        if lt(r, x):
            A.append(r)
        elif lt(e, r):
            B.append(r)
        else:
            C.append(r)
            assert (r[0] < e[0] and r[1] > x[1]) or (r[0] > x[0] and r[1] < e[1])
    return A, B, C

def inR(z, e, x):
    return lt(e, z) and lt(z, x)

def conds(P, lev, h, e, x, T0):
    A, B, C = classes(P, e, x)
    o1 = lev[e] >= T0 + 1
    o2 = all(lev[r] <= lev[e] for r in A)
    o3 = all(h[r] <= h[x] for r in B)
    o4 = not any(lev[r] >= lev[e] + 2 and h[r] >= h[x] + 2 for r in C)
    o5 = not any(lev[r] == lev[e] and r[0] < e[0] and r[1] > e[1]
                 and not any(inR(z, r, x) and not inR(z, e, x) for z in P) for r in A)
    o6 = not any(h[r] == h[x] and r[0] < x[0] and r[1] > x[1]
                 and not any(inR(z, e, r) and not inR(z, e, x) for z in P) for r in B)
    return (o1, o2, o3, o4, o5, o6)

# ---------------------------------------------------------------- lens from the fibre definitions
def lens_at(P, S, p, b):
    """Is there a lens at (W_S[1..p], I_b)?  Everything from Section 2 definitions; board computed in O."""
    lev, N, st = levels(P, S)
    h = heights(P)
    if p >= len(st):
        return False, None
    I = [q for q in P if member(q, st[p]) and h[q] >= b + 1]
    if len(I) != 3:
        return False, None
    O = [q for q in P if q not in I]
    stO = U_stairs(O, S, p)
    hO = heights(O)
    X = sorted(q[0] for q in I)
    Y = sorted(q[1] for q in I)
    def inUO(z):
        return member(z, stO[p]) if p < len(stO) else False
    def inSO(z):
        return b == 0 or any(lt(z, o) and hO[o] >= b for o in O)
    board = {(xx, yy) for xx in X for yy in Y if inUO((xx, yy)) and inSO((xx, yy))}
    full = {(xx, yy) for xx in X for yy in Y}
    ok = (board == full - {(X[0], Y[0]), (X[2], Y[2])}) and not inUO((X[0], Y[0])) and not inSO((X[2], Y[2]))
    if ok:
        # weight (a-1)/F from the definitions
        F = a = 0
        for perm in permutations(Y):
            g = list(zip(X, perm))
            if all(c in board for c in g):
                F += 1
                d = any(g[i][1] > g[j][1] and inUO((g[i][0], g[j][1])) and inSO((g[j][0], g[i][1]))
                        for i in range(3) for j in range(i + 1, 3))
                a += (not d)
        assert (F, a) == (3, 2)
    return ok, sorted(I)

# ---------------------------------------------------------------- generators
def rand_config(n, rng):
    xs = rng.sample(range(1, 10**6), n)
    ys = rng.sample(range(1, 10**6), n)
    return [(float(a), float(b)) for a, b in zip(xs, ys)]

def plant(P, e, x, rng, pat=PLANT):
    k = len(pat)
    xs = sorted(rng.uniform(e[0], x[0]) for _ in range(k))
    ys = sorted(rng.uniform(e[1], x[1]) for _ in range(k))
    return [(xs[i], ys[pat[i] - 1]) for i in range(k)]

def is_plant(P, e, x):
    Q = sorted(z for z in P if inR(z, e, x))
    return len(Q) == 7 and std([q[1] for q in Q]) == PLANT

def validate(rng, trials=400):
    for _ in range(trials):
        n = rng.randint(1, 9)
        P = rand_config(n, rng)
        S = set(rng.sample(range(1, 5), rng.randint(0, 3)))
        lev, N, st = levels(P, S)
        for t in range(0, n + 1):
            pat = W_prefix(S, t)
            assert contains_bf(P, pat) == (t <= N), (P, S, t, N)
            for q in P:
                sw = [r for r in P if lt(r, q)]
                assert contains_bf(sw, pat) == (lev[q] >= t + 1), (P, S, t, q)
    print("validate: staircase recursion for levels and N agrees with brute-force containment,", trials, "cases")

def main(trials, seed):
    rng = random.Random(seed)
    stats = dict(l12=0, l16_pairs=0, plants_opt=0, plants_gen=0, l13=0, l14=0, l15=0, tiebreak_needed=0,
                 neg_o2=0, neg_o3=0, neg_o4=0, lens_unique=0, G_sizes={})
    for it in range(trials):
        n = rng.randint(12, 34)
        P = rand_config(n, rng)
        mS = rng.randint(0, 3)
        S = set(rng.sample(range(1, 4), min(mS, 3)))
        T0 = 2 * max(S) if S else 0
        lev, N, st = levels(P, S)
        h = heights(P)
        # ---- Lemma 12
        for t in range(T0, n + 1):
            for q in P:
                lhs = member(q, st[t + 1]) if t + 1 < len(st) else False
                rhs = any(lt(r, q) and lev[r] >= t + 1 for r in P)
                assert lhs == rhs, "Lemma 12(a)"
        for q in P:
            if lev[q] >= T0 + 1:
                assert lev[q] == 1 + max([T0] + [lev[r] for r in P if lt(r, q)]), "Lemma 12(b)"
                assert lev[q] + h[q] - 1 <= N, "Lemma 12(c)"
            for r in P:
                if lt(r, q) and lev[r] >= T0 + 1:
                    assert lev[q] >= lev[r] + 1
        stats["l12"] += 1
        if N < T0 + 2:
            continue
        # ---- Lemma 16
        z = {}
        for i in range(T0 + 1, N + 1):
            G = [q for q in P if lev[q] == i and h[q] == N - i + 1]
            assert G, "Lemma 16: G_i empty"
            z[i] = min(G)
        for i in range(T0 + 1, N):
            e, x = z[i], z[i + 1]
            assert lt(e, x), "Lemma 16: z_i < z_{i+1}"
            assert not any(inR(q, e, x) for q in P), "Lemma 16: empty rectangle"
            assert all(conds(P, lev, h, e, x, T0)), "Lemma 16: E(z_i,z_{i+1})"
            stats["l16_pairs"] += 1
        # ---- choose a pair with empty rectangle to plant in
        mode = rng.choice(["opt", "gen", "gen4"])
        if mode == "opt":
            i = rng.randint(T0 + 1, N - 1)
            cand = [(z[i], z[i + 1])]
        else:
            cand = []
            for e in P:
                for x in P:
                    if lt(e, x) and not any(inR(q, e, x) for q in P):
                        c = conds(P, lev, h, e, x, T0)
                        if (mode == "gen" and all(c)) or (mode == "gen4" and all(c[:4])):
                            cand.append((e, x))
            if not cand:
                continue
        e, x = rng.choice(cand)
        c0 = conds(P, lev, h, e, x, T0)
        Qn = plant(P, e, x, rng)
        P2 = P + Qn
        lev2, N2, st2 = levels(P2, S)
        h2 = heights(P2)
        # ---- Lemma 13
        assert lev2[e] == lev[e] and h2[x] == h[x], "Lemma 13: l(e), h(x)"
        assert conds(P2, lev2, h2, e, x, T0) == c0, "Lemma 13: conditions"
        # also with an arbitrary filling of the rectangle
        k = rng.randint(1, 6)
        P3 = P + plant(P, e, x, rng, pat=tuple(rng.sample(range(1, k + 1), k)))
        lev3, N3, st3 = levels(P3, S); h3 = heights(P3)
        assert lev3[e] == lev[e] and h3[x] == h[x] and conds(P3, lev3, h3, e, x, T0) == c0, "Lemma 13 (random filling)"
        stats["l13"] += 1
        # ---- Lemma 14 (only (O1)-(O4) assumed)
        p = lev[e] + 1
        b = h[x] + 1
        ok, I = lens_at(P2, S, p, b)
        names = dict(zip("u1 p1 u2 p2 v1 p3 v2".split(), Qn))
        assert ok and I == sorted([names["p1"], names["p2"], names["p3"]]), "Lemma 14"
        assert (lev2[names["u1"]], lev2[names["u2"]], lev2[names["p1"]], lev2[names["p3"]], lev2[names["p2"]]) == (p, p, p + 1, p + 1, p + 2)
        assert (h2[names["v1"]], h2[names["v2"]], h2[names["p2"]], h2[names["p3"]], h2[names["p1"]]) == (b, b, b + 1, b + 1, b + 2)
        stats["l14"] += 1
        stats["plants_opt" if mode == "opt" else "plants_gen"] += 1
        # ---- Lemma 11: lens at (Pi[1..p], b') for at most one b'
        nb = sum(lens_at(P2, S, p, bb)[0] for bb in range(0, len(P2)))
        assert nb == 1, "Lemma 11 uniqueness of b"
        stats["lens_unique"] += 1
        # ---- Lemma 15: whole set G_p of the planted configuration
        G_full, G_four = [], []
        for e2 in P2:
            if lev2[e2] != p - 1:
                continue
            for x2 in P2:
                if lt(e2, x2) and is_plant(P2, e2, x2):
                    c = conds(P2, lev2, h2, e2, x2, T0)
                    if all(c[:4]):
                        G_four.append((e2, x2))
                    if all(c):
                        G_full.append((e2, x2))
        assert len(G_full) <= 1, ("Lemma 15", G_full)
        if all(c0):
            assert G_full == [(e, x)]
        stats["G_sizes"][len(G_full)] = stats["G_sizes"].get(len(G_full), 0) + 1
        if len(G_four) > 1:
            stats["tiebreak_needed"] += 1
        stats["l15"] += 1
        # ---- negative controls: drop one hypothesis of Lemma 14 and see whether the lens can fail
        for e2 in P:
            for x2 in P:
                if lt(e2, x2) and not any(inR(q, e2, x2) for q in P):
                    c = conds(P, lev, h, e2, x2, T0)
                    if c[0] and sum(c[1:4]) == 2:
                        P4 = P + plant(P, e2, x2, rng)
                        if not lens_at(P4, S, lev[e2] + 1, h[x2] + 1)[0]:
                            which = ["neg_o2", "neg_o3", "neg_o4"][[c[1], c[2], c[3]].index(False)]
                            stats[which] += 1
                        break
            else:
                continue
            break
    print(stats)

if __name__ == "__main__":
    if "--validate" in sys.argv:
        validate(random.Random(1))
    else:
        trials = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
        seed = int(sys.argv[2]) if len(sys.argv) > 2 else 12345
        main(trials, seed)
```

### `stress15.py`

```python
#!/usr/bin/env python3
"""Stress test of Lemma 15 (|G_p| <= 1) and Lemma 14 on small adversarial configurations:
seven planted points in the unit square plus a few extra points scattered around it, so that many
pairs (e,x) compete for the same planted set.  For every p and every pair e<x with l(e)=p-1 and
P cap R(e,x) ~ 3416725:  if (O1)-(O4) hold, check the lens (Lemma 14); count pairs passing (O1)-(O4)
and pairs passing (O1)-(O6); assert the latter count is <= 1 for each p.
usage: python3 stress15.py [trials] [seed]
"""
import sys, random
from gadget import levels, heights, conds, lens_at, is_plant, lt, PLANT

def main(trials, seed):
    rng = random.Random(seed)
    multi4 = 0; tested = 0; lens_checked = 0; hist = {}
    for it in range(trials):
        xs = sorted(rng.random() for _ in range(7)); ys = sorted(rng.random() for _ in range(7))
        Q = [(xs[i], ys[PLANT[i] - 1]) for i in range(7)]
        m = rng.randint(2, 9)
        extra = []
        for _ in range(m):
            r = rng.random()
            if r < 0.4:   # south-west region
                extra.append((rng.uniform(-1, 0), rng.uniform(-1, 0)))
            elif r < 0.8: # north-east region
                extra.append((rng.uniform(1, 2), rng.uniform(1, 2)))
            else:         # anywhere outside the open unit square
                while True:
                    z = (rng.uniform(-1, 2), rng.uniform(-1, 2))
                    if not (0 < z[0] < 1 and 0 < z[1] < 1):
                        break
                extra.append(z)
        P = Q + extra
        S = set(rng.sample([1, 2], rng.randint(0, 1))) if rng.random() < 0.3 else set()
        T0 = 2 * max(S) if S else 0
        lev, N, st = levels(P, S); h = heights(P)
        per_p = {}
        for e in P:
            for x in P:
                if lt(e, x) and is_plant(P, e, x):
                    c = conds(P, lev, h, e, x, T0)
                    p = lev[e] + 1
                    if all(c[:4]):
                        ok, I = lens_at(P, S, p, h[x] + 1)
                        assert ok, ("Lemma 14", P, S, e, x)
                        lens_checked += 1
                        per_p.setdefault(p, [0, 0])[0] += 1
                        if all(c):
                            per_p[p][1] += 1
        for p, (n4, n6) in per_p.items():
            tested += 1
            assert n6 <= 1, ("Lemma 15 fails", P, S, p)
            if n4 > 1:
                multi4 += 1
            hist[(min(n4, 5), n6)] = hist.get((min(n4, 5), n6), 0) + 1
    print(f"trials={trials} (config,p) cases with a pair passing O1-O4: {tested}; lenses checked: {lens_checked}; "
          f"cases with >1 pair passing O1-O4: {multi4}")
    print("histogram {(#pairs O1-O4 (capped 5), #pairs O1-O6): count} =", dict(sorted(hist.items())))

if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 20000, int(sys.argv[2]) if len(sys.argv) > 2 else 1)
```

### `mecke_mc.py`

```python
#!/usr/bin/env python3
"""Monte Carlo sanity check of the structure of Lemma 17 with a ONE-point plant (the seven-point plant has
probability ~ A^7/(7!)^2 and cannot be sampled):
   E #{(e,x): e<x, l(e)=p-1, E(e,x), |P_T cap R(e,x)| = 1}  =  E sum_{(e,x)} 1{e<x, l(e)=p-1, E(e,x), P_T cap R = empty} |R(e,x)|
Both sides are estimated on the same Poisson samples; the paired difference should be 0 within noise.
usage: python3 mecke_mc.py [samples] [T] [seed]
"""
import sys, random, math
from gadget import levels, heights, conds, lt, inR

def poisson(lam, rng):
    L = math.exp(-lam); k = 0; p = 1.0
    while True:
        p *= rng.random()
        if p <= L:
            return k
        k += 1

def main(samples, T, seed):
    rng = random.Random(seed)
    for S, p in [(set(), 3), ({1}, 4), ({1, 2}, 6)]:
        T0 = 2 * max(S) if S else 0
        assert p >= T0 + 2
        sl = sr = sd2 = 0.0
        for _ in range(samples):
            n = poisson(T * T, rng)
            P = [(rng.uniform(0, T), rng.uniform(0, T)) for _ in range(n)]
            if n < 2:
                continue
            lev, N, st = levels(P, S); h = heights(P)
            L = R = 0.0
            for e in P:
                if lev[e] != p - 1:
                    continue
                for x in P:
                    if not lt(e, x):
                        continue
                    k = sum(1 for z in P if inR(z, e, x))
                    if k > 1:
                        continue
                    if all(conds(P, lev, h, e, x, T0)):
                        if k == 1:
                            L += 1
                        else:
                            R += (x[0] - e[0]) * (x[1] - e[1])
            sl += L; sr += R; sd2 += (L - R) ** 2
        m = (sl - sr) / samples
        se = math.sqrt(max(sd2 / samples - m * m, 0) / samples)
        print(f"S={sorted(S)} p={p} T={T}: LHS={sl/samples:.4f} RHS={sr/samples:.4f} diff={m:+.4f} +- {se:.4f} (1 s.e.)")

if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 20000, float(sys.argv[2]) if len(sys.argv) > 2 else 4.0,
         int(sys.argv[3]) if len(sys.argv) > 3 else 5)
```

### `simplified_tiebreak.py`

```python
#!/usr/bin/env python3
"""Variant: (O5'),(O6') = (O5),(O6) WITHOUT the emptiness clauses (a stronger, simpler tie-break).
Checks that Lemma 16 still holds for the leftmost optimal copy and that at most one pair passes.
usage: python3 simplified_tiebreak.py [trials] [seed]"""
import sys, random
import gadget
from gadget import levels, heights, lt, inR, classes, rand_config, plant, is_plant

def conds2(P, lev, h, e, x, T0):
    A, B, C = classes(P, e, x)
    return (lev[e] >= T0 + 1,
            all(lev[r] <= lev[e] for r in A),
            all(h[r] <= h[x] for r in B),
            not any(lev[r] >= lev[e] + 2 and h[r] >= h[x] + 2 for r in C),
            not any(lev[r] == lev[e] and r[0] < e[0] and r[1] > e[1] for r in A),
            not any(h[r] == h[x] and r[0] < x[0] and r[1] > x[1] for r in B))

def main(trials, seed):
    rng = random.Random(seed); pairs = plants = 0
    for _ in range(trials):
        n = rng.randint(12, 30); P = rand_config(n, rng)
        S = set(rng.sample(range(1, 4), rng.randint(0, 3))); T0 = 2 * max(S) if S else 0
        lev, N, st = levels(P, S); h = heights(P)
        if N < T0 + 2: continue
        z = {i: min(q for q in P if lev[q] == i and h[q] == N - i + 1) for i in range(T0 + 1, N + 1)}
        for i in range(T0 + 1, N):
            assert all(conds2(P, lev, h, z[i], z[i + 1], T0)); pairs += 1
        i = rng.randint(T0 + 1, N - 1); e, x = z[i], z[i + 1]
        P2 = P + plant(P, e, x, rng); lev2, N2, st2 = levels(P2, S); h2 = heights(P2); p = lev[e] + 1
        G = [(a, b) for a in P2 if lev2[a] == p - 1 for b in P2 if lt(a, b) and is_plant(P2, a, b)
             and all(conds2(P2, lev2, h2, a, b, T0))]
        assert G == [(e, x)], G; plants += 1
    print(f"simplified tie-break: Lemma 16 ok on {pairs} pairs; G_p = {{(z_(p-1), z_p)}} exactly in {plants} plantings")

main(int(sys.argv[1]) if len(sys.argv) > 1 else 3000, int(sys.argv[2]) if len(sys.argv) > 2 else 3)
```

### `constants.py`

```python
#!/usr/bin/env python3
"""Recompute every numerical constant of Sections 5-7 of layered-refutation.md.  usage: python3 constants.py"""
from math import *
import random
print("Lemma 19: 1-1/e =", 1-exp(-1), "; Hoeffding exponent 2*(0.132)^2*2 =", 2*0.132**2*2, "(claimed >= 0.069)")
A1 = 1e-10
print("Lemma 20: 16 e^2 (A1/2)^(1/4) =", 16*e**2*(A1/2)**0.25, "(claimed < 0.315 < 1/3)")
# exact Pr(E1 E2 < t) versus the bound 2 sqrt t, by simulation
rng = random.Random(0); t = 0.01
est = sum(rng.expovariate(1)*rng.expovariate(1) < t for _ in range(400000))/400000
print("          Pr(E1E2<0.01) ~", est, "<= 2 sqrt t =", 2*sqrt(t))
# covering: for random (W,H) with W,H<=T, WH<=M^2 find r as in the proof
bad = 0
for _ in range(200000):
    T = 2**rng.uniform(1, 40); k = rng.randint(1, 500); M = 2*k
    R0 = ceil(log2(T)) + 1
    W = T*rng.random()**rng.choice([1, 5, 30]); H = min(T, M*M/W)*rng.random()**rng.choice([0.01, 1, 5])
    if W/M >= 2.0**(-R0):
        r = ceil(log2(W/M))
    else:
        r = -R0
    if not (abs(r) <= R0 and W <= M*2.0**r*(1+1e-12) and H <= 2*M*2.0**(-r)*(1+1e-12)):
        bad += 1
print("          covering by rectangles: failures in 200000 random (T,k,W,H):", bad)
print("Lemma 21: 4 e^-4 =", 4*exp(-4), "(claimed > 0.073); 0.063*floor(T/2) >= 0.03 T needs T >=", 0.063/0.0015)
print("Thm 3:   0.069*90 =", 0.069*90, "; 90 ln 3 =", 90*log(3))
print("         0.015/45.1^2 =", 0.015/45.1**2, "(claimed J/K >= 7e-6 T/ln^2 T)")
c = A1**7/(6*factorial(7)**2)
print("         A1^7/(6 (7!)^2) =", c, "(claimed > 6.5e-79); product with 7e-6 =", 7e-6*c, "(claimed >= 1e-84)")
print("Lemma 22: sqrt(8 pi 5) =", sqrt(40*pi), "(claimed <= 12); s^2/(80T) with s=20 sqrt(T ln T): exponent", 400/80, "ln T")
s = sum(2**(-j/2)*(1+sqrt(j)) for j in range(0, 400))/2
print("Lemma 23: (1/2) sum 2^(-j/2)(1+sqrt j) =", s, "(claimed < 3.79); 45*that =", 45*s, "(claimed <= 171)")
print("Thm 1:   need (1/2)1e-84/(ln T)^2 > 200 sqrt(ln T/T): first holds near ln T ~", end=" ")
L = 10.0
while 0.5e-84/L**2 <= 200*sqrt(L)*exp(-L/2): L += 1
print(L)
```
