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

## Can you reduce from ALL_TM instead?

**In principle yes, but it is the wrong tool.** ALL_TM = { ⟨M⟩ : L(M) = Σ* } **is** coRE-hard
(Ā_TM ≤m ALL_TM), so ALL_TM ≤m L would give coRE-hardness by transitivity, and such a reduction does
exist. Two costs make it a bad choice:

**1. Extra proof burden.** ALL_TM is **not coRE-complete** — the formula sheet's page-4 table lists it
under $\overline{RE ∪ coRE}$ (it is Π⁰₂-complete, strictly above coRE). Reducing from it means you
must *also* prove ALL_TM is coRE-hard first. NON-HALT is coRE-**complete**, a citable one-liner —
one reduction instead of two.

**2. The polarity is hostile.** You would need L(M) = Σ* ⇒ L(M′) decidable, and L(M) ≠ Σ* ⇒ L(M′)
undecidable. The second case gives you almost nothing to work with — possibly just one missing word.
All the natural attempts die:

| attempt | ALL case | non-ALL case | verdict |
|---|---|---|---|
| L(M′) = L(M) | Σ* ✓ | L(M) could be ∅ — decidable | ✗ |
| L(M′) = L(M) ∪ A_TM | Σ* ✓ | L(M) = Σ*∖{x₀} with x₀ ∈ A_TM ⇒ union = Σ* | ✗ |
| L(M′) = { x : M accepts all z with \|z\| ≤ \|x\| } | Σ* ✓ | shortest missing word at length m ⇒ { x : \|x\| < m }, **finite** | ✗ |

The third row is the **same length-threshold collapse** as Pitfall 1.

### The useful lesson: the budget gadget is right, the target was wrong

The standard proof of Ā_TM ≤m ALL_TM is *exactly* the step-budget construction that fails here:

> M′ on x: simulate M on w for |x| steps; **accept iff M has not accepted w within |x| steps**.
> M doesn't accept w ⇒ L(M′) = Σ* ✓; M accepts w at step t ⇒ L(M′) = { x : |x| < t } ≠ Σ* ✓

Same machine, same budget, same finite length-threshold language — and against **ALL_TM** it works
perfectly, because a finite set is emphatically **not Σ***. Against **"L(M) ∈ R"** the identical
construction is useless, because a finite set **is decidable**.

> **The gadget is real and reusable; it just needs a target property that length thresholds can
> distinguish.** `= Σ*` can see them. `∈ R` cannot — every length-threshold language falls on the
> same side of it.

*(Beyond course scope: ALL_TM ≤m L exists because L is Σ⁰₃-complete while ALL_TM is Π⁰₂ ⊆ Σ⁰₃ — a
degree-theoretic guarantee, not a construction worth writing.)*

---

## L is RE-hard as well (not asked, but worth knowing)

The question asks only for coRE-hardness, but **A_TM ≤m L** holds too, so L is hard for *both*
classes. Given ⟨M,w⟩, let M′ on input x **dovetail** two threads:

- (a) simulate M on w; if it accepts, accept x;
- (b) test x ∈ A_TM (parse x = ⟨N,y⟩ and simulate N on y); if so, accept x.

Then:

- **M accepts w** ⇒ thread (a) eventually accepts every x ⇒ L(M′) = Σ* ∈ R ⇒ ⟨M′⟩ ∈ L
- **M does not accept w** ⇒ thread (a) never fires ⇒ L(M′) = A_TM ∉ R ⇒ ⟨M′⟩ ∉ L

So A_TM ≤m L, i.e. **L is RE-hard**. Combined with the coRE-hardness above, L is hard for RE and for
coRE simultaneously — exactly what you expect of a language sitting far above both (Σ⁰₃-complete).
coRE-hardness is just the slice the question happens to ask for.

*(Note the polarity flip between the two reductions: for coRE-hardness the "good" case is the one
where M **fails** to halt, giving L(M′) = ∅; for RE-hardness the "good" case is where M **succeeds**,
giving L(M′) = Σ*. Both use a trivial decidable language on the yes-side and A_TM on the no-side.)*

---

## The contrast that matters most — { ⟨M⟩ : L(M) ∈ coRE ∖ R } is trivial

These two look nearly identical and land at opposite extremes:

| language | answer |
|---|---|
| { ⟨M⟩ : L(M) ∈ **R** } (this doc) | RE-hard **and** coRE-hard; far outside RE ∪ coRE |
| { ⟨M⟩ : L(M) ∈ **coRE ∖ R** } (Comp 2025-2026 moed A Q5) | **R** — the language is **∅** |

The first is a genuine non-trivial semantic property: ∅ ∈ R and A_TM ∉ R give the two witnesses Rice
requires. The second is **unsatisfiable**, because L(M) ∈ RE always and RE ∩ coRE = R, so
`coRE ∖ R` is empty once restricted to languages of the form L(M).

**Produce the two witnesses before proving anything** — that single check separates these two cases
and costs ten seconds. See
`Study guide - empty-language traps (when a machine property is unsatisfiable).md`.

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

- **Part (ג) (follow-up 2)** — Asked whether the reduction could instead come from **ALL_TM**.
  Answer: possible in principle but the wrong tool, for two reasons. (1) ALL_TM is **not
  coRE-complete** — it is Π⁰₂-complete, listed under $\overline{RE ∪ coRE}$ on the formula sheet's
  page-4 table — so using it as a source adds the burden of first proving Ā_TM ≤m ALL_TM, i.e. two
  reductions where NON-HALT (coRE-**complete**) needs one. (2) The required polarity
  ("L(M) ≠ Σ* ⇒ L(M′) undecidable") gives almost nothing to work with, and every natural attempt
  fails: L(M′) = L(M) breaks when L(M) = ∅; L(M′) = L(M) ∪ A_TM breaks when L(M) = Σ*∖{x₀} with
  x₀ ∈ A_TM; and L(M′) = { x : M accepts all z with |z| ≤ |x| } yields a **finite** language in the
  non-ALL case — the same length-threshold collapse as Pitfall 1. Resolved with the connection worth
  keeping: the step-budget gadget the student kept reaching for **is** the textbook proof of
  Ā_TM ≤m ALL_TM, and it works there because a finite length-threshold language is not Σ*. It fails
  against "L(M) ∈ R" because that same finite language *is* decidable. The gadget is sound and
  reusable — it just needs a target property that length thresholds can distinguish.

- **Part (ג) (follow-up 3)** — Asked for a full walkthrough of the coRE-hardness argument. Two
  sections added above. (1) **L is RE-hard too**: A_TM ≤m L via an M′ that dovetails "simulate M on
  w, accept x if it accepts" with "accept x iff x ∈ A_TM", giving L(M′) = Σ* ∈ R when M accepts w
  and L(M′) = A_TM ∉ R otherwise — so L is hard for RE and coRE simultaneously, as expected of a
  Σ⁰₃-complete language; coRE-hardness is only the slice the question asks for. Note the polarity
  flip between the two reductions: coRE-hardness puts the *decidable* language on the
  non-halting side, RE-hardness on the halting side. (2) **The contrast with
  { ⟨M⟩ : L(M) ∈ coRE ∖ R }** (Comp 2025-2026 moed A Q5), which is trivially **R** because L(M) is
  always RE and RE ∩ coRE = R — nearly identical phrasing, opposite extremes, separated by the
  ten-second check of producing the two Rice witnesses. Also re-emphasized in the walkthrough that
  the reduction f never runs M on w; it only *writes source code* for M′ by plugging the fixed
  strings ⟨M⟩ and w into a template, which is why f is total and computable.
