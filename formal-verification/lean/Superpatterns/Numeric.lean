import Mathlib

/-!
# The numeric constant in Theorem A (Step 5)

We certify that at `θ = 7.37`, `λ = 1.0003`,

  `λθ/e² − log θ + 1 + ½ log(1 − e^{−θ}) < 0`.

The true value is about `−1.25·10⁻⁵`, so every term must be bounded to a few parts in `10⁶`.
We use Mathlib's decimal bounds on `e` and `log 2`, the Taylor bound `Real.exp_bound` for
`exp 0.37`, the Taylor bound `Real.abs_log_sub_add_sum_range_le` for `log(1 − 63/800)`
(`7.37 = 2³·(1 − 63/800)`) and `log y ≤ y − 1` for the last term.
-/

open Real Finset

namespace Superpatterns

/-- `λθ/e² ≤ 0.9977203`. -/
theorem termA_le : (1.0003 : ℝ) * 7.37 / exp 1 ^ 2 ≤ 0.9977203 := by
  have he : (2.7182818283 : ℝ) < exp 1 := exp_one_gt_d9
  have h2 : (2.7182818283 : ℝ) ^ 2 ≤ exp 1 ^ 2 :=
    pow_le_pow_left₀ (by norm_num) he.le 2
  rw [div_le_iff₀ (by positivity)]
  nlinarith

/-- `log 7.37 = 3 log 2 + log (1 − 63/800)`. -/
theorem log_737 : log (7.37 : ℝ) = 3 * log 2 + log (1 - 63 / 800) := by
  rw [show (7.37 : ℝ) = 2 ^ 3 * (1 - 63 / 800) by norm_num,
    log_mul (by norm_num) (by norm_num), log_pow]
  push_cast
  ring

/-- `log 7.37 ≥ 1.9974176`. -/
theorem termB_ge : (1.9974176 : ℝ) ≤ log 7.37 := by
  rw [log_737]
  have hl2 : (0.6931471803 : ℝ) < log 2 := log_two_gt_d9
  have h := abs_log_sub_add_sum_range_le (x := (63 / 800 : ℝ)) (by norm_num) 6
  rw [abs_le] at h
  obtain ⟨h1, -⟩ := h
  simp only [sum_range_succ, sum_range_zero] at h1
  norm_num [abs_of_pos] at h1
  norm_num
  linarith

/-- `exp 0.37 ≤ 1.4477347`. -/
theorem exp_037_le : exp (0.37 : ℝ) ≤ 1.4477347 := by
  have h := exp_bound (x := (0.37 : ℝ)) (by rw [abs_le]; constructor <;> norm_num) (n := 7)
    (by norm_num)
  rw [abs_le] at h
  obtain ⟨-, h2⟩ := h
  simp only [sum_range_succ, sum_range_zero, Nat.factorial] at h2
  norm_num [abs_of_pos] at h2
  linarith

/-- `exp 7.37 ≤ 1588`. -/
theorem exp_737_le : exp (7.37 : ℝ) ≤ 1588 := by
  have he : exp 1 < (2.7182818286 : ℝ) := exp_one_lt_d9
  have h7 : exp 1 ^ 7 ≤ (2.7182818286 : ℝ) ^ 7 :=
    pow_le_pow_left₀ (exp_pos 1).le he.le 7
  have hsplit : exp (7.37 : ℝ) = exp 1 ^ 7 * exp 0.37 := by
    rw [← exp_nat_mul, ← exp_add]
    norm_num
  rw [hsplit]
  have h037 := exp_037_le
  have hpos : (0 : ℝ) ≤ exp 1 ^ 7 := by positivity
  calc exp 1 ^ 7 * exp 0.37 ≤ (2.7182818286 : ℝ) ^ 7 * 1.4477347 := by
        exact mul_le_mul h7 h037 (exp_pos _).le (by norm_num)
    _ ≤ 1588 := by norm_num

/-- `½ log(1 − e^{−7.37}) ≤ −1/3176`. -/
theorem termC_le : log (1 - exp (-(7.37 : ℝ))) / 2 ≤ -(1 / 3176) := by
  have hu : exp (-(7.37 : ℝ)) = 1 / exp 7.37 := by rw [exp_neg]; ring
  have hE := exp_737_le
  have hEpos := exp_pos (7.37 : ℝ)
  have hu_ge : (1 / 1588 : ℝ) ≤ exp (-(7.37 : ℝ)) := by
    rw [hu]; exact one_div_le_one_div_of_le hEpos hE
  have hu_lt : exp (-(7.37 : ℝ)) < 1 := by
    rw [exp_lt_one_iff]; norm_num
  have hlog := log_le_sub_one_of_pos (x := 1 - exp (-(7.37 : ℝ))) (by linarith)
  linarith

/-- **The constant certificate**: `λθ/e² − log θ + 1 + ½ log(1 − e^{−θ}) < 0` at
`θ = 7.37`, `λ = 1.0003`. -/
theorem constant_certificate :
    (1.0003 : ℝ) * 7.37 / exp 1 ^ 2 - log 7.37 + 1 + log (1 - exp (-(7.37 : ℝ))) / 2 < 0 := by
  have hA := termA_le
  have hB := termB_ge
  have hC := termC_le
  norm_num at hA hB hC ⊢
  linarith

end Superpatterns
