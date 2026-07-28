# Comp 2025-2026 winter (חורף) moed A — full exam, Q1–Q8 (study notes)

*(Source: `Complexity/2017-2025 Exams/Comp 2025-2026 moed A (annotated).pdf`, exam date **6.2.2026**,
09:00, course 67521. Lecturer: Prof. Orna Kupferman; TAs: Nir Lavi, Ofer Leshkowitz.
No official solution PDF available — these are worked from scratch.)*

**Points.** Q1 = 9, Q2 = 14, Q3 = 10, Q4 = 14, Q5 = 7, Q6 = 14, Q7 = 14, Q8 = 9 + 9 = 18 → **100**.
(The Q8 header prints "36 נקודות", but the instructions say "בכל אחד משני הסעיפים א-ב" and the two
parts are marked 9 each; 18 is what makes the exam sum to 100. Treat the 36 as a typo.)

**Answer key at a glance**

| Q | Answer |
|---|---|
| 1 | **L ∈ REG**; minimal DFA has **3 states** |
| 2 | Claim 1 **נכונה** (true, via 2n+1 construction); Claim 2 **לא נכונה** (false) |
| 3 | Claim 1 **true**; Claim 2 **false** |
| 4 | Claim 1 **נכונה** (true); Claim 2 **לא נכונה** (false) |
| 5 | **R** — the language is **empty** ⚠️ *(trap — see Issues log)* |
| 6 | **RE ∖ R** |
| 7 | **NP-complete** |
| 8א | **א. נכונה** (the claim is true) |
| 8ב | **ג. נכונותה לא ידועה** — would imply **NP = PSPACE** and **NP = coNP** |

---

## Q1 (9 pts) — parity of the tail

L = { σ·w : σ ∈ {0,1}, w ∈ {0,1}*, and σ = |w| mod 2 }

(Given: ε, 00, 101 ∉ L; and 0, 11, 001 ∈ L.)

**Answer: L ∈ REG. The minimal DFA has 3 states.**

### The DFA

| state | on 0 | on 1 | accepting? | meaning |
|---|---|---|---|---|
| **q_ε** (start) | q_A | q_B | no | nothing read yet |
| **q_A** | q_B | q_B | **yes** | first letter fixed, parity currently *matches* |
| **q_B** | q_A | q_A | no | first letter fixed, parity currently *mismatches* |

Formally A = ⟨{q_ε, q_A, q_B}, {0,1}, δ, q_ε, {q_A}⟩ with
δ(q_ε,0) = q_A, δ(q_ε,1) = q_B, and δ(q_A,σ) = q_B, δ(q_B,σ) = q_A for both σ.

*Spot checks:* 0 → q_A ✓accept. 11 → q_B → q_A ✓. 001 → q_A → q_B → q_A ✓.
ε → q_ε ✗. 00 → q_A → q_B ✗. 101 → q_B → q_A → q_B ✗. All six examples agree.

### Why only 3 states — the residual computation

For a non-empty word u = σ·v and any z: u·z ∈ L ⟺ σ ≡ |v| + |z| (mod 2) ⟺ **|z| ≡ σ − |v| (mod 2)**.
So the residual of u depends *only* on the single bit (σ − |v|) mod 2, giving exactly two residuals
among non-empty words:

  u ∈ L ⇒ u⁻¹L = { z : |z| even }   and   u ∉ L ⇒ u⁻¹L = { z : |z| odd }

That is why q_A and q_B suffice after the first letter — the automaton never needs to *remember*
which letter σ was, only whether the parity currently matches it. (Merging the naive four states
(σ, parity) down to two is the whole content of the minimality claim.)

### Minimality proof (Myhill–Nerode)

Exhibit three pairwise-inequivalent words **ε, 0, 1**:

- **0 vs 1**: take z = ε — 0 ∈ L, 1 ∉ L.
- **ε vs 0**: take z = ε — ε ∉ L, 0 ∈ L.
- **ε vs 1**: take z = 1 — ε·1 = 1 ∉ L, but 1·1 = 11 ∈ L.

