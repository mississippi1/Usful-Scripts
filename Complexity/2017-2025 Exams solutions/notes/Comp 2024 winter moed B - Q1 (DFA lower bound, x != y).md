# Comp 2024 winter (חורף) moed B — Q1 (25 pts): DFA lower bound for L_k = {xy : x ≠ y}

**Question.** For k ∈ ℕ, L_k = { xy : x, y ∈ {0,1}^k and x ≠ y }.
(a) Show that every DFA deciding L_k must have at least 2^k states.

This is the "lower bound for NFA determinization" question: L_k has an NFA with O(k²)
states, yet every DFA needs ≥ 2^k — so the subset construction's blowup is unavoidable.

## Reading the definition: exactly k, not at most k

`{0,1}^k` means words of length **exactly** k (Σ^k = Σ·Σ···Σ, k times).
"At most k" would be written Σ^{≤k} = ⋃_{i=0}^{k} Σ^i.

Consequences of "exactly k":
- L_k ⊆ Σ^{2k}, and |L_k| = 2^k(2^k − 1) = 4^k − 2^k. Finite ⇒ regular, so a DFA exists
  and the only question is its size.
- The split is **unique**, so membership is a positional condition:
  w ∈ L_k ⟺ |w| = 2k and ∃ i ∈ [k] : w_i ≠ w_{k+i}.
  That is exactly what the small NFA guesses, and it is what forces a DFA to remember
  the entire first half.
- Under "≤ k" membership becomes an existential over split points and the language
  degenerates (see Version 3 below) — though the 2^k bound survives.

## (a) Solution — pigeonhole on the 2^k possible first halves

Let D = (Q, Σ, δ, q₀, F) be a DFA with L(D) = L_k, and let δ̂ be the extended transition
function. Assume for contradiction |Q| ≤ 2^k − 1.

The map x ↦ δ̂(q₀, x) sends the 2^k words of {0,1}^k into Q, |Q| < 2^k, so by pigeonhole
there exist **distinct** x ≠ x' ∈ {0,1}^k with

    δ̂(q₀, x) = δ̂(q₀, x') = q.

Feed both the same suffix z = x (note |z| = k):

    δ̂(q₀, x·x)  = δ̂(δ̂(q₀,x),  x) = δ̂(q, x)
    δ̂(q₀, x'·x) = δ̂(δ̂(q₀,x'), x) = δ̂(q, x)

Both runs end in the same state, so D accepts xx iff it accepts x'x. But

- xx  ∉ L_k — the only legal split is into two length-k blocks, and they are equal;
- x'x ∈ L_k — |x'| = |x| = k and x' ≠ x.

Contradiction ⇒ |Q| ≥ 2^k. ∎

**Myhill–Nerode phrasing.** S = {0,1}^k is pairwise distinguishable w.r.t. L_k: for x ≠ x'
the suffix z = x gives x'z ∈ L_k but xz ∉ L_k. Hence ≡_{L_k} has ≥ 2^k classes, and the
minimal DFA has exactly MN(L_k) states, so every DFA has ≥ 2^k states.

### Three details

1. **Direction of the suffix.** z = x gives xx ∉ L_k, x'x ∈ L_k. (z = x' works
   symmetrically: x'x' ∉ L_k, xx' ∈ L_k.) Naming z explicitly is where points are lost.
2. **|z| must be exactly k.** Any z with |z| ≠ k puts both xz and x'z outside Σ^{2k}, so
   both are rejected and z separates nothing. The choice z = x is essentially forced.
3. **Partial DFAs.** The bound still holds: every x' ∈ Σ^k must have a defined run (a dead
   run would reject x'x'' for every x''), so pigeonhole applies to the defined states.

### How tight is 2^k?

2^k is an underestimate; the exam only asks for it. In fact all 2^{k+1} − 1 words of
length ≤ k are pairwise distinguishable:
- |u| = |v| = i ≤ k, u ≠ v: take z = 0^{k−i} v 0^{k−i} ⇒ uz ∈ L_k, vz ∉ L_k.
- |u| = i < |v| = j: take any z with vz ∈ L_k; then |uz| = 2k − (j−i) ≠ 2k ⇒ uz ∉ L_k.

The true minimal DFA is Θ(2^k). Brute force (Myhill–Nerode over all words of length
≤ 2k+1): **5, 12, 25, 50** states for k = 1, 2, 3, 4 (≈ 3·2^k).

### The NFA counterpart (why the question exists)

NFA with O(k²) states: guess the mismatch position i ∈ [k] and the bit b = w_i, walk k
more letters, verify w_{k+i} ≠ b, with a position counter enforcing |w| = 2k. Each (i,b)
branch is a chain of 2k+1 states ⇒ ~2k² states.

So: an NFA with m = O(k²) states whose minimal DFA needs ≥ 2^k = 2^{Ω(√m)} states.
Determinization really can cost exponentially many states.

## Version 2a — x = y allowed (constraint dropped): A_k = {xy : x,y ∈ Σ^k} = Σ^{2k}

Just "length = 2k". Minimal DFA = **2k + 2** states (counter q₀..q_{2k} + dead state);
verified 4, 6, 8 for k = 1, 2, 3.

