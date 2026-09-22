# Corrected C′: a certified deterministic coefficient 1.0073

10 September 2026. This proof supersedes the asymptotic justification of C′ in
`review.md` and the C′ addendum in W7. It uses only the even-index stable rule.
The certificate is `certify_cprime.py`, with output `cprime_certificate.json`.
The result is not formalized in Lean and does not specify an effective k₀.

**Theorem.** For all sufficiently large k,

    sp(k) > 1.0073 k²/e².

The published comparison is Chroman–Kwan–Singhal's coefficient 1.000076
(JCTA 182, 2021, 105467; arXiv:2004.02375). This establishes a coefficient
increment 0.007224 over that bound. The optimized value approximately
1.0073384 remains numerical; rounding it up to 1.00734 is not justified.

## 1. A finite inequality with a valid width domain

Fix σ∈S_n, k≥3, x∈(0,1), q=1−x, ℓ=floor((k−1)/2), and integers
3≤β≤M≤n−2. For T=(t₁<...<t_k), select precisely the even indices i for
which b_i=t_(i+1)−t_(i−1)≥β. The rule is stable because all its inputs
are odd-indexed positions. The corrected slot-encoding lemma of W7 gives

    pat_k(σ) ≤ Σ_T W(T),
    W(T) = min(1, Π_(j=1)^r min(M_(i_j)(T)+j−1,k)/(b_(i_j)−1)).             (1)

Here M_i counts the distinct slots of the values in the open position window
relative to the off-I values. To recall the counting step: a class with fixed
off-I positions has exactly Π(b_i−1) extensions. Its distinct patterns number
at most min(Π_j min(M_(i_j)+j−1,k), Π_j(b_(i_j)−1)); sum this bound over
classes, or divide by the extension count and sum over T. Do not divide
again when already summing over classes.

Let B be independent Bernoulli(q) sites on the positive integers, let T(B)
be its first k points, and set W(T(B))=0 if t_k>n. Only B∩[n] is used when
forming value sets through σ. Since P(T(B)=T)=q^k x^(t_k−k),

    pat_k(σ) ≤ A(n,k,x) E W(T(B)),
    A(n,k,x) = x^(−n−1) (x/q)^(k+1).                                    (2)

The ℓ even widths are independent with

    P(b)=(b−1)q²x^(b−2), b≥2.

For a fixed window (lo,hi) of width b≤M, its internal values in sorted
order determine b−2 disjoint sets A_j of external positions, with
Σ|A_j|≤n−b−1. The number S of gaps hit by B is the sum of independent
Bernoulli variables of probabilities 1−x^|A_j|, independent of B∩[lo,hi].
Adding the two endpoint values shows M_i≤S+3.

Set d_b=b−2 and p_b=1−x^((n−b−1)/d_b). For z≥0 the function

    f_z(a)=log(e^z−(e^z−1)x^a)

is increasing and concave in a≥0. Jensen and the bound on Σ|A_j| imply
E exp(zS)≤(1−p_b+p_b e^z)^d_b. Consequently, if p_b≤u≤1,

    P(S>d_b u) ≤ exp(−d_b D(u||p_b)),                                   (3)

with the usual Bernoulli relative entropy D; for u=1 the probability is zero.

Choose any R>0. If d_b log(1/p_b)>Rk, let u_b∈(p_b,1) solve
d_b D(u_b||p_b)=Rk; otherwise let u_b=1. Set z_b=d_b u_b. Thus
P(S>z_b)≤exp(−Rk), including the capped case. All quantities are defined
only for β≤b≤M; no negative slot means at unbounded geometric widths occur.

Let H={all even widths≤M}. On H and when every selected S≤z_b, (1) is
at most min(1,Π_j min(z_(b_j)+j+2,k)/(b_j−1)). Outside the good event use
0≤W≤1. A fixed window has endpoints in B and exactly one internal site
with probability q P(b). Independence from its external gap hits and a
union bound over ℓ indices and at most n windows of each width give

    E W ≤ E[1_H Π_(j=1)^r (z_(b_j)+j+2)/(b_j−1)]
          + ℓ n q exp(−Rk) + ℓ P(b>M).                                 (4)

This upper bound drops the caps only in its first, nonnegative term. It is
valid for every σ; the union bound does not condition the external sites on
their order statistics.

## 2. The limiting quantile and two monotonicity facts

Fix rational parameters

    λ=1.0073, τ=0.96813, β₀=0.53692, R=0.00783, c₀=0.4805,
    n=floor(λk²/e²), θ=τe²/λ, x=exp(−θ/k),
    β=ceil(β₀k), M=floor(n/4).

For t≥β₀ define p(t)=1−exp(−τ/t), and let u(t)>p(t) solve
tD(u(t)||p(t))=R. The certificate verifies R<β₀ log(1/p(β₀)); since
t log(1/p(t)) increases, the root exists and is below 1 for every t≥β₀.

**Lemma.** u(t) is nonincreasing, and c(t)=t u(t) is nondecreasing.

For the first assertion, p(t) decreases. For a fixed u≥p(t₁), both t
and D(u||p(t)) increase on t≥t₁, so the upper root cannot increase.