So the Myhill–Nerode index of L is ≥ 3, and we exhibited a DFA with 3 states, hence **index(L) = 3**
and the DFA above is minimal. ∎

---

## Q2 (14 pts) — index of info(L)

comp(L) = {0,1}* ∖ L, and **info(L) = (1·L) ∪ (0·comp(L))**.
L ⊆ {0,1}* is regular and **non-trivial** (L ≠ ∅, L ≠ {0,1}*). Write n = index(L).

### Claim 1: index(info(L)) ≤ 2·index(L) + 1 — **TRUE (נכונה)**

Let A = ⟨Q, {0,1}, δ, q₀, F⟩ be the minimal DFA for L, |Q| = n. Build

  B = ⟨Q′, {0,1}, δ′, s, F′⟩ where

- **Q′ = {s} ⊎ (Q × {1}) ⊎ (Q × {0})** — a fresh start state plus **two copies of A**
- δ′(s, 1) = (q₀, 1) and δ′(s, 0) = (q₀, 0)
- δ′((q, i), σ) = (δ(q, σ), i) for i ∈ {0,1} and σ ∈ {0,1}
- **F′ = (F × {1}) ∪ ((Q ∖ F) × {0})**

Copy 1 is A itself; copy 0 is A with its accepting set complemented (a DFA for comp(L)). The first
letter routes into the right copy and is never revisited, so L(B) = (1·L) ∪ (0·comp(L)) = info(L).

|Q′| = 1 + n + n = **2n + 1**, and index counts the *minimal* DFA, so
index(info(L)) ≤ 2n + 1 = 2·index(L) + 1. ∎

Note ε ∉ info(L) (every word there has length ≥ 1), which is why s must be non-accepting.

### Claim 2: index(info(L)) ≥ 2·index(L) + 1 — **FALSE (לא נכונה)**

The bound of Claim 1 is *not* tight in general: the two copies can collapse into each other.

**Counterexample: L = { w ∈ {0,1}* : |w| is even }.**
Regular ✓, non-trivial ✓ (ε ∈ L, 1 ∉ L). **index(L) = 2** (the two length-parity classes,
separated by ε). So 2·index(L) + 1 = **5**.

Now info(L) = {1w : |w| even} ∪ {0w : |w| odd}. Its residuals: for u = σ·v,

  u·z ∈ info(L) ⟺ |z| ≡ |v| + σ + 1 (mod 2)

so again only two residuals among non-empty words ({z : |z| even} and {z : |z| odd}), plus the
residual of ε. That is **index(info(L)) = 3**, witnessed by the DFA

| state | on 0 | on 1 | accepting? |
|---|---|---|---|
| s (start) | q_B | q_A | no |
| q_A | q_B | q_B | **yes** |
| q_B | q_A | q_A | no |

(All three are pairwise distinguishable: ε separates q_A from s and q_B; the word 0 separates s from
q_B, since s·0 = 0 ∉ info(L) while q_B·0 accepts.)

**3 < 5**, so index(info(L)) ≥ 2·index(L) + 1 fails. ∎

**Why the collapse happens.** A state (q,1) of copy 1 and a state (p,0) of copy 0 merge exactly when
L_q = comp(L_p) (the residual at q is the complement of the residual at p). For a length-parity
language the complement is just the *other* parity class, which is already a state of the same
automaton — so the two copies are isomorphic-with-a-shift and fuse completely. Structurally, this
is the same phenomenon as Q1: what looked like it needed (letter, parity) really only needs
"does the parity currently match".

---

## Q3 (10 pts) — count(L) = { 1^|w| : w ∈ L }

For each claim: prove for **every CFG G**, or give a counterexample.

### Claim 1: L(G) regular ⇒ count(L(G)) regular — **TRUE**

count(L) is the image of L under the **homomorphism h : {a,b}* → {1}*** with h(a) = h(b) = 1,
and REG is closed under homomorphism.

