# W36 — γ_∞ = 1: exact solution of the cross-strip first-passage functional (Burke property)

Date 2026-08-30.  Tags PROVED / NUMERICAL as marked.  Background: W34 proof.md §2 (the round problem
(2.1), backward recursion (2.2), scaling Lemma 2.2, Theorem 3.4 = paper Theorem 18(a)); W20 (Theorem 12);
W11 §4 (Theorem 10).  Numerics: verify.py, results.md.  Chronology: log.md.

**Summary.**  Let Ψ_1, …, Ψ_n be independent Poisson processes of intensity 1 on (0,∞)² and

    K_n := min { x_n + Σ_{s=1}^n y_s :  p_s = (x_s, y_s) ∈ Ψ_s,  0 < x_1 < x_2 < ⋯ < x_n }.          (0.1)

W34 conjectured (numerically, ±0.002) that γ_∞ := lim E K_n / n = 1.  We prove (Theorem 3.3)

    n − √(2n)  ≤  E K_n  ≤  n + √(2n) + 1/2      for every n ≥ 1,                                   (0.2)

hence γ_∞ = 1 exactly, with the explicit finite-n error |γ_n − 1| ≤ √(2/n) + 1/(2n).  The proof is a
Burke-type stationarity argument for the backward recursion G_s(a) = min_{p∈Ψ_s, x_p>a}[y_p + G_{s+1}(x_p)]:
the compound Poisson boundary functions G^ρ (jumps at rate ρ, i.i.d. sizes Exp(1/ρ), so slope ρ²) are
*exactly stationary* under one strip step, the increment G_s(0) − G_{s+1}(0) of the stationary system is
Exp(1/ρ) with mean ρ (§2), and the true boundary G_{n+1}(x) = x is sandwiched between the stationary
boundaries with ρ² ≷ 1 up to a sup of a Lévy process with negative drift (§3).  This is the analogue of
Aldous–Diaconis's sources/sinks stationarity for Hammersley's process (source density ρ ↔ sink density
1/ρ; here jump rate ρ ↔ jump mean ρ).

Consequences (§4): the constants of paper Theorem 18 satisfy C_b, C^{mix}_b → 1/4 (with certified
finite-b bounds), so every tilted grid / block-grid pattern π_τ ∈ 𝒢(r,h) satisfying Theorem 18's
no-revisit hypothesis (H_b), with min(r,h) ≥ (ln k)³, is contained in Π_{(1/4+ε)k²} — and hence in a
uniform random permutation of length (1/4+ε)k² — w.h.p., for every ε > 0 (Theorem 4.1, PROVED).  This is
the first non-monotone family with threshold constant ≤ 1/4 = Alon's constant; the matching *lower*
bound ≥ 1/4 is NOT available (the paper's only lower bound valid for these patterns is the universal
0.1925k²), see §5.  What is exact is the mean-field fixed-strip full-lookahead constant: γ_∞²/4 = 1/4.

## 0. Setting, conventions

All point processes are Poisson of intensity 1 (Lebesgue) unless stated.  "Jump process", "step
function": right-continuous, nondecreasing, finitely many jumps on bounded intervals.  For a function
B: (0,∞) → [0,∞] (the *boundary*) and a Poisson process Ψ on ℝ × (0,∞) define the one-strip operator

    (T_Ψ B)(a) := min { y_p + B(x_p) :  p = (x_p, y_p) ∈ Ψ,  x_p > a },      a ∈ ℝ,                  (0.3)

(min over an empty set = +∞; the min is attained a.s. when finite because only finitely many points have
y_p + B(x_p) ≤ any given level — B ≥ 0 and Ψ has finitely many points in bounded sets — and the values are
a.s. distinct).  With G_{n+1}(x) := x and G_s := T_{Ψ_s} G_{s+1} (s = n, …, 1) one has K_n = G_1(0)
(W34 (2.2): the min over p_1 of y_1 + (min over the remaining path with x_2 > x_1) = G_1(0), by induction).
G_1(0) depends only on B = G_{n+1} restricted to (0,∞) and on Ψ_s ∩ ((0,∞)×(0,∞)), since every x_p > a ≥ 0.

