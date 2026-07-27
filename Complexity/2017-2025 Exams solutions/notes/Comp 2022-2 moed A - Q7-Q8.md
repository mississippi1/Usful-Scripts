# Comp 2022-2, Moed A — Questions 7-8 (study notes)

Source exam: `Complexity/2017-2025 Exams/comp 2022-2 moed A.pdf`
Official solution: `Complexity/2017-2025 Exams solutions/Comp 2022-2 moed A solution.pdf`

## Q7 (12 pts)

Define the language
LongPath = { <G,s,t,k> | G is a directed graph s.t. the distance from s to t is at least k }.

Which complexity class does LongPath belong to? (circle: NL-Complete / NP-Complete / PSPACE-Complete)

**Answer: NL-Complete.** (Abbreviate LP = LongPath.)

### The key observation

"distance ≥ k" is a *universal* ("no short path exists") condition, and t may even be
unreachable (distance ∞ ≥ k). Nondeterminism can confirm a path *exists*, not that every
path is long — so the **complement** is the naturally-NL side, and we rely on
**NL = coNL** (Immerman–Szelepcsényi) to bring LP itself into NL. This is the trap: it
looks like plain PATH but it is really the coNL side.

### Membership: LP ∈ NL

By Immerman (NL = coNL) it suffices to put the complement LP̄ = { distance < k } ∈ NL.
LP̄ = { <G,s,t,k> : there is an s→t path of length < k }.

NL machine for LP̄: nondeterministically guess a length i < k, then guess a path of i
steps from s to t (store only the current vertex + a step counter, following edges of ⟨G⟩).
Accept iff t is reached. Some run accepts ⟺ a short (< k) s→t path exists ⟺ distance < k.

Space: current vertex, candidate next vertex, and a step counter all hold values ≤ |V| — the
counter never needs to exceed min(k−1, |V|−1) because a shortest path is simple — so
O(log n) bits. Hence LP̄ ∈ NL, and by NL = coNL, **LP ∈ NL**.

### Hardness: NL-hard (official chain reduction)

Since PATH is NL-hard, it suffices to give a log-space reduction relating PATH and LP.
The official reduction maps
  f(<G=(V,E), s, t>) = <G', s, t, |V|+2>,
where, writing V = {v₁,…,vₙ} and adding n fresh vertices x₁,…,xₙ:
  V' = V ∪ {x₁,…,xₙ}
  E' = E ∪ { (xᵢ, xᵢ₊₁) : i < n } ∪ { (s, x₁), (xₙ, t) }.

So G' adds one long detour chain  s → x₁ → x₂ → … → xₙ → t  (|V|+2 vertices on it; the
solution counts path length in **vertices**, so this chain has length |V|+2).

Correctness:
- If there is **no** s→t path in G, then the chain is the *only* s→t path in G', so
  distance = |V|+2 = k ⟹ f(...) ∈ LP.
- If there **is** an s→t path in G, it is simple, so it uses ≤ |V| vertices and still exists
  in G'; hence distance ≤ |V| < |V|+2 = k ⟹ f(...) ∉ LP.

Log-space: copying E and V is log-space; the new vertices/edges need one counter i ∈ [n];
computing k = |V|+2 is log-space.

### Subtlety worth remembering (direction of the reduction)

The solution labels this "PATH ≤ₗ LP", but the construction actually satisfies
  <G,s,t> ∈ PATH  ⟺  f(...) ∉ LP,
i.e. it maps **non-reachability** to LP-membership. So what it really realizes is
**PATH̄ ≤ₗ LP** (equivalently PATH ≤ₗ LP̄). That is still a valid NL-hardness proof, because
PATH̄ is itself NL-complete (NL = coNL). This is not an accident: because "distance ≥ k"
fires precisely when t is *far/unreachable*, no monotone gadget can turn "s reaches t" into
"no short path exists" — the complementation is unavoidable, and the whole problem rests on
NL = coNL. A direct "positive" PATH ≤ₗ LP gadget with a small k cannot work.

(Note on the distance convention: the solution measures path length in **vertices**, giving
k = |V|+2. With the more common edge-count distance the same reduction uses k = |V|+1, or
simply k = |V| with the unreachable case giving distance ∞.)

## Q8 (12 pts)

Define the language
LargeCycle = { (G,x) | G is an **undirected** graph, with a **simple cycle** that contains
at least |V(G)|/2 distinct vertices including x }.

Which complexity class does LargeCycle belong to? (circle: NL-Complete / NP-Complete / PSPACE-Complete)

**Answer: NP-Complete.** (NOT NL-complete — see the trap below.)

### The trap: why this is NOT NL

The tempting wrong answer is NL, via "guess the cycle and verify in log space." That fails on
the one check that matters: the cycle must be **simple** (all vertices distinct). The certificate
here is a cycle of ≥ |V|/2 vertices — a **linear-size** object — and certifying that its vertices
are all distinct needs to remember the set of vertices already seen: Θ(|V|) bits, not O(log n).
The NL verifier characterization gives a **read-once** certificate tape plus an O(log n) work
tape, so you can neither store the seen-set nor re-scan to catch repeats.

This is the exact NL/NP boundary:
- `PATH` ∈ NL because reachability needs only a **walk** — you guess vertex-by-vertex keeping just
  the current vertex + a counter ≤ |V|, and you never certify simplicity (if a walk exists a simple
  path exists).
- "simple cycle/path covering many **distinct** vertices" (Hamiltonian family: HamCycle,
  LongestPath, LargeCycle) forces certifying no repeats → out of log space → NP.

