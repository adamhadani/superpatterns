# Current research notes — 10 November 2026

Read [SESSION-STATE.md](SESSION-STATE.md) first, then [RESULTS.md](RESULTS.md) (exact scopes, certificates,
withdrawals, reproduction commands), [AUDIT-2026-11-10.md](AUDIT-2026-11-10.md) and [ALON-STRATEGY.md](ALON-STRATEGY.md) §0.
Earlier notes are preserved under `archive/`, including their obsolete claims.

**Where things stand.** Alon's conjecture is open here. W90 proves that flipping a block 12 → 21 in a direct sum
never increases containment, hence c₂₁ ≤ 1, and gives numerical evidence (n up to 10⁸) that c₂₁ ≈ 0.99887 < 1,
which would refute the conjecture at the sharp constant ¼. The strict inequality is reduced to a "start regularity"
lemma in `experiments/w90-layered-deficit/strict-deficit-plan.md`; it is not proved.

**What was withdrawn.** Workstreams W43–W89 (22–27 September 2026) claimed universality at C·k², the sharp ¼
threshold for bounded-LDS classes, c₂₁ = 1 and the full conjecture. None is proved; see the audit. They are archived
in `experiments/archive-2026-09-unverified/`.

**Literature anchors.** General random universality: He–Kwan, 2000 k² log log k. Individual / typical targets:
arXiv:2608.19050 (online embedding; 0.50568 and 0.49967), which also notes that the increasing permutation is not
extremal online. Deterministic lower bound: Chroman–Kwan–Singhal 1.000076/e² (ours: 1.0073/e²). Skew-shape
inequality behind W90: Jelínek–Karpilovskij 2021; Burstein–Pantone; equality case Backelin–West–Xin. Details and
caveats in [priority-check.md](priority-check.md).

**Standing cautions** (from the September 10 review, still valid). Individual, typical and simultaneous statements
are different; a per-pattern bound e^{−ck} does not give a union bound over k!; finite means below a benchmark are
not bounds on a limiting constant; the both-parity encoding rule and the old H_b inference stay withdrawn.