**Lemma 0.1 (monotonicity and translation; PROVED).**  (i) If B ≤ B' pointwise on (0,∞) then
T_Ψ B ≤ T_Ψ B' on [0,∞).  (ii) T_Ψ(B + c) = T_Ψ B + c for every constant c ∈ ℝ.  (iii) T_Ψ B is
nondecreasing in a.  Both (i) and (ii) iterate over n strips: G_1(0)[B] ≤ G_1(0)[B'] and
G_1(0)[B + c] = G_1(0)[B] + c.

*Proof.*  (i),(ii): termwise in (0.3).  (iii): the index set {x_p > a} shrinks as a grows.  ∎

**Compound Poisson boundaries.**  For ρ > 0 put θ := 1/ρ and let G^ρ be the two-sided compound Poisson
process with G^ρ(0) = 0, jump locations a Poisson(ρ) process on ℝ, i.i.d. jump sizes J ~ Exp(θ) (mean ρ),
independent of the locations.  Thus E[G^ρ(x) − G^ρ(a)] = ρ·ρ·(x − a) = ρ²(x − a): *slope ρ²*.  Write
Ψ for a Poisson(1) process on ℝ × (0,∞) independent of G^ρ, G' := T_Ψ G^ρ, and

    D(a) := G'(a) − G^ρ(a) = min { y_p + (G^ρ(x_p) − G^ρ(a)) :  p ∈ Ψ, x_p > a } ≥ 0.                 (0.4)

D(a) is a function of the inputs strictly to the right of a only (Ψ ∩ {x > a} and the increments of G^ρ
on (a,∞)), whose joint law does not depend on a; so (D(a))_{a∈ℝ} is a stationary process.

## 1. One strip: the law of D and the leftward Markov structure

**Lemma 1.1 (law of D; PROVED).**  For every a, P(D(a) > z) = e^{−θ z} (z ≥ 0), i.e. D(a) ~ Exp(θ) = Exp(1/ρ),
E D(a) = ρ.  (Holds for every ρ > 0 — the relation θ = 1/ρ is what makes it true.)

*Proof.*  By stationarity take a = 0 and write H(x) := G^ρ(x), x ≥ 0.  Given H, the event {D(0) > z} is the
event that Ψ has no point in the region R_z := {(x,y): x > 0, 0 < y < z − H(x)} (the boundary
y = z − H(x) has measure zero), so P(D(0) > z | H) = exp(−|R_z|) with |R_z| = ∫_0^∞ (z − H(x))^+ dx.  Let
φ(z) := P(D(0) > z) = E exp(−∫_0^∞ (z − H(x))^+ dx) ∈ [0,1].  Let T_1 ~ Exp(ρ) be the first jump time of
H, J_1 ~ Exp(θ) its size, and H'(x) := H(T_1 + x) − J_1 the process after the jump: H' is a copy of H
independent of (T_1, J_1).  Then ∫_0^∞ (z − H)^+ dx = z T_1 + ∫_0^∞ (z − J_1 − H'(x))^+ dx, and the second
term is 0 if J_1 ≥ z.  Conditioning on (T_1, J_1):

    φ(z) = E[e^{−z T_1}] · ( P(J_1 ≥ z) + ∫_0^z θ e^{−θ j} φ(z − j) dj )
         = (ρ/(ρ + z)) · ( e^{−θ z} + ∫_0^z θ e^{−θ j} φ(z − j) dj ).                                   (1.1)

The function ψ(z) := e^{−θ z} satisfies (1.1): ∫_0^z θ e^{−θ j} e^{−θ(z−j)} dj = θ z e^{−θ z}, so the right
side is (ρ/(ρ+z)) e^{−θ z}(1 + θ z) = e^{−θ z} · ρ(1 + z/ρ)/(ρ + z) = e^{−θ z}, using ρθ = 1.  Uniqueness
among bounded solutions: if φ, ψ both solve (1.1), δ := φ − ψ satisfies |δ(z)| ≤ ∫_0^z θ |δ(z − j)| dj =
θ ∫_0^z |δ(u)| du, so δ ≡ 0 by Grönwall.  Hence φ = ψ.  ∎

**Lemma 1.2 (leftward evolution; PROVED).**  For a < b,

    D(a) = min ( D(b) + G^ρ(b) − G^ρ(a),  min { y_p + G^ρ(x_p) − G^ρ(a) : p ∈ Ψ, a < x_p ≤ b } ).      (1.2)

Consequently, reading the x-axis from right to left, D is a pure jump process whose jumps are exactly:
(U) at each jump location t of G^ρ with size J: D(t−) = D(t) + J (an *up-jump* by J);
(D) at each point p = (t, y) ∈ Ψ with y < D(t): D(t−) = y (a *down-jump* to y); points with y ≥ D(t) do
nothing.  Here D(t−) := lim_{a↑t} D(a) and D(t) = D(t+) (D is right-continuous by (1.2)).
Moreover G' = G^ρ + D is a pure jump function whose jumps (read left to right) occur exactly at the
(D)-events, at p = (t,y) with y < D(t), with size D(t) − y = D(t) − D(t−) > 0; at the (U)-events G' is
continuous.

*Proof.*  (1.2) splits the min in (0.4) into points with x_p > b (giving D(b) + G^ρ(b) − G^ρ(a) after
adding and subtracting G^ρ(b)) and points with a < x_p ≤ b.  Letting b ↓ t and a ↑ t in (1.2): if the only
input in (a, b] is a G^ρ-jump J at t, D(a) = D(b) + J; if it is a point (t, y) ∈ Ψ, D(a) = min(D(b), y);
if there is no input, D(a) = D(b).  A.s. no two inputs share an x-coordinate.  For G' = G^ρ + D: across a
(U)-event G^ρ increases by J and D decreases by J; across a (D)-event G^ρ is continuous and D increases
(left to right) from y to D(t); elsewhere both are constant.  ∎

**Lemma 1.3 (leftward Markov jump process; PROVED).**  Fix T > 0 and set X(t) := D(T − t), t ∈ [0, T].
Then X is a Markov jump process on [0,∞) with initial law π(dx) = θ e^{−θ x} dx (Lemma 1.1), holding rate
λ(x) = ρ + x, and jump density

    q(x, x') = ρ θ e^{−θ(x' − x)}  (x' > x),      q(x, x') = 1  (0 < x' < x),                          (1.3)

i.e. from state x it waits an Exp(ρ + x) time, then jumps up by an Exp(θ) amount with probability
ρ/(ρ + x) or down to a uniform point of (0, x) with probability x/(ρ + x); a.s. finitely many jumps on
[0, T].  Its law on path space is therefore: for the event {X(0) ∈ dx_0, exactly m jumps at times
t_1 < ⋯ < t_m in dt_i to states dx_i},

    π(x_0) e^{−λ(x_0) t_1} q(x_0,x_1) e^{−λ(x_1)(t_2−t_1)} q(x_1,x_2) ⋯ q(x_{m−1},x_m) e^{−λ(x_m)(T − t_m)}
        dx_0 dt_1 dx_1 ⋯ dt_m dx_m.                                                                    (1.4)

*Proof.*  By Lemma 1.2, X evolves from X(t) using only the inputs in the x-interval (T − t − h, T − t], and
by (0.4) X(t) is a function of the inputs in [T − t, ∞) only; the inputs on disjoint intervals are
independent (Poisson), so X is Markov.  Given X(t) = x, the next event (going left) is the first of: a
G^ρ-jump (locations Poisson(ρ), so waiting time Exp(ρ), size Exp(θ) independent), or a point of Ψ in the
strip {0 < y < x} (a Poisson process of rate x in the x-direction, with y uniform on (0,x) — and points
with y ≥ x are ignored since they cause no jump).  Independence of the two inputs gives the Exp(ρ + x)
holding time and the jump law (1.3), independent of the past by the memorylessness of the Poisson inputs
to the left of T − t.  Finiteness of the number of jumps: up-jumps are the finitely many G^ρ-jumps in
[0,T]; down-jumps are the points of Ψ in [0,T] × (0, max_{[0,T]} D), finitely many since D is finite on
[0,T] (D is bounded on [0,T] by D(T) + G^ρ(T) − G^ρ(0) by (1.2)).  (1.4) is the standard path density of a
non-explosive Markov jump process with these holding rates and jump densities.  ∎

## 2. Burke's property: compound Poisson boundaries are stationary

**Lemma 2.1 (detailed balance; PROVED).**  With π(x) = θ e^{−θ x} and q as in (1.3), π(x) q(x, x') =
π(x') q(x', x) for all x ≠ x' > 0 iff ρθ = 1.

*Proof.*  For x' > x: LHS = θ e^{−θ x} ρ θ e^{−θ(x'−x)} = ρ θ² e^{−θ x'}; RHS = θ e^{−θ x'} · 1.  Equal iff
ρθ = 1.  The case x' < x is the same identity with the roles exchanged.  ∎

**Lemma 2.2 (reversibility; PROVED).**  With θ = 1/ρ, (X(T − t))_{t∈[0,T]} has the same law as
(X(t))_{t∈[0,T]}; equivalently (D(t))_{t∈[0,T]} =_d (D(T − t))_{t∈[0,T]}.

*Proof.*  The time reversal maps the configuration (x_0; t_1, x_1; …; t_m, x_m) of (1.4) to
(x_m; T − t_m, x_{m−1}; …; T − t_1, x_0), a measure-preserving bijection of the reference measure
dx_0 dt_1 dx_1 ⋯ dt_m dx_m (for each m).  The density (1.4) of the reversed configuration is
π(x_m) e^{−λ(x_m)(T−t_m)} q(x_m, x_{m−1}) e^{−λ(x_{m−1})(t_m − t_{m−1})} ⋯ q(x_1, x_0) e^{−λ(x_0) t_1}.  The
holding factors coincide with those of (1.4), and π(x_0) q(x_0,x_1) ⋯ q(x_{m−1},x_m) =
π(x_m) q(x_m,x_{m−1}) ⋯ q(x_1,x_0) by applying Lemma 2.1 m times (π(x_0)q(x_0,x_1) = π(x_1)q(x_1,x_0),
then π(x_1)q(x_1,x_2) = π(x_2)q(x_2,x_1), …).  So the path law is invariant under time reversal.  ∎

**Theorem 2.3 (Burke property; PROVED).**  Let θ = 1/ρ, G^ρ and Ψ as in §0, G' = T_Ψ G^ρ.  Then the jumps
of G' (locations and sizes) form a Poisson process of rate ρ on ℝ with i.i.d. Exp(θ) marks; consequently
(G'(x) − G'(0))_{x∈ℝ} =_d (G^ρ(x) − G^ρ(0))_{x∈ℝ}, and G'(0) − G^ρ(0) = D(0) ~ Exp(1/ρ) has mean ρ.

*Proof.*  Fix T > 0.  By Lemma 1.2, read from left to right on [0,T], D increases exactly at the (D)-events,
by the sizes of the jumps of G', and decreases exactly at the (U)-events, by the sizes of the jumps of G^ρ.
Hence: the marked point process of *increases* of t ↦ D(t) on [0,T] is the jump process of G' on [0,T],
and the marked point process of increases of t ↦ D(T − t) on [0,T] is the jump process of G^ρ on [0,T]
reflected (t ↦ T − t).  By Lemma 2.2 the two paths have the same law, so the two marked point processes
of increases (measurable functionals of the path) have the same law.  The reflection of a Poisson(ρ)
process with i.i.d. Exp(θ) marks is again such a process.  So the jumps of G' on [0,T] form a Poisson(ρ)
process with i.i.d. Exp(θ) marks; by stationarity (§0) and consistency over T → ∞ (and the same argument on
[−T, 0], or translation invariance) the statement holds on ℝ.  Since G' is a pure jump function (Lemma 1.2),
G'(x) − G'(0) is the sum of its jump sizes in (0, x] (x > 0; minus the sum over (x, 0] for x < 0), which is
the compound Poisson process G^ρ − G^ρ(0) in law.  The last claim is Lemma 1.1.  ∎

**Corollary 2.4 (stationary n-strip system; PROVED).**  Let G^ρ_{n+1} := G^ρ (two-sided) and
G^ρ_s := T_{Ψ_s} G^ρ_{s+1}, s = n, …, 1, with Ψ_1, …, Ψ_n i.i.d. Poisson(1) on ℝ × (0,∞) independent of G^ρ.
Then for every s, (G^ρ_s(x) − G^ρ_s(0))_x =_d (G^ρ(x) − G^ρ(0))_x, G^ρ_s is independent of Ψ_1, …, Ψ_{s−1},
and G^ρ_s(0) − G^ρ_{s+1}(0) ~ Exp(1/ρ).  In particular

    E G^ρ_1(0) = n ρ.                                                                                  (2.1)

*Proof.*  Downward induction on s.  G^ρ_{s+1} is a function of (G^ρ, Ψ_{s+1}, …, Ψ_n), hence independent
of Ψ_s, and its increments are compound Poisson(ρ, Exp(1/ρ)) by the induction hypothesis; T_{Ψ_s} depends on
G^ρ_{s+1} only through its increments and the value G^ρ_{s+1}(0) (Lemma 0.1(ii)), so Theorem 2.3 applies to
the pair (G^ρ_{s+1} − G^ρ_{s+1}(0), Ψ_s).  Summing G^ρ_s(0) − G^ρ_{s+1}(0) over s and using G^ρ_{n+1}(0) = 0
gives (2.1).  ∎

## 3. Comparison with the true boundary: n − √(2n) ≤ E K_n ≤ n + √(2n) + 1/2

**Lemma 3.1 (Lundberg bounds; PROVED).**  Let G^ρ be as in §0 restricted to x ≥ 0, θ = 1/ρ.
(a) If ρ > 1: Z := sup_{x≥0} (x − G^ρ(x)) satisfies P(Z ≥ z) ≤ e^{−κ z} with κ := ρ − 1/ρ > 0; hence
    E Z ≤ 1/κ = ρ/(ρ² − 1).
(b) If 0 < ρ < 1: Z' := sup_{x≥0} (G^ρ(x) − x) satisfies P(Z' ≥ z) ≤ e^{−κ' z} with κ' := 1/ρ − ρ > 0; hence
    E Z' ≤ 1/κ' = ρ/(1 − ρ²).

*Proof.*  (a) X(x) := x − G^ρ(x) is a Lévy process with E e^{κ X(x)} = exp( x [κ + ρ(E e^{−κ J} − 1)] ) =
exp( x [κ + ρ(θ/(θ + κ) − 1)] ) = exp( x κ [1 − ρ/(θ + κ)] ), which equals 1 iff θ + κ = ρ, i.e. κ = ρ − θ =
ρ − 1/ρ.  For this κ, M_x := e^{κ X(x)} is a positive martingale (stationary independent increments, M_0 = 1).
Let τ := inf{x : X(x) ≥ z}.  Optional stopping at τ ∧ x_0: 1 = E M_{τ∧x_0} ≥ E[M_τ ; τ ≤ x_0] ≥ e^{κ z}
P(τ ≤ x_0); let x_0 → ∞.  E Z = ∫_0^∞ P(Z ≥ z) dz ≤ 1/κ.
(b) X'(x) := G^ρ(x) − x: for 0 < κ < θ, E e^{κ X'(x)} = exp( x [−κ + ρ(θ/(θ − κ) − 1)] ) = exp( x κ [ρ/(θ − κ) − 1] ),
equal to 1 iff θ − κ = ρ, κ' = θ − ρ = 1/ρ − ρ (which is < θ).  Same martingale argument (the level z
may be overshot by a jump, which only helps: M_τ ≥ e^{κ' z} on {τ < ∞}).  ∎

**Lemma 3.2 (sandwich; PROVED).**  With K_n as in (0.1) and G^ρ_1(0) as in Corollary 2.4 (coupled on the
same Ψ_1, …, Ψ_n), for every ρ > 0:
    G^ρ_1(0) − Z' ≤ K_n ≤ G^ρ_1(0) + Z,   where Z = sup_{x≥0}(x − G^ρ(x))^+, Z' = sup_{x≥0}(G^ρ(x) − x)^+.

*Proof.*  K_n = G_1(0)[B_0] with B_0(x) = x, and G^ρ_1(0) = G_1(0)[G^ρ] (both determined by the boundary
on (0,∞)).  Pointwise on (0,∞): G^ρ(x) − Z' ≤ x ≤ G^ρ(x) + Z.  Apply Lemma 0.1 (i) and (ii) (Z, Z' are
constants for the pathwise recursion).  ∎

