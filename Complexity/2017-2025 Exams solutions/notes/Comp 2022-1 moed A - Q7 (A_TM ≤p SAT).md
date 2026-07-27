# Comp 2022-1 (חורף) moed A — חלק III, Question 7 (study notes)

Source exam: `Complexity/2017-2025 Exams/Comp 2022-1 moed A.pdf` (dated 24.1.22, מועד א חורף 2022),
חלק III (35 pts), Q7 (7 pts).
Official solution: `Complexity/2017-2025 Exams solutions/Comp 2022-1 moed A solution.pdf`.

חלק III instructions: mark each claim נכונה / לא נכונה / נכונותה לא ידועה; if "לא ידוע", mark **and
prove** which of P=NP, NP=coNP, PSPACE=NP, PSPACE=P, NL=P would follow from the claim being true.
(Note this exam's list differs from the 2020 one — it has PSPACE=NP and NL=P instead of P≠NP.)

## Q7 — the claim

> **Claim:** A_TM ≤p SAT

## Answer

**לא נכונה (FALSE)** — and provably so, with no assumption and no open problem involved.
**Nothing is circled**; the five-statement list only applies when marking "נכונותה לא ידועה".

## Proof

Assume toward contradiction that A_TM ≤p SAT via a poly-time computable f.

1. **≤p ⊆ ≤m.** A machine computing f in polynomial time is in particular a TM computing f that
   **halts on every input**, so f is a computable mapping reduction.
2. **SAT ∈ R.** Given φ over n variables, enumerate all 2ⁿ assignments and evaluate each.
   Exponential time, but it always halts — decidability is all we need here.
3. **R is closed downward under ≤m.** If A ≤m B via f and B ∈ R with decider D_B, then A is decided
   by: on x, compute f(x), run D_B on f(x), output its answer. This halts on every input (f total,
   D_B a decider) and is correct since x ∈ A ⟺ f(x) ∈ B.
4. By 1–3, **A_TM ∈ R**.
5. But **A_TM ∉ R** — undecidable, by the diagonalization proof from class.

Contradiction; no such f exists. ∎

## Why this is a computability question wearing a complexity costume

This is the trap. The item sits in the P/NP part, the claim is written with ≤p, and five collapse
statements are dangled — so the reflex is "unknown, would imply P=NP". But the refutation never
touches time bounds:

- A reduction A ≤ B in **any** of these senses says *A is no harder than B*. Here A is **undecidable**
  and B is **decidable** — a gap no reduction can bridge.
- The proof uses only that f is **total and computable**. It equally refutes A_TM ≤m SAT,
  A_TM ≤L SAT, and any reduction notion with computable maps. The "p" in ≤p plays no role.
- If P = NP were proved tomorrow, the claim would *still* be false. That independence is precisely
  the signal that nothing should be circled.

## The neighbouring items (same part) sharpen the contrast

- **Q8: TQBF ≤p A_TM — TRUE.** Map ⟨φ⟩ to ⟨M_φ, w⟩ where M_φ hardcodes φ, ignores its input,
  evaluates φ, and accepts iff φ is true. Writing that machine description is polynomial in |φ|, and
  ⟨φ⟩ ∈ TQBF ⟺ ⟨M_φ, w⟩ ∈ A_TM. Reducing *into* the undecidable language is the harmless direction.
- **Q9: TQBF ≤p SAT — UNKNOWN**, and this is where circling happens: it would give **PSPACE = NP**
  (TQBF is PSPACE-complete, SAT ∈ NP, NP closed under ≤p), and hence **NP = coNP** (PSPACE is closed
  under complement, so NP = PSPACE = coPSPACE = coNP). PSPACE = P and NL = P do not follow.

Across the three: false by computability, true by construction, genuinely open. Q7's job is to check
you notice the first one is not about complexity at all.

## Exam checklist for this item

- [x] Mark **לא נכונה**; circle nothing.
- [x] Give the contradiction: ≤p is in particular a computable ≤m, SAT ∈ R, R closed under ≤m,
      so A_TM ∈ R — contradiction.
- [x] Say explicitly why SAT ∈ R (brute-force over assignments halts) — don't just assert it.
- [x] Note the direction principle: reductions go easy → hard, never hard → easy.

---

## Issues log

Track here which parts gave trouble, and how they were resolved.

- **Q7 (A_TM ≤p SAT — the "לא נכונה" marking on the answer sheet, is it right?):** Yes, correct, and
  nothing should be circled. Resolution recorded: a ≤p reduction is in particular a total computable
  mapping reduction, SAT ∈ R by brute force over assignments, and R is closed downward under ≤m —
  so the claim would make A_TM decidable, contradicting its undecidability. Key insight confirmed:
  despite living in the P/NP part and being written with ≤p, this is a **computability** refutation —
  it uses only totality and computability of f, so it also kills ≤m and ≤L, and would remain false
  even if P = NP were proved. That independence from all five listed statements is exactly why the
  circling row stays empty. Contrast noted with the neighbours: Q8 (TQBF ≤p A_TM) is **true** by
  hardcoding φ into a machine, and Q9 (TQBF ≤p SAT) is the genuinely **open** one, implying
  PSPACE = NP and NP = coNP.
