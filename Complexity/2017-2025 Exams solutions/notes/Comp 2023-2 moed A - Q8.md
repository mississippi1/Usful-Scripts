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

- **Q8 (follow-up — "but G8 says PATH ∈ NL ⊆ P"):** True, but G8's PATH is a *different language*.
  This is a **language-identity** error, not a complexity-class error. In `PROOFS_REFERENCE.md`:
  - **G8 (PATH is NL-complete)** = reachability, {⟨G,s,t⟩ : some walk s⇝t exists}. Its NL machine
    stores *only the current vertex + a step counter* — which is exactly why it works: it never
    enforces simplicity (if any walk exists a simple one does too, so simplicity is free) and has no
    "≥ k" bound. That machine **cannot** decide L: (1) enforcing "no repeated vertex" needs to
    remember all visited vertices = linear space, not O(log n); (2) without simplicity, "length ≥ k"
    is trivial to satisfy by looping a cycle — the lower bound only bites *because* the path must be
    simple.
  - **F12 (U-ST-HAMPATH is NP-complete)** sits right next to G8 and is the correct analogue: its
    verifier checks the vertex sequence is "all distinct (and all of V present)" — a *simple* path of
    length n−1. That is a special case of L (k = n−1), which is why L inherits F12's NP-hardness.
  So L belongs to the **F12 (Hamiltonian) family**, not the **G8 (reachability) family**. PATH ∈ NL,
  and PATH-bar ∈ NL too (G10/G11, NL = coNL) — both correct, both irrelevant to the *long simple
  path* problem L.
