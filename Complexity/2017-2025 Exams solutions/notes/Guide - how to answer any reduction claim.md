# Guide — how to answer any reduction claim

Everything needed to settle a claim of the form **`A ≤_r B`** — true, false, or unknown — in three
to five minutes, with the marks written down in the form the papers reward.

Reference material lives elsewhere:
- `Study guide - the reduction verdict table (source x target x budget).md` — the lookup grids
- `Drill sheet - 147 worked reduction claims (budget x source x target).md` — worked instances
- `Study guide - classifying a language (P, NP-complete, PSPACE-complete).md` — how to find `A`'s class

This doc is the **procedure**.

---

# Part 0 — The whole thing on one screen

```
MARGIN:   budget: ≤L / ≤p / ≤m
          source: <language> → <class C₁>     ← from the DEFINITION, not the name
          target: <language> → <class C₂>

TRIAGE:   C₁ ⊆ C₂ ?  → TRUE. Name the lemma. Move on.   (~half of all items)
          budget ≤m and both decidable? → TRUE. Move on.
          otherwise ↓

WORK:     1. closure_r(C₂) = max(C₂, D_r)      D_L = L · D_p = P · D_m = R
          2. claim ⟺ C₁ ⊆ closure_r(C₂)
          3. interval test on the span [closure_r(C₂), C₁]
                 a proven separation fits inside  ⟹ FALSE, cite it
                 nothing fits                     ⟹ UNKNOWN, name the open problem
```

---

# Part 1 — Why any of this is valid

## The collapse chain

`A ≤_r B` looks like a statement about two languages. It is not. Assume A is **C₁-complete** and
`B ∈ C₂`:

| | step | justification |
|---|---|---|
| 1 | `B ∈ C₂` | given |
| 2 | `A ≤_r B` | the claim |
| 3 | **`A ∈ C₂`** | C₂ closed under `≤_r` |
| 4 | `X ≤_r A` for every `X ∈ C₁` | A is C₁-**complete** |
| 5 | **`X ∈ C₂`** for every such X | C₂ closed under `≤_r`, again |
| 6 | **`C₁ ⊆ C₂`** | from 4–5 |

**Completeness of the source is what makes it a collapse.** Without step 4 the claim would only
constrain A itself; because A is complete, it drags its whole class along.

Steps 3 and 5 both require *"C₂ is closed under `≤_r`"*. When it isn't, you climb to the smallest
class that is — that is the closure, and it is the only place the budget enters.

## The converse

If `C₁ ⊆ closure_r(C₂)` then the reduction really does exist — either by the target's completeness
(when `C₁ ⊆ C₂`) or by the constant-output lemma (when the containment came from the closure).
So:

> ### `A ≤_r B` ⟺ `C₁ ⊆ closure_r(C₂)`
> An equivalence, not an implication. After step 2 you may forget the languages entirely.

## The two lemmas everything rests on

> **Constant-output lemma.** If A is decidable within budget r and B is **non-trivial**
> (`B ≠ ∅, Σ*`), then `A ≤_r B`: decide A within budget, then print one of two hardcoded strings —
> one in B, one not. The output tape is **write-only and uncharged**, so printing is free.

> **Completeness lemma.** If B is C₂-complete under `≤_r` and `A ∈ C₂`, then `A ≤_r B` by
> definition of completeness.

Every TRUE verdict in this guide is one of these two. Know which one you are using.

---

# Part 2 — The procedure

## Step 0 — Fill in three lines in the margin

```
budget:  ≤L / ≤p / ≤m
source:  <language>  →  <class>
target:  <language>  →  <class>
```

**Classify from the definition, never the name.** The papers plant near-identical names on
languages in different classes — "LongPath" was NL-complete, "LargeCycle" NP-complete. Ask:

- Does the witness have to certify **distinctness**? ⟹ Θ(n) bits ⟹ **NP**, never NL.
- Is the condition **universal** ("no shorter path", "stays connected")? ⟹ complement ∈ NL, then
  **NL = coNL** ⟹ **NL**.
- Is the bound a **constant**? ⟹ **L**. A **fraction of n**? ⟹ **NP-complete**.

⚠️ **If you are stuck for more than a minute, you are stuck on step 0, not on the reduction.** The
reduction question is a lookup once both classes are known. Go back and classify properly rather
than pushing harder on the reduction.

## Step 1 — Triage on the SOURCE

Compare the two classes before doing anything else.

