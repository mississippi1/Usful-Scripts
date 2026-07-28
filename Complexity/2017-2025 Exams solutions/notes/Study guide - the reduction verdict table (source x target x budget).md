# The reduction verdict table — source × target × budget

Every `A ≤_r B` question on every paper in the archive is one lookup in the grids below.

Companion to `Study guide - classifying a language (P, NP-complete, PSPACE-complete).md`, which
derives the machinery (constant-output lemma, closure, the interval test). This doc is the
**lookup table** built from it, with named languages instead of abstract classes.

---

# 1. The one rule

Let A be a language complete for class **C₁**, and B a non-trivial language complete for class
**C₂**, both under `≤_r`. Then:

> ### `A ≤_r B`  is TRUE  ⟺  `C₁ ⊆ closure_r(C₂)`

where `closure_r(C₂)` is the **smallest ≤_r-closed class containing C₂**.

*Why both directions hold:*
- **(⇐)** If `C₁ ⊆ C₂`, use B's completeness. If `C₁ ⊆ closure_r(C₂)` only via the closure being
  bigger, use the **constant-output lemma**: the reducer decides A within budget r and prints one
  of two hardcoded strings. Printing is free — the output tape is write-only.
- **(⇒)** `B ∈ C₂ ⊆ closure_r(C₂)`, which is ≤_r-closed, so `A ∈ closure_r(C₂)`. Since A is
  C₁-complete under ≤_r, all of C₁ follows.

So the verdict is **TRUE / FALSE / UNKNOWN** exactly as the inclusion `C₁ ⊆ closure_r(C₂)` is
known-true, known-false, or open. **You are never reasoning about the languages — only about two
classes and one budget.**

## The closure table — this is the whole difference between the budgets

| C | `closure_L(C)` | `closure_p(C)` | `closure_m(C)` |
|---|---|---|---|
| L | **L** | **P** ⚠️ | R |
| NL | **NL** | **P** ⚠️ | R |
| P | P | P | R |
| NP | NP | NP | R |
| coNP | coNP | coNP | R |
| PSPACE | PSPACE | PSPACE | R |
| EXP | EXP | EXP | R |
| R | R | R | **R** |
| RE | RE | RE | **RE** |
| coRE | coRE | coRE | **coRE** |

**Read off the three consequences:**

1. **`≤L` and `≤p` differ only when the TARGET is `L` or `NL`.** Everywhere else the columns are
   identical. A poly-time reducer may burn poly time *before* writing anything, so a target in NL
   is worth no more to it than a target in P.
2. **`≤m` erases every distinction among decidable classes** — `closure_m` of all of them is R.
   Hence the entire decidable `≤m` grid is TRUE (§5). This is why the exams only ask `≤m`
   questions about *undecidable* languages.
3. **The finer the budget, the more FALSE verdicts you can prove.** `≤L` is the sharpest
   instrument, `≤m` the bluntest.

## The four proven separations (the only licence for a FALSE verdict)

`L ⊊ PSPACE`  ·  `NL ⊊ PSPACE`  ·  `P ⊊ EXP`  ·  `PSPACE ⊊ EXPSPACE`

**The interval test.** For `C₁ ⊆ C₂?`, form the span `[C₂, C₁]` and ask whether some proven
separation `X ⊊ Y` fits inside it — i.e. `C₂ ⊆ X` **and** `Y ⊆ C₁`. Fits ⟹ **FALSE**. Does not
fit ⟹ **UNKNOWN**, and name the open problem.

⚠️ **Never compare endpoints.** None of the four separations is between adjacent classes, so a
proven separation can sit inside a span built entirely from open steps.

---

# 2. Candidate languages per class

Pick the canonical one; the whole point of §1 is that any complete language behaves identically.

