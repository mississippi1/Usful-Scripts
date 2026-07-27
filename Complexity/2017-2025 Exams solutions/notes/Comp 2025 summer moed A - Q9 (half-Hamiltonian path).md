# Comp 2025 summer (קיץ) moed A — Question 9 (12 pts) (study notes)

Source exam: `Complexity/2017-2025 Exams/טופס בחינה 2025 מועד א.pdf`, שאלה 9 (12 נקודות).
Official solution: `Complexity/2017-2025 Exams solutions/פתרון 2025 מועד א.pdf`, Question 9
(verified against it — the official answer is NP-complete).

## The question

Reminder given on the exam: a **simple path of length k ≥ 0** in G is a sequence (v₀, v₁, …, v_k) of
**distinct** vertices with (v_j, v_{j+1}) ∈ E(G) for every j ∈ [k−1]. So *length = number of edges =
(number of vertices) − 1*.

  L = { ⟨G⟩ : there exists a simple path in G of length ≥ n/2 − 1, where n = |V(G)| is even and positive }

Which class does L belong to: **P / NP-complete / PSPACE-complete**?

## Answer

**NP-complete.** (A "P" marking on the answer sheet is wrong — see the trap section.)

## L ∈ NP

Certificate: the path P itself, whose encoding is polynomial in |⟨G⟩| (at most n distinct vertices).
The verifier checks that n is even and positive, that P is a sequence of **distinct** vertices, that
each consecutive pair is an edge of G, and that the length is ≥ n/2 − 1 (equivalently: at least n/2
vertices). All of these are polynomial-time operations. ✓

## L is NP-hard — reduction from HAM-PATH

HAM-PATH is NP-hard (theorem from class), so a reduction HAM-PATH ≤p L suffices.

**Construction.** Given ⟨G'⟩ with n' vertices, output ⟨G⟩ where G is G' plus **n' new isolated
vertices** (no edges whatsoever). Then n := |V(G)| = 2n' — even and positive by construction — and the
threshold becomes

  n/2 − 1 = n' − 1,

which is exactly the length of a Hamiltonian path of G'.

**(⇒)** If G' has a Hamiltonian path P, it visits all n' vertices, so its length is n' − 1 = n/2 − 1,
and it is still a simple path in G. Hence ⟨G⟩ ∈ L.

**(⇐)** Suppose G has a simple path P of length ≥ n/2 − 1.
- If n' = 1: G' trivially has a Hamiltonian path (the single vertex, a path of length 0).
- Otherwise n' ≥ 2, so n/2 − 1 ≥ 1 and P contains at least one edge, hence at least two vertices.
  **The added vertices are isolated, so no path with ≥ 2 vertices can touch them** — P lies entirely
  within G'. P has ≥ n' vertices while G' has exactly n', so P uses all of them: a Hamiltonian path
  in G'. Hence ⟨G'⟩ ∈ HAM-PATH.

**Time.** Adding n' isolated vertices is polynomial in |⟨G'⟩|. ∎

## The trap: why "P" is tempting, and why it is not a small slip

The tempting thought is: *k is not part of the input here — it is pinned to n/2 − 1 by the graph
itself — so this is more restricted than LONGEST-PATH and might be easy.* Two things kill that:

- **A fixed threshold is easy; a fixed *fraction* is not.** If L demanded a path of length ≥ c for a
  **constant** c independent of n, then L ∈ P: brute-force all O(n^{c+1}) vertex tuples. What makes
  this problem hard is that the threshold **grows with n**.
- **Padding converts Hamiltonicity into any constant fraction.** Nothing is special about ½: for any
  fixed rational α ∈ (0,1], "there is a simple path of length ≥ αn − 1" is NP-complete — pad with
  n'(1−α)/α isolated vertices instead of n'. Isolated padding is precisely the tool for turning a
  *global* requirement (visit every vertex) into a *fractional* one.

And the stakes: L ∈ P together with the NP-hardness proved above would yield **P = NP**. Marking P
is not a minor error — it asserts an unproven breakthrough.

## Why brute force fails, and what "not in P" actually means here

**Framing first: "L ∉ P" is *not* known.** NP-completeness says precisely L ∈ P ⟺ P = NP. The reason
"P" is the wrong marking is that it asserts an unproven breakthrough — not that P has been ruled out.

**Brute force #1 — enumerate candidate paths.** A witness is a simple path on n/2 vertices, so
enumerate ordered sequences of n/2 distinct vertices and check adjacency:

  n · (n−1) · … · (n/2 + 1) = n!/(n/2)! = 2^Θ(n log n),

which is *worse* than exponential. At n = 100 that is 100!/50! ≈ 3·10⁹³ sequences. With a **constant**
threshold c the same algorithm enumerates only O(n^{c+1}) tuples — polynomial, because the exponent is
fixed. The whole difficulty is that here the exponent **is** n/2.

