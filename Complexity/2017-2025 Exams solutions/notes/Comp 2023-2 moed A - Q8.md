# Comp 2023-2, Moed A — Question 8 (study notes)

Source exam: `Complexity/2017-2025 Exams/Comp 2023-2 moed A.pdf`
Official solution: `Complexity/2017-2025 Exams solutions/Comp 2023-2 moed A solution.pdf`

## Q8 (12 pts)

A path is *simple* (מסלול פשוט) if it does not contain the same vertex twice (no repeated node).

L = { (G, s, t, k) : G is a directed graph containing a **simple** path from s to t of **length ≥ k** }.

Question: which complexity class does L belong to?

**Answer: L is NP-complete.**

### Membership in NP
Certificate = the path itself (a sequence of vertices). A verifier checks in poly time that it
starts at s, ends at t, every consecutive pair is an edge of G, no vertex repeats (simple), and it
uses ≥ k edges. ✓

### NP-hardness — reduce from Hamiltonian path (fixed endpoints)
Directed Hamiltonian s→t path is NP-complete. A Hamiltonian s→t path is exactly a *simple* path
from s to t visiting all n vertices, i.e. of length n−1. So

  G has a Hamiltonian s→t path  ⟺  (G, s, t, n−1) ∈ L.

The map ⟨G,s,t⟩ ↦ ⟨G,s,t,n−1⟩ is poly-time computable ⟹ L is NP-hard. Combined with membership,
**L is NP-complete.**

### The trap: L is NOT reachability
The two words doing all the work are **"simple"** and **"≥ k"** (a *lower* bound — we want a *long*
path). Change either and it collapses into P:

| Problem | Class |
|---|---|
| Is t reachable from s? (any walk) | P (BFS/DFS) |
| Shortest s→t path of length ≤ k? | P (BFS) |
| Simple s→t path of length **≥ k** (this L) | **NP-complete** |

Reachability (st-connectivity) only tells you *some* path exists — nothing about whether a *long
simple* one does. That gap is the NP-hard core.

---

## Issues log

Track here which parts gave trouble, and how they were resolved.

- **Q8 (reachability-vs-long-path confusion):** Reasoned "PATH ∈ P, so PATH-bar ∈ P, therefore if L
  excludes the unreachable-t cases it is also in P." Resolved: the fallacy is conflating L with
  **reachability**. PATH/st-connectivity ("does any walk from s to t exist?") is in P and so is its
  complement — but L asks for a **simple path of length ≥ k**, which is the LONG-PATH problem and is
  **NP-complete** (Hamiltonian s→t path ≤p L via k = n−1). Filtering out unreachable-t instances in
  poly time is a *valid preprocessing step*, but it does not put L in P: the hard instances are
  precisely those where **t IS reachable**, and knowing a path exists says nothing about whether a
  *long simple* one does. Key takeaway: "simple" + "≥ k" (a lower bound) is what forces NP-hardness;
  dropping simplicity (walks) or flipping to "≤ k" (short path) would land it in P.