**Theorem 3.3 (γ_∞ = 1; PROVED).**  For every n ≥ 1,

    n ρ − ρ/(1 − ρ²) ≤ E K_n   (0 < ρ < 1),        E K_n ≤ n ρ + ρ/(ρ² − 1)   (ρ > 1),               (3.1)

and consequently

    n − √(2n) ≤ E K_n ≤ n + √(2n) + 1/2,      |E K_n / n − 1| ≤ √(2/n) + 1/(2n),      γ_∞ = lim E K_n/n = 1.   (3.2)

*Proof.*  (3.1): take expectations in Lemma 3.2 and use (2.1) and Lemma 3.1 (Z ≥ 0 and Z' ≥ 0 have the
stated means; K_n and G^ρ_1(0) are integrable — K_n is bounded by the corner-greedy cost Σ_s T_s,
T_s i.i.d. with E T_s = √(π/2) (W34 §2/Lemma 3.3), and E G^ρ_1(0) = nρ < ∞).  (3.2): upper bound with ρ = 1 + δ, δ = 1/√(2n): ρ/(ρ² − 1) = (1+δ)/(δ(2+δ)) ≤
(1+δ)/(2δ), so E K_n ≤ n + nδ + 1/(2δ) + 1/2 = n + √(n/2) + √(n/2) + 1/2.  Lower bound with ρ = 1 − δ,
δ = 1/√(2n) ≤ 1: ρ/(1 − ρ²) = (1−δ)/(δ(2−δ)) ≤ 1/(2δ) (as (1−δ)/(2−δ) ≤ 1/2), so E K_n ≥ n − nδ − 1/(2δ) =
n − √(2n).  ∎

