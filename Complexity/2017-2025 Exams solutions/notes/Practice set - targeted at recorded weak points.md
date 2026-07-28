# Practice set — targeted at recorded weak points

Twenty questions written against the error record in
`Study guide - weak points and exam focus plan.md` and
`Handwritten notebook - full scan index and mistakes.md`.

These are **new questions**, not reprints — but every one is built around a trap you have actually
fallen into, in the same shape the exams use it. Several are deliberate near-misses of past
questions: the surface looks familiar, the answer is different.

**How to use it:** sit Part 1 cold, with no notes, in ~2 hours. Then mark against Part 2. The
weak-point tags (W1–W8) are in the answer key only — they would give the answers away.

Scoring: 12 points each unless marked otherwise, 240 total.

---

# Part 1 — Questions

## Section A — Graph language classification

**Q1.** `EXACT5 = {⟨G,s,t⟩ : G is a directed graph and the distance from s to t is exactly 5}`.
Which complexity class does `EXACT5` belong to? Circle the tightest one and prove it.

  `L`  `NL-Complete`  `NP-Complete`  `PSPACE-Complete`

**Q2.** `THIRD = {⟨G,s,t⟩ : G is a directed graph containing a simple path from s to t with at
least |V(G)|/3 edges}`. Which class does `THIRD` belong to? Prove it.

  `L`  `NL-Complete`  `NP-Complete`  `PSPACE-Complete`

**Q3.** (12 pts, 6 each) Classify **both** of the following, and say in one sentence what makes
them differ:

  (a) `CYC₁₀₀ = {⟨G⟩ : G is a directed graph containing a cycle of length at most 100}`
  (b) `CYC = {⟨G⟩ : G is a directed graph containing a cycle}`

**Q4.** `EVENDIST = {⟨G,s,t⟩ : G is a directed graph, t is reachable from s, and the distance
from s to t is even}`. Which class does `EVENDIST` belong to? Prove membership **and** hardness.

## Section B — Computability classification

**Q5.** `L = {⟨M⟩ : M is a TM, M halts on every input, and L(M) ∈ RE ∖ coRE}`.
To which computability class does L belong?

  `R`  `RE ∖ R`  `coRE ∖ R`  `outside RE ∪ coRE`

**Q6.** `L = {⟨M⟩ : M is a TM and for every w ∈ Σ*, M accepts w in exactly |w| steps}`.
To which computability class does L belong?

  `R`  `RE ∖ R`  `coRE ∖ R`  `outside RE ∪ coRE`

**Q7.** (18 pts, 6 each) Classify each of the following. For each one, **first write the
quantifier prefix explicitly**, then classify.

  (a) `L₁ = {⟨M⟩ : there exists w ∈ Σ* such that M halts on w within |w|² steps}`
  (b) `L₂ = {⟨M⟩ : for every w ∈ Σ*, if M halts on w then M accepts w}`
  (c) `L₃ = {⟨M⟩ : there exists w ∈ Σ* such that M does not halt on w}`

**Q8.** `L = {⟨M⟩ : L(M) ∈ P}`. Show that L is **neither** RE **nor** coRE.

## Section C — True / False / Unknown

For each claim, mark **נכונה** (true), **לא נכונה** (false), or **נכונותה לא ידועה** (unknown).
A "false" answer requires an actual proof. If the answer is "unknown", name the open problem it
is equivalent to.

**Q9.** (18 pts, 6 each) Three claims about the *same* two languages:

  (a) `TQBF ≤ₘ SAT`
  (b) `TQBF ≤p SAT`
  (c) `TQBF ≤L PATH`

**Q10.** (6 pts) `HALT ≤p A_TM`.

**Q11.** (6 pts) `TQBF ∉ NP`.

**Q12.** (12 pts, 6 each)  (a) `NL ⊊ PSPACE`   (b) `P ⊊ PSPACE`

**Q13.** (6 pts) For all languages A, B: if `A ≤ₘ B` then `Ā ≤ₘ B`.

**Q14.** (6 pts) For all languages A, B: if `A ≤p B` and B is NP-complete, then A is NP-complete.

## Section D — Automata

**Q15.** Let N be the following NFA over Σ = {0,1}: states {q₀,q₁,q₂}, start q₀, accepting {q₂},
transitions δ(q₀,0) = {q₀}, δ(q₁,1) = {q₂}, an ε-move q₀ → q₁, and **no other transitions**.

  (a) Apply the subset construction. How many states does the resulting DFA have? List them.
  (b) What is L(N)?
  (c) Is the resulting DFA minimal? Justify.

