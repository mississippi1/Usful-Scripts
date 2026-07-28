# Weak points & exam focus plan

*Compiled 2026-07-28 from all 35 notes docs under `Complexity/2017-2025 Exams solutions/notes/`,
cross-referenced against the 22 exam papers in `Complexity/2017-2025 Exams/`.
Sources: every "Issues log" entry across the archive.*

Two parts:
- **Part A — weak points**, ranked by how often they cost a real mark, with the exact fix for each.
- **Part B — which exams to work tomorrow**, tiered.

---

# Part A — Weak points

## The scoreboard

Errors recorded across the archive, split by whether the *answer bucket itself* was wrong
(costs the whole question) versus a gap in the justification (costs partial credit).

**Wrong final answer — 9 instances:**

| Exam | Q | Answered | Correct | Root cause |
|---|---|---|---|---|
| 2025-2026 winter moed A | Q5 | coRE ∖ R | **R** (L = ∅) | didn't test whether the property is satisfiable |
| 2025 summer moed A | Q9 | P | **NP-complete** | threshold is a *fraction of n*, not a constant |
| 2022-2 moed A | Q7 | NP-complete | **NL-complete** | read the *name* "LongPath", not the definition ("distance ≥ k") |
| 2022-2 moed A | Q8 | NL | **NP-complete** | forgot the certificate must prove **distinctness** |
| 2025-1 moed A | Q6 | ¬(RE ∪ coRE) | **RE ∖ R** | "∃n …" over a semi-decidable condition is RE |
| 2025-1 moed A | Q8.א | לא נכונה (false) | **ג (unknown)** | applied Space Hierarchy to a poly-**time** reduction |
| 2025-1 moed A | Q8.ג | "NL ⊆ L" | **L ⊆ NL** | containment direction reversed |
| 2022-1 moed B | Q10 | ג (unknown), circled P=NP | **נכונה (true)** | missed that A_NFA ∈ P |
| 2023-2 moed A | Q6 | נכונה | **לא נכונה** | (marking on the sheet contradicted the official solution) |

**Right bucket, broken/incomplete reasoning — 8 instances:** 2025-1 moed A Q5 (misread the
problem — per-run tape output vs the language condition L(M₁) = rev(L(M₂))); 2022-2 moed B Q8
(estimated space as |V|·log|V|); 2022-2 moed B Q9 (over-engineered a reduction that was also
buggy); 2023-2 moed A Q8 (three separate failed attempts to put it in P); 2020 summer moed A Q7
(read ≤p as "same difficulty"); 2022-1 moed A Q7 (didn't see it was a *computability*
refutation); `L(M) ∈ R is coRE-hard` (two dead-end budget constructions); `L = pairs with
L(M₁) ≤ L(M₂)` (a reduction whose no-case mapped to a yes-instance).

**Couldn't start — 2 instances:** 2025 summer moed A Q1 (didn't identify the MN product bound as
the tool); 2025-1 moed A Q2.א (colored DFA construction).

---

## W1 — Reduction *direction* and *resource bound* ⭐ biggest cluster

**8 separate incidents.** This is the single most repeated source of lost marks in the archive,
and it shows up in every year.

Three distinct confusions live here:

1. **Direction.** `A ≤m B` means *A is no harder than B*. Reducing an **easy** language into a
   **hard** one is free and proves nothing. Missed at 2020 summer moed A Q7 (`PATH ≤p HAMCYCLE`
   — thought it needed P = NP; it is unconditionally true) and again at 2022-1 moed B Q10.
2. **Resource bound.** `≤m` (unbounded), `≤p`, `≤L` are three different relations and class
   separations only bite for the bounded ones. 2024 summer moed A Q5 (`ALL_NFA ≤m VC` is
   **true** despite PSPACE vs NP, because ≤m is unbounded); 2025-1 moed A Q8.א
   (`ALL_NFA ≤p PATH` is **unknown**; `ALL_NFA ≤L PATH` is **provably false** — same claim, two
   verdicts, only the bound changed).
3. **Polarity.** `A ≤m B` does **not** give `Ā ≤m B`; it gives `Ā ≤m B̄`. Direction-swapped
   complement claims (2021 moed A Q6) are usually **false**.

