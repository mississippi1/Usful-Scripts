# Exam moed A (Solution-2) — Question 8 (study notes)

Source exam: `Exam_moed_A_Solution-2.pdf` (⚠ not located in the repo's `Complexity/2017-2025 Exams/`
folder as of this writing — filename taken from the user; rename this doc if it maps to a tracked exam).

## Q8 (12 pts)

L = { ⟨G,k⟩ : G is an undirected graph, k ≥ 1 an integer **given in unary**, ⟨G,k⟩ ∈ VC and ⟨G,k⟩ ∈ IS }.

Classify L among: P / NP-complete / PSPACE-complete.

Definitions used:
- VC = { ⟨G,k⟩ : G has a vertex cover of size ≤ k }.
- IS = { ⟨G,k⟩ : G has an independent set of size ≥ k }.

**Answer: NP-complete.**

### Membership in NP
Certificate = a pair: a vertex cover C with |C| ≤ k **and** an independent set I with |I| ≥ k. Both
are poly-size; verifying "C covers every edge, |C| ≤ k" and "I has no internal edge, |I| ≥ k" is
poly-time. ✓

### NP-hardness — reduce VC ≤p L (add k isolated vertices)
Given a VC instance ⟨G,k⟩ with G on n vertices, output ⟨G', k⟩ where **G' = G plus k isolated
vertices** (no new edges), same parameter k.

- **(⇒)** ⟨G,k⟩ ∈ VC ⟹ τ(G') = τ(G) ≤ k (isolated vertices need no covering) ⟹ ⟨G',k⟩ ∈ VC; and the
  k new isolated vertices form an independent set of size k ⟹ α(G') ≥ k ⟹ ⟨G',k⟩ ∈ IS. Both ⟹
  ⟨G',k⟩ ∈ L.
- **(⇐)** ⟨G',k⟩ ∈ L ⟹ ⟨G',k⟩ ∈ VC ⟹ τ(G) = τ(G') ≤ k ⟹ ⟨G,k⟩ ∈ VC.

The design idea: the k isolated vertices make the **IS half trivially true**, so membership in L
collapses onto the VC condition alone.

Poly-time: adding k vertices is polynomial **because k is in unary** (input already has ≥ k symbols;
in binary this same reduction would be exponential).

---

## Issues log

Track here which parts gave trouble, and how they were resolved.

- **Q8 (must the VC→L reduction check k ≤ |V|?):** No. The reduction G' = G + k isolated vertices
  (parameter k) is correct for **every** k ≥ 1 with no side condition. Reasons: (1) the IS half can
  never fail — the k added isolated vertices are themselves an independent set of size k, so
  α(G') ≥ k regardless of how k compares to the original n = |V(G)|; this even handles the trivial
  VC instances with k ≥ n. (2) Any "well-formedness needs k ≤ #vertices" worry self-resolves: G' has
  n + k vertices, so k ≤ n + k holds by construction. (3) The unary encoding of k is what makes
  "add k vertices" polynomial. Also flagged: you cannot economize by adding k − α(G) vertices,
  since computing α(G) is itself NP-hard — a flat k isolated vertices is the right, α-oblivious
  choice. Classification: **NP-complete** (∈NP via a cover+independent-set certificate; NP-hard via
  this VC reduction).
