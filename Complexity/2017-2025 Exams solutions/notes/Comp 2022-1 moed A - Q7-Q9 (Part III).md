# Comp 2022-1 (חורף) moed A — חלק III, Questions 7-9 (study notes)

Source exam: `Complexity/2017-2025 Exams/Comp 2022-1 moed A.pdf` (dated 24.1.22, מועד א חורף 2022),
חלק III (35 pts), Q7-Q9 (7 pts each). (Q10, NFA/DFA containment, is not covered here.)
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

## Exam checklist for this item

- [x] Mark **לא נכונה**; circle nothing.
- [x] Give the contradiction: ≤p is in particular a computable ≤m, SAT ∈ R, R closed under ≤m,
      so A_TM ∈ R — contradiction.
- [x] Say explicitly why SAT ∈ R (brute-force over assignments halts) — don't just assert it.
- [x] Note the direction principle: reductions go easy → hard, never hard → easy.

---

# Q8 (7 pts) — the claim

> Reminder: TQBF = { ⟨φ⟩ : φ is a true fully quantified Boolean formula }.
>
> **Claim:** TQBF ≤p A_TM

## Answer

**נכונה (TRUE), unconditionally.** Nothing is circled.

## Proof (the short version)

TQBF is **decidable** — TQBF ∈ PSPACE ⊆ R (evaluate the quantifier tree recursively, reusing space).
Fix once and for all a decider **M_TQBF** for it. Define

  f(x) = ⟨M_TQBF, x⟩.

⟨M_TQBF⟩ is a **constant** string baked into the reduction, so f just prints that constant and copies
x — linear time. And

  x ∈ TQBF ⟺ M_TQBF accepts x ⟺ ⟨M_TQBF, x⟩ ∈ A_TM. ∎

**The general fact behind it:** for *every* L ∈ RE, with recognizer M, the map x ↦ ⟨M, x⟩ shows
**L ≤p A_TM**. So A_TM is ≤p-hard for all of RE, and TQBF ∈ R ⊆ RE is just one instance. This is the
classic ≤m reduction from the computability part of the course; the only new observation is that it
happens to run in linear time, so it is a fortiori a ≤p reduction.

## Variant proof (hardcoding), and why the running time of the output machine is irrelevant

Alternative: f(⟨φ⟩) = ⟨M_φ, ε⟩ where M_φ hardcodes φ, ignores its input, evaluates φ, and accepts iff
φ is true. Writing that description is polynomial in |φ|.

Either way, the point students trip on: **M_φ (or M_TQBF) may run for exponential time** — that costs
nothing. A_TM asks only *whether* the machine accepts, not how fast. The polynomial budget constrains
the reduction f, not the machine f outputs.

## Why the "two constants" trick does NOT work here

Contrast with the PATH ≤p HAMCYCLE item (see the Comp 2020 summer moed A notes): there the reduction
could decide the source language itself and print one of two hard-coded instances. That needs the
source language in **P**. Here the source is TQBF, and TQBF ∈ P is exactly the open P = PSPACE
question — so the trick is unavailable and the honest construction above is required. The trick also
needs the *target* to be non-trivial, which A_TM is, but that is not the binding constraint.

---

# Q9 (7 pts) — the claim

> **Claim:** TQBF ≤p SAT

## Answer

**נכונותה לא ידועה (UNKNOWN).** Mark and prove **PSPACE = NP** and **NP = coNP**.
P = NP, PSPACE = P and NL = P do **not** follow.

## Why unknown

The claim is *equivalent* to PSPACE = NP, which is open (and believed false):

- If TQBF ≤p SAT then TQBF ∈ NP (SAT ∈ NP, NP closed under ≤p), and by PSPACE-completeness that
  forces PSPACE ⊆ NP (below).
- Conversely if PSPACE = NP then TQBF ∈ NP, and SAT is NP-complete, so TQBF ≤p SAT.

Note that Q7's refutation style is unavailable here: both TQBF and SAT are **decidable**, so there is
no computability obstruction to exploit — only an open complexity question.

