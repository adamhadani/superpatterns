# W40 log

- 2026-09-10: Derived the completed-threshold/pending-interval state and both
  exact updates. Implemented a segment tree for the pending-profile query.
  This addresses the requested global-state milestone without committing
  to a local renewal choice. Verification and sample outputs are recorded
  alongside the source.
- The proposed direct reuse of W36's monotone boundary law does not follow:
  a concrete prefix gives a downward jump in the pending profile, and all
  levels use the same arrival process. An appropriate stationary law or
  comparison remains open. No new asymptotic bound for c_21 is claimed.

## 10 September 2026 — continuation after “go ahead and continue”

- Proved permanent pruning of every level-m pending apex at least F_(m+1).
  The remaining intervals lie in disjoint threshold gaps, so each new point
  updates just one gap. `pruned.c` uses O(n log n) time and O(n) space.
- `verify_pruned.py`: all 46,233 hosts through length 8, 100 random hosts
  through 128 and nine extreme hosts; all 372,249 prefix thresholds match an
  independent unpruned list recurrence. Exhaustive final answers also match
  brute subsequences. Compiler warnings: none under Wall/Wextra/pedantic.
- Derived the exact interval-union current across a height cut; 5912 finite
  cut checks match full-state extensions. A four-point reachable counterexample
  shows activation marks are still required even with all apices retained.
- Primary prior-art check: Albert, arXiv:math/0505485, §4 already reports
  O(n log n) for the related layered class allowing singleton blocks.
  We claim an implementation/state reduction here, not algorithmic priority.
- No stationary law or new c_21 bound follows yet. Next: test a proposed
  marked invariant distribution against the exact local generator and current.

## 10 September 2026 — prominent result record and Alon-directed queue

- Wrote a self-contained six-page note with the full recurrence, pruning,
  complexity proof, marked counterexample, flux and conditional Alon criterion.
  Deliverables are PDF and reader Markdown in `output/pdf/`, with source and
  bibliography in `output/paper/`. Added `report.md` and prominent navigation.
- Checked Albert et al. (2003), §3.7, p. 236: the specialized size-1/2 layered
  problem has an O(n²) bound, sharper than the broad O(n² log n) description.
  Cited both this paper and Albert's 2005 preprint / 2007 publication §4.
  Maximizing complete pairs is a weighted variant; priority is unestablished.
- Recorded the elementary general obstruction: if a repeated length-d
  pattern has limiting constant cτ<2/d, then Alon is false. For 21 the
  missing step is a rigorous upper bound below one, not finite-size fitting.
- The user prioritizes proof/disproof of Alon. `memory/ALON-STRATEGY.md`
  now leads with common host events for general interleavings and rigorous
  repeated-pattern obstructions. W42 separately completes the first
  two-exchange selection-cost test; its first moment is target-dependent.
