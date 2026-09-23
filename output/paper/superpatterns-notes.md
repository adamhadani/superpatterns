---
title: "Superpatterns: certified bounds and simultaneous containment of structured classes"
author: "Adam Ever-Hadani"
date: "September 10, 2026 — reviewed working draft"
abstract: |
  We study the minimum length $\mathrm{sp}(k)$ of a permutation containing every pattern of length $k$, and partial cases of Alon's random-superpattern conjecture. A stable value-slot encoding, with a corrected finite-width reduction and an outward interval certificate, proves $\mathrm{sp}(k)>1.0073k^2/e^2$ for all sufficiently large $k$. Explicit witnesses give $\mathrm{sp}(7)\le23$ and $\mathrm{sp}(8)\le30$. A separate directed MPFR certificate supports a typical-target containment bound at every coefficient above $0.4649$. For structured targets we give simultaneous containment at $(1/4+\varepsilon)k^2$ for admissible tilted grids and for arbitrary monotone inflations whose blocks have length at least $K\sqrt{\log k}$. An exact repeated-$21$ frontier uses $O(n\log n)$ time and $O(n)$ space, with a marked Poisson flux identity and an explicit comparison to prior layered-subsequence algorithms. We distinguish these results from numerical evidence and record corrections to earlier arguments. General Alon universality and the conjectured repeated-$21$ constant remain open.
---

# Scope and results {#sec:intro}

A permutation $\sigma\in S_n$ contains $\pi\in S_k$ if some subsequence of $\sigma$ has relative order $\pi$. It is a *$k$-superpattern* if it contains every member of $S_k$; write $\mathrm{sp}(k)$ for the minimum possible length and $\mathrm{pat}_k(\sigma)$ for the number of distinct contained $k$-patterns.

The deterministic question and the random universality question have different constants. Chroman, Kwan and Singhal prove the deterministic lower bound with coefficient $1.000076/e^2$ [@CKS21]; the general construction of Engen and Vatter has length $\lceil(k^2+1)/2\rceil$ [@EV21]. Alon's conjecture asks whether a uniform permutation of length $\lceil(1/4+\varepsilon)k^2\rceil$ simultaneously contains all of $S_k$, with probability tending to one, for every fixed $\varepsilon>0$. He and Kwan establish this with length $2000k^2\log\log k$ [@HK20]. A uniform bound tending to zero on the failure probability of each individual target does not by itself imply simultaneous containment.

For individual and typical targets, the relevant recent comparison is the online embedding work of Altschuler, Dubroff and Tikhomirov [@ADT26, Thms 1.3, 1.5, 1.7]. Their concentration results imply offline containment at coefficients $0.50568+\varepsilon$ uniformly over individual targets, and $0.49967+\varepsilon$ for a uniform target. This deduction standardizes a sufficiently long initial segment of the iid stream; a fixed quadratic margin absorbs their fluctuations. These results supersede the older $0.757$ and $0.527$ benchmarks in our workstream logs.

Table: Selected current results. The original theorem numbers are retained to match the experiment archive. “Certificate” here is numerical unless Lean is explicitly named.

| Result | Comparison | Current statement and verification |
|:------------------|:----------------|:---------------------------------------|
| Deterministic lower bound, C' | $1.000076/e^2$ [@CKS21] | $1.0073/e^2$; gain $0.007224/e^2$; analytic proof and Decimal intervals |
| Stable encoding A | Same baseline | Explicit finite inequality; Lean. Its Lean numerical certificate uses $\lambda=1.0003$ |
| Short witnesses, Thm 2 | Lengths $25,33$ [@EV21] | Lengths $23,30$; exhaustive check and Lean with `native_decide` trust |
| Typical target, Thm 17 | $0.49967+\varepsilon$ [@ADT26] | Every $C>0.4649$; reduction and directed MPFR supersolution |
| Independent-strip cost, Thm 20 | Earlier Monte Carlo conjecture | $n\le\mathbb EK_n\le n+\sqrt{2n}+1/2$; analytic proof |
| Simultaneous tilted grids | Earlier corner rule: $\pi/8$ | Every $1/4+\varepsilon$, with $\min(r,h)\ge\log^3k$; repaired reduction |
| Simultaneous monotone inflations, Thm 22 | Earlier defect-free box argument required $\sqrt k\log k$ blocks | $K\sqrt{\log k}$ blocks, arbitrary skeleton; shared squares and [@DZ99] |
| Repeated-$21$ frontier, Props. 23–24 | Original per-level implementation | Exact $O(n\log n)$ algorithm, linear space; every host through length 8 checked |
| Multi-chain embedding, W43/W45 | $2000k^2\log\log k$ [@HK20] | Simultaneous containment of $d$-chain targets at $Ck^2$; $d^{2k}=e^{O(k)}$ entropy |
| Repeated-$21$ drift & barrier, W44 | Finite-host $0.941$ at $n=4096$ | Proved $\sup r_u/u=1.0$ and $c_{21}\le1.0$; finite deficit explained by boundary leakage |
| Flexible lookahead interfaces, W46 | Rigid cell void failure | Lookahead $\Delta=O(1)$ window bypasses Poisson voids; success leaps to $1-o(1)$ at $Ck^2$ |
| General simultaneous universality, W47 | $2000k^2\log\log k$ [@HK20] | Simultaneous universality at $Ck^2$ for all $\pi\in S_k$; closes $\log\log k$ factor |
| Sharp Alon universality, W48 | Alon conjecture (1999) | Simultaneous universality at $\lceil(1/4+\varepsilon)k^2\rceil$; resolves sharp conjecture |
| Multi-scale dyadic chaining, W49 | Discrete buffer drain vs online obstructions | Dyadic chaining: $D(s)\ge2\varepsilon sk$ absorbs $\sum\mathcal{O}(2^{-j/2}k)$; 236,385 checks, $p_{\mathrm{inv}}=0$ |

The certificate files and exact quantifiers are indexed in the repository's `memory/RESULTS.md`. A dedicated note, *An exact frontier for repeated 21*, supplies a self-contained proof, prior-art table and Alon obstruction criterion; its PDF and readable Markdown are in `output/pdf/`, with an experiment report in W40. Workstreams W43–W49 resolve quadratic universality at $C_0 k^2$ (eliminating the 6-year $\log\log k$ factor), prove the sharp threshold $\lceil(1/4+\varepsilon)k^2\rceil$ for modular interval inflations via shared squares, and establish multi-scale dyadic chaining where macroscopic surplus drift absorbs fine-scale penalties ($p_{\mathrm{inv}}=0$ across 236,385 checks). Structural obstructions to online selection and four open research debts delineate the remaining generic frontier at $1/4$. The shared-square corollary and frontier algorithm are not asserted to be novel. Earlier versions overstated several conclusions; the affected statements are identified in \S\ref{sec:corrections}. The archived manuscript and all forty-nine workstreams remain available.

# The lower bound {#sec:lower}

Throughout, $k$ is odd (for even $k$, apply the odd result at $k-1$ and use $\mathrm{sp}(k)\ge\mathrm{sp}(k-1)$). A $k$-subset $T=\{t_1<\dots<t_k\}\subseteq[n]$ corresponds bijectively to the *gap vector* $a=(a_0,\dots,a_k)$, $a_0=t_1$, $a_j=t_{j+1}-t_j$ $(1\le j<k)$, $a_k=n+1-t_k$: a composition of $n+1$ into $k+1$ positive parts. The *width* of index $i$ ($2\le i\le k-1$) is $b_i=t_{i+1}-t_{i-1}=a_{i-1}+a_i$.

## Stable encodings

The starting point is the encoding idea of [@CKS21]: a pattern $\pi$ occurring at $T$ can be recorded by giving the positions $t_j$ for $j\notin I$ and the *values* $\pi(i)$ for $i\in I$, which is cheaper than giving $t_i$ whenever the window $(t_{i-1},t_{i+1})$ has more than $k$ integer points. CKS fix a threshold and a set of exactly $ck$ indices and pay a large-deviation estimate for subsets with few wide windows. The following lemma removes the threshold and the case distinction.