**Brute force #2 — the smart exponential (Held–Karp DP over subsets).** State
D[S][v] = "is there a simple path visiting exactly S and ending at v", with transition
D[S ∪ {u}][u] = ⋁_{v ∈ S, (v,u) ∈ E} D[S][v]; accept if D[S][v] holds for some |S| ≥ n/2. Runtime
O(2ⁿ·n²) — at n = 100 about 10³⁰, still hopeless but astronomically better than 10⁹³.

**This DP exposes the real obstruction:** the state must carry the *entire set* S, not a summary of
it, giving 2ⁿ states instead of polynomially many. "Simple" is a **global** constraint — whether the
path may be extended by u depends on the whole history of which vertices were already used, and
nothing shorter than the set itself suffices.

**Why the usual polynomial tricks fail.** Shortest path is in P thanks to optimal substructure: every
sub-path of a shortest path is shortest, so BFS/Dijkstra keep one number per vertex and never revise
it. Longest *simple* path has no such property — a longest path does not decompose into longest
sub-paths, since greedily taking a long prefix can consume vertices a globally longer path needed.
The cleanest evidence that the bookkeeping is the culprit: **longest path in a DAG is in P**
(O(V+E), DP in topological order), precisely because acyclicity makes revisiting impossible, so the
algorithm need not remember which vertices were used.

**Where the boundary really sits.** "Constant threshold ⟹ P" understates it. By **color coding**
(Alon–Yuval–Zwick), finding a simple path on k vertices takes 2^O(k)·poly(n). Hence:

- k = O(log n) ⟹ 2^O(log n)·poly(n) = **polynomial** — even a growing threshold can be easy;
- k = n/2 ⟹ 2^Θ(n), and NP-completeness says not to expect better.

So the dividing line is around k = Θ(log n), not at constants. Under ETH there is no 2^o(n) algorithm
for Hamiltonian-path-type problems, so the exponential is very likely inherent.

## Where marks are lost

The (⇐) direction has two steps that are easy to skip, and they are exactly where the official
solution spends its space:

1. Justifying that the padding vertices cannot appear in P — this is where **isolated** (not merely
   "new") is load-bearing.
2. The **n' = 1 edge case**, where the path has length 0 and the "P has ≥ 2 vertices" argument does
   not apply.

Also: state explicitly that n = 2n' is even, since L's definition *requires* an even number of
vertices — an odd-n graph is out of L regardless of its paths.

## Exam checklist for this item

- [x] Mark **NP-complete** (not P).
- [x] NP membership with an explicit verifier: path as certificate, poly-size, poly-time checks
      including "n even and positive".
- [x] Hardness from **HAM-PATH**, padding with n' **isolated** vertices so n = 2n'.
- [x] Both directions, including the isolated-vertices argument and the n' = 1 case.
- [x] State that the reduction runs in polynomial time.

---

## Issues log

Track here which parts gave trouble, and how they were resolved.

- **Q9 (which class does the "path of length ≥ n/2 − 1" language belong to — the answer sheet had P
  circled):** The marking is **wrong**; the correct answer is **NP-complete**, confirmed against the
  official solution `פתרון 2025 מועד א.pdf`. Resolution: NP membership via the path as certificate;
  NP-hardness by HAM-PATH ≤p L, padding G' (n' vertices) with n' **isolated** vertices so that
  n = 2n' and the threshold n/2 − 1 becomes exactly n' − 1, a Hamiltonian path. Source of the
  confusion identified: the threshold is not part of the input, which suggests the problem is "more
  restricted" and therefore easier — but what matters is that the threshold is a **fraction of n**
  rather than a constant. With a constant threshold c the language *would* be in P (brute force over
  O(n^{c+1}) tuples); with any fixed rational fraction α it is NP-complete by the same padding
  (n'(1−α)/α extra isolated vertices). Also flagged: L ∈ P plus this hardness would prove P = NP.
  Two proof steps not to skip in (⇐): the padding vertices are isolated so a path with ≥ 2 vertices
  cannot use them, and the n' = 1 edge case.
- **Q9 (why is the problem not in P — what goes wrong with brute force?):** See the "Why brute force
  fails" section added above. Framing corrected first: **"L ∉ P" is not known** — NP-completeness only
  gives L ∈ P ⟺ P = NP, so marking P asserts a breakthrough rather than being refuted outright.
  Two brute forces quantified: enumerating ordered sequences of n/2 distinct vertices costs
  n!/(n/2)! = 2^Θ(n log n) (≈3·10⁹³ at n = 100), while Held–Karp DP over subsets costs O(2ⁿ·n²)
  (≈10³⁰ at n = 100). The DP is the diagnostic: its state must carry the **entire visited set**,
  because "simple" is a global constraint — extendability by u depends on the whole history — so
  there are 2ⁿ states rather than polynomially many. Contrast recorded with shortest path (optimal
  substructure ⟹ one number per vertex) and, most tellingly, with **longest path in a DAG, which is
  in P**: acyclicity removes the need to remember visited vertices. Refinement of the earlier
  "constant threshold ⟹ P" remark: color coding gives 2^O(k)·poly(n), so thresholds up to
  k = O(log n) are still polynomial — the real boundary is around Θ(log n), and under ETH no 2^o(n)
  algorithm should be expected at k = n/2.
