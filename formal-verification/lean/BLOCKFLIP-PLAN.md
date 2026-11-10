# Feasibility: formalising the block-flip theorem and the planted gadget

Date: 2026-11-10. This is an assessment only; **none of the work below has been started.** What exists is
`Superpatterns/BlockFlip.lean`: the statement `BlockFlipStatement`, a verified containment test and exhaustively
checked instances (n ≤ 9). Sources: `experiments/w90-layered-deficit/proof.md` §1–2 (Theorem 1, Lemmas 1–4),
`experiments/w91-strict-deficit/proof.md` §2 (Lemma 2.3).

**Headline.** Theorem 1 is a realistic, self-contained target: about 1 500–2 200 lines of Lean, 4–6 weeks for
someone fluent in Mathlib. Lemma 2.3 is a further 900–1 400 lines, 3–4 weeks. The Poisson-process layer of W91
(Theorems A, B, Corollary C, c₂₁ < 1) is not realistically formalisable with current Mathlib.

## 1. Definitions

* **Hosts are point sets, patterns stay lists.** A configuration is a `Finset (ℕ × ℕ)` with both projections
  injective. ℕ suffices: every point in W90 §2 (points of P, corners a∧b and a∨b, board cells) takes its
  coordinates from P. `graph σ = {(i, σ[i])}`, and `word Q` lists the y-coordinates of Q by increasing x, so
  `word (graph σ) = σ`. "Q contains γ" is `Contains (word Q) γ` with the project's `Contains`. A
  permutation-only setting (`Equiv.Perm (Fin n)`) fails because U_α(O) is containment in a partial configuration.
* **Order and regions.** `z ≪ w := z.1 < w.1 ∧ z.2 < w.2` (Mathlib's product `<` is weaker).
  `U α P z := Contains (word (P.filter (· ≪ z))) α`; `S β P z` is the mirror image; `inside`, `outside` are filters.
* **Fibres without boards.** The fibre of σ ∈ S_n is `{τ ∈ S_n | outside (graph τ) = outside (graph σ)}`; X and Y
  are then forced. Boards and bijections X → Y appear only inside the proofs of Lemmas 3 and 4.

Everything stays executable, so each lemma statement can be tested by `decide` on S_n, n ≤ 7, before it is proved.

## 2. Lemma breakdown for Theorem 1 (the inequality)

| Step | Content | Lines |
|:--|:--|--:|
| A | `graph`, `word`, monotonicity in the host, U is an up-set, S a down-set; splitting lemma: Q ⊇ α ⊕ₚ γ iff a copy of α lies ≪-below a copy of γ | 350–500 |
| B | Lemma 1: reading the middle block; the middle points are inside | 150–200 |
| C | Lemma 2: U_α(P) = U_α(O), extremal copy by `Finset.exists_min_image` | 150–250 |
| D | Lemma 3: all members of a fibre share O, U, S; any filling of the board stays in the fibre | 300–450 |
| E | Lemma 4(ii) by an extremal argument: uncrossing a D-inversion raises Φ = Σ x·y by (x_b − x_a)(y_a − y_b) > 0, so a Φ-maximal member (`Finset.exists_max_image`) has none. Lemma 4(i), easy half: at most one member has no increasing inside pair (`Finset.orderEmbOfFin_unique`) | 200–300 |
| F | In each fibre #{⊇ α⊕21⊕β} ≤ F − 1 ≤ #{⊇ α⊕12⊕β}; sum by `Finset.card_eq_sum_card_fiberwise` | 150–250 |
| G | Bridge to `BlockFlipStatement` (lists, `⊕ₚ`, `List.range' 1 n`) | 150–250 |

The inequality needs neither "f_dec is valid" nor inversion counting; the exact formula Σ(a − 1) needs the full
Lemma 4(i), about 200 lines more. Mathlib supplies the finite-set and order toolkit named above, but it has no
permutation-pattern library: step A is all project code (`ErdosSzekeres.lean` has a start, `ofFn_sublist`).

## 3. Lemma 2.3 (planted 3416725 gadget)

New definitions: block words and prefixes Π[1..t], U_t, the level ℓ(q) (`Nat.findGreatest`), the height h(q)
(`Finset.sup` over ≪-chains; Mathlib's `Order.coheight` is ℕ∞-valued and costs more than it saves), R(e,x),
classes (a)–(c), (O1)–(O4), "P ∩ R ≅ π_s" as `OrdIso (word (P ∩ R)) π_s`, and the lens.

Steps: Lemma 2.1(a), (b), (d) (250–400 lines; (c) is not used). A relative-level lemma (200–300): under
(O1)–(O3), for q in Q = P ∩ R, ℓ(q) − ℓ(e) and h(q) − h(x) are the longest chains of Q ending and starting at q.
That turns the "levels" and "heights" paragraphs into a finite computation on π₀, π₁, closed by `decide`. The
inside set {p₁, p₂, p₃} uses (O4) (150–250). The board with its two missing cells uses step C and 2.1(a), (d)
(250–400). Lemma 1.2 in counting form (a lens fibre adds exactly 1 to the difference) is about 150 lines more.

## 4. Main risks

1. Mis-stated definitions (off-by-one in ℓ, strict versus weak order). Mitigation: test every statement on small
   S_n in Lean and against `verify_fibers.py` and `gadget_check.py` before proving it.
2. Lemma 3 is bookkeeping-heavy and its estimate is the least certain. The splitting lemma of step A is awkward
   with the sublist-based `Contains`; an index-map form may have to be proved first.
3. W91 has been reviewed only by AI agents, with corrections after each review, and is recorded as "claimed, not
   externally verified". Formalising Lemma 2.3 doubles as an audit, and its statement may still move.

## 5. What cannot realistically be formalised

The pinned Mathlib (v4.33.1, sources searched) lacks every probabilistic tool that W91 uses:

* **Poisson point processes and the Mecke equation.** Mathlib has the Poisson distribution on ℕ only: no point
  processes, no Mecke or Campbell formula, no proof that the order type of a Poisson sample of size n is uniform.
* **First-moment bounds.** They integrate probabilities of events defined through ℓ, h and LIS over pairs of
  points, so they need the previous item plus measurability of all these functionals.
* **Talagrand's inequality.** Absent. Azuma–Hoeffding exists but gives fluctuations of order √n, the order of
  E LIS itself; the argument needs the n^{1/4} scale.
* **LIS asymptotics.** Logan–Shepp/Vershik–Kerov and Baik–Deift–Johansson are absent (no RSK, no hook-length formula).

Each is a library project of months to years. The realistic end state is the deterministic layer in Lean, with
the probabilistic theorems as explicit hypotheses, never as axioms.
