---
title: "A layered pattern and the sharp form of Alon's conjecture on random universal permutations"
author: "Adam Ever-Hadani"
date: "November 10, 2026 — draft for independent verification"
abstract: |
  The longest increasing subsequence of a random permutation of length $n$ has length about $2\sqrt n$, so a random permutation contains the increasing pattern of length $k$ with high probability when $n\ge(1+\varepsilon)k^2/4$ and not when $n\le(1-\varepsilon)k^2/4$. Alon conjectured that, for every fixed $\varepsilon>0$, a random permutation of length $(1+\varepsilon)k^2/4$ contains *every* pattern of length $k$ with high probability. We give a proof that this fails for small $\varepsilon$: the layered pattern 2 1 4 3 $\cdots$ $k\,(k-1)$ has a sharp containment threshold at $(1+\varepsilon_0)k^2/4$ for a constant $\varepsilon_0>0$. The proof combines an exact fibre formula comparing the blocks 12 and 21 in a direct sum, a planted copy of the pattern 3416725 that creates a defect fibre at a controlled cost, and the rate of convergence of a superadditive mean. The proof was found by an AI system and has not yet been verified by a specialist.
---

# Declaration on the use of generative AI {-}

The proofs in this note were found and written by Claude (Anthropic), working as a coding agent in the author's repository on 10 November 2026. The author does not claim credit for the proof ideas. At the time of writing the proofs have been re-derived by AI reviewers (separate sessions of the same system, without access to the writing session) and the deterministic lemmas have been tested by programs that these reviewers wrote without seeing each other's code; details are in the verification record at the end. The proofs have not yet been verified line by line by the author or read by a specialist. The note is circulated to obtain that verification.

# Introduction {#sec:intro}

A permutation $\sigma\in S_n$ *contains* a pattern $\pi\in S_k$ if some $k$ entries of $\sigma$ are in the same relative order as $\pi$; it is *$k$-universal*, or a $k$-superpattern, if it contains every $\pi\in S_k$. Let $\sigma_n$ be a uniform element of $S_n$. Since the longest increasing subsequence of $\sigma_n$ has length $(2+o(1))\sqrt n$ with high probability[^whp] [@LS77; @VK77; @Romik15], $\sigma_n$ is not $k$-universal with high probability when $n\le(1-\varepsilon)k^2/4$.

[^whp]: "With high probability" (w.h.p.) means with probability tending to one as $k\to\infty$.

**Conjecture 1.1 (Alon; see [@Alon16; @Arratia99] and [@HK20, Conjecture 1.1]).** For every fixed $\varepsilon>0$, a uniform random permutation of length $(1+\varepsilon)k^2/4$ is w.h.p. $k$-universal.

He and Kwan proved that length $2000\,k^2\log\log k$ suffices [@HK20]; a recent preprint of Chen and Wang announces length $32k^2$ [@ChenWang26]. The conjecture is motivated in [@HK20] by analogy with random graphs, where cliques and independent sets are the hardest subgraphs to find: the monotone patterns are believed to be the hardest patterns. He and Kwan also state the weaker conjecture that every *fixed* $\pi\in S_k$ is contained w.h.p. at length $(1+\varepsilon)k^2/4$ [@HK20, Conjecture 5.3], and ask for the containment threshold of a fixed pattern.

We show that a layered pattern is strictly harder than the monotone ones. For a permutation $\sigma$ let $\mathrm{LIS}(\sigma)$ be the length of its longest increasing subsequence and $L_{21}(\sigma)$ the largest $m$ such that $\sigma$ contains
$$21^{\oplus m}\ =\ 2\ 1\ 4\ 3\ \cdots\ (2m)\,(2m-1),$$
the direct sum of $m$ decreasing pairs.

**Theorem 1.2.** The limit $c_{21}=\lim_{n\to\infty}\mathbb E L_{21}(\sigma_n)/\sqrt n$ exists and $0<c_{21}<1$.

**Corollary 1.3 (threshold for the layered pattern).** Let $\varepsilon_0=c_{21}^{-2}-1>0$, let $\varepsilon>-1$ be fixed and $n=\lfloor(1+\varepsilon)k^2/4\rfloor$. As $k\to\infty$, the probability that $\sigma_n$ contains $21^{\oplus\lfloor k/2\rfloor}$ tends to $0$ if $\varepsilon<\varepsilon_0$ and to $1$ if $\varepsilon>\varepsilon_0$. In particular, for $0<\varepsilon<\varepsilon_0$, $\sigma_n$ is w.h.p. not $k$-universal.

So Conjecture 1.1 fails for $\varepsilon<\varepsilon_0$, and so does [@HK20, Conjecture 5.3]. The main step is a lower bound for the gap between the two patterns in a Poissonised model.

**Theorem 1.4 (deficit).** Let $P_T$ be a Poisson process of unit intensity on $[0,T]^2$. There is $T_\ast$ such that for all $T\ge T_\ast$,
$$\mathbb E\,\mathrm{LIS}(P_T)-2\,\mathbb E L_{21}(P_T)\ \ge\ 10^{-84}\,\frac{T}{(\ln T)^2}.$$

The constants in the proofs are explicit and very small; they carry no information. Simulations give $\mathbb E\lfloor\mathrm{LIS}(\sigma_n)/2\rfloor-\mathbb EL_{21}(\sigma_n)=(0.00113\pm0.00002)\sqrt n$ for $n$ from $10^3$ to $10^8$ (1.29 million permutations, both statistics computed on the same permutation; data and programs are in the repository cited at the end), that is $c_{21}\approx0.99887$ and $\varepsilon_0\approx0.0023$. Together with [@ChenWang26], Corollary 1.3 would place the least constant $C$ such that length $Ck^2$ is w.h.p. $k$-universal between $(1+\varepsilon_0)/4$ and $32$.

## Proof outline

*Fibres (Section \ref{sec:flip}).* Replacing a block $12$ by $21$ in a direct sum never increases the probability of containment. This is known: after reversal it is the case of chains of size two of the skew shape conjecture, proved by Jelínek and by Burstein and Pantone [@Jelinek08; @BP15; @JK21]. We need its proof, because it expresses the difference of the two probabilities as the expectation of a non-negative quantity over *fibres*, and identifies a three-point fibre, the *lens*, on which this quantity equals $1/3$. Flipping blocks one at a time bounds $\mathbb E\,\mathrm{LIS}-2\,\mathbb EL_{21}$ from below by a sum of non-negative *stage costs*.

*The gadget (Sections \ref{sec:gadget} and \ref{sec:resample}).* Seven points in the order 3416725, the pattern of [@BP15], placed in the empty rectangle between two consecutive points of an optimal copy, create a lens. By the Mecke equation, the probability of finding such a planted configuration equals an expectation, over configurations with an empty rectangle, of a power of the area of that rectangle. So a stage is expensive unless the relevant step of the optimal copy spans a very small area.

*Counting (Sections \ref{sec:count} and \ref{sec:deficit}).* First-moment bounds show that, with high probability, in every window of $90\ln T$ consecutive steps of every optimal copy most steps span an area that is not small. Placing each flipped block at a random position within such a window makes one optimal copy serve all positions of the window, and gives Theorem 1.4.

*Rate of convergence (Section \ref{sec:rate}).* The mean of $L_{21}$ in the Poisson square is superadditive and within $O(\sqrt{T\ln T})$ of its limit $c_{21}T$, as for longest common subsequences [@Alexander94]. A deficit of order $T/(\ln T)^2$ is larger than this error, so it is a deficit of the constant.

## Notation

Points of the plane are written $z=(z^{\mathsf x},z^{\mathsf y})$; $z<z'$ means that both coordinates of $z$ are strictly smaller, and $z\le z'$ that both are at most as large. $R(z,z')=\{w:z<w<z'\}$ is the open rectangle and $|R|$ its area. $I_b$ is the increasing pattern of length $b$, $\oplus$ the direct sum, and "$Q\supseteq\gamma$" means that the point set $Q$ contains the pattern $\gamma$. $\mathbb E[X;A]$ is the expectation of $X\mathbf 1_A$, and $\mathrm e$ is the base of the natural logarithm (the letter $e$ denotes a point). Statements are numbered within sections.

# Fibres and the block-flip theorem {#sec:flip}

## Setting

A *configuration* is a finite set $P\subset\mathbb R^2$ whose points have distinct abscissae and distinct ordinates. For a location $z$ put $\mathrm{SW}(z)=\{r\in P:r<z\}$ and $\mathrm{NE}(z)=\{r\in P:r>z\}$. A set of points contains a pattern $\gamma$ if some $|\gamma|$ of its points are order-isomorphic to $\gamma$; every set contains the empty pattern. A permutation $\sigma$ is identified with the configuration $\{(i,\sigma(i))\}$, and a property of configurations is an *order-type invariant* if it depends only on the permutation that the configuration induces. A point $a$ is *north-west* of $c$ if $a^{\mathsf x}<c^{\mathsf x}$ and $a^{\mathsf y}>c^{\mathsf y}$; then $a\wedge c=(a^{\mathsf x},c^{\mathsf y})$ and $a\vee c=(c^{\mathsf x},a^{\mathsf y})$ are the *corners* of the pair.