For the second assertion define Λ_t(z)=t log(1+(e^z−1)p(t)), z≥0.
Writing g(v)=log(e^z−(e^z−1)e^(−v)), we have g(0)=0 and g concave, so
d[t g(τ/t)]/dt=g(τ/t)−(τ/t)g′(τ/t)≥0. Therefore the upper-tail rate
I_t(c)=sup_(z≥0){zc−Λ_t(z)} is nonincreasing in t for each c. Its upper
level-R endpoint c(t) is consequently nondecreasing. ∎

The certificate establishes c₀<β₀u(β₀) by testing
β₀D(c₀/β₀||p(β₀))<R and c₀/β₀>p(β₀). It also verifies

    1−exp(−3τ/4)>c₀.                                                    (5)

It follows that z_b≥c₀k uniformly for β≤b≤M, for all sufficiently large
k. Indeed on β≤b≤k, the finite quantile z_b/k converges uniformly to
c(b/k); the limiting root stays strictly inside its domain on this compact
interval. Its minimum exceeds c₀ by the lemma and the strict certificate.
For k≤b≤n/4, use z_b≥d_b p_b. Writing t′=(b−2)/k,

    d_b p_b/k ≥ t′[1−exp(−(3τ/4−o(1))/t′)]
              ≥ 1−exp(−3τ/4)−o(1)>c₀,

because t′≥1−2/k and t↦t(1−exp(−a/t)) is increasing. This proves the
required minimum without assuming a numerical grid finds every minimum.

## 3. The good-event rate, with control of the whole supremum

Put g_k(b)=z_b/(b−1) for β≤b≤M. Using z_b≥c₀k and
Σ_(j=1)^r(j+2)=(r²+5r)/2, the first term of (4) is bounded by

    E[1_H Π_selected g_k(b) exp((r²+5r)/(2c₀k))].                         (6)

Use the exact Gaussian integral identity for exp(r²/(2c₀k)) and independence
of the even widths. With P_k=P(b<β) and G_k=Σ_(b=β)^M P(b)g_k(b), (6) is

    ≤ sqrt(c₀k/(2π)) ∫_R exp(−c₀k s²/2)
         [P_k+exp(s+5/(2c₀k))G_k]^ℓ ds.                                (7)

The scaled width b/k converges to the law with density θ²t exp(−θt).
Since 0≤g_k≤1, compact convergence and tightness give

    P_k → P₀=1−(1+θβ₀)exp(−θβ₀),
    G_k → G=∫_(β₀)^∞ θ²t exp(−θt)u(t) dt.

The limit of the upper exponent in (7) is bounded by sup_s F(s), where

    F(s)=−c₀s²/2+(1/2)log(P₀+G exp(s)).

This passage is uniform on compact s intervals, and the tails are controlled
by a quadratic plus a linear term, since P_k,G_k≤1. Alternatively the
finite exponent has second derivative at most −c₀+ℓ/(4k)<−c₀+1/8,
which gives an integrable Gaussian upper bound about its unique maximizer.
In particular,

    limsup (1/k)log(good term) ≤ sup_(s∈R) F(s).                          (8)

For all real s, F″(s)≤−κ, where κ=c₀−1/8>0. At any chosen s₀,

    sup_s F(s) ≤ F(s₀)+F′(s₀)²/(2κ).                                   (9)

Thus certifying a single value and derivative, together with the analytic
curvature bound, controls the global supremum. No finite grid of s values
is used as a substitute for a continuous maximum.

## 4. Bad windows, width tail, and certificate

The second term of (4) has rate at most −R. The exact geometric-pair tail is

    P(b>M)=x^(M−1)[1+(M−1)q],

whose log divided by k tends to −τ/4. Finally Stirling in (2) gives

    (1/k)log(A(n,k,x)/k!) → P=τ−1−log τ+log λ.

Consequently the uniform upper rate for pat_k(σ)/k! is at most

    P + max(sup_s F(s), −R, −τ/4).                                     (10)

`python3 experiments/w25-asymptopia-review/certify_cprime.py` encloses
P₀ and G using outward Decimal intervals. It partitions [β₀,4] into 8192
panels. On each panel, the monotonicity of u gives lower and upper Darboux
bounds, multiplied by the exact Gamma interval mass. The omitted tail is
bounded by P(b/k≥4) in the limiting law, since 0≤u≤1. All root brackets are
checked by interval KL evaluations. Binary floating calculations only
suggest brackets and are not trusted for any proof inequality. Equation
(9) is evaluated at s₀=0.1005. Each of the three rates in (10) is verified
to be less than −0.00001; exact enclosures are saved in the JSON output.

Thus pat_k(σ)<k! for every σ∈S_floor(1.0073k²/e²), for all sufficiently
large k. Any shorter superpattern could be extended to this length, which
would contradict the same statement. Since sp(k) is an integer, this
proves the theorem. ∎

**Verification scope.** The counting lemma and every reduction above were
re-derived in the coordinating session. The certificate uses Python's
specified correctly rounded Decimal elementary functions and outward
arithmetic; it is not a machine-checked formalization of this proof. An
independent SciPy quadrature/root computation gave G≈0.08639355273193
and an optimized good rate approximately −3.75·10⁻⁵ before conservative
enclosure. Fixed-k floating DP outputs are historical cross-checks, not
the justification for the all-sufficiently-large-k statement.