Self-contained construction (no closure theorem needed): let A = ⟨Q, {a,b}, δ, q₀, F⟩ be a DFA for
L(G). Define the **NFA** B = ⟨Q, {1}, η, q₀, F⟩ over the unary alphabet by

  **η(q, 1) = { δ(q, a), δ(q, b) }**

i.e. relabel every transition of A with the letter 1. Then B has a run on 1ⁿ from q₀ to an accepting
state iff A has a path of length n from q₀ to an accepting state iff **some** word of length n is in
L(G). So L(B) = count(L(G)), which is therefore regular. ∎

### Claim 2: count(L(G)) regular ⇒ L(G) regular — **FALSE**

**Counterexample.** Let G generate L(G) = { aⁿbⁿ : n ≥ 0 } (context-free, e.g. S → aSb | ε).
Then count(L(G)) = { 1²ⁿ : n ≥ 0 } = **(11)\***, which is regular — but L(G) is **not** regular
(standard pumping-lemma example, seen in class). ∎

**Remark (why Claim 2 is false as badly as possible).** By **Parikh's theorem** the length set of
*every* context-free language is ultimately periodic, so count(L(G)) is regular for **every** CFG G —
the hypothesis of Claim 2 is vacuously always satisfied. If Claim 2 held, every context-free language
would be regular. *(Parikh is beyond the course's toolkit; the aⁿbⁿ counterexample stands on its own
and is what an exam answer should give.)*

---

## Q4 (14 pts) — reductions and reversal

rev(σ₁⋯σₙ) = σₙ⋯σ₁, rev(L) = { rev(w) : w ∈ L }. Given: L₁, L₂ ⊆ Σ* **non-trivial**, and
**L₁ ≤m rev(L₂)**. Let f be the reduction, so for all w:

  **w ∈ L₁ ⟺ f(w) ∈ rev(L₂) ⟺ rev(f(w)) ∈ L₂**

(the last step because rev is an involution: u ∈ rev(K) ⟺ rev(u) ∈ K).

### Claim 1: rev(L₁) ≤m L₂ — **TRUE (נכונה)**

Define **g(u) = rev( f( rev(u) ) )**. Then for every u ∈ Σ*:

  u ∈ rev(L₁) ⟺ rev(u) ∈ L₁ ⟺ f(rev(u)) ∈ rev(L₂) ⟺ rev(f(rev(u))) ∈ L₂ ⟺ g(u) ∈ L₂ ✓

g is computable as a composition of computable functions (rev is computable — reverse the tape
contents; f is computable by assumption). Hence rev(L₁) ≤m L₂. ∎

*Slogan:* reversal is a **computable involution**, so it can be conjugated through a reduction for
free — `rev ∘ f ∘ rev` moves rev from one side of the ≤m to the other.

### Claim 2: L₂ ≤m rev(L₁) — **FALSE (לא נכונה)**

Claim 2 asks to reverse the *direction* of the reduction, and ≤m is not symmetric.

**Counterexample.** Σ = {0,1}, **L₁ = {0}**, **L₂ = A_TM**. Both non-trivial ✓
(rev(L₂) = rev(A_TM) is non-trivial too, since rev is a bijection on Σ*).

- *Hypothesis holds:* L₁ = {0} is **decidable** and rev(L₂) is non-trivial, so L₁ ≤m rev(L₂)
  (decide the input, then output a fixed yes- or no-instance of rev(L₂)).
- *Conclusion fails:* rev(L₁) = {0} ∈ R. If A_TM ≤m {0} then A_TM ∈ R, since **R is closed under
  ≤m** — contradicting the undecidability of A_TM. So L₂ ≰m rev(L₁). ∎

**The asymmetry to remember:** L₁ ≤m K says "L₁ is *no harder* than K". It puts no upper bound on
L₁'s difficulty being matched by K, so nothing flows backwards. Claim 1 survives only because it
rearranges the *same* reduction; Claim 2 asks for a genuinely new one.

---

## Q5 (7 pts) — L(M) ∈ coRE ∖ R  ⚠️ trap

