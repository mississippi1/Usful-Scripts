# Comp 2025 Moed B — Question 7 (study notes)

Source exam: `Complexity/2017-2025 Exams/טופס בחינה 2025 מועד ב.pdf` (מבחן מועד ב', 22.8.2025).
Official solution: `Complexity/2017-2025 Exams solutions/פתרון 2025 מועד ב.pdf`.

## Q7 (12 pts)

Prove that the following language is **NP-complete**:

  EVEN-CLIQUE = { ⟨G,k⟩ : G is an undirected graph, k is even, and there is a clique of size k in G }.

(Note: "clique of size k" = "clique of size ≥ k" here, since cliques are downward-closed — any subset
of a clique is a clique.)

**Membership (∈ NP).** Certificate = a set of k vertices; verify in poly time that it is a clique of
size k and that k is even. ✓

**NP-hardness — reduce CLIQUE ≤p EVEN-CLIQUE.** CLIQUE = { ⟨G,k⟩ : G has a clique of size ≥ k }.
Given ⟨G,k⟩ with G on n vertices:
- G' = G plus **k new vertices, each adjacent to every other vertex** — to all original vertices AND
  to each other (the k new vertices are "universal").
- k' = **2k**. Output ⟨G', 2k⟩.

Correctness:
- **Parity (the crux):** 2k is automatically even, so the output always meets EVEN-CLIQUE's "k even"
  requirement — doubling handles the parity constraint for free.
- **(⇒)** G has a clique of size ≥ k ⟹ it has one of size exactly k, say C. The k new vertices are
  adjacent to all of C and to each other, so C ∪ {k new} is a clique of size k + k = 2k in G' ⟹
  ⟨G', 2k⟩ ∈ EVEN-CLIQUE.
- **(⇐)** G' has a clique of size 2k ⟹ it uses ≤ k new vertices (only k exist) ⟹ ≥ 2k − k = k
  original vertices; edges among original vertices in G' are exactly G's edges, so those ≥ k
  originals form a clique in G ⟹ ⟨G,k⟩ ∈ CLIQUE.

Polynomial time: in CLIQUE assume WLOG k ≤ n (else trivially reject), so adding k ≤ n vertices is
polynomial — no unary encoding needed (the "k ≤ |V| rescues it" case).

---

## Issues log

Track here which parts gave trouble, and how they were resolved.

- **Q7 (is my EVEN-CLIQUE reduction correct?):** Yes. Reduction from CLIQUE: G' = G + k universal
  vertices (adjacent to all others incl. each other), k' = 2k. Verified both directions and that it
  is the hardness half of NP-completeness. Key points confirmed: (1) k' = 2k is **even by
  construction**, which is exactly what satisfies EVEN-CLIQUE's parity clause — the reason for
  doubling. (2) Forward: a k-clique in G plus the k universal vertices makes a 2k-clique. (3)
  Backward works **because only k padding vertices were added**: any 2k-clique in G' must reuse ≥ k
  original vertices, which form a clique in G (added edges only touch new vertices). (4) Polynomial
  since CLIQUE has k ≤ n WLOG, so "add k vertices" is poly with no unary needed. Two reminders to not
  lose points: state EVEN-CLIQUE ∈ NP (certificate = the k-vertex clique; NP-complete = ∈NP + NP-hard),
  and make explicit that the new vertices are **pairwise adjacent** too — otherwise C ∪ {new} would
  not be a clique.
