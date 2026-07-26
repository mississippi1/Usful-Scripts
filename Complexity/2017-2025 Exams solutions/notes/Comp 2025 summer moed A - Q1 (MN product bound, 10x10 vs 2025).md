# Comp 2025 summer (קיץ) moed A — Q1 (12 pts, MN worksheet): can MN(L1)=MN(L2)=10 give MN(L1∩L2)=2025?

**Question.** Claim: there exist languages L1, L2 such that each has 10 Myhill–Nerode
equivalence classes, and the intersection L1 ∩ L2 has 2025 Myhill–Nerode equivalence
classes. Is the claim correct? Prove your answer.

Note: this exam PDF is not present in this repo (only "2017-2025 Exams" has a "Comp 2025-1
moed A/B/C" set, dated 2025.2.16 — winter, not summer). Filed alongside
"Comp 2025 summer moed A - Q3 (MN, finite-or-infinite dichotomy).md" from the same
"MN (קיץ 2025, מועד א')" worksheet.

## Answer: the claim is FALSE

## The tool: MN(L1 ∩ L2) ≤ MN(L1) · MN(L2)

Same fact used in "Comp 2024 winter moed A - Q1 (Myhill-Nerode, intersection).md" parts (b)
and (c) — restated self-contained here.

**Lemma.** For any L1, L2 ⊆ Σ*, MN(L1 ∩ L2) ≤ MN(L1) · MN(L2).

*Proof.* Let m = MN(L1), m' = MN(L2). Define

    Φ : Σ* → (Σ*/≡_{L1}) × (Σ*/≡_{L2}),   Φ(u) = ( [u]_{L1} , [u]_{L2} )

— at most m·m' possible outputs. If Φ(u) = Φ(v), then u, v lie together in some class C of
≡_{L1} and together in some class C' of ≡_{L2}, i.e. u, v ∈ C ∩ C'. For arbitrary z ∈ Σ*:

    uz ∈ L1 ∩ L2  ⟺ uz ∈ L1 ∧ uz ∈ L2  ⟺ vz ∈ L1 ∧ uz ∈ L2  ⟺ vz ∈ L1 ∧ vz ∈ L2  ⟺ vz ∈ L1 ∩ L2

(swap u for v in each conjunct via u ≡_{L1} v and u ≡_{L2} v, both true since u, v share a
class of each relation). So u ≡_{L1∩L2} v. Hence Φ determines the ≡_{L1∩L2} class: the map
(C, C') ↦ [u]_{L1∩L2} (any u ∈ C ∩ C') is a well-defined surjection from Image(Φ) onto
Σ*/≡_{L1∩L2}. A surjection cannot increase cardinality, so MN(L1 ∩ L2) ≤ m·m'. ∎

## Applying it

MN(L1) = MN(L2) = 10 forces MN(L1 ∩ L2) ≤ 10 · 10 = 100. Since 2025 > 100, it is impossible
for MN(L1) = MN(L2) = 10 and MN(L1 ∩ L2) = 2025 to hold simultaneously, for ANY choice of
L1, L2 — the lemma is unconditional (no regularity or other structural assumption needed).
**The claim is false.** ∎

## Alternate proof of the lemma — logical clauses only, no map/image/surjection

Same lemma, same conclusion, but built purely from the ≡_L definition and a
pigeonhole-by-contradiction instead of a pair-map + surjection.

Since ≡_{L1} partitions Σ* into m = MN(L1) classes, label them C_1,…,C_m (every w ∈ Σ*
lies in exactly one C_i, and u ≡_{L1} v iff u, v share a C_i). Likewise label the m' = MN(L2)
classes of ≡_{L2} as D_1,…,D_{m'}.

Important: C_1,…,C_m already partition ALL of Σ*, not just the words that happen to be in
L1 — this is not something that needs separate proof, it's the standard "an equivalence
relation partitions its whole domain" fact from part (a): reflexivity puts every w ∈ Σ*
in its own class w ≡_{L1} w, and symmetry+transitivity force any two classes to be equal or
disjoint. So MN(L1) = m counts classes of words IN L1 and classes of words NOT in L1 alike
(e.g. for L1 = {ε} over Σ = {a}, MN(L1) = 2: C_1 = {ε} and C_2 = {a,aa,aaa,…}, the latter
entirely outside L1). Consequently every word w_t below — whether or not it happens to lie
in L1, L2, or L1 ∩ L2 — automatically falls into exactly one C_i and exactly one D_j; that
coverage is inherited from "{C_i} is a partition of Σ*", not argued separately here.

**Step 1 (key implication, a chain of biconditionals).** If u, v ∈ Σ* lie in a common C_i
and a common D_j (i.e. u ≡_{L1} v and u ≡_{L2} v), then u ≡_{L1∩L2} v.

Proof: by hypothesis ∀z ∈ Σ*: (uz∈L1 ⟺ vz∈L1) and ∀z ∈ Σ*: (uz∈L2 ⟺ vz∈L2). Fix an
arbitrary z ∈ Σ*:

    uz ∈ L1 ∩ L2
     ⟺ uz ∈ L1 ∧ uz ∈ L2       (definition of ∩)
     ⟺ vz ∈ L1 ∧ uz ∈ L2       (instantiate the first hypothesis at this z)
     ⟺ vz ∈ L1 ∧ vz ∈ L2       (instantiate the second hypothesis at this same z)
     ⟺ vz ∈ L1 ∩ L2            (definition of ∩)

z was arbitrary, so ∀z: uz ∈ L1∩L2 ⟺ vz ∈ L1∩L2, i.e. u ≡_{L1∩L2} v. ∎ (Nothing but two
applications of the definition of ≡_L chained through a conjunction — no function is built.)

**Step 2 (pigeonhole by contradiction).** Suppose MN(L1 ∩ L2) ≥ m·m' + 1. Then there are
m·m'+1 words w_1,…,w_{mm'+1}, one from each of m·m'+1 distinct ≡_{L1∩L2} classes — so they
are pairwise inequivalent under ≡_{L1∩L2}.

Each w_t lies in exactly one C_i (among m choices) and exactly one D_j (among m' choices),
so each of the m·m'+1 words falls into one of only m·m' combinations (C_i, D_j). Since
m·m'+1 > m·m', pigeonhole gives s ≠ t whose words share the same combination: w_s, w_t lie
in a common C_i and a common D_j. By Step 1, w_s ≡_{L1∩L2} w_t — contradicting that the
w_t were chosen pairwise inequivalent. So MN(L1 ∩ L2) ≤ m·m'. ∎

Same 100 cap, same 2025 > 100 conclusion — only the packaging differs.

## Why the bound is tight (so the disproof is really about arithmetic, not structure)

100 is achievable, not merely an upper limit. Over Σ = {a,b}:

    L1 = { w : |w| ≡ 0 (mod 10) }        (length-counter language, 10 classes)
    L2 = { w : #a(w) ≡ 0 (mod 10) }      (a-counter language, 10 classes)

Each has exactly 10 MN classes (minimal DFA = a 10-state counting cycle). L1 ∩ L2 tracks two
*independent* counters — |w| mod 10 and #a(w) mod 10 — because appending b changes only the
first, appending a changes both by 1 (letting either coordinate be corrected freely). All
10×10 = 100 combined states are reachable and pairwise distinguishable, so
MN(L1 ∩ L2) = 100 exactly.

Machine-verified with the analogous mod-3 construction (brute force, words up to length 8):
MN(L1) = 3, MN(L2) = 3, MN(L1 ∩ L2) = 9 = 3·3 — confirms the bound is achieved exactly, not
just an inequality.

So 100 is the *maximum* possible value of MN(L1 ∩ L2) once MN(L1) = MN(L2) = 10, and 2025
sits far above anything the construction can reach.

## Common wrong moves

- Trying to engineer L1, L2 to hit 2025 directly — impossible regardless of construction,
  since the lemma holds unconditionally for all L1, L2.
- Citing the bound but skipping the actual arithmetic check (10·10 = 100 < 2025) — the whole
  disproof is exactly that one inequality.
- The identical lemma and disproof (swap ∧ for the relevant connective in the unfolding step)
  disposes of the same claim if ∩ were replaced by ∪ or symmetric difference.

## Issues log

- **Q1** — Was unable to solve; needed to identify which tool applies. Resolved by reusing
  the product bound MN(L1 ∩ L2) ≤ MN(L1)·MN(L2) proved on the winter 2024 moed A MN
  worksheet (see "Comp 2024 winter moed A - Q1" notes): with MN(L1)=MN(L2)=10 this caps
  MN(L1 ∩ L2) at 100, and 2025 > 100 makes the claim false — no construction can evade an
  unconditional inequality. Confirmed the bound is tight (not just an upper limit) via a
  two-independent-counters construction, verified by brute force at modulus 3
  (MN(L1)=MN(L2)=3, MN(L1∩L2)=9).
- **Q1 follow-up** — Asked to redo the lemma's proof "without mapping", using logical
  clauses/MN definitions instead. Resolved: replaced the pair-map Φ + surjection argument
  with (1) a direct ⟺-chain from the ≡_L definition showing u,v sharing an L1-class and an
  L2-class implies u ≡_{L1∩L2} v, and (2) a pigeonhole-by-contradiction over m·m'+1
  hypothetically-inequivalent words, landing in only m·m' (class,class) combinations. Same
  bound, same conclusion, purely first-order phrasing.
- **Q1 follow-up #2** — Concern that Step 2's "each w_t lies in exactly one C_i and one D_j"
  was unproven for words outside the intersection. Resolved: C_1,…,C_m already partition
  ALL of Σ*, not just words in L1 — a direct consequence of ≡_{L1} being an equivalence
  relation (reflexivity + symmetry/transitivity, part (a)), not something Step 1 needs to
  establish. Example added: L1 = {ε} over Σ={a} has MN(L1) = 2, with C_2 = {a,aa,aaa,…}
  entirely outside L1 — MN classes cover rejected words too, so every w_t automatically
  falls into some C_i and some D_j regardless of language membership.