L = { ⟨M⟩ : M is a TM and **L(M) ∈ coRE ∖ R** }

**Answer: L ∈ R — because L = ∅.**

**Proof.** For every TM M, the language L(M) is recognized by M, so **L(M) ∈ RE — always**.
Suppose some ⟨M⟩ were in L. Then L(M) ∈ coRE as well, so

  **L(M) ∈ RE ∩ coRE = R**

(the standard theorem: a language and its complement both recognizable ⇒ decidable, by running the
two recognizers in parallel). But then L(M) ∉ coRE ∖ R — contradiction.

So no ⟨M⟩ satisfies the condition, and strings that are not valid encodings are not in L either.
Hence **L = ∅**, decided by the machine that rejects every input, so **L ∈ R**. ∎

**Why it's a trap.** The set `coRE ∖ R` is a perfectly sensible class *for languages in general* —
Ā_TM lives there. But it is **empty once you restrict to languages of the form L(M)**, because
those are exactly the RE languages, and RE ∩ coRE = R. The phrase "L(M) ∈ coRE ∖ R" is
self-contradictory, so the whole classification collapses before any reduction is needed.

Before reaching for Rice or a reduction here, ask: **can the stated property hold at all?**
Compare the identically-shaped trap in *Comp 2024 summer moed A Q6* (`accepts σσ in one step but
does not halt on σσσσ` — also empty, also R, also for a purely structural reason).

**Contrast — the questions this is NOT:**

| language | answer | why |
|---|---|---|
| { ⟨M⟩ : L(M) ∈ coRE ∖ R } | **R** (= ∅) | RE ∩ coRE = R makes it unsatisfiable |
| { ⟨M⟩ : L(M) ∈ R } | far outside RE ∪ coRE (Σ⁰₃-complete) | genuinely a semantic property; coRE-hard — see the separate `L(M) in R is coRE-hard` notes |
| { ⟨M⟩ : L(M) ∈ coRE } | trivially **all** of Σ* (restricted to encodings) | ⟺ L(M) ∈ R, still a real property — but ∈ coRE∖R is the empty slice |

---

## Q6 (14 pts) — accepts w and has ≥ 2026 words

L = { ⟨M, w⟩ : M is a TM, w ∈ Σ*, **M accepts w**, and **|L(M)| ≥ 2026** }

**Answer: L ∈ RE ∖ R.**

### L ∈ RE

Both conjuncts are RE, and **RE is closed under intersection**:

- "M accepts w" — recognizable by simulating M on w.
- "|L(M)| ≥ 2026" — recognizable by **dovetailing**: enumerate pairs (x, t) over all x ∈ Σ* and
  t ∈ ℕ, simulate M on x for t steps, and collect the words found accepted; accept once **2026
  distinct** words have been collected.

Concretely the recognizer runs both searches in parallel on ⟨M,w⟩ and accepts when *both* have
succeeded. If ⟨M,w⟩ ∈ L, M accepts w within finitely many steps and each of the ≥ 2026 accepted
words is found within finitely many steps, so the recognizer accepts. If ⟨M,w⟩ ∉ L, then either M
never accepts w or fewer than 2026 words are ever collected, so it never accepts. **L ∈ RE.** ✓

### L ∉ R — reduce A_TM ≤m L

Given ⟨M, w⟩, output **⟨M′, ε⟩** where M′ on input x ignores x, simulates M on w, and accepts iff M
accepts w. So L(M′) = Σ* if M accepts w, and L(M′) = ∅ otherwise.

- M accepts w ⇒ M′ accepts ε ✓ and |L(M′)| = |Σ*| = ∞ ≥ 2026 ✓ ⇒ ⟨M′, ε⟩ ∈ L
- M does not accept w ⇒ M′ does not accept ε ⇒ ⟨M′, ε⟩ ∉ L

So A_TM ≤m L. Since **A_TM ∉ coRE**, we get L ∉ coRE, hence **L ∉ R**. ∎

