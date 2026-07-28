# Study guide — the Time Hierarchy Theorem, proof walkthrough

Sources: `Complexity/lessons/lesson 10.pdf` §10.1 (משפט היררכיה בזמן, Lemmas + Example 10.1.1 +
Corollary 10.1.1); `Complexity/תרגול 12 (4).pdf`; distilled entries **D4/D5/G5/G6** in
`Complexity/PROOFS_REFERENCE.md`.

---

## 0. Get the statement right first

A frequent mis-statement is:

> "there is a language computable in `O(f(n))` but not in `o(f(n)·log f(n))`"

That is **impossible as written**: `O(f) ⊆ o(f·log f)`, so anything satisfying the first half
satisfies the second half automatically. The log factor sits on the other side of the gap. The two
correct phrasings:

| Phrasing | Statement |
|---|---|
| **Course version** (Lecture 10) | for time-constructible `f`: `TIME(o(f(n))) ⊊ TIME(f(n)·log f(n))` — i.e. some language is decidable in `O(f·log f)` but **not** in `o(f)` |
| **Rescaled (Sipser) version** | for time-constructible `t`: some language is decidable in `O(t(n))` but not in `o(t(n)/log t(n))` |

They are the same theorem: substitute `t = f·log f`, note `log t = Θ(log f)`, so
`f = Θ(t/log t)`. The rescaled form is what "computable in `O(f)` but not in `o(f/log f)`" means —
the log **divides**, it does not multiply.

Two more framing points:

- It is a **language** (a decision problem), not a function. The diagonal argument needs a yes/no
  answer to flip.
- `f` must be **time-constructible**: `f(n) = Ω(n log n)`, and the map `1ⁿ ↦ ⟨f(n)⟩₂` is computable
  in `O(f(n))` time. This is exactly what lets the decider compute its own step budget without
  blowing the budget.

---

## 1. The witness language

```
A_f = { ⟨M,w⟩ : M accepts w, and the run of M on w ends within f(|w|) steps }
```

Everything else is two lemmas about this one language.

---

## 2. Lemma 1 (upper bound) — `A_f ∈ TIME(f(n)·log f(n))`

**Decider** on input `x`:

1. check `x` parses as `⟨M,w⟩` with `M` a TM encoding — linear time; reject if not;
2. `t := f(|w|)` — `O(f(n))` by time-constructibility;
3. universal-simulate `M` on `w`, maintaining a counter initialized to `t` and decremented per
   simulated step; abort the simulation when the counter hits 0;
4. accept iff the simulation reached `q_accept` before the budget ran out.

**Correctness (both directions, state them):**

- `⟨M,w⟩ ∈ A_f` ⟹ the accepting run is `≤ f(|w|)` steps, so the counter never cuts it off, and the
  decider accepts.
- `⟨M,w⟩ ∉ A_f` ⟹ either `M(w)` halts without accepting (simulation finishes, decider rejects), or
  the run exceeds `f(|w|)` steps (the counter cuts it off, decider rejects).

**Where the `log f` comes from** — the only substantive point of this lemma, and its own
טענת עזר in the lecture. Simulating one step of `M` universally is `O(1)` amortized; the extra cost
is **maintaining the step counter**, which is `log t` bits wide:

- counter parked at a fixed tape position ⟹ the head walks up to `t` cells there and back on every
  simulated step ⟹ `O(t²)` total (the naive bound);
- counter carried in a track alongside the simulation head (the "movable counter" construction,
  exercise 3/5) ⟹ `O(log t)` per step to shift and decrement ⟹ **`O(t·log t) = O(f·log f)`**.

So `A_f ∈ TIME(f·log f)`. ∎

---

## 3. Lemma 2 (lower bound) — `A_f ∉ TIME(o(f(n)))`

Assume for contradiction `M_f` decides `A_f` in time `g(n) = o(f(n))`. Diagonalize.

**The diagonal language.**

```
A_self = { ⟨M⟩ : ⟨M, ⟨M⟩⟩ ∈ A_f }      "M accepts its own encoding within f steps"
```

`A_self ∈ TIME(o(f))`: on input `⟨M⟩`, duplicate the input to form `⟨M,⟨M⟩⟩` (linear, and
`n = O(f(n))`), then run `M_f`. Its complement `co-A_self` is in the same class **because `M_f` is a
decider** — swap the accepting and rejecting states, no time cost. Let `M′` be a machine deciding
`co-A_self` within `o(f)`.

**The self-application.** What does `M′(⟨M′⟩)` return?

- **Case `M′` accepts `⟨M′⟩`.** Then `⟨M′⟩ ∈ co-A_self`, so `⟨M′⟩ ∉ A_self`, so
  `⟨M′,⟨M′⟩⟩ ∉ A_f`. By the definition of `A_f`, that means either
  1. `M′` does not accept `⟨M′⟩` — false, we just assumed it accepts; or
  2. `M′(⟨M′⟩)` ran for more than `f(|⟨M′⟩|)` steps — impossible, `M′` runs in `o(f)`, which is
     strictly below `f` on all large enough inputs.

  Both options die. Contradiction.
