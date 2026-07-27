# "L(M) ∈ R" is coRE-hard — part (ג) (source exam unidentified)

**Question.** Define L ≝ { ⟨M⟩ : L(M) ∈ R }. Show that L is **coRE-hard**.

*(Labeled part (ג) of a multi-part question. Searched all 21 PDFs in
`Complexity/2017-2025 Exams/` — text layers where present, rendered pages for the three scans
(`Comp 2022-2 moed B`, `Comp 2024-2 moed A`, `Comp 2024-2 moed B`) — and this question does not
appear in any of them. Likely from a תרגיל / תרגול sheet or an external source. Rename/merge this
doc if the exam is identified.)*

---

## Answer

Reduce from **NON-HALT** = { ⟨M,w⟩ : M does not halt on w }, which is **coRE-complete**
(HALT_TM is RE-complete). Since ≤m is transitive, K ≤m NON-HALT ≤m L for every K ∈ coRE.

### Construction (unbounded simulation — the clean version)

f(⟨M,w⟩) = ⟨M′⟩ where **M′ on input x**:

1. Simulate M on w (no step budget).
2. If the simulation halts, parse x as ⟨N,y⟩ and **accept iff N accepts y** (i.e. accept iff x ∈ A_TM).

**Correctness.**

- **M does not halt on w** ⇒ step 1 never returns, for *every* x ⇒ M′ accepts nothing ⇒
  **L(M′) = ∅ ∈ R** ⇒ ⟨M′⟩ ∈ L.
- **M halts on w** ⇒ step 1 always returns ⇒ **L(M′) = A_TM ∉ R** ⇒ ⟨M′⟩ ∉ L.

So ⟨M,w⟩ ∈ NON-HALT ⟺ ⟨M′⟩ ∈ L.

**Computability of f.** M′ is obtained by plugging the fixed strings ⟨M⟩ and w into a fixed program
template. No simulation happens at reduction time — the reduction only *writes code*. ∎

### Variant with a |x|-step budget (also correct, but needs one extra lemma)

**M′ on input x:** simulate M on w for **|x| steps**; if it has not halted, **reject**; if it has
halted, accept iff x ∈ A_TM.

- **M does not halt on w** ⇒ the budget always expires ⇒ L(M′) = ∅ ∈ R ✓
- **M halts on w in exactly t steps** ⇒ inputs with |x| < t are rejected, inputs with |x| ≥ t are
  accepted iff x ∈ A_TM. So

      L(M′) = A_TM ∖ S,   S = A_TM ∩ { x : |x| < t }  is **finite**.

  **Extra lemma needed: R is closed under finite symmetric difference.** If D decided L(M′), then
  A_TM would be decided by: on input x, if |x| ≥ t run D(x); otherwise consult a **hard-coded finite
  lookup table** for the strings of length < t. Such a machine *exists* — decidability is an
  existence claim, not a construction, so it does not matter that we cannot compute the table.
  Hence A_TM ∈ R, contradiction ⇒ L(M′) ∉ R. ✓

The budget therefore buys nothing here and costs an extra argument. It is worth using only when the
construction genuinely needs M′ to be **total**.

---

## Pitfalls

### 1. A step budget alone can NEVER work (both branches must not be trivial)

The single most common way to break this reduction: make both branches trivial actions
(accept / reject / loop), so that the only non-trivial thing M′ does is check the step budget.
Every such attempt fails, and there is a clean reason why.

> **Impossibility.** If M′'s behaviour on x depends **only on |x|**, then L(M′) is determined by a
> set S ⊆ ℕ of accepted lengths. In a budget construction S is
> { n : M halts on w within n steps } or its complement — and that predicate is **monotone in n**,
> so S is always ∅, ℕ, { n ≥ t }, or { n < t }. All four languages are regular, hence **decidable**.

So no budget-only construction can ever leave R, **in either polarity**:

| "budget expired" branch | "M halted" branch | L(M′) when M halts on w at step t | in R? |
|---|---|---|---|
| reject | accept | { x : \|x\| ≥ t } (co-finite) | ✓ decidable |
| **accept** | **loop** | { x : \|x\| < t } (**finite**) | ✓ decidable |

Both rows give a decidable language, and the non-halting case gives ∅ or Σ* — also decidable. So f
maps *every* input to a yes-instance of L and carries no information whatsoever.

Note the second row's language is the set of **short** words, not the long ones: when |x| < t the
budget expires *before* M halts, so those are exactly the inputs that reach the "expired" branch.

