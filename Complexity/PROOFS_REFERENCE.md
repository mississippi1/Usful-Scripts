# Computability & Complexity — Proof Catalog (Ground Truth)

Every proof appearing in the `Complexity` folder's files, **grouped by technique**, with stable IDs used identically in Part 1 (overview) and Part 2 (full detail).

**Source key — abbreviation → exact file in `Complexity/`:**

| Tag | Exact file |
|---|---|
| `Sum wN` (all weeks) | `מודלים חישוביים, חישוביות וסיבוכיות - סיכום קורס 2025 סמסטר ב.pdf` (the 82-page course summary; `wN` = week N inside it) |
| `Rec1` | `תרגול 1.pdf` |
| `Rec2` | `תרגול 2-מעודכן.pdf` |
| `Rec3` | `Computability_2025_2026_b (1).pdf` (English Recitation 3) |
| `Rec5` | `תרגול 5 - חישוביות.pdf` |
| `Rec6` | `תרגול 6.pdf` |
| `Rec7` | `Computability_2025_2026_b.pdf` (English Recitation 7) |
| `Rec8` | `תרגול 8.pdf` |
| `Rec9` | `תרגול 9 (2).pdf` |
| `Rec10` | `תרגול 10.pdf` |
| `Rec12` | `תרגול 12 (4).pdf` |
| `HRec10` | `recitations/recitation 10.pdf` (Hebrew) |
| `HRec11` | `recitations/recitation 11.pdf` (Hebrew — the TQBF proofs, no English twin exists) |
| `Lec9` | `lessons/lesson 9.pdf` (content-identical to the corresponding pages of `lessons/all-lectures.pdf`) |
| `Lec10` | `lessons/lesson 10.pdf` |
| `Lec12` | `lessons/lesson 12.pdf` |
| `Lec13` | `lessons/lesson 13.pdf` |
| `Ex1` (hint only, not a proof) | `Computability_2025_2026_b (11).pdf` (Exercise 1) |

**Grounding rule (enforced):** only arguments actually written in the files appear here. Where a file *states* a result but defers the proof to homework or the lecture, the entry is marked **⚠ INCOMPLETE IN SOURCES** and only what the file contains is given. Exercise sheets contain statements without solutions, so nothing is sourced *only* to an `[ExN]`.

**Technique groups:**
- **A** — Induction on words & automata constructions
- **B** — Myhill–Nerode, separating suffixes & pigeonhole
- **C** — Simulation & TM construction (closure properties, dovetailing)
- **D** — Counting & diagonalization
- **E** — Mapping reductions (computability)
- **F** — Polynomial reductions, NP & Cook–Levin
- **G** — Space complexity, hierarchy theorems, NL, PSPACE
- **H** — Randomized classes (probabilistic arguments)

---

## Per-proof source index

Every one of the 90 proofs below, with the **exact file(s)** it was read from — no abbreviations. Where two files are listed, the result is corroborated across both (e.g. an English recitation and the course summary covering the same session).

<details>
<summary><b>Click to expand — full ID → source-file table (90 rows)</b></summary>

