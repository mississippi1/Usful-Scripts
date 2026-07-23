# Comp 2022-1 moed B — Q7 & Q10 (study notes)

*(Source exam: `Complexity/2017-2025 Exams/Comp 2022-1 moed B.pdf`;
official solution: `Complexity/2017-2025 Exams solutions/Comp 2022-1 moed B solution.pdf`.
Part III, "חלק III (46 נק')" — prove or disprove claims about languages L₁, L₂, L₃ over Σ.)*

---

## Q7 (7 pts) — mixing ≤m and ≤_L does not compose to ≤_L

**Claim:** if `L₁ ≤m L₂` **and** `L₂ ≤_L L₃`, then `L₁ ≤_L L₃`.

**Answer: לא נכונה (FALSE).**

The two premises use *different* reduction strengths: `≤m` is an **arbitrary computable** (mapping)
reduction; `≤_L` is a **logspace** reduction. Composing them yields only `L₁ ≤m L₃` (the weaker `≤m`
dominates — a computable map followed by a logspace map is just computable), **not** `L₁ ≤_L L₃`. So the
conclusion is strictly stronger than what the premises give, and the claim fails.

**Counterexample.** Take **L₂ = L₃ = {a}** over Σ = {a} (a fixed language in **L** = deterministic
logspace), and **L₁ = any language that is *decidable* but *not in L***. Then:

- `L₁ ≤m L₂`: L₁ ∈ R and L₂ is nontrivial, so map `f(x) = a` if `x ∈ L₁`, else `ε` (`ε ∉ {a}`). f is
  computable (simulate a decider for L₁, output a constant word), so `L₁ ≤m L₂`. ✓
- `L₂ ≤_L L₃`: identity function (L₂ = L₃), computable in constant space. ✓
- `L₁ ≰_L L₃`: if `L₁ ≤_L {a}`, then since `{a} ∈ L` and **L is closed under ≤_L**, we'd get `L₁ ∈ L` —
  contradicting the choice of L₁ ∉ L. ✗

**Two valid choices for L₁:**
- The **official solution** uses `L₁ ∈ EXPTIME ∖ P` (exists by the time hierarchy theorem); then
  `L₁ ≤_L {a}` ⇒ `L₁ ∈ L ⊆ P`, contradicting `L₁ ∉ P`.
- **L₁ = TQBF** works equally well (arguably cleaner — a concrete, named language). The only property
  needed is **L₁ ∉ L**, and `TQBF ∉ L` is a one-line space-hierarchy argument: TQBF is
  **PSPACE-complete**, so `TQBF ∈ L ⟹ PSPACE = L`, contradicting `L ⊊ PSPACE` (Space Hierarchy Theorem).
  ⚠ Justify **TQBF ∉ L**, *not* "TQBF ∉ P" — whether TQBF ∈ P is the open P-vs-PSPACE question; the
  counterexample only requires that TQBF is not in *logspace*, which is provable.

---

## Q10 (10 pts) — A_NFA ≤p A_DFA

Reminder: `A_NFA = {⟨A,w⟩ : A is an NFA and w ∈ L(A)}`, `A_DFA = {⟨A,w⟩ : A is a DFA and w ∈ L(A)}`.

**Claim:** `A_NFA ≤p A_DFA`.

**Answer: נכונה (TRUE) — unconditionally** (not "unknown", so no collapse like P = NP is involved).

**Key fact: `A_NFA ∈ P`** (in fact NL). Decide ⟨A,w⟩ by **on-the-fly subset simulation** — never
determinize the whole NFA:
- `S₀` = ε-closure of A's start states;
- `Sᵢ` = ε-closure of `⋃_{q ∈ Sᵢ₋₁} δ(q, wᵢ)` for i = 1 … |w|;
- accept iff `S_{|w|}` contains an accepting state.

Each `Sᵢ ⊆ Q` and there are |w| steps, so this is polynomial in |A|,|w|. (This is the "finite set of
possibilities per state" intuition made precise — track the *set* of reachable states, not one guessed
run.)

**The reduction.** Once `A_NFA ∈ P` and `A_DFA` is **nontrivial** (some ⟨DFA,w⟩ are members, some are
not), the generic decide-then-map reduction works:

> given ⟨A,w⟩, decide `A_NFA` in poly time; output a fixed **yes**-instance of `A_DFA` (a trivial DFA
> that accepts a fixed word, with that word) if accepted, a fixed **no**-instance otherwise.

This is a polynomial-time many-one reduction, so `A_NFA ≤p A_DFA` holds — no complexity assumption
needed. (Same phenomenon as `Comp 2025-1 moed A` Q8.א: under ≤p, `A ≤p (nontrivial P-language) ⟺ A ∈ P`;
here A_NFA ∈ P, so the reduction exists outright.) The exponential blow-up of NFA→DFA determinization is
irrelevant — the reduction never builds an equivalent DFA.

**Why "unknown ⇒ P = NP" is wrong here.** `P = NP` would be the answer only if `A_NFA` were **NP-hard**
(then `A_NFA ≤p A_DFA ∈ P` would give `NP ⊆ P`). But `A_NFA` is **not** NP-hard — it is in P — so nothing
open is at stake; the claim is just true.

---

## Issues log

- **Q7** — **Correct.** Disproved the claim and chose **L₁ = TQBF**. Valid: with L₂ = L₃ = {a} ∈ L, the
  premises hold (L₁ ≤m {a} since TQBF decidable + {a} nontrivial; {a} ≤_L {a} by identity) while
  `L₁ ≤_L {a}` would force `TQBF ∈ L`, impossible since TQBF is PSPACE-complete and `L ⊊ PSPACE` (Space
  Hierarchy). Watch-out: the justification must be **TQBF ∉ L**, not "TQBF ∉ P" (the latter is open). The
  official solution used an `EXPTIME ∖ P` language; TQBF is an equally correct, more concrete choice.

- **Q10** — **Incorrect.** Chose "נכונותה לא ידועה" and marked **P = NP, NP = coNP**; the correct answer
  is **נכונה (TRUE)**. Mistake: reasoning "NFA-acceptance is in NP", which would tie the reduction to a
  collapse *only if* A_NFA were NP-hard. Resolved: **A_NFA ∈ P** (poly-time subset simulation — exactly
  the "finite possibilities per state" instinct in the second half of the question), and A_DFA is
  nontrivial, so the decide-then-map poly reduction gives `A_NFA ≤p A_DFA` **unconditionally** — no
  P = NP needed. The self-correction ("maybe it is in P") was the right track and lands on the true answer.