| class | canonical | others (and the ones from your papers) |
|---|---|---|
| **L** | `EVEN = {w : \|w\| even}` | `ST-Conn₂₀₂₂` (2022-2 moed B Q8), `ST-Conn_c` for constant c, `EXACT5`, `CYC₁₀₀` |
| **NL** | **`PATH`** | `PATH‾`, `2SAT`, `ALL_DFA`, `CYC`, `EVENDIST`, `DISCONN` (2022-2 moed C Q9), `LongPath` = "distance ≥ k" (2022-2 moed A Q7) |
| **P** | **`CVP`** (circuit value) | `LP`, `A_DFA`, `E_DFA` |
| **NP** | **`SAT`** | `3SAT`, `CLIQUE`, `VC`, `IS`, `HAMPATH`, `HAMCYCLE`, `SUBSET-SUM`, `LargeCycle`, `2MON`, `2-Clique`, `ALT-SAT`, `E-SET-COVER`, `HALF-VC` |
| **coNP** | **`TAUTOLOGY`** | `UNSAT`, `NON-HAMPATH` |
| **PSPACE** | **`TQBF`** | `ALL_NFA`, `EQ_NFA`, `EQ_REX`, generalized geography |
| **EXP** | generalized chess / succinct-circuit problems | (rarely named in this course — you mostly need EXP as a *class* for the hierarchy theorem) |
| **R** | `SAT`, `TQBF` | `A_DFA`, `EQ_DFA`, `A_LBA` — **every** decidable language |
| **RE-complete** | **`HALT`** | `A_TM` |
| **coRE-complete** | **`HALT‾`** | `A_TM‾`, `E_TM = {⟨M⟩ : L(M) = ∅}`, `NON-HALT` |
| **neither** | `TOTAL` | `EQ_TM`, `REG_TM`, `{⟨M⟩ : L(M) ∈ P}`, `{⟨M⟩ : ∃w, M doesn't halt on w}` |

⚠️ **L has no known ≤L-complete language.** The `L` column still works, because
`A ≤L B` for non-trivial `B ∈ L` is equivalent to `A ∈ L` outright (constant-output one way, `L`
closed under `≤L` the other). So read the L column as "**B is any non-trivial language in L**".

---

# 3. Grid A — `≤L` (logspace reductions)

**Rows = source A. Columns = target B.** Entry answers "`A ≤L B`?"

✓ TRUE · ✗ FALSE · ? UNKNOWN (with the open problem it is equivalent to)

| A ↓ \ B → | **L** | **NL** | **P** | **NP** | **coNP** | **PSPACE** | **EXP** |
|---|---|---|---|---|---|---|---|
| **L** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| **NL** | ? `L=NL` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| **P** | ? `L=P` | ? `NL=P` | ✓ | ✓ | ✓ | ✓ | ✓ |
| **NP** | ? `L=NP` | ? `NL=NP` | ? `P=NP` | ✓ | ? `NP=coNP` | ✓ | ✓ |
| **coNP** | ? `L=coNP` | ? `NL=coNP` | ? `P=NP` | ? `NP=coNP` | ✓ | ✓ | ✓ |
| **PSPACE** | **✗** | **✗** | ? `P=PSPACE` | ? `NP=PSPACE` | ? `coNP=PSPACE` | ✓ | ✓ |
| **EXP** | **✗** | **✗** | **✗** | ? `NP=EXP` | ? `coNP=EXP` | ? `PSPACE=EXP` | ✓ |

**The five FALSE cells, and the separation that kills each:**

| cell | reads | refuted by |
|---|---|---|
| `TQBF ≤L EVEN` | PSPACE ⊆ L | `L ⊊ PSPACE` |
| `TQBF ≤L PATH` | PSPACE ⊆ NL | `NL ⊊ PSPACE` |
| EXP-complete `≤L EVEN` | EXP ⊆ L | `P ⊊ EXP` (L ⊆ P) |
| EXP-complete `≤L PATH` | EXP ⊆ NL | `P ⊊ EXP` (NL ⊆ P) |
| EXP-complete `≤L CVP` | EXP ⊆ P | `P ⊊ EXP` |

**Everything on or above the diagonal is ✓** — that is the constant-output/completeness half, and
it never needs thought. All the content is strictly below the diagonal.

⚠️ **The row that surprises everyone: EXP.** `EXP ⊆ NP` is **open**, not false. The interval test
is why: to refute it you need a proven `X ⊊ Y` with `NP ⊆ X` and `Y ⊆ EXP`. `P ⊊ EXP` needs
`NP ⊆ P` — not known. `PSPACE ⊊ EXPSPACE` needs `EXPSPACE ⊆ EXP` — false. Nothing fits.
(Contrast: `EXPSPACE ⊆ NP` **is** FALSE, since `PSPACE ⊊ EXPSPACE` fits the span `[NP, EXPSPACE]`.)

