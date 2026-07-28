# Drill sheet — 147 worked reduction claims

Complete coverage of **budget × source × target**: 3 budgets (`≤L`, `≤p`, `≤m`) × 7 source classes
× 7 target classes = 147 combinations, each with **3 concrete example claims**.

The same three language pairs serve all three budgets, so each row below gives 3 examples and
**three verdicts**. Reading a row across is the fastest way to see what the budget actually buys.

Companion to `Study guide - the reduction verdict table (source x target x budget).md`, which
derives the rule. This sheet is the worked instantiation.

---

## The rule being applied everywhere

> `A ≤_r B` is TRUE ⟺ `C₁ ⊆ closure_r(C₂)`

`closure_L` = identity. `closure_p` = identity **except `L, NL ↦ P`**. `closure_m` = `R` for every
decidable class.

**Legend:** ✓ TRUE · ✗ FALSE · ? UNKNOWN (equivalent open problem named)

## The language pools

| class | the three representatives used below |
|---|---|
| **L** | `EVEN = {w : \|w\| even}` · `PALINDROME` · `ST-Conn₂₀₂₂` |
| **NL** | `PATH` · `2SAT` · `ALL_DFA` |
| **P** | `CVP` · `HORN-SAT` · `A_CFG` |
| **NP** | `SAT` · `CLIQUE` · `HAMPATH` |
| **coNP** | `TAUTOLOGY` · `UNSAT` · `NON-HAMPATH` |
| **PSPACE** | `TQBF` · `ALL_NFA` · `EQ_REX` |
| **EXP** | `EXP-HALT = {⟨M,w,1ⁿ⟩ : M accepts w within 2ⁿ steps}` · `GEN-CHESS` · `SUCCINCT-CVP` |

⚠️ The **L** column means "target is any non-trivial language *in* L" — there is no known
≤L-complete language for L. The maths is unaffected: for non-trivial `B ∈ L`,
`A ≤L B ⟺ A ∈ L` and `A ≤p B ⟺ A ∈ P`.

---

# Source: **L** — `EVEN`, `PALINDROME`, `ST-Conn₂₀₂₂`

Every cell ✓ under every budget: the source is already decidable in logspace, so the
constant-output lemma fires at the tightest budget and *a fortiori* at the looser ones.

| target | 3 examples | ≤L | ≤p | ≤m |
|---|---|---|---|---|
| **L** | `EVEN ≤ PALINDROME` · `PALINDROME ≤ ST-Conn₂₀₂₂` · `ST-Conn₂₀₂₂ ≤ EVEN` | ✓ | ✓ | ✓ |
| **NL** | `EVEN ≤ PATH` · `PALINDROME ≤ 2SAT` · `ST-Conn₂₀₂₂ ≤ ALL_DFA` | ✓ | ✓ | ✓ |
| **P** | `EVEN ≤ CVP` · `PALINDROME ≤ HORN-SAT` · `ST-Conn₂₀₂₂ ≤ A_CFG` | ✓ | ✓ | ✓ |
| **NP** | `EVEN ≤ SAT` · `PALINDROME ≤ CLIQUE` · `ST-Conn₂₀₂₂ ≤ HAMPATH` | ✓ | ✓ | ✓ |
| **coNP** | `EVEN ≤ TAUTOLOGY` · `PALINDROME ≤ UNSAT` · `ST-Conn₂₀₂₂ ≤ NON-HAMPATH` | ✓ | ✓ | ✓ |
| **PSPACE** | `EVEN ≤ TQBF` · `PALINDROME ≤ ALL_NFA` · `ST-Conn₂₀₂₂ ≤ EQ_REX` | ✓ | ✓ | ✓ |
| **EXP** | `EVEN ≤ EXP-HALT` · `PALINDROME ≤ GEN-CHESS` · `ST-Conn₂₀₂₂ ≤ SUCCINCT-CVP` | ✓ | ✓ | ✓ |

---

# Source: **NL** — `PATH`, `2SAT`, `ALL_DFA`

