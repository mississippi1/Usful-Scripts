# Comp 2022-2, Moed B — Question 8 (study notes)

Source exam: `Complexity/2017-2025 Exams/Comp 2022-2 moed B.pdf`
Official solution: `Complexity/2017-2025 Exams solutions/Comp 2022-2 moed B solution.pdf`

## Q8 (12 pts)

Define the language
ST-Conn₂₀₂₂ = { (G,s,t) | G is a directed graph and there is a path from s to t of length ≤ 2022 }.

Which class does it belong to? (circle: L / NL-Complete / NP-Complete)

**Answer: L.** The decisive fact is that **2022 is a constant** bound on the path length (not |V|).
That is exactly what makes this L rather than NL.

### Log-space algorithm (depth-bounded DFS)

```
Reach(u, d):          // is there a walk from u to t using ≤ d edges?
    if u == t: return true
    if d == 0: return false
    for v = 1 .. |V|:                 // scan candidate neighbours one at a time
        if (u,v) ∈ E and Reach(v, d-1): return true
    return false

answer = Reach(s, 2022)
```

### Space accounting (the point)

- Recursion **depth ≤ 2022 = O(1)** — a constant, independent of the graph.
- Each stack frame stores only: current vertex u (log|V| bits) + loop index v (log|V| bits) + d (O(1)).
- Cells are **reused across sibling branches**: when a recursive call returns, its frame is freed
  before the next neighbour is tried. At any instant only the single current root-to-node path
  (≤ 2022 vertices) is on the stack.

Total = 2022 × O(log|V|) = **O(log|V|)** (constant factor absorbed). Deterministic ⟹ ST-Conn₂₀₂₂ ∈ L.

Equivalent view: write 2022 explicitly-nested loops, each with one vertex variable →
2022 × log|V| = O(log|V|) variables.

No distinctness check is needed: "∃ walk of length ≤ 2022" ⟺ "∃ simple path of length ≤ 2022"
(chopping cycles only shortens a walk), so exploring walks is correct and there is no linear-memory
trap.

### Common mistake (branching ≠ space)

The tempting wrong estimate is |V|·log|V| ("each vertex has up to |V| neighbours"). But the
branching factor |V| is spent in **time** (runtime up to |V|^2022), **not space** — you never store
all neighbours or a BFS frontier; you hold only the current path plus one neighbour index per level.

### Contrast that pins down why it's L

| | length bound | recursion depth | space | class |
|---|---|---|---|---|
| general PATH | \|V\| | \|V\| | \|V\|·log\|V\| — too big | NL (not known in L) |
| ST-Conn₂₀₂₂ | 2022 (const) | 2022 | O(log\|V\|) | **L** |

General PATH needs a stack up to |V| deep (|V|·log|V|, not log space) → we use nondeterminism
(guess the path step-by-step with a counter) and land in NL. Capping the length at a constant kills
the stack depth, so deterministic log space suffices.

---

## Issues log

Track here which parts gave trouble, and how they were resolved.

- **Q8 (couldn't prove log space):** Knew the answer was L but estimated the space as |V|·log|V|,
  reasoning that each vertex has up to |V| neighbours. Resolved: the branching factor |V| is a
  **time** cost (runtime up to |V|^2022), not a space cost. The log-space algorithm is a
  depth-bounded recursive DFS: recursion **depth = 2022 is constant**, each frame keeps only the
  current vertex + a neighbour index (O(log n)), and cells are **reused across sibling branches**, so
  total space = O(1) × O(log n) = O(log n). Key contrast drawn with general PATH (bound |V| ⇒ depth
  |V| ⇒ |V|·log|V| ⇒ NL, not known L): the *constant* length bound is precisely what drops this into
  L. Also noted no simplicity check is needed (walk-existence ⟺ short-simple-path-existence).
