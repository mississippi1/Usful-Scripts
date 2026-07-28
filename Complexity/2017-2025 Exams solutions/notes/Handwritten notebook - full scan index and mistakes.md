# Handwritten notebook — full scan, index and mistakes log

Source: handwritten PDF uploaded 2026-07-28 (`9f76f958`, iOS-exported, **51 pages** — the upload
banner claimed 175, that was wrong). Scanned page by page as images; the embedded OCR layer is
garbage and was not used.

The notebook has two halves:

- **pp. 1–8 (+ p. 51)** — topic recap sheets (definitions, theorems, standing reminders).
- **pp. 9–50** — photographed exam questions with the answer circled and a handwritten
  post-mortem underneath. This is the actual mistakes log.

Colour convention in the notebook: **black/blue = first attempt**, **red = correction after
marking**. A crossed-out option next to a circled one means the first answer was wrong.

Legibility: most annotations are readable, some Hebrew shorthand is not. Entries below marked
*(partly illegible)* are the ones where only the gist could be recovered.

---

# Part 1 — Recap sheets (pp. 1–8, 51)

| Page | Content |
|---|---|
| 2 | Standing reminders: prove by **induction on \|w\|**; **product automaton**; NFA→DFA by **subset construction — don't forget the dead/trap state**; MN needs **suffixes**. Worked pattern: `L = {w \| w ∈ L₁, \|w\| mod 2 = 0}` ⟹ product `L₁ × Parity`. |
| 3 | Reduction doctrine; poly-time checkability, Vertex-Cover-style verification. |
| 4 | Closure table: REG/DFA and NREG/NFA closed under union, intersection, complement. |
| 5 | ε-closure: `E(q) = {q′ ∈ Q \| q′ reachable from q by ε-moves only}`, and `δ′(q,σ) = ⋃_{q′∈E(q)} E(δ(q′,σ))`. Plus: MN gives the minimal DFA state count. |
| 6 | **L-Mix**: `L = {w \| ∃z, \|z\| = \|w\|, w₁z₁w₂z₂… ∈ L₁}` with `δ′(q,σ) = {δ(δ(q,α),σ) : α ∈ Σ}` — guess the interleaved letter inside the transition. |
| 7 | NP: `NP = ⋃_k NTIME(n^k)`, plus the **verifier characterization** written out in full (∃c accepted / ∀c rejected, V poly-time). |
| 8 | **Savitch**: for `S(n) = Ω(log n)`, `NSPACE(S(n)) ⊆ SPACE(S²(n))`. **Space hierarchy**: if S is space-constructible there is an L decidable in `O(S(n))` but not in `o(S(n))`; time hierarchy analogous. |
| 51 | No reduction exists **from ∅ or from Σ\*** to a non-trivial language. Hierarchy corollary: for `1 ≤ ε₁ < ε₂`, `TIME/SPACE(n^{ε₁}) ⊊ TIME/SPACE(n^{ε₂})`. |

---

# Part 2 — The mistakes log (pp. 9–50)

## A. Answers that were marked wrong and corrected in red

These are the six pages where a first answer is visibly crossed out. They are the highest-value
items in the notebook.

| Page | Exam / Q | Language | Answered | Correct | Root cause written on the page |
|---|---|---|---|---|---|
| 18 | 2022-2 moed A Q8 | `LargeCycle` — simple cycle through x with ≥ \|V\|/2 vertices | **NL-Complete** | **NP-Complete** | witness must certify **distinct** vertices. Fix: `HAMCYCLE ≤ₘ LargeCycle`. |
| 39 | 2022-2 moed A Q7 | `LongPath` — *distance* from s to t ≥ k | **NP-Complete** | **NL-Complete** | "distance ≥ k" is a **universal** statement — complement is `PATH`-like, then `NL = coNL`. |
| 26 | 2025-1 moed A Q6 | `{⟨M⟩ : ∃n ≥ 0, M accepts all words of length n}` | **¬(RE ∪ coRE)** | **RE ∖ R** | ∃n over a semi-decidable condition is still RE — **dovetail** over n = 1, 2, … |
| 38 | 2025 summer moed A Q9 | simple path of length ≥ n/2 − 1 | **P** | **NP-Complete** | threshold is a *fraction of n*, not a constant. Fix: `HAMPATH ≤p L` by padding with \|V\| isolated vertices. |
| 34 | 2023-2 moed A Q6 | `f(L) ≠ Σ*` ⟹ `L ≤ₘ f(L)` or `L ∈ RE` | **נכונה (true)** | **לא נכונה (false)** | counterexample on the page: `L = HALT`, `f(w) = ε`, so `f(L) = {ε} ≠ Σ*` and `f(L) ∈ R`. |
| 41 | 2024 summer moed B Q7 | `2MON` — 2-monotone CNF satisfied by ≤ k true vars | **P** | **NP-Complete** | assumed brute force was polynomial; the page corrects it: `C(n,k) = n!/(k!(n−k)!)` is **not** poly. |

