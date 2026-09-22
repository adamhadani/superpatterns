# W7 — value-slot encoding and corrected C′

Reviewed 2026-09-10. The deterministic lemma below remains valid. The old
finite C formula applied the slot mean m(b) to unbounded geometric widths,
including widths beyond the host, where the formula becomes invalid. Its
asymptotic minimum was also justified only numerically. The complete repair,
with an explicit width cutoff, an analytic quantile monotonicity proof and
an outward interval certificate, is [W25 corrected C′](../w25-asymptopia-review/proof.md).
It proves sp(k)>1.0073 k²/e² for all sufficiently large k. The older
coefficients 1.00483 and approximately 1.0073384 are historical numerical
optimizations, not additional interval certificates.

`historical-proof.md` preserves the superseded C derivation. The both-parity
extension proposed there is withdrawn: see W3's stability counterexample.

### Lemma 1' (slot encoding; deterministic)

Let I(T) ⊆ even indices be a *stable* rule (I(T) depends only on the odd positions t_1,t_3,…). For T write
I(T) = {ι_1<…<ι_r}, V(T) := σ({t_j : j ∉ I(T)}) (the k−r "off-I values"), and for i ∈ I(T)

    M_i(T) := #{ distinct slots relative to V(T) of the values σ(p), p ∈ (t_{i−1}, t_{i+1}) }.

Then

    pat(σ) ≤ Σ_T  min( 1,  Π_{j=1}^{r(T)} min( M_{ι_j}(T) + j − 1,  k ) / (b_{ι_j}(T) − 1) ).                (L1')

**Warning.** The per-factor cap min(…, b_{ι_j} − 1) that a first draft of this note used is FALSE (found by the
coordinator by per-class enumeration on the sp(6) witness, k = 6, β = 5: class I = {2,4}, off-I positions
(1,6,11,16), V = {4,6,9,17}, M = (2,4), b_4 − 1 = 4: the false bound gives 2·4 = 8 but the class realises 9
patterns; lemma_check.py's worst case there is I = {2,4}, off-I (2,11,16,17), V = {4,9,14,15}, M = (4,4),
b = (9,5): 18 patterns vs the false 16). The number of positions in window j does not bound the number of
achievable s_j given a prefix, because realisations of the same prefix with different values v_l put a fixed
window position into different slots.
Only the *product* Π(b_{ι_j} − 1) = |ext(ψ)| is a valid cap, whence the min(1, ·).

*Proof.* Fix for each pattern π ⊆ σ an occurrence T(π) and let ψ(T) := (I(T), (t_j)_{j∉I(T)}). Let ext(ψ) be the
set of T' agreeing with ψ off I; since I is non-adjacent, |ext(ψ)| = Π_{i∈I}(b_i−1), and by stability
I(T') = I for all T' ∈ ext(ψ), so the ext(ψ) are pairwise disjoint (T' determines ψ(T')). Every π equals
pat(σ|T') for some T' ∈ ext(ψ(T(π))), hence pat(σ) ≤ Σ_ψ N(ψ), N(ψ) := #{pat(σ|T') : T' ∈ ext(ψ)}.

Trivially N(ψ) ≤ |ext(ψ)| = Π_i(b_i−1). Claim: N(ψ) ≤ Π_{j=1}^r min(M_{ι_j} + j − 1, k), with M_i = M_i(T) for
any T ∈ ext(ψ) (V, hence M_i, is a function of ψ alone).

Write v_j := σ(t'_{ι_j}) for T' ∈ ext(ψ), V_j := V ∪ {v_1,…,v_{j−1}}, and s_j := slot of v_j relative to V_j.
pat(σ|T') is determined by the relative order of the k values; the relative order of V is fixed by ψ; and the
sequence (s_1,…,s_r) determines the relative order of V ∪ {v_1,…,v_r} (insert the v_j one at a time into the
sorted list). So N(ψ) ≤ #{(s_1,…,s_r) realised by some T' ∈ ext(ψ)} ≤ Π_j max_{prefix} #{s_j realised given
(s_1,…,s_{j−1})}. It remains to bound, for a fixed prefix (s_1,…,s_{j−1}), the number of values of s_j over ALL
T' ∈ ext(ψ) realising that prefix — note that different realisations may have different v_1,…,v_{j−1}, so the
set V_j varies; the count is not bounded by the number of positions t'_{ι_j} (that was the error).

The prefix determines the relative order of V_j = V ∪ {v_1,…,v_{j−1}}, hence for every l < j the V-slot
c_l ∈ {0,…,k−r} of v_l, and, within each V-slot c, the relative order of {v_l : c_l = c}. Let n_c := #{l<j : c_l = c}
(Σ_c n_c = j−1). For any realisation and any value u in V-slot c,

    slot of u relative to V_j  =  c + #{l<j : c_l < c} + #{l<j : c_l = c, v_l < u},

where the middle term depends only on the prefix and the last term is an integer in [0, n_c]. Hence over all
realisations of the prefix and all u ∈ σ((t_{ι_j−1}, t_{ι_j+1})), s_j takes at most Σ_{c hit by the window}(1 + n_c)
≤ M_{ι_j} + (j−1) distinct values. Also s_j ∈ {0,…,|V_j|} gives ≤ k − r + j ≤ k values. This proves the claim.

Finally Σ_ψ N(ψ) = Σ_ψ Σ_{T'∈ext(ψ)} N(ψ)/|ext(ψ)| ≤ Σ_{T'} min(1, (Π_j min(M_{ι_j}+j−1,k))/Π_i(b_i−1)) by disjointness. ∎

Remarks. Any fixed insertion order is valid. The checker enumerates each
class once, so its summed bound is Σ_ψ min(Π_j min(M_j+j−1,k),Π_j(b_j−1));
it must not divide by the class size again. The 2026-09-10 rerun has zero
violations for the corrected bound on every tested class, and also asserts
that the total bound exceeds the actual pattern count. For the length-23
7-superpattern at β=2 the corrected total is 152657 (the old 3746.65 total
was the double-division bug). See `lemma_check_out.txt` for every case.