**Q16.** L₁ and L₂ are languages over Σ = {a} with exactly 6 and exactly 7 Myhill–Nerode classes
respectively. **Claim:** every DFA recognising `L₁ ∩ L₂` has at least 20 states.
True or false? Prove or give a counterexample.

**Q17.** Recall the *k-coloured DFA* from `2025-1 moed A Q2`: a DFA together with a total colouring
`f : Q → [k]`, where a run `q₀,q₁,…,qₙ` is **accepting** iff for every colour `c ∈ [k]` there is
some `i` with `f(qᵢ) = c` — the run must visit **every** colour.

  (a) (8 pts) Give a 4-coloured DFA with the **minimum** number of states for
      `L = {w ∈ {a,b,c}* : all three letters appear in w}`. Prove minimality.
  (b) (4 pts) State the general transform converting a k-coloured DFA into an ordinary DFA, and
      give the resulting state count.

**Q18.** For `w ∈ {1,2}*`, `sort(w)` is w with its letters rearranged in non-decreasing order, and
`sort(L) = {sort(w) : w ∈ L}`. You already know that L regular does **not** imply sort(L) regular.

**Claim:** if `sort(L)` is regular then L is regular. True or false? Prove or give a counterexample.

## Section E — Reductions and gadgets

**Q19.** `HALF-VC = {⟨G⟩ : G is an undirected graph with a vertex cover of size at most |V(G)|/2}`.
Which class does `HALF-VC` belong to? Give a full reduction — note that the input has **no k**.

  `P`  `NP-Complete`  `PSPACE-Complete`

**Q20.** Alice holds `x ∈ {0,1}ⁿ`, Bob holds `y ∈ {0,1}ⁿ`. Let `#₁(z)` be the number of 1s in z.
Give a communication protocol using `O(log n)` bits that lets Bob output

  `f(x,y) = 1` if `#₁(x) > #₁(y)`, and `0` otherwise,

and explain why `O(log n)` bits suffice.

---
---

# Part 2 — Answer key

## Q1 — `EXACT5`  →  **L**   *(W2: constant bound, not the name "distance")*

The word "distance" is the trap: it made `LongPath` NL-complete on 2022-2 moed A Q7, so it now
reads as an NL signal. Here the bound is a **constant**, and the constant wins.

`distance(s,t) = 5` ⟺ (∃ path s→t of length exactly 5) ∧ (∄ path s→t of length ≤ 4).

Both conjuncts are decided by depth-bounded DFS of **constant depth**: enumerate all sequences of
at most 5 vertices, checking consecutive edges. Space = depth × frame = `5 · O(log n) = O(log n)`,
and it is **deterministic** — nothing is guessed, we exhaustively iterate. So the second conjunct
needs no `NL = coNL` appeal. Hence `EXACT5 ∈ L`.

> **The rule:** a threshold that does not grow with the input is decided by brute force at constant
> depth. `L`, not `NL`. Compare `ST-Conn₂₀₂₂` (2022-2 moed B Q8), which you got right.

## Q2 — `THIRD`  →  **NP-Complete**   *(W2 threshold rule + W8 padding)*

**In NP:** the witness is the path. Verify in poly time that it starts at s, ends at t, uses real
edges, has ≥ |V|/3 edges, and — the part that was missed on 2022-2 moed A Q8 — that **all its
vertices are distinct**. Distinctness is what forces Θ(n) witness bits and rules out NL.

**NP-hard:** `HAMPATH ≤p THIRD`. Given `⟨G,s,t⟩` with n vertices, a Hamiltonian path has exactly
`n−1` edges. Build `G'` by adding `2n−3` **isolated** vertices, so `|V(G')| = 3n−3` and the
threshold becomes `|V(G')|/3 = n−1`.

Isolated vertices add no edges, so the longest simple path in `G'` is the longest simple path in G,
which has at most `n−1` edges. Therefore `G'` has a simple path s→t with ≥ n−1 edges **iff** G has
one with exactly n−1 edges, i.e. iff `⟨G,s,t⟩ ∈ HAMPATH`. Poly-time. ∎