**Corollary 3.4 (subadditivity: E K_n ≥ n for every n; PROVED).**  (E K_n) is subadditive:
E K_{m+n} ≤ E K_m + E K_n.  Hence lim E K_n/n = inf_n E K_n/n (Fekete), and with Theorem 3.3,
E K_n ≥ n for every n ≥ 1.  Consequently C_b ≥ 1/4 and C^{mix}_b ≥ 1/4 for every b: the block constants
of paper Theorem 18 approach 1/4 strictly from above, and no block rule of this family beats 1/4.

*Proof.*  Let P* be an optimal path for strips 1..m, with final clock a_m and cost K_m, and let
K''_n := min{ (x_n − a_m) + Σ y_s } over x-increasing paths through Ψ_{m+1}, …, Ψ_{m+n} with all x > a_m.
Concatenation is feasible for K_{m+n}, so K_{m+n} ≤ K_m + K''_n.  a_m is σ(Ψ_1,…,Ψ_m)-measurable, and
conditionally on a_m = a the processes Ψ_{m+i} ∩ (a,∞)×(0,∞), translated by −a in x, are i.i.d. Poisson(1)
on (0,∞)² (independence of the first m strips; translation invariance), so E[K''_n | Ψ_1,…,Ψ_m] = E K_n.
Take expectations.  For the last claim: γ^{mix}_b = (E K_b + E K_{b+1})/(2b+1) ≥ (b + (b+1))/(2b+1) = 1.  ∎

