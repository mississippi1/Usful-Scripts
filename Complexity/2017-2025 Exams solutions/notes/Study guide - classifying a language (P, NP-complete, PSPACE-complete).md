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
- **The language's *name* is not evidence — read the definition.** "**distance** from s to t is at
  least k" means *no short path exists* (a ∀ condition, **NL**-complete via NL = coNL), while "there
  **exists** a simple path of length ≥ k" is the Hamiltonian family (**NP**-complete). Comp 2022-2
  moed A calls the first one *LongPath* and it is NL-complete; Q8 of the same exam, *LargeCycle*, is
  genuinely NP-complete because its certificate must prove all vertices **distinct**.
- **Check your answer against your own membership proof.** If you can put L in NL (or P), then
  marking it NP-complete asserts P = NP. A class marking that contradicts a membership argument you
  can produce yourself is self-refuting.
- **Reduction direction generally.** A ≤p B means *A is no harder than B*: reducing an easy language
  into a hard one is free and proves nothing about hardness.

## Why "short is easy, long is hard" — and why min-vs-max is the wrong axis

A frequent misreading of the contrast-pair table is "minimisation is easy, maximisation is hard".
**False:** max-flow, maximum matching and maximum spanning tree are all in P, while TSP is a
*minimisation* and NP-hard. The real axis is different.

**Minimising makes "simple" free; maximising makes it binding.** Both shortest and longest path are
really "find a **simple** path", and the difference is who enforces simplicity:

- **Shortest path:** the constraint enforces itself. A walk that repeats a vertex contains a cycle,
  and deleting the cycle gives a *shorter* walk — so the optimum is automatically simple. BFS/Dijkstra
  may roam freely over walks, an unconstrained and well-behaved space.
- **Longest path:** the constraint fights the objective. Repetition makes a walk *longer*, so without
  simplicity the answer is infinite. Every step must remember which vertices are already used — that
  memory is the 2ⁿ DP state.

**One line: shortest path is easy because "simple" is not a constraint there; longest path is hard
because "simple" is the whole problem.**

Three tests confirming it is the constraint and not the direction:

1. **Longest path in a DAG is in P** — same maximisation, but acyclicity makes repetition impossible,
   so the constraint is free again.
2. **Longest *walk* is trivial** — drop simplicity and the problem collapses. All difficulty lived in
   that one word.
3. **Shortest *simple* path with negative cycles is NP-hard** (reduction from HAM-PATH). Minimisation
   no longer self-enforces simplicity once repeating can be profitable, and the minimisation problem
   immediately becomes as hard as the maximisation one.

Why the algorithms then break:

- **Optimal substructure dies.** Dijkstra works because every sub-path of a shortest path is shortest,
  so one number d(v) summarises all history at v. For longest simple paths, whether a prefix is good
  depends on **which vertices it burned** — two equal-length prefixes are not interchangeable, so the
  state cannot compress from a *set* to a *number*: n states become 2ⁿ.
- **Local optimality certificates die.** Shortest path has a dual proof of optimality — potentials d
  with d(u) + w(u,v) ≥ d(v) on every edge (LP duality) — verifiable by checking m inequalities, no
  search. Longest simple path has no known local certificate; proving *no* longer path exists is
  coNP-hard. A problem tends to be in P when **both** "there is one" and "there is none" have short
  proofs; long-path has only the first.

Higher-level frame: min-cut is easy and max-cut is hard because cut capacity is **submodular**, and
submodular *minimisation* is polynomial while submodular *maximisation* is NP-hard. Similarly, greedy
works exactly on structures with a matroid exchange property.

Finally, do not over-apply the rule — **"long" is not always hard**: longest increasing subsequence,
longest common subsequence, and diameter (the longest shortest-path) are all in P. None carries a
global disjointness requirement. What makes long-path hard is not length but "use each vertex at most
once".

## The s-t path family on one page (L / NL / NP)

