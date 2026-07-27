# Study guide — how to classify a language fast (P / NP-complete / PSPACE-complete)

A triage checklist for the "לאיזו מחלקה שייכת L?" items. The classification is usually decidable
from the **input type and the quantifier shape**, before thinking about any algorithm.

## Step 0 — what is the input object?

This one question eliminates most of the answer space.

| Input | Default expectation |
|---|---|
| A **TM** ⟨M⟩ | Undecidable — Rice's theorem for any non-trivial *semantic* property of L(M). Only **syntactic** facts ("M has 5 states", "M writes b on its first move") are in P |
| A **DFA** / deterministic object | **P** (often NL-complete) — emptiness, equivalence, finiteness, minimality: product construction + reachability |
| An **NFA** / regex with `*` / "for all words" | **PSPACE-complete** — universality, containment, equivalence. The subset construction is the exponential |
| A **CFG** | Membership and emptiness in **P** (CYK); equivalence and universality **undecidable** |
| A **graph / formula / set system** + "does there exist …" | **NP**, and probably NP-complete |
| A **game**, or alternating ∃∀∃ | **PSPACE-complete** |

One-line version: **determinism in the input object → P; nondeterminism in the input object →
PSPACE-complete; existential search over a combinatorial structure → NP.**

## Step 1 — rewrite the property with explicit quantifiers

Express the language as x ∈ L ⟺ ∃y (…) or ∀y (…), then ask:

1. **How big is y?** A subset, path, assignment, coloring, matching, subgraph — all O(n log n) bits,
   polynomial ⟹ NP plausible. A TM, an arbitrary-length word, a strategy tree — unbounded ⟹ not NP.
2. **How hard is checking (…) given y?** Poly-time ⟹ you have a verifier and L ∈ NP is *proved*.
   That is the membership half, usually worth 3-4 of the 12 points.

**One quantifier ⟹ NP or coNP. Alternating quantifiers ⟹ PSPACE.** ∃assignment is SAT; ∃∀∃… is TQBF;
"player 1 has a winning strategy" is alternation wearing a costume.

## Step 2 — signals pushing toward P

- **Polynomial search space.** "Is there a clique of size 3?" → O(n³) triples. Constant-size objects
  are always P.
- **Threshold is a constant or O(log n)** rather than a fraction of n. (With color coding, k-path is
  2^O(k)·poly(n), so even k = O(log n) stays polynomial.)
- **A number is encoded in unary** ⟹ pseudo-polynomial algorithms become polynomial (subset-sum,
  knapsack).
- **It reduces to the P toolbox:** reachability/BFS, shortest path, max-flow/min-cut, bipartite
  matching, MST, topological sort, 2-coloring, 2-SAT, Gaussian elimination, LP, GCD, DFA product.
- **Structural tells:** optimal substructure with polynomially many DP states; a greedy/exchange
  (matroid) property; the constraint is **local** (checkable edge-by-edge) rather than **global**.

## Step 3 — signals pushing toward NP-complete

- The phrase "**there exists a subset / subgraph / assignment / tour / partition of size ≥ k**", with
  **k given in the input in binary**.
- The constraint is **global disjointness or coverage**: "all vertices distinct", "covers every edge",
  "visits every vertex". That is exactly what defeats DP with small state.