| ID | Proof | Source file(s) |
|---|---|---|
| **A1** | A specific DFA decides L = {w starts with a} — the template for all... | `תרגול 1.pdf` |
| **A2** | δ*(q, w·w′) = δ*(δ*(q,w), w′) | `תרגול 1.pdf`; `מודלים חישוביים, חישוביות וסיבוכיות - סיכום קורס 2025 סמסטר ב.pdf` |
| **A3** | REG closed under ∪ and ∩ (product automaton) | `מודלים חישוביים, חישוביות וסיבוכיות - סיכום קורס 2025 סמסטר ב.pdf` |
| **A4** | NREG closed under union | `תרגול 2-מעודכן.pdf`; `מודלים חישוביים, חישוביות וסיבוכיות - סיכום קורס 2025 סמסטר ב.pdf` |
| **A5** | NREG closed under concatenation | `תרגול 2-מעודכן.pdf`; `מודלים חישוביים, חישוביות וסיבוכיות - סיכום קורס 2025 סמסטר ב.pdf` |
| **A6** | The two definitions of δ* for NFAs agree | `תרגול 2-מעודכן.pdf` |
| **A7** | NREG = REG (determinization / subset construction) | `Computability_2025_2026_b (1).pdf`; `מודלים חישוביים, חישוביות וסיבוכיות - סיכום קורס 2025 סמסטר ב.pdf` |
| **A8** | L_EVEN = {w∈L : \|w\| even} is regular | `תרגול 1.pdf` |
| **A9** | L_mix ∈ NREG for regular L | `תרגול 2-מעודכן.pdf`; `Computability_2025_2026_b (1).pdf` |
| **B1** | Words reaching the same DFA state have no separating suffix | `Computability_2025_2026_b (1).pdf` |
| **B2** | ∼_L is an equivalence relation | `Computability_2025_2026_b (1).pdf` |
| **B3** | Myhill–Nerode theorem: finitely many classes ⟺ regular; #classes =... | `מודלים חישוביים, חישוביות וסיבוכיות - סיכום קורס 2025 סמסטר ב.pdf`; `Computability_2025_2026_b (1).pdf` |
| **B4** | Any DFA for L_k (kth letter from the end is a) has ≥2^k states | `תרגול 2-מעודכן.pdf`; `מודלים חישוביים, חישוביות וסיבוכיות - סיכום קורס 2025 סמסטר ב.pdf` |
| **B5** | {w : #a(w) ≥ #b(w)} not regular | `Computability_2025_2026_b (1).pdf` |
| **B6** | {1^{n²}} not regular | `Computability_2025_2026_b (1).pdf` |
| **B7** | {1^p : p prime} not regular | `Computability_2025_2026_b (1).pdf` |
| **B8** | {aⁿbⁿ} not regular | `מודלים חישוביים, חישוביות וסיבוכיות - סיכום קורס 2025 סמסטר ב.pdf` |
| **C1** | {⟨M,w,k⟩ : M accepts w within k steps} ∈ R | `תרגול 5 - חישוביות.pdf` |
| **C2** | NON-EMPTY_TM ∈ RE (dovetailing) | `תרגול 5 - חישוביות.pdf` |
| **C3** | R closed under complement, ∪, ∩ | `תרגול 5 - חישוביות.pdf` |
| **C4** | RE closed under ∩ and ∪ | `תרגול 5 - חישוביות.pdf` |
| **C5** | R = RE ∩ coRE | `מודלים חישוביים, חישוביות וסיבוכיות - סיכום קורס 2025 סמסטר ב.pdf` |
| **C6** | HALT ∈ RE | `מודלים חישוביים, חישוביות וסיבוכיות - סיכום קורס 2025 סמסטר ב.pdf` |
| **C7** | A universal TM exists — **proof-idea level in source** | `מודלים חישוביים, חישוביות וסיבוכיות - סיכום קורס 2025 סמסטר ב.pdf` |
| **C8** | Every 2-tape (k-tape) TM has an equivalent 1-tape TM; time O(t)→O(t... | `תרגול 8.pdf` |
| **C9** | USELESS ∈ coRE | `תרגול 6.pdf` |
| **D0** | Undecidable decision problems exist (counting) | `מודלים חישוביים, חישוביות וסיבוכיות - סיכום קורס 2025 סמסטר ב.pdf`; `Computability_2025_2026_b (11).pdf` |
| **D1** | HALT ∉ R | `תרגול 5 - חישוביות.pdf`; `מודלים חישוביים, חישוביות וסיבוכיות - סיכום קורס 2025 סמסטר ב.pdf` |
| **D2** | DECIDABLE (provable-or-refutable claims) ∉ R | `מודלים חישוביים, חישוביות וסיבוכיות - סיכום קורס 2025 סמסטר ב.pdf` |
| **D3** | BB(n) is not computable | `תרגול 6.pdf` |
| **D4** | Time Hierarchy Theorem: TIME(o(f)) ⊊ TIME(f·log f), f time-construc... | `lessons/lesson 10.pdf`; `תרגול 12 (4).pdf` |
| **D5** | Space Hierarchy Theorem: SPACE(o(f)) ⊊ SPACE(f), f space-constructible | `lessons/lesson 10.pdf` |
| **E1** | L_even-length ≤m L_odd-length, two ways | `תרגול 5 - חישוביות.pdf` |
| **E2** | HALT ≤m NON-EMPTY_TM | `תרגול 5 - חישוביות.pdf` |
| **E3** | Reduction theorem: A≤mB ∧ B∈{R,RE,coRE} ⇒ A∈ same | `תרגול 5 - חישוביות.pdf`; `תרגול 6.pdf` |
| **E4** | HALT ≤m A_TM and A_TM ≤m HALT | `מודלים חישוביים, חישוביות וסיבוכיות - סיכום קורס 2025 סמסטר ב.pdf` |
| **E5** | A_TM is RE-complete | `מודלים חישוביים, חישוביות וסיבוכיות - סיכום קורס 2025 סמסטר ב.pdf` |
| **E6** | HALT-bar is coRE-complete | `מודלים חישוביים, חישוביות וסיבוכיות - סיכום קורס 2025 סמסטר ב.pdf` |
| **E7** | Non-HALT is coRE-complete | `מודלים חישוביים, חישוביות וסיבוכיות - סיכום קורס 2025 סמסטר ב.pdf` |
| **E8** | ALL_TM ∉ RE ∪ coRE | `תרגול 6.pdf` |
| **E9** | REG_TM ∉ coRE (∉ RE was Ex6 Q2 | `תרגול 6.pdf` |
| **E10** | RE-hard ⇒ ∉coRE; L RE-complete ⟺ L̄ coRE-complete; hardness spreads... | `תרגול 6.pdf` |
| **E11** | USELESS is coRE-hard (with C9: coRE-complete) | `תרגול 6.pdf` |
| **E12** | NY-HALT is RE-hard and coRE-hard, hence ∉ RE ∪ coRE | `מודלים חישוביים, חישוביות וסיבוכיות - סיכום קורס 2025 סמסטר ב.pdf` |
| **F1** | ≤p composes (transitivity) | `מודלים חישוביים, חישוביות וסיבוכיות - סיכום קורס 2025 סמסטר ב.pdf` |
| **F2** | Reduction theorem for P: A≤pB, B∈P ⇒ A∈P | `Computability_2025_2026_b.pdf` |
| **F3** | P closed under ∪ and complement | `Computability_2025_2026_b.pdf` |
| **F4** | NP closed under ∪ | `Computability_2025_2026_b.pdf` |
| **F5** | CLIQUE ∈ NP and CLIQUE ∈ EXP | `Computability_2025_2026_b.pdf`; `מודלים חישוביים, חישוביות וסיבוכיות - סיכום קורס 2025 סמסטר ב.pdf` |
| **F6** | 3-SAT ∈ NP | `מודלים חישוביים, חישוביות וסיבוכיות - סיכום קורס 2025 סמסטר ב.pdf` |
| **F7** | 3-SAT ≤p CLIQUE | `מודלים חישוביים, חישוביות וסיבוכיות - סיכום קורס 2025 סמסטר ב.pdf` |
| **F8** | CLIQUE ≤p IS | `Computability_2025_2026_b.pdf` |
| **F9** | IS ≤p VC | `תרגול 8.pdf` |
| **F10** | k-SAT ≤p 3-SAT (k>3) | `תרגול 8.pdf` |
| **F11** | 3-SAT ≤p D-ST-HAMPATH | `תרגול 8.pdf` |
| **F12** | U-ST-HAMPATH is NP-complete | `תרגול 9 (2).pdf` |
| **F13** | 3-COLORING is NP-complete | `תרגול 9 (2).pdf` |
| **F14** | 2-SAT ∈ P | `תרגול 9 (2).pdf` |
| **F15** | SUBSET-SUM is NP-complete | `lessons/lesson 9.pdf`; `recitations/recitation 10.pdf` |
| **F16** | SUBSET-SUM ≤p KNAPSACK (KNAPSACK NPC with its verifier) | `תרגול 10.pdf` |
| **F17** | If L is NPC then AtLeastTwo(L) is NPC (2024-A exam) | `תרגול 10.pdf` |
| **F18** | NP = NP′ (verifier characterization) | `תרגול 9 (2).pdf`; `מודלים חישוביים, חישוביות וסיבוכיות - סיכום קורס 2025 סמסטר ב.pdf` |
| **F19** | Cook–Levin: SAT (hence 3-SAT) is NP-complete | `מודלים חישוביים, חישוביות וסיבוכיות - סיכום קורס 2025 סמסטר ב.pdf`; `lessons/lesson 9.pdf` |
| **F20** | coNP hardness mirrors; NP-hard ∩ NP∩coNP ⇒ NP=coNP | `תרגול 10.pdf` |
| **F21** | CNF-TAUTOLOGY ∈ P | `תרגול 10.pdf` |
| **F22** | Search-to-decision: a poly decider for SAT yields a poly *assignmen... | `lessons/lesson 12.pdf` |
| **G1** | Savitch: NSPACE(f) ⊆ SPACE(f²), f space-constructible | `מודלים חישוביים, חישוביות וסיבוכיות - סיכום קורס 2025 סמסטר ב.pdf`; `lessons/lesson 10.pdf` |
| **G2** | PSPACE = NPSPACE | `מודלים חישוביים, חישוביות וסיבוכיות - סיכום קורס 2025 סמסטר ב.pdf` |
| **G3** | L ⊆ P; log-space machines have poly-length output | `מודלים חישוביים, חישוביות וסיבוכיות - סיכום קורס 2025 סמסטר ב.pdf` |
| **G4** | Log-space functions compose (f∘g computable in O(log n) space) | `מודלים חישוביים, חישוביות וסיבוכיות - סיכום קורס 2025 סמסטר ב.pdf`; `lessons/lesson 12.pdf` |
| **G5** | P ⊊ EXP; TIME(n²) ⊊ TIME(n³) | `lessons/lesson 10.pdf`; `תרגול 12 (4).pdf` |
| **G6** | No k with ⋃_{i≤k}TIME(nⁱ) = P | `תרגול 12 (4).pdf` |
| **G7** | Padding: SPACE(n)⊆P ⟺ PSPACE=P; corollary SPACE(nᵏ)≠P ∀k | `תרגול 12 (4).pdf` |
| **G8** | PATH is NL-complete | `מודלים חישוביים, חישוביות וסיבוכיות - סיכום קורס 2025 סמסטר ב.pdf` |
| **G9** | ≤L composes; NL-hardness spreads (B NL-hard ∧ B≤LC ⇒ C NL-hard) | `מודלים חישוביים, חישוביות וסיבוכיות - סיכום קורס 2025 סמסטר ב.pdf` |
| **G10** | NL=coNL ⟺ PATH-bar ∈ NL | `מודלים חישוביים, חישוביות וסיבוכיות - סיכום קורס 2025 סמסטר ב.pdf` |
| **G11** | Immerman–Szelepcsényi: PATH-bar ∈ NL (hence NL=coNL) | `מודלים חישוביים, חישוביות וסיבוכיות - סיכום קורס 2025 סמסטר ב.pdf`; `lessons/lesson 12.pdf` |
| **G12** | NPSPACE = coNPSPACE | `מודלים חישוביים, חישוביות וסיבוכיות - סיכום קורס 2025 סמסטר ב.pdf` |
| **G13** | STRONGLY-CONNECTED is NL-complete | `תרגול 12 (4).pdf`; `lessons/lesson 12.pdf` |
| **G14** | E_NFA (NFA emptiness) is NL-complete | `תרגול 12 (4).pdf` |
| **G15** | 10-CSS (exactly 10 SCCs) is NL-complete; 2-Con, AL2SCC ∈ NL | `תרגול 12 (4).pdf`; `מודלים חישוביים, חישוביות וסיבוכיות - סיכום קורס 2025 סמסטר ב.pdf`; `lessons/lesson 12.pdf` |
| **G16** | TQBF ∈ PSPACE | `recitations/recitation 11.pdf` |
| **G17** | TQBF is PSPACE-hard (with G16: PSPACE-complete) | `recitations/recitation 11.pdf` |
| **H1** | P ⊆ ZPP, P ⊆ RP, P ⊆ BPP | `מודלים חישוביים, חישוביות וסיבוכיות - סיכום קורס 2025 סמסטר ב.pdf` |
| **H2** | RP ⊆ NP | `מודלים חישוביים, חישוביות וסיבוכיות - סיכום קורס 2025 סמסטר ב.pdf` |
| **H3** | RP(p) = RP for any constant p (one-sided amplification) | `מודלים חישוביים, חישוביות וסיבוכיות - סיכום קורס 2025 סמסטר ב.pdf` |
| **H4** | BPP(ε) = BPP (two-sided amplification) | `lessons/lesson 13.pdf` |
| **H5** | BPP = coBPP; RP, coRP ⊆ BPP | `מודלים חישוביים, חישוביות וסיבוכיות - סיכום קורס 2025 סמסטר ב.pdf` |
| **H6** | BPP ⊆ EXP | `מודלים חישוביים, חישוביות וסיבוכיות - סיכום קורס 2025 סמסטר ב.pdf` |
| **H7** | ZPP = RP ∩ coRP | `מודלים חישוביים, חישוביות וסיבוכיות - סיכום קורס 2025 סמסטר ב.pdf`; `lessons/lesson 13.pdf` |

</details>

---

# Part 1 — Overview

## A. Induction on words & automata constructions

| ID | Proves | Core idea |
|---|---|---|
| **A1** | A specific DFA decides L = {w starts with a} — the template for all "L(A)=L" proofs [Rec1] | Characterize which words end in each state (q₀↔ε, q₁↔starts-with-a, q₂↔rest), then induct on \|w\|: base ε, step w=uσ, split by the state reached on u and check every transition preserves the characterization. The characterization instantly gives L(A)=L since q₁ is the only accepting state. |
| **A2** | δ*(q, w·w′) = δ*(δ*(q,w), w′) [Rec1, Sum w1] | Induction on \|w′\| using only the recursive definition of δ*. Base w′=ε collapses by definition; step peels the last letter: δ*(q,ww″σ)=δ(δ*(q,ww″),σ), apply IH, reassemble. Running a concatenation = running the parts in sequence. |
| **A3** | REG closed under ∪ and ∩ (product automaton) [Sum w2] | Build C with states Q×P, ψ((q,p),α)=(δ(q,α),η(p,α)). The whole proof is one invariant, shown by induction: ψ*((q₀,p₀),w) = (δ*(q₀,w), η*(p₀,w)). Choosing accepting states F×P∪Q×G (union) or F×G (intersection) finishes it. |
| **A4** | NREG closed under union [Rec2, Sum w2] | Take the disjoint union of the two NFAs (states, initial states, accepting states all unioned). Key lemma, by induction: every run of C lives entirely inside Q or entirely inside P. Then two-sided containment: a run of A is verbatim a run of C, and any accepting run of C is a run of one original machine. |
| **A5** | NREG closed under concatenation — **⚠ construction only; correctness "left as exercise"** [Rec2, Sum w3] | Keep both NFAs; initial states from A, accepting from B; add ε-transitions from every accepting state of A to every initial state of B. Nondeterminism "guesses" the split point of w=uv. |
| **A6** | The two definitions of δ* for NFAs agree [Rec2] | Show the run-based definition satisfies the recursion's base and recursive case, hence equals the recursively-defined function. Base: runs on ε end where they start. Step: two-sided containment — peel the last configuration of a run / extend a run by one transition. |
| **A7** | NREG = REG (determinization / subset construction) [Rec3, Sum w3] | DFA states = subsets of NFA states; α(S,σ)=⋃_{q∈S}δ(q,σ); accept when S∩F≠∅. One induction shows α*(S,w)=δ*(S,w) — the DFA deterministically tracks the *set* of states the NFA could be in. (REG⊆NREG direction was homework — Ex2 Q1.) |
| **A8** | L_EVEN = {w∈L : \|w\| even} is regular [Rec1] | Product-with-parity: states Q×{0,1}, flip the bit each letter, accept (q,0) with q∈F. Proof sketch level in the source: "A′ is a DFA deciding L_EVEN". |
| **A9** | L_mix ∈ NREG for regular L [Rec2 §6, Rec3 §1] | From a DFA A for L build NFA B with η(q,σ) = {δ(δ(q,α),σ) : α∈Σ} — the NFA guesses the interleaved letter zᵢ, then reads wᵢ. Correctness by splicing runs: an accepting A-run on z₁w₁…zₙwₙ contracts to a B-run on w by keeping every second state, and conversely a B-run expands by naming the guessed zᵢ's. |

## B. Myhill–Nerode, separating suffixes & pigeonhole

| ID | Proves | Core idea |
|---|---|---|
| **B1** | Words reaching the same DFA state have no separating suffix [Rec3 Prop 4] | δ*(q₀,xz) = δ*(δ*(q₀,x),z) = δ*(δ*(q₀,y),z) = δ*(q₀,yz) by A2 — so xz and yz land together, in or out of F together. Contrapositive: a separating suffix forces different states ⇒ k pairwise-separated words force ≥k states. |
| **B2** | ∼_L is an equivalence relation — **⚠ only transitivity proven; refl./symm. "exercise"** [Rec3] | Transitivity: chain the iff's — xz∈L ⟺ yz∈L ⟺ wz∈L for every z. |
| **B3** | Myhill–Nerode theorem: finitely many classes ⟺ regular; #classes = minimal DFA size [Sum w3; Rec3 Prop 6 cites the lecture] | Build the DFA whose states *are* the classes: q₀=[ε], δ([w],α)=[wα], F={[w]:w∈L}. The written proof shows δ is **well-defined**: [w]=[y] ⇒ ∀z(wz∈L⟺yz∈L) ⇒ (specialize z=αz′) ⇒ [wα]=[yα]. Lower bound direction is B1. (The claim δ*([ε],w)=[w] was assigned as Ex3 Q5 — **⚠ not proven in sources**.) |
| **B4** | Any DFA for L_k (kth letter from the end is a) has ≥2^k states [Rec2, Sum w2] | Pigeonhole: 2^k words of length k, fewer states ⇒ two words u≠v collide in a state; append a^{i−1} where i = first differing index; now the kth-from-end letters differ but the runs end in the same state — one accepted, one not: contradiction. |
| **B5** | {w : #a(w) ≥ #b(w)} not regular [Rec3 Prop 7] | Pigeonhole over ε,a,a²,…,a^k for a k-state DFA: some aⁱ, aʲ (i>j) share a state, but bⁱ is a separating suffix (aⁱbⁱ∈L, aʲbⁱ∉L), contradicting B1. |
| **B6** | {1^{n²}} not regular [Rec3 Prop 8] | Infinitely many MN classes: for i<j, z=1^{2i+1} separates 1^{i²} from 1^{j²} because i²+2i+1=(i+1)² is a square while j² < j²+2i+1 < (j+1)² is not. |
| **B7** | {1^p : p prime} not regular — **⚠ sketch only in source** [Rec3 Prop 9] | Any infinite unary regular language contains an arithmetic progression (a state-loop of size k pumps w to w1^k, w1^{2k},…), but primes contain unbounded gaps: n!+2,…,n!+n are all composite. |
| **B8** | {aⁿbⁿ} not regular [Sum w3] | For n≠m, aⁿ ≁_L a^m via suffix bⁿ (aⁿbⁿ∈L, a^m bⁿ∉L) — infinitely many classes. |

## C. Simulation & TM construction

| ID | Proves | Core idea |
|---|---|---|
| **C1** | {⟨M,w,k⟩ : M accepts w within k steps} ∈ R [Rec5 Prop 6] | Universal simulation with a step budget: run M on w for ≤k steps, accept iff it accepted. Halting is guaranteed by the finite budget — bounding the resource is exactly what restores decidability. |
| **C2** | NON-EMPTY_TM ∈ RE (dovetailing) [Rec5 Prop 7] | Can't run M on one word (may loop) or on all words (infinitely many) — so interleave: for n=0,1,2,… run M for n steps on every word of length ≤n. If some w is accepted in k steps, iteration max(\|w\|,k) finds it. |
| **C3** | R closed under complement, ∪, ∩ [Rec5 Props 8–10] | Complement: swap q_acc/q_rej (legal because the machine always halts). Union/intersection: run M₁ then M₂ sequentially (safe — both halt); tape hygiene: keep a marked spare copy of w. Intersection also = complement+union by De Morgan. |
| **C4** | RE closed under ∩ and ∪ [Rec5 Props 11–12] | ∩: sequential still works — a hang means some Mᵢ hasn't accepted, correct behavior. ∪: sequential **fails** (M₁ may hang while M₂ would accept) — dovetail instead: for n=0,1,2,… run each for n steps; accept when either accepts. |
| **C5** | R = RE ∩ coRE [Sum w6] | ⊆ trivial. ⊇: given recognizers M_L and M_L̄, alternate them with growing step budgets; exactly one must eventually answer on any input, so the combined machine always halts and decides L. |
| **C6** | HALT ∈ RE [Sum w5] | Run the universal machine U on ⟨M,w⟩ with **every** final state made accepting: U halts iff M halts on w. |
| **C7** | A universal TM exists — **proof-idea level in source** [Sum w5] | U keeps ⟨M⟩⟨C⟩ on its tape and loops ⟨M⟩⟨C⟩→⟨M⟩⟨C⁺⟩ (look up the δ-rule matching the state/symbol in C, rewrite C) until a final configuration; then cleans up. Each step costs poly(\|⟨M⟩⟨C⟩\|); with optimizations t steps simulate in O(t log t). |
| **C8** | Every 2-tape (k-tape) TM has an equivalent 1-tape TM; time O(t)→O(t²) (O(f)→O(f²)) [Rec8 §4] | Pack both tapes into one via alphabet Γ′=(Γ×Γ×{0,1}×{0,1}): each cell holds both symbols plus "head here" flags. One simulated step = scan for head 1, scan for head 2, apply δ, update. Heads drift ≤t apart, so O(t) per step. |
| **C9** | USELESS ∈ coRE [Rec6 Prop 8, membership half] | USELESS-bar = USEFUL ∪ invalid-inputs; USEFUL ∈ RE by C2-style dovetailing while recording the set of visited states; if M is useful, finitely many (word, step-count) witnesses cover all states, so some iteration k sees them all. |

## D. Counting & diagonalization

| ID | Proves | Core idea |
|---|---|---|
| **D0** | Undecidable decision problems exist (counting) [Sum w1; hinted as Ex1 Q7] | #words over Σ = ℵ₀ ⇒ #TMs/Python programs = ℵ₀, but #languages = 2^{ℵ₀} > ℵ₀. A bijection decision-problems↔languages transfers the gap. Pure cardinality — no explicit hard language produced. |
| **D1** | HALT ∉ R [Rec5 §3, Sum w5] | Diagonalization. From a decider D build E(⟨M⟩): duplicate input to ⟨M,⟨M⟩⟩, ask D; if "halts" → loop forever, else halt. Run E on ⟨E⟩: both answers contradict E's own construction. |
| **D2** | DECIDABLE (provable-or-refutable claims) ∉ R — **⚠ idea-level in source** [Sum w6] | If T decided it, decide HALT: write the claim "M doesn't halt on w"; if T says unprovable-and-irrefutable answer "no"; if provable-or-refutable, search all proofs in parallel with simulating M — something must terminate the search. Either way HALT ∈ R, contradiction. |
| **D3** | BB(n) is not computable [Rec6 Prop 9] | If BB were computable, decide HALT_ε: t := BB(\|M\|) bounds the runtime of every halting \|M\|-state machine on ε; simulate M for t steps and answer. BB is total ⇒ this always halts — contradiction with HALT_ε ∉ R (**⚠ HALT_ε∉R for the binary alphabet was itself "left as exercise" in this rec; the general HALT_ε∉R is proven — see E4′ note**). |
| **D4** | Time Hierarchy Theorem: TIME(o(f)) ⊊ TIME(f·log f), f time-constructible [Lec10; stated Rec12/13] | Resource-bounded diagonalization. A_f = {⟨M,w⟩ : M accepts w within f(\|w\|) steps} is decidable in O(f log f) (universal TM + step counter). If it were decidable in o(f), build A_self = {⟨M⟩ : ⟨M,⟨M⟩⟩∈A_f}, complement it, and feed the complement's decider M′ to itself — the o(f) runtime guarantees the A_f membership question about M′ is answered by M′'s own behavior, closing the contradiction. |
| **D5** | Space Hierarchy Theorem: SPACE(o(f)) ⊊ SPACE(f), f space-constructible [Lec10] | Same proof with a space budget instead of a step counter. Tighter (no log factor) because a universal TM can simulate with only constant-factor space overhead. |

## E. Mapping reductions (computability)

| ID | Proves | Core idea |
|---|---|---|
| **E1** | L_even-length ≤m L_odd-length, two ways [Rec5 §2.1] | Reduction 1 "solve the problem": f(w)= a if \|w\| even else aa — legal only because the source is decidable. Reduction 2 "transfer the problem": f(w)=a·w — constant time, flips the parity without deciding anything. The contrast is the point. |
| **E2** | HALT ≤m NON-EMPTY_TM [Rec5 Prop 17] | f(⟨M,w⟩)=⟨T_{M,w}⟩ where T erases its input x, writes w, runs M on w, accepts if M halts. M halts on w ⇒ L(T)=Σ*≠∅; M loops ⇒ L(T)=∅. **Pitfall (in the file):** the case-split "output M_ALL if M halts else M_EMPTY" satisfies the iff but is *not computable*. |
| **E3** | Reduction theorem: A≤mB ∧ B∈{R,RE,coRE} ⇒ A∈ same — **⚠ statement + intuition in files; proof assigned as Ex5 Q5** [Rec5 Thm 18, Rec6 Thm 1] | Compose: decide/recognize A(x) by computing f(x) then running B's machine. "B is at least as hard as A." |
| **E4** | HALT ≤m A_TM and A_TM ≤m HALT [Sum w6] | HALT≤A_TM: M′ = M with rejecting also turned to accepting — M′ accepts w iff M halts on w. A_TM≤HALT: M′ = M with q_rej replaced by an infinite loop — M′ halts on w iff M accepts w. Same machine-surgery pattern, opposite directions. |
| **E5** | A_TM is RE-complete [Sum w6] | Membership: universal machine. Hardness: L∈RE has recognizer M_L; the reduction x ↦ ⟨M_L, x⟩ is trivially computable and x∈L ⟺ ⟨M_L,x⟩∈A_TM. |
| **E6** | HALT-bar is coRE-complete [Sum w6] | L∈coRE ⇒ L̄∈RE ⇒ L̄ ≤m HALT (via E4/E5 chain) ⇒ L ≤m HALT-bar with the **same** reduction function. |
| **E7** | Non-HALT is coRE-complete [Sum w6] | Membership: complement = HALT ∪ E (invalid inputs), both in RE, RE closed under ∪ (C4). Hardness: reduce HALT-bar; valid inputs map to themselves tagged appropriately, and *invalid* inputs (which belong to HALT-bar by definition) map to a fixed ⟨M₀,w₀⟩ known not to halt. |
| **E8** | ALL_TM ∉ RE ∪ coRE [Rec6 Prop 2] | Two reductions from opposite sides. HALT ≤m ALL_TM: M′ ignores x, runs M on w, accepts if it halts (L(M′)=Σ* or ∅). HALT-bar ≤m ALL_TM: M′ runs M on w **for \|x\| steps** and accepts iff it hasn't halted — non-halting gives L(M′)=Σ*, halting kills all long x. The \|x\|-step timer converts "never halts" into "accepts everything". |
| **E9** | REG_TM ∉ coRE (∉ RE was Ex6 Q2 — **⚠ that half not in sources**) [Rec6 Prop 3] | HALT ≤m REG_TM: M′ accepts aⁿbⁿ inputs immediately, and additionally accepts everything if M halts on w. Halting ⇒ L(M′)=Σ* (regular); looping ⇒ L(M′)={aⁿbⁿ} (not regular, by B8). |
| **E10** | RE-hard ⇒ ∉coRE; L RE-complete ⟺ L̄ coRE-complete; hardness spreads along ≤m [Rec6 Props 5–7] | All from the reduction theorem plus Ā≤mB̄ ⟺ A≤mB. E.g., if RE-hard L were in coRE, then HALT≤mL gives HALT∈coRE, i.e. HALT-bar∈RE, making HALT decidable by C5 — contradiction. |
| **E11** | USELESS is coRE-hard (with C9: coRE-complete) [Rec6 Prop 8] | A_TM-bar ≤m USELESS: H erases input, runs M on w; if M accepts, H enters a special state that *traverses every state of H* (via @@ tape-marker gadget) then accepts. M accepts w ⇒ no useless state; M doesn't ⇒ the traversal state is never reached. The gadget's computability discussion is part of the proof. |
| **E12** | NY-HALT is RE-hard and coRE-hard, hence ∉ RE ∪ coRE [Sum w6] | Tag-with-Y reduces HALT; tag-with-N reduces Non-HALT. Then E10 gives ∉coRE and ∉RE respectively. |

## F. Polynomial reductions, NP & Cook–Levin

| ID | Proves | Core idea |
|---|---|---|
| **F1** | ≤p composes (transitivity) [Sum w8] | Run M_f then M_g. The subtlety is the runtime: M_g's bound is in \|y\| where y=f(x), but \|y\| ≤ (time of M_f) = O(\|x\|^{k₁}), so total O(\|x\|^{k₁k₂}). Output length ≤ running time — the one-line fact everything rests on. |
| **F2** | Reduction theorem for P: A≤pB, B∈P ⇒ A∈P [Rec7 Thm 15] | Same composition, same output-length bookkeeping. Corollary shape used everywhere: NPC∩P≠∅ ⇒ P=NP; NPC⊄P witness ⇒ P≠NP [Sum w8]. |
| **F3** | P closed under ∪ and complement [Rec7 Props 10, 12] | ∪: run M₁ then M₂ (keep a spare copy of x; per-step copy overhead is poly). Complement: swap q_acc/q_rej — valid since deciders halt; runtime unchanged. The file's remark: this complement argument **fails** for NTMs — rejection of one run means nothing (CLIQUE-bar discussion). |
| **F4** | NP closed under ∪ [Rec7 Prop 11] | Nondeterministically choose which machine to simulate; runtime = max of the two, +O(1). |
| **F5** | CLIQUE ∈ NP and CLIQUE ∈ EXP [Rec7 Ex. 3, Prop 17; Sum w8] | NP: guess k vertices, check all C(k,2) pairs against E — poly. EXP: enumerate all C(\|V\|,k)=O(2^{k log\|V\|}) subsets — exponential is enough for membership in EXP, and k is part of the input so \|V\|^k is *not* poly. Verifier version: certificate = the clique [Sum w8]. |
| **F6** | 3-SAT ∈ NP [Sum w8] | NTM checks 3-CNF syntax, guesses an assignment, evaluates φ. |
| **F7** | 3-SAT ≤p CLIQUE [Sum w8] | Per clause, 7 vertices = its satisfying local assignments; edges between vertices of different clauses that don't contradict on shared variables; k=m. Satisfying assignment ⇒ pick the consistent vertex per layer = k-clique. k-clique ⇒ one vertex per layer (no intra-layer edges), consistent by construction ⇒ read off an assignment satisfying every clause. |
| **F8** | CLIQUE ≤p IS [Rec7 Prop 16] | Complement the graph: S is a clique in G ⟺ S independent in Ḡ. f(⟨G,k⟩)=⟨Ḡ,k⟩; O(\|V\|²) pair scan. |
| **F9** | IS ≤p VC [Rec8 Prop 2] | S independent ⟺ V∖S vertex cover. f(⟨G,k⟩)=⟨G,\|V\|−k⟩ (map k>\|V\| to a fixed non-instance). |
| **F10** | k-SAT ≤p 3-SAT (k>3) [Rec8 Prop 9] | Clause-shortening: (ℓ₁∨…∨ℓₖ) becomes (y∨ℓ₃∨…∨ℓₖ) ∧ [three clauses forcing y⟺(ℓ₁∨ℓ₂)]. Lemma: satisfying assignments extend/restrict across the rewrite. Repeat until all clauses have 3 literals; poly many rounds. (**⚠ the check that the 3 clauses encode y⟺(ℓ₁∨ℓ₂) is "left as exercise".**) |
| **F11** | 3-SAT ≤p D-ST-HAMPATH [Rec8 Prop 7] | Diamond gadget per variable: a horizontal chain traversable L→R (=True) or R→L (=False); a vertex per clause, reachable by a detour from a chain only in the direction matching the literal that satisfies it; separator vertices between detour pairs. Ham path ⇒ direction per chain = assignment; a first "cheating" jump strands a ⋆-vertex, so paths can't cheat. Assignment ⇒ route each chain by its truth value, detour once per clause via a chosen true literal. |
| **F12** | U-ST-HAMPATH is NP-complete [Rec9 Props 3–4] | ∈NP: witness = vertex sequence; check endpoints, distinctness, edges. Hardness: D-ST-HAMPATH ≤p U-ST-HAMPATH by splitting v into v_in–v_mid–v_out; a claimed undirected Ham path can't traverse "backwards" — the first backward edge strands some v_mid (proof by looking at the first violation). |
| **F13** | 3-COLORING is NP-complete [Rec9 Prop 5] | ∈NP: witness = the coloring; check every edge. Hardness from 3-SAT: base triangle T–F–B; per variable, v_x–v_x̄ edge, both joined to B (forces one True, one False); per clause an OR-gadget whose output is wired to B and F, so it must color True — impossible iff all three literals are False. |
| **F14** | 2-SAT ∈ P [Rec9 Prop 6] | Unit propagation with one backtrack per variable: set xᵢ=T, propagate forced literals ((ℓ₁∨ℓ₂) with ℓ₁ false forces ℓ₂); contradiction ⇒ retry xᵢ=F; contradiction again ⇒ reject. Correctness: after a clean round, the touched clauses are satisfied and the residual instance is independent, so failures are intrinsic. O(n) outer × O(n) inner × O(m·poly). |
| **F15** | SUBSET-SUM is NP-complete [Lec9 §9.2; HRec10] | ∈NP: witness = the subset; sum and compare. Hardness from 3-SAT: one number per literal — digit columns for variables (forces exactly one of xᵢ/x̄ᵢ chosen) and for clauses (contributions where the literal appears); slack numbers add ≤2 per clause column; target = 1…1‖3…3. Base large enough that no carries occur. |
| **F16** | SUBSET-SUM ≤p KNAPSACK (KNAPSACK NPC with its verifier) [Rec10] | Set wᵢ=vᵢ=sᵢ, W=V=t. Feasibility forces Σw ≤ t ≤ Σv with Σw=Σv, pinning the sum to exactly t. |
| **F17** | If L is NPC then AtLeastTwo(L) is NPC (2024-A exam) [Rec10 §2] | ∈NP: AtLeastTwo(L) = (Σ*·#)*·L·{#}·(Σ*·#)*·L·(#·Σ*)* — a finite concatenation of NP languages (regular pieces are in P⊆NP), and NP is closed under concatenation. Hardness: w ↦ w#w. |
| **F18** | NP = NP′ (verifier characterization) [Rec9 Prop 2 cites lecture; proof Sum w9] | ⊇: NTM guesses the certificate c (WLOG poly-length — the verifier can't read more) and runs V(w,c). ⊆: the certificate is the *transcript of nondeterministic choices*; a deterministic V replays the run, reading one letter of c per step to resolve each δ-choice. |
| **F19** | Cook–Levin: SAT (hence 3-SAT) is NP-complete [Sum w9; Lec9] | For any L∈NP with poly NTM M: accepting runs ⟺ legal fillings of a t×t configuration tableau (t=poly(n); WLOG unique accepting configuration — clean the tape, park the head). φ = φ_init ∧ φ_acc ∧ ⋀_{i,j} φ_legal over 2×3 windows; booleanize each cell with ⌈log(\|Γ\|+\|Q\|)⌉ bits; windows→CNF by negating the DNF of the *false* rows (De Morgan). The reduction machine prints φ̂_init, φ̂_acc, and t² shifted copies of one fixed window formula — poly time. |
| **F20** | coNP hardness mirrors; NP-hard ∩ NP∩coNP ⇒ NP=coNP [Rec10 §3] | L NP-hard ⟺ L̄ coNP-hard: the same reduction f works for complements. If NP-hard L∈NP∩coNP: any L′∈NP has L′≤pL∈coNP ⇒ L′∈coNP, so NP⊆coNP, and symmetrically equality. |
| **F21** | CNF-TAUTOLOGY ∈ P — **⚠ remark-level in source ("why?")** [Rec10 §3.1] | A CNF is a tautology iff *every clause* is one, and a clause is a tautology iff it contains x∨x̄ — a linear scan. TAUTOLOGY for general formulas is coNP-complete via φ ↦ ¬φ from CNF-CONTRADICTION = complement of CNF-SAT. |
| **F22** | Search-to-decision: a poly decider for SAT yields a poly *assignment-finder*; same for E3SAT [Lec12 §12.2] | Self-reduction: fix x₁=True by simplifying φ (drop satisfied clauses, delete falsified literals); if the decider says unsatisfiable, flip to False; iterate over variables. Invariant: the residual formula stays satisfiable. For E3SAT, re-apply the SAT≤pE3SAT normalizer after each fixing so the decider's promise is respected. |

## G. Space complexity, hierarchy theorems, NL, PSPACE

| ID | Proves | Core idea |
|---|---|---|
| **G1** | Savitch: NSPACE(f) ⊆ SPACE(f²), f space-constructible [Sum w11; Lec10] | Configuration graph G_{M,w} (#conf = \|Q\|·O(f)·\|Γ\|^{O(f)}); acceptance ⟺ path C₀→C_acc. Reach(u,v,t) recursion through a middle configuration with **space reuse**: both half-calls use the same workspace. Depth log(#conf)=O(f), frame size O(f) ⇒ O(f²). |
| **G2** | PSPACE = NPSPACE [Sum w11] | Savitch with f=nᵏ: the square of a polynomial is a polynomial. The file notes: a time analogue would prove P=NP — squaring doesn't hurt space because space is reusable. |
| **G3** | L ⊆ P; log-space machines have poly-length output [Sum w11] | #configurations of an O(log n)-space machine = \|Q\|·O(log n)·n·\|Γ\|^{O(log n)} = poly(n); a halting deterministic machine never repeats a configuration ⇒ runtime ≤ #conf. Output length ≤ #print-steps ≤ runtime. |
| **G4** | Log-space functions compose (f∘g computable in O(log n) space) [Sum w12; Lec12] | Never materialize g(x): simulate M_f, and whenever it needs input letter #i of g(x), re-run M_g from scratch counting print-steps until the i-th. State = two O(log n) counters + both work tapes. Time explodes, space doesn't — the tradeoff is the lesson. |
| **G5** | P ⊊ EXP; TIME(n²) ⊊ TIME(n³) [Lec10; Rec12] | Instantiate the Time Hierarchy Theorem (D4) with f(n)=2ⁿ (resp. f=n^{2.5}): every polynomial is o(2ⁿ), and the diagonal language lives in TIME(2ⁿ·n) ⊆ EXP. |
| **G6** | No k with ⋃_{i≤k}TIME(nⁱ) = P [Rec12 Claim 1.5] | If so, P ⊆ TIME(nᵏ) ⊊ TIME(n^{k+1}) ⊆ P by the hierarchy theorem — a strict inclusion of P in itself. |
| **G7** | Padding: SPACE(n)⊆P ⟺ PSPACE=P; corollary SPACE(nᵏ)≠P ∀k [Rec12 §3] | Pad L∈SPACE(nᵏ) to L′={w#1^{\|w\|ᵏ}}: relative to the padded length N, L′∈SPACE(N) ⊆(hyp) P; unpad in poly time to decide L. Corollary: SPACE(nᵏ)=P would give PSPACE=P=SPACE(nᵏ) ⊋ contradiction with the space hierarchy. |
| **G8** | PATH is NL-complete [Sum w12] | ∈NL: guess the path one vertex at a time, store only current vertex + step counter ≤\|V\|. Hard: for A∈NL with machine M, w ↦ ⟨G_{M,w}, C₀, C_acc⟩; configurations of a log-space machine take O(log n) bits, so a log-space reduction can enumerate all pairs and print the successor-edges. |
| **G9** | ≤L composes; NL-hardness spreads (B NL-hard ∧ B≤LC ⇒ C NL-hard) [Sum w12] | Directly from G4 (composition of log-space computable functions). |
| **G10** | NL=coNL ⟺ PATH-bar ∈ NL [Sum w13] | ⇒ trivial. ⇐: A∈coNL ⇒ Ā≤L PATH (G8) ⇒ A ≤L PATH-bar (same f) ⇒ A∈NL; then symmetry closes NL=coNL. Also shown: flipping q_acc/q_rej of an NTM does **not** complement its language (PATH counterexample). |
| **G11** | Immerman–Szelepcsényi: PATH-bar ∈ NL (hence NL=coNL) [Sum w13; Lec12] | Inductive counting. Cₖ = #vertices reachable from s in ≤k steps; C₀=1. Compute C_{k+1} from Cₖ certifiably: for each target v, re-enumerate all u, *guess* a ≤k-step path to each claimed-reachable u (count successes in Dₖ); only if Dₖ=Cₖ was every reachable u seen, so "v unreachable in k+1" is certain. Run twice: C for G, C′ for G∖{t}; accept iff Cₙ=C′ₙ. All counters O(log n). |
| **G12** | NPSPACE = coNPSPACE [Sum w13] | Via G2: NPSPACE=PSPACE is deterministic, hence closed under complement. The file stresses this route **fails** for NL (Savitch would land in SPACE(log²n), outside NL) — which is why G11 needs a new idea. |
| **G13** | STRONGLY-CONNECTED is NL-complete [Rec12 §6; Lec12] | ∈NL: for every ordered pair (u,v) guess a path (or, in the rec's version, use the PATH-bar machine + Immerman). Hard: PATH ≤L STRONGLY-CONNECTED — add edges (v,s) and (t,v) for all v; new edges only enter s / leave t, so s⇝t paths are unaffected, and any s⇝t path makes everything mutually reachable. |
| **G14** | E_NFA (NFA emptiness) is NL-complete [Rec12 §7] | L(A)≠∅ ⟺ path from Q₀ to F in the state graph: guess a state sequence of length ≤\|Q\| (E_NFA-bar ∈ NL), apply Immerman. Hard: PATH ≤L E_NFA-bar-style — turn G into a one-letter NFA (Q=V, Q₀={s}, F={t}, δ(u,a)={v:(u,v)∈E}); L(A)≠∅ ⟺ s⇝t; compose with complementation via NL=coNL. |
| **G15** | 10-CSS (exactly 10 SCCs) is NL-complete; 2-Con, AL2SCC ∈ NL [Rec12 §8; Sum w13; Lec12] | ∈NL: count SCCs by counting "first vertices" — v is first in its SCC iff no u<v with u⇝v and v⇝u; both reachability and its negation are NL-checkable (Immerman); accept iff counter =10. Hard: STRONGLY-CONNECTED ≤L 10-CSS by adding 9 isolated vertices (1+9=10 vs ≥2+9=11). |
| **G16** | TQBF ∈ PSPACE [HRec11 §11.3] | Recursive evaluation: for the outermost quantifier try x=True and x=False, recurse on ψ, combine by ∧ (for ∀) or ∨ (for ∃); constant-size result markers on the tape. Depth n, O(n) tape per level ⇒ O(n²) space. |
| **G17** | TQBF is PSPACE-hard (with G16: PSPACE-complete) [HRec11 §11.4–11.5] | Encode configurations of an s(n)-space machine by boolean variables (x_{i,α}, y_i, z_q) with an O(s²) validity formula and an O(s²) one-step formula ψ. Two failed attempts are part of the proof: unrolling all t=2^{s} steps (exponential formula), and the Savitch-style split φ_k = ∃c_mid(φ_{k/2}∧φ_{k/2}) (formula doubles). The fix: **∃c_mid ∀(c₃,c₄)∈{(c₁,c_mid),(c_mid,c₂)}: φ_{k/2}(c₃,c₄)** — the ∀ shares one copy of the sub-formula, giving size poly(s·log t)=poly(n). |

## H. Randomized classes

| ID | Proves | Core idea |
|---|---|---|
| **H1** | P ⊆ ZPP, P ⊆ RP, P ⊆ BPP [Sum w14] | A deterministic poly decider ignores its coin tape: expected time = worst-case poly (ZPP); error 0 beats every threshold (RP/BPP). |
| **H2** | RP ⊆ NP [Sum w14] | An RP machine *is* a verifier: certificates = coin strings; w∈L ⇒ ≥half the coin strings accept (∃c), w∉L ⇒ none do (∀c reject). |
| **H3** | RP(p) = RP for any constant p (one-sided amplification) [Sum w14] | Run M twice, reject only if both reject: no-instances still never accepted; yes-instances missed with prob ≤(1/2)²=1/4. Iterate for any constant. |
| **H4** | BPP(ε) = BPP (two-sided amplification) [Lec13 §13.1] | Majority of t independent runs, t odd; Chernoff bounds the probability that fewer than half are correct when each is correct w.p. ≥2/3. Constant t gives any constant ε; poly t gives exponentially small ε; runtime stays poly. |
| **H5** | BPP = coBPP; RP, coRP ⊆ BPP [Sum w14] | Swap q_acc/q_rej (two-sided error is symmetric). RP=RP(1/3)⊆BPP directly; coRP by taking complements through BPP=coBPP. |
| **H6** | BPP ⊆ EXP [Sum w14] | A poly-time machine reads ≤poly(n) coins ⇒ enumerate all 2^{poly} coin strings, simulate each, answer by majority — exponential but exact. |
| **H7** | ZPP = RP ∩ coRP [Sum w14; Lec13 Prop 13.1.5] | ⊆: truncate the ZPP machine at c·E[runtime]; Markov (P[T>cE[T]]≤1/c) bounds the forced-stop probability; answer q_rej on force-stop (RP direction) or q_acc (coRP direction). ⊇: alternate the RP machine (its accept is certain) and the coRP machine (its reject is certain) until one speaks; each round terminates w.p. ≥1/2, so E[#rounds]≤2 (geometric series) — zero error, expected poly time. |

---

# Part 2 — Full Detail

## A. Induction on words & automata constructions

### A1 — Template proof that a DFA decides its language [Rec1 §4]
**Statement.** For the 3-state DFA A (q₀ start; a→q₁ which loops on a,b and accepts; b→q₂ which loops), L(A) = L := {w : w begins with a}.

**Proof.** Claim (state characterization): the words ending their run in each state are exactly — q₀: only ε; q₁: words starting with a; q₂: nonempty words not starting with a.

*The claim suffices:* w∈L ⟺ w starts with a ⟺ run on w ends in q₁ ⟺ A accepts w (q₁ is the only accepting state) ⟺ w∈L(A).

*Proof of claim by induction on |w|.*
- Base |w|=0: the run on ε ends in q₀, and indeed ε matches q₀'s description.
- Step: assume for length n; take w=uσ with |u|=n. Case on the state reached on u (using the IH):
  - u ended in q₀ ⇒ u=ε. If σ=a: w=a starts with a and δ(q₀,a)=q₁ ✓. If σ=b: w=b is nonempty, doesn't start with a, δ(q₀,b)=q₂ ✓.
  - u ended in q₁ ⇒ u starts with a ⇒ w=uσ starts with a, and δ(q₁,σ)=q₁ for both σ ✓.
  - u ended in q₂ ⇒ u nonempty, not starting with a ⇒ so is w, and δ(q₂,σ)=q₂ ✓. ∎

**Pitfalls.** The characterization must cover *all* words (each word must belong to exactly one state's description). The induction step must handle *every* (state, letter) pair — skipping a transition is the standard lost point. The recitation's warning: you may later argue informally, but must be able to produce this "at gunpoint."

### A2 — δ*(q, w·w′) = δ*(δ*(q,w), w′) [Rec1 Prop 1]
**Statement.** For any DFA, q∈Q, w,w′∈Σ*.

**Proof.** Induction on |w′|.
- Base w′=ε: δ*(δ*(q,w),ε) = δ*(q,w) = δ*(q,w·ε) — the middle equality is the ε-case of δ*'s definition, the right one is w·ε=w.
- Step: assume for length n; let w′=w″σ, |w″|=n. Then
  δ*(q, w·w′) = δ*(q, w·w″·σ) = δ(δ*(q,w·w″), σ)  [def. of δ* on a nonempty word]
  = δ(δ*(δ*(q,w), w″), σ)  [IH on w″]
  = δ*(δ*(q,w), w″σ) = δ*(δ*(q,w), w′). ∎

**Pitfall.** Induct on the *second* word: δ* peels letters from the right, so the recursion aligns with w′.

### A3 — REG closed under union and intersection (product automaton) [Sum w2]
**Statement.** L₁,L₂∈REG ⇒ L₁∪L₂, L₁∩L₂ ∈ REG.

**Proof.** WLOG both are over the same Σ (else pass to Σ₁∪Σ₂, adding a rejecting sink state for foreign letters — the file makes this explicit). Let A=⟨Q,Σ,q₀,F,δ⟩ decide L₁ and B=⟨P,Σ,p₀,G,η⟩ decide L₂. Define C = ⟨Q×P, Σ, (q₀,p₀), F_C, ψ⟩ with ψ((q,p),α) = (δ(q,α), η(p,α)) and F_C = F×P ∪ Q×G for union (F×G for intersection).

Key claim: ψ*((q₀,p₀),w) = (δ*(q₀,w), η*(p₀,w)) for all w. Induction on |w|:
- Base: ψ*((q₀,p₀),ε) = (q₀,p₀) = (δ*(q₀,ε), η*(p₀,ε)).
- Step w=w′α: ψ*((q₀,p₀),w′α) = ψ(ψ*((q₀,p₀),w′),α) = ψ((δ*(q₀,w′),η*(p₀,w′)),α)  [IH]
  = (δ(δ*(q₀,w′),α), η(η*(p₀,w′),α)) = (δ*(q₀,w), η*(p₀,w)).

Then w∈L(C) ⟺ (δ*(q₀,w),η*(p₀,w))∈F_C ⟺ δ*(q₀,w)∈F or/and η*(p₀,w)∈G ⟺ w∈L₁∪L₂ (resp. ∩). ∎

**Pitfall.** Union accepting set is F×P ∪ Q×G, **not** F×G — mixing these up flips ∪ and ∩.

### A4 — NREG closed under union [Rec2 §3.1; Sum w2]
**Statement.** L₁,L₂∈NREG ⇒ L₁∪L₂∈NREG.

**Proof.** Let A=⟨Q,Σ,δ,Q₀,F⟩, B=⟨P,Σ,η,P₀,G⟩ recognize L₁,L₂ with Q∩P=∅ (rename if needed). Define C=⟨Q∪P, Σ, α, Q₀∪P₀, F∪G⟩ where α(q,σ)=δ(q,σ) for q∈Q and η(q,σ) for q∈P.

Lemma: every run of C lies entirely in Q or entirely in P. Induction along the run: if rᵢ∈Q then r_{i+1}∈α(rᵢ,w_{i+1})=δ(rᵢ,w_{i+1})⊆Q; so r₀∈Q₀ forces the whole run into Q (symmetrically for P).

⊆: let w∈L₁∪L₂, WLOG w∈L₁ with accepting A-run r₀…rₙ. The same sequence is a C-run (r₀∈Q₀⊆Q₀∪P₀; each transition satisfies α=δ on Q) and rₙ∈F⊆F∪G. So w∈L(C).

⊇: let w∈L(C) with accepting run r₀…rₙ, say rₙ∈F. By the lemma the run is inside Q, hence r₀∈Q₀ and every step uses δ — it is an accepting A-run, so w∈L₁. ∎

**Pitfall.** The disjointness assumption ("WLOG rename states") must be stated; without it α is ill-defined.

### A5 — NREG closed under concatenation ⚠ [Rec2 §3.2; Sum w3]
**Status: construction given; correctness proof explicitly "left as an exercise" in the source.**

**Construction.** C over Σ with states Q∪P, initial states Q₀ (of A), accepting states G (of B); transitions = all of δ, all of η, plus an ε-transition from every state of F (A's accepting) to every state of P₀ (B's initial); A's accepting states and B's initial states lose their special roles. Intuition recorded in the file: nondeterminism guesses where to split w=uv, u∈L₁, v∈L₂. The ε-transitions are then compiled away by the ε-elimination recipe (E(q)-closure — see the Rec2 §4 formalization). ∎(construction)

### A6 — The two δ* definitions for NFAs agree [Rec2 Prop 1]
**Statement.** For an NFA, define δ*(S,w) (i) as the set of endpoints of runs on w starting in S, and (ii) recursively: δ*(S,ε)=S; δ*(S,w′σ)=⋃_{q∈δ*(S,w′)} δ(q,σ). These are the same function.

**Proof.** Show (i) satisfies (ii)'s base and recursion; since the recursion determines a unique function, they agree.
- Base: a run on ε starts at some r₀∈S and stops immediately, so the reachable set is exactly S.
- Recursive case, two containments for δ*(S,w′σ):
  (⊆) If rₙ is reachable via run r₀…rₙ on w′σ from S, then r₀…r_{n−1} is a run on w′ from S, so r_{n−1}∈δ*(S,w′) and rₙ∈δ(r_{n−1},σ) ⊆ ⋃_{q∈δ*(S,w′)}δ(q,σ).
  (⊇) If rₙ∈δ(r_{n−1},σ) for some r_{n−1}∈δ*(S,w′), extend a witnessing run on w′ by rₙ to get a run on w′σ ending at rₙ. ∎

### A7 — NREG = REG (subset construction) [Rec3 §2; Sum w3]
**Statement.** For every NFA A=⟨Q,Σ,δ,Q₀,F⟩ there is an equivalent DFA; hence NREG=REG.

**Proof.** REG⊆NREG: a DFA is an NFA (this direction was homework, Ex2 Q1 — flagged). For NREG⊆REG define the DFA B=⟨2^Q, Σ, α, Q₀, G⟩ with α(S,σ)=⋃_{q∈S}δ(q,σ) and G={S : S∩F≠∅}.

Claim: α*(S,w)=δ*(S,w) for all S⊆Q, w∈Σ*. Induction on |w|:
- Base: α*(S,ε)=S=δ*(S,ε).
- Step: α*(S,wσ) = α(α*(S,w),σ) [def α*] = α(δ*(S,w),σ) [IH] = ⋃_{q∈δ*(S,w)}δ(q,σ) [def α] = δ*(S,wσ) [def δ*, A6].

Then w∈L(A) ⟺ δ*(Q₀,w)∩F≠∅ ⟺ α*(Q₀,w)∈G ⟺ w∈L(B). ∎

**Notes.** The 2^Q blowup is *necessary*: L_k needs 2^k DFA states (B4) but has a (k+1)-state NFA. Unreachable subset-states may be omitted when drawing.

### A8 — L_EVEN regular [Rec1 §6]
**Statement.** L∈REG ⇒ L_EVEN = {w∈L : |w| even} ∈ REG.

**Proof (as given — construction + brief argument).** From DFA A=⟨Q,Σ,δ,q₀,F⟩ build A′=⟨Q×{0,1}, Σ, δ′, (q₀,0), F′⟩, δ′((q,p),a)=(δ(q,a),1−p), F′={(q,0):q∈F}. A′ tracks A's state and the input length's parity simultaneously; it accepts exactly when A would accept *and* the parity bit is 0. Since A′ is a DFA and L(A′)=L_EVEN, the language is regular. (The file gives this as a "proof sketch" — the state-characterization induction is the same pattern as A3's invariant.) ∎

### A9 — L_mix ∈ NREG [Rec2 §6 = Rec3 §1]
**Statement.** For regular L, L_mix := {w : ∃z∈Σ^{|w|} with z₁w₁⋯z_{|w|}w_{|w|} ∈ L} ∈ NREG.

**Proof.** Let DFA A=⟨Q,Σ,δ,q₀,F⟩ decide L. Define NFA B=⟨Q,Σ,η,{q₀},F⟩ with η(q,σ) = {δ(δ(q,α),σ) : α∈Σ} — reading σ=wᵢ, B guesses α=zᵢ and jumps two A-steps at once.

(⊆) w=w₁…wₙ∈L_mix: take z with z₁w₁⋯zₙwₙ∈L and A's accepting run r₀,s₁,r₁,s₂,…,sₙ,rₙ on it. Then r₀,r₁,…,rₙ is a B-run on w: r₀=q₀, rₙ∈F, and r_{i+1}=δ(s_{i+1},w_{i+1})=δ(δ(rᵢ,z_{i+1}),w_{i+1})∈η(rᵢ,w_{i+1}) (choose α=z_{i+1}). So w∈L(B).

(⊇) w∈L(B) with accepting B-run r₀…rₙ: each step supplies a letter z_{i+1} with r_{i+1}=δ(δ(rᵢ,z_{i+1}),w_{i+1}); set s_{i+1}=δ(rᵢ,z_{i+1}). Then r₀,s₁,r₁,…,sₙ,rₙ is an accepting A-run on z₁w₁⋯zₙwₙ, witnessing w∈L_mix. ∎

**Pitfall.** The two directions build *different* objects (contract an A-run vs. expand a B-run); writing only one direction is the common loss.

## B. Myhill–Nerode, separating suffixes & pigeonhole

### B1 — Same state ⇒ no separating suffix [Rec3 Prop 4]
**Statement.** If DFA A recognizes L and δ*(q₀,x)=δ*(q₀,y), then no z separates x,y w.r.t. L.

**Proof.** For any z: δ*(q₀,xz) = δ*(δ*(q₀,x),z) = δ*(δ*(q₀,y),z) = δ*(q₀,yz), using A2 twice. The runs on xz and yz end in the same state; if it is accepting both are in L, otherwise neither. ∎

**Use (lower bounds).** Contrapositive: pairwise-separated words w₁,…,w_k must reach k distinct states, so every DFA for L has ≥k states. Worked instances in the file: {w contains aa} needs ≥3 states (words a,b,aa with suffixes a,ε,ε); {no repeated adjacent letter} needs 4 (ε,a,b,aa); {|w|≥3} has classes |w|=0,1,2,≥3 separated by z=a^{3−|y|}.

### B2 — ∼_L is an equivalence relation ⚠ [Rec3 Def 5]
**Status: only transitivity is proven; reflexivity and symmetry "left as an exercise".**

**Transitivity (as in source).** If x∼_L y and y∼_L w then for every z: xz∈L ⟺ yz∈L ⟺ wz∈L, hence xz∈L ⟺ wz∈L, i.e. x∼_L w. ∎

### B3 — Myhill–Nerode theorem [Sum w3; Rec3 Prop 6]
**Statement.** If ∼_L has k<∞ equivalence classes then L∈REG with a k-state DFA; conversely infinitely many classes ⇒ L∉REG, and #classes lower-bounds every DFA (B1). Classes correspond to states of the minimal DFA.

**Proof (as written in the summary).** Let Q = {[w]_L}. Define A=⟨Σ,Q,[ε]_L,F,δ⟩ with F={[w]_L : w∈L} and δ([w]_L,α)=[wα]_L.

Well-definedness of δ (the written core): if [w]=[y] then w∼_L y, i.e. ∀z (wz∈L ⟺ yz∈L). Specializing to suffixes z=αz′: ∀z′ (wαz′∈L ⟺ yαz′∈L), i.e. wα∼_L yα, i.e. [wα]=[yα]. (Well-definedness of F is the observation that x∼_L y with x∈L forces y∈L — take z=ε.)

Intended invariant δ*([ε]_L,w)=[w]_L then gives L(A)=L; **⚠ this final claim's proof was assigned as Ex3 Q5 and is not written in the sources.** The lower-bound half is B1. ∎(as far as the sources go)

**Pitfall (exam).** A DFA may have *more* reachable states than classes (Ex3 Q3b asks to build one) — MN counts the *minimum*.

### B4 — DFA lower bound 2^k for L_k [Rec2 §2.4; Sum w2]
**Statement.** Every DFA deciding L_k = {w : the kth letter from the end is a} has ≥2^k states.

**Proof.** Suppose A has <2^k states. There are 2^k words of length k, so by pigeonhole two distinct u≠v of length k reach the same state. Let i be the first index where they differ, WLOG uᵢ=a, vᵢ=b. Append the same suffix — both extended words still reach a common state, hence are accepted or rejected together. Choose the suffix a^{i−1}: in u·a^{i−1} the kth-from-the-end letter is uᵢ=a (∈L_k) while in v·a^{i−1} it is vᵢ=b (∉L_k). They must be distinguished — contradiction. ∎

**Pitfall.** The suffix length is calibrated so position i lands exactly k from the end; state the arithmetic (|u|−i letters after position i, plus i−1 appended = k−... — check it explicitly on the exam).

### B5 — {w : #a(w) ≥ #b(w)} ∉ REG [Rec3 Prop 7]
**Proof.** Suppose DFA A with k states recognizes L. Among ε,a,a²,…,a^k (k+1 words) two reach the same state: aⁱ,aʲ with i>j. But z=bⁱ separates them — aⁱbⁱ∈L (equal counts), aʲbⁱ∉L (j<i) — contradicting B1. ∎

### B6 — {1^{n²}} ∉ REG [Rec3 Prop 8]
**Proof.** Show all 1^{i²} lie in distinct MN classes. For 0≤i<j take z=1^{2i+1}: |1^{i²}z| = i²+2i+1 = (i+1)² so 1^{i²}z∈L; |1^{j²}z| = j²+2i+1 satisfies j² < j²+2i+1 < j²+2j+1 = (j+1)², strictly between consecutive squares, so 1^{j²}z∉L. Infinitely many classes ⇒ not regular (B3). ∎

### B7 — {1^p : p prime} ∉ REG ⚠ sketch [Rec3 Prop 9]
**Sketch (as in source).** (1) Every infinite unary regular language contains an infinite arithmetic progression: with finitely many states, a long word's run repeats a state, giving a loop of some length k; then w∈L ⇒ w1^k, w1^{2k}, … ∈ L. (2) The primes contain no infinite arithmetic progression of this pumped form because they have unbounded gaps: for every n, the n−1 consecutive numbers n!+2, n!+3, …, n!+n are composite (n!+j divisible by j). The file presents this as a sketch; the bridging details (choosing the progression inside a gap) are not spelled out. ∎(sketch)

### B8 — {aⁿbⁿ} ∉ REG [Sum w3]
**Proof.** For n≠m: aⁿ ≁_L a^m, separated by z=bⁿ (aⁿbⁿ∈L, a^m bⁿ∉L). So {[aⁿ]} are infinitely many distinct classes; by B3, L∉REG. ∎

## C. Simulation & TM construction

### C1 — Bounded acceptance is decidable [Rec5 Prop 6]
**Statement.** L = {⟨M,w,k⟩ : M accepts w within ≤k steps} ∈ R.

**Proof.** Build T: on ⟨M,w,k⟩ simulate M on w for at most k steps (universal machine with a side step-counter). Accept iff the simulation reached q_acc within the budget; otherwise reject. Correctness is by construction (accept ⟺ M accepts within k). Totality: the simulation is capped at k steps, so T halts on every input. ∎

### C2 — NON-EMPTY_TM ∈ RE [Rec5 Prop 7]
**Statement.** {⟨M⟩ : L(M)≠∅} ∈ RE.

**Proof.** T on ⟨M⟩: for n=0,1,2,…: for every w with |w|≤n, run M on w for n steps; accept if any simulation accepts.

If T accepts, some w is accepted by M, so L(M)≠∅. Conversely if L(M)≠∅, fix an accepted w with accepting run of length k; at iteration i := max(|w|,k), the word w is included (|w|≤i) and simulated long enough (i≥k), so T accepts. If L(M)=∅, T runs forever — permitted for a recognizer. ∎

**Pitfall.** Neither "run M on each word to completion" (may hang on the first word) nor "run on all words" (infinitely many) works; the *triangular* enumeration is the entire content.

### C3 — R closed under complement, union, intersection [Rec5 Props 8–10]
**Complement.** M decides L ⇒ swap q_acc↔q_rej to get T. T halts everywhere (only final states changed) and T accepts w ⟺ M rejects w ⟺ w∉L. 

**Union.** Run M₁ on w; if it accepts, accept; else run M₂ on w; accept iff it accepts; else reject. Both halt, so the composite halts. Tape hygiene (from the file): keep a marked spare copy of w far on the tape, shifting it if M₁'s computation encroaches; after M₁, erase M₁'s workspace and restore w for M₂.

**Intersection.** Same sequencing, accept iff both accept; or apply De Morgan L₁∩L₂ = complement(complement L₁ ∪ complement L₂). ∎

### C4 — RE closed under intersection and union [Rec5 Props 11–12]
**Intersection.** Sequential composition as in C3 works verbatim: if some Mᵢ hangs, w∉Lᵢ, and hanging (=not accepting) is correct for w∉L₁∩L₂.

**Union.** Sequential fails: M₁ may hang while M₂ would accept. Dovetail: for n=0,1,2,…, run M₁ on w for n steps, then M₂ on w for n steps; accept the moment either accepts.
- w∈L₁∪L₂, WLOG accepted by M₁ in k steps ⇒ at iteration k the simulation of M₁ reaches acceptance ⇒ T accepts.
- T accepts ⇒ one of the machines accepts w ⇒ w∈L₁∪L₂. ∎

**Remark recorded in the file:** RE is *not* closed under complement (follows once HALT∈RE∖R is known, via C5).

### C5 — R = RE ∩ coRE [Sum w6]
**Proof.** (⊆) A decider both recognizes L and, with flipped finals, recognizes L̄. (⊇) Let M_L recognize L and M_L̄ recognize L̄. Build M_D: for i=0,1,2,… run M_L on x for i steps and M_L̄ on x for i steps. If M_L accepts — accept; if M_L̄ accepts — reject. Every x lies in L or L̄, so one recognizer accepts within some finite number of steps; hence M_D halts on every input and answers correctly. ∎

**Pitfall.** Must interleave (or alternate with growing budgets); running M_L to completion first may hang.

### C6 — HALT ∈ RE [Sum w5]
**Proof.** Take a universal TM U (C7) and declare *all* of its final states accepting. On ⟨M,w⟩: if M halts on w, U halts (in some final state) and thus accepts; if M doesn't halt, U doesn't halt, so ⟨M,w⟩ is not accepted. Hence this machine recognizes HALT. ∎

### C7 — A universal TM exists ⚠ proof-idea level [Sum w5]
**Statement.** There is a TM U with: M doesn't halt on w ⇒ U doesn't halt on ⟨M,w⟩; M halts ⇒ U halts with U(⟨M,w⟩)=⟨M(w)⟩; if M's finals are encoded 0/1 (rej/acc), U ends in the matching state.

**Idea (as written).** U's tape holds ⟨M⟩⟨C⟩ for the current configuration C, initially ⟨M⟩⟨q₀w⟩. Loop: locate in ⟨C⟩ the encoded state and scanned symbol; scan ⟨M⟩ for the matching transition rule ##(q)_b#(α)_b#(q′)_b#(β)_b#(D)_b##; rewrite ⟨C⟩ to ⟨C⁺⟩ (shifting as needed). On reaching a final configuration: erase ⟨M⟩, erase the state encoding, and finish. The file notes each choice can be made so simulation overhead is polynomial per step, and O(t log t) total is achievable with optimizations. ∎(idea)

### C8 — Multi-tape to single-tape simulation [Rec8 §4]
**Statement.** Every 2-tape TM M has an equivalent 1-tape TM M′; t steps simulate in O(t²). Generalizes to k tapes: O(f(n)) time ⇒ O(f(n)²).

**Proof.** Let Γ′ = (Γ×Γ×{0,1}×{0,1}) ∪ Σ ∪ {⌴}: cell i stores (tape-1 symbol, tape-2 symbol, head-1 flag, head-2 flag). Initialization: rewrite input σ…σ to (σ,⌴,0,0)…, then set flags (·,·,1,1) on the first cell. One simulated step: scan left-to-right to find the h₁=1 cell, record its Γ-component in the state; continue to the h₂=1 cell, record; now (q,γ₁,γ₂) determines δ's action; scan again updating symbol and flag for head 1, then for head 2. Q′ and Γ′ are finite (constant-size bookkeeping). After t steps the heads are ≤t cells apart, so each simulated step costs O(t) scans ⇒ O(t²) total. For k tapes use Γ′=(Γ^k×{0,1}^k)∪Σ∪{⌴}: O(k·f·f)=O(f²). Corollary: multi-tape poly time ⇒ single-tape poly time. ∎

### C9 — USELESS ∈ coRE [Rec6 Prop 8, membership half]
**Statement.** USELESS = {⟨M⟩ : some non-final state of M is never reached on any input} ∈ coRE.

**Proof.** USELESS-bar = USEFUL ∪ E (E = invalid encodings, decidable). Show USEFUL ∈ RE: T on ⟨M⟩ dovetails as in C2 — for n=0,1,2,… simulate M for n steps on every input of length ≤n — while maintaining the set of states visited across all simulations; accept when every state has been visited.
- ⟨M⟩∉USEFUL: some state q is never reached in any run, so the visited-set never completes and T never accepts.
- ⟨M⟩∈USEFUL: every state q has a witness (w_q, step count n_q); with finitely many states, let k = max over q of max(|w_q|,n_q); by iteration k all states have been observed and T accepts.
Then USELESS-bar = USEFUL ∪ E ∈ RE (C4 union closure; E∈R⊆RE), so USELESS ∈ coRE. ∎

## D. Counting & diagonalization

### D0 — Uncountably many languages, countably many programs [Sum w1]
**Argument (as written).** For finite Σ: #words of length k = |Σ|^k < ∞, so |Σ*| = ℵ₀; the set of languages is the power set, of size 2^{ℵ₀} > ℵ₀. There are ℵ₀ Python programs/TMs (each is a finite string). Decision problems over Σ biject with languages, so there are 2^{ℵ₀} problems but only ℵ₀ programs — some decision problem is solved by no program. (The explicit diagonal construction wₙ∈L ⟺ wₙ∉Lₙ appears only as the hint of Ex1 Q7 — **⚠ not worked in the sources**.) ∎

### D1 — HALT ∉ R [Rec5 §3; Sum w5]
**Statement.** No TM decides HALT = {⟨M,w⟩ : M halts on w}.

**Proof.** Suppose decider D exists. Build E, on input ⟨M⟩:
1. Duplicate the input to ⟨M,⟨M⟩⟩.
2. Run D on it (as a procedure — D always halts).
3. If D answers "yes" (M halts on ⟨M⟩): enter a deliberate infinite loop. If "no": halt.

Run E on ⟨E⟩ and ask whether it halts.
- If E halts on ⟨E⟩: then ⟨E,⟨E⟩⟩∈HALT, D answers "yes", so E enters the infinite loop — E does *not* halt. Contradiction.
- If E doesn't halt on ⟨E⟩: D answers "no", so by construction E halts. Contradiction.
Both cases are impossible, so D cannot exist. ∎

**Corollary in the same files [Sum w5]:** HALT_ε ∉ R — a machine Red maps ⟨M,w⟩ to ⟨M′⟩ where M′ (on empty input) writes w and runs M; a decider for HALT_ε would then decide HALT. (This is a reduction avant la lettre; the formal ≤m framework is E-group.)

**Pitfalls.** E must *flip* D's answer through behavior (loop vs halt), not merely report it; and E is run on its *own* encoding — both cases must be argued separately and both must yield contradictions.

### D2 — DECIDABLE ∉ R ⚠ idea-level [Sum w6]
**Statement (Turing, as recorded).** DECIDABLE = {claims that can be proved or refuted} is not decidable.

**Argument (as written).** Suppose T decides it. Build S: given ⟨M,w⟩, write the claim φ = "M does not halt on w" and run T on φ.
- If T says "no" (φ neither provable nor refutable): then in particular M's halting can't be settled by exhibiting a halting run — the file concludes S answers "no" (M doesn't halt; a halting run would be a proof).
- If T says "yes": S searches all proofs in increasing length for a proof or refutation of φ; by assumption one exists, so the search terminates, and its outcome settles whether M halts on w.
Either way HALT is decided — contradiction with D1. **The source presents this compressed (two bullet points); the proof-search formalization is not developed.** ∎(idea)

### D3 — Busy Beaver is incomputable [Rec6 Prop 9]
**Statement.** BB(n) = max steps before halting, over all n-state binary-alphabet TMs that halt on ε, is not a computable function.

**Proof.** Suppose a TM computes BB. Decide HALT_ε as follows: given ⟨M⟩ with n states, compute t := BB(n); simulate M on ε for t steps; accept iff it halted. If M halts on ε at all, it halts within BB(n) steps (BB is the max over halting n-state machines — exceeding it would contradict maximality); if M doesn't halt, the capped simulation times out and we reject. BB total ⇒ this machine always halts ⇒ HALT_ε ∈ R, contradiction. (**⚠ the file defers "HALT_ε over the binary alphabet ∉ R" to an exercise; the general-alphabet version is D1's corollary, and Ex6 Q6 bridges alphabets — statement only.**) Historical note in file: BB(5)=47,176,870. ∎

### D4 — Time Hierarchy Theorem [Lec10 §10.1; statements Rec12/13]
**Statement.** For every time-constructible f (f=Ω(n log n), 1ⁿ↦binary f(n) computable in O(f(n))): Time(o(f(n))) ⊊ Time(f(n)·log f(n)).

**Proof.** Define A_f = {⟨M,w⟩ : M accepts w and its run on w takes ≤ f(|w|) steps}.

*Upper bound (Lemma 10.1.1):* A_f ∈ Time(f·log f). Decider: compute t=f(|w|) (time-constructibility, O(f)); simulate M on w for t steps with a universal machine whose step-counting implementation simulates f(n) steps in O(f log f); accept iff M accepted within the budget. Correctness: accepted-within-budget is precisely A_f's condition; over-budget or rejecting runs are correctly rejected because the counter cuts them off.

*Lower bound (Lemma 10.1.2):* A_f ∉ Time(o(f)). Suppose M_f decides A_f in o(f). Define A_self = {⟨M⟩ : ⟨M,⟨M⟩⟩ ∈ A_f} and its complement A̅_self; both would be decidable in o(f) time (compose with input duplication / flip finals). Let M′ decide A̅_self within o(f). Ask: what does M′(⟨M′⟩) return?
- If M′ accepts ⟨M′⟩: then ⟨M′⟩∈A̅_self, i.e. ⟨M′⟩∉A_self, i.e. ⟨M′,⟨M′⟩⟩∉A_f. That means M′ on ⟨M′⟩ either rejects (false — it accepts) or overruns f(|⟨M′⟩|) steps (false — M′ runs in o(f), which is <f for large inputs; the file notes the padding/large-input caveat implicitly via asymptotics). Contradiction.
- If M′ rejects ⟨M′⟩: then ⟨M′⟩∉A̅_self, so ⟨M′,⟨M′⟩⟩∈A_f, meaning M′ *accepts* ⟨M′⟩ (within budget) — contradiction.
Combining the two lemmas separates the classes. ∎

**Pitfall (explicit in file).** The o(f)-runtime hypothesis is what rules out the "rejected because over-budget" escape hatch in the first case — cite it.

### D5 — Space Hierarchy Theorem [Lec10 §10.1.2]
**Statement.** For space-constructible f: Space(o(f(n))) ⊊ Space(f(n)).

**Proof (as written: same as D4 with two changes).** (1) A_f is redefined with "…and the run uses ≤ f(|w|) tape cells". (2) The upper bound needs no log factor: there is a universal TM with a *space* budget whose overhead is O(1)-factor in space — simulation with a space counter is more efficient than with a time counter. The diagonalization is verbatim. The file adds: improving the time version's log factor would require a more efficient time-counting universal machine. ∎

## E. Mapping reductions (computability)

### E1 — Parity languages: L₁ ≤m L₂ two ways [Rec5 §2.1]
**Setup.** L₁ = even-length words, L₂ = odd-length words over {a,b}.

**Reduction 1 ("solve the problem").** f(w) = a if |w| even, aa if odd. Computable (a TM can compute |w| mod 2). Correctness: |w| even ⇒ f(w)=a∈L₂; |w| odd ⇒ f(w)=aa∉L₂. Works — but *only because membership in L₁ is decidable*, since f decides it en route.

**Reduction 2 ("transfer the problem").** f(w) = a·w. Computable in constant time (step left, write a). Correctness: |aw| = |w|+1 flips parity, so w∈L₁ ⟺ aw∈L₂ — no deciding happened.

**Lesson (as in file).** Style 1 is unavailable when the source language is undecidable; style 2 is the template for all the hard reductions below. ∎

### E2 — HALT ≤m NON-EMPTY_TM [Rec5 Prop 17]
**The framing recipe (quoted structure from the file).** (1) What to construct: a computable f:Σ*→Σ*. (2) Types: valid inputs ⟨M,w⟩ ↦ machine encodings ⟨T_{M,w}⟩. (3) Condition: M halts on w ⟺ L(T_{M,w})≠∅.

**Common pitfall (boxed in the file).** f(⟨M,w⟩) = ⟨M_ALL⟩ if M halts on w else ⟨M_EMPTY⟩ satisfies the condition but is **not computable** — computing it requires deciding HALT. Every reduction proof must argue computability.

**Proof.** f: invalid inputs ↦ ε (∉NON-EMPTY). Valid ⟨M,w⟩ ↦ ⟨T_{M,w}⟩ where T_{M,w} on any x: erase x, write w, run M on w as a procedure; if M reaches any final state, accept.
- Computability: input-validity checking is decidable; assembling T = (eraser ∘ writer-of-w ∘ M) is string manipulation on ⟨M⟩,w.
- ⟨M,w⟩∈HALT ⇒ M halts on w ⇒ T accepts every x ⇒ L(T)=Σ*≠∅.
- ⟨M,w⟩∉HALT ⇒ the procedure never returns ⇒ T accepts nothing ⇒ L(T)=∅. ∎

**Corollary in file.** With D1 and E3: NON-EMPTY_TM ∉ R.

### E3 — Reduction theorem ⚠ statement + intuition only [Rec5 Thm 18; Rec6 Thm 1]
**Statement.** If L₁ ≤m L₂ then for every C∈{R,RE,coRE}: L₂∈C ⇒ L₁∈C (equivalently L₁∉C ⇒ L₂∉C).

**What the sources contain.** The statement, and the intuition: to handle L₁, apply the reduction machine then whatever machine L₂ has; "L₂ is at least as hard as L₁." The proof itself was assigned (Ex5 Q5: the R and RE cases; Ex5 Q6 adds transitivity, L₁≤mL₂ ⟺ L̄₁≤mL̄₂, and L,L̄∈RE ⇒ L∈R — all statements without written solutions). Everything in group E *uses* this theorem. ∎(statement)

### E4 — HALT ≤m A_TM and A_TM ≤m HALT [Sum w6]
**HALT ≤m A_TM.** f(⟨M,w⟩) = ⟨M′,w⟩ where M′ behaves like M except that rejecting is redirected to accepting. Then M′ accepts w ⟺ M halts on w (either verdict becomes acceptance), so ⟨M′,w⟩∈A_TM ⟺ ⟨M,w⟩∈HALT. f is machine-surgery on the encoding — computable.

**A_TM ≤m HALT.** f(⟨M,w⟩) = ⟨M′,w⟩ where M′ = M with q_rej replaced by an infinite loop. The problematic case this handles: M rejects w (∉A_TM but ∈HALT before surgery). Now M′ halts on w ⟺ M accepts w. ∎

**Consequences drawn in the files.** A_TM ∉ R (E3 + D1); with C6-style membership, A_TM ∈ RE.

### E5 — A_TM is RE-complete [Sum w6]
**Proof.** Membership: A_TM ∈ RE via the universal machine (simulate M on w; accept iff it accepts). Hardness: let L∈RE with recognizer M_L. Define f(x) = ⟨M_L, x⟩ — a fixed prefix stapled to the input, clearly computable. Then x∈L ⟺ M_L accepts x ⟺ ⟨M_L,x⟩∈A_TM. ∎

### E6 — HALT-bar is coRE-complete [Sum w6]
**Proof.** Membership: HALT∈RE (C6) ⇒ HALT-bar∈coRE by definition. Hardness: L∈coRE ⇒ L̄∈RE ⇒ (E5 + composition with A_TM≤mHALT, E4) L̄ ≤m HALT. A reduction f for L̄→HALT is *the same function* as a reduction L→HALT-bar (x∈L ⟺ x∉L̄ ⟺ f(x)∉HALT ⟺ f(x)∈HALT-bar). ∎

### E7 — Non-HALT is coRE-complete [Sum w6]
**Setup.** HALT-bar = {⟨M,w⟩ : M doesn't halt on w} ∪ E where E = invalid encodings; Non-HALT is the first part (valid encodings only).

**Membership.** Non-HALT-bar = HALT ∪ E; HALT∈RE (C6), E∈R⊆RE (validity is decidable), RE closed under ∪ (C4) ⇒ Non-HALT-bar∈RE ⇒ Non-HALT∈coRE.

**Hardness.** Reduce HALT-bar ≤m Non-HALT. On valid ⟨M,w⟩: output it unchanged (YES↦YES, NO↦NO). On invalid x — which *is* in HALT-bar — output a fixed ⟨M₀,w₀⟩ where M₀ is known never to halt on w₀ (so the image is in Non-HALT, preserving the truth value). This invalid-input patch is the entire point of the example in the file. ∎

### E8 — ALL_TM ∉ RE ∪ coRE [Rec6 Prop 2]
**Statement.** ALL_TM = {⟨M⟩ : L(M)=Σ*} is neither in RE nor in coRE. (Overline in the file's "∈ R̄E ∪ coRE-bar" denotes class complement.)

**Proof, part 1: HALT ≤m ALL_TM (⇒ ∉coRE since HALT∉coRE).** f(⟨M,w⟩)=⟨M′⟩; M′ on x: erase x, write w, run M on w; if M halts, accept.
- M halts on w ⇒ M′ accepts every x ⇒ L(M′)=Σ* ⇒ ⟨M′⟩∈ALL_TM.
- M doesn't halt ⇒ M′ accepts nothing ⇒ L(M′)=∅≠Σ*.
Computability: erase/write/simulate assembly as in E2.

*Why this yields ∉coRE:* HALT∉coRE (else HALT-bar∈RE and with HALT∈RE, C5 gives HALT∈R, contradicting D1); by E3's coRE case, ALL_TM∈coRE would pull HALT into coRE.

**Proof, part 2: HALT-bar ≤m ALL_TM (⇒ ∉RE since HALT-bar∉RE).** f(⟨M,w⟩)=⟨M′⟩; M′ on x: run M on w for **|x| steps**; if M halted within them, reject; otherwise accept.
- M never halts on w ⇒ M′ accepts every x ⇒ L(M′)=Σ*.
- M halts on w after k steps ⇒ every x with |x|≥k is rejected ⇒ L(M′)≠Σ*.
Computability: bounded simulation with the input's length as the budget (C1 machinery). ∎

**Pitfall.** The |x|-step timer is the only known way (in this course) to make "M does NOT halt" *verifiable per-input*; students who try to "wait for non-halting" produce non-computable reductions.

### E9 — REG_TM ∉ coRE ⚠ (∉ RE half assigned as Ex6 Q2) [Rec6 Prop 3]
**Statement.** REG_TM = {⟨M⟩ : L(M)∈REG} ∉ coRE.

**Proof.** HALT ≤m REG_TM. f(⟨M,w⟩)=⟨M′⟩; M′ on x: (1) if x=aⁿbⁿ for some n, accept; (2) otherwise run M on w; if it halts, accept.
- ⟨M,w⟩∈HALT ⇒ M′ accepts everything ⇒ L(M′)=Σ*∈REG.
- ⟨M,w⟩∉HALT ⇒ M′ accepts exactly {aⁿbⁿ} ⇒ L(M′)∉REG (B8).
Computability: pattern-check aⁿbⁿ (a decidable TM procedure) + standard simulation assembly. Conclusion via E3 as in E8 part 1. ∎

### E10 — Hardness bookkeeping propositions [Rec6 Props 5–7]
**(a) Hardness spreads (Prop 5 — ⚠ "exercise" in the file, statement only):** L C-hard ∧ L≤mK ⇒ K C-hard.

**(b) RE-hard ⇒ ∉coRE (Prop 6, proven).** Let L be RE-hard, suppose L∈coRE. HALT∈RE ⇒ HALT≤mL; the same reduction gives HALT-bar ≤m L̄. L∈coRE means L̄∈RE, so by E3, HALT-bar∈RE — but then HALT∈RE∩coRE=R (C5), contradicting D1. Symmetrically coRE-hard ⇒ ∉RE; hard for both ⇒ outside RE∪coRE.

**(c) L RE-complete ⟺ L̄ coRE-complete (Prop 7, proven).** If L∈RE and every K∈RE has K≤mL: then L̄∈coRE by definition; for L′∈coRE, L̄′∈RE gives L̄′≤mL, and the same function is a reduction L′≤mL̄. Other direction symmetric. ∎

### E11 — USELESS is coRE-complete [Rec6 Prop 8]
**Membership** = C9. **Hardness:** A_TM-bar ≤m USELESS (A_TM-bar is coRE-hard by E5+E10c; conclude by E10a-style transitivity, which the file invokes).

**Construction.** f(⟨M,w⟩)=⟨H⟩; H on x: erase x, write w, run M on w. If M *accepts* w: H moves to a fresh traversal state (not among M's states), visits every state of itself, then accepts. If M rejects w: H rejects.

**Correctness.** ⟨M,w⟩∈A_TM-bar (M doesn't accept w — rejects or loops) ⇒ the traversal is never triggered ⇒ the traversal state itself is never reached ⇒ ⟨H⟩∈USELESS. ⟨M,w⟩∉A_TM-bar (M accepts w) ⇒ on every input H runs the traversal ⇒ every state visited ⇒ ⟨H⟩∉USELESS.

**Computability — the gadget (the part the file insists on).** How does a machine "visit every state"? Write a special symbol @ on two adjacent cells; order the states arbitrarily; from each state, upon reading @, transition to the *next* state in the order while bouncing between the two @ cells. The @-transitions are only reachable from the traversal entry (no other part of H writes @), so the tour neither fires early nor misses a state. Assembling H (simulation part + traversal part) is computable. ∎

### E12 — NY-HALT: hard on both sides [Sum w6]
**Setup.** Y-HALT = {(⟨M,w⟩,Y) : M halts on w}; N-HALT = {(⟨M,w⟩,N) : M doesn't halt}; NY-HALT = their union.

**RE-hardness.** HALT ≤m NY-HALT via ⟨M,w⟩ ↦ (⟨M,w⟩, Y): halting instances land in Y-HALT⊆NY-HALT; non-halting ones land nowhere (wrong tag).

**coRE-hardness.** Non-HALT ≤m NY-HALT via ⟨M,w⟩ ↦ (⟨M,w⟩, N), symmetrically.

**NY-HALT ∉ RE (and by symmetry ∉ coRE).** If NY-HALT∈RE then by E3 Non-HALT∈RE; with Non-HALT∈coRE (E7) and C5, Non-HALT∈R — "rolling downhill" (the file's phrase) to a contradiction with D1. ∎

## F. Polynomial reductions, NP & Cook–Levin

### F1 — ≤p is transitive (composition) [Sum w8]
**Statement.** A≤pB ∧ B≤pC ⇒ A≤pC.

**Proof.** Let M_f compute the A→B reduction in time O(|x|^{k₁}) and M_g the B→C one in O(|y|^{k₂}). M_h: on x, run M_f to get y=f(x), then M_g to get z=g(y); output z. Correctness: z∈C ⟺ y∈B ⟺ x∈A. Runtime: step (a) is O(|x|^{k₁}). The subtlety (spelled out in the file): step (b)'s bound is in |y|, an internal quantity — but a machine's output is no longer than its running time, so |y|=O(|x|^{k₁}), making step (b) O((|x|^{k₁})^{k₂}); total O(|x|^{k₁k₂}) — polynomial. ∎

### F2 — Reduction theorem for P [Rec7 Thm 15]
**Statement.** A≤pB and B∈P ⇒ A∈P.

**Proof.** M_A: run M_f on x (poly), then M_B on f(x) (poly in |f(x)|), answer as M_B. Correctness identical to E3's pattern. Time: |f(x)|=O(|x|^k) (output≤runtime), so M_B costs O(|x|^{km}); total polynomial. **Corollaries used constantly [Sum w8]:** if L is NPC and L∈P then P=NP (every L′∈NP has L′≤pL∈P); if L is NPC and L∉P then P≠NP. ∎

### F3 — P closed under union and complement [Rec7 Props 10, 12]
**Union.** Run M₁ on x; if accept, accept; else clean up, restore x, run M₂. Both poly ⇒ sum poly. The file's remark: keeping a spare copy of x costs poly-per-step shifting, still poly overall; and note this "contains" the machines directly rather than simulating encodings (universal simulation is *also* poly — exercise 5 fact cited).

**Complement.** Swap q_acc/q_rej of a poly decider: runtime untouched, language complemented. **Non-extension to NP (file's discussion):** for CLIQUE-bar one must certify *no* k-subset is a clique; flipping an NTM's finals makes "some run rejects" the acceptance criterion, which is not complementation. Whether NP=coNP is open. ∎

### F4 — NP closed under union [Rec7 Prop 11]
**Proof.** NTM N on w: nondeterministically pick i∈{1,2}; simulate Nᵢ on w; accept iff it accepts. Some accepting run of N exists ⟺ some accepting run of N₁ or N₂ exists ⟺ w∈L₁∪L₂. Runtime: max of the two polys + O(1). ∎

### F5 — CLIQUE ∈ NP and ∈ EXP [Rec7; Sum w8]
**NP (NTM version, Sum w8).** Guess a vertex subset S nondeterministically; deterministically verify |S|=k (reject otherwise) and that every pair in S is an edge (scan ⟨E⟩ per pair). Correctness: yes-instances have a guess that survives; no-instances kill every guess. Time: guessing linear; checking O(k²) pairs × O(n) scan = O(n³).

**Verifier version [Sum w8].** V(⟨G,k⟩, c): interpret c as k vertex names; check pairwise edges. w∈CLIQUE ⇒ the clique itself is a c making V accept; w∉CLIQUE ⇒ every c fails. Poly in |⟨G,k⟩|.

**EXP [Rec7 Prop 17].** Enumerate every C⊆V with |C|=k; accept if some C is a clique. Each check is poly; there are C(n,k)=O(n^k)=O(2^{k log n}) candidates — exponential since k is part of the input (the file flags exactly this: n^k is *not* poly). ∎

### F6 — 3-SAT ∈ NP [Sum w8]
**Proof.** NTM: verify 3-CNF syntax; guess one truth value per variable; evaluate φ clause by clause. Yes ⟺ some guess satisfies. All steps poly. ∎

### F7 — 3-SAT ≤p CLIQUE [Sum w8]
**Construction.** Given φ (validate 3-CNF; invalid ↦ fixed non-instance, e.g. k>|V|). For each clause cᵢ create a *layer* of 7 vertices — one per assignment of cᵢ's three literals that satisfies cᵢ. Add an edge between two vertices in different layers unless they assign a shared variable oppositely. No intra-layer edges. Set k=m (#clauses). 

**Correctness (⇒).** A satisfying assignment A satisfies each clause, so each layer holds exactly one vertex agreeing with A; those m vertices are pairwise consistent (all read off one A) hence pairwise adjacent — a k-clique.

**Correctness (⇐).** A k-clique S has exactly one vertex per layer (≤1 since layers are edgeless; ≥1 since |S|=m=#layers). Adjacency forces agreement on shared variables, so the union of the local assignments is a well-defined partial assignment; extend arbitrarily. Each clause's chosen vertex is a satisfying local assignment, so every clause — hence φ — is satisfied.

**Complexity.** 7m vertices; O((7m)²) pairs, each checked in O(|φ|); total O(|φ|³). ∎

### F8 — CLIQUE ≤p IS [Rec7 Prop 16]
**Proof.** f(⟨G,k⟩) = ⟨Ḡ,k⟩ where Ḡ has edge {u,v} ⟺ u≠v and {u,v}∉E. S is a clique in G ⟺ S has no Ḡ-edges ⟺ S independent in Ḡ; sizes match. Compute by iterating all O(|V|²) pairs with a membership scan — poly. File's remark: IS≤pCLIQUE holds by the mirror map (assigned, Ex7 Q4a), so the two "go together" w.r.t. P. ∎

### F9 — IS ≤p VC [Rec8 Prop 2]
**Key fact (proven in file).** S independent ⟺ V∖S is a vertex cover: no edge inside S ⟺ every edge touches V∖S.

**Proof.** f(⟨G,k⟩) = ⟨G, |V|−k⟩ (if k>|V|, output a fixed non-instance, e.g. ε — the file's side remark). Independent S, |S|=k ⇒ cover V∖S of size |V|−k; cover C of size |V|−k ⇒ independent V∖C of size k. Counting |V| and subtracting is poly arithmetic. ∎

### F10 — k-SAT ≤p 3-SAT (k>3) [Rec8 Prop 9]
**One shortening step.** For clause φ=(ℓ₁∨ℓ₂∨…∨ℓₖ), introduce fresh y and write φ′ = (y∨ℓ₃∨…∨ℓₖ) ∧ (ℓ₁∨ȳ∨ȳ) ∧ (ℓ₂∨ȳ∨ȳ) ∧ (ℓ̄₁∨ℓ̄₂∨y). The three right clauses are logically equivalent to y ⟺ (ℓ₁∨ℓ₂) (**⚠ this check "left as exercise"**).

**Lemma (proven).** Any satisfying assignment of the original extends to one of the rewrite by setting y := value of ℓ₁∨ℓ₂ (the equivalence clauses hold by construction; the shortened clause holds because either y=T covers it or some ℓᵢ, i≥3, was true). Conversely a satisfying assignment of the rewrite restricted to the old variables satisfies the original: y⟺(ℓ₁∨ℓ₂) is forced, and (y∨ℓ₃∨…∨ℓₖ) true means ℓ₁∨ℓ₂ true or some later literal true.

**Iteration & complexity.** Each application shortens one clause by one and adds one variable; #applications ≤ (input length) × k; each is a local rewrite — poly total. Case k≤3: pad by duplicating literals (noted trivial / Ex). ∎

### F11 — 3-SAT ≤p D-ST-HAMPATH [Rec8 Prop 7]
**Construction.** φ with variables x₁…xₙ, clauses c₁…c_m. Chain of n diamond gadgets from s to t; diamond i contains a horizontal chain of vertices traversable left→right (meaning xᵢ=T) or right→left (xᵢ=F). One vertex per clause c_j, off to the side. If literal xᵢ∈c_j: add a detour usable only left-to-right — exit vertex → c_j → return vertex (return sits right of exit); if x̄ᵢ∈c_j: a detour usable only right-to-left. Separator vertices sit between consecutive exit/return pairs.

**Assignment ⇒ Ham path.** Traverse each diamond in the direction of its variable's value. For each clause pick one true literal (say the first) and take that single detour. Every gadget vertex is covered by the chain traversals; each clause vertex exactly once via its chosen detour; ends at t.

**Ham path ⇒ assignment.** Suppose the path never "cheats" (each detour returns to the adjacent return vertex): reading each diamond's direction defines A, and each clause vertex is visited from some chain whose direction makes that literal true — A satisfies φ. *No cheating:* consider the first deviation. Two shapes (drawn in the file): (i) after a detour the path re-enters a *different* chain; (ii) the path enters a clause from a literal of the wrong direction. In both, a specific vertex ⋆ (the abandoned neighbor / separator) can afterwards only be entered from one side and then has no continuation, so the path can never cover ⋆ and still end at t — contradiction with Hamiltonicity.

**Complexity.** n gadgets, O(m) vertices each (two per clause + separators); wiring each clause is a scan of φ — poly. ∎

**Pitfall.** The separator vertices are load-bearing (they kill cheat (ii)); omitting them from a reproduction breaks the hard direction.

### F12 — U-ST-HAMPATH is NP-complete [Rec9 Props 3–4]
**Membership.** Verifier V(⟨G,s,t⟩, c=⟨v₁…vₙ⟩): check v₁=s, vₙ=t; all vertices distinct (and all of V present — n=|V|); consecutive pairs are edges. Witness poly-sized; checks poly.

**Hardness: D-ST-HAMPATH ≤p U-ST-HAMPATH.** (D-ST-HAMPATH is NP-hard by F11 + 3-SAT's hardness.) Map G to G′: each v becomes v_in, v_mid, v_out with undirected edges {v_in,v_mid},{v_mid,v_out}; each directed (u,v) becomes {u_out, v_in}. Ask for a path s_in → t_out. Size 3×, trivially poly.

*Easy direction.* A directed Ham path s,u¹,…,u^k,t induces s_in,s_mid,s_out,u¹_in,…,t_out — covers all of V′.

*Hard direction.* Claim: an undirected Ham path from s_in to t_out never traverses an edge "backwards" (from some v_in to some u_out). Take the *first* such backward traversal. The path must visit v_mid sometime. If it already did, it must have come from v_out — but reaching v_out earlier requires arriving from some x_in, contradicting "first". If v_mid comes later, it must be entered from v_out, after which the path is stuck at v_mid's dead end (can't exit; must still reach t_out). Either way contradiction. Hence the path has the form s_in,s_mid,s_out,u¹_in,… and contracts to a directed Ham path in G. ∎

### F13 — 3-COLORING is NP-complete [Rec9 Prop 5]
**Membership.** Verifier: witness = a coloring c:V→[3]; scan all edges checking endpoint colors differ. Poly.

**Hardness: 3-SAT ≤p 3-COLORING.** Base triangle on {T,F,B} (mutually adjacent — pins three distinct colors; name them true/false/base). Per variable xᵢ: vertices v_{xᵢ}, v_{x̄ᵢ}, edge between them, and edges from each to B — so one gets color T, the other F. Per clause (l₁∨l₂∨l₃): an OR-gadget (two stacked triangles computing l₁∨l₂ then (l₁∨l₂)∨l₃) whose input taps are the literal vertices and whose output vertex is wired to both B and F — forcing the output to color T.

*Gadget property (stated + used).* If all three inputs are colored F the output must be F — clashing with its F-neighbor: no valid coloring. If some input is T, the gadget extends to a valid coloring with output T.

*⇒.* From a satisfying A: color v_{xᵢ} T iff A(xᵢ)=T (partner gets F) — consistent with B-edges; every clause has a true literal, so every OR-gadget colors validly.

*⇐.* From a 3-coloring: define A(xᵢ)=T iff v_{xᵢ} has T's color (well-defined by the variable gadget). If some clause were unsatisfied, its three literal vertices are F-colored, so its gadget is uncolorable — contradicting the given coloring. Hence A satisfies φ.

**Complexity.** 2 vertices + 3 edges per variable; constant-size gadget per clause. Poly. ∎

### F14 — 2-SAT ∈ P [Rec9 Prop 6]
**Algorithm (as in file).** For each still-unassigned variable xᵢ: tentatively set xᵢ=T; propagate: while changes occur, for each clause (l₁∨l₂), if one literal is false and the other unassigned, assign it true; if a clause becomes wholly false — contradiction: undo this round's assignments and retry xᵢ=F; a second contradiction ⇒ reject. If all variables get assigned without contradiction ⇒ accept.

**Correctness.** Accept ⇒ full assignment, every clause satisfied ⇒ φ∈2-SAT. For reject: the propagation of xᵢ=b assigns only *forced* consequences of xᵢ=b within the still-active clauses; a clean round satisfies all clauses it touched, and the remaining instance shares no assigned variables — a genuinely independent subproblem. Hence a contradiction under xᵢ=T *and* under xᵢ=F means no assignment of the residual instance extends either choice — the formula (equivalently the residual subproblem) is unsatisfiable, so rejecting is correct.

**Complexity.** Outer loop ≤n; each inner while-pass makes ≥1 new assignment ⇒ ≤n passes; each pass scans m clauses with poly work; the one retry doubles it. Polynomial overall. (Worked accept/reject traces are in the file.) ∎

### F15 — SUBSET-SUM is NP-complete [Lec9 §9.2; HRec10]
**Membership.** Verifier: witness = the subset I; check I⊆{aᵢ} and Σ_{x∈I}x = s. Poly.

**Hardness: 3-SAT ≤p SUBSET-SUM.** Represent numbers in a base large enough that no carries can occur (file's explicit warning). Build a digit table: one column per variable x₁…xₙ, one per clause c₁…c_m. For each literal (xᵢ and x̄ᵢ) create a number with digit 1 in column xᵢ, and digit 1 in each clause column whose clause contains that literal. Add slack numbers per clause column: two extra numbers contributing 1 and 1 (allowing +1 or +2 top-up). Target s: digit 1 in every variable column, digit 3 in every clause column.

*Satisfying assignment ⇒ subset.* Pick the number of each true literal. Variable columns: exactly one of xᵢ/x̄ᵢ picked ⇒ digit 1 ✓. Clause columns: each clause has ≥1 true literal ⇒ base contribution 1..3; slack numbers top up to exactly 3 ✓.

*Subset ⇒ assignment.* Variable columns force exactly one of each literal pair chosen — interpret as A. Clause columns: slacks give ≤2, so reaching 3 needs ≥1 from literal rows — i.e., each clause contains a chosen (=true) literal ⇒ A satisfies φ.

**Complexity.** (n+m)-digit numbers, 2n+2m of them — table size poly; construction is direct. ∎

### F16 — KNAPSACK is NP-complete [Rec10 §1]
**Membership.** Verifier on (⟨(w₁,v₁)…(wₙ,vₙ),W,V⟩, c=I′): check I′ is a valid item subset; compute Σwᵢ and Σvᵢ; accept iff Σw≤W ∧ Σv≥V. Poly sums.

**Hardness: SUBSET-SUM ≤p KNAPSACK.** Given ⟨S={s₁…sₙ}, t⟩: items wᵢ=vᵢ=sᵢ; W=V=t.
(⇒) A subset summing to t satisfies both constraints with equality. (⇐) Feasible I′: Σw≤t and Σv≥t, but wᵢ=vᵢ ⇒ the two sums are equal ⇒ t ≤ Σ = Σ ≤ t ⇒ Σ=t exactly — a SUBSET-SUM solution. Linear-work reduction. ∎

### F17 — NPC closed under AtLeastTwo (2024-A exam question) [Rec10 §2]
**Statement.** L NPC (over Σ, #∉Σ) ⇒ AtLeastTwo(L) = {w₁#…#wₙ : n≥2, ∃i<j wᵢ,wⱼ∈L} is NPC.

**Membership.** Identity (verified in file): AtLeastTwo(L) = (Σ*·#)* · L · {#} · (Σ*·#)* · L · (#·Σ*)*. The regular factors are in DTIME(n)⊆P⊆NP; L∈NP; NP is closed under finite concatenation (cited) — so AtLeastTwo(L)∈NP.

**Hardness.** w ↦ w#w is a poly reduction L ≤p AtLeastTwo(L): if w∈L both blocks qualify (i=1,j=2); if w∉L no block does. ∎

### F18 — NP = NP′ (verifier characterization) [Sum w9; Rec9 Prop 2]
**⊇ (verifier ⇒ NTM).** Let V verify L. WLOG |c| ≤ poly(|w|): V runs poly(|w|) steps and cannot read more of c. NTM M: nondeterministically write a candidate c of that length; run V(w,c) deterministically. w∈L ⇒ the good c is one guess ⇒ some accepting run. w∉L ⇒ all c rejected ⇒ no accepting run. Time: generation + verification, both poly.

**⊆ (NTM ⇒ verifier).** Let nondeterministic poly M recognize L. Each step offers ≤ K:=|Q|·|Γ|·2 choices, so a run is described by a choice-string c over [K] of poly length. Deterministic V(w,c): simulate M on w, resolving the i-th nondeterministic step by the i-th letter of c. w∈L ⇒ some accepting run ⇒ its choice-string makes V accept. w∉L ⇒ every run rejects ⇒ every c leads to rejection. Time: poly steps, each simulated in ≤ tape-length ≤ poly. ∎

**Pitfall.** In ⊆, the certificate is the *transcript of choices*, not "the witness object"; conflating the two loses the generality of the argument.

### F19 — Cook–Levin: SAT is NP-complete (⇒ 3-SAT NPC via F10) [Sum w9; Lec9]
**Membership.** CNF-SAT∈NP (guess assignment, evaluate — F6 pattern; also ∈E by enumerating 2ⁿ assignments).

**Hardness: L ≤p SAT for every L∈NP.** Fix a poly-time NTM M recognizing L with time bound t=poly(n).

*Normalization (proven).* WLOG M has a unique accepting configuration: replace q_acc by q_almost-acc in which M erases its tape, homes the head, then enters q_acc. Adds only poly time. (Same for a unique rejecting configuration.)

*Tableau.* A (t+1)×(t+1) table of cells over Γ∪Q; row i encodes configuration Cᵢ (state symbol written at the head position). A filling is *legal* iff row 0 = C₀ = q₀w⌴…⌴, row t = the unique accepting configuration, and every pair of consecutive rows are successive configurations — checkable **locally**: every 2×3 window ("six") must match a pattern derived from δ (rows differ only near the head; the window catalog includes both movement directions and the no-head-nearby identity windows). Then: w∈L ⟺ M has an accepting run on w ⟺ a legal filling exists.

*Formulas.* φ_init(x₀,·) fixes row 0 cell by cell; φ_acc(x_t,·) fixes row t; φ_legal(i,j) over the six cells (x_{i,j},x_{i,j+1},x_{i,j+2},x_{i+1,j},x_{i+1,j+1},x_{i+1,j+2}) accepts exactly the legal window contents. φ = φ_init ∧ φ_acc ∧ ⋀_{i,j} φ_legal(i,j).

*Booleanization.* Each cell variable becomes ⌈log₂(|Γ|+|Q|)⌉ boolean variables (a constant of the machine, not the language). φ̂_init, φ̂_acc are conjunctions of literals — already CNF. For φ̂_legal: its truth table over the (constant-size) window is fixed; take the DNF of the *false* rows, negate, apply De Morgan — a CNF of constant size, the same formula for every (i,j) up to variable renaming.

*The reduction machine M′.* On w: compute t=poly(|w|) (the polynomial is hard-coded); print φ̂_init and φ̂_acc (poly); loop i,j∈[0,t] printing a re-indexed copy of the fixed φ̂_legal with ∧ separators (t² copies). Total time poly.

*Correctness.* w∈L ⇒ an accepting run fills the tableau legally ⇒ the bit-encoding of that filling satisfies every conjunct ⇒ φ̂∈SAT. w∉L ⇒ every filling either isn't legal or ends non-accepting ⇒ some check fails in every assignment ⇒ φ̂ unsatisfiable. ∎

**File's own advice:** "the longest proof in the course — you are expected to read and explain it, not reinvent it." Reproduce the *structure* (tableau → local windows → CNF per window → t² copies) and the two normalizations.

### F20 — coNP mirror facts [Rec10 §3]
**(a) L NP-hard ⟺ L̄ coNP-hard (Claim 5; ⇒ NPC ⟺ complement coNPC).** If every K∈NP has K≤pL, take L′∈coNP: L̄′∈NP ⇒ L̄′≤pL, and the same reduction function shows L′≤pL̄. Converse symmetric.

**(b) If some NP-hard L lies in NP∩coNP then NP=coNP (Thm 7).** For any L′∈NP: L′≤pL and L∈coNP ⇒ L′∈coNP (reduction theorem, coNP case). So NP⊆coNP; complementing both sides gives coNP⊆NP. (Ex10 Q2 = the NPC∩coNP variant, same proof.) The file also records: NP≠coNP ⇒ P≠NP (P is closed under complement, so P=NP would force NP closed under complement), and the three-worlds picture. ∎

### F21 — CNF-TAUTOLOGY ∈ P ⚠ remark-level [Rec10 §3.1]
**As written.** A CNF is a tautology iff each clause is (a falsifying assignment of one clause falsifies the conjunction — the "why?" is left to the reader), and a single disjunctive clause is a tautology iff it contains a complementary pair x, x̄ — a linear scan. By contrast CNF-CONTRADICTION = complement of CNF-SAT is coNP-complete, and general TAUTOLOGY is coNP-complete via the poly map ⟨φ⟩↦⟨¬φ⟩ from CNF-CONTRADICTION. ∎(remark)

### F22 — Self-reduction: search from decision [Lec12 §12.2]
**Statement (SAT).** If a poly-time deterministic M decides SAT, then a poly-time deterministic M′ *outputs a satisfying assignment* of any satisfiable CNF φ.

**Proof.** M′ processes variables in order. To fix xᵢ=T: delete every clause containing literal xᵢ (satisfied) and delete literal x̄ᵢ from every clause containing it (it can't help). Query M on the simplified formula; if unsatisfiable, instead fix xᵢ=F (mirror simplification). Invariant: if the current formula is satisfiable, at least one of the two fixings leaves it satisfiable, and M tells us which — so the invariant persists from the initial satisfiable φ. After n rounds all variables are set and the formula is empty (no clauses) — the accumulated assignment satisfies the original φ. Time: n rounds × (simplification + one M-call on a ≤|φ|-size input) = poly.

**E3SAT variant.** Same loop, but the simplified formula may leave the E3CNF format that M's promise requires. Fix: E3SAT is NPC, so a poly reduction M_f : SAT ≤p E3SAT exists; after each fixing, pass the intermediate formula through M_f before querying M. M_f preserves satisfiability, formulas stay ≤ poly size, so correctness and poly time carry over. ∎

## G. Space complexity, hierarchy theorems, NL, PSPACE

### G1 — Savitch's theorem [Sum w11; Lec10 §10.2]
**Statement.** For space-constructible f: NSpace(f(n)) ⊆ Space(f²(n)). (Stated for f(n)≥n; extended to log n ≤ f(n) in week 13 — the counting of configurations for sublinear space excludes the read-only input tape.)

**Proof.** Let nondeterministic M decide L in space O(f). Configuration graph G_{M,w}: a vertex per configuration (state, head position(s), work-tape contents), an edge u→v iff v is a legal δ-successor of u. WLOG (normalization from Cook–Levin, F19 — noted as not increasing space) there is a unique accepting configuration C_acc. Then w∈L ⟺ there is a directed path C₀→C_acc.

#conf = |Q| · O(f(n)) · |Γ|^{O(f(n))} — exponential in f, so materializing G or BFS is out of budget. Instead decide Reach(u,v,t) — "is there a path u→v of length ≤t?" — recursively:
```
Reach(u,v,t):  if u=v: True
               if v is a δ-successor of u: True
               if t≤1: False
               for each configuration m:                (re-enumerated in place)
                   if Reach(u,m,⌈t/2⌉) and Reach(m,v,⌈t/2⌉): True
               False
```
Top call: Reach(C₀, C_acc, #conf).

*Space accounting (the heart).* The two recursive calls at the same level reuse the same workspace — only one is alive at a time. Each stack frame stores the triple (u,v,t): u,v cost O(f) each (log #conf = log|Q| + O(log f) + O(f)·log|Γ| = O(f)); t ≤ #conf costs O(f) bits. Recursion depth = log(#conf) = O(f). Total: O(f) per frame × O(f) depth = **O(f²)**. Successor checking and u=v need no extra asymptotic space. Correctness: any path of length ≤t splits at its midpoint into two halves of length ≤⌈t/2⌉, and conversely. ∎

**Pitfall.** Say "the two half-calls share space" and "depth × frame = f²" explicitly — that pair of sentences *is* the theorem.

### G2 — PSPACE = NPSPACE [Sum w11]
**Proof.** ⊆: determinism is a special case. ⊇: L∈NPSpace ⇒ L∈NSpace(nᵏ) for some k ⇒ (G1) L∈Space(n^{2k}) ⊆ PSPACE. The file's remark: the square of a polynomial is a polynomial — the same argument for *time* would prove P=NP, which is exactly what we cannot do; space survives squaring because it is reusable. ∎

### G3 — L ⊆ P; log-space outputs are poly-bounded [Sum w11]
**L⊆P.** Let deterministic M decide A in space O(log n) (3-tape model). Possible work-tape contents: |Γ|^{O(log n)} = 2^{O(log n)·log|Γ|} = O(n^c); with |Q| states, n+1 input-head positions, O(log n) work-head positions: #conf = O(n^d). A halting deterministic machine never repeats a configuration (a repeat implies an eternal loop), so runtime ≤ #conf = poly ⇒ A∈P.

**Output bound.** A log-space transducer's print-steps ≤ its runtime ≤ #conf = poly, so |f(w)| ≤ poly(|w|). ∎

### G4 — Log-space functions compose [Sum w12; Lec12]
**Statement.** f,g computable in O(log n) space ⇒ f∘g computable in O(log n) space.

**Proof.** *Wrong first attempt (in the file):* compute w=g(x) onto the work tape, then run M_f on it — but |g(x)| may be poly(n) (G3), busting the budget.

*Correct construction:* run M_f and M_g simultaneously, materializing nothing. Keep two counters: P = the position of M_f's (virtual) input head inside g(x); C = the count of letters M_g has printed in the current re-run. Whenever M_f needs the letter at position P: restart M_g on x from scratch with C:=0, incrementing C at every print-step, until C=P — the letter about to be printed is the one M_f reads. M_f's head moves = increment/decrement P.

*Space:* M_f's work tape: O(log|g(x)|) = O(log n^c) = O(log n); M_g's work tape: O(log n); counters P, C count up to |g(x)| ≤ n^c: O(log n) each. Total O(log n). Time explodes (a full M_g re-run per M_f read) — irrelevant for the space claim. Correctness: each demanded letter is exactly g(x)_P. ∎

### G5 — P ⊊ EXP; TIME(n²) ⊊ TIME(n³) [Lec10 Cor/Ex; Rec12 Cor 1.4]
**TIME(n²)⊊TIME(n³) [Lec10 Example 10.1.1].** Apply D4 with f(n)=n^{2.5} (time-constructible): n² = o(n^{2.5}), so some L∈Time(n^{2.5}log n^{2.5}) ⊆ Time(n³) is not in Time(n²).

**P⊊EXP [Lec10 Cor 10.1.1 / Rec12].** Apply D4 with f(n)=2ⁿ: every polynomial is o(2ⁿ), so the diagonal language L is outside every Time(nᵏ) ⊇-member, i.e. L∉P; and L∈Time(2ⁿ·n) ⊆ EXP. (Rec12's phrasing: P ⊆ TIME(2ⁿ) ⊊ TIME(4ⁿ) ⊆ EXPTIME.) ∎

### G6 — P is not ⋃_{i≤k}TIME(nⁱ) for any fixed k [Rec12 Claim 1.5]
**Proof.** Assume P = ⋃_{i=1}^{k}TIME(nⁱ) ⊆ TIME(nᵏ). Since nᵏ = o(n^{k+1}/log n^{k+1}) and n^{k+1} is time-constructible, the hierarchy theorem gives TIME(nᵏ) ⊊ TIME(n^{k+1}). So P ⊊ TIME(n^{k+1}) ⊆ P — a strict inclusion of a set in itself, absurd. ∎

### G7 — Padding: SPACE(n)⊆P ⟺ PSPACE=P; SPACE(nᵏ)≠P [Rec12 §3]
**Lemma (three equivalents).** (1) PSPACE=P; (2) ∃k: SPACE(nᵏ)⊆P; (3) SPACE(n)⊆P. (1)⇒(2)⇒(3) are inclusions. (3)⇒(1) is padding: take L∈PSPACE, say L∈Space(nᵏ). Define L′ = {w#1^m : w∈L, m=|w|ᵏ} with padded length N = |w|+1+|w|ᵏ = O(|w|ᵏ).
- L′∈SPACE(N): check the pad length (compute |w|ᵏ space-constructibly, rejecting if the output would exceed m cells; compare with m); then decide w∈L in O(|w|ᵏ)=O(N) space. By (3), L′∈P.
- Then L∈P: on w, compute m=|w|ᵏ in poly time, build w#1^m, and run L′'s poly-time decider; its runtime is poly in N = poly(|w|).

**Corollary.** If SPACE(nᵏ)=P for some k, then PSPACE=P=SPACE(nᵏ), so SPACE(n^{k+1}) ⊆ PSPACE = SPACE(nᵏ) — contradicting the space hierarchy's SPACE(nᵏ)⊊SPACE(n^{k+1}). Hence SPACE(nᵏ)≠P for every k (they're incomparable-or-strict, never equal). ∎

### G8 — PATH is NL-complete [Sum w12]
**Membership.** Nondeterministic log-space machine: current := s; repeat: nondeterministically move current to one of its out-neighbors (located by scanning ⟨G⟩ with O(log n) counters); accept upon reaching t. Space: current vertex, candidate next vertex, a scan counter — all O(log n). (File's remark: add a step counter bounded by |V| and reject on overflow to make every run halt.) Correctness: an s→t path yields an accepting guessed walk; no path ⇒ no run ever reaches t.

**Hardness.** Let A∈NL via nondeterministic log-space M. Reduction: w ↦ ⟨G_{M,w}, C₀, C_acc⟩ (unique accepting configuration WLOG). Correctness: w∈A ⟺ accepting run ⟺ directed path C₀→C_acc (G1's equivalence). Log-space computability: a configuration of M on w = (state, input-head position ≤n+1, work-head position, work tape of O(log n) cells) fits in O(log n) bits; the reduction enumerates all ordered pairs (c₁,c₂) of configuration-encodings with two O(log n) counters, checks the local successor condition (configurations almost equal, difference matching δ), and prints the edge if so; C₀,C_acc are printed directly. Nothing beyond O(log n) is ever stored. ∎

### G9 — ≤L composes; NL-hardness spreads [Sum w12]
**Proof.** Transitivity of ≤L: the composed reduction g∘f is log-space computable by G4. Hardness spread: B NL-hard and B≤L C ⇒ for any A∈NL, A≤L B≤L C ⇒ A≤L C. (Reduction theorem for L/NL stated alongside; used with G4-style composition.) ∎

### G10 — NL = coNL ⟺ PATH-bar ∈ NL [Sum w13]
**Proof.** (⇒) PATH∈NL, so its complement is in coNL=NL. (⇐) Assume PATH-bar∈NL. Take A∈coNL: Ā∈NL ⇒ (G8 hardness) Ā ≤L PATH ⇒ the *same* reduction function gives A ≤L PATH-bar ⇒ (reduction theorem, PATH-bar∈NL) A∈NL. So coNL⊆NL; for B∈NL, B̄∈coNL⊆NL shows NL⊆coNL. 

**Accompanying counterexample (why the easy route fails).** Swapping q_acc/q_rej of an NL machine for Ā promises only: w∈Ā ⇒ some run rejects; w∉Ā ⇒ all runs accept — not a machine for A. Concretely for PATH's guess-a-walk machine: a flipped machine accepts whenever some guessed walk misses t, which happens even when a path exists. ∎

### G11 — Immerman–Szelepcsényi: PATH-bar ∈ NL [Sum w13; Lec12]
**Goal.** A nondeterministic log-space machine that, on ⟨G,s,t⟩, has an accepting run iff there is **no** s→t path — using machines that either compute a value correctly and accept, or reject (with at least one non-rejecting run per input).

**Layer counts.** C_k := #vertices reachable from s by ≤k steps. C₀=1. Main loop: compute C₀,C₁,…,C_{n} (n=|V|); then recompute the same for G′ = G minus t (delete t and its edges): C′₀,…,C′_n. Accept iff C_n = C′_n. Justification: t unreachable ⟺ deleting t changes no reachability count ⟺ the two final counts agree; if t is reachable the counts must differ (t itself). 

**Computing C_{k+1} from C_k, certifiably.** For each candidate vertex v (in order): decide *with certainty* whether dist(s,v) ≤ k+1. Inner certification: initialize D_k:=0; for each u∈V: nondeterministically guess a walk of ≤k steps from s (step-by-step, storing only current vertex + step counter); if the guess reaches u, increment D_k and check whether u→v is an edge or u=v (then v is (k+1)-reachable). After the u-loop, compare D_k with C_k (known from the previous round): if D_k < C_k, some reachable u was missed by the guessing — this run's information is incomplete: **reject** (kill the run). If D_k = C_k, every ≤k-reachable vertex was visited, so "no u certified v" genuinely means v is not (k+1)-reachable. Increment C_{k+1} iff v was certified. Honest runs (all guesses succeed) exist for every input, and only honest runs survive to the end — so surviving runs compute every C_k correctly, and the final comparison decides PATH-bar correctly.

**Space.** Current C_k, C_{k+1}, D_k, loop indices u,v, walk position + step counter, and the C/C′ pair — each O(log n); constant count of them. ∎

**Pitfall.** The reject-on-D_k≠C_k step is what turns guessing into *certainty* — without it the machine can't trust a failed guess. Say it.

### G12 — NPSPACE = coNPSPACE (and why NL needs Immerman) [Sum w13]
**Proof.** A∈NPSPACE ⇒ (G2) A∈PSPACE, decided by a deterministic poly-space machine; swap q_acc/q_rej to decide Ā in the same space ⇒ Ā∈PSPACE ⊆ NPSPACE. **Why the same trick fails one level down (file's discussion):** Savitch applied to B∈NL lands in Space(log²n) ⊋ L — there is no way back into NL from the deterministic side, which is exactly the gap Immerman's counting closes. ∎

### G13 — STRONGLY-CONNECTED is NL-complete [Rec12 §6; Lec12]
**Membership (recitation's version).** Nondeterministically choose a pair (a,b); run the PATH-bar NL-machine (G11) on ⟨G,a,b⟩; accept iff it accepts — this recognizes NOT-strongly-connected in NL; conclude STRONGLY-CONNECTED ∈ coNL = NL (Immerman). (Lecture's direct version: for every ordered pair (u,v), guess a u→v walk; accept if all succeed — same O(log n) bookkeeping: two pair indices + walk state.)

**Hardness: PATH ≤L STRONGLY-CONNECTED.** Map ⟨G,s,t⟩ to G′ = G + {(v,s) : v∈V} + {(t,v) : v∈V}.
- If s⇝t in G: for any x,y take x→s ⇝ t→y — G′ strongly connected.
- If s̸⇝t in G: still s̸⇝t in G′ — a simple s→t path cannot use the new edges (they all point *into* s or *out of* t), so it would be a G-path; hence G′ not strongly connected.
Log-space: copy G edge-by-edge; for each vertex index i, print (i,s) and (t,i) — one O(log n) counter. ∎

### G14 — E_NFA is NL-complete [Rec12 §7]
**Membership.** Work with the complement Ē = {⟨A⟩ : L(A)≠∅}. A accepts something iff its state graph has a path from some q₀∈Q₀ to some f∈F. NL machine: guess q₀∈Q₀; guess a state sequence of length ≤|Q| step-by-step, verifying each step is a δ-transition (on some letter); accept upon hitting F. Space: current state, counter ≤|Q|. So Ē∈NL, and by Immerman E_NFA = complement ∈ NL.

**Hardness: PATH ≤L E_NFA-side.** From ⟨G,s,t⟩ build the one-letter NFA A = (V, {a}, δ, {s}, {t}) with δ(u,a) = {v : (u,v)∈E}. Then L(A)≠∅ ⟺ s⇝t. This is a log-space relabeling (scan adjacency structure, print transitions with one vertex counter). Composing with complementation via NL=coNL (as the file does) yields NL-hardness of E_NFA itself. ∎

### G15 — 10-CSS is NL-complete; 2-Con and AL2SCC ∈ NL [Rec12 §8; Sum w13; Lec12]
**Membership of 10-CSS = {⟨G⟩ : G has exactly 10 SCCs}.** Count SCCs with a counter c: iterate v over V; v is the *first vertex of its SCC* iff there is no u<v with u⇝v ∧ v⇝u. Reachability u⇝v is NL; its **absence** is NL by Immerman; the conjunction/negation bookkeeping stays NL (closure under ∩,∪). Each SCC increments c exactly once (at its minimal vertex). Accept iff c=10. Space: u, v, c, and the reachability machinery — O(log n).

**Hardness: STRONGLY-CONNECTED ≤L 10-CSS.** G ↦ G′ = G + 9 fresh isolated vertices. Strongly connected ⇒ #SCC(G′) = 1+9 = 10. Not strongly connected ⇒ ≥2 SCCs in G ⇒ #SCC(G′) ≥ 11. Log-space: copy G, print 9 fixed vertices.

**Companions (proven in Sum w13/Lec12).** A = {⟨G,u,v⟩ : u,v in different SCCs}: ⟨G,u,v⟩∈A ⟺ ⟨G,u,v⟩∈PATH-bar ∨ ⟨G,v,u⟩∈PATH-bar — a union of two NL languages (Immerman for each), so A∈NL. 2-Con/AL2SCC = {G with ≥2 SCCs}: run the PATH-bar machine over all pairs (u,v), accept when some pair certifies non-mutual reachability — O(log n) counters. ∎

### G16 — TQBF ∈ PSPACE [HRec11 §11.3]
**Statement.** TQBF = {⟨φ⟩ : φ a fully-quantified boolean formula that is true} ∈ PSPACE. (Background stated: a fully-quantified formula is simply true or false; all-∃ TQBF = SAT.)

**Proof.** Recursive decider Is-TQBF(φ):
- No variables left: evaluate the constant formula; erase it; leave marker T̂ or F̂.
- φ = ∀x:ψ — write marker ∀̂; recurse on ψ[x:=True], then on ψ[x:=False]; result := T̂ iff both submarkers are T̂; erase, leave result.
- φ = ∃x:ψ — same with ∨: result F̂ iff both are F̂.
Correctness mirrors the semantics of the quantifiers by induction on the number of quantifiers. Space: recursion depth ≤ n (one level per variable); each level keeps one substituted copy of (part of) the formula plus O(1) markers — O(n) per level; total **O(n²)** ⊆ PSPACE. ∎

### G17 — TQBF is PSPACE-hard [HRec11 §11.4–11.5]
**Setup.** L∈PSPACE decided by M in space s(n) = poly(n); WLOG unique accepting configuration c_acc with clean tape (cited from lecture). Reduction w ↦ ⟨φ⟩ with w∈L ⟺ φ∈TQBF.

**Configurations as boolean variables (§11.4).** For a machine using ≤s cells: x_{i,α} ("cell i holds α", i∈[s], α∈Γ), y_i ("head at i"), z_q ("state is q"). Two formulas, both of size O(s²):
- φ_valid(c): exactly one α per cell (⋀_i ⋁_α (x_{i,α} ∧ ⋀_{β≠α} x̄_{i,β})), exactly one head position (⋁_i (y_i ∧ ⋀_{j≠i} ȳ_j)), exactly one state.
- φ(c₁,c₂) — "c₂ is a successor of c₁": φ_valid(c₁) ∧ φ_valid(c₂) ∧ ⋀_{α,i,q} ψ_{i,α,q}, where for δ(q,α)=(r,β,R): ψ_{i,α,q}(c₁,c₂) = (y¹_i ∧ x¹_{i,α} ∧ z¹_q) → (z²_r ∧ y²_{i+1} ∧ x²_{i,β} ∧ ⋀_{j≠i}⋀_η (x¹_{j,η} ↔ x²_{j,η})) — head moves, one cell rewritten, all others copied. (L-moves analogous.)

**Reachability formula (§11.5) — two wrong attempts, then the fix (all three are in the file).**
1. *Naive unrolling:* φ = ∃c₁…∃c_t: (c₁=c₀) ∧ (c_t=c_acc) ∧ ⋀_i φ(cᵢ,c_{i+1}) with t = 2^{s(n)} — exponentially long. Rejected.
2. *Savitch-style split:* φ_k(c₁,c₂) = ∃c_mid: φ_{k/2}(c₁,c_mid) ∧ φ_{k/2}(c_mid,c₂); base φ₁ = φ. Each level *doubles* the formula: O(2^{log t}) = O(t) copies — still exponential. Rejected.
3. *The fix — share the two halves with a ∀:* φ_k(c₁,c₂) = ∃c_mid ∀c₃ ∀c₄: [((c₃=c₁)∧(c₄=c_mid)) ∨ ((c₃=c_mid)∧(c₄=c₂))] → φ_{k/2}(c₃,c₄). Now each level adds O(s) quantified variables and O(s²)-size scaffolding but contains only **one** copy of the sub-formula. Depth log t = s(n) levels ⇒ total size O(s(n)·s(n)²)-ish = poly(n).

φ := φ_t(c₀, c_acc) with t = 2^{s(n)}. Correctness: φ_k(c₁,c₂) is true iff c₂ is reachable from c₁ in ≤k steps (induction on k, using the semantics of the ∀-guard: the implication must hold for both instantiations, which are exactly the two halves). Hence φ true ⟺ M accepts w ⟺ w∈L. The construction is computable in poly time (fixed-shape formulas indexed by i, level count s(n)). ∎

**Pitfall (the file builds the whole section around it).** Writing attempt 2 on an exam is *the* classic error; the ∀-sharing trick is the single idea to remember, and it is the same midpoint idea as Savitch's — implemented in logic instead of recursion.

## H. Randomized classes

### H1 — P ⊆ ZPP, P ⊆ RP, P ⊆ BPP [Sum w14]
**Proof.** A deterministic poly decider, given a coin tape it ignores, always answers correctly in worst-case poly time — hence expected poly time (ZPP). For RP: w∈L accepted with probability 1 ≥ 1/2; w∉L rejected always. For BPP: correct with probability 1 ≥ 2/3 on both sides. ∎

### H2 — RP ⊆ NP [Sum w14]
**Proof.** Compare an RP machine to a polynomial verifier where the certificate is the coin string: both run poly time; for w∉L, every coin string leads to rejection (∀c reject); for w∈L, at least half — in particular at least one — coin string leads to acceptance (∃c accept). So an RP machine literally *is* a verifier of the F18 kind, and L∈NP. ∎

### H3 — One-sided amplification: RP = RP(p) [Sum w14]
**Statement.** RP(p) = RP-with-error-≤p; for constants, RP(1/2) = RP(1/4) = ….

**Proof.** RP(1/4)⊆RP(1/2) trivially. Conversely, from M with one-sided error ≤1/2 build M′: run M on w twice (fresh coins); reject iff both runs rejected, else accept. Time: 2× poly. w∉L: M always rejects ⇒ both runs reject ⇒ M′ rejects — error still zero on this side. w∈L: P[M′ rejects] = P[both reject] ≤ (1/2)² = 1/4. Iterating k times gives error 2^{-k}: any constant. ∎

### H4 — Two-sided amplification: BPP = BPP(ε) [Lec13 §13.1]
**Statement.** For any ε∈(0,1/3]: BPP(ε) = BPP.

**Proof.** BPP(ε)⊆BPP is definitional (smaller error is better). For BPP⊆BPP(ε): from BPP machine M build M′: choose t odd with ε ≤ exp(−(1/4²)·(2/3)t); run M on w t times independently, counting acceptances s; output the majority (accept iff 2s>t).

Analysis via Chernoff (stated in file): for i.i.d. indicators, P[ΣXᵢ < (1−δ)E[ΣXᵢ]] ≤ exp(−δ²E[Xᵢ·t]-style bound as printed). Let Xᵢ indicate "run i answered correctly"; E[ΣXᵢ] ≥ (2/3)t. M′ errs only if ≥t/2 runs err, i.e. correct runs < t/2 = (1−δ)(2/3)t with (1−δ)(2/3)=1/2 ⇒ δ=1/4 > 0. Chernoff bounds this by exp(−(1/4²)(2/3)t) ≤ ε by the choice of t. Constant ε needs constant t; exponentially small ε needs polynomial t — either way runtime = t × poly = poly. ∎

### H5 — BPP = coBPP; RP, coRP ⊆ BPP [Sum w14]
**Proof.** coBPP: swap q_acc/q_rej of a BPP machine — the two-sided ≥2/3 guarantee is symmetric under complement. RP⊆BPP: RP = RP(1/3) by H3; a machine with one-sided error ≤1/3 satisfies BPP's two-sided ≤1/3 requirement a fortiori. coRP⊆BPP: L∈coRP ⇒ L̄∈RP ⊆ BPP ⇒ L∈coBPP = BPP. ∎

### H6 — BPP ⊆ EXP [Sum w14]
**Proof.** Let M be a BPP machine for L running in poly p(n); it reads at most ℓ ≤ p(n) coin cells. M′: enumerate all 2^ℓ coin strings; simulate M on w with each; count acceptances; answer by majority. Correctness: the majority over all coin strings matches the ≥2/3-probability side exactly. Time: 2^{poly(n)} × poly(n) ⊆ EXP. ∎

### H7 — ZPP = RP ∩ coRP [Sum w14; Lec13 Prop 13.1.5]
**(⊆), ZPP→RP.** Let M be a ZPP machine, T its runtime on w (random, E[T] ≤ poly). Build M₁: run M with a step counter capped at k := 4·E[T] (the file uses c=4; the summary's variant uses 2 — same argument); if M finished, answer as M (always correct); if force-stopped, answer q_rej. Time: ≤k = poly always. Errors: w∉L ⇒ either M's (correct) rejection or the forced q_rej — never wrong. w∈L ⇒ wrong only on force-stop; by Markov, P[T > 4E[T]] ≤ 1/4 ≤ 1/2. So M₁ is an RP machine. **ZPP→coRP:** identical, but answer q_acc on force-stop — now the error side is w∉L, again ≤1/4.

**(⊇).** Given RP machine M₁ and coRP machine M₂ for L (both poly-time, one-sided): build M: loop — run M₁(w): if it accepts, output True (M₁ accepting is *certain*: it never accepts w∉L); run M₂(w): if it rejects, output False (certain symmetrically); else repeat with fresh coins.

Correctness: M only ever outputs certainties — zero error. Termination: in each round, if w∈L then M₁ accepts with probability ≥1/2; if w∉L then M₂ rejects with probability ≥1/2 — either way the round terminates the loop with probability ≥1/2. E[#rounds] = Σᵢ i·2^{-i} = O(1) (≤2), so expected time ≤ E[R]·(runtime of both machines) = poly. Hence L∈ZPP. ∎

**Pitfall.** In (⊆), the direction of the forced answer must match the machine's *allowed* error side (reject-on-timeout for RP, accept-on-timeout for coRP); flipping it silently breaks the zero-error side.

---

## Files that couldn't be fully processed

All **51 unique PDFs were read** (1 byte-identical duplicate skipped). Proof-specific caveats:

1. **English recitation 13 (תרגול 13)** — the four embedded past-exam questions and their solutions are **screenshots with no text layer**; the surrounding theory (all statements) was captured, but any proofs inside those images could not be extracted and are **not** in this catalog.
2. **Diagrams** — the HAMPATH gadget figures (F11, F12), the 3-COLORING or-gadget (F13), the Cook–Levin tableau/window figure (F19), and the class Venn diagrams are images; the written reconstructions above follow the surrounding prose, and the "shape" details of gadgets should be re-drawn from the originals when memorizing.
3. **Deferred proofs** — the following are *stated* in lecture/recitation files but their proofs live only in unsolved exercise sheets, and are therefore flagged, not completed: reduction theorem (E3 / Ex5 Q5), REG⊆NREG (A7 / Ex2 Q1), δ*([ε],w)=[w] in Myhill–Nerode (B3 / Ex3 Q5), ∼_L reflexivity+symmetry (B2), NREG-concatenation correctness (A5), subset-simulation invariant (Rec3 Prop 2), REG_TM∉RE (E9 / Ex6 Q2), 3-clause⟺y-equivalence check (F10), IS≤pCLIQUE (Ex7 Q4a), NP⊆EXP (Ex7 Q6), HALT_ε,bin∉R (Ex6 Q6), hardness-spread Prop 5 (E10a), ≤L transitivity details (Rec12 "similar to standard"), NL closure under ∪/∩ (Ex12 Q4), and the log-space verifier characterization of NL (Ex12 Q2).
4. **Sketch/idea-level proofs in the sources** (reported at their actual depth, per the grounding rule): universal TM (C7), DECIDABLE∉R (D2), primes-not-regular (B7), CNF-TAUTOLOGY∈P (F21), L_EVEN (A8), Cook–Levin's window-catalog enumeration (F19 — the file shows the R-move windows and says "similarly for L").