**Pattern.** Four of the six are the *same* error in two directions: reading the **name** of a
graph language instead of its **definition** (pp. 18, 39, 38) or misjudging whether a search space
is polynomial (p. 41). Two are quantifier-shape errors (pp. 26, 34).

## B. Questions worked correctly, with the reasoning recorded

| Page | Exam / Q | Item | Answer | Note on the page |
|---|---|---|---|---|
| 9 | 2022-2 moed C Q1 | NFA → DFA | — | *"forgot the ε-move — a trap"*. Recorded as a recurring slip, not a wrong final answer. |
| 9 | 2022-2 moed C Q6 | `XYTIME ∈ coRE` | **false** | *"didn't know which way the reduction goes"*. Both directions are written on the page; the one that works is `HALT ≤ₘ XYTIME`. |
| 10–11 | 2022-2 moed C Q7 | `PolyNL = co-PolyNL` | **true** | Savitch `NSPACE(f) ⊆ SPACE(f²)` for `f = Ω(log n)`; then `co-SPACE = SPACE` ⟹ `co-Poly = Poly`. |
| 11 | 2022-2 moed C Q8 | `LongPath` — visits all vertices, ≤ 2 visited twice | NP-Complete | *"didn't picture the gadget"* — sketch of the forced-detour construction is drawn. |
| 12 | 2022-2 moed C Q9 | `DISCONN` | NL | `NL = coNL`; the complement language is written out in full. |
| 13 | (DFA drawing) | every `00` run immediately followed by `11` | — | Red corrections add a missing `1`-edge and a **dead state** `q₄`. Same trap as p. 2. |
| 14 | 2024 summer moed B Q5 | exactly one non-halting input | ¬(RE ∪ coRE) | reasoning via `ALL_TM`, `L(M) = Σ*`. |
| 15–16 | (moed C) Q4 | `EXP_TM = {⟨M⟩ : L(M) ∈ EXP ∖ P}` ∈ R | **false** | `HALT ≤ EXP_TM` (Rice-style): build `M′` that runs M on w then simulates T; `L(M′) = ∅ ∈ P` iff `⟨M,w⟩ ∉ HALT`. |
| 16 | (moed C) Q5 | `L ≤ₘ L̄`, could `L = SAT`? | **true** | `SAT ∈ NP ⊆ R`, and any decidable L reduces to its own complement. |
| 19 | 2022-1 moed B Q3 | `sort(L)` regular whenever L is | **false** | clean counterexample: `L = (12)* ∈ REG`, `sort(L) = {1ⁿ2ⁿ} ∉ REG`. |
| 20, 40 | 2022-2 moed B Q8 | `ST-Conn₂₀₂₂` — path s→t of length ≤ 2022 | **L** | p. 40 has the full recursive `Reach(G,s,t,d)` with **constant depth 2022** ⟹ `O(log n)` space. Explicitly notes depth, not branching, is what costs space. |
| 21 | 2022-2 moed B Q9 | `2-Clique` — two disjoint cliques, sizes k and 2k | NP-Complete | note flags that the earlier attempt over-complicated the construction. |
| 22–23 | 2025-1 moed A Q2 | 3-**coloured** DFA, minimal, for "both a and b appear" | — | 3-state solution drawn; subset-construction remark alongside. |
| 24 | 2025-1 moed A Q5 | `{⟨M₁,M₂⟩ : L(M₁) = rev(L(M₂))}` | ¬(RE ∪ coRE) | short note on M₁ vs M₂ roles. |
| 25 | 2025-1 moed A Q7 | CNF with a satisfying assignment setting ≥ half the variables T | NP-Complete | *"reduce from **3SAT**, not from SAT"* — recorded as the slip. |
| 27 | 2025-1 moed A Q8.א | `ALL_NFA ≤p PATH` | **unknown** | `PATH ∈ NL`; the page argues that a poly-**time** reduction is not ruled out — contrast with `≤L`, which is provably false. |
| 28–29 | (moed A) Q2 | `cyclic(L)` regular | **true** | Full construction written out: `Q′ = Q × Σ ∪ {(q₀,ε)}`, `F′ = {(q,σ) : δ(q,σ) ∈ F}`, `q₀′ = (q₀,ε)`, with the transition function and both directions of correctness. The most complete proof in the notebook. |
| 30 | (moed A) Q8 | simple path s→t of length ≥ k | NP-complete | — *(partly illegible)* |
| 31 | (moed C) Q4 | `L(M₁) ∩ L(M₂) = ∅` | coRE ∖ R | — |
| 32 | 2024 summer moed A Q6 | accepts `σσ` in one step but does **not** halt on `σσσσ` | **R** | the empty-language trap: the condition is unsatisfiable, so `L = ∅ ∈ R`. |
| 33 | 2024 summer moed A Q8 | `⟨G,k⟩ ∈ VC` **and** `⟨G,k⟩ ∈ IS` | NP-complete | note on `H ⊆ V` being simultaneously a cover and independent. |
| 35 | 2020 winter moed A III.7 | `PATH ≤p HAMCYCLE` | **true** | crossed out `P = NP` and `NP = NL` — correctly identified as unconditionally true, no collapse needed. |
| 36 | (unidentified) Q3.א | NP verifier characterization, fill in the theorem | — | the missed clause written large: **"\|c\| polynomial in \|w\|!"** |
| 37 | 2022-1 moed A Q8 | `TQBF ≤p A_TM` | **true** | `TQBF ∈ R`, so a decider can be hard-coded into the target instance. |
| 42 | 2020 summer moed B Q10 | CNF satisfiable with `xᵢ = 1` and also with `xᵢ = 0`, for every i | NP-complete | reduction from CNF-SAT adding `(y ∨ ȳ)`-style clauses. |
| 43 | 2024 winter moed B Q4 | `ALT-SAT` → direct reduction to CNF-SAT | — | expands `ALT(ℓ₁,…,ℓ_k)` and counts the non-satisfying assignments of an ALT clause over k literals. |
| 44 | 2024 winter sample | `E-SET-COVER ≤p CNF-SAT` | — | pairwise-disjointness needs `C(m,2) = O(m²)` clauses ⟹ still polynomial. **Page notes the answer was checked against Gemini** — worth re-verifying against the official solution. |
| 45–46 | 2021 summer moed B III.7 | `ALL_DFA ≤L PATH̄` | **true** | two-DFA sketch; `⟨A⟩ ↦ ⟨G,s,t⟩` with `L(A) = Σ*` ⟺ no s→t path. |
| 47 | (unidentified) part ג | `L = {⟨M⟩ : L(M) ∈ R}` is coRE-hard | — | `NON-HALT ≤ₘ L`. |
| 48 | (unidentified) Q4 | communication complexity of `f(x,y) = #₁(x) + #₁(y)` | `O(log n)` | send the count in binary — `log n` bits suffice. |
| 49 | (unidentified) | `S-3-XOR-SAT ≤p S-3-CNF-SAT` | — | `⟨φ,k⟩ ↦ ⟨φ′, 3m+k⟩`; each XOR clause expands to 4 CNF clauses. |
| 50 | — | heading only ("leaves at least 3 clauses"), otherwise blank. |

