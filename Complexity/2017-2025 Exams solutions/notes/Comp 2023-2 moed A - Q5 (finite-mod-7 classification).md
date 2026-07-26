# Comp 2023-2 (קיץ 2023) moed A — Q5 (12 pts, class classification): finite language, size ≡0 mod 7

Source exam: `Complexity/2017-2025 Exams/Comp 2023-2 moed A.pdf` (page 6)
Official solution: `Complexity/2017-2025 Exams solutions/Comp 2023-2 moed A solution.pdf` (page 6)

**Question.** Define L = { ⟨M⟩ : |L(M)| < ∞ and |L(M)| mod 7 = 0 }. Which computability
class does L belong to: R, RE\R, coRE\R, or complement(RE∪coRE)?

## Answer: complement(RE∪coRE) — neither RE nor coRE (student's circled answer is correct,
matches the official solution)

## Proof — two reductions from A_TM (matches the official solution)

### L ∉ coRE — reduce A_TM to L

Given ⟨M,w⟩, build K: on input x,

    if x = w·0^i for some 1 ≤ i ≤ 6:  accept
    if x = w:                         simulate M on w, answer the same
    otherwise:                        reject

- ⟨M,w⟩ ∈ A_TM (M accepts w): L(K) = {w, w·0, w·00, …, w·0⁶} — exactly 7 strings. Finite,
  7 mod 7 = 0 ⟹ ⟨K⟩ ∈ L.
- ⟨M,w⟩ ∉ A_TM (M rejects or loops on w): L(K) = {w·0, …, w·0⁶} — exactly 6 strings.
  Finite, 6 mod 7 ≠ 0 ⟹ ⟨K⟩ ∉ L.

So A_TM ≤m L. Since A_TM ∉ coRE, L ∉ coRE.

### L ∉ RE — reduce co-A_TM to L

Given ⟨M,w⟩, build K': fix 7 arbitrary distinct constant strings w1,…,w7 (not depending on
M,w). On input x,

    if x ∈ {w1,…,w7}:  accept
    otherwise:         simulate M on w; accept x iff M accepts w

- ⟨M,w⟩ ∈ co-A_TM (M does not accept w): only the 7 baseline strings ever get accepted ⟹
  L(K') = {w1,…,w7}, exactly 7, 7 mod 7 = 0 ⟹ ⟨K'⟩ ∈ L.
- ⟨M,w⟩ ∉ co-A_TM (M accepts w): every x∉{w1,…,w7} eventually gets accepted too (the
  simulation succeeds, and its outcome doesn't depend on x) ⟹ L(K') = Σ* — infinite ⟹
  ⟨K'⟩ ∉ L.

So co-A_TM ≤m L. Since co-A_TM ∉ RE, L ∉ RE.

## Combining

L ∉ RE and L ∉ coRE, so L ∈ complement(RE ∪ coRE). ∎

## Alternate route — reduce FIN_TM directly (mentioned in the official solution as
"additional method")

FIN_TM = {⟨M⟩ : |L(M)| < ∞} is itself a classic example of neither RE nor coRE (same style
of two-directional reduction from A_TM/co-A_TM, applied to plain finiteness instead of
finiteness-with-residue). Given that fact, a single reduction transfers both
non-memberships at once:

Given ⟨M⟩, build M' that on input ⟨y,i⟩ (encoding a pair, y∈Σ*, i∈{1,…,7}) accepts iff M
accepts y (ignoring i entirely). Then L(M') = L(M) × {1,…,7}, so:

    |L(M')| = 7·|L(M)|   whenever |L(M)| < ∞   (always a multiple of 7!)
    |L(M')| = ∞          whenever |L(M)| = ∞

So ⟨M⟩ ∈ FIN_TM ⟺ ⟨M'⟩ ∈ L — a valid reduction FIN_TM ≤m L. Since FIN_TM ∉ RE and
FIN_TM ∉ coRE, both facts transfer to L through this one mapping. ∎

## Why this fits the running quantifier-pattern cheat sheet

L is "FIN_TM intersected with a residue condition that's automatically satisfiable once you
control the count in multiples of 7." The residue condition itself is decidable-once-you-
know-the-count, so it doesn't add hardness on its own — it's FIN_TM's own hardness (the
∀-over-RE structure hiding inside "finite": |L(M)|<∞ ⟺ ∃n ∀w(|w|>n → ¬Accept(M,w)), an
∃n[coRE(n)] statement, generically neither RE nor coRE) doing all the work, and ×7 padding
preserves it losslessly. See "Comp 2020 summer moed B - Q5-Q6" and
"Comp 2024 summer moed B - Q5" notes for the rest of this pattern family.

## Issues log

- **Q5** — Given as a marked-answer classification question (student circled
  complement(RE∪coRE)); confirmed against the official solution PDF. Verified via the two
  A_TM/co-A_TM-based reductions above, plus a slicker single-reduction alternate (FIN_TM≤mL
  via a ×7 pairing trick) that transfers both non-RE and non-coRE status from the
  already-known classification of FIN_TM in one step.
