# Comp 2024 summer (קיץ) moed A — full exam, Q1–Q9 (study notes)

*(Source: `Complexity/2017-2025 Exams/Comp 2024-2 moed A.pdf`, exam date 22.8.23, מועד א,
course 67521. Official solution: `Comp 2024-2 moed A solution.pdf`.
9 questions × 12 pts = 108 pts, capped at 100.)*

Shape of the exam: Q1 is a construction (NFA → DFA), Q2/Q3/Q5/Q7/Q9 are **true/false + proof**,
Q4/Q6 are **computability classification** (R / RE∖R / coRE∖R / $\overline{RE ∪ coRE}$),
Q8 is a **complexity classification** (P / NP-complete / PSPACE-complete).

**Answer key at a glance**

| Q | Answer |
|---|---|
| 1 | DFA with 4 reachable subsets; L(A) = Σ*001 |
| 2 | **Claim correct** — L(A) is infinite |
| 3 | **Claim incorrect** — flipping accept states does not complement an NFA |
| 4 | **coRE ∖ R** |
| 5 | **Claim correct** — ALL_NFA ≤m VC (mapping reductions are unbounded) |
| 6 | **R** — the language is **empty** |
| 7 | **Claim correct** — POINT-SAT ∈ P, so SAT ≤p POINT-SAT ⇒ P = NP |
| 8 | **NP-complete** |
| 9 | **Claim correct** — NPC is closed under AtLeastTwo |

---

## Q1 (12 pts) — determinize the NFA

Given the NFA A over Σ = {0,1}: q₀ has a self-loop on 0 and 1, and
q₀ --0--> q₁ --0--> q₂ --1--> q₃, with q₃ the only accepting state.

So **L(A) = Σ*001** — all words ending in `001`.

**Subset construction.** Start from {q₀} and close under δ:

| subset | on 0 | on 1 | accepting? |
|---|---|---|---|
| {q₀} (start) | {q₀,q₁} | {q₀} | no |
| {q₀,q₁} | {q₀,q₁,q₂} | {q₀} | no |
| {q₀,q₁,q₂} | {q₀,q₁,q₂} | {q₀,q₃} | no |
| {q₀,q₃} | {q₀,q₁} | {q₀} | **yes** |

Only 4 of the 2⁴ subsets are reachable. A subset is accepting iff it contains q₃.

**Sanity check on the semantics of the states:** {q₀} = "suffix so far is not a prefix of 001",
{q₀,q₁} = "last letter is 0", {q₀,q₁,q₂} = "last two letters are 00", {q₀,q₃} = "just read 001".
Note {q₀,q₁,q₂} on 0 stays put — reading `000` still leaves you with a usable `00` suffix,
which is exactly the nondeterministic "when do I start the 001 pattern?" guess being collapsed.

---

## Q2 (12 pts) — long word ⇒ infinite language (NFA pumping)

A is an NFA with **n states**, and it is given that some **w ∈ L(A) with |w| > n**.
Claim: L(A) is infinite.

**Answer: the claim is correct.**

**Proof.** Let w = σ₁σ₂⋯σ_k with k = |w| > n, and fix an accepting run
r = q₀, q₁, …, q_k (q_i is the state after reading σ₁⋯σ_i, q_k ∈ F). The run touches
**k + 1 > n + 1 > n states-with-multiplicity**, but the NFA has only n distinct states, so by
pigeonhole there are indices 0 ≤ i < j ≤ k with **q_i = q_j**.

Write w = x·y·z with x = σ₁⋯σ_i, y = σ_{i+1}⋯σ_j, z = σ_{j+1}⋯σ_k. Since i < j we have
**|y| = j − i ≥ 1**. The loop from q_i back to q_j = q_i can be traversed any number of times, so
for every t ≥ 1 the word x·yᵗ·z has an accepting run, i.e. **x yᵗ z ∈ L(A)**, and
|x yᵗ z| = k + (t−1)(j−i) strictly increases with t. Infinitely many distinct words ⇒ **L(A) is infinite**. ∎

**Why the hypothesis |w| > n and not |w| ≥ n:** with |w| = n the run has n+1 states, which
already forces a repeat — so the claim holds a fortiori. The exam's bound is just the safe one.

**ε-transitions caveat.** The pigeonhole above is applied to the states at the **k+1 letter
boundaries** (after reading 0, 1, …, k letters), not to every state of the transition path. That
way the pumped block y is guaranteed non-empty even if the NFA has ε-moves — a repeat found on an
ε-cycle would pump *nothing*. Always index the run by letters consumed.