---

# What this notebook adds over the existing notes archive

Cross-referenced against the 37 docs in this folder.

**Already covered elsewhere** (the notebook agrees with them): 2022-2 moed C Q6–Q9; 2022-2 moed A
Q7–Q8; 2025 summer moed A Q9; 2025-1 moed A Q5–Q8; 2024 summer moed A Q6/Q8; 2023-2 moed A Q6;
2020 winter moed A III.7; the `L(M) ∈ R` coRE-hardness question.

**Not covered by any existing notes doc** — these are the gaps this scan surfaces:

1. **`sort(L)` regularity** (2022-1 moed B Q3) — with a one-line counterexample worth keeping.
2. **`cyclic(L)` regularity** — the notebook's fullest construction, nothing in the archive.
3. **`EXP_TM = {⟨M⟩ : L(M) ∈ EXP ∖ P}`** — an EXP-flavoured Rice question absent from the archive.
4. **`ALT-SAT`** (2024 winter moed B Q4) — the direct-reduction variant.
5. **`E-SET-COVER ≤p CNF-SAT`** — and the page itself flags that it was checked against an AI,
   not the official solution.
6. **`S-3-XOR-SAT ≤p S-3-CNF-SAT`.**
7. **`2MON`** (2024 summer moed B Q7) — one of the six wrong answers, no notes doc exists.
8. **Communication complexity** (`#₁(x) + #₁(y)` in `O(log n)`) — the archive has no
   communication-complexity material at all.
9. **`L-Mix`** and the interleaving transition trick (p. 6).
10. **`ALL_DFA ≤L PATH̄`** (2021 summer moed B III.7).

**One new recurring slip not in the weak-points doc:** the **dead/trap state** in subset
construction. It appears three times — as a standing reminder (p. 2), as the ε-move slip on p. 9,
and as a red correction on the DFA drawing (p. 13). Everything else in the notebook maps onto
weak points W1–W8 already recorded in `Study guide - weak points and exam focus plan.md`.

**Two items to re-verify before trusting them:** the `E-SET-COVER` answer (p. 44, AI-checked
only), and the reduction direction written on p. 9 for `XYTIME` — the page carries both
directions and the correct one is `HALT ≤ₘ XYTIME`.

---

## Issues log

- **(2026-07-28)** Initial scan of the 51-page handwritten notebook. Indexed all pages, extracted
  6 crossed-out wrong answers and ~30 worked questions, and cross-referenced against the existing
  notes archive — 10 questions in the notebook have no corresponding notes doc. Dominant error
  pattern in the notebook matches W2 (name vs definition) and W5 (quantifier shape); the one new
  recurring slip is the missing dead/trap state in subset construction.
