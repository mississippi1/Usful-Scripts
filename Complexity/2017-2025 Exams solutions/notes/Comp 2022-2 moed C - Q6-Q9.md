# Comp 2022-2, Moed C — Questions 6-9 (study notes)

Source exam: `Complexity/2017-2025 Exams/Comp 2022-2 moed C.pdf`
Official solution: `Complexity/2017-2025 Exams solutions/Comp 2022-2 moed C solution.pdf`

## Q6 (12 pts)

Claim: XYTIME ∈ co-RE, where
XYTIME = { <M> | there exist two inputs x and y such that M accepts x and y in the same running time }

**Answer: FALSE** (XYTIME ∉ coRE).

**Proof (direct reduction from HALT):**

We show HALT ≤m XYTIME, where HALT = {<M,w> : M halts on w}. Since HALT ∉ coRE, and a language reducible *to* a coRE language must itself be coRE, this forces XYTIME ∉ coRE.

Given <M,w>, build M' as follows, on input z:
1. Simulate M on the fixed string w (ignore z during this phase). This costs some number of steps T depending only on M, w — the same for every z.
2. If that simulation halts, erase z from the tape (scan right to the blank, then scan back erasing) — a cost depending only on |z|.
3. Accept.

(WLOG assume M's alphabet has ≥ 2 symbols, padding it with a spare symbol if needed.)

Total running time of M' on z is T + (erase cost depending only on |z|).

- If M halts on w: for two distinct single-symbol strings z1 = σ, z2 = τ (σ ≠ τ), M' accepts both in exactly the same time T + O(1), so <M'> ∈ XYTIME.
- If M does not halt on w: step 1 never finishes for any z, so M' never accepts anything: L(M') = ∅, so <M'> ∉ XYTIME.

So <M,w> ∈ HALT ⟺ <M'> ∈ XYTIME. The reduction is computable (standard TM-construction: hardcode w into M', simulate M on it, then erase-and-accept). Hence HALT ≤m XYTIME, and XYTIME ∉ coRE.

(The original official solution instead reduces from HALT-on-empty-tape; the direct HALT reduction above is simpler since w is already fixed/hardcoded, so no "erase-then-simulate" step is needed before the halting check — erasing is only needed afterward, to make timing depend solely on |z|.)

## Q7 (12 pts)

Define PolyNL = ⋃_{i≥1} NSPACE(log^i n).

Claim: PolyNL = co-PolyNL.

**Answer: TRUE.**

By Savitch's theorem, NSPACE(log^i n) ⊆ SPACE(log^{2i} n) for every i ≥ 1. Also SPACE(log^i n) ⊆ NSPACE(log^i n) trivially (deterministic ⊆ nondeterministic). Hence:

PolyNL ⊆ ⋃_i SPACE(log^{2i} n) ⊆ ⋃_i SPACE(log^i n) ⊆ ⋃_i NSPACE(log^i n) = PolyNL

(the middle inclusion holds because {2i : i≥1} ⊆ {i : i≥1}, so the union over all i absorbs it). All inclusions are therefore equalities, giving:

PolyNL = ⋃_{i≥1} SPACE(log^i n)

Each deterministic class SPACE(log^i n) is closed under complementation (flip accept/reject of a decider), so a countable union of complement-closed classes is complement-closed. Hence co-PolyNL = PolyNL.

## Q8 (12 pts)

Define LongPath = { <G,s,t> | G is a directed graph that has a path from s to t that visits all vertices at least once, and at most two vertices are visited twice }.

Which class does LongPath belong to? **Answer: NP-Complete.**

**In NP:** the witness is the path itself. Verify in poly time: (1) the path has length ℓ ∈ [|V|, |V|+2] (check this first, to bound the rest), (2) it starts at s and ends at t, (3) every vertex appears at least once. All checkable in poly time once the length is bounded.

**NP-hard:** reduce HAMPATH ≤p LongPath. Given <G,s,t>, build G' by adding two fresh vertices u, v and edges {(s,u), (u,s), (t,v), (v,t)}. Since u and v's only neighbors are s and t respectively, any path through G' that visits u and v must traverse the loops s→u→s and t→v→t, forcing s and t to each be visited twice — exactly using up the "at most two vertices visited twice" budget. So <G',s,t> ∈ LongPath iff, after stripping the forced s,u,s...t,v,t prefix/suffix, the middle segment is a Hamiltonian path in G. Hence <G,s,t> ∈ HAMPATH ⟺ <G',s,t> ∈ LongPath. The construction is poly-time (2 new vertices, 4 new edges).

## Q9 (12 pts)

Define DISCONN = { <G> | G = (V,E) is a directed graph and there is a single edge e such that after removing e, G is disconnected }.

Which class does DISCONN belong to? **Answer: NL.**

Use NL = coNL (Immerman–Szelepcsényi): give an NL algorithm for the complement, DISCONN-bar. On input G = (V,E): for every edge e ∈ E and every pair of distinct vertices s, t, nondeterministically guess a path of length ≤ |V| from s to t that avoids e. Accept only if such a path is found for every (e,s,t) triple; otherwise reject.

**Correctness:** <G> ∈ DISCONN iff some edge e, when removed, disconnects some pair s,t — i.e. no e-avoiding path exists for that pair. The algorithm (which requires success for *all* triples) accepts exactly DISCONN-bar.

**Space:** iterating over (e,s,t) needs O(log|V| + log|E|) bits; guessing/verifying a bounded-length path needs another O(log|V|) bits (a length counter plus current/last vertex, to compare against e). Total: O(log n) — logspace.

Since DISCONN-bar ∈ NL and NL = coNL, DISCONN ∈ NL.

---

## Issues log

Track here which questions gave trouble, and how they were resolved. Updated as issues come up.

*(none logged yet)*