---

# 4. Grid B — `≤p` (polynomial-time reductions)

Same grid with columns **L** and **NL** replaced by the **P** column, since
`closure_p(L) = closure_p(NL) = P`.

| A ↓ \ B → | **L** | **NL** | **P** | **NP** | **coNP** | **PSPACE** | **EXP** |
|---|---|---|---|---|---|---|---|
| **L** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| **NL** | ✓ 🔄 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| **P** | ✓ 🔄 | ✓ 🔄 | ✓ | ✓ | ✓ | ✓ | ✓ |
| **NP** | ? `P=NP` | ? `P=NP` | ? `P=NP` | ✓ | ? `NP=coNP` | ✓ | ✓ |
| **coNP** | ? `P=NP` | ? `P=NP` | ? `P=NP` | ? `NP=coNP` | ✓ | ✓ | ✓ |
| **PSPACE** | ? `P=PSPACE` 🔄 | ? `P=PSPACE` 🔄 | ? `P=PSPACE` | ? `NP=PSPACE` | ? `coNP=PSPACE` | ✓ | ✓ |
| **EXP** | **✗** | **✗** | **✗** | ? `NP=EXP` | ? `coNP=EXP` | ? `PSPACE=EXP` | ✓ |

## 🔄 The five cells where `≤L` and `≤p` disagree — memorise these

| cell | `≤L` | `≤p` | why it moves |
|---|---|---|---|
| NL → L | ? `L=NL` | **✓** | poly time can just *decide* the NL source |
| P → L | ? `L=P` | **✓** | same |
| P → NL | ? `NL=P` | **✓** | same |
| **PSPACE → L** | **✗** | **?** `P=PSPACE` | ⚠️ loses the proven `L ⊊ PSPACE` |
| **PSPACE → NL** | **✗** | **?** `P=PSPACE` | ⚠️ loses the proven `NL ⊊ PSPACE` |

**The bottom two are the exam's favourite trap** — this is `ALL_NFA ≤p PATH` vs `ALL_NFA ≤L PATH`
(2025-1 moed A Q8.א), the claim you got wrong. Same claim, two budgets, two different verdicts:

- `TQBF ≤L PATH` → **FALSE.** `closure_L(NL) = NL`, so the claim says `PSPACE ⊆ NL`, and
  `NL ⊊ PSPACE` is a theorem.
- `TQBF ≤p PATH` → **UNKNOWN.** `closure_p(NL) = P`, so the claim only says `PSPACE ⊆ P` — open.

⚠️ Note also that cells like NP → L keep the **same verdict** but change **which open problem**
they are equivalent to (`L=NP` under `≤L`, `P=NP` under `≤p`). Exams ask you to name it.

⚠️ And the EXP row does **not** move: `EXP ⊆ P` is refuted by `P ⊊ EXP`, and widening the target
from L to P does not help. **A proven separation survives the budget change when it straddles the
closure; it dies when the closure swallows it.**

---

# 5. Grid C — `≤m` (any computable reduction)

`closure_m(C) = R` for every decidable class. So for **every** pair of non-trivial decidable
languages, `A ≤m B` is:

> ## ✓ TRUE — all 49 cells

Decide A (taking as long as you like — `≤m` has **no** budget), print one of two constants.
`TQBF ≤m SAT`, `SAT ≤m EVEN`, EXP-complete `≤m PATH` — all true, all trivially.

**Therefore an `≤m` question is only ever interesting when a language is undecidable**, which is
the grid below.

---

# 6. Grid D — computability

Rows/columns as before; `closure_r(R) = R`, `closure_r(RE) = RE`, `closure_r(coRE) = coRE` for
**every** budget r, so **this one grid is correct for `≤m`, `≤p` and `≤L` alike.**

| A ↓ \ B → | **R** (`SAT`) | **RE-c** (`HALT`) | **coRE-c** (`HALT‾`) | **neither** (`TOTAL`) |
|---|---|---|---|---|
| **R** (`SAT`) | ✓ | ✓ | ✓ | ✓ |
| **RE-c** (`HALT`) | **✗** | ✓ | **✗** | ✓ |
| **coRE-c** (`HALT‾`) | **✗** | **✗** | ✓ | ✓ |
| **neither** (`TOTAL`) | **✗** | **✗** | **✗** | ✓ |