## The implications, proved

**PSPACE = NP.** Let L ∈ PSPACE be arbitrary. TQBF is PSPACE-complete, so L ≤p TQBF. By assumption
TQBF ≤p SAT, and ≤p is transitive, so L ≤p SAT. Since SAT ∈ NP and NP is closed under ≤p, L ∈ NP.
Hence PSPACE ⊆ NP; and NP ⊆ PSPACE always (enumerate certificates, reusing space — or
NP ⊆ NPSPACE = PSPACE by Savitch). ∎

**NP = coNP.** PSPACE is closed under complement (flip the accept/reject decision of a deterministic
poly-space decider — it always halts, and the space bound is unchanged). So
coNP = co(PSPACE) = PSPACE = NP. ∎

**Not P = NP / PSPACE = P / NL = P.** PSPACE = NP says nothing about where P sits inside that class;
no collapse to P follows. (No justification is required on the exam for statements you did not mark.)

## The three items side by side

| | claim | status | why |
|---|---|---|---|
| Q7 | A_TM ≤p SAT | **false** | undecidable ≤ decidable is impossible — computability, not complexity |
| Q8 | TQBF ≤p A_TM | **true** | x ↦ ⟨M_TQBF, x⟩; A_TM is ≤p-hard for all of RE |
| Q9 | TQBF ≤p SAT | **open** | equivalent to PSPACE = NP; implies NP = coNP |

The unifying principle: a reduction A ≤p B says *A is no harder than B*. Q8 reduces into a strictly
harder (undecidable) target — free. Q7 tries the reverse and dies outright. Q9 stays inside the
decidable world where the ordering between the two is genuinely unknown.

## Exam checklist for Q8-Q9

- [x] Q8: mark **נכונה**, circle nothing; give f(x) = ⟨M_TQBF, x⟩ and say **why TQBF is decidable**.
- [x] Q8: state that ⟨M_TQBF⟩ is a constant, so f is linear-time — that is what makes it ≤p and not
      merely ≤m.
- [x] Q9: mark **לא ידוע**, mark PSPACE = NP and NP = coNP, and **prove both** (the exam says "סמנו
      והוכחו").
- [x] Q9: the PSPACE = NP proof needs transitivity of ≤p plus PSPACE-completeness of TQBF — write
      both steps.

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
- **Q8 (TQBF ≤p A_TM):** Resolved as **נכונה, unconditionally**, nothing circled. Cleanest proof
  recorded: TQBF ∈ PSPACE ⊆ R, so fix a decider M_TQBF and map x ↦ ⟨M_TQBF, x⟩ — ⟨M_TQBF⟩ is a
  constant baked into the reduction, so this is linear time, hence ≤p and not merely ≤m. General fact
  extracted: **A_TM is ≤p-hard for all of RE** via x ↦ ⟨M, x⟩ for a recognizer M. Two traps cleared:
  (1) the output machine may run in exponential time — A_TM only asks *whether* it accepts, and the
  polynomial budget binds the reduction, not the machine it prints; (2) the "print one of two
  constants" trick from the PATH ≤p HAMCYCLE item is **not** available here, since it would require
  TQBF ∈ P, i.e. P = PSPACE.
- **Q9 (TQBF ≤p SAT):** Resolved as **לא ידוע**, marking **PSPACE = NP** and **NP = coNP** (and
  proving both, as the exam demands). Chain recorded: L ∈ PSPACE ⟹ L ≤p TQBF ≤p SAT by transitivity
  ⟹ L ∈ NP since NP is closed under ≤p; with NP ⊆ PSPACE always, that gives PSPACE = NP, and then
  coNP = co(PSPACE) = PSPACE = NP because PSPACE is closed under complement. Noted the claim is
  *equivalent* to PSPACE = NP (converse via Cook–Levin), and that P = NP, PSPACE = P, NL = P do not
  follow. Also noted why Q7's refutation style fails here: TQBF and SAT are both decidable, so there
  is no computability obstruction — only an open complexity question.