Therefore **L ∈ RE ∖ R**.

**Note on the 2026.** The constant is decoration — any fixed k ≥ 1 gives the same answer, because
"at least k accepted words" is RE for every fixed k (a finite conjunction of RE witnesses found by
dovetailing). It would only change things if the bound were *upper* ("|L(M)| ≤ 2026", a coRE-flavoured
condition) or if it depended on the input.

---

## Q7 (14 pts) — at least two Hamiltonian paths

L = { ⟨G, s, t⟩ : G = ⟨V,E⟩ directed, s,t ∈ V, and there are **at least two** Hamiltonian paths
from s to t }

**Answer: NP-complete.**

### L ∈ NP

Certificate: **two** sequences P₁, P₂ of vertices. The verifier checks that each P_i is a permutation
of V starting at s and ending at t with every consecutive pair an edge of E, and that **P₁ ≠ P₂**.
Both certificates are of size O(|V| log|V|) and all checks are polynomial. ✓

### L is NP-hard — D-ST-HAMPATH ≤p L

D-ST-HAMPATH = { ⟨G,s,t⟩ : G directed has a Hamiltonian path from s to t } is NP-complete
(formula-sheet language). The gadget **forces every solution to come in a pair**.

**Construction.** Given ⟨G, s, t⟩ with G = ⟨V,E⟩, output ⟨G′, s′, t⟩ where G′ = ⟨V′, E′⟩ with

  V′ = V ∪ {s′, s′₁, s′₂}  (three fresh vertices)
  E′ = E ∪ { (s′,s′₁), (s′,s′₂), (s′₁,s′₂), (s′₂,s′₁), (s′₁,s), (s′₂,s) }

i.e. a new source s′ pointing at two new vertices s′₁, s′₂ that form a 2-cycle between themselves and
both point into the old source s. Computable in polynomial time (adds 3 vertices and 6 edges). ✓

**Correctness.**

- **(⇒)** If P is a Hamiltonian path s → t in G, then
  s′ → s′₁ → s′₂ → s → (P) → t and s′ → s′₂ → s′₁ → s → (P) → t
  are **two distinct** Hamiltonian paths s′ → t in G′ (each covers V′ exactly once). So ⟨G′,s′,t⟩ ∈ L.
- **(⇐)** Conversely, any Hamiltonian path from s′ in G′ must leave s′ into s′₁ or s′₂ (its only
  out-edges), then must cover the other one of {s′₁, s′₂} — whose only remaining out-edge leads to
  s — and can never return to {s′, s′₁, s′₂} afterwards (s′ has no in-edges; s′₁, s′₂ have in-edges
  only from s′ and from each other). So the path has the form
  s′ → s′_i → s′_j → s → (Q) → t where Q covers V exactly once, i.e. **Q is a Hamiltonian path
  s → t in G**. Hence ⟨G′,s′,t⟩ ∈ L ⇒ ⟨G,s,t⟩ ∈ D-ST-HAMPATH.

In fact the gadget doubles the count exactly: G has k Hamiltonian s–t paths ⟺ G′ has 2k
Hamiltonian s′–t paths. So "≥ 1" in G ⟺ "≥ 2" in G′. ∎

**The idea to keep.** "At least two solutions" is NP-complete whenever "at least one" is, provided
you can build a gadget that **multiplies every solution by a fixed factor ≥ 2** while creating no new
ones. A symmetric pair of forced-detour vertices (here s′₁ ↔ s′₂, attachable at either the source or
the target end) is the standard way to do it.

---

## Q8 (9 + 9 pts) — true / false / unknown

### Q8.א (9 pts) — claim: A_NFA ≤_logspace PATH

A_NFA = { ⟨N,w⟩ : N is an NFA over Σ, w ∈ Σ*, w ∈ L(N) };
PATH = { ⟨G,s,t⟩ : G directed, s,t ∈ V, there is a path from s to t }.

**Answer: א. נכונה — the claim is TRUE.** (Nothing to circle in part ג.)