- **Case `M′` rejects `⟨M′⟩`.** Then `⟨M′⟩ ∉ co-A_self`, so `⟨M′⟩ ∈ A_self`, so
  `⟨M′,⟨M′⟩⟩ ∈ A_f`, which by definition says `M′` **accepts** `⟨M′⟩`. Contradiction.

Both branches are contradictory, so no such `M_f` exists. ∎

Combining Lemma 1 and Lemma 2: `A_f` separates `TIME(o(f))` from `TIME(f·log f)`. ∎

### 3.1 The pitfall to cite explicitly

The hypothesis is `o(f)`, **not** `O(f)`, and that is precisely what kills option (2) in the first
case. With only `O(f)` the "rejected because over budget" escape hatch stays open: `M′` could
genuinely accept `⟨M′⟩` after more than `f(n)` steps, and there is no contradiction. This is also why
the theorem cannot be stated as `TIME(f) ⊊ TIME(f·log f)`.

### 3.2 Fine print the lecture glosses (know it, cite if asked)

- **Padding for "large enough n".** `o(f)` only gives `time_{M′}(n) < f(n)` for `n ≥ n₀`, but
  `|⟨M′⟩|` is a single fixed number that may be below `n₀`. Standard patch: TM encodings admit
  padding — let `⟨M′⟩10^k` denote the same machine for every `k` — pick `k` with
  `|⟨M′⟩10^k| ≥ n₀`, and run the argument on the padded encoding.
- **Input duplication changes the length.** `⟨M,⟨M⟩⟩` is a constant factor longer than `⟨M⟩`, so
  the composed running time is `g(O(n))`; concluding it is still `o(f(n))` uses the tacit niceness
  assumption `f(O(n)) = O(f(n))`, which every `f` used in practice (`nᵏ`, `2ⁿ`, …) satisfies.

---

## 4. Why there is a gap at all — and why space is tighter

The theorem separates `o(f)` from `f·log f`, not `f` from `f·log f`. Two independent losses:

1. **the diagonalization needs strict slack** (`o(f)`, §3.1);
2. **universal simulation with a clock costs `log f`** (§2).

The space version, `SPACE(o(f)) ⊊ SPACE(f)`, is **tighter — no log factor** — because a universal
TM simulates with only constant-factor *space* overhead: the space counter needs `log f` bits, which
is dominated by the `f` cells already allotted, whereas a time counter costs `log f` *per step*.
The lecture states the consequence directly: improving the time hierarchy would require a more
time-efficient universal machine with a counter.

| | Simulation overhead | Resulting theorem |
|---|---|---|
| Time | `O(log f)` per step (counter maintenance) | `TIME(o(f)) ⊊ TIME(f·log f)` |
| Space | `O(1)` factor (counter fits inside the budget) | `SPACE(o(f)) ⊊ SPACE(f)` |

---

## 5. Corollaries (how it actually shows up on exams)

- **`TIME(n²) ⊊ TIME(n³)`** [Lecture Example 10.1.1] — take `f(n) = n^{2.5}` (time-constructible).
  Then `n² = o(n^{2.5})`, so the theorem gives `L ∈ TIME(n^{2.5}·log n^{2.5}) ⊆ TIME(n³)` with
  `L ∉ TIME(n²)`.
- **`P ⊊ EXP`** [Corollary 10.1.1] — take `f(n) = 2ⁿ`. Every polynomial is `o(2ⁿ)`, so `L ∉ P`,
  while `L ∈ TIME(2ⁿ·n) ⊆ EXP`.
- **`P ≠ ⋃_{i≤k} TIME(nⁱ)` for every fixed `k`** [Rec12 Claim 1.5] — otherwise
  `P ⊆ TIME(nᵏ) ⊊ TIME(n^{k+1}) ⊆ P`, a set strictly contained in itself.
- **`PSPACE ⊊ EXPSPACE`, `L ⊊ PSPACE`, `NL ⊊ PSPACE`** — the space version (`NL ⊆ SPACE(log²n)` by
  Savitch, then space hierarchy).

---

## 6. Exam traps

1. **Wrong side for the log.** "In `O(f)` but not in `o(f·log f)`" is vacuous nonsense. It is either
   `O(f·log f)` / not `o(f)`, or `O(f)` / not `o(f/log f)`.
2. **`O` instead of `o` in the lower bound.** The proof collapses (§3.1).
3. **Crossing resources.** The *space* hierarchy theorem says nothing about a poly-*time* reduction,
   and vice versa — hierarchy theorems separate strictly within one resource. (This exact mistake is
   logged on 2025-1 moed A Q8.א.)
4. **Crossing determinism.** The deterministic proof uses free complementation of a decider
   (`co-A_self`), which a nondeterministic machine does not have. The nondeterministic time
   hierarchy is a different (lazy-diagonalization) proof.
5. **Forgetting time-constructibility.** Without it the decider cannot compute `t = f(|w|)` inside
   its budget, and the theorem is false in general (Gap Theorem territory).
6. **Claiming a strict separation the theorems do not give.** Only the four hierarchy separations are
   proven; `P` vs `NP`, `P` vs `PSPACE`, `NL` vs `P` are open.