**Source ⊆ target ⟹ TRUE.** One sentence, move on. This is roughly half the marks on these items
and needs no thought. Say which lemma:
- `C₁ ⊆ C₂` → **completeness of the target**
- source decidable within the budget → **constant-output lemma**

**Budget is `≤m` and both languages are decidable ⟹ TRUE.** Stop here; `D_m = R` and every
decidable class is inside R. Steps 2–4 never run.

**Source ⊋ target ⟹ class collapse.** Now do the work below.

## Step 2 — Closure

> ### `closure_r(C) = max(C, D_r)`
> where **`D_r` = what a budget-r machine can decide outright**:
> **`D_L = L`** · **`D_p = P`** · **`D_m = R`**

The classes are nested, so "max" is literally "whichever is higher in the chain".

| budget | effect |
|---|---|
| `≤L` | `D_L = L` is the bottom ⟹ **identity everywhere** |
| `≤p` | `D_p = P` absorbs **L** and **NL**; everything from P upward is unchanged |
| `≤m` | `D_m = R` absorbs **every decidable class**; only `RE` and `coRE` survive |

**Why the leak exists.** Take non-trivial `B ∈ NL` and any `A ∈ P`. Then `A ≤p B` by the
constant-output lemma — so NL is *not* `≤p`-closed. The leak stops exactly at P: if `A ≤p B` with
`B ∈ NL ⊆ P`, then A is decidable in poly time. Hence `closure_p(NL) = P` precisely.

**Why `≤L` doesn't leak.** "Decidable in logspace" means `A ∈ L ⊆ NL` — already inside. Nothing new
gets in.

⚠️ `≤m` is not "`≤p` with a longer exception list". `L` and `NL` are not special; they are simply
the classes below P. Under `≤m` the bar is R, so *everything decidable* is below it.

## Step 3 — Restate as an inclusion

Write the line: **"the claim is equivalent to `C₁ ⊆ closure_r(C₂)`"**. Graders look for it.

## Step 4 — The interval test

**The four proven separations:**

```
L  ⊆  NL  ⊆  P  ⊆  NP  ⊆  PSPACE  ⊆  EXP  ⊆  EXPSPACE
└──────────── L ⊊ PSPACE ──────────┘
       └───── NL ⊊ PSPACE ─────────┘
                  └──── P ⊊ EXP ──────────┘
                              └─ PSPACE ⊊ EXPSPACE ─┘
```

⚠️ **Not one adjacent pair in that chain is known strict.** Every proven separation straddles at
least two links. This is exactly why you cannot reason link by link.

**The test.** Form the span `[closure_r(C₂), C₁]`. Ask: does some proven `X ⊊ Y` sit **inside** it —
i.e. `closure_r(C₂) ⊆ X` **and** `Y ⊆ C₁`?

- **Fits ⟹ FALSE.** Proof: `Y ⊆ C₁ ⊆ C₂ ⊆ X` would give `Y ⊆ X`, contradicting `X ⊊ Y`.
- **Doesn't fit ⟹ UNKNOWN.** Name the open problem.

**Both endpoints must squeeze** — hence *contained in*, not *overlapping*. A separation poking out
either end leaves the squeeze open.

⚠️ **Openness does not chain; strictness does.** If `X ⊊ Y` is proven and `X' ⊆ X`, `Y ⊆ Y'`, then
`X' ⊊ Y'` — proven separations widen freely. Nothing similar holds for open problems. So "NP vs
PSPACE is open and PSPACE vs EXP is open" tells you **nothing** about NP vs EXP, and nothing about
NP vs EXPSPACE, which is in fact settled.

## Step 5 — Write it down

> **TRUE (completeness):** "`B` is `C₂`-complete under `≤_r` and `A ∈ C₂`, so the reduction exists
> by definition of completeness."

> **TRUE (constant-output):** "`A` is decidable within budget `r` and `B` is non-trivial, so the
> reduction decides `A` and prints one of two hardcoded constants — the output tape is write-only
> and uncharged."

> **FALSE:** "`B ∈ C₂` and `C₂` is closed under `≤_r`, so the claim implies `C₁ ⊆ C₂`, i.e.
> `⟨collapse⟩`. This contradicts `⟨proven separation⟩`."

> **UNKNOWN:** "… so the claim is equivalent to `⟨open problem⟩`, whose truth is unknown."

**Always name the open problem.** It is the difference between an answer and a guess, and the
papers award the mark for it.

---

# Part 3 — Which separations exist, and why

Don't memorise a list — memorise the generator:

> ### A separation is provable when both sides are the **same resource** (time / space) in the **same mode** (deterministic / nondeterministic), differing only in the **bound**. Cross either boundary and it goes open.

| separation | resource | mode | source |
|---|---|---|---|
| `L ⊊ PSPACE` | space | det / det | deterministic space hierarchy |
| `PSPACE ⊊ EXPSPACE` | space | det / det | deterministic space hierarchy |
| `P ⊊ EXP` | time | det / det | deterministic time hierarchy |
| `NL ⊊ PSPACE` | space | **nondet / det** ⚠️ | needs **Savitch** first |
| `NP ⊊ NEXP` | time | nondet / nondet | **nondeterministic** time hierarchy |

**`NL ⊊ PSPACE` is the one that looks like it breaks the rule.** It only works because **Savitch
lets space cross the determinism boundary for free**: either read it as `NL ⊊ NPSPACE` (both
nondeterministic space, since `NPSPACE = PSPACE`), or push `NL ⊆ SPACE(log²n) ⊊ PSPACE`.

**There is no Savitch for time — that missing theorem is P vs NP.** So every time-class question
crossing the determinism boundary is open:

| claim | crosses? | status |
|---|---|---|
| `NP ⊊ NEXP` | no — nondet to nondet | **provable** |
| `NP ⊊ EXP` | yes — nondet to det, in time | **open** |
| `P ⊊ NP` | yes | **open** |

Same source class, one target apart, opposite status.

Corollaries worth having ready: `NPSPACE ⊊ EXPSPACE` is **true but not new** — Savitch makes it a
restatement of `PSPACE ⊊ EXPSPACE`.

---

# Part 4 — Ten worked examples

**1. `PATH ≤p SAT` → TRUE.** Step 1 triage: `PATH ∈ P`, `SAT` non-trivial ⟹ constant-output lemma.
Never reach step 2.

**2. `PATH ≤L SAT` → TRUE.** `PATH ∈ NL ⊆ NP` and SAT is NP-complete **under ≤L** (Cook–Levin is a
logspace reduction) ⟹ completeness lemma. Note the *different* lemma from example 1 — the
constant-output route is unavailable because `PATH ∈ L` is open.

**3. `TQBF ≤m SAT` → TRUE.** Budget `≤m`, both decidable ⟹ stop at step 1. `TQBF ∈ PSPACE ⊆ R`;
decide it (taking however long — `≤m` has **no** budget) and print a constant.

**4. `ALL_NFA ≤L PATH` → FALSE.** Source PSPACE-complete, target NL-complete.
`closure_L(NL) = max(NL, L) = NL`. Claim ⟺ `PSPACE ⊆ NL`. Span `[NL, PSPACE]` — the interval
`NL ⊊ PSPACE` fits it exactly. **FALSE.**

**5. `ALL_NFA ≤p PATH` → UNKNOWN.** Identical claim, one budget looser.
`closure_p(NL) = max(NL, P) = **P**`. Claim ⟺ `PSPACE ⊆ P`. Span `[P, PSPACE]`: `NL ⊊ PSPACE`
needs `P ⊆ NL` ✗; `P ⊊ EXP` needs `EXP ⊆ PSPACE` ✗. Nothing fits. **UNKNOWN**, equivalent to
`P = PSPACE`.

> **4 and 5 together are the whole guide in miniature.** Widening the closure from NL to P
> swallowed the very separation that produced the FALSE. This is 2025-1 moed A Q8.א.

**6. `GEN-CHESS ≤p SAT` → UNKNOWN.** Source EXP-complete, `closure_p(NP) = NP`. Span `[NP, EXP]`:
`P ⊊ EXP` needs `NP ⊆ P` ✗; `PSPACE ⊊ EXPSPACE` needs `EXPSPACE ⊆ EXP` ✗. **UNKNOWN**,
equivalent to `NP = EXP`.

**7. `EXPSPACE-complete ≤p SAT` → FALSE.** Span `[NP, EXPSPACE]`: `PSPACE ⊊ EXPSPACE` fits —
`NP ⊆ PSPACE` ✓ and `EXPSPACE ⊆ EXPSPACE` ✓. **FALSE.**

> **6 and 7 are the interval test's reason to exist.** One step further out and the verdict flips.
> Endpoint intuition gets both wrong.

**8. `SAT ≤p HALT` → TRUE.** Map `⟨φ⟩` to a machine that brute-forces assignments and halts iff one
satisfies φ; building it from φ is poly-time. **Undecidability of the target obstructs nothing** —
the budget constrains the *mapping*, not the targets.