**The two lemmas that resolve most of these instantly:**

> **Constant-output lemma.** If A is decidable within resource bound r and B is non-trivial
> (B ≠ ∅, Σ*), then **A ≤_r B** — decide A within budget r, then print one of two hard-coded
> constants. Output is write-only, so printing is free.

> **𝒞-complete lemma.** If L is 𝒞-complete and 𝒟 ⊆ 𝒞 is closed under ≤p, then
> **"L ∈ 𝒟" ⟺ 𝒞 = 𝒟.** Every "this complete language is in that smaller class" claim is a
> class collapse in disguise.

**Exam habit:** before writing anything, say out loud — *which* relation (≤m / ≤p / ≤L), and
*which* direction. Then check whether the constant-output lemma already settles it.

---

## W2 — Reading the *name* instead of the *definition* ⭐

Cost two full questions on the same paper (2022-2 moed A Q7 **and** Q8, in opposite directions)
and one more on 2025 summer moed A Q9. The exams deliberately plant near-identical names on
languages in different classes.

**The s–t path family — memorize this table, it has appeared in at least five papers:**

| Language | Condition | Class | Why |
|---|---|---|---|
| ∃ path s→t of length ≤ **constant c** | constant bound | **L** | depth-bounded DFS, depth O(1) |
| PATH — ∃ path s→t | bound is \|V\| | **NL-complete** | guess the walk, counter |
| "**distance** s→t ≥ k" | ∀ — *no short path exists* | **NL-complete** | complement ∈ NL, then NL = coNL |
| ∃ **simple** path s→t of length ≥ k | ∃ + distinctness | **NP-complete** | witness needs Θ(n) bits |

**The two deciding words:**
- **"distance"** = a *minimum over paths*, so a lower bound on it is a **universal** statement → NL.
- **"contains a simple path"** = existential over an object that must certify **all vertices
  distinct** → Θ(n) memory → NP, never NL.

**And the threshold rule:** a **constant** threshold ⟹ P (brute force over O(n^{c+1}) tuples;
with color coding, up to k = O(log n) still works). A threshold that is a **fraction of n**
⟹ NP-complete, absorbed by isolated-vertex padding. "The threshold isn't in the input" does
*not* make the problem easier — that was the 2025 summer moed A Q9 trap.

---

## W3 — Space accounting for logspace algorithms

Recurring: confusing what costs **time** with what costs **space**.

- 2022-2 moed B Q8: estimated |V|·log|V| because "each vertex has up to |V| neighbours". The
  branching factor is a **time** cost (runtime |V|^2022). Space is
  **recursion depth × per-frame size**, and cells are reused across sibling branches.
- **Depth is everything.** Constant depth ⟹ L. Depth |V| ⟹ NL (not known L).
- **A counter for k written in binary is still O(log n)**, because it is capped at
  min(k−1, |V|−1) — shortest paths are simple.
- **NL = coNL (Immerman–Szelepcsényi) is load-bearing, not decorative.** Whenever the condition
  is universal ("no path exists", "G stays connected"), the move is: put the *complement* in NL,
  then cite NL = coNL. Used in 2022-2 moed C Q9, 2022-2 moed A Q7.
- **Logspace reductions:** the output tape is **write-only and uncharged**. You may emit a
  polynomially large graph while keeping O(log n) work space — stream it, never store it.

**Self-check that would have caught two of these errors:** *a class marking that contradicts a
membership proof you can produce yourself is self-refuting.* If you can put L in NL, marking it
NP-complete asserts P = NP.

---

## W4 — Empty / unsatisfiable property traps ⭐ (cost the most recent exam)

Two papers, same shape. Before reaching for Rice or a reduction, ask: **can any machine satisfy
this at all?**

- **2025-2026 winter moed A Q5:** `{⟨M⟩ : L(M) ∈ coRE ∖ R}`. L(M) is **always RE**, and
  **RE ∩ coRE = R**, so the slice `coRE ∖ R` is unsatisfiable → L = ∅ ∈ **R**.
- **2024 summer moed A Q6:** "accepts σσ in one step but does not halt on σσσσ". A one-step
  computation cannot see past the first cell, and both inputs start with σ → contradictory →
  L = ∅ ∈ **R**.