---

## Q3 (12 pts) — flipping accepting states of an NFA

For an NFA A, define A_mirror by swapping accepting and non-accepting states.
Claim: L(A_mirror) = Σ* ∖ L(A) for every NFA A.

**Answer: the claim is incorrect.**

This complementation trick works for a **complete deterministic** automaton, where every word has
**exactly one** run, so the run either ends in F or ends in Q∖F. An NFA can have **several runs on
the same word**, and the word is accepted if *at least one* run ends in an accepting state. If a
word has one run ending in F and another ending in Q∖F, it is in **both** L(A) and L(A_mirror).

**Counterexample (the official one).** Σ = {1}; Q = Q₀ = {q₁,q₂} (both are start states);
F = {q₁}; δ(q,1) = {q} for every q — i.e. two disjoint self-loops. Every word 1ᵏ has exactly two
runs, one staying at q₁ and one staying at q₂. Hence L(A) = Σ*. Flipping to F' = {q₂} gives
L(A_mirror) = Σ* as well, not ∅ = Σ* ∖ L(A). ∎

**Second counterexample (missing transitions, not multiple runs).** Take A with a single state q₀
that is both start and accepting, and no transitions at all. Then L(A) = {ε}. In A_mirror, q₀ is
non-accepting, so L(A_mirror) = ∅ ≠ Σ* ∖ {ε}. Here the failure comes from **incompleteness**
(a dead-end run rejects but its "flip" does not accept), which is the other half of why the DFA
proof needs a *complete* DFA.

**Takeaway:** complementation of an NFA requires determinizing first (subset construction, up to
exponential blow-up) and *then* flipping — the reason ALL_NFA is hard while ALL_DFA is easy.

---

## Q4 (12 pts) — disjointness of two recognized languages

L = { ⟨M₁, M₂⟩ : M₁, M₂ are TMs with the same input alphabet s.t. **L(M₁) ∩ L(M₂) = ∅** }

**Answer: L ∈ coRE ∖ R.**

### L ∈ coRE

We recognize the **complement** L̄ = { ⟨M₁,M₂⟩ : ∃x, both M₁ and M₂ accept x }.
The witness "∃x accepted by both" is a single existential over a semi-decidable condition, so
**dovetail**: for i = 0, 1, 2, …, run *every* x ∈ Σ* with |x| ≤ i on both M₁ and M₂ for at most
i steps each; accept as soon as some x is accepted by both within the budget. Otherwise go to i+1.

Correctness: if some x is accepted by both, take i = max(|x|, t₁, t₂) where t₁,t₂ are the accepting
times; iteration i finds it. Conversely the machine only accepts when it has actually witnessed a
common accepted x. So L̄ ∈ RE, i.e. **L ∈ coRE**.

### L ∉ RE (hence L ∉ R)

Reduce **NE_TM** = { ⟨M⟩ : L(M) ≠ ∅ } to **L̄**. NE_TM ∈ RE∖R, and crucially **NE_TM ∉ coRE**.

**Construction.** f(⟨M⟩) = ⟨M, M_all⟩, where M_all is a TM with the *same input alphabet* as M
whose initial state is also its accepting state (so it accepts immediately, L(M_all) = Σ*).
Computable: copy ⟨M⟩ and emit a fixed-shape M_all over M's alphabet.

**Correctness.** L(M) ∩ L(M_all) = L(M) ∩ Σ* = L(M), so
⟨M⟩ ∈ NE_TM ⟺ L(M) ≠ ∅ ⟺ L(M) ∩ L(M_all) ≠ ∅ ⟺ ⟨M, M_all⟩ ∈ L̄.

So NE_TM ≤m L̄. If L̄ were in coRE then NE_TM would be in coRE — false. Hence **L̄ ∉ coRE**,
i.e. **L ∉ RE**. Combined with L ∈ coRE: **L ∈ coRE ∖ R**. ∎