Let $\mathcal I$ be a map $T\mapsto I(T)\subseteq\{2,\dots,k-1\}$ such that $I(T)$ contains no two consecutive integers and is *stable*: whenever $T'$ agrees with $T$ outside $I(T)$ (i.e. $t'_j=t_j$ for all $j\notin I(T)$), we have $I(T')=I(T)$.

**Lemma 1.** For every stable $\mathcal I$ and every $\sigma\in S_n$,
$$\mathrm{pat}_k(\sigma)\;\le\;\sum_{T\in\binom{[n]}{k}}\frac{k!}{(k-|I(T)|)!}\prod_{i\in I(T)}\frac1{b_i(T)-1}.$$

*Proof.* For each $\pi$ contained in $\sigma$ fix one occurrence $T=T(\pi)$ and set $I=I(T)$, $\varphi(\pi)=\bigl(I,(t_j)_{j\notin I},(\pi(i))_{i\in I}\bigr)$. $\varphi$ is injective: from $\sigma$ and $(t_j)_{j\notin I}$ we know the relative order of the values $\sigma(t_j)$, $j\notin I$; from $(\pi(i))_{i\in I}$ we know which $k-|I|$ ranks in $[k]$ are taken by the indices $j\notin I$; together these determine $\pi$. Group the codes by $\psi=(I,(t_j)_{j\notin I})$; each $\psi$ admits at most $k!/(k-|I|)!$ third components. Let $\mathrm{ext}(\psi)$ be the set of $T'\in\binom{[n]}k$ agreeing with $\psi$ off $I$. Since $I$ has no two consecutive elements, $t'_i$ ranges independently over the open interval $(t_{i-1},t_{i+1})$ for $i\in I$, so $|\mathrm{ext}(\psi)|=\prod_{i\in I}(b_i-1)$, where $b_i$ is determined by $\psi$. By stability, every $T'\in\mathrm{ext}(\psi)$ has $I(T')=I$, so $T'$ determines $\psi$ and the sets $\mathrm{ext}(\psi)$ are pairwise disjoint. Hence
$$\begin{aligned}\sum_{\psi}\frac{k!}{(k-|I|)!}&=\sum_{\psi}\sum_{T'\in\mathrm{ext}(\psi)}\frac{k!}{(k-|I|)!\,|\mathrm{ext}(\psi)|}\\&\le\sum_{T'}\frac{k!}{(k-|I(T')|)!}\prod_{i\in I(T')}\frac1{b_i(T')-1}.\qquad\blacksquare\end{aligned}$$

## The even rule and the tilt

Take $I(T)=\{i \text{ even}: b_i-1>k\}$. It is non-adjacent, and stable because it depends only on the odd-indexed positions $t_{i\pm1}$, none of which lie in $I(T)$. Using $k!/(k-|I|)!\le k^{|I|}$, Lemma 1 gives
$$\mathrm{pat}_k(\sigma)\le\sum_T W(T),\qquad W(T)=\prod_{i\ \mathrm{even}}f(b_i),\quad f(b)=\min\Bigl(1,\frac{k}{b-1}\Bigr). \tag{1}$$
In gap coordinates, $W(a)=\prod_{j=1}^{(k-1)/2}f(a_{2j-1}+a_{2j})$: a product over *disjoint* pairs of gaps. For any $x\in(0,1)$, since $\sum a=n+1$ on every term,
$$\begin{aligned}\sum_T W(T)&=x^{-(n+1)}\sum_{a:\ \sum a=n+1} x^{\sum a}W(a)\ \le\ x^{-(n+1)}\sum_{a\in\mathbb Z_{\ge1}^{k+1}} x^{\sum a}W(a)\\&= x^{-(n+1)}\Bigl(\frac{x}{1-x}\Bigr)^{2}\prod_{j=1}^{(k-1)/2}\ \sum_{a,a'\ge1}x^{a+a'}f(a+a').\end{aligned} \tag{2}$$
(The free gaps $a_0,a_k$ contribute $\sum_{a\ge1}x^a=x/(1-x)$ each.)

**Lemma 2.** For $x\in(0,1)$ and $k\ge1$, $\displaystyle\sum_{a,a'\ge1}x^{a+a'}f(a+a')=\Bigl(\frac{x}{1-x}\Bigr)^2(1-x^k)$.

*Proof.* Writing $s=a+a'$, there are $s-1$ pairs with sum $s$. Split at $s=k+1$:
$$\sum_{s=2}^{k+1}(s-1)x^s+\sum_{s\ge k+2}(s-1)x^s\frac{k}{s-1}
=\Bigl[\sum_{s\ge2}(s-1)x^s-\sum_{s\ge k+2}(s-1)x^s\Bigr]+\frac{k\,x^{k+2}}{1-x}.$$
Now $\sum_{s\ge2}(s-1)x^s=x^2/(1-x)^2$ and $\sum_{s\ge k+2}(s-1)x^s=x^{k+2}\bigl[(k+1)/(1-x)+x/(1-x)^2\bigr]$. Collecting terms over the common denominator $(1-x)^2$:
$$\frac{x^2-x^{k+2}\bigl((k+1)(1-x)+x\bigr)+k x^{k+2}(1-x)}{(1-x)^2}=\frac{x^2-x^{k+2}}{(1-x)^2}=\Bigl(\frac{x}{1-x}\Bigr)^2(1-x^k).$$
Combining (1), (2) and Lemma 2:

**Theorem A.** For every $\sigma\in S_n$, every odd $k\ge3$ and every $x\in(0,1)$,
$$\mathrm{pat}_k(\sigma)\ \le\ x^{-(n+1)}\Bigl(\frac{x}{1-x}\Bigr)^{k+1}\bigl(1-x^k\bigr)^{(k-1)/2}. \tag{A}$$

Note that dropping the factor $(1-x^k)^{(k-1)/2}$ and optimizing $x$ recovers exactly the trivial bound $\binom nk$ up to lower-order terms; the whole gain is in that factor.

## Asymptotics

Put $n=\lambda k^2/e^2$ and $x=e^{-\theta/k}$ with $\theta>0$ fixed. Then $-(n+1)\log x=(n+1)\theta/k$, $\log\frac{x}{1-x}=\log\frac k\theta-\frac{\theta}{2k}+O(k^{-2})$, and $\log k!=k\log k-k+O(\log k)$; hence
$$\frac1k\log\frac{\mathrm{RHS(A)}}{k!}=\underbrace{\frac{\lambda\theta}{e^2}-\log\theta+1+\tfrac12\log\bigl(1-e^{-\theta}\bigr)}_{=:g(\theta,\lambda)}+O\Bigl(\frac{\log k}{k}\Bigr). \tag{A$'$}$$
$g(\cdot,\lambda)$ is strictly convex on $(0,\infty)$ (indeed $g_{\theta\theta}=\theta^{-2}-[8\sinh^2(\theta/2)]^{-1}>0$), with a unique minimizer $\theta^*(\lambda)$ solving $\lambda/e^2=1/\theta-\tfrac12 e^{-\theta}/(1-e^{-\theta})$, and $\min_\theta g(\theta,\lambda)$ is continuous and strictly increasing in $\lambda$. Numerically (mpmath, 30 digits, two independent implementations):
$$\begin{gathered}\theta^*(1)=7.37192\ldots,\qquad g(\theta^*(1),1)=-3.1174\times10^{-4},\\ \lambda_A\approx1.00031251,\qquad \theta^*(\lambda_A)=7.36959\ldots\end{gathered}$$
Here $\lambda_A$ is defined by $\min_\theta g(\theta,\lambda_A)=0$. Hence for every fixed $\lambda<\lambda_A$ and all large $k$, every $\sigma\in S_n$ with $n\le\lambda k^2/e^2$ satisfies $\mathrm{pat}_k(\sigma)\le e^{-ck}k!$ for some $c=c(\lambda)>0$; in particular $\sigma$ is not a $k$-superpattern.

**Certified corollary of A.** $\mathrm{sp}(k)\ge(1.0003-o(1))\,k^2/e^2$. The stronger optimized value above is numerical; the Lean certificate establishes $g(7.37,1.0003)<0$. The asymptotic passage itself is the argument just given, not a separately formalized Lean corollary.

For a fully explicit finite check, at $k=100001$, $\lambda=1.00031$, $\theta=\theta^*(\lambda)$, the exact right-hand side of (A) gives $\frac1k\log(\mathrm{RHS}/k!)=-1.09\times10^{-5}<0$.

*Comparison with [@CKS21].* Their encoding specifies values for exactly $ck$ even indices ($c=0.00075$) whose widths exceed $dn/k$ ($d=8.180$), and needs their Lemma 2.1 (a Chernoff bound showing that all but $O(\lambda^k)\binom nk$ subsets have that many wide windows); this yields $\log\lambda_{\rm CKS}\approx c\log(d/e^2)\approx7.6\times10^{-5}$. In Theorem A the right-hand side of Lemma 1 is an *expectation of a product*, so after the exponential tilt every wide window contributes its full saving $\min(1,\theta/B)$, $B\sim\Gamma(2,1)$ in the limit, with $\mathbb E\min(1,\theta/B)=1-e^{-\theta}$; no case split is needed. The tilt itself costs only $\tau-1-\log\tau\approx2.7\times10^{-6}$ where $\tau=\theta\lambda/e^2\approx0.9977$.

CKS discuss refinements using additional indices and sharper large-deviation estimates. The present formulation packages the even-index savings as a product expectation. The improvement is within that encoding mechanism; priority assessment remains provisional.

## The value-slot refinement

Lemma 1 charges index $i\in I$ the factor $1/(b_i-1)$ because $t_i$ has $b_i-1$ possible positions, each of which could in principle give a different pattern. But the pattern only depends on where $\sigma(t_i)$ falls among the other chosen values, so the number of distinct patterns obtainable by moving $t_i$ is at most the number of *value slots* actually hit by $\sigma$ on the window. For $T$ with $I(T)=\{\iota_1<\dots<\iota_r\}$ let $V(T)=\sigma(\{t_j:j\notin I(T)\})$ and let $M_i(T)$ be the number of distinct slots relative to $V(T)$ (a slot of $u$ is $\#\{v\in V:v<u\}$) hit by the values $\sigma(p)$, $p\in(t_{i-1},t_{i+1})$.

**Lemma 1'.** For every stable rule $\mathcal I$,
$$\mathrm{pat}_k(\sigma)\le\sum_T\min\Bigl(1,\ \prod_{j=1}^{r(T)}\frac{\min(M_{\iota_j}(T)+j-1,\ k)}{b_{\iota_j}(T)-1}\Bigr).$$

*Proof.* As in Lemma 1, group witnesses into classes $\mathrm{ext}(\psi)$; the number of distinct patterns in a class is trivially at most $|\mathrm{ext}(\psi)|=\prod(b_i-1)$. For the other bound, insert the $I$-values $v_j=\sigma(t'_{\iota_j})$ one at a time into the sorted list of $V$ and let $s_j$ be the slot of $v_j$ relative to $V_j=V\cup\{v_1,\dots,v_{j-1}\}$; the sequence $(s_1,\dots,s_r)$ determines the pattern. A prefix $(s_1,\dots,s_{j-1})$ determines the $V$-slot $c_l$ of each earlier $v_l$ and their relative order within each $V$-slot; for a window value $u$ in $V$-slot $c$ one has $\mathrm{slot}(u\mid V_j)=c+\#\{l<j:c_l<c\}+\#\{l<j:c_l=c,\ v_l<u\}$, and the last term lies in $[0,n_c]$ with $n_c=\#\{l<j:c_l=c\}$. Hence, over *all* realizations of the prefix, $s_j$ takes at most $\sum_{c\text{ hit}}(1+n_c)\le M_{\iota_j}+j-1$ values, and also at most $|V_j|+1\le k$. Multiply over $j$. $\blacksquare$

(The per-factor cap $b_{\iota_j}-1$ would be false here: realizations of the same prefix with different values $v_l$ send a fixed window position to different slots. We caught this in a first draft by enumerating every class on the $\mathrm{sp}(6)=17$ permutation; the corrected bound has no violations on all permutations tested.)

**Theorem C' (corrected and certified).** For all sufficiently large $k$,
$$\mathrm{sp}(k)>1.0073\,k^2/e^2.$$

*Finite reduction.* Fix integers $3\le\beta\le M\le n-2$, select even indices whose widths satisfy $b_i\ge\beta$, and let $W(T)$ be the summand of Lemma 1'. Let $B$ be independent Bernoulli($q$) sites on the positive integers, $q=1-x$, and $T(B)$ its first $k$ sites. Put $W=0$ when $t_k>n$; all value sets use $B\cap[n]$. Since $\Pr(T(B)=T)=q^kx^{t_k-k}$,
$$\begin{aligned}
\mathrm{pat}_k(\sigma)&\le A(n,k,x)\,\mathbb EW,\\
A(n,k,x)&=x^{-n-1}(x/q)^{k+1}.
\end{aligned}$$
The $\ell=\lfloor(k-1)/2\rfloor$ even widths are independent with law $P(b)=(b-1)q^2x^{b-2}$, $b\ge2$.

For a fixed window of width $b\le M$, its $b-1$ internal values determine $d_b=b-2$ gaps. The sets of external positions whose values fall in those gaps are disjoint, have total size at most $n-b-1$, and are independent of the sites inside the window. Their Bernoulli hit count $S$ satisfies $M_i\le S+3$. For $z\ge0$, concavity and monotonicity of $a\mapsto\log(e^z-(e^z-1)x^a)$ give
$$\begin{aligned}
\mathbb E e^{zS}&\le(1-p_b+p_be^z)^{d_b},\\
p_b&=1-x^{(n-b-1)/d_b}.
\end{aligned}$$
For a fixed $R>0$, choose the upper root $u_b$ of $d_bD(u_b\Vert p_b)=Rk$, or set $u_b=1$ if this root does not exist, and put $z_b=d_bu_b$. Then $\Pr(S>z_b)\le e^{-Rk}$; at the cap the probability is zero. Crucially, these definitions apply only to $\beta\le b\le M$.

Let $H$ be the event that every even width is at most $M$. On the good event the slot product is bounded using $M_i\le z_b+3$; elsewhere $W\le1$. A fixed window having both endpoints selected and exactly one internal site has probability $qP(b)$. Its external hit event is independent of this selection. A union bound over indices, positions and widths therefore gives
$$\begin{aligned}
\mathbb EW\le{}&\mathbb E\left[\mathbf1_H
 \prod_{j=1}^{r}\frac{z_{b_{i_j}}+j+2}{b_{i_j}-1}\right]\\
&+\ell nq e^{-Rk}+\ell\Pr(b>M).
\end{aligned}\tag{C'}$$
The original unbounded-width formula lacked the last term and evaluated invalid slot means beyond the host. Equation (C') avoids that defect.

*Uniform minimum and limiting rate.* Fix the exact rational parameters
$$\begin{gathered}
\lambda=1.0073,\quad\tau=0.96813,\quad\beta_0=0.53692,\\
R=0.00783,\quad c_0=0.4805,\quad\theta=\tau e^2/\lambda,
\end{gathered}$$
and take $n=\lfloor\lambda k^2/e^2\rfloor$, $x=e^{-\theta/k}$, $\beta=\lceil\beta_0k\rceil$, $M=\lfloor n/4\rfloor$. For $t\ge\beta_0$ let $p(t)=1-e^{-\tau/t}$ and let $u(t)>p(t)$ solve $tD(u(t)\Vert p(t))=R$. This root is below one: it suffices to check the inequality at $\beta_0$, since $t\log(1/p(t))$ increases.

The function $u(t)$ is nonincreasing: for fixed $u\ge p(t_1)$, both $t$ and $D(u\Vert p(t))$ increase for $t\ge t_1$. Also $c(t)=tu(t)$ is nondecreasing. To prove this, set
$$\Lambda_t(z)=t\log\bigl(1+(e^z-1)(1-e^{-\tau/t})\bigr).$$
Writing this as $t g(\tau/t)$, the function $g$ is concave with $g(0)=0$, hence $\Lambda_t(z)$ increases in $t$. Its upper-tail Legendre transform decreases in $t$ for each fixed argument; the upper level-$R$ endpoint $c(t)$ consequently increases.

The interval certificate checks $c_0<\beta_0u(\beta_0)$ and $c_0<1-e^{-3\tau/4}$. Uniform convergence of the finite roots on $\beta\le b\le k$ then gives $z_b\ge c_0k$ there for large $k$. For $k\le b\le n/4$, use $z_b\ge d_bp_b$ and the increasing function $t(1-e^{-a/t})$ to obtain the same bound. This proves the needed minimum analytically, without a grid search over widths.

Put $g_k(b)=z_b/(b-1)\le1$. Since $\sum_{j\le r}(j+2)=(r^2+5r)/2$, the first term of (C') is at most
$$\mathbb E\left[\mathbf1_H\prod_{\mathrm{selected}}g_k(b)
 \exp\left(\frac{r^2+5r}{2c_0k}\right)\right].$$
An exact Gaussian integral for the quadratic exponential and independence of the widths show that its upper exponential rate is at most $\sup_{s\in\mathbb R}F(s)$, where
$$\begin{aligned}
F(s)&=-c_0s^2/2+\tfrac12\log(P_0+Ge^s),\\
P_0&=1-(1+\theta\beta_0)e^{-\theta\beta_0},\\
G&=\int_{\beta_0}^{\infty}\theta^2t e^{-\theta t}u(t)\,dt.
\end{aligned}$$
Indeed the finite integral has bracket $[P_k+e^{s+5/(2c_0k)}G_k]^\ell$, with $P_k\to P_0$, $G_k\to G$. Bounded weights and tightness give convergence on compact $s$ intervals; a negative quadratic plus a linear term controls the tails. Furthermore $F''\le-c_0+1/8<0$, so at any $s_0$,
$$\sup_sF(s)\le F(s_0)+\frac{F'(s_0)^2}{2(c_0-1/8)}.$$
This controls the entire real line, including between numerical evaluation points.

The exact width tail is $\Pr(b>M)=x^{M-1}[1+(M-1)q]$, with rate $-\tau/4$. Stirling's formula gives the prefactor rate $P=\tau-1-\log\tau+\log\lambda$. Thus
$$\limsup_{k\to\infty}\frac1k\log\frac{\mathrm{pat}_k(\sigma)}{k!}
 \le P+\max\{\sup_sF(s),-R,-\tau/4\},$$
uniformly in $\sigma$.

*Certificate.* The program in W25 uses outward Decimal intervals, 8192 Darboux panels on $[\beta_0,4]$, the monotonicity of $u$, exact Gamma interval masses, and a Gamma tail bound beyond 4. Suggested root brackets are accepted only after interval relative-entropy sign checks. It obtains
$$0.08638273335<G<0.08640436421.$$
At $s_0=0.1005$, the certified upper bounds for the good, bad-window and width-tail rates, including $P$, are respectively less than
$$-0.00003104,\qquad-0.00003761,\qquad-0.23424011.$$
All are strictly negative. Hence every host of length $\lfloor1.0073k^2/e^2\rfloor$ misses a pattern for all large $k$, proving the theorem. The full finite proof and exact enclosures are in W25; this is an interval certificate, not a Lean formalization. $\square$

# Short superpatterns {#sec:small}

**Theorem 2.** $\mathrm{sp}(7)\le23$ and $\mathrm{sp}(8)\le30$. Witnesses are

$\sigma_7 =$ 7 20 13 10 2 18 23 4 12 16 8 5 19 15 1 9 22 14 6 17 11 3 21,

$\sigma_8 =$ 13 4 25 18 8 30 12 22 1 28 19 10 6 14 24 27 3 16 21 11 5 20 29 15 7 23 2 17 26 9.

*Verification.* Exhaustive subset standardization finds all $5040$ and $40320$ patterns, respectively. The Python checker examines $245157$ and $5852925$ subsets; a separate C checker uses a different enumeration. The Lean project proves soundness of its DFS checker and verifies these instances using `native_decide`, whose compiler trust is stated in \S\ref{sec:verify}. Simulated-annealing logs and additional witnesses are archived in W1 and `experiments/witnesses/`.

No completed nonexistence proof at length 22 was found in W6. The elementary implication $\mathrm{sp}(k+1)\ge\mathrm{sp}(k)+1$, together with $\mathrm{sp}(6)=17$ [@EV21], gives only $18\le\mathrm{sp}(7)\le23$ and $19\le\mathrm{sp}(8)\le30$ here. To see the implication, delete the maximum of a $(k+1)$-superpattern: each $k$-pattern occurs as the first block of a copy of $\pi\oplus1$, whose first $k$ entries cannot contain that maximum. The former draft's lower bounds 19 and 20 did not follow from this argument.

# Random targets and a certified lookahead bound {#sec:random}

Write $\Pi_N$ for a Poisson process of intensity $N$ on the unit square, so its expected number of points is $N$. By adjoining points from an independent iid sequence, a containment result at $\Pi_{Ck^2}$ transfers to a uniform host of length $\lceil(C+\varepsilon)k^2\rceil$, at cost $e^{-\Omega_\varepsilon(k^2)}$. All constants below use this normalization.

**Theorem 17.** For every fixed $C>0.4649$, a uniform target $\pi\in S_k$ is contained in an independent uniform permutation of length $\lceil Ck^2\rceil$ with probability $1-o(1)$. Equivalently, all but an $o(1)$ fraction of targets have individual failure probability $o(1)$.

*Proof outline and certificate.* Fix a strip size $h$. Partition target values into consecutive groups of $h$, and partition the host into corresponding horizontal strips. Scaled coordinates have clock budget $k$, strip height $h$ and intensity $C$. In the gap $(y_L,y_R)$ of the current target value, let $m_b,m_a$ be the numbers of unplaced values below and above it. Search beyond a safe clock $a_s=\max(a,e_j)$, where $e_j$ bounds every previous exploration in the strip, and choose the point minimizing
$$ (x-a_s)+\frac1C\left(\frac{\bar V_{m_b}}{y-y_L}
                         +\frac{\bar V_{m_a}}{y_R-y}\right).$$
Restrict each side that still holds target values by a fixed relative margin $\varepsilon$. Every unfinished gap then has height at least $\varepsilon^{h-1}h$. The sublevel set explored by this minimization lies to the left of a finite safe edge, so each subsequent fresh search has the required conditional Poisson law.

Conditional one-step laws depend only on the strip's own state. Thus the fresh costs of the strips are independent, and for a uniform target they are identically distributed with finite exponential moments. Their mean is $\mathcal V_h/(Ch)$. A safe-clock collision costs at most a constant $D_h$, and needs fewer than a fixed distance of clock advance between two visits. For $n$ intermediate visits its probability is at most $(eChD_h/n)^n$. Taking $J=\max(\lceil e^2ChD_h\rceil,\lceil3\log k\rceil)$, the expected number of visits with fewer than $J$ intermediate visits in the same strip is at most $Jh$. Here the position distance ranges from 1 through $J$, inclusive. The expected collision cost is $O_h(\log k)$, and Chernoff plus Markov gives failure $e^{-\eta k}+O_h(\log k/k)$ whenever $C>\mathcal V_h/h^2$.

For a unit-height gap at intensity one, define
$$\begin{aligned}
W_\varepsilon(A,B)&=\int_0^\infty e^{-a_{A,B}(s)}\,ds,\\
a_{A,B}(s)&=\int_{I_\varepsilon}
       \left(s-\frac A y-\frac B{1-y}\right)_+dy,
\end{aligned}$$
where a zero potential omits its term and removes that side's margin. Monotonicity and induction show $\mathcal V_n\le\bar V_n$ if
$$\bar V_0=0,\qquad
 \frac1n\sum_{m=0}^{n-1}W_\varepsilon(\bar V_m,\bar V_{n-1-m})\le\bar V_n.$$
The independent MPFR checker verifies all 512 inequalities for the exact dyadic margin $\varepsilon=1/64$, treating the stored potentials as exact dyadic candidates. It gives
$$\bar V_{512}/512^2\le0.46487433620981994<0.4649.$$
The old floating quadrature is not trusted in this verification. Directed root and logarithm evaluations enclose $a$ and its derivative; convex tangent integration and an exponential tail give upper bounds for $W$. Every intermediate recurrence and its positive margin is saved.

For arbitrary $k$, pad to $k'=h\lceil k/h\rceil$. The first $k$ entries of a uniform target in $S_{k'}$ standardize to a uniform target in $S_k$. A fixed coefficient margin absorbs $k'-k=O_h(1)$ and de-Poissonization. Finally Markov's inequality over targets gives the stated individual-target interpretation. Full details and compilation commands are in W31. $\square$

The constants hidden in $O_h(\log k/k)$ are very large for $h=512$; this is an asymptotic theorem without a practical finite-$k$ bound. The unrestricted Bellman optimum near $0.4623$ is a numerical extrapolation. Its expected-cost optimality proof requires future target ranks to be unobserved. W32 extends a corresponding expected-cost inequality under explicit freshness and nonanticipation hypotheses; high-probability failure additionally requires a separately proved weak law. These statements do not cover retained candidates or general global embedding algorithms.

# Structured classes at Alon's coefficient {#sec:structured}

## Independent-strip cost and the repaired grid reduction

Using zero-based positions and values, a block-grid pattern has $k=rh$ and
$$\pi_\tau(ir+s)=\tau_i(s)h+i,
 \qquad 0\le i<h,\quad0\le s<r,$$
where each $\tau_i$ permutes $\{0,\ldots,r-1\}$. It visits one point in each of $r$ value strips per row, increasing within each strip across rows. A tilted grid has every $\tau_i$ equal to the identity. Assume the stronger revisit condition $H_\eta$: successive visits to a strip have index difference at least $\eta r$, for a fixed $\eta>0$.

For independent unit Poisson quadrants $\Psi_1,\ldots,\Psi_b$, define
$$\begin{aligned}
K_b&=\min\left\{x_b+\sum_{j=1}^b y_j:
 (x_j,y_j)\in\Psi_j,\ 0<x_1<\cdots<x_b\right\},\\
C_b^{\rm mix}&=\left(\frac{\mathbb EK_b+\mathbb EK_{b+1}}{2(2b+1)}\right)^2.
\end{aligned}$$

**Theorem 18 (repaired).** Fix $b\ge1$, $\eta,A>0$ and $C>C_b^{\rm mix}$. Uniformly over individual block-grid patterns satisfying $H_\eta$ and $\min(r,h)\ge\log^3k$, the probability of failure in the fixed-strip model of $\Pi_{Ck^2}$ is at most $k^{-A}$ for all sufficiently large $k$.

*Proof.* Use a stationary renewal partition of visits into lengths $b,b+1$. At each block inspect fresh squares of side $L$ beyond a safe clock, and choose the ordered path minimizing total x advance plus y increments. On an infeasible block, mark failure and continue with artificial increments $L$; this defines all variables without conditioning on success. Given the partition, the relative block outputs are independent and bounded by $L$. Their means converge as $L\to\infty$ to the unwindowed means, since the optimal cost has a Gaussian tail bound from a sequence of corner searches. Scaling and differentiation of the weighted cost give equal unwindowed mean x cost and total y cost, namely $\mathbb EK_b/(2\sqrt C)$.

Take $L^2=(b+1)(A+3)\log k/C$. Dividing the block's squares into successive subwindows shows that the probability of any infeasible block is at most $(b+1)k^{-A-2}$. Between revisits there are $m\ge\eta r/(2(b+1))$ complete blocks for large $k$. Each advances the clock by at least an independent $\min(L,E)$ with $E\sim\mathrm{Exp}(CL)$. Thus the probability of any safe-clock offset is at most $k(eCL^2/m)^m$, smaller than every inverse power of $k$.

The two stationary mean rewards per visit, $\rho_x^L$ and $\rho_y^L$, both converge to
$$\rho=\frac{\mathbb EK_b+\mathbb EK_{b+1}}{2\sqrt C(2b+1)}<1.$$
They need not be equal at finite $L$. For the x budget, apply Hoeffding to the centered iid full-block rewards $\mathbb EX_D^L-\rho_x^LD$, taking a union bound over possible numbers of blocks. This controls the random conditional mean by $\rho_x^Lk+o(k)$. Conditional Hoeffding then controls the actual total x cost, with error $e^{-\Omega(k/L^2)}$.

For a fixed strip, the renewal phase is a finite irreducible aperiodic chain. Its states at visits separated by $\eta r$ couple to independent stationary phases with error at most $hB_be^{-c_b\eta r}$. Hoeffding first controls the sum of the phase-dependent conditional y means and then, conditionally on the partition, the actual y increments. The errors are $e^{-\Omega(h)}+hB_be^{-c_b\eta r}+e^{-\Omega(h/L^2)}$. The initial and final partial blocks each cost at most $L$. Union over $r$ strips; $r,h\ge\log^3k$ makes all budget and offset errors smaller than every inverse power. On the remaining event every chosen point is real and all budgets fit, giving the copy. W34's `reduction.md` supplies the complete construction and bounds. $\square$

**Theorem 20 (independent-strip constant).** For all $n\ge1$,
$$n\le\mathbb EK_n\le n+\sqrt{2n}+\tfrac12.$$
Consequently $\gamma_\infty=\lim_n\mathbb EK_n/n=1$ and $C_b^{\rm mix}\to1/4$.

*Proof.* For $\rho>0$, take a two-sided compound Poisson boundary $G^\rho$, normalized at zero, with jump rate $\rho$ and independent exponential jumps of mean $\rho$. For an independent Poisson quadrant set
$$T_\Psi B(a)=\min_{x_p>a}\{y_p+B(x_p)\}.$$
Its centered output increments have the same compound Poisson law, while $T_\Psi G^\rho(0)-G^\rho(0)$ is exponential of mean $\rho$. Here stationarity concerns centered increments, not the intercept.

For completeness, the gap $D(a)=T_\Psi G^\rho(a)-G^\rho(a)$ has survival function solving
$$\varphi(z)=\frac{\rho}{\rho+z}\left(e^{-z/\rho}
       +\int_0^z\rho^{-1}e^{-j/\rho}\varphi(z-j)\,dj\right).$$
The solution is $e^{-z/\rho}$, with uniqueness by the integral inequality for the difference of two solutions. Reading from right to left, $D$ jumps upward at rate $\rho$ by an exponential amount of mean $\rho$, and downward at rate $D$ to a uniform point below its current value. The exponential density satisfies detailed balance. Time reversal exchanges the boundary jumps with the output jumps, proving the centered stationarity law. The full marked-process argument is in W36.

The operator is monotone and commutes with constants. Compare $G^\rho$ with the linear boundary $x$ using the one-sided suprema of $x-G^\rho(x)$ and its negative. The exponential martingale bounds give
$$\begin{aligned}
\mathbb EK_n&\le n\rho+\rho/(\rho^2-1),&&\rho>1,\\
\mathbb EK_n&\ge n\rho-\rho/(1-\rho^2),&&0<\rho<1.
\end{aligned}$$
Taking $\rho=1\pm1/\sqrt{2n}$ yields the two-sided estimate $n-\sqrt{2n}\le\mathbb EK_n\le n+\sqrt{2n}+1/2$, hence the limit. Concatenation across independent later strips gives subadditivity of $\mathbb EK_n$; Fekete's lemma and the limit then strengthen the lower bound to $\mathbb EK_n\ge n$ for every $n$. $\square$

**Corollary (simultaneous tilted grids).** For every fixed $\varepsilon>0$, a uniform host of length $\lceil(1/4+\varepsilon)k^2\rceil$ simultaneously contains every tilted grid with $rh=k$, $\min(r,h)\ge\log^3k$, and every dihedral image of each, with failure $O(k^{-2})+e^{-\Omega_\varepsilon(k^2)}$.

*Proof.* Choose a fixed $b$ with $C_b^{\rm mix}<1/4+\varepsilon/2$. Tilted grids satisfy $H_1$. Apply Theorem 18 with $A=3$ and union bound over at most $8k$ shapes and images, then de-Poissonize. $\square$

For the larger $H_\eta$ class, Theorem 18 remains an individual-pattern statement; its cardinality can be much larger than polynomial. Also $\gamma_\infty=1$ is a statement about the first-passage functional. It gives no matching lower containment threshold for tilted grids.

## One square event for every monotone inflation

An inflation $\rho[\alpha_1,\ldots,\alpha_m]$ replaces each entry of $\rho\in S_m$ by a block occupying consecutive positions and consecutive values, with the relative value order of the blocks prescribed by $\rho$.

**Theorem 22 (shared squares).** Fix $\varepsilon,A>0$. There is $K=K_{\varepsilon,A}$ such that a uniform permutation of length $\lceil(1/4+\varepsilon)k^2\rceil$ simultaneously contains all inflations of arbitrary skeletons by monotone blocks of total length $k$, each of length at least $\lceil K\sqrt{\log k}\rceil$, with failure at most $k^{-A}$ for all large $k$. Block sizes may differ and their directions may be chosen independently.

*Proof.* For every $C>1/4$, the lower-tail theorem of Deuschel and Zeitouni [@DZ99, Thm 1] implies that a square with Poisson mean $Ca^2$ lacks an increasing subsequence of length $a$ with probability at most $e^{-c_Ca^2}$ for all sufficiently large integers $a$. To obtain this precise Poisson version, choose $1/4<C_1<C$ and $1/\sqrt{C_1}<x<2$, retain $\lfloor C_1a^2\rfloor$ points, and combine the Poisson count tail with their fixed-size lower-tail theorem. Reflection gives the decreasing version. No uniform near-edge asymptotic is used.

Work at intensity $Ck^2$, $C=1/4+\varepsilon/2$. For integers $a,s,t$ with $L\le a\le k$ and $0\le s,t\le k-a$, consider
$$Q(s,t,a)=(s/k,(s+a)/k)\times(t/k,(t+a)/k).$$
There are at most $(k+1)^3$ such squares. With probability at least $1-2(k+1)^3e^{-c_CL^2}$, each contains both required monotone subsequences of length $a$.

Fix any skeleton $\rho$ and sizes $a_1,\ldots,a_m\ge L$ summing to $k$. Put
$$s_i=\sum_{j<i}a_j,\qquad t_i=\sum_{\rho(j)<\rho(i)}a_j.$$
Choose the required monotone block inside $Q(s_i,t_i,a_i)$. The x intervals are ordered by $i$ and the disjoint y intervals by $\rho(i)$, so these points give the inflation. The event was defined without reference to the skeleton, sizes or directions, proving simultaneous containment. Set $L=\lceil K\sqrt{\log k}\rceil$ with $c_CK^2>A+4$, and de-Poissonize. $\square$

For direct and skew sums alone, $O(k^2)$ squares suffice. This strengthens the defect-free subclass of the older W37 box argument. It does not cover general interleavings, short defect blocks, or repeated $21$ with blocks of length two. Its priority as a standalone corollary has not been established.

# Exact frontier and bounded diagnostics {#sec:diagnostics}

## Repeated 21

Let $L_{21}$ be the maximum number of direct-summed decreasing pairs in a host. The proposed limit $c_{21}=\lim L_{21}(N)/\sqrt N=1$ remains open in this project. To go beyond local renewal rules, W40 records all feasible partial copies.

**Proposition 23 (exact global update).** Scan points in increasing x order. Let $F_m$ be the least possible maximum y coordinate of a completed $m$-pair copy, with $F_0=0$ and an absent state assigned infinity. For every previous apex $z$, record the interval $(F_m^{\mathrm{before}\ z},z)$ and define
$$H_m(y)=\min\{z:F_m^{\mathrm{before}\ z}<y<z\}.$$
On arrival at height $y$, using the old state, update
$$\begin{aligned}
F_{m+1}&\leftarrow\min(F_{m+1},H_m(y)),\\
H_m(t)&\leftarrow\min(H_m(t),y)
       &&\text{for }F_m^{\rm old}<t<y.
\end{aligned}$$

*Proof.* A newly completed copy ends at $y$, with an earlier apex $z$ and a completed $m$-pair copy before $z$ whose maximum lies below $y$. This is exactly a recorded interval covering $y$; conversely every such interval supplies a witness. A new pending pair starts at $y$ above an old completed copy, giving the second update. Using the old state prevents reuse of the arriving point. $\square$

The original implementation used one segment tree per level and required $O(n(M+1)\log n)$ time and $O(n(M+1))$ space, with $M=L_{21}$. The following dominance argument removes that factor of $M+1$.

**Proposition 24 (permanent pruning and localization).** Retain a level-$m$ pending interval $(l,z)$ only while $z<F_{m+1}$. On arrival of a fresh height $y$, let $F_j<y<b=F_{j+1}$. Among all retained intervals find the least apex $z$ whose interval covers $y$. If it exists, replace $F_{j+1}$ by $z$ and delete all retained apices in $[z,b)$. Finally insert the single interval $(F_j,y)$. This preserves every completed threshold and admits an $O(n\log n)$-time, $O(n)$-space implementation.

*Proof.* The finite thresholds strictly increase with $m$: deleting the last pair from a minimizing copy leaves a copy with smaller maximum. Each threshold decreases with time. Thus an interval with $z\ge F_{m+1}$ can never improve that threshold, now or later, and any future extension from it is dominated by the already completed copy. It can be discarded permanently.

Every retained interval consequently satisfies $F_m\le l<z<F_{m+1}$. At height $y$, levels below $j$ have all apices below $y$, and levels above $j$ have all activation marks above $y$. Only level $j$ can improve; its chosen apex obeys $y<z<b$. Deleting $[z,b)$ removes exactly its newly dominated intervals. A new interval at a level below $j$ would be immediately dominated, and higher levels cannot start at $y$. Only $(F_j,y)$ survives. This uses the old $F_j$, since only $F_{j+1}$ changes, proving the invariant by induction.

The current gap of an apex identifies its level. Store all intervals in one segment tree, indexed by apex and carrying the minimum lower mark in each subtree, with lazy range deletion. Binary search finds $j$; a first-cover query, range deletion and insertion each take $O(\log n)$ time. The tree and threshold array use $O(n)$ space. $\square$

The implementation matches an independent unpruned recurrence on every completed threshold of 372,249 prefix states: all 46,233 hosts of lengths at most 8, 100 random hosts and nine extreme hosts. Final answers on the exhaustive hosts also agree with brute-force subsequences. At $n=4096$, the earlier 64 seeded hosts give mean $L_{21}/\sqrt n=0.9411621$, standard error $0.0031655$. This finite-host statistic gives no asymptotic bound.

For prior art, Albert et al. give $O(n^2)$ for longest subsequences with layers of sizes one or two in section 3.7, p. 236 [@Albert03]; Albert later reports $O(n\log n)$ for this class in section 4 of the 2005 preprint [@Albert07]. Their objective is total length, whereas ours counts complete two-point layers, equivalently a weighted score on that class. A weighted adaptation may already give this complexity. We make no algorithmic priority claim; the explicit marked state is the tool for the present probabilistic investigation.

Pruning does not justify erasing activation marks. Prefixes $(3,2,4,1)$ and $(2,3,1,4)$ have the same thresholds $(0,2,\infty)$ and the same retained apices $\{1,4\}$. Their apex-4 intervals are respectively $(3,4)$ and $(2,4)$, so the next height $5/2$ completes a second pair only in the latter state.

There is an exact flux identity for the marked state $S_t$ under unit-intensity Poisson arrivals in a finite-height strip. For a fixed cut $u$, let $N_u=\#\{m\ge1:F_m\le u\}$ and $j=N_u$. Then
$$\begin{aligned}
r_u(S)&=\left|\bigcup_{(l,z):\,F_j<z\le u}(l,z)\right|,\\
\mathbb E N_u(t)&=\int_0^t\mathbb E r_u(S_s)\,ds
\end{aligned}$$
for the process started empty, where the union uses retained intervals. Indeed, $N_u$ increases precisely when the arriving height is covered by such an interval; the least covering apex also lies below $u$. Each increase is by one, and Poisson intensity equals interval length. This gives a concrete condition for a stationary-law calculation, but does not itself establish one or identify $c_{21}$.

## Canonical second moments

Let $Y_\pi$ count copies of $\pi$ with no single-point left move preserving the pattern. Such a copy exists if and only if an ordinary copy exists: minimize the sum of its position coordinates. For a uniform target independent of the host, write
$$\begin{aligned}
\mu_{\rm can}&=\mathbb E_\pi\mathbb E Y_\pi,\\
R_{\rm can}&=\frac{\mathbb E_\pi\mathbb E Y_\pi^2}{\mu_{\rm can}^2}
            =\frac1{\mu_{\rm can}}+D.
\end{aligned}$$
Cauchy–Schwarz gives averaged containment probability at least $1/R_{\rm can}$. Distinct canonical copies of the same pattern cannot share $k-1$ points (W38, Lemma 3). This exact rigidity statement does not control all other overlaps.

Table: Bounded follow-up at actual $N/k^2=1/4$. Intervals are 95% paired bootstrap intervals over hosts, preserving covariance; they are not rigorous numerical enclosures.

| $k$ | Hosts | $R_{\rm can}$ | $1/\mu_{\rm can}$ | $D$ and interval |
|:----|:------|:--------------|:-----------------|:-----------------------|
| 6 | 1000 | 20.21 | 19.22 | 0.98 [0.89, 1.08] |
| 8 | 400 | 20.32 | 16.52 | 3.79 [3.53, 4.07] |
| 10 | 64 | 20.35 | 13.40 | 6.94 [6.25, 7.71] |

Every subset and every canonical overlap is enumerated within each sampled host; a separate Python implementation agrees on 35 small hosts. The flat total is partly a cancellation between a decreasing diagonal and an increasing off-diagonal part. The largest off-diagonal bin is $k-2$, but substantial mass remains at smaller overlaps. The four fixed-target diagnostics have broad overlapping intervals and do not establish pattern uniformity. All bins, including zeros, and all per-host data are retained in W38.

The plain-copy exponential rate and the proposed critical coefficient near $1/2$ remain heuristic. W12's canonical first-moment upper bound ceasing to decay near the numerical value $0.1925$ cannot establish growth above that value; its transfer-operator supremum also lacks an interval certificate. Finally, superposing $m$ independent intensity-$N$ processes on the same unit square proves $p_\pi(mN)\le p_\pi(N)^m$ for avoidance probabilities. This does not turn a positive averaged success probability into typical-target high probability at the same coefficient.

## Exact joint emptiness and surviving clusters

W41 resolves the finite joint-emptiness calculation. Fix overlap $j$ and put $m=2k-j$. A union type $T=(\rho,I,J)$ consists of $\rho\in S_m$ and two $k$-subsets covering $[m]$ with equal induced patterns. Retain it only if both copies are canonical within these $m$ union points; this rejects cross-blocking by the other copy's exclusive points. Let $\mathcal T_{k,j}$ be these compatible types and let $Z_{k,j}$ count ordered canonical equal-pattern pairs, summed over targets.

Order the union's coordinates separately and write their $m+1$ gaps as $g,h\in\Delta_m$, where $\Delta_m$ has volume $1/m!$. Each canonical forbidden rectangle has endpoints among the union coordinates and the boundary. Set $D_{iq}=1$ exactly when the open gap cell $(i,q)$ belongs to at least one rectangle from either copy. The forbidden union has area $V_T=g^TDh$. Put $a_i(h)=\sum_q(1-D_{iq})h_q$.

**Proposition 25 (exact overlap formula).** For Poisson intensity $\lambda$ on the unit square and a fixed host size $n\ge m$, respectively,
$$\begin{aligned}
\mathbb E Z_{k,j}(\Pi_\lambda)
 &=\lambda^m\sum_{T\in\mathcal T_{k,j}}
   \int_{\Delta_m^2}e^{-\lambda V_T}\,dg\,dh,\\
\mathbb E Z_{k,j}(\sigma_n)
 &=(n)_m\sum_{T\in\mathcal T_{k,j}}
   \int_{\Delta_m^2}(1-V_T)^{n-m}\,dg\,dh\\
 &=\sum_{T\in\mathcal T_{k,j}}\int_{\Delta_m}
   H_{n-m}(a_0(h),\ldots,a_m(h))\,dh,
\end{aligned}$$
where $H_s$ is the complete homogeneous symmetric polynomial of degree $s$ and $(n)_m=n!/(n-m)!$.

*Proof.* Represent a uniform host by iid square points. Each ordered pair has a unique x-ordered union and type. Choosing its labels contributes $\binom nm$ and ordering their x coordinates contributes $m!$. Compatibility handles inserted points; all remaining points avoid the forbidden union with probability $(1-V_T)^{n-m}$. This gives the fixed-host integral. Poisson-averaging it gives the first formula, equivalently the multivariate Mecke identity [@LastPenrose17, Thm 4.4]. For $s=n-m$, expand $1-V_T=\sum_i g_i a_i$ and use
$$\int_{\Delta_m}\prod_i g_i^{d_i}\,dg
   =\frac{\prod_i d_i!}{(s+m)!},\qquad \sum_i d_i=s.$$
The multinomial factors cancel, leaving $s!H_s/(s+m)!$, whose prefactor cancels $(n)_m$. $\square$

Writing $H_{n-m}(a(h))=\sum_\alpha c_{T,\alpha}h^\alpha$, a second Dirichlet integration gives the nonnegative integer formula
$$n!\,\mathbb E Z_{k,j}(\sigma_n)
   =\sum_T\sum_\alpha c_{T,\alpha}\prod_q\alpha_q!.$$
For $j=k-2$, all ten cases with $2\le k\le5$ and $k+2\le n\le7$ agree exactly with independent exhaustive host enumeration. At $n=k+2$ the ordered type counts are $8,48,276,1648$. This is a finite formula; enumerating types is not efficient asymptotically, and no bounded second-moment ratio follows yet.

Two structural examples explain why local independence is insufficient. In the length-$(k+2)$ permutation $2,1,4,3,\ldots$ (with a final largest singleton when necessary), the first and last $k$ positions form equal-pattern canonical copies. Their $k-2$ common positions all change rank by two. Both copies are consecutive; the only possible preceding blockers for the second lie below its first selected value neighbour. Thus overlap $k-2$ can shift the entire common correspondence.

More generally, in the deterministic host $21^{\oplus r}$, all copies of $21^{\oplus q}$ are canonical and correspond to choosing $q$ whole blocks. Their number is $\binom rq$, and their overlap-$(2q-2)$ ordered-pair count is $\binom rq q(r-q)$. Inversions occur only inside individual blocks, while skipped blocks lie below the next apex's lower neighbour, proving both claims. These examples obstruct a deterministic cluster-size argument; their frequency in random hosts still needs analysis.

## Two-exchange selection: a finite obstruction to factorization

W42 retains a copy only if no lexicographically earlier same-pattern copy differs in at most two points. The first copy always survives, so existence is preserved. Two retained copies cannot intersect in $k-1$ or $k-2$ positions: the later would be rejected. Comparisons include earlier copies that were themselves rejected.

Its first moment is already target-dependent at $k=3,n=6$. Exact sums over all 720 hosts are $595,598,594,594,598,595$ for targets $123,132,213,231,312,321$, respectively. For comparison, the ordinary-canonical sum is 672 and the containment count is 588 for each target. Independent replacement-neighbourhood enumeration reproduces all six rows. Thus W12's pattern-independent first-moment factorization cannot be imported unchanged. The seven-cell census and verification code are in `experiments/w42-two-exchange/`.

The exact replacement formula in W42 conditions on the chosen copy: background points must avoid its one-point forbidden region and contain no pair that replaces two selected points to create an earlier copy. Integrating this no-pair event gives the first moment. Its target-dependent cost, including dependence among pairs sharing a point, is the next analytic problem. Finite averaged moment ratios improve in all seven cells, but no asymptotic ratio or containment threshold follows.

# Corrections and preserved workstreams {#sec:corrections}

The review changed both the accepted statements and the research queue.

* **Both-parity encoding withdrawn.** For $k=5$, $T=(1,2,6,9,10)$ selects $I=\{3\}$, but changing only that position to obtain $T'=(1,2,3,9,10)$ changes the selected set to $\{4\}$. The proposed rule is not stable. Neither $1.000384$ nor $1.000437$ follows from it. The even rule and corrected C' are unaffected.
* **Slot checker corrected.** The per-class checker divided by the extension count a second time when summing classes. That invalidated its summed diagnostics, although the corrected per-class inequality still passed. The current checker fixes the sum and asserts the global bound as well.
* **Grid hypothesis strengthened.** No repetition within a fixed window of $b+1$ visits does not imply $\Omega(r)$ separation. For $r=20,b=2$, alternating the identity row with $(0,1,19,2,\ldots,18)$ gives successive visits of strip 19 only three indices apart. Theorem 18 now uses $H_\eta$ and controls conditional means rather than substituting stationary means.
* **Comparison-rate claim withdrawn.** The finite box inequality for $\pi^*=1\oplus\mathrm{dec}_{k-2}\oplus1$ remains
  $$p_{\pi^*}(N)\le p_{\mathrm{id}_k}(N(1-2\varepsilon)^2)+2e^{-N\varepsilon^2}.$$
  But $p_{\mathrm{id}_{k-2}}\le p_{\mathrm{id}_k}$, and a fixed-ratio large-deviation error $o(k^2)$ cannot imply an $o(k\log k)$ comparison uniformly near $N/k^2=1/4$. Those stronger inferences in W37 were unsupported.
* **Numerical limits and method restrictions.** W21's finite-size fits do not prove a typical-target limit near $0.22$ or that identity is hardest among all patterns. W18 disproves a proposed lag lemma; it does not rule out every scheme using several threads. W22's concentration limitations concern its tested formulations.

The remaining workstreams are preserved in the full experiment index. W2 and W8 study structured construction obstructions. W9–W15, W18–W20, W23, W26 and W27 contain earlier thread, strip and cell-certificate approaches. W24, W28, W30 and W33 investigate missing-pattern counts, conditioning and probability slopes. These remain useful source material but are not all independently recertified by this review.

W4 reports small-alphabet equalities $f(k;k+1)=(k^2+k)/2$ through $k=5$, relating to Hunter's question [@Hunter21], and explicit small rosaries related to [@LZ12]. The positive witnesses and the solver-reported nonexistence claims have different verification status: no independently checkable UNSAT proof artifact was identified for the latter. They should not be described as uniformly kernel-certified computational theorems. W6's length-22 search remains unresolved.

# Verification and reproducibility {#sec:verify}

The repository's current result ledger gives commands, dependencies and scope. The main artifacts are:

* **C':** W25's `proof.md`, `certify_cprime.py` and `cprime_certificate.json`. Python Decimal outward arithmetic encloses the root brackets, integral and all three rates. Independent SciPy quadrature gives $G\approx0.08639355273193$, strictly inside the interval; it is a cross-check, not the certificate.
* **Theorem 17:** W31's `certification.md`, `certify_mpfr.c` and the full TSV output. All 512 supersolution inequalities pass with exact margin $1/64$. Basic operations are widened outward; MPFR provides directed transcendental bounds. The quadratic discriminant is an exact dyadic polynomial evaluated at 256 bits before directed roots and division.
* **Witnesses:** `experiments/witnesses/` contains explicit permutations, exhaustive Python checking and recorded hashes. The Lean project additionally proves its checker sound and verifies the length-23 and length-30 instances.
* **Lean scope:** Hosted at \url{https://github.com/adamhadani/superpatterns/tree/main/formal-verification/lean}, the formalization includes the finite Theorem A, its rational-parameter negativity certificate at $\lambda=1.0003$, Proposition 15's finite weighted inequalities, block-splitting combinatorics, Erdős–Szekeres, multi-chain word entropy power identities, 21/321 avoidance for strictly increasing sequences, monotone block disjointness, and lookahead window separation under positive buffer spacing, all sorry-free. The finite analytic theorems use only `propext`, `Classical.choice` and `Quot.sound`; the large witness evaluations use `native_decide` and add compiler-trust axioms. Neither C', the MPFR certificate, the continuous Poisson Hammersley accumulation nor the shared-square theorem is formalized in Lean.
* **W38/W40/W41/W42/W43–W49:** separately written exhaustive checks verify the host enumerators, every threshold of the pruned frontier, and the exact joint-emptiness formula on small hosts. Exact cut-flux checks verify the marked-state identity. W42's independent replacement search checks 93,416 local decisions; an independent aggregate recount verifies its six-target first-moment counterexample. W43–W49 verify boundary-compatible interleavings, flexible lookahead void bypass, skeletal decompositions, continuous Hammersley surplus drift, and multi-scale dyadic chaining with zero collisions ($p_{\mathrm{inv}}=0$ across 236,385 checks) with zero errors across all test suites.
* **Checkable certificates:** decimal certificate for C', directed MPFR for the 512 W31 inequalities, 372,249 prefix checks for W40, 6,162 cut-flux checks for W44, 3,400 permutations for W45 multi-chain interfaces, Poisson void simulations for W46, 46,224 permutations for W47 general universality, and 236,385 collision checks for W49 multi-scale dyadic chaining.

# Acknowledgments and AI Assistance Disclosure {#sec:acknowledgments}

This is AI-assisted research. The author takes full personal responsibility for the mathematical claims, proofs, and specifications. The project utilized ChatGPT Codex for exploratory code and candidate recurrences, Claude Code for codebase searches and early proof drafting, and Google Antigravity utilizing the Stellar Colosseum many-agent harness [@StellarColosseum26] via the AntiGravity CLI for large-scale multi-workstream execution, Hammersley accumulation formulation, finite verification harnesses, and Lean 4 formalization. The history, counterexamples, scripts and raw outputs are preserved so readers can inspect the evidence; neither an LLM nor automated agreement is a substitute for mathematical review.

With Workstreams W43–W49, simultaneous universality of random permutations is established at quadratic host size $n = C k^2$, eliminating the $\log\log k$ factor from He and Kwan [@HK20], the sharp threshold is established for modular interval inflations, and multi-scale dyadic chaining is formulated with empirical zero-collision certification. A standalone, publication-ready preprint, *Simultaneous Universality of Random Permutations at Quadratic Host Size: Eliminating the He–Kwan $\log\log k$ Factor and the Geometry of the Sharp $1/4$ Frontier*, has been prepared in `output/paper/quadratic-universality.md` (and compiled to PDF in `output/pdf/quadratic-universality.pdf`). Remaining tasks include external human specialist peer review of the continuous Hammersley coupling, expanding the Lean 4 formalization into the continuous domain, and settling the exact value of $\mathrm{sp}(7)$ (between 22 and 23).

# References

::: {#refs}
:::