**Trigger:** a classification question naming a class *slice* (`X ∖ Y`) applied to L(M), or a
**bounded-step** condition that must distinguish two inputs sharing a prefix. Test satisfiability
first; ∅ and Σ* are decidable no matter how exotic the wording.

Full treatment: `Study guide - empty-language traps (when a machine property is unsatisfiable).md`.

---

## W5 — Quantifier shape → RE / coRE / neither

Missed at 2025-1 moed A Q6 (answered "outside RE ∪ coRE" for something that was **RE ∖ R**).
The cheat sheet, assembled across 2020 summer moed B Q5-Q6, 2024 summer moed B Q5, 2023-2 moed A Q5:

| Shape | Class |
|---|---|
| ∃t "M accepts w within t steps" — ∃ over a **decidable** predicate | **RE** |
| ∃n / ∃w over a **semi-decidable** condition (dovetail!) | **RE** — ← the one that was missed |
| ∀w over a **decidable** predicate | **coRE** |
| ∀w over a bare **RE** predicate (even inside an outer ∃) | **outside RE ∪ coRE** |
| both ∃ and ∀ over unbounded ranges | usually **outside RE ∪ coRE** — prove with **two** reductions |

**Rule of thumb:** an existential over something semi-decidable stays inside RE — dovetailing
finds it. It only escapes RE ∪ coRE when a **universal** wraps a merely-RE predicate.

**And negate quantified properties mechanically** (the UC/coRE-hard note): ¬∀ = ∃¬, and
**¬(A → B) = A ∧ ¬B** — never negate an implication into another implication. Both x and y in
"∃x∃y" are witnesses; a mismatched ∃x∀y is the classic slip.

---

## W6 — "False" vs "unknown" ⭐ (and what to circle)

Three incidents, all on the 9-point true/false/unknown items, which are cheap marks when you get
the discrimination right.

> **INCORRECT requires an actual proof** — a computability gap, a hierarchy theorem, or closure
> under a known-true inclusion. **UNKNOWN** is anything gated behind an unresolved separation,
> however confidently believed.

- **Trap 1 (2025-1 moed A Q8.א):** using the **Space** Hierarchy Theorem against a poly-**time**
  reduction. Hierarchy theorems separate within *one* resource; they never rule out a poly-time
  map between problems.
- **Trap 2 (2025-2026 winter moed A Q8.ב):** marking "false" because L is PSPACE-hard. That
  asserts NP ≠ PSPACE — an open problem. You can *never* prove a language is outside NP by
  showing it is PSPACE-hard.
- **Trap 3:** circling **P = NP** just because a 3CNF formula appears in the statement. Under the
  reduction the formula is frozen to a constant; all the hardness flows from the NFA. The collapse
  is at **NP/PSPACE**, not P/NP.
- **The consequence most often missed: NP = coNP.** From NP = PSPACE: PSPACE is closed under
  complement, so coNP ⊆ coPSPACE = PSPACE = NP and symmetrically. Always check whether the
  collapse you derived also forces a coNP identity — it usually does, and it is a separate circle.
- **Known aggregate strictness does not give you a sub-link.** L ⊊ PSPACE is proven, but it spans
  four adjacent links; L vs NL remains fully open. Only a *directly* proven strict pair licenses
  a FALSE verdict. The four direct separations: **L ⊊ PSPACE, NL ⊊ PSPACE, P ⊊ EXP,
  PSPACE ⊊ EXPSPACE.** Everything else adjacent in the chain is open.

Full grids: `Study guide - classifying a language (P, NP-complete, PSPACE-complete).md`.

---

## W7 — Myhill–Nerode & DFA lower bounds

Weaker than the computability material, but these are the **Q1/Q2 cheap points** and they open
the paper.

- **2025 summer moed A Q1:** couldn't identify the tool. The tool is
  **MN(L₁ ∩ L₂) ≤ MN(L₁)·MN(L₂)** — an unconditional inequality no construction can evade
  (10 × 10 = 100 < 2025 ⟹ claim false). The bound is **tight**, via two independent counters.
