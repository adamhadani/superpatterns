# W36 log — γ_∞ = 1 (2026-08-30)

09:10 Read SESSION-STATE, W34 proof/results, fpp.py, paper Thm 18. Lower bound check: the paper's only
lower bound valid for grids is the universal 0.1925k² (§Rigorous bounds on c_21); there is NO ≥ 1/4 lower
bound for grids (and the FREE model may lie below 1/4: (12)^h fixed ≈0.22 at bounded r). So the rigorous
target is: γ_∞ = 1 (both directions, for the first-passage functional) and threshold ≤ (1/4+o(1))k².

09:25 Approach (a) works. Key observation: with G_s(a)=a+F_s(a), one strip step is
G'(a) = min_{x_p>a}[y_p + G(x_p)].  Put D(a) := G'(a) − G(a) = min_{x_p>a}[y_p + G(x_p) − G(a)].
If G is a compound Poisson process (rate ρ, jumps Exp(θ)), D(·) read LEFTWARD is a Markov process:
up-jump by J~Exp(θ) at rate ρ (a jump of G), down-jump to y~U(0,D) at rate D (a Ψ-point with y<D).
Stationary law θe^{−θD} iff ρθ = 1 (also verified directly by a void-probability renewal equation).
Detailed balance holds with ρθ=1 ⇒ reversible ⇒ the down-jump events (= jumps of G') are, read rightward,
the up-jumps of an identical-in-law process ⇒ Poisson(ρ)⊗Exp(θ): BURKE.  Per strip E D = ρ.
Stationary boundary with slope ρ² vs the true boundary x: comparison via Z = sup(x − G^ρ(x)) (Lundberg,
κ = |ρ − 1/ρ|) gives n − √(2n) ≤ E K_n ≤ n + √(2n) + 1/2.
Next: numerics (Burke test, D law, E K_n vs bounds using an independent DP), then proof.md.

10:00 verify.py (own DP, validated vs brute force by check_small.py) passes all checks, seeds 1 & 2:
D~Exp(1/ρ) (KS), Burke (G'-jump rate/size/gap laws + zero correlations), E G^ρ_1(0)=nρ, Lundberg E Z=1/κ,
E K_n inside [n−√(2n), n+√(2n)+½].  constants.py: certified C^mix_b crosses π/8 at b=64 (0.3504),
0.2507 at b=10⁶.
10:15 proof.md complete: §1 law of D (renewal eq., Grönwall uniqueness); §2 Burke via detailed balance +
path-density reversibility (elementary, no general Markov theory); §3 sandwich + Lundberg ⇒
n−√(2n) ≤ E K_n ≤ n+√(2n)+½; Cor 3.4 subadditivity ⇒ E K_n ≥ n exactly (so C_b ≥ 1/4: block rules
never beat 1/4); §4 Thm 4.1 tilted grids ≤ (1/4+ε)k² via W34 Thm 3.4; §5 states clearly that the ≥ 1/4
threshold lower bound does NOT exist in the paper (universal 0.1925 only; grid LIS = r+h−1 kills LIS-type
bounds) — the brief's parenthesis "(≥ follows from LIS-type lower bounds already in the paper)" is FALSE
and I checked the paper to confirm.  "Exactly 1/4" is proved for the mean-field fixed-strip full-lookahead
model (W34 Conj 5.1), and the containment threshold statement is one-sided: ≤ (1/4+o(1))k².
Dead ends: none serious; first attempt at Burke via abstract time-reversal theory replaced by the
elementary path-density argument (avoids semigroup/self-adjointness machinery for the unbounded rate ρ+d).
DONE.  Files: proof.md, results.md, verify.py (+outs), check_small.py (+out), constants.py (+out).