**Equivalent route (same content, other source language):** Ā_TM ≤m L via
f(⟨M,w⟩) = ⟨M', M'⟩ where M' on any input x simulates M on w and accepts iff M accepts w
(so L(M') = Σ* or ∅). Then L(M') ∩ L(M') = ∅ ⟺ M does not accept w. Since Ā_TM ∉ RE, L ∉ RE.
Watch the direction: reduce the **non-RE** language into L to kill RE-ness, and the **non-coRE**
language into L̄ — mixing these up is the classic sign-error here.

---

## Q5 (12 pts) — ALL_NFA ≤m VC

Claim: there is a **mapping reduction** from ALL_NFA = { ⟨A⟩ : A is an NFA with L(A) = Σ* }
to **VC** = { ⟨G,k⟩ : G has a vertex cover of size k }.

**Answer: the claim is correct.**

The bait is that ALL_NFA is **PSPACE-complete** and VC is only **NP-complete**, so "the target is
easier than the source, impossible". That reasoning would apply to **≤p** (poly-time reductions),
but the claim uses **≤m**, a *mapping reduction with no resource bound* — just a computable
function (Definition 2 on the formula sheet).

**Key principle.**
> If A is **decidable** and B is **non-trivial** (B ≠ ∅ and B ≠ Σ*), then **A ≤m B**.

The reduction is allowed to *solve* A outright and emit a canned answer.

**Construction.** ALL_NFA ∈ PSPACE ⊆ R, so it is decidable. Let G be the triangle:
V = {1,2,3}, E = {{1,2},{2,3},{3,1}}. Its minimum vertex cover has size 2 (any single vertex misses
the opposite edge; {1,2} covers everything). Define

  f(⟨A⟩) = ⟨G, 2⟩ if ⟨A⟩ ∈ ALL_NFA, and f(⟨A⟩) = ⟨G, 1⟩ otherwise.

**Correctness.** ⟨G,2⟩ ∈ VC and ⟨G,1⟩ ∉ VC, so ⟨A⟩ ∈ ALL_NFA ⟺ f(⟨A⟩) ∈ VC.

**Computability.** Decide ⟨A⟩ ∈ ALL_NFA (possible since ALL_NFA ∈ R — e.g. determinize and check
for a reachable non-accepting subset, or Savitch-style in poly space), then print one of two
constant strings. Total: computable. ∎

**The general lemma worth memorizing.** Under ≤m, *every* decidable language reduces to *every*
non-trivial language, and *every* language reduces to Σ* or ∅ vacuously fails (those are the two
trivial ones — no yes-instance or no no-instance to map to). So ≤m questions between two
**decidable** languages are always "true, trivially". Complexity separations only bite once the
reduction is **resource-bounded** (≤p, ≤_L).

---

## Q6 (12 pts) — "accepts σσ in one step but does not halt on σσσσ"

L = { ⟨M⟩ : M is a TM and **there exists a letter σ in M's input alphabet** such that
M accepts σσ **in one step** but **does not halt** on σσσσ }

**Answer: L ∈ R — because L = ∅.**

**Proof that L = ∅.** The machine's *first* step is determined by (q₀, symbol under the head at
time 0) = (q₀, **first input letter**). On input σσ the first letter is σ; on input σσσσ the first
letter is **also σ**. The two computations therefore take the *identical* first step.

So if M accepts σσ in one step, then either q₀ = q_accept, or δ(q₀,σ) = (q_accept, γ, d). In either
case M **accepts every word beginning with σ within one step** — in particular it accepts σσσσ in
at most one step, so it **halts** on σσσσ.

Hence for every ⟨M⟩ and every σ, at least one of the two conditions fails: either M does not accept
σσ in one step, or M halts on σσσσ. No ⟨M⟩ satisfies the definition, so **L = ∅ ∈ R**
(the machine that rejects everything decides it). ∎

> **Full treatment of this trap family:** `Study guide - empty-language traps (when a machine
> property is unsatisfiable).md` — the bounded-computation contradiction used here, the
> `L(M) ∈ coRE ∖ R` contradiction from Comp 2025-2026 moed A Q5, and the link to Rice's
> non-triviality hypothesis.

**Why this is the trap.** The question is *dressed up* as a coRE-flavoured classification: the
"does not halt on …" clause looks like Ā_TM/HALT-bar, and the reflex is to answer coRE∖R and start
building a reduction. But a one-step computation **cannot see past the first tape cell**, so the
"σσ vs σσσσ" distinction is invisible to it and the two clauses become contradictory. Always check
whether a bounded-step condition can actually distinguish the two inputs before reaching for Rice
or a reduction — and remember that ∅ and Σ* are decidable no matter how exotic the wording is
(Rice's theorem does not apply here at all: the property is **syntactic** (about δ and step counts),
not semantic).

---

## Q7 (12 pts) — POINT-SAT

A *point assignment* is (a₁,…,a_n) ∈ {0,1}ⁿ with **exactly one** a_i = 1 and all other a_j = 0.
(So (0,1,0,0) is a point assignment; (0,1,1,0) and (0,0,0,0) are not.)

POINT-SAT = { ⟨φ⟩ : φ is a Boolean formula with a satisfying point assignment }

Claim: if **SAT ≤p POINT-SAT** then **P = NP**.

**Answer: the claim is correct.**

**Step 1 — POINT-SAT ∈ P.** A formula φ over n ≥ 1 variables has **exactly n point assignments**
(one per choice of the unique index i set to 1) — the search space is *linear*, not 2ⁿ. Algorithm:
for i = 1,…,n build ā^i (the i-th point assignment) and call the poly-time evaluator/verifier
V(φ, ā^i) that checks whether an assignment satisfies φ; accept iff some call accepts.

*Complexity:* each ā^i is written in poly time, each evaluation is poly time, and there are n ≤ |φ|
calls ⇒ poly time overall. *Correctness:* accepts iff some point assignment satisfies φ, which is
the definition. So **POINT-SAT ∈ P**.

**Step 2 — SAT ≤p POINT-SAT ⇒ P = NP.** Let A ∈ NP be arbitrary. SAT is NP-hard, so A ≤p SAT.
Assuming SAT ≤p POINT-SAT and using **transitivity of ≤p**, we get A ≤p POINT-SAT. Since
POINT-SAT ∈ P and P is **closed under ≤p** (Theorem 5), A ∈ P. As A was arbitrary, NP ⊆ P;
P ⊆ NP always, so **P = NP**. ∎

**The moral.** "Restricting the assignment space to something polynomially small makes the problem
easy" — the NP-hardness of SAT lives entirely in the **exponential** assignment space. Compare
2-SAT ∈ P (structural restriction) versus this one (search-space restriction). And note the claim is
an *implication*, not an assertion that the reduction exists: SAT ≤p POINT-SAT is in fact equivalent
to P = NP (open), but proving the stated implication does not require settling that.

---

## Q8 (12 pts) — VC **and** IS of the same size k

L = { ⟨G,k⟩ : G is an undirected graph, k ≥ 1 an integer **given in unary**,
⟨G,k⟩ ∈ VC **and** ⟨G,k⟩ ∈ IS }

i.e. G has a vertex cover of size k *and* an independent set of size k.

**Answer: L is NP-complete.**

### L ∈ NP

L = VC ∩ IS, both in NP, and **NP is closed under intersection** — so L ∈ NP.
(Directly: the certificate is a pair (C, S) with |C| = |S| = k, C a vertex cover and S an
independent set; both checks are poly-time, and the certificate is poly-size because k is unary.)

### L is NP-hard: VC ≤p L

**Construction.** On input ⟨G,k⟩ for VC with G = ⟨V,E⟩:

- If **k > |V|**: ⟨G,k⟩ ∈ VC trivially (V itself is a cover of size ≤ k). Output the fixed
  yes-instance ⟨Ĝ, 1⟩ where Ĝ = ⟨{1}, ∅⟩ is a single isolated vertex — it has both a vertex cover
  of size 1 and an independent set of size 1, so ⟨Ĝ,1⟩ ∈ L.
- Otherwise **k ≤ |V|**: output ⟨G′, k⟩ where G′ = ⟨V ∪ V″, E⟩ adds **k new isolated vertices**
  V″ (disjoint from V, |V″| = k). Same edge set.

**Complexity.** Comparing k to |V| is poly-time. Adding k ≤ |V| isolated vertices costs
O(k·log²|V|) = O(|V|·log²|V|) bits of writing — polynomial in |⟨G,k⟩| (and k unary keeps the
output size polynomial).

**Correctness** (the interesting case k ≤ |V|):

- *Vertex cover is unchanged.* V″ is isolated and contributes nothing to covering E, so if C ⊆ V′
  is a vertex cover of G′ then C ∩ V is a vertex cover of G of size ≤ |C|. Conversely a cover of G
  is a cover of G′. Hence **G′ has a VC of size k ⟺ G has a VC of size k**.
- *Independent set is now free.* V″ is an independent set of G′ of size exactly k. So
  **⟨G′,k⟩ ∈ IS always**.

Therefore ⟨G,k⟩ ∈ VC ⟺ ⟨G′,k⟩ ∈ VC and ⟨G′,k⟩ ∈ IS ⟺ ⟨G′,k⟩ ∈ L. ∎

**Why the conjunction doesn't make it easier.** Tempting reasoning: "the complement of a vertex
cover is an independent set, so the two conditions collapse." What is true is
minVC(G) = |V| − maxIS(G), so ⟨G,k⟩ ∈ L ⟺ **minVC ≤ min(k, |V| − k)**. That is still a vertex-cover
question — for k ≤ |V|/2 it is *exactly* VC — so it stays NP-hard. The reduction above just
sidesteps the arithmetic by padding with isolated vertices that donate the independent set for free.

**Why "k in unary" is stated.** It keeps the certificate and the padded graph polynomial in the
input length; it does *not* make the problem easy (unlike, say, SubsetSum with unary numbers,
where the pseudo-polynomial DP kicks in). Here k ≤ |V| always after the trivial case, so it changes
nothing about hardness.

---

## Q9 (12 pts) — the AtLeastTwo operator

Given Σ and a fresh letter # ∉ Σ, for L ⊆ Σ* define

AtLeastTwo(L) = { w₁#w₂#…#w_n : n ≥ 2, w_i ∈ Σ*, and **there exist two distinct indices**
1 ≤ i < j ≤ n with w_i ∈ L and w_j ∈ L }

Claim: if **L ∈ NP-Complete** then **AtLeastTwo(L) ∈ NP-Complete**.

**Answer: the claim is correct — NPC is closed under the AtLeastTwo operator.**

### Direction 1: L ∈ NP ⇒ AtLeastTwo(L) ∈ NP

*Verifier argument.* On input w₁#…#w_n, guess the indices i < j (O(log n) bits each) together with
the NP-certificates c_i, c_j for w_i ∈ L and w_j ∈ L, and run L's verifier twice. Poly-size
certificate, poly-time check ⇒ AtLeastTwo(L) ∈ NP.

*Closure argument (the official one).* One checks the identity

  AtLeastTwo(L) = (Σ*·#)* · L · {#} · (Σ*·#)* · L · (#·Σ*)*

The blocks (Σ*·#)*, {#}, (#·Σ*)* are **regular** ⊆ P ⊆ NP, and L ∈ NP by assumption, so
AtLeastTwo(L) is a finite **concatenation** of NP languages — and NP is closed under concatenation
(formula sheet, `L₁·L₂` column ✓). Hence AtLeastTwo(L) ∈ NP.

### Direction 2: L NP-hard ⇒ AtLeastTwo(L) NP-hard

The reduction is **w ↦ w#w**. It is computable in poly time (copy the input once with a separator).

Correctness: w#w is a valid n = 2 encoding, and the only candidate index pair is (i,j) = (1,2).
So w#w ∈ AtLeastTwo(L) ⟺ w ∈ L and w ∈ L ⟺ **w ∈ L**.

Hence L ≤p AtLeastTwo(L). If L is NP-hard, then for every A ∈ NP, A ≤p L ≤p AtLeastTwo(L), so
AtLeastTwo(L) is NP-hard.

Both directions together: **AtLeastTwo(L) ∈ NP-Complete**. ∎

**Why "at least two" instead of "at least one" changes nothing.** The duplication trick w ↦ w#w
supplies both witnesses at once. The same argument shows closure for "at least k" (map w ↦ w#w#…#w,
k copies) for any fixed k. What *would* break the pattern is a **counting/threshold** condition
depending on n (e.g. "a majority of the blocks are in L"), where the certificate is no longer a
constant number of L-witnesses.

---

## Cross-question themes

1. **Read the reduction's resource bound.** Q5 (≤m, unbounded — so any decidable source reduces to
   any non-trivial target) versus Q7/Q8/Q9 (≤p, where class separations actually bite). The single
   most repeated trap in this course.
2. **Bounded-step conditions are syntactic, not semantic.** Q6's "in one step" collapses the whole
   question; Rice's theorem is irrelevant, and the answer is the degenerate ∅ ∈ R.
3. **Nondeterminism is not symmetric.** Q3: multiple runs (and dead ends) break the flip-the-accept-states
   complementation that works for complete DFAs.
4. **Pigeonhole on letter boundaries.** Q2's NFA pumping must index the run by letters consumed,
   or ε-cycles give an empty pump.
5. **Padding gives a free half of a conjunction.** Q8: isolated vertices donate the independent set
   without touching the vertex cover, so the conjunctive language stays exactly as hard as VC.

---

## Issues log

*(No student issues logged yet for this exam — entries go here when a specific question is
re-asked or misanswered, per the repo convention: question number, one-line summary of the
confusion, and how it was resolved.)*