$P_T$ denotes a Poisson process of unit intensity on $[0,T]^2$. Almost surely it is a configuration, and given that it has $n$ points its order type is uniform on $S_n$. Hence the expectation of an order-type invariant under $P_T$ is a mixture over $n$ of its expectations under $\sigma_n$.

Fix patterns $\alpha,\beta$, possibly empty, and a configuration $P$. Let
$$\mathcal U=\mathcal U_\alpha(P)=\{z:\ \mathrm{SW}(z)\supseteq\alpha\},\qquad\mathcal V=\mathcal V_\beta(P)=\{z:\ \mathrm{NE}(z)\supseteq\beta\}.$$
$\mathcal U$ is an up-set and $\mathcal V$ a down-set for $\le$. The *inside* points are $I=P\cap\mathcal U\cap\mathcal V$, the *outside* points are $O=P\setminus I$. Let $X$ and $Y$ be the sets of abscissae and of ordinates of the inside points. The *board* is the set of cells $(x,y)\in X\times Y$ that lie in $\mathcal U_\alpha(O)\cap\mathcal V_\beta(O)$. A *valid filling* is a bijection $\varphi:X\to Y$ whose graph $\Gamma_\varphi$ lies in the board. A *$D$-inversion* of $\varphi$ is a pair $a,c\in\Gamma_\varphi$ with $a$ north-west of $c$, $a\wedge c\in\mathcal U_\alpha(O)$ and $a\vee c\in\mathcal V_\beta(O)$.

## The theorem

**Lemma 2.1 (reading the middle block).** $P\supseteq\alpha\oplus12\oplus\beta$ if and only if there are $r<r'$ in $P$ with $r\in\mathcal U$ and $r'\in\mathcal V$; then $r,r'\in I$. $P\supseteq\alpha\oplus21\oplus\beta$ if and only if there are $a,c\in P$, $a$ north-west of $c$, with $a\wedge c\in\mathcal U$ and $a\vee c\in\mathcal V$; then $a,c\in I$.

*Proof.* A copy of $\alpha\oplus B\oplus\beta$, with $B$ a block of two points, consists of a copy $A$ of $\alpha$, two middle points, and a copy $A'$ of $\beta$, with $A$ below-left of both middle points and $A'$ above-right of both. For middle points $r<r'$ a suitable $A$ exists iff $r\in\mathcal U$ and a suitable $A'$ iff $r'\in\mathcal V$; then $r\in\mathcal V$ and $r'\in\mathcal U$ by monotonicity. For $a$ north-west of $c$, "$A$ below-left of both" means $A\subset\mathrm{SW}(a\wedge c)$ and "$A'$ above-right of both" means $A'\subset\mathrm{NE}(a\vee c)$; and $a\wedge c\le a,c\le a\vee c$ gives $a,c\in\mathcal U\cap\mathcal V$. $\blacksquare$

**Lemma 2.2 (the regions are determined by the outside points).** $\mathcal U_\alpha(P)=\mathcal U_\alpha(O)$ and $\mathcal V_\beta(P)=\mathcal V_\beta(O)$.

*Proof.* Let $z\in\mathcal U_\alpha(P)$ with $\alpha$ non-empty. Among the copies of $\alpha$ in $\mathrm{SW}(z)$ choose one, $A$, whose rightmost point is leftmost possible. If $A$ contained an inside point $r$, then $r\in\mathcal U_\alpha(P)$ would give a copy of $\alpha$ in $\mathrm{SW}(r)\subset\mathrm{SW}(z)$ lying entirely to the left of $r$, contradicting the choice. So $A\subset O$ and $z\in\mathcal U_\alpha(O)$. The reverse inclusion is trivial, and the statement for $\mathcal V$ is symmetric. $\blacksquare$

**Lemma 2.3 (fibres).** Let $\varphi$ be a valid filling of the board of $P$ and $P_\varphi=O\cup\Gamma_\varphi$. Then the outside points of $P_\varphi$ are exactly $O$, its inside points are exactly $\Gamma_\varphi$, and $\mathcal U_\alpha(P_\varphi)=\mathcal U_\alpha(O)$, $\mathcal V_\beta(P_\varphi)=\mathcal V_\beta(O)$. Consequently the configurations with outside set $O$ and inside coordinate sets $X,Y$ are exactly the $P_\varphi$, $\varphi$ a valid filling.