| target | 3 examples | ≤L | ≤p | ≤m |
|---|---|---|---|---|
| **L** | `PATH ≤ EVEN` · `2SAT ≤ PALINDROME` · `ALL_DFA ≤ ST-Conn₂₀₂₂` | ? `L=NL` | ✓ 🔄 | ✓ |
| **NL** | `PATH ≤ 2SAT` · `2SAT ≤ ALL_DFA` · `ALL_DFA ≤ PATH` | ✓ | ✓ | ✓ |
| **P** | `PATH ≤ CVP` · `2SAT ≤ HORN-SAT` · `ALL_DFA ≤ A_CFG` | ✓ | ✓ | ✓ |
| **NP** | `PATH ≤ SAT` · `2SAT ≤ CLIQUE` · `ALL_DFA ≤ HAMPATH` | ✓ | ✓ | ✓ |
| **coNP** | `PATH ≤ TAUTOLOGY` · `2SAT ≤ UNSAT` · `ALL_DFA ≤ NON-HAMPATH` | ✓ | ✓ | ✓ |
| **PSPACE** | `PATH ≤ TQBF` · `2SAT ≤ ALL_NFA` · `ALL_DFA ≤ EQ_REX` | ✓ | ✓ | ✓ |
| **EXP** | `PATH ≤ EXP-HALT` · `2SAT ≤ GEN-CHESS` · `ALL_DFA ≤ SUCCINCT-CVP` | ✓ | ✓ | ✓ |

🔄 **The one moving cell.** `PATH ≤L EVEN` needs `NL ⊆ L` — open. `PATH ≤p EVEN` is **true**: poly
time is enough to run BFS and decide `PATH` outright, then print a constant.

---

# Source: **P** — `CVP`, `HORN-SAT`, `A_CFG`

| target | 3 examples | ≤L | ≤p | ≤m |
|---|---|---|---|---|
| **L** | `CVP ≤ EVEN` · `HORN-SAT ≤ PALINDROME` · `A_CFG ≤ ST-Conn₂₀₂₂` | ? `L=P` | ✓ 🔄 | ✓ |
| **NL** | `CVP ≤ PATH` · `HORN-SAT ≤ 2SAT` · `A_CFG ≤ ALL_DFA` | ? `NL=P` | ✓ 🔄 | ✓ |
| **P** | `CVP ≤ HORN-SAT` · `HORN-SAT ≤ A_CFG` · `A_CFG ≤ CVP` | ✓ | ✓ | ✓ |
| **NP** | `CVP ≤ SAT` · `HORN-SAT ≤ CLIQUE` · `A_CFG ≤ HAMPATH` | ✓ | ✓ | ✓ |
| **coNP** | `CVP ≤ TAUTOLOGY` · `HORN-SAT ≤ UNSAT` · `A_CFG ≤ NON-HAMPATH` | ✓ | ✓ | ✓ |
| **PSPACE** | `CVP ≤ TQBF` · `HORN-SAT ≤ ALL_NFA` · `A_CFG ≤ EQ_REX` | ✓ | ✓ | ✓ |
| **EXP** | `CVP ≤ EXP-HALT` · `HORN-SAT ≤ GEN-CHESS` · `A_CFG ≤ SUCCINCT-CVP` | ✓ | ✓ | ✓ |

🔄 Both flips are the same mechanism as the NL row: under `≤p` the reducer simply decides the
P-source itself. **`CVP ≤p PATH` is TRUE even though `CVP ≤L PATH` is open.**

---

# Source: **NP** — `SAT`, `CLIQUE`, `HAMPATH`

| target | 3 examples | ≤L | ≤p | ≤m |
|---|---|---|---|---|
| **L** | `SAT ≤ EVEN` · `CLIQUE ≤ PALINDROME` · `HAMPATH ≤ ST-Conn₂₀₂₂` | ? `L=NP` | ? `P=NP` | ✓ |
| **NL** | `SAT ≤ PATH` · `CLIQUE ≤ 2SAT` · `HAMPATH ≤ ALL_DFA` | ? `NL=NP` | ? `P=NP` | ✓ |
| **P** | `SAT ≤ CVP` · `CLIQUE ≤ HORN-SAT` · `HAMPATH ≤ A_CFG` | ? `P=NP` | ? `P=NP` | ✓ |
| **NP** | `SAT ≤ CLIQUE` · `CLIQUE ≤ HAMPATH` · `HAMPATH ≤ SAT` | ✓ | ✓ | ✓ |
| **coNP** | `SAT ≤ TAUTOLOGY` · `CLIQUE ≤ UNSAT` · `HAMPATH ≤ NON-HAMPATH` | ? `NP=coNP` | ? `NP=coNP` | ✓ |
| **PSPACE** | `SAT ≤ TQBF` · `CLIQUE ≤ ALL_NFA` · `HAMPATH ≤ EQ_REX` | ✓ | ✓ | ✓ |
| **EXP** | `SAT ≤ EXP-HALT` · `CLIQUE ≤ GEN-CHESS` · `HAMPATH ≤ SUCCINCT-CVP` | ✓ | ✓ | ✓ |