Four exam items, nearly identical wording, four different answers. Read the **bound** and the
**quantifier**, never the name:

| Language | The condition | Class | Why |
|---|---|---|---|
| ST-Conn₂₀₂₂ — ∃ path s→t of length ≤ **2022** | constant bound | **L** | depth-bounded DFS: recursion depth O(1), each frame one vertex + one index ⟹ O(log n) |
| PATH — ∃ path s→t (unbounded) | bound is \|V\| | **NL-complete** | depth \|V\| kills deterministic log space; guess the walk step-by-step with a counter |
| LongPath — **distance** s→t ≥ k | universal: no short path exists | **NL-complete** | complement is bounded reachability ∈ NL, then NL = coNL |
| ∃ **simple** path s→t of length ≥ k | existential + distinctness | **NP-complete** | witness must prove no repeated vertex: Θ(n) bits, not O(log n) |

Two reusable rules fall out:

- **Upper bounds (≤ k) are cheap, lower bounds (≥ k) are expensive.** For "≤ k" simplicity is free
  (chopping cycles only shortens a walk), so you may search over walks. For "≥ k" simplicity is the
  entire difficulty.
- **A constant bound collapses the depth.** Any "≤ c" for fixed c makes bounded DFS run in
  O(c · log n) = O(log n) space. The branching factor |V| is spent in **time** (|V|^c, still
  polynomial), never in space — the classic wrong estimate is |V|·log|V|.

## Reduction type must be strictly weaker than the class, or completeness collapses

**The mechanism (constant-output lemma, any resource bound r):** if A is decidable within resource
bound r and B is any non-trivial language (B ≠ ∅, Σ*), then A ≤_r B — decide A within budget r, then
print one of two hard-coded constants (printing is free; it never touches the work tape). This one
fact is the source of every degenerate completeness result below.

Consequence: under **≤p**, every non-trivial B (however easy) becomes simultaneously "P-hard",
"NL-hard", "L-hard" — P is closed under ≤p, and the lemma only needs A ∈ P. Under **≤L**, the same
collapse happens one class lower: every non-trivial B becomes "L-hard" in the same vacuous sense.

### Class × reduction-type grid

