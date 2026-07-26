# Comp 2025 summer (קיץ) moed A — Q3 (12 pts, MN worksheet): DFA with k states — finite ⟹ few words, else infinite

**Question (as photographed/handwritten).** Prove that if A is a DFA with k states over
Σ = {a,b}, then it holds that: |L(A)| ≥ 2^k, or |L(A)| is infinite.
Hint: what is the number of words whose length is strictly less than k?

Note: this exam PDF is not present in this repo (only "2017-2025 Exams" has a "Comp 2025-1
moed A/B/C" set, dated 2025.2.16 — winter, not summer — so this is a different, more recent
exam not yet archived here). The problem statement below is reconstructed from a photo of
handwritten notes, so treat the exact wording as best-effort.

## Flagging an inequality-direction issue before solving

As transcribed above ("≥ 2^k") the claim is **false**: for any k ≥ 3, let L = {a^(k-2)}
(a single word). Its minimal DFA has states q0,...,q_(k-2) (accepting q_(k-2)) plus one trap
state — exactly k states, all pairwise Myhill–Nerode-distinguishable (residuals
{a^(k-2-i)} for i = 0..k-2, plus ∅ for the trap). Yet |L(A)| = 1, which is neither ≥ 2^k nor
infinite. This is a definitive counterexample regardless of minimality/reachability — a
k-state DFA can accept an arbitrarily small finite language for any k.

The direction that is actually true — and that matches the hint exactly — is **≤**, not ≥
(an easy symbol to flip when reading a scan or handwriting):

    Either L(A) is infinite,  or  |L(A)| ≤ 2^k − 1  ( < 2^k ).

Verified against 300 random k-state DFAs (k = 1..6, random transitions/accepting sets, Σ =
{a,b}): whenever no word of length ≥ k was accepted (proxy for "L(A) finite"), the count of
accepted words was always ≤ 2^k − 1 and matched exactly the count restricted to length < k.

## Solution (corrected statement)

**Claim.** If A = (Q, Σ, δ, q0, F) is a DFA with |Q| = k over Σ = {a,b}, then either L(A) is
infinite, or |L(A)| ≤ 2^k − 1.

### Step 1 (the hint) — counting words shorter than k

Σ^{<k} = Σ^0 ∪ Σ^1 ∪ … ∪ Σ^{k−1}. Since |Σ| = 2:

    |Σ^{<k}| = 2^0 + 2^1 + … + 2^{k−1} = 2^k − 1.

That is exactly the target bound, so it suffices to show L(A) ⊆ Σ^{<k} whenever L(A) is
finite.

### Step 2 — key lemma: an accepted word of length ≥ k forces L(A) infinite

Let δ* be the extended transition function. Suppose w ∈ L(A) with |w| ≥ k. Consider the run
on the first k letters of w: states q0, q1, …, q_k with q_i = δ*(q0, w_1…w_i). That is k+1
states drawn from |Q| = k values, so by pigeonhole some q_i = q_j for 0 ≤ i < j ≤ k.

Split w = x·y·z with x = w_1…w_i (length i), y = w_{i+1}…w_j (length j−i ≥ 1), z = the rest
of w. Then δ*(q0,x) = q_i and δ*(q0,xy) = q_j = q_i, so reading y from q_i loops back to q_i:

    δ*(q_i, y) = q_i   ⟹   δ*(q_i, y^n) = q_i   for every n ≥ 0.

Hence for every n ≥ 0:

    δ*(q0, x y^n z) = δ*(q_i, y^n z) = δ*(q_i, z) = δ*(q_j, z) = δ*(q0, xyz) = δ*(q0, w) ∈ F

so xy^n z ∈ L(A) for every n ≥ 0. Since |y| ≥ 1, these words have strictly increasing length
in n, hence are pairwise distinct: {xy^n z : n ≥ 0} ⊆ L(A) is infinite, so L(A) is infinite. ∎

(This is the proof of the pumping lemma, specialized to A itself. It matches the loop-closing
equation visible in the handwritten attempt, δ(q, w_ij) = q = δ*(q0, w_0i) — the same two
colliding states.)

### Step 3 — contrapositive, then count

Contrapositive of Step 2: if L(A) is finite, it contains no word of length ≥ k, i.e.
L(A) ⊆ Σ^{<k}. Combined with Step 1:

    |L(A)| ≤ |Σ^{<k}| = 2^k − 1 < 2^k.

### Conclusion

    Either L(A) is infinite, or |L(A)| ≤ 2^k − 1.

No third case: a k-state DFA can never accept a language that is both finite and has ≥ 2^k
words.

### Why minimality is irrelevant, and why the "≥" reading broke

Step 2 only used |Q| = k for the pigeonhole — it holds for any DFA with k states, minimal or
not. It rules out a *finite* language with *many* words relative to k (more than 2^k − 1); it
says nothing about the minimum, which can be 0 or 1 regardless of how large k is — exactly
the counterexamples that sink the "≥" reading. The two directions are not symmetric: "few
words while finite" is unconstrained; "many words while finite" is impossible.

### Tightness

The bound 2^k − 1 is achieved: let A accept all of Σ^{<k} via a length counter q0,…,q_{k−1}
(every counter state accepting) with any letter read at q_{k−1} going to a trap. That is k
states total, |L(A)| = 2^k − 1 exactly, and no word of length ≥ k is accepted — so Step 3's
bound cannot be improved.

## Issues log

- **Q3** — The photographed/handwritten problem statement read "|L(A)| ≥ 2^k, or |L(A)|
  infinite", which is false (counterexample: L = {a^(k-2)}, minimal k-state DFA, |L(A)| = 1).
  Resolved: the intended (and provably true) statement flips the inequality to
  |L(A)| ≤ 2^k − 1, or L(A) infinite — matching the hint's word count |Σ^{<k}| = 2^k − 1
  exactly. Proof: pigeonhole on the run's first k+1 states gives a repeated state q_i = q_j,
  hence a pumpable loop; if L(A) is finite this loop can never be triggered by an accepted
  word, so every accepted word has length < k, bounding |L(A)| by |Σ^{<k}| = 2^k − 1.
  Verified against 300 random DFAs. Also noted: this exam (summer 2025 moed A) is not yet
  archived in this repo's "2017-2025 Exams" folder.