**Slick proof.** **A_NFA ∈ NL**: guess the run of N on w one step at a time, storing only the current
state and the current position in w — O(log(|N| + |w|)) bits. **PATH is NL-complete** under logspace
reductions (seen in class). By definition of NL-completeness, every language in NL logspace-reduces
to PATH, so A_NFA ≤_logspace PATH. ∎

**Explicit construction** (the layered run-graph, which is really the same proof unrolled).
Given ⟨N, w⟩ with N = ⟨Q, Σ, δ, Q₀, F⟩ and w = σ₁⋯σₙ, output ⟨G, s, t⟩ with

- **vertices** (q, i) for q ∈ Q, 0 ≤ i ≤ n, plus two fresh vertices s and t
- **edges**
  - (q, i) → (q′, i+1) whenever q′ ∈ δ(q, σ_{i+1}), for 0 ≤ i < n  *(consume a letter)*
  - (q, i) → (q′, i) whenever q′ ∈ δ(q, ε)  *(ε-move, if the course's NFAs have them)*
  - s → (q, 0) for every q ∈ Q₀, and (q, n) → t for every q ∈ F

Then a path s ⇝ t in G is exactly an accepting run of N on w, so **⟨N,w⟩ ∈ A_NFA ⟺ ⟨G,s,t⟩ ∈ PATH**.

**Logspace:** the output has |Q|·(n+1) + 2 vertices. Iterate over (q, i, q′) with three counters of
O(log(|Q|·n)) bits, and for each triple scan the input's description of δ to decide whether to emit
the edge. Work space is O(log |⟨N,w⟩|); the output tape is write-only and does not count. ✓

> **Cross-link — do not confuse membership with universality.** Compare
> *Comp 2025-1 moed A Q8.א*, where the claim was **ALL_NFA ≤p PATH** and the answer was
> **"truth unknown"** (equivalent to P = PSPACE). The difference is entirely in the NFA problem:
>
> | problem | question | complexity | reduction to PATH |
> |---|---|---|---|
> | **A_NFA** | is *this word* accepted? | **NL-complete** | ≤_logspace — **provably true** |
> | **ALL_NFA** | is *every word* accepted? | **PSPACE-complete** | ≤p — **unknown** (⟺ P = PSPACE); ≤_L provably false |
>
> Membership in an NFA is cheap (guess one run); universality needs the subset construction.

### Q8.ב (9 pts) — claim: L ∈ NP, where L couples 3SAT to ALL_NFA

L = { ⟨θ, A⟩ : θ is a 3CNF formula, A is an NFA, and **θ is satisfiable iff L(A) = Σ*** }

**Answer: ג. נכונותה לא ידועה — and it would imply NP = PSPACE and NP = coNP.**

**Circle: NP = PSPACE and NP = coNP.** (Not P = NP, not P ≠ NP, not P = PSPACE, not P = NL, not L = NL.)

The claim is **equivalent to NP = PSPACE**, an open problem. Here is the whole picture:

**Step 1 — L is PSPACE-hard.** Fix a satisfiable 3CNF formula θ_sat (e.g. (x ∨ x ∨ x)) and map
⟨A⟩ ↦ ⟨θ_sat, A⟩. Since "θ_sat is satisfiable" is *true*, the biconditional reduces to its right
side: ⟨θ_sat, A⟩ ∈ L ⟺ L(A) = Σ* ⟺ ⟨A⟩ ∈ ALL_NFA. This map is computable in polynomial time
(it prepends a constant), so **ALL_NFA ≤p L**. ALL_NFA is PSPACE-complete, so L is **PSPACE-hard**.

**Step 2 — L ∈ PSPACE.** Decide "θ satisfiable" (3SAT ∈ NP ⊆ PSPACE), decide "L(A) = Σ*"
(ALL_NFA ∈ PSPACE), and return the XNOR of the two bits. PSPACE is closed under these operations,
so L ∈ PSPACE. Together with Step 1, **L is PSPACE-complete**.

**Step 3 — the equivalence.**
- (⇒) If L ∈ NP, then since L is PSPACE-hard, every K ∈ PSPACE satisfies K ≤p L ∈ NP, and NP is
  closed under ≤p, so K ∈ NP. Hence PSPACE ⊆ NP; with NP ⊆ PSPACE this gives **NP = PSPACE**.
- (⇐) If NP = PSPACE, then L ∈ PSPACE = NP, so the claim holds.

So the claim is true **iff** NP = PSPACE — open, hence answer ג.

**Which listed facts follow.**

| fact | follows? | why |
|---|---|---|
| **NP = PSPACE** | ✅ | Step 3 (⇒) directly |
| **NP = coNP** | ✅ | PSPACE is closed under complement, so coNP = coPSPACE = PSPACE = NP |
| P = NP | ❌ | NP = PSPACE is consistent with P ⊊ NP |
| P ≠ NP | ❌ | also consistent with P = NP = PSPACE |
| P = PSPACE | ❌ | would additionally need P = NP |
| P = NL, L = NL | ❌ | nothing about the space classes below P is implied |

**The trap in the "iff".** A biconditional between an easy-ish condition (3SAT, NP-complete) and a
hard one (ALL_NFA, PSPACE-complete) inherits the **harder** side: fixing the easy side to a constant
makes the biconditional *become* the hard side. Do not read "θ is satisfiable iff …" as making the
language a mere NP question — the NFA universality half dominates.

---

## Cross-question themes

1. **Check satisfiability of the property before classifying.** Q5's `L(M) ∈ coRE ∖ R` is empty
   because RE ∩ coRE = R. Same shape as Comp 2024 summer moed A Q6.
2. **A computable involution can be conjugated through a reduction.** Q4's `rev ∘ f ∘ rev` — but
   reductions still never run backwards (Claim 2).
3. **"At least two" ≡ "at least one" via a solution-doubling gadget.** Q7's forced s′₁ ↔ s′₂ detour.
4. **Two copies of a DFA can collapse.** Q2 — the 2n+1 upper bound is real, the matching lower bound
   is not, exactly when a residual equals the complement of another residual.
5. **Membership vs universality for NFAs.** Q8.א is NL-complete and settles cleanly; ALL_NFA is
   PSPACE-complete and leaves things open (Q8.ב, and Comp 2025-1 moed A Q8.א).

---

## Issues log

- **Q5** — Circled **coRE∖R** and started a reduction `¬HALT ≤m L`; **the correct answer is R**.
  The error: treating "L(M) ∈ coRE ∖ R" as a normal non-trivial semantic property and going straight
  for a hardness reduction, without first checking whether *any* machine can satisfy it. Resolved:
  L(M) is always **RE**, and **RE ∩ coRE = R**, so L(M) ∈ coRE would force L(M) ∈ R — the condition
  `coRE ∖ R` is unsatisfiable for languages of the form L(M). Hence **L = ∅ ∈ R**, no reduction
  needed. Takeaway: when a classification question names a class *slice* (`X ∖ Y`) applied to L(M),
  test the slice against RE ∩ coRE = R before proving anything. Same trap shape as Comp 2024 summer
  moed A Q6 (`accepts σσ in one step but does not halt on σσσσ`, also empty, also R).

- **Q6** — Circled **RE ∖ R**: **correct**. (Recorded for completeness; the written justification
  sketched the dovetail over the ≥ 2026 accepted words, which is the right idea.)

- **Q7** — Circled **NP-complete**: **correct**, with a valid solution-doubling gadget attached at
  the **source** side (new s′ → s′₁, s′₂ forming a 2-cycle, both → s). That is exactly equivalent to
  the target-side version; the write-up above uses the student's source-side construction.

- **Q1–Q4, Q8** — Left blank on the exam form; solved from scratch above. Q8.ב is the one most worth
  re-reading: the answer is **ג (unknown)** with **NP = PSPACE** *and* **NP = coNP** to be circled,
  because L is in fact PSPACE-complete.