⚠️ **No verdict changes in this row, but the open problem does.** `SAT ≤L EVEN` is equivalent to
`L = NP`; `SAT ≤p EVEN` is equivalent to `P = NP`. Both UNKNOWN — but the papers award the mark for
**naming the right one**.

---

# Source: **coNP** — `TAUTOLOGY`, `UNSAT`, `NON-HAMPATH`

| target | 3 examples | ≤L | ≤p | ≤m |
|---|---|---|---|---|
| **L** | `TAUTOLOGY ≤ EVEN` · `UNSAT ≤ PALINDROME` · `NON-HAMPATH ≤ ST-Conn₂₀₂₂` | ? `L=coNP` | ? `P=NP` | ✓ |
| **NL** | `TAUTOLOGY ≤ PATH` · `UNSAT ≤ 2SAT` · `NON-HAMPATH ≤ ALL_DFA` | ? `NL=coNP` | ? `P=NP` | ✓ |
| **P** | `TAUTOLOGY ≤ CVP` · `UNSAT ≤ HORN-SAT` · `NON-HAMPATH ≤ A_CFG` | ? `P=NP` | ? `P=NP` | ✓ |
| **NP** | `TAUTOLOGY ≤ SAT` · `UNSAT ≤ CLIQUE` · `NON-HAMPATH ≤ HAMPATH` | ? `NP=coNP` | ? `NP=coNP` | ✓ |
| **coNP** | `TAUTOLOGY ≤ UNSAT` · `UNSAT ≤ NON-HAMPATH` · `NON-HAMPATH ≤ TAUTOLOGY` | ✓ | ✓ | ✓ |
| **PSPACE** | `TAUTOLOGY ≤ TQBF` · `UNSAT ≤ ALL_NFA` · `NON-HAMPATH ≤ EQ_REX` | ✓ | ✓ | ✓ |
| **EXP** | `TAUTOLOGY ≤ EXP-HALT` · `UNSAT ≤ GEN-CHESS` · `NON-HAMPATH ≤ SUCCINCT-CVP` | ✓ | ✓ | ✓ |

⚠️ `coNP ⊆ P` collapses to **`P = NP`**, not to some separate "P = coNP" problem — P is closed
under complement, so the two are the same statement. Write `P = NP`.

---

# Source: **PSPACE** — `TQBF`, `ALL_NFA`, `EQ_REX`

**The row that carries the exam's favourite trap.**

| target | 3 examples | ≤L | ≤p | ≤m |
|---|---|---|---|---|
| **L** | `TQBF ≤ EVEN` · `ALL_NFA ≤ PALINDROME` · `EQ_REX ≤ ST-Conn₂₀₂₂` | **✗** `L⊊PSPACE` | ? `P=PSPACE` 🔄 | ✓ |
| **NL** | `TQBF ≤ PATH` · `ALL_NFA ≤ 2SAT` · `EQ_REX ≤ ALL_DFA` | **✗** `NL⊊PSPACE` | ? `P=PSPACE` 🔄 | ✓ |
| **P** | `TQBF ≤ CVP` · `ALL_NFA ≤ HORN-SAT` · `EQ_REX ≤ A_CFG` | ? `P=PSPACE` | ? `P=PSPACE` | ✓ |
| **NP** | `TQBF ≤ SAT` · `ALL_NFA ≤ CLIQUE` · `EQ_REX ≤ HAMPATH` | ? `NP=PSPACE` | ? `NP=PSPACE` | ✓ |
| **coNP** | `TQBF ≤ TAUTOLOGY` · `ALL_NFA ≤ UNSAT` · `EQ_REX ≤ NON-HAMPATH` | ? `coNP=PSPACE` | ? `coNP=PSPACE` | ✓ |
| **PSPACE** | `TQBF ≤ ALL_NFA` · `ALL_NFA ≤ EQ_REX` · `EQ_REX ≤ TQBF` | ✓ | ✓ | ✓ |
| **EXP** | `TQBF ≤ EXP-HALT` · `ALL_NFA ≤ GEN-CHESS` · `EQ_REX ≤ SUCCINCT-CVP` | ✓ | ✓ | ✓ |

🔄 **These two cells are the whole point of the sheet.** `ALL_NFA ≤L PATH` is **FALSE** — the claim
says `PSPACE ⊆ NL`, refuted by `NL ⊊ PSPACE`. `ALL_NFA ≤p PATH` is **UNKNOWN** — `closure_p(NL) = P`,
so the claim only says `PSPACE ⊆ P`, which is open. Same claim, one budget apart, opposite answers.

This is 2025-1 moed A Q8.א, the question you got wrong.

---