Also note: a reduction **from** PATH (`PATH ≤ₗ LargeCycle`) would only prove NL-**hardness** (a lower
bound), which every NP-complete problem already satisfies — it says nothing about NL-**membership**.
So even a correct PATH reduction argues for the wrong thing. (In fact LargeCycle ∉ NL unless P = NP,
since it is NP-hard and NL ⊆ P.)

### Membership: LargeCycle ∈ NP

Witness = the cycle. Verify in poly **time** (poly work space, which is what lets you check
distinctness): it is a simple cycle, has ≥ |V|/2 vertices, and includes x.

### Hardness: NP-hard via HamCycle ≤p LargeCycle (official)

Given G = (V,E), build G' by duplicating each vertex with an **isolated twin**:
  V' = V ∪ { v' : v ∈ V }   (so |V'| = 2|V|, hence |V'|/2 = |V|),
  E' = E   (the twins v' get no edges),   and pick any x ∈ V.
Since every edge of G' lies inside the original V, any simple cycle with ≥ |V'|/2 = |V| distinct
vertices must use **all** of V — i.e. a Hamiltonian cycle of G (which automatically passes through x).
So G ∈ HamCycle ⟺ (G',x) ∈ LargeCycle; the reduction adds |V| vertices in poly time. Hence NP-hard,
and with membership, **NP-Complete**.

---

## Issues log

Track here which parts gave trouble, and how they were resolved.

- **Q7 (hardness direction):** Asked to prove LongPath's class "using an NTM and a reduction
  from PATH." Resolved: LP is **NL-complete** — membership by putting the complement
  (short path, < k) in NL and invoking NL = coNL (Immerman); hardness by the official
  chain-detour reduction with k = |V|+2. The clarifying point was that a *direct* PATH ≤ₗ LP
  with a positive gadget cannot work: "distance ≥ k" is a coNL condition that fires on
  non-reachability, so the reduction inherently goes through the complement (PATH̄ ≤ₗ LP), and
  the official solution — despite its "PATH ≤ₗ LP" label — in fact maps non-reachable
  instances to LP-membership. Also clarified the solution's length-in-vertices convention
  (k = |V|+2 vs the edge-count k = |V|+1).

- **Q8 (misclassified as NL):** Thought LargeCycle was NL-complete, reasoning "a log-space verifier
  can guess the cycle and check ≥ |V|/2 vertices + edges + closure," plus a reduction from PATH.
  Resolved: correct answer is **NP-Complete**. The verifier argument fails because it omits the
  **simplicity/distinctness** check — certifying that ≥ |V|/2 guessed vertices are all distinct needs
  Θ(|V|) memory (a read-once certificate + O(log n) work tape can't store the seen-set or re-scan),
  which is exactly the NL→NP boundary (contrast PATH, where a mere walk suffices and simplicity is
  never certified). Separately, a reduction *from* PATH only gives NL-hardness (a lower bound every
  NP-complete problem meets) and never NL-membership. Correct proof: in NP (witness = cycle, checked
  in poly time), NP-hard via HamCycle ≤p LargeCycle using the isolated-twin vertex-doubling gadget so
  that |V'|/2 = |V| forces the large cycle to be Hamiltonian. General rule captured: "simple
  path/cycle over many distinct vertices" ⇒ Hamiltonian-family ⇒ NP, not NL.

- **Q7 (answer sheet circled NP-Complete):** The marking is **wrong** — the answer is
  **NL-Complete**, as derived above. Root cause of the error identified: reading the language by its
  **name** rather than its definition. "**distance** from s to t is at least k" means the *shortest*
  path is long, i.e. **no s→t path of length < k exists** — a **universal** condition — whereas the
  name "LongPath" suggests the existential "there is a simple path of length ≥ k", which is the
  Hamiltonian family and would indeed be NP-complete (cf. `Comp 2025 summer moed A - Q9
  (half-Hamiltonian path).md`). One word, two classes:
  | reading | shape | class |
  |---|---|---|
  | dist(s,t) ≥ k — no short path exists (the real definition) | ∀ | NL-complete |
  | ∃ simple path of length ≥ k (what the name hints at) | ∃ + global distinctness | NP-complete |
  Structural sanity check to apply next time: LongPath ∈ NL ⊆ P, so it **cannot** be NP-complete
  unless P = NP — a class marking that contradicts a membership proof you can produce yourself is
  self-refuting. Also re-confirmed: the counter in the complement's NL machine stays O(log n) even
  when k is written in **binary**, since it is capped at min(k−1, |V|−1) (shortest paths are simple),
  and that NL = coNL (Immerman–Szelepcsényi) is genuinely load-bearing here, not decorative.
  Contrast within this same exam: Q8 (LargeCycle) *is* NP-complete, because there the certificate must
  prove all vertices are **distinct**, which log space cannot do.

- **Q7 (cross-reference — the near-identical twin that IS NP-complete):** Comp 2023-2 moed A Q8
  defines L = {⟨G,s,t,k⟩ : G contains a **simple path** from s to t of length ≥ k} — same vocabulary,
  opposite class (**NP-complete**, by HAM-PATH ≤p L with k = n−1). Full write-up and the side-by-side
  comparison table live in `Comp 2023-2 moed A - Q8.md`. Keep the pair together when revising: the
  deciding word is **"distance"** (a minimum over paths ⟹ a lower bound on it is universal ⟹ NL)
  versus **"contains a simple path"** (existential over an object needing a distinctness check ⟹ NP).