**The fix, keeping either polarity:** replace the trivial branch with a hard one. E.g. budget
expired → accept; M halted → accept iff x ∈ A_TM. Then M doesn't halt on w ⇒ L(M′) = Σ* ∈ R, and
M halts at t ⇒ L(M′) = { x : |x| < t } ∪ (A_TM ∩ { x : |x| ≥ t }), which differs from A_TM on
finitely many strings and is therefore undecidable.

**The shape to remember:** simulating M on w is only a **switch** selecting *which* language M′
recognizes. At least one setting of that switch must be genuinely undecidable — the switch itself
can never supply that.

### 2. L(M) ∈ R is a property of the *language*, not of the *machine*

A machine that loops on every input is a perfectly good witness for ⟨M′⟩ ∈ L — its language is
∅, which is decidable. This is why the unbounded version is fine and no totality is required.

Contrast with **DECIDER_TM** = { ⟨M⟩ : M is a decider }, where the machine's halting behaviour *is*
the property; there a looping M′ would be fatal and a step budget genuinely earns its keep.

### 3. Direction of the reduction

coRE-hard means K ≤m L for K coRE-complete: reduce **from** NON-HALT (or Ā_TM) **into L**.
Reducing from HALT, or into L̄, proves **RE**-hardness instead. Cheap check: NON-HALT ∈ coRE ✓,
and the map sends its yes-instances to yes-instances of L ✓.

### 4. Rice gives undecidability, not hardness

"L(M) ∈ R" is a non-trivial semantic property (∅ ∈ R, A_TM ∉ R), so **Rice's theorem gives L ∉ R** —
but Rice says nothing about coRE-hardness, which is why the explicit reduction is required.

**Formula-sheet shortcut (good sanity check).** Theorem 4 ("if T_∅ ∉ P then A_TM ≤m L_P") does *not*
apply to P = "L(M) ∈ R", because ∅ ∈ R means T_∅ **is** in P. Apply it to the complement property
P′ = "L(M) ∉ R": now T_∅ ∉ P′, so A_TM ≤m L_{P′} = L̄, i.e. **Ā_TM ≤m L** — exactly coRE-hardness,
for free. A question phrased "הראו/הוכיחו" normally still wants the explicit construction.

---

## Where this language really sits

coRE-hard is a **weak** lower bound here. "L(M) is decidable" is the index set REC, which is
**Σ⁰₃-complete** — far outside RE ∪ coRE. So do not go hunting for a matching L ∈ coRE upper bound;
the exam is asking only for the one reduction.

---

## Issues log

- **Part (ג)** — Asked whether coRE-hardness can be shown by reducing from **NON-HALT**, with M′
  simulating M on w for **|x| steps** (budget = length of M′'s own input). **Yes, the approach is
  valid**, with two corrections. (1) The sketch was missing the essential part: the branch reached
  when the simulation *halts* must run something **undecidable** (accept iff x ∈ A_TM) — if M′ just
  accepts there, the halting case gives L(M′) = {x : |x| ≥ t}, which is regular and therefore
  decidable, so both cases fall inside L and the reduction fails. (2) The |x|-budget makes
  L(M′) = A_TM minus a **finite** set in the halting case, so the proof must additionally invoke
  closure of R under finite symmetric difference (a hard-coded finite lookup table exists even
  though it cannot be computed). Resolved: the **unbounded** simulation (run M on w to completion,
  then accept iff x ∈ A_TM) gives L(M′) = ∅ or exactly A_TM, avoiding the finite-difference lemma
  entirely. The instinct to add a step budget comes from constructions needing a **total** M′, which
  is unnecessary here because L(M) ∈ R constrains the *language*, not the machine — a machine
  looping on every input has L(M′) = ∅ ∈ R and is a valid yes-instance.

- **Part (ג) (follow-up)** — Tried the budget construction with **both branches trivial**: budget
  expired → **accept**, M halted → **loop forever**. Correctly suspected it fails, but identified
  the wrong language: it is the **finite** set { x : |x| < t } (the *short* words — when |x| < t the
  budget expires before M halts, so those are the inputs reaching the "accept" branch), not the long
  ones. Resolved: the failure is total, not partial — the non-halting case gives L(M′) = Σ* and the
  halting case gives a finite language, both decidable, so f maps *every* input to a yes-instance of
  L. Root cause: no undecidable ingredient anywhere. Generalized into the impossibility result now in
  Pitfall 1 — if M′'s behaviour depends only on |x|, the accepted-length set is
  { n : M halts on w within n steps } or its complement, which is **monotone**, hence always ∅, ℕ,
  { n ≥ t } or { n < t } — all regular. So a budget-only construction can never leave R in *either*
  polarity. Fix keeps the student's polarity: budget expired → accept, M halted → **accept iff
  x ∈ A_TM**, giving Σ* in the good case and a finite modification of A_TM in the bad one.