| Class | Example under ≤L | Verdict | Example under ≤p | Verdict |
|---|---|---|---|---|
| L | "EVEN (even-length strings) is L-complete under ≤L" | **degenerate-true** — any non-trivial B ∈ L absorbs all of L this way | "REACH-DAG (∈ L) is L-complete under ≤p" | **degenerate-true** — even makes it "P-complete" too |
| NL | "PATH is NL-complete under ≤L" | **correct, meaningful** — the standard theorem | "PATH is NL-complete under ≤p" | **degenerate-true** — any non-trivial B ∈ P qualifies the same way |
| P | "CVP is P-complete under ≤L" | **correct, meaningful** — the textbook definition of P-completeness | "CVP is P-complete under ≤p" | **degenerate-true** — true of any non-trivial P language |
| NP | "SAT is NP-complete under ≤L" | **correct, meaningful** (stronger than usual — Cook–Levin's reduction is log-space computable) | "SAT is NP-complete under ≤p" | **correct, meaningful** — Cook–Levin |
| PSPACE | "TQBF is PSPACE-complete under ≤L" | **correct, meaningful** (Stockmeyer–Meyer's reduction is log-space computable) | "TQBF is PSPACE-complete under ≤p" | **correct, meaningful** — standard |

**Reading the pattern:** ≤p is a meaningful reduction only for NP and PSPACE (classes not obviously
inside P). For L, NL, P themselves, ≤p is useless — drop to ≤L. Even ≤L is already too strong for L
itself; genuine L-completeness needs something weaker still (AC⁰/NC⁰ reductions), which is why
"L-complete" problems are rarely defined in an intro course at all.

### The three verdict buckets, with genuine examples of each

The grid above is all "true" in some sense (meaningful or degenerate) — none of those cells are
*false* or *open*. Real examples of all three buckets require crossing an unsettled class boundary,
or hitting a genuine impossibility:

| Claim | Verdict | Why |
|---|---|---|
| SAT is NP-complete under ≤p | **CORRECT** | Cook–Levin, unconditional |
| A_TM is NP-hard under ≤p (i.e. NP-complete) | **INCORRECT, provably** | A_TM is undecidable, NP ⊆ R — pure computability gap, no complexity assumption needed (same shape as `A_TM ≤p SAT` in `Comp 2022-1 moed A - Q7-Q9 (Part III).md`) |
| SAT is NL-complete under ≤L | **UNKNOWN** | Hardness half is unconditionally true (SAT is NL-hard by transitivity through NP-hardness); membership — SAT ∈ NL — is equivalent to **NP = NL**, believed false, unproven |
| 2-SAT is NP-hard under ≤p | **UNKNOWN**, not "false" | 2-SAT ∈ P, so NP-hardness would give **P = NP**; believed false but, like `TQBF ∈ P`, never disproven |

**The line between "incorrect" and "unknown":** incorrect requires an actual proof (a computability
gap, a hierarchy theorem, a closure argument under a known-true inclusion). Unknown is everything that
would only be settled by resolving P vs NP, L vs NL, etc. — even when the answer is all but certain.

## Class-vs-class reductions: C1 ≤_r C2 for C1,C2 ∈ {L,NL,P,NP,PSPACE,EXP,EXPSPACE}

Reading "C1 ≤_r C2" (r ∈ {L, p}) as: every language in C1 reduces via ≤_r to some language in C2 —
equivalently, C1 ⊆ closure_r(C2), where closure_r(C2) is everything that ≤_r-reduces into C2.

**Two facts decide every case.**

*Fact 1 (real chain, all proven):* L ⊆ NL ⊆ P ⊆ NP ⊆ PSPACE ⊆ EXP ⊆ EXPSPACE. Whenever the source
sits at or before the target in this chain, the statement is **TRUE** automatically, by the identity
reduction.

#### Proof that "smaller into bigger" is always true

The statement C1 ≤_r C2 is: *for every* A ∈ C1, *there exists* B ∈ C2 with A ≤_r B. The existential is
the whole game — you get to choose the target language.

*Step 1 (reflexivity).* id(x) = x is computable by a log-space transducer: read-only input tape,
write-only output tape, copy symbols as the head sweeps right, O(1) work space. And x ∈ A ⟺ id(x) ∈ A
by inspection. So **A ≤L A and A ≤p A for every language A**, with no assumptions on A.

*Step 2 (apply containment).* Let A ∈ C1. Since C1 ⊆ C2, A ∈ C2. Take B := A. Then B ∈ C2 and
A ≤_r B. ∎

So the real theorem is: **if C1 ⊆ C2 then C1 ≤_r C2, for any reduction notion whose function class
contains the identity** (≤L, ≤p, ≤m, ≤T, AC⁰ — i.e. all of them). "Smaller into bigger" is a fact about
*inclusions* wearing a reduction as a costume; every ounce of content is in the six chain proofs:

| Inclusion | Argument |
|---|---|
| L ⊆ NL | A deterministic machine is a nondeterministic one that never branches. |
| NL ⊆ P | Config graph has 2^O(log n) = poly(n) nodes; BFS it in poly time. |
| P ⊆ NP | Ignore the certificate. |
| NP ⊆ PSPACE | Enumerate all 2^poly certificates, **reusing** the same poly space each time. |
| PSPACE ⊆ EXP | Only 2^O(poly) configurations exist ⟹ a halting poly-space machine runs in 2^O(poly) time. |
| EXP ⊆ EXPSPACE | A machine running in time t touches at most t cells. |

*Two caveats.*

1. The identity reduction dodges the non-triviality trap that the constant-output lemma (Fact 2 below)
   suffers: it never emits a hard-coded string, so it works even for B = ∅ or Σ*.
2. **Watch the quantifier order.** If the question instead asks for a *single* B ∈ C2 that *all* of C1
   reduces to, B := A is illegal (B must be fixed before A is quantified). That version asks for a
   C1-hard language inside C2, i.e. essentially a C1-complete problem under ≤_r — true for NL (PATH),
   P (CVP), NP (SAT), PSPACE (TQBF), EXP; but for C1 = L under ≤L there are no known ≤L-complete
   problems, exactly the "reduction as strong as the class" collapse discussed above. Under ≤p, any
   non-trivial language in L works via the constant-output lemma.

*Fact 2 (closure):* closure_L(C)=C for every class here (all closed under ≤L, unconditionally).
closure_p(C)=C for C ∈ {P,NP,PSPACE,EXP,EXPSPACE} (standard). But **closure_p(L) = closure_p(NL) = P**
— for any non-trivial B ∈ L (or NL), the constant-output lemma lets every A ∈ P reduce to B via ≤p
(decide A in poly time, print a constant), and NL ⊆ P means the closure can't overshoot P. So ≤L and
≤p give the SAME verdict everywhere except when the **target is L or NL**, where ≤p is strictly more
generous — it really asks "is source ⊆ P?" instead of "⊆ L (or NL)?".

**Only four direct strict separations are proven** (hierarchy theorems); every other adjacent pair in
the chain is individually open:
1. L ⊊ PSPACE (space hierarchy)
2. NL ⊊ PSPACE (Savitch + space hierarchy)
3. P ⊊ EXP (time hierarchy / direct diagonalization)
4. PSPACE ⊊ EXPSPACE (space hierarchy)

Everything chainable from these (strict step + plain inclusion) is also proven (e.g. L ⊊ EXP from
L ⊊ PSPACE ⊆ EXP). But L vs NL, NL vs P, P vs NP, NP vs PSPACE, PSPACE vs EXP, EXP vs EXPSPACE are
each **individually open**, even though some strictness is known to exist somewhere in the chain.

### Grid: source (rows) × target (columns), verdict for ≤L / ≤p

Source before target (upper triangle incl. diagonal): **TRUE** always, both reductions — omitted below.
Only source-after-target ("backward") cells are shown; everything else is TRUE by Fact 1.

| Source ↓ \ Target → | L | NL | P | NP | PSPACE | EXP |
|---|---|---|---|---|---|---|
| NL | ≤L UNKNOWN (L=NL?) · ≤p TRUE (NL⊆P known) | — | — | — | — | — |
| P | ≤L UNKNOWN (L=P?) · ≤p TRUE | ≤L UNKNOWN (NL=P?) · ≤p TRUE | — | — | — | — |
| NP | ≤L/≤p UNKNOWN (both reduce to "NP⊆P?") | ≤L/≤p UNKNOWN (same) | **≤L/≤p UNKNOWN — the P vs NP question itself** | — | — | — |
| PSPACE | **≤L FALSE** (L⊊PSPACE proven) · ≤p UNKNOWN (PSPACE⊆P? open) | **≤L FALSE** (NL⊊PSPACE proven) · ≤p UNKNOWN | ≤L/≤p UNKNOWN (P vs PSPACE) | ≤L/≤p UNKNOWN (NP vs PSPACE) | — | — |
| EXP | **≤L/≤p FALSE** (L⊊PSPACE⊆EXP) | **≤L/≤p FALSE** (NL⊊PSPACE⊆EXP) | **≤L/≤p FALSE** (P⊊EXP proven directly) | ≤L/≤p UNKNOWN (NP = EXP? open) | ≤L/≤p UNKNOWN (PSPACE vs EXP) | — |
| EXPSPACE | **≤L/≤p FALSE** (L⊆PSPACE⊊EXPSPACE) | **≤L/≤p FALSE** (NL⊆PSPACE⊊EXPSPACE) | **≤L/≤p FALSE** (P⊆PSPACE⊊EXPSPACE) | **≤L/≤p FALSE** (NP⊆PSPACE⊊EXPSPACE) | **≤L/≤p FALSE** (PSPACE⊊EXPSPACE proven directly) | ≤L/≤p UNKNOWN — *equivalent to P vs PSPACE* (padding) |

Note the EXPSPACE row is not trivial: EXPSPACE is the largest class here, so **every** one of its cells is
backward, and five of the six are FALSE. In particular `EXPSPACE ≤_r NP` is the **only FALSE cell in the
whole grid whose target is NP** — it does not come from an NP-specific separation (NP vs EXP is open) but
from routing NP through PSPACE: NP ⊆ PSPACE ⊊ EXPSPACE. Same trick supplies the P and L/NL cells of this
row; only `PSPACE` is refuted by the hierarchy theorem directly.

The last cell is the one to state precisely: `EXP = EXPSPACE ⟺ P = PSPACE` (pad an instance of a PSPACE
problem out to exponential length and back). So that cell is not merely "open" — it is the *same* open
problem as the `PSPACE → P` cell two rows up, which is a nice consistency check on the whole table.

### The pattern to remember

1. Source before target in the chain ⟹ always TRUE (identity reduction) — no exceptions.
2. Source after target ⟹ check whether a proven hierarchy separation lies in that gap: if yes, **FALSE**
   unconditionally (a proof, not a belief); if no, **UNKNOWN**, and name the open problem it is
   equivalent to (L=NL, NL=P, P=NP, NP=PSPACE, PSPACE=EXP, EXP=EXPSPACE).
3. ≤p only ever changes the verdict when the **target is L or NL**, and only ever makes TRUE more
   likely (never FALSE more likely) — it substitutes "source ⊆ P?" for "source ⊆ L/NL?". This is why
   NL and P (whose containment in L/NL is individually open) flip to TRUE under ≤p, while EXP — which
   is *provably* outside P — stays FALSE regardless of reduction type.

### The interval test (use this instead of comparing endpoints)

Point 2 above is the one that goes wrong under time pressure. The failure mode: see `EXPSPACE ≤_r NP`,
recall that NP vs PSPACE, PSPACE vs EXP and EXP vs EXPSPACE are all open, conclude UNKNOWN. Wrong — it
is FALSE.

**Why the instinct misfires: none of the four proven separations is an adjacent pair.** Each one jumps
over at least one class:

| Separation | Classes strictly between the endpoints |
|---|---|
| L ⊊ PSPACE | NL, P, NP |
| NL ⊊ PSPACE | P, NP |
| P ⊊ EXP | NP, PSPACE |
| PSPACE ⊊ EXPSPACE | EXP |

Not a coincidence: a hierarchy theorem compares a resource against more of the *same* resource (space vs
space, time vs time), and this chain alternates space- and time-defined classes, so the endpoints of any
hierarchy separation always have something between them. Consequence: **a proven separation can sit
inside a span whose every individual step is open.** PSPACE ⊊ EXPSPACE lives inside the span NP…EXPSPACE
even though all three steps NP|PSPACE, PSPACE|EXP, EXP|EXPSPACE are unresolved.

**The asymmetry to internalise:** separations propagate outward when the span widens (shrink the target
or grow the source and the witness language stays a witness); *openness does not*. So "the narrow
question is open" is never evidence about the wider question.

**The test.** Memorise the four separations as intervals: `[L,PSPACE] [NL,PSPACE] [P,EXP] [PSPACE,EXPSPACE]`.
For a backward item C1 ≤_r C2, form the span [C2, C1] and ask: *does some interval [X,Y] fit inside it,
i.e. C2 ⊆ X and Y ⊆ C1?* Yes ⟹ **FALSE**. No ⟹ **UNKNOWN** (name the open problem). For ≤p, first
replace an L or NL target by P (closure_p), then run the same test.

| Item | Span | Interval that fits | Verdict |
|---|---|---|---|
| EXPSPACE ≤_r NP | [NP, EXPSPACE] | [PSPACE, EXPSPACE] ✓ | **FALSE** |
| EXP ≤_r NP | [NP, EXP] | none ([P,EXP] would need NP ⊆ P) | UNKNOWN (P vs NP) |
| EXP ≤_r P | [P, EXP] | [P, EXP] ✓ | **FALSE** |
| PSPACE ≤_r P | [P, PSPACE] | none | UNKNOWN |
| PSPACE ≤p L | [P, PSPACE] | none | UNKNOWN |
| EXP ≤p L | [P, EXP] | [P, EXP] ✓ | **FALSE** |
| EXPSPACE ≤p L | [P, EXPSPACE] | [P, EXP] ✓ | **FALSE** |

One rule, both reduction types, every backward cell of the grid.

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
- **General (why is "short" easy and "long" hard?):** See the section above. The premise "minimisation
  is easy, maximisation is hard" was **rejected** — max-flow, maximum matching and maximum spanning
  tree are in P, while TSP and shortest-simple-path-with-negative-cycles are NP-hard. Correct axis
  identified: whether the **simplicity (no repeated vertex) constraint is self-enforcing**. Minimising
  deletes cycles for free, so shortest path may search over walks; maximising makes repetition
  profitable, so simplicity must be tracked explicitly — which is exactly the 2ⁿ DP state. Three
  confirming tests recorded (DAG longest path ∈ P; longest walk trivial; shortest simple path with
  negative cycles NP-hard), plus the two algorithmic mechanisms: loss of optimal substructure (a
  prefix's value depends on *which* vertices it consumed, so state cannot compress from a set to a
  number) and loss of a local/dual optimality certificate (feasible potentials for shortest path;
  nothing comparable for longest, whose complement is coNP-hard). Higher-level frame noted: submodular
  minimisation is poly while submodular maximisation is NP-hard (min-cut vs max-cut). Counterweight
  noted so the rule is not over-applied: LIS, LCS and diameter are "long" problems in P — the hardness
  comes from global disjointness, not from length.
- **General (for each complexity class and reduction type, which combinations of completeness are
  correct / incorrect / unknown?):** Full grid added above. Core mechanism identified: a
  constant-output lemma at *any* resource bound r (decide A within budget r, print a hard-coded
  constant — free, since output is write-only) makes "C-complete under ≤r" **degenerate** whenever r
  is not strictly weaker than C itself. Consequence tabulated across L, NL, P, NP, PSPACE × {≤L, ≤p}:
  ≤p degenerates completeness for L, NL, and P (any non-trivial P language becomes "NL-complete" etc.
  — the same fact already logged for PATH ≤p HAMCYCLE); ≤L is meaningful for NL, P, NP, PSPACE but
  degenerates for L itself. Separately produced clean examples of all three requested verdict buckets
  to contrast with the degenerate-but-true cells: CORRECT (SAT NP-complete under ≤p, Cook–Levin),
  INCORRECT (A_TM NP-hard under ≤p — refuted by a computability gap, no open problem needed), and
  UNKNOWN (SAT ∈ NL, equivalent to NP = NL; 2-SAT NP-hard under ≤p, equivalent to P = NP). Rule
  extracted for telling INCORRECT from UNKNOWN: incorrect requires an actual proof (computability gap,
  hierarchy theorem, closure under a known inclusion); unknown is anything gated behind an unresolved
  class-separation conjecture, however confidently believed.
- **General (prove/disprove/unknown for C1 ≤_r C2 across L, NL, P, NP, PSPACE, EXP, EXPSPACE and
  r ∈ {≤L, ≤p}):** Full grid added above (84 statements systematically resolved). Framework: C1 ≤_r C2
  ⟺ C1 ⊆ closure_r(C2). Two governing facts: (1) the real chain L⊆NL⊆P⊆NP⊆PSPACE⊆EXP⊆EXPSPACE makes
  every "source before/at target" cell TRUE via the identity reduction; (2) closure_L(C)=C for every
  class here, but **closure_p(L) = closure_p(NL) = P** — the same degenerate-collapse mechanism
  already logged for PATH ≤p HAMCYCLE and the reduction-type grid, now shown to inflate the *target*
  class rather than just the source. Only four direct proven strict separations exist (L⊊PSPACE,
  NL⊊PSPACE, P⊊EXP, PSPACE⊊EXPSPACE, all via hierarchy theorems); every other adjacent link (L vs NL,
  NL vs P, P vs NP, NP vs PSPACE, PSPACE vs EXP, EXP vs EXPSPACE) is individually **open**, even
  though the aggregate gaps are proven strict. Consequence for the grid: "backward" cells (source
  strictly after target in the chain) are FALSE only when a proven separation spans that gap
  (giving several unconditional refutations, e.g. EXP ≤_r P/NL/L all FALSE since P⊊EXP is proven and
  ≤p's target-inflation to P doesn't rescue it); otherwise UNKNOWN, each equivalent to a named open
  problem (P≤_L NL ⟺ NL=P; NP≤_r P ⟺ P=NP; PSPACE≤_r P ⟺ P=PSPACE; EXP≤_r NP ⟺ NP=EXP; etc.). Key
  corrected misconception during derivation: knowing an AGGREGATE span is strict (e.g. L⊊PSPACE, which
  spans four adjacent links) does NOT let you conclude any specific narrower sub-link (e.g. L vs NL)
  is strict — that remains fully open; only a DIRECTLY proven strict pair (or one chainable from it via
  ⊊ then ⊆) licenses a FALSE verdict.
- **Class-vs-class grid — "smaller into bigger is trivially true", why?** Asked for a general proof
  rather than the assertion. Resolved by separating the two steps: (1) the identity map is log-space
  computable and satisfies x ∈ A ⟺ id(x) ∈ A, so A ≤L A and A ≤p A for *every* language with no
  assumptions; (2) for A ∈ C1 ⊆ C2, pick the witness B := A. The general theorem is therefore
  "C1 ⊆ C2 ⟹ C1 ≤_r C2 for any reduction notion containing the identity" — a fact about *inclusions*,
  not about reductions; all the real content is in the six chain-inclusion proofs. Also recorded: the
  identity reduction avoids the non-triviality caveat that the constant-output lemma carries, and the
  ∃B∀A reading (a single B serving all of C1) is genuinely non-trivial — it asks for a C1-hard language
  inside C2. Written up under Fact 1.
- **Class-vs-class grid — the EXPSPACE row and the NP-target trap.** Two errors caught and fixed. First,
  the grid claimed EXPSPACE never appears as a source "because it is the largest class"; that is
  inverted — being largest makes *every* one of its cells backward, and five of six are FALSE. Second,
  and the more expensive one under time pressure: `EXPSPACE ≤_r NP` reads as UNKNOWN if you compare
  endpoints (NP vs PSPACE, PSPACE vs EXP, EXP vs EXPSPACE are all open), but it is FALSE via
  NP ⊆ PSPACE ⊊ EXPSPACE. Root cause identified: **none of the four proven separations is an adjacent
  pair** — each straddles at least one intermediate class, because hierarchy theorems compare a resource
  against more of the same resource while the chain alternates space and time classes. So a proven
  separation can sit inside a span built entirely from open steps. Resolved with the **interval test**
  (memorise the four separations as intervals, ask whether one fits inside the span [target, source]
  rather than comparing endpoints), which decides every backward cell for both ≤L and ≤p.