# Source: **EXP** — `EXP-HALT`, `GEN-CHESS`, `SUCCINCT-CVP`

| target | 3 examples | ≤L | ≤p | ≤m |
|---|---|---|---|---|
| **L** | `EXP-HALT ≤ EVEN` · `GEN-CHESS ≤ PALINDROME` · `SUCCINCT-CVP ≤ ST-Conn₂₀₂₂` | **✗** `P⊊EXP` | **✗** `P⊊EXP` | ✓ |
| **NL** | `EXP-HALT ≤ PATH` · `GEN-CHESS ≤ 2SAT` · `SUCCINCT-CVP ≤ ALL_DFA` | **✗** `P⊊EXP` | **✗** `P⊊EXP` | ✓ |
| **P** | `EXP-HALT ≤ CVP` · `GEN-CHESS ≤ HORN-SAT` · `SUCCINCT-CVP ≤ A_CFG` | **✗** `P⊊EXP` | **✗** `P⊊EXP` | ✓ |
| **NP** | `EXP-HALT ≤ SAT` · `GEN-CHESS ≤ CLIQUE` · `SUCCINCT-CVP ≤ HAMPATH` | ? `NP=EXP` ⚠️ | ? `NP=EXP` ⚠️ | ✓ |
| **coNP** | `EXP-HALT ≤ TAUTOLOGY` · `GEN-CHESS ≤ UNSAT` · `SUCCINCT-CVP ≤ NON-HAMPATH` | ? `coNP=EXP` | ? `coNP=EXP` | ✓ |
| **PSPACE** | `EXP-HALT ≤ TQBF` · `GEN-CHESS ≤ ALL_NFA` · `SUCCINCT-CVP ≤ EQ_REX` | ? `PSPACE=EXP` | ? `PSPACE=EXP` | ✓ |
| **EXP** | `EXP-HALT ≤ GEN-CHESS` · `GEN-CHESS ≤ SUCCINCT-CVP` · `SUCCINCT-CVP ≤ EXP-HALT` | ✓ | ✓ | ✓ |

⚠️ **`GEN-CHESS ≤p SAT` is UNKNOWN, not FALSE** — the single most counter-intuitive cell in the
whole sheet. To refute it you need a proven `X ⊊ Y` with `NP ⊆ X` and `Y ⊆ EXP`: `P ⊊ EXP` would
need `NP ⊆ P`, and `PSPACE ⊊ EXPSPACE` would need `EXPSPACE ⊆ EXP`. Neither holds, so nothing
fits and the claim stands open. Compare **`EXPSPACE`-complete `≤p SAT`, which *is* FALSE** —
there `PSPACE ⊊ EXPSPACE` fits the span exactly.

⚠️ Note this row does **not** move between `≤L` and `≤p`: widening the target from `L`/`NL` to `P`
does not save it, because `P ⊊ EXP` is proven. **A separation survives the budget change when it
straddles the closure; it dies when the closure swallows it.**

---

# The whole sheet in four observations

1. **The `≤m` column is uniformly ✓ — all 49 cells, all 147 examples.** Every one of these
   languages is decidable, so the constant-output lemma applies with no budget to violate.
   `GEN-CHESS ≤m EVEN` is true. This is why an `≤m` question about decidable languages is never
   worth asking, and why every `≤m` item on your papers involves `HALT` or `A_TM`.
2. **Only 5 cells differ between `≤L` and `≤p`**, all in the `L` and `NL` columns:
   `NL→L`, `P→L`, `P→NL` (? → ✓) and `PSPACE→L`, `PSPACE→NL` (✗ → ?).
3. **Only 8 cells are ✗ anywhere**, generated by just three theorems: `L ⊊ PSPACE`,
   `NL ⊊ PSPACE`, `P ⊊ EXP`. If your FALSE answer does not trace to one of those, it is wrong.
4. **Everything on or above the diagonal is ✓ under all three budgets** — 28 of the 49 cells, more
   than half the sheet, needing no thought at all. Triage on the source first.

---

## Issues log

- **(2026-07-28)** Built to give concrete instances for every budget × source × target
  combination, after the abstract verdict table alone did not make the claims easy to settle.
  Format chosen so the three budgets sit side by side on one row rather than in three separate
  grids — the budget comparison is the thing being learned, and separating it hides it.
  147 example claims over 49 cells. Cells worth re-reading before the exam: `PSPACE → L/NL` (the
  only FALSE→UNKNOWN flip, and the 2025-1 moed A Q8.א error) and `EXP → NP` (UNKNOWN, not FALSE —
  the endpoint-comparison trap).