*Remarks.*  (i) Numerically E K_n − n ≈ 0.21√n (W34 §4: b = 4, 16, 64, 256 give 0.56, 1.08, 1.95, 3.41);
(3.2) allows ±1.41√n.  The true correction is presumably of order n^{1/3} (KPZ) with the √n in (3.2) an
artefact of the crude Lundberg step; not pursued.  (ii) The stationary system says: with boundary slope
σ = ρ² the cost per strip is exactly √σ; the free boundary x (slope 1) is the case σ = 1, cost 1 per strip.
This is the exact analogue of the Hammersley sources/sinks relation (density ρ ↔ 1/ρ) and identifies γ_∞ = 1
= the LIS constant (2 per unit √N in the LIS normalisation: x-part + y-part = n/2 + n/2, and 2√((n/2)(n/2)) = n).
(iii) Lemma 1.1 alone (without Burke) gives only the last strip.  (iv) Nothing in §1–3 uses the half-plane
restriction; the whole-line construction is what makes D stationary.

## 4. Consequences for block-grid patterns

Recall (W34 §3–4, paper Theorem 18): C_b := (E K_b/(2b))², γ^{mix}_b := (E K_b + E K_{b+1})/(2b+1),
C^{mix}_b := (γ^{mix}_b/2)², and Theorem 18(a): for every b ≥ 1 and C > C^{mix}_b, every π_τ ∈ 𝒢(r,h)
satisfying (H_b) (no strip revisited within b+1 consecutive visits; all tilted grids (12⋯r)^h) with
min(r,h) ≥ (ln k)³ is contained in Π_{Ck²} in the fixed-strip model, hence contained, w.h.p. as k = rh → ∞,
uniformly in τ.