- **It is a Karp problem in costume.** These exams rarely invent a hard problem; they dress an old
  one. See through the costume (EVEN-CLIQUE → CLIQUE, MCLIQUE → CLIQUE, "simple path of length
  ≥ n/2 − 1" → HAM-PATH) and absorb the twist with **padding**. The usual suspects: SAT/3SAT, CLIQUE,
  IS, VC, HAM-PATH/HAM-CYCLE, TSP, SUBSET-SUM/PARTITION, 3-COLOR, SET-COVER, DOMINATING SET, 3DM.

**The "2 vs 3" heuristic** catches many: 2-SAT ∈ P but 3-SAT NPC; 2-coloring ∈ P but 3-coloring NPC;
2-dimensional matching ∈ P but 3DM NPC.

**Contrast pairs worth memorizing** — the fastest classifier available:

| In P | NP-complete |
|---|---|
| Euler path (constraint on **edges**) | Hamiltonian path (constraint on **vertices**) |
| Shortest path | Longest simple path |
| 2-SAT | 3-SAT |
| 2-coloring | 3-coloring |
| Bipartite matching | 3-dimensional matching |
| Min cut | Max cut |
| MST | Steiner tree / TSP |
| Linear programming | Integer programming |
| DFA equivalence | NFA equivalence (**PSPACE**-complete) |

## Step 4 — signals pushing toward PSPACE-complete

- Quantifier **alternation**, explicit (TQBF-shaped) or implicit (two-player game, "for every input
  there is a response").
- **NFA / regex universality, containment, equivalence**; "does this NFA accept Σ*".
- A poly-space process explored over exponentially many configurations.
- Membership proof pattern: recursion of poly depth reusing space, or Savitch.

## Step 5 — if the input is a TM, switch to the computability ladder

- Non-trivial property of L(M) → **undecidable** (Rice).
- Then classify RE/coRE by quantifier shape: ∃t "M accepts w within t steps" is **RE**;
  ∀-shaped ("M never accepts", "L(M) = ∅") is **coRE**; both ∃ and ∀ over unbounded ranges usually
  lands **outside RE ∪ coRE** (prove with two reductions, from A_TM and from its complement).

## Exam meta-hints (specific to these papers)

- **The offered options are information.** If PSPACE-complete appears on the menu, some item in that
  part involves a game, an NFA, or quantifier alternation — usually exactly one does.
- **Point value signals the expected shape.** 12-14 points ⟹ both membership *and* hardness are
  wanted. 7 points ⟹ one direction, or a true/false with a short proof.
- **"המחלקה הקטנה ביותר" ("the smallest class")** means: prove membership *and* completeness.
- **Cosmetic constraints are cosmetic.** "n is even", "k is even", "exactly k" are absorbed by
  padding and never change the class — don't let them scare you off the obvious base problem.

## Traps that actually cost marks

- **Binary vs unary encoding.** SUBSET-SUM is NP-complete in binary, polynomial in unary.
- **Constant threshold vs fraction of n.** "≥ 5" is P; "≥ n/2" is NP-complete.
- **Unbounded witnesses.** "There exists a TM such that…" is not an NP certificate however natural the
  phrasing sounds.
- **Membership ≠ hardness.** A verifier proves ∈ NP and nothing more; you still owe a reduction
  **from** a known-hard problem (known-hard ≤p yours — direction matters).
- **Sounding hard ≠ being hard.** {⟨G,k⟩ : k > |V(G)|} mentions all the right nouns and is trivially
  in P.
- **Reduction direction generally.** A ≤p B means *A is no harder than B*: reducing an easy language
  into a hard one is free and proves nothing about hardness.

## Worked instances elsewhere in these notes

- `Comp 2025 summer moed A - Q9 (half-Hamiltonian path).md` — fraction-of-n threshold ⟹ NP-complete
  via HAM-PATH padding; why brute force and DP both blow up.
- `Comp 2025 moed B - Q7 (EVEN-CLIQUE).md` — parity twist absorbed by doubling.
- `Comp 2022-1 moed A - Q7-Q9 (Part III).md` — reduction-direction items, including the
  computability-vs-complexity trap.
- `Comp 2020 summer moed A - Q7-Q8 (Part III).md` — trivial reductions, and TQBF ∈ P ⟺ P = PSPACE.

---

## Issues log

Track here which parts gave trouble, and how they were resolved.

- **General (what hints in a question suggest P vs NP?):** Consolidated into the triage above. The
  headline rules: classify by **input object** first (TM → undecidable/Rice; DFA → P; NFA/regex →
  PSPACE-complete; graph/formula + "∃ structure" → NP; game/alternation → PSPACE-complete), then by
  **quantifier shape** (one quantifier ⟹ NP/coNP, alternating ⟹ PSPACE), then check the **witness
  size** and **verification cost**. Secondary tells recorded: constant or O(log n) threshold and unary
  encodings pull toward P; binary-encoded k, global disjointness/coverage constraints, and
  Karp-problem costumes pull toward NP-complete; the 2-vs-3 heuristic and the contrast-pair table are
  the fastest lookups. Traps listed: binary vs unary, constant threshold vs fraction of n, unbounded
  witnesses, confusing membership with hardness, and reduction direction.