**Every cell is decided — there are no UNKNOWNs in computability.** All the separations are
theorems (`R ⊊ RE`, `RE ∩ coRE = R`, the arithmetical hierarchy is strict), unlike complexity
where almost everything is open. Worth internalising: **a computability claim always has a
provable answer; a complexity claim usually does not.**

The two cells people get wrong:

- **`HALT ≤ₘ HALT‾` is FALSE.** It would give `HALT ∈ coRE`, and with `HALT ∈ RE` and
  `RE ∩ coRE = R`, `HALT ∈ R`. This is also why **`A ≤ₘ B` does *not* give `Ā ≤ₘ B`** — it gives
  `Ā ≤ₘ B̄`. Polarity, not direction.
- **`SAT ≤ₘ HALT` is TRUE**, and so is `SAT ≤p HALT`. Undecidability of the *target* never
  obstructs anything; the budget constrains the **mapping**, not the targets. (Likewise
  `HALT ≤p A_TM` is TRUE — the reject-to-accept rewrite is linear time.)

---

# 7. Using it under exam pressure

**Triage in one glance — look at the SOURCE first:**

- **Source weaker than target** (on or above the diagonal) ⟹ **TRUE**. Say which lemma:
  *completeness of the target* if `C₁ ⊆ C₂`, or the *constant-output lemma* if the budget alone
  already decides A. Write one line, move on. This is half the marks and needs no thought.
- **Source stronger than target** ⟹ the claim is a **class collapse in disguise**. Now do work.

**Then, for the below-diagonal cells, three steps:**

1. Write `closure_r(C₂)` — the **only** step where the budget matters. Read it off by budget:

   | budget | what to write for `closure_r(C₂)` |
   |---|---|
   | `≤L` | `C₂` unchanged, always |
   | `≤p` | `C₂` unchanged — **except `L` and `NL`, which both become `P`** |
   | `≤m` | **`R`** if `C₂` is any decidable class; `RE` if `C₂ = RE`; `coRE` if `C₂ = coRE` |

   ⚠️ **`≤m` is not "≤p with a bigger exception list" — it flattens everything.** If the budget is
   `≤m` and both languages are decidable, you are already done: `C₁ ⊆ R` holds for every decidable
   `C₁`, so the answer is **TRUE** and you never reach steps 2–3. An `≤m` question only has
   content when a language is **undecidable** (Grid D).
2. State the claim as the inclusion `C₁ ⊆ closure_r(C₂)`.
3. Run the interval test. Fits a proven separation ⟹ **FALSE**, cite it. Otherwise ⟹
   **UNKNOWN**, and **name the open problem** — the papers award marks for naming it.

**The three sentences worth having verbatim:**

> "Since `B` is `C₂`-complete under `≤_r` and `C₂` is closed under `≤_r`, the claim implies
> `C₁ ⊆ C₂`."

> "`A` is decidable within budget `r` and `B` is non-trivial, so the reduction decides `A` and
> prints one of two hardcoded constants — the output tape is write-only and uncharged."

> "This is equivalent to `⟨open problem⟩`, so its truth is unknown."

**Two things that are never reasons for FALSE:**
- the target being undecidable (Grid D, bottom rows: `SAT ≤p HALT` is fine);
- the source being hard for a bigger class, unless a **proven** separation fits the span
  (`TQBF ∉ NP` is *unknown*, not false).

---

## Issues log

- **(2026-07-28)** Written after difficulty applying the abstract class-vs-class grid in
  `Study guide - classifying a language` to concrete claims (`TQBF ≤L SAT`, `TQBF ≤p PATH`,
  `SAT ≤p PATH`, `PATH ≤p SAT`, …). Resolved by collapsing everything to the single rule
  `A ≤_r B ⟺ C₁ ⊆ closure_r(C₂)` and tabulating all three budgets over the seven complexity
  classes plus the computability classes. Key findings recorded: (1) `≤L` and `≤p` disagree in
  **exactly five cells**, all with target `L` or `NL`, and the two that matter are
  `PSPACE → L/NL` flipping FALSE → UNKNOWN; (2) the whole decidable `≤m` grid is TRUE;
  (3) `EXP ⊆ NP` is open, not false — the interval test, not endpoint comparison, is what decides
  the EXP row; (4) the computability grid has no UNKNOWN cells at all.