- MN classes **partition all of Σ\***, including rejected words — that confusion came up twice.
- **Lower bound recipe:** pigeonhole 2^k words of Σ^k into the states, get x ≠ x′ landing in the
  same state, append a distinguishing suffix. The suffix length is often **forced** (z = x).
- **Minimality recipe:** exhibit *n* pairwise-inequivalent representatives to match your n-state
  DFA. Done well at 2025-2026 winter moed A Q1 and 2021 moed B Part I.
- **2025-1 moed A Q2.א (colored DFA)** — solved incorrectly. General transform: augment each
  state with the **subset of colors seen so far**, Q × P([k]), accept when the subset = [k];
  blowup |Q|·2^k.
- **NFA vs DFA:** the NFA **guesses a witness** and verifies locally (O(k²)); the DFA must store
  the whole first half (2^k). And **flipping accepting states does not complement an NFA** —
  multiple runs *and* dead ends both break it.

---

## W8 — Gadget discipline

- **Don't over-engineer** (2022-2 moed B Q9): a "contains a 2k-clique disjoint from …" clause is
  satisfied by **bolting on a separate disconnected component**. Splitting/duplicating the
  original graph was both harder and wrong.
- **Padding donates a free conjunct.** k isolated vertices give an independent set of size k
  without touching the vertex cover (2024 summer moed A Q8); isolated padding converts "cover
  everything" into "cover a fraction" (2025 summer moed A Q9, 2022-2 moed A Q8).
- **Solution-doubling** for "at least two solutions": a symmetric pair of forced-detour vertices
  multiplies every solution by exactly 2 and creates none (2025-2026 winter moed A Q7).
- **k in unary vs k ≤ |V|** — two *independent sufficient* conditions to keep "build k gadgets"
  polynomial; you need at most one, and **neither is needed for correctness**.
- **The no-case must collapse the target to a trivial m-degree** (finite / ∅ / Σ*), not merely
  shrink it — deleting one word from HALT leaves it RE-complete. This killed a reduction outright.
- **Every reduction needs an undecidable ingredient somewhere.** A construction whose behaviour
  depends only on |x| yields a monotone, hence regular, hence decidable language in *both*
  polarities (the `L(M) ∈ R` budget-gadget dead end).

---

## The 8-item pre-flight checklist

Read this before the exam and again before each classification question:

1. **Can the property be satisfied at all?** (W4) — especially for `L(M) ∈ X ∖ Y` and bounded-step conditions.
2. **Read the definition, ignore the name.** (W2) — "distance" vs "contains a simple path".
3. **Which reduction relation, which direction?** (W1) — ≤m / ≤p / ≤L, and does the constant-output lemma already settle it?
4. **Write the quantifiers explicitly.** (W5) — ∃ over semi-decidable = RE; ∀ over RE = neither.
5. **Does the witness need distinctness?** (W2) — yes ⟹ NP, never NL.
6. **Space = depth × frame, not branching.** (W3) — and consider NL = coNL for universal conditions.
7. **Is "false" actually provable, or am I asserting an open problem?** (W6)
8. **Sanity-check the marking against your own membership proof.** (W3) — self-refuting answers are free marks lost.

---

# Part B — Which exams to work tomorrow

Tomorrow's paper (2026-07-29) is a **summer moed A**, one year after
`טופס בחינה 2025 מועד א` (30.7.2025). The most recent papers in the archive are the best format
predictors; the 2017–2019 papers are a different era and a different question style.

## Tier 1 — do these first (≈3 hours)

| Exam | File | Why |
|---|---|---|
| **2025-2026 winter moed A** | `Comp 2025-2026 moed A (annotated).pdf` | **The most recent paper in the archive** (6.2.2026, Kupferman) and the closest to tomorrow's syllabus and format. Q5 was answered wrong; **Q1–Q4 and Q8 were left blank entirely** and have never been attempted under time pressure. No official solution exists — full worked notes are in the archive. |
| **2025 summer moed A** | `טופס בחינה 2025 מועד א.pdf` | **Exactly one year before tomorrow's paper** — same moed, same season, so the strongest structural predictor. Only Q1, Q3, Q9 have notes; **Q2, Q4–Q8 are uncovered.** Q9 was answered wrong (P instead of NP-complete) and Q1 couldn't be started. Solution: `פתרון 2025 מועד א.pdf`. |
| **2025-1 moed A** | `Comp 2025-1 moed A.pdf` | **Four recorded errors on one paper** — Q2.א, Q5 (misread), Q6, Q8.א, Q8.ג. The highest error density in the archive and the material is current. |

