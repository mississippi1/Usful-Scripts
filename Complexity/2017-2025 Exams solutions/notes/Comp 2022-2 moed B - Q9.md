# Comp 2022-2, Moed B — Question 9 (study notes)

Source exam: `Complexity/2017-2025 Exams/Comp 2022-2 moed B.pdf`
Official solution: `Complexity/2017-2025 Exams solutions/Comp 2022-2 moed B solution.pdf`

## Q9 (12 pts)

Define the language
2-Clique = { (G,k) | G has two vertex-disjoint cliques, one of size k and one of size 2k }.

Which class does it belong to? (circle: P / NP-Complete / PSPACE-Complete)

**Answer: NP-Complete.**

### Membership: 2-Clique ∈ NP

Witness = 3k vertices. Verify in poly time: no vertex repeats, the first k form a clique in G, and
the other 2k form a clique in G.

### Hardness: CLIQUE ≤p 2-Clique (official)

CLIQUE = { ⟨G,k⟩ : G has a clique of size k }. Given ⟨G,k⟩:
- If k > |V|: return a fixed non-instance (no k-clique can exist).
- Else: add 2k brand-new vertices {v₁,…,v_{2k}}, fully connected among themselves and with **no edges
  to G**. Return ⟨G', k⟩. (G' = G plus a disconnected, ready-made 2k-clique gadget H.)

Correctness — G' has disjoint k- and 2k-cliques ⟺ G has a k-clique:
- (⟸) A k-clique C in G, together with H (size 2k), are disjoint cliques.
- (⟹) H is a **separate component**, so every clique of G' lies entirely in G or entirely in H. The
  2k-clique is either inside G (then G has a 2k-clique ⊇ a k-clique) or equals H; in the latter case
  the disjoint k-clique cannot reuse H, so it lives in G. Either way G has a k-clique.

The 2k-clique requirement is satisfied **by construction**, so the only remaining question is "does G
have a k-clique?" — exactly CLIQUE.

### The k > |V| guard (binary k)

k is given in **binary**, so k > |V| may be exponential in the input length — adding 2k gadget
vertices would then be super-polynomial. Since k > |V| also means G trivially has no k-clique, map it
to a fixed non-instance. (Same binary-k subtlety as the other doubling reductions in this exam set.)

### Design lesson (why not build the 2k-clique from the k-clique)

A tempting alternative is to *manufacture* the 2k-clique out of the instance — e.g. duplicate G and
split each vertex v into v, v' with v' joined to N(v) — hoping a k-clique becomes a 2k-clique. Two
things go wrong:
1. It usually is not even a clique: two split copies u_i', u_j' are each wired only to *original*
   vertices, not to each other, so {u₁,u₁',…,u_k,u_k'} is not complete.
2. Even if it were, the derived 2k-clique reuses the same original vertices as the k-clique, so the
   two cliques are not **vertex-disjoint**, which 2-Clique requires.

General rule: a "∃ a vertex-disjoint sub-structure of fixed size f(k)" clause is usually free — attach
it as a separate component and let the remaining requirement carry the original hard instance. Reserve
gadgetry for the part that actually encodes the problem.

---

## Issues log

Track here which parts gave trouble, and how they were resolved.

- **Q9 (over-engineered reduction):** Built a duplicate-and-split construction to turn a k-clique into
  a 2k-clique, whereas the official reduction simply bolts on a disconnected 2k-clique gadget.
  Resolved: for CLIQUE ≤p 2-Clique you only need to *supply* the 2k-clique (a separate component,
  guaranteed complete and guaranteed disjoint from G), leaving the k-clique requirement to be exactly
  CLIQUE. The split construction is both more complex and buggy — split copies u_i', u_j' are joined
  only to original neighbours, not to each other (so no 2k-clique forms), and even if it did the
  result overlaps the k-clique, violating vertex-disjointness. Also noted the k > |V| binary-k guard
  (adding 2k vertices could be exponential; k > |V| ⇒ trivial non-instance). Lesson captured: a
  fixed-size disjoint-gadget clause is free — append it as its own component.