**9. `HALT ≤m SAT` → FALSE.** `closure_m(R) = R`, so the claim implies `HALT ∈ R`. It isn't.

**10. `HALT ≤m HALT‾` → FALSE.** It would give `HALT ∈ coRE`; with `HALT ∈ RE` and
`RE ∩ coRE = R`, that forces `HALT ∈ R`. This is also why **`A ≤ₘ B` does not give `Ā ≤ₘ B`** — it
gives `Ā ≤ₘ B̄`. **Polarity, not direction.**

---

# Part 5 — Degenerate cases the procedure doesn't cover

**Trivial target.** The constant-output lemma needs `B ≠ ∅, Σ*`. If the target *is* trivial the
whole machinery dies and the answer is forced:

- `A ≤ₘ ∅` ⟺ `A = ∅`
- `A ≤ₘ Σ*` ⟺ `A = Σ*`

Because `w ∈ A ⟺ f(w) ∈ ∅` is unsatisfiable unless A is empty, and dually. Check this **first**
whenever `∅` or `Σ*` appears — it is a one-line answer masquerading as a hard question.

**Trivial source.** `∅ ≤ₘ B` holds iff `B ≠ Σ*` (map everything outside B); `Σ* ≤ₘ B` holds iff
`B ≠ ∅`.

**Source not complete, only a member.** The collapse chain breaks at step 4. You may then conclude
only `A ∈ closure_r(C₂)` — a statement about A, not about C₁. Replace `C₁` throughout with **the
tightest class you can actually place A in**, and ask about A's membership rather than a class
inclusion. Exam questions almost always use complete languages, but check.

---

# Part 6 — The traps, from your own error record

Run this before committing to an answer:

1. **Did I classify from the definition or the name?** (2022-2 moed A Q7 **and** Q8, in opposite
   directions, on the same paper.)
2. **Which direction?** `A ≤ B` means **A is the easy one** — you are borrowing B's power. Easy
   into hard is free and proves nothing.
3. **Is a complement involved?** `A ≤ₘ B` gives `Ā ≤ₘ B̄`, never `Ā ≤ₘ B`.
4. **Am I about to write FALSE?** Name the separation out loud.
   - "PSPACE-hard, therefore not in NP" is **not** a separation — it asserts an open problem.
     (2025-2026 winter moed A Q8.ב.)
   - Check the **resource**: the *Space* Hierarchy Theorem says nothing about a poly-**time**
     reduction. (2025-1 moed A Q8.א.)
5. **Does my answer contradict something I could prove myself?** If you can put L in NL, marking it
   NP-complete asserts P = NP. Self-refuting answers are free marks lost.

## The trichotomy that decides everything

| you can produce… | answer |
|---|---|
| the reduction, or the lemma that yields it | **TRUE** |
| the contradiction, citing a proven separation | **FALSE** |
| **neither** — and you can name why | **UNKNOWN** |

⚠️ **"I can't build it" is not evidence for FALSE.** FALSE is a positive claim requiring a theorem.
If all you have is "surely not", the answer is UNKNOWN. This inference cost you a full question.

---

# Part 7 — Time

These are 6–12 point items. **3–5 minutes each.** Past ten minutes you have misidentified a class —
go back to step 0 and redo it rather than pushing harder on the reduction.

More than half of all such items are settled at step 1 by triage alone. Spend the saved time on the
classification questions, where the real work is.

---

## Issues log

- **(2026-07-28)** Written after a run of difficulty settling concrete claims (`TQBF ≤L SAT`,
  `TQBF ≤p PATH`, `SAT ≤p PATH`, `PATH ≤p SAT`). Consolidates the procedure into one doc.
  Two pieces of machinery introduced here that the earlier docs lacked: (1) **`closure_r(C) = max(C, D_r)`**
  with `D_r` = what a budget-r machine decides outright — this replaces three memorised closure rows
  with one formula, and makes the `≤m` case fall out instead of being an exception (the gap that
  produced the §7 error fixed in #82); (2) the **generating rule for separations** — same resource,
  same mode, differing bound — which explains why the canonical four are what they are, why
  `NL ⊊ PSPACE` needs Savitch, why `NP ⊊ NEXP` is provable, and why `NP ⊊ EXP` is not.
  Also added: the degenerate `∅` / `Σ*` cases, and the non-complete-source caveat.