**How to work them:** redo Q5 of 2025-2026 winter *cold* (the empty-language trap), then sit
2025 summer moed A as a full timed paper — it is the closest analogue and mostly unseen.

## Tier 2 — high value, do what time allows (≈2 hours)

| Exam | File | Why |
|---|---|---|
| **2022-2 moed A** | `comp 2022-2 moed A.pdf` | Q7 **and** Q8 both wrong, in opposite directions — the LongPath/LargeCycle mirror pair, which is W2 in its purest form. Highest concentration of the name-vs-definition trap. |
| **2025 moed B** | `טופס בחינה 2025 מועד ב.pdf` | Current era, **only Q7 covered** — 8 questions never attempted. Solution available (`פתרון 2025 מועד ב.pdf`). |
| **2023-2 moed A** | `Comp 2023-2 moed A.pdf` | Q6 answered wrong; Q8 needed three attempts before landing. Only Q5, Q6, Q8 covered — Q1-Q4, Q7, Q9 unseen. |
| **2024-2 moed B** | `Comp 2024-2 moed B.pdf` | Only Q5 covered; the rest untouched. Same lecturer era as the recent papers. |

## Tier 3 — only if you finish Tier 1 & 2

- `Comp 2023-2 moed B.pdf` — **no notes at all**, recent-ish era, solution available. The single
  largest completely-unseen recent paper.
- `Comp 2022-2 moed B.pdf` — Q6, Q8, Q9 covered; the rest unseen. (Note: this PDF is a **scan** —
  no extractable text.)
- `Comp 2022-1 moed A.pdf` / `Comp 2022-1 moed B.pdf` — Part III covered on both (moed B Q10 was
  wrong); Parts I–II unseen.
- `Comp 2021 Moed B.pdf` — heaviest NP/PSPACE keyword density of any paper in the archive; good
  targeted drilling for W6 if the true/false/unknown items feel shaky.

## Tier 4 — skip unless you have spare time

`Comp 2017 moed B`, `Comp 2018 moed A/B`, `Comp 2019 moed A/B`, `Comp 2020 moed A/B`,
`Comp 2021 Moed A`, `Comp 2022-2 moed C`. Different era and question style; the 2020/2021/2022-C
papers already have their hard parts covered by notes. Low marginal value the night before.

## Gaps in the archive (don't waste time hunting)

- **`Comp 2025-2026 moed A` has no official solution** — the notes doc is the only worked answer key.
- **Solutions without the matching exam paper:** `Comp 2017 moed A`, `Comp 2025-1 moed B`,
  `Comp 2025-1 moed C`.
- Three exam PDFs are **image scans** with no extractable text: `Comp 2022-2 moed B`,
  `Comp 2024-2 moed A`, `Comp 2024-2 moed B`.

## Suggested sequence for tonight

1. **30 min** — read Part A's checklist and the W2 s–t path table until both are automatic.
2. **90 min** — 2025 summer moed A (`טופס בחינה 2025 מועד א.pdf`) as a **full timed paper**, then mark against `פתרון 2025 מועד א.pdf`.
3. **45 min** — 2025-2026 winter moed A Q1–Q4 and Q8 (the never-attempted ones), against the notes doc.
4. **30 min** — 2022-2 moed A Q7 + Q8 back to back, deliberately, as a W2 drill.
5. **15 min** — re-read the six wrong-answer rows in the scoreboard above. Those are the specific mistakes most likely to recur.

---

## Issues log

- **(2026-07-28)** Initial compilation. Scanned all 35 notes docs and all 22 exam papers; extracted
  19 recorded errors from the Issues logs, clustered them into eight weak points (W1–W8) ranked by
  frequency, and tiered the exam archive by error density, coverage gaps, and recency relative to a
  summer moed A. Largest cluster: reduction direction/resource bound (8 incidents). Costliest
  single trap: unsatisfiable-property questions (cost Q5 of the most recent paper).