*Proof.* Points of $\Gamma_\varphi$ lie in $\mathcal U_\alpha(O)\cap\mathcal V_\beta(O)\subset\mathcal U_\alpha(P_\varphi)\cap\mathcal V_\beta(P_\varphi)$, so they are inside for $P_\varphi$. Let $o\in O$. By Lemma 2.2 for $P$, $o\notin\mathcal U_\alpha(O)\cap\mathcal V_\beta(O)$; say $o\notin\mathcal U_\alpha(O)$. If $o\in\mathcal U_\alpha(P_\varphi)$, take a copy $A$ of $\alpha$ in $\mathrm{SW}(o)$ within $P_\varphi$. It is not contained in $O$, so it has a point $g\in\Gamma_\varphi$; but $g\in\mathcal U_\alpha(O)$ gives a copy of $\alpha$ in $O$ below-left of $g<o$, a contradiction. So $o$ is outside for $P_\varphi$, and the equalities of regions are Lemma 2.2 for $P_\varphi$. Conversely, if $P'$ has outside set $O$ and inside coordinate sets $X,Y$, its inside points lie in $\mathcal U_\alpha(P')\cap\mathcal V_\beta(P')=\mathcal U_\alpha(O)\cap\mathcal V_\beta(O)$ by Lemma 2.2 for $P'$, hence on the board; so $P'=P_\varphi$ for a valid $\varphi$. $\blacksquare$

**Lemma 2.4 (two sorting arguments).** Suppose a board has a valid filling. (i) The decreasing bijection is valid, and it is the only valid filling without an increasing pair. (ii) There is a valid filling without a $D$-inversion.

*Proof.* (i) If a valid $\varphi$ has an increasing pair $r<r'$, replace $r,r'$ by $(r^{\mathsf x},r'^{\mathsf y})$ and $(r'^{\mathsf x},r^{\mathsf y})$. Both lie between $r\in\mathcal U_\alpha(O)$ and $r'\in\mathcal V_\beta(O)$ for $\le$, hence on the board. The number of inversions increases; iterate. (ii) If a valid $\varphi$ has a $D$-inversion $(a,c)$, replace $a,c$ by $a\wedge c$ and $a\vee c$. Then $a\wedge c\in\mathcal U_\alpha(O)$ by assumption and $a\wedge c\le a\in\mathcal V_\beta(O)$; $a\vee c\in\mathcal V_\beta(O)$ by assumption and $a\vee c\ge a\in\mathcal U_\alpha(O)$. The number of inversions decreases; iterate. $\blacksquare$

For a configuration with $I\ne\emptyset$ let $F$ be the number of valid fillings of its board and $F^\circ\ge1$ the number of those without a $D$-inversion; put $\rho=(F^\circ-1)/F$, and $\rho=0$ if $I=\emptyset$. Both $F$ and $F^\circ$ are order-type invariants.

**Theorem 2.5 (block flip; fibre formula).** For all patterns $\alpha,\beta$ and all $n$,
$$\Pr(\sigma_n\supseteq\alpha\oplus12\oplus\beta)-\Pr(\sigma_n\supseteq\alpha\oplus21\oplus\beta)\ =\ \mathbb E\,\rho(\sigma_n)\ \ge\ 0,\tag{2.1}$$
and the same identity holds with $P_T$ in place of $\sigma_n$.

*Proof.* Partition $S_n$ into classes according to $(O,X,Y)$. By Lemma 2.3 a class with $I\ne\emptyset$ is in bijection with the valid fillings of its board, and $\mathcal U,\mathcal V$ are constant on it. By Lemmas 2.1 and 2.3, $P_\varphi\supseteq\alpha\oplus12\oplus\beta$ iff $\Gamma_\varphi$ has an increasing pair, i.e. by Lemma 2.4(i) iff $\varphi$ is not the decreasing bijection; and $P_\varphi\supseteq\alpha\oplus21\oplus\beta$ iff $\varphi$ has a $D$-inversion. So a class with $F$ members has $F-1$ members containing the first pattern and $F-F^\circ$ containing the second, and $F^\circ\ge1$ by Lemma 2.4(ii). Classes with $I=\emptyset$ contain neither. For $P_T$, average over the number of points; all quantities are order-type invariants. $\blacksquare$

After reversing permutations, the inequality in Theorem 2.5 is the case of chains of size two of the skew shape conjecture for transversal fillings, proved by Jelínek [@Jelinek08] and by Burstein and Pantone [@BP15, Lemmas 1.4 and 1.5]; see [@JK21, Theorem 2.5]. For $\alpha$ or $\beta$ empty the two probabilities are equal [@BWX07].

## Stage costs

For a set $S$ of positive integers let $W_S=B_1\oplus B_2\oplus\cdots$ be the infinite pattern with $B_i=21$ if $i\in S$ and $B_i=12$ otherwise, let $W_S[1..t]$ be the pattern of its first $t$ entries, and for a configuration $P$ let
$$N_S(P)=\max\{t\ge0:\ P\supseteq W_S[1..t]\}.$$
Since $W_S[1..t]$ is contained in $W_S[1..t+1]$, $\mathbb EN_S(P)=\sum_{t\ge1}\Pr(P\supseteq W_S[1..t])$ for a random configuration $P$. Clearly $N_\emptyset=\mathrm{LIS}$ and $2L_{21}\le N_{\mathbb N}$. Note that $W_S[1..2m+1]=B_1\oplus\cdots\oplus B_m\oplus1$ whether or not $m+1\in S$, because the first entry of a block is larger than everything before it.

**Corollary 2.6 (monotonicity).** Let $P$ be $\sigma_n$ or $P_T$. If $S\subset S'$ then $\Pr(P\supseteq W_{S'}[1..t])\le\Pr(P\supseteq W_S[1..t])$ for every $t$. Hence $\mathbb EN_{S'}(P)\le\mathbb EN_S(P)$, and in particular
$$2\,\mathbb EL_{21}(P)\ \le\ \mathbb EN_S(P)\ \le\ \mathbb E\,\mathrm{LIS}(P)\qquad\text{for every }S.$$

*Proof.* $W_S[1..t]$ is obtained from $W_{S'}[1..t]$ by replacing complete blocks $21$ by $12$, one at a time; each replacement is an instance of Theorem 2.5. $\blacksquare$

For $i\in S$ let $\alpha_i=W_{S\cap[1,i-1]}[1..2i-2]$, the first $i-1$ blocks, and define the *cost of stage $i$*
$$\mathrm{Cost}_S(i)=\sum_{b\ge0}\Bigl[\Pr(P_T\supseteq\alpha_i\oplus12\oplus I_b)-\Pr(P_T\supseteq\alpha_i\oplus21\oplus I_b)\Bigr]\ \ge0.$$
It depends on $S$ only through $S\cap[1,i-1]$.

**Lemma 2.7 (telescoping).** For every $S$,
$$\mathbb E\,\mathrm{LIS}(P_T)-2\,\mathbb EL_{21}(P_T)\ \ge\ \mathbb E\,\mathrm{LIS}(P_T)-\mathbb EN_S(P_T)\ =\ \sum_{i\in S}\mathrm{Cost}_S(i).$$

*Proof.* The inequality is Corollary 2.6. For the identity fix $t$ and let $i_1<\dots<i_r$ be the elements of $S$ that are at most $t/2$; put $S^{(u)}=\{i_1,\dots,i_u\}$ for $0\le u\le r$. Then $W_S[1..t]=W_{S^{(r)}}[1..t]$, and
$$W_{S^{(u-1)}}[1..t]=\alpha_{i_u}\oplus12\oplus I_{t-2i_u},\qquad W_{S^{(u)}}[1..t]=\alpha_{i_u}\oplus21\oplus I_{t-2i_u}.$$
So $\Pr(P_T\supseteq I_t)-\Pr(P_T\supseteq W_S[1..t])$ is a telescoping sum over $u$ of non-negative terms. Summing over $t$ and collecting, for each $i\in S$, the terms with $t=2i+b$, $b\ge0$, gives the claim. $\blacksquare$

**Definition 2.8 (lens).** A configuration $P$ has a *lens at $(\alpha,b)$* if, for the pair $(\alpha,\beta=I_b)$, there are exactly three inside points and, writing $x_1<x_2<x_3$ and $y_1<y_2<y_3$ for their abscissae and ordinates, the board consists of all nine cells except $(x_1,y_1)$, which is not in $\mathcal U_\alpha(O)$, and $(x_3,y_3)$, which is not in $\mathcal V_\beta(O)$.

For a point $r$ of a configuration $P$ let $h(r)$, the *height* of $r$, be the number of points of the longest increasing chain of $P$ that starts at $r$. Then $\mathrm{NE}(r)\supseteq I_b$ iff $h(r)\ge b+1$, and a location $z$ lies in $\mathcal V_{I_b}$, $b\ge1$, iff some $r>z$ has $h(r)\ge b$.

**Lemma 2.9 (lenses).** Let $\alpha$ be a pattern.

(i) A configuration has a lens at $(\alpha,b)$ for at most one $b$.

(ii) $\displaystyle\sum_{b\ge0}\Bigl[\Pr(P_T\supseteq\alpha\oplus12\oplus I_b)-\Pr(P_T\supseteq\alpha\oplus21\oplus I_b)\Bigr]\ \ge\ \frac13\,\Pr\bigl(P_T\text{ has a lens at }(\alpha,b)\text{ for some }b\bigr).$

*Proof.* (i) A point $r$ is inside for $(\alpha,I_b)$ iff $r\in\mathcal U_\alpha$ and $h(r)\ge b+1$, so the inside sets decrease as $b$ increases. Suppose there is a lens at $(\alpha,b)$ and let $r$ be its inside point with the largest abscissa. If $h(r)\ge b+2$, some $r'>r$ has $h(r')\ge b+1$, and $r'\in\mathcal U_\alpha$ because $r'>r$; then $r'$ is an inside point to the right of $r$, which is impossible. So $h(r)=b+1$, and for $b'>b$ the inside set does not contain $r$ and has at most two points.

(ii) On a lens board the valid fillings are 231, 312 and 321, so $F=3$. In 321 the points in columns $x_1,x_2$ form a $D$-inversion, with corners $(x_1,y_2)$ and $(x_2,y_3)$. In 231 and in 312 each of the two inversions has $(x_1,y_1)$ as lower corner or $(x_3,y_3)$ as upper corner, so there is no $D$-inversion. Hence $F^\circ=2$ and $\rho=1/3$. Having a lens at $(\alpha,b)$ is an order-type invariant, so by (2.1) for $P_T$ the bracket for $b$ is at least $\frac13\Pr(P_T\text{ has a lens at }(\alpha,b))$. By (i) these events are disjoint for different $b$. $\blacksquare$

# The gadget {#sec:gadget}

Throughout this section $S$ is a finite set of positive integers, $\Pi=W_S$, and $t_0=2\max S$ ($t_0=0$ if $S=\emptyset$), so that $\Pi$ is increasing after its first $t_0$ entries: $\Pi[1..t+1]=\Pi[1..t]\oplus1$ for $t\ge t_0$. Fix a configuration $P$ and let $N=N_S(P)$. For $t\ge0$ let $\mathcal U_t=\mathcal U_{\Pi[1..t]}(P)$; these are up-sets, decreasing in $t$. The *level* of a point $r\in P$ is
$$\ell(r)=1+\max\{t:\ r\in\mathcal U_t\},$$
and $h(r)$ is its height, as defined before Lemma 2.9.

**Lemma 3.1 (levels beyond $t_0$).**

(i) For $t\ge t_0$: a location $z$ lies in $\mathcal U_{t+1}$ iff some $r\in P$ with $r<z$ has $\ell(r)\ge t+1$.

(ii) If $\ell(r)\ge t_0+1$ then $\ell(r)=1+\max(\{t_0\}\cup\{\ell(r'):r'\in P,\ r'<r\})$. For any $r$: if $r'<r$ and $\ell(r')\ge t_0+1$ then $\ell(r)\ge\ell(r')+1$. In particular points of the same level $\ge t_0+1$ are incomparable.

(iii) If $\ell(r)\ge t_0+1$ then $\ell(r)+h(r)-1\le N$.

*Proof.* (i) A copy of $\Pi[1..t]\oplus1$ in $\mathrm{SW}(z)$ is a copy $A$ of $\Pi[1..t]$ and a point $r<z$ above-right of $A$; the latter says $r\in\mathcal U_t$, i.e. $\ell(r)\ge t+1$. (ii) Let $\bar\ell$ be the maximum of $\ell(r')$ over $r'<r$, with $\bar\ell=0$ if there is no such point. If $\bar\ell\ge t_0+1$, (i) with $t=\bar\ell-1$ gives $r\in\mathcal U_{\bar\ell}$ and (i) with $t=\bar\ell$ gives $r\notin\mathcal U_{\bar\ell+1}$. If $\bar\ell\le t_0$, the hypothesis gives $r\in\mathcal U_{t_0}$ and (i) with $t=t_0$ gives $r\notin\mathcal U_{t_0+1}$. The second assertion is (i) with $t=\ell(r')-1$. (iii) A copy of $\Pi[1..\ell(r)-1]$ below-left of $r$, the point $r$, and a chain of $h(r)-1$ points above $r$ form a copy of $\Pi[1..\ell(r)+h(r)-1]$, because $\ell(r)-1\ge t_0$. $\blacksquare$

**Anchors and outside conditions.** Let $e<f$ be points of $P$ and $R=R(e,f)$. A point $r\in P\setminus(R\cup\{e,f\})$ is called *lower* if $r<f$, *upper* if $r>e$, and *lateral* otherwise. No point is both lower and upper, and a lateral point is north-west or south-east of the whole rectangle. Consider the conditions:

* (O1) $\ell(e)\ge t_0+1$.
* (O2) $\ell(r)\le\ell(e)$ for every lower point $r$.
* (O3) $h(r)\le h(f)$ for every upper point $r$.
* (O4) No lateral point $r$ has both $\ell(r)\ge\ell(e)+2$ and $h(r)\ge h(f)+2$.
* (O5) No lower point $r$ with $\ell(r)=\ell(e)$ is north-west of $e$.
* (O6) No upper point $r$ with $h(r)=h(f)$ is north-west of $f$.

Write $\mathcal E(e,f)$ for the conjunction of (O1)–(O6). Conditions (O5) and (O6) are tie-breaking rules, used only in Lemma 3.4.

**Lemma 3.2 (the conditions do not see the rectangle).** The numbers $\ell(e)$, $h(f)$ and the truth of $\mathcal E(e,f)$ are the same for $P$ and for every configuration $P'$ with $P'\setminus R=P\setminus R$.

*Proof.* If $r\notin R$ and ($r<f$ or $r=e$), then no point of $R$ is below-left of $r$: such a point $w$ would satisfy $e<w<r$, which forces $r\in R$ if $r<f$ and is absurd if $r=e$. So $\ell(r)$ depends only on $P\setminus R$. Symmetrically $h(r)$ depends only on $P\setminus R$ if $r\notin R$ and ($r>e$ or $r=f$). For a lateral point both $\mathrm{SW}(r)$ and $\mathrm{NE}(r)$ avoid $R$. The conditions involve only these quantities and the classification of points outside $R$. $\blacksquare$

**The planted pattern.** "$P\cap R\cong3416725$" means that $R$ contains exactly seven points of $P$, order-isomorphic to 3 4 1 6 7 2 5. From left to right we name them $u_1,q_1,u_2,q_2,v_1,q_3,v_2$. The comparable pairs among them are exactly
$$u_1<q_1,q_2,v_1,v_2;\qquad u_2<q_2,q_3,v_1,v_2;\qquad q_1<q_2,v_1,v_2;\qquad q_2<v_1;\qquad q_3<v_2.$$

**Lemma 3.3 (the gadget).** Let $e<f$ in $P$ satisfy (O1)–(O4) and suppose $P\cap R(e,f)\cong3416725$. Put $p=\ell(e)+1$ and $b=h(f)+1$. Then $P$ has a lens at $(\Pi[1..p],b)$, with inside points $q_1,q_2,q_3$. The levels and heights of the planted points are those of Table 1.

Table: The planted points. Rank means rank among the seven points.

| Point | Abscissa rank | Ordinate rank | Level | Height | Inside for $(\Pi[1..p],I_b)$ |
|:------|:------:|:------:|:------:|:------:|:----------------------|
| $u_1$ | 1 | 3 | $p$ | $b+3$ | no: level $<p+1$ |
| $q_1$ | 2 | 4 | $p+1$ | $b+2$ | yes |
| $u_2$ | 3 | 1 | $p$ | $b+2$ | no: level $<p+1$ |
| $q_2$ | 4 | 6 | $p+2$ | $b+1$ | yes |
| $v_1$ | 5 | 7 | $p+3$ | $b$ | no: height $<b+1$ |
| $q_3$ | 6 | 2 | $p+1$ | $b+1$ | yes |
| $v_2$ | 7 | 5 | $p+2$ | $b$ | no: height $<b+1$ |

*Proof.* Let $Q=P\cap R$. A point of $P$ below-left of a point of $Q$ is in $Q$, equals $e$, or is lower; a point above-right of a point of $Q$ is in $Q$, equals $f$, or is upper.

*Levels.* Every $r\in Q$ is above $e$, so $\ell(r)\ge\ell(e)+1\ge t_0+2$ and Lemma 3.1(ii) computes $\ell(r)$ from the points below-left of $r$. By (O2) those outside $Q$ have level at most $\ell(e)=p-1$, with equality for $e$. Going through the list of comparable pairs gives the column of levels.

*Heights.* By (O3) the points above-right of $r\in Q$ outside $Q$ have height at most $h(f)=b-1$, with equality for $f$. Going through the list downwards gives the column of heights.

*Inside points.* A point $r$ is inside for $(\Pi[1..p],I_b)$ iff $r\in\mathcal U_p$ and $\mathrm{NE}(r)\supseteq I_b$, i.e. iff $\ell(r)\ge p+1$ and $h(r)\ge b+1$. In $Q$ this holds exactly for $q_1,q_2,q_3$. It fails for $e$ and for lower points, whose level is at most $p-1$; for $f$ and for upper points, whose height is at most $b-1$; and for lateral points by (O4).

*Board.* The abscissae $x_1<x_2<x_3$ are those of $q_1,q_2,q_3$ and the ordinates $y_1<y_2<y_3$ those of $q_3,q_1,q_2$. By Lemma 2.2 cells may be tested in $P$: a cell is in $\mathcal U_p$ iff some point below-left of it has level at least $p$ (Lemma 3.1(i)), and in $\mathcal V_{I_b}$ iff some point above-right of it has height at least $b$. The points below-left of $(x_1,y_1)$ are $e$ and lower points — not $u_1$, whose ordinate lies between $y_1$ and $y_2$, and not $u_2$, which is to the right of $x_1$ — so they have level at most $p-1$ and $(x_1,y_1)\notin\mathcal U_p$. The cells $(x_1,y_2)>u_1$ and $(x_2,y_1)>u_2$ are in $\mathcal U_p$, and every other cell is $\ge$ one of them. Symmetrically, the points above-right of $(x_3,y_3)$ are $f$ and upper points — not $v_1$, which is to the left of $x_3$, and not $v_2$, whose ordinate lies between $y_2$ and $y_3$ — so $(x_3,y_3)\notin\mathcal V_{I_b}$; the cells $(x_2,y_3)<v_1$ and $(x_3,y_2)<v_2$ are in $\mathcal V_{I_b}$, and every other cell is $\le$ one of them. $\blacksquare$

For $p\ge t_0+2$ let $\mathcal G_p(P)$ be the set of pairs $e<f$ of points of $P$ with $\ell(e)=p-1$, $\mathcal E(e,f)$, and $P\cap R(e,f)\cong3416725$.

**Lemma 3.4 (at most one planted pair).** $|\mathcal G_p(P)|\le1$, and if $\mathcal G_p(P)\ne\emptyset$ then $P$ has a lens at $(\Pi[1..p],b)$ for some $b$.

*Proof.* The second assertion is Lemma 3.3. Let $(e,f)$ and $(e',f')$ be in $\mathcal G_p(P)$. By Lemma 3.3 each gives a lens at $(\Pi[1..p],b)$, with $b=h(f)+1$, respectively $b=h(f')+1$; by Lemma 2.9(i) the two values of $b$ agree, so $h(f)=h(f')$, and the inside set $\{q_1,q_2,q_3\}$ is the same for both pairs and lies in both rectangles. The hypotheses are symmetric in the two pairs. Suppose $e\ne e'$. Both have level $p-1\ge t_0+1$, so they are incomparable by Lemma 3.1(ii), and we may assume that $e'$ is north-west of $e$. Then $e'<q_1<f$, and $e'\notin R(e,f)\cup\{e,f\}$ because $e'$ is not above $e$; so $e'$ is a lower point for $(e,f)$, of the same level as $e$ and north-west of $e$: this contradicts (O5) for $(e,f)$. Suppose $f\ne f'$. They have the same height, so they are incomparable, and we may assume that $f'$ is north-west of $f$. Then $f'>q_1>e$, and $f'\notin R(e,f)\cup\{e,f\}$ because $f'$ is not below $f$; so $f'$ is an upper point for $(e,f)$, of the same height as $f$ and north-west of $f$: this contradicts (O6). $\blacksquare$

**Lemma 3.5 (leftmost optimal copy).** Suppose $N\ge t_0+2$. For $t_0+1\le i\le N$ let $Z_i=\{r\in P:\ell(r)=i,\ h(r)=N-i+1\}$ and let $z_i$ be the point of $Z_i$ with the smallest abscissa. Then every $Z_i$ is non-empty, and for $t_0+1\le i<N$: $z_i<z_{i+1}$, $R(z_i,z_{i+1})\cap P=\emptyset$, and $\mathcal E(z_i,z_{i+1})$ holds.

*Proof.* Take a copy of $\Pi[1..N]$ in $P$ and let $r_j$ be its point in position $j>t_0$. Then $\ell(r_j)\ge j$ and $h(r_j)\ge N-j+1$, and Lemma 3.1(iii) forces equality, so $r_j\in Z_j$. Each $Z_i$ is an antichain by Lemma 3.1(ii); in an antichain the leftmost point is the topmost, so $z_i$ has the largest ordinate in $Z_i$.

Every $r\in Z_{i+1}$ has a predecessor in $Z_i$: since $\ell(r)=i+1\ge t_0+2$, the maximum in Lemma 3.1(ii) equals $i>t_0$ and is attained by a point $r'<r$ with $\ell(r')=i$; then $h(r')\ge h(r)+1$, with equality by Lemma 3.1(iii). Every $r\in Z_i$ with $i<N$ has a successor in $Z_{i+1}$: some $r'>r$ has $h(r')=N-i$, and $\ell(r')\ge i+1$ with equality by Lemma 3.1(iii). Let $w\in Z_i$ be a predecessor of $z_{i+1}$ and $w'\in Z_{i+1}$ a successor of $z_i$. Then $z_i^{\mathsf x}\le w^{\mathsf x}<z_{i+1}^{\mathsf x}$ and $z_i^{\mathsf y}<w'^{\mathsf y}\le z_{i+1}^{\mathsf y}$, so $z_i<z_{i+1}$. A point of $P$ strictly between them would have a level strictly between $i$ and $i+1$.

Write $e=z_i$, $f=z_{i+1}$; then $h(e)=N-i+1$ and $h(f)=N-i$. (O1) is clear. (O2): if $r<f$ then either $\ell(r)\le t_0\le i$, or $\ell(r)\ge t_0+1$ and $\ell(r)\le\ell(f)-1=i$ by Lemma 3.1(ii). (O3): $r>e$ gives $h(r)\le h(e)-1=h(f)$. (O4): $\ell(r)\ge i+2$ and $h(r)\ge N-i+2$ would contradict Lemma 3.1(iii). (O5): a lower point $r$ with $\ell(r)=i$ has $h(r)\ge h(f)+1=N-i+1$, with equality by Lemma 3.1(iii); so $r\in Z_i$, and it cannot be north-west of $z_i$. (O6): an upper point $r$ with $h(r)=N-i$ has $\ell(r)\ge i+1$, with equality; so $r\in Z_{i+1}$, and it cannot be north-west of $z_{i+1}$. $\blacksquare$

# Resampling {#sec:resample}

**Lemma 4.1 (resampling identity).** Let $S$ be finite, $\Pi=W_S$ and $t_0=2\max S$, with levels, heights and the conditions $\mathcal E$ as in Section \ref{sec:gadget}, and let $p\ge t_0+2$. Then
$$\Pr\bigl(\mathcal G_p(P_T)\ne\emptyset\bigr)\ =\ \mathbb E\sum_{(e,f)}\mathbf 1\bigl\{e<f,\ \ell(e)=p-1,\ \mathcal E(e,f),\ P_T\cap R(e,f)=\emptyset\bigr\}\,\frac{|R(e,f)|^{7}}{(7!)^2},$$
where the sum is over ordered pairs of distinct points of $P_T$.

*Proof.* By Lemma 3.4 the left side is $\mathbb E|\mathcal G_p(P_T)|$. By the bivariate Mecke equation [@LastPenrose17, Theorem 4.4], for measurable $g\ge0$,
$$\mathbb E\sum_{(e,f)}g\bigl(e,f,P_T\setminus\{e,f\}\bigr)=\int\!\!\int\mathbb E\,g(e,f,P_T)\,\mathrm de\,\mathrm df,$$
the integral being over $([0,T]^2)^2$. By Lemma 3.2 the indicator of $\{\ell(e)=p-1,\ \mathcal E(e,f)\}$, evaluated in the configuration $\chi\cup\{e,f\}$, is a function $\Phi(e,f,\chi\setminus R(e,f))$; it is measurable, being an order-type invariant of finitely many points. Fix $e<f$ in $[0,T]^2$. The open rectangle $R=R(e,f)$ lies in $[0,T]^2$ and contains neither $e$ nor $f$; $P_T\cap R$ and $P_T\setminus R$ are independent, and $P_T\cap R$ is a Poisson process on a set of area $A=|R|$. Seven independent uniform points have a prescribed order type with probability $1/7!$, so
$$\Pr(P_T\cap R\cong3416725)=\exp(-A)\,\frac{A^7}{(7!)^2},\qquad\Pr(P_T\cap R=\emptyset)=\exp(-A).$$
Apply the Mecke equation twice, with $g=\mathbf 1\{e<f\}\,\Phi\cdot\mathbf 1\{\chi\cap R\cong3416725\}$ and with $g=\mathbf 1\{e<f\}\,\Phi\cdot\mathbf 1\{\chi\cap R=\emptyset\}\,A^7/(7!)^2$: both sides of the lemma equal $\int\!\!\int_{e<f}\mathbb E\,\Phi(e,f,P_T\setminus R)\,\exp(-A)A^7/(7!)^2\,\mathrm de\,\mathrm df$. $\blacksquare$

**Proposition 4.2 (cost of a stage).** Let $S$ be finite, $\Pi=W_S$, $p\ge t_0+2$, $\alpha=\Pi[1..p]$, $N=N_S(P_T)$, and let $(z_i)$ be the leftmost optimal copy of Lemma 3.5. Then
$$\sum_{b\ge0}\Bigl[\Pr(P_T\supseteq\alpha\oplus12\oplus I_b)-\Pr(P_T\supseteq\alpha\oplus21\oplus I_b)\Bigr]\ \ge\ \frac{1}{3\,(7!)^2}\ \mathbb E\Bigl[\,|R(z_{p-1},z_p)|^{7};\ N\ge p\Bigr].$$

*Proof.* By Lemma 2.9(ii) and Lemma 3.4 the left side is at least $\frac13\Pr(\mathcal G_p(P_T)\ne\emptyset)$. By Lemma 4.1 this is $\frac13$ of an expected sum of non-negative terms, and on the event $N\ge p$ the pair $(z_{p-1},z_p)$ is one of them, by Lemma 3.5 with $i=p-1\ge t_0+1$. $\blacksquare$

# Three first-moment estimates {#sec:count}

A *step* is a pair of points $z<z'$; it is *thin* if $|R(z,z')|<\theta$, where $\theta=10^{-10}$. A chain $z_0<\dots<z_k$ has $k$ steps, with increments $(\omega_i,\eta_i)=z_i-z_{i-1}$, and its *span* is $R(z_0,z_k)$.

**Lemma 5.1 (a large rectangle contains a long chain).** For every integer $k\ge1$, the expected number of pairs $z<z'$ of points of $P_T$ such that $|R(z,z')|\ge4k^2$ and $P_T\cap R(z,z')$ contains no chain of $k$ points is at most $T^4\exp(-0.069\,k)$.

*Proof.* By the Mecke equation the expectation is the integral over $z<z'$ of the probability that the Poisson process in the open rectangle has no chain of $k$ points. Cut a rectangle of area at least $4k^2$ into a $2k\times2k$ grid of congruent cells, each of area at least $1$. The $2k$ diagonal cells are non-empty independently with probability at least $1-\exp(-1)>0.632$, and points in distinct diagonal cells form a chain. By Hoeffding's inequality the probability that fewer than $k$ of them are non-empty is at most $\exp(-2(0.132)^2\cdot2k)\le\exp(-0.069\,k)$. $\blacksquare$

**Lemma 5.2 (chains of bounded span have few thin steps).** For every integer $k\ge1$ and $T\ge2$, the expected number of chains $z_0<\dots<z_k$ in $P_T$ with $|R(z_0,z_k)|\le4k^2$ and at least $k/2$ thin steps is at most $(2\log_2T+5)\,T^2\,3^{-k}$.

*Proof.* By the Mecke equation the expectation is the Lebesgue measure of the set of such $(z_0,\dots,z_k)$. Let $W=\sum\omega_i$, $H=\sum\eta_i$, $M=2k$ and $R_0=\lceil\log_2T\rceil+1$. Then $W,H\le T$ and $WH\le M^2$. There is an integer $d$ with $|d|\le R_0$, $W\le M2^d$ and $H\le2M2^{-d}$: if $W/M\ge2^{-R_0}$ take $d=\lceil\log_2(W/M)\rceil$, so that $H\le M^2/W<2M2^{-d}$ and $d\le\lceil\log_2(T/2)\rceil<R_0$; otherwise take $d=-R_0$ and use $H\le T\le2^{R_0}$. Fix $d$ and put $a=M2^d$, $c=2M2^{-d}$, so $ac=8k^2$. The indicator of $\{W\le a,\ H\le c\}$ is at most
$$\exp\bigl(k(1-W/a)+k(1-H/c)\bigr)=\exp(2k)\prod_i\exp(-k\omega_i/a-k\eta_i/c).$$
Choose which $\lceil k/2\rceil$ steps are thin (at most $2^k$ ways), integrate $z_0$ over $[0,T]^2$ and each increment over $(0,\infty)^2$. A step without constraint contributes $ac/k^2=8$. A thin step contributes, after the substitution $\omega=(a/k)s$, $\eta=(c/k)s'$, the amount $8\Pr(E_1E_2<\theta/8)\le8\cdot2\sqrt{\theta/8}=8\sqrt{\theta/2}$, where $E_1,E_2$ are independent standard exponential variables and we used $\Pr(E_1E_2<t)\le\Pr(\min(E_1,E_2)<\sqrt t)\le2\sqrt t$. Since $8\sqrt{\theta/2}<1$, the total for one $d$ is at most $T^2\,(16\exp(2)(\theta/2)^{1/4})^k$, and $16\exp(2)(5\cdot10^{-11})^{1/4}<0.315<1/3$. There are $2R_0+1\le2\log_2T+5$ values of $d$. $\blacksquare$

**Lemma 5.3.** For $T\ge50$, $\Pr(2L_{21}(P_T)<0.06\,T)\le\exp(-10^{-4}(T-2))$.

*Proof.* The $\lfloor T/2\rfloor$ squares $[2j,2j+2)^2$ on the diagonal contain an inversion independently, with probability at least $4\exp(-4)>0.073$ (exactly two points, forming an inversion), and inversions in distinct squares form a copy of $21^{\oplus m}$. By Hoeffding's inequality the number of such squares is at least $0.063\lfloor T/2\rfloor\ge0.03\,T$ except with probability $\exp(-2\cdot10^{-4}\lfloor T/2\rfloor)$. $\blacksquare$

# Proof of Theorem 1.4 {#sec:deficit}

Let $\ln T\ge10$, $K=\lceil45\ln T\rceil\le45.1\ln T$ and $J=\lfloor0.015\,T/K\rfloor$. Let $\xi_1,\dots,\xi_J$ be independent and uniform on $\{1,\dots,K\}$, independent of $P_T$, and put $i_0=0$, $i_j=i_{j-1}+K+\xi_j$, $S=\{i_1,\dots,i_J\}$. Lemma 2.7 holds for every value of $S$, hence on average:
$$\mathbb E\,\mathrm{LIS}(P_T)-2\,\mathbb EL_{21}(P_T)\ \ge\ \sum_{j=1}^{J}\mathbb E\bigl[\mathrm{Cost}_S(i_j)\bigr].\tag{6.1}$$
Fix $j$ and $i_1<\dots<i_{j-1}$. Let $\Pi=W_{\{i_1,\dots,i_{j-1}\}}$, so that $t_0=2i_{j-1}$ in the notation of Section \ref{sec:gadget}; let $N$ be the length of the longest prefix of $\Pi$ contained in $P_T$, and $(z_\iota)$ its leftmost optimal copy. $\mathrm{Cost}_S(i_j)$ depends only on $i_1,\dots,i_j$. For each of the $K$ possible values $i=i_{j-1}+K+\xi$ of $i_j$, the pattern $\alpha_i$ is $\Pi[1..2i-2]$, because the blocks between $i_{j-1}$ and $i$ are $12$ in both. So the conditional expectation of $\mathrm{Cost}_S(i_j)$ given $i_1,\dots,i_{j-1}$ is $\frac1K\sum_iC(i)$, where $C(i)$ is the left side of Proposition 4.2 for $p=2i-2$. The indices are related as follows, with $\iota_0=t_0+2K-2$.

Table: Bookkeeping for one stage.

| Quantity | Value | Range as $\xi=1,\dots,K$ |
|:--------------------|:-----------------------|:-------------------------------|
| candidate block $i$ | $i_{j-1}+K+\xi$ | $i_{j-1}+K+1,\dots,i_{j-1}+2K$ |
| prefix length $p=2i-2$ | $t_0+2K+2\xi-2$ | at least $t_0+2K\ge t_0+2$ |
| step used: $(z_{p-1},z_p)$ | $p-1=\iota_0+2\xi-1$ | steps number $2,4,\dots,2K$ of the window |

Here the *window* is the chain $z_{\iota_0}<z_{\iota_0+1}<\dots<z_{\iota_0+2K}$, whose $2K$ steps are numbered $1,\dots,2K$. By Proposition 4.2,
$$C(i)\ \ge\ \frac{1}{3\,(7!)^2}\ \mathbb E\Bigl[\,|R(z_{p-1},z_p)|^{7};\ N\ge p\Bigr],\qquad p=2i-2.$$
Let $\mathcal A$ be the event that

* (A1) $N\ge\iota_0+2K$;
* (A2) no pair of points of $P_T$ is as in Lemma 5.1 with $k=2K$;
* (A3) no chain of $P_T$ is as in Lemma 5.2 with $k=2K$.

On $\mathcal A$ the window exists (Lemma 3.5; note $\iota_0\ge t_0+1$) and $N\ge p$ for every candidate. A chain of $P_T$ inside the span of the window has at most $2K-1$ points, because levels increase strictly along a chain from $z_{\iota_0}$ to $z_{\iota_0+2K}$ (Lemma 3.1(ii)), from $\iota_0$ to $\iota_0+2K$. By (A2) the span therefore has area less than $4(2K)^2$, and then by (A3) fewer than $K$ of the $2K$ steps are thin. So at least $K+1$ steps are not thin, and one of them has an even number. Hence
$$\sum_iC(i)\ \ge\ \frac{\theta^7}{3\,(7!)^2}\,\Pr(\mathcal A).$$
*Probability of $\mathcal A$.* (A1): $\iota_0+2K=2i_{j-1}+4K-2<4KJ\le0.06\,T$, since $i_{j-1}\le2K(j-1)$; and $\Pr(N\ge t)=\Pr(P_T\supseteq\Pi[1..t])\ge\Pr(P_T\supseteq W_{\mathbb N}[1..t])\ge\Pr(2L_{21}(P_T)\ge t)$, by Corollary 2.6 and because a copy of $21^{\oplus\lceil t/2\rceil}$ contains $W_{\mathbb N}[1..t]$; so (A1) fails with probability at most $\exp(-10^{-4}(T-2))$ by Lemma 5.3. (A2) fails with probability at most $T^4\exp(-0.069\cdot90\ln T)\le T^{-2}$. (A3) fails with probability at most $(2\log_2T+5)\,T^2\,3^{-90\ln T}\le T^{-2}$. Hence $\Pr(\mathcal A)\ge1/2$ for large $T$, and every stage satisfies
$$\mathbb E\bigl[\mathrm{Cost}_S(i_j)\,\big|\,i_1,\dots,i_{j-1}\bigr]\ \ge\ \frac{\theta^7}{6K\,(7!)^2}.$$
Summing over $j\le J$ in (6.1), with $J/K\ge7\cdot10^{-6}\,T/(\ln T)^2$ for large $T$ and $\theta^7/(6\,(7!)^2)>6.5\cdot10^{-79}$, gives Theorem 1.4. $\blacksquare$

**Remarks.** (i) With a second planted pattern, 1 4 5 2 7 8 3 6, which produces a lens one level higher, the odd-numbered steps of the window can be used as well and the bound improves to $c\,T/\ln T$; this variant is written out in the repository and is not used here. (ii) The logarithms come from (A2) and (A3), which are union bounds over all of $[0,T]^2$ and need windows of length of order $\ln T$. (iii) The randomisation of $i_j$ is what allows one optimal copy, that of $\Pi$, to serve all $K$ candidate positions.

# From the deficit to the constant {#sec:rate}

Let $P$ be a unit Poisson process on the quadrant $[0,\infty)^2$; for a rectangle $R$ write $L_{21}(R)$ and $\mathrm{LIS}(R)$ for the functionals of $P\cap R$. Put
$$\Lambda_{21}(T)=\mathbb EL_{21}([0,T]^2),\qquad\Lambda(T)=\mathbb E\,\mathrm{LIS}([0,T]^2),$$
and let $\nu$ be the number of points of $P$ in $[0,T]^2$. Let $Y_n$ be $L_{21}$ of $n$ independent uniform points of a rectangle, which has the law of $L_{21}(\sigma_n)$, and $\mu_n=\mathbb EY_n$; thus $\Lambda_{21}(T)=\mathbb E\mu_\nu$.

**Standing facts.**

* (F1) The law of $L_{21}(R)$ depends only on $|R|$ and is stochastically non-decreasing in it, because the maps $(x,y)\mapsto(sx,y/s)$ and translations preserve both the Poisson process and the order $<$.
* (F2) $L_{21}$ changes by at most one when a point is added, removed or moved, and for an integer $s$ the event $L_{21}\ge s$ is certified by $2s$ points. Also $L_{21}\le\mathrm{LIS}$ pointwise, by taking one point from each block.
* (F3) $\Lambda_{21}$ is non-decreasing and superadditive, $\Lambda_{21}(T_1+T_2)\ge\Lambda_{21}(T_1)+\Lambda_{21}(T_2)$, since copies in $[0,T_1]^2$ and $[T_1,T_1+T_2]^2$ concatenate. It is finite, being at most $\Lambda$, and $\Lambda(T)\le3T+1$ by the first-moment bound $\Pr(\mathrm{LIS}([0,T]^2)\ge k)\le(\mathrm eT/k)^{2k}$; so the supremum below is finite. By Fekete's lemma, $c_{21}:=\lim\Lambda_{21}(T)/T=\sup_T\Lambda_{21}(T)/T$, so $\Lambda_{21}(T)\le c_{21}T$; and $c_{21}>0$ by Lemma 5.3. In the same way $\Lambda(T)\le T\cdot\lim\Lambda(T)/T=2T$: here $\Lambda(T)=\mathbb E\,g(\nu)$ with $g(n)=\mathbb E\,\mathrm{LIS}(\sigma_n)$ non-decreasing, $g(n)/\sqrt n\to2$ [@LS77; @VK77], and $\nu/T^2\to1$ in $L^1$.
* (F4) $2\mu_n\le\mathbb E\,\mathrm{LIS}(\sigma_n)\le3\sqrt n$ for $n\ge n_0$: the first inequality is Corollary 2.6 for $\sigma_n$; the second follows from $\Pr(\mathrm{LIS}(\sigma_n)\ge k)\le\binom nk/k!$. Moreover $0\le\mu_{n+1}-\mu_n\le2\mu_{n+1}/(n+1)\le3/\sqrt{n+1}$: deleting a uniformly chosen point from $n+1$ points lowers $L_{21}$ only if the point is one of the $2Y_{n+1}$ points of a fixed optimal copy.

**Lemma 7.1 (concentration).** Let $T$ be large, $n_0\le n\le2T^2$, and let $m_n$ be an integer median of $Y_n$.

(i) For $u\ge0$: $\Pr(Y_n\ge m_n+u)\le2\exp\bigl(-u^2/(8(m_n+u))\bigr)$ and $\Pr(Y_n\le m_n-u)\le2\exp\bigl(-u^2/(8m_n)\bigr)$.

(ii) $m_n\le5T$ and $|m_n-\mu_n|\le17\sqrt T$. Consequently $\Pr(Y_n\ge\mu_n+17\sqrt T+u)\le2\exp(-u^2/(80T))$ for $0\le u\le5T$, and $\Pr(Y_n\le\mu_n-17\sqrt T-u)\le2\exp(-u^2/(40T))$ for $u\ge0$.

(iii) $|\Lambda_{21}(T)-\mu_{\lfloor T^2\rfloor}|\le5\ln T+1$, and $Y=L_{21}([0,T]^2)$ satisfies
$$\mathbb E\bigl(Y-\Lambda_{21}(T)-18\sqrt T-20\sqrt{T\ln T}\bigr)^+\ \le\ T^{-4}.$$

*Proof.* (i) $Y_n$ is a function of $n$ independent points that is $1$-Lipschitz and, by (F2), $\psi$-certifiable with $\psi(s)=2s$. Talagrand's inequality [@Talagrand95] in the form [@AlonSpencer16, Theorem 7.7.1] gives $\Pr(Y_n\le y-t\sqrt{2y})\,\Pr(Y_n\ge y)\le\exp(-t^2/4)$ for integers $y\ge1$ and real $t\ge0$. We may assume $m_n\ge1$, enlarging $n_0$. Take $y=m_n+\lceil u\rceil$ and $t=\lceil u\rceil/\sqrt{2y}$: the first factor is $\Pr(Y_n\le m_n)\ge\frac12$, and since $Y_n$ is an integer and $v\mapsto v^2/(m_n+v)$ is increasing, the first bound follows. Take $y=m_n$ and $t=u/\sqrt{2m_n}$: the second factor is at least $\frac12$, which gives the second bound.

(ii) By Markov's inequality and (F4), $m_n\le2\mu_n\le3\sqrt n\le5T$. By (i), $m_n-\mu_n\le\mathbb E(m_n-Y_n)^+=\int_0^\infty\Pr(Y_n\le m_n-u)\,\mathrm du\le\sqrt{8\pi m_n}\le12\sqrt T$, and $\mu_n-m_n\le\int_0^\infty\Pr(Y_n\ge m_n+u)\,\mathrm du\le\int_0^{m_n}2\exp(-u^2/(16m_n))\,\mathrm du+\int_{m_n}^\infty2\exp(-u/16)\,\mathrm du\le\sqrt{16\pi m_n}+32\le17\sqrt T$. The two tail bounds follow from (i), using $8(m_n+u)\le80T$ for $u\le5T$ and $8m_n\le40T$.

(iii) Put $r=T\ln T$. By (F4), $|\mu_n-\mu_{\lfloor T^2\rfloor}|\le5\ln T$ when $|n-T^2|\le r$. By a Chernoff bound for the Poisson distribution, $\Pr(|\nu-T^2|>r)\le2\exp(-(\ln T)^2/3)$. Since $\mu_n\le n/2$, this gives $|\Lambda_{21}(T)-\mu_{\lfloor T^2\rfloor}|\le5\ln T+\mathbb E[(\nu+T^2)/2;\,|\nu-T^2|>r]\le5\ln T+1$. So $\mu_n\le\Lambda_{21}(T)+\sqrt T$ when $|n-T^2|\le r$, and by (ii), for $0\le u\le5T$,
$$\Pr\bigl(Y\ge\Lambda_{21}(T)+18\sqrt T+u\bigr)\ \le\ 2\exp(-u^2/(80T))+2\exp(-(\ln T)^2/3).$$
Let $s=20\sqrt{T\ln T}$. The expectation in (iii) is $\int_s^\infty\Pr(Y\ge\Lambda_{21}(T)+18\sqrt T+u)\,\mathrm du$. The part over $[s,5T]$ is at most $(80T/s)\,T^{-5}+10T\exp(-(\ln T)^2/3)$. The part over $[5T,\infty)$ is at most $\mathbb E[Y;Y\ge5T]\le\mathbb E[\nu;\mathrm{LIS}([0,T]^2)\ge5T]\le(\mathbb E\nu^2\,(\mathrm e/5)^{10T})^{1/2}$, by (F2) and the first-moment bound $\Pr(\mathrm{LIS}([0,T]^2)\ge k)\le(\mathrm eT/k)^{2k}$. The sum is at most $T^{-4}$ for large $T$. $\blacksquare$

**Lemma 7.2 (rate of convergence).** For large $T$,
$$\Lambda_{21}(2T)\le2\,\Lambda_{21}(T)+45\sqrt{T\ln T},\qquad\text{and hence}\qquad c_{21}T-200\sqrt{T\ln T}\ \le\ \Lambda_{21}(T)\ \le\ c_{21}T.$$

*Proof.* Let $m=L_{21}([0,2T]^2)$ and take a copy of $21^{\oplus m}$ with blocks $\beta_1,\dots,\beta_m$; let $c_j$ be the upper-right corner of the bounding box of $\beta_j$. Both points of $\beta_i$ are $\le c_j$ if $i\le j$ and $>c_j$ if $i>j$. Let $j^*$ be the largest $j$ such that the coordinates of $c_j$ sum to at most $2T$, with $j^*=0$ if there is none. If $j^*\ge1$, the blocks $\beta_1,\dots,\beta_{j^*}$ lie in $R_x=[0,x]\times[0,2T-x]$, where $x=c_{j^*}^{\mathsf x}$. If $j^*\le m-1$, the blocks $\beta_{j^*+2},\dots,\beta_m$ lie in $R'_{x'}=[x',2T]\times[2T-x',2T]$, where $x'=c_{j^*+1}^{\mathsf x}$. Only $\beta_{j^*+1}$ is not accounted for. Therefore, in all cases,
$$m\ \le\ 1+M+M',\qquad M=\sup_{0\le x\le2T}L_{21}(R_x),\quad M'=\sup_{0\le x\le2T}L_{21}(R'_x).$$
The reflection $z\mapsto(2T,2T)-z$ maps $R_x$ to $R'_{2T-x}$, preserves the Poisson process on $[0,2T]^2$, and maps copies of $21^{\oplus m}$ to copies of $21^{\oplus m}$; so $M'$ has the law of $M$ and $\Lambda_{21}(2T)\le1+2\,\mathbb EM$.

Put $\delta=1/(2T)$. For $l=0,\dots,\lceil4T^2\rceil-1$ and $l\delta\le x\le(l+1)\delta$, the rectangle $R_x$ is contained in $\tilde R_l=[0,(l+1)\delta]\times[0,2T-l\delta]$, a rectangle in the quadrant of area at most $T^2+1$. By (F1), $X_l=L_{21}(\tilde R_l)$ is stochastically dominated by $Y'=L_{21}([0,T']^2)$ with $T'=\sqrt{T^2+1}$; and $\Lambda_{21}(T')\le\Lambda_{21}(T)+1$ by (F2), since $[0,T']^2\setminus[0,T]^2$ has area $1$. For every real $a$ we have $M\le a+\sum_l(X_l-a)^+$, so $\mathbb EM\le a+\lceil4T^2\rceil\,\mathbb E(Y'-a)^+$; no independence is used. With $a=\Lambda_{21}(T')+18\sqrt{T'}+20\sqrt{T'\ln T'}$, Lemma 7.1(iii) gives $\mathbb EM\le a+1\le\Lambda_{21}(T)+22\sqrt{T\ln T}$ for large $T$. This proves the first inequality. Iterating it,
$$\frac{\Lambda_{21}(2^jT)}{2^jT}\ \le\ \frac{\Lambda_{21}(T)}T+\sum_{i<j}\frac{45\sqrt{2^iT\ln(2^iT)}}{2^{i+1}T}\ \le\ \frac{\Lambda_{21}(T)}T+171\sqrt{\frac{\ln T}{T}},$$
because $\sqrt{\ln(2^iT)}\le\sqrt{\ln T}\,(1+\sqrt i)$ and $\frac12\sum_{i\ge0}2^{-i/2}(1+\sqrt i)<3.79$. Let $j\to\infty$ and use (F3). $\blacksquare$

Lemma 7.2 is the analogue for $L_{21}$ of Alexander's theorem on the rate of convergence of the mean length of the longest common subsequence [@Alexander94]; see also [@Rhee95]. Cutting an optimal object along an antidiagonal and combining superadditivity with a concentration inequality is the scheme of [@LMT12].

*Proof of Theorem 1.2.* By Lemma 7.1(iii) with $T=\sqrt n$, $|\Lambda_{21}(\sqrt n)-\mu_n|\le5\ln\sqrt n+1$, so $\lim\mu_n/\sqrt n=c_{21}$, which is positive by (F3). For large $T$, Theorem 1.4, (F3) and Lemma 7.2 give
$$2c_{21}T-400\sqrt{T\ln T}\ \le\ 2\,\Lambda_{21}(T)\ \le\ \Lambda(T)-10^{-84}\frac{T}{(\ln T)^2}\ \le\ 2T-10^{-84}\frac{T}{(\ln T)^2}.$$
Hence $1-c_{21}\ge\frac12\,10^{-84}(\ln T)^{-2}-200\sqrt{\ln T/T}$, which is positive for large $T$. $\blacksquare$

*Proof of Corollary 1.3.* Let $m=\lfloor k/2\rfloor$. Then $m/(c_{21}\sqrt n)\to(c_{21}\sqrt{1+\varepsilon})^{-1}$, which is larger than $1$ if $\varepsilon<\varepsilon_0$ and smaller than $1$ if $\varepsilon>\varepsilon_0$. By the previous proof, (F3) and Lemma 7.2, $c_{21}\sqrt n-O(n^{1/4}\sqrt{\ln n})\le\mu_n\le c_{21}\sqrt n+O(\ln n)$. If $\varepsilon<\varepsilon_0$, there is $\kappa\in(0,1)$ with $m\ge\mu_n+17n^{1/4}+\kappa\sqrt n$ for large $k$, and Lemma 7.1(ii) with $T=\sqrt n$ and $u=\kappa\sqrt n$ gives $\Pr(L_{21}(\sigma_n)\ge m)\le2\exp(-\kappa^2\sqrt n/80)\to0$. If $\varepsilon>\varepsilon_0$, there is $\kappa>0$ with $m\le\mu_n-17n^{1/4}-\kappa\sqrt n$ for large $k$, and the lower-tail bound of Lemma 7.1(ii) gives $\Pr(L_{21}(\sigma_n)<m)\to0$. Finally $21^{\oplus\lfloor k/2\rfloor}$ is contained in a pattern of length $k$, so a permutation that does not contain it is not $k$-universal. $\blacksquare$

# Concluding remarks {#sec:remarks}

**The universality constant.** Let $C^\ast$ be the infimum of the constants $C$ such that a uniform permutation of length $Ck^2$ is w.h.p. $k$-universal. Conjecture 1.1 states $C^\ast=1/4$. Corollary 1.3 gives $C^\ast\ge(1+\varepsilon_0)/4$, and [@ChenWang26] announces $C^\ast\le32$. We do not know the value of $C^\ast$, nor which patterns determine it.

**Which pattern is hardest?** Simulations of the analogous quantity for patterns $J_d\oplus J_d\oplus\cdots$ with decreasing layers of size $d$ show deficits that grow with $d$: about $0.005\sqrt n$, $0.0075\sqrt n$ and $0.0105\sqrt n$ for $d=3,4,6$, and up to $0.017\sqrt n$ for $d=16$, against $0.0023\sqrt n$ for $d=2$. A proof along the lines of this note would need the analogue of Theorem 2.5 for blocks of size $d$, which would follow from the skew shape conjecture [@JK21, Conjecture 2.4] and is open for $d\ge3$. Upper bounds for individual patterns are discussed in [@ADT26].

**An effective bound.** Theorem 1.2 gives no usable lower bound for $1-c_{21}$, and the deficit proved at a finite scale is $T/(\ln T)^2$ rather than the order $T$ suggested by simulation. The logarithms come from the union bounds (A2) and (A3). A deficit of order $T$ with an explicit constant would follow from the same proof if, for some constants $K$ and $a>0$, a window of $2K$ consecutive steps of the leftmost optimal copy at a prescribed level contained an even-numbered step of area at least $a$ with probability bounded below, uniformly in the stage. This is a statement about the environment seen from the starting point of a last-passage geodesic, and we expect it to require the theory of the Hammersley process rather than first-moment counting.

**The monotone heuristic.** The analogy with cliques in random graphs suggests that the most structured pattern is the hardest. For the comparison made here the relevant structure is local: every interior block $21$ of a direct sum creates configurations, the lenses, in which two points can each continue an optimal copy but cannot both be used. The monotone pattern has no such blocks.

# Verification record {#sec:verify .unnumbered}

This appendix records how the argument has been checked so far. It is not a substitute for refereeing.

**Dependencies.** Theorem 1.2 uses, from outside this note: the multivariate Mecke equation; Hoeffding's inequality; Talagrand's inequality for certifiable Lipschitz functions; Fekete's lemma; a Chernoff bound for the Poisson distribution; and $\mathbb E\,\mathrm{LIS}(\sigma_n)/\sqrt n\to2$. Theorem 2.5 is proved in full, although it is known. The logical order is: Theorem 2.5 $\to$ Corollary 2.6, Lemmas 2.7, 2.9 $\to$ Lemmas 3.1–3.5 $\to$ Lemma 4.1, Proposition 4.2 $\to$ Lemmas 5.1–5.3 $\to$ Theorem 1.4 $\to$ Lemmas 7.1, 7.2 $\to$ Theorem 1.2 and Corollary 1.3.

**Where an error would most likely hide.** In our judgement: Lemma 3.2 and its use in Lemma 4.1, that is, the claim that every outside condition is unaffected by the contents of the rectangle; Lemma 3.4, on which the passage from an expected number to a probability rests; the bookkeeping of indices in Section \ref{sec:deficit}; and the passages between the Poisson model and uniform permutations.

Table: What has been checked, and how. Counts refer to brute-force computation from the definitions of Sections \ref{sec:flip} and \ref{sec:gadget}; different counts in one row come from programs written separately.

| Statement | Check |
|:-----------------------|:-----------------------------------------------------|
| Theorem 2.5 | Exhaustive on $S_n$, $n\le8$, for seven pairs $(\alpha,\beta)$, and $n\le7$ for thirteen pairs by a second program |
| Theorem 2.5, in Lean 4 | Exact counts over $S_n$, $n\le9$, for six pairs $(\alpha,\beta)$, and the inequality for all $\alpha,\beta$ of size at most two and $n\le8$, proved for the mathematical containment predicate; kernel-checked for $n=7$ and for 1234 against 1324 at $n=8$, compiled evaluation otherwise. The general theorem is not formalised |
| Lemma 2.7 | Exact on $S_7,S_8,S_9$ for ten sets $S$ |
| Lemmas 3.2, 3.3 | Three programs: 7,756, 47,428 and 8,040 random plantings; negative controls fail when a hypothesis is dropped |
| Lemmas 2.9, 3.1 | Tested on random configurations by one program |
| Lemma 3.4 | 4,730 random cases; 54,649 and 23,674 adversarial cases by two further programs; both tie-breaking rules are needed |
| Lemma 3.5 | 1,922, 6,714 and 30,888 consecutive pairs of leftmost optimal copies (three programs) |
| Lemma 4.1 | Monte Carlo with a one-point plant (two programs); exact at leading order in $T$ for the seven-point plant |
| Lemma 7.2 | $\Lambda_{21}(2T)-2\Lambda_{21}(T)\approx0.65\,T^{1/3}$ for $T=10,\dots,400$; the cutting inequality holds in 3,300 of 3,300 samples |
| Proposition 4.2, Lemmas 5.1–5.3, 7.1 | Written proofs; re-derived by the reviewers; all numerical constants recomputed |
| Theorems 1.2, 1.4, Corollary 1.3 | Written proofs only; re-derived by four AI reviewers, two of which read only an earlier version of this note |

Two of the reviews were of the working files in the repository and two of earlier versions of this note; the present text incorporates their corrections, and its last changes (notation and wording) have not been re-read. The constants of Theorems 1.2 and 1.4 are far outside the range of simulation, so these theorems cannot be tested numerically except through their consistency with the measured value $c_{21}\approx0.99887$. Programs, raw outputs and the review reports are in the folders `experiments/w90-layered-deficit` and `experiments/w91-strict-deficit` of the repository \url{https://github.com/adamhadani/superpatterns}.

# References {-}

::: {#refs}
:::