**Corollary 4.0 (certified constants; PROVED).**  For all b ≥ 1,
    C_b ≤ ( 1/2 + 1/√(2b) + 1/(4b) )²,      C^{mix}_b ≤ ( 1/2 + (√(2b) + √(2b+2) + 1)/(2(2b+1)) )²,
and both tend to 1/4.  (Numerical values: results.md; e.g. C^{mix}_b ≤ 0.2731 at b = 10³, ≤ 0.2572 at
b = 10⁴ (value 0.2571), ≤ 0.2522 at b = 10⁵.  The Monte Carlo values of W34 (0.266 at b = 64) are of course smaller; the
certified bound only needs to reach 1/4 in the limit.)

*Proof.*  Insert (3.2) into the definitions.  ∎

**Theorem 4.1 (tilted grids at Alon's constant; PROVED).**  For every ε > 0 there is b = b(ε) such that:
for every sequence of block-grid patterns π_τ ∈ 𝒢(r,h) satisfying (H_b) — in particular every tilted grid
(12⋯r)^h — with min(r,h) ≥ (ln k)³, k = rh → ∞,
    Pr( π_τ ⊆ Π_{(1/4+ε)k²} ) → 1,
and a uniformly random permutation of length n ≥ (1/4 + 2ε)k² contains π_τ w.h.p.  The convergence is
uniform in τ.  In the fixed-strip model (rigid value strips) with full lookahead, the mean-field
threshold constant is exactly γ_∞²/4 = 1/4 (Theorem 3.3), settling W34 Conjecture 5.1.

*Proof.*  By Corollary 4.0 choose b with C^{mix}_b < 1/4 + ε; apply Theorem 18(a) (W34 Theorem 3.4) with
C = 1/4 + ε, and the Poisson-to-uniform coupling of the paper (W19 Cor. 2.2 / W11 Remark 0.3) for the
permutation statement.  ∎

**Corollary 4.2 (FREE model; PROVED).**  The same holds for the FREE model (copy chooses its own strip
boundaries), since fixed-strip containment implies containment; and by W20 Remark 4.7 the FREE constant is
≤ min over both strip directions, so C^{free}(r,h) ≤ 1/4 + o(1) on the diagonal r = h → ∞ from both sides.

## 5. What is and is not proved about "exactly 1/4"

PROVED: (α) γ_∞ = 1 with explicit error (3.2), in both directions; (β) threshold of tilted grids and all
(H_b)-patterns ≤ (1/4 + o(1))k² (Theorem 4.1).
NOT PROVED (and not claimed): a lower bound (1/4 − o(1))k² for the containment threshold of tilted grids.
The paper's lower bounds valid for these patterns are the universal ones (every π ∈ S_k has threshold
≥ 0.1925k², §"Rigorous bounds on c_21"); LIS-type lower bounds do not apply because the tilted grid has
LIS = r + h − 1 ≈ 2√k only.  What (α) makes exact is the *mean-field fixed-strip model with full
lookahead*: its constant is 1/4, so rigid strips lose nothing at first order, but the FREE model (non-rigid
strip geometry) could in principle be lower; W20's numerics for (12)^h at bounded r (fixed model ≈ 0.22)
show that outside the mean-field regime the fixed-strip constant itself drops below 1/4.  A lower bound
would require the comparison principle (W37) or a direct argument that sup_c L(Π_c) < k below 1/4 for the
grid's cut family; both open.  Conjecturally (identity hardest, W21) the truth for grids is ≤ 1/4 with
equality only in the limit min(r,h) → ∞ — consistent with everything here but not established.