> **The rule (the 2025 summer moed A Q9 trap, restated):** a **constant** threshold ⟹ P. A
> threshold that is a **fraction of n** ⟹ NP-complete, and isolated-vertex padding is always the
> reduction. "There is no k in the input" does not make it easier.

## Q3 — the mirror pair   *(W3: depth is everything)*

**(a) `CYC₁₀₀` → L.** For each start vertex v, search for a return to v at depth ≤ 100. Constant
depth ⟹ `O(log n)` space, deterministic. The outer loop over v reuses the same space.

**(b) `CYC` → NL-complete.** *In NL:* guess a vertex v, then guess a walk from v back to v of
length between 1 and |V|, keeping only the current vertex, v, and a counter — `O(log n)` bits.
*NL-hard:* `PATH ≤L CYC`. Given `⟨G,s,t⟩`, output `G'` = G plus the edge `(t,s)`, after first
deleting every edge not on some s–t-relevant part… simpler and correct: delete all outgoing edges
of t except the new `(t,s)`, and all incoming edges of s. Then any cycle in `G'` must use `(t,s)`,
so `G'` has a cycle iff G has a path s→t. The output is emitted **streamed** — the output tape is
write-only and uncharged, so this is logspace.

**The difference in one sentence:** the bound on the search depth. Constant ⟹ L; `|V|` ⟹ NL.
**Branching factor is a time cost, never a space cost** — this is exactly the error made on
2022-2 moed B Q8 (estimating `|V|·log|V|`).

## Q4 — `EVENDIST` → **NL-Complete**   *(W3: NL = coNL is load-bearing)*

**In NL:** nondeterministically guess the distance `d ∈ {0,…,|V|−1}` (a counter, `O(log n)` bits;
shortest paths are simple so d < |V|). Then verify **both**:

- `∃` path s→t of length exactly d — guess it, `O(log n)` bits; and
- `∄` path s→t of length < d — this is a **universal** condition. Its complement ("some path
  shorter than d exists") is in NL, so by **`NL = coNL`** (Immerman–Szelepcsényi) the condition
  itself has an NL algorithm.

Accept iff d is even and both checks pass. Space is reused between the two checks, so the total
stays `O(log n)`.

**NL-hard:** `PATH ≤L EVENDIST`. Given `⟨G,s,t⟩`, **subdivide every edge**: replace each `(u,v)`
with `(u,m_{uv})` and `(m_{uv},v)` for a fresh midpoint. Every path length doubles, so every
distance in `G'` is even, and t is reachable from s in `G'` iff it is in G. Hence
`⟨G,s,t⟩ ∈ PATH ⟺ ⟨G',s,t⟩ ∈ EVENDIST`. Logspace: emit two edges per input edge, streamed. ∎

> **The trigger to memorise:** whenever the condition contains a **universal** ("no shorter path",
> "stays connected", "every edge"), the move is *complement ∈ NL, then cite NL = coNL*. You have
> now needed this on 2022-2 moed C Q9, 2022-2 moed A Q7, and here.

## Q5 — → **R**  (L = ∅)   *(W4: test satisfiability first)*

If M halts on every input then M is a decider, so `L(M) ∈ R`. And `R ⊆ coRE`. So
`L(M) ∈ RE ∖ coRE` is **impossible** — the two conditions are contradictory. Hence `L = ∅ ∈ R`.

> This is the trap that cost Q5 of the most recent paper (2025-2026 winter moed A), in a new
> disguise: there the slice was `coRE ∖ R` against `L(M)` always being RE; here it is `RE ∖ coRE`
> against `L(M)` being forced into R by the halting condition. **Whenever a question names a class
> slice `X ∖ Y` applied to `L(M)`, check satisfiability before anything else.**

## Q6 — → **R**  (L = ∅)   *(W4: bounded-step traps)*

Take `w = ε`, of length 0. "M accepts ε in exactly 0 steps" forces the start state `q₀` to be
accepting. But then M accepts **every** input in 0 steps — in particular it accepts each `w` with
`|w| = 1` in 0 steps, not in exactly 1 step, since the computation has already halted.

So no machine satisfies the condition: `L = ∅ ∈ R`.

> Same family as 2024 summer moed A Q6 ("accepts σσ in one step but does not halt on σσσσ"), which
> you got right. The tell is a **step count tied to the input** — check the shortest input first,
> it usually collapses the whole thing.

## Q7 — the quantifier drill   *(W5)*

**(a) `L₁` → RE ∖ R.** Prefix: `∃w [M halts on w within |w|² steps]`. The bracket is **decidable**
— simulate for exactly `|w|²` steps and look. `∃` over a decidable predicate ⟹ **RE** (dovetail
over all w). Not in R: `HALT ≤ₘ L₁`. Given `⟨M,w⟩`, build `M'` that on input x hardcodes w,
simulates M on w, and halts if that simulation halts. If M halts on w in T steps, then for every x
with `|x|² > T + c` (overhead), `M'` halts on x within `|x|²` steps — such x exist, so
`⟨M'⟩ ∈ L₁`. If M never halts on w, `M'` halts on nothing, so `⟨M'⟩ ∉ L₁`. ∎

**(b) `L₂` → coRE ∖ R.** Prefix: `∀w [M halts on w → M accepts w]`. **Negate it mechanically:**
`¬∀ = ∃¬`, and **`¬(A → B) = A ∧ ¬B`** — never negate an implication into another implication.
So `L̄₂ = {⟨M⟩ : ∃w, M halts on w AND M rejects w}`, which is **RE** (dovetail; halting-and-
rejecting is observable). Hence `L₂ ∈ coRE`. Not in R by a reduction from `HALT`-complement in the
same style. ∎

**(c) `L₃` → outside RE ∪ coRE.** Prefix: `∃w [M does not halt on w]`. The bracket is **coRE, not
decidable**. This is `¬TOTAL`, and TOTAL is the standard Π₂-complete language, so `L₃` is Σ₂-
complete — outside both. Prove it on an exam with **two** reductions: `HALT ≤ₘ L₃` and
`HALT ≤ₘ L̄₃`.

> **The distinction that was missed on 2025-1 moed A Q6:** `∃` over a **decidable** or even a
> merely **semi-decidable** condition stays inside RE — dovetailing finds the witness. It escapes
> RE ∪ coRE only when the inner predicate is **coRE** (as in (c)), or when a `∀` wraps an RE
> predicate. (a) and (c) look almost identical and land in different classes; the only difference
> is whether the inner condition is step-bounded.

## Q8 — `{⟨M⟩ : L(M) ∈ P}` is neither RE nor coRE   *(W5: two reductions)*

Fix `A = A_TM`, which is RE but **not** in P (it is not even decidable). Both directions
ignore-and-simulate:

**`HALT ≤ₘ L`, so L ∉ coRE.** Given `⟨M,w⟩`, build `M₁`: on input x, run M on w and *in parallel*
check `x ∈ A_TM`; accept if **either** succeeds.
- M halts on w ⟹ `L(M₁) = Σ*` ∈ P ⟹ `⟨M₁⟩ ∈ L`.
- M does not halt on w ⟹ `L(M₁) = A_TM` ∉ P ⟹ `⟨M₁⟩ ∉ L`.

**`HALT ≤ₘ L̄`, so L ∉ RE.** Given `⟨M,w⟩`, build `M₂`: on input x, **first** simulate M on w
(ignoring x); only if that halts, decide whether `x ∈ A_TM` and accept accordingly.
- M does not halt on w ⟹ `M₂` loops on everything ⟹ `L(M₂) = ∅` ∈ P ⟹ `⟨M₂⟩ ∈ L`.
- M halts on w ⟹ `L(M₂) = A_TM` ∉ P ⟹ `⟨M₂⟩ ∉ L`.

Both reductions are computable. ∎

> **The pattern to reuse:** *parallel* simulation puts the hard language in the **no**-case;
> *sequential* simulation puts it in the **yes**-case. Switching between the two is how you get the
> two opposite-polarity reductions that "neither RE nor coRE" always requires.

## Q9 — same two languages, three verdicts   *(W1 resource bound + W6)*

**(a) `TQBF ≤ₘ SAT` → TRUE.** By the **constant-output lemma**: `TQBF ∈ PSPACE ⊆ R`, so it is
decidable, and SAT is non-trivial (`SAT ≠ ∅, Σ*`). The reduction decides its input — taking
however long it takes, since `≤ₘ` has **no resource bound** — then prints one of two hardcoded
constants, one satisfiable formula and one unsatisfiable one. Output is write-only and free.

**(b) `TQBF ≤p SAT` → UNKNOWN.** SAT ∈ NP and NP is closed under `≤p`, so this claim gives
`PSPACE ⊆ NP`, and `NP ⊆ PSPACE` always holds. So the claim is **equivalent to `NP = PSPACE`** —
an open problem. Not false: nothing rules it out.

**(c) `TQBF ≤L PATH` → FALSE.** `PATH ∈ NL` and NL is closed under `≤L`, so the claim gives
`PSPACE ⊆ NL`, i.e. `NL = PSPACE`. But `NL ⊊ PSPACE` is a **theorem** (Savitch gives
`NL ⊆ SPACE(log²n)`, and the space hierarchy theorem gives `SPACE(log²n) ⊊ PSPACE`).
Contradiction, so the claim is refuted. ∎

> **This is W1 in one question.** The same pair of hard languages, three relations, three
> different verdicts. Before writing anything: *which relation, and which direction?* This is
> exactly the `ALL_NFA ≤p PATH` vs `ALL_NFA ≤L PATH` split on 2025-1 moed A Q8.א.

## Q10 — `HALT ≤p A_TM` → **TRUE**   *(W1)*

The map `⟨M,w⟩ ↦ ⟨M',w⟩`, where `M'` is M with its reject state rewired into an accepting state,
is a syntactic rewrite of the transition table — **linear time**. Then M halts on w iff M' accepts
w. Both languages are undecidable, which is irrelevant: **undecidability does not obstruct a
poly-time reduction.** Resource bounds constrain the *mapping*, not the *targets*.

## Q11 — `TQBF ∉ NP` → **UNKNOWN**   *(W6, trap 2)*

TQBF is PSPACE-complete. `TQBF ∉ NP` would give `NP ≠ PSPACE`, which is open. **You can never
prove a language is outside NP by showing it is PSPACE-hard** — this was the 2025-2026 winter
moed A Q8.ב error, and it is the single most attractive wrong "false" on these papers.

## Q12 — the hierarchy pair   *(W6: aggregate strictness ≠ sub-link)*

**(a) `NL ⊊ PSPACE` → TRUE.** Proven: Savitch gives `NL ⊆ SPACE(log²n)`, and the space hierarchy
theorem gives `SPACE(log²n) ⊊ SPACE(n) ⊆ PSPACE`.

**(b) `P ⊊ PSPACE` → UNKNOWN.** Open. `P ⊆ PSPACE` is trivial, but no separation is known.

> The tempting bad inference is "we know `L ⊊ PSPACE`, and P sits between them, so P ⊊ PSPACE".
> **Known aggregate strictness gives you no sub-link.** The only four *directly* proven
> separations you may cite for a FALSE verdict: **`L ⊊ PSPACE`, `NL ⊊ PSPACE`, `P ⊊ EXP`,
> `PSPACE ⊊ EXPSPACE`.** Note (a) is on that list and (b) is not — that is the whole question.

## Q13 — → **FALSE**   *(W1 polarity)*

`A ≤ₘ B` gives `Ā ≤ₘ B̄`, **not** `Ā ≤ₘ B`.

Counterexample: `A = B = HALT`. Certainly `HALT ≤ₘ HALT` (identity). If also
`HALT‾ ≤ₘ HALT`, then since HALT ∈ RE and RE is closed downward under `≤ₘ`, we would get
`HALT‾ ∈ RE`; combined with `HALT ∈ RE` and `RE ∩ coRE = R`, this gives `HALT ∈ R` —
contradiction. ∎

## Q14 — → **FALSE**   *(W1 direction)*

`A ≤p B` means **A is no harder than B**. Reducing an easy language into a hard one is free and
proves nothing about A.

Counterexample: `A = 2SAT ∈ P`, `B = 3SAT`, NP-complete. `2SAT ≤p 3SAT` holds (decide the 2SAT
instance in poly time, then output a fixed satisfiable or unsatisfiable 3CNF — the constant-output
lemma again). But `2SAT` is not NP-complete unless P = NP. ∎

> The true statement is the mirror: if `A ≤p B` and **A** is NP-hard, then **B** is NP-hard.
> Hardness flows *forward* along the reduction, membership flows *backward*.

## Q15 — subset construction   *(the notebook's own recurring slip: the dead state)*

**(a) Three states.** First, `E(q₀) = {q₀,q₁}` (the ε-move), so the start state is `{q₀,q₁}`, not
`{q₀}`.

| state | on 0 | on 1 |
|---|---|---|
| `{q₀,q₁}` (start) | `E(δ(q₀,0)) ∪ E(δ(q₁,0)) = {q₀,q₁} ∪ ∅ = {q₀,q₁}` | `∅ ∪ E(q₂) = {q₂}` |
| `{q₂}` (accepting) | `∅` | `∅` |
| `∅` | `∅` | `∅` |

Reachable states: `{q₀,q₁}`, `{q₂}`, **`∅`**. The empty set is a genuine reachable state and the
DFA is not a DFA without it — every state needs an outgoing edge on **every** letter.

**(b) `L(N) = 0*1`.**

**(c) Yes, minimal** — three pairwise-inequivalent MN classes: `ε ~ 0` (suffix `1` accepted),
`1` (suffix `ε` accepted), `11` (nothing accepted, the dead class). Note the dead class is a
**real MN class**: MN classes partition all of `Σ*`, including rejected words.

> Recorded three separate times in the notebook (p. 2 reminder, p. 9 missed ε-move, p. 13 red
> correction on a DFA drawing). It is the cheapest recurring loss in the archive: **always take
> `E(q₀)` first, and always include `∅`.**

## Q16 — → **FALSE**   *(W7: the product bound is an upper bound)*

`MN(L₁ ∩ L₂) ≤ MN(L₁) · MN(L₂) = 42` is an **upper** bound. No lower bound follows from it.

Counterexample over `Σ = {a}`:
- `L₁ = {aⁿ : n ≡ 0 mod 6}` — exactly 6 MN classes ✓
- `L₂ = {aⁿ : n ≥ 6}` — classes `a⁰,…,a⁵` and `{aⁿ : n ≥ 6}`, exactly 7 ✓
- `L₁ ∩ L₂ = {aⁿ : n ≡ 0 mod 6, n ≥ 6}`

The MN classes of the intersection are determined by `(n mod 6, whether n ≥ 6)`; for `n < 6` the
residue already pins n down, giving `6 + 6 = 12` classes. (Check that `a⁰ ≁ a⁶`: with `z = ε`,
`a⁰ ∉ L` but `a⁶ ∈ L`.)

So the minimal DFA has **12** states, and `12 < 20`. The claim is refuted. ∎

> The 2025 summer moed A Q1 tool, used in the other direction: there the product bound **refuted**
> a claimed lower bound of 2025 (`10 × 10 = 100 < 2025`). Here it cannot **establish** one. Same
> inequality, and it only ever points one way.

## Q17 — coloured DFA   *(W7: the construction that was never solved)*

**(a) Four states, and four is minimal.**

States `{s, A, B, C}`; on reading letter `x ∈ {a,b,c}` move to the corresponding state `A`, `B`, or
`C`, from **any** state. Start `s`. Colouring: `f(s) = 4`, `f(A) = 1`, `f(B) = 2`, `f(C) = 3`.

*Correctness:* every run begins at `s`, so colour 4 is always visited. State `A` is visited iff the
letter `a` is read at least once, and likewise for `B`, `C`. So the run visits all four colours iff
all three letters appear. ✓

*Minimality:* the colouring is total and 4 colours must each be visited by some accepting run, so
the automaton needs at least 4 states — one per colour, since a single state carries exactly one
colour. Hence 4 is optimal. ∎

> Sanity-check against 2025-1 moed A Q2, which you solved: there `Σ = {a,b}`, `k = 3`, answer
> 3 states. Same shape — `|Σ| + 1` states, `|Σ| + 1` colours, one "letter just read" state per
> letter plus the start state.

**(b) The general transform.** Augment each state with the **set of colours seen so far**:

`Q' = Q × P([k])`, start `(q₀, {f(q₀)})`, transition `δ'((q,S),σ) = (δ(q,σ), S ∪ {f(δ(q,σ))})`,
accepting states `{(q,S) : S = [k]}`.

State count: **`|Q| · 2^k`**.

## Q18 — → **FALSE**   *(new territory: no notes doc covers `sort`)*

`sort` destroys order information, so it can turn a non-regular language into a regular one.

Take `L = {1ⁿ2ⁿ : n ≥ 0} ∪ {w ∈ {1,2}* : w contains the factor "21"}`.

**`sort(L)` is regular.** A word `w` containing "21" has at least one 1 and at least one 2, so its
sort is `1^a 2^b` with `a,b ≥ 1`; and conversely for any `a,b ≥ 1` the word `2·1^a·2^{b−1}`
contains "21" and sorts to `1^a2^b`. The first part contributes `ε` and the words `1ⁿ2ⁿ` (n ≥ 1),
all of which already have `a,b ≥ 1`. So

`sort(L) = {ε} ∪ {1^a2^b : a,b ≥ 1}`, matched by `ε + 11*22*` — **regular**. ✓

**L is not regular.** `L ∩ 1*2* = {1ⁿ2ⁿ : n ≥ 0}` (a word in `1*2*` contains no "21"), which is not
regular; REG is closed under intersection with a regular language, so L ∉ REG. ∎

> **The recipe for "does the image being regular pull the source back?" questions:** almost always
> no, because the operation is lossy. To build the counterexample, **union in a large regular
> language that swallows the image** — here "contains 21" makes the sort go regular while the
> intersection with `1*2*` still exposes `1ⁿ2ⁿ`.

## Q19 — `HALF-VC` → **NP-Complete**   *(W8: padding in both directions)*

**In NP:** guess the cover, check it covers every edge and has `≤ |V|/2` vertices. Poly time.

**NP-hard:** `VC ≤p HALF-VC`. The difficulty is that `HALF-VC` has **no k** — the threshold is
welded to `|V|`. So the reduction must move the *ratio* `k/n` to exactly `1/2`, and it may need to
move it **in either direction**. Two gadgets, both added as disjoint components:

- an **isolated vertex** adds 1 to n and 0 to the cover ⟹ pushes the ratio **down**;
- a **disjoint triangle** adds 3 to n and exactly 2 to the cover ⟹ pushes the ratio **up**
  (2/3 > 1/2).

Given `⟨G,k⟩` with `|V| = n`, let `t = max(0, n − 2k)` and `a = 2k + t − n` (note `a ≥ 0` by the
choice of t). Build `G'` = G ⊎ (t disjoint triangles) ⊎ (a isolated vertices). Then

`n' = n + a + 3t` and the target threshold is `n'/2 = (n + a + 3t)/2 = k + 2t` by the choice of a.

Since the added components are disjoint from G and a triangle needs exactly 2 cover vertices,
`VC(G') = VC(G) + 2t`. Therefore `VC(G') ≤ k + 2t ⟺ VC(G) ≤ k`, i.e.
`⟨G,k⟩ ∈ VC ⟺ ⟨G'⟩ ∈ HALF-VC`. Both `a` and `t` are `O(n + k)`, so the construction is poly-time. ∎

> **The W8 lesson made explicit:** padding is not only for making things bigger. When a threshold
> is *pinned to |V|*, you need a gadget in each direction, and you solve a small linear equation to
> land on the ratio exactly. The "bolt on a separate disconnected component" move — the one you
> over-engineered past on 2022-2 moed B Q9 — is doing all the work here.

## Q20 — communication protocol, `O(log n)` bits

Alice computes `#₁(x) ∈ {0,1,…,n}` and sends it to Bob **in binary**. Bob computes `#₁(y)` locally
and outputs 1 iff `#₁(x) > #₁(y)`.

**Cost:** `#₁(x)` is an integer in `{0,…,n}`, so it takes `⌈log₂(n+1)⌉ = O(log n)` bits. One
message, one direction. ✓

**Why this is the whole trick:** the function depends on x only through the *count*, not through
which bits are set. Sending `x` itself costs n bits; sending the only statistic that matters costs
`log n`. Nothing about the protocol needs the two counts compared bit by bit — Bob has `#₁(y)` for
free, since local computation is uncharged in this model.

> Same idea as the notebook's p. 48 (`#₁(x) + #₁(y)`), and it generalises: **any f that factors
> through a small statistic of x has communication cost `log(range of the statistic)`.**

---

## Issues log

- **(2026-07-28)** Set written. Coverage by weak point: W1 — Q9, Q10, Q13, Q14; W2 — Q1, Q2, Q3;
  W3 — Q3, Q4; W4 — Q5, Q6; W5 — Q7, Q8; W6 — Q9, Q11, Q12; W7 — Q15, Q16, Q17; W8 — Q19.
  Q15 targets the dead/trap-state slip recorded three times in the handwritten notebook. Q18 and
  Q20 cover `sort` and communication complexity, two topics with no notes doc in the archive.
  Q1/Q2 and Q3(a)/(b) are deliberate mirror pairs — the near-identical surface with different
  answers is the format that cost two questions on 2022-2 moed A.