The 2^k bound collapses to Θ(k), and the proof visibly dies: for x ≠ x' now both xx ∈ A_k
and x'x ∈ A_k, so z = x separates nothing — indeed all words of Σ^k are ≡_{A_k}-equivalent.
All the hardness lived in the "≠".

## Version 2b — x = y required: E_k = {xx : x ∈ Σ^k}

Bound **survives**, same proof with the two cases swapped: if δ̂(q₀,x) = δ̂(q₀,x') for
x ≠ x', then xx and x'x reach the same state, yet xx ∈ E_k and x'x ∉ E_k. So every DFA for
E_k has ≥ 2^k states (measured minimal: 5, 11, 23, 47 for k = 1..4).

**Contrast worth remembering:** for E_k even *NFAs* need 2^k states. Fooling set
S = {(x,x) : x ∈ Σ^k}: each x·x ∈ E_k, but for x ≠ x' the crossed word x·x' ∉ E_k — the
extended-fooling-set condition ⇒ any NFA for E_k has ≥ 2^k states. The exponential
DFA/NFA gap in (a) is a property of the *inequality* version: "≠" is cheap for an NFA
(guess one witnessing position), "=" requires checking all k positions.

## Version 3 — at most k: M_k = {xy : x,y ∈ Σ^{≤k}, x ≠ y}

Now a word may split many ways and it suffices that *some* split works.

**Characterization.** For |w| = n the legal split points are max(0, n−k) ≤ i ≤ min(k, n),
i.e. n+1 options when n ≤ k and 2k−n+1 options when k < n ≤ 2k. Any *unbalanced* split
(i ≠ n−i) is automatically good, since |x| ≠ |y| forces x ≠ y. At most one split point is
balanced, so ≥ 2 legal split points already puts w in M_k. Therefore:

- n = 0: only ε = ε·ε with x = y ⇒ ε ∉ M_k;
- 1 ≤ n ≤ 2k−1: ≥ 2 legal splits ⇒ w ∈ M_k unconditionally;
- n = 2k: unique split i = k ⇒ w ∈ M_k iff the halves differ, i.e. iff w ∈ L_k.

    M_k = { w : 1 ≤ |w| ≤ 2k − 1 } ∪ L_k        (brute-force verified for k = 1,2,3)

**Lower bound unchanged: ≥ 2^k.** The witnesses live at length 2k, where M_k agrees with
L_k: for x ≠ x' ∈ Σ^k colliding on the same state, z = x gives xx ∉ M_k and x'x ∈ M_k.
Measured minimal DFA: 5, 12, 25, 50 for k = 1..4 — identical to L_k, since the two
languages differ only on short words the prefix structure already separates.

So "≤ k" changes the language a lot (it swallows every nonempty word shorter than 2k) but
not the answer to (a): the bound is driven entirely by the length-2k layer.

Fourth combination, for completeness: {xy : x,y ∈ Σ^{≤k}} = Σ^{≤2k}, minimal DFA 2k+2
states (4, 6, 8 verified) — trivial again.

## Summary

| language | words | DFA lower bound | minimal DFA (k = 1..4) |
|---|---|---|---|
| L_k = {xy : \|x\|=\|y\|=k, x ≠ y} | ⊆ Σ^{2k} | **2^k** | 5, 12, 25, 50 |
| E_k = {xx : \|x\|=k} | ⊆ Σ^{2k} | 2^k (also for NFAs) | 5, 11, 23, 47 |
| {xy : \|x\|=\|y\|=k} = Σ^{2k} | = Σ^{2k} | Θ(k) — collapses | 2k+2 |
| M_k = {xy : \|x\|,\|y\| ≤ k, x ≠ y} | Σ^{1..2k−1} ∪ L_k | 2^k (unchanged) | 5, 12, 25, 50 |
| {xy : \|x\|,\|y\| ≤ k} = Σ^{≤2k} | = Σ^{≤2k} | Θ(k) | 2k+2 |

## Issues log

- **Q1(a)** — Uncertainty whether `x, y ∈ {0,1}^k` means length exactly k or at most k.
  Resolved: exactly k (Σ^k is length-exactly-k; "at most" would be Σ^{≤k}), so L_k ⊆ Σ^{2k}
  with a unique split and the positional condition ∃i: w_i ≠ w_{k+i}. Also checked that the
  "≤ k" variant M_k = {w : 1 ≤ |w| ≤ 2k−1} ∪ L_k still needs ≥ 2^k states, so the reading
  does not change part (a)'s answer.
- **Q1(a)** — How to run the lower-bound argument. Resolved: pigeonhole the 2^k words of
  Σ^k into the state set, get x ≠ x' reaching the same state, then append z = x — xx ∉ L_k
  (equal halves) vs x'x ∈ L_k (differing halves) — contradiction. Key subtlety: the
  distinguishing suffix must have length exactly k, so z = x is forced.
- **Q1 variants** — Asked what happens if x = y is allowed. Resolved: dropping "≠" gives
  Σ^{2k} and the bound collapses to 2k+2 states (all of Σ^k becomes equivalent); *requiring*
  x = y gives E_k = {xx}, where 2^k still holds by the same argument and additionally holds
  for NFAs via the fooling set {(x,x)}.