## 6. Approaches (b), (c) of the brief

(b) Sub/superadditivity + chain surgery and (c) stochastic comparison sup_c L(Π_c) ≥ LIS − o(k) were not
needed: (a) gives an exact solution with explicit error terms.  Of (b), the subadditive half survives as
Corollary 3.4 (it gives existence of γ_∞ and, combined with Theorem 3.3, the exact inequality E K_n ≥ n);
Fekete alone cannot identify the value, and the direct chain-surgery coupling with LIS was not pursued —
the Burke identification of §2 is what pins γ_∞ to the LIS constant.  (c) would be a route to the missing
*lower* bound of §5, not to the upper bound, and remains open (W37's territory).

## 7. Numerical certification (verify.py; results.md)

All checks use independently written code (own suffix-minimum DP; not W34's fpp.py):
A. D(0) ~ Exp(1/ρ) (Lemma 1.1) for ρ = 0.5, 1, 2: KS distance 0.008–0.018 with 4000 samples (95% level 0.0215).
B. Burke (Theorem 2.3): jumps of G' in the bulk of a strip of length 4000: rate ρ (0.4993/0.9988/2.0005),
   size mean ρ and E s²/(2 mean²) = 1.000–1.003 (exponential), gap mean 1/ρ and exponential, lag-1
   correlations of sizes, of gaps and size–next-gap all within ±0.007 of 0; KS distance of the size law to
   Exp(1/ρ) ≤ 0.004 with 6·10⁴–2.4·10⁵ jumps.
C. E G^ρ_1(0) = nρ (Corollary 2.4) for (n,ρ) = (10,1), (10,1.5), (10,0.7), (50,1), (50,1.2), (200,1) within
   1.2 s.e.; E K_n = 10.85 ± 0.07, 51.99 ± 0.22, 201.6 ± 1.1 inside the bounds (3.2) [5.5,15.0], [40.0,60.5],
   [180.0,220.5] and inside the ρ-specific bounds (3.1).
D. Lundberg (Lemma 3.1a): E Z = 1.22 ± 0.03 vs 1/κ = 1.20 (ρ = 1.5), 0.68 ± 0.02 vs 0.667 (ρ = 2);
   P(Z > 1) = 0.44/0.24 vs e^{−κ} = 0.43/0.22 (the bound is an equality for ρ > 1 since X crosses continuously).
E. DP validation: the suffix-minimum DP agrees with brute-force path enumeration on 300 random small
   instances to within the staircase discretisation error 2·10⁻³ (check_small.py).
Commands: `experiments/w12-c21/.venv/bin/python experiments/w36-gamma-limit/verify.py 1` (9 s; seed 2 in
verify_seed2.out, same conclusions), `... check_small.py`, `... constants.py` (certified-constant table,
constants.out).
